from django.urls import path

from .views import employee_hello


urlpatterns = [

    # /employees/ calls the employee_hello view
    path("", employee_hello),
]