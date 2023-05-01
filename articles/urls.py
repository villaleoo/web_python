from django.urls import path
from articles.views import ListArticles, CreateArticle, EditArticle, DeleteArticle, MoreDetailsArticle

app_name="article"

urlpatterns = [
    path('', ListArticles.as_view(), name='home'),
    path('article/create', CreateArticle.as_view(), name="creator_article"),
    path('article/delete/<int:pk>', DeleteArticle.as_view(), name="eliminator_article"),
    path('article/modify/<int:pk>', EditArticle.as_view(), name="modificator_article" ), #pk: primary key funciona como id
    path('article/<int:pk>', MoreDetailsArticle.as_view(), name="details_article")
]