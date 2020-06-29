from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import UserAPI
from .serializers import UserAPISerializer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives



import osimport math


from .serializers import UserApiSerializer
from wrkyetuez import statement

class UserAPIView(APIView):

    def get(self, request):
        print(request.data)
        queryset = UserAPI.objects.filter(email=request.data.get('email'))
        if queryset:
            if queryset.values('password').first()['password'] == request.data.get('password'):
                return Response("You are successfully looged in")
            else:
                return Response("Password is incorrect")
        else:
            return Response("User is not registered")
        return Response(UserAPI.objects.all())

    def login(request):
        return render(request, 'login.html')

    def post(self, request):
        queryset =request.data

        serializer = UserAPISerializer(data=queryset)
        if serializer.is.valid(raise_exception=True):
            save_data = serializer.save()
            emailSend(request.data.get['email'], request.data.get[])
         return Response ({"Success":"User '{}" created sucessfully".format(save_data.name)})





        return Response ("Success":"User '{}' created successfully".format(save_data.name)})


    def put(self, request, pk):
        queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)

        ##queryset.update(email="random@gmail.com")
        parsed_data = request.data ## it will give the new values
        serializer = UserApiSerializer(instance=queryset, data=parsed_data, partial=True)

        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
        return Response ({"Success": "User '{}' updated suceesfully".format{save_data.name}})

        def submitUser(request):
            email = request.GET['emailid']
            password = request.GET['pass']
            name = request.GET['name']
            print(email, password, name, "this is me")

    payload = {"email":email, "password":password, "name":name}
        payload = json.dumps(payload)
        headers = {
        'Content-Type': 'application/json'
        }



        def delete(self, request, pk):
            queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)
            queryset.delete()
            return Response ({"Success":"USer with id'{}' deleted successfully".format(pk)})

        response = requests.request("POST", url, headers=headers, data = payload)
        data = response
        return render()


def emailSend(email, username):
    text_content = "Yay! Succesfully registered"
    subject = "Welcome to our website"
    template_name = "emailactivation.html"

context = {
    'username':username
}

from_email = "random@gmail.com"
recipients = [email]
html_content = render_to_string(template_name, context)
email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
email.attach_alternative(html_content, "text/html")
email.send()

