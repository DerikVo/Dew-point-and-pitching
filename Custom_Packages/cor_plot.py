import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, ttest_ind, wilcoxon, ttest_1samp
from sklearn.metrics import mean_squared_error, r2_score

def cor_plot(feat1, feat2, _df):
    """
    Creates a Joint plot of two features and prints out the statistics such as Pearson R, SPearmen R, T-Test, and RMSE.
    Concept taken from Nick Wan's data science bootcamp on youtube.
    =============================================================================    
    Keyword arguments:
    Feat 1 -- The first feature you're comparing
    Feat 2 -- The Second feature you're comparing
    _df -- The dataframe youre using
    
    =================================================
    Example:
    cor_plot('INDUCED_VERTICAL_BREAK', 'VERTICAL_APPROACH_ANGLE', model_df)
    
    """
    r= pearsonr(_df[feat1], _df[feat2])
    r2 = r[0]**2
    
    sr = spearmanr(_df[feat1], _df[feat2])
    sr2= sr[0]**2
    sr[0], sr2, sr[-1]
    
    t= ttest_ind(_df[feat1], _df[feat2])
    t[0], t[-1]
    
    #rmse
    rmse= mean_squared_error(_df[feat1], _df[feat2])**.5
    title= f"""
    {feat1} and {feat2}
    Pearson r: {round(r[0],3)} P-value: {round(r[-1],3)}
    Spearmen r: {round(sr[0],3)} P-value: {round(sr[-1],3)}
    T-test: {round(t[0],3)} P-value: {round(t[1],3)}
    RMSE: {round(rmse,3)}
    """
    sns.jointplot(data=_df, x=feat1,y =feat2, kind='reg')
    plt.title(title)
    plt.show()
    print(title)