from collections import OrderedDict

hp = OrderedDict()

hp['book one'] = "sorcs stone"
hp['book two'] = "chamber of secrets"
hp['book three'] = "prisoner of azkaban"
hp['book four'] = "goblet of fire"
hp['book five'] = "order of the pheonix"
hp['book six'] = "the half blood prince"
hp['book seven'] = "the deathly hollows"

for book, title in hp.items():
    print("\n" + book.title() + ": " + title)
