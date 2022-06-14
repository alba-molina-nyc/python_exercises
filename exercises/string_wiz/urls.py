from django.urls import path

from . import views

urlpatterns = [
    # path('url_route_name', views_page.url_name, name='url_name'),
    path('', views.home, name='home'),
    path('<int:Translation_Question_id>/', views.detail, name='detail'),
   
    
]