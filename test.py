import customtkinter as ctk

# إعداد نافذة التطبيق
app = ctk.CTk()

# إنشاء إطار لعلامات التبويب العمودية
tab_frame = ctk.CTkFrame(app)
tab_frame.pack(side="left", fill="y", padx=20, pady=20)

# إطار لمحتوى التبويبات
content_frame = ctk.CTkFrame(app)
content_frame.pack(side="right", fill="both", expand=True)

# وظيفة لتغيير المحتوى عند الضغط على زر
def show_tab(tab_name):
    for widget in content_frame.winfo_children():
        widget.destroy()  # مسح المحتوى السابق
    
    if tab_name == "التبويب الأول":
        label = ctk.CTkLabel(content_frame, text="هذا هو المحتوى في التبويب الأول")
        label.pack(pady=20)
    elif tab_name == "التبويب الثاني":
        label = ctk.CTkLabel(content_frame, text="هذا هو المحتوى في التبويب الثاني")
        label.pack(pady=20)
    elif tab_name == "التبويب الثالث":
        label = ctk.CTkLabel(content_frame, text="هذا هو المحتوى في التبويب الثالث")
        label.pack(pady=20)

# إضافة أزرار للتبويبات العمودية
tab1_button = ctk.CTkButton(tab_frame, text="التبويب الأول", command=lambda: show_tab("التبويب الأول"))
tab1_button.pack(pady=10, padx=10)

tab2_button = ctk.CTkButton(tab_frame, text="التبويب الثاني", command=lambda: show_tab("التبويب الثاني"))
tab2_button.pack(pady=10, padx=10)

tab3_button = ctk.CTkButton(tab_frame, text="التبويب الثالث", command=lambda: show_tab("التبويب الثالث"))
tab3_button.pack(pady=10, padx=10)

# إظهار التبويب الأول بشكل افتراضي
show_tab("التبويب الأول")

# تشغيل التطبيق
app.mainloop()
