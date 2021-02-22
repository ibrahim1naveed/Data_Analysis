The following project does the following things: 

- It uses the dataset from https://www.kaggle.com/liury123/my-little-pony-transcript, called clean_dialog.csv.
- Analysis.py uses this csv file to conduct data analysis over the data set. It then calculates the following for each pony :

verbosity : fraction of dialogues by each pony as proportion of the rest of the ponies.
mentions : number of mentions of that pony as a proportion of the total mentions of those 6 ponies.
follow_on_comments : the fraction of times each pony has a line that DIRECTLY follows the others pony’s line.
non_dictionary_words : a list of the 5 non-dictionary words used most often by each Pony. Note : non dictionary words are any not present in the words_alpha.txt @ https://github.com/dwyl/english-words. Uses this data to filter out the non-english words.










