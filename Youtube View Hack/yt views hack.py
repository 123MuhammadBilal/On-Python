import selenim
import webdriver
import time
import random

driver = webdriver.chrome('F:\\All Software\\chromedriver_win32\\chromedriver.exe')

videos = [
    'https://youtu.be/kEu5D52_z-0',
    'https://youtu.be/c4pwVUZNa7g',
    'https://youtu.be/z_Y-aEwrdG0',
    'https://youtu.be/kEu5D52_z-0',
    'https://youtu.be/c4pwVUZNa7g',
    'https://youtu.be/z_Y-aEwrdG0',
    'https://youtu.be/z_Y-aEwrdG0',
    'https://youtu.be/kEu5D52_z-0',
    'https://youtu.be/c4pwVUZNa7g',    
]

for i in range(10):
    print("running the video for {} time".format(i))
    random_video = random.randint(0,8)
    drive.get(videos[random_video])
    sleep_time = random.random.randint(18,20)
    time.sleep(sleep_time)
drive.quit()