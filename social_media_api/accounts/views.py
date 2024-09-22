from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
 
User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        # Use the serializer to handle user registration data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user (and automatically create a token)
            user = serializer.save()
            # Retrieve the token created for the user
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate the user using Django's built-in authenticate function
        user = authenticate(username=username, password=password)
        if user:
            # Retrieve or create a token for the authenticated user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
