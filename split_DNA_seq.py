import Primerselectiontools_py3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--sequence', help='text file containing DNA sequence', required=True)
parser.add_argument('-m', '--oligosizemax', type=int, help='maximum size of oligos', default=300)
parser.add_argument('-l', '--lengthleeway', type=int, help='leeway in length of oligos', default=15)
parser.add_argument('-p', '--positionleeway', type=int, help='leeway in position of oligos', default=15)
parser.add_argument('-a', '--avgoverlapsize', type=int, help='average overlap size of oligos', default=20)
parser.add_argument('-t', '--overlaptemps', type=int, help='temperatures for overlap', nargs=2, default=[58,62])
parser.add_argument('-d', '--deltaGThreshold', type=int, help='deltaG threshold for overlap', default=-4)
parser.add_argument('-e', '--selfDimersThreshold', type=int, help='self dimers threshold for overlap', default=4)
parser.add_argument('-n', '--num_of_oligos', type=int, help='number of oligos', required=True)
parser.add_argument('-o', '--output', help='output file name', required=True)

args = parser.parse_args()

with open(args.sequence, 'r') as f:
    seq = f.read()

seq = seq.upper()
asm_fwd = "ATCGGGGATGGTAACTAACG"
asm_rev = "ACCAACGGACAATCAGCTAT"
seq = asm_fwd + seq + asm_rev

oligos = Primerselectiontools_py3.optimizedSplit(seq=seq, oligosizemax=args.oligosizemax, lengthleeway=args.lengthleeway,
                                                 positionleeway=args.positionleeway, avgoverlapsize=args.avgoverlapsize,
                                                 overlaptemps=args.overlaptemps, deltaGThreshold=args.deltaGThreshold,
                                                 selfDimersThreshold=args.selfDimersThreshold, num_of_oligos=args.num_of_oligos)
print(oligos)