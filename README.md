# MOVEL AI 2025-2026

Deze repository bevat de bronbestanden van de online module **AI en Onderwijs**. Deze module is onderdeel van de [HAN Master Ontwerpen Van Eigentijds Leren](https://www.han.nl/opleidingen/master/ontwerpen-van-eigentijds-leren/deeltijd/) (MOVEL).

## Over deze module

Deze module biedt een gestructureerd overzicht van de ontwikkelingen rondom AI in een educatieve context. De inhoud is thematisch opgezet en bedoeld voor docenten, studenten van lerarenopleidingen en onderwijsprofessionals.

### Inhoud van de module
- **Inleiding**: Basisconcepten en de impact van AI op de samenleving.
- **AI-geletterdheid**: Wat moeten docenten, studenten en leidinggevenden weten en kunnen?
- **Voorbeelden van AI**: Een verzameling actuele tools en hun toepassingen.
- **AI in het onderwijs**: Wat betekent AI voor het onderwijs?
- **Vibecoding**: Essentiële vaardigheden voor de toekomst?
- **Literatuur**: Waar vind je meer informatie over AI en onderwijs?
- **De mens en AI**: Ethische vraagstukken, wetgeving (AI Act) en bias.
- **AI in de film**: Reflectie op AI via popcultuur.

## Techniek: Quarto

Deze module is gebouwd met [Quarto](https://quarto.org/), een open source auteurssysteem gebaseerd op Markdown. Dit maakt het eenvoudig om de bronbestanden te bewerken en de module statisch te renderen als website.
Een exemplaar van de meest recente versie kun je downloaden via het "releases" tabblad hier op github.

### Lokaal renderen
Om de module lokaal te bewerken of te bouwen, heb je Quarto nodig.

1.  Installeer Quarto van [quarto.org](https://quarto.org/docs/get-started/).
2.  Clone deze repository.
3.  Installeer de volgende R libraries als je die nog niet hebt:

```r
install.packages(c("rmarkdown", "knitr", "exams2forms"))
```

4.  Installeer de benodigde extensies:

```bash
quarto add gadenbuie/now
```

4.  Gebruik de volgende commando's in de terminal:

```bash
# Preview de website lokaal
quarto preview

# Render de website naar de 'docs' map
quarto render
```

De website wordt standaard gerenderd naar de `docs` map.

## Realisatie en Licentie

- **Auteur**: [Pierre Gorissen](https://www.ixperium.nl/over-ons/medewerkers/pierre-gorissen/).
- **Ontwikkeling**: Initieel in 2023 (Xerte), geconverteerd naar Quarto in 2026.
- **Licentie**: Deze inhoud wordt beschikbaar gesteld onder een [Creative Commons Naamsvermelding-GelijkDelen (CC BY-SA)](https://creativecommons.org/licenses/by-sa/4.0/deed.nl) licentie.

## Contact
Voor vragen of suggesties over de inhoud van deze module kun [je contact opnemen](mailto:info@ixperium.nl?subject=Over%20de%20module%20AI%20en%20Onderwijs).
