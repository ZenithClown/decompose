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

<p align = "justify">Insulation failure is a severe threat to high voltage equipment, and its protection using a reliable and efficient diagnostic tool has always been the interest to power utilities. The modern power industry relies heavily on the transformer, which focuses on providing an interruption-free constant power factor, forcing the utilities to keep operating as much as possible, requiring a fault-free operation of transformers. Many traditional and newer techniques are available; however, due to the complex aging process of oil-paper insulation under the influence of different types of stresses, insulation condition assessment is generally performed by experts after carefully evaluating additional measurement data. The paper presents an approach to determine the dielectric dissipation factor of the power transformer insulation, considering transformer physical and operational parameters in addition to the recovery voltage measurement.</p>

## Keywords

<p align = "justify"><i>power transformer, dissipation factor, tan delta, return voltage, recovery voltage, central time constant, principal component analysis, regression, oil moisture, initial rate, machine learning, curve fitting</i></p>

## Figures

<p align = "center">
<img src = "./assets/figures/Figure 1 Two-Electrode Model for Capturing RV Data.jpeg" /><br>
Figure 1 Two-Electrode Model for Capturing RV Data<br><br>
<img src = "./assets/figures/Figure 2 Flowchart of RV Measurement using Two-Electrode Model.png" /><br>
Figure 2 Flowchart of RV Measurement using Two-Electrode Model<br><br>
<img src = "./assets/figures/Figure 3 RVM Spectrum of trf1.svg" /><br>
Figure 3 RVM Spectrum of trf1<br><br>
<img src = "./assets/figures/Figure 4 The Scree Plot representing the Percentage of Explained Variance of all the Individual Principal Components calculated from PCA considering all the Transformer Parameters.svg" /><br>
Figure 4 The Scree Plot representing the Percentage of Explained Variance of all the Individual Principal Components calculated from PCA considering all the Transformer Parameters<br><br>
<img src = "./assets/figures/Figure 5 First Principal Component (PC-1) vs tan 𝛿.svg" /><br>
Figure 5 First Principal Component (PC-1) vs tan 𝛿<br><br>
<img src = "./assets/figures/Figure 6 PC-1 against Dissipation Factor with Class Label based on User-Defined Boundaries.svg" /><br>
Figure 6 PC-1 against Dissipation Factor with Class Label based on User-Defined Boundaries<br><br>
<img src = "./assets/figures/Figure 7 Proposed Curve to Estimate tan 𝛿 w.r.t. PC-1.svg" /><br>
Figure 7 Proposed Curve to Estimate tan 𝛿 w.r.t. PC-1<br><br>
<img src = "./assets/figures/Figure 8 Final Proposed Polynomial Equation to Determine tan 𝛿 considering an Error Band of 0.25 𝜎^2.svg" /><br>
Figure 8 Final Proposed Polynomial Equation to Determine tan 𝛿 considering an Error Band of 0.25 𝜎^2<br><br>
</p>

## License

This is licensed to &copy; Debmalya Pramanik, Arijit Baral [MIT License](LICENSE)

## Credits & Reference

<p align = "justify">Principal Component Analysis (PCA) tries to find the axes with the maximum variance <a href = "https://sebastianraschka.com/Articles/2014_pca_step_by_step.html">[1]</a>. The <code>decomposition.PCA()</code> function is written using the mathematical formulation and step-by-step guide provided by Sebastian Raschka.</p>

[1] Raschka, S. (2015). _Python Machine Learning_. Packt Publishing Ltd.

## Additional Notes

<p align = "justify">Paper is still under review and modifications, thus the content may change significantly.</p>
