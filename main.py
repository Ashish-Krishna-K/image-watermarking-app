from tkinter import Button, Canvas, Entry, Tk, filedialog, messagebox

from PIL import Image, ImageDraw, ImageFont, ImageTk


class App:
    "a"
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Image Watermarking App")
        add_img_btn = Button(text="Choose a file to open", command=self.open_file)
        add_img_btn.pack()
        launch_popup_btn = Button(text="Add watermark", command=self.launch_popup)
        launch_popup_btn.pack()
        self.canvas = Canvas()
        self.canvas_img = self.canvas.create_image(0, 0, anchor="nw")
        self.canvas.pack()
        self.img = None
        self.photo = None
        self.popup = None
        self.text_input = None
        self.file_path = None

        self.window.mainloop()

    def load_img(self, file_path):
        "b"
        self.img = Image.open(file_path)
        self.photo = ImageTk.PhotoImage(self.img)
        self.canvas.config(width=self.img.width, height=self.img.height)
        self.canvas.itemconfigure(self.canvas_img, image=self.photo)

    def open_file(self):
        "c"
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.load_img(self.file_path)
            self.launch_popup()

    def launch_popup(self):
        "d"
        if self.img is None:
            messagebox.showwarning(
                "Image not opened", "Please open an image before trying that."
            )
            return
        self.popup = Tk()
        self.popup.title("Please input the text you want to use as watermark")
        self.text_input = Entry(master=self.popup)
        self.text_input.pack()

        confirm_btn = Button(
            master=self.popup, text="Confirm", command=self.add_watermark
        )
        confirm_btn.pack()
        cancel_btn = Button(master=self.popup, text="Cancel", command=self.cancel_input)
        cancel_btn.pack()

    def cancel_input(self):
        "e"
        if self.popup is not None:
            self.popup.destroy()

    def add_watermark(self):
        "f"
        if self.text_input is not None and self.img is not None:
            drawing = ImageDraw.Draw(self.img)
            fill_color = (255, 255, 255)
            text = self.text_input.get()
            font = ImageFont.load_default(size=50)
            x = self.img.width - 150
            y = self.img.height - 100
            pos = (x, y)
            drawing.text(xy=pos, text=text, fill=fill_color, font=font)
            self.img.save(self.file_path if self.file_path else "./edited.jpeg")
            self.load_img(self.file_path)
            if self.popup is not None:
                self.popup.destroy()


app = App()

app.open_file()
