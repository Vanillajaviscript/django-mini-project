from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finchees/', views.finchees_index, name='index'),
  path('finchees/<int:finch_id>/', views.finchees_detail, name='detail'),
  path('finchees/create/', views.FinchCreate.as_view(), name='finchees_create'),
  path('finchees/<int:pk>/update/', views.FinchUpdate.as_view(), name='finchees_update'),
  path('finchees/<int:pk>/delete/', views.FinchDelete.as_view(), name='finchees_delete'),
  path('finchees/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]