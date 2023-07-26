import pandas as pd
from django.shortcuts import render
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from .utils import *
import numpy as np


def get_template(temp):
    return f"app/{temp}.html"


class LandingPage(TemplateView):
    template_name = get_template('index')

    def get_context_data(self, **kwargs):
        year, month, qlt = None, None, None
        context = super().get_context_data(**kwargs)
        month_list = ['januari', 'febuari', 'maret', 'april', 'mei', 'juni', 'juli', 'agustus', 'september', 'oktober',
                      'november', 'desember']

        month_list = [x.capitalize() for x in month_list]
        x_premium, y_premium, x_medium, y_medium, x_low, y_low = data_frame()

        premium_scaler = StandardScaler()
        premium_scaler.fit(x_premium)

        medium_scaler = StandardScaler()
        medium_scaler.fit(x_medium)

        low_scaler = StandardScaler()
        low_scaler.fit(x_low)

        premium_scaled_data = premium_scaler.transform(x_premium)
        premium_scaled_data = pd.DataFrame(premium_scaled_data, columns=x_premium.columns)

        medium_scaled_data = medium_scaler.transform(x_medium)
        medium_scaled_data = pd.DataFrame(medium_scaled_data, columns=x_medium.columns)

        low_scaled_data = low_scaler.transform(x_low)
        low_scaled_data = pd.DataFrame(low_scaled_data, columns=x_low.columns)

        model_premium = LogisticRegression(solver='newton-cg', penalty=None)
        model_medium = LogisticRegression(solver='newton-cg', penalty=None)
        model_low = LogisticRegression(solver='newton-cg', penalty=None)

        model_premium.fit(premium_scaled_data, y_premium)
        model_medium.fit(medium_scaled_data, y_medium)
        model_low.fit(low_scaled_data, y_low)

        if self.request.GET.get('year') is not None:
            year = int(self.request.GET.get('year')) if self.request.GET.get('year') is not None else None
            month = self.request.GET.get('month')
            month = clean_month(month)

            qlt = self.request.GET.get('qlt')

            months = month + (year - start_year) * 12

            pred = np.array([[month]])
            if qlt.lower() == 'premium':
                predict = prediction(model_premium, pred)
            elif qlt.lower == 'medium':
                predict = prediction(model_medium, pred)
            else:
                predict = prediction(model_low, pred)

            context['predict'] = f"Rp {round(predict[0], 4):,.4f}"

        context['months'] = month_list
        context['year'] = year
        context['monthss'] = month
        context['qlt'] = qlt
        return context

    # @method_decorator(login_required(login_url=settings.LOGIN_URL))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
