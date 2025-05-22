def process_file(input_filename, output_filename, omit_phrases):
    try:
        # Open and read the input file
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        # Process the lines
        processed_list = []
        for line in lines:
            stripped_line = line.strip()  # Remove whitespace and unprintable characters
            if stripped_line.isdigit() or not stripped_line:  # Skip numbers and empty lines
                continue
            
            # Skip lines containing any phrase from omit_phrases
            if any(phrase in stripped_line for phrase in omit_phrases):
                continue
            
            processed_list.append(stripped_line)  # Add valid strings to the list
        
        # Write the processed list to the output file
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(str(processed_list))
        
        print(f"Processed list written to '{output_filename}'")
    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
omit_phrases = ['', 'IP Address']  # Add phrases you want to omit
process_file('input.txt', 'output.txt', omit_phrases)
