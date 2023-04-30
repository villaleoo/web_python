from django.urls import path
from articles.views import get_last_articles,create_new_article, delete_article, modify_article, get_article

app_name="article"

urlpatterns = [
    path('', get_last_articles, name='home'),
    path('article/create', create_new_article, name="creator_article"),
    path('article/delete/<int:id_article>', delete_article, name="eliminator_article"),
    path('article/modify/<int:id_article>', modify_article, name="modificator_article" ),
    path('article/<int:id_article>', get_article, name="get_article")
]