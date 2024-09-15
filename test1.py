# Begrüßung durch Computer
# Abfrage des Namens
# Ausgabe: "Hallo" + Name

print ("Hallo!")
deinName = input ("Wie heißt du? ")
print ("Hallo, " + deinName)

deinAlter = input ("Wie alt bist du? ")
print ("Soso! Schon " + deinAlter + " Jahre!")

print ("Ich merke mir das mal... ")
dieDatei = open('schuelerDaten.can','w')
dieDatei.write("derName " + deinName + "\n")
dieDatei.write("dasAlter " + deinAlter)
dieDatei.close()