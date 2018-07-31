from models import Restaurant, Table, Wait

def seed_data():
    n1_key = Restaurant(name = "Shake Shack", phone = "3234883010", Street_address = "8520 Santa Monica Blvd", city = "West Hollywood", state = "CA", zip_code = "90069")
    t1_key = Table(description = "booth", max = "5", min = "2", full = False)
    w1_key = Wait(customer = "John Doe", phone = "3107176463", party_size = "5")
