#!/usr/bin/env python -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Rakuten, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Applies the Byte Pair Encoding compression to an input file.
"""

from __future__ import print_function

import io
import time
import sys
from collections import Counter

from tqdm import tqdm

infile = 'big.txt'
jump = 500          # no. of replacements per pass.
unused_char = 5632  # max no. of unused characters to be used for replacements.

rulefile = 'bpe-rules.trg'
compressfile = 'train.compressed.trg'

with io.open(rulefile, 'w', encoding='utf8') as rule_fout, \
io.open(compressfile, 'w', encoding='utf8') as fout:
    with io.open(infile, 'r', encoding='utf8') as fin:
        text = fin.read().replace(u' ', u"\uE000")
        unused_char = int(unused_char / jump) * jump
        for i in tqdm(range(1, unused_char, jump)):
            ##start = time.time()
            _bigrams = filter(lambda x: '\n' not in x,
                              zip(*[text[i:] for i in range(2)]))
            bigram_counter = Counter(_bigrams).most_common(jump)
            ##print (time.time() - start)
            #print (bigram_counter)
            for k, (_bigram, _count) in enumerate(bigram_counter):
                unused_char = chr(ord(u'\uE000') + i + k)
                _bigram_str = ''.join(_bigram)
                text = text.replace(_bigram_str, unused_char)
                print ('\t'.join([unused_char, _bigram_str]), end='\n', file=rule_fout)
        print (' '.join(text).replace(' \n ', '\n'), file=fout)
