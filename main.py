import customtkinter as ctk
from widgets import init_widget, init_menubar
from filelogic import openfile, saveAs

__version__ = "0.11"

def main():
    root = ctk.CTk()
    root.geometry("480x360")
    root.title(f"kPad {__version__}")

    textbox = ctk.CTkTextbox(root)

    init_menubar(root, textbox, version_label=__version__)

    textbox.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()