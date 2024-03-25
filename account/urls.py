
from django.urls import path, include

from account import views
from dj_rest_auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
    # path('getlist/', tasks_list),
    # path('create/', categories_create)

]
