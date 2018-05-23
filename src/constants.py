# -*- coding: utf-8 -*-

import os

HOME_DIR = os.path.expanduser("~")
DEFAULT_DATA_DIR = HOME_DIR

DATA_FILE = os.path.join(DEFAULT_DATA_DIR, 'Lcquad_data.xlsx')
OUTPUT_DATA_FILE = os.path.join(DEFAULT_DATA_DIR, 'questions.json')
OUTPUT_SORTED_DATA_FILE = os.path.join(DEFAULT_DATA_DIR, 'questions_sorted.json')
OUTPUT_QALD_FILE = os.path.join(DEFAULT_DATA_DIR, 'questions_qald.json')
LCQUAD_DATA_FILE = os.path.join(DEFAULT_DATA_DIR, "lcquad_qaldformat.json")
LCQUAD_MODIFIED_FILE = os.path.join(DEFAULT_DATA_DIR, "lcquad_modified.json")

SPARQL = 'SPARQL'
ORIGINAL = 'Original Question'
MODIFIED = 'Paraphrased Question'
COMMENTS = 'Comments/Remark'
METRICS = 'Metrics'
VECS = 'VectorExtremaCosineSimilarity'
GMS = 'GreedyMatchingScore'
EACS = 'EmbeddingAverageCosineSimilairty'


LIMIT = 1830
LANGUAGE_EN = 'en'
DATASET_ID = 'sqa_test'
ID='id'
QUESTION = 'question'
QUESTIONS = 'questions'
LANGUAGE = 'language'
STRING = 'string'
