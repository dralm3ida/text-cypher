import logging, argparse, getpass

logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)

printable_ascii_list = list(map(chr, range(32, 127)))
ascii_len = len(printable_ascii_list)

def validate_input(label, input_value):
   has_all = any([char in input_value for char in printable_ascii_list])
   log.info("validate_input(): has_all='{}'".format(has_all))
   if has_all == False:
      raise Exception("Sorry, '{}' has invalid characters!".format(label))

def get_list_item_round_robin(list, index, length):
   return list[index % length]

def is_number_even(value):
   if ((value % 2) == 0):
      return True
   else:
      return False

def calculate_key_index(key_value):
   index = 0
   for c in key_value:
      if (is_number_even(index) == True):
         index += printable_ascii_list.index(c)
      else:
         index -= printable_ascii_list.index(c)

   return index


def encrypt(input_value, key_value):
   ''' Encrypt function '''

   secret_key = calculate_key_index(key_value)

   result = ""
   for i, v in enumerate(input_value):
      new_index = printable_ascii_list.index(v) + secret_key
      result += get_list_item_round_robin(printable_ascii_list, new_index, ascii_len)
   
   log.info("encrypt(): result='{}'".format(result))
   return result


def decrypt(input, key):
   ''' Decrypt function '''

def main():
   parser = argparse.ArgumentParser('Starting cypher ...')
   parser.add_argument('-m', dest='mode', type=str, help='Cypher mode option: can either be in encrypt(e) or decrypt(d) mode.')
   parser.add_argument('-k', dest='key', type=str, required=False, help=argparse.SUPPRESS)
   parser.add_argument('-i', dest='input', type=str, required=False, help=argparse.SUPPRESS)

   args = parser.parse_args()

   output = ''

   if not args.input:
      args.input = getpass.getpass('Cypher input: ')

   if not args.key: 
      args.key = getpass.getpass('Cypher key: ')

   log.info(args)

   validate_input("args.key", args.key)
   validate_input("args.input", args.input)

   if args.mode == 'e':
      output = encrypt(args.input, args.key)
   elif args.mode == 'd':
      output = decrypt(args.input, args.key)
   else:
      raise ValueError("Cypher mode: '{}' is not a valid one!".format(args.mode))

   log.info("Output: '{}'".format(output))


if __name__ == '__main__':
   main()



