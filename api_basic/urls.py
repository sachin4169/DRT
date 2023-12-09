from django.urls import path
from . import views

urlpatterns = [
    # path('article/', views.old_article_list),
    # path('article/<int:pk>/', views.article_list),

    path('article/', views.ArticleList.as_view()),
    path('article/<int:pk>/', views.ArticleDetail.as_view()),
]