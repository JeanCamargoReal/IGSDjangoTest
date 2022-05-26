from sqlite3 import Cursor

from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeesAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

