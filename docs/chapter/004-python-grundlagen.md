# Python - Grundlagen
Python ist eine Skriptsprache in der die Ausführung immer von oben nach unten erfolgt. Das heißt der Befehl in Zeile 1 wird normalerweise vor dem in Zeile 2 gemacht. 

## Ausgaben
Die zwei Möglichkeiten von Ausgaben sind: Die Ausgabe auf der Konsole oder im Terminal und die andere Möglichkeit wäre die Ausgabe innerhalb einer GUI (Grafische Oberfläche engl. Graphical User Interface) zu machen. Da wir allerdings aktuell nichts in einer GUI
machen wollen arbeiten wir mit einer Konsole und den Ausgaben innerhalb dieser. 

Eine Ausgabe kann in Python mit der Funktion `print()` erfolgen. Innerhalb der Klammern von print kommt der Text, die Zahlen oder aber die Variable die wir auf der Konsole ausgeben wollen. Hier ein paar Beispiele:

```python
print("Hallo")
print("Welt")
print("Hallo TKR")
print("Dies ist mal ein etwas längerer Satz")
print("Auch Zahlen können in einem Text stehen")
print(10)
print(meineVariable)
```

## Datentypen
Mittels eines Datentyps einer Variablen kann bestimmt werden, welche Werte diese Variable annehmen kann oder welche Operationen wir auf Sie anwenden können. 
So kann man auf Text die + Operation anwenden um Texte miteinander zu kombinieren und auf Zahlen 
 +,-,/ und *. Außerdem kann noch unterschieden Werden zwischen einem Float (Fließkommazahl) und einem Int (Ganzzahl)

## Kommentare
Kommentare sind in einem Programm Zeilen, die vom Computer nicht beachtet werden. Das heißt Sie werden bei der Ausführung einfach ignoriert. In Python kann man einen Kommentar schreiben, indem man eine Raute (#) vor einer Zeile packt.

```python
# Ich bin ein Kommentar
```

## Aufgaben
Hier sind ein paar Aufgaben, die du machen kannst um noch etwas weiter zu üben:

### Name Ausgeben
Erstelle ein Programm, das deinen Vorname, Nachname und dein Geburtsdatum auf der Konsole ausgibt.

> Zusatzaufgabe: Erweitere das Programm, so dass es zusätzlich noch deine Adresse und deine Telefonnummer auf der Konsole ausgibt. 

## Rechnen
Computer können nichts besser als rechnen, daher kann man auch in allen Programmiersprachen mit den Zahlen berechnungen anstellen.
Python stellt uns dafür verschiedene Operatoren zur Verfügung:

- &#43; (Pluszeichen) dient zur Addition
- &#45; (Minuszeichen) dient zur Subtraktion
- &#42; (Asteriks) dient zur Multiplikation
- / (Slash oder Schrägstrich) dient zur Division

Dabei muss man aber aufpassen mit welchen Datentyp man zu tun hat, denn je nachdem welcher Datentyp es ist 
stehen nur wenige oder alle Operatoren zur Verfügung. Es ist allerdings auch verstädnlich, dass man bei einem Text keine Division durchführen kann und das nur bei Zahlen geht.


## Aufgaben
Hier sind ein paar Aufgaben, die du machen kannst um noch etwas weiter zu üben. Nächste Woche bekommt ihr dann die Lösung dafür:

### Weitere Operatoren
Probiere die unten stehenden Operatoren mit verschiedenen Zahlen aus und notiere dir, was sie tun. Setze für x und y verschiedene Zahlen ein, bis du herausgefunden hast, was die Operatoren tun.

```python
x + y
x - y
x * y
x / y
x ** y
x // y
x % y
```

> In der nächsten PDF werden diese Operatoren natürlich oben ergänzt, so dass ihr auch eine Erklärung habt.



### Was gibt das Programm aus?
Was ist der Rückgabewert des unten stehenden Programms? Gehe es zuerst im Kopf durch und probiere es anschliessend aus, in dem du das Programm mit PyCharm in einer neuen Datei abspeicherst.

```python
x = 2
y = 3
z = x + y
x = z
y = x
print(x)
print(y)
print(z)
```

### Zeit umrechnen
Schreibe ein Programm, welches eine Zeitangabe in Stunden, Minuten und Sekunden in die Anzahl Sekunden insgesamt umrechnet

### Werkstatt kosten
Eine Werkstatt verlangt für die Benützung einer Maschine eine Grundgebühr von 60 Franken sowie 35 Fanken pro Stunde. Man überlege sich, welche Daten einzugeben und wel che Daten zu berechnen sind und erstelle ein passendes Programm.

### Leihwagen kosten
Ein Kleinunternehmen stellt seinen Kunden für Tran sporte einen Lieferwagen und einen Lastwagen zur Verfügung. Für Transporte mit dem Lieferwagen werden Fr. 1.60 pro Kilometer verrechnet, für den Lastwagen beträgt der Tarif Fr. 2.80 pro Kilometer. Welche Gebühr hat ein Kunde zu bezahlen, wenn der Lieferwagen 85 km und der Lastwagen 120 km zurückgelegt hat?

### Der Weinhändler
Ein Weinhändler verkauft Rotwein zu 18 Franken pro Flasche, Roséwein zu 13 und Weisswein zu 12 Franken pro Flasche. Ein Kunde bestellt (beispielsweise) 12 Flaschen Rotwein, 6 Flaschen Rosé und 24 Flaschen Weisswein. Schreibe ein Programm, welches den Gesamtpreis berechnet.

### Temperatur umrechnen
Schreibe ein Programm, das Temperaturen in verschiedene Skalensystemen ineinander umwandelt. Das Programm soll zu Beginn eine Auswahl mit den verschiedenen Möglichkeiten anbieten:

- Umrechnung von Celsius nach Kelvin
- Umrechnung von Celsius nach Fahrenheit
- Umrechnung von Kelvin nach Celsius
- Umrechnung von Kelvin nach Fahrenheit
- Umrechnung von Fahrenheit nach Celsius
- Umrechnung von Fahrenheit nach Kelvin

>Dies kann dir sicher helfen.
>- Celsius = 5/9 * (Fahrenheit - 32).
>- Celsius = Kelvin - 273.15.
>- Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K.


## Fallunterscheidung
Eine Fallunterscheidung dient dazu zwischen zwei Zuständen zu unterscheiden und verschiedenen Code für die Zustände auszuführen.
Als Beispiel möchte man z.B. zusätzlichen Code ausführen wenn jemand über 18 ist (z.B. Zugang zu einer Webseite). Auch in der realen Welt gibt es natürlich auch Fallunterscheidungen die wir intuitiv fällen. So gibt es z.B. die Möglichkeit sich wenn es kalt ist eine Jacke anzuziehen.

In der Programmierung ist es allerdings nicht ganz so einfach mit den Bedingungen. Hier muss jede Bedingung nach WAHR oder FALSCH beurteilt werden können. Diese Werte WAHR oder FALSCH werden auch als boolsche Werte bezeichnet. Für diese Aussagen (boolsche Bedingung => Eine Bedingung die nach einer boolschen Wert auswertbar ist) stehen uns folgende Operatoren zur Verfügung:

| Operator | Wort | Beispiel  |
|----------|----------------|-----------|
| >        | größer         | 5 > 10  5 ist kleiner als 10 (WAHR)                                                                                          |
| <        | kleiner        | 10 < 5  10 ist kleiner als 5 (FALSCH)                                                                                        |
| >=       | größer gleich  | 16 >= 17  16 ist größer oder gleich 17 (FALSCH)                                                                                |
| <=       | kleiner gleich | 16 <= 16  16 ist kleiner oder gleich 16 (WAHR)                                                                                 |
| !=       | nicht gleich   | 0 != 1  0 ist nicht gleich 1 (WAHR)                                                                                          |
| ==       | gleich         | 1 == 1  1 ist gleich 1 (WAHR)                                                                                                |


Mithilfe dieser Operatoren lassen sich nun die Bedingungen schreiben. Um so eine Bedingung zu schreiben, müssen wir vorher das Schlüsselwort für eine Fallunterscheidung voran schreiben `if` um in Klammern dahinter die Bedingung zu schreiben. Sollte nun die Bedingung wahr sein, wird alle was in den geschweiften Klammern dahinter kommt ausgeführt. Wenn man möchte kann man hinter der `if` noch ein `else` schreiben um einen block nur Auszuführen, wenn die Bedingung in der `if` Anweisung den Wert FALSCH liefert.  

Als Beispiele:

```python
# definiere eine Variable die mein Alter speichert
meinAlter = 23

if meinAlter >= 18:
  print('Du bist volljährig')

``` 
> Programm welches das Alter speichert und "Du bist volljährig" auf der Konsole schreibt wenn man älter oder gleich 18 Jahre alt ist.

```python
meinAlter = 23

if meinAlter >= 18:
  print('Du bist volljährig')
else:
  print('Du bist noch minderjährig')

```
> Programm welches das Alter speichert und "Du bist volljährig" auf der Konsole schreibt wenn man älter oder gleich 18 Jahre alt ist. Sollte man jedoch jünger als 18 Jahre alt sein wird "Du bist noch minderjährig" auf die Konsole geschrieben


```python
meinAlter = 23

if meinAlter >= 18:
  print('Du bist volljährig')
elif meinAlter >= 16:
  print('noch nicht volljährig, aber nah dran')
else:
  print('Du bist noch minderjährig')
```

> Dieses Programm gibt ein "Du bist volljährig" wenn der Benutzer älter oder gleich 18 Jahre alt ist. Zudem wird noch ein anderer Text ausgebenen wenn das alter größer oder gleich 16 ist. Als alternative wenn nichts anderes zutrifft wird "Du bist noch minderjährig" ausgegeben. 
> In dem Beispiel wird das `elif`-Konstrukt verwendet, welches nur die erste Bedingung ausführt. Das ist hier besonders Sinnvoll, da ansonsten immer beide Texte ausgebeben werden würden (da jemand der über 18 Jahre ist auch immer über 16 Jahre alt ist) und wir mit dem `elif`-Konstrukt nun nach der ersten Bedingung den rest des Konstrukts überspringen können, sollte jemand über oder gleich 18 Jahre alt sein. 

### Aufgaben

#### Wie viel kostet das Paket?
Schreibe ein Programm welches berechnet wie teuer ein Paket ist, wenn folgende Annahmen gelten:
- Das Gewicht des Pakets darfst du dir aussuchen
- Der Grundpreis beträgt 3,50 €
- Für Pakete bis 5kg gibt es eine Gebühr von zusätzlich 1€
- Für Pakete bis 7,5 kg gibt es eine Gebühr von zusätzlich 2€
- Für Pakete bis 10 kg gibt es eine Gebühr von zusätzlich 3€
- Für Pakete ab 10kg gibt es eine Gebühr von zusätzlich 3€ und pro KG nochmal 0,50 € dazu


## Arrays
Ein Array ist eine Möglichkeit unter einer Variable mehrere Werte zu addressieren. So brauchen wir aktuell um zum Beispiel die Werte für die Temperaturen der letzten Woche zu speichern insgesamt 7 Variablen. Leider können wir mit diesen Variablen nicht sehr dynamisch umgehen, da bei einem Zugriff auf eine Variable der Name der Variablen immer angegeben werden muss. Um die Werte also zum Beispiel alle zu addieren müssten wir die in unserem Fall die 7 Variablen zusammen addieren. Sobald wir jetzt aber ein weiteren Wert speichern wollen, müssen wir uns wieder eine neue Variable anlegen und das Programm ändern, so dass wir die neue Variable mit in die Berechnungen mit einbeziehen. 

Um das einfacher und dynamischer zu halten kommen nun Arrays in spiel. Hiermit ist es möglich wie gesagt mehrere Werte über einen gemeinsamen Namen und einen Index zu definieren. So können wir uns zum Beispel die ersten 5 Ungerade Zahlen in einem Array so definieren:

```python
meineZahlen = [1,3,5,7,9]
```
> Ein Array wird wie eine Variable definiert, nur statt einen Wert anzugeben, können wir hier in Eckgen-Klammern mehrere Werte desselben Typs angeben.

Die länge eines Arrays kann man sich in Python ebenfalls dynamisch Anzeigen lassen, indem man die in Python integrierte Funktion `len()` benutzt.

```python
meineZahlen = [1,2,3,5,7,9]
print(len(meineZahlen))
```


## Schleifen
Schleifen dienen in der Programmierung dazu Aufgaben zu bewältigen die öfters getan werden müssen. So ist bei einem Spiel immer so eine Schleife dabei die z.B. unseren Bildschirm immer neu lädt um so z.B. Dinge bewegen zu können. So kann man mit dem Schlüsselwort `while` so eine Schleife einleiten und dann in runden Klammern dahinter sofort die Bedingung definieren.

### Die while-Schleife

```python
while(x < 1000):
  # Wird solange ausgeführt wie die Bedingung (in den Klammern) wahr ist.
```

Also um ein kleines Beispiel zu machen, wollen wir nun die Zahlen von 1 bis 1000 ausgeben. Mit der alten weise müssten wir leider 1000x `print()` schreiben. Wir wollen das aber natürlich etwas vereinfachen und nehmen daher eine Schleife.

```python
x = 1; # wir wollen bei 1 anfangen

while(x <= 1000): # solange x kleiner oder gleich ist als 1000 gehen wir in die Schleife
  # wird solange ausgeführt wie die Variable x kleiner oder gleich 1000 ist. 
  # Ausgabe der Variablen x
  print(x)

  # erhöhe x um eins um die Schleife auch irgendwann beenden zu können.
  x = x + 1
```

### Die for-Schleife
Die for-Schleife dient dazu über eine Sequenz zu iterieren. Das heißt bei jeden Schleifendurchlauf nimmt die Zählvariable jedes Element in der Datenstruktur einmal als Wert an.

```python
temp = [9, 11, 14, 16, 16, 15, 12, 15]

for i in temp:
    print(i)
```
> Ausgabe:
9
11
14
16
16
15
12
15


## Aufgaben

### Summe Berechnen
Schreibe ein Programm, welches die Summe einer Zahlenfolge berechnet. Als Beispiel von 50 bis 200

### Fibonacci Zahlen
Gebe die Fibonacci Zahlen aus bis zu einer bestimmten Stelle.
Die Fibonacci Zahlen werden wie folgt berechnet:

1 1 2 3 5 8 11

Man nimmt die erstren beiden Zahlen 1 + 1 wobei dann 2 rauskommt. Als nächstes rechnet man 1 + 2 wo dann drei rauskommt usw.

### Fakultät berechnen
Schreibe ein Programm, welches die Fakultät einer Zahl berechnet. Die Fakultät ist das Produkt einer Zahlenfolge.
Beispiel Fakultät von 5
1 * 2 * 3 * 4 * 5 = 120

### Quersumme
Lasse die Quersumme von einer bestimmten Zahl berechnen

### Multiplizieren
Versuche eine Multiplikation (* oder mal nehmen) ohne das * Zeichen zu schreiben

### Dividieren
Versuche eine Division (/ oder geteilt nehmen) ohne das / Zeichen zu schreiben

### Modulo
Versuche eine Modulo (% oder mal nehmen) ohne das % Zeichen zu schreiben




### Funktionen
Mittels Funktionen können Codeteile ausgelagert werden und zentral an einer Stelle zur Verfügung gestellt werden. Das ist von Vorteil, wenn man Code in einem Programm oft verwendet und daher den Code nur an einer Stelle updaten möchte. Desweiteren ist es mit Funktionen einfacher funktionalitäten zu teilen und anderen Bereit zustellen oder aber in diese Funktionen selber in anderen Projekten wiederzuverwenden.

Um in Python eine Funktion zu erstellen, wird das Schlüsselwort `def` vor dem Namen der Funktion geschrieben. Danach kommen Klammern `()`. In diesen Klammern können nun Parameter definiert werden um bestimmte Variablen auch innerhalb der Funktion zur Verfügung zu haben. Die Funktion kann nach der definition aufgerufen werden, indem man den Namen mit den beiden Klammern schreibt.

```python
# definition der Funktion
def meineFunktion():
  print('Ich bin eine Funktion')


# Aufruf der Funktion.
meineFunktion()

# definition der Funktion mit einem Parameter
def meineFunktion2(meinParameter):
  print(meinParameter)


# Aufruf der Funktion mit Parameter
# Hier wird in den Klammern der Wert eingetragen und kann in der Funktion benutzt werden
meineFunktion2('hello')
```