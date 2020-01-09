from django.urls import path

from .views import PersonDataList, PersonDataDetail, UserList, UserDetail


urlpatterns = [
    path('person/', PersonDataList.as_view()),
    path('person/<int:pk>/', PersonDataDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
