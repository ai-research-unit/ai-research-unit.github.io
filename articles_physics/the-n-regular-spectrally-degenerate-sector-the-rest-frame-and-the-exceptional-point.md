# __The N-Regular, Spectrally Degenerate Sector: The Rest Frame and the Exceptional Point__

## Introduction

The cell $\Sigma_{10}$ is the set of elements that have an invariant magnitude but no spectral splitting: $N\neq0$ and $B^2=0$. The two eigenvalues coincide at $Q_t$, the characteristic polynomial is a square, and the element is a unit. The question of the cell is what remains of a two-mode object when the two modes meet.

Two answers live in the same cell, and they are physically different. The **scalar line** $Q_te_t$ is semisimple: the eigenvalue is repeated, but the element is diagonalisable, every basis is an eigenbasis, and the two-term writing is not unique. It is the **rest frame** of a massive momentum. The **Jordan part** $Q_t e_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ is defective: the eigenvalue is repeated and the element is a single Jordan block. It is the **exceptional point** of the complexified algebra, where two modes have coalesced and the eigenbasis has disappeared.

The article reads both faces. It states the cell and its geometry, reads the scalar line as the rest frame, reads the Jordan part as the exceptional point, and states where the two readings stop. It proves nothing; the sector theorems are those of *The N-Regular, Spectrally Degenerate Sector*, and the Jordan basis is that of *The Jordan Basis of a Spectrally Degenerate Biquaternion*.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The definition, the five descriptions and the geometry of the cell | [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html) |
| The two regimes, the centraliser and the Peirce data | [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html), §*The Two Regimes* |
| The Jordan basis and the canonical flag | [The Jordan Basis of a Spectrally Degenerate Biquaternion](../articles_maths/the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html) |
| The repeated eigenvalue and the discriminant | [The Spectrum](../articles_maths/the-spectrum.html) |
| The exponential and the logarithm in the degenerate regimes | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The four-vector dictionary and the rest frame | [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The spectral reading of a four-momentum | [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html) |
| The polar word and its degenerate boundary | [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html) |
| The exponential boundary | [The Exponential, the Logarithm and the Generator](the-exponential-the-logarithm-and-the-generator.html) |

## The Cell

The cell is

$$
\Sigma_{10}=\{N\neq0,\ B^2=0\}
=\{Q_t^2+B^2\neq0,\ B^2=0\}.
$$

On the spectral cone $B^2=0$ one has $N=Q_t^2$, so the norm is non-zero exactly when the scalar part is non-zero. The cell is therefore

$$
\Sigma_{10}=\mathcal S\setminus\mathcal N
=\{Q_t e_t+\vec\Upsilon\ :\ Q_t\in\mathbb{C}^\times,\ \vec\Upsilon^2=0\}.
$$

The pair $(Q_t,\vec\Upsilon)$ is determined by the element: $Q_t$ is the scalar part and $\vec\Upsilon=\vec Q$. The cell is a complex cone of complex dimension three and real dimension six, with the apex removed. Its singular locus is the punctured scalar line, the vertex of the spectral cone.

An element of the cell is a unit with a repeated eigenvalue:

$$
p_{\tilde Q}(X)=(X-Q_t)^2,
\qquad
\lambda=Q_t
\quad\text{with multiplicity }2,
\qquad
N=Q_t^2\neq0.
$$

The cell splits by the vector part into two regimes:

$$
\Sigma_{10}=\Sigma_{10}^{\mathrm{s}}\sqcup\Sigma_{10}^{\mathrm{J}},
\qquad
\Sigma_{10}^{\mathrm{s}}=\{Q_te_t\},
\qquad
\Sigma_{10}^{\mathrm{J}}=\{Q_t e_t+\vec\Upsilon,\ \vec\Upsilon\neq0\}.
$$

The scalar line is closed, of complex dimension one; the Jordan part is open and dense, of complex dimension three. They meet only in the limit $\vec\Upsilon\to0$.

## The Scalar Line: The Rest Frame

### The Element

On the scalar line the element is central:

$$
\tilde Q=Q_te_t,
\qquad
\tilde Q\tilde X=\tilde X\tilde Q
\quad\text{for every }\tilde X.
$$

It is semisimple, with minimal polynomial $X-Q_t$, not $(X-Q_t)^2$. The spectral idempotent is $e_t$ itself, and it is unique; the two-term refinement is not. Every orthogonal pair $\tilde\Pi_1+\tilde\Pi_2=e_t$ gives

$$
\tilde Q=Q_t\tilde\Pi_1+Q_t\tilde\Pi_2,
$$

with the same coefficient on both terms, and the pair is not determined by $\tilde Q$. The canonical Peirce decomposition attached to $\tilde Q$ has one term, $\tilde Q=Q_te_t$; every two-term refinement is non-unique.

### The Physics

On the material slice, a four-momentum at rest is

$$
\tilde P=i\frac{E}{c}e_t=i\,mc\,e_t,
\qquad
\vec p=0,
\qquad
B=0,
\qquad
N=-m^2c^2.
$$

It is the scalar line with $Q_t=imc$. The two eigenvalues coincide at $imc$, and the two light-cone frequencies are equal:

$$
\lambda_+=\lambda_-=i\,mc.
$$

The **rest frame** is therefore the scalar line. The reading has three parts.

- **One frequency.** The two light-cone frequencies coincide; the spectral splitting, which is twice the momentum, vanishes. There is no beat and no preferred null pair.
- **No preferred axis.** Every direction is an eigenaxis, because the element is central. The two-term writing is not unique: every complementary pair of idempotents gives the same element. The rest frame is the only frame in which the momentum has no preferred axis.
- **A global phase and a scale.** The central element commutes with everything and acts as a scalar on every module. Its modulus is the mass; its phase is the causal label of the material sector, fixed to $i$ on the positive-energy timelike slice. Read on a state module, the same central phase multiplies every component and is unobservable on rays. The rest frame carries the rest frequency, not an orientation.

The scalar line is the boundary of the two-mode cell. A massive particle in motion approaches it as $\vec p\to0$; the two eigenvalues coalesce, the two-term writing becomes non-unique, and the direction $\vec p/\lvert\vec p\rvert$ is lost. The limit is continuous in the element and discontinuous in the frame: the element has a limit, the eigenbasis does not.

## The Jordan Part: The Exceptional Point

### The Element

On the Jordan part the element is

$$
\tilde Q=Q_t e_t+\vec\Upsilon,
\qquad
\vec\Upsilon^2=0,
\qquad
\vec\Upsilon\neq0.
$$

It is defective: the minimal polynomial is $(X-Q_t)^2$, and the element is a single Jordan block of size two. The centraliser is the dual-number algebra

$$
\mathbb{C}[\tilde Q]=\{a e_t+b\vec\Upsilon\}
\cong\mathbb{C}[\varepsilon]/(\varepsilon^2),
$$

whose only idempotents are $0$ and $e_t$. No non-trivial idempotent commutes with $\tilde Q$, so no non-trivial Peirce decomposition is attached to the element and there is no spectral decomposition. A Peirce decomposition still exists: with $f=e_t-e$ and an idempotent $e$ such that $\vec\Upsilon=e\vec\Upsilon f$, the Peirce form is

$$
e\tilde Qe=Q_te,\qquad
e\tilde Qf=\vec\Upsilon,\qquad
f\tilde Qe=0,\qquad
f\tilde Qf=Q_tf,
$$

and the Peirce matrix is the single block $J_2(Q_t)$ for every such choice. The closest structure attached to the element is a flag: an isotropic line inside the common kernel–image of $L_{\vec\Upsilon}$, with no canonical complement. The flag is invariant; only the scale of the vector that spans its line is a gauge of the flag, and the frame that splits the flag is chosen.

The powers and the inverse are

$$
\tilde Q^n=Q_t^ne_t+nQ_t^{n-1}\vec\Upsilon,
\qquad
\tilde Q^{-1}=\frac{1}{Q_t}e_t-\frac{1}{Q_t^2}\vec\Upsilon.
$$

The inverse exists, and it is again in the Jordan part. The element is a unit, but it is not diagonalisable.

### The Physics

The physical reading of the Jordan part is the **exceptional point**. Read as the $2\times2$ element, the two eigenvalues and the two eigendirections have coalesced into one eigenvalue and one eigendirection: the element is a single Jordan block. Read as the operator $L_{\tilde Q}$ on the algebra, the four eigendirections of the generic case collapse to a two-dimensional eigenspace, and $L_{\tilde Q}$ has two Jordan blocks; the eigenbasis has disappeared, and a perturbation needs a Jordan chain. The reading is the algebraic form of the exceptional point of a non-Hermitian operator.

Three consequences follow, and each is a reading of a theorem.

- **Coalesced modes.** The two eigenvalues are equal and the two eigendirections of the element have merged. The element and $L_{\tilde Q}$ cannot be diagonalised, and the response to a perturbation is not a sum of two exponentials but a term linear in the parameter times the exponential.
- **A shear.** The element is a scale times a unipotent, $Q_t e_t+\vec\Upsilon=Q_t(e_t+\vec\Upsilon/Q_t)$ with $(\vec\Upsilon/Q_t)^2=0$. The unipotent is a null rotation of the frame: it preserves the flag and moves along it. The reading is a rate with a shear, not a rate with a direction.
- **A double pole.** The inverse $\tilde Q^{-1}=Q_t^{-1}e_t-Q_t^{-2}\vec\Upsilon$ has a double pole in $Q_t$. In a propagator or a resolvent, the double pole is the signature of a defective mode; the residue is not a projector but a projector plus a nilpotent.

The exceptional point is not on the real material slice. A real spatial vector has $B^2=\lvert\vec p\rvert^2$, which vanishes only at $\vec p=0$, and then $\vec\Upsilon=0$: the real slice meets the cell on the scalar line only. The Jordan part needs a complex isotropic spatial vector, and its physical reading is a complexified momentum, not a real four-momentum.

## The Spectrum and the Beat

The cell has one eigenvalue. The two spectral questions have different answers:

| question | answer on the scalar line | answer on the Jordan part |
| --- | --- | --- |
| how many eigenvalues? | one, repeated | one, repeated |
| diagonalisable? | yes | no |
| eigenbasis? | every basis | none |
| spectral decomposition? | one term, non-unique refinement | none |
| canonical Peirce decomposition attached to $\tilde Q$? | one term | none; a chosen adapted idempotent gives $J_2(Q_t)$ |
| inverse? | yes | yes |
| generator? | yes, up to the lattice | yes, up to the lattice |

The **beat stops** on the whole cell: the two frequencies are equal, so there is no oscillation between two modes. The **rate remains**: the eigenvalue $Q_t$ is the frequency of the global phase, and the element still generates a one-parameter group. The reading is precise: a beat needs two frequencies, a phase needs one.

The Fourier kernel degenerates with the cell. At $B=0$ the root $\vec Q/B$ is undefined, the exponential is the dual-number kernel

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\bigl(e_t+\theta\vec\Upsilon\bigr),
$$

and there is no Fourier basis attached to the element. The transform exists, but its characters are not oscillatory in the direction that has collapsed.

## Products and the Boundary

The cell is inverse-closed and not product-closed:

$$
\Sigma_{10}\cdot\Sigma_{10}\subseteq\Sigma_{10}\cup\Sigma_{11}.
$$

The scalar line is closed under products and lies in the cell. The Jordan part is closed under powers: the square of $Q_t e_t+\vec\Upsilon$ is $Q_t^2 e_t+2Q_t\vec\Upsilon$, which is again Jordan. A product of two Jordan elements with different nilpotent directions can leave the cell and land in $\Sigma_{11}$; the norm stays non-zero, so the product never reaches the null cone.

The boundary of the cell inside the spectral cone is the null-cone intersection $\Sigma_{00}$, which the cell does not contain; the interior boundary between the two regimes is the scalar line. The cell is the boundary of the two-mode cell $\Sigma_{11}$ at $B=0$: a path in $\Sigma_{11}$ that reaches $B=0$ lands here.

## Physical Interpretations

- **The scalar line is the rest frame.** A massive momentum at rest has $Q_t=imc$ and $\vec p=0$. The two light-cone frequencies coincide, the two-term writing is not unique, and no axis is preferred. The rest frame is the only real momentum with one mode.
- **The central element is a global phase and a scale.** It commutes with the algebra, acts as a scalar on every module, and carries no orientation. Its modulus is the mass; its phase is the causal label on the material sector, and on a state module it is the unobservable global phase.
- **The Jordan part is the exceptional point.** The element has a single eigenvalue and a single eigendirection; $L_{\tilde Q}$ is defective, its eigenbasis has collapsed, and a perturbation needs a Jordan chain.
- **The unipotent is a shear.** The element is a scale times a null rotation. It preserves the flag and moves along it; the reading is a rate with a shear, not a rate with a direction.
- **The double pole is the defective response.** The inverse has a double pole in the scalar part; in a resolvent or a propagator, the double pole is the signature of a coalesced mode.
- **The beat stops and the rate remains.** The cell has one frequency; there is no oscillation between two modes, but there is still a global phase and a one-parameter group.
- **The cell is the boundary of the two-mode regime.** A massive particle in motion approaches the rest frame as $\vec p\to0$; the element has a limit, the eigenbasis does not.
- **No canonical Peirce decomposition, only a flag.** A Peirce decomposition always exists, but on the Jordan part no pair of non-trivial idempotents is attached to the element: a chosen adapted idempotent gives the Jordan block $J_2(Q_t)$. There is no spectral decomposition and no eigenbasis. The closest structure attached to the element is a flag; the flag is the invariant, and only the scale of the vector that spans its line is a gauge of the flag.

## Limits

The rest-frame reading needs the material slice and the four-momentum chart. In the full algebra the scalar line is the centre minus the origin, and calling it a rest frame is an identification.

The exceptional-point reading is conditional on reading the element as the operator $L_{\tilde Q}$. It is not a claim that a physical Hamiltonian is defective, and it supplies no dynamics and no perturbation theory.

The Jordan part is not on the real material slice. A real four-momentum with $B=0$ has $\vec p=0$ and lies on the scalar line. The Jordan part is a complexified regime.

The cell is not a phase transition. "Degenerate" is spectral, not thermodynamic; the cell is a property of one element, not a basin of attraction.

The cell is not a particle count. A repeated eigenvalue is not two particles with equal masses; it is one element with one eigenvalue and, on the Jordan part, one eigendirection.

No dynamics is supplied. The cell says what the element is at an instant; it does not say how it gets there or what it does.

## Summary

- $\Sigma_{10}=\{N\neq0,\ B^2=0\}$ is the spectral cone minus the null cone: units with a repeated eigenvalue $Q_t$, of real dimension six.
- The scalar line $Q_te_t$ is semisimple, central and the real rest frame: one frequency, no preferred axis, non-unique two-term writing.
- The Jordan part $Q_t e_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$ is defective: one eigenvalue, one Jordan block, no eigenbasis, no canonical Peirce decomposition; a chosen adapted idempotent gives $J_2(Q_t)$, and the flag is the invariant.
- The physical reading of the Jordan part is the exceptional point: coalesced modes, a shear, a double pole in the inverse.
- The beat stops on the whole cell; the rate remains. The cell has one frequency and still generates a one-parameter group.
- The cell is inverse-closed and not product-closed; products stay in $\Sigma_{10}\cup\Sigma_{11}$.
- The real material slice meets the cell on the scalar line only; the Jordan part is a complexified regime.
- The cell is the boundary of the two-mode cell at $B=0$; the element has a limit, the eigenbasis does not.
- The cell supplies no dynamics, no phase transition and no particle count.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Sigma_{10}$ | the cell $N\neq0$, $B^2=0$ |
| $\Sigma_{10}^{\mathrm{s}}$ | the scalar line $Q_te_t$, $Q_t\neq0$ |
| $\Sigma_{10}^{\mathrm{J}}$ | the Jordan part $Q_t e_t+\vec\Upsilon$, $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ |
| $Q_t$ | the repeated eigenvalue |
| $\vec\Upsilon$ | the pure nilpotent direction |
| $N=Q_t^2$ | the norm on the cell |
| $\tilde Q^{-1}=Q_t^{-1}e_t-Q_t^{-2}\vec\Upsilon$ | the inverse on the Jordan part |
| $L_{\tilde Q}$ | left multiplication, the operator reading |

## Further Reading

- [The Four Regimes of an Element: Mass and Motion](the-four-regimes-of-an-element-mass-and-motion.html), for the partition and the other three cells.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the rest frame and the Doppler pair.
- [The N-Regular, Spectrally Regular Sector: Mass in Motion](the-n-regular-spectrally-regular-sector-mass-in-motion.html), for the cell whose boundary this is.
- [The N-Degenerate, Spectrally Degenerate Sector: The Vacuum and the Nilpotent Ladder](the-n-degenerate-spectrally-degenerate-sector-the-vacuum-and-the-nilpotent-ladder.html), for the nilpotents, the other defective regime.
- [The Exponential, the Logarithm and the Generator](the-exponential-the-logarithm-and-the-generator.html), for the logarithm and the boundary.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the word at the degenerate boundary.
