import unittest
import sys

from helloworld_inference import HelloWorldInference

"""
python -m unitest TestHelloWorldInference.test_run
"""
 
class TestHelloWorldInference(unittest.TestCase):
    """Test FFDMetadataExtractor"""

    def test_run(self):
        hello_inf = HelloWorldInference(1,2)
        MilesPredicted = hello_inf.run()

        #self.assertEqual(17.8849806, MilesPredicted)
        self.assertAlmostEqual(17.8849806, MilesPredicted, places=7)

def main():
    m = TestHelloWorldInference()
    #print(m)

    return m.test_run()


if __name__== "__main__":
    retval = main()
    print(f"End with ({retval})")