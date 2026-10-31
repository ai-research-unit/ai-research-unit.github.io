# __The Upper-Index Problem: The Caret Rule and the Corpus__

The rule forbids one use of the caret: the frame slot. Two tables list every article that breaks it in the screened range. The first lists 39 mathematics articles and 583 raised frame slots, with the forms and the count in each article. The second lists 22 physics articles and 90 raised colour or isospin indices.

## The Rule

*Operator and Calculus Conventions* states it in one sentence:

> A caret marks a power or a name, never a frame slot: $e^\lambda$, $2^k$ and $(-1)^k$ are powers, and $\mathrm{Cl}^i$, $K^0$, $M_4^\sigma$ and $\mathbb{B}^\sigma$ are names; a coordinate, a field component, a basis vector, a gamma and a sign symbol are written with a low index — $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$, $\varepsilon_{ijk}$ — and a contraction is written as an explicit sum with the sign vector or as the quaternionic product that carries it.

The word "name" hides two different things. The list in that sentence holds two grades, $\mathrm{Cl}^i$ and $K^0$, and two parameters, $M_4^\sigma$ and $\mathbb{B}^\sigma$. Neither is a name, and neither can be tested by the word. The checkable form of the rule is the table:

| Use | Test | Examples |
|---|---|---|
| Power | a repeated product | $2^k$, $(-1)^k$, $e^\lambda$ |
| Grade | the degree of a grading | $\mathrm{Cl}^i$, $\Omega^k$, $K^0$ |
| Parameter | the argument of a construction | $A^\sigma$, $M_4^\sigma$, $\mathbb{B}^\sigma$ |

A caret outside these three marks a frame slot. The slot is low: $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$, $\varepsilon_{ijk}$.

## The Screens

Three screens produce the tables.

- **Greek screen.** A caret on $\mu,\nu,\rho,\lambda,\kappa,\sigma,\tau$ over a base that could be a coordinate, a derivative, a component or a metric. It reads 1,514 carets in mathematics and 8 in physics one by one. It finds no frame slot, so it produces no row.
- **Latin screen.** A caret on $i,j,k,l$ over a component base: $x$, $dx$, $dq$, $\partial$, $q$, $Q$, $g$, $\pi$, $F$, $R$, $\Gamma$, $\theta$, $\omega$, $e$, $v$, $\xi$. It covers Parts III and IV of the mathematical corpus, the geometry and mechanics parts, where those letters denote components.
- **Internal screen.** A caret on a colour or isospin index $a,b,c$ in a gauge article. It covers the whole physics corpus.

The Latin screen is then corrected by reading. The corrections are listed so the count can be reproduced:

- **9 power carets** are removed: $x^j$ in the filtration of *Regularity and the Cauchy–Riemann Operator* (7) and $x^k$ in *Clifford Analysis* (2).
- **Coframe carets** are not counted as debt. The five articles that use a dual basis write $e^i$ for the dual of $e_i$; they are listed under *The Exceptions*.
- **Carets on $R$** are kept only when $R$ is a curvature component, $R^i{}_{jk\bar l}$ or $R^{ij}$. The derived functor $R^i\Gamma$ and the grading $R^iR^j\subseteq R^{i+j}$ are removed.
- **Parts I–II, V–VI are out of scope.** There the same letters denote ring elements, powers and graded pieces: $x^i$ in a polynomial ring, $R^0\oplus R^1$, $\Gamma^n(M)$. The Latin screen applies to components, so it cannot read those parts without a separate semantic pass.

The internal screen is corrected in the same way. Seven articles were cleared by hand. *BRST Symmetry in Biquaternionic Form* carried 99 raised internal indices and has none; *The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form* carried 68 and has none; *Anomalies and Anomaly Cancellation in Biquaternionic Form* carried 40 and has none; *The Pion and the Chiral Lagrangian in Biquaternionic Form* carried 34 and has none; *The Gluon: An Octet Outside the Biquaternion Algebra* carried 25 and has none; *The W and Z Bosons in Biquaternionic Form* carried 24 and has none; *The Nonlinear Sigma Model in Biquaternionic Form* carried 16 and has none. Their colour and isospin contractions are now explicit sums. The internal count is therefore 396 − 306 = 90, in 22 articles, not the 29 and 396 of the first reading.

## The State

| Corpus | Articles | Articles with issues | Issues | Greek slots |
|---|---:|---:|---:|---:|
| Physics | 403 | 22 | 90 internal | 0 |
| Mathematics | 2,407 | 39 | 583 frame slots | 0 |
| Total | 2,810 | 61 | 673 | 0 |

Seven rows have left the physics table since the first count: the corpus reads 29 / 396, then 28 / 297, then 27 / 229, then 25 / 155, then 22 / 90. The rows are gone rather than zeroed, and the totals follow.

Physics has no raised frame slot left. Its 8 carets on the Greek letters are three integration limits $\int_0^\tau$, one exponent $(\alpha/\pi)^\lambda$, one sign label $\nabla^\sigma$, and the three specimens $e^\lambda$, $M_4^\sigma$ and $\mathbb{B}^\sigma$ in the sentence of the rule.

Mathematics splits into 19 articles and 362 slots in Part III, and 20 articles and 221 slots in Part IV. *Lagrangian and Hamiltonian Systems* alone carries 167, and the first three articles carry 262 of the 583.

## Mathematics: The Articles

| # | Article | Part | Problems | Issues |
|---:|---|---|---|---:|
| 1 | [Lagrangian and Hamiltonian Systems](../articles_maths/lagrangian-and-hamiltonian-systems.html) | III | $dq^i$ 81, $q^i$ 66, $Q^i$ 16, $\theta^i$ 2, … | 167 |
| 2 | [Poisson Geometry](../articles_maths/poisson-geometry.html) | IV | $x^i$ 36, $\pi^{ij}$ 13, $dx^i$ 5 | 54 |
| 3 | [The Hamilton–Jacobi Equation and Separability](../articles_maths/the-hamilton-jacobi-equation-and-separability.html) | III | $q^i$ 32, $dq^i$ 6, $Q^i$ 3 | 41 |
| 4 | [The Geodesic Flow Operator](../articles_maths/the-geodesic-flow-operator.html) | IV | $\xi^k$ 16, $\Gamma^k$ 8, $dx^i$ 6, $x^k$ 6, … | 38 |
| 5 | [Smooth Manifolds and Differential Geometry](../articles_maths/smooth-manifolds-and-differential-geometry.html) | III | $x^i$ 32, $v^i$ 5 | 37 |
| 6 | [Curvature and Geodesics](../articles_maths/curvature-and-geodesics.html) | IV | $x^i$ 13, $\Gamma^k$ 6, $dx^i$ 5, $\theta^i$ 3, … | 30 |
| 7 | [Riemannian Geometry](../articles_maths/riemannian-geometry.html) | IV | $x^i$ 13, $\Gamma^k$ 6, $dx^i$ 6, $\theta^i$ 2, … | 29 |
| 8 | [Hermitian Manifolds and the Canonical Connection](../articles_maths/hermitian-manifolds-and-the-canonical-connection.html) | III | $\Gamma^i$ 17, $R^i$ 4, $\omega^i$ 1 | 22 |
| 9 | [Geometric Calculus and the Vector Derivative](../articles_maths/geometric-calculus-and-the-vector-derivative.html) | III | $x^i$ 19 | 19 |
| 10 | [The Geodesic Flow](../articles_maths/the-geodesic-flow.html) | IV | $\xi^k$ 8, $\Gamma^k$ 3, $dx^k$ 2, $g^{ij}$ 2, … | 18 |
| 11 | [Differential Forms and Stokes' Theorem](../articles_maths/differential-forms-and-stokes-theorem.html) | III | $x^j$ 9, $dx^j$ 8 | 17 |
| 12 | [The Calculus of Variations](../articles_maths/the-calculus-of-variations.html) | III | $dx^i$ 7, $\Gamma^k$ 3, $x^i$ 2 | 12 |
| 13 | [Hermitian Metrics and the Levi-Civita Connection](../articles_maths/hermitian-metrics-and-the-levi-civita-connection.html) | III | $x^j$ 6, $\Gamma^i$ 2, $dx^i$ 2 | 10 |
| 14 | [Fibre Bundles, Connections and Curvature](../articles_maths/fibre-bundles-connections-and-curvature.html) | III | $\omega^i$ 5, $\Gamma^i$ 1, $dx^k$ 1 | 7 |
| 15 | [Pseudo-Riemannian and Lorentzian Geometry](../articles_maths/pseudo-riemannian-and-lorentzian-geometry.html) | IV | $x^i$ 4, $\Gamma^k$ 2, $\theta^i$ 1 | 7 |
| 16 | [The Exterior Derivative](../articles_maths/the-exterior-derivative.html) | III | $dx^i$ 6, $x^i$ 1 | 7 |
| 17 | [Hermitian Connections and the Adjoint](../articles_maths/hermitian-connections-and-the-adjoint.html) | III | $\omega^i$ 4, $g^{ij}$ 2 | 6 |
| 18 | [Ricci Flow](../articles_maths/ricci-flow.html) | IV | $g^{ij}$ 4, $R^{ij}$ 2 | 6 |
| 19 | [Contact Geometry](../articles_maths/contact-geometry.html) | IV | $dq^i$ 5 | 5 |
| 20 | [The Adjoint of the Clifford Multiplication](../articles_maths/the-adjoint-of-the-clifford-multiplication.html) | IV | $\theta^i$ 5 | 5 |
| 21 | [The Spinor Operator](../articles_maths/the-spinor-operator.html) | IV | $v^i$ 5 | 5 |
| 22 | [Adjoints on a Clifford Module](../articles_maths/adjoints-on-a-clifford-module.html) | III | $x^i$ 4 | 4 |
| 23 | [Symplectic Geometry](../articles_maths/symplectic-geometry.html) | IV | $dq^i$ 4 | 4 |
| 24 | [The Codifferential on a Spinor Bundle](../articles_maths/the-codifferential-on-a-spinor-bundle.html) | IV | $\theta^i$ 4 | 4 |
| 25 | [Differential Operators on a Manifold](../articles_maths/differential-operators-on-a-manifold.html) | III | $x^j$ 2, $dx^j$ 1 | 3 |
| 26 | [Distributions on Surfaces, Layers, and Jump Conditions](../articles_maths/distributions-on-surfaces-layers-and-jump-conditions.html) | III | $\partial^k$ 3 | 3 |
| 27 | [Harmonic Maps](../articles_maths/harmonic-maps.html) | IV | $g^{ij}$ 3 | 3 |
| 28 | [The Adjoint of the Twistor Operator](../articles_maths/the-adjoint-of-the-twistor-operator.html) | IV | $\theta^i$ 3 | 3 |
| 29 | [The Geodesic Symmetry and Locally Symmetric Spaces](../articles_maths/the-geodesic-symmetry-and-locally-symmetric-spaces.html) | IV | $x^k$ 3 | 3 |
| 30 | [Involutions of the Twistor Operator](../articles_maths/involutions-of-the-twistor-operator.html) | IV | $\theta^i$ 2 | 2 |
| 31 | [The Covariant Derivative](../articles_maths/the-covariant-derivative.html) | III | $\Gamma^i$ 2 | 2 |
| 32 | [The Lagrange Identity and the Self-Adjoint System](../articles_maths/the-lagrange-identity-and-the-self-adjoint-system.html) | III | $dx^k$ 2 | 2 |
| 33 | [The Twistor Operator](../articles_maths/the-twistor-operator.html) | IV | $\theta^i$ 2 | 2 |
| 34 | [Differential Topology](../articles_maths/differential-topology.html) | III | $x^i$ 1 | 1 |
| 35 | [Minimal Surfaces](../articles_maths/minimal-surfaces.html) | III | $g^{ij}$ 1 | 1 |
| 36 | [The Clifford Multiplication Operator](../articles_maths/the-clifford-multiplication-operator.html) | IV | $\theta^i$ 1 | 1 |
| 37 | [The Fourier Operator](../articles_maths/the-fourier-operator.html) | III | $dx^k$ 1 | 1 |
| 38 | [The Hodge Laplacian](../articles_maths/the-hodge-laplacian.html) | IV | $dx^i$ 1 | 1 |
| 39 | [The Parallel Transport Operator](../articles_maths/the-parallel-transport-operator.html) | IV | $\Gamma^k$ 1 | 1 |
| | **Total** | | | **583** |

## Physics: The Internal Class

The columns are families. $A_\mu^a$ includes $\mathcal{A}_\mu^a$; *other* collects $\sigma^a$, $\tau^a$, $\eta^a$, $\omega^a$, $Q^a$, $J^a$ and $u^a$.

| # | Article | $A_\mu^a$ | $c^a$ | $B^a$ | $T^a$ | $\pi^a$ | $F^a$ | $f^{abc}$ | Other | Issues |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | [Instantons and Solitons in Biquaternionic Form](../articles_physics/instantons-and-solitons-in-biquaternionic-form.html) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 11 |
| 2 | [Lattice Gauge Theory and the Biquaternion Path Integral](../articles_physics/lattice-gauge-theory-and-the-biquaternion-path-integral.html) | 4 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 8 |
| 3 | [The Theta Parameter and Strong CP in Biquaternionic Form](../articles_physics/the-theta-parameter-and-strong-cp-in-biquaternionic-form.html) | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 4 | 8 |
| 4 | [Wilson Loops in Biquaternionic Form](../articles_physics/wilson-loops-in-biquaternionic-form.html) | 0 | 0 | 0 | 5 | 0 | 1 | 0 | 2 | 8 |
| 5 | [The Gauge Field Path Integral in Biquaternionic Form](../articles_physics/the-gauge-field-path-integral-in-biquaternionic-form.html) | 3 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 7 |
| 6 | [SU(3) Representations and the Gell-Mann–Okubo Mass Formula in Biquaternionic Form](../articles_physics/su3-representations-and-the-gell-mann-okubo-mass-formula-in-biquaternionic-form.html) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 6 |
| 7 | [The Axion and the Peccei–Quinn Mechanism in Biquaternionic Form](../articles_physics/the-axion-and-the-peccei-quinn-mechanism-in-biquaternionic-form.html) | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 6 |
| 8 | [The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge](../articles_physics/the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html) | 1 | 3 | 1 | 0 | 0 | 0 | 1 | 0 | 6 |
| 9 | [Custodial Symmetry and the Rho Parameter in Biquaternionic Form](../articles_physics/custodial-symmetry-and-the-rho-parameter-in-biquaternionic-form.html) | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 4 |
| 10 | [The Schwinger–Dyson Equations and the Ward–Takahashi Identities in Biquaternionic Form](../articles_physics/the-schwinger-dyson-equations-and-the-ward-takahashi-identities-in-biquaternionic-form.html) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 4 |
| 11 | [Non-Abelian Gauge Fields in Biquaternionic Form](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| 12 | [The ADHM Construction and Biquaternion Instanton Data](../articles_physics/the-adhm-construction-and-biquaternion-instanton-data.html) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 |
| 13 | [The Conformal Group in Biquaternionic Form](../articles_physics/the-conformal-group-in-biquaternionic-form.html) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| 14 | [Electroweak Theory under the Biquaternion Framework](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| 15 | [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| 16 | [The Majorana Equation in Biquaternionic Form](../articles_physics/the-majorana-equation-in-biquaternionic-form.html) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| 17 | [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](../articles_physics/torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| 18 | [Confinement and the Loss of Partonic Information in Biquaternionic Form](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| 19 | [Grand Unification and the Biquaternion Algebra Ceiling](../articles_physics/grand-unification-and-the-biquaternion-algebra-ceiling.html) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 20 | [The Particle Roster of the Complex Octonionic Chain Algebra](../articles_physics/the-particle-roster-of-the-complex-octonionic-chain-algebra.html) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| 21 | [The Renormalization Group in Biquaternionic Form](../articles_physics/the-renormalization-group-in-biquaternionic-form.html) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| 22 | [The Yang–Mills Equation in Biquaternionic Form](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| | **Total** | | | | | | | | | **90** |

One article still writes both heights in the same text: *Electroweak Theory* writes $T^a$ twice alongside $T_a$. The height there records a component, so the raised pair is residual debt of the kind the seven cleared articles carried.

## The Exceptions

The coframe $e^i$ is the dual of $e_i$, with $e^i(e_j)=\delta^i_j$. Lowering it would collide with the frame and erase the pairing. The 20 occurrences sit in *Geometric Calculus and the Vector Derivative* (13), *Symmetric Tensors and Spherical Harmonics* (4), *Hermitian Connections and the Adjoint* (1), *Exterior Powers* (1) and *The Coboundary Operator* (1). The convention should name this exception, or the articles should rename the dual to $\epsilon^i$.

Three physics rows keep their heights because the height labels a representation: the Okubo matrix $A^i{}_k$, the dimensions $\mathbb{C}^k$ and $\mathbb{C}^N$, and the Bhabha pair $\Lambda^l{}_j$ and $\Lambda^{\bar l}_j$. Lowering them would make a mixed object look Euclidean.

## The Word "Name"

The rule files the grade and the parameter under one word, and the word does not survive the test.

1. **There is no test.** Nothing separates $A^\sigma$ from $A^\mu$ except the article. The same letter $\sigma$ is a frame slot in physics, lowered to $\sigma_i$, and an involution label in mathematics, kept high.
2. **The word carries the verdict.** A caret is cleared when it is called a name, and the same caret would be debt under another word.
3. **It cannot be screened.** A regression check cannot fire on a new $Q^\sigma$, because "name" can always be claimed.
4. **It is unstable.** An earlier draft of this note lowered the specimens to $\mathrm{Cl}_i$, $K_0$ and $B^\sigma$.

Drop "name" and keep "grade" and "parameter". The convention can then list its permitted forms, and the gate can fire on everything else.

## The Label Caret

A fourth kind of caret hides in the corpus, and the word "name" does not cover it: the label. *The Yang–Mills Path Integral* wrote the propagator with $p^y$ in place of the scalar, 20 times, and defined $p^y=-\sum_\mu p_\mu p_\mu$ as the momentum-space invariant.

- **It is not a power.** Nothing is raised to the $y$.
- **It is not a grade.** No grading carries the label $y$.
- **It is not a parameter.** The label does not parametrise a construction; it abbreviates a scalar.
- **It reads as a frame slot.** $y$ is the name of an axis, so $p^y$ reads as the $y$ component of $p$, which is exactly the confusion the rule forbids.

The article now writes $\Pi\equiv-\sum_\mu p_\mu p_\mu$. The rename was checked against the Proca companion: on shell $\Pi=\mu^2$, so the Proca completeness relation $\eta_{\mu\nu}+p_\mu p_\nu/\mu^2$ is $\eta_{\mu\nu}+p_\mu p_\nu/\Pi$. Off shell the two differ, and only $\Pi$ keeps the projector idempotent at every momentum; the symbols are therefore not merged.

The gate needs a fourth rule, and it is a prohibition: a scalar label written with a caret is renamed, not excused. A caret is allowed only for a power, a grade or a parameter; a label that borrows an index letter is debt even when it denotes no index.

## The Next Pass

1. **The mathematics pass.** 583 slots in 39 articles. Start with *Lagrangian and Hamiltonian Systems* (167), *Poisson Geometry* (54) and *The Hamilton–Jacobi Equation and Separability* (41).
2. **The internal class.** Decide whether a colour or isospin index is a representation label or a component, then apply the decision to the 22 articles above.
3. **The convention.** Replace "name" with "grade" and "parameter", add the coframe and label cases, and keep the specimens high.
4. **The gate.** Screen against an explicit list of permitted forms, not against a word, and reject a scalar label that borrows an index letter.

## Further Reading

- [Operator and Calculus Conventions](../articles_physics/conventions-of-the-operators-and-the-calculus.html) — the rule, with its specimens.
- [Index, Notation and Corpus Conventions](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) — the same rule for mathematics.
- [The Up-and-Low Proportions of the Physics Corpus](the-up-and-low-proportions-of-the-physics-corpus.html) — the companion count.
