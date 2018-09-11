import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input",
                    help="Input Midi File")
parser.add_argument("-o", "--output",
                    help="Output Midi File")
args = parser.parse_args()
print(args.input)
print(args.output)

if args.input != None:
    print("input: {} output: equals {}".format(args.input, args.output))
else:
    pass
