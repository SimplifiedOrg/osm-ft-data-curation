"""
clean_data.py - starter code

Clean the raw, messy raw_transactions.csv export and produce a cleaned,
standardised set of transactions.

Your job is to fill in normalize_description() and normalize_amount()
below, plus each TODO inside clean() where a row gets dropped.
"""

import csv
import json

INPUT_PATH = "./raw_transactions.csv"
OUTPUT_PATH = "./cleaned_transactions.jsonl"

# Out-of-scope junk rows that aren't real transactions and should be dropped.
JUNK_DESCRIPTIONS = {
    "OPENING BALANCE", "INTEREST CHARGED", "ACCOUNT MAINTENANCE FEE ADJUSTMENT",
    "STATEMENT CARRIED FORWARD", "BALANCE BROUGHT FORWARD",
}


def normalize_description(raw_desc):
    """
    Clean up a raw description so formatting is consistent.

    Trim leading/trailing whitespace, collapse repeated spaces down
    to single spaces, and uppercase the result.
    """

    pass


def normalize_amount(raw_amount):
    """
    Parse an amount string into a number.

    Strip the "$" and convert what's left to a float.
    If it can't be converted (invalid text), return None instead of
    raising, clean() uses that to drop unrecoverable rows.
    """

    pass


def clean(input_path, output_path):
    seen = set()
    kept = []
    stats = {"total": 0, "duplicate": 0, "missing_field": 0, "junk": 0, "kept": 0}

    with open(input_path, newline="") as f:
        for row in csv.DictReader(f):
            stats["total"] += 1
            raw_desc, raw_amount = row["description"], row["amount"]

            # TODO: Drop rows missing a description or amount


            # TODO: Drop exact duplicates (same cleaned description + amount).


            # TODO: Drop out-of-scope junk rows.


            kept.append({"description": description, "amount": amount})
            stats["kept"] += 1

    with open(output_path, "w") as f:
        for row in kept:
            f.write(json.dumps(row) + "\n")

    return stats


if __name__ == "__main__":
    stats = clean(INPUT_PATH, OUTPUT_PATH)
    print("Cleaning summary:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
