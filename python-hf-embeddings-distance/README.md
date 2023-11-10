# "Poor man's Vector DB with Python"
## HuggingFace embeddings, plus NumPy python script 

Use a model from HuggingFace to compute the embeddings

Few lines of Python numpy to compute the cosine similarity between embeddings

Not intended for production! 

25 lines of Python, 25 lines of YAML, if you need custom code it isn’t hard

Also shows how to use NumPy to work with the embeddings JSON

## Running locally
This uses the [Multilingual-E5-small](https://huggingface.co/intfloat/multilingual-e5-small)
embedding from Hugging Face, which works on a range of languages, and should 
place similar words from different languages in into similar embeddings.

```
ln -s ~/.langstream/ghrepos/LangStream/langstream/main/examples/ examples

export HUGGING_FACE_PROVIDER=local
export HUGGING_FACE_EMBEDDINGS_MODEL=multilingual-e5-small
export HUGGING_FACE_EMBEDDINGS_MODEL_URL=djl://ai.djl.huggingface.pytorch/intfloat/multilingual-e5-small

langstream docker run test -app hf-embeddings-distance -i examples/instances/kafka-kubernetes.yaml -s examples/secrets/secrets.yaml
```

## Based on
 * https://github.com/LangStream/langstream/tree/main/examples/applications/compute-hugging-face-embeddings
 * https://github.com/LangStream/langstream/tree/main/examples/applications/python/python-processor-embeddings
