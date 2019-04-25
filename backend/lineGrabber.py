import nltk;
import glob;
import os;
#import sketches_txt_files/soccercommentating;

def main():
    searchword = "soccer";
    corpus = [] ;
    relevance = 0;
    max = 0;
    index = 0;

    #file_list = glob.glob(os.path.join(os.getcwd(), "sketches txt files", "*.txt")) ;

    myfile = open("/Users/ryancallaghan/Desktop/EECS/338/338comedy/sketches txt files/soccercommentating.txt")
    lines = myfile.readlines()

    for line in lines:
        if line.contains("soccer"):
            relevance = relevance + 1;
        if relevance > max:
            index = line;
        relevance = 0;
    print(lines[index]);
    return lines[index] ; 



#    with open(file_path) as f_input:
#        corpus.append(f_input.read())
