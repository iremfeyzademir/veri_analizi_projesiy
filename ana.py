import veri_isle
import grafik_ciz

# Veriyi oku
df = veri_isle.veri_oku("veri.csv")

# Veriyi analiz et ve ekrana yazdır
analiz_sonucu = veri_isle.veri_analiz_et(df)
print(analiz_sonucu)

# Grafik çiz
grafik_ciz.grafik_ciz(df)

