
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.starting_page ,name = "home"),
    path("posts",views.posts, name = "posts"),
    path("posts/<slug:slug>",views.full_post, name = "full-post")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)