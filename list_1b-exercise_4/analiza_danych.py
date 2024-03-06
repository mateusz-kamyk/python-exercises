def sort_by_year(data):
    sorted_by_year = sorted(data, key=lambda x: x["year"])
    return sorted_by_year

def sort_by_title(data):
    sorted_by_title = sorted(data, key=lambda x: x["title"])
    return sorted_by_title

def sort_by_author(data):
    sorted_by_author = sorted(data, key=lambda x: x["author"])
    return sorted_by_author

def group_by_year(data):
    years_group = list(map(lambda x: x["year"], data))
    return years_group

def group_by_title(data):
    title_group = list(map(lambda x: x["title"], data))
    return title_group

def group_by_author(data):
    author_group = list(map(lambda x: x["author"], data))
    return author_group

