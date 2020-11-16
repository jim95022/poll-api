from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/poll', PollViewSet, 'poll')
router.register('api/questions', QuestionsViewSet, 'questions')
router.register('api/results', ResultsViewSet, 'results')

urlpatterns = router.urls