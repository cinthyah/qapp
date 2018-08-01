from models import Restaurant, Table, Wait

def seed_data():
    #restaurants
    Shake_key = Restaurant(name = "Shake Shack", phone = "3234883010", street_address = "8520 Santa Monica Blvd", city = "West Hollywood", state = "CA", zip_code = "90069", user_email = "example@gmail.com").put()
    in_key = Restaurant(name = "In n Out", phone = "8007861000", street_address = "13425 Washington Blvd", city = "Marina Del Rey", state = "CA", zip_code = "90292", user_email = "example@gmail.com").put()
    cheese_key = Restaurant(name = "Cheescake Factory", phone = "3102601296", street_address = "395 Santa Monica Place", city = "Santa Monica", state = "CA", zip_code = "90401", user_email = "example@gmail.com").put()
    blaze_key = Restaurant(name = "Blaze Pizza", phone = "3103400638", street_address = "4114 Sepulveda Blvd", city = "Culver City", state = "CA", zip_code = "90230", user_email = "example@gmail.com").put()

    #tables
    shake1_table_key = Table(max = "5", min = "2", full = False).put()
    shake2_table_key = Table(max = "2", min = "1", full = False).put()
    shake3_table_key = Table(max = "4", min = "2", full = False).put()
    shake4_table_key = Table(max = "5", min = "2", full = False).put()

    in1_table_key = Table(max = "5", min = "2", full = False).put()
    in2_table_key = Table(max = "4", min = "2", full = False).put()
    in3_table_key = Table(max = "2", min = "1", full = False).put()

    cheese1_table_key = Table(max = "5", min = "2", full = False).put()
    cheese2_table_key = Table(max = "4", min = "2", full = False).put()
    cheese3_table_key = Table(max = "2", min = "1", full = False).put()

    #wait
    shake_c1_key = Wait(customer = "John Doe", phone = "3107176463", party_size = "5").put()
    shake_c2_key = Wait(customer = "Jane Doe", phone = "3107176463", party_size = "2").put()
    shake_c3_key = Wait(customer = "Bob", phone = "3107176463", party_size = "4").put()

    in_c1_key = Wait(customer = "John Doe", phone = "3107176463", party_size = "5").put()
    in_c2_key = Wait(customer = "Jane Doe", phone = "3107176463", party_size = "2").put()
    in_c3_key = Wait(customer = "Bob", phone = "3107176463", party_size = "4").put()

    cheese_c1_key = Wait(customer = "John Doe", phone = "3107176463", party_size = "5").put()
    cheese_c2_key = Wait(customer = "Jane Doe", phone = "3107176463", party_size = "2").put()
    cheese_c3_key = Wait(customer = "Bob", phone = "3107176463", party_size = "4").put()
