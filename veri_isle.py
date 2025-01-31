import pandas as pd

def veri_oku(dosya_adi):
    """
    CSV dosyasını okur ve Pandas DataFrame olarak döndürür.
    """
    df = pd.read_csv(dosya_adi)
    return df

def veri_analiz_et(df):
    """
    Verinin temel istatistiklerini döndürür.
    """
    return df.describe()

