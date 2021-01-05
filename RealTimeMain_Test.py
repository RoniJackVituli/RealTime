import unittest
import RealTimeMain

class RealTimeMain_TEST(unittest.TestCase):

    def test_about(self):
        x = [3,4,5]
        self.assertIsNotNone(RealTimeMain.about)
        self.assertIsNot(RealTimeMain.about, x)
        self.assertNotIn(RealTimeMain.about,x)

    # def test_cp(self):


    def test_return_dic(self):
        tuple = ('Zara', 'http//:www.zara.com', 'photo', 'hour', 'desc', 'username')
        self.assertIsNotNone(RealTimeMain.tupleToDic(tuple))
        self.assertIn('company', RealTimeMain.tupleToDic(tuple))
        self.assertIn('link', RealTimeMain.tupleToDic(tuple))
        self.assertIn('photo', RealTimeMain.tupleToDic(tuple))
        self.assertIn('hour', RealTimeMain.tupleToDic(tuple))
        self.assertIn('desc', RealTimeMain.tupleToDic(tuple))
        self.assertIn('username', RealTimeMain.tupleToDic(tuple))
        self.assertNotIn('Zara',RealTimeMain.tupleToDic(tuple))
        self.assertNotIn('http//:www.zara.com',RealTimeMain.tupleToDic(tuple))
        self.assertNotIn('10:00-12:00',RealTimeMain.tupleToDic(tuple))
        self.assertNotIn('RJV@gmail.com',RealTimeMain.tupleToDic(tuple))
        self.assertNotIn('P&B',RealTimeMain.tupleToDic(tuple))
        self.assertNotIn('Dominos',RealTimeMain.tupleToDic(tuple))



if __name__ == '__main__':
    unittest.main()
