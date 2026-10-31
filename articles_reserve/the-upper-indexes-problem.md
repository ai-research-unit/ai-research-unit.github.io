# __The Upper-Index Problem: What Is Left, What Was Lowered, and the Cost of the Rest__

## Introduction

The corpus states one rule for indices in *Operator and Calculus Conventions*: a contraction is a form, never an index, and no index is raised or lowered. A component is written low. The Minkowski signs sit in the sign vector $\varepsilon$ inside the product, not in a metric that moves indices.

The rule is not yet obeyed everywhere. A scan of the 402 physics articles and the 884 articles of Part VI finds 110 physics articles and twelve Part VI articles that still write at least one raised Greek spacetime index. The gamma indices are gone: no gamma with a raised index survives in either corpus.

The remainder is not one problem. Three kinds occur, and they cost three different things to repair. In the first the superscript is a slot; in the second it is paired with a lower index; in the third it is only a label. A blind lowering is destructive for the first, wrong for the second wherever it is a contraction, and correct for the third.

Twenty-two files were repaired while this article was written. Seventeen lost their Greek upper indices, four lost numeric ones, and one moved a complex time coordinate to the $\mathbb{B}$ frame. They are listed in §*What Was Already Lowered*, and every count here is after that pass.

The examples in this article quote the offending notation. They are the object of study, not the notation of the article.

## The Screen

The count is made on the mathematics regions only, the text between single or double dollars. A superscript counts when its content is one or more spacetime letters, $\mu$, $\nu$, $\rho$, $\lambda$ or $\kappa$, with nothing else, and it sits on a component symbol. It is a **slot** when a lower index follows it immediately. It is **paired** when the same letter appears as a lower index elsewhere in the same formula; in most entries the pairing is a contraction. It is **plain** otherwise. Superscripts on a closing delimiter and on $\exp$ are excluded, and so is the exponential $e^{\lambda}$ of the matrix articles, since these are powers.

| Corpus | Articles | Superscripts | Index-like tokens | Articles with an index |
|---|---:|---:|---:|---:|
| Physics | 402 | 43,868 | 2,423 | 110 |
| Part VI mathematics | 884 | 65,868 | 73 | 12 |

The count does not include numeric components, because $x^2$ the square and $x^2$ the second component are the same string. The four physics articles that wrote only numeric time components have been lowered and no longer appear.

The screen is deliberately narrow. Thousands of superscripts that a regex would catch are not indices:

- **exponents** — $x^2$, $a^\lambda$, $e^\lambda$, and the Bessel order in $(Q/2)^\nu$;
- **parameter labels** — $\Lambda^\alpha_x$ in the signed-operator articles, $T^\alpha_{a,b}$, $a^{(\alpha)}$, and $\psi^{\mathrm{fop}}$;
- **stars, duals and inverses** — $E_\gamma^*$, $\gamma^*$, $U^{-1}$.

The Part VI numbers show why the screen matters. Its 65,868 superscripts yield 102 tokens of index shape, and only 73 of those are genuine. The rest are Bessel orders, powers and parameter labels. A mechanical scan flags 25 Part VI articles; 13 are false.

The last column of the inventory tables names the objects that carry the raised index, quoted in the form the article writes them, with the number of occurrences. At most four objects are shown; `+n more` counts the objects not shown.

## The Three Kinds

### Class A — the superscript is a slot

The object carries two indices of different kinds, and position distinguishes them: $\Lambda^\mu{}_\nu$ for a Lorentz matrix, $T^\mu{}_\nu$ for a stress tensor with one contravariant and one covariant slot, $\Gamma^\mu{}_{\nu\rho}$ for a connection, $c^\lambda{}_{\mu\rho}$ for structure constants.

Lowering both gives $\Lambda_{\mu\nu}$, and the information of which index is the row and which the column is gone. The corpus has no second slot marker, so the repair is not a relabel. It is a matrix display, a stated slot order, or the cell form $T_{ab}=L_aR_b$. This is the only class where the raised index carries structure that no lowered pair reproduces by itself.

Eleven physics articles and three Part VI articles are in this class: 326 occurrences, of which 58 in physics and 5 in mathematics are slots.

### Class B — the superscript is paired with a lower index

The raised index is paired with a lowered one in the same formula: $F_{\mu\nu}F^{\mu\nu}$, $\partial_\mu T^{\mu\nu}$, $D_\mu F^{\mu\nu}=J^\nu$, $p^\mu x_\mu$, $j^\mu=\bar\psi\gamma_\mu\psi$.

Lowering both sides is not a relabel here. The corpus reads a repeated label as a sum over the four values, and the Minkowski signs come from $\varepsilon$. The invariant is
$$
F_{\mu\nu}F^{\mu\nu}=\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu F_{\mu\nu}F_{\mu\nu},
$$
so a blind lowering produces a sixteen-term sum with no signs and a different value. The repair is the explicit sum with $\varepsilon$, the quaternionic form $\langle\tilde F,\tilde F\rangle_\natural$, or the cell product. The contraction has to be rewritten, not relettered. Not every pairing is a contraction: in the definition $\Sigma^{\mu\nu}=\tfrac{i}{2}[\gamma_\mu,\gamma_\nu]$ the lower letters only name the generators, and lowering is safe. The scan counts both, so every Class B entry has to be read.

Ninety-nine physics articles and six Part VI articles are in this class. Between them they hold 2,164 occurrences, of which 1,590 in physics and 36 in mathematics are paired. This is the bulk of the problem: imported tensor formulas that were never translated into the form language.

### Class C — the superscript is only a label

A single component is named, with no partner and no slot: $x^\mu=(ct',\vec x)$, $p^\mu=(E,\vec p)$, $A^\nu$ alone in a definition, $u^\mu$ for a four-velocity. Nothing is lost by writing the index low, because no second occurrence depends on its height. The repair is local and safe.

No physics article remains in this class: the fourteen that did are listed in §*What Was Already Lowered*. Three Part VI articles remain, with 6 occurrences, all tuple labels of the element representations, $Q_0$, $Q_1$ and $\tilde q_0$.

### Class D — not an index

The superscript is an exponent, a parameter label, a star, a dual or an inverse. No action is required, and touching these would be an error. They are outside the inventory.

| Class | Role of the superscript | Lowering is | Repair | Physics articles | Part VI articles |
|---|---|---|---|---|---|
| A | a slot | destructive | matrix, slot order, cell form | 11 | 3 |
| B | a pairing | wrong if a contraction | explicit sum with $\varepsilon$, or the form | 99 | 6 |
| C | a label | safe | local relabel | 0 | 3 |
| D | not an index | not applicable | none | excluded | excluded |

## What Was Already Lowered

The pass took the files whose raised index carries no structure: in those files no formula both raised a letter and lowered the same letter, and no raised letter was followed by a lower slot. The height is decoration there, so lowering cannot change a value. Seventeen files lost 47 occurrences: fourteen in physics, three in Part VI.

| Article | Occurrences |
|---|---:|
| [What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions](../articles_physics/what-the-biquaternion-algebra-cannot-do-a-catalogue-of-algebraic-obstructions.html) | 7 |
| [The Field-Strength Biquaternion and Its Invariants](../articles_physics/the-field-strength-biquaternion-and-its-invariants.html) | 6 |
| [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](../articles_physics/the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html) | 5 |
| [Split-Quaternion Four-Vector Element Representation](../articles_maths/split-quaternion-four-vector-element-representation.html) | 4 |
| [Complex Two-Component Element Representation](../articles_maths/complex-two-component-element-representation.html) | 4 |
| [The Neutrino and Majorana Fermions in Biquaternionic Form](../articles_physics/the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) | 3 |
| [Split-Complex Two-Component Element Representation](../articles_maths/split-complex-two-component-element-representation.html) | 3 |
| [The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form](../articles_physics/the-spin-mass-formula-and-the-particle-spectrum-in-biquaternionic-form.html) | 2 |
| [The Biquaternion Space, the Group of Involutions and the Six Subspaces](../articles_physics/the-biquaternion-space-the-group-of-involutions-and-the-six-subspaces.html) | 2 |
| [Quantum Gravity under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-gravity-under-the-biquaternion-framework-a-research-agenda.html) | 2 |
| [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](../articles_physics/parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html) | 2 |
| [Møller Scattering in Biquaternionic Form](../articles_physics/moller-scattering-in-biquaternionic-form.html) | 2 |
| [The Feynman Propagator in Biquaternionic Form](../articles_physics/the-feynman-propagator-in-biquaternionic-form.html) | 1 |
| [The Empirical Status of the Biquaternion Framework](../articles_physics/the-empirical-status-of-the-biquaternion-framework.html) | 1 |
| [Spin Entropy and the Lorentz Group in Biquaternionic Form](../articles_physics/spin-entropy-and-the-lorentz-group-in-biquaternionic-form.html) | 1 |
| [Exercise: The Electromagnetic Field of a Moving Charge](../articles_physics/exercise-the-electromagnetic-field-of-a-moving-charge.html) | 1 |
| [Exercise: Duality Rotation and the Riemann–Silberstein Vector](../articles_physics/exercise-duality-rotation-and-the-riemann-silberstein-vector.html) | 1 |

The three Part VI rows are the element representations, whose indices $Q_0$, $Q_1$, $\tilde q_0$ are tuple slots rather than spacetime events. They were lowered with the rest; if the Part VI tuple convention wants the upper form back, the change is local and the value is unaffected.

Four further physics articles wrote only numeric components, and were lowered in the same pass:

- [The Bisognano–Wichmann Theorem under the Biquaternion Framework](../articles_physics/the-bisognano-wichmann-theorem-under-the-biquaternion-framework.html) — $x^0$ to $x^3$ lowered to $x_0$ to $x_3$;
- [The Quantized Scalar Field in Biquaternionic Form](../articles_physics/the-quantized-scalar-field-in-biquaternionic-form.html) — $x^0$ and $y^0$ lowered;
- [Exercise: Chirality and the Weyl Spinors](../articles_physics/exercise-chirality-and-the-weyl-spinors.html) — $x^0$ lowered;
- [The Spin–Statistics Theorem in Biquaternionic Form](../articles_physics/the-spin-statistics-theorem-in-biquaternionic-form.html) — $x^0$ and $y^0$ lowered.

One article needed a frame change, not a lowering. [Why Complexify Spacetime?](../articles_physics/why-complexify-spacetime.html) writes $Q_t=ic_0t'$, the time coordinate of the $\mathbb{B}$ frame, and now says so in those letters. Lowering it to $x_0$ would have asserted $x_0=ct'$, which is false in that frame. The letter $R$ was not used either: $R_t$ and $R_x$ are already the right-regular matrices of *Matrix Representations Conventions*, and $Q_t$ is already the name of that coordinate there. The material position stays $\tilde R=ict'e_t+x\vec e_x+y\vec e_y+z\vec e_z$.

The pass left every file that mixes a slot or a pairing untouched. A partial lowering inside one formula would put two heights in one contraction, which is the error the rule exists to prevent.

## The Frames of the Inventory

The inventory rows now carry a Frame column. It records the frame in which the article's displays are read, taken from the article's derivative and time coordinate, and from its metric signature when it writes no derivative: $\mathbb{B}$ when the displays use $\partial/\partial Q_\mu$ or $Q_t=ict'$, $\mathbb{M}_-$ when they use $\partial/\partial x_\mu$ or $x_0=ct'$, *both* when the article writes both, and — when the raised index is a label of an algebraic element and no spacetime frame is involved. The column is a reading of the article as it stands, not a verdict that the reading is right; the *both* rows are the ones where the article has not chosen.

Ten physics articles wrote a raised Greek index and named neither frame. Each now declares one before its first display:

| Article | Frame declared |
|---|---|
| [Nonlinear Maxwell Equations in Biquaternionic Form](../articles_physics/nonlinear-maxwell-equations-in-biquaternionic-form.html) | $\mathbb{B}$ |
| [The Theta Parameter and Strong CP in Biquaternionic Form](../articles_physics/the-theta-parameter-and-strong-cp-in-biquaternionic-form.html) | $\mathbb{B}$ |
| [Maxwell's Theory on Non-Commutative Spaces and Quaternions](../articles_physics/maxwells-theory-on-non-commutative-spaces-and-quaternions.html) | $\mathbb{B}$ |
| [Canonical Quantization of the Biquaternion Graviton Field](../articles_physics/canonical-quantization-of-the-biquaternion-graviton-field.html) | $\mathbb{B}$ |
| [Electric–Magnetic Duality and the Modular Group in Biquaternionic Form](../articles_physics/electric-magnetic-duality-and-the-modular-group-in-biquaternionic-form.html) | $\mathbb{B}$ |
| [Matter Makes Space — An External Construction from Quaternionic Spinors](../articles_physics/matter-makes-space-an-external-construction-from-quaternionic-spinors.html) | $\mathbb{B}$ |
| [The Majorana Equation in Biquaternionic Form](../articles_physics/the-majorana-equation-in-biquaternionic-form.html) | $\mathbb{B}$ |
| [The Index Theorem and the Zero-Mode Count in Biquaternionic Form](../articles_physics/the-index-theorem-and-the-zero-mode-count-in-biquaternionic-form.html) | $\mathbb{B}$ |
| [The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form](../articles_physics/the-semiclassical-expansion-and-the-instanton-gas-in-biquaternionic-form.html) | $\mathbb{B}$ |
| [Dual Equivalence of the Dirac and Topologically Massive Gauge Fields](../articles_physics/dual-equivalence-of-the-dirac-and-topologically-massive-gauge-fields.html) | $\mathbb{M}_-$ |

The declarations change no index. They fix the frame in which the repair is to be read, which is the first thing a lowering pass needs and the one thing the ten articles did not supply.

The distribution is 87 $\mathbb{B}$, 19 $\mathbb{M}_-$, 7 *both* and 9 —. The frame fixes the weight but not the reading. In the 19 $\mathbb{M}_-$ rows the Clifford metric and the plain weight coincide, both $(1,-1,-1,-1)$, so a paired index lowers as a relabel under an explicit $\varepsilon$ sum. In the 87 $\mathbb{B}$ rows they differ, $g=(1,1,1,1)$ and $\varepsilon=(1,-1,-1,-1)$: a paired index there is either a $\delta$-contraction or an $\varepsilon$-contraction, and the display must say which. That is where the 1,109 $\mathbb{B}$ pairs sit, and why they are not the cheap ones.

## The Physics Inventory

After the Frame column, the columns give the total number of raised Greek indices, then how many are slots, contracted, and plain, then the objects that carry them. A row can have all three kinds. The tables are ordered by total within each class.

### Class A articles

| Article | Frame | Raised | Slot | Contracted | Plain | Objects (quoted form) |
|---|---|---:|---:|---:|---:|---:|
| [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](../articles_physics/the-algebrodynamical-programme-nonlinear-cauchy-riemann-and-self-quantized-charge.html) | $\mathbb{M}_-$ | 86 | 29 | 54 | 3 | $A^{\mu}$ (20), $\delta^{\mu}$ (13), $\varepsilon^{\rho}$ (10), $E^{\lambda}$ (7), +12 more |
| [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](../articles_physics/stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html) | $\mathbb{B}$ | 66 | 10 | 42 | 14 | $T^{\mu\nu}$ (38), $F^{\mu\nu}$ (8), $f^{\nu}$ (6), $\epsilon^{\nu}$ (3), +5 more |
| [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](../articles_physics/the-gordon-decomposition-in-biquaternionic-form.html) | $\mathbb{M}_-$ | 66 | 4 | 52 | 10 | $\sigma^{\mu\nu}$ (26), $\nabla^{\mu}$ (12), $\Sigma^{\mu\nu}$ (11), $T^{\mu\nu}$ (4), +7 more |
| [The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | $\mathbb{M}_-$ | 30 | 1 | 17 | 12 | $\sigma^{\mu\nu}$ (28), $\Gamma^{\mu}$ (2) |
| [The Trace Anomaly in Biquaternionic Form](../articles_physics/the-trace-anomaly-in-biquaternionic-form.html) | $\mathbb{B}$ | 25 | 2 | 19 | 4 | $T^{\mu}$ (22), $\partial^{\mu}$ (2), $\eta^{\mu\nu}$ (1) |
| [Radiation from Accelerated Charges in Biquaternionic Form](../articles_physics/radiation-from-accelerated-charges-in-biquaternionic-form.html) | $\mathbb{B}$ | 19 | 6 | 6 | 7 | $K^{\mu}$ (7), $du^{\nu}$ (5), $d^{\mu}$ (3), $u^{\mu}$ (3), +1 more |
| [The Lorentz Transformation as a Biquaternionic Rotation](../articles_physics/the-lorentz-transformation-as-a-biquaternionic-rotation.html) | $\mathbb{B}$ | 11 | 1 | 1 | 9 | $L^{\mu}$ (3), $E^{\mu}$ (2), $q^{\mu}$ (2), $F^{\mu\nu}$ (1), +3 more |
| [Bosonization in Biquaternionic Form](../articles_physics/bosonization-in-biquaternionic-form.html) | $\mathbb{B}$ | 7 | 2 | 4 | 1 | $\epsilon^{\mu\nu}$ (4), $j^{\mu}$ (2), $T^{\mu}$ (1) |
| [Hawking Radiation in Biquaternionic Form](../articles_physics/hawking-radiation-in-biquaternionic-form.html) | $\mathbb{B}$ | 5 | 1 | 4 | 0 | $v^{\mu}$ (2), $\chi^{\nu}$ (1), $\delta^{\mu}$ (1), $\nabla^{\mu}$ (1) |
| [The Axion and the Peccei–Quinn Mechanism in Biquaternionic Form](../articles_physics/the-axion-and-the-peccei-quinn-mechanism-in-biquaternionic-form.html) | $\mathbb{B}$ | 5 | 1 | 3 | 1 | $K^{\mu}$ (3), $F^{\mu\nu}$ (1), $j^{\mu}$ (1) |
| [The Functional Determinant in Biquaternionic Form](../articles_physics/the-functional-determinant-in-biquaternionic-form.html) | both | 1 | 1 | 0 | 0 | $T^{\mu}$ (1) |

### Class B articles

| Article | Frame | Raised | Slot | Contracted | Plain | Objects (quoted form) |
|---|---|---:|---:|---:|---:|---:|
| [The s-Vector Representation of the Dirac Spinor in Biquaternionic Form](../articles_physics/the-s-vector-representation-of-the-dirac-spinor-in-biquaternionic-form.html) | $\mathbb{B}$ | 176 | 0 | 102 | 74 | $c^{\mu\nu\lambda}$ (33), $k^{\mu}$ (23), $G^{\mu}$ (21), $B^{\mu}$ (15), +16 more |
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | both | 149 | 0 | 98 | 51 | $E^{\mu}$ (41), $x^{\mu}$ (37), $e^{\mu}$ (13), $n^{\mu}$ (10), +15 more |
| [Exercise: The Electromagnetic Energy–Momentum Tensor](../articles_physics/exercise-the-electromagnetic-energy-momentum-tensor.html) | $\mathbb{B}$ | 123 | 0 | 68 | 55 | $T^{\mu\nu}$ (84), $k^{\mu}$ (12), $f^{\nu}$ (10), $Q^{\mu}$ (4), +7 more |
| [Linearized Gravity in Biquaternionic Form](../articles_physics/linearized-gravity-in-biquaternionic-form.html) | $\mathbb{M}_-$ | 122 | 0 | 87 | 35 | $x^{\mu}$ (67), $\eta^{\mu\nu}$ (14), $\varepsilon^{\nu}$ (11), $\partial^{\lambda}$ (10), +7 more |
| [The Classical Spinning Particle: The Bargmann–Michel–Telegdi Equation in Biquaternionic Form](../articles_physics/the-classical-spinning-particle-the-bargmann-michel-telegdi-equation-in-biquaternionic-form.html) | $\mathbb{B}$ | 94 | 0 | 65 | 29 | $v^{\mu}$ (33), $F^{\mu\nu}$ (32), $S^{\mu}$ (12), $dS^{\mu}$ (11), +3 more |
| [The Yang–Mills Equation in Biquaternionic Form](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html) | $\mathbb{B}$ | 82 | 0 | 72 | 10 | $F^{\mu\nu}$ (48), $J^{\nu}$ (28), $L^{\mu\nu}$ (2), $\partial^{\mu}$ (2), +1 more |
| [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | both | 57 | 0 | 45 | 12 | $x^{\rho}$ (29), $e^{\mu}$ (14), $\partial^{\mu}$ (9), $\Gamma^{\mu\nu}$ (3), +2 more |
| [Matter Makes Space — An External Construction from Quaternionic Spinors](../articles_physics/matter-makes-space-an-external-construction-from-quaternionic-spinors.html) | $\mathbb{B}$ | 56 | 0 | 23 | 33 | $q^{\mu}$ (20), $T^{\rho}$ (12), $J^{\mu}$ (6), $\delta^{\mu\nu}$ (4), +7 more |
| [Noether's Theorem in Biquaternionic Form](../articles_physics/noethers-theorem-in-biquaternionic-form.html) | $\mathbb{B}$ | 49 | 0 | 15 | 34 | $p^{\mu}$ (11), $T^{\mu}$ (10), $L^{\mu\nu}$ (7), $J^{\nu}$ (6), +7 more |
| [The Anomalous Magnetic Moment in Biquaternionic Form](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | $\mathbb{B}$ | 49 | 0 | 30 | 19 | $\sigma^{\mu\nu}$ (22), $S^{\mu\rho}$ (13), $\Gamma^{\mu}$ (7), $g^{\mu\nu}$ (6), +1 more |
| [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](../articles_physics/torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html) | $\mathbb{M}_-$ | 49 | 0 | 13 | 36 | $\Gamma^{\lambda}$ (10), $K^{\lambda}$ (9), $e^{\lambda}$ (9), $T^{\lambda}$ (5), +7 more |
| [Maxwell's Theory on Non-Commutative Spaces and Quaternions](../articles_physics/maxwells-theory-on-non-commutative-spaces-and-quaternions.html) | $\mathbb{B}$ | 48 | 0 | 14 | 34 | $\theta^{\mu\nu}$ (17), $x^{\mu}$ (16), $\tau^{\mu}$ (5), $\epsilon^{\mu\nu}$ (4), +4 more |
| [The Gauge Field Path Integral in Biquaternionic Form](../articles_physics/the-gauge-field-path-integral-in-biquaternionic-form.html) | $\mathbb{B}$ | 48 | 0 | 34 | 14 | $p^{\mu}$ (12), $J^{\mu}$ (11), $j^{\nu}$ (8), $K^{\mu\nu}$ (4), +6 more |
| [Gravitational Waves in Biquaternionic Form](../articles_physics/gravitational-waves-in-biquaternionic-form.html) | $\mathbb{B}$ | 42 | 0 | 33 | 9 | $\partial^{\lambda}$ (11), $\eta^{\mu\nu}$ (9), $k^{\mu}$ (8), $x^{\mu}$ (6), +2 more |
| [Wilson Loops in Biquaternionic Form](../articles_physics/wilson-loops-in-biquaternionic-form.html) | $\mathbb{B}$ | 42 | 0 | 36 | 6 | $dx^{\mu}$ (29), $\Sigma^{\mu\nu}$ (9), $J^{\mu}$ (2), $dy^{\nu}$ (2) |
| [Canonical Quantization of the Biquaternion Rarita–Schwinger Field](../articles_physics/canonical-quantization-of-the-biquaternion-rarita-schwinger-field.html) | $\mathbb{M}_-$ | 40 | 0 | 35 | 5 | $p^{\mu}$ (15), $P^{\mu\nu}$ (13), $x^{\mu}$ (9), $\pi^{\mu}$ (3) |
| [The Conformal Group in Biquaternionic Form](../articles_physics/the-conformal-group-in-biquaternionic-form.html) | $\mathbb{B}$ | 40 | 0 | 20 | 20 | $x^{\mu}$ (29), $a^{\mu}$ (7), $\Lambda^{\mu}$ (2), $\eta^{\mu}$ (2) |
| [The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form](../articles_physics/the-yang-mills-path-integral-and-the-faddeev-popov-procedure-in-biquaternionic-form.html) | $\mathbb{B}$ | 39 | 0 | 39 | 0 | $J^{\nu}$ (12), $F^{\mu\nu}$ (11), $D^{\mu}$ (6), $p^{\mu}$ (6), +2 more |
| [Dual Equivalence of the Dirac and Topologically Massive Gauge Fields](../articles_physics/dual-equivalence-of-the-dirac-and-topologically-massive-gauge-fields.html) | $\mathbb{M}_-$ | 38 | 0 | 23 | 15 | $\varepsilon^{\mu\nu\lambda\rho}$ (11), $c^{\nu\mu\lambda}$ (9), $B^{\mu\nu}$ (4), $H^{\mu\nu}$ (4), +5 more |
| [Conformal Invariance and the Massless Limit in Biquaternionic Form](../articles_physics/conformal-invariance-and-the-massless-limit-in-biquaternionic-form.html) | $\mathbb{B}$ | 37 | 0 | 31 | 6 | $\Theta^{\mu}$ (15), $x^{\nu}$ (9), $T^{\mu}$ (3), $D^{\mu}$ (2), +6 more |
| [Canonical Quantization of the Biquaternion Proca Field](../articles_physics/canonical-quantization-of-the-biquaternion-proca-field.html) | $\mathbb{B}$ | 34 | 0 | 26 | 8 | $p^{\nu}$ (11), $A^{\mu}$ (6), $F^{\mu\nu}$ (6), $\pi^{\mu}$ (5), +3 more |
| [Instantons and Solitons in Biquaternionic Form](../articles_physics/instantons-and-solitons-in-biquaternionic-form.html) | $\mathbb{B}$ | 34 | 0 | 26 | 8 | $F^{\mu\nu}$ (24), $J^{\mu}$ (9), $T^{\mu\nu}$ (1) |
| [The Einstein Field Equations under the Biquaternion Framework — A Research Agenda](../articles_physics/the-einstein-field-equations-under-the-biquaternion-framework-a-research-agenda.html) | $\mathbb{B}$ | 30 | 0 | 22 | 8 | $R^{\mu\nu}$ (5), $\eta^{\mu\nu}$ (5), $s^{\mu}$ (4), $k^{\mu}$ (3), +8 more |
| [Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form](../articles_physics/triality-and-the-ding-construction-for-the-dirac-spinor-in-biquaternionic-form.html) | $\mathbb{M}_-$ | 29 | 0 | 13 | 16 | $B^{\mu}$ (7), $N^{\mu}$ (5), $\varepsilon^{\nu\mu\lambda}$ (5), $t^{\nu\mu\lambda}$ (5), +3 more |
| [The Majorana Equation in Biquaternionic Form](../articles_physics/the-majorana-equation-in-biquaternionic-form.html) | both | 28 | 0 | 16 | 12 | $\sigma^{\mu}$ (19), $r^{\mu}$ (5), $\eta^{\mu\nu}$ (4) |
| [Relativistic Mechanics in Biquaternionic Form](../articles_physics/relativistic-mechanics-in-biquaternionic-form.html) | $\mathbb{B}$ | 27 | 0 | 15 | 12 | $T^{\nu\mu}$ (8), $V^{\nu}$ (5), $G^{\mu}$ (3), $J^{\nu}$ (3), +5 more |
| [The Dirac Path Integral in Biquaternionic Form](../articles_physics/the-dirac-path-integral-in-biquaternionic-form.html) | $\mathbb{B}$ | 27 | 0 | 17 | 10 | $dx^{\mu}$ (10), $\psi^{\mu}$ (9), $F^{\mu\nu}$ (4), $g^{\mu\nu}$ (3), +1 more |
| [The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | $\mathbb{B}$ | 25 | 0 | 14 | 11 | $A^{\mu}$ (10), $V^{\mu}$ (8), $T^{\mu\nu}$ (3), $\sigma^{\mu\nu}$ (2), +2 more |
| [Maxwell's Equations in the Biquaternionic Formulation](../articles_physics/maxwells-equations-in-biquaternionic-form.html) | $\mathbb{B}$ | 23 | 0 | 3 | 20 | $A^{\mu}$ (10), $F^{\mu\nu}$ (5), $\partial^{\mu}$ (5), $J^{\mu}$ (2), +1 more |
| [The Relativistic Action and the Stationary-Action Principle in Biquaternionic Form](../articles_physics/the-relativistic-action-and-the-stationary-action-principle-in-biquaternionic-form.html) | $\mathbb{B}$ | 20 | 0 | 13 | 7 | $F^{\mu\nu}$ (6), $\partial^{\mu}$ (4), $T^{\mu}$ (3), $du^{\mu}$ (3), +3 more |
| [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](../articles_physics/the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html) | $\mathbb{B}$ | 19 | 0 | 12 | 7 | $\sigma^{\mu\nu}$ (8), $\gamma^{\mu}$ (3), $j^{\mu}$ (3), $p^{\mu}$ (2), +3 more |
| [The Lorentz Force in Biquaternion Form](../articles_physics/the-lorentz-force-in-biquaternion-form.html) | $\mathbb{M}_-$ | 19 | 0 | 11 | 8 | $F^{\mu\nu}$ (8), $K^{\mu}$ (6), $P^{\nu}$ (2), $dP^{\mu}$ (2), +1 more |
| [The Fujikawa Method and the Path-Integral Anomaly in Biquaternionic Form](../articles_physics/the-fujikawa-method-and-the-path-integral-anomaly-in-biquaternionic-form.html) | $\mathbb{M}_-$ | 18 | 0 | 13 | 5 | $\sigma^{\mu\nu}$ (9), $x^{\mu}$ (7), $j^{\mu}$ (2) |
| [Canonical Quantization of the Biquaternion Graviton Field](../articles_physics/canonical-quantization-of-the-biquaternion-graviton-field.html) | $\mathbb{B}$ | 16 | 0 | 13 | 3 | $\partial^{\mu}$ (8), $h^{\mu\nu}$ (3), $\eta^{\mu\nu}$ (2), $x^{\mu}$ (2), +1 more |
| [The Higgs Mechanism in Biquaternionic Form](../articles_physics/the-higgs-mechanism-in-biquaternionic-form.html) | $\mathbb{B}$ | 16 | 0 | 16 | 0 | $g^{\mu\nu}$ (12), $A^{\mu}$ (4) |
| [Canonical Quantization of the Biquaternion Maxwell Field](../articles_physics/canonical-quantization-of-the-biquaternion-maxwell-field.html) | $\mathbb{B}$ | 15 | 0 | 13 | 2 | $F^{\mu\nu}$ (5), $\epsilon^{\lambda}$ (4), $\pi^{\mu}$ (4), $A^{\nu}$ (1), +1 more |
| [Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form](../articles_physics/fermion-doubling-and-the-nielsen-ninomiya-theorem-in-biquaternionic-form.html) | $\mathbb{B}$ | 14 | 0 | 7 | 7 | $p^{\mu}$ (12), $\pi^{\mu}$ (1), $ap^{\mu}$ (1) |
| [The Theta Parameter and Strong CP in Biquaternionic Form](../articles_physics/the-theta-parameter-and-strong-cp-in-biquaternionic-form.html) | $\mathbb{B}$ | 14 | 0 | 11 | 3 | $F^{\mu\nu}$ (11), $J^{\mu}$ (3) |
| [The First-Order Root of the Biquaternion Klein–Gordon Operator](../articles_physics/the-first-order-root-of-the-biquaternion-klein-gordon-operator.html) | $\mathbb{B}$ | 13 | 0 | 9 | 4 | $x^{\mu}$ (7), $g^{\mu\nu}$ (3), $k^{\mu}$ (3) |
| [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) | $\mathbb{B}$ | 12 | 0 | 6 | 6 | $B^{\mu}$ (3), $K^{\mu}$ (2), $N^{\mu}$ (2), $G^{\mu}$ (1), +4 more |
| [The Relativistic Particle in an External Field, in Biquaternionic Form](../articles_physics/the-relativistic-particle-in-an-external-field-in-biquaternionic-form.html) | $\mathbb{B}$ | 12 | 0 | 9 | 3 | $F^{\mu\nu}$ (8), $dP^{\mu}$ (3), $K^{\mu}$ (1) |
| [The Schwinger–Dyson Equations and the Ward–Takahashi Identities in Biquaternionic Form](../articles_physics/the-schwinger-dyson-equations-and-the-ward-takahashi-identities-in-biquaternionic-form.html) | $\mathbb{B}$ | 12 | 0 | 11 | 1 | $j^{\mu}$ (7), $J^{\nu}$ (3), $F^{\mu\nu}$ (2) |
| [The Stueckelberg Mechanism in Biquaternionic Form](../articles_physics/the-stueckelberg-mechanism-in-biquaternionic-form.html) | $\mathbb{B}$ | 12 | 0 | 12 | 0 | $A^{\mu}$ (4), $F^{\mu\nu}$ (4), $\mu^{\mu}$ (2), $g^{\mu\nu}$ (1), +1 more |
| [Hamiltonian Field Theory in Biquaternionic Form](../articles_physics/hamiltonian-field-theory-in-biquaternionic-form.html) | $\mathbb{B}$ | 11 | 0 | 9 | 2 | $p^{\mu}$ (9), $\partial^{\mu}$ (2) |
| [Non-Abelian Gauge Fields in Biquaternionic Form](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) | $\mathbb{B}$ | 11 | 0 | 11 | 0 | $F^{\mu\nu}$ (10), $\varepsilon^{\lambda\mu\nu\rho}$ (1) |
| [The W and Z Bosons in Biquaternionic Form](../articles_physics/the-w-and-z-bosons-in-biquaternionic-form.html) | $\mathbb{B}$ | 11 | 0 | 11 | 0 | $J^{\mu}$ (3), $A^{\mu}$ (2), $F^{\mu\nu}$ (2), $B^{\mu\nu}$ (1), +3 more |
| [Lattice Gauge Theory and the Biquaternion Path Integral](../articles_physics/lattice-gauge-theory-and-the-biquaternion-path-integral.html) | $\mathbb{B}$ | 9 | 0 | 9 | 0 | $F^{\mu\nu}$ (9) |
| [The Classical Free Particle and Inertial Frames in Biquaternionic Form](../articles_physics/the-classical-free-particle-and-inertial-frames-in-biquaternionic-form.html) | $\mathbb{B}$ | 9 | 0 | 4 | 5 | $v^{\mu}$ (3), $f^{\mu}$ (2), $\Lambda^{\mu}$ (1), $dx^{\mu}$ (1), +2 more |
| [The Covariant Derivative and Gauge Connection in Biquaternionic Form](../articles_physics/the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) | $\mathbb{B}$ | 9 | 0 | 9 | 0 | $dx^{\mu}$ (9) |
| [The Unruh Effect in Biquaternionic Form](../articles_physics/the-unruh-effect-in-biquaternionic-form.html) | $\mathbb{B}$ | 9 | 0 | 3 | 6 | $\chi^{\mu}$ (9) |
| [Goldstone's Theorem in Biquaternionic Form](../articles_physics/goldstones-theorem-in-biquaternionic-form.html) | $\mathbb{B}$ | 8 | 0 | 1 | 7 | $ifp^{\mu}$ (4), $p^{\mu}$ (2), $F^{\mu}$ (1), $J^{\mu}$ (1) |
| [The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form](../articles_physics/the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html) | $\mathbb{B}$ | 8 | 0 | 8 | 0 | $j^{\mu}$ (8) |
| [The Proca Equation: Massive Spin 1 in Biquaternionic Form](../articles_physics/the-proca-equation-massive-spin-1-in-biquaternionic-form.html) | $\mathbb{B}$ | 8 | 0 | 5 | 3 | $A^{\mu}$ (5), $F^{\mu\nu}$ (3) |
| [The Spinor Representation of the Lorentz Group in Biquaternionic Form](../articles_physics/the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html) | — | 8 | 0 | 3 | 5 | $M^{\mu}$ (3), $\psi^{\rho}$ (3), $N^{\rho}$ (1), $S^{\mu}$ (1) |
| [The Berry Phase and Geometric Phases in Biquaternionic Form](../articles_physics/the-berry-phase-and-geometric-phases-in-biquaternionic-form.html) | $\mathbb{B}$ | 7 | 0 | 7 | 0 | $dR^{\mu}$ (4), $R^{\mu}$ (1), $\lambda^{\mu}$ (1), $dS^{\mu\nu}$ (1) |
| [The Theta Vacuum in Biquaternionic Form](../articles_physics/the-theta-vacuum-in-biquaternionic-form.html) | both | 7 | 0 | 7 | 0 | $F^{\mu\nu}$ (7) |
| [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html) | $\mathbb{B}$ | 6 | 0 | 6 | 0 | $\varepsilon^{\lambda\mu\nu\rho}$ (5), $F^{\mu\nu}$ (1) |
| [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](../articles_physics/the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) | $\mathbb{B}$ | 6 | 0 | 6 | 0 | $j^{\mu}$ (4), $F^{\mu\nu}$ (2) |
| [The Skyrme Model and the Topological Baryon in Biquaternionic Form](../articles_physics/the-skyrme-model-and-the-topological-baryon-in-biquaternionic-form.html) | $\mathbb{B}$ | 6 | 0 | 5 | 1 | $B^{\mu}$ (6) |
| [Anomalies and Anomaly Cancellation in Biquaternionic Form](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) | $\mathbb{B}$ | 5 | 0 | 4 | 1 | $J^{\mu}$ (3), $j^{\mu}$ (2) |
| [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](../articles_physics/exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html) | $\mathbb{M}_-$ | 5 | 0 | 1 | 4 | $S^{\mu\nu}$ (2), $x^{\mu}$ (2), $p^{\mu}$ (1) |
| [Hannay's Angles and the Classical Geometric Phase in Biquaternionic Form](../articles_physics/hannays-angles-and-the-classical-geometric-phase-in-biquaternionic-form.html) | — | 5 | 0 | 5 | 0 | $dR^{\mu}$ (5) |
| [The Gauge Principle in Biquaternionic Form](../articles_physics/the-gauge-principle-in-biquaternionic-form.html) | $\mathbb{B}$ | 5 | 0 | 5 | 0 | $dx^{\mu}$ (2), $j^{\mu}$ (2), $x^{\mu}$ (1) |
| [The Higgs Mechanism as an Erasure of Information in Biquaternionic Form](../articles_physics/the-higgs-mechanism-as-an-erasure-of-information-in-biquaternionic-form.html) | $\mathbb{B}$ | 5 | 0 | 5 | 0 | $g^{\mu\nu}$ (4), $F^{\mu\nu}$ (1) |
| [The Poincaré Group and the Biquaternion Frame](../articles_physics/the-poincare-group-and-the-biquaternion-frame.html) | $\mathbb{M}_-$ | 5 | 0 | 2 | 3 | $a^{\mu}$ (2), $x^{\mu}$ (2), $\Lambda^{\mu}$ (1) |
| [BRST Symmetry in Biquaternionic Form](../articles_physics/brst-symmetry-in-biquaternionic-form.html) | $\mathbb{B}$ | 4 | 0 | 4 | 0 | $D^{\mu}$ (3), $F^{\mu\nu}$ (1) |
| [Canonical Quantization of the Biquaternion Dirac Field](../articles_physics/canonical-quantization-of-the-biquaternion-dirac-field.html) | $\mathbb{B}$ | 4 | 0 | 1 | 3 | $p^{\mu}$ (3), $j^{\mu}$ (1) |
| [Cosmology under the Biquaternion Framework — A Research Agenda](../articles_physics/cosmology-under-the-biquaternion-framework-a-research-agenda.html) | $\mathbb{M}_-$ | 4 | 0 | 4 | 0 | $T^{\mu\nu}$ (2), $\eta^{\mu\nu}$ (2) |
| [Electric–Magnetic Duality and the Modular Group in Biquaternionic Form](../articles_physics/electric-magnetic-duality-and-the-modular-group-in-biquaternionic-form.html) | $\mathbb{B}$ | 4 | 0 | 4 | 0 | $F^{\mu\nu}$ (4) |
| [Electroweak Theory under the Biquaternion Framework — A Research Agenda](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | $\mathbb{B}$ | 4 | 0 | 4 | 0 | $F^{\mu\nu}$ (2), $A^{\mu}$ (1), $j^{\mu}$ (1) |
| [Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form](../articles_physics/gauge-redundancy-and-the-information-in-the-gauge-orbit-in-biquaternionic-form.html) | $\mathbb{B}$ | 4 | 0 | 4 | 0 | $dx^{\mu}$ (2), $F^{\mu\nu}$ (1), $J^{\nu}$ (1) |
| [The Biquaternion Basis of a Unified-Field Fibre Bundle](../articles_physics/the-biquaternion-basis-of-a-unified-field-fibre-bundle.html) | $\mathbb{M}_-$ | 4 | 0 | 2 | 2 | $J^{\nu\lambda}$ (3), $\delta^{\nu}$ (1) |
| [The Daviau Map and the Space Clifford Formulation of the Dirac Equation](../articles_physics/the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html) | both | 4 | 0 | 3 | 1 | $\Sigma^{\mu}$ (3), $x^{\mu}$ (1) |
| [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](../articles_physics/the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html) | $\mathbb{M}_-$ | 4 | 0 | 4 | 0 | $J^{\mu}$ (4) |
| [The Effective Optical Metric of the Local Complex Structure](../articles_physics/the-effective-optical-metric-of-the-local-complex-structure.html) | $\mathbb{B}$ | 4 | 0 | 1 | 3 | $v^{\mu}$ (4) |
| [The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form](../articles_physics/the-semiclassical-expansion-and-the-instanton-gas-in-biquaternionic-form.html) | $\mathbb{B}$ | 4 | 0 | 2 | 2 | $F^{\mu\nu}$ (2), $x^{\mu}$ (2) |
| [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html) | both | 3 | 0 | 1 | 2 | $T^{\mu}$ (2), $J^{\nu}$ (1) |
| [Gauge Transformations of the First and Second Kind in Biquaternionic Form](../articles_physics/gauge-transformations-of-the-first-and-second-kind-in-biquaternionic-form.html) | $\mathbb{B}$ | 3 | 0 | 3 | 0 | $F^{\mu\nu}$ (3) |
| [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) | $\mathbb{B}$ | 3 | 0 | 3 | 0 | $j^{\mu}$ (2), $F^{\mu\nu}$ (1) |
| [The CPT Theorem in Biquaternionic Form](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) | $\mathbb{B}$ | 3 | 0 | 2 | 1 | $x^{\mu}$ (3) |
| [The Determination of the Possible Spins in Biquaternionic Form](../articles_physics/the-determination-of-the-possible-spins-in-biquaternionic-form.html) | — | 3 | 0 | 1 | 2 | $W^{\mu}$ (3) |
| [The Electron in Biquaternionic Form](../articles_physics/the-electron-in-biquaternionic-form.html) | $\mathbb{B}$ | 3 | 0 | 3 | 0 | $j^{\mu}$ (3) |
| [The Quantized Dirac Field in Biquaternionic Form](../articles_physics/the-quantized-dirac-field-in-biquaternionic-form.html) | $\mathbb{B}$ | 3 | 0 | 1 | 2 | $J^{\mu}$ (3) |
| [The Standard Model under the Biquaternion Framework — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) | $\mathbb{B}$ | 3 | 0 | 3 | 0 | $F^{\mu\nu}$ (2), $j^{\mu}$ (1) |
| [Anyons and Braid Statistics in Biquaternionic Form](../articles_physics/anyons-and-braid-statistics-in-biquaternionic-form.html) | — | 2 | 0 | 2 | 0 | $\varepsilon^{\mu\nu\rho}$ (2) |
| [Chiral Fermions in the Biquaternion Framework](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) | $\mathbb{B}$ | 2 | 0 | 2 | 0 | $j^{\mu}$ (2) |
| [Confinement and the Loss of Partonic Information in Biquaternionic Form](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) | $\mathbb{B}$ | 2 | 0 | 2 | 0 | $dx^{\mu}$ (2) |
| [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html) | $\mathbb{B}$ | 2 | 0 | 2 | 0 | $x^{\mu}$ (2) |
| [Nonlinear Maxwell Equations in Biquaternionic Form](../articles_physics/nonlinear-maxwell-equations-in-biquaternionic-form.html) | $\mathbb{B}$ | 2 | 0 | 2 | 0 | $T^{\mu\nu}$ (1), $f^{\nu}$ (1) |
| [The Central Scalar Field: Classical Dynamics in the Biquaternion Centre](../articles_physics/the-central-scalar-field-classical-dynamics-in-the-biquaternion-centre.html) | $\mathbb{B}$ | 2 | 0 | 1 | 1 | $T^{\mu\nu}$ (1), $j^{\nu}$ (1) |
| [The Local Complex Structure and the Speed of Light](../articles_physics/the-local-complex-structure-and-the-speed-of-light.html) | $\mathbb{B}$ | 2 | 0 | 2 | 0 | $dx^{\mu}$ (2) |
| [Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form](../articles_physics/bhabha-multi-mass-wave-equations-and-the-bivector-space-in-biquaternionic-form.html) | $\mathbb{M}_-$ | 1 | 0 | 1 | 0 | $x^{\mu}$ (1) |
| [Exercise: The Retarded Potentials and the Green's Function](../articles_physics/exercise-the-retarded-potentials-and-the-greens-function.html) | $\mathbb{B}$ | 1 | 0 | 1 | 0 | $A^{\mu}$ (1) |
| [Subluminal and Superluminal Electromagnetic Waves in Biquaternionic Form](../articles_physics/subluminal-and-superluminal-electromagnetic-waves-and-the-lepton-mass-spectrum.html) | $\mathbb{M}_-$ | 1 | 0 | 1 | 0 | $v^{\mu}$ (1) |
| [The Foldy–Wouthuysen Transformation in Biquaternionic Form](../articles_physics/the-foldy-wouthuysen-transformation-in-biquaternionic-form.html) | $\mathbb{B}$ | 1 | 0 | 1 | 0 | $x^{\mu}$ (1) |
| [The Hydrogen Atom in Biquaternionic Form — The Relativistic Case](../articles_physics/the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html) | $\mathbb{B}$ | 1 | 0 | 1 | 0 | $j^{\mu}$ (1) |
| [The Index Theorem and the Zero-Mode Count in Biquaternionic Form](../articles_physics/the-index-theorem-and-the-zero-mode-count-in-biquaternionic-form.html) | $\mathbb{B}$ | 1 | 0 | 1 | 0 | $F^{\mu\nu}$ (1) |
| [The Material Sector: Four-Vectors, Interval and Lorentz Action](../articles_physics/the-material-sector-four-vectors-interval-and-lorentz-action.html) | $\mathbb{M}_-$ | 1 | 0 | 1 | 0 | $J^{\mu}$ (1) |
| [The Proton in Biquaternionic Form](../articles_physics/the-proton-in-biquaternionic-form.html) | $\mathbb{B}$ | 1 | 0 | 1 | 0 | $j^{\mu}$ (1) |

## The Part VI Inventory

Twelve of the 884 Part VI articles carry a raised index. Three are Class A, in the matrix and Clifford group of $M_4(\mathbb{C})$; six are Class B, led by the split-biquaternion element representations and the first-order root; three are Class C, the tuple labels of the element representations.

| Article | Frame | Raised | Slot | Contracted | Plain | Objects (quoted form) |
|---|---|---:|---:|---:|---:|---:|
| [Split-Biquaternion Algebraic Element Representations](../articles_maths/split-biquaternion-algebraic-element-representations.html) | $\mathbb{B}$ | 25 | 0 | 10 | 15 | $Q^{\mu}$ (13), $q^{\mu}$ (12) |
| [The First-Order Root of the Biquaternion D'Alembertian](../articles_maths/the-first-order-root-of-the-biquaternion-d-alembertian.html) | $\mathbb{B}$ | 25 | 0 | 18 | 7 | $x^{\mu}$ (15), $g^{\mu\nu}$ (10) |
| [Split-Quaternion Higher Special Functions](../articles_maths/split-quaternion-higher-special-functions.html) | $\mathbb{B}$ | 4 | 0 | 3 | 1 | $\xi^{\nu}$ (4) |
| [The Killing Form of the Antisymmetric Plain Algebra](../articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternioid.html) | $\mathbb{B}$ | 4 | 0 | 1 | 3 | $h^{\mu\nu}$ (3), $\delta^{\mu\nu}$ (1) |
| [The Escape Radius and the Green's Function](../articles_maths/the-escape-radius-and-the-greens-function.html) | — | 3 | 0 | 0 | 3 | $U^{\mu}$ (3) |
| [$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra](../articles_maths/m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html) | $\mathbb{B}$ | 2 | 0 | 2 | 0 | $\Sigma^{\mu\nu}$ (2) |
| [Quaternion Involutions and Projections](../articles_maths/quaternion-involutions-and-projections.html) | — | 2 | 0 | 0 | 2 | $q^{\nu}$ (2) |
| [The Clifford Group and the Frame Stabiliser](../articles_maths/the-clifford-group-and-the-frame-stabiliser.html) | — | 2 | 2 | 0 | 0 | $\Lambda^{\mu}$ (2) |
| [The Fierz–Kofink Identities and the Classification of Spinors](../articles_maths/the-fierz-kofink-identities-and-the-classification-of-spinors.html) | $\mathbb{M}_-$ | 2 | 0 | 2 | 0 | $J^{\mu}$ (1), $\eta^{\mu\nu}$ (1) |
| [The Matrix Algebra $M_4(\mathbb{C})$](../articles_maths/the-matrix-algebra-m4c.html) | $\mathbb{B}$ | 2 | 2 | 0 | 0 | $c^{\lambda}$ (2) |
| [Split-Biquaternion Element Representation Theory](../articles_maths/split-biquaternion-element-representation-theory.html) | — | 1 | 0 | 0 | 1 | $a^{\lambda}$ (1) |
| [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](../articles_maths/the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html) | — | 1 | 1 | 0 | 0 | $\Lambda^{\mu}$ (1) |

The other 29 index-shaped tokens in Part VI are not indices. They are the order $\nu$ of a Bessel function written in a power, the eigenvalue $\lambda$ in $e^\lambda$, and parameter labels on signed operators.

## What a Pass Would Cost

The 2,423 physics occurrences divide as 58 slots, 1,590 paired and 775 plain labels. The 73 Part VI occurrences divide as 5 slots, 36 paired and 32 plain. Only the plain labels, 807 in all, can be lowered mechanically.

The Frame column splits the work by kind of decision, not by difficulty. The 336 $\mathbb{M}_-$ pairs lower as relabels under one explicit $\varepsilon$ sum, because the two weights coincide there. The 1,109 $\mathbb{B}$ pairs do not: $g$ and $\varepsilon$ differ, so each display must declare which contraction it means. The 170 *both* pairs carry the same choice, made per display inside one article. A pass in the order A, B, C is still the cheap order. Class A is 14 articles and 326 occurrences, and every one needs a decision about the slot before any edit. Class B is 105 articles and 2,164 occurrences, of which 1,626 are paired. Most are textbook formulas quoted in the middle of a biquaternion argument, and the decision is editorial before it is technical: does the article own the formula, or quote it? A quotation may keep its notation if the article says so; an owned formula may not. Class C is 3 Part VI articles and a local relabel.

The corpus does not yet state a quotation rule. Until it does, Class B cannot be closed by a script, because the same string needs two different treatments in two different articles.

## Recommendation

1. Declare the frame before any edit. Done for the physics inventory: the ten silent articles now declare one, and every row carries its frame. The seven *both* rows still need a per-display choice.
2. Lower Class C everywhere it survives. In physics this is done; in Part VI it is 3 files of tuple labels, held until the tuple convention is stated.
3. Fix Class A next. It is small, structural, and each repair is a matrix, a cell form or a stated slot order. No bulk edit is possible.
4. Adopt a quotation rule for imported tensor formulas, then treat Class B article by article.
5. Keep the numeric components in the same pass as the Greek ones. An article that lowers $x^\mu$ and leaves $x^0$ is half converted.

## Summary

The gamma indices are gone. 110 physics articles and twelve Part VI articles still carry a raised Greek index, 2,496 occurrences in all.

The remaining occurrences fall into three kinds. Class A, the slot, occurs in 11 physics and 3 Part VI articles, 326 occurrences; lowering destroys the row-column distinction. Class B, the pairing, occurs in 99 physics and 6 Part VI articles, 2,164 occurrences; where it is a contraction, lowering drops the signs of $\varepsilon$ and changes the value. Class C, the plain label, occurs in 3 Part VI articles, 6 occurrences; lowering is safe.

The Frame column divides the remainder by kind of decision. 19 articles read in $\mathbb{M}_-$, where the two weights coincide and a paired index lowers as a relabel; 87 in $\mathbb{B}$, where $g$ and $\varepsilon$ differ and each display must choose its contraction; 7 in *both*; 9 carry only algebraic labels.

A scan that counts every caret reports tens of thousands of false positives. The real count is 2,423 physics occurrences and 73 in Part VI. The work is concentrated in Class A and Class B, and Class B needs an editorial decision before it needs an edit.

## Summary of Notation

| Token | Meaning |
|---|---|
| $\gamma_\mu$ | gamma cell; the index is a label, never raised |
| $T_{\mu\nu}=L_\mu R_\nu$ | cell of the two-sided algebra |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector inside the product, the metric of the series |
| $Q_t=ict'$ | time coordinate of the $\mathbb{B}$ frame |
| $x_0=ct'$ | time coordinate of the $\mathbb{M}_-$ frame |
| $\tilde R=ict'e_t+x\vec e_x+y\vec e_y+z\vec e_z$ | material four-position |
| $\mu,\nu,\rho,\lambda,\kappa$ | spacetime component labels, always low |
| Frame (column) | the frame the article's displays are read in; — marks an algebraic label, not a spacetime index |

## Further Reading

- [Operator and Calculus Conventions](../articles_physics/conventions-of-the-operators-and-the-calculus.html) — the rule: a contraction is a form, never an index.
- [Matrix Representations Conventions](../articles_physics/conventions-of-the-matrix-models.html) — the gamma set, the $\mathbb{B}$ frame and the $\mathbb{M}_-$ frame, and the low-index rule.
- [The First-Order Root of the Biquaternion D'Alembertian](../articles_maths/the-first-order-root-of-the-biquaternion-d-alembertian.html) — the largest Part VI case of a raised index inside a derivative.
