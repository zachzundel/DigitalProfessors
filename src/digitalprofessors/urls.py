from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^users/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('tutoring.urls')),
]
