# Müşteri hesap bilgilerini ve hesap işlemlerini tutan sınıf 
class Hesap:
    def __init__(self , ad ,sifre, bakiye=0):
        self.ad = ad                #Hesap sahibinin adı
        self.sifre = sifre          #Hesap giriş şifresi
        self.bakiye = bakiye        #Başlangıç bakiyesi
        self.gecmis = []            #Yapılan işlemlerin tutulacağı liste
    # Hesaba para yatırma metodu
    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            self.gecmis.append(f"Para yatırıldı: {miktar} TL")
            print(f"{miktar} TL başarıyla yatırıldı. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Lütfen geçerli bir miktar girin.")
    # Hesaptan para çekme metodu
    def para_cek(self, miktar):
        if miktar > 0:
            if miktar <= self.bakiye:
                self.bakiye -= miktar
                self.gecmis.append(f"Para çekildi: {miktar} TL")
                print(f"{miktar} TL başarıyla çekildi. Güncel bakiye: {self.bakiye} TL")
            else:
                print("Yetersiz bakiye. İşlem gerçekleştirilemedi.")
        else:
            print("Lütfen geçerli bir miktar girin.")
    # Güncel bakiyeyi ve yapılan işlemleri gösteren metot
    def bakiye_goster(self):
        print(f"selam {self.ad}, güncel bakiyeniz: {self.bakiye} TL") 
        for islem in self.gecmis:
            print(islem)
# ATM güvenlik ve menü akışını yöneten sınıf
class Bankamatik:
    def __init__(self,hesap):
        self.hesap = hesap      #İşlem yapılacak müşteri nesnesi
        self.hak = 3            #Maksimum hatalı şifre deneme hakkı
    # 3 hak ile kullanıcı şifre doğrulaması yapan metot
    def giris_yap(self):
        while self.hak > 0:
         sifre = input("Lütfen şifrenizi girin: ")
         if sifre == self.hesap.sifre:
            print(f"Hoşgeldiniz {self.hesap.ad}!")
            if sifre == self.hesap.sifre:
                print("Şifre doğru. Giriş başarılı.")
                return True
        else:
            self.hak -= 1
            print(f"Hatalı şifre. Kalan hakkınız: {self.hak}")
            if self.hak == 0:
                print("Hesabınız bloke olmuştur. Lütfen banka ile iletişime geçin.")
                return False
    # Giriş başarılıysa ATM ana menüsünü döngüde çalıştıran metot
    def calisitr(self):        
     if self.giris_yap():
        while True:
            print("\n1. Para Yatır")
            print("2. Para Çek")
            print("3. Bakiye Göster")
            print("4. Çıkış")
            secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-4): ")
            if secim == "1":
                miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
                self.hesap.para_yatir(miktar)
            elif secim == "2":
                miktar = float(input("Çekmek istediğiniz miktarı girin: "))
                self.hesap.para_cek(miktar)
            elif secim == "3":
                self.hesap.bakiye_goster()
            elif secim == "4":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
# Programın başlatılması (Nesne oluşturma ve çalıştırma)
musteri=Hesap("Sude", "1234", 1000)
atm = Bankamatik(musteri)
atm.calisitr()

                             
