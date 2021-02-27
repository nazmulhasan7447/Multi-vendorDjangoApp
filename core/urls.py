from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from core.api import MessageModelViewSet, UserModelViewSet, upload_file, download
from django.conf import settings
from django.views.static import serve

router = DefaultRouter()
router.register(r'message', MessageModelViewSet, basename='message-api')
router.register(r'user', UserModelViewSet, basename='user-api')

urlpatterns = [
    path('chat', include(router.urls)),
    
    path('upload_file', upload_file, name='upload_file'),
    path('download/<path:file_name>', download, name='download'),
    path('', login_required(
        TemplateView.as_view(template_name='core/chat.html')), name='home'),
]

