from django.conf import settings
from django.core.mail import EmailMessage

from rest_framework import serializers


class EmailSendingSerializer(serializers.Serializer):
    email_addresses = serializers.ListField()
    email_subject = serializers.CharField(trim_whitespace=True)
    email_body = serializers.CharField(trim_whitespace=True)
    attachment = serializers.FileField(required=False)

    def send(self):
        try:
            email = EmailMessage(
            subject=self.validated_data.get('email_subject'),
            body=self.validated_data.get('email_body'),
            from_email=settings.FROM_EMAIL,
            to=self.validated_data.get('email_addresses'),
            )
            attachment = self.validated_data.get('attachment')
            if attachment :
                email.attach(attachment.name, attachment.read(), attachment.content_type)
            email.send(fail_silently=False)
            return {"success": True, "message": "Emails have been sent successfully"}
        except Exception as e:
            return {"success": False, "message": f"Sorry there was an error while sending the mail {e}"}

