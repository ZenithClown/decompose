<h1 align = "center">
  decompose<img src = "./assets/LogoMakr-6pNJd4.png" height = "108" width = "200" align = "right" /><br>
  <sup>(supplement code)</sup><br>
  <table align = "center">
    <!-- using TAB-SPACE = 2 - as long lines present -->
    <thead>
      <tr>
        <th><sub>Debmalya Pramanik</sub></th>
        <th><sub>Dr. Arijit Baral</sub></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <a href = "https://www.linkedin.com/in/dpramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/linkedin.svg"/></a>
          <a href = "https://github.com/ZenithClown"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/github.svg"/></a>
          <a href = "https://gitlab.com/ZenithClown/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/gitlab.svg"/></a>
          <a href = "https://www.researchgate.net/profile/Debmalya_Pramanik2"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/researchgate.svg"/></a>
          <a href = "https://www.kaggle.com/dPramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/kaggle.svg"/></a>
          <a href = "https://app.pluralsight.com/profile/Debmalya-Pramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/pluralsight.svg"/></a>
          <a href = "https://stackoverflow.com/users/6623589/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/stackoverflow.svg"/></a>
          <a href = "https://scholar.google.com/citations?user=GPHPApYAAAAJ&hl=en"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/googlescholar.svg"/></a>
        </td>
        <td>
          <a href = "https://www.linkedin.com/in/arijit-baral-2a2b4819/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/linkedin.svg"/></a>
          <a href = "https://scholar.google.com/citations?user=PYdjFe8AAAAJ&hl=en"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/googlescholar.svg"/></a>
        </td>
      </tr>
    </tbody>
  </table>
</h1>

<p align = "justify">A implementation of <i>Principal Component Analysis (PCA)</i> Algorithm for determining the Functional Age of Power Transformer, for the Paper Titled "<i>Reliable Estimation of Dissipation Factor of In-service Power Transformer</i>", by Debmalya Pramanik (<a href = "https://orcid.org/0000-0002-3955-8170">ORCiD:0000-0002-3955-8170</a>) and Dr. Arijit Baral (<a href = "https://orcid.org/0000-0002-1905-9059">ORCiD:0000-0002-1905-9059</a>).</p>

## Abstract

<p align = "justify">Insulation failure is a severe threat to high voltage equipment, and its protection using a reliable and efficient diagnostic tool has always been the interest to power utilities. Many traditional and newer techniques are available. Due to the complex aging process of oil-paper insulation, experts generally perform assessments after carefully evaluating measurement data. The paper presents a methodology to analyze recovery voltage measurement data to estimate aging sensitive performance parameters (dissipation factor).</p>

### Keywords

<p align = "justify"><i>power transformer, dissipation factor, tan delta, return voltage, recovery voltage, central time constant, principal component analysis, regression, oil moisture, initial rate, machine learning, curve fitting</i></p>

<div align = "center">

[![IEEE Conference Paper Link](https://img.shields.io/badge/📃-IEEE_Conference_Paper_Link-blue)](https://ieeexplore.ieee.org/document/9972517)

</div>

## Figures

<p align = "justify">Significant figures related to the paper is added here for reference. Images files are available <a href = "./assets/figures/">here</a>, and the overall flowchart of the proposed algorithm and PCA is created using <a href = "https://draw.io/">draw.io</a> founded by <i>Gaudenz Alder</i>.</p>

<div align = "center">

<table>
  <thead>
    <tr colspan = 3><b><i>Significant Figures from Conference Paper</i></b></tr>
  </thead>
  <tbody>
    <tr>
      <td><img src = "./assets/figures/Figure 3 RVM Spectrum of trf1.svg" width = 512/></td>
      <td></td>
      <td><img src = "./assets/figures/Figure 4 The Scree Plot representing the Percentage of Explained Variance of all the Individual Principal Components calculated from PCA considering all the Transformer Parameters.svg" width = 512/></td>
    </tr>
    <tr>
      <td><p align = "center"><b>Fig.:</b> RVM Spectrum of <i>trf1</i></p></td>
      <td></td>
      <td><p align = "center"><b>Fig.:</b> The <i>Scree Plot</i> to determine Optimal Components</p></td>
    </tr>
    <tr>
      <td>image</td>
      <td></td>
      <td>image</td>
    </tr>
    <tr>
      <td><p align = "center"><b>Fig.:</b> </p></td>
      <td></td>
      <td><p align = "center"><b>Fig.:</b> </p></td>
    </tr>
    <tr>
      <td>image</td>
      <td></td>
      <td>image</td>
    </tr>
    <tr>
      <td><p align = "center"><b>Fig.:</b> </p></td>
      <td></td>
      <td><p align = "center"><b>Fig.:</b> </p></td>
    </tr>
    <tr>
      <td>image</td>
      <td></td>
      <td>image</td>
    </tr>
    <tr>
      <td><p align = "center"><b>Fig.:</b> </p></td>
      <td></td>
      <td><p align = "center"><b>Fig.:</b> </p></td>
    </tr>
    <tr>
      <td>image</td>
      <td></td>
      <td>image</td>
    </tr>
    <tr>
      <td><p align = "center"><b>Fig.:</b> </p></td>
      <td></td>
      <td><p align = "center"><b>Fig.:</b> </p></td>
    </tr>
  </tbody>
</table>

</div>

<p align = "center">
  <img src = "./assets/figures/Figure 1 Two-Electrode Model for Capturing RV Data.jpeg" /><br>
  Figure 1 Two-Electrode Model for Capturing RV Data<br><br>
  <!-- <img src = "./assets/figures/Figure 2 Flowchart of RV Measurement using Two-Electrode Model.png" /><br>
  Figure 2 Flowchart of RV Measurement using Two-Electrode Model<br><br> -->
  <br>
  Figure 2 RVM Spectrum of trf1<br><br>
  <img src = "./assets/figures/Figure 4 The Scree Plot representing the Percentage of Explained Variance of all the Individual Principal Components calculated from PCA considering all the Transformer Parameters.svg" /><br>
  Figure 3 The Scree Plot representing the Percentage of Explained Variance of all the Individual Principal Components calculated from PCA considering all the Transformer Parameters<br><br>
  <img src = "./assets/figures/Figure 5 First Principal Component (PC-1) vs tan 𝛿.svg" /><br>
  Figure 4 First Principal Component (PC-1) vs tan 𝛿<br><br>
  <img src = "./assets/figures/Figure 6 PC-1 against Dissipation Factor with Class Label based on User-Defined Boundaries.svg" /><br>
  Figure 5 PC-1 against Dissipation Factor with Class Label based on User-Defined Boundaries<br><br>
  <img src = "./assets/figures/Figure 7 Proposed Curve to Estimate tan 𝛿 w.r.t. PC-1.svg" /><br>
  Figure 6 Proposed Curve to Estimate tan 𝛿 w.r.t. PC-1<br><br>
  <img src = "./assets/figures/Figure 8 Final Proposed Polynomial Equation to Determine tan 𝛿 considering an Error Band of 0.25 𝜎^2.svg" /><br>
  Figure 7 Final Proposed Polynomial Equation to Determine tan 𝛿 considering an Error Band of 0.25 𝜎^2<br><br>
</p>

## License & Citaitions

This is licensed to &copy; Debmalya Pramanik, Arijit Baral [MIT License](LICENSE). If you find this document useful, please *cite the original paper* as (or refer to [citation](./CITATION.cff) file):

### Paper/Plain Text Citations

```
D. Pramanik and A. Baral, "Reliable Estimation of Dissipation Factor of In-service Power Transformer," 2022 IEEE 2nd Mysore Sub Section International Conference (MysuruCon), Mysuru, India, 2022, pp. 1-6, doi: 10.1109/MysuruCon55714.2022.9972517.
```

### BibTex

```latex
@INPROCEEDINGS{9972517,
  author={Pramanik, Debmalya and Baral, Arijit},
  booktitle={2022 IEEE 2nd Mysore Sub Section International Conference (MysuruCon)}, 
  title={Reliable Estimation of Dissipation Factor of In-service Power Transformer}, 
  year={2022},
  volume={},
  number={},
  pages={1-6},
  keywords={Voltage measurement;Fitting;Estimation;High-voltage techniques;Aging;Oil insulation;Reliability;power transformer;dissipation factor;tan delta;return voltage;recovery voltage;central time constant;principal component analysis;regression;oil moisture;initial rate;machine learning;curve fitting},
  doi={10.1109/MysuruCon55714.2022.9972517}}
```

## Credits & Reference

<p align = "justify">Principal Component Analysis (PCA) tries to find the axes with the maximum variance <a href = "https://sebastianraschka.com/Articles/2014_pca_step_by_step.html">[1]</a>. The <code>decomposition.PCA()</code> function is written using the mathematical formulation and step-by-step guide provided by Sebastian Raschka.</p>

[1] Raschka, S. (2015). _Python Machine Learning_. Packt Publishing Ltd.

## Additional Notes

<p align = "justify">Paper is still under review and modifications, thus the content may change significantly.</p>
