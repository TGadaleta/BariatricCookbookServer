from .models import Profile
from rest_framework import generics
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            profile = user.profile
            profile.allergies = request.data.get('allergies', [])
            profile.diet = request.data.get('diet', '')
            profile.max_calories = request.data.get('max_calories', 0)
            profile.max_carbs = request.data.get('max_carbs', 0)
            profile.max_protein = request.data.get('max_protein', 0)
            profile.max_fat = request.data.get('max_fat', 0)
            profile.save()
            # Automatically log in the user after registration
            login(request, user)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)