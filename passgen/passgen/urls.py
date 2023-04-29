from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('password', include('main.urls')),
]
