from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('create/', create_post, name='create_post'),
    path('topics/', topics, name='topics'),
    path('topics/<topic>/subscribe/', topic_subscribe, name='topic_subscribe'),
    path('topics/<topic>/unsubscribe/', topic_unsubscribe, name='topic_unsubscribe'),
    path('profile/<str:username>/', profile, name='profile'),
    path('set-password/', set_password, name='set_password'),
    path('set-userdata/', set_userdata, name='set_userdata'),
    path('deactivate/', deactivate_profile, name='deactivate_profile'),
    path('register/', register_new_profile, name='register_new_profile'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('<article>/', show_article, name='show_article'),
    path('<article>/comment/', article_comment, name='article_comment'),
    path('<article>/update/', article_update, name='article_update'),
    path('<article>/delete/', article_delete, name='article_delete'),
]