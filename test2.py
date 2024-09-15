print("Ich weiß alles über dich!")

dieDatei = open("schuelerDaten.can", "r")
zeile1 = dieDatei.read()[9]
zeile2 = dieDatei.read()
dieDatei.close()

print (zeile1)
print (zeile2)