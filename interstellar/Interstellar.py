from interstellar.DeploymentDescriptor import DeploymentDescriptor
from confluent_kafka.admin import AdminClient, NewTopic, NewPartitions, ConfigResource, ConfigSource
from confluent_kafka import KafkaException
import sys
import threading
import yaml


class Interstellar:
    def __init__( self, config_file ):
        if self.check_config( config_file ) is False:
            exit( 1 )

        yaml_file = open( config_file )
        yaml_content = yaml_file.read()
        yaml_file.close()

        deployment_yaml = yaml.load( yaml_content )
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

    def deploy( self ):
        topics = [ ]
        print( len( self.deployment.topics ) )
        for topic in self.deployment.topics:
            ktopic = NewTopic( topic.name,
                               num_partitions = topic.num_partitions,
                               replication_factor = topic.replication_factor,
                               config = topic.get_topic_confi() )
            topics.append( ktopic )

        results = self.admin_client.create_topics( topics )
        for topic, f in results.items():
            try:
                f.result()  # The result itself is None
                print( "Topic {} created".format( topic ) )
            except Exception as e:
                print( "Failed to create topic {}: {}".format( topic, e ) )