import exports
print(exports.make_pizza('extra cheese', 'mushrooms'))

from exports import make_pizza
print(make_pizza('bbq chicken', 'onions'))

from exports import make_pizza as p
print(p('veggies', 'soy cheese'))

import exports as e
print(e.make_pizza('kobe beef', 'gold'))

from exports import *
print(city_country('sf', 'usa'))
