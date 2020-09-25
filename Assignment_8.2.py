dict = {}

while(1):

    print("------ WELCOME TO VIRTUAL GARAGE------")

    vehicle = input("What do you want to add Car/Pickup? ")

    print("Please enter attributes for ",vehicle,"separated by comma ',' ")

    attributes = input()

    options = ['power mirrors', 'power locks','remote start', 'backup camera', 'bluetooth', 'cruise control']

    dict[vehicle.lower()] = []

    dict[vehicle.lower()].append(attributes.split(','))

    print("Please select any of the following options to add:")

    for i in range(len(options)):

        print(i+1," : ",options[i])

        while(1):

            option = int(input('option: '))

            check = input("still want to add? y/n: ")

            dict[vehicle.lower()].append(options[option])

            if check.lower() == 'n':

                break

                if 'car' in dict and 'pickup' in dict:

                    cont = input("Continue? y/n: ")

                    if cont == 'n':

                        print("----------------------------------------------------")

                        print("----------- VIRTUAL GARAGE--------------------------")

                        print("----------------------------------------------------")

                        print("vehicle attributes options")

                        for key in dict.keys():

                            opt = dict[key]

                            attr = dict[key]

                            print(key,' ',' '.join(attr[0]),' ',','.join(opt[1:len(opt)]))

                            break

                        else:

                            print("\n minimum a car and a pickup should be present in virtual garage to complete: ")





                            #code:
