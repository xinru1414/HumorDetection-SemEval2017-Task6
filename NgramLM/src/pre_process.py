import preprocessor as p
import sys, os

infile = sys.argv[1]
outfile = sys.argv[2]

def main():
	with open(outfile, 'w') as o:
		with open(infile, "r", encoding='UTF-8') as f:
			for line in f:
				o.write(line.lower())

if __name__ == '__main__':
    main()