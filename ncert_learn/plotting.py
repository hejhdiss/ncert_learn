import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# General function for configuring and customizing plots
def plot_config(title, xlabel, ylabel):
    """
    Configures the title and axis labels for the plot.

    :param title: The title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating successful plot setup
    """
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return True

# 1. Histogram plot
def plot_histogram(data, bins=10, title='Histogram', xlabel='Value', ylabel='Frequency'):
    """
    Plots a histogram.
    
    :param data: List of numeric data points
    :param bins: Number of bins for the histogram
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.hist(data, bins=bins)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 2. Line plot
def plot_line(x, y, title='Line Plot', xlabel='X', ylabel='Y'):
    """
    Plots a line chart.
    
    :param x: List of x-values
    :param y: List of y-values
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.plot(x, y)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 3. Scatter plot
def plot_scatter(x, y, title='Scatter Plot', xlabel='X', ylabel='Y'):
    """
    Creates a scatter plot.
    
    :param x: List of x-values
    :param y: List of y-values
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.scatter(x, y)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 4. Bar chart
def plot_bar(categories, values, title='Bar Chart', xlabel='Categories', ylabel='Values'):
    """
    Plots a bar chart.
    
    :param categories: List of category names
    :param values: List of corresponding values for each category
    :param title: Title of the chart
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.bar(categories, values)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 5. Pie chart
def plot_pie(labels, values, title='Pie Chart'):
    """
    Plots a pie chart.
    
    :param labels: List of labels for pie chart
    :param values: List of values corresponding to each label
    :param title: Title of the pie chart
    :return: Boolean indicating plot success
    """
    try:
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title(title)
        plt.show()
        return True
    except:
        return False

# 6. Box plot
def plot_box(data, title='Box Plot', xlabel='Category', ylabel='Value'):
    """
    Plots a box plot.
    
    :param data: List of values for the box plot
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.boxplot(data)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 7. Heatmap
def plot_heatmap(matrix, title='Heatmap', xlabel='Columns', ylabel='Rows'):
    """
    Plots a heatmap.
    
    :param matrix: 2D list (matrix) representing data
    :param title: Title of the heatmap
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.imshow(matrix, cmap=cm.viridis, interpolation='nearest')
        plt.colorbar()
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 8. Stacked bar chart
def plot_stacked_bar(data, categories, title='Stacked Bar Chart', xlabel='Categories', ylabel='Values'):
    """
    Plots a stacked bar chart.
    
    :param data: List of values for each category in a stacked form
    :param categories: List of category names
    :param title: Title of the chart
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.bar(categories, data[0], label='Dataset 1')
        for i in range(1, len(data)):
            plt.bar(categories, data[i], bottom=np.sum(data[:i], axis=0), label=f'Dataset {i+1}')
        plot_config(title, xlabel, ylabel)
        plt.legend()
        plt.show()
        return True
    except:
        return False

# 9. Area chart
def plot_area(x, y, title='Area Chart', xlabel='X', ylabel='Y'):
    """
    Plots an area chart.
    
    :param x: List of x-values
    :param y: List of y-values
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.fill_between(x, y)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 10. Violin plot
def plot_violin(data, title='Violin Plot', xlabel='Category', ylabel='Value'):
    """
    Plots a violin plot.
    
    :param data: List of values for the violin plot
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.violinplot(data)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 11. Pair plot (scatter plot matrix)
def plot_pair(x, y, title='Pair Plot', xlabel='X', ylabel='Y'):
    """
    Plots a pair plot (scatter plot matrix).
    
    :param x: List of x-values
    :param y: List of y-values
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        for i in range(len(x)):
            plt.scatter(x[i], y[i])
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 12. 3D Plot
def plot_3d(x, y, z, title='3D Plot', xlabel='X', ylabel='Y', zlabel='Z'):
    """
    Plots a 3D scatter plot.
    
    :param x: List of x-values
    :param y: List of y-values
    :param z: List of z-values
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :param zlabel: Label for the Z-axis
    :return: Boolean indicating plot success
    """
    try:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        plt.title(title)
        plt.show()
        return True
    except:
        return False

# 13. Subplots (multiple plots in a single figure)
def plot_subplots(data, title='Subplots', xlabel='X', ylabel='Y'):
    """
    Plots multiple subplots in one figure.
    
    :param data: List of datasets to plot
    :param title: Title of the main plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        fig, axs = plt.subplots(len(data), 1)
        for i, dataset in enumerate(data):
            axs[i].plot(dataset)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 14. Hexbin plot
def plot_hexbin(x, y, gridsize=30, title='Hexbin Plot', xlabel='X', ylabel='Y'):
    """
    Plots a hexbin plot for large datasets.
    
    :param x: List of x-values
    :param y: List of y-values
    :param gridsize: Size of the grid for hexbin
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.hexbin(x, y, gridsize=gridsize, cmap=cm.PuBuGn)
        plt.colorbar()
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False

# 15. Contour plot
def plot_contour(x, y, z, title='Contour Plot', xlabel='X', ylabel='Y'):
    """
    Plots a contour plot.
    
    :param x: List of x-values
    :param y: List of y-values
    :param z: Corresponding values to be contoured
    :param title: Title of the plot
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    :return: Boolean indicating plot success
    """
    try:
        plt.contour(x, y, z)
        plot_config(title, xlabel, ylabel)
        plt.show()
        return True
    except:
        return False
