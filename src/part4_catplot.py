'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pred_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.

def create_catplot_felony(pred_universe):
    '''
    Creates a categorical plot for prediction of felony rearrest by charge type.

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    sns.catplot(data=pred_universe,
                x='has_felony_charge',
                y='prediction_felony',
                kind='bar')
    plt.title('Prediction for Felony Rearrest by Charge Type')
    plt.xlabel('Has Felony Charge')
    plt.ylabel('Prediction for Felony Rearrest')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest.png', bbox_inches='tight')
    plt.close()

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# In a print statement, answer the following question: What might explain the difference between the plots?
def create_catplot_nonfelony(pred_universe):
    '''
    Creates a categorical plot for prediction of nonfelony rearrest by charge type.

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    sns.catplot(data=pred_universe,
                x='has_felony_charge',
                y='prediction_nonfelony',
                kind='bar')
    plt.title('Prediction for Nonfelony Rearrest by Charge Type')
    plt.xlabel('Has Felony Charge')
    plt.ylabel('Prediction for Nonfelony Rearrest')
    plt.savefig('./data/part4_plots/catplot_nonfelony_rearrest.png', bbox_inches='tight')
    plt.close()

    # Print statement to answer the question
    print("The difference between the plots might be explained by the nature of the charges. Felony charges are more severe and might have different factors compared to nonfelony charges, leading to a different prediction outcome.")

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?

def create_catplot_felony_hue(pred_universe):
    '''
    Creates a categorical plot for prediction of felony rearrest by charge type, hue by actual felony rearrest.

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    sns.catplot(data=pred_universe,
                x='has_felony_charge',
                y='prediction_felony',
                kind='bar',
                hue='y_felony')
    plt.title('Prediction for Felony Rearrest by Charge Type with Hue by Actual Felony Rearrest')
    plt.xlabel('Has Felony Charge')
    plt.ylabel('Prediction for Felony Rearrest')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest_hue.png', bbox_inches='tight')
    plt.close()

    print("If arrestees with a current felony charge who did not get rearrested for a felony have a higher predicted probability than those with a current misdemeanor charge who did get rearrested, this might suggest that the model is predicting higher probabilities based on the current charge type and not accurately reflecting actual rearrest outcomes.")
