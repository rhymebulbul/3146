import table
import sampler

"""
This file contains the main method.
It runs the sampler first
And runs the table 
Then starts the server
"""

def main():
    sampler.main()
    # Starts sampling till threshold reached
    table.main()
    # Parses CSV data values into HTML table
    import serve
    # Starts server & keeps running infinitely

if __name__ == "__main__":
    main()
