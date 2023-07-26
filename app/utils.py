from os import path
import pandas as pd
from django.conf import settings
from sklearn.preprocessing import StandardScaler, LabelEncoder

start_year = 2021


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
    df = df[df['tahun'] >= start_year]

    df['bulan'] = df['bulan'].apply(clean_month)
    df['harga'] = df['harga'].apply(int)
    df['bulan'] = df['bulan'] + (df['tahun'] - start_year) * 12

    premium_df = df[df['kualitas'] == 'Premium']
    medium_df = df[df['kualitas'] == 'Medium']
    low_df = df[df['kualitas'] == 'Luar Kualitas']

    premium_df = premium_df.drop('kualitas', axis=1)
    medium_df = medium_df.drop('kualitas', axis=1)
    low_df = low_df.drop('kualitas', axis=1)

    premium_df = premium_df.drop('tahun', axis=1)
    medium_df = medium_df.drop('tahun', axis=1)
    low_df = low_df.drop('tahun', axis=1)

    X_premium, Y_premium = premium_df.iloc[:, :-1], premium_df.iloc[:, -1]
    X_medium, Y_medium = medium_df.iloc[:, :-1], medium_df.iloc[:, -1]
    X_low, Y_low = low_df.iloc[:, :-1], low_df.iloc[:, -1]

    return X_premium, Y_premium, X_medium, Y_medium, X_low, Y_low


def prediction(model, pred):
    return model.predict(pred)
