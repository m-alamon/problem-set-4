'''
- You will run Problem Set 4 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    # 1
    part3.plot_fta_barplot(pred_universe)
    # 2
    part3.plot_fta_barplot_by_sex(pred_universe)
    # 3
    part3.plot_age_histogram(pred_universe)
    # 4
    part3.plot_age_histogram_custom_bins(pred_universe)

    ##  PART 4: CATEGORICAL PLOTS  ##
    # 1
    part4.create_catplot_felony(pred_universe)
    # 2
    part4.create_catplot_nonfelony(pred_universe)
    # 3
    part4.create_catplot_felony_hue(pred_universe)

    ##  PART 5: SCATTERPLOTS  ##
    # 1
    part5.create_scatter_felony_vs_nonfelony(pred_universe)
    # 2
    part5.create_scatter_felony_rearrest_vs_actual(pred_universe)

if __name__ == "__main__":
    main()
