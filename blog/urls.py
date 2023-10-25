from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<uuid:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<uuid:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<uuid:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
