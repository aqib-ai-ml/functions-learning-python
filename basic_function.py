import pandas as pd
import matplotlib.pyplot as plt

student1 = [45, 50, 55, 60, 65]
student2 = [40, 42, 48, 52, 58]
student3 = [30, 35, 40, 45, 50]

tests = [1, 2, 3, 4, 5]

df = pd.DataFrame({"Kevin": student1, "Peter": student2, "Brevis": student3}, index=tests)
df.plot(kind="line", marker="o", linestyle="dashed")
plt.title("Student Performance Over Tests")
plt.xlabel("Test Number")
plt.ylabel("Marks")
plt.show()