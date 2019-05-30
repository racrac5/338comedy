import nltk

#Ryan edit to fit the I used to ____ but then I _____ format
def main():
    searchword = "soccer"
    corpus = []
    relevance = 0
    max_amount = 0
    index = -1
    printlin = 0

    # not necessary to seach whole folder now, they are working on tags as object feature
    myfile = open("../scripting/sketches txt files/soccercommentating.txt", encoding="utf8")
    lines = myfile.readlines()

    for line in lines:
        index += 1
        if "massive" in line.lower(): relevance += 1
        if (relevance > max_amount): printlin = index
        relevance = 0

    if printlin != -1:
        print(lines[printlin])
        # return lines[printlin]

main()
