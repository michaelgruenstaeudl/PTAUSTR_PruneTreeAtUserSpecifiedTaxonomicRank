#!/usr/bin/env python3
""" A Python script to prune a phylogenetic tree to a user-specified 
taxonomic rank """
__title__ = "A Python script to prune a phylogenetic tree to a \
user-specified taxonomic rank"
__version__ = "some version information"

# ---------------------------------------------------------------------#
# IMPORTS
# ---------------------------------------------------------------------#
import argparse
import coloredlogs
#from Bio import SeqIO, Nexus, SeqRecord, AlignIO
import ete3
import logging
import os

# ---------------------------------------------------------------------#
# DEBUGGING HELP
# import ipdb
# ipdb.set_trace()
# ---------------------------------------------------------------------#


# ---------------------------------------------------------------------#
# CLASSES AND FUNCTIONS
# ---------------------------------------------------------------------#


# ---------------------------------------------------------------------#
# MAIN
# ---------------------------------------------------------------------#

def setup_logger(user_args):
    logger = logging.getLogger(__name__)
    log_format = "%(asctime)s [%(levelname)s] %(message)s"
    log_level = logging.DEBUG if user_args.verbose else logging.INFO
    coloredlogs.install(fmt=log_format, level=log_level, logger=logger)
    logger.debug(f"{parser.prog} {__version__}")
    return logger


def main(user_args):
    
    log.info(f"Reading input tree(s)")
    tree_collection = []
    for tree in open(user_args.infile):
        tree_collection.append(ete3.Tree(tree))
  
    # do the pruning
    print("Do the pruning operations here")
    
    log.info(f"Writing input tree")
    outFn = os.path.dirname(os.path.abspath(user_args.infile))+"/"+user_args.outfile
    outtree = tree_collection[0]
    outtree.write(outfile=outFn)

    log.info("end of script\n")
    quit()

# ---------------------------------------------------------------------#
# ARGPARSE
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Purpose of this script: " + __title__)

    # Required
    parser.add_argument(
        "--infile",
        "-i",
        type=str,
        required=True,
        help="Path and name of input file",
        default="~/intree.tre",
    )
    parser.add_argument(
        "--taxlevel",
        "-t",
        type=str,
        required=True,
        help="Select a taxonomic level (e.g., 'family')",
        default="family",
    )

    # Optional
    parser.add_argument(
        "--outfile",
        "-o",
        type=str,
        required=False,
        help="(Optional) Name of output file",
        default="outtree.tre",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        required=False,
        help="(Optional) Enable verbose logging",
    )

    user_args = parser.parse_args()
    log = setup_logger(user_args)
    main(user_args)
# ---------------------------------------------------------------------#
# EOF
# ---------------------------------------------------------------------#
