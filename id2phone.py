#!/usr/bin/env python

import csv, sys

def id2phone(phonestxt, ctmfilename):
    '''Replace phone-IDs in CTM file, with actual phones'''
    with open(phonestxt, 'rb') as phonefile:
        phones = list(csv.reader(phonefile, delimiter=' '))

    with open(ctmfilename, 'rb') as ctmfile:
        ctm = list(csv.reader(ctmfile, delimiter=' '))

    id2phone = {}
    for row in phones:
        id2phone[row[1]] = row[0]

    for phone in ctm:
        phone_id = phone[-1]
        phone_name = id2phone[phone_id]
        phone[-1] = phone_name
    
    with open(ctmfilename, 'wb') as ctmfile:
        ctmout = csv.writer(ctmfile, delimiter=' ')
        for phone in ctm:
            ctmout.writerow(phone)

def main():
    if (len(sys.argv) < 1):
        print "Usage: %s <phonelvl.ctm> [<phones.txt>]" % (sys.argv[0])
        exit(1)
    ctmfilename = sys.argv[1]
    phonestxt = 'exp/tdnn_7b_chain_online/phones.txt' 
    if (len(sys.argv) == 3):
        phonestxt = sys.argv[2]
    id2phone(phonestxt, ctmfilename)

if __name__ == '__main__':
    main()
