from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

#Genera 4 url para get, post, delete, put
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls