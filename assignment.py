def modify_file_content(content):
    return content.upper()

def main():
    try:
        input_filename = input("Enter the name of the file to read: ")
        
        with open(input_filename, 'r') as infile:
            content = infile.read()

        modified_content = modify_file_content(content)
        
        output_filename = input("Enter the name of the file to write the modified content to: ")
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written.")

if __name__ == "__main__":
    main()