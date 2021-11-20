from tkinter import *

root = Tk()
root.title("Book your trip")
root.geometry("500x300")
mainFrame = LabelFrame(root, text="", padx=20, pady=20)
mainFrame.pack(padx=10, pady=10)
mainLabel = Label(mainFrame, text="Book Your Trip").grid(row=1, column=1)

destinationlabel = Label(mainFrame, text="Destination: ").grid(row=2, column=0)
fromlabel = Label(mainFrame, text="From").grid(row=3, column=0)
fromEntry = Entry(mainFrame, width=15)
fromEntry.grid(row=3, column=1)
tolabel = Label(mainFrame, text="To").grid(row=3, column=2)
toEntry = Entry(mainFrame, width=15).grid(row=3, column=3)

numbertravellers = Label(mainFrame, text="No. of travellers ").grid(row=4, column=0, padx=(20, 0), pady=(10, 10))
travellersEntry = Entry(mainFrame, width=10).grid(row=4, column=1, pady=(10, 10))


#non-stop
nonstop = Checkbutton(mainFrame, text="Non-Stop").grid(row=5, column=0, padx=(40,0))

dateslabel = Label(mainFrame, text="Dates: ", justify=LEFT).grid(sticky="w", row=6, column=0, padx=(25,0))
fromdateslabel = Label(mainFrame, text="From").grid(row=7, column=0)
fromdatesEntry = Entry(mainFrame, width=15)
fromdatesEntry.grid(row=7, column=1)
todateslabel = Label(mainFrame, text="To").grid(row=7, column=2)
todatesEntry = Entry(mainFrame, width=15).grid(row=7, column=3)

searchButton= Button(mainFrame, text="Search")
searchButton.grid(row=8, column=1, pady=(10,10))

root.mainloop()
