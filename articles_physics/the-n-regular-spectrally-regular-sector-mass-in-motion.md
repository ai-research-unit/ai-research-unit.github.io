# __The N-Regular, Spectrally Regular Sector: Mass in Motion__

## Introduction

The cell $\Sigma_{11}$ is the set of elements for which both questions of the arrangement receive the positive answer: the norm does not vanish, and the two eigenvalues do not coincide. It is the generic cell, open and dense in the algebra. It is also the cell of a massive particle in motion, and of a spacelike momentum. Its physical content is the two-mode picture: two distinct light-cone frequencies, two invariant planes, a mode basis, and a beat. The two frequencies differ by $2\lvert\vec p\rvert=2mc\lvert\sinh\psi\rvert$, and that difference is the beat frequency: a kinematic beat between the two modes, not a dynamical effect.

The article reads the cell. It states the conditions and the spectrum, reads the two-mode structure, the causal sign, the frame dependence, the invertibility and the spinor decomposition, and it labels the interpretations. It proves nothing: the sector theorems, the eigenbasis and the Peirce data are those of the mathematics articles cited below.

The name of the cell is deliberately double. **Mass in motion** is the timelike branch; the cell also contains the spacelike branch, where the invariant $N$ is positive and the two eigenvalues lie on opposite halves of the imaginary axis. The cell is a spectral type, not a single causal class; the sign of $N$ is a second reading of the same cell.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The definition, the five descriptions and the geometry of the cell | [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html) |
| The spectrum, the spectral idempotents and the two-term writing | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| The eigenbasis and the Peirce corners | [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html) |
| The spinor spaces and chirality | [The Minimal Left Ideals](../articles_maths/the-minimal-left-ideals.html) |
| The independence of the two conditions | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html) |
| The four-vector dictionary and the mass shell | [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The spectral reading of a four-momentum | [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html) |
| The polar word and the unit group | [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html) |
| The Lorentz action as a sandwich | [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html) |

## The Cell

The cell is

$$
\Sigma_{11}=\{N\neq0,\ B^2\neq0\}
=\mathbb{B}\setminus(\mathcal N\cup\mathcal S),
$$

the complement of the union of the null cone and the spectral cone. It is open, dense and of full measure; its complement is the union of the two complex hypersurfaces $N=0$ and $B^2=0$, each of real codimension two, and it has measure zero. A generic element of the algebra lies here. The cell is connected but not simply connected, and it is of complex dimension four, real dimension eight.

An element of the cell is a unit with two distinct eigenvalues. The characteristic polynomial is

$$
p_{\tilde Q}(X)=X^2-2Q_tX+N,
\qquad
\operatorname{disc}p_{\tilde Q}=-4B^2\neq0,
$$

and its roots are

$$
\lambda_\pm=Q_t\pm iB,
\qquad
\lambda_+\neq\lambda_-,
\qquad
\lambda_+\lambda_-=N\neq0.
$$

The two roots are non-zero, so the element is invertible: $\tilde Q^{-1}=\tilde Q^{\natural}/N$. The cell is inverse-closed. The spectral idempotents are unique,

$$
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},
\qquad
\tilde Q=\lambda_+e_++\lambda_-e_-,
$$

and both coefficients are non-zero. This is the only cell in which the spectral decomposition has two non-zero terms and two non-trivial idempotents.

## The Spectrum

### The Doppler Pair

On the material slice, with $\tilde P=i\frac{E}{c}e_t+\vec p$ and $B=\lvert\vec p\rvert$,

$$
\lambda_\pm=i\left(\frac{E}{c}\pm\lvert\vec p\rvert\right)
=i\,mc\,e^{\pm\psi},
\qquad
\cosh\psi=\frac{E}{mc},
\qquad
\sinh\psi=\frac{\lvert\vec p\rvert}{mc}.
$$

The two eigenvalues are the two light-cone frequencies of one momentum, multiplied by $i$. Their sum is $2iE/c$ and their difference is $2i\lvert\vec p\rvert$; their product is $-m^2c^2$, and their ratio is the squared Doppler factor:

$$
\lambda_++\lambda_-=2i\frac{E}{c},
\qquad
\lambda_+-\lambda_-=2i\lvert\vec p\rvert,
\qquad
\lambda_+\lambda_-=-m^2c^2,
\qquad
\frac{\lambda_+}{\lambda_-}=e^{2\psi}.
$$

The product is the invariant. The two factors are frame-dependent, and their dependence is exactly the Doppler rescaling. The cell therefore carries the whole relativistic kinematics of one particle: mass, energy, momentum and rapidity are four readings of one pair.

### The Causal Sign

The sign of $N$ separates the two branches of the cell. On the material slice $N=-E^2/c^2+\lvert\vec p\rvert^2$.

| branch | condition | eigenvalues | reading |
| --- | --- | --- | --- |
| timelike | $\lvert\vec p\rvert<E/c$ | both on the same imaginary half | a massive particle in motion |
| lightlike | $\lvert\vec p\rvert=E/c$ | one zero | the boundary cell $\Sigma_{01}$ |
| spacelike | $\lvert\vec p\rvert>E/c$ | on opposite imaginary halves | a spacelike momentum |

The timelike branch is the one the cell is named after. The spacelike branch is in the same cell because both conditions are non-zero; its spectrum has one eigenvalue with a positive imaginary part and one with a negative imaginary part, and its norm is positive. The two branches are not connected inside the real material slice without crossing the light cone, which is the boundary $\Sigma_{01}$; in the full complex cell they are connected through complexified momenta.

### What the Spectrum Does Not Determine

The spectrum fixes the trace and the norm, and nothing else:

$$
\lambda_++\lambda_-=2Q_t,
\qquad
\lambda_+\lambda_-=N.
$$

It does not fix the direction $\vec Q/B$, the two angles of the axis, or the reality of the vector part. A rotation leaves the pair unchanged and rotates the axis. The cell is therefore larger than the spectrum: it is the spectrum together with the eigenprojections, and the eigenprojections carry the frame.

## The Two Modes

### The Spectral Decomposition

The two-term writing

$$
\tilde Q=\lambda_+e_++\lambda_-e_-
$$

is unique, and both terms are non-zero. Each term is a complex multiple of a minimal idempotent, hence a null element. The decomposition is the split of the element into two null components, not into two particles. The sum of the coefficients is twice the scalar part and their product is the norm; neither is the energy of a separate object.

In the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ the left action of $\tilde Q$ is diagonal with values $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$. The two eigenspaces are complex planes, each spanned by one idempotent and one nilpotent. The mode basis is a basis of the algebra, not of a Hilbert space of states; it is the frame in which the element is diagonal.

### The Spinors

The two minimal left ideals

$$
S_+=\mathbb{B}\tilde\Pi_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-
$$

are the two spinor spaces. Each is a complex plane, and the algebra is their direct sum. On each spinor space, left multiplication by $\tilde Q$ is diagonal with the same two eigenvalues:

$$
L_{\tilde Q}\big|_{S_+}=L_{\tilde Q}\big|_{S_-}
=\operatorname{diag}(\lambda_+,\lambda_-).
$$

A spinor of either chirality therefore carries both modes. Chirality is the right eigenvalue, not the left one: right multiplication by $\tilde Q$ acts as $\lambda_+$ on $S_+$ and $\lambda_-$ on $S_-$. The physical reading is that a spinor is not a mode; it is a two-component object, and the two components are the two modes. The two chiralities are the two ways of splitting the algebra, not the two modes.

### The Peirce Data

The Peirce decomposition relative to $\tilde Q$ is diagonal with two non-zero coefficients,

$$
e_+\tilde Qe_+=\lambda_+e_+,
\qquad
e_-\tilde Qe_-=\lambda_-e_-,
\qquad
e_+\tilde Qe_-=e_-\tilde Qe_+=0.
$$

The two idempotents are the two pure states along the axis $\vec Q/B$; on the material slice they are the two null directions of the momentum. The Peirce decomposition is a two-state basis, and the eigenvalues are the two weights. The normalisation of the nilpotents inside each eigenspace is a gauge; the idempotents themselves are unique.

## Invertibility and Frame

The cell is contained in the unit group. Every element has an inverse,

$$
\tilde Q^{-1}=\lambda_+^{-1}e_++\lambda_-^{-1}e_-=\frac{\tilde Q^{\natural}}{N},
$$

and the inverse lies in the cell. The polar word

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
$$

exists on the whole cell, with $r=\lvert N\rvert^{1/2}$ and the three factors a scale, a central phase, a Hermitian boost and a real rotor. The cell is therefore contained in the domain of the polar decomposition: every element of the cell has a frame, an amplitude and a phase.

The cell is inverse-closed but not product-closed. The norm is multiplicative, so the product of two elements of the cell has non-zero norm and lies in $\Sigma_{11}\cup\Sigma_{10}$; both outcomes occur, and inside $\Sigma_{10}$ both the scalar line and the Jordan part occur. A product of two elements of the cell can land on the scalar line, where the two eigenvalues coincide, or in the Jordan part, where the element is defective. The cell is a symmetric subset of the unit group, not a subgroup: it contains no subgroup, because it does not contain the identity.

The boundary of the cell is the arrangement. A path inside the cell that reaches $B=0$ lands in $\Sigma_{10}$; a path that reaches $N=0$ lands in $\Sigma_{01}$; a path that reaches both lands in $\Sigma_{00}$. The scalar line is the rest-frame part of the boundary $B=0$, and the Jordan part is its exceptional-point part; the cell $\Sigma_{01}$ is the boundary component $N=0$ with $B\neq0$.

## Physical Interpretations

- **The cell is a particle in motion.** On the material slice the two eigenvalues are the two light-cone frequencies of one momentum, and the pair is the Doppler pair. The cell is the spectral form of relativistic kinematics: mass is the product, energy the sum, momentum the difference, rapidity the ratio.
- **The two terms are two null components, not two particles.** Each term is a complex multiple of a minimal idempotent. Their sum is one element, their coefficients sum to $2iE/c$, and their product is $-m^2c^2$. A two-particle reading would need two independent mass-shell conditions; the cell has one.
- **The causal sign is the sign of the norm.** Timelike and spacelike momenta share the cell because both conditions are non-zero; they differ in the sign of $N$ and in the placement of the eigenvalues on the imaginary axis. The cell is a spectral type, and the causal class is a second invariant read from the same element.
- **The eigenbasis is a frame attached to the element.** The two eigenspaces are unique; the idempotents are unique; the nilpotents inside each eigenspace are a gauge. The frame is not a laboratory frame, and the mode basis is not a measurement basis until a laboratory frame is chosen.
- **A spinor carries both modes.** Each minimal ideal is a complex plane on which the left action is diagonal with both eigenvalues. Chirality is the right eigenvalue. The reading is the algebraic form of the two-component spinor, not a derivation of the spin-statistics theorem.
- **The cell lies in the domain of the polar word.** Every element has a scale, a phase, a boost and a rotor. The frame is a coordinate on the cell; the word exists on the whole cell and degenerates on the boundary, failing when the modulus vanishes ($N=0$) and losing its axis data when the eigenvalues coalesce ($B=0$).
- **The cell is generic.** Its complement is the union of the two complex hypersurfaces $N=0$ and $B^2=0$, of measure zero. A generic element is a unit with two distinct modes; each cone is one complex equation, hence two real conditions, and a degeneracy is the vanishing of one of the two.
- **Invertibility is reversibility.** The element has an inverse, a logarithm up to the branch lattice, and a one-parameter group. The cell is the regime in which the element is a reversible process with a generator.

## Limits

The identification of the cell with a particle in motion needs the material slice and the four-momentum chart. In the full algebra the cell is a spectral type, and the names mass and motion are readings of $N$ and $B^2$, not definitions.

The two eigenvalues are not two energies and not two particles. The sum of the coefficients is $2iE/c$, and the product is $-m^2c^2$; the individual coefficients are frame-dependent null components.

The cell contains the spacelike branch. The name "mass in motion" describes the timelike branch; a spacelike momentum has $N>0$ and its "mass" is imaginary. The cell is not a causal class.

The spinor reading is algebraic. The two minimal ideals are the two chiral spaces of the algebra; the identification with physical chirality and with the spin-statistics theorem is an extra step, not a theorem of the cell.

No dynamics is supplied. The cell is a property of one element at one instant; the article does not say how the element evolves, and it does not supply a mass spectrum.

## Summary

- $\Sigma_{11}=\{N\neq0,\ B^2\neq0\}$ is the complement of the two cones, open, dense and of real dimension eight.
- Its elements are units with two distinct non-zero eigenvalues $\lambda_\pm=Q_t\pm iB$, and the spectral decomposition has two non-zero terms.
- On the material slice the pair is the Doppler pair $i\,mc\,e^{\pm\psi}$; the sum is $2iE/c$, the difference $2i\lvert\vec p\rvert$, the product $-m^2c^2$.
- The sign of $N$ separates the timelike branch (eigenvalues on the same imaginary half) from the spacelike branch (opposite halves).
- The eigenbasis is unique, the Peirce decomposition is diagonal with both coefficients non-zero, and the spinor spaces each carry both eigenvalues.
- The cell is inverse-closed and not product-closed; products land in $\Sigma_{11}$ or in $\Sigma_{10}$, on its scalar line or its Jordan part.
- The cell lies in the domain of the polar word: scale, phase, boost and rotor.
- The boundary of the cell is the arrangement: $B=0$ gives the rest frame and the exceptional point, $N=0$ gives the light ray.
- The cell is generic and reversible; it supplies no dynamics, no particle count and no mass spectrum.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Sigma_{11}$ | the cell $N\neq0$, $B^2\neq0$ |
| $N=Q_t^2+B^2$ | the norm |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the vector square, the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $e_\pm$ | the spectral idempotents |
| $\tilde\Pi_\pm,\vec\Upsilon_\pm$ | the normalised Peirce basis |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two spinor spaces |
| $\psi$ | the rapidity, $\cosh\psi=E/(mc)$ |
| $r,\alpha,\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the polar factors |

## Further Reading

- [The Four Regimes of an Element: Mass and Motion](the-four-regimes-of-an-element-mass-and-motion.html), for the partition and the other three cells.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the Doppler pair and the two-term writing.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the polar word.
- [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html), for the sandwich and the boost.
- [Spin and the Two State Spaces](spin-and-the-two-state-spaces.html), for the minimal ideals.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the boundary $N=0$.
- [The N-Regular, Spectrally Degenerate Sector: The Rest Frame and the Exceptional Point](the-n-regular-spectrally-degenerate-sector-the-rest-frame-and-the-exceptional-point.html), for the boundary $B=0$.
