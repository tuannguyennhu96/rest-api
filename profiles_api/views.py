from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            '11',
            'sdasd',
            'asdasd11',
            'skk144',
        ]

        return Response({'message':"helo", 'an_apiview':an_apiview})
