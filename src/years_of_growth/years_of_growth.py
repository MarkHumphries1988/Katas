
def years_of_growth(
    initial_population,
    target_population,
    growth_rate,
    net_migration
):
    if initial_population>=target_population:
        return 0
    else:
        newPopulation=initial_population*(1+growth_rate/100)+net_migration
        return 1 + years_of_growth(newPopulation,target_population,growth_rate,net_migration)




    pass
