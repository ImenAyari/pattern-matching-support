# pattern-matching-support

to run test: ```python -m unittest tests```


https://www.graphviz.org/Gallery/directed/fsm.html

# Export graphviz

required: https://www.graphviz.org/download/ 

if main.py print the export:
```python export_example.py | dot -Tpng > graph.png```

if main.py defines filename (graph.dot) to export:
```python export_example.py && dot -Tpng graph.dot > graph.png```

required: ```pip install setuptools```


launch command:  ```python setup.py check```
launch command:  ```python setup.py sdist```
