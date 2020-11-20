from django.urls import path
from .views import PollViewSet, ChoiceList, CreateVote, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path(r'docs/', include_docs_urls(title='Polls API')),
    path('api/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
urlpatterns += router.urls
