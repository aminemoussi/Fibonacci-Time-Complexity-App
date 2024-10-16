import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

with open("..\\Fibonacci_stats\\cmake-build-debug\\Fibonacci_calc_results.txt", 'r') as f:
    data = f.read()


#print(data)
data = data.strip()
#print(data)
data = data.split('\n')   #splits them into a list of records, each one represents the stats of an index
#print(data)

data_rows = []
for row in data:
    data_rows.append(row.split(", "))    #splits them whenever u find ', ' in a row

#print(data_rows)        #list of rows

df = pd.DataFrame(data_rows, columns = ["index", "Fibonacci Value", "Execution time"])   #here u get that dataframe shape we're all used to
print(df)

df["index"] = df["index"].astype(int)
df["Execution time"] = df["Execution time"].astype(float)

plt.figure(figsize=(10, 6))
plt.plot(df["index"], df["Execution time"], marker='o', color='b', label="Time Complexity Curve.")
plt.title("Time Complexity Exponential Curve.", fontsize=16)
plt.xlabel("Fibonacci Index", fontsize=14)
plt.ylabel("Execution Time (seconds)", fontsize=14)

plt.grid(True)
plt.legend()
plt.savefig("dull_fibonacci_execution_time_plot.png", dpi = 300)

plt.show()


