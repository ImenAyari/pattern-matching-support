import unittest
from pattern_matching_support.automata.automata import automata_factory

class TestMatching(unittest.TestCase):
    INPUT_FILE_NAME = 'resources/input_01'
    AUTOMATA_FILE_NAME = 'resources/sample.automata'

    def test(self):
        automata = automata_factory(filename=self.AUTOMATA_FILE_NAME)
        reader = open(self.INPUT_FILE_NAME, 'r')
        matched_list = []
        for line in reader:
            words = line.strip().split()
            m = automata.match(words)
            matched_list.append(m)
        reader.close()

        expected_match_list = ['P7', 'P2', None, 'P1', 'P2']
        self.assertListEqual(matched_list, expected_match_list)

if __name__ == '__main__':
    unittest.main()
