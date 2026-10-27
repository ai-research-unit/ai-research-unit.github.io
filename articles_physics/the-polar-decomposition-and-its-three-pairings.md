# __The Polar Decomposition and Its Three Pairings__

## Introduction

Every biquaternion off the null cone is the ordered product of four factors: a positive scale, a central phase, a Hermitian boost and a real quaternion rotor,

$$
\boxed{\;\tilde Q=r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi_w}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr)\;}.
$$

The word is the **N-norm** refinement. The general **H-norm** decomposition is the two-factor pair $\tilde Q=\tilde H\tilde U$, with $\tilde H=(\tilde Q\tilde Q^{*})^{1/2}\ge0$ and $\tilde U=\tilde H^{+}\tilde Q$ a partial isometry on the cone; it is defined for every nonzero element and is read in *The General Polar Decomposition, the Amplitude and the Operator-to-State Map*. The four-factor word below exists only where $\langle\tilde Q\rangle_{\natural}\neq0$.

The four factors carry $1+1+3+3=8$ real parameters, the real dimension of the algebra. The word is a change of coordinates on the complement of the zero-divisor cone, not a dynamical decomposition: it says what an element is at one instant and not how it evolves.

The article is the hub of the polar programme. It fixes the word, brackets it in the three ways the corpus uses, compares the bracketings, and records what each factor does to the remarkable subspaces. The detail now lives in two synthesis articles: *The General Polar Decomposition, the Amplitude and the Operator-to-State Map* develops the amplitude–phase reading, and *The Hamilton Pairing: Mass as Modulus and the Complex Angle* develops the invariant and the complex angle. The comparison of the three first factors is stated below, in §*The Three Factors Compared*.

Two distinctions organise the article and are worth naming at the start. A **pairing** is a bracketing of the four-factor product into two factors; a **split** is a direct-sum decomposition of the algebra as a vector space. The corpus has three of each, and the two threes are not the same three. §*The Three Splits* separates them.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The four factors, their ranges, their dimensions, the theorem and the uniqueness | [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html) |
| The exponential word, the logarithm, the kernel and the boundary limits | [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html) |
| The quaternion pairing, its construction and its domain | [The Quaternion Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html) |
| The Hamilton pairing, the complex modulus and the complex angle | [The Hamilton Root Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html) |
| The Cartan pairing and the matrix polar decomposition | [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html) |
| The generalized pairing on the null cone | [The Polar Decomposition of a N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html) |
| The action of the four factors on the sectors and the six remarkable subspaces | [The Polar Decomposition and Remarkable Subspaces](../articles_maths/the-polar-decomposition-and-remarkable-subspaces.html) |

## The Four Factors

| # | Factor | Name | Exponent | Root | Range | Real dimension | Action on the algebra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | $r$ | scale | — | — | $r>0$ | $1$ | dilation by $r^2$ |
| 2 | $\exp(i\alpha)$ | central phase | $i\alpha$ | $i$ | $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | $1$ | multiplication by the scalar |
| 3 | $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi_w}{2}\vec u_{\mathrm b})$ | boost | $i\tfrac{\psi_w}{2}\vec u_{\mathrm b}$ | $i\vec u_{\mathrm b}$ | $\psi_w\ge0$, $\vec u_{\mathrm b}\in\mathcal{A}$ | $3$ | congruence $X\mapsto \tilde U_{\mathrm b}X\tilde U_{\mathrm b}^{*}$ |
| 4 | $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | rotor | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\vec u_{\mathrm r}\in\mathcal{A}$ | $3$ | conjugation $X\mapsto \tilde u_{\mathrm r}X\tilde u_{\mathrm r}^{-1}$ |

The axis sphere $\mathcal{A}$ is the set of unit real pure quaternions, the roots of $-e_t$. The phase is the only factor whose action is not a sandwich; its action is scalar multiplication.

The scale and the phase are central, the boost is Hermitian positive and non-compact, and the rotor is compact and real. The order of the factors is forced: the scale and the phase commute with everything, the boost stands on the left of the rotor, and the rotor is what remains after the Hermitian part is divided out. The word is unique once the branch of the square root is fixed.

## Reading the Eight Numbers

The word returns the physical description of an element in eight real numbers: the scale $r$, the phase $\alpha$, the rapidity $\psi_w$ and the two angles of the boost axis $\vec u_{\mathrm b}$, and the rotation angle $\theta$ and the two angles of the rotor axis $\vec u_{\mathrm r}$.

The first two are the central data, the next three the non-compact data, the last three the compact data. The scale and the phase are fixed by the norm $N$: $r=\lvert N\rvert^{1/2}$ and $\alpha=\tfrac12\arg N$. The word's rapidity $\psi_w$ is fixed by the ratio of the two invariants,

$$
\cosh\psi_w=\frac{\langle\tilde Q,\tilde Q\rangle_{*}}{\lvert N\rvert},
$$

and the two axes are fixed by the phases of the four complex coordinates. The pair $(N,\langle\tilde Q,\tilde Q\rangle_{*})$ fixes the scale, the phase and the rapidity and cannot fix the two directions: a rotation of the vector part leaves both invariants unchanged and turns the axes.

The word is a parametrization of the eight-dimensional algebra and not a constraint on it. It is surjective onto the units and not injective where an axis degenerates, at $\psi_w=0$ and at $\theta=0$.

## The Domain

The word exists if and only if $N\neq0$, that is, if and only if the element is outside the zero-divisor cone. On the cone the product of the four factors has norm of modulus $r^{2}>0$, so no factorisation exists. The condition is one complex equation, hence two real equations, and the cone has real codimension two: the domain is the complement of a six-real-dimensional cone in the eight-real-dimensional algebra.

The failure is physical. A lightlike four-vector has no rest frame, so the scale degenerates and there is no boost split: there is no frame in which its spatial part vanishes and no rapidity that carries it to that frame. The algorithm stops on the cone for the same reason a boost parametrisation stops at the speed of light.

The three pairings have smaller domains than the word, and the table states each once. The distinction between the **factorisation** and the **construction from the parts** is owned by *Conventions in the Biquaternion Universe*, §*The Domains of the Three Pairings*; it is restated here because every statement below must be read against it.

| pairing | factorisation exists | construction exists | witness of the smaller domain |
| --- | --- | --- | --- |
| word | $N\neq0$ | same | any element of the cone |
| quaternion | $N\neq0$ | $N\neq0$ and $\tilde q_r\neq0$ | $i\vec e_x+i\vec e_y$: $N=-2$, $\tilde q_r=0$ |
| Hamilton | $N\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ | same | $e_t+\vec e_x+i\vec e_y$: $N=1$, $B=0$ |
| Cartan | $N\neq0$; generalized: all $\tilde Q$ | same | $e_t+i\vec e_x$: on the cone |

The domains are not nested. The quaternion construction fails at $\tilde q_r=0$; the Hamilton pairing fails when the vector part is null; the Cartan pairing is the widest and the generalized pairing extends it to the cone with a partial isometry. A statement proved in one pairing does not transport to another without checking the witness.

## The Three Pairings

The four-factor word is the reference. The three pairings are its three bracketings into two factors, and the table records which pair of factors each one groups together.

| Pairing | First factor | Second factor | What it separates |
| --- | --- | --- | --- |
| Quaternion | $\tilde q=r\tilde u_{\mathrm r}$ | $\exp(i\tilde\Psi)$ | scale and rotor / phase and boost |
| Hamilton | $\Rho=r\exp(i\alpha)$ | $\exp(\vec U\Theta)$ | scale and phase / boost and rotor |
| Cartan | $\tilde H=r\tilde U_{\mathrm b}$ | $\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}$ | scale and boost / phase and rotor |

### The Quaternion Pairing

The quaternion pairing writes the element as a **real quaternion modulus** times the exponential of a **real quaternion angle**:

$$
\boxed{\;\tilde Q=\tilde q\,\exp(i\tilde\Psi), \qquad
\tilde q=r\,\tilde u_{\mathrm r}, \qquad
\exp(i\tilde\Psi)=\exp(i\alpha)\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\;}.
$$

The modulus is an ordinary quaternion in its polar form, and it is the spatial frame. The exponent has scalar part $\alpha$ and pure part $\tfrac{\psi_w}{2}\vec u_{\mathrm b,2}$, with the boost axis rotated by the rotor. The reading is the frame: the rotor carries the reference axes to the axes of the element, and $r$ is the scale at which the frame is taken. §*The Three Factors Compared* states it with the other two.

### The Hamilton Pairing

The Hamilton pairing writes the element as a modulus times a complex cosine plus a complex axis times the complex sine:

$$
\boxed{\;\tilde Q=\Rho\bigl(\cos\Theta+\vec\Xi\sin\Theta\bigr), \qquad
\Rho=\sqrt N, \qquad
\vec\Xi=\frac{\vec Q}{B}, \qquad
B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}\;}.
$$

The modulus is the only central scalar of the three pairings. The axis and the angle carry the boost and the rotor; on aligned axes the real part of $\Theta$ is half the rotation and the imaginary part is half the word's rapidity $\psi_w$, and in general the two do not separate. The physical reading — the mass for a four-momentum, the amplitude otherwise — is developed in *The Hamilton Pairing*, §*The Central Modulus*.

### The Cartan Pairing

The Cartan pairing writes the element as a **Hermitian positive factor** times a **unitary factor**:

$$
\boxed{\;\tilde Q=\tilde H\tilde U, \qquad
\tilde H=\sqrt{\tilde Q\tilde Q^{*}}=r\tilde U_{\mathrm b}, \qquad
\tilde U=\tilde H^{-1}\tilde Q=\exp(i\alpha)\tilde u_{\mathrm r}\;}.
$$

The first factor is the amplitude, the part that changes norms and not phases; the second is the phase, the part that preserves the inner product. The state reading is developed in *The General Polar Decomposition, the Amplitude and the Operator-to-State Map*.

The Cartan pairing has the widest construction domain, the quaternion pairing the most direct electromagnetic reading, and the Hamilton pairing the most direct Lorentz-group reading. None is more fundamental than the others, and none adds information to the four-factor word.

## The Three Factors Compared

The three pairings have three first factors, and the comparison is the synthesis that the separate articles used to carry.

| pairing | first factor | type | real dimension | the question it answers |
| --- | --- | --- | --- | --- |
| quaternion | $\tilde q=r\tilde u_{\mathrm r}$ | real quaternion, norm $r^{2}$ | $4$ | what is the spatial frame? |
| Hamilton | $\Rho=r e^{i\alpha}$ | central complex scalar | $2$ | what is the invariant? |
| Cartan | $\tilde H=r\tilde U_{\mathrm b}$ | Hermitian positive, $\det=r^{2}$ | $4$ | what is the state amplitude? |

The three factors have three different types. Two of them are not scalars. Only $\Rho$ is central. The real dimensions add to $10$, not to $8$:

$$
4+2+4=10=8+2.
$$

The redundancy is exactly the scale $r$, which appears in all three factors. Each factor is a partial description that includes the scale and adds one structural datum: the rotor, the phase, or the boost. The three together are three summaries of the same eight numbers, each shaped for a different question. This is the precise sense in which the pairings are readings and not decompositions.

| factor | determined by | blind to |
| --- | --- | --- |
| $\tilde q=r\tilde u_{\mathrm r}$ | $r$, the rotation angle and axis | the phase $\alpha$, the rapidity $\psi_w$, the boost axis |
| $\Rho=r e^{i\alpha}$ | $r$, the phase | the rotation, the boost, both axes |
| $\tilde H=r\tilde U_{\mathrm b}$ | $r$, the rapidity, the boost axis | the phase, the rotation angle and axis |

The factors are three **products**, not three terms:

$$
\tilde Q=\tilde q\,e^{i\tilde\Psi}
=\Rho\,e^{\tilde U\Theta}
=\tilde H\,\tilde U.
$$

There is no sense in which $\tilde Q=\tilde q+\Rho+\tilde H$. Each identity is the whole element, written three times. No conservation law attaches to a factor, no factor is a field, and no factor evolves on its own: the polar factors of $\tilde Q(t)$ depend on $t$ through $\tilde Q(t)$.

The three questions and their readings are:

| question | factor | reading | the object where the reading is sharpest |
| --- | --- | --- | --- |
| what frame? | $\tilde q=r\tilde u_{\mathrm r}$ | the spatial orientation and the scale of the frame | a rotation, a rigid body, a polarization frame |
| what invariant? | $\Rho=r e^{i\alpha}$ | the mass of a four-momentum, or the invariant amplitude | a particle, a scattering element |
| what state? | $\tilde H=r\tilde U_{\mathrm b}$ | the positive amplitude whose normalised square is the state | a Kraus operator, a Jones matrix, a state preparation |

The readings are compatible because they read one element. A scattering element has a Cartan factor that gives the state it prepares, a Hamilton modulus that gives its invariant size, and a quaternion factor that gives the frame in which its spin is described. The three descriptions are not three measurements and do not compete.

## The Three Splits

A split is a direct-sum decomposition of the algebra, not a bracketing of a product. The algebra has three natural two-way splits, and each belongs to a different reading.

| split | pieces | used by | physical reading |
| --- | --- | --- | --- |
| real vs. imaginary coefficients | $\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ | the quaternion construction | the real quaternion frame and the imaginary-coefficient part |
| Hermitian vs. anti-Hermitian | $\mathbb{M}_+\oplus\mathbb{M}_-$ | the physical sectors; the Cartan exponents | the informational and material generators |
| scalar vs. vector | $\mathbb{C}_{\mathbb{B}}\oplus\operatorname{Vect}(\mathbb{B})$ | the four-vector reading; the eigenvalue decomposition | time and space; the spectral axis |

The quaternion construction uses the **first** split. The physical sectors are the **second**. Conflating them would identify the real part with the informational sector and the imaginary part with the material sector, and that is wrong: the material sector $\mathbb{M}_-$ has an imaginary scalar and a real vector, so it mixes the real and imaginary coefficient splits. A table of the sector action of the central $i$ is in *Conventions in the Biquaternion Universe*, §*The Central Map and Its Restrictions*.

The three splits and the three pairings are different structures with the same number. A split asks what the algebra is made of; a pairing asks how the product is grouped. The word's four factors are grouped by the pairings and typed by the splits, and neither classification implies the other.

The **Cartan exponents** are the one place where a split and a pairing meet. The logarithms lie in the two sectors, $\ln\tilde H=\ln r\,e_t+i\tfrac{\psi_w}{2}\vec u_{\mathrm b}\in\mathbb{M}_+$ and $\ln\tilde U=i\alpha\,e_t+\tfrac{\theta}{2}\vec u_{\mathrm r}\in\mathbb{M}_-$, but the **factors** do not split one per sector: $\tilde H$ is Hermitian positive, while $\tilde U$ is unitary and not an element of the linear subspace $\mathbb{M}_-$. Only the logarithms split cleanly. The direct sum is a statement about the Lie algebra of generators, not about the product. The Cartan pairing is $\tilde H\tilde U$, not $\mathbb{M}_+\times\mathbb{M}_-$.

## The Action on the Sectors and the Subspaces

The four factors act by four different operations, and the table records which subspace each one preserves.

| Factor | Operation | Stable subspaces |
| --- | --- | --- |
| scale $r$ | dilation by $r^2$ | all six |
| phase $\exp(i\alpha)$ | multiplication by the scalar | centre, vector space |
| boost $\tilde U_{\mathrm b}$ | congruence | $\mathbb{M}_+$, $\mathbb{M}_-$ |
| rotor $\tilde u_{\mathrm r}$ | conjugation | all six |

The six subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector space $\operatorname{Vect}(\mathbb{B})$, the real quaternion space $\mathbb{H}_{\mathbb{B}}$, the imaginary quaternion space $i\mathbb{H}_{\mathbb{B}}$, and the two sectors $\mathbb{M}_\pm$. No subspace is preserved by all four factors, and that is why no single subspace characterises the word.

On the material sector the boost reads

$$
a_2=a\cosh\psi_w-b_\parallel\sinh\psi_w, \qquad
b_{\parallel,2}=b_\parallel\cosh\psi_w-a\sinh\psi_w,
$$

with $a$ the scalar coordinate and $b_\parallel$ the component of the vector part along the boost axis; on the informational sector the two cross terms carry the opposite sign. The difference is the sector sign. The same congruence reads as the Lorentz action on matter and as a positive congruence on the state space.

The phase at $\alpha=\pi/2$ is multiplication by $i$: it exchanges the two sectors and reverses the norm. The rotor at $\theta=2\pi$ is $-e_t$, the sign a spinor picks up after a full turn.

## The Factor of Two

The word's third factor has one slot and two jobs.

| element | third factor | exponent angle | relation to the kinematic rapidity |
| --- | --- | --- | --- |
| transformation | $\tilde U_{\mathrm b}(\psi_w)=\exp(i\tfrac{\psi_w}{2}\vec u_{\mathrm b})$ | $\psi_w/2$ | $\psi_w=\psi$ |
| four-vector | $\mathcal B=\exp(-i\psi\vec u_{\mathrm b})=\tilde U_{\mathrm b}(\psi)^{-2}$ | $-\psi$ | $\psi_w=2\psi$ |

For a transformation the factor is the frame rotor, and its congruence is the boost of rapidity $\psi_w$. For a four-vector element the factor is the inverse square of the same rotor, and the element is $\tilde Q=r e^{i\alpha}\mathcal B$. The four-momentum is the case $r=mc$, $\alpha=\pi/2$, where $\tilde P=i mc\,\mathcal B$.

The doubling is between the word parameter and the kinematic rapidity of a four-vector. With $\beta=v/c$ and $\beta=\tanh\psi$,

$$
\cosh\psi_w=\frac{1+\beta^{2}}{1-\beta^{2}}=\cosh(2\psi),
\qquad
\gamma=\cosh\psi=\cosh\frac{\psi_w}{2}.
$$

Three errors follow, and each is a check.

- Reading the word parameter $\psi_w$ of a four-vector element as its kinematic rapidity doubles the rapidity.
- Using the frame rotor $\tilde U_{\mathrm b}(\psi)$ where the four-vector factor $\mathcal B=\tilde U_{\mathrm b}(\psi)^{-2}$ belongs halves the rapidity of the four-vector: $i mc\,\tilde U_{\mathrm b}(\psi)$ is a four-vector of rapidity $\psi/2$.
- Identifying $\gamma$ with $\cosh\psi_w$ instead of $\cosh(\psi_w/2)$ overstates the energy.

The four objects called a boost are separated in *Conventions in the Biquaternion Universe*, §*The Four Objects Called a Boost*.

## A Four-Vector Is Bilinear, a Spinor Is Linear

The unit factor acts on a four-vector and on a spinor by two different laws: a four-vector transforms by the congruence $X\mapsto\tilde U X\tilde U^{*}$, which is bilinear in the spinor when $X=\psi\psi^{*}$, and a spinor transforms by the left multiplication $\psi\mapsto\tilde U\psi$. The first law is quadratic in the spinor, the second linear. The sandwich is the four-vector column of the representation theory and the left multiplication is the spinor column. The polar action on the two sectors is the four-vector action; the action on the spinor module is the left multiplication, and it is the one that carries the double cover and the sign of the spinor.

A rotation through $2\pi$ gives $-\tilde U$ on the spinor and $+\mathrm{id}$ on the four-vector, because the congruence by $-\tilde U$ is the congruence by $\tilde U$. The sign is visible only in the linear action.

## Physical Readings

The word is the physical description of an element, and each factor has a reading.

- The **scale** is the invariant length: the modulus of the four-position, $c$ for the four-velocity, $mc$ for the on-shell four-momentum. It is the only factor that survives the sandwich as a scalar, and it survives squared.
- The **phase** is the timelike/spacelike label and the gauge phase. It is $\pi/2$ on the timelike cone and $0$ on the spacelike sheet; it is the central $\mathrm{U}(1)$ that the sandwich does not see.
- The **boost** is the velocity: the axis and the word's rapidity $\psi_w$, which is twice the kinematic rapidity $\psi$ when the element is a four-vector.
- The **rotor** is the spin orientation: the rotation angle and axis of the spatial frame.

The pairings read the same data under different headings, and the readings are dictionaries, not derivations. The word is a coordinate statement, not a dynamics: it does not say that a system moves through the factors, that they are conserved, or that the decomposition is stable under evolution.

## Limits

- The decomposition is defined off the null cone and nowhere on it. The failure is the absence of a rest frame, not a singularity of the algebra. The generalized Cartan pairing extends the amplitude–phase split to the cone with a partial isometry.
- The branch of the square root is the only convention. The interval $(-\pi/2,\pi/2]$ for the phase fixes the sign of the modulus; every other step is forced.
- The Hamilton pairing has a smaller domain than the word; the quaternion construction needs a non-vanishing real quaternion part; the Cartan pairing and the word have the widest domain. A statement proved in one pairing need not hold in another without checking the domain.
- The three splits are not the three pairings. A split decomposes the algebra; a pairing brackets a product. The real/imaginary split of the quaternion pairing is not the sector split.

## Summary

- Every biquaternion off the null cone is $r\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, with $1+1+3+3=8$ real parameters.
- The scale is the modulus of the norm, the phase is half its argument, the boost is the Hermitian positive factor and the rotor is the real quaternion factor.
- The word exists exactly off the zero-divisor cone; on the cone a lightlike four-vector has no rest frame and no boost split.
- The quaternion pairing is $\tilde Q=\tilde q\exp(i\tilde\Psi)$; the Hamilton pairing is $\tilde Q=\Rho(\cos\Theta+\vec\Xi\sin\Theta)$; the Cartan pairing is $\tilde Q=\tilde H\tilde U$.
- The three pairings are the three bracketings of the four-factor word; none adds information to it.
- The three first factors have three types — a real quaternion, a central complex scalar, a Hermitian positive element — and only the Hamilton factor is a scalar.
- The three factors carry $4+2+4=10$ real numbers for an eight-dimensional element; the redundancy is the scale, which all three contain.
- The factors are three products of the same element, not three terms; none is conserved, none is a field, and none evolves on its own.
- The domains are not nested: $i\vec e_x+i\vec e_y$ has no quaternion construction, $e_t+\vec e_x+i\vec e_y$ has no Hamilton pairing, and $e_t+i\vec e_x$ needs the generalized Cartan form.
- The algebra has three splits — real/imaginary, Hermitian/anti-Hermitian, scalar/vector — and they are not the three pairings.
- The Cartan factors do not split one per sector: $\tilde H$ is Hermitian and lies in $\mathbb{M}_+$, $\tilde U$ is unitary and not in $\mathbb{M}_-$, and $\ln\tilde H$ and $\ln\tilde U$ lie in the two sectors.
- The scale and the rotor preserve all six remarkable subspaces, the phase preserves the centre and the vector space, and the boost preserves the two sectors and moves the centre.
- A four-vector transforms by the congruence and a spinor by the left multiplication; the first is bilinear in the spinor, the second linear.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $r$ | the positive scale, $r=\lvert N\rvert^{1/2}$ |
| $\alpha$ | the central phase, $\alpha=\tfrac12\arg N\in(-\pi/2,\pi/2]$ |
| $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi_w}{2}\vec u_{\mathrm b})$ | the frame rotor, the word's third factor for a transformation |
| $\mathcal B=\tilde U_{\mathrm b}^{-2}=e^{-i\psi_w\vec u_{\mathrm b}}$ | the four-vector factor, the word's third factor for a four-vector element |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $\psi_w$, $\theta$ | the word parameter and the rotation angle |
| $\psi$ | the kinematic rapidity; $\psi_w=\psi$ for a transformation and $\psi_w=2\psi$ for a four-vector element |
| $\tilde q=r\tilde u_{\mathrm r}$ | the real quaternion modulus of the quaternion pairing |
| $\tilde\Psi=\alpha+\tfrac{\psi_w}{2}\vec u_{\mathrm b,2}$ | the real quaternion angle of the quaternion pairing |
| $\Rho=\sqrt N$, $\vec\Xi$, $\Theta$ | the modulus, axis and complex angle of the Hamilton pairing |
| $B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}$ | the vector-part root, not the four-vector factor $\mathcal B$ |
| $\tilde H=r\tilde U_{\mathrm b}$, $\tilde U=e^{i\alpha}\tilde u_{\mathrm r}$ | the Hermitian and unitary factors of the Cartan pairing |
| $\mathbb{M}_\pm$ | the Hermitian and anti-Hermitian sectors |

## Further Reading

- [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html), for the general H-norm two-factor decomposition and the partial isometry on the cone.
- [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four factors, the theorem and the uniqueness.
- [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html), for the exponential word, the logarithm, the kernel and the boundary limits.
- [The Quaternion Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html), for the real quaternion modulus and the angle.
- [The Hamilton Root Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html), for the complex axis-angle.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the amplitude–phase split.
- [The Polar Decomposition and Remarkable Subspaces](../articles_maths/the-polar-decomposition-and-remarkable-subspaces.html), for the sector action, the cross-term signs and the preservation table.
- [The General Polar Decomposition, the Amplitude and the Operator-to-State Map](the-general-polar-decomposition-amplitude-and-the-operator-to-state-map.html), for the state defined by an operator and the modular reading.
- [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html), for the mass shell and the complex angle.
- [The Polar Decomposition of a Jones Matrix: Diattenuation, Retardance and Polarizers](the-polar-decomposition-of-a-jones-matrix-diattenuation-retardance-and-polarizers.html), for the Cartan pair as diattenuator and retarder, and the polarizer as its cone case.
- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), §*The Polar Word and the Three Pairings*, for the frozen notation and the domains.
