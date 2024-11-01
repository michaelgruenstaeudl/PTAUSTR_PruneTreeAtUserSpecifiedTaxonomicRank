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
#from Bio import SeqIO, Nexus, SeqRecord, AlignIO
import ete3
import logging

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

def setup_logger(user_params: UserParameters) -> logging.Logger:
    logger = logging.getLogger(__name__)
    log_format = "%(asctime)s [%(levelname)s] %(message)s"
    log_level = logging.DEBUG if user_params.verbose else logging.INFO
    coloredlogs.install(fmt=log_format, level=log_level, logger=logger)
    logger.debug(f"{parser.prog} {__version__}")
    return logger


def main(user_params: UserParameters):
    
    logger.info(f"Reading input tree(s)")
    tree_collection = []
    for tree in open(user_params.infile):
        tree_collection.append(ete3.Tree(tree))
  
    # do the pruning
    
    logger.info(f"Writing input tree")
    outtree = tree_collection[0]
    outtree.write(outfile=user_params.outfile)

    log.info("end of script\n")
    quit()

# ------------------------------------------------------------------------------#
# ARGPARSE
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Purpose of this script: " + __title__)

    # Required
    parser.add_argument(
        "--infile",
        "-i",
        type=str,
        required=True,
        help="path and name of input file",
        default="~/intree.tre",
    )
    parser.add_argument(
        "--taxlevel",
        "-t",
        type=str,
        required=True,
        help="taxonomic level",
        default="family",
    )

    # Optional
    parser.add_argument(
        "--outfile",
        "-o",
        type=str,
        required=False,
        help="(Optional) path and name of input file",
        default="~/outtree.tre",
    )

    params = UserParameters(parser)
    log = setup_logger(params)
    main(params)
# ------------------------------------------------------------------------------#
# EOF
# ------------------------------------------------------------------------------#
