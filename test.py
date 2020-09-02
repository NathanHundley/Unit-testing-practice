import unittest
import go_file

class TestMain(unittest.TestCase):

    def setup(self):
        print('About to test a funciton.')

    def test_do_stuff(self):
        test_num = 10
        result = go_file.do_stuff(test_num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_num = 'banana'
        result = go_file.do_stuff(test_num)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_num = None
        result = go_file.do_stuff(test_num)
        self.assertEqual(result, 'Please enter a number.')

    def test_do_stuff4(self):
        test_num = ''
        result = go_file.do_stuff(test_num)
        self.assertEqual(result, 'Please enter a number.')

    def test_do_stuff5(self):
        test_num = 0
        result = go_file.do_stuff(test_num)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('Cleanng Up.')

if __name__ == '__main__':
    unittest.main()