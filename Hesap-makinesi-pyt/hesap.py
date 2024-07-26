
gecmis = []

while True:
    print("\nMenü:")
    print("1) Toplama işlemi")
    print("2) Çıkarma işlemi")
    print("3) Çarpma işlemi")
    print("4) Bölme işlemi")
    print("5) İşlem geçmişini görüntüleme işlemi")
    print("6) Hesap makinesinden çıkış yapma işlemi")

    secim = input("Bir seçim yapınız (1-6): ")

    if secim == '1':
        a = float(input("Birinci sayıyı giriniz: "))
        b = float(input("İkinci sayıyı giriniz: "))
        sonuc = a + b
        print(f"Sonuç: {sonuc}")
        gecmis.append(f"{a} + {b} = {sonuc}")

    elif secim == '2':
        a = float(input("Birinci sayıyı giriniz: "))
        b = float(input("İkinci sayıyı giriniz: "))
        sonuc = a - b
        print(f"Sonuç: {sonuc}")
        gecmis.append(f"{a} - {b} = {sonuc}")

    elif secim == '3':
        a = float(input("Birinci sayıyı giriniz: "))
        b = float(input("İkinci sayıyı giriniz: "))
        sonuc = a * b
        print(f"Sonuç: {sonuc}")
        gecmis.append(f"{a} * {b} = {sonuc}")

    elif secim == '4':
        a = float(input("Birinci sayıyı giriniz: "))
        b = float(input("İkinci sayıyı giriniz: "))
        if b != 0:
            sonuc = a / b
            print(f"Sonuç: {sonuc}")
            gecmis.append(f"{a} / {b} = {sonuc}")
        else:
            print("Hata: Bölme işlemi sıfıra yapılamaz.")
            gecmis.append(f"{a} / {b} = Hata (Bölme işlemi sıfıra yapılamaz)")

    elif secim == '5':
        print("\nİşlem Geçmişi:")
        for islem in gecmis:
            print(islem)

    elif secim == '6':
        print("Hesap makinesinden çıkış yapılıyor.")
        break

    else:
        print("Geçersiz İşlem! Lütfen tekrar seçim yapınız.")

# hesap_makinesi()
