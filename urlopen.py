from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
story_lines = []
for line in story:
    #  print(line)
    story_lines.append(line.decode('utf8'))
    print(story_lines)
    line_words = line.decode('utf8').split()
    #  print(line_words)
    for word in line_words:
        #  print(word[0])
        story_words.append(word)

story.close()
print()
print(story_lines[0])
print(story_words)

