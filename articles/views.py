from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from articles.models import Articles
from articles.forms import CreateNewArticleForm, ModifyArticleForm


class ListArticles(ListView):
    model = Articles
    template_name='index.html'

class CreateArticle(LoginRequiredMixin,CreateView):
    model= Articles
    template_name='creator_article.html'
    success_url=reverse_lazy("article:home")
    form_class= CreateNewArticleForm
    

class EditArticle(LoginRequiredMixin,UpdateView):
    model= Articles
    template_name='modify_article.html'
    success_url=reverse_lazy("article:home")
    form_class= ModifyArticleForm
  

class DeleteArticle(LoginRequiredMixin,DeleteView):
    model=Articles
    template_name='delete_article.html'
    success_url=reverse_lazy("article:home")
    

class MoreDetailsArticle(LoginRequiredMixin,DetailView):
    model=Articles
    template_name='article_layout.html'
    