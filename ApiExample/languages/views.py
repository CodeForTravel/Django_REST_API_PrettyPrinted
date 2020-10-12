from django.shortcuts import render
from django.views import View
from rest_framework import viewsets,permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Language,Paradigm,Programmer
from .serializers import LanguageSerializer,ParadigmSerializer,ProgrammerSerializer
class HomeView(View):
    template_name = 'home.html'

    def get(self,request):
        return render(request,self.template_name)

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

