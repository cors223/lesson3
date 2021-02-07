name2 = str(input(f"Enter your name: "))
surname2 = str(input(f"Enter your last name: "))
year2 = str(input(f"Enter your year of birth: "))
city2 = str(input(f"Enter your city of residence: "))
email2 = str(input(f"Enter your e-mail: "))
phone2 = str(input(f"Enter your phone number: "))


def personal_info(name,surname,year,city,email,phone):
    return ' '.join([
        "name: ", name,
        ". surname: ", surname,
        ". year: ", year,
        ". city: ", city,
        ". email: ", email,
        ". phone: ", phone, "."
        ])

print(personal_info(name=name2, surname=surname2, year=year2, city=city2, email=email2, phone=phone2))