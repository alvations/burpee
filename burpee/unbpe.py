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
Applies the Byte Pair Encoding uncompression to an input file.
"""

from __future__ import print_function

import io
import re
from tqdm import tqdm

rulefile = 'bpe-rules.trg'
compressfile = 'train.compressed.trg'

with io.open(compressfile, 'r', encoding='utf8') as fin:
    text = fin.read()

with io.open(rulefile, 'r', encoding='utf8') as fin:
    rules = reversed(fin.readlines())

for i, rule in tqdm(enumerate(rules)):
    #print (i, line.strip().split('\t'))
    source, trg = rule.strip().split('\t')
    text = text.replace(source, trg)

#text = text.replace(u'\n ', '\n')
#text = re.sub(r'[ \ue000]+', lambda m: ' ' if '\ue000' in m.group() else '_ _', text)
#text = text.replace('  ', ' ')
#print (text)

# Display
text = text.replace(u'\n ', '\n')
text = text.replace(u' ', '')
text = text.replace(u"\uE000", u' ')
text = text.replace(u'  ', u' ')
print (text)
