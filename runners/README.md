# Model runners

Here is a list of different ways of running models. If a model requires
one of these runners, an accompanying connector should be implemented in [connectors](../eval/connectors/)

## LLamafile
> Get the executable [here](https://github.com/Mozilla-Ocho/llamafile)

Example command:
```bash
./llamafile -ngl 9999 \
    -m llava-v1.5-vicuna-13b/ggml-model-f16.gguf \
    --mmproj llava-v1.5-vicuna-13b/mmproj-model-f16.gguf
```

Based on llama.cpp (see below). Enables running a .gguf model as a single executable + creates an HTTP server exposing a REST API for tasks.

## llama.cpp
> See github page [here](https://github.com/ggerganov/llama.cpp)

## LM Studio
> ⚠️ Requires GUI

> Download from [here](https://lmstudio.ai)

Enables running a model on a local server, behind an OpenAI API.