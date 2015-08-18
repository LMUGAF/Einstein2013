Das erstellen des Ersti-Einsteins läuft in den follgenden vier Schritten ab
 1. Inhalt erstellen
 Check: Rechtschreibung, Gramatik, Inhalt, ...
 2. An LaTeX automatissmen anpassen
 Check: Optik, Zeilenumbruch, Seitenanzahl ist vielfaches von 4
 3. Drucken
 4. Aufräumen


An LaTeX automatissmen anpassen, das beinhaltet vorallem die follgenden drei Punkte
 a. Over- und underfull boxes ausgleichen
 b. Automatische Worttrennung kontrollieren/korrigieren
 c. Blockweise umstrukturieren

Diese Punkte werden im ersten run noch in dieser reihenfollge abgearbeitet, jedoch kann eine Änderung die wiederholung der Schritte a-c nach sich ziehen. Eine Änderung wirkt sich zum glück nur auf den gesamten Text ab dieser Änderung aus. Eine art Savepoint ist ein erzwungener Seitenwechsel, der z.B. durch ein neues Kapitel eingeleitet wird. D.h. die Änderungen wirken sich nur bis dahin aus. Hat eine Änderung zur follge, dass sich die Seitenzahl bis zum nächsten savepoint ändert, kann das auswirkungen auf die Anordnung aller follgenden Seiten bis zum ende des gesamten Dokuments.

AUTOBUILD
----------
Der Einstein wird auch automatisch bei jedem commit neu gebaut. Für weitere informationen finden sich in AUTOBUILDER.HEROKU; der Output findet sich auf http://build.opha.se/einstein/
