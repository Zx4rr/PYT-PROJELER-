liste = []
print("TODO List Uygulaması")
while True:



    print(50*"*")
    menu = ["Listeyi Göster", "Yeni Görev Ekle", "Görev Sil", "Çıkış Yap"]
    for i in menu:
        print(menu.index(i) + 1, i)



    secim = int(input("Bir işlem seçiniz: "))

    if secim == 1:
        if len(liste)==0:
            print("ŞUAN LİSTE BOŞ!!!")
        else:
         for i in range(len(liste)):
             print(f"{i+1}.{liste[i]}")



    elif secim == 2:
        yeniGorev = input("Yeni görevi yazın: ")
        liste.append(yeniGorev)
        print("(",yeniGorev,") yeni görev başarı ile eklendi!!!")

    elif secim == 3:
        if len(liste) == 0:
            print("liste şuan boş hiç bir şey yazılmamaış")

        else:

            for i in range(len(liste)):
                print(f"görev: {liste[i]}")
            gorevsilme = input("Silmek istediğiniz görevi yazın: ")
            if gorevsilme in liste:
                liste.remove(gorevsilme)
                print(f"'{gorevsilme}' görev silindi")
            else:
                print("Bu görev listede yok!!!")

    elif secim == 4:
        break

    else:
        print("Lütfen geçerli bir sayı giriniz!")