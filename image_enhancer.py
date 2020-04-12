import os

from tkinter import Label, Tk, mainloop, Scale, HORIZONTAL, X, ttk, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageEnhance, ImageTk

class ImageEnhancer():
    def __init__(self):
        self.root = Tk()
        image_path = askopenfilename()
        self.original_image = Image.open(image_path)
        self.original_image_directory = os.path.dirname(image_path)
        self.original_image_extension = os.path.splitext(image_path)[-1]

        # set max image size
        size = 500,500
        self.original_image.thumbnail(size, Image.ANTIALIAS)

        self.current_brightness = 1
        self.current_contrast = 1

    def contrast_slider_callback(self, new_value):
        self.current_contrast = (int(new_value)/100) * 2
        self.replace_image()

    def brightness_slider_callback(self, new_value):
        self.current_brightness = (int(new_value)/100) * 2
        self.replace_image()

    def replace_image(self):
        im_output = self.adjust_image(self.original_image)

        enhanced_image = ImageTk.PhotoImage(im_output)
        self.img_lbl.configure(image=enhanced_image)
        self.img_lbl.image = enhanced_image

    def adjust_image(self, original_image):
        contrast_enhancer = ImageEnhance.Contrast(original_image)
        contrast_output = contrast_enhancer.enhance(self.current_contrast)

        brightness_enhancer = ImageEnhance.Brightness(contrast_output)
        return brightness_enhancer.enhance(self.current_brightness)
    
    def apply_all(self):
        images_to_modify = [file for file in os.listdir(self.original_image_directory) if file.endswith(self.original_image_extension)]
        
        MsgBox = messagebox.askquestion('Modify images', f'Are you sure you want to replace {len(images_to_modify)} image(s) with new brightness/contrast settings?', icon = 'warning')
        if MsgBox == 'no':
            return
        
        for image_filename in images_to_modify:
            original_image_path = os.path.join(self.original_image_directory, image_filename)
            new_image = self.adjust_image(Image.open(original_image_path))
            new_image.save(original_image_path)
    
    def create_gui(self):
        self.img_lbl = Label(self.root, image=ImageTk.PhotoImage(master = self.root, image = self.original_image))
        contrast_scale = Scale(self.root, from_=0, to=100, label='Contrast', command=self.contrast_slider_callback, orient=HORIZONTAL)
        contrast_scale.set(50)
        brightness_scale = Scale(self.root, from_=0, to=100, label='Brightness', command=self.brightness_slider_callback, orient=HORIZONTAL)
        brightness_scale.set(50)
        apply = ttk.Button(self.root, text='Apply settings to all images in directory', command=self.apply_all)

        contrast_scale.pack(fill=X)
        brightness_scale.pack(fill=X)
        apply.pack(fill=X)
        self.img_lbl.pack(fill=X)

        self.root.mainloop()

if __name__ == '__main__':
    ImageEnhancer().create_gui()