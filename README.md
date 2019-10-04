# Nahrungsmittelbestand mit Ablaufdatum

## Ausgangslage
Die Lebensmittelverschwendung ist nach wie vor ein heissdiskutiertes Thema auf unserem Planeten. Angeblich sollen 50% der produzierten Lebensmittel weggeworfen werden. Um im eigenen Haushalt etwas dagegen zu unternehmen, soll die folgende zu programmierende Applikation unterstützend zur Verfügung stehen. 

## Funktion/Projektidee
Sämtliche Nahrungsmittel werden unmittelbar nach dem Kauf erfasst (Dateneingabe). Hierbei stehen die Werte "Nahrungsmittel" und "Ablaufdatum" im Vordergrund. Somit werden die Nahrungsmittel gespeichert (Datenspeicherung). Zwei Tage vor Ablauf der erfassten Nahrungsmittel wird eine Benachrichtigung generiert (Datenausgabe) und mitgeteilt, welches "Nahrungsmittel" in zwei Tagen das Ablaufdatum erreichen wird. Folgerichtig kann der Konsument 

## Workflow

* Dateneingabe
Nahrungsmittel erfassen (evtl. mit Bild), Ablaufdatum erfassen

* Datenverarbeitung/-speicherung
Datenbank 1: erfasste Produkte
Datenbank 2: Serviervorschläge (Nahrungsmittel muss mind. 1x enthalten sein)
Programmierung: bspw. 2 Tage vor Erreichen des Ablaufdatums wird eine Push-Nachricht/Benachrichtigung (evtl. in Form einer E-Mail,…) ausgelöst, Serviervorschläge ausgeben
	
* Datenausgabe
Benachrichtigung (Push-Nachricht, E-Mail) mit Standard-Text und Ablaufdatum (und evtl. Serviervorschläge)


![Ablaufdiagramm](/Pfad/Ablaufdiagramm.jpg)