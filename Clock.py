from time import strftime, localtime

root = Tk()
root.geometry("1920x1080")
root.title("Clock")
frame = Frame(root, width=1920, height=1080)
frame.pack()

str = StringVar()
label = Label(frame, textvariable=str, font=('Calibri', 100), anchor='center', padx=30, pady=200, fg='blue')

str.set('Digital Clock')
label.pack()

str2 = StringVar()
label2 = Label(frame, textvariable=str2, font=('Calibri', 45), anchor='center', fg='blue', justify='left')
str2.set(strftime("%A, %B %d, %Y %H:%M:%S", localtime()))
label2.pack()

t = True

def pause():
    global t
    if t is True:
        t = False
        button.configure(bg='green', text='Resume')
    else:
        t = True
        button.configure(bg='red', text='Stop')
        time()
    return t

def time():
    global t
    if t is True:
        str2.set(strftime("%A, %B %d, %Y %H:%M:%S", localtime()))
        label.after(1000, time)
    else:
        return


button = Button(frame, bg='red', width=30, font=('Calibri', 16), height=10, text='Stop', fg='white', command=pause)
button.pack()
time()

root.mainloop()
