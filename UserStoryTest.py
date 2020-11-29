import unittest
import UserStory16

class test_UserStory16(unittest.TestCase):
    def test_check_account(self):
        UserStory16.account = "Roni Jack Vituli"
        UserStory16.password = "5t4r3e2w1q"
        UserStory16.store = "Zap"
        self.assertFalse(UserStory16.check_account())
        UserStory16.store = "Zara"
        self.assertTrue(UserStory16.check_account())
        UserStory16.account = "TOMNIfdsdf"
        self.assertFalse(UserStory16.check_account())
        UserStory16.account = "Roni Jack Vituli"
        UserStory16.password = "5t4r3e2w1q"
        UserStory16.store = "Zara"
        self.assertTrue(UserStory16.check_account())
        UserStory16.account = "Avi Kohen"
        UserStory16.password = "5t4r3e2w1q"
        UserStory16.store = "H&M"
        self.assertTrue(UserStory16.check_account())
        UserStory16.account = "Josh kliver"
        UserStory16.password = "5t4r3e2w1q"
        UserStory16.store = "Mango"
        self.assertTrue(UserStory16.check_account())
    def test_Take_info_store(self):
        self.assertEqual(UserStory16.obj['Stores'][0]['Name'],'Zara')
        self.assertEqual(UserStory16.obj['Stores'][1]['Name'], 'Mango')
        self.assertEqual(UserStory16.obj['Stores'][2]['Name'], 'H&M')
        self.assertNotEqual(UserStory16.obj['Stores'][0]['Name'],"4221")
        self.assertNotEqual(UserStory16.obj['Stores'][1]['Name'], "ewrfd")
        self.assertNotEqual(UserStory16.obj['Stores'][2]['Name'], "gfklje3lkrjnv")

if __name__ == '__main__':
    unittest.main()
