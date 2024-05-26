#MAIN PROGRAM FILE for the Critical Care Helper App

#AUTHOR: Brian Ocque
#START DATE: 04/02/2024
#FINISH DATE: 04/24/2024

import critical_care_util

def main():
    print('=====================================================')
    print("v.1   CRITICAL CARE HELPER APPLICATION")
    print("***This app is not a suitable substitution***")
    print("***Double  Check    your    Math   Skills!***")
    print('=====================================================')
    

    while True:
        print("\nMenu:")
        print("1. Weight Converter")
        print("2. Tidal Volume Calculator")
        print("3. Normal Metabolic Panel Values")
        print("4. Rapid Sequence Intubation (RSI) Procedure")
        print("5. Medication Calculator")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            critical_care_util.weight_converter()
        elif choice == '2':
            critical_care_util.tidal_volume_calculator()
        elif choice == '3':
            critical_care_util.show_normal_values()
        elif choice == '4':
            critical_care_util.rsi_procedure()
        elif choice == '5':
            critical_care_util.med_calc()
        elif choice == '6':
            print('================================================================')
            print("BE SURE TO CONSULT MED CONTROL IF UNSURE OF ANYTHING! Good Luck!")
            print('================================================================')
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":


    main()