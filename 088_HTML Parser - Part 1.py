#HTML Parser - Part 1


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start    :",tag)
        if attrs:
            for each in attrs:
                print('-> '+' > '. join(list(map(str, each))))

    def handle_endtag(self, tag):
        print("End      :",tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty    :",tag)
        if attrs:
            for each in attrs:
                print('-> '+' > '.join(list(map(str, each))))

parser = MyHTMLParser()
for each in range(int(input())):
    parser.feed(input())