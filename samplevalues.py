import pdb
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_phone_number():
    ist_number = random.randint(2, 9)
    end_literal = random.randint(1111111, 9999999)
    starting_literal = "030"
    phone_number = starting_literal + str(ist_number) + str(end_literal)
    return phone_number

def generate_random_name():
    first = ("Ali", "Usama", "Abdullah", "Tariq", "Fatima", "Haris", "Faizan", "Anas", "Farhan", "Abid", "Fahad", "Suleman", "Haseeb",
    "Tayyab", "Saleeem", "Azeem", "Arsal", "Razaq", "Shan", "Ahmed", "Tuseef")
    second = ("Tufeeq", "Asif", "Afridi", "Khan", "Hasnat", "Zahoor", "Utba", "Rasheed", "Ashfaq", "Yaqoob", "Rehmat", "Inayat",
    "Sami", "Zeeshan", "Ajmal", "Javed", "Kamal", "Khalid", "Aziz")
    firrst = random.choice(first)
    seccond = random.choice(second)
    name = (firrst + " " + seccond)
    return name


def generate_random_first_name():
    first = ("Ali", "Usama", "Abdullah", "Tariq", "Fatima", "Haris", "Faizan", "Anas", "Farhan", "Abid", "Fahad", "Suleman", "Haseeb",
    "Tayyab", "Saleeem", "Azeem", "Arsal", "Razaq", "Shan", "Ahmed", "Tuseef")
    second = ("Tufeeq", "Asif", "Afridi", "Khan", "Hasnat", "Zahoor", "Utba", "Rasheed", "Ashfaq", "Yaqoob", "Rehmat", "Inayat",
    "Sami", "Zeeshan", "Ajmal", "Javed", "Kamal", "Khalid", "Aziz")
    first = random.choice(first)
    return first

def generate_random_last_name():
    second = (
        "Tufeeq", "Asif", "Afridi", "Khan", "Hasnat", "Zahoor", "Utba", "Rasheed", "Ashfaq", "Yaqoob", "Rehmat",
        "Inayat",
        "Sami", "Zeeshan", "Ajmal", "Javed", "Kamal", "Khalid", "Aziz")
    second= random.choice(second)
    return second
    # seccond = random.choice(second)
    # name = (firrst + " " + seccond)
    # return name

def generate_random_adress():
    area= ("Korangi", "Liaqatabad", "Nagin chorancgi", "Bhens cololony", "college road", "stadium road", "school road", "madina market", "Housing colony", "Rehamandbad", "Mughal pura", "Baghban Pura",
    "Muradabad", "School Muhalla", "Safoora", "Atomic Colony", "PAF Colony", "Gulberg", "DHA")
    city= ("Islamabad", "Karachi", "Lahore", "Hydrabad", "Sheikhupura", "Multan", "Sargodha")
    house_number = "House Number" + " " + str(random.randint(1, 100))
    street_name="Street"+" "+str(random.randint(1,100))
    area = random.choice(area)
    city = random.choice(city)
    adress=house_number+" "+street_name+" "+area+" "+city
    return adress

def generate_random_card_number():
    random_wrong_number=str(generate_phone_number())
    card_numbers_collection=("4242424242424242","36227206271668","4000056655665556","5555555555554444","2223003122003222","5200828282828210",random_wrong_number,random_wrong_number,random_wrong_number,random_wrong_number)
    number=random.choice(card_numbers_collection)
    return str(number)

def generate_random_date():
    #05/27
    month="0"+str(random.randint(1,9))
    year=str(random.randint(20,30))
    date=str(month+"/"+year)
    return str(date)

def generate_random_quantity(upperlimit):
    number=random.randint(1,upperlimit)
    return str(number)




def generate_random_zipcodes():
    zipcode=random.randint(11111,99999)
    return str(zipcode)

def generate_random_email():
    name=generate_random_first_name()+generate_random_last_name()
    random_num=str(random.randint(1,99999))
    end_literal="@ensx.com"
    email=name+random_num+end_literal
    email=email.strip()
    return email.lower()




def generate_random_city():
    city = ("Islamabad", "Karachi", "Lahore", "Hydrabad", "Sheikhupura", "Multan", "Sargodha")
    city = random.choice(city)
    return city




#false values
def generate_bad_phone_number():
    return str("bad"+generate_phone_number()+"bad")
# for i in range(1,450):
#     print("Sample****", i)
# adress1 = generate_random_adress()
# adress2 = generate_random_adress()
# name = generate_random_name()
# phone_number = phone = generate_phone_number()
    # print("Adress1", adress1)
    # print("Adress2", adress2)
    # print("Name", generate_random_name())
    # print("Carld Holder Name", name)
    # print("Phone Number", phone_number)

def generate_bad_date():
    return str(get_random_string(5))


def generate_bad_zip_code():
    return str(get_random_string(5))


def generate_bad_city():
    return str(random.randint(11111,99999))



def generate_bad_email():
    name = generate_random_first_name() + generate_random_last_name()
    random_num = str(random.randint(1, 99999))
    email = name + random_num
    return email.lower()

