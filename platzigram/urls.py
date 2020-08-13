from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    # First examples
    path('hello-world', local_views.hello_world, name="hello_world"),
    path('sorted', local_views.hi, name="sort"),
    path('validate-age/<str:name>/<int:age>/',local_views.validate_age, name = "hi"),
    # Admin
    path('admin', admin.site.urls),
    # Posts
    path('', include(('posts.urls','posts'), namespace="posts")),
    path('users/', include(('users.urls','users'), namespace="users"))
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
