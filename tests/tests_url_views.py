from django.test import SimpleTestCase
from django.urls import reverse, resolve

from source.accounts.urls import (LogInView, SignUpView, ResendActivationCodeView, RestorePasswordView,
                                  ChangeProfileView, ChangeEmailView, RemindUsernameView, ChangePasswordView,
                                  LogOutView, )


class TestUrls(SimpleTestCase):

    # Sign In Test
    def test_sign_in_url_is_resolved(self):
        url = reverse('log-in/')
        self.assertEqual(resolve(url).func, LogInView)

    # Sign Up Test
    def test_sign_up_url_is_resolved(self):
        url = reverse('sign-up/')
        self.assertEqual(resolve(url).func, SignUpView)

    # Resend Activation Code Test
    def test_resend_activation_code_resolved(self):
        url = reverse('resend/activation-code/')
        self.assertEqual(resolve(url).func, ResendActivationCodeView)

    # Restore Password Test
    def test_restore_password_is_resolved(self):
        url = reverse('restore/password/')
        self.assertEqual(resolve(url).func, RestorePasswordView)

    # Change Profile Test
    def test_change_profile_view_is_resolved(self):
        url = reverse('change/profile/')
        self.assertEqual(resolve(url).func, ChangeProfileView)

    # Change Email Test
    def test_change_email_is_resolved(self):
        url = reverse('change/email/')
        self.assertEqual(resolve(url).func, ChangeEmailView)

    # Change Remind User Name Test
    def test_remind_user_name_is_resolved(self):
        url = reverse('remind/username/')
        self.assertEqual(resolve(url).func, RemindUsernameView)

    # Change Password Test
    def test_change_password_is_resolved(self):
        url = reverse('change/password/')
        self.assertEqual(resolve(url).func, ChangePasswordView)

    # Log Out Test
    def test_log_out_is_resolved(self):
        url = reverse('log-out/')
        self.assertEqual(resolve(url).func, LogOutView)
