from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('abouts',views.About.as_view(),name='about'),
    #Posts
    path('create-post',views.createPost.as_view(),name='create-post'),
    path('list',views.listPosts.as_view(),name='list'),
    path('draft',views.DraftPost.as_view(),name='draft'),
    #Post CRUD
    re_path(r'^detail/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='post_detail'),
    re_path(r'^list/(?P<pk>\d+)/$',views.deletePost.as_view(),name='delete'),
    # re_path(r'^update/(?P<pk>\d+)/$',views.updatePost.as_view(),name='update'),
    #Comments
    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comments,name='comment'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='approve'),
    re_path(r'^comment/(?P<pk>\d+)/delete/$',views.comment_remove,name='comment_delete'),
]