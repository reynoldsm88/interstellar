# -*- coding: utf-8 -*-
import unittest

import yaml

from interstellar.DeploymentDescriptor import DeploymentDescriptor
from interstellar.TopicDescriptor import TopicDescriptor


class ParsingTestSuite( unittest.TestCase ):
    """Advanced test cases."""

    def test_parse_topic( self ):
        file_name = "tests/resources/topic-example.yaml"
        yaml_file = open( file_name )
        yaml_content = yaml_file.read()
        yaml_file.close()

        topic_yaml = yaml.load( yaml_content )
        topic = TopicDescriptor( **topic_yaml.get( "topic" ) )

        # assert values we supplied are set
        assert topic.name == "test"
        assert topic.cleanup_policy == "delete"
        assert topic.compression_type == "zstd"

        # also assert some default values
        assert topic.delete_retention_ms == 86400000
        assert topic.preallocate == False

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
        assert deployment.topics[ 1 ].name == "test-2"
        assert deployment.topics[ 1 ].compression_type == "zstd"
        assert deployment.topics[ 1 ].preallocate == True


if __name__ == '__main__':
    unittest.main()