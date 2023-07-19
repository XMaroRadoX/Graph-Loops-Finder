# app/gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from graph_loops_finder import read_csv_edges, find_loops_in_graph, draw_graph_with_loops

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        edges_list = read_csv_edges(file_path)
        loops = find_loops_in_graph(edges_list)

        if loops:
            message = "Loops found:\n"
            for loop in loops:
                message += " -> ".join(loop) + "\n"
            result_label.config(text=message)
            draw_graph_with_loops(edges_list, loops)
        else:
            result_label.config(text="No loops found in the graph.")
    else:
        result_label.config(text="Please select a valid CSV file.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Graph Loops Finder")

    header_label = tk.Label(root, text="Graph Loops Finder", font=("Arial", 16))
    header_label.pack(pady=10)

    browse_button = tk.Button(root, text="Browse CSV File", command=browse_file)
    browse_button.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="left")
    result_label.pack(pady=10)

    canvas = tk.Canvas(root, width=300, height=150)
    canvas.pack()

    root.mainloop()
