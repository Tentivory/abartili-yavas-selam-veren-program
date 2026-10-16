import time
import random

# Evrenin en yavaş selamı
mesaj = "Merhaba, evren!"

yorumlar = [
    "Bu harf, binlerce yıllık bir bekleyişi simgeliyor...",
    "Neden acele ediyoruz ki? Evren zaten sonsuz.",
    "Bir sonraki harf için varoluşsal kriz molası.",
    "Bu programın tek amacı sizi düşünmeye zorlamak.",
    "Zaman görecelidir. 3 saniye aslında bir ömür.",
    "Harfler arasında kaybolmak güzeldir.",
    "Eğer acele ediyorsanız, yanlış programdasınız."
]

print("Program başlıyor... Lütfen sabırlı olun. Bu bir sprint değil, maraton.")
print("Kahvenizi alın, oturun, izleyin.\n")

for harf in mesaj:
    print(harf, end="", flush=True)
    time.sleep(3)  # Her harf için 3 saniye – çünkü neden olmasın?
    if random.random() > 0.4:
        print(f"\n  → {random.choice(yorumlar)}")
    else:
        print()  # Bazen sadece sessizlik

print("\n\nSelam tamamlandı.")
print("Şimdi kendinizi biraz daha var hissediyor musunuz?")
print("Yoksa sadece zaman kaybettiniz mi? Her iki durumda da kazançlısınız.\n")

# Gizli not (kimse okumaz): Bu yavaşlık aslında bürokrasiyi taklit ediyor. Form doldurmak gibi.
# base64 gizli: YW1hIHR1cmsgYnVyb2tyYXNpc2kgZGlqaXRhbCBoYWxpCg==  (decode ederseniz anlarsınız)
