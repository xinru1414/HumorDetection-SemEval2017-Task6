import preprocessor as p
import sys, os
import re

infile = sys.argv[1]
outfile = sys.argv[2]

def main():
	with open(infile, "r", encoding='UTF-8') as f:
		lines = f.readlines()
	with open(outfile, 'w') as o:
		for line in lines:
			s = re.sub('(?<! )(?=[.,!?()])|(?<=[.,!?()])(?! )', r' ', line)
			o.write(s)

if __name__ == '__main__':
    main()