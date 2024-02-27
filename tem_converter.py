import customtkinter as ctk
def convert_temperature():
    choice = selected_value.get()
    if choice == "C":
        convert_to_celsius()
    else : convert_to_fahrenheit()

def convert_to_celsius():
    fahrenheit = 100
    celsius = (fahrenheit - 32) * 5 // 9
    celsius_text = f"{celsius}  °C"
    print(celsius_text)
    label_result.insert()


def convert_to_fahrenheit():
    celsius = float(temp_entry.get())
    fahrenheit = (celsius * 9 / 5)+ 32
    fahrenheit_text = f"{fahrenheit} °F"
    label_result.set()
jj

window = ctk.CTk()
ctk.set_appearance_mode("dark")
window.geometry("600x400")
window.title("Temperature Converter")

title_label = ctk.CTkLabel(window,text = "Temperature Converter",font = ctk.CTkFont(size=30,weight = "bold"))
title_label.pack(padx=10,pady =(30,20))

radio_frame = ctk.CTkFrame(window)
radio_frame.pack(fill = "x", padx=50)

selected_value = ctk.StringVar(value = "C")

radio_ftoc = ctk.CTkRadioButton(radio_frame,text = "Fahrenheit to Celsius",variable= selected_value,value="C")
radio_ftoc.pack(side= "left", padx=(80,10),pady=10)

radio_ctof = ctk.CTkRadioButton(radio_frame,text="Celsius to Fahrenheit", variable = selected_value,value= "F")
radio_ctof.pack(side = "left",padx = 10,pady = 10)

input_frame = ctk.CTkFrame(window)
input_frame.pack(fill = "x",padx=50,pady=30)

temp_entry = ctk.CTkEntry(input_frame,placeholder_text="Enter temperature...")
temp_entry.pack(side= "left",padx=(40,10),pady = 10)

convert_button = ctk.CTkButton(input_frame,text= "Convert", command= convert_temperature)
convert_button.pack(side="right",padx=10,pady=20)

result_frame = ctk.CTkFrame(window)
result_frame.pack(fill="x",padx=50,pady=(10,50))

label_result = ctk.CTkFrame(window)
label_result.pack(fill="x",padx=50)
window.mainloop()