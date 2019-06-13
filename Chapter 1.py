
# Problem 1.1 : G
# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except for the one at i




def arrayProduct(numbers):
    # Generate prefix product
    prefix_products = []
    for num in numbers:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
            
    # Generate suffix product
    suffix_products = []
    for num in reversed(numbers):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))
            
    # Generate result from the product of the prefixes and suffixes
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(numbers) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
            
    return result



numbers = [hash("foo"), hash("dog")]

print(arrayProduct(numbers))

print(hash("foo"))
            

