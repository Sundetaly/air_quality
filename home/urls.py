from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('city/', views.city),
    path('district/', views.district),
]