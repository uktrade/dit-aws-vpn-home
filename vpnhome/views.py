import requests

from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required


class home_page(View):
    template_name = 'home-page.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ovpn_page(View):
    template_name = 'downloads/aws-ci-vpn.ovpn'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        response = render(request, self.template_name, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="vpn_client_config.ovpn"'
        return response
