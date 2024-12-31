from rest_framework.views import APIView
from rest_framework.response import Response
from .emotion_detection import detect_emotion
from .services.recommendation_engine import get_recommendations
from rest_framework.parsers import MultiPartParser, FormParser

class EmotionRecommendationView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file = request.FILES.get("image")
        with open("temp_image.jpg", "wb") as f:
            f.write(file.read())
        emotion = detect_emotion("temp_image.jpg")
        user_language = request.user.preferred_language or "en"
        recommendations = get_recommendations(emotion, user_language)
        return Response({"emotion": emotion, "recommendations": recommendations})
