#Python Program to Sort a List According to the Length of the Elements within the list.
words = [1123,34,5,678,906754,22,123,]

n = len(words)

for i in range(n):
    for j in range(0, n - i - 1):
        if words[j] > words[j + 1]:
            words[j], words[j + 1] = words[j + 1], words[j]

print("Sorted by length:", words)