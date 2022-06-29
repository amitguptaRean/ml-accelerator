import unittest
from helloworld_inference import HelloWorldInference

"""
python -m unitest TestHelloWorldInference.test_run
"""
 
class TestHelloWorldInference(unittest.TestCase):
    """Test FFDMetadataExtractor"""

    def test_run(self):
        hello_inf = HelloWorldInference(1,1)
        MilesPredicted = hello_inf.run()
        self.assertEqual(36, MilesPredicted)
        