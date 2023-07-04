from django.shortcuts import render
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LinearRegression
from .utils import *
import numpy as np


def get_template(temp):
    return f"app/{temp}.html"


class LandingPage(TemplateView):
    template_name = get_template('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = LinearRegression()
        month_list = ['januari', 'febuari', 'maret', 'april', 'mei', 'juni', 'juli', 'agustus', 'september', 'oktober',
                      'november', 'desember']

        X, y = data_frame()
        model.fit(X, y)
        coef = model.coef_
        rank = model.rank_
        intercept = model.intercept_
        score = model.score(X, y)

        if self.request.GET.get('year') is not None:
            year = int(self.request.GET.get('year')) if self.request.GET.get('year') is not None else None
            month = self.request.GET.get('month')
            month = clean_month(month)

            qlt = self.request.GET.get('qlt')
            qlt = clean_quality(qlt)

            pred = np.array([[year, qlt, month]])
            predict = model.predict(pred)
            context['predict'] = predict

        context['months'] = month_list
        return context

    # @method_decorator(login_required(login_url=settings.LOGIN_URL))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
