from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers

from user import views as userViews
from auteur import views as auteurViews

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register(r'user', userViews.UserViewSet)
router.register(r'groups', userViews.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auteur/', include('auteur.urls')),
    path('article/', include('article.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]