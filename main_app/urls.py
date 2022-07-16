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
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('finchees/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]