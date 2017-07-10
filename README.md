# ASR Scripts

This project aims to simplify using Kaldi for speech recognition and alignment.
It currently works with the [ASpIRE pre-trained model](http://kaldi-asr.org/models.html), although the scripts can be extended easily to work with different/custom trained models.

## Installation

### Prerequisites

* Compiled Kaldi instance ([instructions](https://github.com/kaldi-asr/kaldi/blob/master/INSTALL))
* ASpIRE chain pre-trained model ([download](http://kaldi-asr.org/models.html), [preparation](https://chrisearch.wordpress.com/2017/03/11/speech-recognition-using-kaldi-extending-and-using-the-aspire-model/))
* For generating TextGrid alignment files, you will need to install the python package for [praatIO](https://github.com/timmahrt/praatIO).
If you do not need TextGrid files, comment out the function call from `aspire.py`.

### Download scripts

* `$ git clone https://github.com/jailuthra/asr`
* Place the scripts in `kaldi/egs/aspire/s5` directory.

#### Input audio constraints
Mono PCM wave files, 16-bit sample size, 8KHz sampling rate.

## Scripts

* **`aspire.py`**: Decodes and aligns the wav files using the pre-trained model, calls the other scripts
* `filegen.py`: Generates reqd. speaker-id, utterance-id information files using the wav files
* `id2phone.py, id2word.py`: Convert phone/word ids in ctm output, to actual phones/words
* `ctm2tg.py`: Convert ctm output to Praat TextGrid files

## Usage

1. Create a directory with all your wav files.
2. File naming convention is `<speaker_id>_<utterance_id>.wav` for example `0001_0001.wav`, `0001_0002.wav`.
3. Call the aspire script: `./aspire.py <wavdir> <outputdir>`.
4. It will generate text transcriptions and alignment files in the output directory.
