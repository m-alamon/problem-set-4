'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?

def create_scatter_felony_vs_nonfelony(pred_universe):
    '''
    Creates a scatter plot for prediction of felony vs. nonfelony, hue by current felony charge.

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    sns.lmplot(data=pred_universe,
               x='prediction_felony',
               y='prediction_nonfelony',
               hue='has_felony_charge',
               aspect=1.5,
               line_kws={'color': 'orange'})
    plt.title('Prediction for Felony vs Nonfelony Rearrest by Current Felony Charge')
    plt.xlabel('Prediction for Felony Rearrest')
    plt.ylabel('Prediction for Nonfelony Rearrest')
    plt.savefig('./data/part5_plots/scatter_felony_vs_nonfelony.png', bbox_inches='tight')
    plt.close()

    print("The group of dots on the right side of the plot represents individuals with high predictions for both felony and nonfelony rearrests. This indicates that these individuals are predicted to generally have a high risk of rearrest, regardless of the charge type.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

def create_scatter_felony_rearrest_vs_actual(pred_universe):
    '''
    Creates a scatter plot for prediction of felony rearrest vs. actual felony rearrest.

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    sns.scatterplot(data=pred_universe,
                    x='prediction_felony',
                    y='y_felony',
                    hue='has_felony_charge')
    plt.title('Prediction for Felony Rearrest vs Actual Felony Rearrest')
    plt.xlabel('Prediction for Felony Rearrest')
    plt.ylabel('Actual Felony Rearrest')
    plt.savefig('./data/part5_plots/scatter_felony_rearrest_vs_actual.png', bbox_inches='tight')
    plt.close()

    print("Based on this plot, if the predictions are closely aligned with actual outcomes, it indicates that the model might be well-calibrated. If there is significant scatter and inconsistencies, the model may need adjustments to better align predictions with observed outcomes.")
