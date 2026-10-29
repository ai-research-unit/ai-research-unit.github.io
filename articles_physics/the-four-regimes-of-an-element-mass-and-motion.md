# __The Four Regimes of an Element: Mass and Motion__

## Introduction

A biquaternion carries two quadratic numbers invariant under the algebra's automorphisms, and each answers a physical question. The first is the norm

$$
N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2,
\qquad B^2=Q_x^2+Q_y^2+Q_z^2 .
$$

On the material sector $N$ is the interval, and on a four-momentum it is $-m^2c^2$: it answers **is there a mass, and of which causal sign?** The second is the vector square $B^2$. It is the discriminant of the characteristic polynomial, and it answers **are there two distinct modes?** On a four-momentum $B=\lvert\vec p\rvert$: it answers **is the element in motion?**

The two questions are independent, and their four answers partition the algebra:

$$
\Sigma_{ij}=\{N=0\text{ iff }i=0,\quad B^2=0\text{ iff }j=0\}.
$$

The partition is the subject of this article. It is not a classification of mathematical cases with physical labels added afterwards. It is the mass–motion classification of a four-momentum, extended to the full complex algebra, and each cell is a different physical regime with its own spectral behaviour, its own invertibility, and its own relation to the mass shell and the light cone.

The four cells are treated one to an article: *The N-Regular, Spectrally Regular Sector: Mass in Motion* for $\Sigma_{11}$, *The N-Regular, Spectrally Degenerate Sector: The Rest Frame and the Exceptional Point* for $\Sigma_{10}$, *The N-Degenerate, Spectrally Regular Sector: The Massless Regime* for $\Sigma_{01}$, and *The N-Degenerate, Spectrally Degenerate Sector: The Vacuum and the Nilpotent Ladder* for $\Sigma_{00}$. This article states the partition, the table, the real slices and the limits of the reading. It proves nothing; the sector theorems are those of the four mathematics articles cited below.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The norm, the null cone and its two strata | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| The characteristic polynomial, the discriminant and the two eigenvalues | [The Spectrum](../articles_maths/the-spectrum.html) |
| The independence of the two conditions and the four sectors | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) |
| The doubly regular sector | [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html) |
| The norm-regular, spectrally degenerate sector | [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html) |
| The norm-degenerate, spectrally regular sector | [The N-Degenerate, Spectrally Regular Sector](../articles_maths/the-n-degenerate-spectrally-regular-sector.html) |
| The doubly degenerate sector | [The N-Degenerate, Spectrally Degenerate Sector](../articles_maths/the-n-degenerate-spectrally-degenerate-sector.html) |
| The four-vector dictionary and the interval | [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The spectral reading of a four-momentum | [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html) |
| The massless cone and its spectrum | [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html) |
| The fermionic interpretation of the nilpotents | [The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge](the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html) |

## The Two Questions

### The Norm: Mass and Causal Sign

The norm is the constant term of the characteristic polynomial,

$$
p_{\tilde Q}(X)=X^2-2Q_tX+N,
\qquad N=Q_t^2+B^2 .
$$

It is multiplicative, $\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$, and its vanishing set is the null cone $\mathcal N$, the set of zero divisors. On the material sector, with $\tilde P=i\frac{E}{c}e_t+\vec p$,

$$
N=-\frac{E^2}{c^2}+\lvert\vec p\rvert^2=-m^2c^2 .
$$

The sign of $N$ is the causal sign: negative timelike, zero lightlike, positive spacelike. The norm therefore answers two questions at once: whether there is an invariant magnitude, and which causal class that magnitude carries. The second is a property of the real slice; in the full algebra $N$ is complex, and only its vanishing is invariant under the full structure.

### The Vector Square: Motion

The vector square is the discriminant,

$$
\operatorname{disc}p_{\tilde Q}=-4B^2,
\qquad \lambda_\pm=Q_t\pm iB .
$$

It vanishes exactly when the two eigenvalues coincide. On a four-momentum $B=\lvert\vec p\rvert$, so the condition $B^2=0$ is the condition $\vec p=0$: the element is at rest. The second question is therefore **motion**: a four-momentum has two distinct light-cone frequencies exactly when it moves, and one frequency when it is at rest.

The identification is not a metaphor. The eigenvalues are $\lambda_\pm=i(E/c\pm\lvert\vec p\rvert)$, and their difference is $2i\lvert\vec p\rvert$. The splitting is twice the momentum. The rest frame is the only frame in which the splitting vanishes, and it is the only frame in which the two-term spectral writing is not unique.

### Why the Two Questions Are Independent

The two conditions are two quadratic equations in four complex variables, and neither implies the other. The mixed cells are the witnesses:

$$
e_t+i\vec e_x\in\Sigma_{01}
\qquad(N=0,\ B^2=-1),
$$

$$
e_t+\vec e_x\in\Sigma_{11}
\qquad(N=2,\ B^2=1),
$$

$$
i e_t\in\Sigma_{10}
\qquad(N=-1,\ B^2=0),
$$

$$
\vec e_x+i\vec e_y\in\Sigma_{00}
\qquad(N=0,\ B^2=0).
$$

The first is a zero divisor with two distinct modes; the second is a unit with two distinct modes; the third is a unit with one mode; the fourth is a zero divisor with one mode. The four together are the proof that mass and motion are independent questions: each combination occurs.

The independence is also the reason the partition is fourfold and not twofold. The norm alone gives the unit group and the null cone. The discriminant alone gives the regular and the degenerate cone. The arrangement of the two cones is the four-cell partition, and the cells are the four combinations.

## The Table

| cell | conditions | spectrum | invertible? | Peirce decomposition | real material slice | physical name |
| --- | --- | --- | --- | --- | --- | --- |
| $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | $\{\lambda_+,\lambda_-\}$ distinct, both non-zero | yes | unique, both coefficients non-zero | timelike or spacelike momentum with $\vec p\neq0$ | **mass in motion** |
| $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | $\{Q_t\}$ repeated | yes | one term on the scalar line; none on the Jordan part | a massive momentum at rest; the complex Jordan part is the exceptional point | **rest frame and exceptional point** |
| $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | $\{2Q_t,0\}$ distinct | no | unique, one coefficient zero | a massless momentum, $\vec p\neq0$ | **light ray** |
| $\Sigma_{00}$ | $N=0$, $B^2=0$ | $\{0\}$ | no | none off the origin | the zero momentum, and nothing else | **vacuum and nilpotent ladder** |

The last two columns are the interpretive step, and they are the reason the table is worth an article. The first five columns are algebraic; the last two say what the algebra is a table of.

The table is exhaustive: every element lies in exactly one cell. The cells are the four combinations of the two conditions; the two cones are their boundaries, and the origin lies in the closure of all four.

## The Four Regimes

### Mass in Motion: $\Sigma_{11}$

The generic cell. The element is a unit with two distinct eigenvalues, and it is the only cell in which the spectral decomposition has two non-zero coefficients. On the material sector it is a timelike momentum with $\vec p\neq0$ or a spacelike momentum. The eigenvalues are the two light-cone frequencies $mc\,e^{\pm\psi}$ multiplied by $i$; the product is $-m^2c^2$ and the ratio is the squared Doppler factor. The cell is open and dense, of real dimension eight, and its complement is the arrangement.

The physical content is the **two-mode picture**: two invariant planes, a mode basis, a beat, and a unique decomposition of the element into two null components. It is the regime in which a particle has both a mass and a direction of motion, and in which the mass shell is a level set rather than the cell itself.

### The Rest Frame and the Exceptional Point: $\Sigma_{10}$

The cell of units with a repeated eigenvalue. It has two faces. The **scalar line** $Q_te_t$ is the real rest frame: $\vec p=0$, $B=0$, $N=Q_t^2$, and the single eigenvalue $Q_t=iE/c$. It is semisimple, every basis is an eigenbasis, and the two-term writing is not unique. The **Jordan part** $Q_t e_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ is defective: one eigenvalue, a Jordan block, no eigenbasis, a shear. It is not on the real material slice, because a real spatial vector has $B^2=\lvert\vec p\rvert^2$, which vanishes only at $\vec p=0$.

The physical content is therefore double. The scalar line is **the rest frame**: the frame in which the momentum is purely temporal and the two light-cone frequencies coincide. The Jordan part is **the exceptional point**: a complexified momentum at which two modes have coalesced and the operator has become defective. The two share the algebra $N\neq0$, $B^2=0$; they do not share a physics.

### The Light Ray: $\Sigma_{01}$

The cell of zero divisors with two distinct eigenvalues. The element is a non-zero multiple of a non-trivial idempotent, $\tilde Q=\kappa\tilde\Pi$ with $\kappa=2Q_t\neq0$, and its spectrum is $\{\kappa,0\}$. On the material sector it is the light cone minus the apex: a massless momentum, with one light-cone eigenvalue zero and the other $2iE/c$. It has a unique Peirce decomposition, a mode basis, and no rest frame: one eigenvalue is zero, so there is no frame in which the two eigenvalues coincide.

The physical content is the **light ray**: a rank-one element, a direction and a scale; a spinor representative adds a little-group phase. It is a zero divisor, hence not invertible; it has no logarithm and no generator. The cell is part of the boundary of the unit group: the null cone with its vertex and the doubly degenerate cone removed.

### The Vacuum and the Nilpotent Ladder: $\Sigma_{00}$

The cell of square-zero elements. Off the origin the element is a pure nilpotent, $\tilde Q=\vec\Upsilon$ with $\vec\Upsilon^2=0$; the origin is the only semisimple point. On the material sector the cell contains only the origin: a real four-momentum with $N=0$ and $B=0$ has $Q_t=0$ and $\vec p=0$. The non-zero nilpotents are not physical null four-momenta; they are the algebraic ladder.

The physical content is therefore the **vacuum** together with its **nilpotent excitations**. The origin is the unique zero-momentum, zero-scale element. The nilpotents are the one-site fermionic ladder: two nilpotents with anticommutator $e_t$, whose products are orthogonal idempotents in $\Sigma_{01}$. The cell is the common boundary of the other three; its origin is the apex and the common limit.

## The Real Slices

The table is a table of the full algebra. A physical four-momentum is a point of a real four-dimensional slice, and the slice selects part of each cell.

### The Material Slice

On $\mathbb{M}_-$ the coordinates are $Q_t=ict'$ and $\vec Q=(x,y,z)$ real. Hence

$$
B^2=x^2+y^2+z^2\ge0,
\qquad
N=-c^2t'^2+x^2+y^2+z^2 .
$$

The vector square is non-negative and vanishes exactly at the spatial origin. The material slice therefore meets the four cells as follows.

| cell | intersection with $\mathbb{M}_-$ |
| --- | --- |
| $\Sigma_{11}$ | timelike momenta with $\vec p\neq0$, and spacelike momenta |
| $\Sigma_{10}$ | the scalar line $Q_t\neq0$, $\vec p=0$: the rest frame |
| $\Sigma_{01}$ | the light cone minus the apex: massless momenta |
| $\Sigma_{00}$ | the origin only |

This is the mass–motion table of a real four-momentum. A real momentum has two distinct modes exactly when it moves. At rest it has one mode. On the light cone it has one zero mode. At the origin it has neither.

The table also shows what is **not** on the real slice: the Jordan part of $\Sigma_{10}$ and the non-zero nilpotents of $\Sigma_{00}$. Both need a complex isotropic spatial vector. They are regimes of the complexified algebra, not of a real four-momentum, and the physics articles that use them say so.

### The Informational Slice

On $\mathbb{M}_+$ the coordinates are $Q_t=ct$ real and $\vec Q=i(x',y',z')$. Hence

$$
B^2=-(x'^2+y'^2+z'^2)\le0,
\qquad
N=c^2t^2-x'^2-y'^2-z'^2 .
$$

The vector square is non-positive and vanishes exactly at the spatial origin. The slice meets $\Sigma_{10}$ on the scalar line $x'=y'=z'=0$ and meets $\Sigma_{00}$ only at the origin. The mirror symmetry is exact: on each real slice the vector square has a definite sign, and the spectral cone cuts the slice only along the scalar line.

The sign reversal is the content of the sector bridge. The same $B^2$ is non-negative on matter and non-positive on information, and the same norm is the interval on one and minus the interval on the other. The four-cell partition is the same partition on both slices; the mirror reverses the signs, not the cells.

## The Mass Shell and the Light Cone

The four cells are not the mass shell and the light cone. They are the regions cut by the two cones, and the physically distinguished level sets cut across them.

- The **mass shell** $N=-m^2c^2$ is a level set of the norm. It lies in $\Sigma_{11}$ for $\vec p\neq0$ and meets $\Sigma_{10}$ at the rest point $\vec p=0$. It is not a cell: it is a hypersurface that crosses the spectral cone at the rest frame.
- The **light cone** $N=0$ is the union of $\Sigma_{01}$ and the doubly degenerate cell $\Sigma_{00}$. It is the boundary of the unit group and the set of zero divisors.
- The **spectral cone** $B^2=0$ is the union of $\Sigma_{10}$ and $\Sigma_{00}$. It is the set of elements with a repeated eigenvalue.
- The **origin** lies on both cones and in the closure of all four cells. The intersection of the two cones is the doubly degenerate cell $\Sigma_{00}$.

The reading is the reason the partition is physically useful. A particle is not a cell; a particle is a level set of $N$ together with a motion class. The four cells tell what kind of spectral object the level set is made of. A massive particle at rest and a massive particle in motion are in different cells, although they lie on the same mass shell; a massless particle and the vacuum are in different cells, although they lie on the same light cone.

## What the Table Does Not Say

The table is a partition of the algebra by two invariant values. It does not say that the four cells are phases of matter, that they evolve into one another, or that a physical system occupies one cell for all time. The cells are properties of one element at one instant.

The table does not supply a dynamics. It does not say how an element moves from one cell to another, and it does not supply a mass spectrum. The mass shell is a level set, not an equation of motion.

The table does not say that the non-zero nilpotents are physical. On the real material slice they are absent; in the full algebra they are the fermionic ladder, and the corpus's reading of them is algebraic, not a claim about physical statistics.

The table does not say that the cells are Lorentz invariant. The norm is invariant under a norm-one dagger sandwich, and the discriminant is not. A boost preserves $N$ and changes $B$, so it moves a massive element along its mass shell; in particular, it moves a massive element from the rest frame $\Sigma_{10}$ into $\Sigma_{11}$. The mass shell and the light cone are Lorentz invariant; the cells are not. A cell is a spectral type at an instant, not an orbit of the Lorentz group.

## Physical Interpretations

- **The partition is the mass–motion classification.** $N$ is the invariant mass-squared, and $B^2$ is the motion. The four cells are massive at rest, massive in motion, massless, and the vacuum, extended to the complex algebra.
- **The two questions are independent.** A zero divisor can have two modes, and a unit can have one. The mixed cells are the proof, and they are the reason the algebra needs four sectors and not two.
- **The spectrum is the pair of light-cone frequencies.** $\lambda_\pm=i(E/c\pm\lvert\vec p\rvert)$ on the material slice. The sum is $2iE/c$, the difference $2i\lvert\vec p\rvert$, and the product $-m^2c^2$.
- **The rest frame is the scalar line.** It is the only real momentum with one mode, and the only frame in which the spectral writing is not unique. The exceptional point is its complex neighbour, where the one mode is defective.
- **The light cone is the massless cell plus the doubly degenerate cell.** A massless momentum is a scaled idempotent: a rank-one element with one zero mode. The origin is the apex, the only element with no scale and no mode; the nilpotent directions complete the cell.
- **The mass shell crosses the cells.** A particle at rest and a particle in motion are on the same mass shell but in different cells; the cell is the spectral type, the shell is the value of the norm.
- **The real slices select half of the table.** On each real slice the vector square has a definite sign, so the spectral cone meets the slice only on the scalar line. The Jordan part and the nilpotents are complex regimes.
- **The arrangement is the boundary structure of the unit group.** The units are $\Sigma_{11}\cup\Sigma_{10}$; the zero divisors are $\Sigma_{01}\cup\Sigma_{00}$; the spectral cone is $\Sigma_{10}\cup\Sigma_{00}$; the origin is the common limit.

## Limits

The identification of $N$ with $-m^2c^2$ needs the material slice and the four-momentum chart. In the full algebra $N$ is complex, and calling it a mass is an extra identification.

The identification of $B$ with $\lvert\vec p\rvert$ needs the material slice. In the full algebra $B^2$ is a complex invariant, and "motion" is a name for the spectral splitting, not a velocity.

The table is a partition of elements, not of states. It does not say that a quantum state is in one cell, and it does not supply a Hilbert-space interpretation of the cells.

The non-zero nilpotents are not physical null four-momenta. On the real material slice the doubly degenerate cell contains only the origin.

The cells are not phases and not basins of attraction. No dynamics, no order parameter and no transition is claimed.

## Summary

- The norm $N=Q_t^2+B^2$ answers whether there is an invariant magnitude and, on the material slice, which causal sign it carries. On a four-momentum $N=-m^2c^2$.
- The vector square $B^2$ is the discriminant. It answers whether there are two distinct modes. On a four-momentum $B=\lvert\vec p\rvert$, so it answers whether the momentum moves.
- The two conditions are independent and partition the algebra into four cells: $\Sigma_{11}$ (mass in motion), $\Sigma_{10}$ (rest frame and exceptional point), $\Sigma_{01}$ (light ray), $\Sigma_{00}$ (vacuum and nilpotent ladder).
- $\Sigma_{11}$ is the generic unit with two distinct non-zero eigenvalues and a unique two-term spectral decomposition.
- $\Sigma_{10}$ is the unit with a repeated eigenvalue: the scalar line is the real rest frame, the Jordan part is the complex exceptional point.
- $\Sigma_{01}$ is the zero divisor with spectrum $\{2Q_t,0\}$: a scaled idempotent, a rank-one light ray.
- $\Sigma_{00}$ is the square-zero cell: the origin, the vacuum, and the non-zero nilpotents, the fermionic ladder.
- On the material slice $B^2\ge0$ and the spectral cone meets the slice only on the scalar line; the Jordan part and the nilpotents are complex regimes.
- The mass shell crosses $\Sigma_{11}$ and $\Sigma_{10}$; on the material slice the light cone is $\Sigma_{01}$ together with the apex. The cells are spectral types, not level sets.
- The table is a partition of elements at an instant. It supplies no dynamics, no mass spectrum and no phase structure.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the vector square, the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $\mathcal N=\{N=0\}$ | the null cone, the zero-divisor cone |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\Sigma_{ij}$ | the cell with $N=0$ iff $i=0$ and $B^2=0$ iff $j=0$ |
| $\mathbb{M}_-$ | the material slice, $Q_t=ict'$, $\vec Q$ real |
| $\mathbb{M}_+$ | the informational slice, $Q_t=ct$, $\vec Q$ imaginary |
| $\tilde P=i\frac{E}{c}e_t+\vec p$ | the four-momentum chart |
| $m$, $\vec p$, $\psi$ | mass, momentum, rapidity |

## Further Reading

- [The N-Regular, Spectrally Regular Sector: Mass in Motion](the-n-regular-spectrally-regular-sector-mass-in-motion.html), for $\Sigma_{11}$.
- [The N-Regular, Spectrally Degenerate Sector: The Rest Frame and the Exceptional Point](the-n-regular-spectrally-degenerate-sector-the-rest-frame-and-the-exceptional-point.html), for $\Sigma_{10}$.
- [The N-Degenerate, Spectrally Regular Sector: The Massless Regime](the-n-degenerate-spectrally-regular-sector-the-massless-regime.html), for $\Sigma_{01}$.
- [The N-Degenerate, Spectrally Degenerate Sector: The Vacuum and the Nilpotent Ladder](the-n-degenerate-spectrally-degenerate-sector-the-vacuum-and-the-nilpotent-ladder.html), for $\Sigma_{00}$.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the Doppler pair and the two-term writing.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the four-vector dictionary.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone and the massless limit.
