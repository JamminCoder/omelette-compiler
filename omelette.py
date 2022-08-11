class Omelette:
    def encode(text):
        output = ""

        for c in text:
            nums = str(ord(c))
            for num in nums:
                num = int(num) + 1
                output += "omelette" * num
                output += " "
            output += " "
        
        return output


    def decode(text):
        output = ""
        omlette_chunks = text.split("  ")
        for omlettes in omlette_chunks:
            omlette_bits = omlettes.split(" ")
            ascii_str = ""

            for omlette in omlette_bits:
                if omlette == "omelette":
                    ascii_str += "0"
                    continue 

                char_seg = len(omlette.split("omelette")) - 2
                if char_seg < 0:
                    char_seg = 0
                
                ascii_str += str(char_seg)

            output += chr(int(ascii_str))

        return output


    def write_omelette_file(path, text):
        with open(path, "w") as f:
            f.write(Omelette.encode(text))

    def read_omelette_file(path):
        with open(path, "r") as f:
            return Omelette.decode(f.read())
