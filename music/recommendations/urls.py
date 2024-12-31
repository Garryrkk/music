from django.urls import path
from .views import EmotionRecommendationView

urlpatterns = [
    path("recommend/", EmotionRecommendationView.as_view(), name="recommend"),
]

