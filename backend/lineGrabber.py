import nltk;
import glob;
import os;
#import sketches_txt_files/soccercommentating;

def main():
    searchword = "soccer";
    corpus = [] ;
    relevance = 0;
    max = 0;
    index = -1;
    printlin = 0;

    #file_list = glob.glob(os.path.join(os.getcwd(), "sketches txt files", "*.txt")) ;

    myfile = open("/Users/ryancallaghan/Desktop/EECS/338/338comedy/sketches txt files/soccercommentating.txt")
    # not necessary to seach whole folder now, they are working on tags as object feature
    lines = myfile.readlines()

    for line in lines:
        index = index+1;
        if "Massive" in line:
            relevance = relevance + 1;
        if (relevance > max):
            printlin = index;
        relevance = 0;

    if printlin != -1:
        print(lines[printlin]);
        return lines[printlin] ;

main();

#    with open(file_path) as f_input:
#        corpus.append(f_input.read())
