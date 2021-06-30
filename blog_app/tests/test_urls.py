from django.test import TestCase
from django.urls import resolve
from ..views import IndexView, DetailView, ArchiveView, TagIndexView, tag_detail, FormView
from ..models import Article, Tag


# それぞれのページのURLが適切なビュー画面を返すか確認

class IndexUrlTests(TestCase):

    def test_resolve_index_url_to_index_view(self):
        view = resolve('/blog_app/')
        self.assertEqual(view.func.view_class, IndexView)


class DetailUrlTests(TestCase):

    def test_resolve_detail_url_to_detail_view(self):
        article1 = Article.objects.create()
        pk = article1.id
        view = resolve('/blog_app/' + str(pk) + '/')
        self.assertEqual(view.func.view_class, DetailView)


class ArchiveUrlTests(TestCase):

    def test_resolve_archive_url_to_archive_view(self):
        view = resolve('/blog_app/archive/')
        self.assertEqual(view.func.view_class, ArchiveView)


class TagIndexUrlTests(TestCase):

    def test_resolve_tag_index_url_to_tag_index_view(self):
        view = resolve('/blog_app/tag/')
        self.assertEqual(view.func.view_class, TagIndexView)


class TagDetailUrlTests(TestCase):

    def test_resolve_tag_detail_url_to_tag_detail_view(self):
        tag1 = Tag.objects.create()
        pk = tag1.id
        view = resolve('/blog_app/tag/' + str(pk) + '/')
        self.assertEqual(view.func, tag_detail)


class FormUrlTests(TestCase):

    def test_resolve_form_url_to_form_view(self):
        view = resolve('/blog_app/postarticle/')
        self.assertEqual(view.func.view_class, FormView)

