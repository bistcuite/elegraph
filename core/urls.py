from django.urls import path, include
import core.views as views

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('upload_image/', views.upload_image),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='category_detail'),
    path('',views.home)
]