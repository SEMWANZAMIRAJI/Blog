from django.contrib import admin
from django.urls import path
from feed.views import HomePage, CreateFeed, Login, Logout, PostUpdateView, PostDeleteView,FeedDetailview,CreateComment,RegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", HomePage.as_view(), name="home"),
    path("create-post/", CreateFeed.as_view(), name="create_post"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path("feed/<int:pk>", FeedDetailview.as_view(), name="feed_detail"),
    path("comment/<int:pk>", CreateComment.as_view(), name="create_comment"),
    path('register/', RegisterView.as_view(), name='register'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
