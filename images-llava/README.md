# llama.cpp + LLaVA
## [LLaVA - Large Language and Vision Assistant](https://llava-vl.github.io/)

## Setup
Use `llama.cpp` (LLaMA + friends inference in plain C/C++ with no extra 
dependencies, using GGUF models) from https://github.com/ggerganov/llama.cpp

`llama.cpp` recently gained the ability to work with 
[LLaVA](https://llava-vl.github.io/) image models as well.

Clone the https://github.com/ggerganov/llama.cpp repo, then follow the
steps at https://github.com/ggerganov/llama.cpp#build

## Model
Needs a GGUF format LLaVA model and mmproj. These are available from
https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main

You need the `mmproj-model-f16.gguf` mmproj file. For the main model, if
you have the memory you can use the full `ggml-model-f16.gguf` model,
but likely you want one of the q# quantised smaller forms like
`ggml-model-q4_k.gguf`

## Demo 1 - Image description / captioning
`llama.cpp` with LLaVA provides "chat with my image", where similar to a
LLaMA-like model you can ask natural language questions of the model,
getting back natural language answers.

A prompt like *please describe the image in detail* will get a full
description of the image, suitable for indexing or captioning.

This assumes `llama.cpp` was cloned into `/models/llama.cpp`, the
LLaVA models are in `/models/llava`, and you want all your pictures
describing.

```
#!/bin/bash

PROMPT="please describe the image in detail"

LLAVA=/models/llama.cpp
MODEL=../llava/ggml-model-q4_k.gguf
PROJ=../llava/mmproj-model-f16.gguf

for i in ~Pictures/*.jpg; do 
  echo $i
  ${LLAVA}/llava-cli -t 8 -m ${LLAVA}/${MODEL} \
    --mmproj ${LLAVA}/${PROJ} --temp 0.1 -p "$PROMPT" \
    --image $i
  echo ""
  sleep 4
done
```

## Demo 2 - OCR
A prompt of *read the text from this image* will trigger OCR of the image,
but will also return some descriptions around it...

Further prompt engineering will be required!
