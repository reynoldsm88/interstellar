import os

from interstellar.TopicDescriptor import TopicDescriptor


class DeploymentDescriptor:
    def __init__( self, deployment_yaml: dict ):

        deployment = deployment_yaml.get( "deployment" )
        self.name = deployment.get( "name" )
        self.bootstrap_servers = deployment.get( "bootstrap_servers" )

        if '_env_' in self.bootstrap_servers:
            env_servers = [ os.environ.get( "KAFKA_BOOTSTRAP_SERVERS" ) if host == '_env_' else host for host in self.bootstrap_servers ]
            self.bootstrap_servers = env_servers

        topics = [ ]
        for topic in deployment.get( "topics" ):
            topics.append( TopicDescriptor.parse( topic ) )

        print( "deploying the following configuration : \n" + str( deployment_yaml ) )
        print( f'deployment_name: {self.name}' )
        print( f'bootstrap_servers: {self.bootstrap_servers}' )
        print( 'topics:[' )
        for t in topics:
            print( f'\t{t.name}' )
        print( ']' )

        self.topics = topics