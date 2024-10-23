import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("1000x500")
app.grid_columnconfigure(2, weight=1)

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()