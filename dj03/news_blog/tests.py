from django.test import TestCase
from .models import NewsPost
from django.contrib.auth.models import User

class NewsPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        NewsPost.objects.create(
            title="Test News",
            short_description="Short description of the test news.",
            text="Full text of the test news.",
            author=self.user,
        )

    def test_news_post_creation(self):
        news_post = NewsPost.objects.get(title="Test News")
        self.assertEqual(news_post.author.username, 'testuser')

