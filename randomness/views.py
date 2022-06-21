from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

@permission_classes((AllowAny,))
class hello(APIView):
    def get(self, request):
        
        import random

        first_names=('Namrata','Nam','Nam Nam')
        last_names=('deesh','Deesh','Reddy')

        group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(1))
        return Response(
            group
            )
class RandomList(APIView):
    def get(self, request):
        import random

        first_names=('Namrataaaa','Nam','Nam Nam')
        last_names=('Jags','Deesh','Reddy')

        group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(1))
        return Response(
            group
            )