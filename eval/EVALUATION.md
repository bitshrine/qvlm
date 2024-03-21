# Evaluation

Across the different VLM architectures being developed, there are a variety of setups needed to run the models and evaluate them. Thankfully, many methods allow the model to be run interactively through a REST API. The current repository contains code to abstract the particularities of each setup away: the model is run on a server, and an evaluator instance connects to the server to perform model evaluation.

> The evaluation server currently being used is [text-generation-webui](https://github.com/oobabooga/text-generation-webui) as it fulfills the following criteria:
> - Supports a variety of model backends, which is useful to evaluate different model architectures
>  - Also supports AutoGPTQ / AWQ models, meaning we can run baseline evaluations on those methods
> - Supports multimodality
> - Provides a REST API which we can query programmatically to run evaluations automatically.
>
> See [PATCH.md](/patch) for an overview of current issues with `text-generation-webui`.

|Project|Backends|Multimodality|Can be run automatically / without UI|
|--|--|--|--|
|text-generation-webui|Transformers, llama.cpp, ExLlamaV2, AutoGPTQ, AutoAWG, GPTQ-for-LLaMa, CTransformers, QuIP#|✅|✅ Through REST API|
|llamafile / llama.cpp|llama.cpp (supports .gguf/.ggml files)|✅|✅ Through REST API|

> Note: to use one of these projects as a model server, an accompanying connector needs to be implemented in [connectors](connectors/)