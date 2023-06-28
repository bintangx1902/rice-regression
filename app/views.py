from django.shortcuts import render
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from sklearn.linear_model import LinearRegression


def get_template(temp):
    return f"app/{temp}.html"


class LandingPage(TemplateView):
    template_name = get_template('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = LinearRegression()
        month_list = ['januari', 'febuari', 'maret', 'april', 'mei', 'juni', 'juli', 'agustus', 'septermber', 'oktober', 'november', 'desember']

        context['months'] = month_list
        return context

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
