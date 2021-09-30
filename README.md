# Texminology_extraction_base
This repository contains the literature, dataset, and codes I collected on the topic of terminology extraction
The literature includes some traditional methods for term extraction, such as C-score, Text rank.

# Basic code 1
The basement codes has two parts.
One is using the so called emantic relatedness, which is based on calculation of vector semantics.It could be found in branch master.
This is extracted from the codes used in the paper "SemRe-Rank: Improving Automatic Term Extraction By Incorporating
Semantic Relatedness With Personalised PageRank"

The other is using the pattern matching method. It could be found in branch master2.
The idea is to use the POS taggings as the pattern to match the qualified terms.
The pattern match algorithm, KMP algorithm is used. 
