import analiza_danych
import example_data

def sort_and_group(data):
    decision = input("Do you want to sort and group by year, title, or author?: ")
    if decision == "year":
        sorted_by_year = analiza_danych.sort_by_year(example_data.data)
        years_group = analiza_danych.group_by_year(sorted_by_year)
        print(years_group)
    elif decision == "title":
        sorted_by_title = analiza_danych.sort_by_title(data)
        title_group = analiza_danych.group_by_title(sorted_by_title)
        print(title_group)
    elif decision == "author":
        sorted_by_author = analiza_danych.sort_by_author(data)
        author_group = analiza_danych.group_by_author(sorted_by_author)
        print(author_group)
    else:
        print("You've probably entered wrong answer or this program doesn't support this.")


if __name__ == "__main__":
    sort_and_group(example_data.data)