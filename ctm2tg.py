#!/usr/bin/env python

import csv, sys, os
from praatio import tgio

def readCSV(filename):
    with open(filename, 'rb') as fileobj:
        out = list(csv.reader(fileobj, delimiter=' '))
    return out 

def csv2tgdict(ctmlist):
    out = {}
    for row in ctmlist:
        if row[0] not in out:
            out[row[0]] = []
        segment = (row[2], str(float(row[2]) + float(row[3])), row[4])
        out[row[0]].append(segment)
    return out

def wavscp2dict(wavscp):
    out = {}
    for row in wavscp:
        out[row[0]] = row[1]
    return out

def ctm2tg(wavdir, outdir):
    print "Converting ctm files to Praat Textgrids...",
    words = readCSV(os.path.join(outdir, 'wordlvl.ctm'))
    phones = readCSV(os.path.join(outdir, 'phonelvl.ctm'))
    word_dict = csv2tgdict(words)
    phone_dict = csv2tgdict(phones)
    wavscp = wavscp2dict(readCSV(os.path.join(outdir, 'wav.scp')))
    if not os.path.exists(os.path.join(outdir, 'tg')):
        os.makedirs(os.path.join(outdir, 'tg'))
    for utt in wavscp.keys():
        tg = tgio.Textgrid()
        wordTier = tgio.IntervalTier('words', word_dict[utt], 0, pairedWav=wavscp[utt])
        phoneTier = tgio.IntervalTier('phones', phone_dict[utt], 0, pairedWav=wavscp[utt])
        tg.addTier(wordTier)
        tg.addTier(phoneTier)
        tg.save(os.path.join(outdir, 'tg', utt + '.TextGrid'))
    print "stored in " + os.path.join(outdir, 'tg')

def main():
    if (len(sys.argv) < 3):
        print "Usage: %s <wavdir> <datadir>" % (sys.argv[0])
        exit(1)
    wavdir = sys.argv[1]
    outdir = sys.argv[2]
    ctm2tg(wavdir, outdir)

if __name__ == '__main__':
    main()
