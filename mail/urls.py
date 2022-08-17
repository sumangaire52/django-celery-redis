from django.urls import path

from . import views

app_name = 'mail'
urlpatterns = [ 
    path('', views.SendMailView.as_view(), name='send_mail'),
    path('success/', views.SuccessView.as_view(), name='success'),
]