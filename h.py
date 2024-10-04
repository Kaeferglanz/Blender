#!/bin/python

"""
With this program one is able to easily copy multiple pages via screenshots automatically.
The program requires the user to have pyautogui installed. This can be done with the following command:
pip install pyautogui
Running the program gives the user the screen dimensions in x and y coordinates. It wil later open up the
windows sniping tool. Thus the user will be prompted to put the cursor to the position where the program
is supposed tp start, afterwards he must to the same for the end point of the program. Last but not least,
the user must input how many pages he wants to coppy. The screenshots will be stored under
 C:/user/username/pictures/screenshots.
"""
import pyautogui

#prints screen dimensions in x and y coordinates
s=pyautogui.size()
print(s)

#logs position of mouse-cursor at current coordinates after 5 seconds and after user confirmed that the program can run
#cooridnates are refernece for beginning of page

print("Positioniere deine Maus am oberen linken Ende der Seite.")
print("Zeiger ist an gewünschter Stelle? (Y)")
p = input(">>> ")

if p == "Y" :
    pyautogui.sleep(5)
    global beginning_position
    beginning_position = pyautogui.position()
    print("Fertig")

#logs position of mouse-cursor at current coordinates after 5 seconds and after user confirmed that the program can run;
#coordinates are refernece for end of page

print("Positioniere deine Maus am unteren rechten Ende der Seite.")
print("Zeiger ist an gewünschter Stelle? (Y)")
p = input(">>> ")

if p == "Y" :
    pyautogui.sleep(5)
    global end_position 
    end_position = pyautogui.position()
    print("Fertig")

#number of pages that the user wants to coppy

print("Wie viele Seiten möchtest du fotografieren?")
anzahl = int(input(">>>"))

#saves where the buttons to move one page is located
print("Positioniere deine Maus über dem Knopf zum umblättern der Seite.")
print("Zeiger ist an gewünschter Stelle? (Y)")
p = input(">>> ")

if p == "Y" :
    pyautogui.sleep(5)
    global button
    button = pyautogui.position()
    print("Fertig")

#the program will automatically make pictures of the page with the given coordinates 
z = 1
while z <= anzahl:
    z += 1
    pyautogui.sleep(2)
    pyautogui.moveTo(beginning_position, duration=0)
    pyautogui.hotkey("win", "shift", "s")
    pyautogui.sleep(1)
    pyautogui.dragTo(end_position, duration=0)
    pyautogui.sleep(0.5)
    pyautogui.click(button)
