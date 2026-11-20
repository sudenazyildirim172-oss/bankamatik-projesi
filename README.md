# Bankamatik (ATM) Simülasyonu

Uludağ Üniversitesi Yapay Zeka Topluluğu (TALOSLU OLMAK) 1. Hafta Python Giriş görevi kapsamında geliştirilmiş, Nesne Tabanlı Programlama (OOP) temelli konsol Bankamatik uygulamasıdır.

## Projenin Amacı ve Çalışma Mantığı

Uygulama, gerçek bir ATM cihazının temel güvenlik doğrulama ve finansal işlem adımlarını simüle eder:
1. **Giriş ve Güvenlik Kontrolü:** Kullanıcının şifresini doğrulaması için 3 deneme hakkı bulunur. 3 hatalı denemede hesap güvenlik amacıyla bloke edilir.
2. **İşlem Menüsü:** Doğrulama başarılı olduğunda kullanıcı `while` döngüsü içinde sürekli çalışan ana menüye yönlendirilir ve çıkış seçeneğini kullanana kadar ardışık işlemler yapabilir.
3. **Bakiye ve Geçmiş Takibi:** Yapılan her para yatırma ve çekme işlemi anlık olarak bakiyeyi günceller ve işlem geçmişi listesine (`self.gecmis`) kaydedilir.

## Sınıf ve Fonksiyon Yapısı

Proje sorumlulukların ayrılması (modülerlik) ilkesiyle 2 ana sınıf üzerine kurulmuştur:

* **`Hesap` Sınıfı:** Müşteri verilerini (`ad`, `sifre`, `bakiye`, `gecmis`) tutar ve doğrudan hesap üzerindeki işlemleri yönetir.
  * `para_yatir(miktar)`: Pozitif tutar kontrolü yaparak bakiyeyi artırır ve işlemi geçmişe kaydeder.
  * `para_cek(miktar)`: Tutarın pozitifliğini ve bakiye yeterliliğini kontrol ederek bakiyeden düşer.
  * `bakiye_goster()`: Kullanıcının güncel bakiyesini ve yaptığı tüm işlemlerin listesini ekrana yazdırır.
* **`Bankamatik` Sınıfı:** ATM arayüzünü, şifre deneme hakkını (`hak = 3`) ve menü akışını yönetir.
  * `giris_yap()`: `while` döngüsü ve koşullu ifadelerle şifre doğrulaması yapar.
  * `calisitr()`: Giriş onaylandıktan sonra kullanıcı seçimlerine göre `Hesap` nesnesinin ilgili metotlarını çağırır.

## Akış Şeması (Flowchart)

```mermaid
flowchart TD
    A([BAŞLA]) --> B[/Hesap Nesnesi Oluştur: Ad, Şifre, Bakiye, Hak = 3/]
    B --> C{hak > 0 mı?}
    C -- Hayır --> D[/Hesap Bloke Edildi Mesajı/]
    D --> Z([BİTİR])
    C -- Evet --> E[/Kullanıcıdan Şifre Al/]
    E --> F{Şifre Doğru mu?}
    F -- Hayır --> G[hak = hak - 1]
    G --> H[/Hatalı Şifre ve Kalan Hak Yazdır/]
    H --> C
    F -- Evet --> I[/Hoş Geldiniz Mesajı/]
    I --> J[/Menü Göster: 1-Para Yatır, 2-Para Çek, 3-Bakiye, 4-Çıkış/]
    J --> K[/Seçim Al/]
    K --> L{Seçim Nedir?}
    L -- 1 --> M[/Miktar Al ve Bakiye Artır, Geçmişe Ekle/]
    M --> J
    L -- 2 --> N[/Miktar Al/]
    N --> O{Miktar <= Bakiye mi?}
    O -- Evet --> P[Bakiye Azalt, Geçmişe Ekle]
    P --> J
    O -- Hayır --> Q[/Yetersiz Bakiye Uyarısı/]
    Q --> J
    L -- 3 --> R[/Güncel Bakiye ve İşlem Geçmişini Yazdır/]
    R --> J
    L -- 4 --> S[/Çıkış Mesajı Yazdır/]
    S --> Z
    L -- Geçersiz --> T[/Geçersiz Seçim Uyarısı/]
    T --> J
