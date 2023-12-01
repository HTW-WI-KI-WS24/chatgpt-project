[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/cVeImKGm)

## Installation Guide

Execute <code>pip install customtkinter</code> as well as <code>pip install openai</code> in your command line.


### Weiteres Vorgehen
- Summary agent erstellen 
    -   dafür als context bei jeder user request "[User]:" mitgeben, um dem summary agent ganz klar mitzuteilen,
        welche sachen vom user ausgegangen sind, bzw. für welche sachen er sich entschieden hat (bisheriges problem,
        dass summaries auch input von agents die nicht vom user abgesegnet wurden aufgenommen haben)
- Role-Prompts darauf spezialisieren, dass die Agents nicht von ihrem Job abweichen bzw. versuchen ins Detail zu gehen.
- Agents miteinander connecten.
- weitere agents einrichten und user journay aufbauen
- als model chatgpt4 verwenden
