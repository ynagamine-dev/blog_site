from django.test import TestCase
from ..models import Article, Tag


class ArticleModelTests(TestCase):

    def test_is_empty(self):
        # 初期状態では記事が登録されていないことを確認

        saved_articles = Article.objects.all()
        self.assertEqual(saved_articles.count(), 0)

    def test_is_one(self):
        # 記事を1つ登録すると、1としてカウントされるかどうか確認
        # フィールド必要？

        article = Article(title='test_title', text='test_text', author='test_author')
        article.save()
        saved_articles = Article.objects.all()
        self.assertEqual(saved_articles.count(), 1)

    def test_save_and_retrieve_article(self):
        # 記事に特定の値を指定して保存し、保存した値と同じ値が返されるかどうか確認

        article = Article()

        title = 'test_title_to_retrieve'
        text = 'test_text_to_retrieve'
        author = 'test_author_to_retrieve'

        article.title = title
        article.text = text
        article.author = author

        article.save()

        saved_articles = Article.objects.all()
        new_post = saved_articles[0]

        self.assertEqual(new_post.title, title)
        self.assertEqual(new_post.text, text)
        self.assertEqual(new_post.author, author)


class TagModelTests(TestCase):

    def test_is_empty(self):
        # 初期状態ではタグが登録されていないことを確認

        saved_tags = Tag.objects.all()
        self.assertEqual(saved_tags.count(), 0)

    def test_is_one(self):
        # タグを1つ登録すると、1としてカウントされるかどうか確認
        # フィールド必要？

        tag = Tag(name='test_name')
        tag.save()
        saved_tags = Tag.objects.all()
        self.assertEqual(saved_tags.count(), 1)

    def test_save_and_retrieve_tag(self):
        # 保存したタグを取り出せるのか確認

        tag = Tag()
        name = tag.name
        tag.save()

        saved_tags = Tag.objects.all()
        new_tag = saved_tags[0]

        self.assertEqual(new_tag.name, name)


class ArticleSetModelTests(TestCase):

    def test_select_tag_and_retrieve_article_set(self):
        # 保存されたタグを選択して記事を作成し、Article.tagsのフィールド変数であるrelated_name='article_set'を使ってタグから記事を逆参照できるのか確認

        tag = Tag()
        tag.save()

        article = Article.objects.create()
        article.tags.add(tag)

        self.assertIn(article, tag.article_set.all())

