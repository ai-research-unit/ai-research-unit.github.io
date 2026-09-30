# __Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form__

## Introduction

The mass formula of the companion *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form* comes from a family of wave equations, not from a single one. These are the **relativistic wave equations of Bhabha, Gel'fand and Yaglom**: finite-dimensional equations for a field in an arbitrary Lorentz representation $\tau^{l\dot l}$, whose mass operator is a matrix and whose determinant is a polynomial in $p^2$ with several roots — one field, several masses. When the representation is an interlocking chain $(l,\dot l)\oplus(\dot l,l)$, the equation describes a particle of the generalised spin $s=|l-\dot l|$ and of mass $m$, and the chain that carries the proton is a case in point: the proton's equation is a $3540$-component equation, and its mass is the leading root.

This article records the equations, the spin chains they live on, and the third ingredient the programme attaches to them: the reduction of the equations from Minkowski space to the **bivector space** $\mathbb{R}^6$. The reduction is not decorative. The Lorentz group is six-dimensional, its parameter space is six-dimensional, and the space of antisymmetric two-tensors — the bivectors, the field strengths — is six-dimensional; the programme maps the wave equations into that space and writes them there. The corpus knows this space under another name: the field-strength biquaternion $\mathbf{E}+i\mathbf{B}$, the subject of *The Field-Strength Biquaternion and Its Invariants*, which has six real components and is exactly a point of the bivector space. The article notes the identification and states where it stops.

It is worth separating this article from the companion that shares the name Bhabha. *Bhabha Scattering in Biquaternionic Form* is about the elastic scattering of an electron and a positron; the present article is about Bhabha's *wave equations*, a different piece of work by the same author. The two are cross-referenced and not merged.

The article is organised as follows. A first section fixes the spintensors and the spin chains. A second states the wave equations and the determinant argument. A third gives the bivector-space reduction. A fourth works the proton chain and its Dirac limit. A closing section states the biquaternion reading.

**Conventions.** The Lorentz conventions are the corpus's: $\mathrm{Spin}^{+}(1,3)\cong\mathrm{SL}(2,\mathbb{C})$, representations $\tau^{l\dot l}$ with $l=k/2$, $\dot l=r/2$, spin $s=|l-\dot l|$. The equations, the chains and the bivector-space material are transcribed from the spinor-structure programme (V. V. Varlamov, arXiv:1409.1400, §2.2) and from the Bhabha and Gel'fand–Yaglom papers. One convention differs and is flagged forward: the source's Minkowski metric is $\mathrm{diag}(-1,-1,-1,+1)$, whereas the corpus uses the $ict$ metric with three positive spacelike directions; the bivector-space signs below are the source's, and a discrepancy in their printed metric is recorded as a convention issue rather than smoothed over.

- Companion article *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form*, for the mass spectrum these equations produce.
- Companion article *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form*, for the space in which the multi-mass fields are placed.
- Corpus article *The Field-Strength Biquaternion and Its Invariants*, for the biquaternion form of the bivector space.
- Corpus article *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, for the spinor form of the Dirac and Maxwell equations used in the Dirac limit.
- Corpus article *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation*, for the Maxwell–Dirac package in the corpus's own form.
- Corpus article *Clifford Structure of the Biquaternion Algebra*, for the algebra the first member of the chain is.
- Corpus article *Bhabha Scattering in Biquaternionic Form*, for the other work bearing Bhabha's name.

## Spintensors and the Spin Chains

### The Spintensor

A representation of $\mathrm{SL}(2,\mathbb{C})$ is carried by a **spintensor** with $k$ undotted and $r$ dotted indices,

$$
S = s_{\alpha_1\alpha_2\dots\alpha_k\dot\alpha_1\dot\alpha_2\dots\dot\alpha_r},
$$

a polynomial in the products of the undotted and dotted spinors $s_\alpha$ and $s_{\dot\alpha}$; the representation is $\tau^{l\dot l}$ with

$$
l = \tfrac{k}{2}, \qquad \dot l = \tfrac{r}{2},
$$

and the spintensor is the image of the tensor product with $k$ fundamental factors and $r$ conjugate factors,

$$
\underbrace{\mathbb{C}^2\otimes\cdots\otimes\mathbb{C}^2}_{k}\otimes
\underbrace{\bar{\mathbb{C}}^2\otimes\cdots\otimes\bar{\mathbb{C}}^2}_{r},
$$

whose spin space is

$$
\underbrace{S_2\otimes\cdots\otimes S_2}_{k}\otimes
\underbrace{\dot S_2\otimes\cdots\otimes\dot S_2}_{r}
$$

with $2^{k+r}$ components. Using the symmetry under permutations of the indices within each group, a spintensor can be taken **symmetric**, and the space $\mathrm{Sym}^{(k,r)}$ of symmetric spintensors has dimension

$$
\dim\mathrm{Sym}^{(k,r)} = (k+1)(r+1),
$$

the **degree** of the representation $\tau^{l\dot l}$. This is the number that the mass formula uses: because $l=k/2$ and $\dot l=r/2$, the degree is $(2l+1)(2\dot l+1)$, and $\mathrm{SL}(2,\mathbb{C})$ has representations of every degree.

### The Two Schemes

The representations do not stand alone. $\tau^{l\dot l}$ and $\tau^{l'\dot l'}$ are **interlocking** when $l'=l\pm\frac12$, $\dot l'=\dot l\pm\frac12$, and the interlocking relations arrange all representations into three schemes: the **Bose scheme** of integer spin (the spin-0, spin-1, ... lines) and the **Fermi scheme** of half-integer spin (the spin-$\frac12$, spin-$\frac32$, ... lines), each an infinite grid of representations joined diagonally. A **field of type $(l,\dot l)\oplus(\dot l,l)$** is a field transforming in a representation and its conjugate; the wave equations of the next section are written for such fields and describe a particle of generalised spin

$$
s = |l-\dot l| .
$$

The usual spin is recovered only on the restriction $\tau^{l\dot l}\to\tau^{l,0}$ (or $\to\tau^{0,\dot l}$), that is, at $\mathrm{SU}(2)\subset\mathrm{SL}(2,\mathbb{C})$, where the spin values run over $-l,-l+1,\dots,l$.

## The Wave Equations and the Determinant Argument

The equations are written with a set of generators $\Lambda^{l\dot l}_j$ of the representation, one for each spatial direction, and read, for the field $\psi$ of the representation $\tau^{l\dot l}$,

$$
\Bigl(\Gamma^{0}p_0-\Gamma^{1}p_1-\Gamma^{2}p_2-\Gamma^{3}p_3\Bigr)\psi + m\psi = 0,
\qquad\text{or}\qquad \Gamma(p)\psi = -m\psi,
$$

with $\Gamma(p)$ the momentum-contracted generator matrix. A nonzero solution requires

$$
D(p) = \det\bigl(\Gamma(p)+mE\bigr) = 0 .
$$

The determinant is a polynomial in $p_0,p_1,p_2,p_3$ and is constant on the transitivity surfaces of the Lorentz group, the hyperboloids $s^2(p)=p_0^2-p_1^2-p_2^2-p_3^2=\text{const}$, so it depends on $s^2$ alone and factors as

$$
\tilde D\bigl(s^2\bigr) = c\bigl(s^2-m_1^2\bigr)\bigl(s^2-m_2^2\bigr)\cdots\bigl(s^2-m_k^2\bigr).
$$

The equation has a solution exactly when $s^2=m_i^2$, so the roots $m_i$ are the masses the field can carry: a multi-mass field. Putting $\mathbf{p}=0$ makes $\Gamma(p)=p_0\Gamma^0$ and

$$
\det\bigl(p_0\Gamma^0+mE\bigr) = \tilde c\,\bigl(p_0-\mu_0\lambda_1\bigr)\bigl(p_0-\mu_0\lambda_2\bigr)\cdots,
$$

with $\lambda_i$ the eigenvalues of $\Gamma^0$ and $\mu_0$ a single mass scale. Comparing the two factorisations gives

$$
m_1 = \mu_0\lambda_1,\quad -m_1=\mu_0\lambda_2,\quad m_2=\mu_0\lambda_3=-\mu_0\lambda_4,\ \dots
$$

for the representations of type $\tau^{0,\dot l}$, and in the general case of $\tau^{l\dot l}$

$$
m_1 = \mu_0\lambda_1\dot\lambda_1,\qquad -m_1=\mu_0\lambda_2\dot\lambda_2,\qquad m_2=\mu_0\lambda_3\dot\lambda_3=-\mu_0\lambda_4\dot\lambda_4,\ \dots
$$

Each non-null eigenvalue $\lambda$ occurs with $-\lambda$ of the same multiplicity, so the masses come in $\pm$ pairs, and the physical masses are the positive $|\lambda_i\dot\lambda_i|$ times $\mu_0$. In the infinite-dimensional limit $l,\dot l\to\infty$ the formula degenerates to

$$
m^{(s)} = \mu_0\bigl(l+\tfrac12\bigr)\bigl(\dot l+\tfrac12\bigr),
\qquad s=|l-\dot l| ,
$$

which is the companion mass formula; in degree form it is $m^{(s)}=\frac{\mu_0}{4}\deg\tau^{l\dot l}$. The present article's contribution is the equations and the chains; the companion's is the spectrum and the assignments, and the two are not repeated against each other.

## The Bivector Space R6

### The Metric Mapping

Minkowski space and the space of bivectors are related by the algebraic mapping

$$
g_{ab} \longrightarrow g_{\alpha\beta\gamma\delta} \equiv g_{\alpha\gamma}g_{\beta\delta}-g_{\alpha\delta}g_{\beta\gamma},
$$

which sends the metric of $\mathbb{R}^{1,3}$ to a metric on the six-dimensional space of antisymmetric two-tensors. The programme's Minkowski metric is $\mathrm{diag}(-1,-1,-1,+1)$, and the printed bivector metric is

$$
g_{ab} = \mathrm{diag}(-1,-1,-1,+1,+1,+1),
$$

with the collective-index order

$$
23\to0,\qquad 10\to1,\qquad 20\to2,\qquad 30\to3,\qquad 31\to4,\qquad 12\to5 .
$$

The signature $(3,3)$ is the signature of the Lorentz group's parameter space: three directions belong to the boosts and three to the rotations, and the split is the split between the non-compact and the compact generators. The space is also isometric to $\mathbb{C}^3$, the three-dimensional complex space, which is why the programme calls it "a parameter space of the Lorentz group".

**A convention issue, recorded.** Evaluating the mapping componentwise for the printed index order under the corpus's conventions does not reproduce the printed diagonal. With $g=\mathrm{diag}(-1,-1,-1,+1)$ and the pairs $23,10,20,30,31,12$, the componentwise values are

$$
23\mapsto-1,\quad 10\mapsto+1,\quad 20\mapsto+1,\quad 30\mapsto-1,\quad 31\mapsto-1,\quad 12\mapsto+1,
$$

i.e. a diagonal $(-1,+1,+1,-1,-1,+1)$, while the printed metric is $(-1,-1,-1,+1,+1,+1)$: the two agree on the pairs $23$ and $12$ and differ on the four pairs that mix the timelike direction with a spacelike one. Either the printed metric uses a different index ordering or sign convention, or one of the two printed forms carries a slip. The $(3,3)$ signature is common to both; the component-by-component signs are not settled here and the article records the metric as **transcribed, with this discrepancy flagged** rather than silently reconciling it.

### The equations in R6

Mapping the wave equations into $\mathbb{R}^6$ turns the four spacetime derivatives into the six bivector derivatives. With $\Lambda^{l\dot l}_j$ the generators, $a_j$ the three complex coordinates ($a_1,a_2,a_3$), $g_4=ia_1$, $g_5=ia_2$, $g_6=ia_3$ and $\tilde a_j$ the dual coordinates, the equations for the field and its conjugate become

$$
\sum_{j=1}^{3}\Bigl(\Lambda^{l}_j\otimes\mathbf{1}_{2\dot l+1}-\mathbf{1}_{2l+1}\otimes\Lambda^{\dot l}_j\Bigr)\frac{\partial\psi}{\partial a_j}
+i\sum_{j=1}^{3}\Bigl(\Lambda^{l}_j\otimes\mathbf{1}_{2\dot l+1}-\mathbf{1}_{2l+1}\otimes\Lambda^{\dot l}_j\Bigr)^{*}\frac{\partial\psi}{\partial a_j^{*}}+m\psi = 0,
$$

together with the conjugate equation for $\dot\psi$. The equations are defined in the three-dimensional complex space $\mathbb{C}^3$, which is isometric to $\mathbb{R}^6$; the generalised spin is $s=|l-\dot l|$ and the mass is $m$, exactly as in Minkowski space. The passage to $\mathbb{C}^3\cong\mathbb{R}^6$ is the programme's way of writing the spinor structure's own wave equations, and the structure of the equations — a difference of two tensor-product generators contracted with a derivative — is the structure that will become the Dirac equation's gamma matrices at the first chain member.

## The Proton Chain and the Dirac Limit

The chain that carries the nucleon is the spin-$\frac12$ line's Fermi-scheme chain

$$
\Bigl(\tfrac12,0\Bigr)\longleftrightarrow\Bigl(0,\tfrac12\Bigr)
\ \longrightarrow\
\Bigl(1,\tfrac12\Bigr)\longleftrightarrow\Bigl(\tfrac12,1\Bigr)
\ \longrightarrow\ \cdots\ \longrightarrow\
\Bigl(\tfrac{59}{2},29\Bigr)\longleftrightarrow\Bigl(29,\tfrac{59}{2}\Bigr)\ \longrightarrow\ \cdots
$$

The first member is the **fundamental doublet**: the representation $\tau^{\frac12,0}\oplus\tau^{0,\frac12}$, a linear superposition of the two spin states $\pm\frac12$, which is the **electron** and satisfies the Dirac equation

$$
\gamma^{\mu}\frac{\partial\psi}{\partial x^{\mu}}+m_e\psi = 0 .
$$

Mapping the Dirac equation into $\mathbb{R}^6$ gives generators $\Lambda^{1/2,0}_j$ and $\Lambda^{*\,0,1/2}_j$ whose explicit matrices — built from $\mathbf{1}$ and the companion $2\times2$ block — coincide with the **Pauli matrices** $\sigma_j$ when their normalisation constant takes the value $c_{\frac12,\frac12}=2$. This is the concrete way in which the algebra's first member is the Dirac equation's carrier, and it is the same statement the corpus makes in its Dirac–Hestenes and bispinor articles.

The nucleon sits on the same chain, but far up it: the programme takes the chain member

$$
\tau^{\frac{59}{2},29}\oplus\tau^{29,\frac{59}{2}},
\qquad\text{degree } 60\times59 = 3540,
$$

as the proton, because the mass ratio fixes it. The rule is the mass formula: normalising so that the electron's fundamental representation gives $m_e=\mu_0/2$, the ratio is

$$
\frac{m_p}{m_e} = \frac{(2l+1)(2\dot l+1)}{2},
$$

and $(59/2,29)$ gives $60\times59/2=1770$. The programme's own text states the condition as $(l+\frac12)(\dot l+\frac12)\approx1800$, which is loose by a factor two — $(l+\frac12)(\dot l+\frac12)=30\times29.5=885$ — and corresponds to the normalisation $m_e=\mu_0$ rather than the $m_e=\mu_0/2$ that its own ratios require (the same factor-two slip recorded in the companion article's context). In the correct normalisation $m_p/m_e=1770$, $3.6\%$ below the measured $1836$. The proton's wave equation in $\mathbb{R}^6$ is then the $3540$-component version of the equations above, with $\Lambda^{59/2,29}_j$ replacing $\Lambda^{1/2,0}_j$. The programme's reason for not keeping the electron's chain — that the chain $(\frac12,0)\leftrightarrow(0,\frac12)$ is algebraically too simple to describe the proton's internal structure — is recorded, and the replacement of the simple chain by the high member is recorded as a **choice**, not a derivation.

## The Biquaternion Reading

Three points connect this material to the framework, and only the first is an identification.

First, the **fundamental doublet's factor** is the biquaternion algebra. The tensor product with $k$ factors of $\mathbb{C}^2$ and $r$ of $\bar{\mathbb{C}}^2$ begins at $k=r=1$, and $\mathbb{C}^2$ is the defining module of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{C l}_2\cong M_2(\mathbb{C})$. The chain of algebras the programme writes for the spin-0 line,

$$
\mathbb{C}_0\longrightarrow \mathbb{C}_2\otimes\bar{\mathbb{C}}_2\longrightarrow \mathbb{C}_2\otimes\bar{\mathbb{C}}_2\otimes\mathbb{C}_2\otimes\bar{\mathbb{C}}_2\longrightarrow\cdots,
$$

is thus a chain whose second member is the biquaternion algebra, and the first member is the centre. The corpus's *Higher Spin from Tensor Products* and *Clifford Structure of the Biquaternion Algebra* are the framework's statements of the same nesting; the present chain is the spinor-structure programme's version. One caution: the programme writes "$\mathbb{C}^2$ and complex conjugate $\bar{\mathbb{C}}^2$ are biquaternion algebras", which conflates the algebra with its module. $\mathbb{C}^2$ is the two-dimensional complex vector space on which $\mathbb{B}\cong M_2(\mathbb{C})$ acts; the algebra is the matrix algebra, and the tensor products of the chain are tensor products of **modules** until an algebra structure is imposed. The article keeps the distinction.

Second, the **bivector space** is the corpus's field-strength space. The six-dimensional space of antisymmetric two-tensors is, under the Hodge decomposition, the pair of a vector and an axial vector, and in the corpus's notation it is the field-strength biquaternion $\mathbf{E}+i\mathbf{B}$ with six real components. The mapping $g_{ab}\to g_{\alpha\beta\gamma\delta}$ is the metric structure the corpus's *Field-Strength Biquaternion and Its Invariants* meets when it classifies a field by its two invariants; and the programme's $\mathbb{C}^3\cong\mathbb{R}^6$ is the complex form in which the corpus's $\mathbf{B}$ and $\mathbf{E}$ are two vectors of one complex space. This is a genuine agreement of objects, and the article records it as one.

Third, the **equations** themselves are the corpus's Dirac-Maxwell package in the programme's form. The Dirac limit's generators reduce to the Pauli matrices; the massless limit of the equations is the Maxwell field in spinor form, which is the content of the corpus's *Bispinor Fields* and *Dirac–Hestenes* articles. The higher chain members are the multi-mass generalisations, and they lie outside $\mathbb{B}$ exactly as the companion articles say.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The spintensor degree $\dim\mathrm{Sym}^{(k,r)}=(k+1)(r+1)$ equals the representation degree $(2l+1)(2\dot l+1)$ at $l=k/2$, $\dot l=r/2$; for the proton's chain member $60\times59=3540$. Confirmed in the companion verification.
- The determinant factorisation $D(p)=\tilde D(s^2)$, the relation $m_i=\mu_0\lambda_i$ (and $m_i=\mu_0\lambda_i\dot\lambda_i$ for $\tau^{l\dot l}$), and the $\pm$ pairing of the eigenvalues of $\Gamma^0$; reproduced in outline.
- The bivector metric's $(3,3)$ signature, matching the six-dimensional Lorentz parameter space's boost/rotation split.
- The Dirac-limit generators reducing to the Pauli matrices at $c_{\frac12,\frac12}=2$; reproduced from the printed matrices.

**Transcribed, not derived.**

- The wave equations in Minkowski space and their images in $\mathbb{R}^6\cong\mathbb{C}^3$.
- The interlocking schemes and the assignment of the proton to the chain member $(59/2,29)$.
- The printed bivector metric and its index order.

**Gap, left visible.**

- The printed bivector metric is not reproduced componentwise by the stated mapping; recorded as a discrepancy, not resolved.
- The passage from the abstract chain to a physical particle remains a choice fixed by the mass ratio.
- The infinite-dimensional limit is used to state the mass formula, while the chains used are finite-dimensional; the same weakness as the companion mass article.
- The Dirac–Maxwell relation is cited as known and not re-derived here; the corpus has its own versions.

## Open Questions

1. **The bivector metric.** Is the printed $\mathrm{diag}(-1,-1,-1,+1,+1,+1)$ the componentwise image of the Minkowski metric under some other index order or sign convention, or is it a slip? The question is small but it decides whether the bivector-space equations can be written in the corpus's own conventions without a patch.

2. **$\mathbb{C}^3$ versus $\mathbb{R}^6$ in the corpus's hands.** The corpus's field-strength biquaternion is a $\mathbb{C}^3$-valued object; the programme's bivector space is $\mathbb{R}^6$. Are the two complex structures the same — the central imaginary unit $i$ of the corpus and the $i$ of $\mathbb{C}^3$?

3. **Does the chain of algebras carry the mass spectrum?** The companion mass article orders a spin line by degree; the present chain orders the same line by algebra. Is the chain's algebra sequence ($\mathbb{C}_2, \mathbb{C}_2\otimes\bar{\mathbb{C}}_2,\dots$) the object that fixes which chain members are physical?

4. **The multi-mass sector.** The equations have several roots, only the leading one of which is used. Are the subleading masses physical — further particles on the same chain — and does the corpus have a reading for them?

5. **The Maxwell–Dirac package.** The corpus's *Bispinor Fields* article derives the Maxwell–Dirac solution in the corpus's form. Does the programme's massless limit coincide with it exactly, including the conventions of the axial current?

## Summary

The Bhabha–Gel'fand–Yaglom wave equations place a field in an arbitrary Lorentz representation $\tau^{l\dot l}$, carried by coefficients of symmetric spintensors of degree $(k+1)(r+1)=(2l+1)(2\dot l+1)$, and give it a matrix mass whose determinant factors in $s^2=p^2$ with roots $m_i=\mu_0\lambda_i\dot\lambda_i$. The representations are organised into interlocking chains — the Bose and Fermi schemes — and the fields of type $(l,\dot l)\oplus(\dot l,l)$ carry generalised spin $s=|l-\dot l|$. The equations can be mapped into the six-dimensional bivector space $\mathbb{R}^6\cong\mathbb{C}^3$, whose metric and index order are transcribed and whose printed form is not fully reproduced by the stated mapping. The first chain member is the electron's Dirac doublet, whose $\mathbb{R}^6$ generators reduce to the Pauli matrices at normalisation $c=2$; the nucleon is taken at the chain member $(59/2,29)$ of degree $3540$.

The framework's relation to this is the fundamental doublet's factor: $\mathbb{C}^2$ is the defining module of the biquaternion algebra, the bivector space is the corpus's field-strength space, and the equations' massless limit is the corpus's spinor Maxwell field. The higher chain members lie outside $\mathbb{B}$, and the physical assignments are choices fixed by the mass ratio.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $s_{\alpha_1\dots\alpha_k\dot\alpha_1\dots\dot\alpha_r}$ | Spintensor of the representation $\tau^{l\dot l}$ |
| $l=k/2$, $\dot l=r/2$ | Lorentz labels from the numbers of undotted/dotted indices |
| $\dim\mathrm{Sym}^{(k,r)}=(k+1)(r+1)$ | Degree of the representation |
| $s=\lvert l-\dot l\rvert$ | Generalised spin of the field type $(l,\dot l)\oplus(\dot l,l)$ |
| $\Gamma(p)$, $\Gamma^{0}$ | Momentum-contracted generator matrix and its time part |
| $D(p)=\det(\Gamma(p)+mE)$ | Determinant whose roots are the masses |
| $m_i=\mu_0\lambda_i\dot\lambda_i$ | Masses from the eigenvalues of $\Gamma^0$ |
| $g_{ab}$, collective order $23,10,20,30,31,12$ | Bivector-space metric and index order |
| $\mathbb{C}^3\cong\mathbb{R}^6$ | Complex form of the bivector space, Lorentz parameter space |
| $(59/2,29)$, degree $3540$ | The proton's chain member |

## Further Reading

- H. J. Bhabha, "Relativistic wave equations for the elementary particles," *Reviews of Modern Physics* **17** (1945) 200–216, for the finite-dimensional relativistic wave equations and their multi-mass spectra.
- I. M. Gel'fand and A. M. Yaglom, "General relativistic-invariant equations with a mass spectrum," *Zhurnal Eksperimentalnoi i Teoreticheskoi Fiziki* **18** (1948) 703–733, for the general theory of the equations with a mass spectrum.
- E. Majorana, "Teoria relativistica di particelle con momento intrinseco arbitrario," *Nuovo Cimento* **9** (1932) 335–344, for the infinite-component equation.
- I. M. Gel'fand, R. A. Minlos and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the representations, the spintensors and the interlocking schemes.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, vol. 1 (Cambridge, 1984), for the van der Waerden two-spinor formalism by which a Minkowski vector is a pair of conjugate spinors.
- A. Z. Petrov, *Einstein Spaces* (Pergamon, 1969), for the mapping of the curvature tensor into $\mathbb{R}^6$ and the classification of Einstein spaces.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the wave equations, the chains and the bivector-space reduction recorded here.
- Companion articles: *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form*; *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form*; *Bhabha Scattering in Biquaternionic Form*; *The Field-Strength Biquaternion and Its Invariants*; *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*; *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation*.
