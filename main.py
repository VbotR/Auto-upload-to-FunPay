import pyautogui as pg 


print("1920x1080 or 2560x1080 or 3440x1440")
size = input("Select your display resolution : ")
print("You have selected : ", size)
if size == ("1920x1080"):
    print(pg.alert(text = 'start?', title='Auto-upload-to-FunPay', button = 'Yes'))
    print ("[                    ] 0% ")
    pg.click(1414, 208)
    pg.moveTo(755, 320, duration = 0.2)
    pg.click(755, 320)
    pg.typewrite('product') # product title 
    pg.moveTo(742, 510, duration = 0.2)
    pg.click(742, 510)
    pg.typewrite('price') # product price
    pg.click(741, 657)
    pg.typewrite('30')
    pg.press('enter') 
    #print(pg.alert(text = 'start?', title='Auto-upload-to-FunPay', button = 'Yes'))
    print ("[==========          ] 50%")
    pg.moveTo(1414, 208, duration = 0.2)
    pg.click(1414, 208)
    pg.moveTo(755, 320, duration = 0.2)
    pg.click(755, 320)
    pg.typewrite('product') # product title 
    pg.moveTo(742, 510, duration = 0.2)
    pg.click(742, 510)
    pg.typewrite('price') # product price
    pg.click(741, 657)
    pg.typewrite('30')
    pg.press('enter') 
    print ("[====================] 100%")
else:
    print("In development")
