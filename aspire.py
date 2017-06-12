#!/usr/bin/env python

import subprocess, shlex

command = '''/Users/darkapex/git/kaldi/src/online2bin/online2-wav-nnet3-latgen-faster
  --online=false
  --do-endpointing=false
  --frame-subsampling-factor=3
  --config=exp/tdnn_7b_chain_online/conf/online.conf
  --max-active=7000
  --beam=15.0
  --lattice-beam=6.0
  --acoustic-scale=1.0
  --word-symbol-table=exp/tdnn_7b_chain_online/graph_pp/words.txt
  exp/tdnn_7b_chain_online/final.mdl
  exp/tdnn_7b_chain_online/graph_pp/HCLG.fst
  'ark:echo utterance-id1 utterance-id1|'
  'scp:echo utterance-id1 %s |'
  ark:/dev/null
'''

# Take wav file and get text transcription
def decode(wavfile):
    args = shlex.split((command % (wavfile)))
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = proc.communicate()[1]
    for line in output.splitlines():
        if line.startswith('utterance-id1 '):
            return line.strip('utterance-id1 ')
    return 'Unable to get text'

def main():
    out = decode('~/weather.wav')
    print(out)

if __name__ == '__main__':
    main()
