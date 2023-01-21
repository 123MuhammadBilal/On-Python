from playsound import playsound
import pyautogui

print("____________________________UBL____________________________\n____________________________UNITED BANK LIMITED____________________________")
password1="1225"
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
  print("____________________________WELLCOM IN UBL SERVICES____________________________\n")
else:
    exit("____________________________ACCOUNT TEMPORARY BLOCKED____________________________\n")









#import pyautogui
#print("_________UBL_______\n__UNITED BANK LIMITED__")
#password_a="1225"
#password_b= pyautogui.password ("ENTER PASSWORD")
#if password_a == password_b:
#   pass
#elif password_a != password_b:
#    print("WRONG PASSWORD!")
#password_b= pyautogui.password ("TRY AGAIN")
#if password_a == password_b:
#    print("WELLCOM IN UBL SERVICES")
#else:
#    print("ACCOUNT TEMPORARY BLOCKED")
#    exit("WARNING! ACCOUNT TEMPORARY BLOCKED")



custumer_a ="bilal"
custumer_b = pyautogui.password ("USER NAME")
account_a ="345232-234-540633"
account_b = pyautogui.password ("ENTER ACCOUNT NUMBER")
amount= pyautogui.password ("ENTER AMOUNT")

if custumer_a == custumer_b :
    pass
elif custumer_a != custumer_b :
    print("TRY AGAIN PLEASE")
    

if (custumer_a == custumer_b , account_a==account_b):
    print(f"WELLCOM IN UBL SERVICES\n DEAR {custumer_b}\n RS {amount} \n TRANSFER SUCCESSFULY\n THANK YOU.")
else:
    exit("USER NAME OR ACCOUNT NUMBER IS WRONG")
    



#custumer_b= pyautogui.password ("USER NAME")
#account_b= pyautogui.password ("ENTER ACCOUNT NUMBER")
#amount_b= pyautogui.password ("ENTER AMOUNT")
#password_b= pyautogui.password ("ENTER PASSWORD")
