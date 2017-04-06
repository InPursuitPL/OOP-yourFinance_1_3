Hi, this is my Text User Interface program called yourFinance. 
It is created as a project to get to know and learn Object Oriented Programming in practice.
I am aware that some elements (like functionality itself) are a bit goofy but please remember
that this is just a simple program to learn OOP and this is the only reason why I created it.
My main goals, while working on it, were to design it as good as I can at this moment 
(in terms of Object Oriented Design, not functionality) and to make it possibly user-error-proof.
I created some (not advanced) unit tests and I would like to extend this topic in the future.

I've used here Observer design pattern to save data as well as changelog file.

All sugestions, advices and constructive criticism will be MUCH appreciated!

Start it with main.py, program stores data as shelve files and uses nose for automated tests.

TODO list:
Clearer separation between application layers (data access layers seems to be quite ok but there
are user input elements in some objects' functions and this would make them harder to transfer 
into models in MVC pattern web app based on this program).
