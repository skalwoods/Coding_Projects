#UTILITY FILE for the Critical Care Helper App
#NEEDS TO BE USED IN CONJUNCTION WITH THE critical_care_helper.py file

#AUTHOR: Brian Ocque
#START DATE: 04/02/2024
#FINISH DATE: 04/24/2024


import time
import sys
import os

def weight_converter():
    choice = input("Enter 'kg' to convert kilograms to pounds or 'lbs' to convert pounds to kilograms: ")
    if choice == 'kg':
        weight = float(input("Enter weight in kilograms: "))
        pounds = weight * 2.20462
        print()
        print()
        print(f"{weight} kilograms is equal to {pounds} pounds.")
    elif choice == 'lbs':
        weight = float(input("Enter weight in pounds: "))
        kilograms = weight / 2.20462
        print()
        print()
        print(f"{weight} pounds is equal to {kilograms} kilograms.")
    else:
        print("Invalid choice. Please enter 'kg' or 'lbs'.")

def tidal_volume_calculator():
    sex = input("Enter 'm' for male or 'f' for female: ")
    height = float(input("Enter height in inches: "))
    if sex == 'm':
        tidal_volume = (50 + 2.3 * (height - 60)) * 6
    elif sex == 'f':
        tidal_volume = (45.5 + 2.3 * (height - 60)) * 6
    else:
        print("Invalid input for sex. Please enter 'm' or 'f'.")
        return
    print()
    print()
    print(f"The tidal volume is {tidal_volume} cc's.")

def show_normal_values():
    normal_values = {
        "Albumin": "3.5-5.0 g/dL",
        "Alkaline phosphatase": "30-125 units/L",
        "ALT": "0-40 units/L",
        "AST": "3-44 units/L",
        "Bilirubin": "0.2-1.3 mg/dL",
        "Blood urea nitrogen (BUN)": "8-21 mg/dL",
        "Calcium": "8.7-10.7 mg/dL",
        "CO2": "22-29 mmol/L",
        "Chloride": "99-108 mmol/L",
        "Creatinine": "0.75-1.20 mg/dL (male); 0.65-1.00 mg/dL (female)",
        "Glucose": "fasting 60-99 mg/dL; nonfasting 60-200 mg/dL",
        "Potassium": "3.4-5.3 mmol/L",
        "Protein (total)": "6.0-8.2 g/dL"
    }
    print()
    print("Normal Metabolic Panel Values:")
    for key, value in normal_values.items():
        print(f"{key}: {value}")

def rsi_procedure():
    steps = [
        "1. ***Identify a clear need for intubation***",
        "2. Pre-Oxygenate the patient - highflow by NRB, CPAP, BVM",
        "3. Prepare your equipment - ET Tube, Handle, ET Capno, Tube Holder, 10cc syringe x2, bougie, stylet, iGel, Crich Kit, Suction that is working and running",
        "4. Check Saturations and Ensure 95-100% Saturation",
        "5. ***Reconfirm with crew your tasks and the plan for Failed Airway***",
        "6. Pass induction agent",
        "7. Pass Paralytic",
        "8. Pass Tube, confirm tube, secure tube."
    ]

    print("\nRapid Sequence Intubation (RSI) Procedure:")

    print("RSI procedure completed. ENSURE WAVEFORM CAPNOGRAPHY AND DIGITAL READING")

def rsi_procedure():
    #this section is timed purposely to simulate the necessary time to prepare the actual procedure IRL
    print("\nRapid Sequence Intubation (RSI) Procedure:")
    print("1. Identify a clear need for intubation")
    time.sleep(10)
    print("2. Pre-Oxygenate the patient - highflow by NRB, CPAP, BVM")
    time.sleep(60)
    print("3. Prepare your equipment - ET Tube, Handle, ET Capno, Tube Holder, 10cc syringe x2, bougie, stylet, iGel, Crich Kit, Suction that is working and running")
    time.sleep(60)
    print("4. Check Saturations and Ensure 95-100 Saturation")
    time.sleep(10)
    print("5. Reconfirm with crew your tasks and the plan for Failed Airway")
    time.sleep(60)
    print("6. Pass induction agent")
    time.sleep(15)
    print("7. Pass Paralytic")
    time.sleep(15)
    print("8. Pass Tube, confirm tube, secure tube.")
    print("RSI procedure completed.")

def med_calc():
    weight = float(input('What is the weight in KILOS rounded to the nearest kilo?'))
    print()
    rocuronium = weight * 1
    print('ROCURONIUM:', rocuronium, "mg")
    print()
    sux = weight * 1.5
    print('SUCCINYLCHOLINE:', sux, "mg")
    print()
    etomidate = weight * 0.3
    print("ETOMIDATE:", etomidate, "mg")
    print()
    ketamine = weight * 2
    print("KETAMINE:", ketamine, "mg")