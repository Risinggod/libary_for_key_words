dictionary={"Hallo": "Hi",
            "wellt":"World",
            "Auto": "Car",
            "Frau":"Woman",
            "Man":"mann",
            "Gefahr":"danger",
            "springen": "jump",
            "Rennen": "run",
            "ducken": "duck",
            "ente": "duck",
            }

while True:
    user_input1=input("geben sie ein wort ein was übersetzt werden soll")
    user_input2=input("fügen sie neue wörter dem wörterbuch hinzu")
    user_input3=input("geben sie die übersetzung an")
    user_input4=input("welches wort wollen sie löschen?")
    if user_input1 or user_input2 or user_input3 or user_input4 == "":
        break
    else:
        continue
    dictionary[user_input2] = user_input3
    print("Englisch:", dictionary[user_input1])
    dictionary.pop(user_input4)


















