def combine_guests(guests1, guests2):
  guests1 = Rorys_guests
  guests2 = Taylors_guests

  combined = {**guests1, **guests2}
  for name in guests1:
    if guests2.get(name) and guests1.get(name):
      combined[name] = guests1[name] + guests2[name]
      return(combined)

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
print(combine_guests(Rorys_guests, Taylors_guests))