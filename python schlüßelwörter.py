python_dic={ "if/else" : "verzweigung von bedingungen",
             "and" : "zwei bedingungen müßen erfühlt sein",
             "or" : "eine von zwei bedingugnen müßen erfühlt werden",
             "while": "einleten einer schleife mit einer bedingung",
             "for": "eine schleife mit einer bestimmten anzahl von wiederholungen",
             "in": "gibt die anzahl von wiederholungen von einer schleife wieder",
             "not": "wenn etwas nicht erfühlt werden darf",
             "import": "um externe medien wieder zu geben",
             "True": "wenn eine bedingung zutrieft",
             "False": "wenn eine bedingung nicht zutrieft",
             "breake": "beendet eine schleife",
             "continue": "läst eine schleife von vorne anfangen",
             "def" : "leitet eine Funktion ein",
             "None": "der wert wird als 0 festgelegt",
             "class": "wird benötigt um eine neue klasse zu defienieren",
             }

while True:
    user_input=input("von welchem schlüßelwort wollen sie die übersetzung")
    if user_input=="Exit":
        break
    else:
        print("die bedeutung ist:", python_dic[user_input])
        continue
