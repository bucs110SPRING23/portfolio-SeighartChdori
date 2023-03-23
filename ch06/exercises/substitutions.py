import json

def main() :
    newstext = open("news.txt","r").read()
    subsjs = open("subs.json","r")
    substitute = json.load(subsjs)

    for x,y in substitute.items() :
        newstext = newstext.replace(x,y)
        print(x,y)

    betternews = open("betternews.txt","w")
    betternews.write(newstext)

main()