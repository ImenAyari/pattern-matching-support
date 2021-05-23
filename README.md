# pattern-matching-support


# How does the Matching-Pattern-Support Work ? 
The matching support pattern algorithm is a sort of a reinforcement for Matching text-based input. Mainly inspired of AHO-CORASICK algorithm developped in the late 60's to 70's.
If interested to read more, follow the link: (put link here)
This Algorithm implementation is based on the functionning of a simple trie on top of an automaton with finite deterministic states.

    Note: This is a ready to use Package and you can use it as simply as any other Python Package. Click here to jump right to it.

## Objectif: Being able to recognize patterns in long input texts. 
Requirements: 
1. Data.Automata : 

This file is basically a larg dictionnary which includes all various patterns we need to recognize.

It is as important as the algorithm itself as it's used as a reference to our matching process.
The ```data.automata``` structure is simple to implement and to understand. 
It is structured as follow: 
    P<sub>x</sub> : X
  
P<sub>x</sub>: Is a finite state and it's the pattern we want to recognize in our matching process. 
X: Is the sequence of words which constitutes the pattern we intend to look for in the pattern-matching process
See ```resources/sample.automata``` as an example.

    P1: A
    P2: A B
    P3: A B C
    P4: A C
    P5: B
    P6: B C
    P7: A B C D E
    P1: Q Y 

2. Input: Simply put, the input file is the file you want to play and extract patterns declared in ```resources/data.automata``` from.

## Implementation: 
The implementaiton of the Pattern-Matching-Support Algorithm is based on two fundamental components which are Automata & Node.

### Node
A Node is composed of a name, a transition, a state and an index.
- Name: Is the name of the node, say P<sub>x<sub>
- Transition: Is the transtion -A Horizontal read on input text- we make from word to word in the text to recognize some pattern.
- A state: A node has different states but it only matters to us when it's final, say when we have succeeded to find the pattern in the input file.
- Index: The index is the position of node in the automaton.

--Detail: In order for a node to be final and to be able to continue the flow from a word to word with ease according to the automaton, we have implemented a slight regex pattern matching for some rare use cases. 

Utility of Regex: 
- We only wanted to implement regex in order recognize some patterns found in a non-normalized text unlike our perfect 
``` resources/input01``` 

Example: 
Input text: A B somethingC

Automata: 

P1: A B /C/

/C/ is an already implemented regex which can ignore *something* between the text lines and return to us the final pattern needed which is ``` P1 -- > ABC*```.


### Automata
Our Automata does the work of **matching**, **exploring** and **Exporting graph of final automata**

#### Matching
Since we have already defined our nodes and we can navigate easily between the words of our input, we can simply map the patterns found in the automata file with our input.
#### Explore
Exploring is the simple navigation of current nodes to next availabe node in our automata. 
Explore is a recursive funciton which returns the current node, the index of current node, the transtion, the next node and the index of next node. 

#### Graphviz_Export
If you need to know what Graphviz is , follow this link: https://www.graphviz.org/Gallery/directed/fsm.html

The ``` graphviz_export ``` function is where the satisfying part where we can see a png export of our automaton. 

Command: 
```python export_example.py | dot -Tpng > graph.png```
See output based on ```resources/sample.automata``` file and ```input01``` input file. 


![Automata png file](/home/imen/pattern-matching-support/miaou.png" "Automata png file.")

# Tests: 
We have stuffed our implementation of this Package with unitary tests using ```Unittest```.
Command : ```python -m unittest tests```

# Insatll Package 
Use the following url to be able to install the package and play along: 
1. Create a virtual env. 
Command: ``` python -m venv venv ```
2. Install Package: 
Command: ``` pip install git+ssh://git@github.com/ImenAyari/pattern-matching-support.git ```