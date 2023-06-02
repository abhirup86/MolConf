with open('crest_conformers.xyz', 'r') as input_file:
    line_counter = 0
    file_counter = 1

    # Open the first output file
    with open(f'crest_conformers_{file_counter}.xyz', 'w') as output_file:

        # Iterate over the lines in the input file
        for line in input_file:
            # Write the line to the output file
            output_file.write(line)
            
            # Increment the line counter
            line_counter += 1
            if line_counter == 2:
              print(f'conformer: {file_counter} \t energy:{line}')
            # If the line counter is 55, reset it and increment the file counter
            if line_counter == 55:
              
                
                line_counter = 0                
                file_counter += 1

                # Close the current output file and open a new one
                output_file.close()
                output_file = open(f'crest_conformers_{file_counter}.xyz', 'w')
