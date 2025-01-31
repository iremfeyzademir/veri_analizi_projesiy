import matplotlib.pyplot as plt

def grafik_ciz(df):
    """
    Verideki ilk 10 kişinin yaş dağılımını çizen bir bar grafiği oluşturur.
    """
    df = df.head(10)  # İlk 10 satırı al
    plt.bar(df["İsim"], df["Yaş"], color="skyblue")
    plt.xlabel("İsim")
    plt.ylabel("Yaş")
    plt.title("İlk 10 Kişinin Yaş Dağılımı")
    plt.xticks(rotation=45)
    plt.show()

