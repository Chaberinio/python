from django.urls import path

from users_app.views import create_user, LoginView, ImportantDataView, MakeLogout, RegisterView

urlpatterns = [
    path('createTest/', create_user),
    path('login/', LoginView.as_view()),
    path('data/', ImportantDataView.as_view()),
    path('logout/', MakeLogout),
    path('register/', RegisterView.as_view()),
]