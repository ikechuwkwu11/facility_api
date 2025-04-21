from django.urls import path
from .views import Register,Login,FacilityListView,FacilitySingle,AddFacility,EditFacility,DeleteFacility,AddBooking,BookingView,BookingSingle,EditBooking,DeleteBooking

urlpatterns =[
    path('register/',Register.as_view(),name= 'register'),
    path('login/',Login.as_view(),name = 'login'),
    path('facility-listview/',FacilityListView.as_view(),name='facility-listview'),
    path('facility-single/<int:facility_id>',FacilitySingle.as_view(),name='facility-single'),
    path('add-facility/',AddFacility.as_view(),name='add-facility'),
    path('edit-facility/<int:facility_id>',EditFacility.as_view(),name='edit-facility'),
    path('delete-facility/<int:facility_id>',DeleteFacility.as_view(),name='delete-facility'),
    path('add-booking/',AddBooking.as_view(),name='add-booking'),
    path('booking-view/',BookingView.as_view(),name='booking-view'),
    path('booking-single/<int:booking_id>',BookingSingle.as_view(),name='booking-single'),
    path('edit-booking/<int:booking_id>',EditBooking.as_view(),name='edit-booking'),
    path('delete-booking/<int:booking_id>',DeleteBooking.as_view(),name='delete-booking')
]