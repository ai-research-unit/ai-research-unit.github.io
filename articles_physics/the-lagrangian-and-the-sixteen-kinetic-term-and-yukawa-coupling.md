# __The Lagrangian and the Sixteen: The Kinetic Term and the Yukawa Coupling__

## Introduction

**The question.** What do the sixteen Weyl fields contribute to the $\mathrm{SU}(4)$ action, and what does the scalar couple to them through?

**The answer.** Two pieces and two matrices.

$$
\boxed{\;\mathcal{L}_{\xi}=\sum_{f=1}^{16}\bar\xi_{f}\,i\gamma_{\imath}D_{\imath}\,\xi_{f},
\qquad
\mathcal{L}_{\mathrm{Yuk}}=y_{\alpha\beta}\,\bar\xi^{\alpha}Ξ\,\xi^{\beta}+\text{h.c.}\;}
$$

**One covariant derivative with fifteen matrices of each kind, and one Yukawa matrix on the copy index.** The kinetic term is fixed by the representation and carries no free number; the Yukawa term is one $2\times2$ complex matrix and carries four real numbers.

**What this article does.** It writes both pieces, counts the states and the vertices, derives why the Yukawa operator needs the matrix index, extracts the mass matrix after the condensate, and computes the one ratio the sector predicts — the ratio that falsifies it.

**What it does not do.** It does not diagonalise the Yukawa matrix or run the masses; that is [The Yukawa Sector](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html)'s, and this article stops where that one begins. **Nor does it repeat the masslessness argument**, which is [The Sixteen Above $M_C$](the-sixteen-above-m-c-massless-vector-like-and-what-that-costs.html)'s.

## The Kinetic Term

**Sixteen Weyl fields, two representations, one derivative.**

$$
D_{\imath}\xi_{i}=\partial_{\imath}\xi_{i}-ig_4A_{a,\imath}\bigl(t_{a}\bigr)_{i}{}^{j}\xi_{j},
\qquad
D_{\imath}\bar\xi^{i}=\partial_{\imath}\bar\xi^{i}+ig_4A_{a,\imath}\bar\xi^{j}\bigl(t_{a}\bigr)_{j}{}^{i},
$$

with $t_{a}$ the fifteen generators in whichever representation the field sits in, and the sign difference the statement that one carries the index up and the other down.

**Why the coupling is the same $g_4$ and not a second one.** A gauge symmetry has one coupling per simple factor, and $\mathrm{SU}(4)$ is one factor. **The identity of the coupling across representations is what makes the gauge sector a gauge sector**, and it is the sense in which the primordial force is one force.

**The content and the state count.**

| representation | Weyl fields | states | the generator matrices |
| --- | --- | --- | --- |
| $\mathbf4$ | $2$ per copy value | $2\times2\times2=8$ | $t_{a}$, $4\times4$ |
| $\bar{\mathbf4}$ | $2$ per copy value | $8$ | $-t_{a}^{T}$, $4\times4$ |
| **total** | $16$ | $\mathbf{32}$ | |

**Thirty-two states, sixteen fields, and the pair is what makes a mass possible.** A Dirac mass needs a left-handed and a right-handed field of the same charge, and the content supplies them in conjugate pairs — **which is why the corpus's choice not to write a bare mass is a choice and not a prohibition.** [The Sixteen Above $M_C$](the-sixteen-above-m-c-massless-vector-like-and-what-that-costs.html) states what that choice costs.

**The current the kinetic term produces.**

$$
j^{\xi}_{a,\imath}=\sum_{f=1}^{16}\bar\xi_{f}\gamma_{\imath}t_{a}\xi_{f},
$$

**a vector current, bilinear in the fields, and the only source of the gauge field above $M_C$ apart from the scalar's.** Its ordinary divergence is not zero; its covariant divergence is. **So no gauge charge exists in this phase**, and the corpus's conserved charges are properties of the residual group below $M_C$.

**The vertices, counted.** Each of the fifteen generators gives one vertex per Weyl field it acts on, and the count is read off the representation:

| vertex | count | why |
| --- | --- | --- |
| $\bar\xi A\xi$ for $\xi\in\mathbf4$ | $15$ | one per generator, per field, summed over the eight |
| $\bar\xi A\xi$ for $\xi\in\bar{\mathbf4}$ | $15$ | the conjugate matrices, the same count |
| distinct Lorentz structures | $1$ | $\gamma_{\imath}$, no $\sigma_{\imath\jmath}$ at dimension four |

**At dimension four there is no Pauli term and no dipole coupling**, because $\bar\xi\sigma_{\imath\jmath}F_{\imath\jmath}\xi$ has dimension five. **The kinetic term is therefore minimal and the gauge vertex is fixed by the representation alone**, with no free coefficient to adjust.

## The Yukawa Operator

**The operator is forced to be a trace, and the trace is what needs the matrix index.**

$$
\bar\xi^{\alpha}\,Ξ\,\xi^{\beta}\to\mathbf1
\quad\Longleftrightarrow\quad
\bar{\mathbf4}\otimes\bigl(\mathbf{15}\oplus\mathbf1\bigr)\otimes\mathbf4\supset\mathbf1 .
$$

**The product contains exactly one singlet, and it comes from the $\mathbf1$ in $Ξ$.** The $\mathbf{15}$ part contributes nothing: $\bar{\mathbf4}\otimes\mathbf{15}\otimes\mathbf4$ has no invariant with one $\bar\xi$ and one $\xi$. **So the operator is unique and the Yukawa matrix is $2\times2$, not a matrix per block.**

**The quartet would have given nothing at all.** $\bar{\mathbf4}\otimes\mathbf4\otimes\mathbf4$ has no singlet because $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$, and neither summand is $\bar{\mathbf4}$. **A scalar in the fundamental has no Yukawa coupling to these sixteen fermions**, so the operator's existence is an argument for the matrix index and not a convention about it.

**The copy index is what the matrix $y$ acts on.** $\alpha,\beta$ run over the two values, and the gauge sector is blind to them: no vertex in the kinetic term carries $\alpha$. **So the Yukawa matrix is the only place where the two copies mix**, and its diagonalisation is a change of basis that no gauge interaction can see.

**Four real parameters, and their count.** A $2\times2$ complex matrix has eight real entries, of which three phases are removed by rephasing the fermions and one by an overall phase that is unobservable; that leaves four. **The corpus's Yukawa article states the same count from the other side**, and the four are the sector's whole content.

## The Mass Matrix After the Condensate

**Substitute $Ξ=Ξ_{0}+\delta Ξ$ with $Ξ_{0}=v_{C}D$ and the Yukawa term becomes a mass term plus a coupling.**

$$
\mathcal{L}_{\mathrm{Yuk}}\supset y_{\alpha\beta}\,\bar\xi^{\alpha}\bigl(v_{C}D\bigr)\xi^{\beta}+\text{h.c.}
=y_{\alpha\beta}\,v_{C}\,\bar\xi^{\alpha}_{\,i}D_{ij}\xi^{\beta}_{\,j}+\text{h.c.}
$$

**The condensate enters as a diagonal matrix with entries $(-3,1,1,1)$**, so a fermion on the lepton line gets $-3v_{C}$ times its Yukawa entry and a fermion on a colour line gets $+v_{C}$ times its own.

**The ratio is three, and it is the sector's only prediction.**

| line | the condensate entry | the mass |
| --- | --- | --- |
| lepton | $-3$ | $3\lvert y\rvert v_{C}$ |
| colour, each of three | $+1$ | $\lvert y\rvert v_{C}$ |

**So a lepton and a down-type quark with the same Yukawa entry have masses in the ratio $3:1$**, which is the statement $m_{e}=3m_{d}$ once the two entries are identified.

**The identification is the weak point and it is stated.** $y$ is one matrix on the copy index, so the lepton and the down quark receive the *same* $y$ only if they sit in the same copy — and the copy index is precisely what becomes the right-handed weak index at the transition. **The corpus makes that identification explicitly**, and the whole content of the prediction is that it is made.

**The number.** With $m_{d}=4.67\ \mathrm{MeV}$ and $m_{e}=0.511\ \mathrm{MeV}$ at the scales where they are quoted,

$$
\frac{3m_{d}}{m_{e}}=\frac{3\times4.67}{0.511}=27.4 .
$$

**The model says $1$ and the world says $27.4$**, so the sector is falsified by a factor of twenty-seven and the falsification is not an arithmetic slip. **The article that owns this comparison says the same number and treats it as the model's sharpest failure**; this article's contribution is to show that the factor comes from the condensate's entries and from nowhere else.

## The Scale the Yukawa Sector Sits At

**Two numbers tie the pieces together, and both are computed from the matching.**

$$
v_{C}=\frac{\sqrt2\,M_X}{g_4}=\frac{1.4142\times2.33\times10^{5}}{0.8544}=3.85\times10^{5}\ \mathrm{GeV},
\qquad
M_X=\tfrac12 g_4^{2}v_{C}^{2} .
$$

**So the condensate is three hundred and eighty-five TeV**, and a fermion with $y=1$ has a mass of order $v_{C}$. **Every fermion in the model that is not protected is therefore at the transition scale**, and the corpus's light fermions are light because their Yukawa entries are small and not because their scale is.

**The check is the inverse.** $\tfrac12(0.730)(3.853\times10^{5})^{2}=5.42\times10^{10}\ \mathrm{GeV}^{2}$, whose square root is $2.33\times10^{5}\ \mathrm{GeV}$ — the matching scale the coupling article uses. **The two numbers are the same number twice**, and that is what a matching relation is.

**What the Yukawa sector does not fix.** $v_{C}$ is fixed by the matching and not by the Yukawa; $y$'s four numbers are free; and the light fermion masses come from small entries and not from a hierarchy mechanism. **The model has a hierarchy problem and this article does not solve it**: it states that the ratio $m_e/m_d$ is a group prediction and that the smallness of all the masses is not.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the Weyl count | $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$ | $16$ |
| the state count | $2$ per Weyl | $32$ |
| the gauge vertices per representation | one per generator per field | $15$ |
| Lorentz structures at dimension four | $\gamma_{\imath}$ only | $1$ |
| the Yukawa singlets | $\bar{\mathbf4}\otimes(\mathbf{15}\oplus\mathbf1)\otimes\mathbf4$ | exactly $1$, from the $\mathbf1$ |
| the quartet's singlets | $\bar{\mathbf4}\otimes\mathbf4\otimes\mathbf4$ | $0$ |
| the Yukawa parameters | $8$ real minus $3$ rephasings minus $1$ overall | $4$ |
| the mass ratio from the condensate | $\lvert-3\rvert:\lvert+1\rvert$ | $3:1$ |
| the predicted ratio against the measured | $3m_{d}/m_{e}$ | $27.4$ $\Rightarrow$ falsified |
| $v_{C}$ from the matching | $\sqrt2M_X/g_4$ | $3.85\times10^{5}\ \mathrm{GeV}$ |

## Summary

**The kinetic term is minimal and fixed**: sixteen Weyl fields, two representations, fifteen matrices of each kind, thirty-two states, one vertex per generator per field, and no free coefficient at dimension four.

**The Yukawa operator exists only for the matrix index.** $\bar{\mathbf4}\otimes(\mathbf{15}\oplus\mathbf1)\otimes\mathbf4$ has one singlet and $\bar{\mathbf4}\otimes\mathbf4\otimes\mathbf4$ has none, so the quartet reading would leave the sixteen with no mass operator anywhere in the theory.

**The condensate's entries $(-3,1,1,1)$ give a $3:1$ mass ratio**, and identifying the two copy entries gives $m_{e}=3m_{d}$, which is wrong by a factor $27.4$. **That number is the sector's whole output and it is a refutation**, not a fit.

**And the scale is not a prediction.** $v_{C}=385\ \mathrm{TeV}$ comes from the matching, the four Yukawa numbers are free, and the lightness of the observed fermions is an input the model reproduces by small entries and does not explain.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\xi_{f}$, $\bar\xi_{f}$ | the sixteen Weyl fields, $f=1,\dots,16$, of $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$ |
| $t_{a}$ | the fifteen generators in the $\mathbf4$; $-t_{a}^{T}$ in the $\bar{\mathbf4}$ |
| $y_{\alpha\beta}$ | the $2\times2$ Yukawa matrix on the copy index, four real parameters |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the condensate's shape |
| $v_{C}$ | the condensate's magnitude, $3.85\times10^{5}\ \mathrm{GeV}$ |
| $M_X$ | $\tfrac12g_4^{2}v_{C}^{2}=2.33\times10^{5}\ \mathrm{GeV}$ |

## Further Reading

- [The Yukawa Sector of the $\mathrm{SU}(4)$ Model](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html). The diagonalisation this article stops short of, and the falsification in full.
- [The Sixteen Above $M_C$](the-sixteen-above-m-c-massless-vector-like-and-what-that-costs.html). Why the content is massless above the transition, and what the vector-like pairing costs.
- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). Both pieces inside the full display.
- [The Primordial Coupling](the-primordial-coupling-g4-as-a-boundary-condition-and-what-runs-above-m-c.html). $g_4$ at $M_X$, from which $v_{C}$ is computed here.
