import time

def get_time_input():
    while True:
        try:
            minutes = int(input("Geri sayım süresini dakika olarak girin: "))
            seconds = int(input("Geri sayım süresini saniye olarak girin: "))
            if minutes < 0 or seconds < 0 or seconds >= 60:
                print("Geçersiz giriş. Dakika ve saniye pozitif olmalı ve saniye 60'tan küçük olmalı.")
            else:
                return minutes, seconds
        except ValueError:
            print("Geçersiz giriş. Lütfen sayıları doğru formatta girin.")

def countdown(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Geri sayım: {time_format}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print("Geri sayım tamamlandı!")

def main():
    print("Zamanlayıcıya hoş geldiniz!")
    minutes, seconds = get_time_input()
    countdown(minutes, seconds)

if __name__ == "__main__":
    main()
