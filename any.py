import customtkinter as ctk
from PIL import Image, ImageTk

# النص
x = '''جمهورية العراق 
هيئة النزاهة الاتحادية 
دائرة التحقيقات 
مديرية تحقيق البصرة'''

# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")  

def create_responsive_gui():
    # Create the main window
    root = ctk.CTk()
    root.title("Responsive CustomTkinter GUI")
    
    # Set the window size
    root.geometry("600x400")

    # Create a main frame
    main_frame = ctk.CTkFrame(root, fg_color="#1D3C6B")
    main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

    # Create a sub frame
    sub_frame = ctk.CTkFrame(main_frame, fg_color="#FFFFFF", height=125 , corner_radius=20)
    sub_frame.grid(row=0, column=0, columnspan=30, padx=15, pady=10, sticky="nsew")

    # Load images (ensure correct paths)
    img1 = Image.open("img/INV_logo.jpg").resize((120, 90), Image.LANCZOS)  
    img1_tk = ImageTk.PhotoImage(img1)
    img_label1 = ctk.CTkLabel(sub_frame, image=img1_tk, text='')
    img_label1.grid(row=0, column=2, padx=5, pady=10)

    img_label1.image = img1_tk
    img2 = Image.open("img/images.png").resize((120, 120), Image.LANCZOS)
    img2_tk = ImageTk.PhotoImage(img2)
    img_label2 = ctk.CTkLabel(sub_frame, image=img2_tk, text='')
    img_label2.grid(row=0, column=0, padx=5, pady=10)

    img_label2.image = img2_tk
    label = ctk.CTkLabel(sub_frame, text=x, text_color="black", font=("Arial", 20, "bold"))
    label.grid(row=0, column=1, padx=5, pady=5)

    # Create a frame for the inquiries
    inquiry_frame = ctk.CTkFrame(main_frame, fg_color="#44689D", corner_radius=30)
    inquiry_frame.grid(row=1, column=0, columnspan=3, padx=55, pady=15)

    label2 = ctk.CTkLabel(inquiry_frame, text="الأستعلامات", 
                           text_color="#ffffff", width=300, height=70, font=("Arial", 36, "bold"))
    label2.pack(padx=80, pady=15)


    image = Image.open('img/noun-6560269-FFFFFF.png')
    icon = ImageTk.PhotoImage(image)


    # Name Entry
    frame_name = ctk.CTkFrame(master=main_frame, height=40 ,corner_radius=10 , fg_color='#44689D')
    frame_name.grid(row=2, column=1, padx=68, pady=55/2, sticky="ew")

    label_name = ctk.CTkLabel(master=frame_name, text="الأسم", bg_color="#44689D", width=120, image=icon, compound="right", font=("Arial", 20, "bold"))
    label_name.pack(padx=10, side="right")

    en_name = ctk.CTkEntry(
        master=frame_name, 
        fg_color='#ffffff', 
        bg_color='white', 
        border_color='#ffffff', 
        width=380, 
        height=40,
        text_color="black",  # لون الخط
        font=("Arial", 16),  # حجم الخط
        justify="right"      # اتجاه النص
    )
    en_name.pack(fill=ctk.X, expand=True)

    # Job Entry

    image = Image.open('img/noun-profession-6346513-FFFFFF.png')
    icon = ImageTk.PhotoImage(image)

    frame_job = ctk.CTkFrame(master=main_frame, height=40 ,corner_radius=10 , fg_color='#44689D')
    frame_job.grid(row=2, column=0, padx=68, pady=55/2, sticky="ew")

    label_job = ctk.CTkLabel(master=frame_job, text="الوظيفة", bg_color="#44689D", width=120, image=icon, compound="right", font=("Arial", 20, "bold"))
    label_job.pack(padx=10, side="right")

    en_job = ctk.CTkEntry(
        master=frame_job, 
        fg_color='#ffffff', 
        bg_color='white', 
        border_color='#ffffff', 
        width=380, 
        height=40,
        text_color="black", 
        font=("Arial", 16), 
        justify="right"     
    )
    en_job.pack(fill=ctk.X, expand=True)

    # Identity Entry

    image = Image.open('img/noun-name-1946973-FFFFFF.png')
    icon = ImageTk.PhotoImage(image)

    frame_identity = ctk.CTkFrame(master=main_frame, height=40 ,corner_radius=10 , fg_color='#44689D')
    frame_identity.grid(row=3, column=1, padx=68, pady=55/2, sticky="ew")

    label_identity = ctk.CTkLabel(master=frame_identity, text="رقم الهوية", bg_color="#44689D", width=120, image=icon, compound="right", font=("Arial", 20, "bold"))
    label_identity.pack(padx=10, side="right")

    en_identity = ctk.CTkEntry(
        master=frame_identity, 
        fg_color='#ffffff', 
        bg_color='white', 
        border_color='#ffffff', 
        width=380, 
        height=40,
        text_color="black", 
        font=("Arial", 16), 
        justify="right"     
    )
    en_identity.pack(fill=ctk.X, expand=True)

    # Date Entry
    frame_date = ctk.CTkFrame(master=main_frame, height=40 ,corner_radius=10 , fg_color='#44689D')
    frame_date.grid(row=3, column=0, padx=68, pady=55/2, sticky="ew")

    label_date = ctk.CTkLabel(master=frame_date, text="تاريخ وجهة الاصدار", bg_color="#44689D", width=120, image=icon, compound="right", font=("Arial", 20, "bold"))
    label_date.pack(padx=10, side="right")

    en_date = ctk.CTkEntry(
        master=frame_date, 
        fg_color='#ffffff', 
        bg_color='white', 
        border_color='#ffffff', 
        width=380, 
        height=40,
        text_color="black", 
        font=("Arial", 16), 
        justify="right"     
    )
    en_date.pack(fill=ctk.X, expand=True)

    # Review Entry

    image = Image.open('img/noun-contact-details-6046708-FFFFFF (1).png')
    icon = ImageTk.PhotoImage(image)

    frame_dis = ctk.CTkFrame(master=main_frame, height=40 ,corner_radius=10 , fg_color='#44689D')
    frame_dis.grid(row=4, column=0, columnspan=3, padx=68, pady=55/2, sticky="ew")

    label_dis = ctk.CTkLabel(master=frame_dis, text="صفة المراجعة", bg_color="#44689D", width=120, image=icon, compound="right", font=("Arial", 20, "bold"))
    label_dis.pack(padx=10, side="right")

    en_dis = ctk.CTkEntry(
        master=frame_dis, 
        fg_color='#ffffff', 
        bg_color='white', 
        border_color='#ffffff', 
        width=380, 
        height=40,
        text_color="black", 
        font=("Arial", 16), 
        justify="right"     
    )
    en_dis.pack(fill=ctk.X, expand=True)


    image = Image.open('img/noun-name-card-1906376-FFFFFF.png')
    icon = ImageTk.PhotoImage(image)

    frame_side = ctk.CTkFrame(master=main_frame, height=40 ,corner_radius=10 , fg_color='#44689D')
    frame_side.grid(row=5, column=0, columnspan=3, padx=68, pady=55/2, sticky="ew")

    label_side = ctk.CTkLabel(master=frame_side, text="جهة المراجعة", bg_color="#44689D", width=120, image=icon, compound="right", font=("Arial", 20, "bold"))
    label_side.pack(padx=10, side="right")
    

    en_side = ctk.CTkEntry(
        master=frame_side, 
        fg_color='#ffffff', 
        bg_color='white', 
        border_color='#ffffff', 
        width=380, 
        height=40,
        text_color="black", 
        font=("Arial", 16), 
        justify="right"     
    )
    en_side.pack(fill=ctk.X, expand=True)

    image = Image.open('img/noun-submit-6735931-FFFFFF.png')
    icon = ImageTk.PhotoImage(image)



    submit_btn = ctk.CTkButton (master=main_frame , width=227, height=64 , corner_radius=30 , fg_color="#44689D", image=icon, compound="left", text='')
    submit_btn.grid(row=6, column=0, columnspan=1, padx=68, pady=27.5, sticky="w")


    image = Image.open('img/noun-7211434-FFFFFF.png')
    icon = ImageTk.PhotoImage(image)


    finprin_btn = ctk.CTkButton (master=main_frame , width=227, height=64 , corner_radius=30 , fg_color="#44689D", image=icon, compound="left", text='')
    finprin_btn.grid(row=6, column=1, columnspan=1, padx=68, pady=27.5, sticky="e")




    # Configure grid weights for responsive resizing
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    # Configure sub_frame grid weights
    sub_frame.grid_columnconfigure(0, weight=0)  
    sub_frame.grid_columnconfigure(1, weight=1)  
    sub_frame.grid_columnconfigure(2, weight=0)

    # Start the application
    root.mainloop()

create_responsive_gui()
