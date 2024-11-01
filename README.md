# PTAUSTR: Slice Tree At User-Specified Taxonomic Rank
A Python script to prune a phylogenetic tree at a user-specified taxonomic rank

## Background
Phylogenetic trees are diagramatic representations of evolutionary history that consist of nested 'clades'. In practical phylogenetic research, one often needs to prune specific clades from a tree to make it easier to handle. Multiple software tools have been developed to achieve such a pruning operation. The most versatile such tool is [treesliceR](https://github.com/AraujoMat/treesliceR). treesliceR does its job pretty well, but it lacks one critical function: to slice/prune a given phylogenetic tree at a specific taxonomic rank, assuming that the tips of the tree are labelled by full species names. This is what we wish to achieve through a simple Python script.

Taxonomic ranks are a set of nested hierarchies, with the highest rank being the "domain" and the lowest rank typically the "species" ([https://en.wikipedia.org/wiki/Taxonomic_rank](https://en.wikipedia.org/wiki/Taxonomic_rank)). The [NCBI Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi) let's you click your way through the taxonomic ranks. The full set of taxonomic ranks for humans as per [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=9606) would be: 
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
                                                      Homininae;
                                                        Homo;  (the rank "genus")
                                                          Homo sapiens (the rank "species")

We want to implement this script in Python because the individual functions to achieve a taxonomy-driven pruning operation on a given phylogenetic tree are already existant in a famous Python library: the [ETE Toolkit](https://github.com/etetoolkit/ete). We merely need to take the relevant functions from ETE and combine them to achieve a script that prunes a user-provided phylogenetic tree at a user-specified taxonomic rank.
