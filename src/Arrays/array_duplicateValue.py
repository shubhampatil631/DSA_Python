#DSA Day-1
num=[1,1,1,3,3,4,3,2,4,2]
if len(set(num)) == len(num):
    print("No duplicate values")
else:
    print("Duplicate values are present")
    print("Unique values:", set(num))
    seen = set()
    duplicates = list(x for x in num if x in seen or seen.add(x))
    print("Duplicate values:", duplicates)