# PTAUSTR: Slice Tree At User-Specified Taxonomic Rank
A Python script to prune a phylogenetic tree at a user-specified taxonomic rank

## Background
Phylogenetic trees are diagramatic representations of evolutionary history that consist of nested 'clades'. In pratical phylogenetic research, one often needs to prune specific clades from a tree to make it easier to handle. Multiple software tools have been developed to achieve such a pruning operation. The most versatile such tool is [treesliceR](https://github.com/AraujoMat/treesliceR). treesliceR does its job pretty well, but it lacks one critical function: to slice/prune a given phylogenetic tree at a specific taxonomic rank, assuming that the tips of the tree are labelled by full species names. This is what we wish to achieve through a simple Python script.

We want to implement this script in Python because the individual functions to achieve a taxonomy-driven pruning operation on a given phylogenetic tree are already existant in a famous Python library: the [ETE Toolkit](https://github.com/etetoolkit/ete).
