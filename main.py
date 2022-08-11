from omelette import Omelette


text = """
This text is to be compiled into omelette!!
"""
output_file = "test.oml"

Omelette.write_omelette_file(output_file, text)
print(Omelette.read_omelette_file(output_file))