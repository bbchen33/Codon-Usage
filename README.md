# Codon-Usage (Molecular biology)
This is a function for calculating the codon usage of an organism by entering a set of gene sequences without any space in between.
It is recommended that using 10+ genes will result in a more accurate calculation.

Although it might say warning (see below), you will still be able to get the result.


Warning (from warnings module):
  File "getCodonUsage.py", line 40
    CodonAndNumber_df[3][i] = 100*CodonAndNumber_df[1][i]/CodonAndNumber_df[2][i]
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy"

