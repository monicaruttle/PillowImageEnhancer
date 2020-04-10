from tkinter import Label, Tk, mainloop, Scale, HORIZONTAL, X
from PIL import Image, ImageEnhance, ImageTk

class ImageEnhancer():
    def __init__(self):
        self.original_image = Image.open('data.tif')
        self.current_brightness = 1
        self.current_contrast = 1
        self.root = Tk()

        img = ImageTk.PhotoImage(self.original_image)  # PIL solution
        self.img_lbl = Label(self.root, image=img)

    def contrast_slider_callback(self, new_value):
        self.current_contrast = (int(new_value)/100) * 2
        self.render_image()

    def brightness_slider_callback(self, new_value):
        self.current_brightness = (int(new_value)/100) * 2
        self.render_image()

    def render_image(self):
        contrast_enhancer = ImageEnhance.Contrast(self.original_image)
        contrast_output = contrast_enhancer.enhance(self.current_contrast)

        brightness_enhancer = ImageEnhance.Brightness(contrast_output)
        im_output = brightness_enhancer.enhance(self.current_brightness)

        new_image = ImageTk.PhotoImage(im_output)
        self.img_lbl.configure(image=new_image)
        self.img_lbl.image = new_image
    
    def create_gui(self):
        contrast_scale = Scale(self.root, from_=0, to=100, command=self.contrast_slider_callback, orient=HORIZONTAL)
        contrast_scale.set(50)
        brightness_scale = Scale(self.root, from_=0, to=100, command=self.brightness_slider_callback, orient=HORIZONTAL)
        brightness_scale.set(50)

        contrast_scale.pack(fill=X)
        brightness_scale.pack(fill=X)
        self.img_lbl.pack(fill=X)

        self.root.mainloop()

ImageEnhancer().create_gui()
