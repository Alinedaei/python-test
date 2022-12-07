from itertools import cycle
import tkinter as tk
class App(tk.Tk):
    def __int__(self,image_files,x,y,delay):
        tk.Tk.__init__(self)
        self.geometry('+ {}+ {}'format(x,y))
        self.delay = delay
        self.pictures = cycle(tk.PhotoImage(file=image),image)
        for  image in image_files
            self.pictures_display = tk.Label(self)
            self.pictures_display.pack()

    def show__slides(self):
     img_object, img_name = next(self.pictures)
     self.pictures_display.config(image=img_object)
     self.title(img_name)
     self.after(self.delay,self.show__slides)
     def run(self):
         self.mainloop()

         delay = 3500

         image_files = [
             '1.gif',
            '2.gif',
             '3.gif',
             '4.gif',
             '5.gif',
             '6.gif',
             '7.gif',
         ]
    x =100
    y =50
    app = App(images_files,x,y,delay)
    app.show__slides()
    app.run()

