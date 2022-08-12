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
* **[Keys](#keys)**
* **[AI Functionning](#ai-functionning)**
    * **[Beginning](#beginnning)**
    * **[AI Update](#ai-update)**
    * **[Set Theory](#set-theory)**
        * **[Intersection](#intersection)**
        * **[Union](#union)**
        * **[Intersection implementation](#intersection-implementation)**
    * **[Final AI Functionning](#final-functionning)**
* **[Releases](#releases)**

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

|          actions          | keys  |
|:-------------------------:|:-----:|
|         move right        | RIGHT |
|          move left        | LEFT  |
| place coin / Restart Game | SPACE |

# AI Functionning

An AI system is included in the connect 4.

But, ***how does this AI work ?***. 

## beginnning

At the beginning, I wanted an AI that places its coin at the best sequences' position only. If many position are possible, then a random position is chosen.

**example 1:**

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | - | - | - | - | - | - | - |
| 1 | - | - | - | - | - | - | - |
| 2 | - | O | X | O | X | - | - |
| 3 | O | O | X | X | O | O | - |
| 4 | O | X | X | O | O | O | X |
| 5 | X | O | O | X | X | O | X |

In this situation, the AI coin is **O**, and the best positions to place a coin are **{2, 5}**, a value will be chosen **randomly**.

**example 2:**

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | - | - | - | - | - | - | - |
| 1 | - | - | - | - | - | - | - |
| 2 | - | O | X | O | X | - | - |
| 3 | O | O | X | X | X | O | - |
| 4 | O | X | X | O | O | O | X |
| 5 | X | O | O | X | X | O | X |

In this situation, the AI coin is **O**, and the best positions to place a coin are **{5}**, the value chosen will be **5**

This algorithm gives the best positions to place an AI Coin, but there's a problem, if the human player doesn't care about the AI game, then this is almost useless, then I had to check the best next human player sequences.

## AI Update

to improve my AI algorithm, I decided to check the best next human player sequences. Column by column, the human sequences will be checked and only the best position will be kept.

**Example 1**:

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | - | - | - | - | - | - | - |
| 1 | - | - | - | - | - | - | - |
| 2 | - | O | X | O | X | - | - |
| 3 | O | O | X | X | O | O | - |
| 4 | O | X | X | O | O | O | X |
| 5 | X | O | O | X | X | O | X |

In this situation, the human coin is **X**, and the best positions to place a human coin are **{2}** and the best sequences will be equal to 4, the value chosen will be **2**.

**Example 2:**

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | - | - | - | - | - | - | - |
| 1 | - | - | - | - | - | - | - |
| 2 | - | O | X | O | X | X | - |
| 3 | O | O | X | X | X | O | - |
| 4 | O | X | X | O | O | O | X |
| 5 | X | O | O | X | X | O | X |

In this situation, the human coin is **X**, and the best positions to place a human coin are **{2, 5}** and the best sequences will be equal to 4, the value will be chosen **randomly**

## Set Theory

In this AI functionning, the power of this AI is the [set theory](https://en.wikipedia.org/wiki/Set_theory), and particularly the intersection

### Intersection

The intersection's symbol is ``∩``.

**Example**:

**{1, 3, 7, 9, 13} ∩ {1, 2, 6, 8, 9} = {1, 9}**

### Union

The intersection's symbol is ``∪``.

**{1, 3, 7, 9, 13} ∪ {1, 2, 6, 8, 9} = {1, 2, 3, 6, 7, 8, 9, 13}**

### Intersection implementation

To implement an intersection, I wrote this method 

```py
def intersection(self, L1: List[int], L2: List[int]) -> List[int]:
    return [i for i in L2 if i in L1]
```

## Final Functionning

the final functionning is:

```
if (sequence ai size = 4): place AI coin normally

else if (sequences human size >= 3)

.... if (intersection is not empty) place AI coin in intersection

.... else place AI coin in best human sequences

else place AI coin normally
```

# Releases

* **1.0** : 2021-08-10
* **2.0** : 2021-10-13
* **3.0** : 2022-12-22