from django.test import TestCase
from .models import Traveller, Comment


class TravellerModelTest(TestCase):

    def test_create_traveller(self):
        traveller = Traveller.objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            phone_number='1234567890',
            email='testuser@example.com'
        )
        self.assertEqual(str(traveller), 'Traveller(testuser@example.com)')

    # def test_phone_number_length(self):
    #     with self.assertRaises(ValidationError):
    #         Traveller.objects.create(
    #             username='testuser2',
    #             first_name='Test',
    #             last_name='User',
    #             phone_number='123',
    #             email='testuser2@example.com'
    #         )

    def test_default_image(self):
        traveller = Traveller.objects.create(
            username='testuser3',
            first_name='Test',
            last_name='User',
            phone_number='1234567890',
            email='testuser3@example.com'
        )
        self.assertEqual(traveller.image.url, '/media/profile_images/default-image.jpg')


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = Traveller.objects.create(
            username='author',
            first_name='Author',
            last_name='User',
            phone_number='1234567890',
            email='author@example.com'
        )
        cls.receiver = Traveller.objects.create(
            username='receiver',
            first_name='Receiver',
            last_name='User',
            phone_number='0987654321',
            email='receiver@example.com'
        )

    def test_create_comment(self):
        comment = Comment.objects.create(
            author=self.author,
            receiver=self.receiver
        )
        self.assertEqual(str(comment), f'Comment({self.receiver}:{self.author})')
