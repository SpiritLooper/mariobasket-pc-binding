from pynput import mouse
from os import _exit as exit

second_clic = False
first_clic = None

def on_click(x, y, button, pressed):
    global second_clic, first_clic
    if button == mouse.Button.left and pressed :
        if not second_clic:
            second_clic = True
            first_clic = (x,y)
        else:
            f = open("rect.txt", "w")
            f.write(str(first_clic))
            f.write('\n')
            f.write(str((x,y)))
            f.close()
            exit(0)

if __name__ == '__main__':
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()