import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog

class Display:
    def __init__(self, master):
        self.master = master
        self.master.title("Background Image Display")

        # Load and resize the background image
        image = Image.open("images/background.jpg")
        image = self.resize_image(image, 800, 600)
        self.bg_image = ImageTk.PhotoImage(image)

        # Create a canvas and set the background image
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Create buttons
        self.display_button = tk.Button(self.master, text="Select and Display Image", command=self.display_new_image)
        self.display_button.place(relx=0.3, rely=0.95, anchor="center")

        self.display_specific_button = tk.Button(self.master, text="Display Specific Image", command=lambda: self.display_specific_image("images/specific_image.jpg"))
        self.display_specific_button.place(relx=0.7, rely=0.95, anchor="center")

        # Variable to store the new image
        self.new_image = None

    def display_new_image(self):
        try:
            file_path = filedialog.askopenfilename(
                title="Select Image",
                filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
            )
            
            if not file_path:
                return

            self.display_specific_image(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")

    def display_specific_image(self, file_path):
        try:
            # Load and resize the new image
            new_image = Image.open(file_path)
            new_image = self.resize_image(new_image, 200, 200)
            self.new_image = ImageTk.PhotoImage(new_image)

            # Display the new image in the middle column and top row
            self.canvas.create_image(400, 100, image=self.new_image, anchor="center")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")

    def resize_image(self, image, max_width, max_height):
        # Get original image size
        width, height = image.size

        # Calculate aspect ratio
        aspect_ratio = min(max_width/width, max_height/height)

        # Calculate new size
        new_width = int(width * aspect_ratio)
        new_height = int(height * aspect_ratio)

        # Resize image
        return image.resize((new_width, new_height), Image.LANCZOS)

if __name__ == "__main__":
    root = tk.Tk()
    app = Display(root)
    root.mainloop()