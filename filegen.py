#!/usr/bin/env python

import sys
import os
from glob import glob

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            if filepath.endswith('.wav') or filepath.endswith('.flac'):
                file_paths.append(filepath)  # Add it to the list.
    return file_paths  # Self-explanatory.

def get_wavscp(wavs):
    out = {}
    for path in wavs:
        _, wav = os.path.split(path)
        wav = wav.strip('.wav')
        out[wav] = path
    return out

def get_spk2utt(wavscp):
    out = {}
    for wav in wavscp.keys():
        spk, utt = wav.split('_')
        if spk in out:
            out[spk].append(wav)
        else:
            out[spk] = [wav]
    return out

def get_utt2spk(spk2utt):
    out = {}
    for spk, utts in spk2utt.iteritems():
        for utt in utts:
            out[utt] = spk 
    return out

def write_scp(dirname, filename, data):
    f = open(os.path.join(dirname, filename), 'w')
    for key, val in iter(sorted(data.iteritems())):
        if type(val) == list:
            val = ' '.join(sorted(val))
        f.write("%s %s\n" % (key, val))

def filegen(wavdir, outdir):
    wavs = get_filepaths(wavdir)
    wavscp = get_wavscp(wavs)
    # print wavscp
    write_scp(outdir, 'wav.scp', wavscp)
    spk2utt = get_spk2utt(wavscp)
    # print spk2utt
    write_scp(outdir, 'spk2utt', spk2utt)
    utt2spk = get_utt2spk(spk2utt)
    # print utt2spk
    write_scp(outdir, 'utt2spk', utt2spk)

def main():
    if (len(sys.argv) < 3):
        print "Usage: %s <wavdir> <outdir>" % (sys.argv[0])
        exit(1)
    wavdir = sys.argv[1]
    outdir = sys.argv[2]
    filegen(wavdir, outdir)

if __name__ == '__main__':
    main()
