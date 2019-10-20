names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()

def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for x, (name, country) in generator():
        print(f"{x+1}. {name:<11}{country}")

def generator():
    for x, (name, country) in enumerate(zip(names, countries)):
        yield x, (name, country)
