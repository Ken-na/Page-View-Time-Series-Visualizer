import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv").set_index('date')
# Clean data
    #Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df.where((df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))).dropna()

df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax = sns.lineplot(data=df, x="date", y="value", color='red')#.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    #ax = fig.get_axure()
    ax.set(xlabel="Date",
       ylabel="Page Views",
       title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return ax (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    df_bar = df_bar.drop('date', axis=1)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(7, 6))
    ax = sns.barplot(data=df_bar, x="year", y="value", hue="month", ci=None,palette=sns.color_palette(), hue_order=["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"])

    ax.legend().set_title("Months")
    ax.set_ylabel("Average Page Views")
    ax.set_xlabel("Years")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    # Save image and return ax (don't change this part)
        #changed ax.savefig into fig.savefig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(figsize=(18, 6), ncols=2, sharex=False)

    ax2 = sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Year-wise Box Plot (Trend)')

    ax2 = sns.boxplot(x='month', y='value', data=df_box, ax=ax[1])
    ax2.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug","Sep", "Oct", "Nov", "Dec"])#, rotation=90)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return ax (don't change this part)
    fig.savefig('box_plot.png')
    return fig
