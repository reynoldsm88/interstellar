# -*- coding: utf-8 -*-
import unittest

import yaml

import os

from interstellar.DeploymentDescriptor import DeploymentDescriptor


class ParsingTestSuite( unittest.TestCase ):
    """Configuration file parsing"""

    def test_parse_full_deployment( self ):
        file_name = "tests/resources/full-example.yaml"
        yaml_file = open( file_name )
        yaml_content = yaml_file.read()
        yaml_file.close()

        deployment_yaml = yaml.load( yaml_content )
        deployment = DeploymentDescriptor( deployment_yaml )

        assert len( deployment.bootstrap_servers ) == 2
        assert len( deployment.topics ) == 2

        assert deployment.bootstrap_servers.__contains__( "kafka-broker-1:9092" )
        assert deployment.bootstrap_servers.__contains__( "kafka-broker-2:9092" )
        assert deployment.topics[ 0 ].name == "test-1"
        assert deployment.topics[ 0 ].compression_type == "gzip"
        assert deployment.topics[ 0 ].preallocate == False
        assert deployment.topics[ 0 ].num_partitions == 3
        assert deployment.topics[ 1 ].name == "test-2"
        assert deployment.topics[ 1 ].compression_type == "zstd"
        assert deployment.topics[ 1 ].preallocate == True
        assert deployment.topics[ 1 ].max_message_bytes == 50000000
        assert deployment.topics[ 1 ].replication_factor == 2

    def test_parse_environment_variables( self ):
        os.environ[ "KAFKA_BOOTSTRAP_SERVERS" ] = "mytest:9092"
        os.environ[ "NUMBER_RETRIES" ] = "3"
        os.environ[ "RETRY_DELAY "] = "1"

        with open( "tests/resources/env-variables.yaml" ) as file:
            deployment_yaml = yaml.load( file )
            deployment = DeploymentDescriptor( deployment_yaml )

            assert 'mytest:9092' in deployment.bootstrap_servers


if __name__ == '__main__':
    unittest.main()