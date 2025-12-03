
# Scripts for repeating the results presented in [\[1\]](#ref1)

Calculation of the drug-target affinity prediction performances presented in [\[1\]](#ref1) can be repeated by the following steps:

## Install the Python module for calculating the prediction performances (requires an environment with python>=3.11 and pip)
`pip install git+https://github.com/TurkuML/IC-index-experiments`

### Dependencies (automatically installed by pip)
- ic_index>=0.1.3
- numpy>=2.0.0
- pandas>=2.3
- scipy>=1.16

## Download data and precomputed affinity predictions

### Download data files

Data files available from the following links contain observed drug-target affinity strength values forming the ground truth. Place them in a folder "Data sets".

    * Davis et al. and Metz et al.: https://staff.cs.utu.fi/~aatapa/data/DrugTarget/
    * Merget et al.: https://staff.cs.utu.fi/~aatapa/data/Merget_et_al_2017/
    * KiBA: https://github.com/hkmztrk/DeepDTA/tree/master/data/kiba
    * Ion Channel, Enzymes, GPCR: http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/


### Download precomputed affinity predictions

Download the following file:
    * https://staff.cs.utu.fi/~aatapa/data/IC-index_predictions/IC-index%20-%20experiment%20predictions.zip
and extract its contents. This will create a folder named as "Predictions".

## Run the module from Python interpreter

```
from ic_index_experiments import performance
performance.calculate_performances()
```


## References:

\[1\] Pahikkala, T., Numminen, R., Movahedi, P., Karmitsa, N., & Airola, A. (2025). [Interaction Concordance Index: Performance Evaluation for Interaction Prediction Methods](https://arxiv.org/abs/2510.14419). arXiv preprint arXiv:2510.14419. <a name="ref1"></a>

