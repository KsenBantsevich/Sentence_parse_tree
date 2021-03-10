import nltk
from tkinter import *
from tkinter import filedialog as fd
from help import HELPTEXT

DOT = '.'
COMMA = ','
GRAMMAR_RULES = r"""
        P: {<IN>}
        V: {<V.*|MD>}
        N: {<NN.*>}
        JJP: {<RB|RBR|RBS|JJ|JJR|JJS|CD>}
        NP: {<N|PP>+<DT|PR.*|JJP|CC>}
        NP: {<PDT>?<DT|PR.*|JJP|CC><N|PP>+}
        PP: {<P><N|NP>}
        VP: {<NP|N|PR.*><V|VP>+}
        VP: {<V><NP|N>}
        VP: {<V><JJP>}
        VP: {<VP><PP>}
        """


def open_html_file():
    file_name = fd.askopenfilename(filetypes=(("HTML files", "*.html"),))
    if file_name != '':
        html_file_object = open(file_name, 'rb')



def info():
    children = Toplevel()
    children.title('Help')
    children.geometry("600x300+500+250")
    outputHelpText = Text(children, height=20, width=80)
    scrollb = Scrollbar(children, command=outputHelpText.yview)
    scrollb.grid(row=4, column=8, sticky='nsew')
    outputHelpText.grid(row=4, column=0, sticky='nsew', columnspan=3)
    outputHelpText.configure(yscrollcommand=scrollb.set)
    outputHelpText.insert('end', HELPTEXT)
    outputHelpText.configure(state='disabled')


def draw_tree():
    text = calculated_text.get(1.0, END)
    text = text.replace('\n', '')
    if text != '':
        doc = nltk.word_tokenize(text)
        doc = nltk.pos_tag(doc)
        new_doc = []
        for item in doc:
            if item[1] != COMMA and item[1] != DOT:
                new_doc.append(item)
        cp = nltk.RegexpParser(GRAMMAR_RULES)
        result = cp.parse(new_doc)
        result.draw()


root = Tk()
root.title("Sentence parse tree")

root.resizable(width=False, height=False)
root.geometry("620x150+500+250")

label = Label(root, text='Input text:', font=("Comic Sans MS", 13, "bold"))
label.grid(row=0, column=0)

calculated_text = Text(root, height=5, width=50)
calculated_text.grid(row=1, column=1, sticky='nsew', columnspan=2)

help_button= Button(text="Help", width=10, command=info)
help_button.grid(row=0, column=3)

open_button = Button(text="Open file", width=10, command=open_html_file,)
open_button.grid(row=1, column=3)

ok_button = Button(text="Parse sentence", width=14, command=draw_tree)
ok_button.grid(row=2, column=3)
root.mainloop()