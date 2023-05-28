from rest_framework import status
from rest_framework import parsers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle

from .serializers import EmailSendingSerializer


class SendEmailToListOfUsers(APIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'email_sending'

    def post(self, *args, **kwargs):
        serializer = EmailSendingSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.send()
        response_status = status.HTTP_200_OK if response.get('success') else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(response, status=response_status)
