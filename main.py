import time
parola=5548
users_liste = []
kutuphane_liste=[]
class Users():
    knosu=1
    def __init__(self,adi,soyadi,sehir,numarasi,yasi,kitaplar):
        self.adi=adi
        self.soyadi=soyadi
        self.sehir=sehir
        self.numarasi=numarasi
        self.yasi=yasi
        self.kitaplar=kitaplar
        self.knosu=self.__class__.knosu
        self.__class__.knosu+=1

    def goster(self):

        print("""
        Adi : {}
        Soyadı: {}
        Şehiri: {}
        Numarası: {}
        Yaşı: {}
        Aldığı Kitaplar: {}
        Kullanıc Numarası : {}
        
        """.format(self.adi,self.soyadi,self.sehir,self.numarasi,self.yasi,self.kitaplar,self.knosu))
    def numara_degis(self,numarasi):
        print("Numaranız Değişiyor..... Bekleyiniz....")
        time.sleep(1)
        self.numarasi=numarasi
    def kitapal(self,ykitap):
        self.kitaplar.append(ykitap)
        print(self.kitaplar,"Elinizdeki Kitaplar")
    def yeni_sehir(self,sehir):
        print("Yaşadığınız Şehir Değiştiriliyor...")
        time.sleep(1)
        self.sehir=sehir




class Kutuphane():
    def __init__(self,kutuphane_adi,adresi,kutuphane_kitaplari):
        self.kutuphane_adi=kutuphane_adi
        self.adresi=adresi

        self.kutuphane_kitaplari=kutuphane_kitaplari

    def kullanici_ekle(self,veri):
        self.veri=veri
        print("Kullanıcı Kaydı yapılıyorrr...")
        time.sleep(1)
        self.user.append(veri)












ali= Users("Ali Fuat","Aslan","Samsun",54389865,24,["osmanlı","güvercin"])
huso= Users("Hüseyin Emre","Armağan","Muğla",1234566789,24,["zaman","pesoektif","yolcu"])
hasan= Users("Hasan","Kafes","izmie",66666666,23,["mermi","geçmişten günümüze"])
users_liste.append(ali)
users_liste.append(huso)
users_liste.append(hasan)
buca_kutuphanesi=Kutuphane("buca halk","izmir buca",["sevgi","savaş ve baış","holmes"])
kutuphane_liste.append(buca_kutuphanesi)

sorgu=input("değer giriniz ... \n kullanıcılar için 1 e \n kütüphane için 2 ye")

if sorgu=="1":
    while True:
        sorgu = input("""
        * * * ** * * * * ** * 
        Yapmak istediğiniz işlemi Giriniz..
        Yeni Kitap Almak için 1 e
        Kayıt oluşturmak için 2 ye
        Kitap Bırakmak için 3 e
        Numara değiştirmek için 4 e
        Şehir Değiştirmek için 5 e
        Üyelere göz Atmak için 6 ya
        Çıkış için q ya basınız.....
        * * * * * * * * ** * * *\n
        """)
        if sorgu == "q":
            break
        elif sorgu == "1":
            print("Hangi Kullanıcıya kitap vereceksiniz... \nLütfen Kullanıcı numarasını giriniz...")
            for i in range(0, len(users_liste)):
                users_liste[i].goster()
            try:
                no = int(input("Kullanıcı Numarası  :"))
                if len(users_liste[no - 1].kitaplar) < 3:
                    print(len(users_liste[no].kitaplar))
                    ykitap = input("Kitabın Adı  :")
                    users_liste[no - 1].kitapal(ykitap)
                else:
                    print("Kitap Sayınız 3 Veya Üzeridir Lütfen Önce Kitap teslim ediniz....")
            except:
                print("HATAlI İŞLEMMM........")
        elif sorgu == "2":
            print("Yeni Kayır Sayfasındasınız Lütfen Paraloyı Giriniz")
            sifre = input("Parola:   ")
            if str(parola) == sifre:
                adi = input("Adı  :")
                soyadi = input("Soyadı  :")
                sehir = input("Şehir  :")
                numarasi = input("Numarası  :")
                yasi = input("Yaşı  :")
                kitaplar = []
                users_liste.append(Users(adi, soyadi, sehir, numarasi, yasi, kitaplar))
                print("Yeni Kullanıcı Eklendiiii.....")

            else:

                print(" Hatalı Paralo Girişi Yaptınız.... \n Sistemden Çıkış Yapılıyor....")
                time.sleep(1)
                break
        elif sorgu == "3":
            print("Hangi Kullanıcı kitap Bırakacak... \nLütfen Kullanıcı numarasını giriniz...")
            for i in range(0, len(users_liste)):
                users_liste[i].goster()
            try:
                no = int(input("Kullanıcı Numarası  :"))
                print(users_liste[no - 1].kitaplar)
                print("Hangi Kitabı bırakmak istiyorsanız ilk kitap birinci olmak üzere numarasını yazınız...")
                birak = int(input("Numarası : "))
                users_liste[no - 1].kitaplar.pop(birak - 1)
                print("Kitap Başarılı Bir Şekilde Teslim edildi.....")
                time.sleep(2)
            except:
                print("HaTalıııı....")

        elif sorgu == "4":
            print("Hangi Kullanıcının Numarası değişşin Lütfen Kullanıcı Numarasını yazızınız")
            for i in range(0, len(users_liste)):
                users_liste[i].goster()
            try:
                degis = int(input("Kullanıcı Numarası  :"))
                ynum = input("Yeni Numarayı Giriniz.. : ")
                users_liste[degis - 1].numara_degis(ynum)

            except:
                print("HATALI İŞLEMMMMMM")
        elif sorgu == "5":
            print("Hangi Kullanıcının Şehiri değişşin Lütfen Kullanıcı Numarasını yazızınız")
            for i in range(0, len(users_liste)):
                users_liste[i].goster()
            try:
                degis = int(input("Kullanıcı Numarası  :"))
                ysehir = input("Yeni Şehirini Giriniz.. : ")
                users_liste[degis - 1].yeni_sehir(ysehir)

            except:
                print("HATALI İŞLEMMMMMM")

        elif sorgu == "6":
            for i in range(0, len(users_liste)):
                users_liste[i].goster()
        else:
            print("HATALI İŞLEM.......")
            time.sleep(1)
else:
    while True:
        x= input("""
        * * * ** * * * * * *** * * **  *
        tüm kütüphaneler için 1 e 
        kütüphane eklemek için 2 ye
        üyeleri görmek için 3 e 
        üye işlemleri için 4 e 
        çıkıs için q ya basınız...
        
        * * * * * * **  * *** *** ** *  *
        """)
        if x=="q":
            break