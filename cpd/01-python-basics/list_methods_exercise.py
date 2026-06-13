# Using the list below:
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove "Banana" from the list.
# 2. Remove "Blueberries" from the list.
# 3. Add "Kiwi" to the end of the list.
# 4. Add "Apples" to the beginning of the list.
# 5. Count how many "Apples" are in the basket.
# 6. Empty the basket.

# Solution #

# Starting list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 1. Remove "Banana"
basket.remove("Banana")
# 2. Remove "Blueberries"
basket.remove("Blueberries")
# 3. Add "Kiwi" to the end
basket.append("Kiwi")
# 4. Add "Apples" to the beginning
basket.insert(0,"Apples")
# 5. Count how many "Apples"
basket.count("Apples") # (not printed, just executed)
# 6. Empty the basket
basket.clear()

print(basket)