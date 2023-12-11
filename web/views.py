from django.shortcuts import render


def main_view(request):
    return render(request, "web/main.html")


def registration_view(request):
    pass


def auth_view(request):
    pass


def saved_view(request):
    pass


def news_add_view(request):
    pass
