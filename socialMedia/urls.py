from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
    path('pages/',include('pages.urls')),
    path('post/', include('post.urls')),
]
