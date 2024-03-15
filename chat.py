import os
import openai
import customtkinter as ctk
def Generate():
    prompt="please Generate 10 Ideas for coding projects"
    language=laguage_dropdown.get()
    prompt+="The programing language is " +language+ ". "
    difficulty=difficult_value.get()
    prompt+="The difficulty is " +difficulty+ ". "
    if Chechbox1.get():
        prompt+="The project should inlude the database"
    if Chechbox2.get():
        prompt+="The project should include the API"
    print(prompt)
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Generate response using GPT-3.5 model
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        message=[
            {"role": "user", "content": prompt}
        ]

    )

    # Extract and print the response
    answer = response.choices[0].message.content()
    print(answer)
window=ctk.CTk()
window.geometry("750x550")
window.title("ChatGPT Project Idea Generator")
ctk.set_appearance_mode("dark")
title_label=ctk.CTkLabel(window,text="Project Idea Generator",font=ctk.CTkFont(size=30,weight="bold"))
title_label.pack(padx=10,pady=(40,20))
frame=ctk.CTkFrame(window)
frame.pack(fill="x",padx=100)
language_frame=ctk.CTkFrame(frame)
language_frame.pack(padx=70,pady=(20,5),fill="both")
language_label=ctk.CTkLabel(language_frame,text="Programming Language",font=ctk.CTkFont(weight="bold"))
language_label.pack()
laguage_dropdown=ctk.CTkComboBox(language_frame,values=["python","Java","C++","JavaScript","Dart","Golang"])
laguage_dropdown.pack(pady=10)
difficult_frame=ctk.CTkFrame(frame)
difficult_frame.pack(padx=100,pady=5,fill="both")
difficult_label=ctk.CTkLabel(difficult_frame,text="Project difficulty",font=ctk.CTkFont(weight="bold"))
difficult_label.pack()
difficult_value=ctk.StringVar(value="Easy")
Radiobutton1=ctk.CTkRadioButton(difficult_frame,text="Easy",variable=difficult_value,value="Easy")
Radiobutton1.pack(padx=20,pady=10,side="left")
Radiobutton2=ctk.CTkRadioButton(difficult_frame,text="Medium",variable=difficult_value,value="Medium")
Radiobutton2.pack(padx=10,pady=10,side="left")
Radiobutton3=ctk.CTkRadioButton(difficult_frame,text="Hard",variable=difficult_value,value="Hard")
Radiobutton3.pack(padx=10,pady=10,side="left")
feature_frame=ctk.CTkFrame(frame)
feature_frame.pack(padx=100,pady=5,fill="both")
feature_label=ctk.CTkLabel(feature_frame,text="Features",font=ctk.CTkFont(weight="bold"))
feature_label.pack()
Chechbox1=ctk.CTkCheckBox(feature_frame,text="Database")
Chechbox1.pack(side="left",padx=50,pady=50)
Chechbox2=ctk.CTkCheckBox(feature_frame,text="API")
Chechbox2.pack(side="left",padx=50,pady=20)
button=ctk.CTkButton(frame,text="Generate Ideas",command=Generate)
button.pack(padx=100,fill="x",pady=(5,20))
result=ctk.CTkTextbox(window,font=ctk.CTkFont(size=15))
result.pack(pady=10,fill="x",padx=100)
window.mainloop()

