shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         continue            # continue restarts the for loop bypassing print
#
#     print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break            # break stops the for loop completely

    print("Buy " + item)

