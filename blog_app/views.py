from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.views import generic
from django.urls import reverse_lazy

from .models import Article, Tag
from .forms import ContactForm, PostArticleForm


class IndexView(generic.ListView):

    template_name = 'blog_app/index.html'
    context_object_name = 'latest_three_articles'

    def get_queryset(self):
        return Article.objects.order_by('-created_at')[0:3]


class DetailView(generic.DetailView):

    model = Article
    template_name = 'blog_app/detail.html'


class ArchiveView(generic.ListView):

    template_name = 'blog_app/archive.html'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.order_by('-created_at')


def tag_detail(request, tag_id):

    tag = get_object_or_404(Tag, pk=tag_id)
    article_set = tag.article_set.order_by('-created_at')
    paginator = Paginator(article_set, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_app/tag_detail.html', {'tag': tag, 'article_set': article_set, 'page_obj': page_obj})


def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "ブログ閲覧者からのお問い合わせ"
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['name'] + '\n\n' + form.cleaned_data['text']

            try:
                send_mail(subject, message, from_email, ['ynagamine.dev@gmail.com'])

            except BadHeaderError:
                return HttpResponse('無効なヘッダーです。')

            return redirect('blog_app:index')

    else:
        form = ContactForm()

    return render(request, 'blog_app/contact_form.html', {'form': form})


class FormView(generic.CreateView):

    model = Article
    template_name = 'blog_app/form.html'
    form_class = PostArticleForm
    success_url = reverse_lazy('blog_app:index')


class ManageView(generic.ListView):

    template_name = 'blog_app/manage.html'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.order_by('-created_at')


def edit_form(request, pk):

    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = PostArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()

        return redirect('blog_app:manage')

    else:
        form = PostArticleForm(instance=article)

    return render(request, 'blog_app/edit.html', {'form': form, 'article': article})


def delete_form(request, pk):

    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('blog_app:manage')
