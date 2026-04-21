from django.urls import path
from . import views
urlpatterns = [
    #function based views for core app
    path("core/", views.coreViews),
    path("core/<int:pk>/", views.coreDetailViews),

#class based views for employee model
    path("employees/", views.EmployeeViews.as_view()),
    path("employees/<int:pk>/", views.EmployeeDetailViews.as_view()),
]