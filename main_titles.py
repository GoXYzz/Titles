from titles import Titles

category = input("Enter category: ")
# New instance of class Titles with scraped category "svet" with serbian accent
new_titles = Titles(category, "sr")
new_titles.scrape()