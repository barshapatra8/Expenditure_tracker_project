import tkinter as tk
import pandas as pd 
from matplotlib import pyplot as plt





root = tk.Tk()
root.geometry("1000x550")
root.title("Expense Tracker")
root.configure(background="#232323")

item_list = []


def add_item():
    item = item_text.get()
    qty = qty_text.get()
    cost = cost_text.get()
    total = int(qty) * int(cost)
    #print(item, qty, cost, total)
    single_item_lbl = tk.Label(frame2, text=f"{item}\t\t{qty}\t\t{cost}\t\t{total}",bg = "#232323", fg = "#ffffff", font= ("Arial 15"))
    single_item = {"Item":item, "Quantity":qty, "Cost":cost, "Total Amount":total}
    item_list.append(single_item)
    single_item_lbl.pack(pady=5)


def clear_item():
    item_text.delete(0, "end")
    qty_text.delete(0, "end")
    cost_text.delete(0, "end")

def analyse():
    df = pd.DataFrame(item_list)
    items = df["Item"]
    total = df["Total Amount"]
    fig = plt.figure(figsize=(10, 5))
    plt.bar(items, total, color="red", width=0.4)
    plt.ylabel("Cost Of Items")
    plt.xlabel("Items Purchased")
    plt.title("Expenditure Tracker Analysis")
    plt.show()


title_lbl = tk.Label(root, text = "Expenditure Tracker",bg = "#232323", fg = "#ffffff", font= ("Arial 20"))
title_lbl.pack(pady=30)

item_lbl = tk.Label(root, text = "Item",bg = "#232323", fg = "#ffffff", font= ("Arial 15"))
item_lbl.pack(pady=(30,5))

item_text = tk.Entry(root, font= ("Arial 15"))
item_text.pack()

qty_lbl = tk.Label(root, text = "Quantity",bg = "#232323", fg = "#ffffff", font= ("Arial 15"))
qty_lbl.pack(pady=(30, 5))

qty_text = tk.Entry(root, font=("Arial 15"))
qty_text.pack()

cost_lbl = tk.Label(root, text = "Cost per Unit",bg = "#232323", fg = "#ffffff", font= ("Arial 15"))
cost_lbl.pack(pady=(30, 5))

cost_text = tk.Entry(root, font=("Arial 15"))
cost_text.pack()

frame1 = tk.Frame(root, bg="#232323")

add_btn = tk.Button(frame1, text = "Add Item",bg = "#2a2a2a", fg = "#ffffff", font= ("Arial 15"), command=add_item)
add_btn.pack(padx=10, pady=20, side=tk.LEFT)

clear_btn = tk.Button(frame1, text = "Clear",bg = "#2a2a2a", fg = "#ffffff", font= ("Arial 15"), command=clear_item)
clear_btn.pack(side= tk.RIGHT)

frame1.pack()

display_lbl = tk.Label(root, text = "Expenses",bg = "#232323", fg = "#ffffff", font= ("Arial 15"))
display_lbl.pack(pady=(30, 5))

frame2 = tk.Frame(root, bg="#232323")
heading_lbl = tk.Label(frame2, text = "Item\t\tQuantity\t\tUnit Cost\t\tTotal",bg = "#232323", fg = "#ffffff", font= ("Arial 15"))
heading_lbl.pack(pady=5)
frame2.pack()

analyse_btn = tk.Button(root, text = "Analyse",bg = "#2a2a2a", fg = "#ffffff", font= ("Arial 15"), command=analyse)
analyse_btn.pack(pady=30)

root.mainloop()
