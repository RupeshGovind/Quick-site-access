from tkinter import *
from PIL import Image,ImageTk
import webbrowser

def open_google():
    webbrowser.open("https://www.google.com")

def open_insta():
    webbrowser.open("https://www.instagram.com")

def open_facebook():
    webbrowser.open("https://www.facebook.com")

def open_linkedin():
    webbrowser.open("https://www.linkedin.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_telegram():
    webbrowser.open("https://web.telegram.org")

def open_github():
    webbrowser.open("https://www.github.com")

def open_wikipedia():
    webbrowser.open("https://www.wikipedia.org")

def open_chatgpt():
    webbrowser.open("https://chat.openai.com")

root = Tk()
root.geometry("620x620")
root.maxsize(620,620)
root.title("QuickSite Access")
photo = PhotoImage(file = "quckaccess.png")
root.iconphoto(False, photo)

images = []
for i in range(1, 10):
    image = Image.open(f"social{i}.png")
    resized_image = image.resize((200, 200)) 
    images.append(ImageTk.PhotoImage(resized_image))

f1 = Frame(root, bg="red")
f1.pack(fill=BOTH, expand=True)
Button(f1, text="Google",image=images[0],command=open_google).grid(row=0, column=0)
Button(f1, text="Instagram", image=images[1], command=open_insta).grid(row=0, column=1)
Button(f1, text="Facebook", image=images[2], command=open_facebook).grid(row=0, column=2)
Button(f1, text="LinkedIn", image=images[3], command=open_linkedin).grid(row=1, column=0)
Button(f1, text="YouTube", image=images[4], command=open_youtube).grid(row=1, column=1)
Button(f1, text="Telegram", image=images[5], command=open_telegram).grid(row=1, column=2)
Button(f1, text="GitHub", image=images[6], command=open_github).grid(row=2, column=0)
Button(f1, text="Wikipedia", image=images[7], command=open_wikipedia).grid(row=2, column=1)
Button(f1, text="ChatGPT", image=images[8], command=open_chatgpt).grid(row=2, column=2)

root.mainloop()