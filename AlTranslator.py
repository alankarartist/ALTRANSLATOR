from tkinter import *
from tkinter import ttk
from tkinter import font
from googletrans import Translator, LANGUAGES
import os 

cwd = os.path.dirname(os.path.realpath(__file__))

class AlTranslator():
    
    def __init__(self):
        root = Tk(className = " ALTRANSLATOR ")
        root.geometry("1080x400+820+615")
        root.resizable(0,0)
        root.iconbitmap(os.path.join(cwd+'\\UI\\icons', 'altranslator.ico'))
        root.config(bg = '#ffffff')

        appHighlightFont = font.Font(family='sans-serif', size=12, weight='bold')

        inputText = Text(root,font = appHighlightFont, height = 11, wrap = WORD, padx=5, pady=5, width=50, fg='#4877bc')
        inputText.place(x=20, y=100)
        outputText = Text(root,font = appHighlightFont, height = 11, wrap = WORD, padx=5, pady= 5, width=50, bg='#f8f9fb',fg='#4877bc')
        outputText.place(x=600, y=100)

        language = list(LANGUAGES.values())
        srcLang = ttk.Combobox(root, values=language, width=22, font=appHighlightFont)
        srcLang.place(x=20,y=60)
        srcLang.set('Source language')
        destLang = ttk.Combobox(root, values=language, width=22, font=appHighlightFont)
        destLang.place(x=840,y=60)
        destLang.set('Destination language')

        def gTranslate():
            translator = Translator()
            translated = translator.translate(text=inputText.get(1.0, END), src=srcLang.get().capitalize(), dest=destLang.get().capitalize())
            outputText.delete(1.0, END)
            outputText.insert(END, translated.text)

        trans_btn = Button(root, text = 'Translate',font=appHighlightFont, pady = 5, command = gTranslate , fg='#8e8d91', width=9, bg = '#ffffff', bd=0)
        trans_btn.place(x=490, y=180 )

        root.mainloop()

if __name__ == "__main__":
    AlTranslator() 