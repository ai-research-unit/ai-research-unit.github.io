# __Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses__

## Introduction

**The claim.** The electroweak sector breaks $SU(2)_L\times\mathrm{U}(1)_Y$ to $\mathrm{U}(1)_{\mathrm{em}}$ through one scalar doublet. The doublet's four real components become one massive scalar and three longitudinal polarisations, and the gauge bosons acquire the masses

$$
M_W=\frac{g\,v}{2},
\qquad
M_Z=\frac{\sqrt{g^2+g_{\mathrm Y}^2}\,v}{2},
\qquad
M_\gamma=0 ,
$$

with $v=246.22$ GeV. This article writes the mass matrix, diagonalises it, counts the degrees of freedom before and after, and evaluates the numbers against measurement.

**The standing.** The mechanism is standard theory, transcribed. The biquaternion framework supplies the *abelian* version of it as a construction, and §*What the Framework Supplies* states exactly how much of the non-abelian version it reaches, which is the group and not the representation. The article is the full working-out that [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html) names as its own gap, and it does not soften that gap.

**Three results that the single-particle articles do not state.**

- **The mass matrix and its trace.** In the basis $(W^1,W^2,W^3,B)$ the squared-mass matrix is one $4\times4$ object with three non-zero eigenvalues, and it obeys the trace sum rule $2M_W^2+M_Z^2=\tfrac{v^2}{4}(3g^2+g_{\mathrm Y}^2)$.
- **Why the photon is massless, structurally.** Not because of a tuning: the eigenvalue is zero because the generator $Q=T_3+Y$ annihilates the vacuum. The zero is a consequence of the alignment of the vacuum with the charge, and it is the only reason the electromagnetic group survives.
- **The numbers, from three independent sets of inputs.** From $g$, $g_{\mathrm Y}$ and $v$ at $M_Z$ the values are $80.24$ and $91.51$ GeV. From $\alpha$, $G_F$ and $M_Z$ the tree value of $M_W$ is $79.83$ GeV with $\alpha$ at the Z pole and $80.94$ GeV with $\alpha$ at zero momentum, against the measured $80.377$. The two brackets miss in opposite directions by about half a GeV, and $\delta r=0.0355$ reconciles them.

**The order.** What the doublet must do; the potential and its minimum; the covariant derivative at the vacuum; the mass matrix; its eigenvalues and the two structural zeros; the counting of degrees of freedom; the unitary gauge and the physical spectrum; the scalar's own mass and couplings; the numbers; the $\rho$ parameter and custodial symmetry; the equivalence theorem; and the framework's position.

## What the Doublet Must Do

**Three requirements, and one doublet satisfies all three.** A scalar sector that breaks the electroweak group is not free. It must satisfy three conditions, and each rules out something.

| Requirement | Why | What it excludes |
|---|---|---|
| The vacuum must not be invariant under $SU(2)_L$ | a symmetric vacuum gives no mass to $W^\pm$ | a singlet, which no group can break |
| The vacuum must be invariant under one abelian combination | the photon must stay massless | a vacuum charged under every combination |
| The vacuum must carry $T=\tfrac12$ content | $\rho=1$ at tree level | larger multiplets, which shift $\rho$ |

**The third requirement is the one usually left implicit.** A triplet can break the group and leave a massless photon, and it does so at the price of $\rho\neq1$. The doublet is the smallest multiplet meeting the first two conditions, and it happens to be the one that meets the third.

**The representation.** One complex doublet of hypercharge $\tfrac12$,

$$
\varphi=\begin{pmatrix}\varphi^+\\ \varphi^0\end{pmatrix},
\qquad
Y_\varphi=\tfrac12 ,
$$

which is four real fields. The hypercharge is not free here: it is fixed by the invariance of the Yukawa couplings, and [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html) derives it from $-Y_{L_L}+Y_\varphi+Y_{e_R}=0$, that is $Y_\varphi=Y_{L_L}-Y_{e_R}=+\tfrac12$.

**The same object in the companion articles.** [The W and Z Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html) writes this doublet as $\xi_{\mathrm{scl}}$ with components ${\xi_{\mathrm{scl}}}^\pm$ and ${\xi_{\mathrm{scl}}}^0$, and [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html) writes the abelian scalar as $\tilde\Xi=\xi\,e_t$. The three names denote the same object at three levels of generality, and this article uses $\varphi$ throughout.

**Why a doublet of complex fields is four real fields.** Each component is a complex number, so $2\times2=4$. The four are not independent in their charges: $\varphi^+$ and $\varphi^0$ each carry a real and an imaginary part, and the charges are $+1$ for both parts of $\varphi^+$ and $0$ for both parts of $\varphi^0$. The antiparticle of $\varphi^+$ is the field $\varphi^-=(\varphi^+)^*$, and it is not a fifth component.

## The Potential and Its Minimum

**The potential.** The most general potential invariant under the gauge group and renormalisable, given one doublet, is

$$
V(\varphi)=-\mu^2\,\varphi^{\dagger}\varphi+\lambda\left(\varphi^{\dagger}\varphi\right)^2 ,
\qquad
\lambda>0 ,
$$

with the two parameters of the table of article 1. Only $\varphi^\dagger\varphi$ can appear: any other invariant would need more than one power of the doublet in a way the group does not allow, and the audit of [The Standard Model Lagrangian Assembled](the-standard-model-lagrangian-assembled-four-sectors-in-one-expression.html) checks that.

**Why the sign of $\mu^2$ is written this way.** A positive $\mu^2$ makes the origin a maximum and pushes the minimum away from it. A negative $\mu^2$ would make the origin the minimum, the vacuum would be $\langle\varphi\rangle=0$, and the group would be unbroken. The sign is the difference between a theory with masses and a theory without.

**The minimum is a three-sphere.** The potential depends on $\varphi$ through one non-negative number, so it is invariant under the full $SU(2)$ acting on the doublet and under the hypercharge phase. Its minima form the surface

$$
\varphi^{\dagger}\varphi=\frac{v^2}{2},
\qquad
v^2=\frac{\mu^2}{\lambda} ,
$$

which in four real components is a three-sphere $S^3$ of radius $v/\sqrt2$. Every point of it is a minimum, and the theory must choose one.

**The choice is the breaking.** Take

$$
\langle\varphi\rangle=\frac{1}{\sqrt2}\begin{pmatrix}0\\ v\end{pmatrix},
\qquad
\langle\varphi^{\dagger}\varphi\rangle=\frac{v^2}{2} .
$$

The charged component is set to zero and the neutral one takes the whole value. That choice uses the $SU(2)$ freedom to rotate the doublet, and the phase freedom to make the lower component real. Neither is a loss of generality: the three-sphere is transitive under the group, so every minimum is equivalent to this one.

**What the vacuum is not invariant under.** The generator $T_3$ does not annihilate it, since $\sigma_3\binom{0}{1}=-\binom{0}{1}$; the hypercharge generator does not either, since $Y_\varphi=\tfrac12$. Their sum does:

$$
Q\,\langle\varphi\rangle=\left(T_3+Y\right)\frac{1}{\sqrt2}\begin{pmatrix}0\\ v\end{pmatrix}
=\left(-\tfrac12+\tfrac12\right)\langle\varphi\rangle=0 .
$$

That single line is the whole of the alignment: the charge operator annihilates the vacuum, so the electromagnetic group survives, and the three generators orthogonal to it do not, so the other three gauge directions acquire mass.

**The stationarity check.** The minimum conditions $\partial V/\partial\varphi=0$ give $-\mu^2+2\lambda\varphi^\dagger\varphi=0$, which at the minimum reads $\mu^2=\lambda v^2$. The potential energy at the minimum is $V_{\min}=-\mu^4/(4\lambda)=-\lambda v^4/4=-M_H^2v^2/8$, a negative constant. That constant is the cosmological constant problem in its original form: the model sets the zero of energy at the minimum and puts the vacuum at $-M_H^2v^2/8$, and nothing in it cancels the result against the observed dark-energy density. [Cosmology under the Biquaternion Framework — A Research Agenda](cosmology-under-the-biquaternion-framework-a-research-agenda.html) records the logical status of $\Lambda$ and why neither of its standard readings makes it a prediction; the constant plays no part in the masses.

**The shift.** Write the field as the vacuum plus an excitation,

$$
\varphi=\frac{1}{\sqrt2}\begin{pmatrix}0\\ v+h\end{pmatrix},
$$

with $h$ real. Substituting into the potential and expanding gives

$$
V=\frac{M_H^2}{2}h^2+\frac{M_H^2}{2v}h^3+\frac{M_H^2}{8v^2}h^4+\text{const},
\qquad
M_H^2=2\lambda v^2 ,
$$

so the quadratic term is the scalar mass and the two higher terms are the scalar's self-couplings. There is no linear term; the vanishing of the linear term is the stationarity condition, and it is the statement that the expansion is around a minimum and not around an arbitrary point.

**The three parameters are two.** The pair $(\mu^2,\lambda)$ and the pair $(v,M_H)$ carry the same information, through $v^2=\mu^2/\lambda$ and $M_H^2=2\lambda v^2$. The model's parameters are counted once, and the count is in article 1.

## The Covariant Derivative at the Vacuum

**The derivative.** With the normalisation of article 2,

$$
D_\mu\varphi=\frac{\partial\varphi}{\partial R_\mu}+i\,g\sum_a\tau_aW^a_\mu\varphi+i\,g_{\mathrm Y}Y_\varphi B_\mu\varphi ,
\qquad
\tau_a=\tfrac12\sigma_a ,
$$

and the mass term comes from the scalar kinetic term evaluated at the vacuum, where the derivative reduces to the connection alone.

**The four actions on the vacuum.** With $\varphi_0=\frac{1}{\sqrt2}\binom{0}{v}$ and $Y_\varphi=\tfrac12$,

$$
g\tau_1\varphi_0=\frac{g}{2}\varphi_0^{\uparrow},
\qquad
g\tau_2\varphi_0=\frac{i\,g}{2}\varphi_0^{\uparrow},
\qquad
g\tau_3\varphi_0=-\frac{g}{2}\varphi_0 ,
\qquad
g_{\mathrm Y}Y_\varphi\varphi_0=+\frac{g_{\mathrm Y}}{2}\varphi_0 ,
$$

where $\varphi_0^{\uparrow}=\frac{1}{\sqrt2}\binom{v}{0}$ is the same doublet with the entries exchanged. The first two produce the charged directions, and the last two produce the neutral one with opposite signs.

**The kinetic term at the vacuum.** The corpus's sign rule makes the term $-\sum_\mu(D_\mu\varphi)^\dagger(D_\mu\varphi)$, and at the vacuum the derivative carries no spacetime index of its own, so the term is a quadratic form in the four gauge fields,

$$
\mathcal{L}_{\mathrm{mass}}=-\frac{v^2}{8}\left[g^2\left(W^1_\mu\right)^2+g^2\left(W^2_\mu\right)^2+\left(gW^3_\mu-g_{\mathrm Y}B_\mu\right)^2\right] .
$$

**The third bracket is the whole mechanism in one expression.** The combination $gW^3-g_{\mathrm Y}B$ is not zero and not one of the original fields; it is a specific linear combination whose orthogonal partner, $g_{\mathrm Y}W^3+gB$, is absent. The absence is the masslessness of the photon, and the presence is the mass of the $Z$.

**Why the two charged directions carry the same coefficient.** The vacuum is neutral and the two charged directions are related by the residual $\mathrm{U}(1)_{\mathrm{em}}$, so their masses must be equal. The equality $M_{W^1}=M_{W^2}$ is not an accident of the arithmetic; it is the residual symmetry.

## The Mass Matrix

**The matrix.** Writing $\mathcal{L}_{\mathrm{mass}}=-\tfrac12\sum_{i,j}M^2_{ij}A_iA_j$ on the vector $A=(W^1,W^2,W^3,B)$,

$$
M^2=\frac{v^2}{4}
\begin{pmatrix}
g^2 & 0 & 0 & 0\\
0 & g^2 & 0 & 0\\
0 & 0 & g^2 & -g\,g_{\mathrm Y}\\
0 & 0 & -g\,g_{\mathrm Y} & g_{\mathrm Y}^2
\end{pmatrix} .
$$

The matrix is real, symmetric, and block diagonal: a $2\times2$ block proportional to the identity in the charged sector, and a $2\times2$ block in the neutral sector.

**The eigenvalues, in one line each.** The charged block gives

$$
M^2_{W^1}=M^2_{W^2}=\frac{g^2v^2}{4}=M_W^2 ,
$$

so the two real fields combine into $W^\pm=(W^1\mp iW^2)/\sqrt2$ of mass $M_W=gv/2$. The neutral block is a $2\times2$ matrix whose trace is $\tfrac{v^2}{4}(g^2+g_{\mathrm Y}^2)$ and whose determinant is zero, so its eigenvalues are $0$ and that trace:

$$
M^2_\gamma=0 ,
\qquad
M^2_Z=\frac{\left(g^2+g_{\mathrm Y}^2\right)v^2}{4} .
$$

**The determinant zero is structural and not numerical.** The determinant of the neutral block is $\left(\tfrac{v^2}{4}\right)^2\left[g^2g_{\mathrm Y}^2-\left(-gg_{\mathrm Y}\right)^2\right]=0$ identically, for every $g$, $g_{\mathrm Y}$ and $v$. The zero eigenvalue is not a fine-tuning of the parameters; it follows from the rank of the block, which in turn follows from the one-dimensionality of the direction along which $Q$ annihilates the vacuum.

**The eigenvectors.** The zero eigenvector is proportional to $(g_{\mathrm Y},g)$ in the $(W^3,B)$ basis, and the other to $(g,-g_{\mathrm Y})$. Normalising,

$$
A_\mu=\sin\theta_W\,W^3_\mu+\cos\theta_W\,B_\mu ,
\qquad
Z_\mu=\cos\theta_W\,W^3_\mu-\sin\theta_W\,B_\mu ,
\qquad
\tan\theta_W=\frac{g_{\mathrm Y}}{g} ,
$$

which is the mixing of [The W and Z Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html), now derived from the mass matrix rather than quoted. The angle is not an independent input: it is the angle that diagonalises the neutral block, and its value is $\arctan(g_{\mathrm Y}/g)$.

**The trace sum rule.** The trace of $M^2$ is invariant under the rotation, so

$$
2M_W^2+M_Z^2=\frac{v^2}{4}\left(3g^2+g_{\mathrm Y}^2\right).
$$

Checked against the numbers of §*The Numbers*, the left side is $21249$ GeV$^2$ and the right side $21249$ GeV$^2$ — equal because they are the same expression rearranged, so the check is one on the arithmetic and not on the physics. The load-bearing comparison is with the measured masses: $2(80.377)^2+(91.1876)^2=21236$ GeV$^2$, so the tree sum rule overshoots the measured sum by $13$ GeV$^2$, or $0.06$ per cent, which is the size of the correction that §*The Numbers* calls $\delta r$. The sum rule is exact at tree level and is the cheapest check on any computation of the two masses.

**The two masses in terms of one another.** With $\tan\theta_W=g_{\mathrm Y}/g$,

$$
M_Z=\frac{M_W}{\cos\theta_W} ,
\qquad
M_W=M_Z\cos\theta_W ,
$$

so the ratio of the two masses is the cosine of the mixing angle, and the measurement of both masses is a measurement of that angle. The identity is exact at tree level and receives corrections at one loop, which is why the on-shell angle $1-M_W^2/M_Z^2=0.22305$ and the $\overline{\mathrm{MS}}$ angle $0.23122$ are different numbers.

**The electromagnetic coupling.** The unbroken direction carries the coupling

$$
e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W=\frac{g\,g_{\mathrm Y}}{\sqrt{g^2+g_{\mathrm Y}^2}} ,
$$

which is the statement that the photon couples with the charge the two original couplings share after mixing. Numerically, with $g=0.6517$ and $g_{\mathrm Y}=0.3574$, $e=0.3134$ and $\alpha^{-1}=127.95$ at $M_Z$.

## The Counting of Degrees of Freedom

**The count before the breaking.** Count on-shell real degrees of freedom in four dimensions.

| Object | Count | Degrees of freedom |
|---|---|---|
| four gauge fields, massless | $4$ | $4\times2=8$ |
| scalar doublet, four real components | $4$ | $4$ |
| **total** | | $\mathbf{12}$ |

A massless vector has two transverse polarisations. A massless real scalar has one.

**The count after.** The same fields, now in the broken phase.

| Object | Count | Degrees of freedom |
|---|---|---|
| photon, massless | $1$ | $2$ |
| $W^+$, $W^-$, $Z$, massive | $3$ | $3\times3=9$ |
| physical scalar $h$ | $1$ | $1$ |
| **total** | | $\mathbf{12}$ |

A massive vector has three polarisations: two transverse and one longitudinal.

**The balance is $12=12$, and it is not automatic.** The equality holds because exactly three scalar components ceased to be independent fields and exactly three gauge polarisations were gained. The two events are one event, seen from two sides. Had the group been broken to nothing, four gauge fields would be massive and no photon would survive, and the count would still balance — the count does not determine the pattern, only its arithmetic.

**Where each component went.** The three eaten components are the two real parts of $\varphi^+$ and the imaginary part of $\varphi^0$. The fourth, the real part of $\varphi^0$ after the shift, is $h$. The identification is worth writing because it fixes which field is which:

| Component of $\varphi$ | Real fields | Charge | Fate |
|---|---|---|---|
| $\varphi^+$ | $2$ | $+1$ | the charged Goldstones, longitudinal $W^\pm$ |
| $\mathrm{Im}\,\varphi^0$ | $1$ | $0$ | the neutral Goldstone, longitudinal $Z$ |
| $\mathrm{Re}\,\varphi^0$ after the shift | $1$ | $0$ | the physical scalar $h$ |

**The number of Goldstones equals the number of broken generators.** The group has four generators and the surviving group has one, so three are broken, and three is the number of eaten components. This is the Goldstone theorem in its counting form, and the equality is the content of the previous table. The abelian case of [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html) has one broken generator and one eaten mode, and the two articles are the same argument at two sizes.

**The would-be Goldstones are gauge directions.** In a generic gauge the doublet is

$$
\varphi=\exp\left(\frac{i}{v}\sum_a\xi_a\tau_a\right)\frac{1}{\sqrt2}\begin{pmatrix}0\\ v+h\end{pmatrix},
$$

and the three fields $\xi_a$ are the would-be Goldstones. A gauge transformation with parameter $\Gamma_a=-\frac{2}{gv}\xi_a$ removes them, at the price of shifting the gauge fields by $\partial\xi/\partial R_\mu$. The combination that is gauge invariant is $W^a_\mu+\frac{2}{gv}\partial\xi_a/\partial R_\mu$, and it is that combination which carries the mass. The Goldstone is not destroyed: it becomes the longitudinal part of the field that absorbed it.

**Why this is a statement about a field and not about a particle.** The Goldstone mode never appears in the physical spectrum, and at the same time it is present in every gauge but the unitary one. The two statements are consistent because the mode is a gauge artefact: its presence or absence is a choice of coordinates on field space, and no observable depends on the choice. What is observable is the three polarisations of the massive vector, and those are counted in the second table.

## The Unitary Gauge and the Physical Spectrum

**The gauge.** The unitary gauge is the choice in which the three Goldstones are set to zero and the doublet is $\frac{1}{\sqrt2}(0,v+h)^{T}$. Three gauge conditions, three eaten fields, and no ghosts in the spectrum at tree level.

**The spectrum.** Five particles come out of the four gauge fields and the four scalar components:

| Particle | Mass | Polarisations | Coupling to $h$ |
|---|---|---|---|
| $\gamma$ | $0$ | $2$ | none |
| $W^\pm$ | $gv/2$ | $3$ | $2M_W^2/v$ |
| $Z$ | $\sqrt{g^2+g_{\mathrm Y}^2}\,v/2$ | $3$ | $2M_Z^2/v$ |
| $h$ | $\sqrt{2\lambda}\,v$ | $1$ | self-couplings below |

**The couplings are fixed by the masses.** Each coupling of the scalar to a pair of vectors is proportional to the mass squared, with no free constant:

$$
g_{hWW}=\frac{2M_W^2}{v}=g_{\mathrm{os}}M_W ,
\qquad
g_{hZZ}=\frac{2M_Z^2}{v} ,
\qquad
g_{hhWW}=\frac{2M_W^2}{v^2}=\frac{g^2}{2} ,
\qquad
g_{hhZZ}=\frac{2M_Z^2}{v^2}=\frac{g^2+g_{\mathrm Y}^2}{2} .
$$

The proportionality is not an extra assumption. It follows from the fact that the mass and the coupling both come from the same term $|D_\mu\varphi|^2$, expanded to different orders in $h$: the mass is the second-order term at $h=0$, and the coupling is the third-order term. The identity $g_{hWW}=g_{\mathrm{os}}M_W$ holds with the coupling $g_{\mathrm{os}}=2M_W/v=0.6529$ that belongs to the same scheme as $M_W$, and not with the $\overline{\mathrm{MS}}$ value $0.6517$ of §*The Numbers*; the two differ in the third digit, and the table below uses the measured mass.

**The scalar's self-couplings.** Expanding the potential to fourth order,

$$
g_{hhh}=\frac{3M_H^2}{v} ,
\qquad
g_{hhhh}=\frac{3M_H^2}{v^2} ,
$$

both fixed by the mass and the scale. These are the model's sharpest predictions that have not been tested: the $hhh$ coupling is the target of the next generation of colliders, and its measurement would test whether the potential has the double-well shape or something else.

**The numbers, for the measured scalar mass $M_H=125.09$ GeV.**

| Quantity | Value |
|---|---|
| $v$ | $246.22$ GeV |
| $\lambda=M_H^2/(2v^2)$ | $0.1291$ |
| $\mu=\sqrt{\mu^2}=M_H/\sqrt2$ | $88.45$ GeV |
| $g_{hhh}=3M_H^2/v$ | $190.7$ GeV |
| $g_{hhhh}=3M_H^2/v^2$ | $0.7743$ |
| $g_{hWW}=2M_W^2/v$ | $52.48$ GeV |
| $g_{hZZ}=2M_Z^2/v$ | $67.54$ GeV |

**The vintage of $M_H$.** The value is $125.09$ GeV, the 2015 ATLAS+CMS run-1 combination that the rest of the corpus quotes. The current average is $125.25\pm0.17$ GeV, a shift of $0.16$ GeV or $0.9\sigma$, and it moves no number here: $\lambda$ by $0.0003$, $g_{hhh}$ by $0.4$ GeV. The corpus keeps the older central value for one reason, the same one that keeps the fermion masses on a single vintage — [The Landau Pole, Triviality and Vacuum Stability](the-landau-pole-triviality-and-vacuum-stability.html) states the metastability margin as $1.39$ GeV $=4.6\sigma$ against $\sigma=0.30$, and a new central value would force a recomputation of a number quoted in two articles.

**The dimension of each coupling is the check.** A triple scalar coupling has dimension one and is measured in GeV; a quartic has dimension zero and is a pure number; a scalar-vector-vector coupling has dimension one. The table's units agree with the dimensions, which is a check on the powers of $v$ and not a deep statement.

**What the unitary gauge hides.** The Goldstones are gone, and so is the manifest $SU(2)$ invariance: the gauge looks asymmetric, and the propagators of the massive vectors grow with energy in a way that requires the scalar exchange to cancel. That cancellation is a check on the whole sector, and [Gauge Fixing in the Electroweak Theory](gauge-fixing-in-the-electroweak-theory-r-xi-gauges-ghosts-and-the-goldstone-equivalence-theorem.html) carries it. The unitary gauge is a convenient bookkeeping and a poor place to compute loops.

## The Numbers

**Two routes to the same two masses, and they do not agree at tree level.** This is the most informative numerical fact of the sector, and it is usually hidden by quoting one route.

**Route A: from the couplings and the scale.** With $\alpha^{-1}(M_Z)=127.95$, $\sin^2\theta_W=0.23122$ in the $\overline{\mathrm{MS}}$ scheme and $v=246.22$ GeV, the two couplings are

$$
g=\frac{e}{\sin\theta_W}=0.65174 ,
\qquad
g_{\mathrm Y}=\frac{e}{\cos\theta_W}=0.35742 ,
\qquad
e=\sqrt{4\pi\alpha}=0.31339 .
$$

Then

$$
M_W=\frac{gv}{2}=80.24\ \mathrm{GeV} ,
\qquad
M_Z=\frac{\sqrt{g^2+g_{\mathrm Y}^2}\,v}{2}=91.51\ \mathrm{GeV} ,
$$

against the measured $80.377$ and $91.1876$ GeV. The tree $W$ is $0.14$ GeV low and the tree $Z$ is $0.32$ GeV high, so the two misses are in opposite directions even within one route.

**Route B: from $\alpha$, $G_F$ and $M_Z$.** Three measured inputs over-determine the two masses, so the third is a test. The tree-level relations are

$$
M_W=M_Z\cos\theta_W ,
\qquad
\sin^2\theta_W\cos^2\theta_W=\frac{\pi\alpha}{\sqrt2\,G_F\,M_Z^2} .
$$

With $\alpha$ at the Z pole, $\alpha^{-1}(M_Z)=127.95$, the right-hand side is $0.17901$, the quadratic solves to $\sin^2\theta_W=0.23357$, and

$$
M_W=79.83\ \mathrm{GeV} ,
$$

which sits $0.55$ GeV below the measured $80.377$, a gap of $0.68$ per cent.

**Route C: the same relation with $\alpha$ at zero momentum.** Take instead $\alpha^{-1}(0)=137.036$. The right-hand side becomes $0.16714$, the quadratic solves to $\sin^2\theta_W=0.21215$, and

$$
M_W=80.94\ \mathrm{GeV} ,
$$

which sits $0.56$ GeV *above* the measured value. So the tree-level prediction moves by $1.1$ GeV when $\alpha$ is moved from the Z pole to zero momentum, and the gap flips sign. The two tree-level numbers bracket the measurement, and the pair of them is the clearest statement of what the correction is doing.

**The correction has a name and a size.** The quantity that reconciles the routes is

$$
\delta r=1-\frac{\pi\alpha(0)}{\sqrt2\,G_F\,M_W^2\sin^2\theta_W} ,
$$

evaluated with the measured $M_W$, the on-shell $\sin^2\theta_W=1-M_W^2/M_Z^2=0.22305$ and $\alpha(0)$. It equals

$$
\delta r=0.0355 ,
$$

and the two pieces of it are as large as the total. The running of the electromagnetic coupling from zero momentum to $M_Z$ contributes $+0.071$, the largest single term, and it is the piece that route B absorbs into its input. The top-quark and scalar loops contribute about $-0.033$, through $\delta\rho$ in the combination $-\tfrac{\cos^2\theta_W}{\sin^2\theta_W}\delta\rho$ with $\cos^2/\sin^2=3.48$ and $\delta\rho\approx0.0095$. The sum, $0.071-0.033=0.038$, is the $0.0355$ quoted. Neither piece is a small correction, and their near-cancellation is why the tree-level prediction is as good as it is.

**Why route A lands between them.** Route A uses measured $g$, $g_{\mathrm Y}$ and $v$, all three of which are themselves extracted with radiative corrections already folded in, so its tree values $80.24$ and $91.51$ are not a pure tree-level statement. It is a consistency check on the relations $M_W=gv/2$ and $M_Z=\sqrt{g^2+g_{\mathrm Y}^2}\,v/2$, and it passes at the level of the differences between the schemes in which its inputs are defined.

**The lesson, stated once.** A tree-level prediction in this sector is only as good as the definition of the couplings used to make it, and the standard practice is to quote $\delta r$ rather than to quote a discrepancy. A reader who compares a tree-level mass with a measured one without saying which $\alpha$ was used has compared two different statements.

**The scale of the breaking, from the muon lifetime.** The most precise input is $G_F$, and it fixes $v$ through

$$
\frac{G_F}{\sqrt2}=\frac{g^2}{8M_W^2}=\frac{1}{2v^2} ,
\qquad
v=\left(\sqrt2\,G_F\right)^{-1/2}=246.2197\ \mathrm{GeV} .
$$

This is the sector's counterpart of the pion decay constant: a low-energy constant, measured to five digits, that fixes the scale of a symmetry breaking. The analogy is exact in structure and not in size — the pion constant is $92$ MeV and the electroweak scale is $246$ GeV, and the ratio is the ratio of the two breakings.

**A third number, for the same reason.** The width of the $W$ into one lepton pair is computable at tree level from the same three inputs,

$$
\Gamma\left(W\to e\nu\right)=\frac{G_F\,M_W^3}{6\pi\sqrt2}=227\ \mathrm{MeV} ,
$$

against the measured $223$ MeV. The agreement to two per cent is a check on the coupling $g/\sqrt2$ that enters the leptonic vertex, and the difference is again the radiative correction.

**What the three numbers establish.** The sector has five measured quantities — $M_W$, $M_Z$, $\sin^2\theta_W$, $\alpha$ and $G_F$ — and four relations among them at tree level, so one combination is a genuine test. The test passes at tree level to the accuracy of the one-loop correction, which is the strongest empirical statement available about the sector and is the subject of [The Electroweak Precision Observables](electroweak-precision-observables-the-oblique-parameters-s-t-u.html).

## The $\rho$ Parameter and Custodial Symmetry

**The parameter.** Define

$$
\rho=\frac{M_W^2}{M_Z^2\cos^2\theta_W} .
$$

With the tree-level masses and $\cos^2\theta_W=g^2/(g^2+g_{\mathrm Y}^2)$, the numerator is $g^2v^2/4$ and the denominator is $\frac{(g^2+g_{\mathrm Y}^2)v^2}{4}\cdot\frac{g^2}{g^2+g_{\mathrm Y}^2}=\frac{g^2v^2}{4}$. So $\rho=1$ identically for the doublet. That is not a measurement; it is an algebraic identity, and the measured value is consistent with it.

**The general formula.** For a scalar sector of several multiplets, each with weak isospin $T_i$ and vacuum expectation value $v_i$ in the component of third component $T_{3i}$,

$$
\rho=\frac{\sum_i v_i^2\left[T_i(T_i+1)-T_{3i}^2\right]}{\sum_i 2\,v_i^2\,T_{3i}^2} .
$$

For one doublet with $T=\tfrac12$ and $T_3=-\tfrac12$ the numerator is $v^2\left(\tfrac34-\tfrac14\right)=\tfrac12v^2$ and the denominator is $2v^2\tfrac14=\tfrac12v^2$, giving one. For one triplet with $T=1$ and $T_3=-1$ the numerator is $v^2(2-1)=v^2$ and the denominator $2v^2$, giving one half. A triplet therefore pulls $\rho$ below one, and the measurement bounds its vacuum expectation value.

**Why $\rho=1$ is structural.** The doublet, written as a $2\times2$ matrix $\Phi=(\tilde\varphi,\varphi)$ whose columns are the doublet and its conjugate, has a potential that depends only on $\mathrm{tr}(\Phi^\dagger\Phi)$. The potential therefore has an $SU(2)_L\times SU(2)_R$ symmetry larger than the gauged one, and the vacuum $\langle\Phi\rangle\propto\mathrm I$ breaks it to the diagonal $SU(2)_V$. That residual symmetry is **custodial**, and it is what makes the three gauge bosons' masses related.

**The hypercharge breaks custodial symmetry explicitly.** The gauged hypercharge is the third generator of $SU(2)_R$, so switching it on distinguishes the third direction from the other two. The tree-level $\rho=1$ survives because the vacuum is custodially invariant; the breaking appears at one loop, in the difference between the $W$ and $Z$ self-energies, and it is one of the corrections inside $\delta r$.

**The empirical bound, in the form that matters here.** The measured $\rho$ is unity to about four parts in $10^4$, and that number bounds any additional multiplet's vacuum expectation value. A triplet at the electroweak scale would move $\rho$ by an amount of order $v_t^2/v^2$, so the bound is a bound on $v_t/v$ of a few per cent. The doublet is not merely the simplest choice; it is the one the measurement allows at the scale of the breaking.

## The Equivalence Theorem

**The statement.** At energies large compared with the gauge-boson mass, an amplitude with a longitudinal $W$ or $Z$ in the initial or final state equals, up to corrections of order $M/E$, the amplitude with the corresponding Goldstone field. In the notation above, $\mathcal{M}(W_L\ldots)=\mathcal{M}(\xi\ldots)+O(M/E)$.

**Why it is true here.** The Goldstone fields are the gauge directions that the mass term mixes with the longitudinal polarisation. In the $R_\xi$ gauges the mixing is proportional to the Goldstone mass, which is $M_W$ in unitary-weighted gauges; at high energy the mixing is small and the two states are effectively the same.

**The use.** The theorem converts a calculation in a gauge theory into a calculation in a scalar theory, which is the reason the longitudinal amplitudes of the Standard Model are computable. It is also the reason the sector is testable: the scattering of longitudinal gauge bosons at high energy would grow with energy if the scalar were absent, and the scalar exchange cancels the growth. The cancellation is exact only if the scalar's couplings are the ones in the table above, so a measurement of longitudinal scattering is a measurement of that table.

**The bound it gives.** Without a scalar, the amplitude for $W_LW_L\to W_LW_L$ grows as $E^2/v^2$ and violates unitarity at about $1.2$ TeV. The scalar's exchange cancels the growth, and the residual term is of order $M_H^2/v^2$. The scale $1.2$ TeV is therefore the scale at which something must appear if the sector is not as described, and it is the reason the scalar was expected below about a TeV.

**The theorem is a check on the counting.** It says that the eaten Goldstone and the longitudinal polarisation are the same object at high energy, which is the dynamical counterpart of the counting identity $12=12$ of §*The Counting of Degrees of Freedom*. The count says the number is right; the theorem says which number is which.

## What the Framework Supplies

**The abelian mechanism, whole.** The framework constructs, for a single charged scalar and one abelian gauge field, everything the previous sections use: a potential whose minimum is away from the origin, a kinetic term that becomes a mass term at the vacuum, the mass $M_A=\kappa v$ with $\kappa$ the effective charge, a radial mode of mass $\sqrt{2\beta}\,v$, and a count that balances. [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html) carries the construction, and nothing in it is imported except the potential's shape.

**The distance to the electroweak case is exactly three items.** Stated as a list, because the list is the boundary.

| Item | Framework | Standard Model |
|---|---|---|
| the gauge group | central $\mathrm{U}(1)$, or $SU(2)$ from $\mathbb{B}_\Phi$ | $SU(2)_L\times\mathrm{U}(1)_Y$ |
| the scalar's representation | the centre, a singlet of $SU(2)$ | a doublet, charged under both factors |
| the scalar's hypercharge | one central charge, vector-like | $\tfrac12$, chiral |

**The singlet cannot break the group, and this is the sharpest statement.** A field in the centre commutes with every element of the algebra, so it is annihilated by the $SU(2)$ action. A vacuum invariant under a group does not break it. The framework's scalar gives a mass to the abelian factor and to nothing else, and no amount of rewriting changes that: the obstruction is the representation, not the mechanism.

**What the algebra does supply.** A two-dimensional module, since $\mathbb{B}\cong M_2(\mathbb{C})$ acts on $\mathbb{C}^2$. A doublet-shaped object is therefore available. What is missing is the assignment of the two factors' actions on it, which is the content of [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html) and which that article shows is imported.

**The one place the framework's formula matches.** The abelian mass formula $M_A=\kappa v$ and the standard $M_W=gv/2$ are the same formula with $\kappa=g/2$. The factor of one half is the isospin of the scalar and not a property of the vector, and [The W and Z Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html) records the identification. It is a genuine match of structure, and it is a match of one number with a reinterpreted charge, not a derivation.

**What a derivation would need.** A scalar in the algebra's defining module, a hypercharge operator acting on it with the two chiralities distinguished, and a potential invariant under both. The corpus records the first as available and the second as open. Until both are settled, the electroweak sector is imported, and this article's computation is a computation about the model.

## Summary

The electroweak group is broken to $\mathrm{U}(1)_{\mathrm{em}}$ by one complex doublet of hypercharge $\tfrac12$ with the potential $-\mu^2\varphi^\dagger\varphi+\lambda(\varphi^\dagger\varphi)^2$. The minima form a three-sphere $\varphi^\dagger\varphi=v^2/2$ with $v^2=\mu^2/\lambda$, and the vacuum $\langle\varphi\rangle=\frac{1}{\sqrt2}(0,v)^{T}$ is annihilated by $Q=T_3+Y$ and by no other generator. That single line is why the photon stays massless and the other three directions acquire mass.

The mass matrix in the basis $(W^1,W^2,W^3,B)$ is $\tfrac{v^2}{4}$ times a block-diagonal matrix with the charged block $g^2\mathrm I$ and the neutral block $\binom{g^2\ -gg_{\mathrm Y}}{-gg_{\mathrm Y}\ \ g_{\mathrm Y}^2}$. Its eigenvalues are $g^2v^2/4$ twice, zero once and $(g^2+g_{\mathrm Y}^2)v^2/4$ once, giving $M_W=gv/2$, $M_\gamma=0$ and $M_Z=\sqrt{g^2+g_{\mathrm Y}^2}\,v/2=M_W/\cos\theta_W$. The zero eigenvalue is structural: the neutral block's determinant vanishes identically, because the direction along which $Q$ annihilates the vacuum is one-dimensional. The eigenvectors are the photon $A=\sin\theta_WW^3+\cos\theta_WB$ and the $Z=\cos\theta_WW^3-\sin\theta_WB$, so the mixing angle is the diagonalising angle and not an independent parameter. The trace sum rule $2M_W^2+M_Z^2=\tfrac{v^2}{4}(3g^2+g_{\mathrm Y}^2)$ is exact at tree level and closes on the numbers.

The counting balances at twelve. Before the breaking, four massless vectors give eight polarisations and the four real scalar components give four. After, the photon gives two, the three massive vectors nine and the physical scalar one. Three scalar components ceased to be independent fields and three gauge polarisations were gained, and the two events are one. In the unitary gauge the spectrum is a massless photon, a $W$ pair, a $Z$ and one scalar, with couplings $g_{hWW}=2M_W^2/v$, $g_{hZZ}=2M_Z^2/v$, $g_{hhh}=3M_H^2/v$ and $g_{hhhh}=3M_H^2/v^2$, all fixed by the masses.

Numerically the sector is over-determined and the over-determination is the test. From $g$, $g_{\mathrm Y}$ and $v$ the tree masses are $80.24$ and $91.51$ GeV; from $\alpha$, $G_F$ and $M_Z$ the tree value of $M_W$ is $79.83$ GeV against the measured $80.377$. Both routes miss by about half a GeV, in opposite directions, and the discrepancy is the one-loop correction: $\delta r=0.0355$, of which $+0.071$ is the running of $\alpha$ from zero momentum to $M_Z$ and about $-0.033$ is the top-quark and scalar loop contribution. The scale itself comes from the muon lifetime, $v=(\sqrt2G_F)^{-1/2}=246.2197$ GeV, which is the electroweak counterpart of a pion decay constant. The same three inputs give $\Gamma(W\to e\nu)=227$ MeV at tree level against $223$ measured.

The $\rho$ parameter is unity by identity for a doublet and deviates for larger multiplets, through the general formula $\rho=\sum v_i^2[T_i(T_i+1)-T_{3i}^2]/\sum 2v_i^2T_{3i}^2$, which gives one half for a triplet. The identity is the visible sign of a custodial $SU(2)$ symmetry of the potential that the vacuum preserves and the hypercharge gauging breaks. The measurement of $\rho$ to four parts in $10^4$ is therefore a bound on any additional multiplet's vacuum expectation value.

The framework supplies the abelian mechanism whole and stops at three items: the group, the representation and the hypercharge. Its scalar is central, hence a singlet, hence unable to break the non-abelian factor; its algebra nonetheless supplies a two-dimensional module in which a doublet could live, and what is missing there is the assignment of the two actions on it. The abelian mass formula $\kappa v$ equals $gv/2$ with $\kappa=g/2$, which is a match of structure and a reinterpretation of one charge, not a derivation. The electroweak sector is imported, and this article measures how much of it the import brings.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi$, $\varphi^+$, $\varphi^0$ | The scalar doublet of hypercharge $\tfrac12$ and its components |
| $\xi_{\mathrm{scl}}$, $\tilde\Xi=\xi e_t$ | The same object in the W/Z and Higgs articles |
| $\tilde\varphi$ | The conjugate doublet of hypercharge $-\tfrac12$ |
| $\mu^2$, $\lambda$ | The two parameters of the potential; $\mu^2=\lambda v^2$ |
| $v$ | Vacuum expectation value, $\sqrt2\langle\varphi^0\rangle=246.2197$ GeV |
| $h$ | The radial excitation of the neutral component |
| $\varphi_0$ | The vacuum $\frac{1}{\sqrt2}(0,v)^{T}$ |
| $\tau_a=\sigma_a/2$ | Weak-isospin generators in the doublet |
| $M^2$ | The $4\times4$ squared-mass matrix in the basis $(W^1,W^2,W^3,B)$ |
| $M_W$, $M_Z$, $M_H$ | The three masses; $M_Z=M_W/\cos\theta_W$, $M_H=\sqrt{2\lambda}\,v$ |
| $A_\mu$, $Z_\mu$ | The photon and the neutral massive field |
| $\theta_W$ | $\tan\theta_W=g_{\mathrm Y}/g$ |
| $e$ | $g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$ |
| $g_{hWW}$, $g_{hZZ}$, $g_{hhh}$, $g_{hhhh}$ | Scalar couplings, fixed by the masses |
| $\rho$ | $M_W^2/(M_Z^2\cos^2\theta_W)$, identically one for a doublet |
| $\delta r$ | The correction to the tree-level mass relation, $0.0355$, computed from $\alpha(0)$ |
| $G_F$ | $1.1663787\times10^{-5}$ GeV$^{-2}$, fixing $v$ |
| $\xi_a$ | The three would-be Goldstone fields |

## Further Reading

- [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). Why $Y_\varphi=\tfrac12$, which this article takes as given.
- [The Standard Model Lagrangian Assembled: Four Sectors in One Expression](the-standard-model-lagrangian-assembled-four-sectors-in-one-expression.html). The scalar sector in the assembled sum, and the sign rule that fixes the kinetic term.
- [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html). The abelian case in full, whose gap this article fills for the electroweak group.
- [The W and Z Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html). The mixing and the masses, here derived from the mass matrix.
- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). Where the two scalar parameters sit in the count of nineteen.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The intrinsic group that the framework's scalar can and cannot break.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html). Why the framework's central scalar is a singlet, and why a singlet breaks nothing.
- [The Standard Model under the Biquaternion Framework — A Research Agenda](the-standard-model-under-the-biquaternion-framework-a-research-agenda.html). The sector in agenda form, with this article's three items marked imported.

The two companions that §*The Numbers* leans on — [The QCD Lagrangian: Colour, the Triplet, the Octet and the Feynman Rules](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html), for the sector at the other end of the mass ladder, and [Electroweak Precision Observables: the Oblique Parameters $S$, $T$, $U$](electroweak-precision-observables-the-oblique-parameters-s-t-u.html), for the $\delta r$ and $\rho$ statements used above — are both in the corpus.
