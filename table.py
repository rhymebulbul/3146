from prettytable import PrettyTable

def parse_light():
    """
    Opens the CSV file containing light data
    reads row by row & adds to a html file in table format
    """
    csv_light = open("light_data.csv")
    light = csv_light.readlines()
    # Open CSV file
    lrow = light[0]
    lrow = lrow.split(',')
    # Splits the header by each value
    x = PrettyTable([lrow[0], lrow[1], lrow[2]])
    for a in range(1, len(light), 2):
        lrow = light[a]
        lrow = lrow.split(',')
        x.add_row([lrow[0], lrow[1], lrow[2]])
    # Adds each row in the CSV file to table in HTML format
    light_code = x.get_html_string()
    html_light = open('resources\light.html', 'w')
    html_light.write(light_code)
    # Writes the HTML table to a html file
def parse_temp():
    """
    Opens the CSV file containing temperature data
    reads row by row & adds to a html file in table format
    """
    csv_tempe = open("tempe_data.csv")
    tempe = csv_tempe.readlines()
    # Open CSV file
    trow = tempe[0]
    trow = trow.split(',')
    # Splits the header by each value
    y = PrettyTable([trow[0], trow[1], trow[2]])
    for a in range(1, len(tempe), 2):
        trow = tempe[a]
        trow = trow.split(',')
        y.add_row([trow[0], trow[1], trow[2]])
    # Adds each row in the CSV file to table in HTML format
    tempe_code = y.get_html_string()
    html_tempe = open('resources\\tempe.html', 'w')
    html_tempe.write(tempe_code)
    # Writes the HTML table to a html file
def main():
    """
    Uses the prettyTable module to parse the CSV values into a HTML table
    """
    print('Parsing CSV data to Table...')
    parse_light()
    #parses light data
    parse_temp()
    #parses temperature datass
    print('CSV data parsed to Table!')

if __name__ == "__main__":
    main()