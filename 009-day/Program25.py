#Nesting a dictionary
capitals = {
    "India": "Delhi",
    "Pakistan": "Lahore",
    "Nepal": "Kadmandu"
}

travel_log = {
    "India": {"cities_visited":["Calicut", "Delhi", "Mumbai"], "total_visit": 6},
    "Pakistan": {"cities_visited":["Lahore", "Karachi", "Ravalpindi"], "total_visit": 1},
    "Nepal": {"cities_visited":["Kadmandu", "Pokra"], "total_visit": 2}
}

#nested Dictionary in a  list

travel_log = [
     {"Country":"India", 
      "cities_visited":["Calicut", "Delhi", "Mumbai"], 
      "total_visit": 6},
     
     {"Country":"Pakistan",
      "cities_visited":["Lahore", "Karachi", "Ravalpindi"], 
      "total_visit": 1},
     
     {"Country":"Nepal",
      "cities_visited":["Kadmandu", "Pokra"], 
      "total_visit": 2}
]