from tkinter import *
root = Tk()
root.title('Test canvas')
root.geometry("500x500")


my_label = Label(root, text = "Hello world I love Pie!")
my_canvas = Canvas(root, width=200, height=200, bg="white")

my_canvas.create_rectangle(0,50,100,100, fill="green")

my_canvas.create_line(0,100,300,100, fill="red")
my_canvas.create_line(100,0,100,200, fill="red")
my_canvas.create_line(50,00,50,200, fill="red")



my_label.pack()
my_canvas.pack()

root.mainloop()