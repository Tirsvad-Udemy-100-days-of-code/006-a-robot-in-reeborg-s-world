# Sådan virker det

🌐 [English](How-It-Works) · **Dansk** · [Bahasa Melayu](How-It-Works-ms)

## Metoden

Robotten følger den højre væg:

1. Gå fremad, indtil en væg stopper den, og drej derefter til venstre. Så er der en væg til højre, og robotten undgår en endeløs vandring i åbent rum.
2. Indtil målet er nået: hvis højre side er fri, drej til højre og gå; ellers, hvis fronten er fri, gå; ellers drej til venstre.

Reeborgs verden har ikke "drej til højre", så et højredrej er tre venstredrej.

## Delene

| Lag | Mappe i `src/reeborg_maze` | Hvad den indeholder |
| --- | --- | --- |
| Domæne | `domain/` | Reglen om at følge væggen og robottens grænseflade; importerer intet andet |
| Applikation | `application/` | Use casen, der løser en verdensfil, og de porte den bruger |
| Infrastruktur | `infrastructure/` | Simulatoren uden forbindelse og læseren af Reeborgs verdensfiler |
| Præsentation | `presentation/` | Kommandolinjen, tekstudtegningen og scriptet, der indsættes i Reeborgs verden |

Scriptet i `presentation/reeborg_script.py` gentager reglen, fordi Reeborgs verden ikke kan importere kode. En test kører scriptet mod simulatoren fra hver ledig start, så de to kopier ikke kan skilles ad.
