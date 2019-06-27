# -*- coding: utf-8 -*-
import unittest

from interstellar.Interstellar import Interstellar


@unittest.skip( "TODO - need to implement a docker integration test, locally this works" )
class ParsingTestSuite( unittest.TestCase ):
    """Advanced test cases."""

    def test_connect( self ):
        interstellar = Interstellar( "tests/resources/integration-test.yaml" )
        interstellar.deploy()


if __name__ == '__main__':
    unittest.main()