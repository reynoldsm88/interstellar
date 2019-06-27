# -*- coding: utf-8 -*-
from interstellar.TopicDescriptor import TopicDescriptor
from interstellar.DeploymentDescriptor import DeploymentDescriptor

import yaml
import unittest
from os.path import exists


class ParsingTestSuite( unittest.TestCase ):
    """Advanced test cases."""

    def test_parse_topic( self ):
        f = open( "tests/resources/topic-example.yaml", "r" )
        content = f.read()
        f.close()
        topic_yaml = yaml.load( content )
        topic = TopicDescriptor( **topic_yaml.get( "topic" ) )
        print( "#######" + topic.cleanup_policy )

    def test_parse_full_deployment( self ):
        file_name = "tests/resources/example-full.yaml"
        yaml_content = open( file_name ).read()
        parsed = yaml.load( yaml_content )
        deployment = DeploymentDescriptor.parse( parsed )


if __name__ == '__main__':
    unittest.main()