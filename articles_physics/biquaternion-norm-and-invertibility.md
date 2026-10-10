# __Biquaternion Norm and Invertibility__

## Introduction

The biquaternion norm fixes the interval of the framework, the light cone on which it vanishes and the group of the transformations that preserve it; this article studies it and the invertibility of the elements it decides, and reads both physically. It follows the physics algebra article, which defined the algebra, its conjugations, its remarkable subspaces and the coordinate dictionary, and it uses the same notation throughout.

The biquaternion norm is the object the series calls the **level-1 form**, and it is the reason the framework is written the way it is. It is multiplicative, it is complex-valued in general, and it vanishes on a set of nonzero elements. Multiplicativity is what makes a unit-norm element a transformation that preserves an interval; the complex value is what lets one algebraic object carry the metric of the material sector and the opposite signature on the informational sector; and the vanishing set is the light cone. Invertibility is then the algebraic counterpart of being off the cone, and the group of units is the group of the transformations of the series.

Every claim is proved or checked. The physical readings are identifications with the coordinate dictionary of *Conventions in the Biquaternion Universe*, and they are flagged as readings wherever they occur.

Throughout, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ and the scalar imaginary is $i$, so that it does not collide with the quaternion units. A general biquaternion is

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + i q'_\mu \in \mathbb{C},
$$

with quaternion conjugate $\tilde{Q}^{\natural}$, complex conjugate $\bar{\tilde{Q}}$, Hermitian conjugate $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ and anti-Hermitian conjugate $\tilde{Q}^\flat = -\tilde{Q}^{*}$. The material coordinate is $\tilde{Q} = ict\,e_0 + \mathbf{x}$ with $\mathbf{x} = x e_1 + y e_2 + z e_3$, and the informational coordinate is $\tilde{Q} = ct'\,e_0 + i\mathbf{x}'$ with $\mathbf{x}' = x' e_1 + y' e_2 + z' e_3$.

## The Biquaternion Norm

### Definition

The **biquaternion norm** of a biquaternion is

$$
N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural} = \sum_{\mu=0}^{3} Q_\mu^2 ,
$$

where $\tilde{Q}^{\natural}$ is the quaternion conjugate.

**Basic properties.**

- $N(\tilde{Q})$ is a complex scalar (a complex multiple of $e_0$) in general. It is real on the real sector $\mathbb{H}_{\mathbb{B}}$ and on the imaginary sector $i\mathbb{H}_{\mathbb{B}}$; outside their union it need not be real.
- $N(\tilde{Q})$ is not positive-definite: it can vanish for a nonzero biquaternion. Those are the zero divisors, studied in *Zero Divisors of the General Plain Algebra*; physically they are the null elements, and the light cone is their locus.
- $N(\tilde{Q}^{\natural}) = N(\tilde{Q})$, $N(\tilde{Q}^*) = N(\tilde{Q})^*$ and $N(\tilde{Q}^{*}) = N(\tilde{Q})^*$.

**Physical reading: this is the metric.** On the material coordinate the biquaternion norm is the Minkowski interval,

$$
N\!\left(ict\,e_0 + \mathbf{x}\right) = -c^2t^2 + \mathbf{x}^2 ,
$$

and on the informational coordinate it is the same form with the opposite signature,

$$
N\!\left(ct'\,e_0 + i\mathbf{x}'\right) = c^2(t')^2 - (\mathbf{x}')^2 .
$$

The remaining sections of this article are, in physical terms, the study of this one object: its multiplicativity is the invariance of the interval under the transformations of the theory, its vanishing is the light cone, and its real absolute value is the scale of the polar representation.

### The Polarisation and the Complex Quadratic Space

$N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu=0}^{3} Q_\mu^2$ is homogeneous of degree two, hence is a quadratic form on $\mathbb{B}\cong\mathbb{C}^4$. Its polar form is

$$
N(\tilde{P},\tilde{Q})=\tfrac{1}{2}\bigl(N(\tilde{P}+\tilde{Q})-N(\tilde{P})-N(\tilde{Q})\bigr)=\sum_{\mu=0}^{3} P_\mu Q_\mu,
$$

the complex bilinear dot product, the **general quaternionic bilinear form**, written $\langle\tilde P,\tilde Q\rangle_{\natural}$ elsewhere in the corpus. It is not the general plain bilinear form $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ of *The Ordinary Product and the Material Sector*, from which it differs by the sign of the vector part; and in the mathematical chapter the same polar form carries the letter $B$. It is symmetric and non-degenerate, and the quaternion units are orthonormal,

$$
N(e_\mu,e_\nu)=\delta_{\mu\nu}.
$$

So $(\mathbb{B},N)$ is the standard non-degenerate quadratic space of dimension $4$ over $\mathbb{C}$. The form $N$ is complex-bilinear: it is **not** the Hermitian form $\tilde{P}\tilde{Q}^{*}$ of the next section, and the two must not be conflated. Geometrically $N$ is the form whose vanishing locus is the null cone, the object the quadric of *The Null Quadric and Its Projective Geometry* is built from.

### Multiplicativity

**Theorem.** The biquaternion norm is multiplicative:

$$
N(\tilde{Q} \circ \tilde{R}) = N(\tilde{Q})\,N(\tilde{R}) .
$$

**Proof.** Compute

$$
N(\tilde{Q}\tilde{R}) = (\tilde{Q}\tilde{R})\overline{(\tilde{Q}\tilde{R})} = \tilde{Q}\tilde{R}\tilde{R}^{\natural}\tilde{Q}^{\natural} = \tilde{Q}\,N(\tilde{R})\,\tilde{Q}^{\natural} .
$$

Since $N(\tilde{R})$ is a complex scalar and $e_0$ is central, the factor commutes with $\tilde{Q}$ and with $\tilde{Q}^{\natural}$, so $\tilde{Q}N(\tilde{R})\tilde{Q}^{\natural} = N(\tilde{R})\tilde{Q}\tilde{Q}^{\natural} = N(\tilde{R})N(\tilde{Q})$.

**Corollary.** If either factor has vanishing biquaternion norm, so does the product. In particular the product of a zero divisor with any biquaternion is either zero or a zero divisor: **the null cone is preserved by multiplication**.

**Physical reading: why the rotors work.** An element of unit norm, $N(\tilde{R}) = 1$, is called a **rotor** in the series, and multiplicativity says exactly that a rotor preserves the biquaternion norm of everything it acts on:

$$
N(\tilde{R}\,\tilde{Q}\,\tilde{R}^{*}) = N(\tilde{R})\,N(\tilde{Q})\,N(\tilde{R}^{*}) = |N(\tilde{R})|^2 N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = N(\tilde{Q}) .
$$

With $N$ read as the interval, this is the invariance of the interval under the transformation, which is the Lorentz transformation of the series; the chain of equalities above is the whole algebraic content of it. The four-velocity and the four-momentum are the standard instances:

$$
\tilde{U} = i\gamma c\,e_0 + \gamma\mathbf{v}, \qquad N(\tilde{U}) = -c^2 ,
$$

$$
\tilde{P} = i\frac{E}{c}e_0 + \mathbf{p}, \qquad N(\tilde{P}) = -\frac{E^2}{c^2} + \mathbf{p}^2 = -m^2c^2 \ \text{ on shell},
$$

so the constancy of the biquaternion norm of the four-velocity along a worldline is the statement that the proper time is the same for every observer, and the **mass shell** $E^2 = c^2\mathbf{p}^2 + m^2c^4$ is the statement that the four-momentum lies on the level set $N = -m^2c^2$. The photon is the case $N = 0$, on the light cone. The four-vector calculus itself belongs to *The Four-Vector Element Representation of Biquaternions*; the rotor action belongs to *Biquaternion Rotations and Lorentz Transformations*.

### The Biquaternion Norm as a Semi-Norm

The biquaternion norm of this article is the **semi-norm** of the biquaternion literature (Ward; Sangwine, Ell and Le Bihan), the name recording two departures from a norm: the value is complex rather than real, and a nonzero element can have vanishing value. The audit of the usual axioms is as follows.

- The **sign axiom** holds: $N(-\tilde{Q}) = N(\tilde{Q})$.
- The **triangle inequality** has no content: $\mathbb{C}$ carries no order.
- The **scaling axiom** is **false**, in both the form usually written and the form the complex modulus suggests. Homogeneity is quadratic, $N(\lambda\tilde{Q}) = \lambda^2N(\tilde{Q})$, and for the square root one gets $\sqrt{N(\lambda\tilde{Q})} = \sqrt{\lambda^2}\sqrt{N(\tilde{Q})}$, where the principal square root $\sqrt{\lambda^2}$ lies in the right half-plane and not at $|\lambda|$: with $\lambda = i$ and $\tilde{Q} = e_0$, $\sqrt{N(ie_0)} = \sqrt{-1} = i$ while $|\lambda|\sqrt{N(e_0)} = 1$. For real $\lambda$ the axiom is satisfied, and it is precisely the complex case that the algebra is about.

So the biquaternion norm is a complex-valued multiplicative semi-norm: multiplicative, homogeneous of degree two over the complex scalars, indefinite, vanishing exactly on the zero divisors. A reader applying the scaling axiom with a complex scalar will be off by a factor in the right half-plane. **This is what makes the phase in the polar representation a phase**: the factor by which $N$ fails to be absolute is the factor the polar scale must supply separately.

### The Unique Real Norm, and the Polar Scale

The positive statement about size is sharp. There is a **unique** real norm that is multiplicative and normalised on the real scalars: if $\rho$ is a continuous multiplicative function from the group of units of $\mathbb{B}$ to the non-negative reals with

$$
\rho(\lambda e_0) = |\lambda| \qquad \text{for } \lambda \in \mathbb{R},
$$

then $\rho$ is determined, and it is

$$
r(\tilde{Q}) = \sqrt{|N(\tilde{Q})|} = \sqrt{|\det\Phi(\tilde{Q})|} ,
$$

where $\Phi$ is the $2\times2$ matrix realisation.

**Proof in one paragraph.** The group of units is $\mathrm{GL}_2(\mathbb{C})$ under $\Phi$. A continuous homomorphism from $\mathrm{GL}_2(\mathbb{C})$ to $\mathbb{R}_{>0}$ is constant on the commutator subgroup; that subgroup is $\mathrm{SL}_2(\mathbb{C})$, which is perfect, so the homomorphism factors through the determinant, $\mathrm{GL}_2(\mathbb{C}) \to \mathbb{C}^\times$. A continuous homomorphism $\mathbb{C}^\times \to \mathbb{R}_{>0}$ is $z \mapsto |z|^t$: on the positive reals it is a power, and the unit circle is compact and connected, so its image is trivial. Hence $\rho(\tilde{Q}) = |\det\Phi(\tilde{Q})|^t$, and the normalisation gives $|\lambda|^{2t} = |\lambda|$, so $t = \tfrac12$, which is $r$ because $\det\Phi(\tilde{Q}) = N(\tilde{Q})$.

**Physical reading: this is the scale of the polar representation.** The function $r$ is the real factor of the polar representations of the series: it is the modulus that multiplies the central phase, the boost and the rotor. It vanishes exactly on the zero divisors and is a genuine norm on the units. The physical consequence of the uniqueness is that the scale carried by the polar representation is **not a convention**: it is the only real size function compatible with multiplicativity and with $r(e_0) = 1$. Its reading for the four-position, the four-velocity and the four-momentum — the scale $c\tau$, $c$ and $mc$ — belongs to *The Polar Element Representation of Biquaternions* and *The Polar Element Representation in Subspaces*. The matrix face $\sqrt{|\det\Phi|}$ is the $2\times2$ one; the regular $4\times4$ representation carries $\det = N^2$ instead, as *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* records.

The function $r$ was verified to be multiplicative on random pairs, $r(\tilde{P}\tilde{Q}) = r(\tilde{P})r(\tilde{Q})$, and to satisfy $r(\tilde{Q})^2 = |\det\Phi(\tilde{Q})|$.

### The Biquaternion Norm from the Halves

Writing $\tilde{Q} = q_r + i q_i$ with $q_r, q_i$ real quaternions (the quaternion decomposition of the algebra article), the biquaternion norm splits as

$$
\Re N(\tilde{Q}) = N(q_r) - N(q_i), \qquad \Im N(\tilde{Q}) = 2\langle q_r, q_i\rangle ,
$$

with $\langle q_r, q_i\rangle = \sum_\mu (q_r)_\mu (q_i)_\mu$ the scalar product of the two real quaternions. The special cases read directly:

- $q_r \perp q_i$: the biquaternion norm is real, and negative whenever $N(q_i) > N(q_r)$;
- $N(q_r) = N(q_i)$: the biquaternion norm is purely imaginary;
- $q_r = 0$: the biquaternion norm is $-N(q_i)$, negative real;
- $q_r \perp q_i$ **and** $N(q_r) = N(q_i)$: the biquaternion norm vanishes.

So the criterion $N(\tilde{Q}) = 0$ is the statement that the two halves of the element have **equal norms and vanishing scalar product**, which is the algebraic shape of a null element.

## The Hermitian Form

### Definition

The **Hermitian form** of a biquaternion is the biquaternion $\tilde{Q}\tilde{Q}^{*}$.

- Its **scalar part** is

$$
\mathrm{Sc}\!\left(\tilde{Q}\tilde{Q}^{*}\right) = \sum_{\mu=0}^{3} |Q_\mu|^2 = \sum_{\mu=0}^{3}\left(q_\mu^2 + (q'_\mu)^2\right),
$$

non-negative, vanishing only for $\tilde{Q} = 0$. Its vector part does not vanish in general: for $\tilde{Q} = e_0 + ie_1$, $\tilde{Q}^{*} = \tilde{Q}$ and $\tilde{Q}\tilde{Q}^{*} = (e_0+ie_1)^2 = 2e_0 + 2ie_1$. Note that this same element has $N(\tilde{Q}) = 1 + i^2 = 0$: the two forms are distinct, and an element can be a zero divisor for the biquaternion norm and perfectly regular for the Hermitian one.
- The Hermitian form is **not** multiplicative, and its scalar part is not the biquaternion norm in general.
- It is **Hermitian**: $(\tilde{Q}\tilde{Q}^{*})^{*} = \tilde{Q}\tilde{Q}^{*}$, so it lies in the informational sector $\mathbb{M}_+$.

**Physical reading.** The Hermitian form is the positive-definite object of the pair. Its scalar part is the squared length in the underlying real space, and it vanishes only at the origin; the full form is an element of the informational sector, whose vector part is the part a purely scalar reading of the norm would discard. In the informational side of the series the scalar part is the probabilistic norm and the vector part is the residue that the informational reading has to keep.

### The Euclidean Norm

$$
\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}\!\left(\tilde{Q}\tilde{Q}^{*}\right)} = \sqrt{\sum_{\mu=0}^{3}|Q_\mu|^2} = \sqrt{\sum_{\mu=0}^{3}\left(q_\mu^2 + (q'_\mu)^2\right)} .
$$

It is a genuine norm on the real vector space $\mathbb{B}\cong\mathbb{R}^8$: positive-definite, subadditive and homogeneous of degree one. It is **not** multiplicative.

The trace version is

$$
\mathrm{Tr}\!\left(\tilde{Q}\tilde{Q}^{*}\right) = 2\sum_{\mu=0}^{3}|Q_\mu|^2 = 2\|\tilde{Q}\|_E^2 ,
$$

the Frobenius norm squared of the representing matrix under $\mathbb{B}\cong M_2(\mathbb{C})$.

**Physical reading.** This is the norm that makes the algebra a Hilbert space, and it is the norm with which the operator side of the series is built: the sandwich operators of *Biquaternion Rotations and Lorentz Transformations* are bounded with respect to it, and the probabilistic reading of the informational sector uses it. It is **not** the norm that carries the metric: the metric is the biquaternion norm, indefinite. The two must be kept apart, and the series does keep them apart.

### Relation Between the Biquaternion Norm and the Hermitian Form

- The **biquaternion norm** $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2$ is a complex scalar, multiplicative, capable of vanishing for nonzero $\tilde{Q}$.
- The **Hermitian form** $\tilde{Q}\tilde{Q}^{*}$ is a Hermitian element whose scalar part is $\sum_\mu|Q_\mu|^2$, non-negative and vanishing only at $\tilde{Q} = 0$, with vector part generally nonzero. Not multiplicative.

They coincide as biquaternions exactly when $\tilde{Q}$ lies in the real sector $\mathbb{H}_{\mathbb{B}}$, that is, when all coefficients are real. On the imaginary sector $i\mathbb{H}_{\mathbb{B}}$ the Hermitian form is $+\sum_\mu (q'_\mu)^2\,e_0$, which is the **negative** of the biquaternion norm. So the two forms agree on the real sector, differ by a sign on the imaginary sector, and differ in kind elsewhere.

The two roles are complementary and both are used: the **biquaternion norm** controls the multiplicative structure — invertibility, zero divisors, the metric and the rotors — while the **scalar part of the Hermitian form** controls the topological structure: the Euclidean norm, the topology of $\mathbb{B}$, the completeness of the underlying real space.

## Invertibility

### Definition

A biquaternion $\tilde{Q}$ is **invertible** if there exists $\tilde{R}$ with

$$
\tilde{Q}\circ\tilde{R} = \tilde{R}\circ\tilde{Q} = e_0 ,
$$

and $\tilde{R}$ is then the **inverse** $\tilde{Q}^{-1}$.

### Left and Right Inverses

In a general non-commutative algebra the left, right and two-sided notions differ. Here they coincide: $\mathbb{B}$ is finite-dimensional over $\mathbb{R}$, and in a finite-dimensional algebra over a field a right inverse is also a left inverse and the two are equal. So "the" inverse is unambiguous.

### Criterion for Invertibility

**Theorem.** $\tilde{Q}$ is invertible if and only if $N(\tilde{Q}) \neq 0$.

**Proof.** If $N(\tilde{Q}) \neq 0$, put $\tilde{R} = \tilde{Q}^{\natural}/N(\tilde{Q})$. Then $\tilde{Q}\tilde{R} = \tilde{Q}\tilde{Q}^{\natural}/N(\tilde{Q}) = e_0$, so $\tilde{R}$ is a right inverse, hence an inverse. Conversely, if $\tilde{Q}$ is invertible, applying $N$ to $\tilde{Q}\tilde{Q}^{-1} = e_0$ and using multiplicativity gives $N(\tilde{Q})N(\tilde{Q}^{-1}) = 1$, so $N(\tilde{Q}) \neq 0$.

**Physical reading.** For a material element this criterion says: a four-vector is invertible exactly when it is **not null**. The timelike and spacelike four-vectors are invertible; the lightlike ones are the zero divisors. The algebra partitions the material sector by the light cone, and the physics does the same: this is the algebraic counterpart of the statement that a null vector has no rest frame.

### The Inverse Formula

$$
\tilde{Q}^{-1} = \frac{\tilde{Q}^{\natural}}{N(\tilde{Q})} ,
$$

the biquaternionic analogue of $q^{-1} = \bar{q}/|q|^2$.

**Corollary.** If $\tilde{Q}$ is invertible, so is $\tilde{Q}^{\natural}$, and $(\tilde{Q}^{\natural})^{-1} = \overline{\tilde{Q}^{-1}}$.

**The inverse of a rotor, and the dagger.** For an element of **unit norm**, $N(\tilde{Q}) = 1$, the formula collapses to

$$
\tilde{Q}^{-1} = \tilde{Q}^{\natural} ,
$$

the **quaternion conjugate**. This is the case of every rotor of the series. It is worth naming what the dagger does in comparison, because the two are not the same operation: the dagger equals the quaternion conjugate exactly when $\tilde{Q}$ is **unitary**, $\tilde{Q}\tilde{Q}^{*} = e_0$, and for a rotor that means the rotation rotors. A boost rotor is Hermitian, $\tilde{B}^{*} = \tilde{B}$, so its dagger is itself while its inverse is its quaternion conjugate:

$$
\tilde{B} = \cosh\frac{\psi}{2}e_0 + i\sinh\frac{\psi}{2}\,e_3, \qquad
\tilde{B}^{-1} = \tilde{B}^{\natural} = \cosh\frac{\psi}{2}e_0 - i\sinh\frac{\psi}{2}\,e_3 \neq \tilde{B}^{*} = \tilde{B} .
$$

For a rotation rotor $\tilde{R}$ with real coefficients the two coincide, $\tilde{R}^{-1} = \tilde{R}^{\natural} = \tilde{R}^{*}$, which is why the two operations are interchangeable in the rotation case and must be distinguished in the boost case. The distinction is also what the series states where it matters: the action $\tilde{Q}\mapsto \tilde{R}\tilde{Q}\tilde{R}^{*}$ is an inner automorphism in the unitary sector, where $\tilde{R}^{*} = \tilde{R}^{-1}$, and not elsewhere; see *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*, and the operator article, which takes the dagger sandwich as its subject.

## The Group of Units

### Definition

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\} ,
$$

a group under multiplication with identity $e_0$.

### Basic Properties

**Openness.** $\mathbb{B}^\times = N^{-1}(\mathbb{C}\setminus\{0\})$ is the preimage of an open set under a continuous map, hence open in the Euclidean topology. Physically, the complement of the light cone is open: a small perturbation of a non-null vector stays non-null.

**Non-compactness.** It contains the unbounded real line $\{a e_0 : a \in \mathbb{R}, a \neq 0\}$.

**Connectedness.** $\mathbb{B}^\times$ is **connected**: under $\mathbb{B}\cong M_2(\mathbb{C})$ it is $\mathrm{GL}(2,\mathbb{C})$, and $\mathrm{GL}(n,\mathbb{C})$ is connected (Gram–Schmidt retracts it onto the connected $U(n)$).

**Lie group structure.** $\mathbb{B}^\times$ is a real Lie group of dimension $8$, corresponding to $\mathrm{GL}(2,\mathbb{C})$, a complex Lie group of complex dimension 4. Its Lie algebra is $\mathbb{B}$ itself, with the commutator bracket $[\tilde{P},\tilde{Q}] = \tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$.

**Centre.** The centre of $\mathbb{B}^\times$ is $\mathbb{C}^\times$, the nonzero complex scalars, since the centre of $\mathbb{B}$ is $\mathbb{C}$. Physically, the centre is the two-dimensional complex time sector minus the origin; the central elements act as the identity operator on the algebra up to scale, which is the algebraic form of the statement that an overall complex scale carries no direction.

### The Inverse Map

$$
\iota : \mathbb{B}^\times \to \mathbb{B}^\times, \qquad \iota(\tilde{Q}) = \tilde{Q}^{-1},
$$

is a smooth involution, and its differential at the identity is $-\mathrm{id}_\mathbb{B}$.

## The Three-Way Classification

| Condition on $N(\tilde{Q})$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $N(\tilde{Q}) \neq 0$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

So the algebra is partitioned into the zero element, the invertible elements and the zero divisors, and the partition is disjoint and exhaustive. **Physically, on the material sector, this is the partition of four-vectors into the null ones and the rest**: the zero divisors are the lightlike four-vectors and their multiples, and they are the physical locus of the light cone.

### The Algebra Is Not a Division Algebra

A **division algebra** is one in which every nonzero element is invertible, equivalently one with no zero divisors. The biquaternion algebra has zero divisors and is therefore **not** a division algebra, in contrast with the Frobenius theorem, which says that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. **This is not a defect in the physics but the physics itself**: the light cone exists because the algebra is not a division algebra, and a division algebra over the reals would give no null directions and hence no propagation velocity.

## Distribution of the Invertible Elements

The criterion is the same in all remarkable subspaces: invertible if and only if the biquaternion norm is nonzero. The distribution is read off physically subspace by subspace.

### The Complex Time Sector $\mathbb{C}_{\mathbb{B}}$

$\tilde{Q} = Q_0 e_0$ with $Q_0 \in \mathbb{C}$ gives $N(\tilde{Q}) = Q_0^2$, which vanishes only for $\tilde{Q} = 0$. Every nonzero element is invertible: the sector is a copy of the field $\mathbb{C}$, and its parameter pair $(ct', ict)$ is never null.

### The Complex Space Sector $\mathrm{Vect}(\mathbb{B})$

With $\tilde{Q} = Q_1e_1+Q_2e_2+Q_3e_3$,

$$
N(\tilde{Q}) = Q_1^2+Q_2^2+Q_3^2 = \left(q_1^2+q_2^2+q_3^2-(q'_1)^2-(q'_2)^2-(q'_3)^2\right) + 2i\left(q_1q'_1+q_2q'_2+q_3q'_3\right).
$$

The real part is an indefinite form of signature $(3,3)$ on the six-dimensional sector and the imaginary part a second real form; the two vanish together exactly on the complex cone

$$
Q_1^2+Q_2^2+Q_3^2 = 0 ,
$$

the **nilpotent cone**, whose nonzero elements are the pure zero divisors. As a complex cone in $\mathbb{C}^3$ it has real dimension 4, hence real codimension 2 in the six-dimensional sector, and its complement — the invertible elements — is therefore **connected**. The physical reading is that this sector carries the two spatial triples $(x,y,z)$ and $(ix',iy',iz')$ at once, and a complex spatial vector can be null only through a conspiracy of both: the condition is two real equations, not one, so it does not divide the sector into regions the way a light cone does.

The intersection $\mathrm{Vect}(\mathbb{B})\cap\mathbb{H}_{\mathbb{B}} = \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ consists of invertible elements away from the origin, since $N$ restricts to $q_1^2+q_2^2+q_3^2$ there: **the real spatial vectors are never null**.

### The Real Sector $\mathbb{H}_{\mathbb{B}}$

$N(\tilde{Q}) = q_0^2+q_1^2+q_2^2+q_3^2$, a sum of squares, vanishing only at the origin. Every nonzero element is invertible, and there is no light cone: the real sector carries the coordinates $ct', x, y, z$ and no null direction at all. It is a copy of the division algebra $\mathbb{H}$ and the home of the rotation rotors.

### The Imaginary Sector $i\mathbb{H}_{\mathbb{B}}$

For $\tilde{Q} = i\tilde{P}$ with $\tilde{P}\in\mathbb{H}_{\mathbb{B}}$ real,

$$
N(i\tilde{P}) = -\sum_{\mu=0}^{3}p_\mu^2 ,
$$

**negative-definite**, vanishing only at the origin, so there are no zero divisors either. Its signature $(0,4)$ is the exact negative of the $(4,0)$ of the real sector, as $N(i\tilde{Q}) = -N(\tilde{Q})$ requires. This sector carries $ict, ix', iy', iz'$.

### The Informational Sector $\mathbb{M}_+$

For $\tilde{Q} = q_0e_0 + iq'_1e_1+iq'_2e_2+iq'_3e_3$,

$$
N(\tilde{Q}) = q_0^2-(q'_1)^2-(q'_2)^2-(q'_3)^2 ,
$$

indefinite of signature $(1,3)$, vanishing on the double cone

$$
q_0^2 = (q'_1)^2+(q'_2)^2+(q'_3)^2 .
$$

In the informational coordinate $ct'\,e_0+i\mathbf{x}'$ this is $c^2(t')^2 = (\mathbf{x}')^2$: the informational cone. The invertible elements are the complement, with three connected components — the **future** $q_0>0$, $q_0^2>(\mathbf{q}')^2$ with $N>0$; the **past** $q_0<0$, $q_0^2>(\mathbf{q}')^2$ with $N>0$; and the **inside** $q_0^2<(\mathbf{q}')^2$ with $N<0$.

### The Material Sector $\mathbb{M}_-$

For $\tilde{Q} = iq'_0e_0 + q_1e_1+q_2e_2+q_3e_3$,

$$
N(\tilde{Q}) = -(q'_0)^2+q_1^2+q_2^2+q_3^2 ,
$$

indefinite of signature $(3,1)$, vanishing on the light cone

$$
(q'_0)^2 = q_1^2+q_2^2+q_3^2 .
$$

**This is the physical light cone**, and the sector is the material sector: with the dictionary $q'_0 = ct$, the components of the invertible set are the ones physics names.

- **spacelike** region $q_1^2+q_2^2+q_3^2 > (q'_0)^2$, on which $N > 0$;
- **future timelike** region $q'_0 > 0$ and $(q'_0)^2 > \mathbf{q}^2$, on which $N < 0$;
- **past timelike** region $q'_0 < 0$ and $(q'_0)^2 > \mathbf{q}^2$, on which $N < 0$.

The light cone itself is the zero-divisor set, and its elements are the null four-vectors. A four-momentum on the cone is a photon; a four-momentum off the cone is massive, with $N = -m^2c^2$ on shell. The two timelike components are the two directions of time evolution, and they are the reason the series can speak of a future and a past in purely algebraic terms: the level sets of $N$ on the material sector separate the two.

### Summary of the Distribution

- $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain **no** zero divisors: every nonzero element is invertible. The first two are the subalgebras among the remarkable subspaces and the division algebras; $i\mathbb{H}_{\mathbb{B}}$ is a module and not a subalgebra, but its nonzero elements are invertible in $\mathbb{B}$.
- $\mathbb{M}_-$ and $\mathbb{M}_+$ each contain a cone of zero divisors, and the invertible elements form the complement, with three connected components each: the physical light cone of the material sector, and its informational counterpart.
- $\mathrm{Vect}(\mathbb{B})$ contains the nilpotent cone, of real codimension 2, whose complement is connected.

The two cones in the sectors have the same structure, each being the vanishing set of an indefinite form of signature $(1,3)$ or $(3,1)$, of codimension 1 in a four-dimensional space. The cone in the complex space sector is different: the biquaternion norm is complex there, its vanishing imposes two real conditions, and the complement is connected and not divided into regions.

## The Real Forms and Their Signatures

Over $\mathbb{C}$ a non-degenerate quadratic form has no signature; signature appears only after a real form is chosen. With $Q_\mu=q_\mu+iq'_\mu$, $q_\mu,q'_\mu\in\mathbb{R}$,
$$
\operatorname{Re}N=\sum_{\mu=0}^{3}\bigl(q_\mu^2-(q'_\mu)^2\bigr),\qquad \operatorname{Im}N=2\sum_{\mu=0}^{3} q_\mu q'_\mu .
$$
Hence the realification $\operatorname{Re}N$ on $\mathbb{R}^8$ is non-degenerate of signature $(4,4)$, a **split** (neutral) signature; in the real basis $e_\mu,ie_\mu$ its matrix is $\operatorname{diag}(1,1,1,1,-1,-1,-1,-1)$. The remarkable real subspaces give six real forms, whose signatures are the ones read off sector by sector in *Distribution of the Invertible Elements*:

| Real subspace | $N$ restricted | Signature |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $q_0^2-(q'_0)^2$ | $(1,1)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $q_1^2+q_2^2+q_3^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(3,3)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\sum q_\mu^2$ | $(4,0)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $-\sum (q'_\mu)^2$ | $(0,4)$ |
| $\mathbb{M}_+$ | $q_0^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(1,3)$ |
| $\mathbb{M}_-$ | $-(q'_0)^2+q_1^2+q_2^2+q_3^2$ | $(3,1)$ |

Each is a real slice whose complexification is $(\mathbb{B},N)$; the definite forms are $(4,0)$ and $(0,4)$, the indefinite ones $(1,3)$ and $(3,1)$, the neutral ones $(1,1)$ and $(3,3)$. The sign is the choice of geometry, the datum the geometry of *Biquaternion Lorentzian and Conformal Geometry* is organised by.

Beyond the remarkable subspaces, a mixed real subspace carries a signature of its own. The one the geometry uses is the **split form of signature $(2,2)$**,
$$
W=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,ie_2,ie_3\},\qquad N|_W=a^2+b^2-c^2-d^2 \quad \text{for } a e_0+b e_1+ci e_2+di e_3,
$$
of real dimension $4$ and matrix $\operatorname{diag}(1,1,-1,-1)$; its complexification is $(\mathbb{B},N)$, and its projective quadric is the doubly ruled real surface $S^1\times S^1$ (*The Null Quadric and Its Projective Geometry*, *Biquaternion Lorentzian and Conformal Geometry*).

## The Relation to the Hermitian Decomposition

The invertibility criterion is stated with the biquaternion norm; the Hermitian decomposition $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ relates it to the Hermitian form:

- for $\tilde{Q}\in\mathbb{M}_+$, $N$ is real, positive in the future and past regions and negative inside the cone;
- for $\tilde{Q}\in\mathbb{M}_-$, $N$ is real, positive in the spacelike region and negative in the two timelike regions;
- for a general $\tilde{Q} = \tilde{Q}_++\tilde{Q}_-$ with both parts nonzero, $N$ need not be real, and invertibility is a condition on both its real and its imaginary parts.

The scalar part of the Hermitian form, by contrast, is non-negative and definite on all of $\mathbb{B}$: it vanishes only at the origin and **does not detect the zero divisors at all**. The two forms answer different questions — "is this element invertible" and "how large is this element" — and the series uses them for those two questions respectively.

## Physical Readings

The norm reads as mass and its zero set as light, and the article's own reading is that the norm of the algebra is a semi-norm and not a norm in the analytic sense. Two further readings belong with it. The norm is reversed by the central generator, $N(i\tilde Q) = -N(\tilde Q)$, so the exchange that ticks the clock also flips the sign of the mass form (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). And invertibility fails exactly on the zero divisors, so the directions that travel at $c$ are the directions that cannot be inverted, which is the framework's algebraic reason that light is a boundary rather than a state.

The norm is read as a **scale** and its logarithm $\log\lvert N\rvert$ as a **dilation potential**: a change of the norm is a change of the unit of length, so the norm is what a conformal (Weyl) rescaling acts on, and the polar scale $r$ of *The Polar Element Representation of Biquaternions* is the explicit factor. The reading stands next to the interval reading and does not replace it: the norm is the interval of the material sector (a metric) and the scale of any element (a dilation potential). The norm's fourth part, its **argument**, is not a reading of its own: $N$ is the determinant of the matrix realization and the polar central phase is $\alpha=\tfrac12\arg\det\Phi(\tilde{Q})$, so $\arg N=2\alpha$, twice the central phase owned by *The Polar Element Representation of Biquaternions*. The norm therefore carries three readings — the modulus the scale, the real part the interval and the imaginary part the coupling of the two real quaternions $q_r$ and $q_i$ whose norms it subtracts and whose scalar product it doubles — and its argument belongs to the central-rotation band and not here.

## Summary

The biquaternion norm $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ is a complex-valued multiplicative quadratic form, the semi-norm of the literature. It is the level-1 form and is the metric of the framework: it is the Minkowski interval on the material coordinate and the opposite signature on the informational one. It is not positive-definite and it vanishes on the zero divisors, which on the material sector is the light cone. Of the usual norm axioms only the sign axiom survives; the scaling axiom fails for complex scalars, since $\sqrt{\lambda^2}$ lies in the right half-plane and not at $|\lambda|$. The absolute square root $r = \sqrt{|N(\tilde{Q})|} = \sqrt{|\det\Phi(\tilde{Q})|}$ is the **unique** multiplicative real norm on the units normalised by $r(\lambda e_0) = |\lambda|$ for real $\lambda$, and it is the real scale of the polar representations.

The Hermitian form $\tilde{Q}\tilde{Q}^{*}$ is a Hermitian biquaternion, an element of the informational sector, whose scalar part $\sum_\mu|Q_\mu|^2$ is non-negative and definite and defines the Euclidean norm on $\mathbb{B}\cong\mathbb{R}^8$; its vector part vanishes exactly when $\tilde{Q} = (\alpha+i\beta)A$ with $\alpha,\beta\in\mathbb{R}$ and $A$ a real quaternion. It is not multiplicative and it does not detect the zero divisors.

The invertibility criterion is $N(\tilde{Q})\neq0$, with inverse $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/N(\tilde{Q})$. On the material sector it says that a four-vector is invertible exactly when it is not null. For a unit-norm element — every rotor — the inverse is the quaternion conjugate, $\tilde{Q}^{-1} = \tilde{Q}^{\natural}$, and this coincides with the dagger exactly for the unitary rotors, the rotation rotors; a boost rotor is Hermitian and its dagger is itself, not its inverse.

The group of units $\mathbb{B}^\times$ is open, connected and isomorphic to $\mathrm{GL}(2,\mathbb{C})$, a real Lie group of dimension 8 with Lie algebra $\mathbb{B}$ and centre $\mathbb{C}^\times$. The algebra is partitioned into the zero element, the invertible elements and the zero divisors, and this is the partition of four-vectors into the null ones and the rest. Of the remarkable subspaces, $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain no zero divisors; $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a cone each, with three-component complements; and $\mathrm{Vect}(\mathbb{B})$ contains the complex nilpotent cone of codimension 2, whose complement is connected.

The zero divisors are studied in *Zero Divisors of the General Plain Algebra*, and the classification of the roots of $-1$ that underlies the idempotent classification in *Biquaternion Square Roots of Minus One, Zero and Plus One*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + iq'_\mu$ | Complex coefficient |
| $ict\,e_0+\mathbf{x}$ | Material coordinate |
| $ct'\,e_0+i\mathbf{x}'$ | Informational coordinate |
| $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm; the level-1 form; the semi-norm of the literature |
| $N(ict\,e_0+\mathbf{x}) = -c^2t^2+\mathbf{x}^2$ | The interval on the material sector |
| $N(\tilde{U}) = -c^2$ | Four-velocity |
| $N(\tilde{P}) = -m^2c^2$ on shell | Four-momentum, the mass shell |
| $r(\tilde{Q}) = \sqrt{|N(\tilde{Q})|} = \sqrt{|\det\Phi(\tilde{Q})|}$ | The unique multiplicative real norm on the units; the polar scale |
| $\tilde{Q}\tilde{Q}^{*}$ | Hermitian form (a Hermitian biquaternion) |
| $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*}) = \sum_\mu|Q_\mu|^2$ | Scalar part of the Hermitian form |
| $\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})}$ | Euclidean norm |
| $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/N(\tilde{Q})$ | Inverse |
| $\tilde{Q}^{-1} = \tilde{Q}^{\natural}$ for $N(\tilde{Q}) = 1$ | Inverse of a rotor |
| $\mathbb{B}^\times$ | Group of units |
| $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | Complex time, real and imaginary sectors: no zero divisors |
| $\mathbb{M}_-$ | Material sector: the light cone of zero divisors |
| $\mathbb{M}_+$ | Informational sector: the informational cone |
| $\mathrm{Vect}(\mathbb{B})$ | Complex space sector: the nilpotent cone |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions and the zero divisors.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the semi-norm and its axioms, the unique real norm and the Hermitian form.
- Lidia Obojska, "Patterns of maximally entangled states within the algebra of biquaternions", *Journal of Physics Communications* **4** (2020) 055018, for a use of the complex semi-norm and the pairing $S(VW^\dagger)$ in an entanglement context.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the unique multiplicative real norm of the algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
