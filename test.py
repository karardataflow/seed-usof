import customtkinter as ctk

def show_selection():
    selection = radio_var.get()
    label.config(text=f"You selected: {selection}")

# إنشاء نافذة التطبيق
ctk.set_appearance_mode("light")  # يمكنك تغيير الوضع إلى "dark" إذا أردت
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("CustomTkinter Radio Button Example")

# متغير لتخزين قيمة الزر المختار
radio_var = ctk.StringVar(value="Option 1")

# إنشاء إطار لترتيب العناصر
frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20)

# إنشاء أزرار راديو
radio1 = ctk.CTkRadioButton(frame, text="Option 1", variable=radio_var, value="Option 1", command=show_selection)
radio2 = ctk.CTkRadioButton(frame, text="Option 2", variable=radio_var, value="Option 2", command=show_selection)
radio3 = ctk.CTkRadioButton(frame, text="Option 3", variable=radio_var, value="Option 3", command=show_selection)

# إنشاء تسمية لعرض الاختيار
label = ctk.CTkLabel(root, text="You selected: None")

# ترتيب العناصر في نافذة التطبيق
label.pack(anchor='e', padx=20)  # الاسم على اليسار
radio1.pack(anchor='e')  # أزرار الراديو على اليمين
radio2.pack(anchor='e')
radio3.pack(anchor='e')

# تشغيل حلقة الأحداث
root.mainloop()
