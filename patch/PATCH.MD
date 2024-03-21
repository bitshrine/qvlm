# Patching `text-generation-webui`

There are some issues with the pipeline due to out-of-date code or bugs in the current `text-generaton-webui` implementation. Below is a list of issues and their fixes.

| Source                  | Issue                                                                                          | Fix                                                                                     |
|-------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| AutoGPTQ                | No support for model sharding in the version installed with `text-generation-webui` by default | In the `installer_files/env` conda env, remove and redownload `auto-gptq` through `pip` |
| `text-generation-webui` | Explicitly does not allow loading several AutoGPTQ model shards.                               | Apply patch from [`modules/AutoGPTQ_loader.py`](modules/AutoGPTQ_loader.py)               |
|`text-generation-webui` LLaVA pipeline| Does not handle grayscale images (throws an error and shuts down the server)|Apply patch from [`extensions/multimodal/pipelines/llava.py`](extensions/multimodal/pipelines/llava.py)|

# Other issues
Applying the above patches and using the LLaVA-v1.5-13B model GPTQ-quantized to 8 bits by TheBloke still results in very poor quality in generated responses, as opposed to the 4 bits model which seems to perform better. 
