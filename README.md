# 🏢 Facility & Booking API
A robust and RESTful API built with Django and Django REST Framework (DRF) that allows users to register, authenticate, and manage facilities and their bookings. This system is ideal for managing scheduling and reservations for resources such as hotels, event spaces, or conference rooms.

## ✨ Features
- Authentication
- User registration, login, and logout
- Session or token-based authentication (based on setup)
- Secure password hashing and user management

## 🏢 Facility Management
- Add new facilities (e.g., rooms, venues, equipment)
- View facility listings
- Edit facility details
- Delete facilities

## 📅 Booking Management
- Add new bookings to facilities
- View current and past bookings
- Edit existing bookings
- Cancel/delete bookings

## 🧰 Tech Stack
- Component	Technology
- Backend	Python, Django
- API Framework	Django REST Framework (DRF)
- Authentication	Custom DRF serializers
- Database	SQLite (default, swappable)
- API Testing Tool	Postman, cURL, or HTTPie

## 🧪 API Testing
- Use Postman, Insomnia, or cURL to test endpoints. Typical endpoints may include:
- POST /api/register/ – User registration
- POST /api/login/ – User login
- POST /api/logout/ – User logout
- GET /api/facilities/ – List facilities
- POST /api/facilities/ – Create facility
- GET /api/bookings/ – List bookings
- POST /api/bookings/ – Create booking
- Authentication headers are required for protected routes.

## 🔐 Authentication
This API uses custom serializers for user registration and login. You can implement session or token-based auth depending on your setup.

## 🧩 Optional Enhancements
- JWT or token authentication (via djangorestframework-simplejwt)
- Booking availability validation
- Admin panel for managing facilities and bookings
- Time-based filtering and conflict checks

