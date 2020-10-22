import yaml

try:
    from yaml import FullLoader as DefaultLoader
except ImportError:
    from yaml import Loader as DefaultLoader

from confluent_kafka.admin import AdminClient, NewTopic, KafkaException
from confluent_kafka import KafkaError

from interstellar.DeploymentDescriptor import DeploymentDescriptor

from tenacity import retry, stop_after_attempt, wait_fixed, TryAgain, RetryError


class Interstellar:
    def __init__( self, config_file ):
        if self.check_config( config_file ) is False:
            exit( 1 )

        yaml_file = open( config_file )
        yaml_content = yaml_file.read()
        yaml_file.close()

        deployment_yaml = yaml.load( yaml_content, Loader = DefaultLoader )
        self.deployment = DeploymentDescriptor( deployment_yaml )
        retry_decorator = retry( stop = stop_after_attempt( self.deployment.number_retries ),
                                 wait = wait_fixed( self.deployment.retry_delay ) )
        self.create_topics = retry_decorator( self.__create_topic_with_retry )

    # TODO @michael - implement some kind of validation...
    def check_config( self, config_file ):
        return True

    def connect( self ):
        bootstrap_url = ','.join( self.deployment.bootstrap_servers )
        return AdminClient( { "bootstrap.servers": bootstrap_url } )

    def deploy( self ) -> bool:
        topics = [ ]
        for topic in self.deployment.topics:
            ktopic = NewTopic( topic.name,
                               num_partitions = topic.num_partitions,
                               replication_factor = topic.replication_factor,
                               config = topic.get_topic_config() )
            topics.append( ktopic )

        try:
            self.create_topics( topics )
        except RetryError:
            print( f'Unable to provision topics after {self.create_topics.retry.statistics[ "attempt_number" ]} retries' )
            return False
        except Exception as ex:
            print( f'Unable to provision topics: {ex}' )
            return False

        return True

    def __create_topic_with_retry( self, topics: [ ] ):
        print( 'connecting to Kafka' )
        admin_client = self.connect()
        results = admin_client.create_topics( topics )
        for topic, f in results.items():
            try:
                f.result()  # The result itself is None
                print( f"Topic {topic} created" )
            except KafkaException as e:
                print( f"Failed to create topic {topic}: {e}" )
                if e.args[ 0 ].code() != KafkaError.TOPIC_ALREADY_EXISTS:
                    raise TryAgain
                else:
                    print( f'{topic} already exists' )
            except Exception as ex:
                print( f"Failed to create topic {topic}: {ex}" )
                raise TryAgain
        return True