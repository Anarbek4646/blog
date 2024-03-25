
from django.urls import path, include

from category import views

urlpatterns = [
    path('', views.CategoryCreateLIstViews.as_view()),
    path('<int:pk>/', views.CategoryDetailViews.as_view()),

    # path('getlist/', tasks_list),
    # path('create/', categories_create)

]
