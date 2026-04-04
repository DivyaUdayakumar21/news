from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class TestUserManager(TestCase):
    def testusermodel(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "testuser",
            email = "testuser@example.com",
            password = "testpass123"
            )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def testsuperusermodel(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username= "testsuperuser",
            email="testsuperuser@example.com",
            password="testsuperuser123"
        )

        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)