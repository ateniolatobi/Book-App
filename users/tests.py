from django.test import TestCase
from django.contrib.auth import get_user_model
# from .models import CustomUser

# Create your tests here.


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()

        user = User.objects.create_user(username='dave', email="dave@email.com", password="testPass2344")
        self.assertEquals(user.username, 'dave')
        self.assertEquals(user.email, 'dave@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(username="superadmin", email="admin@email.com", password='adminPass90832')
        self.assertEquals(user.username, 'superadmin')
        self.assertEquals(user.email, 'admin@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
