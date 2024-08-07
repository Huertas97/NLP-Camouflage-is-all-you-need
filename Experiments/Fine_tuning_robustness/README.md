# Information

This folder contains the code for the experiments for the fine-tuning _static_ and _dynamic_ camouflage. The experiments are used to evaluate the robustness of the model against camouflage adversarial attacks. The experiments are conducted using the `transformers` library from Hugging Face, and the `pyleetspeak` library for generating the camouflage. The experiments are conducted using the `Spacy` library for the data processing and the `Pytorch` library for the training of the model.


In the `Results` folder you will find the non-grouped test results for the experiments for each model architecture (encoder-only, decoder-only, and encoder-decoder), and in the `configs` folder you will find the configuration files used for the the fine-tuning experiments. The configuration files are used to ensure reproducibility and ease of use. The configuration files contain the parameters used for the experiments, such as the training parameters, the model parameters, and the levels of complexity. The configuration files are used to ensure reproducibility and ease of use.


## Configs 

The `configs` folder contains the configuration files for the experiments. These files contain the parameters used for the experiments, such as the training parameters, the model parameters, and the levels of complexity. The configuration files are used to ensure reproducibility and ease of use.


Three main configuration files are used for the experiments, the naive for training the model with non-camouflaged data, the _static_ file for training the model with static camouflaged data, and the _dynamic_ file for training the model with dynamic camouflaged data. For these two latest types of files, the are a version for each ratio of data instances camouflaged (0.1, 0.25, 0.5, 0.75, 1). 




### Static Camouflage

These files contain the parameters used for training the model with static camouflaged data. The static camouflage is previously generated using the `pyleetspeak` library. This are the main parameters from the config file that determine the static camouflage:

```yaml
[paths]
train = "./Spacy_Data/Offen_SemEval_2019/Leet_Data/10_per/train.spacy" # path to the already predefined camouflage training data
dev = "./Spacy_Data/Offen_SemEval_2019/Leet_Data/10_per/dev.spacy" # path to the already predefined camouflage development data
```


### Dynamic Camouflage

The main difference between the dynamic and static camouflage is that the dynamic camouflage is generated on the fly, while the static camouflage is generated before the training. The dynamic camouflage is generated using the `pyleetspeak` library, with the augmentation function from `functions.py`, which generates a new camouflage version for each batch of data. The main parameters for dynamic camouflage are:

```yaml
[paths]
train = "./Spacy_Data/Offen_SemEval_2019/Original_Data/train_offen.spacy" # path to the original training data to be augmented in each batch
dev = "./Spacy_Data/Offen_SemEval_2019/Original_Data/dev_offen.spacy" # path to the original development data to be augmented in each batch


[corpora.train.augmenter]
@augmenters = "wordcamouflage_augmenter.v1"
level = 0.1
extractor_type = "yake"
```


## Levels of Complexity

In the experiments, different levels of complexity are used to evaluate the robustness of the model. These levels are highly customizable and can be adjusted to fit the needs of the user, as indicated in [pyleetspeak](https://github.com/Huertas97/pyleetspeak). 
The levels of complexity used are as follows:

|         | **Parameters**                                                                                                                                                                                                                                                                                                                                                       |
| :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Level 1 | max\_top\_n=[5, 20] <br> leet\_punt\_prb=0\.9 <br> leet\_change\_prb=0.8 <br> leet\_change\_frq=0.8 <br> leet\_uniform\_change=0.5 <br> method=["basic\_leetspeak"]                                                                                                                                                                                                  |
| Level 2 | max\_top\_n=[5,20] <br>  leet\_punt\_prb=0\.9 <br>  leet\_change\_prb=0.5 <br>  leet\_change\_frq=0.8 <br>  leet\_uniform\_change=0.6 <br>  punt\_hyphenate\_prb=0.7 <br>  punt\_uniform\_change\_prb=0.95 <br>  punt\_word\_splitting\_prb=0.8 <br> method=[ïntermediate\_leetspeak "punct\_camo"]                                                                  |
| Level 3 | max\_top\_n=[5,20] <br>  leet\_punt\_prb=0\.4 <br>  leet\_change\_prb=0.5 <br>  leet\_change\_frq=0.8 <br>  leet\_uniform\_change=0.6 <br>  punt\_hyphenate\_prb=0.7 <br>  punt\_uniform\_change\_prb=0.95 <br>  punt\_word\_splitting\_prb=0.8 <br>  inv\_max\_dist=4 <br>  inv\_only\_max\_dist\_prb=0.5 <br> method=[ädvanced\_leetspeak "punct\_camo ïnv\_camo"] |


## Training Parameters

All models are trained using the same training parameters, using the same pre-training checkpoint for comparability.

The training parameters are as follows:
| Parameter                  | Value                              |
| -------------------------: | ---------------------------------: |
| learning rate        | initial\_rate = 0\.00005     |
|                      | total\_steps = 20000         |
|                      | scheduler = warmup\_linear   |
|                      | warmup\_steps = 250          |
| epochs               | max\_epochs = 0              |
|                      | max\_steps = 20000           |
|                      | patience = 1600              |
| accumulate\_gradient | 3                            |
| optimizer            | AdamW                        |
|                      | batch\_size = 128            |
|                      | beta = 10\.9                 |
|                      | beta2 = 0\.999               |
|                      | eps = 1e-8                   |
|                      | grad\_clip = 1               |
|                      | l2 = 0\.01                   |
|                      | l2\_is\_weight\_decay = true |
| eval\_frequency      | 200                          |
| dropout              | 0\.1                         |

More information on the training parameters can be found in the config file in the `configs` folder. The use of config files is for reproducibility and ease of use.
