import sys

factors = {'k': 1000.0, '': 1.0, 'c':0.01, 'm':0.001}    

def convert_unit(unit_in:str, unit_out:str, value:float):
    return value * factors[unit_in] / factors[unit_out]

clean_units = [sys.argv[1][:-1], sys.argv[2][:-1]]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Expected Usage : python convertor.py <input_unit> <output_unit> <input_value>")
    elif sys.argv[1][-1] != sys.argv[2][-1] and sys.argv[1][-1] != '':
        print("Invalid unit conversion")
        print("Expected Usage : python convertor.py <input_unit> <output_unit> <input_value>")
    else:
        result = convert_unit(clean_units[0], clean_units[1], float(sys.argv[3]))
        print(f"Result : {result} {sys.argv[2]}")