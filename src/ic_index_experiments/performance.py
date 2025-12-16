import numpy as np
import pandas as pd
from statistics import mode
from pathlib import Path
import ic_index
from scipy.stats import kendalltau

#Somer's D correlation coefficient as nonsymmetric Kendall's tau_c
def somersD(y, p):
    return kendalltau(y, p, variant='c')[0] / kendalltau(y, y, variant='c')[0]

#Concordance index as Somer's D correlation coefficient transformed between [0,1]
def cindex(y, p):
    if len(np.unique(p)) == 1:
        return 0.5
    else:
        return (somersD(y, p) + 1) / 2

#Helper function for drugwise or targetwise concordance index estimates.
def count_pairs(Y, P):
    correct = Y.astype(np.float64)
    predictions = P.astype(np.float64)
    assert len(correct) == len(predictions)
    C = np.array(correct).reshape(len(correct),)
    C.sort()
    pairs = 0
    c_ties = 0
    for i in range(1, len(C)):
        if C[i] != C[i-1]:
            c_ties = 0
        else:
            c_ties += 1
        pairs += i - c_ties
    return pairs

"""
Function for calculating drugwise or targetwise concordance index estimates. 

Input: performance measure function, arrays of labels, predictions and IDs that determine the group.

Output: prediction performance within the group measured by the given performance measure.
"""
def group_performance_normalized(measure, y, y_predicted, group_ids):
    n_concordant = 0
    n_pairs = 0
    for i in set(group_ids):
        y_subset = y[group_ids == i]
        y_predicted_subset = y_predicted[group_ids == i]
        if len(set(y_subset)) > 1:
            pairs = count_pairs(y_subset, y_predicted_subset)
            n_concordant += measure(y_subset, y_predicted_subset)*pairs
            n_pairs += pairs
    return(n_concordant / n_pairs)


"""
Function for calculating interaction concordance index, concordance index, 
as well as drugwise and targetwise concordance indices.

Input: A data frame where the first 4 columns are ID_d, ID_t, fold and Y.
The rest of columns are predictions made by different methods and settings.

Output: The function returns the lists of IC-indices and all variations of C-indices.
"""
def calculate_foldwise_IC_C_indices(df):
    folds = set(df['fold'])

    # Initialize lists for collecting the foldwise performance estimates.
    C_index_list = []
    C_d_index_list = []
    C_t_index_list = []
    IC_index_list = []

    for fold_id in folds:
        # Take a subset of data containing only rows related to the current fold.
        df_fold = df.loc[df['fold'] == fold_id,:]
        drug_inds_fold = df_fold.ID_d.values
        target_inds_fold = df_fold.ID_t.values
        Y_fold = df_fold.Y.values
        P_fold = df_fold.iloc[:,4:]

        C_indices_fold = []
        C_d_indices_fold = []
        C_t_indices_fold = []

        for m in range(P_fold.shape[1]):
            # Calculate global C-index.
            C_indices_fold.append(cindex(Y_fold, P_fold.iloc[:,m].values))
            # Calculate averaged drugwise C-index.
            C_d_indices_fold.append(group_performance_normalized(cindex, Y_fold, \
                                                                    P_fold.iloc[:,m].values, drug_inds_fold))
            # Calculate averaged targetwise C-index.
            C_t_indices_fold.append(group_performance_normalized(cindex, Y_fold, \
                                                                    P_fold.iloc[:,m].values, target_inds_fold))
        # Calculate IC-indices for all predictions in parallel. 
        IC_indices_fold = ic_index.ic_index(drug_inds_fold, target_inds_fold, \
                                                Y_fold.astype(float), P_fold.to_numpy())
        
        # Add the performance measure values related to this fold to the lists where all foldwise values are collected.
        C_index_list.append(C_indices_fold)
        C_d_index_list.append(C_d_indices_fold)
        C_t_index_list.append(C_t_indices_fold)
        IC_index_list.append(IC_indices_fold)
    
    # Calculate the averages of the foldwise C- and IC-indices.
    C_indices = pd.DataFrame(np.vstack(C_index_list)).mean()
    C_d_indices = pd.DataFrame(np.vstack(C_d_index_list)).mean()
    C_t_indices = pd.DataFrame(np.vstack(C_t_index_list)).mean()
    IC_indices = pd.DataFrame(np.vstack(IC_index_list)).mean()

    return IC_indices, C_indices, C_d_indices, C_t_indices


def calculate_performances():
    # List the data sets for which the performances are calculated.
    data_sets = ["davis", "metz", "kiba", "merget", "GPCR", "IC", "E"]

    # Add here the path to the folder where the predictions are stored. 
    data_dir = "Predictions"

    df_ds = []
    for ds in data_sets:
        print("\n\nLoading " + ds + " data:")
        df_gt = pd.read_csv(Path(data_dir, 'ground_truth_'+ds+'.csv'), header = None, names = ['Y'])
        df_folds = pd.read_csv(Path(data_dir, 'folds_'+ds+'.csv'), header = None, names = ['fold'])
        df_dtinds = pd.read_csv(Path(data_dir, 'drug_target_index_'+ds+'.csv'), header = None, names = ['ID_d','ID_t'])
        print("Loaded groud truth, drug-target indices and fold partition.")
        
        list_of_predictions = []
        loaded_method_setting_combinations =[]
        
        # Learning algorithms for which the performances are calculated.
        for m in ["KRLSKRG", "KRLSKRL", "KRLSLRG", "KRLSLRL", "kNN", "ltr", \
                  "RF", "XGBoost", "DDTA", "FF", "GT"]:
            for setting in ['IDIT', 'IDOT', 'ODIT', 'ODOT']:
                ppath = Path(data_dir, 'predictions_'+m+'_'+setting+'_'+ds+'.csv')
                # Some methods may not have predictions for all data sets.
                if ppath.exists():
                    df_predictions = pd.read_csv(ppath, header = None, names = [m + ':' + setting])
                    list_of_predictions.append(df_predictions)
                    loaded_method_setting_combinations.append(m + '_' + setting)
                else:
                    continue
        print("Loaded predictions by method under setting (method_setting): " + ", ".join(loaded_method_setting_combinations))
        print("Calculating prediction performance estimates...")
        
        df_concatenated = pd.concat([df_dtinds, df_folds, df_gt]+list_of_predictions, axis=1)
        
        IC_indices, C_indices, C_d_indices, C_t_indices = calculate_foldwise_IC_C_indices(df_concatenated)
        
        df_ds.append(pd.DataFrame({'data':ds, 'model':df_concatenated.columns[4:].to_flat_index(), \
                                   'IC_index': IC_indices, 'C_index':C_indices, \
                                   'C_d_index':C_d_indices, 'C_t_index':C_t_indices})) 
  
        print("Finished with " + ds + " data.")
    
    # Save all the results in a .csv file. 
    pd.concat(df_ds, ignore_index = True).to_csv('performances.csv', index = False)


if __name__ == "__main__":
    calculate_performances()

