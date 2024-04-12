def read_population_data(file_path):
    population_data = {}

    with open(file_path, 'r') as file:
        for line in file:
            country, year, population = line.strip().split(', ')
            if country not in population_data:
                population_data[country] = {}
            population_data[country][int(year)] = int(population)

    return population_data

def calculate_population_change(population_data):
    population_change = {}

    for country, data in population_data.items():
        years = sorted(data.keys())
        population_change[country] = {}
        for i in range(1, len(years)):
            prev_year = years[i - 1]
            current_year = years[i]
            prev_population = data[prev_year]
            current_population = data[current_year]
            change = current_population - prev_population
            population_change[country][current_year] = change

    return population_change

def main():
    file_path = "population_data.txt"
    population_data = read_population_data(file_path)
    population_change = calculate_population_change(population_data)

    print("Changes in population by years for each country:")
    for country, data in population_change.items():
        print(f"{country}:")
        for year, change in data.items():
            print(f"    {year}: {change}")

if __name__ == "__main__":
    main()