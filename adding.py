P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): ")) / 100
n = int(input("Enter number of times interest is compounded per year: "))
t = float(input("Enter time in years: "))

A = P * (1 + r / n) ** (n * t)

CI = A - P

print("\n----- Compound Interest Result -----")
print(f"Final Amount (A): {A:.2f}")
print(f"Compound Interest (CI): {CI:.2f}")
