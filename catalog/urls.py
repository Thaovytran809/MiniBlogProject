from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='blogger_list'),
    path('bloggers/<int:pk>', views.BloggerDetailView.as_view(), name='blogger_detail'),
    path('blogs/<int:pk>/create', views.CommentCreate.as_view(), name='comment_create'),
    path('blogger/createblogger', views.BloggerCreate.as_view(), name='blogger_create'),
    path('blogger/<int:pk>/updateblogger', views.BloggerUpdate.as_view(), name='blogger_update'),
    path('blogger/<int:pk>/deleteblogger', views.BloggerDelete.as_view(), name='blogger_delete'),
    path('blog/createblog', views.BlogCreate.as_view(), name='blog_create'),
    path('blog/<int:pk>/updateblog', views.BlogUpdate.as_view(), name='blog_update'),
    path('blog/<int:pk>/deleteblog', views.BlogDelete.as_view(), name='blog_delete')
    
    
]



