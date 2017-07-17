#!/usr/bin/env python

import csv, sys

def id2word(wordstxt, ctmfilename):
    '''Replace word-IDs in CTM file, with actual words'''
    with open(wordstxt, 'rb') as wordfile:
        words = list(csv.reader(wordfile, delimiter=' '))

    with open(ctmfilename, 'rb') as ctmfile:
        ctm = list(csv.reader(ctmfile, delimiter=' '))

    id2word = {}
    for row in words:
        id2word[row[1]] = row[0]

    for word in ctm:
        word_id = word[-1]
        word_name = id2word[word_id]
        word[-1] = word_name
    
    with open(ctmfilename, 'wb') as ctmfile:
        ctmout = csv.writer(ctmfile, delimiter=' ')
        for word in ctm:
            ctmout.writerow(word)

def main():
    if (len(sys.argv) < 1):
        print "Usage: %s <wordlvl.ctm> [<words.txt>]" % (sys.argv[0])
        exit(1)
    ctmfilename = sys.argv[1]
    wordstxt = 'exp/tdnn_7b_chain_online/graph_pp/words.txt' 
    if (len(sys.argv) == 3):
        wordstxt = sys.argv[2]
    id2word(wordstxt, ctmfilename)

if __name__ == '__main__':
    main()
