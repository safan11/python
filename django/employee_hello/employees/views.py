from django.http import HttpResponse


# Simple view that returns employee information
def employee_hello(request):

    return HttpResponse(
        "Hello John! Welcome to Employee Application"
    )