import logging, argparse, getopt

logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)

printable_ascii = list(map(chr, range(32, 127)))


def help_message():
   ''' Help function '''

   print("##### Cypher Help #####")
   print(">> cypher -<flag option> <flag value>\n")
   print("+----------------------------------------------+")
   print("| Option | Description                         |")
   print("+----------------------------------------------+")
   print("|     -h | Displays this help message          |")
   print("|     -e | Encrypt mode                        |")
   print("|     -d | Decrypt mode                        |")
   print("|     -t | Input text to be encrypted          |")
   print("|     -f | Input file to be encrypted          |")
   print("|     -o | Output file to be encrypted         |")
   print("+----------------------------------------------+")


def encrypt():
   ''' Encrypt function '''

   log.info("encrypt(): printable_ascii = '{}'", printable_ascii)

def decrypt():
   ''' Decrypt function '''

def main():
   parser = argparse.ArgumentParser('Starting cypher ...')
   parser.add_argument('-h', type=str, help='help')

   args = parser.parse_args()

   inputtext = ''
   inputfile = ''
   outputfile = ''
   log.info(args)

   

if __name__ == '__main__':
   main()



