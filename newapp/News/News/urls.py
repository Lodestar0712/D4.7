from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('news/', include('newapp.urls')),
   path('new/', include('newapp.urls')),
   path('articles/',include('newapp.urls'))
]