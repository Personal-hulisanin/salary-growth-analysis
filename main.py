import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import Union


def read_data_from_csv(file_path: str) -> Union[tuple[list[int], list[float]], tuple[None, None]]:

    years = []
    values = []
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header row if present
            for row in csv_reader:
                years.append(int(row[0]))
                values.append(float(row[1]))
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return None, None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file: {e}")
        return None, None

    return years, values


#Calculate average growth rate and projected value.
def calculate_statistics(values: list[float]) -> tuple[float, float]:

    initial_value = values[0]
    final_value = values[-1]
    num_years = len(values) - 1
    average_growth_rate = (final_value / initial_value) ** (1 / num_years) - 1

    projected_value = final_value * (1 + average_growth_rate)

    return average_growth_rate, projected_value


#Plot the data along with the projected value.
def plot_data(years: list[int], values: list[float], projected_year: int, projected_value: float):

    fig, ax = plt.subplots()

    ax.plot(years, values, marker='o', linestyle='-', label='Actual Data')
    ax.scatter(projected_year, projected_value, color='red', label=f'Projected Value for next review')

    ax.set_title('Value Over Year:')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend()

    ax.grid(True)

    return fig, ax


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        years, values = read_data_from_csv(file_path)
        if years and values:
            global average_growth_rate, projected_value
            average_growth_rate, projected_value = calculate_statistics(values)
            result_label.config(text=f"Average annual growth rate: {round(average_growth_rate * 100, 2)} %")

            # Remove previous plot, if exists
            for widget in canvas_frame.winfo_children():
                widget.destroy()

            fig, ax = plot_data(years, values, years[-1] + 1, projected_value)

            # Embed plot into Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            # Add scrollbar to the canvas
            scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            scrollbar.config(command=canvas.get_tk_widget().yview)
            canvas.get_tk_widget().config(yscrollcommand=scrollbar.set)

            # Bind motion_notify_event to display values
            def display_values(event):
                x, y = event.xdata, event.ydata
                if x is not None and y is not None:
                    ax.set_title(f'Value Over Years\nYear: {int(x)}, Value: {round(y, 2)}')
                    fig.canvas.draw_idle()

            fig.canvas.mpl_connect('motion_notify_event', display_values)


if __name__ == "__main__":

    # Creating the main window
    root = tk.Tk()
    root.title("Salary Growth Analysis")
    root.geometry('800x600')

    # Button to browse and select CSV file
    browse_button = tk.Button(root, text="Browse CSV", command=browse_file)
    browse_button.pack(pady=10)

    # Label to display result
    result_label = tk.Label(root, text="")
    result_label.pack()

    # Frame to contain the canvas and scrollbar
    canvas_frame = tk.Frame(root)
    canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Run the Tkinter event loop
    root.mainloop()
