import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

secim = 0

data = pd.read_csv('titanic.csv')

while secim != 7:
    print("\n*** TITANIC ISLEM MENUSU ***")
    print("1-Veri seti hakkinda bilgi edin")
    print("2-Veri setindeki degiskenlerin anlamlarini gor")
    print("3-Veri setindeki essiz degerleri gor")
    print("4-Gorsellestirmeleri gor")
    print("5-Eksik degerleri gor")
    print("6-Degiskenler arasindaki korelasyonlari gor")
    print("7-Cikis yap")

    secim = int(input("\nBir islem seciniz:"))

    if secim == 1:
        print("-------------------------------------------------------")
        print("** Veri setinin ilk 10 satiri **")
        print("-------------------------------------------------------")
        print(data.head(10))
        print("-------------------------------------------------------\n")

        print("-------------------------------------------------------")
        print("** Gozlemler hakkinda istatiksel bilgiler **")
        print("-------------------------------------------------------")
        print(data.describe())
        print("-------------------------------------------------------")

        print("-------------------------------------------------------")
        print("* Toplam {} satir ve {} sutun veri bulunuyor.".format(data.shape[0], data.shape[1]))
        print("* Toplam {} adet veri bulunuyor.".format(data.size))
        print("-------------------------------------------------------")

    elif secim == 2:
        print("** Degiskenler hakkinda bilgiler **")
        print("-------------------------------------------------------")
        print(data.info())
        print("-------------------------------------------------------")

    elif secim == 3:
        print("Sutunlardaki essiz veri adetleri:\n")
        print(data.nunique())

    elif secim == 4:
        plt.style.use("fivethirtyeight")
        plt.figure(figsize=(12, 10))
        plt.hist(data.Pclass, color="green")
        plt.xlabel("Sınıf")
        plt.ylabel("İnsan Sayısı")
        plt.title("Sınıflara göre insan sayısı")
        plt.show()

        plt.figure(figsize=(12, 10))
        plt.hist(data.Age)
        plt.xlabel("Yaş")
        plt.ylabel("Kurtulan insan sayısı")
        plt.title("Yaşlara göre kurtulan insan sayısı")
        plt.show()

        plt.figure(figsize=(12, 10))
        plt.plot(data.Age, data.Fare, color="red")
        plt.xlabel("Yaş")
        plt.ylabel("Ödenen Para")
        plt.title("Yaşlara göre ödenen toplam para")
        plt.show()

        plt.figure(figsize=(5, 5))
        data.Sex.value_counts().plot(kind='pie')
        plt.title("Cinsiyete göre gemideki insan sayısı dağılımı")
        plt.show()

    elif secim == 5:
        deger = data.isna().values.any()

        if deger == True:
            print("\n--> Veri setinde eksik deger var")
            print("Eksik deger adeti = {}".format(data.isnull().values.sum()))

            print("---------------------------------------")
            print("** Sutunlara gore eksik adet listesi **")
            print("---------------------------------------")
            print(data.isnull().sum())
            print("---------------------------------------\n")

            # Eksik verileri temizledik
            print("--> Eksik veriler temizlendi:\n")
            df = data.dropna()
            print(df.isnull().sum().sort_values(ascending=False))

        else:
            print("--> Veri setinde eksik deger yok\n")

    elif secim == 6:
        print("\nKorelasyon matrisi:\n")
        corr = np.round(data.corr(), 2)
        print(corr)

    elif secim == 7:
        print("Cikis yaptiniz!")
        break

    else:
        print("\nBoyle bir islem bulunamadi!\n")
