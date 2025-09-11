'''4. There is a list with some numbers. Create a new
dictionary using this list in such a way that key is
number and value is frequency of occurrence of that
number in list.'''



numbers = [1,2,3,4,5,6,7]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Display the dictionary
print("Frequency dictionary:", frequency)

 
