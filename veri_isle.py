import pandas as pd

def veri_oku(dosya_adi):
    """
    TXT dosyasını okur ve Pandas DataFrame olarak döndürür.
    """
    # Dosyayı boşluklarla ayırarak oku
    df = pd.read_csv(dosya_adi, delim_whitespace=True, header=None, names=["İsim", "Yaş", "Maaş"])
    return df

def veri_analiz_et(df):
    """
    Verinin temel istatistiklerini döndürür.
    """
    return df.describe()
