

# IC-Index Experiments

The **Interaction Concordance Index (IC-Index)** is a novel metric for evaluating interaction prediction methods. This repository allows users to recompute the drug-target affinity prediction performance results reported in  **[Pahikkala et al. (2025)](#ref1)**. The Python package implementing the IC-Index itself is available in a separate repository: [ic_index](https://github.com/TurkuML/Interaction-Concordance-Index).

## **Requirements**
The following dependencies are **automatically installed** with the package:
- `Python` ≥ 3.11
- `ic_index` ≥ 0.1.3
- `numpy` ≥ 2.0.0
- `pandas` ≥ 2.3
- `scipy` ≥ 1.16

## **Installation**
1. **Set up a Python environment** (e.g., using Anaconda or `venv`):
   ```bash
   conda create -n ic_index_experiments_env python=3.11
   conda activate ic_index_experiments_env
   ```

2. **Install the package** from GitHub:
   ```bash
   pip install git+https://github.com/TurkuML/IC-index-experiments
   ```

## **Data Preparation**
### **Folder Structure**
Ensure your working directory contains:
```
.
├── Data sets/          # Ground truth data (downloaded below)
├── Predictions/        # Precomputed predictions (extracted below)
└── (other files)
```

### **1. Download Ground Truth Data**
Place the following datasets in `Data sets/`:
- [Davis et al. & Metz et al.](https://staff.cs.utu.fi/~aatapa/data/DrugTarget/)
- [Merget et al.](https://staff.cs.utu.fi/~aatapa/data/Merget_et_al_2017/)
- [KiBA](https://github.com/hkmztrk/DeepDTA/tree/master/data/kiba)
- [Ion Channel, Enzymes, GPCR](http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/)

### **2. Download Precomputed Predictions**
Download and extract:
- [IC-Index Experiment Predictions](https://staff.cs.utu.fi/~aatapa/data/IC-index_predictions/IC-index%20-%20experiment%20predictions.zip)
  (This will create the `Predictions/` folder.)

## **Running the Experiments**
Execute the performance calculation in Python:
```python
from ic_index_experiments import performance
performance.calculate_performances()  # Results will be saved to performances.csv
```

## **License**
This project is licensed under the [MIT License](LICENSE).

## **References**
<a name="ref1"></a>
[1] Pahikkala, T., Numminen, R., Movahedi, P., Karmitsa, N., & Airola, A. (2025). [Interaction Concordance Index: Performance Evaluation for Interaction Prediction Methods](https://arxiv.org/abs/2510.14419). *arXiv preprint arXiv:2510.14419*.

