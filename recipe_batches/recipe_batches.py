#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    arr = []
    if recipe.keys() == ingredients.keys():
        for i in recipe:
            for j in ingredients:
                if i == j:
                    if ingredients[j] // recipe[i] > 0:
                        print(i, ingredients[j] // recipe[i])
                        arr.append(ingredients[j] // recipe[i])
                    else:
                        arr.append(0)
    else:
        arr.append(0)

    return min(arr)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
               'milk': 1288, 'flour': 9, 'sugar': 95})

recipe_batches({'milk': 2}, {'milk': 200})
