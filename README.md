# PTUSTR: Prune Tree to User-Specified Taxonomic Rank
A Python script to prune a phylogenetic tree to a user-specified taxonomic rank

## Background
Phylogenetic trees are diagramatic representations of evolutionary history that consist of nested 'clades'. In the following example, species A and B would form a clade. Likewise, species A, B and C would form a clade together.
```
   ________ species C
  |
__|   _____ species A
  |__|
     |_____ species B
```
In practical phylogenetic research, one often needs to prune specific clades from a tree to make it easier to handle. For example, species A and B may belong to the same genus (i.e., genus X; for taxonomic hierarchies, see below), whereas species C may belong to another genus (i.e., genus Y). Hence, one could "prune" the tree such that only the genera are displayed:
```
   __ genus Y
  |
__|
  |__ genus X
```
Multiple software tools have been developed to achieve such a pruning operation. The most versatile such tool is [treesliceR](https://github.com/AraujoMat/treesliceR). treesliceR does its job pretty well, but it lacks one critical function: to slice/prune a given phylogenetic tree at a specific taxonomic rank, assuming that the tips of the tree are labelled by full species names. This is what we wish to achieve through a simple Python script.

Taxonomic ranks are a set of nested hierarchies, with the highest rank being the "domain" and the lowest rank typically the "species" ([https://en.wikipedia.org/wiki/Taxonomic_rank](https://en.wikipedia.org/wiki/Taxonomic_rank)). The [NCBI Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi) let's you click your way through the taxonomic ranks. The full set of taxonomic ranks for humans as per [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=9606) would be: 
```
Eukaryota; (the rank "domain")
  Opisthokonta;
    Metazoa;
      Eumetazoa;
        Bilateria;
          Deuterostomia;
            Chordata;
              Craniata;
                Vertebrata;
                  Gnathostomata;
                    Teleostomi;
                      Euteleostomi;
                        Sarcopterygii;
                          Dipnotetrapodomorpha;
                            Tetrapoda;
                              Amniota;
                                Mammalia;
                                  Theria;
                                    Eutheria;
                                      Boreoeutheria;
                                        Euarchontoglires;
                                          Primates;
                                            Haplorrhini;
                                              Simiiformes;
                                                Catarrhini;
                                                  Hominoidea;
                                                    Hominidae; (the rank "family")
                                                      Homininae; (the rank "subfamily")
                                                        Homo;  (the rank "genus")
                                                          Homo sapiens (the rank "species")
```
We want to implement this script in Python because the individual functions to achieve a taxonomy-driven pruning operation on a given phylogenetic tree are already existent in a famous Python library: the [ETE Toolkit](https://github.com/etetoolkit/ete). We merely need to take the relevant functions from ETE and combine them to achieve a script that prunes a user-provided phylogenetic tree at a user-specified taxonomic rank.

The functions or modules we wish to use from ETE are:
- [ncbi_taxonomy](http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html): This module has the relevant functions to query NCBI Taxonomy to find out which species belongs to which genus, which genus belongs to which subfamily, which subfamily belongs to which family, etc. (see the taxonomic hierarchiy from the bottom up!).
  - **IMPORTANT:** We hereby wish to use several functions of the Python project [TaxonKit](https://github.com/shenwei356/taxonkit), which has solved many issues for us already.
- [Advanced traversing a tree](http://etetoolkit.org/docs/latest/tutorial/tutorial_trees.html#advanced-traversing-stopping-criteria): These are base functions of ETE and will allow us to "prune" (or rather **"collapse"**, to use ETE's terminology) the terminal branches of a given tree to higher taxonomic ranks.

## Objective
To generate a Python script that accepts the name of a NEWICK-formatted tree file and the name of a taxonomic hierarchy as input, traverses through the tree starting from the tips, and collapses each clade to the taxonomic rank desired. The script the writes this reduced tree with new tip labels to file.

## Implementation and Testing

- Example usage
```
python ptustr.py -i ./data/FelixForest_Zenodo_Angiosperms_100trees_firstTree_modified.tre -t family
```

- **Source of full phylogenetic tree (i.e., maximum text case)**
The full phylogenetic tree that is co-supplied with the package is the first tree of the tree set presented here: [https://zenodo.org/records/7600341}(https://zenodo.org/records/7600341). With a total of 79,874 terminals, it is one of the largest phylogenetic trees for seed plants inferred today and represents the maximum size of phylogenetic tree that this script needs to be able to handle.
  
- **Testing to traverse through the tree without the need to interact with NCBI Taxonomy**
In order to test only the functionality of traversing through the tree and collapsing specific clades without having to interact with NCBI Taxonomy yet, we can use the list 'spp_fam_ord.csv' of [https://zenodo.org/records/7600341](https://zenodo.org/records/7600341) to receive the order and the family name for each possible species name among all land plants known. The list provides the information which plant order and which plant family a plant species belongs to.


## Additional considerations
- The new tip labels should be the correct taxonomic name for the organism group at that taxonomic hierarchy. For example, if a clade of humans, chimps, gorillas, and orangutans are collapsed to the subfamily level, the terminal branch should be labelled "Homininae".
- Since there may be duplications in tip labels after the pruning (i.e., when polyphyletic relationships are present), then the tip labels are made unique by adding integers to their labels (e.g., "Homininae_1", "Homininae_2", etc.).
- For the taxonomy of plants, the database 'World Checklist of Vascular Plants' may be better suited than NCBI Taxonomy. WCVP is available via FTP and may even have an API at the time of this writing. See [https://www.nature.com/articles/s41597-021-00997-6](https://www.nature.com/articles/s41597-021-00997-6) for more details.
