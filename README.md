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
    - Dynamic/
      - functions.py
    - Results/
      - encoder-results.csv
      - decoder-results.csv
      - encoder-decoder-results.csv
    - Static/
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


# Citation

```In progress```
