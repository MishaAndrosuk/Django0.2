from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from pd322Django import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('films/', include('films.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    