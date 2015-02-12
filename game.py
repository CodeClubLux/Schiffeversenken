from tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
	height=0
	width=0
	
	def __init__(self,parent,**kwargs):
		print("Init Resizing Canvas")
		Canvas.__init__(self,parent,**kwargs)
		self.bind("<Configure>", self.on_resize)
		self.height = self.winfo_reqheight()
		self.width = self.winfo_reqwidth()
		print("Init Resizing Canvas, ",self.winfo_reqwidth(),self.winfo_reqheight())

	def on_resize(self,event):
		print("on_resize(), ",event.width, event.height)
		## determine the ratio of old width/height to new width/height
		wscale = float(event.width)/self.width
		hscale = float(event.height)/self.height
		self.width = event.width
		self.height = event.height
		# resize the canvas 
		self.config(width=self.width, height=self.height)
		# rescale all the objects tagged with the "all" tag
		self.scale("all",0,0,wscale,hscale)
#-------------------------------------------------------------------------



window = Tk()

frame_1 = Frame(window, width=100, height=140, bg = 'dark blue')
frame_2 = Frame(window, width=100, height=200, bg = 'blue')
frame_3 = Frame(window, width=100, height=100, bg = 'light blue')
canvas_21 = ResizingCanvas(frame_2, width=50, height=50, bg = 'dark red',highlightthickness=0)
canvas_22 = Canvas(frame_2, width=50, height=50, bg = 'red')

frame_1.grid(row=0, column=0, sticky=W+E)
frame_2.grid(row=1, column=0, sticky=N+W+S+E)
frame_3.grid(row=10, column=0, sticky=N+W+S+E)
canvas_21.grid(row=0, column=0, padx=0, pady=0, sticky=N+W+S+E)
canvas_22.grid(row=0, column=1, padx=0, pady=0, sticky=NE+SW)

xmax= 3
ymax= 3

canvas_21.create_line(0,0,20,30)
canvas_21.create_rectangle(20,20,40,50,fill="white")

#for y in range(ymax):
#	print("Y=",y)
#	for x in range(xmax):
#		print("        X=",x)
#		btn = Button(frame_21)
#		btn.grid(column=x, row=y, sticky=N+S+W+E)
#	print("-----")
#for y in range(ymax):
#	frame_21.grid_rowconfigure(y,weight=1)
#for x in range(xmax):
#	frame_21.grid_columnconfigure(x,weight=1)


#for y in range(ymax):
#	print("Y=",y)
#	for x in range(xmax):
#		print("        X=",x)
#		btn = Button(frame_22)
#		btn.grid(column=x, row=y, sticky=N+S+W+E)
#	print("-----")
#for y in range(ymax):
#	frame_22.grid_rowconfigure(y,weight=1)
#for x in range(xmax):
#	frame_22.grid_columnconfigure(x,weight=1)



window.grid_columnconfigure(0,weight=1)
window.grid_rowconfigure(1,weight=1)
frame_2.grid_rowconfigure(0, weight=1)
frame_2.grid_columnconfigure(0, weight=1)
frame_2.grid_columnconfigure(1, weight=1)

# mainloop
window.mainloop()
