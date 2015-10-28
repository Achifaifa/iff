#Interactive Fiction Framework

Minimal framework for "Choose your own adventure" games.  

Current size: 256 bytes

## Creating an adventure

To generate your adventure, edit the files in `st` (Short for story). Each file is considered a chapter, but you can use them however you wish. The only requisite is that the first chapter is called `c1` and the initial fragment is called `a`, so the `cr=c1.a` line can execute properly. You can consider that fragment in that file an introduction and place everything else in other files.  

On each chapter (File), you can define different fragments. The fragments are lists and have the following structure:  

* The first element is the text of the current fragment
* The rest of the elements are lists that represent choices you can make after that fragment

Each choice has the following elements:

* The name of the choice (It's recommended to write option numbers starting from 1)
* The text that explains the choice you selected (e.g. "You decide it's better to run")
* The chapter that choice leads to
* The fragment that choice leads to

The engine will process all the chapters in the `st` folder, so writing your story there will be enough to make it work (As long as you don't have missing fragments or chapters).  

To write the ending of the game, simply create a chapter with a single option called "The End" or something similar.   

## Playing an adventure

* Start the game with `python main.py`
* Read the fragment and select the option you want (writing the option number and pressing enter)

The game does not have save or load functions due to size constraints. Inputting an empty string (Pressing enter), a letter or anything that is not a choice will raise an exception and exit the game. 

To finish your current game, simply press `enter` or issue a `KeyboardInterrupt` (`Ctrl + C` in linux systems).

## Sharing adventures

You can share adventures forking this repository and adding a branch with your story files in the `st` folder. I'll accept any PR that has a working story with a minimum of quality.
