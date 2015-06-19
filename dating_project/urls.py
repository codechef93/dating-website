from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dating_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  https://docs.djangoproject.com/en/dev/howto/static-files/#serving-files-uploaded-by-a-user-during-development


# Todo: Remove above MEDIA_URL in production.
