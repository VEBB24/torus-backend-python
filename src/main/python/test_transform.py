import unittest2
from transform import transform

class testTransform(unittest2.TestCase):

    def testNumbers(self):
        self.assertEquals(transform([1,2,3], lambda x: x+1), [2,3,4])

if __name__ == '__main__':
    unittest2.main()

