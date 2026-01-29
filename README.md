

# IC-Index Experiments
This repository allows users to recompute the drug-target affinity prediction performance results reported in  **[Pahikkala et al. (2025)](#ref1)**. The Python package implementing the IC-Index itself is available as an installable Python package in Python Package Index at [https://pypi.org/project/ic-index/](https://pypi.org/project/ic-index/) and its development version in a separate github repository: [ic_index](https://github.com/TurkuML/Interaction-Concordance-Index).

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
├── Predictions/        # Precomputed predictions (extracted below)
└── (other files)
```

### **Download ground truth affinity values, precomputed predictions and other metadata**
Download and extract the data from:
- [https://doi.org/10.5281/zenodo.18140023](https://doi.org/10.5281/zenodo.18140023)
  (This will create the `Predictions/` folder.)

## **Repetition of the results**
Execute the prediction performance estimation script in Python interpreter:
```python
from ic_index_experiments import performance
performance.calculate_performances()  # Results will be saved to performances.csv
```

## **License**
This project is licensed under the [MIT License](LICENSE).

## **References**
<a name="ref1"></a>
[1] Pahikkala, T., Numminen, R., Movahedi, P., Karmitsa, N., & Airola, A. (2025). [Interaction Concordance Index: Performance Evaluation for Interaction Prediction Methods](https://arxiv.org/abs/2510.14419). *arXiv preprint arXiv:2510.14419*.

