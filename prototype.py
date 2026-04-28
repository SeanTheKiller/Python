import json
import os

#with open(file_path, "a") as "f":
#   data_list = json.load(f)
class Prototype:

    def option_1(self):
        #1 User input data into list from "variables" to LIST SET
        model1 = "justname"
        model2 = "xray"

        sets = {                    #2 Create a dictionary to store data
            "doctor": model1,
            "type": model2
            }

        file_path = "listout.json" # name the json file using a variable 
        data_list = [] # Create an empty list 

        # Load existing data if file exists
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    data_list = json.load(f)
            except (json.JSONDecodeError, ValueError):
                # If file is empty or corrupted, start with an empty list
                data_list = []

        # 3. Add the new entry
        data_list.append(sets)

        # 4. Save back to file
        try:
            with open(file_path, "w") as f:
                json.dump(data_list, f, indent=4)
            print(f"Successfully updated '{file_path}'")
        except IOError as e:
            print(f"File system error: {e}")


        with open(file_path, "r") as f:
            data_list = json.load(f)

        print(f"{"="*40}\n{"Ranking":^40}\n{"="*40}")
        for show in data_list:
            print(f"{show["doctor"]:<10}| {show["type"]}") #


    def option_2(self):
        print("im a blackie!!")

list = Prototype()
user_input = int(input("Enter number: "))
if user_input == 1:
    list.option_1()

elif user_input == 2:
    list.option_2()

elif user_input == 3:

    for i in range(10, 0, -1):
        print(i)

else:
    print("Quit")



