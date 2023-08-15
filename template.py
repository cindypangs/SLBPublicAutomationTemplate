import pyautogui
from time import sleep
from datetime import datetime
from datetime import date

PAUSE=2

def click():
    pyautogui.moveTo(x,y)
    pyautogui.click(x,y)
    sleep(2)


# Replace the (x,y) with the corrdinates of your mouse



# Move mouse to a location and click on it
pyautogui.moveTo(x,y)
pyautogui.click(x,y,button='left')

# Move mouse to a location and right click on it
pyautogui.moveTo(x,y)
pyautogui.click(x,y,button='right')

# Move mouse to a location and double click on it
pyautogui.moveTo(x,y)
pyautogui.doubleClick(x,y,button='left')

# Move mouse to a location and triple click on it
pyautogui.moveTo(x,y)
pyautogui.tripleClick(x,y,button='left')

# Press two keys at once (eg. alt and space)
pyautogui.hotkey('alt', 'space')
pyautogui.hotkey()

# Hold keys at once (eg. shift, ctrl, v)
pyautogui.keyDown('shift', 'ctrl', 'v')
pyautogui.sleep(2)
pyautogui.keyUp

# for loop to press the down key 4 times
for i in range(4):
    pyautogui.press('down')
pyautogui.press('enter')

# Drag from point (x,y) to point (a,b)
pyautogui.moveTo(x,y)
pyautogui.mouseDown()
pyautogui.dragTo(a,b,5)
pyautogui.moveRel(0,0,2)
pyautogui.mouseUp()

#________________________________________________________________________ ADVANCED FOR EXPERIENCED USERS __________________________________________________________________#

# Replace the .png files with your screenshots of the month and day you're looking for. Maake sure they are saved in the same location as this template file. Also make sure it is named the same as below. Eg. name the 
# screenshot of the first month Jan as shown on line 258



# Select a day

search_powerBI_date = (x_starting_point, y_starting_point, horizontal_length, vertical_length) # Replace these values that suits you. This will be the region you're searching the day of the month for.

def check_date(): # ```check_date()``` is your function name. Call this function when you want to search for the day

    day = datetime.now().day # Get today's day

    if day == 1:
        x, y = pyautogui.locateCenterOnScreen('1.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)

    elif day == 2:
        x, y = pyautogui.locateCenterOnScreen('2.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 3:
        x, y = pyautogui.locateCenterOnScreen('3.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 4:
        x, y = pyautogui.locateCenterOnScreen('4.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 5:
        x, y = pyautogui.locateCenterOnScreen('5.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 6:
        x, y = pyautogui.locateCenterOnScreen('6.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 7:
        x, y = pyautogui.locateCenterOnScreen('7.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 8:
        x, y = pyautogui.locateCenterOnScreen('8.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 9:
        x, y = pyautogui.locateCenterOnScreen('9.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 10:
        x, y = pyautogui.locateCenterOnScreen('10.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 11:
        x, y = pyautogui.locateCenterOnScreen('11.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 12:
        x, y = pyautogui.locateCenterOnScreen('12.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 13:
        x, y = pyautogui.locateCenterOnScreen('13.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 14:
        x, y = pyautogui.locateCenterOnScreen('14.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 15:
        x, y = pyautogui.locateCenterOnScreen('15.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 16:
        x, y = pyautogui.locateCenterOnScreen('16.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 17:
        x, y = pyautogui.locateCenterOnScreen('17.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 18:
        x, y = pyautogui.locateCenterOnScreen('18.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 19:
        x, y = pyautogui.locateCenterOnScreen('19.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 20:
        x, y = pyautogui.locateCenterOnScreen('20.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 21:
        x, y = pyautogui.locateCenterOnScreen('21.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 22:
        x, y = pyautogui.locateCenterOnScreen('22.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 23:
        x, y = pyautogui.locateCenterOnScreen('23.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 24:
        x, y = pyautogui.locateCenterOnScreen('24.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 25:
        x, y = pyautogui.locateCenterOnScreen('25.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 26:
        x, y = pyautogui.locateCenterOnScreen('26.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 27:
        x, y = pyautogui.locateCenterOnScreen('27.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 28:
        x, y = pyautogui.locateCenterOnScreen('28.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 29:
        x, y = pyautogui.locateCenterOnScreen('29.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 30:
        x, y = pyautogui.locateCenterOnScreen('30.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)
        
    elif day == 31:
        x, y = pyautogui.locateCenterOnScreen('31.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        sleep(2)


# Select today's month
month = datetime.now().month 


if month == 1:
    try:
        x, y = pyautogui.locateCenterOnScreen('Jan.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 2:
    try:
        x, y = pyautogui.locateCenterOnScreen('Feb.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 3:
    try:
        x, y = pyautogui.locateCenterOnScreen('Mar.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 4:
    try:
        x, y = pyautogui.locateCenterOnScreen('Apr.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 5:
    try:
        x, y = pyautogui.locateCenterOnScreen('May.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 6:
    try:
        x, y = pyautogui.locateCenterOnScreen('Jun.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 7:
    try:
        x, y = pyautogui.locateCenterOnScreen('Jul.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 8:
    try:
        x, y = pyautogui.locateCenterOnScreen('Aug.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 9:
    try:
        x, y = pyautogui.locateCenterOnScreen('Sep.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 10:
    try:
        x, y = pyautogui.locateCenterOnScreen('Oct.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 11:
    try:
        x, y = pyautogui.locateCenterOnScreen('Nov.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

elif month == 12:
    try:
        x, y = pyautogui.locateCenterOnScreen('Dec.png', region = search_powerBI_date, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen")
    click()
    check_date()

else: 
    print("ERROR")
