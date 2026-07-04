from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import showerror
from errors import Errors

OpenPath = None

def openfile(textbox):
    global OpenPath
    OpenPath = askopenfilename()
    if OpenPath:
        try:
            with open(OpenPath, "r", encoding="utf-8") as f:
                textbox.delete("1.0", "end")
                textbox.insert("1.0", f.read())
        except FileNotFoundError:
            showerror(f'kPad {Errors.FILENOTFOUND}', f'File {OpenPath} was not found.')
        except PermissionError:
            showerror(f'kPad {Errors.IOPERMISSIONDENIED}', f'You do not have permission to open {OpenPath}.')
        except UnicodeDecodeError:
            showerror(f'kPad {Errors.BADENCODING}', 'The file has bad encoding. Please check the encoding and verify that the file is not a binary.')
        except OSError as e:
            showerror(f'kPad {Errors.OSERROR}', f'File opening failed with error {e}')


def saveAs(textbox):
    global OpenPath
    SaveAsPath = asksaveasfilename()
    if SaveAsPath:
        try:
            with open(SaveAsPath, "w", encoding="utf-8") as f:
                f.write(textbox.get('1.0', 'end-1c'))
                OpenPath = SaveAsPath
        except PermissionError:
            showerror(f"kPad {Errors.IOPERMISSIONDENIED}", f"You do not have permission to write {OpenPath}")
        except OSError as e:
            if getattr(e, "errno", None) == 28:
                showerror(f"kPad {Errors.DISKFULL}", f"The disk is full.")
            else:
                showerror(f"kPad {Errors.UNKNOWNWRITEERROR}", f"File writing failed with error {e}")


def save(textbox):
    global OpenPath
    if OpenPath:
        try:
            with open(OpenPath, "w", encoding="utf-8") as f:
                f.write(textbox.get('1.0', 'end-1c'))
        except PermissionError:
            showerror(f"kPad {Errors.IOPERMISSIONDENIED}", f"You do not have permission to write {OpenPath}")
        except OSError as e:
            if getattr(e, "errno", None) == 28:
                showerror(f"kPad {Errors.DISKFULL}", f"The disk is full.")
            else:
                showerror(f"kPad {Errors.UNKNOWNWRITEERROR}", f"File writing failed with error {e}")
    else:
        saveAs(textbox=textbox)