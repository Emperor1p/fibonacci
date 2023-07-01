
#fibonacci

num_terms = int(input("Enter the number of term you want: "))
print(f"fibonancci_sequence of {num_terms} is")
fibonancci_sequence = [0,1]
for i in range(2, num_terms):
    next_term = fibonancci_sequence[i-1] + fibonancci_sequence[i-2]
    fibonancci_sequence.append(next_term)

for term in fibonancci_sequence:

    print(term)

