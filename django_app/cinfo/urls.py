from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("count", views.count, name="count"),
    path('__debug__/', include('debug_toolbar.urls')),
]

