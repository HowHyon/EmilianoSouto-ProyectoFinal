from django.urls import path
from blogs import views
from .views import *

app_name = 'blogs'

urlpatterns = [
    path('', views.home_page, name ='inicio'),
    path('post/<slug:slug>', views.PostView.as_view(), name='post'),
    path('destacados/', views.FeaturedListView.as_view(), name='destacados'),
    path('categoria/<slug:slug>', views.CategoryListView.as_view(), name='categoria'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('createpost/', agregar_post, name='NewPost'),
    path('eliminarPost/<int:post_id>/', views.eliminar_post, name='eliminarPost'),
    path('editarPost/<int:post_id>/', views.editar_post, name='editarPost'),
    path('about-me/', aboutMe, name='aboutMe'),
    
    
]
