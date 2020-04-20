import sys
from urllib.request import urlopen

#  url -- 'http://sixty-north.com/c/t.txt'

def fetch_words(url):
    """Fetch a list of words from, a URL."""
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    for items in items:
        print(items)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
