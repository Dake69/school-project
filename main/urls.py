from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from .views import HeroViewSet
from .views import ItemList
from .views import NeutralItemList
from .views import Structures
from .views import LineCreeps
from .views import SmallNeutralCamps
from .views import BigNeutralCamps
from .views import AncientNeutralCamps
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'heroes', HeroViewSet)
router.register(r'items', ItemList)
router.register(r'neutral items', NeutralItemList)
router.register(r'structures', Structures)
router.register(r"line creeps", LineCreeps)
router.register(r'smallneutralcamps', SmallNeutralCamps)
router.register(r'bigneutralcamps', BigNeutralCamps)
router.register(r'ancientneutralcamps', AncientNeutralCamps)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls