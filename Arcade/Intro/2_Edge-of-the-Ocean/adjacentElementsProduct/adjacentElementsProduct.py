def adjacentElementsProduct(values):
    products = []

    for i in range(len(values) - 1):
        products.append(values[i] * values[i + 1])

    products.sort(reverse=True)
    return products[0]


print(adjacentElementsProduct([3, 6, -2, -5, -12, 3]))
