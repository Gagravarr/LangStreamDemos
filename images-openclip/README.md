# clip.cpp + OpenCLIP

## Setup
Use `clip.cpp` (CLIP inference in plain C/C++ with no extra dependencies,
using GGUF models) from https://github.com/monatis/clip.cpp

Follow the building guide at
https://github.com/monatis/clip.cpp#building
(and note that you need to clone the repo with sub-modules as instructed!)

## Model
Needs a GGUF format clip model. You can either convert one, or download
a pre-trained one from Hugging Face from
https://huggingface.co/models?other=clip-cpp-gguf

See https://laion.ai/blog/large-openclip/#32b-samples-seen for details of
what the different models were train on/with.

## Demo 1 - Zero-shot classification
Provide `clip.cpp` a set of possible image classifications, in english text,
and have the probabilities of each returned.

This could be used to send different images down different processing routes
(eg if there's text do OCR, if there are people check for release forms), or
could be used for filtering, or many other things.

Tested with the `CLIP-ViT-L-14-laion2B-s32B-b82K_ggml-model-q5_1.gguf` model

This assumes `clip.cpp` was cloned into `/models/clip.cpp`, and you want 
your all your Pictures classified into *person*, *building* or *food*. 
Tweak paths and categories variables as needed!

```
#!/bin/bash
CATEGORIES="person building food"

CLIP=/models/clip.cpp
CMODEL=CLIP-ViT-L-14-laion2B-s32B-b82K_ggml-model-q5_1.gguf

# Build the command line options from the categories list
COPTS="--text "`echo "$CATEGORIES" | sed 's/ / --text /g'`

# Process all the JPEGs in your home/Pictures folder
for i in Pictures/*.jpg; do 
  echo $i
  ${CLIP}/build/bin/zsl -m ${CLIP}/models/${CMODEL} \
    -v 0 --image $i $COPTS
  echo ""
done
```

## Demo 2 - Embeddings
OpenCLIP has an embeddings space that works for both images and text. If
you generate embeddings for all your images, store those into your
Vector Database, you can then query for images matching an item or 
description!

This is a bit like a simple RAG for images + text

As with demo 1, tweak paths/models as needed. You would ideally feed the
embeddings generated into your Vector Database, eg via LangStream.

```
#!/bin/bash

CLIP=/models/clip.cpp
CMODEL=CLIP-ViT-L-14-laion2B-s32B-b82K_ggml-model-q5_1.gguf

pushd /tmp
for i in ~/Pictures/*; do 
  echo $i
  ${CLIP}/build/bin/extract -m ${CLIP}/models/${CMODEL} \
    -v 0 --image $i

  # Print the numpy embedding vectors
  EMB="img_vec_"`basename "$i"`".npy"
  python3 << EOF
import numpy
emb = numpy.load("$EMB")
print(emb)
EOF
  echo ""
done
popd
```
