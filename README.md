
# Scripts for repeating the results presented in [\[1\]](#ref1)

Repeat the calculation of drug-target affinity prediction performances as presented in [\[1\]](#ref1) as follows:

#### 1. Install the results repeating Python module for recomputation, 

Set up a clean Python environment, e.g. in Anacoda and install python>=3.11 and pip into it. Then install this git repository via the command:

`pip install git+https://github.com/TurkuML/IC-index-experiments`

This will automatically install the following dependencies:

    * ic_index>=0.1.3
    * numpy>=2.0.0
    * pandas>=2.3
    * scipy>=1.16

#### 2. Download data and precomputed affinity predictions

Data files available from the following links contain observed drug-target affinity strength values forming the ground truth. Place them in a folder "Data sets".

    * Davis et al. and Metz et al.: https://staff.cs.utu.fi/~aatapa/data/DrugTarget/
    * Merget et al.: https://staff.cs.utu.fi/~aatapa/data/Merget_et_al_2017/
    * KiBA: https://github.com/hkmztrk/DeepDTA/tree/master/data/kiba
    * Ion Channel, Enzymes, GPCR: http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/

Download the following file containint the precomputed affinity predictions:

    * https://staff.cs.utu.fi/~aatapa/data/IC-index_predictions/IC-index%20-%20experiment%20predictions.zip

and extract its contents. This will create a folder named as "Predictions".

#### 4. Run the module from Python interpreter

```
from ic_index_experiments import performance
performance.calculate_performances()
```


## References:

\[1\] Pahikkala, T., Numminen, R., Movahedi, P., Karmitsa, N., & Airola, A. (2025). [Interaction Concordance Index: Performance Evaluation for Interaction Prediction Methods](https://arxiv.org/abs/2510.14419). arXiv preprint arXiv:2510.14419. <a name="ref1"></a>

