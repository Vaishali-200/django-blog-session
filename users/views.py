from  rest_framework.generics import CreateAPIView
from  rest_framework.response import Response
from .serializers import UserSignUpSerializer
from .models import User


# Create your views here.
# class HelloWorld(APIView):
#     def get(self,request):
#         return Response("Hello World")

class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA",request.data)
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            obj=User.objects.get(email=request.data["email"])

            response_data={
                "id":obj.email,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
                "email":obj.email
            }
            return Response(response_data)
        else:
            return Response(serializer.errors)