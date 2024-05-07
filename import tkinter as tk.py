import tkinter as tk

conversion_table = {
    "USD": {
        "EUR": 0.85,
        "GBP": 0.72,
        "JPY": 109.71,
        "CAD": 1.22,
        "AUD": 1.32
    },
    "EUR": {
        "USD": 1.18,
        "GBP": 0.85,
        "JPY": 129.67,
        "CAD": 1.47,
        "AUD": 1.59
    },
    "GBP": {
        "USD": 1.39,
        "EUR": 1.18,
        "JPY": 151.37,
        "CAD": 1.70,
        "AUD": 1.84
    },
    "JPY": {
        "USD": 0.0091,
        "EUR": 0.0077,
        "GBP": 0.0066,
        "CAD": 0.011,
        "AUD": 0.012
    },
    "CAD": {
        "USD": 0.82,
        "EUR": 0.68,
        "GBP": 0.59,
        "JPY": 87.47,
        "AUD": 1.08
    },
    "AUD": {
        "USD": 0.76,
        "EUR": 0.63,
        "GBP": 0.54,
        "JPY": 81.75,
        "CAD": 0.93
    }
}

def convert_currency():
    amount = float(entry.get())
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()

    if base_currency == target_currency:
        converted_amount = amount
    else:
        conversion_rate = conversion_table[base_currency][target_currency]
        converted_amount = amount * conversion_rate

    result_label.config(text=str(converted_amount))

window = tk.Tk()
window.title("Currency Converter")

label1 = tk.Label(window, text="Amount:")
label1.pack()

entry = tk.Entry(window)
entry.pack()

label2 = tk.Label(window, text="Base Currency:")
label2.pack()

base_currency_var = tk.StringVar()
base_currency_var.set("USD")

base_currency_menu=tk.OptionMenu(window,base_currency_var,*conversion_table.keys())
base_currency_menu.pack()

label3 = tk.Label(window, text="Target Currency:")
label3.pack()

target_currency_var = tk.StringVar()
target_currency_var.set("EUR")

target_currency_menu=tk.OptionMenu(window,target_currency_var,*conversion_table.keys())
target_currency_menu.pack()

label4 = tk.Label(window, text="Converted Amount:")
label4.pack()

result_label = tk.Label(window, text="")
result_label.pack()

button = tk.Button(window, text="Convert", command=convert_currency)
button.pack()

window.mainloop()

