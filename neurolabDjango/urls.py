from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns =[
    path('admin/',admin.site.urls),
    path('',views.index),
    path('videos/',views.videos),
    path('index/',views.index),
<<<<<<< HEAD
    path('videos/'+'dashboard/',views.dashboard)
=======
    path('images/',views.images),
>>>>>>> bf2c203a5e9f2da6725fa43eb2549d65bdaa8243
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 