import unittest
# import os
# import sys
# sys.path.insert(0, os.path.abspath('..\src'))
from helloworld_inference import HelloWorldInference

"""
python -m unitest TestHelloWorldInference.test_run
"""
 
class TestHelloWorldInference(unittest.TestCase):
    """Test FFDMetadataExtractor"""
    def test_ping(self):
         hello_inf = HelloWorldInference(1,2)
         print('class linkage successful')

    def test_run(self):
        hello_inf = HelloWorldInference(1,2)
        MilesPredicted = hello_inf.run()

        #self.assertEqual(17.8849806, MilesPredicted)
        self.assertAlmostEqual(17.8849806, MilesPredicted, places=7)