import csv
import os

row_count = 0
grand_total = 0

top_sku = None
top_line_revenue = 0

with open("data/sales.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            units = int(row["units"])
            unit_price = float(row["unit_price"])

            line_revenue = units * unit_price

            row_count += 1
            grand_total += line_revenue

            if line_revenue > top_line_revenue:
                top_line_revenue = line_revenue
                top_sku = row["sku"]

        except (ValueError, KeyError):
            # Skip malformed rows
            continue

average_line_revenue = grand_total / row_count if row_count else 0

os.makedirs("output", exist_ok=True)

with open("output/summary.txt", "w", encoding="utf-8") as file:
    file.write(f"rows={row_count}\n")
    file.write(f"grand_total={grand_total}\n")
    file.write(f"average_line_revenue={average_line_revenue}\n")
    file.write(f"top_sku={top_sku}\n")
    file.write(f"top_line_revenue={top_line_revenue}\n")

print("Summary report created: output/summary.txt")