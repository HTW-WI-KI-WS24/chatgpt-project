[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/cVeImKGm)

## Installation Guide

Execute <code>pip install openai</code> in your command line.

Put a valid openai-key as well as the correct python version into your environment variables.

## File Documentation
#### Main.py
This is the class that manages all the agents and determines the application's logic flow.

#### BookGPT.py
This class provides general application-user-communication assets.

#### StandardChatGPT.py
This class is supposed to represent a standard instance of ChatGPT like you would find on your browser.
It stores context and provides various basic methods to work with.

It can be used by different agents to complete simple and repetitive tasks that are better off being 
handled by a simple ChatGPT, rather than a fully fleshed out agent.

### src folder
#### Agent.py
This class is an abstract class and represents the base of every agent. It provides all the complex
functionality that is used to have agents interact with input and other things.

All the agents inherit from this class and take over all of its variables and functionality in doing so.

#### AuthorAgent.py
This agent generates the book, chapter by chapter, event by event according to all the information
collected before.

#### CentralAgent.py
This agent communicates with the user in a back-and-forth-discussion and tries to ascertain general (central)
information about the book (e.g. genre, location, target audience etc.).

#### CharacterAgent.py
Generates a set of main characters based on how many characters the user wants for their book (ascertained
by the CentralAgent). Generates characters with backgrounds, unique looks etc. These characters
will fit into the already designed world.

Lets the user make adjustments to the generated characters as often as they like.

#### EventAgent.py
Generates a final event for the book that everything will lead up to. This will fit into the already
designed world and characters.

Lets the user make adjustments to the generated world as often as they like.

#### StoryAgent.py
Generates all the events that will happen within the book and structures them into different chapters.
These events will be based on the already designed world and characters, follow the general idea of
the book and will be made in a way so that they lead up to the final event.

#### WorldAgent.py
Generates a world for the book based on the general things that the user has already thought of for their
book (information provided by the CentralAgent).

Lets the user make adjustments to the generated world as often as they like.

### utils folder
#### ChapterContainer.py
#### ConsoleHelpers.py
#### InputChecker.py
#### PromptHelpers.py
