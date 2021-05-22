import sys
from pattern_matching_support.automata.automata import automata_factory

def cb(n, t, nn):
  print("{} {} {} {} {}".format(n.instance_index, n.name, t, nn.instance_index, nn.name))

def main():
  automata = automata_factory('resources/sample.automata')
  # automata.graphviz_export(filename="graph.dot")
  automata.graphviz_export()
#  automata.explore(cb)

#  for line in sys.stdin:
#    words = line.strip().split()
#    m = automata.match(words)
#    print(m)
#

main()
