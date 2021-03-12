from tkinter import *
import keyboard
import os.path


#Labels
def showDeathCount():
    DEATH_COUNTER = 'Death count: '
    count = ''
    file_path = 'death.txt'
    exist = os.path.exists(file_path)
    

    if not exist:
        with open(file_path, 'w') as file:
            file.write('0')
            count = Label(window, text=f'{DEATH_COUNTER}0', font='Arial 12')
            count.place(relwidth=1, y=20)
    else:
        with open(file_path, 'r') as file:
            count = Label(window, text=f'{DEATH_COUNTER}{file.read()}', font='Arial 12')
            count.place(relwidth=1, y=20)


#Buttons
def addButtons():
    reset_button = Button(text='Reset', command=resetButtonHandler)
    reset_button.place(width=58, height=30, relx=0.5, rely=0.5, anchor='c')


#Keyboard Handlers
def addDeath():
    readed = ''
    with open('death.txt', 'r') as file:
        readed = file.read()
        readed = int(readed)
        readed += 1
        readed = str(readed)
    with open('death.txt', 'w') as file:
        file.write(readed)
    showDeathCount()
def removeDeath():
    readed = ''
    with open('death.txt', 'r') as file:
        readed = file.read()
        readed = int(readed)
        readed -= 1
        if readed < 0:
            return
        else:
            readed = str(readed)
        with open('death.txt', 'w') as file:
            file.write(readed)
        showDeathCount()


#Buttons Handlers
def resetButtonHandler():
    with open('death.txt', 'w') as file:
        file.write('0')
    showDeathCount()


#KeyboardListeneraa
keyboard.add_hotkey('up', addDeath) 
keyboard.add_hotkey('down', removeDeath)
keyboard.add_hotkey('-', resetButtonHandler)


#Init
window = Tk()
window.title('Death Counter')
window.geometry('300x150')
window.iconbitmap('icon.ico')


showDeathCount()
addButtons()


window.mainloop()