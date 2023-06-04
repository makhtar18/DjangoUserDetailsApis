from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse

from .serializers import UserSerializer
from .models import User, UserDetail

# Create your views here.

#Signup API would accept the first name, last name, and email phone as input.
@csrf_exempt
@api_view(['POST'])
def signup(request):
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if(users_serializer.is_valid()):
            user = users_serializer.save()
            return JsonResponse("Signed up Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)


'''@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if(departments_serializer.is_valid()):
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if(departments_serializer.is_valid()):
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)'''