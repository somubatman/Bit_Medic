from django.urls import path

from .views import DocumentView, home, CustomLoginView, RegisterPage, filelistpatient, patientlist, patientview, doctorlist, PrescriptionView, add_doctor, remove_doctor, createpp, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('upload/', DocumentView.as_view(), name="upload"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('myfiles/', filelistpatient, name="myfiles"),
    path('mypatients/', patientlist, name="mypatients"),
    path('patient/<str:name>/', patientview, name="patient"),
    path('doctorlist/', doctorlist, name="doctorlist"),
    path('upload/<str:patient>', DocumentView.as_view(), name="upload"),
    path('prescribe/<str:patient>', PrescriptionView.as_view(), name="prescribe"),
    path('add/', add_doctor, name="add"),
    path('remove/<str:doctor>', remove_doctor, name="remove"),
    path('createpp/', createpp, name="createpp"),
    path('profile/', profile, name="profile"),

]
