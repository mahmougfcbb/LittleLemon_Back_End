from django.shortcuts import render
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
 return render(request, 'index.html', {})

from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from rest_framework import viewsets
from .models import Menu
from .serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    

