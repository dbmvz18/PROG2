benutzereingabe = input("Welcher Eintrag soll gelöscht werden?: ")

dictfoodmanager =  {
  "Milch": "23.11.19",
  "Thunfisch": "04.02.20",
  "Hüttenkäse": "01.01.20",
  "Fleisch": "12.12.19"
}
del dictfoodmanager["Fleisch"]
print(dictfoodmanager)