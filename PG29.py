input_file = "raw.txt"
output_file = "cleaned.txt"

try:
    with open(input_file, "r") as file:

        lines = file.readlines()

    cleaned_lines = []

    for line in lines:

        clean = " ".join(line.split())

        if clean:
            cleaned_lines.append(clean)

    with open(output_file, "w") as file:

        for line in cleaned_lines:
            file.write(line + "\n")

    print("File cleaned successfully!")
    print("Saved as:", output_file)

except FileNotFoundError:
    print("Input file not found")
