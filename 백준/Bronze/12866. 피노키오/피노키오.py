dna = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
num = int(input())
string = input()
for ch in string:
    dna[ch] += 1

summation = 1
for i in dna:
    summation *= dna[i]

print(summation % 1000000007)