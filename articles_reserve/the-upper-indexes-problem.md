# __The Upper-Index Problem: The Caret Rule and the Corpus__

The rule forbids one use of the caret: the frame slot. One table lists every mathematics article that still breaks it; a second records the physics screen, which is closed. The first lists 39 mathematics articles and 583 raised frame slots, the count of the first pass. The second lists the 21 physics articles that carried 48 raised frame slots when the Latin screen was run; that screen is closed now and all 48 are low.

## The Rule

*Operator and Calculus Conventions* states it in one sentence:

> A caret marks a power or a name, never a frame slot: $e^\lambda$, $2^k$ and $(-1)^k$ are powers, and $\mathrm{Cl}^i$, $K^0$, $M_4^\sigma$ and $\mathbb{B}^\sigma$ are names; a coordinate, a field component, a basis vector, a gamma and a sign symbol are written with a low index — $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$, $\varepsilon_{ijk}$ — and a contraction is written as an explicit sum with the sign vector or as the quaternionic product that carries it.

The word "name" hides two different things. The list in that sentence holds two grades, $\mathrm{Cl}^i$ and $K^0$, and two parameters, $M_4^\sigma$ and $\mathbb{B}^\sigma$. Neither is a frame slot, and neither can be tested by the word. The audit therefore separates the uses it can test from the one it cannot. It does not put the second in the rule, and it does not change the convention to admit it.

| Use | Status | Test | Examples |
|---|---|---|---|
| Power | validated | a repeated product | $2^k$, $(-1)^k$, $e^\lambda$, $2^{n}$ |
| Conjugation | validated | the adjoint, the conjugate or the reversal | $a^{*}$, $a^{\dagger}$, $a^{\natural}$ |
| Transposition | validated | the exchange of the two factors | $L^T$, $\psi^T$ |
| Frame slot | validated, low | one term chosen out of a set | $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$, $\varepsilon_{ijk}$, $Q_1$, $T_a$, $\sigma_z$ |
| Name or label | **not validated** | none: a grade, a parameter, a sector and an order are not one kind | $\mathrm{Cl}^i$, $K^0$, $M_4^\sigma$, $\mathbb{B}^\sigma$, $S^{\mathrm{c}}$, ${}^{(l)}$, ${}^{(\mathrm{adj})}$ |

A caret in the last row is neither debt nor validated. It is counted and left aside. The examples there are the ones at issue: a grade is the degree of a grading, a parameter is the argument of a construction, a sector is a physical region and an order is a term of a series, and one word cannot carry all four. No test in the corpus separates them from a frame slot, so the audit records them and does not rule on them.

A caret outside the first four rows marks a frame slot. The slot is low: $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$, $\varepsilon_{ijk}$, $T_a$, $\sigma_z$.

## The Screens

Three screens produce the tables.

- **Greek screen.** A caret on $\mu,\nu,\rho,\lambda,\kappa,\sigma,\tau$ over a base that could be a coordinate, a derivative, a component or a metric. It reads 1,514 carets in mathematics and 8 in physics one by one. It finds no frame slot, so it produces no row.
- **Latin screen.** A caret on $i,j,k,l$ over a component base: $x$, $dx$, $dq$, $\partial$, $q$, $Q$, $g$, $\pi$, $F$, $R$, $\Gamma$, $\theta$, $\omega$, $e$, $v$, $\xi$. It covers Parts III and IV of the mathematical corpus, the geometry and mechanics parts, where those letters denote components. In the second pass it covers the whole physics corpus, with the physics glyphs added: $\sigma$, $\delta$, $S$, $V$, $K$, $\Theta$, $\Lambda$, $l$, $m$, $n$, $Y$, $P$, $\varepsilon$, $w$, $\tau$ and the spinor capitals $A,B,C,D$.
- **Internal screen.** A caret on a colour or isospin index $a,b,c$ in a gauge article. It covers the whole physics corpus.

The Latin screen is then corrected by reading. The corrections are listed so the count can be reproduced:

- **9 power carets** are removed: $x^j$ in the filtration of *Regularity and the Cauchy–Riemann Operator* (7) and $x^k$ in *Clifford Analysis* (2).
- **Coframe carets** are not counted as debt. The five articles that use a dual basis write $e^i$ for the dual of $e_i$; they are listed under *The Exceptions*.
- **Carets on $R$** are kept only when $R$ is a curvature component, $R^i{}_{jk\bar l}$ or $R^{ij}$. The derived functor $R^i\Gamma$ and the grading $R^iR^j\subseteq R^{i+j}$ are removed.
- **Parts I–II, V–VI are out of scope.** There the same letters denote ring elements, powers and graded pieces: $x^i$ in a polynomial ring, $R^0\oplus R^1$, $\Gamma^n(M)$. The Latin screen applies to components, so it cannot read those parts without a separate semantic pass.

The internal screen is corrected in the same way. Nineteen articles were cleared by hand. *BRST Symmetry in Biquaternionic Form* carried 99 raised internal indices and has none; *The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form* carried 68 and has none; *Anomalies and Anomaly Cancellation in Biquaternionic Form* carried 40 and has none; *The Pion and the Chiral Lagrangian in Biquaternionic Form* carried 34 and has none; *The Gluon: An Octet Outside the Biquaternion Algebra* carried 25 and has none; *The W and Z Bosons in Biquaternionic Form* carried 24 and has none; *The Nonlinear Sigma Model in Biquaternionic Form* carried 16 and has none; *Instantons and Solitons in Biquaternionic Form* carried 11 and has none; *Lattice Gauge Theory and the Biquaternion Path Integral* carried 8 and has none; *The Theta Parameter and Strong CP in Biquaternionic Form* carried 8 and has none; *Wilson Loops in Biquaternionic Form* carried 8 and has none; *The Gauge Field Path Integral in Biquaternionic Form* carried 7 and has none; *SU(3) Representations and the Gell-Mann–Okubo Mass Formula in Biquaternionic Form* carried 6 and has none as colour indices, its mixed heights being representation slots; *The Axion and the Peccei–Quinn Mechanism in Biquaternionic Form* carried 6 and has none; *The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge* carried 6 and has none; *Custodial Symmetry and the Rho Parameter in Biquaternionic Form* carried 4 and has none; *The Schwinger–Dyson Equations and the Ward–Takahashi Identities in Biquaternionic Form* carried 4 and has none; *Non-Abelian Gauge Fields in Biquaternionic Form* carried 3 and has none; *The ADHM Construction and Biquaternion Instanton Data* carried 3 and has none. Their colour and isospin contractions are now explicit sums. The internal count was therefore 396 − 380 = 16 on the first reading; the next pass cleared those 16, and the ten articles read zero. The floor is empty.

## The State

| Corpus | Articles | Articles with issues | Issues | Greek slots |
|---|---:|---:|---:|---:|
| Physics | 403 | 0 | 0 frame slots | 0 |
| Mathematics | 2,407 | 39 | 583 frame slots, first pass | 0 |

The sixteen internal rows have left the physics table: the ten articles that carried them now read zero, and their contractions are explicit sums. The Latin screen's 21 articles and 48 slots have followed them: the colour carets of *The Electric Dipole Moment* are $G_{a\mu\nu}$, the spinor and polarization labels are low, and every contraction they fed is an explicit sum. The table that follows is the record of what the screen found, not a list of debt.

Physics has no raised frame slot on the Greek screen's letters. Its eight carets there are three integration limits $\int_0^\tau$, one exponent $(\alpha/\pi)^\lambda$, one sign label $\nabla^\sigma$, and the three specimens $e^\lambda$, $M_4^\sigma$ and $\mathbb{B}^\sigma$ in the sentence of the rule. The 48 sat on the Latin and spinor letters, which the first pass did not screen in physics; they are low now. The two $\sigma^\alpha$ carets of *Kramers Degeneracy* are gone: the article now writes $\sigma_\alpha$, and its two carets were the only ones on that letter outside the Pauli axis.

The internal class is empty in the ten articles it was built on, and the Pauli family $\sigma_x,\sigma_y,\sigma_z,\sigma_\alpha$ is empty too. What is left of the old census of about 300 is the branch labels $G^{ab}$ of *The Schwinger–Keldysh Formalism*, which are labels.

The raised names are a third population, and the audit does not rule on them: 2,891 carets at the last census, since reduced by the physics screen, listed with the other classes in *The Up and Low Proportions of the Physics Corpus*. They are neither debt nor validated, and the convention stays as it is until the corpus decides what a name is.

Mathematics splits into 19 articles and 362 slots in Part III, and 20 articles and 221 slots in Part IV. *Lagrangian and Hamiltonian Systems* alone carries 167, and the first three articles carry 262 of the 583. **This row is the first pass and is not current**: the three largest rows have collapsed — *Lagrangian and Hamiltonian Systems* carries no slot now, *Poisson Geometry* none, and *The Hamilton–Jacobi Equation and Separability* none. The 583 is a ceiling until the mathematics screen is run again, and no total across the two rows is quoted.

## Mathematics: The Articles

The table is the first pass and is kept for the record. The three largest rows have since collapsed — *Lagrangian and Hamiltonian Systems* to no slot, *Poisson Geometry* to none, *The Hamilton–Jacobi Equation and Separability* to none — so the 583 is a ceiling until the mathematics screen is run again.

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

## Physics: The Internal Class, Cleared

The ten articles of the first physics table now carry none of the 16. *Electroweak Theory* no longer writes $T^a$; its $T_a$ stands alone. The colour and isospin contractions are explicit sums, and the rows are gone rather than zeroed.

## Physics: The Latin Screen, Closed

The first pass ran the internal screen on physics and left the Latin screen to mathematics. Run on physics, the Latin screen read **48 raised frame slots in 21 articles**, and those 21 rows have now collapsed like the nine before them: no raised frame slot remains in physics. Nine rows had already collapsed at the earlier reading. The Pauli family — 63 carets in *The Jordan–Wigner Transformation*, 2 in *Kramers Degeneracy* — is now low, $\sigma_{z,k}$, $\sigma_{\pm,j}$ and $\sigma_\alpha$, and both articles carry none. The Newman–Penrose row, 49 carets, is now low too: its tetrad components read $l_a,n_a,m_a,\bar m_a$, its spinor components $o_A,o'_A,k_A$, and its contractions are explicit sums, $\sum_{a,b,c,d}C_{abcd}l_am_bl_cm_d$ for the Weyl scalars and $\sum_{A,B,C,D}\Psi_{ABCD}k_Ak_Bk_Ck_D$ for the quartic. The nine rows that led the table have collapsed as well: the gauge triplet of *The Algebrodynamical Programme* reads $N_{\nu a}$ and $L_{\mu\nu a}$ with explicit sums; the Proca polarization reads $\varepsilon_{r\mu}$; the generators of *Curved Spacetime* read $S_{cd}$ and $V_{abd}$; the contorsion, connection and curvature of *Matter Makes Space* read $K_{\mu ab}$, $\omega_{\mu ab}$ and $R_{\mu\nu ab}$; the harmonics of *The Vibrating Ellipsoid* and *Why the Multipole Tower Is Infinite* read $Y_{lm}$; the Kronecker deltas of *The Dirac Equation* read $\delta_{rs}$; the graviton polarizations read $\varepsilon_{r ij}$; and the twistor of *Twistor Theory and Biquaternions* reads $x_{A\bar A}$ and $\omega_A$. The forms that remain are the mathematics screen's, extended to the physics glyphs: the Kronecker $\delta^{rs}$; the Lorentz generators $S^{cd},S^{ab},V^{ab}$; the connection and curvature $\omega^{ab},\Lambda^{ab},R^{ab},\Theta^{ab}$; the spinor indices $\xi^\alpha,\lambda_i^\alpha,\psi_\mu{}^\alpha$; the harmonics $Y_l^m,P_n^m$; the polarization $\varepsilon^r$; the spin label $w^s$; and the stress components $T^{tk},T^{kt}$.

| # | Article | Forms | Issues |
|---:|---|---|---:|
| 1 | [Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form](../articles_physics/charge-conjugation-and-the-division-ring-in-biquaternionic-form.html) | $\xi^\alpha$ 3, $\Pi^{\bar\alpha\alpha}$ 1 | 4 |
| 2 | [The Multipole Expansion and the Quadrupole Interaction in Biquaternionic Form](../articles_physics/the-multipole-expansion-and-the-quadrupole-interaction-in-biquaternionic-form.html) | $Y_l^m$ 4 | 4 |
| 3 | [The W and Z Bosons in Biquaternionic Form](../articles_physics/the-w-and-z-bosons-in-biquaternionic-form.html) | $\varepsilon^r$ 4 | 4 |
| 4 | [Canonical Quantization of the Biquaternion Dirac Field](../articles_physics/canonical-quantization-of-the-biquaternion-dirac-field.html) | $\delta^{rs}$ 3 | 3 |
| 5 | [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](../articles_physics/exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html) | $\delta^{rs}$ 3 | 3 |
| 6 | [Linearized Gravity in Biquaternionic Form](../articles_physics/linearized-gravity-in-biquaternionic-form.html) | $S^{cd}$ 1, $S^{ab}$ 1, $V^{ab}$ 1 | 3 |
| 7 | [The Covariant Derivative and Gauge Connection in Biquaternionic Form](../articles_physics/the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) | $S^{cd}$ 1, $S^{ab}$ 1, $V^{ab}$ 1 | 3 |
| 8 | [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](../articles_physics/the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) | $S^{cd}$ 1, $S^{ab}$ 1, $V^{ab}$ 1 | 3 |
| 9 | [Harmonic Elementary Particles and the Periodic System of Atoms](../articles_physics/harmonic-elementary-particles-and-the-periodic-system-of-atoms.html) | $P_n^m$ 2 | 2 |
| 10 | [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html) | $\varepsilon^r$ 2 | 2 |
| 11 | [Maxwell's Theory on Non-Commutative Spaces and Quaternions](../articles_physics/maxwells-theory-on-non-commutative-spaces-and-quaternions.html) | $\tau^m$ 2 | 2 |
| 12 | [Møller Scattering in Biquaternionic Form](../articles_physics/moller-scattering-in-biquaternionic-form.html) | $w^s$ 2 | 2 |
| 13 | [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](../articles_physics/stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html) | $T^{tk},T^{kt}$ 2 | 2 |
| 14 | [The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | $G^a{}_\mu$ 2 | 2 |
| 15 | [The Feynman Propagator in Biquaternionic Form](../articles_physics/the-feynman-propagator-in-biquaternionic-form.html) | $\delta^{rs}$ 2 | 2 |
| 16 | [The Stueckelberg Mechanism in Biquaternionic Form](../articles_physics/the-stueckelberg-mechanism-in-biquaternionic-form.html) | $\varepsilon^r$ 2 | 2 |
| 17 | [Canonical Quantization of the Biquaternion Rarita–Schwinger Field](../articles_physics/canonical-quantization-of-the-biquaternion-rarita-schwinger-field.html) | $C^{ab}$ 1 | 1 |
| 18 | [Electromagnetism in Media — The Local Complex Structure at Work](../articles_physics/electromagnetism-in-media-the-local-complex-structure-at-work.html) | $M^\alpha$ 1 | 1 |
| 19 | [Higher Multipoles and the Field-Strength Decomposition in Biquaternionic Form](../articles_physics/higher-multipoles-and-the-field-strength-decomposition-in-biquaternionic-form.html) | $Y_l^m$ 1 | 1 |
| 20 | [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | $\psi_\mu{}^\alpha$ 1 | 1 |
| 21 | [The Spinor-Helicity Formalism and Biquaternions](../articles_physics/the-spinor-helicity-formalism-and-biquaternions.html) | $\lambda_i^\alpha$ 1 | 1 |
| | **Total (first reading)** | | **48** |

A form-by-form recount of the six rows removed in this pass finds 55 slots, not the 40 the screen had named. *Matter Makes Space* also carried $\lambda^a{}_\mu$ (3) and $K_\mu{}^{ab}$ (2), *Twistor Theory and Biquaternions* carried $\omega^A$ (7) with $\omega^{0},\omega^{1}$ (2), and the graviton article carried $\varepsilon^{s*}$ (1) beside $\varepsilon^r$. All are now low, and the dual basis of *Matter Makes Space*, written $q^A$ in the source, is renamed $\check q_A$, so no raised basis vector remains. The 48 was the sum of the rows that remained at that reading; the screen's per-row counts are lower bounds, not a census.

Four formulas carry both heights, which is the proof that the raised form is residual and not a convention:

- *Canonical Quantization of the Biquaternion Dirac Field* writes $\delta^{rs}$ three times and $\delta_{rs}$ five times.
- *Higher Multipoles and the Field-Strength Decomposition* writes $Y_l^m$ once and $Y_{lm}$ twelve times.
- *Charge Conjugation and the Division Ring* writes $\bar\xi^{\bar\alpha}=\Pi^{\bar\alpha\alpha}\xi_\alpha$: raised and low spinor indices in one formula.
- *Electromagnetism in Media* lists $M_\alpha$ and $M^\alpha$ in one table row.

The count leaves out three classes, and each is recorded rather than silently cleared:

| Class | Forms | Carets | Why it is not a frame slot |
|---|---|---:|---|
| Raised label | $G^{ab}$ 4, $Q_3^a,Q_1^b$ 2 | 6 | a branch or an involution, not a component |
| Representation | $A^i{}_k$ 11, $T^{a_1\dots}$ 2, $N_{ab}^c$ 5 | 18 | kept high by *The Exceptions* |
| Declared name and index | $\psi^{\mathrm{op}\mu}$ 8, $P^{\mathrm{fop}\mu}$ 1 | 9 | the name $\mathrm{op}$ and the component $\mu$ in one caret |

The $G^{ab}$ of *The Schwinger–Keldysh Formalism* is the branch pair, and the same formula writes $\tilde\Phi_a$ low. The $Q_3^a,Q_1^b$ of *Unitarity from Centrality* choose the identity or the natural sign on a slot. Neither is a frame slot. The $\psi^{\mathrm{op}\mu}$ is written by the convention itself, beside $p^{\mathrm{op}}$; the form joins a name and a component, and the audit records it without counting it.

## The Physics Lines

The lines are the ones the screen read in the files as they stand after the patches; they move with the text.

| Article | Lines |
|---|---|
| [Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form](../articles_physics/charge-conjugation-and-the-division-ring-in-biquaternionic-form.html) | $\xi^\alpha$ 35, 44, 108; $\Pi^{\bar\alpha\alpha}$ 149 |
| [The Multipole Expansion and the Quadrupole Interaction in Biquaternionic Form](../articles_physics/the-multipole-expansion-and-the-quadrupole-interaction-in-biquaternionic-form.html) | $Y_l^m$ 55, 61, 128, 377 |
| [The W and Z Bosons in Biquaternionic Form](../articles_physics/the-w-and-z-bosons-in-biquaternionic-form.html) | $\varepsilon^r$ 173, 284 |
| [Canonical Quantization of the Biquaternion Dirac Field](../articles_physics/canonical-quantization-of-the-biquaternion-dirac-field.html) | $\delta^{rs}$ 112 |
| [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](../articles_physics/exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html) | $\delta^{rs}$ 247, 336 |
| [Linearized Gravity in Biquaternionic Form](../articles_physics/linearized-gravity-in-biquaternionic-form.html) | $S^{cd}$ 209; $S^{ab}$ 209; $V^{ab}$ 209 |
| [The Covariant Derivative and Gauge Connection in Biquaternionic Form](../articles_physics/the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) | $S^{cd}$ 270; $S^{ab}$ 270; $V^{ab}$ 270 |
| [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](../articles_physics/the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) | $S^{cd}$ 295; $S^{ab}$ 295; $V^{ab}$ 295 |
| [Harmonic Elementary Particles and the Periodic System of Atoms](../articles_physics/harmonic-elementary-particles-and-the-periodic-system-of-atoms.html) | $P_n^m$ 88, 366 |
| [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html) | $\varepsilon^r$ 151 |
| [Maxwell's Theory on Non-Commutative Spaces and Quaternions](../articles_physics/maxwells-theory-on-non-commutative-spaces-and-quaternions.html) | $\tau^m$ 294, 356 |
| [Møller Scattering in Biquaternionic Form](../articles_physics/moller-scattering-in-biquaternionic-form.html) | $w^s$ 86 |
| [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](../articles_physics/stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html) | $T^{tk},T^{kt}$ 153 |
| [The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | $G^a{}_\mu$ 196 |
| [The Feynman Propagator in Biquaternionic Form](../articles_physics/the-feynman-propagator-in-biquaternionic-form.html) | $\delta^{rs}$ 40 |
| [The Stueckelberg Mechanism in Biquaternionic Form](../articles_physics/the-stueckelberg-mechanism-in-biquaternionic-form.html) | $\varepsilon^r$ 42 |
| [Canonical Quantization of the Biquaternion Rarita–Schwinger Field](../articles_physics/canonical-quantization-of-the-biquaternion-rarita-schwinger-field.html) | $C^{ab}$ 127 |
| [Electromagnetism in Media — The Local Complex Structure at Work](../articles_physics/electromagnetism-in-media-the-local-complex-structure-at-work.html) | $M^\alpha$ 956 |
| [Higher Multipoles and the Field-Strength Decomposition in Biquaternionic Form](../articles_physics/higher-multipoles-and-the-field-strength-decomposition-in-biquaternionic-form.html) | $Y_l^m$ 45 |
| [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | $\psi_\mu{}^\alpha$ 19 |
| [The Spinor-Helicity Formalism and Biquaternions](../articles_physics/the-spinor-helicity-formalism-and-biquaternions.html) | $\lambda_i^\alpha$ 14 |

## The Sign Labels

A sign is a subscript in the physics conventions, and the corpus raises 1,053 signed exponents. The count mixes three kinds: a name, $SO^+(1,3)$ 123, $e^\pm$ 74, $W^\pm$ 41, $\pi^\pm$ 29; a sector, $\nabla^\pm$ 109, $\Phi^\pm$ 89, $D^\pm$ 64, $\Psi^\pm$ 47, $F^\pm$ 27, $S^\pm$ 26, $N^\pm$ 22; and a grade, $\mathrm{Cl}^+$. Only the sector is debt of the sign rule, not of the caret rule. It goes low, $\nabla_\pm$, $\Phi_\pm$, $D_\pm$, and the count is left to *The Up and Low Proportions of the Physics Corpus*.

## The Exceptions

The coframe $e^i$ is the dual of $e_i$, with $e^i(e_j)=\delta^i_j$. Lowering it would collide with the frame and erase the pairing. The 20 occurrences sit in *Geometric Calculus and the Vector Derivative* (13), *Symmetric Tensors and Spherical Harmonics* (4), *Hermitian Connections and the Adjoint* (1), *Exterior Powers* (1) and *The Coboundary Operator* (1). The convention should name this exception, or the articles should rename the dual to $\epsilon^i$.

Four physics articles keep their heights because the height labels a representation: in *SU(3) Representations and the Gell-Mann–Okubo Mass Formula* the Okubo matrix $A^i{}_k$ and the tensor $T^{a_1\dots a_n}_{b_1\dots b_m}$, in *The Biquaternion Framework and the Canonical Commutation Relation* the dimensions $\mathbb{C}^k$ and $\mathbb{C}^N$, in *Bhabha Multi-Mass Wave Equations and the Bivector Space* the pair $\Lambda^l{}_j$ and $\Lambda^{\bar l}_j$, and in *Anyons and Braid Statistics in Biquaternionic Form* the fusion multiplicity $N_{ab}^c$. Lowering them would make a mixed object look Euclidean. The six occurrences counted in the SU(3) row were these same mixed heights written with the colour letters $a,b,c$; they now use the representation letters $i,k,l$, and the row leaves the table.

## The Word "Name"

The rule files the grade and the parameter under one word, and the word does not survive the test.

1. **There is no test.** Nothing separates $A^\sigma$ from $A^\mu$ except the article. The same letter $\sigma$ is a frame slot in physics, lowered to $\sigma_i$, and an involution label in mathematics, kept high.
2. **The word carries the verdict.** A caret is cleared when it is called a name, and the same caret would be debt under another word.
3. **It cannot be screened.** A regression check cannot fire on a new $Q^\sigma$, because "name" can always be claimed.
4. **It is unstable.** An earlier draft of this note lowered the specimens to $\mathrm{Cl}_i$, $K_0$ and $B^\sigma$.

Drop "name", and put nothing in its place yet. A grade, a parameter, a sector and an order are not one kind, and the audit does not adopt them. They stay unclassified until the corpus names a test that separates them from a frame slot.

## The Label Caret

A fourth kind of caret hides in the corpus, and the word "name" does not cover it: the label. *The Yang–Mills Path Integral* wrote the propagator with $p^y$ in place of the scalar, 20 times, and defined $p^y=-\sum_\mu p_\mu p_\mu$ as the momentum-space invariant.

- **It is not a power.** Nothing is raised to the $y$.
- **It is not a grade.** No grading carries the label $y$.
- **It is not a parameter.** The label does not parametrise a construction; it abbreviates a scalar.
- **It reads as a frame slot.** $y$ is the name of an axis, so $p^y$ reads as the $y$ component of $p$, which is exactly the confusion the rule forbids.

The article now writes $\Pi\equiv-\sum_\mu p_\mu p_\mu$. The rename was checked against the Proca companion: on shell $\Pi=\mu^2$, so the Proca completeness relation $\eta_{\mu\nu}+p_\mu p_\nu/\mu^2$ is $\eta_{\mu\nu}+p_\mu p_\nu/\Pi$. Off shell the two differ, and only $\Pi$ keeps the projector idempotent at every momentum; the symbols are therefore not merged.

The gate needs a rule it does not have. A scalar label written with a caret is not a power, not a conjugation and not a transposition, so it is renamed, not excused. A label that borrows an index letter is debt even when it denotes no index.

## The Next Pass

1. **The mathematics pass, again.** The table is the first pass, and its three largest rows have collapsed: *Lagrangian and Hamiltonian Systems* carries no slot now, *Poisson Geometry* none, and *The Hamilton–Jacobi Equation and Separability* none. Re-screen Parts III and IV before quoting 583.
2. **The physics pass.** Closed: the 48 slots in 21 articles are low. The colour carets, the spinor indices, the polarization labels and the harmonics were the last four families, and each contraction they fed is now written $\sum$.
3. **The internal class.** Closed: the 16 are gone, and the two gluon carets of *The Electric Dipole Moment* went low with the 48.
4. **The convention.** It is not changed in this pass. A caret on a name, a grade, a parameter or a label stays unclassified until the corpus decides what a name is, and the audit records the count meanwhile.
5. **The gate.** Screen against an explicit list of permitted forms, not against a word, and reject a scalar label that borrows an index letter.

## Further Reading

- [Operator and Calculus Conventions](../articles_physics/conventions-of-the-operators-and-the-calculus.html) — the rule, with its specimens.
- [Index, Notation and Corpus Conventions](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) — the same rule for mathematics.
- [The Up-and-Low Proportions of the Physics Corpus](the-up-and-low-proportions-of-the-physics-corpus.html) — the companion count.
