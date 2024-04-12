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
The directory containing both `tgw` and `qvlm` is referred to as the top-level directory.

2. Choose a dataset to evaluate on:
   - **For VQA_V2**:
     1. Make sure the images and questions are present in `qvlm/datasets/VQA_V2`
     2. Copy the [run_vqav2.ipynb](eval/script_generators/run_vqav2.ipynb) notebook to the top-level directory and run it
     3. Change model parameters if needed
     4. Run all cells until the `nbconvert` cell to get a script which can be run
        - This also generates a SCITAS-compatible job script
     5. These scripts should be run from the top-level directory
     - For evaluation, the output of this job should be converted to a .json file containing a single array, with one object for each line of the .jsonl file. The accuracy metrics can then be obtained using the VQA-V2 scripts provided by the original authors.
   
   - **For SEED**:
     1. Make sure the images and questions are present in `qvlm/datasets/SEED`
     2. Copy the [run_seed.ipynb](eval/script_generators/run_vqav2.ipynb) notebook to the top-level directory and run it
     3. Change model parameters if needed
     4. Run all cells until the `nbconvert` cell to get a script which can be run
        - This also generates a SCITAS-compatible job script
     5. These scripts should be run from the top-level directory