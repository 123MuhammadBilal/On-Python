from playsound import playsound
from selenium import webdriver
import pyautogui
import time


print("____________________________BK____________________________\n____________________________BILAL KING____________________________")
password1="mano1225"
password2=pyautogui.password("____________________________ENTER PASSWORD____________________________\n")
if password1 == password2:
    pass
elif password1 != password2:
    pass
    password2=pyautogui.password("____________________________TRY AGAIN____________________________\n")
elif password1 != password2:
    pass
    password2=pyautogui.password("____________________________TRY AGAIN____________________________\n")
elif password1 != password2:
    pass
    password2=pyautogui.password("____________________________TRY AGAIN____________________________\n")
else:
    pass
    password2=pyautogui.password("____________________________TRY AGAIN____________________________\n")
if password1 == password2:
  print("____________________________BK_____HACK_______KING____________________________\n")
else:
    exit("____________________________TEMPORARY BLOCKED____________________________\n")


no_of_driver = int(input("Enter NO Of Drivers"))
url = input("Enter URL: ")
time_to_refresh = int(input("Enter Refresh Rate In Seconds : "))
drivers = []
for i in range(no_of_driver):
    drivers.append(webdriver.chrome(executeable_path="chromedriver"))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(no_of_driver):
        drivers[i].refresh()
