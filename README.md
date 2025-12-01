
# Repeating the results

Scripts for repeating the experiments in [\[1\]](#ref1).

## Install the prediction performances calculating codes (requires an environment with python>=3.11 and pip)
`pip install git+https://github.com/TurkuML/IC-index-experiments`

### Dependencies (automatically installed by pip)
- ic_index>=0.1.3
- numpy>=2.0.0
- pandas>=2.3
- scipy>=1.16

## Calculate prediction performances from real affinity values and the predicted ones

### Download data and precomputed affinity predictions
1. Download data files and place them in a folder "Data sets"
    * Davis et al. and Metz et al.: https://staff.cs.utu.fi/~aatapa/data/DrugTarget/
    * Merget et al.: https://staff.cs.utu.fi/~aatapa/data/Merget_et_al_2017/
    * KiBA: https://github.com/hkmztrk/DeepDTA/tree/master/data/kiba
    * Ion Channel, Enzymes, GPCR: http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/
1. Download the predictions from https://staff.cs.utu.fi/~aatapa/data/IC-index_predictions/IC-index%20-%20experiment%20predictions.zip and extract. 
    * This will create a folder named as "Predictions"

### Run from Python interpreter

```
from ic_index_experiments import performance
performance.calculate_performances()
```


## References:

\[1\] Pahikkala, T., Numminen, R., Movahedi, P., Karmitsa, N., & Airola, A. (2025). [Interaction Concordance Index: Performance Evaluation for Interaction Prediction Methods](https://arxiv.org/abs/2510.14419). arXiv preprint arXiv:2510.14419. <a name="ref1"></a>

