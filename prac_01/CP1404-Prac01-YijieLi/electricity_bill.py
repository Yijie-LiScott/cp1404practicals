TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = input("Which tariff? 11 or 31: ").strip()
while tariff not in ("11", "31"):
    tariff = input("Which tariff? 11 or 31: ").strip()

rate = TARIFF_11 if tariff == "11" else TARIFF_31

daily_use = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))

estimated = rate * daily_use * days
print(f"Estimated bill: ${estimated:.2f}")