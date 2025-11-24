import pygame

#音声を再生する準備
pygame.mixer.init()

#音声ファイルを読み込む
pygame.mixer.music.load("beep.mp3")
#音声を再生する
pygame.mixer.music.play()
print("再生開始")
#再生終了を待つ
while pygame.mixer.music.get_busy():
	pygame.time.wait(100)

print("再生完了")