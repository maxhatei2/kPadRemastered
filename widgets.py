import customtkinter as ctk
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from filelogic import openfile, saveAs, save

# Universal

def init_widget(parent, WidgetType, PackOptions):
    widget = WidgetType(parent)
    widget.pack(**(PackOptions))
    return widget

def show_about(parent, version_label):
    about = ctk.CTkToplevel(parent)
    about.title("About kPad")
    about.geometry("300x200")
    about.resizable(False, False)

    label = ctk.CTkLabel(
        about,
        text=f"kPad {version_label}. Made in CTk and Python."
    )
    label.pack(pady=30, padx=20)

def init_menubar(parent, textbox, version_label):
    menu = CTkMenuBar(parent)
 
    file_button = menu.add_cascade("File")
    help_button = menu.add_cascade("Help")

    file_dropdown = CustomDropdownMenu(widget=file_button)
    file_dropdown.add_option(option="Save", command=lambda: save(textbox=textbox))
    file_dropdown.add_option(option="Save As", command=lambda: saveAs(textbox=textbox))
    file_dropdown.add_option(option="Open", command=lambda: openfile(textbox=textbox))
    file_dropdown.add_option(option="Exit", command=parent.quit)

    edit_dropdown = CustomDropdownMenu(widget=help_button)
    edit_dropdown.add_option(option="About", command=lambda: show_about(parent=parent, version_label=version_label))
 
    return menu

