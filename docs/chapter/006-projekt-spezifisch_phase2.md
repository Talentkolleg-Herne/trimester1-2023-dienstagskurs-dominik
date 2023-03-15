## Phase 2

In Phase 2 kümmern wir uns zuerst das wir das Spielfeld zeichnen.

### Spielfeld zeichnen ohne alles

Dafür schreiben wir uns zuerst die Breite und die Höhe in jeweils separate Variablen um Sie später zugreifbar zu haben und leichter abänderbar, sollte unser Spielfeld doch größer oder kleiner werden.

```python3
WIDTH = 40
HEIGHT = 20
```

Anschließend laufen wir mit einer For-Schleife über die Höhe um für jede Zeile ein Wert zu erhalten. Da unser Spielfeld ein Koordinatensystem darstellen soll, benutzen wir hier auch direkt die "richtige" Variable: y

```python3
for y in range(0, HEIGHT):
  print("")
```

> durchläuft unsere komplette höhe und springt immer in eine neue Zeile

Anschließend können wir das ganze auch für X machen. Hier ist es nur wichtig auf die Reihenfolge zu achten. Da wir im Terminal immer von Links nach Rechts schreiben und anschließend nicht mehr die Höhe verändern können, müssen wir also y außen haben (wird als letztes gemacht) und x im inneren.

```python3
for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
      print(" ", end="")
    print("")
```

> Damit wäre das Spielfeld fertig. Im inneren wird das ende überschrieben, damit wir nicht in eine extra Zeile rutschen.

### Spielfeld Ball zeichnen

### Spielfeld Paddles zeichnen
