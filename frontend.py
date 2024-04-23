from tkinter import *
import backend 

def get_selected_row(event):
    global index, selected_tuple
    try:
        index = display_cars.curselection()[0]
        selected_tuple = display_cars.get(index)
        car_code_entry.delete(0, END)
        car_code_entry.insert(END, selected_tuple[1])
        model_entry.delete(0, END)
        model_entry.insert(END, selected_tuple[2])
        manufacturer_entry.delete(0, END)
        manufacturer_entry.insert(END, selected_tuple[3])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_tuple[4])
        fuel_capacity_entry.delete(0, END)
        fuel_capacity_entry.insert(END, selected_tuple[5])
        mileage_entry.delete(0, END)
        mileage_entry.insert(END, selected_tuple[6])
        horsepower_entry.delete(0 ,END)
        horsepower_entry.insert(END, selected_tuple[7])
        zero_to_60_entry.delete(0, END)
        zero_to_60_entry.insert(END, selected_tuple[8])
        top_speed_entry.delete(0 ,END)
        top_speed_entry.insert(END, selected_tuple[9])
        price_entry.delete(0 ,END)
        price_entry.insert(END, selected_tuple[10])
    except IndexError:
        pass

def view_command():
    display_cars.delete(0, END)
    for row in backend.view():
        display_cars.insert(END, row) 
        
def search_command():
    display_cars.delete(0, END)
    for row in backend.search(car_code_text.get(), model_text.get(), manufacturer_text.get(), year_text.get(), fuel_capacity_text.get(), mileage_text.get(), horsepower_text.get(), zero_to_60_text.get(), top_speed_text.get(), price_text.get()):
        display_cars.insert(END, row)
        
def add_command():
    backend.insert(car_code_text.get(), model_text.get(), manufacturer_text.get(), year_text.get(), fuel_capacity_text.get(), mileage_text.get(), horsepower_text.get(), zero_to_60_text.get(), top_speed_text.get(), price_text.get())
    display_cars.delete(0, END)
    display_cars.insert(END,(car_code_text.get(), model_text.get(), manufacturer_text.get(), year_text.get(), fuel_capacity_text.get(), mileage_text.get(), horsepower_text.get(), zero_to_60_text.get(), top_speed_text.get(), price_text.get()))
    
def update_command():
    backend.update(selected_tuple[0], car_code_text.get(), model_text.get(), manufacturer_text.get(), year_text.get(), fuel_capacity_text.get(),
     mileage_text.get(), horsepower_text.get(), zero_to_60_text.get(), top_speed_text.get(), price_text.get())

def delete_command():
    backend.delete(selected_tuple[0]) 

window = Tk()

window.wm_title("Car Management System")

car_code = Label(window, text = 'car code')
car_code.grid(row = 0, column = 0)
car_code_text = StringVar()
car_code_entry = Entry(window, textvariable = car_code_text)
car_code_entry.grid(row = 0, column = 1)


model_name = Label(window, text = 'Model')
model_name.grid(row = 0, column = 2)
model_text = StringVar()
model_entry = Entry(window, textvariable = model_text)
model_entry.grid(row = 0, column = 3)

manufacturer = Label(window, text = 'manufacturer')
manufacturer.grid(row = 0, column = 4)
manufacturer_text = StringVar()
manufacturer_entry = Entry(window, textvariable = manufacturer_text)
manufacturer_entry.grid(row = 0, column = 5)

year = Label(window, text = 'Year')
year.grid(row = 0, column = 6)
year_text = StringVar()
year_entry = Entry(window, textvariable = year_text)
year_entry.grid(row = 0, column = 7)

fuel_capacity = Label(window, text = 'fuel capacity (in Liters)')
fuel_capacity.grid(row = 0, column = 8)
fuel_capacity_text = StringVar()
fuel_capacity_entry = Entry(window, textvariable = fuel_capacity_text)
fuel_capacity_entry.grid(row = 0, column = 9)

mileage = Label(window, text = 'mileage')
mileage.grid(row = 1, column = 0)
mileage_text = StringVar()
mileage_entry = Entry(window, textvariable = mileage_text)
mileage_entry.grid(row = 1, column = 1)

horsepower = Label(window, text = 'Horsepower')
horsepower.grid(row = 1, column = 2)
horsepower_text = StringVar()
horsepower_entry = Entry(window, textvariable = horsepower_text)
horsepower_entry.grid(row = 1, column = 3)

zero_to_60 = Label(window, text = '0 to 60 mph')
zero_to_60.grid(row = 1, column = 4)
zero_to_60_text = StringVar()
zero_to_60_entry = Entry(window, textvariable = zero_to_60_text)
zero_to_60_entry.grid(row = 1, column = 5)

top_speed = Label(window, text = 'top speed')
top_speed.grid(row = 1, column = 6)
top_speed_text = StringVar()
top_speed_entry = Entry(window, textvariable = top_speed_text)
top_speed_entry.grid(row = 1, column = 7)

price = Label(window, text = 'price')
price.grid(row = 1, column = 8)
price_text = StringVar()
price_entry = Entry(window, textvariable = price_text)
price_entry.grid(row = 1, column = 9)

display_cars = Listbox(window, height = 6 , width = 120)
display_cars.grid(row = 2, column = 0 , rowspan = 5 , columnspan = 10)

scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column = 9, rowspan = 10)

display_cars.bind('<<ListboxSelect>>', get_selected_row)

view_button = Button(window, text = 'View All', width = 12, command = view_command)
view_button.grid(row = 11, column = 0)

add_button = Button(window, text = 'Add Car', width = 12, command = add_command)
add_button.grid(row = 11, column = 2)

search_entry_button = Button(window, text = 'Search Car', width = 12, command = search_command)
search_entry_button.grid(row = 11, column = 4)

update_entry_button = Button(window, text = 'Update Car', width = 12, command = update_command)
update_entry_button.grid(row = 11, column = 6)

delete_entry_button = Button(window, text = 'Delete Car', width = 12, command = delete_command)
delete_entry_button.grid(row = 11, column = 8)

close_button = Button(window, text = 'Close', width = 24, command= window.destroy)
close_button.grid(row = 12, column = 4)

window.mainloop()
