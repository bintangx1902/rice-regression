from os import path
import pandas as pd
from django.conf import settings


def clean_month(month):
    month_list = ['januari', 'febuari', 'maret', 'april', 'mei', 'juni', 'juli', 'agustus', 'september', 'oktober',
                  'november', 'desember']

    return month_list.index(month.lower()) + 1


def clean_quality(quality):
    a = 1
    if quality.lower() == 'premium':
        a = 3
    elif quality.lower() == 'medium':
        a = 2

    return a


def data_frame():
    df = pd.read_csv(path.join(settings.BASE_DIR, 'static', 'data_beras.csv'))
    df['bulan'] = df['bulan'].apply(clean_month)
    df['kualitas'] = df['kualitas'].apply(clean_quality)

    return df.iloc[:, :-1], df.iloc[:, -1]

