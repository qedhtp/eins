import argparse
def main():
    parser = argparse.ArgumentParser(description='this is a test')

    parser.add_argument('-i', '--input',help='the input path', required='True')
    parser.add_argument('-o', '--output',help='the output path', required='True')
    parser.add_argument('-l', '--length', action='store_true', help='whether display length')

    args = parser.parse_args()

    read_input_file(args.input)

    display_length = args.length
    process_output(display_length)

    
    
url_dict = {}

def read_input_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        url, number_str = line.strip().rsplit('[', 1)
        number = int(number_str[:-1])

        if number not in url_dict:
            url_dict[number] = url

def process_output(display1):

    with open('output.txt', 'w') as output_file:
        for number, url in url_dict.items():
            
            if display1:
                print(f'{url} [{number}]')
                output_file.write(f'{url} [{number}]\n')
            else:
                print(f'{url}')
                output_file.write(f'{url}\n')
            
if __name__ == '__main__':
    main()