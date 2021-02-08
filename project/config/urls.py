from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # csrf_exempt disables for the view the csrf protection
    # when taken away, graphene can query but cannot post
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
