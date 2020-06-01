import random
import time

print("""************************
Sayı Tahmin Oyunu

1 ile 50 arasındaki sayıyı tahmin edin.Toplamda 8 adet tahmin hakkınız olacaktır.

1-) Geriye Kalan Tahmin Hakkınızı Görüntülemek İçin e'yi Tuşlayınız
2-) Oyundan Çıkmak İçin q'yu Tuşlayınız

""")

rastgele_sayi = random.randint(1,100)
tahmin_hakki = 3

while True:
    tahmin = input("Tahmininiz:")
    if (tahmin =="q"):
        print("Çıkış Yapılıyor")
        break
    elif (tahmin=="e"):
        print("Kalan Tahmin Sayınız:",tahmin_hakki)
    else:
        tahmin = int(tahmin)

        if (tahmin < rastgele_sayi):
            print("Kontrol Ediliyor...")
            time.sleep(1)
            print("Daha Yüksek Bir Sayı Girin")
            tahmin_hakki-=1
        
        elif ( tahmin > rastgele_sayi):
            print("Kontrol Ediliyor...")
            time.sleep(1)
            print("Daha Düşük Bir Sayı Girin")
            tahmin_hakki-=1

        else:
            print("Tebrikler bildiniz ! Sayımız:",rastgele_sayi)
            break

        if (tahmin_hakki ==0):
            print("Tahmin Hakkınız Bitmiştir")
            break


