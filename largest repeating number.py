s = [1, 2, 3, 3, 5, 6, 1,  1, 3]
freq ={}
for i in range (0, len(s)):
    if s[i] in freq:
        freq[s[i]] = freq[s[i]]+1
    else:
        freq[s[i]] = 1
print(freq)

maxFreq = 0
maxElement = 0
for i in freq.keys():
    if freq[i] > maxFreq:
        maxFreq = freq[i]
        maxElement = i
print(maxElement)
    