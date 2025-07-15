import argparse
import pandas as pd
from src.feature_engineering import extract_wallet_features
from src.score_generator import generate_scores
from src.utils import load_transactions, save_scores

def main(input_path, output_path):
    print("Loading data...")
    tx_data = load_transactions(input_path)

    print("Extracting features...")
    wallet_df = extract_wallet_features(tx_data)

    print("Generating credit scores...")
    wallet_df['credit_score'] = generate_scores(wallet_df)

    print("Saving results...")
    save_scores(wallet_df[['wallet_address', 'credit_score']], output_path)

    print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to user_transactions.json")
    parser.add_argument("--output", required=True, help="Path to output CSV file")
    args = parser.parse_args()

    main(args.input, args.output)