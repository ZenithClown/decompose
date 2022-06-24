PCA Algorithm
=============

A feature or dimension is a measurable property of an object. Considering
*d*-features (where `d ≥ 4`), visualization and analysis of the data are tiresome,
and the complexity increases as the data correlation decrease. To overcome this,
Hotelling formulated PCA, which explains how d-features (x1,x2,…,xd) can be used
to identify *k*-parameters (where `k < d`) that can explain the original data. In
other words, PCA projects the entire set of data into a different subspace.
Calculation of PCA involves finding the eigenvectors (`e1,e2,…,ed`) and corresponding
eigenvalues (`𝜆1,𝜆2,…,𝜆𝑑`) of each data dimension individually, and then finding
k-eigenvectors with the largest eigenvalues. These *k*-vectors are used to create `dxk`
dimensional matrix that “transforms” the sample onto the new subspace.
Rashcka and Bartholomew also studied PCA to find the correlation coefficients.
VanderPlas discussed the process of selecting an optimal number of components (k)
that is needed to describe the data with the help of a scree plot.
