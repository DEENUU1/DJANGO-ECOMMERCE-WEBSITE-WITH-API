from django.shortcuts import render
from django.views import View
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

# This is a main class that render the template


class BaseView(View):
    template_name: str = ""

    def get(self, request):
        return render(request, self.template_name)


# This is a child class of BaseView
# Returns page -> about


class AboutView(BaseView):
    template_name = "about_info.html"


# This is a child class of BaseView
# Returns page -> documents


class DocumentsView(BaseView):
    template_name = "documents_list.html"


# This is a child class of BaseView
# Returns page -> shipping information


class ShippingView(BaseView):
    template_name = "shipping_info.html"


# This is a child class of BaseView
# Returns page -> FAQ


class FaqView(BaseView):
    template_name = "faq_list.html"


# This is a child class of BaseView
# Returns page -> with all available API
# Is available only for registered users


class MainAPI(APIView):
    permission_classes = (IsAdminUser,)
    template_name = "api_list.html"

    def get(self, request):
        return render(request, self.template_name)
