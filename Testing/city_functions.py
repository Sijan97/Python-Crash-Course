def city_country(city, country, population=0):
    """Returns city and country name in format city, country."""
    if population:
        formatted_detail = f"{city.title()}, {country.title()}"
        formatted_detail += f" - population {population}"
    else:
        formatted_detail = f"{city.title()}, {country.title()}"
    return formatted_detail