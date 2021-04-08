## ****GRANDPY BOT:****

> Find me a place and tell me about it!
>
> GrandPy Bot is a program which will find you a place and a story about it.
>
> -> ask for an address and the program will give you a Wikipedia answer and a 'satellite' Google map position with a marker.

---------------------------------------------------------------------------------------------

[]()**RUN THE APP:**

`Installation required:`

- Install Virtual Environment : python -m pip install --user virtualenv
- Inside the folder "setting" open the file "install.py"
  !! Don’t forget to run cmd or powershell as administrator !

`Launch:`

- To start the app, launch main.py


----------------------------------------------------------------------------------------------

[]()**FEATURES:**

`Encoding:`

- Python 3
- HTML 5
- CSS
- Bootstrap 4
- Javascript (Vanilla)

`Launched:`
Flask



`Fork:`
https://github.com/MyBhive/papy.git

-----------------------------------------------------------------------------------------------

[]()**DESCRIPTION:**

`framework`

| Flask | inside the back-end code (circular import) |
| ----- | ------------------------------------------ |
|       |                                            |

`Back-end files`

| [ROOT]()                  | --------------------------------------------------------------------- |
| ------------------------- | ------------------------------------------------------------ |
| **Install.py**            | File to install “requirement.txt”                            |
| **main.py**               | File to start the game                                       |
| **PPBOT FOLDER**[]()      | **---------------------------------------------------------------------** |
| **init.py**               | To initial the framework (circular import)                   |
| **parse.py**              | File to parse the user input before we can find an address and a wiki answer |
| **views.py**              | File to link back coding and front coding  through the framework (circular import) |
| **PPBOT/APIS FOLDER**[]() | **---------------------------------------------------------------------** |
| **map.py**                | File to find the geocode and the address from a place through the user input parsed |
| **wiki.py**               | file to find the wikipedia answer from a place through the user input parsed |
| **TEST FOLDER**[]()       | **----(run pytest in cmd from the root after downloading pytest in a virtualenv)-----** |
| **test_map.py**           | pytest_mock to check the code                                |
| **test_parse.py**         | pytest to check the code                                     |
| **test_wiki.py**          | pytest to check the code                                     |
|                           |                                                              |

`Front-end files`

| **TEMPLATES FOLDER**[]() | --------------------------------------------------------------------- |
| ------------------------ | ------------------------------------------------------------ |
| **index.html**           | File containing  the html5 coding                            |
| **STATIC FOLDER**[]()    | **---------------------------------------------------------------------** |
| **script.js**            | File containing all the Javascript coding                    |
| **style.css**            | File containing all the CSS coding                           |
| **img**                  | folder containing all the picture used on the homepage       |

`Text files`

| words.json      | list of stop-words to make the user input parse |
| --------------- | ----------------------------------------------- |
| Requirement.txt |                                                 |

​	



----------------------------------------------------------------------------------------------

[]()**TO CONTRIBUTE:** 

> You need to respect PEP8 !!!  

- Fork it 

- Create your feature branch

- Commit your changes

- Push to your branch 

- Create a pull request

-----------------------------------------------------------------------------------------------

##### []()**WRITTEN BY:**

> MyBhive 

*My most sincere thanks to Geoffrey and Abdelhamid who are coaching me and helping me to get better* 