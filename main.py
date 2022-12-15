import textile
import tkinter as tk
import cssutils

def convertHtml():
    entree= saisie.get(1.0, "end-1c")
    html=textile.textile(entree)
    print("\n Conversion HTML : \n", html)
    insertion.config(text="Converti en Html : "+html)



#----------------------------------------------------- CSS Converter----------------------------------------


def convertCss():
    entree2= saisie.get(1.0, "end-1c")
    texte = 'color : blue; font-size : 12px;' # Exemple de texte a inserer
    style = cssutils.css.CSSStyleDeclaration(cssText=texte)
    print("\n Converti en CSS : \n", style.getCssText())
    insertion.config(text="Converti en CSS : "+style.getCssText())





#------------------------- Window creation -------------------------------------------

window = tk.Tk()
window.title("Text2Html")
window.config(padx=100, pady=50)
window.geometry("720x480")


#---------------------- Text-----------------------------------------------
saisie = tk.Text(window, height=5, width=52)
saisie.pack()
saisie.insert(tk.END, """""")



#---------------------- Button --------------------------------------------
b1 = tk.Button(window, text="Transcrire en HTML", command=convertHtml)
b1.pack()
b2 = tk.Button(window, text="Transcrire en CSS", command=convertCss)
b2.pack()


#---------------------- Label -----------------------------------------------
insertion=tk.Label(window,text="")
insertion.pack()



window.mainloop()



