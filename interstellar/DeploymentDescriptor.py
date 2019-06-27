import yaml

from interstellar.TopicDescriptor import TopicDescriptor


class DeploymentDescriptor:
    def __init__( self, name, bootstrap_servers, topics ):
        self.name = name
        self.bootstrap_servers = bootstrap_servers
        self.topics = topics

    def parse( yaml ):
        deployment = yaml.get( "deployment" )
        name = deployment.get( "name" )
        bootstrap_servers = deployment.get( "bootstrap_servers" )
        topics = TopicDescriptor.parse( deployment.get( "topics" ) )
        return DeploymentDescriptor( name, bootstrap_servers, topics )