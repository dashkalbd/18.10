class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def __call__(self, amount):
        return amount * self.rate


uah_to_usd = CurrencyConverter(0.024)
uah_to_eur = CurrencyConverter(0.022)
usd_to_uah = CurrencyConverter(41.5)

print("1000 грн =", uah_to_usd(1000), "$")
print("1000 грн =", uah_to_eur(1000), "€")
print("100 $ =", usd_to_uah(100), "грн")