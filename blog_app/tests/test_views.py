from django.test import TestCase
from django.urls import reverse

from ..models import Article


class IndexViewTests(TestCase):

    def test_get(self):
        # GETメソッドでアクセスした際にステータスコード200が返されることを確認
        response = self.client.get(reverse('blog_app:index'))
        self.assertEqual(response.status_code, 200)


class DetailViewTests(TestCase):
    pass


class ArchiveViewTests(TestCase):

    def setUp(self):
        # テストで使用するためのデータを作成
        Article.objects.create(title='title1')
        Article.objects.create(title='title2')

    def test_get(self):
        # GETメソッドでアクセスした際にステータスコード200が返されることを確認
        response = self.client.get(reverse('blog_app:archive'))
        self.assertEqual(response.status_code, 200)

    def test_get_2_articles_on_archive(self, false=None):
        # GETメソッドでアクセスした際にsetUpメソッドで作成した二件の記事が追加されることを確認
        response = self.client.get(reverse('blog_app:archive'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(

            response.context['article_list'],
            ['<Article: title2>', '<Article: title1>']

        )

        self.assertContains(response, 'title1')
        self.assertContains(response, 'title2')

    def tearDown(self):
        # setUpメソッドで作成したデータを消去
        Article.objects.create(title='title1')
        Article.objects.create(title='title2')


class TagIndexViewTests(TestCase):
    pass


class TagDetailViewTests(TestCase):
    pass


class FormViewTests(TestCase):
    pass
