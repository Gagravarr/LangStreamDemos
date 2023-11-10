from langstream import SimpleRecord, Processor

import json, numpy

def _from_json(record):
    "Process the JSON and convert the embeddings to NumPy"
    data = json.loads(record.value())
    if "question" in data and "embeddings" in data:
        emb = numpy.asarray(data["embeddings"])
        return (data["question"], emb)
    raise Exception("Not in the correct format, found %s" % data.keys())

def _compare(a,b):
    "Compute the Cosine Distance between two embeddings"
    cos_sim = numpy.dot(a,b) / (
        numpy.linalg.norm(a) * numpy.linalg.norm(b) )
    return cos_sim

# Poor man's in-memory vector storage
_seen = []


class Similarity(Processor):
    def process(self, record):
        question, embedding = _from_json(record)
        _seen.append( (question,embedding) )

        if len(_seen) < 2:
            resp = "I've remembered about '%s'. Your embedding has %d dimensions" % (question, len(embedding))
        else:
            pq, pe = _seen[-2]

            cos_sim = _compare(embedding, pe)
            resp = "The similarity between\n   %s\nand\n    %s\nis %0.3f" % (question, pq, cos_sim)

        return [SimpleRecord(resp, headers=record.headers())]
