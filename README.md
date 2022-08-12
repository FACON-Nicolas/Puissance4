# Connect 4 Alpha

![](https://img.shields.io/badge/Release-v3.0-blueviolet)
![](https://img.shields.io/badge/Language-python-005255)
![](https://img.shields.io/badge/Libraries-pygame-00cfff)
![](https://img.shields.io/badge/Size-57Ko-f12222)
![](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

**!! THIS GAME IS NOT FINISHED AND CONTAINS MANY BUGS !!**
This repository contains the source code of a connect4's (puissance 4) copy. In this game, your computer cans also play against you like a human player, good luck ! </p>

![](https://github.com/FACON-Nicolas/FACON-Nicolas/blob/main/resources/connect4.gif?raw=true)

# Summary

* **[Summary](#summary)**
* **[Credits](#credits)**
* **[Features](#features)**
* **[Prerequisites](#prerequisites)**
* **[Install](#install)**
* **[Releases](#releases)**
* **[Keys](#keys)**
* **[AI Functionning](#ai-functionning)**
    * **[Beginning](#beginnning)**

# Credits

* **[Facon Nicolas](https://www.github.com/FACON-Nicolas/)** : Creator of the project 

# Features

+ **AI plays against player**

![](https://i.ibb.co/7CkCW4W/Capture-d-cran-2022-02-19-105805.png)

+ **AI cans take decisions**

![](https://i.ibb.co/RcjdrP4/Capture-d-cran-2022-02-19-105806.png)

# Prerequisites

+ Windows:  
    - **[Python](https://www.python.org/downloads/)**
    - **[Git Bash](https://gitforwindows.org/)**
    - **pygame** (``py -3.8 -m pip install pygame`` in your terminal)
+ Linux: 
    write this in terminal 
    ```sh
    #if python is not installed yet.
    sudo apt install python3.8

    #if pygame is not installed yet.
    pip install pygame
    ```

# Install

Once the prerequisites installed, go on your terminal (or git bash terminal) and write this:

```sh
git clone https://github.com/FACON-Nicolas/Puissance4
cd Puissance4/
#python3 or py on windows
python3 puissance-4/source/game.py

```

# Keys

| actions | keys |
|---------|------|
| move right | RIGHT |
| move left  | LEFT |
| place coin / Restart Game | SPACE |

# AI Functionning

An AI system is included in the connect 4.

But, ***how does this AI work ?***. 

## beginnning

At the beginning, I wanted an AI that places its coin at the best sequences' position only. If many position are possible, then a random position is choosen.

**example 1:**

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | - | - | - | - | - | - | - |
| 1 | - | - | - | - | - | - | - |
| 2 | - | O | X | O | X | - | - |
| 3 | O | O | X | X | O | O | - |
| 4 | O | X | X | O | O | O | X |
| 5 | X | O | O | X | X | O | X |

In this situation, the AI coin is **O**, and the best positions to place a coin are **{2, 5}**, a value will be choosen **randomly**.

**example 2:**

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | - | - | - | - | - | - | - |
| 1 | - | - | - | - | - | - | - |
| 2 | - | O | X | O | X | - | - |
| 3 | O | O | X | X | X | O | - |
| 4 | O | X | X | O | O | O | X |
| 5 | X | O | O | X | X | O | X |

In this situation, the AI coin is **O**, and the best positions to place a coin are **{5}**, the value choosen will be **5**

This algorithm gives the best positions to place an AI Coin, but there's a problem, if the human player doesn't care about the AI game, then this is almost useless, then I had to check the best next human player sequences.