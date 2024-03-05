from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ctypes
from functools import partial
from json import loads, dumps
ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = Tk()
root.geometry('600x600')
AppTitle = 'Text Editor'
root.title(AppTitle)

FilePath = None
InitialDir = '.'
ValidFileTypes = (
    ('Text Editor', '*.te'),
    ('all files', '*')
    )
FontName = 'Banschrift'
padding = 60
document = None
DefaultContent = {
    "content":'',
    "tags":{
        'bold':[(),()]
        }
    }

def rgbToHex(rgb):
    return '%02x%02x%02x' % rgb

TagTypes = {
    #Настройки шрифта
    'Bold':{'font':f'{FontName} 15'},
    'Italic':{'font':f'{FontName} 25'},
    'Code':{'font': 'Consolas 15', 'background': rgbToHex((200, 200, 200))},
    #Размеры
    'NormSize':{'font':f'{FontName} 15'},
    'LarSize':{'font':f'{FontName} 25'},
    'XLargSize':{'font':f'{FontName} 35'},
    #цвет фона
    'Higlight':{'background':rgbToHex((255,255,0))},
    'Highlight Red':{'background':rgbToHex((255, 0, 0))},
    'Highlight Green':{'background':rgbToHex((0, 255, 0))},
    'Highlight Black':{'background':rgbToHex((0,0,0))},
    #Цвет текста
    'Text White':{'foreground': rgbToHex((255, 255, 255))},
    'Text Grey':{'foreground': rgbToHex((200, 200, 200))},
    'Text Blue':{'foreground': rgbToHex((0, 0, 255))},
    'Text Green':{'foreground': rgbToHex((0, 255, 0))},
    'Text Red':{'Foreground': rgbToHex((255, 0, 0))}
    }

TextArea = Text(root, font=f'{FontName} 15', relief=FLAT)
TextArea.pack(fill=BOTH, expand=TRUE, padx=padding, pady = padding)



root.mainloop()