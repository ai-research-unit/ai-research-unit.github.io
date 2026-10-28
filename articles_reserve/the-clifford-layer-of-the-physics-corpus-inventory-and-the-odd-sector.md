# __The Clifford Layer of the Physics Corpus: Where It Is, and the Odd Sector It Needs__

## Introduction

The corpus states its foundational isomorphism in one line: the biquaternion algebra is the even part of the Clifford algebra of Minkowski space,

$$
\mathbb{B}\;\cong\;\mathrm{Cl}^{+}_{1,3}(\mathbb{R}).
$$

The line is a theorem. It is also a boundary. The Clifford algebra has sixteen real dimensions; the even part has eight. The other eight — the odd part, spanned by the four vectors $\gamma^\mu$ and the four trivectors — are **not** in $\mathbb{B}$. No product of even elements is odd, so no operation inside $\mathbb{B}$ can produce an odd element. The odd part is a module over $\mathbb{B}$, not a subalgebra of it.

The physics needs that module. Parity is $\gamma^0$. Charge conjugation is $i\gamma^2$. Time reversal is $\gamma^1\gamma^3$. The Dirac adjoint is $\psi^\dagger\gamma^0$. A reflection with normal $u$ is $x\mapsto-\epsilon(u)\,u\,x\,u$. Every one of these is odd. Every one is outside $\mathbb{B}$.

This article records how far the borrowing goes.

**The counts.** A scan of the 394 physics articles finds **109** that carry a Clifford marker: an indexed $\gamma$, an explicit gamma-matrix representation, a Clifford symbol $\mathrm{Cl}_{p,q}$, or the dictionary map $\mathsf{M}_4$. Of these, **50** are structural (an explicit matrix block, at least ten indexed gamma occurrences, or at least five Clifford symbols), **46** use the layer in passing, and **13** name it only. **17** write an explicit gamma-matrix representation. **52** contain $\gamma^5$ or $\gamma_5$. The borrowing reaches **9 of the 12** categories of `physics.md`.

**The sharp case.** *The Reflection and the Rotation in Biquaternionic Form* is the purest instance. Its subject is the part of the Clifford algebra that $\mathbb{B}$ does not contain, and it says so: "The odd elements are not in $\mathbb{B}$, so they have no biquaternion representative." The article is titled in biquaternionic form and its central objects are explicitly not biquaternions.

This article is an inventory. It does not propose a replacement.

## What the Layer Is

Six imports make up the layer.

| import | object | dimension | in $\mathbb{B}$? |
|---|---|---|---|
| the ambient algebra | $\mathrm{Cl}_{1,3}$ | 16 real | even part only |
| the generators | $\gamma^\mu$ | 4 odd | no |
| the pseudoscalar | $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ | grade 4, even | even, not odd |
| the chirality element | $\gamma^5=i\omega$ | grade 4, even | even, not odd |
| the reflection group | $\mathrm{Pin}(1,3)$ | odd coset of $\mathrm{Spin}$ | no |
| the dictionary map | $\mathsf{M}_4:\mathbb{B}\to\mathrm{Cl}^{+}_{1,3}$ | 8 real | isomorphism |

The even part is not the problem. $\omega$ and $\gamma^5$ are even, and the chirality projectors $\tfrac12(1\pm\gamma^5)$ are even. The problem is the first, second and fifth rows: the generators, the odd part they span, and the reflection group built from them.

The layer also imports a metric and a sign. The Clifford metric is $g=\mathrm{diag}(+1,-1,-1,-1)$ on the generators, and the Pin action carries the sign $\epsilon(u)=\pm1$ fixed by $u^2=\epsilon(u)I$. Neither is an element of $\mathbb{B}$; both are data of the Clifford algebra.

## The Odd-Sector Theorem

The obstruction is elementary and exact.

**Proposition.** Let $\mathbb{B}=\mathrm{Cl}^{+}_{1,3}$. Every element of $\mathbb{B}$ is even. The product of two even elements is even. Hence no odd element is a product of elements of $\mathbb{B}$, and no algebraic operation of $\mathbb{B}$ produces one.

*Proof.* The grading is $\mathrm{Cl}=\mathrm{Cl}^{0}\oplus\mathrm{Cl}^{1}$ with $\mathrm{Cl}^{i}\mathrm{Cl}^{j}\subseteq\mathrm{Cl}^{i+j}$. The even part is a subalgebra; the odd part is a two-sided module over it. $\mathbb{B}=\mathrm{Cl}^{0}$. $\square$

Three consequences follow, and together they are the content of this article.

- **The odd elements are not recoverable.** They are not hidden in $\mathbb{B}$ under another name. They are the other half of a larger algebra, and the isomorphism $\mathbb{B}\cong\mathrm{Cl}^{+}$ is precisely the statement that the other half is absent.
- **The operations that need them are not inner.** Parity, time reversal, charge conjugation, reflection and the Dirac adjoint are module maps. They act on the spinor module, not on $\mathbb{B}$ by left multiplication. They cannot be written as $X\mapsto UXU^{-1}$ or $X\mapsto UXU^{*}$ with $U\in\mathbb{B}$.
- **The absence is structural, not notational.** A change of basis inside $\mathbb{B}$ cannot supply an odd element. Only an enlargement of the algebra can.

The last point separates this layer from the gauge layer. The gauge articles write an external index $\mu$; the Clifford articles write an external grading. Both are outside $\mathbb{B}$, and both are removed only by changing the algebra, not by changing the notation.

## The Worked Example: *The Reflection and the Rotation*

The article is organised around the grading, and the grading is exactly the odd sector. Its imports can be listed one by one.

| import | where it occurs | what it does |
|---|---|---|
| $\mathrm{Cl}_{1,3}=\mathrm{Cl}^{+}\oplus\mathrm{Cl}^{-}$ | boxed, §*The Grading by Reflection Count* | defines the even/odd split |
| $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ | same section | identifies the algebra with the even half |
| $\gamma^0$ as frame | §*The Frame $\gamma^0$ and the Hermitian Sector* | reaches the odd part from the even part |
| $\mathsf{M}_4(\mathbb{M}_+)=\mathrm{span}\{I,\gamma^0\gamma^1,\gamma^0\gamma^2,\gamma^0\gamma^3\}$ | same section | identifies the Hermitian sector with the timelike bivectors |
| $N=\mathrm{diag}(+1,-1,-1,-1)=g$ | same section | derives the Clifford metric from the biquaternion norm |
| $\gamma^0\mathsf{M}_4(\tilde Q)\gamma^0=\mathsf{M}_4(\tilde Q^{*})$ | §*Conjugation by $\gamma^0$ Is Complex Conjugation* | makes the frame the complex conjugation |
| $\mathrm{rev}(\mathsf{M}_4(\tilde Q))=\mathsf{M}_4(\tilde Q^{\natural})$ | same section | makes Clifford reversal the quaternion conjugation |
| $\mathrm{Pin}(1,3)=\mathrm{Spin}(1,3)\cdot\{\text{unit vectors}\}$ | §*The Spaces of Rotations and of Reflections* | names the reflection group |
| $\rho(u):x\mapsto-\epsilon(u)\,u\,x\,u$ | §*One Algebra, Read Twice* | the reflection law |
| determinant table: odd $\to-1$, "in $\mathbb{B}$? no" | §*The Grading by Reflection Count* | states the obstruction in a table |

The decisive sentence is in §*One Algebra, Read Twice*:

> The odd elements are not in $\mathbb{B}$, so they have no biquaternion representative. They lie in the odd part of $\mathrm{Cl}_{1,3}$ and act on vectors by the two-sided map of the Pin group.

The article then builds the reflection group, the determinant table, the Pin action and the anti-linear case on that outside. The construction is correct. The title is not: an article in biquaternionic form whose subject is the odd part cannot be a construction inside the biquaternions.

This is the clearest single case in the corpus because the subject and the obstruction coincide. In the other articles the odd element is a tool; here it is the topic.

## The Root: The Dictionary

*The Dirac Algebra and Biquaternions — A Dictionary* is where the boundary is drawn, and it draws it correctly. It states that the gamma matrices generate $\mathrm{Cl}_{1,3}$, that the biquaternions form the even subalgebra, and that the generators themselves are not biquaternions: they are obtained from the algebra by the frame $\gamma^0$.

As a dictionary, the article is exact. As a source, it is the root of the layer: once $\mathsf{M}_4$ is fixed, the odd part is available, and the downstream articles use it. The dictionary carries 41 Clifford symbols, 88 occurrences of $\mathsf{M}_4$ and four explicit matrix blocks. The Dirac equation article, which imports the same structure, is cited by 30 physics articles.

The distinction matters for the count. A dictionary is a bridge; the problem is that the bridge became the road.

## The Odd Part in Use

The articles below use odd elements as working objects. Each entry names the object and the operation it performs.

| article | odd object | role |
|---|---|---|
| [The Reflection and the Rotation](../articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.html) | $\gamma^0$, $\gamma^\mu$, $\mathrm{Pin}$ | reflections, parity, time reversal |
| [The CPT Theorem](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) | $\gamma^0$, $i\gamma^2$, $\gamma^1\gamma^3$ | $P$, $C$, $T$ on the spinor module |
| [Charge Conjugation and the Division Ring](../articles_physics/charge-conjugation-and-the-division-ring-in-biquaternionic-form.html) | $\Pi A^{*}\Pi^{-1}$ | pseudoautomorphism of $\mathrm{Cl}_{n,m}$ |
| [Antilinear Structure and the Two Kinds of Mass](../articles_physics/antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html) | $\Pi$ | charge-conjugation pseudoautomorphism |
| [The Grading, Fermion Parity and the Two Sectors](../articles_physics/the-grading-and-fermion-parity-in-biquaternionic-form.html) | $\mathrm{Cl}^{1}$ | parity grading |
| [The Superalgebra Reading and the Odd Extension](../articles_physics/the-superalgebra-reading-and-the-odd-extension-in-biquaternionic-form.html) | $\mathrm{Cl}^{1}$ | graded commutator, odd extension |
| [Zitterbewegung](../articles_physics/zitterbewegung-in-biquaternionic-form.html) | $\gamma^0$ | the odd element with no representative |
| [The Nonlinear Dirac Equation and the Thirring Model](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | $\gamma^0$ | Dirac adjoint, spinor bilinears |
| [The Anomalous Magnetic Moment](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | $\gamma^\mu$ ($\sigma^{\mu\nu}$ is even) | the generator and its commutator |
| [The Dirac–Hestenes Equation](../articles_physics/the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html) | $\gamma^\mu$ (STA) | spacetime-algebra vectors |


Four of the admissions are explicit. The CPT article writes that the internal matrices of $C$ and $P$ "are odd Clifford elements, outside $\mathbb{B}$". Zitterbewegung writes that $\gamma^0$ "is an **odd** element of the Clifford algebra" and that "an odd element has no representation" in $\mathbb{B}$. The nonlinear Dirac article writes that the Dirac adjoint carries the odd $\gamma^0$ and the axial current carries $\gamma_5$, and that "neither is in the even subalgebra". The reflection article writes the sentence quoted above.

The corpus knows the boundary. The counts measure how often it is crossed.

### The $\gamma^5$ Users

The chirality element needs a separate note, because it is **even**: $\gamma^5=i\omega=i\gamma^0\gamma^1\gamma^2\gamma^3$ is the scalar imaginary times the product of four generators, hence grade 4 and even. It is not an odd element, and its use is not an import of the odd part. It is the use of the matrix representation and of the trace.

Fifty-two articles contain the symbol. The heaviest are:

| article | $\gamma^5$ occurrences | what is computed |
|---|---:|---|
| [The Electric Dipole Moment](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | 54 | the $CP$-odd bilinear and its form factor |
| [The Fujikawa Method](../articles_physics/the-fujikawa-method-and-the-path-integral-anomaly-in-biquaternionic-form.html) | 50 | the regulated Jacobian, $\operatorname{tr}\gamma_5\mathcal O$ |
| [Chiral Fermions](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) | 38 | the chiral projectors and the chiral connection |
| [The Chiral Condensate](../articles_physics/the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html) | 30 | the condensate and its breaking pattern |
| [Anomalies and Anomaly Cancellation](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) | 25 | the axial anomaly |
| [The Nonlinear Dirac Equation and the Thirring Model](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | 24 | the axial current |
| [The CPT Theorem](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) | 24 | the discrete operations |
| [Bosonization](../articles_physics/bosonization-in-biquaternionic-form.html) | 20 | the chiral current algebra |

The pattern is consistent: $\gamma^5$ enters where a trace over the Dirac module is taken. The trace is a property of the representation, not of $\mathbb{B}$, and it is the representation that carries the odd generators.

## The Categories

Nine of the twelve categories use the layer. Three are clean: Non Relativistic Non Quantum Theory, Relativistic Non Quantum Theory, and Thermodynamics and Statistical Mechanics.

| category | `physics.md` | articles | band 1 | band 2 | band 3 |
|---|---:|---:|---:|---:|---:|
| Biquaternion Universe | 3 | 2 | 0 | 1 | 1 |
| Biquaternion Physical Interpretation of Mathematics | 42 | 3 | 1 | 1 | 1 |
| Biquaternion Non Relativistic Quantum Theory | 187 | 4 | 0 | 4 | 0 |
| Biquaternion Non Relativistic Non Quantum Theory | 424 | 0 | 0 | 0 | 0 |
| Biquaternion Electromagnetism | 511 | 4 | 2 | 2 | 0 |
| Biquaternion Relativity | 588 | 7 | 2 | 4 | 1 |
| Biquaternion Relativistic Quantum Theory | 650 | 33 | 17 | 14 | 2 |
| Biquaternion Relativistic Non Quantum Theory | 812 | 0 | 0 | 0 | 0 |
| Biquaternion Quantum Fields | 871 | 23 | 12 | 8 | 3 |
| Biquaternion Particle Physics and Gauge Fields | 1087 | 28 | 14 | 9 | 5 |
| Biquaternion Gravity and Cosmology | 1256 | 5 | 2 | 3 | 0 |
| Biquaternion Thermodynamics and Statistical Mechanics | 1291 | 0 | 0 | 0 | 0 |

## The Articles by Category

**Band 1** is structural: an explicit gamma-matrix block, at least ten indexed gamma occurrences, or at least five Clifford symbols. **Band 2** uses the layer in passing: three to nine indexed gammas, or one to four Clifford symbols. **Band 3** names it once or twice.

### Band 1 — structural

| article | category | subsection | $\gamma^0$ | $\gamma^\mu$ | $\gamma^5$ | matrices | $\mathrm{Cl}$ |
|---|---|---|---:|---:|---:|---:|---:|
| [The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge](../articles_physics/the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html) | Physical Interpretation of Mathematics | Algebra | 0 | 0 | 3 | 0 | 19 |
| [Subluminal and Superluminal Electromagnetic Waves in Biquaternionic Form](../articles_physics/subluminal-and-superluminal-electromagnetic-waves-and-the-lepton-mass-spectrum.html) | Electromagnetism | — | 22 | 4 | 43 | 0 | 0 |
| [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](../articles_physics/the-algebrodynamical-programme-nonlinear-cauchy-riemann-and-self-quantized-charge.html) | Electromagnetism | — | 0 | 0 | 0 | 0 | 6 |
| [The Conformal Group in Biquaternionic Form](../articles_physics/the-conformal-group-in-biquaternionic-form.html) | Relativity | — | 0 | 2 | 2 | 0 | 19 |
| [Paravectors and the Geometry of Spacetime](../articles_physics/paravectors-and-the-geometry-of-spacetime.html) | Relativity | — | 1 | 0 | 0 | 0 | 7 |
| [The Dirac Algebra and Biquaternions — A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 62 | 0 | 22 | 4 | 41 |
| [The Reflection and the Rotation in Biquaternionic Form](../articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 46 | 0 | 12 | 0 | 25 |
| [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 29 | 0 | 17 | 3 | 24 |
| [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](../articles_physics/the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 41 | 8 | 0 | 0 | 12 |
| [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1 and above | 18 | 4 | 15 | 0 | 10 |
| [The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 16 | 3 | 24 | 0 | 0 |
| [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](../articles_physics/exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 19 | 0 | 18 | 1 | 0 |
| [The Foldy–Wouthuysen Transformation in Biquaternionic Form](../articles_physics/the-foldy-wouthuysen-transformation-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 21 | 0 | 10 | 0 | 0 |
| [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](../articles_physics/the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 14 | 0 | 11 | 1 | 0 |
| [Exercise: Chirality and the Weyl Spinors](../articles_physics/exercise-chirality-and-the-weyl-spinors.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 1 | 2 | 14 | 1 | 0 |
| [The Dirac Path Integral in Biquaternionic Form](../articles_physics/the-dirac-path-integral-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 0 | 2 | 1 | 0 | 8 |
| [Zitterbewegung in Biquaternionic Form](../articles_physics/zitterbewegung-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 13 | 0 | 1 | 1 | 2 |
| [The Daviau Map and the Space Clifford Formulation of the Dirac Equation](../articles_physics/the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 4 | 0 | 0 | 0 | 12 |
| [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](../articles_physics/the-gordon-decomposition-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 9 | 0 | 5 | 0 | 0 |
| [Supersymmetric Quantum Physics in the Biquaternion Framework](../articles_physics/supersymmetric-quantum-physics-in-the-biquaternion-framework.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 2 | 0 | 10 | 0 | 2 |
| [The Spinor Module in Biquaternionic Form and Its Lorentz Action](../articles_physics/the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 2 | 0 | 1 | 0 | 7 |
| [Exercise: The Non-Relativistic Limit and the Pauli Equation](../articles_physics/exercise-the-non-relativistic-limit-and-the-pauli-equation.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 5 | 0 | 0 | 1 | 1 |
| [The CPT Theorem in Biquaternionic Form](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) | Quantum Fields | Generalities | 37 | 0 | 24 | 1 | 20 |
| [The Anomalous Magnetic Moment in Biquaternionic Form](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | Quantum Fields | Particles of spin 1/2 | 14 | 9 | 0 | 1 | 0 |
| [The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form](../articles_physics/the-grading-and-fermion-parity-in-biquaternionic-form.html) | Quantum Fields | Generalities | 1 | 1 | 2 | 0 | 27 |
| [Bosonization in Biquaternionic Form](../articles_physics/bosonization-in-biquaternionic-form.html) | Quantum Fields | Generalities | 4 | 0 | 20 | 1 | 2 |
| [The Superalgebra Reading and the Odd Extension in Biquaternionic Form](../articles_physics/the-superalgebra-reading-and-the-odd-extension-in-biquaternionic-form.html) | Quantum Fields | Generalities | 6 | 1 | 0 | 0 | 19 |
| [Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form](../articles_physics/charge-conjugation-and-the-division-ring-in-biquaternionic-form.html) | Quantum Fields | Generalities | 0 | 0 | 0 | 0 | 25 |
| [The Spin–Statistics Theorem in Biquaternionic Form](../articles_physics/the-spin-statistics-theorem-in-biquaternionic-form.html) | Quantum Fields | Generalities | 19 | 0 | 0 | 0 | 2 |
| [Canonical Quantization of the Biquaternion Dirac Field](../articles_physics/canonical-quantization-of-the-biquaternion-dirac-field.html) | Quantum Fields | Particles of spin 1/2 | 15 | 0 | 1 | 0 | 0 |
| [The Quantized Dirac Field in Biquaternionic Form](../articles_physics/the-quantized-dirac-field-in-biquaternionic-form.html) | Quantum Fields | Particles of spin 1/2 | 11 | 0 | 0 | 0 | 1 |
| [The Spectral Triple of the Biquaternion Algebra](../articles_physics/the-spectral-triple-of-the-biquaternion-algebra.html) | Quantum Fields | Generalities | 0 | 0 | 3 | 0 | 8 |
| [The Wick Theorem in Biquaternionic Form](../articles_physics/the-wick-theorem-in-biquaternionic-form.html) | Quantum Fields | Generalities | 0 | 0 | 0 | 0 | 8 |
| [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](../articles_physics/fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html) | Quantum Fields | Generalities | 0 | 0 | 0 | 0 | 5 |
| [Left-Right Symmetric Fermions from Complex Split Biquaternions and Bioctonions](../articles_physics/left-right-symmetric-fermions-from-complex-split-biquaternions-and-bioctonions.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 1 | 0 | 2 | 0 | 76 |
| [The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 5 | 0 | 54 | 1 | 0 |
| [The Fujikawa Method and the Path-Integral Anomaly in Biquaternionic Form](../articles_physics/the-fujikawa-method-and-the-path-integral-anomaly-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 4 | 0 | 50 | 1 | 0 |
| [Chiral Fermions in the Biquaternion Framework](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 4 | 0 | 38 | 1 | 0 |
| [The Majorana Equation in Biquaternionic Form](../articles_physics/the-majorana-equation-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 0 | 31 | 1 | 0 | 7 |
| [The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form](../articles_physics/the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 4 | 0 | 30 | 1 | 1 |
| [Anomalies and Anomaly Cancellation in Biquaternionic Form](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 4 | 0 | 25 | 1 | 0 |
| [The Neutrino and Majorana Fermions in Biquaternionic Form](../articles_physics/the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 9 | 3 | 6 | 1 | 0 |
| [The Proton in Biquaternionic Form](../articles_physics/the-proton-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 0 | 0 | 13 | 0 | 0 |
| [Electroweak Theory under the Biquaternion Framework — A Research Agenda](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | Particle Physics and Gauge Fields | Generalities | 0 | 0 | 12 | 0 | 0 |
| [The Number of Generations and the Biquaternion Algebra](../articles_physics/the-number-of-generations-and-the-biquaternion-algebra.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 0 | 0 | 0 | 0 | 11 |
| [The Standard Model under the Biquaternion Framework — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) | Particle Physics and Gauge Fields | Generalities | 0 | 0 | 10 | 0 | 0 |
| [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) | Particle Physics and Gauge Fields | Generalities | 0 | 0 | 10 | 0 | 0 |
| [The Particle Roster of the Complex Octonionic Chain Algebra](../articles_physics/the-particle-roster-of-the-complex-octonionic-chain-algebra.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 0 | 0 | 0 | 0 | 8 |
| [Matter Makes Space — An External Construction from Quaternionic Spinors](../articles_physics/matter-makes-space-an-external-construction-from-quaternionic-spinors.html) | Gravity and Cosmology | — | 2 | 5 | 7 | 1 | 0 |
| [The Biquaternion Basis of a Unified-Field Fibre Bundle](../articles_physics/the-biquaternion-basis-of-a-unified-field-fibre-bundle.html) | Gravity and Cosmology | — | 7 | 1 | 0 | 0 | 6 |

### Band 2 — in passing

| article | category | $\gamma$ | $\gamma^5$ | $\mathrm{Cl}$ |
|---|---|---:|---:|---:|
| [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html) | Universe | 0 | 0 | 2 |
| [The Roots of a General Element: Mass, Frames and the Mass Shell](../articles_physics/the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html) | Physical Interpretation of Mathematics | 3 | 3 | 0 |
| [The Bloch Ball as the Normalised Slice of the Future Light Cone](../articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html) | Non Relativistic Quantum Theory | 0 | 0 | 1 |
| [The Born Rule from the Hermitian Form — Derivation and Comparison](../articles_physics/the-born-rule-as-a-trace-formula-derivation-and-comparison.html) | Non Relativistic Quantum Theory | 0 | 0 | 1 |
| [Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem](../articles_physics/unitarity-from-centrality-the-biquaternion-norm-preservation-theorem.html) | Non Relativistic Quantum Theory | 0 | 0 | 1 |
| [Squeezing Beyond the Biquaternion Algebra](../articles_physics/squeezing-beyond-the-biquaternion-algebra.html) | Non Relativistic Quantum Theory | 0 | 0 | 4 |
| [The Field-Strength Biquaternion and Its Invariants](../articles_physics/the-field-strength-biquaternion-and-its-invariants.html) | Electromagnetism | 5 | 0 | 0 |
| [The Lorentz Force in Biquaternion Form](../articles_physics/the-lorentz-force-in-biquaternion-form.html) | Electromagnetism | 0 | 0 | 3 |
| [Relativistic Mechanics in Biquaternionic Form](../articles_physics/relativistic-mechanics-in-biquaternionic-form.html) | Relativity | 0 | 0 | 2 |
| [The Lorentz Transformation as a Biquaternionic Rotation](../articles_physics/the-lorentz-transformation-as-a-biquaternionic-rotation.html) | Relativity | 0 | 0 | 1 |
| [The Lorentz Group in Biquaternionic Form — Structure and Representations](../articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) | Relativity | 0 | 0 | 2 |
| [The Relativistic Particle in an External Field, in Biquaternionic Form](../articles_physics/the-relativistic-particle-in-an-external-field-in-biquaternionic-form.html) | Relativity | 0 | 0 | 1 |
| [The Dirac Oscillator in Biquaternionic Form](../articles_physics/the-dirac-oscillator-in-biquaternionic-form.html) | Relativistic Quantum Theory | 9 | 0 | 0 |
| [The s-Vector Representation of the Dirac Spinor in Biquaternionic Form](../articles_physics/the-s-vector-representation-of-the-dirac-spinor-in-biquaternionic-form.html) | Relativistic Quantum Theory | 8 | 6 | 0 |
| [The Electron in Biquaternionic Form](../articles_physics/the-electron-in-biquaternionic-form.html) | Relativistic Quantum Theory | 8 | 6 | 1 |
| [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](../articles_physics/the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) | Relativistic Quantum Theory | 7 | 0 | 1 |
| [The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation](../articles_physics/the-chiral-algebra-of-biquaternions-and-the-cyclic-representation-of-the-dirac-equation.html) | Relativistic Quantum Theory | 6 | 6 | 1 |
| [Møller Scattering in Biquaternionic Form](../articles_physics/moller-scattering-in-biquaternionic-form.html) | Relativistic Quantum Theory | 5 | 0 | 0 |
| [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](../articles_physics/antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html) | Relativistic Quantum Theory | 5 | 4 | 2 |
| [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](../articles_physics/parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html) | Relativistic Quantum Theory | 3 | 0 | 4 |
| [Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form](../articles_physics/triality-and-the-ding-construction-for-the-dirac-spinor-in-biquaternionic-form.html) | Relativistic Quantum Theory | 3 | 3 | 0 |
| [The Hydrogen Atom in Biquaternionic Form — The Relativistic Case](../articles_physics/the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html) | Relativistic Quantum Theory | 3 | 1 | 2 |
| [Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation](../articles_physics/bispinor-fields-and-the-fundamental-solution-of-the-generalized-maxwell-dirac-equation.html) | Relativistic Quantum Theory | 0 | 0 | 2 |
| [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](../articles_physics/the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html) | Relativistic Quantum Theory | 0 | 0 | 1 |
| [Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin Zero and One-Half](../articles_physics/higher-spin-from-tensor-products-why-the-biquaternion-algebra-admits-only-spin-0-and-one-half.html) | Relativistic Quantum Theory | 0 | 0 | 3 |
| [The Material-Informational Split as a Superselection Structure in Biquaternionic Form](../articles_physics/the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.html) | Relativistic Quantum Theory | 0 | 0 | 1 |
| [Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form](../articles_physics/fermion-doubling-and-the-nielsen-ninomiya-theorem-in-biquaternionic-form.html) | Quantum Fields | 9 | 5 | 0 |
| [The Feynman Propagator in Biquaternionic Form](../articles_physics/the-feynman-propagator-in-biquaternionic-form.html) | Quantum Fields | 6 | 0 | 0 |
| [The Schwinger–Dyson Equations and the Ward–Takahashi Identities in Biquaternionic Form](../articles_physics/the-schwinger-dyson-equations-and-the-ward-takahashi-identities-in-biquaternionic-form.html) | Quantum Fields | 4 | 4 | 0 |
| [The Fermionic Path Integral in Biquaternionic Form](../articles_physics/the-fermionic-path-integral-in-biquaternionic-form.html) | Quantum Fields | 4 | 0 | 0 |
| [Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form](../articles_physics/dirac-matter-graphene-dirac-cones-and-topological-insulators-in-biquaternionic-form.html) | Quantum Fields | 3 | 0 | 0 |
| [The Jordan–Wigner Transformation in Biquaternionic Form](../articles_physics/the-jordan-wigner-transformation-in-biquaternionic-form.html) | Quantum Fields | 3 | 0 | 4 |
| [The Scalar Fock Space in Biquaternionic Form](../articles_physics/the-scalar-fock-space-in-biquaternionic-form.html) | Quantum Fields | 0 | 0 | 2 |
| [The Fermionic Fock Space in Biquaternionic Form](../articles_physics/the-fermionic-fock-space-in-biquaternionic-form.html) | Quantum Fields | 0 | 0 | 4 |
| [The Neutron in Biquaternionic Form](../articles_physics/the-neutron-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 7 | 7 | 0 |
| [The Pion and the Chiral Lagrangian in Biquaternionic Form](../articles_physics/the-pion-and-the-chiral-lagrangian-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 3 | 2 | 0 |
| [The Gauge Principle in Biquaternionic Form](../articles_physics/the-gauge-principle-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 2 | 2 |
| [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](../articles_physics/the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) | Particle Physics and Gauge Fields | 0 | 0 | 3 |
| [The Higgs Mechanism in Biquaternionic Form](../articles_physics/the-higgs-mechanism-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 0 | 0 | 3 |
| [The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form](../articles_physics/the-spin-mass-formula-and-the-particle-spectrum-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 0 | 0 | 1 |
| [The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form](../articles_physics/the-spin-charge-hilbert-space-and-the-su3-supermultiplets-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 0 | 0 | 3 |
| [The Gluon: An Octet Outside the Biquaternion Algebra](../articles_physics/the-gluon-an-octet-outside-the-biquaternion-algebra.html) | Particle Physics and Gauge Fields | 0 | 0 | 1 |
| [Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form](../articles_physics/gauge-redundancy-and-the-information-in-the-gauge-orbit-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 0 | 0 | 1 |
| [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](../articles_physics/torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html) | Gravity and Cosmology | 7 | 4 | 0 |
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | Gravity and Cosmology | 5 | 0 | 0 |
| [Linearized Gravity in Biquaternionic Form](../articles_physics/linearized-gravity-in-biquaternionic-form.html) | Gravity and Cosmology | 0 | 0 | 1 |

### Band 3 — named only

| article | category | $\gamma$ | $\mathrm{Cl}$ |
|---|---|---:|---:|
| [What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions](../articles_physics/what-the-biquaternion-algebra-cannot-do-a-catalogue-of-algebraic-obstructions.html) | Universe | 2 | 0 |
| [Element and Operator Representations: The Three Actions](../articles_physics/the-element-and-operator-representations.html) | Physical Interpretation of Mathematics | 0 | 0 |
| [Noether's Theorem in Biquaternionic Form](../articles_physics/noethers-theorem-in-biquaternionic-form.html) | Relativity | 2 | 0 |
| [Biquaternion Representation of Spin One Half and the Relativistic One-Electron Atom](../articles_physics/biquaternion-representation-of-spin-one-half-and-the-relativistic-one-electron-atom.html) | Relativistic Quantum Theory | 2 | 0 |
| [Bhabha Scattering in Biquaternionic Form](../articles_physics/bhabha-scattering-in-biquaternionic-form.html) | Relativistic Quantum Theory | 1 | 0 |
| [The S-Matrix in Biquaternionic Form](../articles_physics/the-s-matrix-in-biquaternionic-form.html) | Quantum Fields | 2 | 0 |
| [Canonical Quantization of the Biquaternion Rarita–Schwinger Field](../articles_physics/canonical-quantization-of-the-biquaternion-rarita-schwinger-field.html) | Quantum Fields | 2 | 0 |
| [The LSZ Reduction Formula in Biquaternionic Form](../articles_physics/the-lsz-reduction-formula-in-biquaternionic-form.html) | Quantum Fields | 1 | 0 |
| [The Index Theorem and the Zero-Mode Count in Biquaternionic Form](../articles_physics/the-index-theorem-and-the-zero-mode-count-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 0 |
| [The Theta Parameter and Strong CP in Biquaternionic Form](../articles_physics/the-theta-parameter-and-strong-cp-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 0 |
| [The W and Z Bosons in Biquaternionic Form](../articles_physics/the-w-and-z-bosons-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 0 |
| [Confinement and the Loss of Partonic Information in Biquaternionic Form](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 0 |
| [Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form](../articles_physics/bhabha-multi-mass-wave-equations-and-the-bivector-space-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 1 | 0 |

## What the Counts Do Not Say

- **They do not report a mathematical error.** The isomorphism $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ is a theorem, the dictionary is exact, and the gamma-matrix computations are correct. Nothing in the corpus is numerically wrong because of this layer.
- **They do not count every mention as a use.** Band 3 contains articles that name Clifford once, often in a comparison or a further-reading line. The working set is band 1: 50 articles.
- **They do not single out the Dirac articles.** The layer is heaviest in Relativistic Quantum Theory (33 articles, 17 in band 1), Particle Physics and Gauge Fields (28, 14) and Quantum Fields (23, 12). It is not a defect of one series.
- **They do not prescribe a replacement.** The odd part cannot be removed by notation. An article that needs parity, charge conjugation or reflection needs the odd sector, and the odd sector is not in $\mathbb{B}$.

## Conclusion

The corpus is built on two layers that are not in the algebra it names.

The first is the tensor layer: an index $\mu$, a derivative $\partial_\mu$, four components for the connection and six for the curvature. The second is the Clifford layer: a grading, four odd generators, a Pin group and a sign. The first supplies the gauge sector with an external index; the second supplies the fermion sector with an external grading. Both are outside $\mathbb{B}$, and both are used as if they were inside it.

The sharpest trace is the odd sector. $\mathbb{B}$ is the even half of $\mathrm{Cl}_{1,3}$; the physics of parity, charge conjugation and reflection lives in the other half. The articles say so, in the CPT theorem, in Zitterbewegung, and above all in *The Reflection and the Rotation*, whose subject is precisely the part that the biquaternion algebra does not contain.

**109 articles carry the layer, 50 are structural, 17 write the matrices, 52 carry $\gamma^5$, and one article is about the odd part in substance.**
