# Credit Score Analysis

This file analyzes the wallet scores computed by the pipeline.

---

## 🔢 Score Ranges Distribution

| Score Range | Wallet Count |
|-------------|--------------|
| 0–100       | 12           |
| 100–200     | 45           |
| 200–300     | 94           |
| 300–400     | 132          |
| 400–500     | 164          |
| 500–600     | 198          |
| 600–700     | 187          |
| 700–800     | 94           |
| 800–900     | 53           |
| 900–1000    | 21           |

(These values are placeholder examples; your actual histogram will vary.)

---

## 📈 Histogram

View in `notebooks/eda.ipynb`. Code:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../results/wallet_scores.csv')
sns.histplot(df['credit_score'], bins=10, kde=True)
plt.title('Distribution of Credit Scores')
plt.xlabel('Credit Score')
plt.ylabel('Number of Wallets')
plt.grid(True)
plt.show()
