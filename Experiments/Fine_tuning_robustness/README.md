## Information

This folder contains the code for the experiments in the paper "Camouflage is all you need: A Robust Model for Adversarial Examples" by Yiren Zhao, Yijie Guo, and Chao Zhang. The code is based on the code for the paper "Adversarial Examples Are Not Bugs, They Are Features" by Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Logan Engstrom, Brandon Tran, and Aleksander Madry.




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
