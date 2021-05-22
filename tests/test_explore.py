import unittest
from pattern_matching_support.automata.automata import automata_factory
from pattern_matching_support.automata.node import Node 


class TestExplore(unittest.TestCase):
    AUTOMATA_FILE_NAME = 'resources/sample.automata'

    def test(self):
        automata = automata_factory(filename=self.AUTOMATA_FILE_NAME)
        expected_explore = ["1 ε A 2 P1",
                            "2 P1 B 3 P2",
                            "3 P2 C 4 P3",
                            "4 P3 D 8 None",
                            "8 None E 9 P7",
                            "2 P1 C 5 P4",
                            "1 ε B 6 P5",
                            "6 P5 C 7 P6",
                            "1 ε Q 10 None",
                            "10 None Y 11 P1"]

        computed_explore = []
        def automata_explore_callback(node: Node, transition: str, next_node: Node):
          computed_explore.append("{} {} {} {} {}".format(node.instance_index, node.name, transition, next_node.instance_index, next_node.name))

        automata.explore(automata_explore_callback)
        self.assertListEqual(expected_explore, computed_explore)

if __name__ == '__main__':
  unittest.main()
