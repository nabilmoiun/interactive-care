Overview
========
A simple Application using Django, Django Rest Framework (DRF), Vue that allows a user to send bulk emails. For simplicity, I have used dummy SMTP server Mailtrap, for development and testing.
So the mails won't go to real mail inboxes. Follow the steps below to run the application:

Run
====

    $ git clone https://github.com/nabilmoiun/iteractive-care.git
    $ cd iteractive-care
    $ pip install virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py runserver

 ***Now Go to http://localhost:8000***

 You will find the ui displaying a form asking you to input the email_subject, email_body, email_addresses & attachment[optional]

Submit the form properly to send emails to provided addresses.

Or you can directly call ***http://localhost:8000/send-emails/*** this POST api to send emails. This receives a form-data And returns {"success": True, "message": "Emails have been sent successfully"} on success. You must use an api-client such as Postman to call this api directly.


Mailtrap
========
As mentioned above, I have used a dummy Mailtrap SMTP server as instructed. So, the mail go to a Mailtrap inboxe rather than real mail inboxes that are provided. So, to test it in your own inbox you have to login/signup the Mailtrap to create your own credentials to find the mails into your inbox. Currently, the application uses my credentials for testing. So please follow the steps below to test it on your own Mailtrap inbox:

+ First go to https://mailtrap.io/ & signin with your gmail or preferred method.
+ After signin, go to your Inboxes from Email Testing tab from sidebar or you can directly click this https://mailtrap.io/inboxes to enter there
+ Then you will find a demo inbox or you can also create your own. Now click on the inbox link. Now from the Integrations select menu select Django. You will find the credentials as follows:

        $ EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
        $ EMAIL_HOST_USER = '1ade998ba5ad9e'
        $ EMAIL_HOST_PASSWORD = '93344b7b8a5465'
        $ EMAIL_PORT = '2525'

These are my credentials, yours will be different.
Now go to .env file & replace the credentials as provided:

Edit the .env file as follows:

        $ EMAIL_HOST =sandbox.smtp.mailtrap.io
        $ EMAIL_HOST_USER =1ade998ba5ad9e
        $ EMAIL_HOST_PASSWORD =93344b7b8a5465
        $ EMAIL_PORT =2525
        $ FROM_EMAIL =sender_email@gmail.com

FROM_EMAIL can be any mail. Now, the application will send demo/test emails in your Mailtrap inbox that you used. You can go to your inbox and check them out.






