from . import views
from django.urls import path
from .views import IndexView

app_name = 'photo'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/', views.CreatePhotoView.as_view(), name='post'),
]
