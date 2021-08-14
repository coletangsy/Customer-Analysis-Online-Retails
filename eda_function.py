import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('ticks')
plt.rcParams["figure.figsize"] = (10,8)

import warnings
warnings.filterwarnings("ignore")

def target_check(df, target):
    """Return the value counts and a horizontal barplot of target class.

    Args:
    df (dataframe): the raw dataframe with the target
    target (string): the target column
    """

    plt.figure(figsize=(18,6))
    df[target].value_counts().plot(kind="barh")
    plt.xlabel("Count")
    plt.ylabel("Class")
    plt.title("Count of Target Variable")



def df_summary(df):
    """input the dataframe, and it will return a summary table with columns datails.
    which include 

    Args:
    df (dataframe): the raw dataframe with the target

    Returns:
    [dataframe]: summary table with columns datails
    """
    #create a dataframe call summary
    summary = pd.DataFrame(df.dtypes, columns=['dtype'])

    # Number of Missing values (-1 count)
    summary['num_missing'] = df.isna().sum().values    

    # Number of unique values by features
    summary['num_uniques'] = df.nunique().values

    return summary




def dist_box_violin(data):
    """ function plots a combined graph for univariate analysis of continous variable 
    to check spread, central tendency , dispersion and outliers  

    Args:
    data (data.series): the float/int columns you would like to check
    """
    Name = data.name.upper()
    fig, axes =plt.subplots(1,3,figsize=(16,6))
    fig.suptitle(f"SPREAD OF DATA FOR {Name}"  , fontsize=14, fontweight='bold')

    sns.distplot(data,kde=False,color='Blue',ax=axes[0])
    axes[0].axvline(data.mean(), color='y', linestyle='--',linewidth=2)
    axes[0].axvline(data.median(), color='r', linestyle='dashed', linewidth=2)
    axes[0].axvline(data.mode()[0],color='g',linestyle='solid',linewidth=2)
    axes[0].legend({'Mean':data.mean(),'Median':data.median(),'Mode':data.mode()})

    sns.boxplot(x=data,showmeans=True, orient='h',color="purple",ax=axes[1])

    sns.violinplot(data,ax=axes[2],showmeans=True)



def uni_plot(data,target):
    """function plots a combind distribution of class.

    Args:
    data (data.series): the columns you would like to check
    target (data.series): the columns you would like to check
    """
    Name = data.name.upper()
    fig, axes =plt.subplots(1,2,figsize=(16,6))
    fig.suptitle(f"DISTRIBUTION OF {Name}"  , fontsize=14, fontweight='bold')


    sns.countplot(x = data, ax = axes[0])
    sns.countplot(x = data, ax = axes[1], hue = target)
