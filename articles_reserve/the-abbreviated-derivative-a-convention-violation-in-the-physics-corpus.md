# __The Abbreviated Derivative: A Convention Violation in the Physics Corpus__

## Status

This article records an audit made before the repair. The corpus has since been patched: all 458 occurrences were rewritten in the compliant spelling, and the current count in `articles_physics` is zero. The counts below are the pre-repair counts and are kept as the record of what was found.

The repair followed the mapping stated here. Greek coordinate indexes became $\partial/\partial Q_\mu$ or $\partial/\partial x_\mu$, according to the coordinate the article uses; the antisymmetrised pair was expanded as $\tfrac12(\partial/\partial x_\mu-\partial/\partial x_\nu)$; the repeated derivative became $\partial^2/\partial Q_\mu\partial Q_\nu$; and the two $\partial^E_\mu$ became $\partial^E/\partial x_\mu$.

## The Rule

*Operator and Calculus Conventions*, §*Conventions for Derivation*, states the rule in one paragraph:

> In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$. ... The derivative with respect to a coordinate is written $\partial/\partial Q_\mu$ ... a coordinate is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception, neither on a free index nor on any other.

The rule has two halves. A subscript is a component index, as in $v_x$ or $\tilde U_{\mathrm r}$. A derivative is a fraction, $\partial/\partial Q_\mu$, with the variable written in full. The spelling $\partial_\mu$ breaks both halves at once: it turns the derivative into a symbol that carries a component index, and it leaves the variable unstated.

## The Violation

The physics corpus carries 458 occurrences of a subscript attached to $\partial$, in 63 of its 403 articles. One derivative mark in seven is written in the abbreviated form: 2,459 occurrences of $\partial/\partial$ and 128 of $\frac{\partial}{\partial}$ give 2,587 compliant writings, against the 458.

| Measure | Value |
|---|---:|
| Articles with at least one occurrence | 63 of 403 (15.6%) |
| Occurrences | 458 |
| Median per affected article | 4 |
| Highest single article | 55 |
| Derivative marks written abbreviated | 15.0% |

| Occurrences in an article | Articles |
|---|---:|
| 1 | 15 |
| 2 to 5 | 27 |
| 6 to 20 | 14 |
| 21 to 50 | 6 |
| More than 50 | 1 |

Two further occurrences sit in one article, written $\partial^E_\mu$, where the Euclidean label $E$ stands between the derivative and its index. The label is a name, which the convention allows to be raised; the $\mu$ under it is still a subscript on a derivative. The total of indexes attached to a derivative is therefore 460.

## The Forms

The subscript takes twenty distinct forms. The coordinate indexes dominate.

| Mark | Count | Compliant spelling |
|---|---:|---|
| $\partial_\mu$ | 237 | $\partial/\partial Q_\mu$ |
| $\partial_\nu$ | 64 | $\partial/\partial Q_\nu$ |
| $\partial_\tau$ | 42 | $\partial/\partial \tau$ |
| $\partial_\lambda$ | 22 | $\partial/\partial Q_\lambda$ |
| $\partial_{t'}$ | 19 | $\partial/\partial t'$ |
| $\partial_{Q_t}$ | 14 | $\partial/\partial Q_t$ |
| $\partial_k$ | 11 | $\partial/\partial Q_k$ or $\partial/\partial x_k$, as the article means |
| $\partial_\rho$ | 10 | $\partial/\partial Q_\rho$ |
| $\partial_\sigma$ | 6 | $\partial/\partial Q_\sigma$ |
| $\partial_{x_\mu}$ | 6 | $\partial/\partial Q_\mu$ |
| $\partial_\beta$ | 5 | $\partial/\partial \beta$ |
| all other forms | 22 | the variable named in full: $\theta$, $\phi$, $\alpha$, $Q_\mu$, $x_k$, $t$, $c$, $0$, and the antisymmetrised pair |

Seven of the other forms are the antisymmetrised derivative $\partial_{[\mu}F_{\nu\rho]}=0$, where the subscript sits on the derivative and the bracket is split across it. The compliant form writes the two derivatives in full and antisymmetrises the pair.

The compliant spelling is not a fixed string. It names the variable the article differentiates with respect to: $\partial/\partial Q_\mu$ for a coordinate, $\partial/\partial t'$ for the material time, $\partial/\partial \theta$ for an angle, $\partial/\partial \beta$ for a coupling. The one thing the spelling never does is leave that variable out.

## Why the Caret Screen Does Not See It

The 458 occurrences pass every check of the index census. Their index is low, so the screen of raised frame slots counts none of them, and it is right: there is no raised frame slot in the corpus.

The two findings do not conflict. The caret rule asks about the height of an index. This rule asks whether a derivative carries an index at all. An article can obey the first and break the second, and 63 of them do.

The violation is also invisible to a reader who checks only the height. That is why it survived the pass that lowered every frame index: the pass rewrote $\sigma^k$ to $\sigma_k$ and left $\partial_\mu$ untouched, because $\partial_\mu$ was never raised.

## The Articles, in Menu Order

The list below follows the order of `physics.md`. Every article carries a direct link. A section with no entry has no occurrence.

| Menu section | Articles | Occurrences |
|---|---:|---:|
| Biquaternion Universe | 0 | 0 |
| Biquaternion Universe Conventions | 0 | 0 |
| Biquaternion Physical Interpretation of Mathematics | 3 | 6 |
| Biquaternion Non Relativistic Quantum Theory | 3 | 57 |
| Biquaternion Non Relativistic Non Quantum Theory | 2 | 5 |
| Biquaternion Electromagnetism | 9 | 93 |
| Biquaternion Relativity | 5 | 21 |
| Biquaternion Relativistic Quantum Theory | 12 | 95 |
| Biquaternion Relativistic Non Quantum Theory | 1 | 8 |
| Biquaternion Quantum Fields | 12 | 33 |
| Biquaternion Particle Physics and Gauge Fields | 9 | 39 |
| Biquaternion Gravity and Cosmology | 6 | 98 |
| Biquaternion Thermodynamics and Statistical Mechanics | 1 | 3 |
| **All sections** | **63** | **458** |


### Biquaternion Physical Interpretation of Mathematics

| Article | Occurrences |
|---|---:|
| [The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge](../articles_physics/the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html) | 1 |
| [The Material Sector: Four-Vectors, Interval and Lorentz Action](../articles_physics/the-material-sector-four-vectors-interval-and-lorentz-action.html) | 1 |
| [The Analytic Structure of Fields: Regularity, Propagation and the Contour](../articles_physics/the-analytic-structure-of-fields-regularity-propagation-and-the-contour.html) | 4 |

### Biquaternion Non Relativistic Quantum Theory

| Article | Occurrences |
|---|---:|
| [The Determination of the Possible Spins in Biquaternionic Form](../articles_physics/the-determination-of-the-possible-spins-in-biquaternionic-form.html) | 1 |
| [Geometric Phases of Non-Relativistic Spin in Biquaternionic Form](../articles_physics/geometric-phases-of-non-relativistic-spin-in-biquaternionic-form.html) | 1 |
| [The Berry Phase and Geometric Phases in Biquaternionic Form](../articles_physics/the-berry-phase-and-geometric-phases-in-biquaternionic-form.html) | 55 |

### Biquaternion Non Relativistic Non Quantum Theory

| Article | Occurrences |
|---|---:|
| [Lagrangian and Hamiltonian Mechanics in Biquaternionic Form](../articles_physics/lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.html) | 2 |
| [Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form](../articles_physics/pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html) | 3 |

### Biquaternion Electromagnetism

| Article | Occurrences |
|---|---:|
| [Maxwell's Equations in the Biquaternionic Formulation](../articles_physics/maxwells-equations-in-biquaternionic-form.html) | 5 |
| [Exercise: The Electromagnetic Energy–Momentum Tensor](../articles_physics/exercise-the-electromagnetic-energy-momentum-tensor.html) | 28 |
| [The Field-Strength Biquaternion and Its Invariants](../articles_physics/the-field-strength-biquaternion-and-its-invariants.html) | 2 |
| [Exercise: Plane-Wave Propagation in a Medium](../articles_physics/exercise-plane-wave-propagation-in-a-medium.html) | 4 |
| [Maxwell's Theory on Non-Commutative Spaces and Quaternions](../articles_physics/maxwells-theory-on-non-commutative-spaces-and-quaternions.html) | 16 |
| [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](../articles_physics/the-algebrodynamical-programme-nonlinear-cauchy-riemann-and-self-quantized-charge.html) | 4 |
| [The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis](../articles_physics/the-electro-gravimagnetic-field-and-the-magnetic-charge-mass-hypothesis.html) | 30 |
| [The Ether and Photons in the Electro-Gravimagnetic Programme](../articles_physics/the-ether-and-photons-in-the-electro-gravimagnetic-programme.html) | 3 |
| [Subluminal and Superluminal Electromagnetic Waves in Biquaternionic Form](../articles_physics/subluminal-and-superluminal-electromagnetic-waves-and-the-lepton-mass-spectrum.html) | 1 |

### Biquaternion Relativity

| Article | Occurrences |
|---|---:|
| [Similitudes Between Biquaternion Rotors and Hamiltonian Flow](../articles_physics/similitudes-between-biquaternion-rotors-and-hamiltonian-flow.html) | 1 |
| [Noether's Theorem in Biquaternionic Form](../articles_physics/noethers-theorem-in-biquaternionic-form.html) | 4 |
| [The Poincaré Group and the Biquaternion Frame](../articles_physics/the-poincare-group-and-the-biquaternion-frame.html) | 5 |
| [The Conformal Group in Biquaternionic Form](../articles_physics/the-conformal-group-in-biquaternionic-form.html) | 8 |
| [Twistor Theory and Biquaternions](../articles_physics/twistor-theory-and-biquaternions.html) | 3 |

### Biquaternion Relativistic Quantum Theory

| Article | Occurrences |
|---|---:|
| [The Relativistic Action and the Stationary-Action Principle in Biquaternionic Form](../articles_physics/the-relativistic-action-and-the-stationary-action-principle-in-biquaternionic-form.html) | 21 |
| [Conformal Invariance and the Massless Limit in Biquaternionic Form](../articles_physics/conformal-invariance-and-the-massless-limit-in-biquaternionic-form.html) | 2 |
| [The First-Order Root of the Biquaternion Klein–Gordon Operator](../articles_physics/the-first-order-root-of-the-biquaternion-klein-gordon-operator.html) | 8 |
| [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](../articles_physics/the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html) | 4 |
| [The s-Vector Representation of the Dirac Spinor in Biquaternionic Form](../articles_physics/the-s-vector-representation-of-the-dirac-spinor-in-biquaternionic-form.html) | 13 |
| [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](../articles_physics/the-gordon-decomposition-in-biquaternionic-form.html) | 6 |
| [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](../articles_physics/exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html) | 4 |
| [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](../articles_physics/antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html) | 1 |
| [The Hydrogen Atom in Biquaternionic Form — The Relativistic Case](../articles_physics/the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html) | 1 |
| [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](../articles_physics/the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html) | 2 |
| [Dual Equivalence of the Dirac and Topologically Massive Gauge Fields](../articles_physics/dual-equivalence-of-the-dirac-and-topologically-massive-gauge-fields.html) | 7 |
| [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | 26 |

### Biquaternion Relativistic Non Quantum Theory

| Article | Occurrences |
|---|---:|
| [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](../articles_physics/stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html) | 8 |

### Biquaternion Quantum Fields

| Article | Occurrences |
|---|---:|
| [Interpretation of the Wick Rotation in the Biquaternion Universe](../articles_physics/the-interpretation-of-the-wick-rotation-in-the-biquaternion-universe.html) | 2 |
| [The Functional Integral in Biquaternionic Form](../articles_physics/the-functional-integral-in-biquaternionic-form.html) | 2 |
| [The Unruh Effect in Biquaternionic Form](../articles_physics/the-unruh-effect-in-biquaternionic-form.html) | 1 |
| [The Theta Vacuum in Biquaternionic Form](../articles_physics/the-theta-vacuum-in-biquaternionic-form.html) | 1 |
| [Bosonization in Biquaternionic Form](../articles_physics/bosonization-in-biquaternionic-form.html) | 4 |
| [The Spectral Triple of the Biquaternion Algebra](../articles_physics/the-spectral-triple-of-the-biquaternion-algebra.html) | 5 |
| [Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form](../articles_physics/fermion-doubling-and-the-nielsen-ninomiya-theorem-in-biquaternionic-form.html) | 1 |
| [Canonical Quantization of the Biquaternion Maxwell Field](../articles_physics/canonical-quantization-of-the-biquaternion-maxwell-field.html) | 1 |
| [The Gauge Field Path Integral in Biquaternionic Form](../articles_physics/the-gauge-field-path-integral-in-biquaternionic-form.html) | 6 |
| [Wilson Loops in Biquaternionic Form](../articles_physics/wilson-loops-in-biquaternionic-form.html) | 3 |
| [Canonical Quantization of the Biquaternion Graviton Field](../articles_physics/canonical-quantization-of-the-biquaternion-graviton-field.html) | 5 |
| [Anyons and Braid Statistics in Biquaternionic Form](../articles_physics/anyons-and-braid-statistics-in-biquaternionic-form.html) | 2 |

### Biquaternion Particle Physics and Gauge Fields

| Article | Occurrences |
|---|---:|
| [The Hopf Fibration and the Biquaternion Gauge Bundle](../articles_physics/the-hopf-fibration-and-the-biquaternion-gauge-bundle.html) | 3 |
| [Instantons and Solitons in Biquaternionic Form](../articles_physics/instantons-and-solitons-in-biquaternionic-form.html) | 2 |
| [The ADHM Construction and Biquaternion Instanton Data](../articles_physics/the-adhm-construction-and-biquaternion-instanton-data.html) | 2 |
| [The Gauge Extension of the Central Phase: Why the Centre Caps the Group](../articles_physics/the-gauge-extension-of-the-central-phase-why-the-centre-caps-the-group.html) | 1 |
| [Custodial Symmetry and the Rho Parameter in Biquaternionic Form](../articles_physics/custodial-symmetry-and-the-rho-parameter-in-biquaternionic-form.html) | 8 |
| [The Skyrme Model and the Topological Baryon in Biquaternionic Form](../articles_physics/the-skyrme-model-and-the-topological-baryon-in-biquaternionic-form.html) | 2 |
| [The Majorana Equation in Biquaternionic Form](../articles_physics/the-majorana-equation-in-biquaternionic-form.html) | 13 |
| [The Yang–Mills Equation in Biquaternionic Form](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html) | 7 |
| [The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form](../articles_physics/the-yang-mills-path-integral-and-the-faddeev-popov-procedure-in-biquaternionic-form.html) | 1 |

### Biquaternion Gravity and Cosmology

| Article | Occurrences |
|---|---:|
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | 23 |
| [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](../articles_physics/torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html) | 9 |
| [Linearized Gravity in Biquaternionic Form](../articles_physics/linearized-gravity-in-biquaternionic-form.html) | 11 |
| [Gravitational Waves in Biquaternionic Form](../articles_physics/gravitational-waves-in-biquaternionic-form.html) | 38 |
| [Black Hole Thermodynamics in Biquaternionic Form](../articles_physics/black-hole-thermodynamics-in-biquaternionic-form.html) | 1 |
| [Matter Makes Space — An External Construction from Quaternionic Spinors](../articles_physics/matter-makes-space-an-external-construction-from-quaternionic-spinors.html) | 16 |

### Biquaternion Thermodynamics and Statistical Mechanics

| Article | Occurrences |
|---|---:|
| [The Partition Function in Biquaternionic Form](../articles_physics/the-partition-function-in-biquaternionic-form.html) | 3 |

## What a Repair Would Do

The repair is mechanical in form and cautious in reading. Each occurrence becomes a fraction with its variable named: $\partial_\mu$ becomes $\partial/\partial Q_\mu$, $\partial_{t'}$ becomes $\partial/\partial t'$, $\partial_{Q_t}$ becomes $\partial/\partial Q_t$, and $\partial_\theta$ becomes $\partial/\partial \theta$.

Two cases need a decision rather than a substitution. The spatial derivative $\partial_k$ may mean $\partial/\partial Q_k$ or $\partial/\partial x_k$, and the article that carries it says which; the same holds for $\partial_{x_\mu}$ where the variable is already named. The numeric mark $\partial_0$ in *Exercise: The Electromagnetic Energy–Momentum Tensor* is defined by the article itself as a shorthand for a multiple of $\partial/\partial t'$; the shorthand is the violation, and the definition is the place to remove it.

The two occurrences of $\partial^E_\mu$ in *Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form* keep the Euclidean label and lose the subscript: $\partial^E/\partial x_\mu$ or $\partial^E/\partial Q_\mu$, as the article's variable requires.

No repair has been made. The corpus is unmodified.

## Summary

The physics corpus breaks the derivative rule 458 times in 63 articles. The index is low, so the caret screen passes all of them; the fault is that the variable is left under the $\partial$, and the compliant spelling is $\partial/\partial Q_\mu$.

The distribution is uneven. *The Berry Phase and Geometric Phases in Biquaternionic Form* carries 55, *Gravitational Waves* 38, *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* 30, *Exercise: The Electromagnetic Energy–Momentum Tensor* 28, *The Rarita–Schwinger Equation* 26 and *Curved Spacetime* 23. The remaining 57 articles carry 258 between them, and 42 of the 63 carry five or fewer.

## Summary of Notation

| Token | Meaning |
|---|---|
| $\partial/\partial Q_\mu$ | the compliant derivative: the variable named in full |
| $\partial_\mu$, $\partial_\nu$, $\partial_\rho$ | the abbreviated spelling, forbidden by the rule and counted here |
| $\partial_{t'}$, $\partial_\theta$, $\partial_\beta$ | the same fault on a time, an angle and a coupling |
| $\partial^2/\partial Q_\mu\partial Q_\nu$ | a second derivative, written the same way |
| $\partial^E_\mu$ | a name label over a forbidden subscript |

## Further Reading

- [Operator and Calculus Conventions](../articles_physics/conventions-of-the-operators-and-the-calculus.html) — the rule, with the ban on the abbreviated spelling.
- [The Upper-Index Problem: The Extent of the Infestation](the-upper-indexes-problem.html) — the caret screen, which this violation escapes.
- [The Up and Low Proportions of the Physics Corpus](the-up-and-low-proportions-of-the-physics-corpus.html) — the census that counts the derivative indexes among the low marks.
- [Index, Notation and Corpus Conventions](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) — the same discipline for the mathematical corpus.
