# Quantization for Vision-Language Models

## Comparative evaluation

See [Evaluation](/eval/EVALUATION.md).

### Prerequisites:
1. Clone `text-generation-webui` to a directory called `tgw` next to this one
```
├── qvlm
│   ├── this README.md
├── tgw
```
2. Choose a dataset to evaluate on:
   - For VQA_V2:
     1. Open the [run_vqav2.ipynb](eval/script_generators/run_vqav2.ipynb) notebook
     2. Change model parameters if needed
     3. Run all cells until the `nbconvert` cell to get a script which can be run
        - This also generates a SCITAS-compatible job script 