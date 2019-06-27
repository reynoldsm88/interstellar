# -*- coding: utf-8 -*-
from interstellar.TopicDescriptor import TopicDescriptor

import yaml
import unittest


class AdvancedTestSuite( unittest.TestCase ):
    """Advanced test cases."""

    def test_parse_topic( self ):
        f = open( "tests/resources/topic-example.yaml", "r" )
        content = f.read()
        f.close()
        topic_yaml = yaml.load( content )
        topic = TopicDescriptor( **topic_yaml.get( "topic" ) )
        print("#######" + topic.cleanup_policy)


if __name__ == '__main__':
    unittest.main()