# from Function import double_it as dt
# dt(45)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")