from mal import Anime
from mal import AnimeSearch
from mal import config
from tabulate import tabulate

config.TIMEOUT = 1

def main():
  option_number = options()
  match option_number:
    case 1:
      anime = fetch_anime_data()
      printing_anime_data(anime)
      printing_synopsis(anime)
      printing_characters(anime)
      another()
    case 2:
      search = search_for_anime()
      printing_anime_data(search)
      printing_synopsis(search)
      printing_characters(search)
      another()

def options():
  print("Welcome to the ultimate anime companion. Currently, this tool has these options:")
  print("""
  Option 1: Gather anime data using MAL_ID
  Option 2: Gather anime data by search
  """)
  print("Please select the option you wish to explore:")
  while True:
    try:
      option = int(input("Option: "))
      if option < 1 or option > 8:
        raise ValueError
    except ValueError:
      pass
    else:
      break
  return option

def fetch_anime_data():
  while True:
    try:
      id = input("Please enter the MyAnimeList ID of the anime you wish to know more about: ")
      anime = Anime(id, timeout=1)
    except(UnboundLocalError, ValueError):
      pass
    else:
      break
  return anime

def printing_anime_data(anime):
  table = [
    ["Title", anime.title],
    ["Status", anime.status],
    ["Genres", ', '.join(anime.genres)], # Convert from list object to string
    ["Score", anime.score],
    ["Rank", anime.rank],
    ["Popularity", anime.popularity],
    ["Members", format(anime.members, ",")], # Separate int by commas
    ["Favorites", format(anime.favorites, ",")], # Separate int by commas
    ["Episodes", anime.episodes],
    ["Aired", anime.aired],
    ["Studios", ', '.join(anime.studios)], # Convert from list object to string
    ["Rating", anime.rating]
  ]
  print(tabulate(table))

def printing_synopsis(anime):
  while True:
    try:
      answer_synopsis = input("Would you like the synopsis? ").strip().lower()
    except ValueError:
      pass
    else:
      if answer_synopsis == "yes" or answer_synopsis == "y":
        print(anime.synopsis)
        break
      elif answer_synopsis == "no" or answer_synopsis == "n":
        break

def printing_characters(anime):
  while True:
    try:
      answer_characters = input("Would you like to know the characters? ").strip().lower()
    except ValueError:
      pass
    else:
      if answer_characters == "yes" or answer_characters == "no":
        character_table = []
        for character in anime.characters:
          temp = []
          temp.append(character.name)
          temp.append(character.role)
          temp.append(character.voice_actor)
          character_table.append(temp)
        headers = ["Name", "Role", "Voice Actor"]
        print(tabulate(character_table, headers=headers, tablefmt="fancy_grid"))
        break
      elif answer_characters == "no" or answer_characters == "n":
        break

def search_for_anime():
  while True:
    try:
      anime_name = input("What's the anime you're interested in? ")
      search = AnimeSearch(anime_name)
    except ValueError:
      pass
    else:
      break

  print("Is this the anime you were searching for?")
  print("Found: ", search.results[0].title)

  while True:
    try:
      ask = input("Yes or no? ").strip().lower()
    except ValueError:
      pass
    else:
      if ask == "yes" or ask == "y":
        return Anime(search.results[0].mal_id)
      elif ask == "no" or ask == "n":
        search_for_anime()

def another():
  while True:
    try:
      answer_another = input("Would you like to see another anime? ").strip().lower()
    except ValueError:
      pass
    else:
      if answer_another == "yes" or answer_another == "y":
        main()
      elif answer_another == "no" or answer_another == "n":
        quit()

if __name__ == "__main__":
  main()