from django.urls import path
from django.contrib.auth import views as auth_views

from . import views, forms

app_name = 'blog_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    path('tag/<int:tag_id>/', views.tag_detail, name='tag_detail'),
    path('contact/', views.contact_form, name='contact'),

    path('login/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm), name='login'),
    path('manage/', views.ManageView.as_view(), name='manage'),
    path('manage/post/', views.FormView.as_view(), name='form'),
    path('manage/edit/<int:pk>/', views.edit_form, name='edit'),
    path('manage/edit/<int:pk>/delete/', views.delete_form, name='delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
