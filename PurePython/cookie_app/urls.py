from django.urls import path

from cookie_app.views import TestCookie, AddCookies, ShowCookies, DeleteCookies

urlpatterns = [
    path('test/', TestCookie ),
    path('add/', AddCookies ),
    path('show/', ShowCookies ),
    path('delete/<str:key>', DeleteCookies )
]