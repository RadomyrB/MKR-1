def read_population_data(file_path):
    population_data = {}

    with open(file_path, 'r') as file:
        for line in file:
            country, year, population = line.strip().split(', ')
            if country not in population_data:
                population_data[country] = {}
            population_data[country][int(year)] = int(population)

    return population_data
