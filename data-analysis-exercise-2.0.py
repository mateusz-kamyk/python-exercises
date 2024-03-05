import csv

sales_values = []

def analyze_data_with_comprehensions(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        global sales_values
        sales_values = [
            float(row["value"])
            for row in reader
                if row["variable"] == "Sales, government funding, grants and subsidies"
                and row["unit"] == "DOLLARS(millions)"
                and row["value"].isdigit()
        ]
        

def calculate_average(sales_values):
    average_sales = sum(sales_values) / len(sales_values) if sales_values else 0
    print(f"Average Sales: {average_sales}")

def calculate_median(sales_values):
    sorted_sales = sorted(sales_values)
    results_number = len(sorted_sales)
    if results_number % 2 != 0:
        median = sorted_sales[results_number // 2]
    else:
        median = ((sorted_sales[results_number // (2-1)] + sorted_sales[results_number // 2]))
    print(f"Median Sales: {median}")


def main():
    analyze_data_with_comprehensions("path_to_file.csv")
    calculate_average(sales_values)
    calculate_median(sales_values)


if __name__ == "__main__":
    main()