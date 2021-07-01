from tkinter import *
import tkinter
from tkinter import scrolledtext
from datetime import datetime


# Start Button activating function
def activate_form():
    start_time = datetime.now()
    global start_time_minute
    start_time_minute = int(start_time.strftime("%M"))
    global start_time_sec
    start_time_sec = int(start_time.strftime("%s"))
    text_area.focus()
    text_area.delete('1.0', END)





def submit():
    end_time = datetime.now()
    end_time_minute = int(end_time.strftime("%M"))
    end_time_sec = int(end_time.strftime("%s"))
    difference_minute = end_time_minute - start_time_minute
    difference_sec = end_time_sec - start_time_sec
    difference = (difference_minute * 60) + difference_sec

    cur_inp = list(text_area.get("1.0", tkinter.END))
    letters = ""
    for letter in cur_inp:
        letters += letter
    letters = list(letters.split(" "))
    sum_letters = 0
    total_letters = len(letters)
    
    for letter in cur_inp:
        sum_letters += len(letter)
    one_minute_time = difference / 60
    wpm = total_letters / one_minute_time
    for widgets in frame.winfo_children():
      widgets.destroy()
    heading = Label(frame, text='Typing Speed Tester', font=('Arial', 24, 'bold'))
    heading.grid(column=1, row=0)

    photo_image_result = PhotoImage(file="img.png")
    photo_image_result = Label(frame, image=photo_image_result)
    photo_image_result.grid(row=1, column=1)
    wpm = Label(frame, text=f"WPM: {round(wpm)}", font=("Arial", 24, 'normal'))
    wpm.grid(column=1, row=2, padx=100, pady=20)
    cpm = Label(frame, text=f"CPM: {round(sum_letters)}", font=("Arial", 24, 'normal'))
    cpm.grid(column=2, row=2, padx=100, pady=20)
    
    
window = Tk()
window.title('Typing speed tester built by RNTejas')
window.minsize(width=600, height=500)
frame = Frame(window)
frame.grid(column=0, row=0)

name_var=StringVar()
passw_var=StringVar()

heading = Label(frame, text='Typing Speed Tester', font=('Arial', 24, 'bold'))
heading.grid(column=1, row=0)

photo_image = PhotoImage(file="img.png")
label = Label(frame, image=photo_image)
label.grid(row=1, column=1)
sample_text = Label(frame, text="fast teach differ start now give for many air has strong object age farm know looks low size"
                         " been", font=("Arial", 14, 'normal'))
sample_text.grid(column=1, row=2, padx=100, pady=20)


text_area = scrolledtext.ScrolledText(frame, wrap=WORD,
                                      width=40, height=8,
                                      font=("Arial", 15))
text_area.insert(INSERT, "Please click 'Start Test' button")
text_area.grid(column=1, row=3, pady=10, padx=10)

start_btn = Button(frame, text='Start Test', bd='5', width=20, command=activate_form)
start_btn.grid(row=4, column=1)

submit_btn = Button(frame, text='Submit Test', bd='5', width=20, command=submit)
submit_btn.grid(row=5, column=1)


window.mainloop()


