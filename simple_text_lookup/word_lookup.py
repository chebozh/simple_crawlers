import re
import argparse

"""
Small program to look up for a word in a txt file.
Returns the line number where the word was found and the line itself.

The poem.txt file was used for testing.
"""


def perform_lookup():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='enter word to search for')
    parser.add_argument('file_name', help='specify txt file to search')
    args = parser.parse_args()

    with open(args.file_name, 'r') as f:
        line_num = 0
        for line in f.readlines():
            line = line.strip('\n\r')
            line_num += 1
            search_result = re.search(args.word, line, re.M | re.I)

            if search_result:
                print('{}: {}'.format(line_num, line))
                return

        print('Word not found')



if __name__ == '__main__':
    perform_lookup()
