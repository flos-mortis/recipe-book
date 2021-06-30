from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='home'),
    path('add', views.add, name='add'),
    path('recipe', views.recipe, name='recipe'),
    path('profile', views.profile, name='profile'),
    path('search', views.search, name='search'),
    path('autor', views.autor, name='autor'),
    path('register', views.register, name='register')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
