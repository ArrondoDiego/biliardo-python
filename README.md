# Biliardo 2D in Python

Progetto scolastico del 2017: una simulazione 2D di biliardo scritta in Python, con una piccola libreria grafica didattica basata su Tkinter.

> **Stato:** progetto storico, non più mantenuto. Alcune parti sono incomplete o non funzionanti (ad esempio buche laterali e sponde).

## Descrizione

Due palline su un tavolo con sei buche. Si mira ruotando la stecca, si sceglie la potenza del tiro e si cerca di mandare la pallina in buca, simulando gli urti tra le due sfere.

## Come si gioca

| Tasto | Azione |
| --- | --- |
| `←` / `→` | Ruota la mira |
| `↑` / `↓` | Regola la potenza (1–4) |
| `Invio` | Tira |

## Requisiti

- Python 3
- `tkinter` (di solito incluso; su Debian/Ubuntu: `sudo apt install python3-tk`)

Nessuna dipendenza esterna.

## Avvio

```bash
python3 main.py
```

## Struttura del progetto

| File | Contenuto |
| --- | --- |
| `main.py` | Logica di gioco e setup della scena |
| `marioGraphics.py` | Libreria grafica didattica (punti, segmenti, immagini, Tkinter) |
| `marioConsole.py` | Utility di input/output da console |
| `imgs/` | Immagini: sfondo, palline, stecca, schermate di vittoria/sconfitta |

## Note

Il codice risale al 2019 ed è scritto in stile didattico (`import *`, variabili globali, pochissima struttura). È stato conservato così com'era: non è pensato per essere riscritto o mantenuto.
