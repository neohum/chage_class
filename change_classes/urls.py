from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'change_classes'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/upload/', views.upload, name='upload'),
    path('result/', views.result, name='result'),
    path('home/', views.home, name='home'),
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.FILE_URL, document_root=settings.FILE_ROOT)

# # Compare this snippet from change_class/change_classes/forms.py: 



