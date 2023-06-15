from pytube import YouTube
import os

print("""                         
     ; 
     ;;
     ;';.
     ;  ;;
     ;   ;;    🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
     ;    ;;   🔥Shazam Uygulamasına Hoşgeldiniz🔥
     ;    ;;   🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
     ;   ;'
     ;  ' 
,;;;,; 
;;;;;;
`;;;;'
""")

while True:
    # URL girişi
    url = input("İndirmek istediğiniz müziğin linkini girin (0 girerek çıkabilirsin) >> ")
    
    if url == '0':
        break

    try:
        # YouTube video nesnesi oluşturma
        yt = YouTube(url)

        # Sadece sesi filtreleme
        video = yt.streams.filter(only_audio=True).first()

        # Dosyayı indirme
        out_file = video.download()

        # Dosyayı kaydetme ve adını değiştirme
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # Başarılı sonuç
        print(yt.title + " adlı dosya indirildi.")
    
    except Exception as e:
        print("Video indirme hatası:", str(e))

print("Program sonlandırıldı.")


