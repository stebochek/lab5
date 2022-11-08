# дополнительное задание
import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk


def pic():
    url = requests.get('https://aws.random.cat/meow')
    url = url.json()
    url = url["file"]
    return url


def load_image():
    label.config(text='Котик загружается, ожидайте')
    root.update()
    try:
        response = requests.get(pic(), timeout=10)
    except requests.exceptions.Timeout:
        label.config(text='Время ожидания истекло...')
    else:
        if response.status_code != 200:
            label.config(text=f'HTTP error {response.status_code}')
        else:
            pil_image = Image.open(BytesIO(response.content))
            image = ImageTk.PhotoImage(pil_image)
            label.config(image=image, text='')

            label.image = image


root = tk.Tk()
root.title("Генератор котиков")
root.geometry("1920x1080")

tk.Button(root, text='Сгенерировать котика', command=load_image).pack()
label = tk.Label(root)
label.pack()

root.mainloop()
