def greatest_product_of_3(array):
    array.sort()

    return array[-1] * array[-2] * array[-3]
