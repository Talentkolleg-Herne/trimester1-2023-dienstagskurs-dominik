# Python installieren
Hier wird beschrieben wie man PyCharm installiert.

## Was ist überhaupt Python?
Python ist eine sehr bekannte und mittlerweile weit verbreitete Scriptsprache, welche für automatisierungen oder aber auch für Künstliche Intelligenz verwendet wird. Natürlich kann die Sprache aber auch für quasi alle anderen Sachen herhalten und benutzt werden.

## Installation
Die installation teile ich mal in drei Stufen ein.
- Download
- Installation
- Testen

### Download
Python kann von der offiziellen Webseite https://www.python.org/ heruntergeladen werden oder aber von diesem direktlink, der auf den Download der Seite zeigt: https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe

Benutzen tun wir hier die Version für Windows in der 3.9.10er Version. Auf dieser Seite kann die gleiche Version von Python auch für andere Betriebssysteme heruntergeladen werden auf die ich jetzt aber nicht weiter eingehen werde (https://www.python.org/downloads/release/python-3910/).

### Die eigentliche Installation
Um die Installation zu starten, navigieren wir zu dem Download-Ordner und doppelklicken auf die eben gedownloadete Datei. Sie sollte ungefähr wie folgt bennant sein wobei die X für die Versionsnummer stehen: `python-x.x.x-amd64.exe`

Sollte nun ein Fenster scheinen wählen wir nochmal Ausführen.

![Administrator Berechtigung](chapter/images/python-install-window1.PNG)

Nun erscheint ein weiteres Fenster, indem wir anklicken sollen was wir genau wollen. Da klicken wir auf das rot Umrandete `Install Now`

![Installieren](chapter/images/python-install-window2.PNG)

Nun bekommen wir als letztes das Fenster, das alles geklappt hat.

![Erfolgreich installiert](chapter/images/python-install-window3.PNG)

### Testen
Um die Installation zu testen, können wir recht einfach ein Terminal aufmachen und dort `python --version` eingeben um zu sehen ob es den Befehl nun gibt. 


Um das Terminal aufzumachen drücken wir die `Windows`-Taste und die Taste `R`. Damit rufen wir ein Fenster auf (siehe Abbildung 1), indem wir Programme ausführen können. In dieses Fenster schreiben wir nun cmd rein und drücken Enter. Damit öffnen wir die Eingabeauffroderung (siehe Abbildung 2) in der wir nun ebenfalls wieder Befehle ausführen können.

![In dem Ausführen Fenster können wir Programme oder Befehle ausführen](chapter/images/execute_cmd.PNG)

![Unsere Eingabeaufforderung für Befehle unter Windows](chapter/images/cmd_window_empty.PNG)

Nun können wir in diesem Fenster den Befehl `python --version` eingeben um zu schauen ob wir eine Ausgabe mit dr Versionsnummer bekommen:

```bash
Z:>python --version
Python 3.9.10
```
