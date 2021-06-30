def process(name):
    new_name = name.replace(",", "")
    new_name = new_name.replace(".", "")
    new_name = new_name.replace("?", "")
    new_name = new_name.replace("!", "")
    return new_name.lower()


print(process(input()))
