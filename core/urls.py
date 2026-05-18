from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('about/', views.about_page, name='about'),
    path('team/', views.team_page, name='team'),
    path('contact/', views.contact_page, name='contact'),
    path('nexax/', views.nexax_page, name='nexax'),
    path('nexa-school/', views.nexaschool_page, name='nexaschool'),
    path('services/artificial-intelligence/', views.ai_service_page, name='service_ai'),
    path('services/app-development/', views.app_development_page, name='service_app_dev'),
    path('services/website-development/', views.web_development_page, name='service_web_dev'),
]