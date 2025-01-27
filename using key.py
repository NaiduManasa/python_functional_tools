data = [(1, 'apple'), (3, 'banana'), (2, 'orange'),(6, 'mango')]
sorted_data1 = sorted(data, key=lambda x: x[0]) #sorted be key
sorted_data2 = sorted(data, key=lambda x: x[1]) #sorted by value
print(sorted_data1)
print(sorted_data2)
print("_____________________________________")

words = ['apple', 'banana', 'kiwi', 'grape']
longest_word = max(words, key=lambda x: len(x))
shortest_word = min(words, key=lambda x: len(x))
print("logest word:" , longest_word)
print("shortest word:" , shortest_word)  