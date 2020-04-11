from tkinter import Label, Tk, mainloop, Scale, HORIZONTAL, X
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageEnhance, ImageTk

class ImageEnhancer():
    def __init__(self):
        self.root = Tk()
        self.original_image = Image.open(askopenfilename())
        self.current_brightness = 1
        self.current_contrast = 1

    def contrast_slider_callback(self, new_value):
        self.current_contrast = (int(new_value)/100) * 2
        self.enhance_image()

    def brightness_slider_callback(self, new_value):
        self.current_brightness = (int(new_value)/100) * 2
        self.enhance_image()

    def enhance_image(self):
        contrast_enhancer = ImageEnhance.Contrast(self.original_image)
        contrast_output = contrast_enhancer.enhance(self.current_contrast)

        brightness_enhancer = ImageEnhance.Brightness(contrast_output)
        im_output = brightness_enhancer.enhance(self.current_brightness)

        enhanced_image = ImageTk.PhotoImage(im_output)
        self.img_lbl.configure(image=enhanced_image)
        self.img_lbl.image = enhanced_image
    
    def create_gui(self):
        self.img_lbl = Label(self.root, image=ImageTk.PhotoImage(master = self.root, image = self.original_image))
        contrast_scale = Scale(self.root, from_=0, to=100, label='Contrast', command=self.contrast_slider_callback, orient=HORIZONTAL)
        contrast_scale.set(50)
        brightness_scale = Scale(self.root, from_=0, to=100, label='Brightness', command=self.brightness_slider_callback, orient=HORIZONTAL)
        brightness_scale.set(50)

        contrast_scale.pack(fill=X)
        brightness_scale.pack(fill=X)
        self.img_lbl.pack(fill=X)

        self.root.mainloop()

if __name__ == '__main__':
    ImageEnhancer().create_gui()