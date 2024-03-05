import csv
import pylab as plt
from matplotlib.ticker import ScalarFormatter

def analyze_data_with_loops(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        total_sales = 0
        count = 0
        sales_values = []
        sales_per_year = {}
        for row in reader:
            if (
                row["variable"] == "Sales, government funding, grants and subsidies"
                and row["unit"] == "DOLLARS(millions)"
                and row["value"] != "C"
            ):
                total_sales += float(row["value"])
                sales_values.append(float(row["value"]))
                count += 1
                if row["year"] not in sales_per_year:
                    sales_per_year[row["year"]] = []
                sales_per_year[row["year"]].append(float(row["value"]))

        return total_sales, count, sales_values, sales_per_year
       

def calculate_average(total_sales, count):
    average_sales = total_sales / count if count else 0
    print(f"Average Sales: {average_sales}")

def calculate_median(sales_values):
    sorted_sales = sorted(sales_values)
    results_number = len(sorted_sales)
    if results_number % 2 != 0:
        median = sorted_sales[results_number // 2]
    else:
        median = ((sorted_sales[results_number // (2-1)] + sorted_sales[results_number // 2]))
    print(f"Median Sales: {median}")

def calculate_sum_per_year(sales_per_year):
    calculated_sum = {}
    print("Sales per year:")
    for year, sales_values in sales_per_year.items():
        calculated_sum_per_year = sum(sales_values)
        calculated_sum[year] = calculated_sum_per_year
        print(f"{year}: {calculated_sum_per_year}")
    
    return calculated_sum

def create_chart_per_year(calculated_sum):

    years = list(calculated_sum.keys())
    values = list(calculated_sum.values())

    plt.bar(years, values)
    plt.xlabel('Year')
    plt.ylabel('DOLLARS(millions)')
    plt.title('"Sales, government funding, grants and subsidies" per year')
    plt.ticklabel_format(axis='y', style='plain') 
    plt.gca().yaxis.set_minor_formatter(ScalarFormatter())
    plt.tight_layout()
    plt.tight_layout()
    plt.show()


def main():
    total_sales, count, sales_values, sales_per_year = analyze_data_with_loops("path_to_file.csv")
    calculate_average(total_sales, count)
    calculate_median(sales_values)
    calculated_sum = calculate_sum_per_year(sales_per_year)
    create_chart_per_year(calculated_sum)


if __name__ == "__main__":
    main()