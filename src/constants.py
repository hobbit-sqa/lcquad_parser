# -*- coding: utf-8 -*-

import os

HOME_DIR = os.path.expanduser("~")
DEFAULT_DATA_DIR = HOME_DIR

DATA_FILE = os.path.join(DEFAULT_DATA_DIR, 'Lcquad_data.xlsx')
OUTPUT_DATA_FILE = os.path.join(DEFAULT_DATA_DIR, 'questions.json')
OUTPUT_SORTED_DATA_FILE = os.path.join(DEFAULT_DATA_DIR, 'questions_sorted.json')

SPARQL = 'SPARQL'
ORIGINAL = 'Original Question'
MODIFIED = 'Paraphrased Question'
COMMENTS = 'Comments/Remark'
METRICS = 'Metrics'
VECS = 'VectorExtremaCosineSimilarity'