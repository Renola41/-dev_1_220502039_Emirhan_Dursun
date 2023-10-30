while True:

    print()
    #menüde seçenekleri sunulması
    print("1 --> Listede istenilen sıradaki küçük elamnı bulma\t\t".ljust(53),
    end="|    2 --> Verilen listede verilen sayıya en yakın iki çifti bulma\n")
    print("3 -->Listenin tekrar eden elemanını bulma\t\t".ljust(51),
    end="|    4 --> Matris çarpım işlemi\n")
    print("5 --> Text dosyasındaki kelimelerin frekansını bulma\t".ljust(51),
    end="|    6 --> Listedeki en küçük değeri bulma\n")
    print("7 --> babil metoduyla karekök bulma\t\t".ljust(53),
    end="|    8 -->EBOB bulma\n")
    print("9 --> Asal mı değil mi?\t\t".ljust(53),
    end="|    10 --> Hızlı fibonacci hesabı\n")
    print("0 --> Çıkış")
    print()
    #kullanıcıdan yapmak istediği işlemin numarasını alıp ve daha sonra kaçı tuşladıysa
    #programı o fonksiyona yönlendirmek
    secim = int(input("Yapmak istediğiniz işlemin numarasını tuşlayınız (0-10): "))
    print()

    #listedeki istenilen sıradaki küçük sayıyı bulan fonk.
    if secim == 1:
        print("1.işlem seçildi")
        print()
        def k_kucuk(sira, liste):
            sirali_liste = sorted(liste)    #listeyi küçükten büyüğe sıralama
            sirali_liste = list(set(liste)) #tekrar eden elemanları listeden kaldırma
            sonuc = sirali_liste[sira - 1]  #indeksler 0 dan başlar ama sıralamalar 1 den başlar o yüzden indeks bazında bir eksiğidir
            return print(sonuc)

        k_kucuk(3, [7, 10, 4, 3, 20, 15])

    #veilen listede verilen sayıya en yakın iki çifti bulma
    elif secim == 2:

        print("2.işlem seçildi")
        print()

        def en_yakin_cift(sayi, liste):
            liste.append(sayi)      #sayıyı listeye ekle
            yeni_liste = []
            for i in liste:
                if i % 2 == 0:      # sayı çift ise yeni_listeye ekle
                    yeni_liste.append(i)
                else:
                    continue
            sirali_liste = sorted(yeni_liste)   #küçükten büyüğe sırala
            print(sirali_liste)

            # verilen sayının indeksini buluyoruz ve sağındaki ve solundaki sayıların en yakın 2 çifti alıyoruz
            indeks = sirali_liste.index(sayi)
            en_yakin_iki_cift = []
            #verilen sayının soluna ve sağına bakıyoruz en yakın olanı en yakın çift listemize alıyoruz
            if sirali_liste[indeks] - sirali_liste[indeks - 1] < sirali_liste[indeks + 1] - sirali_liste[indeks]:
                en_yakin_iki_cift.append(sirali_liste[indeks - 1])
            #eşitseler ikisini alıyoruz
            elif sirali_liste[indeks] - sirali_liste[indeks - 1] == sirali_liste[indeks + 1] - sirali_liste[indeks]:
                en_yakin_iki_cift.append(sirali_liste[indeks - 1])
                en_yakin_iki_cift.append(sirali_liste[indeks + 1])
            else:
                en_yakin_iki_cift.append(sirali_liste[indeks + 1])
                #eğer sağındaki sayıyı eklediysek
                if sirali_liste[indeks] - sirali_liste[indeks - 1] < sirali_liste[indeks + 2] - sirali_liste[indeks]:
                    en_yakin_iki_cift.append(sirali_liste[indeks - 1])
                else:
                    en_yakin_iki_cift.append(sirali_liste[indeks + 2])
            return en_yakin_iki_cift

        print("en yakın iki çift =",en_yakin_cift(54, [10, 22, 10, 22, 28, 29, 50,  30, 34, 34, 40, 60, 78, 58, 53, 55]))

    elif secim == 3:
        print("3.işlem seçildi")
        print()
        #listedeki tekrarayan elemanları bulma
        def tekrar_eden_elemanlar(liste):

            tekrar_edenler = []
            # listenin içinde bir düngü ve onun içindede bir dögü daha kurarak listedeki her elemanı listenin tüm elemanlarıyla karşılaştırma
            for i in liste:
                sayac = 0
                for a in liste:
                    if i == a:
                        sayac += 1
                if sayac > 1 and i not in tekrar_edenler: #eğer zaten tekrarr edenler listesinde var ise ekleme
                    tekrar_edenler.append(i)
            return tekrar_edenler

        print("listedeki tekrar eden elemanlar= ",tekrar_eden_elemanlar([1, 2, 3, 2, 1, 5, 6, 5, 5, 5]))


    elif secim == 4:
        #matris çarpımı (Zip metodu ile)
        print("4.işlem seçildi")
        print()

        matrisA = [[1, 2, 3], [4, 5, 6]]
        matrisB = [[7, 8], [9, 10], [11, 12]]
        def matris_carpimi(A_matrisi, B_matrisi):
            #matrislerin satır ve sutun sayılarını öğrenme
            satir1 = len(A_matrisi)
            sutun1 = len(A_matrisi[0])
            satir2 = len(B_matrisi)
            sutun2 = len(B_matrisi[0])
    #eğer sutun1 ve satır2 eşit değilse işlem yapılamaz
            if sutun1 != satir2:
                return "İlk matrisin sütunu ile ikinci matrisin satır sayısı eşit olmalıdır!!!"
            #boş matris listemizi oluşturuyoruz
            matris_c = []

            for i in range(satir1):
                matris_c_satirlari = [] #satirları tek liste şeklinde oluşturup matris_c ye sutun sutun ekliyoruz
                for j in range(sutun2):
                    # zip() kullanarak matris elemanlarını çarpıp toplama
                    carpim = sum(x * y for x, y in zip(A_matrisi[i], (satir[j] for satir in B_matrisi)))
                    matris_c_satirlari.append(carpim)
                matris_c.append(matris_c_satirlari)

            return matris_c

        print(matris_carpimi(matrisA, matrisB))



    elif secim == 5:
        #verilen text dosyasındaki kelimelerin adetini bulan fobk.
        print("5.işlem seçildi")
        print()
        def kelime_frekans(kelime_dosyasi):
            with open(kelime_dosyasi, "r") as dosya: #dosyayı okuma yöntemi ile açıyoruz
                metin = dosya.read()    #dosyayı okuyup okunanı bir değişkene atıyoruz

            metin = metin.lower()   #tüm harfleri küçük harf yapıp farklı karakter algılanmamasını sağlamak
            kelimeler = metin.split()   #kelimeleri boşluklar  ile ayırmak

            frekans_sozlugu = {}    #kelimeler value değer ve adetleri sayıları key değer olup
            # beraber kolayca çağırabilmek için sözlük formatında tutuyoruz

            for i in kelimeler:
                sayac = 0                    #iç içe dögü kurup her kelimeyi kelimeler listesindeki her kelime ile karşılaştırıyoruz
                for a in kelimeler:            # eğer eşitseler sayaç 1 artıyor ve o elemandan listede kaç adet olduğu bulunuyor
                    if i == a:
                        sayac += 1
                frekans_sozlugu[i] = sayac

            print("Metinde geçen kelimeler ve frekansları")
            print("------------------------------------------")
            for anahtar, deger in frekans_sozlugu.items():
                print("{} = {}".format(anahtar, deger))
            print("-------------------------------------------")

        kelime_frekans("kelime_frekansı.txt")


    elif secim == 6:
        #listedeki en küçük değeri bulan fonk
        print("6.işlem seçildi")
        print()

        def en_kucuk_deger(liste):
            # eğer tek elemanlı bir liste ise kendisini döndür,boş bir liste ise "boş liste" mesajını döndür
            if len(liste) == 1:
                return liste[0]
            elif len(liste) == 0:
                return "boş liste"

            #listeyi her çağırdığımızda listenin her adımda boyutunu baştan küçülterek
            # bütün elemanları karşılaştırıyoruz
            else:
                en_kucuk_sonraki = en_kucuk_deger(liste[1:])

                if liste[0] < en_kucuk_sonraki:
                    return liste[0]
                else:
                    return en_kucuk_sonraki

        print(en_kucuk_deger([1, 2, 3, -1, 4, -2, 5]))


    elif secim == 7:
        #babil yöntemi ile karekök alma fonk.
        print("7.işlem seçildi")
        print()
    #kökünü almak istenilen sayı ve iki kare arsından tahmin yürüterek ilk tahmin girişi alma
        N = float(input("Karekökünü almak istediğiniz sayıyı girin: "))
        x_0 = float(input("Başlangıç tahminini girin: "))
        def babil_yontemi(N, x_0, tolerans=10 ** (-10), tekrar=10, tekrar_sayisi=0):
            #babil kare kök formulü
            x_1 = (x_0 + N / x_0) / 2

            if tekrar_sayisi > tekrar:
                return "maksimum tekrar sayısına ulaştınız " \
                       "\nen yakın değeri tekrar hesaplamak ister iseniz en son değer = {}".format(x_1)

            if abs(x_1 - x_0) < tolerans:   #eğer tahmin ile sonucun arasındaki fark belilenen toleranstan küçükse fonksiyondaki en yakınsanacak noktaya ulaşılmıştır
                return x_1
            else:
                return babil_yontemi(N, x_1)    #değilse fonksiyon tekrar yinelensin


        yakinsama_sonuc = babil_yontemi(N, x_0)
        print("Babil yöntemi ile en yakınsanacak karekök sonucunuz = {}".format(yakinsama_sonuc))


    elif secim == 8:
        #en büyük ortak bölen bulan fonk.
        print("8.işlem seçildi")
        print()
        #ebobu istenilen iki sayı girişi alma
        print("Sırasıyla büyük ve küçük sayıyı giriniz")
        sayi1 = int(input("1. Sayıyı giriniz"))
        sayi2 = int(input("2. Sayıyı giriniz"))

        def ebob(a, b):
            if b == 0:      #eğer b = 0 sa a'nın kendisini döndür
                return a
            else:
                return ebob(b, a % b)   #kağıt üstünde daha iyi anlaşılacaktı   örnek: 39,13-->13,0 if b==a return a(a=13)

        sonuc = ebob(sayi1, sayi2)
        print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {sonuc}")


    elif secim == 9:
        #asal mı değil mi bulan fonk.
        print("9.işlem seçildi")
        print()

        sayi =int(input("asal mı değil mi bulmak istediğiniz sayıyı giriniz : "))
        def asal_veya_degil(sayi, bolen=2):
            if sayi == 2:
                return True
            elif sayi <= 1:
                return False
            if bolen * bolen > sayi:    #eğer bir sayıyı kare köküne kadar bçlünmüyorsa karesini alınca geçiyorsa başka böleni yoktur demek
                return True                #örnek 19 2 bölmez(4),3 bölmez(9),4 bölmez (16),5 bölmez (25)
            if sayi % bolen == 0:           # 25>19 olduğundan 5 üstündeki sayılara bakmaya gerek kalmaz
                return False
            return asal_veya_degil(sayi, bolen + 1)

        sonuc = asal_veya_degil(sayi)
        if sonuc:
            print(f"{sayi} bir asal sayıdır.")
        else:
            print(f"{sayi} bir asal sayı değildir.")



    elif secim == 10:
        print("10.işlem seçildi")
        print()
        #istenilen adaım kadar fibonacci dizesi elde etme

        n = int(input("n (kaçıncı Fibonacci sayısı hesaplanacak olan) : ")) #8
        k = int(input("bir sayı k(k sayısı n sayısına ulaştığında işlemler biter : ")) #1
        fibk = int(input("fibk : ")) #1
        fibk1 = int(input("fibk1 : ")) #0

        def fib(n, k, fibk, fibk1):
            print(f"n={n}, k={k}, fibk={fibk}, fibk1={fibk1}")
            if n == k:              #istenilen adıma ulaşıldığında dögüyü bitire
                return "Döngü bitti"

            else:
                #değilse fibonacci dizisini hesapla ve k'yi artır fibk ve fibk1 fibonacci ağacı şeklinde birbirinin devamıdır
                next_fib = fibk + fibk1
                return fib(n, k + 1, next_fib, fibk)


        fib(n, k, fibk, fibk1)

    elif secim == 0:
        print("Programdan çıkılıyor..")
        break  # While döngüsünü kır

    else:#uyarı
        print("yanlış tuşlama yaptınız! Lütfen 0-10 arasında bir sayı girin.")
    print()
    tekrar = input("Menüye dönmek için 'm' tuşuna basın, çıkış için '0' tuşuna basın: ")
    if tekrar == 'm':
        continue
    elif tekrar == '0':
        print("Program Sonlandırılıyor")
        break