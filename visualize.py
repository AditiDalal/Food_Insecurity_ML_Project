from train import run_model
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Get trained data and model
df, model = run_model()

# Histogram of PovertyRate
plt.figure(figsize=(8, 5))
plt.hist(df["PovertyRate"], bins=20, color='skyblue', edgecolor='black')
plt.title("Poverty Rate Distribution (All Tracts)")
plt.xlabel("Poverty Rate (%)")
plt.ylabel("Number of Tracts")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Scatter plot of predictions with fixed legend
plt.figure(figsize=(8, 5))
plot = sns.scatterplot(
    data=df,
    x="MedianFamilyIncome",
    y="PovertyRate",
    hue="prediction",
    palette={0: "green", 1: "red"},
    alpha=0.7
)
plt.title("Model Predictions: Poverty vs. Income")
plt.xlabel("Median Family Income ($)")
plt.ylabel("Poverty Rate (%)")

# Fix legend labels manually
handles, labels = plot.get_legend_handles_labels()
plot.legend(
    handles=handles,
    labels=["Not Insecure (0)", "Insecure (1)"],
    title="Prediction",
    loc="best"
)

plt.grid(True)
plt.tight_layout()
plt.show()

#confusion matrix

logCM = confusion_matrix(y_test, log_preds)
#check results
#print(f"Confusion Matrix:\n{logCM}")

#make the heatmap
labels = ['Negative', 'Positive']
#convert matrix to df
dfCM = pd.DataFrame(logCM, index = labels, columns = labels) 

plt.figure(figsize = (6, 4))
sns.heatmap(dfCM, annot = True, fmt = 'd', cmap = 'Blues')
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.title("Confusion Matrix Heatmap");
