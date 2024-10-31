import customtkinter as ctk
from pandastable import Table
import pandas as pd

# قم بإنشاء بيانات كـ DataFrame للاختبار
data = {
    "الاسم": ["علي", "أحمد", "مريم"],
    "العمر": [25, 30, 22],
    "المدينة": ["بغداد", "البصرة", "أربيل"]
}
df = pd.DataFrame(data)

# إعداد CustomTkinter window
app = ctk.CTk()
app.geometry("600x400")
app.title("عرض البيانات باستخدام Pandastable")

# إعداد إطار لجدول البيانات
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True)

# استخدام pandastable لعرض DataFrame في الجدول
table = Table(frame, dataframe=df)
table.show()

# بدء التطبيق
app.mainloop()
