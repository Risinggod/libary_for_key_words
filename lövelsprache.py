lövelsprache={"a":"alewa",
              "i":"ilewi",
              "e":"elewe",
              "o":"olewo",
              "u":"ulewu",
              "ä":"älewä",
              "ö":"ölewö",
              "ü":"ülewü"}

#while True:
user_input=input("schreiben sie ein wort was übersetzt werden soll")
user_input.find("a")

translated_string=""
for char in user_input:
    translated_char= lövelsprache.get(char)

    if translated_char==None:
        translated_string += char
    else:
        translated_string += translated_char

print("Löffelsprache: ", translated_string)



