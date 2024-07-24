from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer

class UserRegistrationView(APIView):
    def post(self, request, *args, **kargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response = {
                "username": {
                    "detail": "User Doesnot exist!"
                }
            }
        return Response("added")