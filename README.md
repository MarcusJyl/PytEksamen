[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MarcusJyl/PytEksamen/HEAD)

Project name: Bird classifier
Description:
Giv et billede af en nord amerikansk fugl, og vores program giver en prediction i procent og noget information, om den fugl den har gættet at dit billede svarer til.

List of used technologies:
Beatuful soup
flask
keras
numpy
(regular expressions)

HOW TO USE:
1. Clone vores projekt ind i det docker miljø som vi har fået givet af vores underviser i starten af semesteret (docker_notebooks/notebooks)
2. Download vores imgage processing model: https://drive.google.com/file/d/1cvDBh90rj4KH1pyMzJXaKBchHbS32WGL/view?usp=sharing (562 MB)
3. Læg modellen i roden af flask mappen.
4. Åben visual studio code og "attach to running container"
5. Åben konsollen (hvis du ikke er i jovyan mappen skal du "cd" til jovyan)
6. Brug denne command for at kører programmet "python PytEksamen/flask/hva.py"
7. Klik på den url der kommer i terminalen
8. Upload et billede af en amerikansk fugl og se hvad der sker ;)


Status: Alt er implementeret, men endpointet er ikke deployet.
List of challenges: Vores model er god til at gætte rigtig.
