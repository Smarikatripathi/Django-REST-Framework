from django.urls import path
from . import views
urlpatterns = [
    path("core/", views.coreViews),
    path("core/<int:pk>/", views.coreDetailViews),
]