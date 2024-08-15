'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pred_universe data frame, create a bar plot for the fta column.

def plot_fta_barplot(pred_universe):
    '''
    Creates a bar plot showing the count of FTA (Failure to Appear) cases.

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    # Count the occurrences of each 'fta' value
    fta_counts = pred_universe['fta'].value_counts().reset_index()
    fta_counts.columns = ['fta', 'count']

    # Designing and initializing the bar plot
    sns.barplot(data=fta_counts, x='fta', y='count')
    plt.title('Count of FTA Cases')
    plt.xlabel('FTA')
    plt.ylabel('Count')
    plt.savefig('./data/part3_plots/fta_barplot.png', bbox_inches='tight')
    plt.close()


# 2. Hue the previous barplot by sex

def plot_fta_barplot_by_sex(pred_universe):
    '''
    Creates a bar plot for the `fta` column, with hue by `sex` in the `pred_universe` DataFrame

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    sns.barplot(data=pred_universe, x='fta', hue='sex', estimator=len)
    plt.title('Bar Plot of FTA by Sex')
    plt.xlabel('FTA')
    plt.ylabel('Count')
    plt.savefig('./data/part3_plots/fta_barplot_by_sex.png', bbox_inches='tight')
    plt.close()

# 3. Plot a histogram of age_at_arrest

def plot_age_histogram(pred_universe):
    '''
    Creates a histogram for the `age_at_arrest` column in the `pred_universe` DataFrame

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=30)
    plt.title('Histogram of Age at Arrest')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Frequency')
    plt.savefig('./data/part3_plots/age_histogram.png', bbox_inches='tight')
    plt.close()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 

def plot_age_histogram_custom_bins(pred_universe):
    '''
    Creates a histogram for the `age_at_arrest` column with custom bins in the `pred_universe` DataFrame

    Parameters:
    - pred_universe dataframe

    Returns:
    - None
    '''
    bins = [18, 21, 30, 40, 100]
    labels = ['18-21', '21-30', '30-40', '40-100']
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins, discrete=True)
    plt.title('Histogram of Age at Arrest with Custom Bins')
    plt.xlabel('Age Group')
    plt.ylabel('Frequency')
    plt.xticks(ticks=[(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)], labels=labels)
    plt.savefig('./data/part3_plots/age_histogram_custom_bins.png', bbox_inches='tight')
    plt.close()
