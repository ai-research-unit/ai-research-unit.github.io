# __The Three Elementary Carriers and the Four Sectors of Regularity and Degeneracy__

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

The partition is the subject of this article. It is not a classification of mathematical cases with physical labels added afterwards. It is the mass–motion classification of a four-momentum, extended to the full complex algebra, and each region is a different physical regime with its own spectral behaviour, its own invertibility, and its own relation to the mass shell and the light cone.

The four regions are treated one to an article: *The N-Regular, Spectrally Regular Sector: Mass in Motion* for $\Sigma_{11}$, *The N-Regular, Spectrally Degenerate Sector: The Rest Frame and the Exceptional Point* for $\Sigma_{10}$, *The N-Degenerate, Spectrally Regular Sector: The Massless Regime* for $\Sigma_{01}$, and *The N-Degenerate, Spectrally Degenerate Sector: The Vacuum and the Nilpotent Ladder* for $\Sigma_{00}$. This article states the partition, the table, the real slices and the limits of the reading. It proves nothing; the sector theorems are those of the four mathematics articles cited below.

**The partition is cut on the algebra, and a field is not free to sit in any region of it.** The three carriers of *Spin and the Three Elementary Carriers* each reach a fixed part of the partition, and the reach is decided by the one invariant the carrier pins. The centre has no vector part, so it is spectrally degenerate at every point and occupies only $\Sigma_{10}$ or $\Sigma_{00}$. The minimal left ideal consists of rank-one elements, so its norm vanishes at every point and it occupies only $\Sigma_{01}$ or $\Sigma_{00}$. Only the material sector has four independent real directions, and only it reaches mass in motion. **The four names of the table are therefore the names of a material classification**, and §*The Three Carriers* states the reach of each carrier region by region. The section is the article's second subject: the four regions were cut by the invariants without reference to any spin, and the carriers are where the spin enters.

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

It is multiplicative, $\langle\tilde P_{\Phi}\tilde Q\rangle_{\natural}=\langle\tilde P_{\Phi}\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$, and its vanishing set is the null cone $\mathcal N$, the set of zero divisors. On the material sector, with $\tilde P_{\Phi}=i\frac{E}{c}e_t+\vec p$,

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

The two conditions are two quadratic equations in four complex variables, and neither implies the other. The mixed regions are the witnesses:

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

The independence is also the reason the partition is fourfold and not twofold. The norm alone gives the unit group and the null cone. The discriminant alone gives the regular and the degenerate cone. The arrangement of the two cones is the four-region partition, and the regions are the four combinations.

## The Table

| region | conditions | spectrum | invertible? | Peirce decomposition | real material slice | physical name |
| --- | --- | --- | --- | --- | --- | --- |
| $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | $\{\lambda_+,\lambda_-\}$ distinct, both non-zero | yes | unique, both coefficients non-zero | timelike or spacelike momentum with $\vec p\neq0$ | **mass in motion** |
| $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | $\{Q_t\}$ repeated | yes | one term on the scalar line; none on the Jordan part | a massive momentum at rest; the complex Jordan part is the exceptional point | **rest frame and exceptional point** |
| $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | $\{2Q_t,0\}$ distinct | no | unique, one coefficient zero | a massless momentum, $\vec p\neq0$ | **light ray** |
| $\Sigma_{00}$ | $N=0$, $B^2=0$ | $\{0\}$ | no | none off the origin | the zero momentum, and nothing else | **vacuum and nilpotent ladder** |

The last two columns are the interpretive step, and they are the reason the table is worth an article. The first five columns are algebraic; the last two say what the algebra is a table of.

The table is exhaustive: every element lies in exactly one region. The regions are the four combinations of the two conditions; the two cones are their boundaries, and the origin lies in the closure of all four.

## The Four Regions

### Mass in Motion: $\Sigma_{11}$

The generic region. The element is a unit with two distinct eigenvalues, and it is the only region in which the spectral decomposition has two non-zero coefficients. On the material sector it is a timelike momentum with $\vec p\neq0$ or a spacelike momentum. The eigenvalues are the two light-cone frequencies $mc\,e^{\pm\tilde{Ξ}}$ multiplied by $i$; the product is $-m^2c^2$ and the ratio is the squared Doppler factor. The region is open and dense, of real dimension eight, and its complement is the arrangement.

The physical content is the **two-mode picture**: two invariant planes, a mode basis, a beat, and a unique decomposition of the element into two null components. It is the regime in which a particle has both a mass and a direction of motion, and in which the mass shell is a level set rather than the region itself.

### The Rest Frame and the Exceptional Point: $\Sigma_{10}$

The region of units with a repeated eigenvalue. It has two faces. The **scalar line** $Q_te_t$ is the real rest frame: $\vec p=0$, $B=0$, $N=Q_t^2$, and the single eigenvalue $Q_t=iE/c$. It is semisimple, every basis is an eigenbasis, and the two-term writing is not unique. The **Jordan part** $Q_t e_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ is defective: one eigenvalue, a Jordan block, no eigenbasis, a shear. It is not on the real material slice, because a real spatial vector has $B^2=\lvert\vec p\rvert^2$, which vanishes only at $\vec p=0$.

The physical content is therefore double. The scalar line is **the rest frame**: the frame in which the momentum is purely temporal and the two light-cone frequencies coincide. The Jordan part is **the exceptional point**: a complexified momentum at which two modes have coalesced and the operator has become defective. The two share the algebra $N\neq0$, $B^2=0$; they do not share a physics.

### The Light Ray: $\Sigma_{01}$

The region of zero divisors with two distinct eigenvalues. The element is a non-zero multiple of a non-trivial idempotent, $\tilde Q=\kappa\tilde\Pi$ with $\kappa=2Q_t\neq0$, and its spectrum is $\{\kappa,0\}$. On the material sector it is the light cone minus the apex: a massless momentum, with one light-cone eigenvalue zero and the other $2iE/c$. It has a unique Peirce decomposition, a mode basis, and no rest frame: one eigenvalue is zero, so there is no frame in which the two eigenvalues coincide.

The physical content is the **light ray**: a rank-one element, a direction and a scale; a spinor representative adds a little-group phase. It is a zero divisor, hence not invertible; it has no logarithm and no generator. The region is part of the boundary of the unit group: the null cone with its vertex and the doubly degenerate cone removed.

### The Vacuum and the Nilpotent Ladder: $\Sigma_{00}$

The region of square-zero elements. Off the origin the element is a pure nilpotent, $\tilde Q=\vec\Upsilon$ with $\vec\Upsilon^2=0$; the origin is the only semisimple point. On the material sector the region contains only the origin: a real four-momentum with $N=0$ and $B=0$ has $Q_t=0$ and $\vec p=0$. The non-zero nilpotents are not physical null four-momenta; they are the algebraic ladder.

The physical content is therefore the **vacuum** together with its **nilpotent excitations**. The origin is the unique zero-momentum, zero-scale element. The nilpotents are the one-site fermionic ladder: two nilpotents with anticommutator $e_t$, whose products are orthogonal idempotents in $\Sigma_{01}$. The region is the common boundary of the other three; its origin is the apex and the common limit.

## The Real Slices

The table is a table of the full algebra. A physical four-momentum is a point of a real four-dimensional slice, and the slice selects part of each region.

### The Material Slice

On $\mathbb{B}_{\Phi}$ the coordinates are $Q_t=i q'_t$ and $\vec Q=(r_x,r_y,r_z)$ real. Hence

$$
B^2=r_x^2+r_y^2+r_z^2\ge0,
\qquad
N=-{r'_{t}}^2+r_x^2+r_y^2+r_z^2 .
$$

The vector square is non-negative and vanishes exactly at the spatial origin. The material slice therefore meets the four regions as follows.

| region | intersection with $\mathbb{B}_{\Phi}$ |
| --- | --- |
| $\Sigma_{11}$ | timelike momenta with $\vec p\neq0$, and spacelike momenta |
| $\Sigma_{10}$ | the scalar line $Q_t\neq0$, $\vec p=0$: the rest frame |
| $\Sigma_{01}$ | the light cone minus the apex: massless momenta |
| $\Sigma_{00}$ | the origin only |

This is the mass–motion table of a real four-momentum. A real momentum has two distinct modes exactly when it moves. At rest it has one mode. On the light cone it has one zero mode. At the origin it has neither.

The table also shows what is **not** on the real slice: the Jordan part of $\Sigma_{10}$ and the non-zero nilpotents of $\Sigma_{00}$. Both need a complex isotropic spatial vector. They are regimes of the complexified algebra, not of a real four-momentum, and the physics articles that use them say so.

### The Informational Slice

On $\mathbb{B}_{\Psi}$ the coordinates are $Q_t=q_t$ real (with $q_t=h_t$) and $\vec Q=i(q'_{x},q'_{y},q'_{z})$ (with $q'_\eta=h'_\eta$). Hence

$$
B^2=-(h'_{x}^2+h'_{y}^2+h'_{z}^2)\le0,
\qquad
N=h_t^2-h'_{x}^2-h'_{y}^2-h'_{z}^2 .
$$

The vector square is non-positive and vanishes exactly at the spatial origin. The slice meets $\Sigma_{10}$ on the scalar line $h'_{x}=h'_{y}=h'_{z}=0$ and meets $\Sigma_{00}$ only at the origin. The mirror symmetry is exact: on each real slice the vector square has a definite sign, and the spectral cone cuts the slice only along the scalar line.

The sign reversal is the content of the sector bridge. The same $B^2$ is non-negative on matter and non-positive on information, and the same norm is the interval on one and minus the interval on the other. The four-region partition is the same partition on both slices; the mirror reverses the signs, not the regions.

## Which Sector the Element Lives In

**Every identification in this article is an identification for an element of one sector, and the sector is not a detail.** The norm is real on a sector and complex off it. For the two halves

$$
\tilde R_\Phi=i\,r'_t\,e_t+\vec r\in\mathbb{B}_{\Phi},
\qquad
\tilde H_\Psi=h_t\,e_t+i\,\vec h'\in\mathbb{B}_{\Psi},
$$

the norm of the sum is

$$
N(\tilde R_\Phi+\tilde H_\Psi)
=N(\tilde R_\Phi)+N(\tilde H_\Psi)
+2i\bigl(r'_th_t+\vec r\cdot\vec h'\bigr),
$$

checked to $4\times10^{-15}$ over one hundred mixed sums. The cross term is the Minkowski inner product of the two halves, in the unit metric, so a mixed element carries two invariants, $\operatorname{Re}N$ and $\operatorname{Im}N$, and a sector element carries one. **The names of the four regions are therefore attached to sectors and not to the algebra**, and the table below is the corrected version of the partition, object by object.

| object | element | sector | $N$ | $B^{2}$ | region |
| --- | --- | --- | --- | --- | --- |
| momentum, massive in motion | $i\frac{E}{c}e_t+\vec p$ | $\mathbb{B}_{\Phi}$ | $-m^{2}c^{2}$ | $\lvert\vec p\rvert^{2}$ | $\Sigma_{11}$ |
| momentum, at rest | $i\,mc\,e_t$ | $\mathbb{B}_{\Phi}$ | $-m^{2}c^{2}$ | $0$ | $\Sigma_{10}$ |
| momentum, massless | $i\frac{E}{c}\bigl(e_t+\vec u\bigr)$ | $\mathbb{B}_{\Phi}$ | $0$ | $(E/c)^{2}$ | $\Sigma_{01}$ |
| four-potential | $i\,a'_t\,e_t+\vec A$ | $\mathbb{B}_{\Phi}$ | real | $\ge0$ | any of the four |
| field strength, general | $i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ | mixed | $\in\mathbb{C}$ | $\in\mathbb{C}$ | $\Sigma_{11}$ |
| field strength, electric | $i\sqrt{\epsilon}\,\vec E$ | $\mathbb{B}_{\Psi}$ | $-\epsilon\lvert\vec E\rvert^{2}$ | $-\epsilon\lvert\vec E\rvert^{2}$ | $\Sigma_{11}$ |
| field strength, magnetic | $-\sqrt{\mu}\,\vec H$ | $\mathbb{B}_{\Phi}$ | $\mu\lvert\vec H\rvert^{2}$ | $\mu\lvert\vec H\rvert^{2}$ | $\Sigma_{11}$ |
| field strength, null | $\lvert\vec E\rvert=c\lvert\vec B\rvert$, $\vec E\perp\vec B$ | mixed | $0$ | $0$ | $\Sigma_{00}$ |
| scalar amplitude | $r\,e^{i\theta_{\mathrm{pha}}}e_t$ | mixed | $r^{2}e^{2i\theta_{\mathrm{pha}}}$ | $0$ | $\Sigma_{10}$ |
| spinor amplitude | $X\tilde\Pi$ | mixed | $0$ | $\neq0$ | $\Sigma_{01}$ |

**The first consequence is that a pure element is never in $\Sigma_{10}$ or in $\Sigma_{01}$.** Since $N-B^{2}=Q_t^{2}$, a pure element has $N=B^{2}$ identically — checked exactly, to $0$ over one hundred pure elements — and $N=B^{2}$ holds if and only if $Q_t=0$. So the two mixed regions are momentum regions: they are reached by a material element (the rest frame, the light cone) and by a mixed one (a scalar amplitude, a spinor amplitude), and never by a field strength. **The Coulomb field is in $\Sigma_{11}$, the radiation field in $\Sigma_{00}$, and nothing pure lies between them.** The reason is geometric: $Q_t=0$ is exactly the locus where $\nabla N$ and $\nabla B^{2}$ are proportional, so the two cones are tangent precisely where pure elements live.

**The second consequence is that the regions are types and not objects.** One hundred random mixed elements gave one hundred elements of $\Sigma_{11}$, so if the region names were allowed to travel they would name every generic element of the algebra. They do not travel: mass is a reading of $N$ on $\mathbb{B}_{\Phi}$, and the modulus $\lvert N\rvert^{1/2}$ is a mass only there, where $\operatorname{Im}N=0$ holds by construction. Off the sector the same complex number splits into the two classical invariants of a field, $\operatorname{Re}N=-\epsilon(\lvert\vec E\rvert^{2}-c^{2}\lvert\vec B\rvert^{2})$ and $\operatorname{Im}N=-2\sqrt{\epsilon\mu}\,\vec E\cdot\vec H$, as the null-field row of the table shows.

**What the sector reduces to, and what it does not.** On $\mathbb{B}_{\Phi}$ both invariants are real and $B^{2}$ is a sum of three real squares, so the partition collapses to two questions: whether the spatial part vanishes, and the sign of the norm. That is exactly the classical table — at rest, in motion, on the cone, at the vacuum — and it is the reason the four regions could be named after mass and motion in the first place. On $\mathbb{B}_{\Psi}$ the mirror holds with the signs reversed: $B^{2}\le0$, the norm is $h_t^{2}-\lvert\vec h'\rvert^{2}$, and the spectrum $\lambda_\pm=h_t\pm\lvert\vec h'\rvert$ is real rather than imaginary, checked to $4\times10^{-15}$ over one hundred elements. **On both sectors the norm is real; the sectors differ in the sign of the vector square, and in whether the spectrum is imaginary or real.**

## The Three Carriers

**A region is a type and a carrier is the object's home, so the two classifications must be crossed.** The regions were cut by the two invariants alone; the carriers were fixed by the dimension and the module of the spin. The question that crossing them answers is the reach of a carrier: which regions contain a member of it. Each carrier pins one invariant, and the pinning is exact rather than typical.

**One convention is forced before the crossing, and the algebra forces it.** The element that a region classifies is whatever element the physics reads there. For a four-momentum it is the momentum; for a field it is the amplitude. Those two are in different carriers, and the algebra says so: **a momentum is a four-vector and lies in $\mathbb{B}_{\Phi}$ whatever the spin of its field, while an amplitude lies in the carrier that the spin fixes.** So a scalar field has its amplitude in the centre and its momentum in the sector, and a spinor has its amplitude in an ideal and its momentum in the sector as well. The two complex carriers below are therefore read as carriers of **amplitudes**, and the material carrier is read as the carrier of **momenta and potentials**, which is how the object table of §*Which Sector the Element Lives In* already distributes them.

| carrier | element | $\dim_\mathbb{R}$ | $N$ | $B^2$ | regions reached | generic region |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathbb{B}_{C}$ | $q\,e_t$ | $2$ | $q^{2}$ | $0$ identically | $\Sigma_{10}$, $\Sigma_{00}$ | $\Sigma_{10}$ |
| $S_{\pm}$ | $q_t(e_t\pm i\vec e_z)+q_x(\vec e_x\mp i\vec e_y)$ | $4$ | $0$ identically | $-q_t^{2}$ | $\Sigma_{01}$, $\Sigma_{00}$ | $\Sigma_{01}$ |
| $\mathbb{B}_{\Phi}$ | $i\,q'_t\,e_t+\vec r$ | $4$ | real | $\lvert\vec r\rvert^{2}\ge0$ | all four | $\Sigma_{11}$ |

**The table says that the two questions belong to two different carriers.** Motion is a vector part, and a carrier with no vector part has no motion: the centre has $B^{2}=0$ at every one of its points, so neither $\Sigma_{11}$ nor $\Sigma_{01}$ contains one. Mass is a non-zero determinant, and a carrier whose members are all rank one has none: the ideal has $N=0$ at every one of its points, so neither $\Sigma_{11}$ nor $\Sigma_{10}$ contains one. **No two carriers share a generic region**, and the three generic regions are the three regions other than $\Sigma_{00}$, in the order of the spins: $\Sigma_{10}$ for the centre, $\Sigma_{01}$ for the ideal, $\Sigma_{11}$ for the sector.

### The First Carrier: The Centre

$$
\mathbb{B}_{C}=\mathbb{C}e_t=\{\,q\,e_t\ :\ q\in\mathbb{C}\,\},
$$

of real dimension two. Its vector part is zero, so $B^{2}=0$ identically, and its norm is $N=q^{2}$. The characteristic polynomial is $(X-q)^{2}$, so the spectrum is $q$ twice and the region is $\Sigma_{10}$ whenever $q\neq0$.

**The whole punctured centre is the scalar line of $\Sigma_{10}$.** The regions reached are $\Sigma_{10}$ for $q\neq0$ and $\Sigma_{00}$ for $q=0$; the other two are empty, and they are empty for one reason, which is that a direction is not in the carrier. The identification is two-sided: the region's semisimple face *is* this carrier, and the region's Jordan face $\{q e_t+\vec\Upsilon,\ \vec\Upsilon\neq0\}$ is disjoint from it, since $\vec\Upsilon\neq0$ is not central.

**Every point of the carrier is a scalar operator.** Left multiplication by $q e_t$ is $q$ times the identity of the algebra, so the eigenspace is $\mathbb{B}$ itself, of dimension four, and the operator is semisimple with a single proper value. That is the content of the region's name *rest frame* in the sharpest form available: the repeated eigenvalue is repeated four times over, and no direction is preferred.

| question | answer on $\mathbb{B}_{C}$ |
| --- | --- |
| element | $q\,e_t$, $q\in\mathbb{C}$ |
| real dimension | $2$ |
| $B^{2}$ | $0$, at every point |
| $N$ | $q^{2}$ |
| spectrum | $q$, twice |
| eigenspace of $L_{qe_t}$ | all of $\mathbb{B}$, dimension four |
| regions reached | $\Sigma_{10}$ for $q\neq0$, $\Sigma_{00}$ for $q=0$ |
| mass shell $N=-m^{2}c^{2}$ | $q=\pm imc$, two points |
| material share | $i\,\mathbb{R}e_t$, the rest-frame line |
| polar word | modulus and phase |

**The norm is real on two lines of the carrier only.** $N=q^{2}$ is real when $q$ is real or purely imaginary, and the two lines are the informational and the material ones. Off them the member has a complex eigenvalue, and the imaginary part is a phase and not a motion: the polar word of the carrier is a modulus and a phase, and *The Klein–Gordon Equation in Biquaternionic Polar Variables* uses exactly those two. **On the material line the element is the rest-frame momentum itself**, $\tilde P_\Phi=i\,mc\,e_t$, so the mass shell $N=-m^{2}c^{2}$ cuts the carrier in the two points $q=\pm imc$ and the sign is the sign of the energy. **Off that line the element is an amplitude, and its $N$ is the amplitude's square and not a mass**: the corpus's polar word writes it $N=r^{2}e^{2i\theta_{\mathrm{pha}}}$, a modulus and a phase with no mass shell in it.

**The empty regions are a statement about the amplitude and not about the field's motion.** A scalar field has two carriers at once: its amplitude is in the centre and its momentum is in the sector, so $\Sigma_{11}$ is closed to the one and generic for the other. **The centre cannot reach $\Sigma_{11}$ because a direction is the one thing its elements do not have**, and the motion of the field is recorded one carrier over, in §*The Third Carrier: The Material Sector*.

### The Second Carrier: The Minimal Left Ideal

$$
S_{\pm}=\mathbb{B}\tilde\Pi_{\pm}
=\{\,q_t(e_t\pm i\vec e_z)+q_x(\vec e_x\mp i\vec e_y)\ :\ q_t,q_x\in\mathbb{C}\,\},
\qquad
\tilde\Pi_{\pm}=\tfrac12(e_t\pm i\vec e_z),
$$

of real dimension four and complex dimension two. A member is a product with a rank-one idempotent, so as a matrix it has rank at most one, so its determinant vanishes; $N$ is the determinant, so

$$
N=0\quad\text{at every point of }S_{\pm},
$$

checked over three hundred random members with a largest residue of $10^{-15}$.

**The vector square follows from the norm.** With the identity $N=Q_t^{2}+B^{2}$ and $N=0$, a member has $B^{2}=-Q_t^{2}=-q_t^{2}$, exactly, since $Q_t=q_t$. So the regions reached are $\Sigma_{01}$ for $q_t\neq0$ and $\Sigma_{00}$ for $q_t=0$, and the two remaining regions are empty. **The boundary between the two is a complex line**, the nilpotent line $\mathbb{C}\vec\Upsilon_y\subset S_+$ and $\mathbb{C}\vec\Upsilon_x\subset S_-$, so $\Sigma_{01}$ occupies the carrier up to a set of real codimension two and $\Sigma_{01}$ is its generic region.

**The frozen zero is structural.** Since $\lambda_+\lambda_-=N$ and $\lambda_++\lambda_-=2Q_t$, a member has the spectrum

$$
\{0,\ 2q_t\},
$$

checked over three hundred members with a largest error of $10^{-14}$. One eigenvalue is zero at every point of the carrier, whatever its amplitude. **So the one zero mode that the massless region attributes to a scaled idempotent is a property of the carrier and not of the region**, and the region's two-term writing $\{2Q_t,0\}$ is the carrier's own spectrum written with $Q_t$ left free.

| question | answer on $S_{\pm}$ |
| --- | --- |
| element | $q_t(e_t\pm i\vec e_z)+q_x(\vec e_x\mp i\vec e_y)$ |
| real dimension | $4$ |
| $N$ | $0$, at every point |
| $B^{2}$ | $-q_t^{2}$ |
| spectrum | $0$ and $2q_t$ |
| regions reached | $\Sigma_{01}$ for $q_t\neq0$, $\Sigma_{00}$ for $q_t=0$ |
| mass shell $N=-m^{2}c^{2}$, $m\neq0$ | empty |
| material share | $\mathbb{R}\,i\tilde\Pi_{\pm}$, one real line, on the null cone |
| polar word | modulus, phase, rotor |
| motion | null at every point |

**The two coefficients are the two directions of the ladder.** The pair $\{\tilde\Pi_\pm,\vec\Upsilon_{y,x}\}$ is a complex basis of the ideal, and it is the pair the corpus already names in the region $\Sigma_{00}$: a rung and a nilpotent. The coefficient $q_t$ measures the rung and $q_x$ the nilpotent, so the passage from $\Sigma_{01}$ to $\Sigma_{00}$ inside the carrier is the vanishing of the rung's coefficient, and the carrier has no third direction to pass through.

**The mass is not on either ideal.** A non-zero mass is a non-zero norm, and no member of either ideal has one, so the mass shell $N=-m^{2}c^{2}$ is empty on the second carrier for every $m\neq0$. The mass of a spin-half field is the cross term of the sum: since $N(\tilde\Xi_{L})=N(\tilde\Xi_{R})=0$ and $N$ is a quadratic form,

$$
N(\tilde\Xi_{L}+\tilde\Xi_{R})=2\langle\tilde\Xi_{L},\tilde\Xi_{R}\rangle,
$$

the polar form of the norm, so the mass belongs to the pair and to neither value. **That is the region $\Sigma_{11}$ refused by both complex carriers and reached by the third**, and it is the algebraic form of the statement that a mass is an interference and not a property of one chiral half.

### The Third Carrier: The Material Sector

**The third carrier is the material sector itself**, and it is why the four regions were cut there first: on it both invariants are real and the vector square is a definite form, which was the subject of §*Which Sector the Element Lives In*.

| question | answer on $\mathbb{B}_{\Phi}$ |
| --- | --- |
| element | $i\,q'_t\,e_t+\vec r$, $q'_t\in\mathbb{R}$, $\vec r\in\mathbb{R}^{3}$ |
| real dimension | $4$ |
| $B^{2}$ | $\lvert\vec r\rvert^{2}\ge0$ |
| $N$ | $\lvert\vec r\rvert^{2}-q_t'^{2}$, real |
| spectrum | $i(q'_t\pm\lvert\vec r\rvert)$ |
| regions reached | all four |
| mass shell $N=-m^{2}c^{2}$ | $\Sigma_{11}$ for $\vec r\neq0$, $\Sigma_{10}$ at $\vec r=0$ |
| share with $\mathbb{B}_{C}$ | $i\,\mathbb{R}e_t$, in $\Sigma_{10}$ |
| share with $S_{\pm}$ | $\mathbb{R}\,i\tilde\Pi_{\pm}$, in $\Sigma_{01}$ |
| polar word | scale, boost and direction |

**The sector is the one carrier that reaches the interior.** $\Sigma_{11}$ is open and dense in it; the other three sit in its boundary, of real dimensions one, three and zero. That is the reason the four regions could be named after mass and motion at all: mass is a reading of a real norm and motion is a reading of a real vector square, and only here are both real and both free.

**Each complex carrier meets the sector in one real line, and each line is on the boundary.** The centre's share is the rest line $i\mathbb{R}e_t$, which is the semisimple stratum of $\Sigma_{10}$; the ideal's share is the line $\mathbb{R}i\tilde\Pi_\pm$, which has $N=0$ and $B^{2}\neq0$ and therefore lies in $\Sigma_{01}$, the frame's third axis becoming a direction of light. **So a material element that is also central is spectrally degenerate, and a material element that is also one value of a spinor is null**, and neither can be massive in motion.

**The vacuum is the only region that all three carriers meet.** The origin belongs to the centre, to both ideals and to the sector, and it is the whole of each complex carrier's share of $\Sigma_{00}$. The region that separates the carriers most sharply is therefore not a region at all but its opposite: $\Sigma_{11}$ contains members of one carrier and of no other.

## The Mass Shell and the Light Cone

The four regions are not the mass shell and the light cone. They are the regions cut by the two cones, and the physically distinguished level sets cut across them.

- The **mass shell** $N=-m^2c^2$ is a level set of the norm. It lies in $\Sigma_{11}$ for $\vec p\neq0$ and meets $\Sigma_{10}$ at the rest point $\vec p=0$. It is not a region: it is a hypersurface that crosses the spectral cone at the rest frame.
- The **light cone** $N=0$ is the union of $\Sigma_{01}$ and the doubly degenerate region $\Sigma_{00}$. It is the boundary of the unit group and the set of zero divisors.
- The **spectral cone** $B^2=0$ is the union of $\Sigma_{10}$ and $\Sigma_{00}$. It is the set of elements with a repeated eigenvalue.
- The **origin** lies on both cones and in the closure of all four regions. The intersection of the two cones is the doubly degenerate region $\Sigma_{00}$.

The reading is the reason the partition is physically useful. A particle is not a region; a particle is a level set of $N$ together with a motion class. The four regions tell what kind of spectral object the level set is made of. A massive particle at rest and a massive particle in motion are in different regions, although they lie on the same mass shell; a massless particle and the vacuum are in different regions, although they lie on the same light cone.

## What the Table Does Not Say

The table is a partition of the algebra by two invariant values. It does not say that the four regions are phases of matter, that they evolve into one another, or that a physical system occupies one region for all time. The regions are properties of one element at one instant.

The table does not supply a dynamics. It does not say how an element moves from one region to another, and it does not supply a mass spectrum. The mass shell is a level set, not an equation of motion.

The table does not say that the non-zero nilpotents are physical. On the real material slice they are absent; in the full algebra they are the fermionic ladder, and the corpus's reading of them is algebraic, not a claim about physical statistics.

The table does not say that the regions are Lorentz invariant. The norm is invariant under a norm-one bilinear two-sided operator, and the discriminant is not. A boost preserves $N$ and changes $B$, so it moves a massive element along its mass shell; in particular, it moves a massive element from the rest frame $\Sigma_{10}$ into $\Sigma_{11}$. The mass shell and the light cone are Lorentz invariant; the regions are not. A region is a spectral type at an instant, not an orbit of the Lorentz group.

## Physical Interpretations

- **The partition is the mass–motion classification.** $N$ is the invariant mass-squared, and $B^2$ is the motion. The four regions are massive at rest, massive in motion, massless, and the vacuum, extended to the complex algebra.
- **The two questions are independent.** A zero divisor can have two modes, and a unit can have one. The mixed regions are the proof, and they are the reason the algebra needs four sectors and not two.
- **The spectrum is the pair of light-cone frequencies.** $\lambda_\pm=i(E/c\pm\lvert\vec p\rvert)$ on the material slice. The sum is $2iE/c$, the difference $2i\lvert\vec p\rvert$, and the product $-m^2c^2$.
- **The rest frame is the scalar line.** It is the only real momentum with one mode, and the only frame in which the spectral writing is not unique. The exceptional point is its complex neighbour, where the one mode is defective.
- **The light cone is the massless region plus the doubly degenerate region.** A massless momentum is a scaled idempotent: a rank-one element with one zero mode. The origin is the apex, the only element with no scale and no mode; the nilpotent directions complete the region.
- **The mass shell crosses the regions.** A particle at rest and a particle in motion are on the same mass shell but in different regions; the region is the spectral type, the shell is the value of the norm.
- **The real slices select half of the table.** On each real slice the vector square has a definite sign, so the spectral cone meets the slice only on the scalar line. The Jordan part and the nilpotents are complex regimes.
- **The arrangement is the boundary structure of the unit group.** The units are $\Sigma_{11}\cup\Sigma_{10}$; the zero divisors are $\Sigma_{01}\cup\Sigma_{00}$; the spectral cone is $\Sigma_{10}\cup\Sigma_{00}$; the origin is the common limit.

## Limits

The identification of $N$ with $-m^2c^2$ needs the material slice and the four-momentum chart. In the full algebra $N$ is complex, and calling it a mass is an extra identification.

The identification of $B$ with $\lvert\vec p\rvert$ needs the material slice. In the full algebra $B^2$ is a complex invariant, and "motion" is a name for the spectral splitting, not a velocity.

The table is a partition of elements, not of states. It does not say that a quantum state is in one region, and it does not supply a Hilbert-space interpretation of the regions.

The non-zero nilpotents are not physical null four-momenta. On the real material slice the doubly degenerate region contains only the origin.

The regions are not phases and not basins of attraction. No dynamics, no order parameter and no transition is claimed.

## Summary

- The norm $N=Q_t^2+B^2$ answers whether there is an invariant magnitude and, on the material slice, which causal sign it carries. On a four-momentum $N=-m^2c^2$.
- The vector square $B^2$ is the discriminant. It answers whether there are two distinct modes. On a four-momentum $B=\lvert\vec p\rvert$, so it answers whether the momentum moves.
- The two conditions are independent and partition the algebra into four regions: $\Sigma_{11}$ (mass in motion), $\Sigma_{10}$ (rest frame and exceptional point), $\Sigma_{01}$ (light ray), $\Sigma_{00}$ (vacuum and nilpotent ladder).
- $\Sigma_{11}$ is the generic unit with two distinct non-zero eigenvalues and a unique two-term spectral decomposition.
- $\Sigma_{10}$ is the unit with a repeated eigenvalue: the scalar line is the real rest frame, the Jordan part is the complex exceptional point.
- $\Sigma_{01}$ is the zero divisor with spectrum $\{2Q_t,0\}$: a scaled idempotent, a rank-one light ray.
- $\Sigma_{00}$ is the square-zero region: the origin, the vacuum, and the non-zero nilpotents, the fermionic ladder.
- On the material slice $B^2\ge0$ and the spectral cone meets the slice only on the scalar line; the Jordan part and the nilpotents are complex regimes.
- The mass shell crosses $\Sigma_{11}$ and $\Sigma_{10}$; on the material slice the light cone is $\Sigma_{01}$ together with the apex. The regions are spectral types, not level sets.
- The table is a partition of elements at an instant. It supplies no dynamics, no mass spectrum and no phase structure.
- A region is a type and a sector is the object's home: $N$ is real on a sector and complex off it, a pure element has $N=B^{2}$ and never lies in $\Sigma_{10}$ or $\Sigma_{01}$, and a mixed element carries the two invariants $\operatorname{Re}N$ and $\operatorname{Im}N$.
- A carrier decides the reach: the centre reaches $\Sigma_{10}$ and $\Sigma_{00}$, the minimal left ideal reaches $\Sigma_{01}$ and $\Sigma_{00}$, and the material sector reaches all four. No two carriers share a generic region.
- Each complex carrier pins one invariant. The centre has $B^{2}=0$ at every point, so it never moves; the ideal has $N=0$ at every point, so it is never massive. Its spectrum is $\{0,2q_t\}$, with one eigenvalue frozen at zero by the carrier and not by the region.
- Each complex carrier meets the material sector in one real line, and each line lies on a cone: $i\mathbb{R}e_t$ in $\Sigma_{10}$ for the centre, $\mathbb{R}i\tilde\Pi_\pm$ in $\Sigma_{01}$ for the ideal. A material element that is also central is spectrally degenerate; one that is also a spinor value is null.
- The mass of a spin-half field is the cross term of the two values, $N(\tilde\Xi_{L}+\tilde\Xi_{R})=2\langle\tilde\Xi_{L},\tilde\Xi_{R}\rangle$, since $N=0$ on either carrier. The vacuum is the only region that all three carriers meet.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the vector square, the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $\mathcal N=\{N=0\}$ | the null cone, the zero-divisor cone |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\Sigma_{ij}$ | the region with $N=0$ iff $i=0$ and $B^2=0$ iff $j=0$ |
| $\mathbb{B}_{\Phi}$ | the material slice, $Q_t=i q'_t$, $\vec Q$ real |
| $\mathbb{B}_{\Psi}$ | the informational slice, $Q_t=q_t$ with $q_t=h_t$, $\vec Q$ imaginary |
| $\mathbb{B}_{C}=\mathbb{C}e_t$ | the centre, the first carrier, $\{q\,e_t\}$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the minimal left ideals, the second carrier |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the idempotents derived from the frame's third unit |
| $q_t$, $q_x$ | the coefficients of $e_t\pm i\vec e_z$ and $\vec e_x\mp i\vec e_y$ in $S_\pm$ |
| $\tilde P_{\Phi}=i\frac{E}{c}e_t+\vec p$ | the four-momentum chart |
| $m$, $\vec p$, $\theta_{\mathrm{rpd}}$ | mass, momentum, rapidity |

## Further Reading

- [The N-Regular, Spectrally Regular Sector: Mass in Motion](the-n-regular-spectrally-regular-sector-mass-in-motion.html), for $\Sigma_{11}$.
- [The N-Regular, Spectrally Degenerate Sector: The Rest Frame and the Exceptional Point](the-n-regular-spectrally-degenerate-sector-the-rest-frame-and-the-exceptional-point.html), for $\Sigma_{10}$.
- [The N-Degenerate, Spectrally Regular Sector: The Massless Regime](the-n-degenerate-spectrally-regular-sector-the-massless-regime.html), for $\Sigma_{01}$.
- [The N-Degenerate, Spectrally Degenerate Sector: The Vacuum and the Nilpotent Ladder](the-n-degenerate-spectrally-degenerate-sector-the-vacuum-and-the-nilpotent-ladder.html), for $\Sigma_{00}$.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the three carriers, their dimensions and their spins.
- [The Carrier of the Klein–Gordon Field](the-carrier-of-the-klein-gordon-field.html), for the centre as the carrier of spin zero.
- [The Carrier of the Dirac Field](the-carrier-of-the-dirac-field.html), for the minimal left ideals as the carriers of the two values.
- [The Carrier of the Proca Field](the-carrier-of-the-proca-field.html), for the material sector as the carrier of the vector potential.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the Doppler pair and the two-term writing.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the four-vector dictionary.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone and the massless limit.
