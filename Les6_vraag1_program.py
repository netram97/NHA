tf = True
car_manufacturer = ['Toyota', 'Mazda', 'Volkswagen', 'Jeep']
while tf == True:
    print('\n')
    print(*car_manufacturer, sep = ", ")
    Add_or_remove = input("Wil je een automerk toevoegen of verwijderen?\nToevoegen[A]\nVerwijderen[D]\nSluiten[Q]: ")
    try:
        if Add_or_remove == "A":
            Add = input("Welk automerk wil je toevoegen?")
            if Add =='' or Add == ' ':
                print('\nJe hebt niks ingevoerd, probeer het opnieuw.')
            car_manufacturer.append(Add)
        elif Add_or_remove == 'D':
            Remove = input("Welk automerk wil je verwijderen?")
            if Remove =='' or Remove == ' ':
                print('\nJe hebt niks ingevoerd, probeer het opnieuw.')
            car_manufacturer.remove(Remove)
        elif Add_or_remove == 'Q':
            tf = False
        else:
            print('\nVerkeerde input, probeer het opnieuw.')
    except ValueError:
        print("Er is iets fout gegaan, probeer het opnieuw.")