from util import F_to_C, C_to_F
import unittest

class unitTest(unittest.TestCase):
    def CFvalidTest(self):
        CFtest = C_to_F(-100)
        self.assertRaises(CFtest, F_to_C, -1000)

    def FCvalidTest(self):
        FCtest = F_to_C(200)
        self.assertRaises(FCtest, F_to_C, -1000)

    def CFinvalidTests(self):
        self.assertRaises(ValueError, F_to_C, -1000)

    def FCinvalidTest(self):
        self.assertRaises(ValueError, C_to_F, -2000)

unittest.main()
