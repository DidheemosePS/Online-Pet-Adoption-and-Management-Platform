from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('search/', views.search, name='search'),
    path('show_interest/<str:id>/', views.show_interest, name="show_interest"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('saved_posts/', views.saved_posts, name='saved_posts'),
    path('interest_showed/', views.interest_showed, name='interest_showed'),
    path('create_posts/', views.create_posts, name='create_posts'),
    path('save_this_post/', views.save_this_post, name='save_this_post'),
    path('posts_created_by_you/', views.posts_created_by_you,
         name='posts_created_by_you'),
    path('confirm_interest/', views.confirm_interest,
         name='confirm_interest'),
    path('edit_created_post/<str:id>/', views.edit_created_post,
         name='edit_created_post'),
    path('delete_created_post/<str:id>/', views.delete_created_post,
         name='delete_created_post'),
]
