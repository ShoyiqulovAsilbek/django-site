from django.contrib import admin
from django.urls import path, include

app_name = 'meetupapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meetupapp.urls'))

]
