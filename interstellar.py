from argparse import ArgumentParser
from interstellar.Interstellar import Interstellar


def do_deploy( config_file ) -> bool:
    deployer = Interstellar( config_file )
    return deployer.deploy()


if __name__ == '__main__':
    parser = ArgumentParser( prog = "Interstellar", description = "Auto-provisioning of Kafka data pipeline environment environment" )
    parser.add_argument( "--deployment_config", required = False, type = str )
    parser.add_argument( "--healthcheck", type = bool, required = False )
    args = parser.parse_args()

    if args.healthcheck != None:
        # TODO implement healthcheck logic
        print( "healtcheck" )
    else:
        result = do_deploy( args.deployment_config )
        if result is False:
            print( "unable to provison the kafka environment" )
            exit( 1 )
        else:
            print( "provisioning successful" )
            exit()