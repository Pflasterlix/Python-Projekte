# Funktion zur Berechnung des BMI
def bmi_berechnen(gewicht, groesse):
    bmi = gewicht / (groesse * groesse)
    return bmi

# Eingabe des Gewichts und der Größe durch den Benutzer
gewicht = float(input("Geben Sie Ihr Gewicht in Kilogramm ein: "))
groesse = float(input("Geben Sie Ihre Größe in Metern ein: "))

# Berechnung des BMI
bmi = bmi_berechnen(gewicht, groesse)

# Ausgabe des berechneten BMI-Werts
print("Ihr BMI beträgt:", bmi)