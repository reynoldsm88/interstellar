import yaml

try:
    from yaml import FullLoader as DefaultLoader
except ImportError:
    from yaml import Loader as DefaultLoader

from confluent_kafka.admin import AdminClient, NewTopic

from interstellar.DeploymentDescriptor import DeploymentDescriptor


class Interstellar:
    def __init__( self, config_file ):
        if self.check_config( config_file ) is False:
            exit( 1 )

        yaml_file = open( config_file )
        yaml_content = yaml_file.read()
        yaml_file.close()

        deployment_yaml = yaml.load( yaml_content, Loader = DefaultLoader )
        self.deployment = DeploymentDescriptor( deployment_yaml )

        self.admin_client = self.connect()

    # TODO @michael - impelent some kind of validation...
    def check_config( self, config_file ):
        return True

    def connect( self ):
        bootstrap_servers = ""
        for broker in self.deployment.bootstrap_servers:
            bootstrap_servers += "," + broker
        bootstrap_url = bootstrap_servers[ 1:len( bootstrap_servers ) ]  # this is a hack
        return AdminClient( { "bootstrap.servers": bootstrap_url } )

    def deploy( self ) -> bool:
        topics = [ ]
        for topic in self.deployment.topics:
            ktopic = NewTopic( topic.name,
                               num_partitions = topic.num_partitions,
                               replication_factor = topic.replication_factor,
                               config = topic.get_topic_config() )
            topics.append( ktopic )

        results = self.admin_client.create_topics( topics )
        for topic, f in results.items():
            try:
                f.result()  # The result itself is None
                print( f"Topic {topic} created" )
            except Exception as e:
                print( f"Failed to create topic {topic}: {e}" )
                return False
        return True