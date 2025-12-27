import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import json
import copy
from datetime import datetime
import os
DATA_FILE = "pharmacy_data.json"
default_load_data = {
    "Tablets": [
        {"id": 1, "name": "Paracetamol", "price": 15, "quantity": 120, "expiry_date": "2026-04-12"},
        {"id": 3, "name": "Ibuprofen", "price": 30, "quantity": 200, "expiry_date": "2027-02-18"},
        {"id": 5, "name": "Azithromycin", "price": 85, "quantity": 60, "expiry_date": "2025-09-21"},
        {"id": 6, "name": "Vitamin C", "price": 25, "quantity": 180, "expiry_date": "2027-01-10"},
        {"id": 7, "name": "Panadol", "price": 20, "quantity": 150, "expiry_date": "2026-06-14"},
        {"id": 8, "name": "Brufen", "price": 32, "quantity": 90, "expiry_date": "2025-12-03"},
        {"id": 9, "name": "Augmentin", "price": 95, "quantity": 55, "expiry_date": "2026-03-27"},
        {"id": 10, "name": "Flagyl", "price": 28, "quantity": 100, "expiry_date": "2027-07-09"},
        {"id": 13, "name": "Aspirin", "price": 18, "quantity": 160, "expiry_date": "2027-05-02"},
        {"id": 15, "name": "Nexium", "price": 70, "quantity": 64, "expiry_date": "2025-10-25"},
        {"id": 18, "name": "Metformin", "price": 30, "quantity": 140, "expiry_date": "2027-06-17"},
        {"id": 19, "name": "Glucophage", "price": 38, "quantity": 95, "expiry_date": "2026-12-01"},
        {"id": 20, "name": "Lipitor", "price": 90, "quantity": 70, "expiry_date": "2025-07-29"},
        {"id": 21, "name": "Atorvastatin", "price": 50, "quantity": 110, "expiry_date": "2026-11-04"},
        {"id": 22, "name": "Losartan", "price": 42, "quantity": 130, "expiry_date": "2027-04-22"},
        {"id": 23, "name": "Amlodipine", "price": 35, "quantity": 85, "expiry_date": "2026-02-15"},
        {"id": 24, "name": "Norvasc", "price": 60, "quantity": 66, "expiry_date": "2025-09-09"},
        {"id": 27, "name": "Multivitamin", "price": 45, "quantity": 210, "expiry_date": "2027-09-14"},
        {"id": 29, "name": "Folic Acid", "price": 20, "quantity": 170, "expiry_date": "2026-07-07"},
        {"id": 30, "name": "Calcium D3", "price": 55, "quantity": 190, "expiry_date": "2027-10-19"},
        {"id": 31, "name": "Diclofenac", "price": 25, "quantity": 115, "expiry_date": "2026-03-05"},
        {"id": 32, "name": "Voltaren", "price": 40, "quantity": 92, "expiry_date": "2025-11-11"},
        {"id": 33, "name": "Ketoprofen", "price": 35, "quantity": 104, "expiry_date": "2027-01-26"},
        {"id": 34, "name": "Naproxen", "price": 45, "quantity": 78, "expiry_date": "2026-06-30"},
        {"id": 36, "name": "Famotidine", "price": 28, "quantity": 121, "expiry_date": "2027-02-09"},
        {"id": 40, "name": "Buscopan", "price": 35, "quantity": 97, "expiry_date": "2026-09-02"},
        {"id": 55, "name": "Domperidone", "price": 25, "quantity": 76, "expiry_date": "2026-02-27"},
        {"id": 57, "name": "Ondansetron", "price": 45, "quantity": 69, "expiry_date": "2027-05-12"},
        {"id": 58, "name": "Zofran", "price": 70, "quantity": 61, "expiry_date": "2026-08-08"},
        {"id": 59, "name": "Prednisolone", "price": 30, "quantity": 54, "expiry_date": "2025-10-31"},
        {"id": 60, "name": "Dexamethasone", "price": 28, "quantity": 73, "expiry_date": "2027-02-23"},
        {"id": 61, "name": "Loratadine", "price": 25, "quantity": 99, "expiry_date": "2026-04-06"},
        {"id": 64, "name": "Chlorpheniramine", "price": 20, "quantity": 83, "expiry_date": "2026-11-26"},
        {"id": 65, "name": "Montelukast", "price": 55, "quantity": 91, "expiry_date": "2027-03-18"},
        {"id": 66, "name": "Singulair", "price": 75, "quantity": 57, "expiry_date": "2026-01-22"},
        {"id": 67, "name": "Theophylline", "price": 30, "quantity": 62, "expiry_date": "2025-12-09"},
        {"id": 73, "name": "Ciprofloxacin", "price": 40, "quantity": 87, "expiry_date": "2025-10-02"},
        {"id": 74, "name": "Levofloxacin", "price": 55, "quantity": 68, "expiry_date": "2027-01-31"},
        {"id": 75, "name": "Moxifloxacin", "price": 80, "quantity": 59, "expiry_date": "2026-03-24"},
        {"id": 77, "name": "Co-trimoxazole", "price": 35, "quantity": 82, "expiry_date": "2026-07-03"},
        {"id": 80, "name": "Erythromycin", "price": 45, "quantity": 67, "expiry_date": "2026-09-15"},
        {"id": 83, "name": "Metoprolol", "price": 35, "quantity": 96, "expiry_date": "2026-06-23"},
        {"id": 84, "name": "Propranolol", "price": 30, "quantity": 89, "expiry_date": "2025-09-01"},
        {"id": 85, "name": "Bisoprolol", "price": 45, "quantity": 93, "expiry_date": "2027-10-08"},
        {"id": 86, "name": "Digoxin", "price": 25, "quantity": 56, "expiry_date": "2026-01-18"},
        {"id": 87, "name": "Furosemide", "price": 20, "quantity": 84, "expiry_date": "2025-12-04"},
        {"id": 88, "name": "Spironolactone", "price": 35, "quantity": 79, "expiry_date": "2027-05-27"},
        {"id": 89, "name": "Hydrochlorothiazide", "price": 28, "quantity": 90, "expiry_date": "2026-08-26"},
        {"id": 90, "name": "Enalapril", "price": 32, "quantity": 81, "expiry_date": "2025-10-18"},
        {"id": 91, "name": "Captopril", "price": 30, "quantity": 77, "expiry_date": "2027-03-06"},
        {"id": 92, "name": "Valsartan", "price": 55, "quantity": 86, "expiry_date": "2026-11-12"},
        {"id": 93, "name": "Warfarin", "price": 40, "quantity": 52, "expiry_date": "2025-09-26"},
        {"id": 95, "name": "Aspirin Cardio", "price": 22, "quantity": 108, "expiry_date": "2026-04-01"},
        {"id": 96, "name": "Clopidogrel", "price": 60, "quantity": 94, "expiry_date": "2027-01-04"},
        {"id": 97, "name": "Rivaroxaban", "price": 85, "quantity": 63, "expiry_date": "2025-12-17"},
        {"id": 98, "name": "Apixaban", "price": 90, "quantity": 58, "expiry_date": "2027-08-24"}
    ],
    "Capsules": [
        {"id": 2, "name": "Amoxicillin", "price": 45, "quantity": 75, "expiry_date": "2025-11-30"},
        {"id": 14, "name": "Omeprazole", "price": 35, "quantity": 88, "expiry_date": "2026-09-30"},
        {"id": 38, "name": "Antinal", "price": 22, "quantity": 58, "expiry_date": "2025-10-07"},
        {"id": 39, "name": "Imodium", "price": 40, "quantity": 80, "expiry_date": "2027-06-25"},
        {"id": 41, "name": "Probiotic Plus", "price": 60, "quantity": 65, "expiry_date": "2027-03-21"},
        {"id": 54, "name": "Loperamide", "price": 30, "quantity": 88, "expiry_date": "2027-09-05"},
        {"id": 71, "name": "Cefixime", "price": 65, "quantity": 72, "expiry_date": "2027-09-29"},
        {"id": 76, "name": "Nitrofurantoin", "price": 45, "quantity": 64, "expiry_date": "2027-08-11"},
        {"id": 78, "name": "Doxycycline", "price": 40, "quantity": 74, "expiry_date": "2025-12-21"},
        {"id": 79, "name": "Tetracycline", "price": 38, "quantity": 71, "expiry_date": "2027-04-28"}
    ],
    "Syrup": [
        {"id": 4, "name": "Coughnil", "price": 35, "quantity": 40, "expiry_date": "2026-08-05"},
        {"id": 11, "name": "Zyrtec", "price": 40, "quantity": 35, "expiry_date": "2026-10-11"},
        {"id": 12, "name": "Claritin", "price": 55, "quantity": 42, "expiry_date": "2025-08-19"},
        {"id": 16, "name": "Ventolin", "price": 45, "quantity": 28, "expiry_date": "2027-03-13"},
        {"id": 25, "name": "Salbutamol", "price": 28, "quantity": 31, "expiry_date": "2027-08-01"},
        {"id": 26, "name": "Dextromethorphan", "price": 33, "quantity": 47, "expiry_date": "2026-05-20"},
        {"id": 28, "name": "Ferrotron", "price": 40, "quantity": 39, "expiry_date": "2025-12-28"},
        {"id": 35, "name": "Ranitidine", "price": 30, "quantity": 44, "expiry_date": "2025-08-16"},
        {"id": 37, "name": "Gaviscon", "price": 50, "quantity": 33, "expiry_date": "2026-04-18"},
        {"id": 42, "name": "Zincovit", "price": 30, "quantity": 41, "expiry_date": "2025-12-14"},
        {"id": 56, "name": "Motilium", "price": 35, "quantity": 29, "expiry_date": "2025-11-19"},
        {"id": 62, "name": "Desloratadine", "price": 35, "quantity": 32, "expiry_date": "2025-09-13"},
        {"id": 63, "name": "Diphenhydramine", "price": 30, "quantity": 38, "expiry_date": "2027-07-01"},
        {"id": 68, "name": "Acetylcysteine", "price": 45, "quantity": 26, "expiry_date": "2027-06-04"},
        {"id": 69, "name": "Ambroxol", "price": 35, "quantity": 48, "expiry_date": "2026-08-16"},
        {"id": 70, "name": "Bromhexine", "price": 32, "quantity": 43, "expiry_date": "2025-11-27"},
        {"id": 99, "name": "Paracetamol Infant", "price": 18, "quantity": 46, "expiry_date": "2026-03-10"},
        {"id": 100, "name": "Zinc Syrup", "price": 22, "quantity": 37, "expiry_date": "2027-11-18"}
    ],
    "Injection": [
        {"id": 17, "name": "Insulin", "price": 180, "quantity": 22, "expiry_date": "2026-01-08"},
        {"id": 72, "name": "Ceftriaxone", "price": 120, "quantity": 18, "expiry_date": "2026-05-14"},
        {"id": 81, "name": "Benzylpenicillin", "price": 110, "quantity": 20, "expiry_date": "2025-11-05"},
        {"id": 82, "name": "Insulin Glargine", "price": 220, "quantity": 15, "expiry_date": "2027-02-07"},
        {"id": 94, "name": "Heparin", "price": 130, "quantity": 23, "expiry_date": "2027-06-15"}
    ],
    "Topical": [
        {"id": 47, "name": "Clotrimazole Cream", "price": 25, "quantity": 52, "expiry_date": "2026-10-03"},
        {"id": 48, "name": "Miconazole Cream", "price": 30, "quantity": 49, "expiry_date": "2025-09-17"},
        {"id": 49, "name": "Neosporin Ointment", "price": 40, "quantity": 36, "expiry_date": "2027-04-07"},
        {"id": 50, "name": "Fucidin Cream", "price": 55, "quantity": 45, "expiry_date": "2026-12-20"},
        {"id": 51, "name": "Hydrocortisone Cream", "price": 28, "quantity": 40, "expiry_date": "2027-01-15"},
        {"id": 52, "name": "Cetaphil Lotion", "price": 90, "quantity": 27, "expiry_date": "2026-06-11"},
        {"id": 53, "name": "Calamine Lotion", "price": 22, "quantity": 34, "expiry_date": "2025-08-24"},
        {"id": 45, "name": "Betadine Solution", "price": 35, "quantity": 24, "expiry_date": "2026-05-09"},
        {"id": 46, "name": "Dettol Solution", "price": 45, "quantity": 19, "expiry_date": "2027-08-30"}
    ],
    "Sachet": [
        {"id": 43, "name": "ORS", "price": 5, "quantity": 300, "expiry_date": "2026-07-28"},
        {"id": 44, "name": "Hydralyte", "price": 6, "quantity": 260, "expiry_date": "2027-11-06"}
    ]
}
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            total_items = sum(len(v) for v in data.values())
            if total_items < 20:
                print("Old data detected. Updating to full database...")
                return copy.deepcopy(default_load_data)
            return data
    except FileNotFoundError:
        return copy.deepcopy(default_load_data)
def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except:
        return False
def add_medicine(data, category, name, price, quantity, expiry):
    current_ids = [med["id"] for cat in data.values() for med in cat]
    new_id = max(current_ids) + 1 if current_ids else 1
    new_med = {"id": new_id, "name": name, "price": float(price), "quantity": int(quantity), "expiry_date": expiry}
    if category in data:
        data[category].append(new_med)
    else:
        data[category] = [new_med]
    save_data(data)
    return True
def delete_medicine(data, med_id):
    for category in data:
        for med in data[category]:
            if med["id"] == int(med_id):
                data[category].remove(med)
                save_data(data)
                return True
    return False
def restock_medicine(data, med_id, added_qty):
    for category in data:
        for med in data[category]:
            if med["id"] == int(med_id):
                med["quantity"] += int(added_qty)
                save_data(data)
                return True
    return False
def search_medicine(data, query):
    results = []
    for category, meds in data.items():
        for med in meds:
            if query.lower() in med['name'].lower():
                item = med.copy()
                item['category'] = category
                results.append(item)
    return results
def check_low_stock(data, threshold=40):
    low_stock = []
    for cat, meds in data.items():
        for med in meds:
            if med['quantity'] < threshold:
                item = med.copy()
                item['category'] = cat
                low_stock.append(item)
    return low_stock
def check_expired(data):
    expired = []
    today = datetime.now().date()
    for cat, meds in data.items():
        for med in meds:
            try:
                exp = datetime.strptime(med['expiry_date'], "%Y-%m-%d").date()
                if exp < today:
                    item = med.copy()
                    item['category'] = cat
                    expired.append(item)
            except:
                pass
    return expired
def process_sale_transaction(data, cart):
    total = 0
    for cart_item in cart:
        for cat, meds in data.items():
            for med in meds:
                if med['id'] == cart_item['id']:
                    med['quantity'] -= cart_item['qty']
                    total += (med['price'] * cart_item['qty'])
    save_data(data)
    return total
def generate_receipt_text(cart, total):
    txt = "\n--- ZC PHARMACY RECEIPT ---\n"
    txt += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    txt += "-" * 35 + "\n"
    for item in cart:
        txt += f"{item['name']:<15} {item['qty']:<5} {item['price'] * item['qty']:.2f}\n"
    txt += "-" * 35 + "\n"
    txt += f"TOTAL PAID: {total:.2f} EGP\n"
    with open("receipts_log.txt", "a", encoding="utf-8") as f: f.write(txt + "\n\n")
    return txt
# SECTION 3: GUI
class PharmacyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ZC City Pharmacy System")
        self.root.geometry("1000x650")
        self.data = load_data()
        self.cart = []
        self.login_frame = tk.Frame(root, bg="#dddddd")
        self.user_frame = tk.Frame(root)
        self.admin_frame = tk.Frame(root)
        for frame in (self.login_frame, self.user_frame, self.admin_frame):
            frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.build_login_screen()
        self.login_frame.tkraise()
    def build_login_screen(self):
        tk.Label(self.login_frame, text="🏥 ZC Pharmacy System", font=("Arial", 24, "bold"), bg="#dddddd").pack(pady=60)
        frm = tk.Frame(self.login_frame, bg="#dddddd")
        frm.pack()
        tk.Label(frm, text="Username:", bg="#dddddd", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        self.entry_user = tk.Entry(frm, font=("Arial", 12))
        self.entry_user.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(frm, text="Password:", bg="#dddddd", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
        self.entry_pass = tk.Entry(frm, show="*", font=("Arial", 12))
        self.entry_pass.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.login_frame, text="LOGIN", command=self.check_login, bg="#4CAF50", fg="white", width=15).pack(
            pady=20)
        tk.Label(self.login_frame, text="(Default: admin/1234 or user)", bg="#dddddd").pack()
    def check_login(self):
        u = self.entry_user.get()
        p = self.entry_pass.get()
        if u == "admin" and p == "1234":
            self.build_admin_screen()
            self.admin_frame.tkraise()
        elif u == "user":
            self.build_user_screen()
            self.user_frame.tkraise()
        else:
            messagebox.showerror("Error", "Invalid Credentials!")
    def logout(self):
        self.entry_user.delete(0, tk.END)
        self.entry_pass.delete(0, tk.END)
        self.login_frame.tkraise()
    def build_user_screen(self):
        for widget in self.user_frame.winfo_children(): widget.destroy()
        tk.Button(self.user_frame, text="Logout", command=self.logout, bg="red", fg="white").pack(anchor="ne", padx=10,
                                                                                                  pady=10)
        notebook = ttk.Notebook(self.user_frame)
        notebook.pack(fill="both", expand=True, padx=10)
        tab1 = tk.Frame(notebook)
        notebook.add(tab1, text="Search & Buy")
        frm_s = tk.Frame(tab1)
        frm_s.pack(pady=10)
        tk.Label(frm_s, text="Medicine Name:").pack(side="left")
        self.search_ent = tk.Entry(frm_s, width=30)
        self.search_ent.pack(side="left", padx=5)
        tk.Button(frm_s, text="Search", command=self.user_search).pack(side="left")
        cols = ("ID", "Name", "Category", "Price", "Stock")
        self.tree = ttk.Treeview(tab1, columns=cols, show="headings", height=15)
        for c in cols: self.tree.heading(c, text=c)
        self.tree.column("ID", width=50)
        self.tree.pack(fill="both", expand=True, padx=10)
        frm_buy = tk.Frame(tab1, bg="#eee", bd=1, relief="solid")
        frm_buy.pack(fill="x", padx=10, pady=10)
        tk.Label(frm_buy, text="Add to Cart -> ID:", bg="#eee").pack(side="left", padx=5)
        self.cart_id_ent = tk.Entry(frm_buy, width=5)
        self.cart_id_ent.pack(side="left", padx=5)
        tk.Label(frm_buy, text="Qty:", bg="#eee").pack(side="left", padx=5)
        self.cart_qty_ent = tk.Entry(frm_buy, width=5)
        self.cart_qty_ent.pack(side="left", padx=5)
        tk.Button(frm_buy, text="Add +", command=self.add_to_cart, bg="green", fg="white").pack(side="left", padx=10)
        tab2 = tk.Frame(notebook)
        notebook.add(tab2, text="My Cart")
        self.cart_listbox = tk.Listbox(tab2, font=("Courier", 10))
        self.cart_listbox.pack(fill="both", expand=True, padx=10, pady=10)
        tk.Button(tab2, text="Checkout & Print Receipt", command=self.checkout, bg="orange").pack(pady=10)
        self.user_search(load_all=True)
    def user_search(self, load_all=False):
        query = self.search_ent.get()
        if load_all: query = ""
        results = search_medicine(self.data, query)
        for i in self.tree.get_children(): self.tree.delete(i)
        for item in results:
            self.tree.insert("", "end",
                             values=(item['id'], item['name'], item['category'], item['price'], item['quantity']))
    def add_to_cart(self):
        try:
            mid = int(self.cart_id_ent.get())
            qty = int(self.cart_qty_ent.get())
            found = None
            for cat, meds in self.data.items():
                for med in meds:
                    if med['id'] == mid: found = med
            if found and found['quantity'] >= qty:
                self.cart.append({"id": mid, "name": found['name'], "price": found['price'], "qty": qty})
                messagebox.showinfo("Success", f"Added {found['name']}")
                self.update_cart_ui()
            else:
                messagebox.showwarning("Error", "Check ID or Stock")
        except:
            messagebox.showerror("Error", "Invalid Input")
    def update_cart_ui(self):
        self.cart_listbox.delete(0, tk.END)
        total = 0
        for item in self.cart:
            sub = item['price'] * item['qty']
            total += sub
            self.cart_listbox.insert(tk.END, f"{item['name']} x{item['qty']} = {sub} EGP")
        self.cart_listbox.insert(tk.END, "-" * 30)
        self.cart_listbox.insert(tk.END, f"TOTAL: {total} EGP")
    def checkout(self):
        if not self.cart: return
        total = process_sale_transaction(self.data, self.cart)
        msg = generate_receipt_text(self.cart, total)
        messagebox.showinfo("Receipt", msg)
        self.cart = []
        self.update_cart_ui()
        self.user_search(load_all=True)
    def build_admin_screen(self):
        for widget in self.admin_frame.winfo_children(): widget.destroy()
        tk.Button(self.admin_frame, text="Logout", command=self.logout, bg="red", fg="white").pack(anchor="ne", padx=10,
                                                                                                   pady=10)
        tk.Label(self.admin_frame, text="Admin Dashboard", font=("Arial", 18)).pack(pady=10)
        low = check_low_stock(self.data)
        exp = check_expired(self.data)
        tk.Label(self.admin_frame, text=f"⚠️ Low Stock: {len(low)} | 📅 Expired: {len(exp)}", fg="red",
                 font=("Arial", 12)).pack()
        frm = tk.Frame(self.admin_frame)
        frm.pack(pady=20)
        tk.Button(frm, text="Add Medicine", width=20, command=self.adm_add).grid(row=0, column=0, pady=5)
        tk.Button(frm, text="Restock", width=20, command=self.adm_restock).grid(row=0, column=1, pady=5)
        tk.Button(frm, text="Delete Medicine", width=20, command=self.adm_del).grid(row=1, column=0, pady=5)
        tk.Button(frm, text="Reset Data", width=20, command=self.adm_reset).grid(row=1, column=1, pady=5)
    def adm_add(self):
        val = simpledialog.askstring("Add", "Category,Name,Price,Qty,YYYY-MM-DD")
        if val:
            try:
                c, n, p, q, e = val.split(",")
                add_medicine(self.data, c, n, p, q, e)
                messagebox.showinfo("Success", "Added")
            except:
                messagebox.showerror("Error", "Format Error")
    def adm_del(self):
        mid = simpledialog.askinteger("Delete", "Enter ID:")
        if mid and delete_medicine(self.data, mid):
            messagebox.showinfo("Success", "Deleted")
        else:
            messagebox.showerror("Error", "Not Found")
    def adm_restock(self):
        val = simpledialog.askstring("Restock", "ID,Qty")
        if val:
            try:
                i, q = val.split(",")
                if restock_medicine(self.data, i, q):
                    messagebox.showinfo("Success", "Updated")
                else:
                    messagebox.showerror("Error", "Not Found")
            except:
                pass
    def adm_reset(self):
        if messagebox.askyesno("Reset", "Reset all data to full 100 items?"):
            global default_load_data
            self.data = copy.deepcopy(default_load_data)
            save_data(self.data)
            messagebox.showinfo("Reset", "Data Reset Successfully")
            self.build_admin_screen()
if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyApp(root)
    root.mainloop()