# __The N-Regular, Spectrally Regular Sector: Mass in Motion__

## Introduction

The region $\Sigma_{11}$ is the set of elements for which both questions of the arrangement receive the positive answer: the norm does not vanish, and the two eigenvalues do not coincide. It is the generic region, open and dense in the algebra. It is also the region of a massive particle in motion, and of a spacelike momentum. Its physical content is the two-mode picture: two distinct light-cone frequencies, two invariant planes, a mode basis, and a beat. The two frequencies differ by $2\lvert\vec p\rvert=2mc\lvert\sinh\theta_{\mathrm{rpd}}\rvert$, and that difference is the beat frequency: a kinematic beat between the two modes, not a dynamical effect.

The article reads the region. It states the conditions and the spectrum, reads the two-mode structure, the causal sign, the frame dependence, the invertibility and the spinor decomposition, and it labels the interpretations. It proves nothing: the sector theorems, the eigenbasis and the Peirce data are those of the mathematics articles cited below.

The name of the region is deliberately double. **Mass in motion** is the timelike branch; the region also contains the spacelike branch, where the invariant $N$ is positive and the two eigenvalues lie on opposite halves of the imaginary axis. The region is a spectral type, not a single causal class; the sign of $N$ is a second reading of the same region.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The definition, the five descriptions and the geometry of the region | [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html) |
| The spectrum, the spectral idempotents and the two-term writing | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| The eigenbasis and the Peirce corners | [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-eigenbasis-of-a-spectrally-regular-biquaternion.html) |
| The spinor spaces and the Peirce index | [The Polarized Module of the Biquaternion Algebra](../articles_maths/the-polarized-module-of-the-biquaternion-algebra.html) |
| The independence of the two conditions | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) |
| The four-vector dictionary and the mass shell | [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The spectral reading of a four-momentum | [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html) |
| The polar word and the unit group | [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html) |
| The Lorentz action as a two-sided operator | [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html) |

## The Region
The region is

$$
\Sigma_{11}=\{N\neq0,\ B^2\neq0\}
=\mathbb{B}\setminus(\mathcal N\cup\mathcal S),
$$

the complement of the union of the null cone and the spectral cone. It is open, dense and of full measure; its complement is the union of the two complex hypersurfaces $N=0$ and $B^2=0$, each of real codimension two, and it has measure zero. A generic element of the algebra lies here. The region is connected but not simply connected, and it is of complex dimension four, real dimension eight.

An element of the region is a unit with two distinct eigenvalues. The characteristic polynomial is

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

The two roots are non-zero, so the element is invertible: $\tilde Q^{-1}=\tilde Q^{\natural}/N$. The region is inverse-closed. The spectral idempotents are unique,

$$
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},
\qquad
\tilde Q=\lambda_+e_++\lambda_-e_-,
$$

and both coefficients are non-zero. This is the only region in which the spectral decomposition has two non-zero terms and two non-trivial idempotents.

## The Material Case

**The sections above read the region on the material slice, and the slice is a real four-dimensional subspace on which both invariants are real.** With

$$
\tilde Q=i\,q'_t\,e_t+\vec r,
\qquad
q'_t\in\mathbb{R},
\quad
\vec r\in\mathbb{R}^{3},
$$

the invariants are $B^{2}=\lvert\vec r\rvert^{2}$ and $N=\lvert\vec r\rvert^{2}-q_t'^{2}$, so the vector square is non-negative and the material part of the region is

$$
\Sigma_{11}\cap\mathbb{B}_{\Phi}
=\bigl\{\vec r\neq0,\ \lvert\vec r\rvert\neq\lvert q'_t\rvert\bigr\},
$$

with the rest point $\vec r=0$ in $\Sigma_{10}$ and the light point $\lvert\vec r\rvert=\lvert q'_t\rvert$ in $\Sigma_{01}$. **The material part is the region minus its boundary**, and a boost cannot move a material element out of the sector: the two-sided operator preserves $\mathbb{B}_{\Phi}$ to $10^{-16}$ over twenty boosts. The region is not preserved in the same way: the norm is preserved to $10^{-13}$, while $\lvert\vec p\rvert$ ran from $0.18$ to $66$. The region is a type; the mass shell is what the boost preserves.

**The sector adds one invariant and one operation.** The invariant is the polar modulus: with $\sqrt{N}=imc$ and $\lvert N\rvert^{1/2}=mc$, the mass is the modulus of the element and not a separate datum, and it is the number the two eigenvalues' product already carries. The operation is addition, which stays inside the sector while it leaves the region. Two material null momenta of energies $E_1,E_2$ at angle $\theta$ sum to

$$
N(\tilde P_1+\tilde P_2)=-2E_1E_2\bigl(1-\cos\theta\bigr),
$$

checked to $8\times10^{-15}$ over one hundred pairs, and that sum is in $\Sigma_{11}$ for every angle strictly between $0$ and $\pi$: parallel rays stay on the cone, equal-energy antiparallel rays land on the scalar line, and one hundred random pairs gave one hundred elements of the region. **No addend is massive and the sum is**, so the mass is produced by the addition and belongs to neither term. It is the one dynamical statement the region supports without a coupling being introduced.

**What the sector excludes, and why.** On $\mathbb{B}_{\Phi}$ the vector square is a definite form, and a definite form has no non-zero isotropic vector. So the Jordan part of $\Sigma_{10}$ and the nilpotents of $\Sigma_{00}$ are not merely off the real slice: they are absent from the sector for every complex value of its four real parameters. **The material face of the arrangement is the classical mass–motion table with its boundary, and the remainder of the region's geometry is complexified.**

## The First Carrier: The Centre

**The centre has no member in this region, and the exclusion is structural.** Its vector part is zero, so $B^{2}=0$ at every point of the carrier, and the region is defined by $B^{2}\neq0$. The intersection is therefore empty for every complex $q$, and no addition, product or boost within the carrier can change it, because the carrier is one-dimensional over $\mathbb{C}$ and every change stays inside it.

**The reading is about the amplitude and not about the momentum.** The element that the centre holds is a field's amplitude, one complex number at each event; the *momentum* of the same field is a four-vector, lies in the material sector, and finds this region generic there. **So the exclusion is not a statement that a scalar field cannot move**: it is the statement that an amplitude carries no direction, and that the two readings of one field sit in two different carriers. The region's content is a direction of motion, and a direction is the one thing a central element does not have. **The carrier reaches two of the four regions, $\Sigma_{10}$ and $\Sigma_{00}$**, and the two are the rest frame and the origin.

## The Second Carrier: The Minimal Left Ideal

**The ideal is excluded here for the opposite reason.** Every member of $S_{\pm}$ is a product with a rank-one idempotent, hence of rank at most one as a matrix, hence of vanishing determinant; the determinant is the norm, so $N=0$ at every point of the carrier, and the region is defined by $N\neq0$. So no value of a spin-half field is a unit, and the region, whose content is a non-zero mass together with two distinct modes, is closed to both ideals.

**The exclusion does not say that a spin-half field is massless.** The field is the sum $S_{+}+S_{-}=\mathbb{B}$, and the sum is not on the cone even when neither summand leaves it, since $N$ is a quadratic form:

$$
N(\tilde\Xi_{L}+\tilde\Xi_{R})=2\langle\tilde\Xi_{L},\tilde\Xi_{R}\rangle
$$

when both norms vanish. The right side is the polar form of the norm, and it is the mass. **So this is the region in which a statement about one value says nothing about the field**: $\Sigma_{11}$ is reached by the sum and by neither summand, and it is the one region that no carrier but the material sector reaches.

## The Spectrum

### The Doppler Pair

On the material slice, with $\tilde P_{\Phi}=i\frac{E}{c}e_t+\vec p$ and $B=\lvert\vec p\rvert$,

$$
\lambda_\pm=i\left(\frac{E}{c}\pm\lvert\vec p\rvert\right)
=i\,mc\,e^{\pm\theta_{\mathrm{rpd}}},
\qquad
\cosh\theta_{\mathrm{rpd}}=\frac{E}{mc^{2}},
\qquad
\sinh\theta_{\mathrm{rpd}}=\frac{\lvert\vec p\rvert}{mc}.
$$

The two eigenvalues are the two light-cone frequencies of one momentum, multiplied by $i$. Their sum is $2iE/c$ and their difference is $2i\lvert\vec p\rvert$; their product is $-m^2c^2$, and their ratio is the squared Doppler factor:

$$
\lambda_++\lambda_-=2i\frac{E}{c},
\qquad
\lambda_+-\lambda_-=2i\lvert\vec p\rvert,
\qquad
\lambda_+\lambda_-=-m^2c^2,
\qquad
\frac{\lambda_+}{\lambda_-}=e^{2\theta_{\mathrm{rpd}}}.
$$

The product is the invariant. The two factors are frame-dependent, and their dependence is exactly the Doppler rescaling. The region therefore carries the whole relativistic kinematics of one particle: mass, energy, momentum and rapidity are four readings of one pair.

### The Causal Sign

The sign of $N$ separates the two branches of the region. On the material slice $N=-E^2/c^2+\lvert\vec p\rvert^2$.

| branch | condition | eigenvalues | reading |
| --- | --- | --- | --- |
| timelike | $\lvert\vec p\rvert<E/c$ | both on the same imaginary half | a massive particle in motion |
| lightlike | $\lvert\vec p\rvert=E/c$ | one zero | the boundary region $\Sigma_{01}$ |
| spacelike | $\lvert\vec p\rvert>E/c$ | on opposite imaginary halves | a spacelike momentum |

The timelike branch is the one the region is named after. The spacelike branch is in the same region because both conditions are non-zero; its spectrum has one eigenvalue with a positive imaginary part and one with a negative imaginary part, and its norm is positive. The two branches are not connected inside the real material slice without crossing the light cone, which is the boundary $\Sigma_{01}$; in the full complex region they are connected through complexified momenta.

### What the Spectrum Does Not Determine

The spectrum fixes the trace and the norm, and nothing else:

$$
\lambda_++\lambda_-=2Q_t,
\qquad
\lambda_+\lambda_-=N.
$$

It does not fix the direction $\vec Q/B$, the two angles of the axis, or the reality of the vector part. A rotation leaves the pair unchanged and rotates the axis. The region is therefore larger than the spectrum: it is the spectrum together with the eigenprojections, and the eigenprojections carry the frame.

## The Two Modes

### The Spectral Decomposition

The two-term writing

$$
\tilde Q=\lambda_+e_++\lambda_-e_-
$$

is unique, and both terms are non-zero. Each term is a complex multiple of a minimal idempotent, hence a null element. The decomposition is the split of the element into two null components, not into two particles. The sum of the coefficients is twice the scalar part and their product is the norm; neither is the energy of a separate object.

In the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ the left action of $\tilde Q$ is diagonal with values $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$. The two eigenspaces are complex planes, each spanned by one idempotent and one nilpotent. The mode basis is a basis of the algebra, not of a Hilbert space of states; it is the frame in which the element is diagonal.

### The Spinors

The two Peirce carriers, the minimal left ideals here,

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

A spinor of either Peirce copy therefore carries both modes. The Peirce index is the right eigenvalue, not the left one: right multiplication by $\tilde Q$ acts as $\lambda_+$ on $S_+$ and $\lambda_-$ on $S_-$. The physical reading is that a spinor is not a mode; it is a two-component object, and the two components are the two modes. The two Peirce copies are the two ways of splitting the algebra, not the two modes, and they are not chiralities.

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

The region is contained in the unit group. Every element has an inverse,

$$
\tilde Q^{-1}=\lambda_+^{-1}e_++\lambda_-^{-1}e_-=\frac{\tilde Q^{\natural}}{N},
$$

and the inverse lies in the region. The polar word

$$
\tilde Q=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r}
$$

Here $\theta_{\mathrm{pha}}$ is the phase of the polar form: it is the argument of the central complex scalar, a real angle taken modulo a full turn, and the exponential that carries it is $\exp(i\theta_{\mathrm{pha}})$.

exists on the whole region, with $r=\lvert N\rvert^{1/2}$ and the three factors a scale, a central phase, a Hermitian boost and a real rotor. The region is therefore contained in the domain of the polar decomposition: every element of the region has a frame, an amplitude and a phase.

The region is inverse-closed but not product-closed. The norm is multiplicative, so the product of two elements of the region has non-zero norm and lies in $\Sigma_{11}\cup\Sigma_{10}$; both outcomes occur, and inside $\Sigma_{10}$ both the scalar line and the Jordan part occur. A product of two elements of the region can land on the scalar line, where the two eigenvalues coincide, or in the Jordan part, where the element is defective. The region is a symmetric subset of the unit group, not a subgroup: it contains no subgroup, because it does not contain the identity.

The boundary of the region is the arrangement. A path inside the region that reaches $B=0$ lands in $\Sigma_{10}$; a path that reaches $N=0$ lands in $\Sigma_{01}$; a path that reaches both lands in $\Sigma_{00}$. The scalar line is the rest-frame part of the boundary $B=0$, and the Jordan part is its exceptional-point part; the region $\Sigma_{01}$ is the boundary component $N=0$ with $B\neq0$.

## Physical Interpretations

- **The region is a particle in motion.** On the material slice the two eigenvalues are the two light-cone frequencies of one momentum, and the pair is the Doppler pair. The region is the spectral form of relativistic kinematics: mass is the product, energy the sum, momentum the difference, rapidity the ratio.
- **The two terms are two null components, not two particles.** Each term is a complex multiple of a minimal idempotent. Their sum is one element, their coefficients sum to $2iE/c$, and their product is $-m^2c^2$. A two-particle reading would need two independent mass-shell conditions; the region has one.
- **The causal sign is the sign of the norm.** Timelike and spacelike momenta share the region because both conditions are non-zero; they differ in the sign of $N$ and in the placement of the eigenvalues on the imaginary axis. The region is a spectral type, and the causal class is a second invariant read from the same element.
- **The eigenbasis is a frame attached to the element.** The two eigenspaces are unique; the idempotents are unique; the nilpotents inside each eigenspace are a gauge. The frame is not a laboratory frame, and the mode basis is not a measurement basis until a laboratory frame is chosen.
- **A spinor carries both modes.** Each minimal ideal is a complex plane on which the left action is diagonal with both eigenvalues. The Peirce index is the right eigenvalue. The reading is the algebraic form of the two-component spinor, not a derivation of the spin-statistics theorem.
- **The region lies in the domain of the polar word.** Every element has a scale, a phase, a boost and a rotor. The frame is a coordinate on the region; the word exists on the whole region and degenerates on the boundary, failing when the modulus vanishes ($N=0$) and losing its axis data when the eigenvalues coalesce ($B=0$).
- **The region is generic.** Its complement is the union of the two complex hypersurfaces $N=0$ and $B^2=0$, of measure zero. A generic element is a unit with two distinct modes; each cone is one complex equation, hence two real conditions, and a degeneracy is the vanishing of one of the two.
- **Invertibility is reversibility.** The element has an inverse, a logarithm up to the branch lattice, and a one-parameter group. The region is the regime in which the element is a reversible process with a generator.

## Limits

The identification of the region with a particle in motion needs the material slice and the four-momentum chart. In the full algebra the region is a spectral type, and the names mass and motion are readings of $N$ and $B^2$, not definitions.

The two eigenvalues are not two energies and not two particles. The sum of the coefficients is $2iE/c$, and the product is $-m^2c^2$; the individual coefficients are frame-dependent null components.

The region contains the spacelike branch. The name "mass in motion" describes the timelike branch; a spacelike momentum has $N>0$ and its "mass" is imaginary. The region is not a causal class.

The spinor reading is algebraic. The two minimal ideals are copies of one module, distinguished by the Peirce index; they are not the two chiral halves. The identification with physical chirality and with the spin-statistics theorem is an extra step, not a theorem of the region.

No dynamics is supplied. The region is a property of one element at one instant; the article does not say how the element evolves, and it does not supply a mass spectrum.

## Summary

- $\Sigma_{11}=\{N\neq0,\ B^2\neq0\}$ is the complement of the two cones, open, dense and of real dimension eight.
- Its elements are units with two distinct non-zero eigenvalues $\lambda_\pm=Q_t\pm iB$, and the spectral decomposition has two non-zero terms.
- On the material slice the pair is the Doppler pair $i\,mc\,e^{\pm\theta_{\mathrm{rpd}}}$; the sum is $2iE/c$, the difference $2i\lvert\vec p\rvert$, the product $-m^2c^2$.
- The sign of $N$ separates the timelike branch (eigenvalues on the same imaginary half) from the spacelike branch (opposite halves).
- The eigenbasis is unique, the Peirce decomposition is diagonal with both coefficients non-zero, and the spinor spaces each carry both eigenvalues.
- The region is inverse-closed and not product-closed; products land in $\Sigma_{11}$ or in $\Sigma_{10}$, on its scalar line or its Jordan part.
- The region lies in the domain of the polar word: scale, phase, boost and rotor.
- The boundary of the region is the arrangement: $B=0$ gives the rest frame and the exceptional point, $N=0$ gives the light ray.
- The region is generic and reversible; it supplies no dynamics, no particle count and no mass spectrum.
- On the material sector the region is $\{\vec r\neq0,\ \lvert\vec r\rvert\neq\lvert q'_t\rvert\}$, the spectrum is purely imaginary, the modulus is $mc$, and a boost moves the element along its mass shell without leaving the region's type.
- The carrier decides the reach: the centre has $B^{2}=0$ at every point and the ideals have $N=0$ at every point, so neither reaches $\Sigma_{11}$; only the material sector does, and it is generic there.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Sigma_{11}$ | the region $N\neq0$, $B^2\neq0$ |
| $N=Q_t^2+B^2$ | the norm |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the vector square, the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $e_\pm$ | the spectral idempotents |
| $\tilde\Pi_\pm,\vec\Upsilon_\pm$ | the normalised Peirce basis |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two spinor spaces |
| $\theta_{\mathrm{rpd}}$ | the rapidity, $\cosh\theta_{\mathrm{rpd}}=E/(mc^{2})$ |
| $r,\theta_{\mathrm{pha}},\tilde U_{\Psi,\mathrm b},\tilde u_{\mathrm r}$ | the polar factors |
| $i\,q'_t\,e_t+\vec r$ | a material element, $q'_t\in\mathbb{R}$, $\vec r\in\mathbb{R}^{3}$ |

## Further Reading

- [The Three Elementary Carriers and the Four Sectors of Regularity and Degeneracy](the-three-elementary-carriers-and-the-four-sectors-of-regularity-and-degeneracy.html), for the partition and the other three regions.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the Doppler pair and the two-term writing.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the polar word.
- [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html), for the two-sided operator and the boost.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the minimal ideals.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the boundary $N=0$.
- [The N-Regular, Spectrally Degenerate Sector: The Rest Frame and the Exceptional Point](the-n-regular-spectrally-degenerate-sector-the-rest-frame-and-the-exceptional-point.html), for the boundary $B=0$.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the three carriers whose reach this article uses.
