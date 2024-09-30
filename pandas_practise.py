import pandas as pd
import matplotlib.pyplot as plt

class PandasDemo:
    """
    A class to demonstrate the capabilities of the pandas package.
    """

    def __init__(self, csv_file):
        """
        Initializes the PandasDemo class by loading a CSV file into a pandas DataFrame.
        
        :param csv_file: Path to the CSV file to load.
        """
        # Load the CSV file into a DataFrame
        self.df = pd.read_csv(csv_file)
        print("Data loaded successfully!")

    def display_basic_info(self):
        """
        Displays basic information about the DataFrame, such as its structure, columns, and types.
        """
        print("\nBasic Information:")
        print(self.df.info())  # Information about data types and missing values
        
        print("\nFirst 5 Rows:")
        print(self.df.head())  # Display first 5 rows of the DataFrame
        
        print("\nDataFrame Shape:")
        print(self.df.shape)  # Number of rows and columns in the DataFrame
        
    def clean_data(self):
        """
        Cleans the data by handling missing values.
        """
        # Show missing data before cleaning
        print("\nMissing data before cleaning:")
        print(self.df.isnull().sum())
        
        # Drop rows with missing data
        self.df.dropna(inplace=True)
        print("\nMissing data after cleaning:")
        print(self.df.isnull().sum())
        
    def basic_statistics(self):
        """
        Displays basic statistical details of the numerical columns in the DataFrame.
        """
        print("\nBasic Statistics:")
        print(self.df.describe())  # Display basic statistics like mean, std, min, and max for numeric columns
    
    def filter_data(self, column_name, condition):
        """
        Filters the DataFrame based on a condition on a specific column.
        
        :param column_name: The column to apply the filter on.
        :param condition: A condition (e.g., a comparison) to filter rows.
        :return: A filtered DataFrame
        """
        # Example filter condition: filter rows where a column's value is greater than the condition
        filtered_df = self.df[self.df[column_name] > condition]
        print(f"\nFiltered Data (where {column_name} > {condition}):")
        print(filtered_df.head())  # Display first 5 rows of filtered data
        return filtered_df

    def group_and_aggregate(self, group_by_column, agg_column, agg_func='mean'):
        """
        Groups the data by a specific column and performs an aggregation on another column.
        
        :param group_by_column: Column to group by.
        :param agg_column: Column to aggregate.
        :param agg_func: Aggregation function (default is 'mean').
        :return: A DataFrame with grouped and aggregated data.
        """
        # Group by the specified column and apply the aggregation function (default is 'mean')
        grouped_df = self.df.groupby(group_by_column)[agg_column].agg(agg_func)
        print(f"\nGrouped Data by '{group_by_column}' with '{agg_func}' aggregation on '{agg_column}':")
        print(grouped_df.head())  # Display first 5 rows of the grouped data
        return grouped_df

    def sort_data(self, column_name, ascending=True):
        """
        Sorts the DataFrame by a specific column.
        
        :param column_name: The column to sort by.
        :param ascending: Sort order (default is True for ascending).
        :return: A sorted DataFrame.
        """
        # Sort the DataFrame based on the specified column
        sorted_df = self.df.sort_values(by=column_name, ascending=ascending)
        print(f"\nData sorted by '{column_name}' ({'ascending' if ascending else 'descending'}):")
        print(sorted_df.head())  # Display first 5 rows of sorted data
        return sorted_df

    def visualize_data(self, x_column, y_column, plot_type='line'):
        """
        Visualizes the data using matplotlib.
        
        :param x_column: Column to plot on the x-axis.
        :param y_column: Column to plot on the y-axis.
        :param plot_type: Type of plot ('line', 'bar', etc.). Default is 'line'.
        """
        print(f"\nVisualizing {y_column} against {x_column} as a {plot_type} plot:")
        
        # Plot the data
        if plot_type == 'line':
            self.df.plot(x=x_column, y=y_column, kind='line', title=f'{y_column} over {x_column}')
        elif plot_type == 'bar':
            self.df.plot(x=x_column, y=y_column, kind='bar', title=f'{y_column} over {x_column}')
        else:
            print(f"Unsupported plot type: {plot_type}")
            return
        
        # Show the plot
        plt.show()

# Example usage

# Initialize the class with a CSV file
demo = PandasDemo('data.csv')

# Display basic information about the dataset
demo.display_basic_info()

# Clean the dataset (handle missing values)
demo.clean_data()

# Show basic statistics of numerical columns
demo.basic_statistics()

# Filter data (for example, filter rows where 'Sales' > 1000)
filtered_data = demo.filter_data('Sales', 1000)

# Group data by a column and aggregate (for example, group by 'Region' and aggregate 'Sales' by mean)
grouped_data = demo.group_and_aggregate('Region', 'Sales', 'mean')

# Sort data by a specific column (for example, sort by 'Sales' in descending order)
sorted_data = demo.sort_data('Sales', ascending=False)

# Visualize data (for example, plot 'Date' vs 'Sales' as a line plot)
demo.visualize_data('Date', 'Sales', 'line')
