from django.shortcuts import render
from django import views

# Create your views here.
class MainPageView(views.View):
    def get(self, request):
        return render(request, "image_board/home_page.html")