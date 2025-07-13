with open("Input/Names/invited_names.txt") as names_file:
    for line in names_file.readlines():
        recipient = line.strip()
        with open(f"./data/output/ready_to_send/letter_to_{recipient}.txt", "w") as new_letter:
            with open("data/input/letters/starting_letter.txt") as template:
                for temp_line in template.readlines():
                    new_letter.write(temp_line.replace("[name]", str(recipient)))
