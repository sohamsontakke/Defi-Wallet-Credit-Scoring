# Defi-Wallet-Credit-Scoring - Aave V2 Protocol

This project assigns a **credit score (0–1000)** to DeFi wallets based on their historical transaction behavior on the Aave V2 protocol. Higher scores represent responsible usage; lower scores may indicate risky, bot-like, or exploitative behavior.

---

## 📦 Dataset

Input: Raw JSON data (~87MB) with transaction-level activity.  
Each record includes:
- `userWallet`: Wallet address
- `action`: Type (`deposit`, `borrow`, `repay`, etc.)
- `timestamp`: Unix time
- `actionData.amount`: Token amount (as string)

---

## ⚙️ Methodology

### 1. **Feature Engineering**

For each wallet, we compute:
- `total_deposit`, `total_borrow`, `total_repay`, `total_redeem`
- `repay_ratio = total_repay / total_borrow`
- `redeem_ratio = total_redeem / total_deposit`
- `liquidation_count`
- `active_days`: Days wallet was active
- `avg_tx_gap`: Time (in seconds) between actions
- `tx_count`: Total number of transactions

### 2. **Credit Score Formula**

A weighted formula computes a score between 0–1000:

score = (
0.25 * normalized(repay_ratio) +
0.25 * normalized(total_deposit) +
0.15 * normalized(redeem_ratio) +
0.15 * normalized(active_days) -
0.20 * (liquidation_count / (tx_count + 1))
) * 1000

yaml
Copy
Edit

Normalization is handled using `MinMaxScaler`.

---

## 🚀 How to Run

1. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

2. Run the script:
python main.py --input data/user_transactions.json --output results/wallet_scores.csv

markdown
Copy
Edit

3. Analyze results:
jupyter notebook notebooks/eda.ipynb

yaml
Copy
Edit

---

## 📁 Folder Structure

aave-credit-scoring/
├── main.py
├── data/
├── results/
├── src/
│ ├── utils.py
│ ├── feature_engineering.py
│ └── score_generator.py
├── notebooks/
│ └── eda.ipynb
├── README.md
└── analysis.md

yaml
Copy
Edit

---

## ✅ Output

Final output (`results/wallet_scores.csv`):
wallet_address,credit_score
0xabc123...,743
0xdef456...,312
...

yaml
Copy
Edit

---

## 📌 Extensibility

- Add more behavioral features (e.g. bot detection)
- Replace rule-based logic with ML (XGBoost, Clustering)
- Integrate price-based valuation of transactions in USD
