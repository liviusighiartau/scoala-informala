import pprint


# Creation of the shop using list comprehension
number_of_items_in_shop = 500
shop_articles = ['gloves', 'hat', 'shirt', 'scarf']
shop_sizes = ['M', 'S', 'L', 'XL', 'XXL']
hobby_shop = [
    (article, size)
    for i in (range(int(number_of_items_in_shop / (len(shop_sizes) * len(shop_articles)))))
    for article in shop_articles
    for size in shop_sizes
]

# Creation of the shop without using list comprehension
# hobby_shop = []
# for i in (range(int(items_in_shop / (len(shop_sizes) * len(shop_articles))))):
#     for article in shop_articles:
#         for size in shop_sizes:
#             hobby_shop.append(article, size)
#             print(hobby_shop)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(hobby_shop)
# print(len(hobby_shop))

# Sell the last item from the shop
article, size = hobby_shop.pop()
print(f'The item sold on the last transaction was a {article} of size {size}.')

# Sell an item on a given position
position = 5
if position in range(number_of_items_in_shop):
    article, size = hobby_shop.pop(position)
    print(f'The item sold on position {position} was a {article} of size {size}.')

# Add new items in the shop
items_for_restock = [('t-shirt', 'S'), ('t-shirt', 'XL')]
hobby_shop.extend(items_for_restock)
pp.pprint(hobby_shop)
for new_item in items_for_restock:
    article, size = new_item
    print(f'The item added is: {article} of size {size}.')
