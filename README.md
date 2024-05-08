# NLP-Camouflage-is-all-you-need emojis 🦎🤖🕵️‍♂️📝
Code for the research work titled: "_Camouflage is all you need: Evaluating and Enhancing Transformer Models Robustness Against Camouflage Adversarial Attacks_"

## Information

This repository contains the code for the experiments in the paper "_Camouflage is all you need: Evaluating and Enhancing Transformer Models Robustness Against Camouflage Adversarial Attacks_". 

The subfolder organization is as follows:

- **Examples**: Contains real examples of word camouflage from social media.
- **Experiments**: Contains the code for the experiments in the paper.

The structure of the repository is as follows:

```bash
- Examples/
  - Real_examples.md
- Experiments/
  - README.md
  - Tokenizers/
    - Tokenizers_overlap.ipynb
    - all_shared_tokens_seed_42.parquet
    - pyleetspeak/
  - Ideal_External_Filters/
    - NER_filter_resilience.ipynb
  - Fine_tuning_robustness/
    - README.md
    - functions.py
    - Fine-tuning_experiments.ipynb
    - Results/
      - encoder-results.csv
      - decoder-results.csv
      - encoder-decoder-results.csv
    - configs/
  - Spacy_Data/
    - Offen_SemEval_2019/
      - Leet_Data/
        - Level_1.2/
        - Level_3.1/
        - Level_2.2/
        - Level_2.1/
        - Level_3.2/
        - Level_1.1/
        - Level_Mixed/
      - Ori_Data/
        - dev.spacy
        - train.spacy
        - test.spacy
        - .ipynb_checkpoints/
```

In each subfolder you will find more information about the experiments and the code used for the experiments.

## Setup 

To ensure you have a suitable environment for running the experiments and examples provided in this repository, we recommend setting up a virtual environment using either `venv` or `conda`.

### Using `venv`

If you prefer to use Python's built-in virtual environments:

1. Navigate to the project's root directory.
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. For NLP-specific packages like Spacy, follow the detailed installation instructions available at [Spacy Usage Documentation](https://spacy.io/usage).

### Using `conda`

For those who prefer using Conda environments, which can manage packages and environments more comprehensively:

1. Create a new Conda environment:
    ```bash
    conda env create -f environment.yml
    ```
2. Activate the Conda environment:
    ```bash
    conda activate your-env-name
    ```
3. Ensure all dependencies are installed as specified in the `environment.yml` file.

For NLP-specific packages like Spacy, follow the detailed installation instructions available at [Spacy Usage Documentation](https://spacy.io/usage).




# Citation

```In progress```
