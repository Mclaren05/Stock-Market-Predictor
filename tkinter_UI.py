from tkinter import *
window = Tk()

window.minsize(1024,768)
window.maxsize(1024,768)
window.title("Hacksprint_ps05_WickedTrojans")

dayValue = IntVar()

def get_prediction_data():
	try:
		day = int(day_entry.get())
		if(day <= 10 and day >= 1):
			print(day)

	except ValueError:
		Errorbox.config(text = "Enter a number between 1 to 10")





stock_title_label = Label(window, text = "Bajaj Stock Prediction Model", font = ("Times", 30)).grid(row = 0, column = 0)
enter_day_label = Label(window, text = "Enter the day you want the stock prediction", font =("Times", 20)).grid(row = 2, column = 0)
day_entry = Entry(window)
day_entry.grid(row =  2, column = 1)
prediction_button = Button(window, text = "Calculate", command = get_prediction_data, font = ("Times", 12)).grid(row = 3, column = 1)
Errorbox = Label(window)
Errorbox.grid(row = 1, column = 1)


window.mainloop()