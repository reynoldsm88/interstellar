from interstellar.TopicDescriptor import TopicDescriptor


class DeploymentDescriptor:
    def __init__( self, deployment_yaml: dict ):
        print( "deploying the following configuration : \n" + str( deployment_yaml ) )
        deployment = deployment_yaml.get( "deployment" )
        self.name = deployment.get( "name" )
        self.bootstrap_servers = deployment.get( "bootstrap_servers" )

        topics = [ ]
        for topic in deployment.get( "topics" ):
            topics.append( TopicDescriptor.parse( topic ) )
        self.topics = topics