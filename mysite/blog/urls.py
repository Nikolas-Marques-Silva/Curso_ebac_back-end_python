from django.urls import path

from blog import views
from blog.views.post_view import PostDetail

urlpatterns = [
  path('', views.PostView.as_view(), name='home'),
  path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail")
]
