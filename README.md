# Salary Growth Analysis Tool

This Python script is a GUI application using Tkinter to analyze and visualize salary growth data from a CSV file. It calculates the average annual growth rate of salary values and projects the value for the next year. The data is displayed using Matplotlib within the Tkinter window.

## Features

- Load salary data from a CSV file.
- Calculate average annual growth rate and project future values.
- Visualize the data with a line chart and highlight the projected value.

## Dependencies

- `tkinter` (included with standard Python installations)
- `matplotlib`
- `csv`

You can install the required external library with:

```bash
pip install matplotlib
```
## Usage

#### 1.Run the Script

Execute the script using Python:

```bash
python salary_growth_analysis.py
```

#### 2.Browse and Select a CSV File:

Click the "Browse CSV" button to select a CSV file containing the salary data. The file should have two columns: year and value. For example:

```csv
Year,Value
2020,50000
2021,52000
2022,54000
```

#### 3.View Results

- The average annual growth rate will be displayed.
- The data will be plotted with the projected value for the next year.

## Code Explanation

- **`read_data_from_csv(file_path: str)`**: Reads data from a CSV file and returns lists of years and values.
- **`calculate_statistics(values: list[float])`**: Computes the average growth rate and projects the next year's value.
- **`plot_data(years: list[int], values: list[float], projected_year: int, projected_value: float)`**: Plots the salary data and the projected value.
- **`browse_file()`**: Handles file browsing, data reading, calculations, and plotting.

## Screenshots

