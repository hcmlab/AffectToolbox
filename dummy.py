import cv2

# Kamera öffnen (0 für die Standardkamera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Fehler: Kamera konnte nicht geöffnet werden.")
    exit()

print("Drücke 'q', um das Programm zu beenden.")

while True:
    # Frame von der Kamera lesen
    ret, frame = cap.read()

    if not ret:
        print("Fehler: Kein Bild von der Kamera erhalten.")
        break

    # Frame anzeigen
    cv2.imshow('Kamera-Stream', frame)

    # Beenden bei Tastendruck 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Ressourcen freigeben
cap.release()
cv2.destroyAllWindows()
