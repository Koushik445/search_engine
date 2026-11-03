"""
BM25 Inverted Index Implementation
"""

import math
from collections import defaultdict, Counter
import numpy as np

class BM25Index:
    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.doc_len = []
        self.avg_doc_len = 0.0
        self.doc_freqs = defaultdict(int)
        self.inverted_index = defaultdict(dict)  # token -> {doc_id: term_freq}
        self.num_docs = 0

    def fit(self, corpus_tokens: list[list[str]]):
        self.num_docs = len(corpus_tokens)
        self.doc_len = [len(doc) for doc in corpus_tokens]
        self.avg_doc_len = sum(self.doc_len) / max(1, self.num_docs)

        for doc_id, tokens in enumerate(corpus_tokens):
            tf = Counter(tokens)
            for token, freq in tf.items():
                self.inverted_index[token][doc_id] = freq
                self.doc_freqs[token] += 1

    def score(self, query_tokens: list[str]) -> np.ndarray:
        scores = np.zeros(self.num_docs, dtype=np.float32)
        for token in query_tokens:
            if token not in self.inverted_index:
                continue
            df = self.doc_freqs[token]
            idf = math.log(1.0 + (self.num_docs - df + 0.5) / (df + 0.5))
            for doc_id, tf in self.inverted_index[token].items():
                doc_l = self.doc_len[doc_id]
                numerator = tf * (self.k1 + 1.0)
                denominator = tf + self.k1 * (1.0 - self.b + self.b * (doc_l / self.avg_doc_len))
                scores[doc_id] += idf * (numerator / denominator)
        return scores

