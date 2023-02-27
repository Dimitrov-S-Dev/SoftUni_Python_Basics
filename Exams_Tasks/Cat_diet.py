"""
fat = 9 kcal
protein = 4kcal
carbs = 4 kcal
"""

percent_fat = int(input()) / 100
percent_protein = int(input()) / 100
percent_carbs = int(input()) / 100
total_kcal = int(input())
percent_water = int(input()) / 100

fat_gram = (total_kcal * percent_fat) / 9
protein_gram = (total_kcal * percent_protein) / 4
carb_gram = (total_kcal * percent_carbs) / 4

total_grams = fat_gram + protein_gram + carb_gram
calories = total_kcal / total_grams
calories *= (1 - percent_water)


print(f"{calories:.4f}")
