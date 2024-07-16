from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView


# Create your views here.
class PlaceHolderView(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:

        return Response(None, status=200)