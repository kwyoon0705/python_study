def format_name(first_name:str, last_name:str):
    """Take a first and last name and format it to return the title case version of the name."""
    if first_name == "" or last_name == "":
        print("You typed wrong name.")
        return
    first_name = first_name.title()
    last_name = last_name.title()
    return f"{first_name} {last_name}"

print(format_name("yuN", "geonWoo"))