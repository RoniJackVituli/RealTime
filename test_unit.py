import os
import unittest

from RealTimeSite import app, db


TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # executed after each test
    def tearDown(self):
        pass


###############
#### tests ####
###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

def register(self, email, password, confirm):
    return self.app.post(
        '/register',
        data=dict(email=email, password=password, confirm=confirm),
        follow_redirects=True
    )

def login(self, email, password):
    return self.app.post(
        '/login',
        data=dict(email=email, password=password),
        follow_redirects=True
    )

def logout(self):
    return self.app.get(
        '/logout',
        follow_redirects=True
    )

def test_valid_user_registration(self):
    response = self.register('patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Thanks for registering!', response.data)


def test_invalid_user_registration_different_passwords(self):
    response = self.register('patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsNotAwesome')
    self.assertIn(b'Field must be equal to password.', response.data)
def test_invalid_user_registration_duplicate_email(self):
     response = self.register('patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
     self.assertEqual(response.status_code, 200)
     response = self.register('patkennedy79@gmail.com', 'FlaskIsReallyAwesome', 'FlaskIsReallyAwesome')
     self.assertIn(b'ERROR! Email (patkennedy79@gmail.com) already exists.', response.data)

if __name__ == "__main__":
    unittest.main()
