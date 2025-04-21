from alembic.util import status
from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlalchemy.sql.coercions import expect

from .serializer import FacilitySerializer,RegistrationSerializer,LoginSerializer,BookingSerializer
from .models import Facility,Booking
from django.contrib.auth import logout
# Create your views here.

class Register(APIView):
    def post(self,request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have been registered. Please Login'}, status=201)
            return Response({'message':'Registration failed. Try again!!'}, status=400)
        except Exception as e:
            return Response({'message':'Internal server error', "error": str(e)}, status=500)

class Login(APIView):
    def post(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully login'},status=200)
            return Response({'message':'Login failed. Try again!!'}, status=400)
        except Exception as e:
            return Response({'message':'Internal server error', 'error':str(e)},status=500)

class Logout(APIView):
    def get(self,request):
        logout(request)
        return Response({'message':'You have successfully logout out'}, status=200)

class FacilityListView(APIView):
    def get(self,request):
       try:
           facility = Facility.objects.all()
           serializer = FacilitySerializer(facility,many=True)
           return Response(serializer.data,status=200)
       except Exception as e:
           return Response({'message':'Internal server error', 'error':str(e)},status=500)

class FacilitySingle(APIView):
    def get(self,request,facility_id):
        try:
            facility = Facility.objects.get(id = facility_id)
            serializer = FacilitySerializer(facility)
            return Response(serializer.data)
        except Facility.DoesNotExist:
            return Response({'error':'Internal server error'},status=400)
        except Exception as e:
            return Response({'error': 'Internal server error', 'details': str(e)},status=500)

class AddFacility(APIView):
    def post(self,request):
        try:
            serializer = FacilitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Facility has been added'},status=200)
            return Response({serializer.errors},status=400)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=500)

class EditFacility(APIView):
    def put(self,request,facility_id):
        try:
            facility = Facility.objects.get(id=facility_id)
            serializer = FacilitySerializer(facility,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully edited the facility','facility':serializer.data},status=200)
            return Response({'message':'This has not been edited'},status=400)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=500)

class DeleteFacility(APIView):
    def delete(self,request,facility_id):
        try:
            facility = Facility.objects.get(id=facility_id)
            facility.delete()
            return Response({'message':'facility has been deleted'},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class AddBooking(APIView):
    def post(self,request):
        try:
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Booking has been added'},status=200)
            return Response({'message','This booking was not added'},status=400)
        except Exception as e:
            return Response({'message':'Internal server error', 'error':str(e)},status=500)

class BookingView(APIView):
    def get(self,request):
        try:
            booking = Booking.objects.all()
            serializer = BookingSerializer(booking, many=True)
            return Response(serializer.data,status=200)
        except Exception as e:
            return Response({'message':'Internal sever error','error':str(e)},500)

class BookingSingle(APIView):
    def get(self,request,booking_id):
        try:
            booking = Booking.objects.get(id= booking_id)
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({'message':'internal server error', 'error':str(e)}, status=500)

class EditBooking(APIView):
    def put(self,request,booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
            serializer = BookingSerializer(booking, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This booking has been edited'},status=200)
            return Response({'message':'This booking has not been edited'},status=400)
        except Exception as e:
            return Response({'message':"internal server error",'error':str(e)},status=500)

class DeleteBooking(APIView):
    def delete(self,request,booking_id):
        try:
            booking = Booking.objects.get(id = booking_id)
            booking.delete()
            return Response({'message':'This booking has been deleted'},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)
