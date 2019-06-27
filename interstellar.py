from argparse import ArgumentParser
from os.path import exists

from interstellar.Interstellar import Interstellar

# if this is false it will never return success, setting to false is for debugging only
do_success_flag = True


def do_deploy( config_file ) -> bool:
    deployer = Interstellar( config_file )
    return deployer.deploy()


if __name__ == '__main__':

    parser = ArgumentParser( prog = "Interstellar", description = "Auto-provisioning of Kafka data pipeline environment environment" )
    parser.add_argument( "--deployment_config", required = False, type = str )
    parser.add_argument( "--healthcheck", required = False, action = "store_true" )
    args = parser.parse_args()

    if args.healthcheck is not False:
        # TODO implement healthcheck logic
        if exists( ".success" ) is True:
            exit( 0 )
        else:
            print( "provisioning is not finished yet" )
            exit( 1 )
    else:
        result = do_deploy( args.deployment_config )
        if result is False:
            print( "unable to provison the kafka environment" )
            exit( 1 )
        else:
            print( "provisioning successful" )
            if do_success_flag is True:
                success_flag = open( ".success", "w+" )
                success_flag.write( "" )
                success_flag.close()
            exit()