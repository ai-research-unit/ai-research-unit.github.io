# __Biquaternion Norm and Invertibility__

## Introduction

This article studies the biquaternion norm of the algebra and the invertibility of its elements. It follows the basic algebra article, which defined the algebra, its conjugations, and its six distinguished subspaces. The goal here is to define the biquaternion norm and polarise it, to read the algebra as a complex quadratic space, to tabulate the real forms and their signatures, to record the associated Clifford algebra, to define the Euclidean norm from the Hermitian form, to establish the criterion for invertibility, and to describe the group of units.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations, its six distinguished subspaces and its Hermitian form.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\bar{\tilde{Q}}$, the complex conjugate is denoted $\tilde{Q}^*$, the Hermitian conjugate is denoted $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is denoted $\tilde{Q}^\flat = -\tilde{Q}^\dagger$.

## The Biquaternion Norm

### Definition

The **biquaternion norm** of a biquaternion $\tilde{Q}$ is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2,
$$

where $\bar{\tilde{Q}}$ is the quaternion conjugate.

**Basic properties.**

- $N(\tilde{Q})$ is a complex scalar (a complex multiple of $e_0$) in general. It is real on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and on the imaginary translate $i \mathbb{H}_{\mathbb{B}}$; outside their union it need not be real.
- $N(\tilde{Q})$ is not positive-definite: it can vanish for a nonzero biquaternion. The nonzero elements with vanishing norm are the zero divisors, studied in the article on biquaternion zero divisors.
- $N(\tilde{Q})$ is invariant under quaternion conjugation: $N(\bar{\tilde{Q}}) = N(\tilde{Q})$.
- $N(\tilde{Q})$ is complex-conjugated under complex conjugation: $N(\tilde{Q}^*) = N(\tilde{Q})^*$.
- $N(\tilde{Q})$ is complex-conjugated under Hermitian conjugation: $N(\tilde{Q}^\dagger) = N(\bar{\tilde{Q}}^*) = N(\tilde{Q})^*$.

### The Polarisation and the Complex Quadratic Space

$N(\tilde{Q})=\sum_{\mu=0}^{3} Q_\mu^2$ is homogeneous of degree two, hence is a quadratic form on $\mathbb{B}\cong\mathbb{C}^4$. Its polar form is
$$
B(\tilde{P},\tilde{Q})=\tfrac{1}{2}\bigl(N(\tilde{P}+\tilde{Q})-N(\tilde{P})-N(\tilde{Q})\bigr)=\sum_{\mu=0}^{3} P_\mu Q_\mu,
$$
the complex bilinear dot product. It is symmetric and non-degenerate, and the quaternion units are orthonormal:
$$
B(e_\mu,e_\nu)=\delta_{\mu\nu}.
$$
So $(\mathbb{B},N)$ is the standard non-degenerate quadratic space of dimension $4$ over $\mathbb{C}$. The form $B$ is complex-bilinear; it is not the Hermitian inner product $\sum_\mu P_\mu^*Q_\mu$ of the basic algebra article.

### Multiplicativity

**Theorem.** The biquaternion norm is multiplicative:

$$
N(\tilde{Q} \circ \tilde{R}) = N(\tilde{Q}) \, N(\tilde{R}).
$$

**Proof.** Compute

$$
N(\tilde{Q} \circ \tilde{R}) = (\tilde{Q} \tilde{R}) \overline{(\tilde{Q} \tilde{R})} = \tilde{Q} \tilde{R} \bar{\tilde{R}} \bar{\tilde{Q}} = \tilde{Q} N(\tilde{R}) \bar{\tilde{Q}}.
$$

Since $N(\tilde{R})$ is a complex scalar (a multiple of $e_0$) and $e_0$ is central in $\mathbb{B}$, the factor $N(\tilde{R})$ commutes with $\tilde{Q}$ and with $\bar{\tilde{Q}}$. So

$$
\tilde{Q} N(\tilde{R}) \bar{\tilde{Q}} = N(\tilde{R}) \tilde{Q} \bar{\tilde{Q}} = N(\tilde{R}) N(\tilde{Q}).
$$

**Corollary.** If $N(\tilde{Q}) \neq 0$ and $N(\tilde{R}) \neq 0$, then $N(\tilde{Q} \circ \tilde{R}) \neq 0$.

**Corollary.** If $N(\tilde{Q}) = 0$ or $N(\tilde{R}) = 0$, then $N(\tilde{Q} \circ \tilde{R}) = 0$. In particular, the product of a zero divisor with any biquaternion is either zero or a zero divisor.

### The Biquaternion Norm as a Semi-Norm

The norm of this article is the **semi-norm** of the biquaternion literature (Ward; Sangwine, Ell and Le Bihan). The name records two departures from a norm: the value is complex rather than real, and a non-zero element can have vanishing value, the vanishing locus being exactly the zero divisors. It is worth recording which of the usual norm axioms survive, because the article uses the symbol $N$ and the multiplicativity theorem speaks of a norm; the audit, following Sangwine, Ell and Le Bihan, is as follows.

- The sign axiom holds: $N(-\tilde{Q}) = N(\tilde{Q})$, because negating a complex number does not change its square and therefore does not change $\sum_\mu Q_\mu^2$.
- The triangle inequality has no content here: $\mathbb{C}$ carries no order, so there is no inequality to prove or to refute.
- The scaling axiom is **false**, in both the form usually written and the form the complex modulus suggests. For the biquaternion norm the homogeneity is quadratic, $N(\lambda\tilde{Q}) = \lambda^2N(\tilde{Q})$. For its square root, the complex modulus $\sqrt{N}$, one gets $\sqrt{N(\lambda\tilde{Q})} = \sqrt{\lambda^2}\,\sqrt{N(\tilde{Q})}$, and the principal square root $\sqrt{\lambda^2}$ lies in the right half-plane and not at $|\lambda|$: with $\lambda = i$ and $\tilde{Q} = e_0$, $\sqrt{N(\lambda\tilde{Q})} = \sqrt{-1} = i$ while $|\lambda|\sqrt{N(\tilde{Q})} = 1$. For real $\lambda$ the axiom is satisfied, $\sqrt{\lambda^2} = |\lambda|$, and it is precisely the complex case that the algebra is about.

So the biquaternion norm is a complex-valued multiplicative semi-norm: multiplicative, homogeneous of degree two over the complex scalars, indefinite, and vanishing exactly on the zero divisors. A reader who applies the scaling axiom with a complex scalar will be off by a factor lying in the right half-plane.

### The Unique Real Norm, and the Polar Scale

The positive statement about size is sharper than the audit, and Sangwine, Ell and Le Bihan quote it from Gürlebeck and Sprössig: there is a **unique** real norm that is multiplicative and normalised on the real scalars. In the notation of this article, let $\rho$ be a continuous multiplicative function from the group of units of $\mathbb{B}$ to the non-negative reals, normalised by

$$
\rho(\lambda e_0) = |\lambda| \qquad\text{for } \lambda \in \mathbb{R}.
$$

Then $\rho$ is uniquely determined, and it is

$$
r(\tilde{Q}) = \sqrt{|N(\tilde{Q})|} .
$$

**Proof.** The biquaternion norm is a surjective group homomorphism $N : \mathbb{B}^\times \to \mathbb{C}^\times$ — multiplicative, and surjective because $N(\lambda e_0) = \lambda^2$ attains every nonzero complex value — with kernel the norm-one group $G_1 = \{\tilde{Q} : N(\tilde{Q}) = 1\}$. A continuous homomorphism into the abelian group $\mathbb{R}_{>0}$ is trivial on the commutator subgroup; the norm-one group $G_1$ is perfect, equal to its own commutator subgroup, so $\rho$ is trivial on $G_1$ and factors as $\rho = f \circ N$ for a continuous homomorphism $f : \mathbb{C}^\times \to \mathbb{R}_{>0}$. Every such $f$ is $z \mapsto |z|^t$: on the positive reals it is a continuous homomorphism to $\mathbb{R}_{>0}$, hence a power, and the unit circle, being compact and connected, maps to the identity. The normalisation $\rho(\lambda e_0) = f(\lambda^2) = |\lambda|^{2t} = |\lambda|$ forces $t = \tfrac12$, so $\rho(\tilde{Q}) = |N(\tilde{Q})|^{1/2} = r(\tilde{Q})$.

The function $r$ is multiplicative, $r(\tilde{P}\tilde{Q}) = r(\tilde{P})r(\tilde{Q})$, by multiplicativity of the biquaternion norm, and satisfies $r(\tilde{Q})^2 = |N(\tilde{Q})|$; it vanishes on the zero divisors, and is therefore a semi-norm on $\mathbb{B}$ while remaining a genuine norm on the units. It is defined by multiplicativity together with the normalisation $r(e_0) = 1$: the proposition says it is the only real size function on the units compatible with those two requirements.

### The Biquaternion Norm from the Halves

Writing a biquaternion as $\tilde{Q} = q_r + iq_i$ with $q_r$ and $q_i$ real quaternions, the biquaternion norm splits as

$$
\Re N(\tilde{Q}) = N(q_r) - N(q_i), \qquad \Im N(\tilde{Q}) = 2\,\langle q_r, q_i\rangle,
$$

where $\langle q_r, q_i\rangle = \sum_\mu (q_r)_\mu (q_i)_\mu$ is the scalar product of the two real quaternions. The real part is a difference of two biquaternion norms and the imaginary part is twice a scalar product, so the special cases of the biquaternion norm are read directly:

- $q_r \perp q_i$: the biquaternion norm is real, and it is negative whenever $N(q_i) > N(q_r)$.
- $N(q_r) = N(q_i)$: the biquaternion norm is purely imaginary.
- $q_r = 0$ (an imaginary biquaternion): the biquaternion norm is negative real, $-N(q_i)$, so its square root is imaginary.
- $q_r \perp q_i$ and $N(q_r) = N(q_i)$: the biquaternion norm vanishes. These are exactly the zero divisors, so the criterion $N(\tilde{Q}) = 0$ of the article on biquaternion zero divisors is the statement that the two halves have equal norms and vanishing scalar product; that article splits the same set into the pure and non-pure families by the vanishing of the scalar part.

## The Euclidean Norm and the Hermitian Form

The **Hermitian form** $\tilde{Q} \tilde{Q}^\dagger$ is defined, with its basic properties, in *Biquaternion Algebra*, §*The Hermitian Form*, immediately before the inner product there. This article reads the metric from it: the Euclidean norm below, and the relation of its scalar part to the biquaternion norm.

### The Euclidean Norm

The **Euclidean norm** of a biquaternion is defined by the scalar part of the Hermitian form:

$$
\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^\dagger\right)} = \sqrt{\sum_{\mu=0}^{3} |Q_\mu|^2} = \sqrt{\sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu)}.
$$

It is a genuine norm on the real vector space $\mathbb{B} \cong \mathbb{R}^8$: positive-definite, subadditive, and homogeneous of degree one. It is **not** multiplicative with respect to the biquaternion product.

**Notation.** The scalar part of the Hermitian form is often written $\|\tilde{Q}\|_E^2$; the trace version is

$$
\mathrm{Tr}\!\left(\tilde{Q} \tilde{Q}^\dagger\right) = 2 \sum_{\mu=0}^{3} |Q_\mu|^2 = 2 \|\tilde{Q}\|_E^2.
$$

### Relation Between the Biquaternion Norm and the Hermitian Form

The two forms are related as follows:

- The **biquaternion norm** $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ is a complex scalar (a multiple of $e_0$), multiplicative, and can vanish for nonzero $\tilde{Q}$.
- The **Hermitian form** $\tilde{Q} \tilde{Q}^\dagger$ is a Hermitian biquaternion whose scalar part is $\sum_\mu |Q_\mu|^2$ (non-negative, vanishing only at $\tilde{Q} = 0$) and whose vector part need not vanish. It is not multiplicative.

They coincide as biquaternions if and only if $\tilde{Q}$ lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, i.e. if and only if all the coefficients $Q_\mu$ are real. On the imaginary translate $i \mathbb{H}_{\mathbb{B}}$, the Hermitian form is also scalar-valued, but it equals $+\sum_\mu q'^2_\mu \cdot e_0$, which is the negative of the biquaternion norm; on that subspace the two forms differ by a sign.

The two forms play different roles:

- The **biquaternion norm** controls the multiplicative structure: it determines invertibility, zero divisors, and the multiplicativity of the biquaternion norm.
- The **scalar part of the Hermitian form** (equivalently the diagonal value $\langle \tilde{Q}, \tilde{Q}\rangle$ of the inner product formed in *Biquaternion Algebra*) controls the topological structure: it defines the Euclidean norm, the topology of $\mathbb{B}$, and the completeness of the underlying real vector space.

## The Real Forms and Their Signatures

Over $\mathbb{C}$ a non-degenerate quadratic form has no signature; signature appears only after a real form is chosen. With $Q_\mu=q_\mu+iq'_\mu$, $q_\mu,q'_\mu\in\mathbb{R}$,
$$
\operatorname{Re}N=\sum_{\mu=0}^{3}\bigl(q_\mu^2-q'_\mu{}^2\bigr),\qquad \operatorname{Im}N=2\sum_{\mu=0}^{3} q_\mu q'_\mu .
$$
Hence the realification $\operatorname{Re}N$ on $\mathbb{R}^8$ is non-degenerate of signature $(4,4)$, a **split** (neutral) signature; in the real basis $e_\mu,ie_\mu$ its matrix is $\operatorname{diag}(1,1,1,1,-1,-1,-1,-1)$. The six distinguished real subspaces $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ (the eigenspaces of the three involutions $\bar{\cdot},{}^{*},\dagger$ of the basic algebra article) give six real forms:

| Real subspace | $N$ restricted | Signature |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $q_0^2-(q'_0)^2$ | $(1,1)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $q_1^2+q_2^2+q_3^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(3,3)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\sum q_\mu^2$ | $(4,0)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $-\sum (q'_\mu)^2$ | $(0,4)$ |
| $\mathbb{M}_+$ | $q_0^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(1,3)$ |
| $\mathbb{M}_-$ | $-(q'_0)^2+q_1^2+q_2^2+q_3^2$ | $(3,1)$ |

Each is a real slice whose complexification is $(\mathbb{B},N)$. The full realification is split; the Lorentzian slice is $\mathbb{M}_+$, and up to sign $\mathbb{M}_-$.

## The Associated Clifford Algebra

With the series convention $v^2=N(v)\cdot1$,
$$
\mathrm{Cl}(\mathbb{B},N)\cong\mathrm{Cl}_4(\mathbb{C})\cong M_4(\mathbb{C}),\qquad \mathrm{Cl}_{4,4}\cong M_{16}(\mathbb{R}),
$$
the second being the split real form of signature $(4,4)$, the case $p-q\equiv0\pmod 8$. The even part is
$$
\mathrm{Cl}^+(\mathbb{B},N)\cong\mathrm{Cl}_3(\mathbb{C})\cong\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B},
$$
whose two simple summands are the two chiralities, matched to the rulings in *Biquaternion Spin Geometry*, §*The Spinor Module and Its Two Chiral Halves*.

A caution. The biquaternion algebra itself is the even Clifford algebra $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$ of the Minkowski quadratic space of signature $(1,3)$ (*The Clifford Structure of the Biquaternion Algebra*). That is a different Clifford algebra, attached to a different quadratic space; it is not $\mathrm{Cl}(\mathbb{B},N)$.

---

## Invertibility

### Definition

A biquaternion $\tilde{Q}$ is **invertible** if there exists a biquaternion $\tilde{R}$ such that

$$
\tilde{Q} \circ \tilde{R} = \tilde{R} \circ \tilde{Q} = e_0.
$$

The biquaternion $\tilde{R}$, if it exists, is the **inverse** of $\tilde{Q}$ and is denoted $\tilde{Q}^{-1}$.

### Left and Right Inverses

In a general non-commutative algebra, the notions of left inverse, right inverse, and two-sided inverse are distinct. An element may have a right inverse without having a left inverse, and vice versa.

In the biquaternion algebra, however, these three notions coincide. The reason is that $\mathbb{B}$ is finite-dimensional over $\mathbb{R}$ (of dimension $8$), and in a finite-dimensional algebra over a field, if an element has a right inverse, then it also has a left inverse, and the two are equal. So we may speak of "the" inverse of $\tilde{Q}$ without ambiguity.

### Criterion for Invertibility

**Theorem.** A biquaternion $\tilde{Q}$ is invertible if and only if its biquaternion norm is nonzero:

$$
N(\tilde{Q}) \neq 0.
$$

**Proof.** Suppose $N(\tilde{Q}) \neq 0$. Define

$$
\tilde{R} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})}.
$$

Then

$$
\tilde{Q} \circ \tilde{R} = \frac{\tilde{Q} \bar{\tilde{Q}}}{N(\tilde{Q})} = \frac{N(\tilde{Q})}{N(\tilde{Q})} = e_0,
$$

so $\tilde{R}$ is a right inverse of $\tilde{Q}$. By the remark above, $\tilde{R}$ is also a left inverse, and hence $\tilde{Q}$ is invertible.

Conversely, suppose $\tilde{Q}$ is invertible. Applying the biquaternion norm to $\tilde{Q} \circ \tilde{Q}^{-1} = e_0$ and using multiplicativity gives

$$
N(\tilde{Q}) N(\tilde{Q}^{-1}) = N(e_0) = 1,
$$

so $N(\tilde{Q}) \neq 0$.

### The Inverse Formula

When $N(\tilde{Q}) \neq 0$, the inverse is

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})}.
$$

This is the biquaternionic analogue of the formula $q^{-1} = \bar{q}/|q|^2$ for quaternions.

**Proof.** The verification is the computation in the first part of the proof of the criterion.

**Corollary.** If $\tilde{Q}$ is invertible, then so is $\bar{\tilde{Q}}$, and $(\bar{\tilde{Q}})^{-1} = \overline{\tilde{Q}^{-1}}$.

## The Group of Units

### Definition

The **group of units** of $\mathbb{B}$ is the set of invertible elements:

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\}.
$$

It is a group under multiplication, with identity $e_0$.

### Basic Properties

**Openness.** The group of units is an open subset of $\mathbb{B}$ in the Euclidean topology. Indeed, the biquaternion norm $N : \mathbb{B} \to \mathbb{C}$ is a continuous map, and $\mathbb{B}^\times = N^{-1}(\mathbb{C} \setminus \{0\})$ is the preimage of an open set.

**Non-compactness.** The group of units is not compact, because it contains the real line $\{a e_0 : a \in \mathbb{R}, a \neq 0\}$, which is unbounded.

**Connected components.** The group of units is **connected**. It is the complement in $\mathbb{B}$ of the null cone together with the origin, $\mathbb{B}^\times = \{\tilde{Q} : N(\tilde{Q}) \neq 0\}$. The null cone is a cone of real codimension two, and its intersection with each sphere centred at the origin is connected, so the cone does not separate the algebra; its complement, the group of units, is therefore connected.

**Group structure.** The group of units is a topological group of real dimension $8$. Its Lie structure — the smoothness of the multiplication and the inversion, and the Lie algebra $\mathbb{B}$ with the commutator bracket $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$ — is analytic and is in *Biquaternion Lie Group and Exponential Structure*.

**Center.** The center of $\mathbb{B}^\times$ is $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$, the group of nonzero complex scalars. This follows from the fact that the center of $\mathbb{B}$ is $\mathbb{C}$.

### The Inverse Map

The **inverse map**

$$
\iota : \mathbb{B}^\times \to \mathbb{B}^\times, \qquad \iota(\tilde{Q}) = \tilde{Q}^{-1},
$$

is an involution of the group. Its smooth structure, and the differential at the identity that explains the antisymmetry of the Lie algebra bracket, are Lie-group theory and are in *Biquaternion Lie Group and Exponential Structure*.

## The Three-Way Classification

Combining the criterion for invertibility with the definition of the zero element, we obtain a complete classification of the elements of $\mathbb{B}$:

| Condition on $N(\tilde{Q})$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $N(\tilde{Q}) \neq 0$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $N(\tilde{Q}) = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $N(\tilde{Q}) = 0$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

So the algebra $\mathbb{B}$ is partitioned into three classes: the zero element, the invertible elements, and the zero divisors. The zero element is neither invertible nor a zero divisor. The invertible elements form a group. The zero divisors are the subject of the article on biquaternion zero divisors.

### The Algebra Is Not a Division Algebra

By definition, a **division algebra** is an algebra in which every nonzero element is invertible. For the finite-dimensional algebra $\mathbb{B}$, this is equivalent to containing no zero divisors: if every nonzero element is invertible, then no nonzero element can annihilate another; and conversely, if there are no zero divisors, then by the invertibility criterion above every nonzero element has an inverse.

The biquaternion algebra $\mathbb{B}$ contains zero divisors, so it is **not** a division algebra. This is in contrast to the Frobenius theorem, which states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$. The biquaternion algebra $\mathbb{B}$ is an eight-dimensional associative real algebra, but it is not a division algebra, because it contains zero divisors. The zero divisors are studied in the article on biquaternion zero divisors.

## Distribution of the Invertible Elements

We now examine how the invertible elements are distributed among the six distinguished subspaces of $\mathbb{B}$ defined in the basic algebra article. The criterion is the same in all cases: an element is invertible if and only if its biquaternion norm is nonzero.

### The Complex Subspace $\mathbb{C}_{\mathbb{B}}$

An element of $\mathbb{C}_{\mathbb{B}}$ has the form

$$
\tilde{Q} = Q_0 e_0, \qquad Q_0 \in \mathbb{C}.
$$

The biquaternion norm is

$$
N(\tilde{Q}) = Q_0^2.
$$

This vanishes if and only if $Q_0 = 0$, i.e. if and only if $\tilde{Q} = 0$. So every nonzero element of $\mathbb{C}_{\mathbb{B}}$ is invertible. This reflects the fact that $\mathbb{C}_{\mathbb{B}}$ is a copy of the field $\mathbb{C}$, in which every nonzero element has an inverse.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

An element of $\mathrm{Vect}(\mathbb{B})$ has vanishing scalar part, $\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_k = q_k + i q'_k$. The biquaternion norm is

$$
N(\tilde{Q}) = Q_1^2 + Q_2^2 + Q_3^2 = \left(q_1^2 + q_2^2 + q_3^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2\right) + 2i\left(q_1 q'_1 + q_2 q'_2 + q_3 q'_3\right).
$$

Its real part is an indefinite quadratic form of signature $(3,3)$ on the six-dimensional real space $\mathrm{Vect}(\mathbb{B})$, and its imaginary part is a second real quadratic form; the two vanish simultaneously exactly on the complex cone

$$
Q_1^2 + Q_2^2 + Q_3^2 = 0.
$$

This is the **nilpotent cone**: its nonzero elements square to zero, and they are the pure zero divisors studied in the companion article on biquaternion zero divisors. As a complex cone in $\mathbb{C}^3$ it has complex dimension $2$, that is, real dimension $4$; it therefore has real codimension $2$ in the six-dimensional space $\mathrm{Vect}(\mathbb{B})$. The elements outside the cone are invertible, and their set is **connected**, being the complement of a subset of codimension $2$.

In particular the intersection $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} = \operatorname{span}_{\mathbb{R}}\{e_1, e_2, e_3\}$ consists entirely of invertible elements away from the origin, since $N$ restricts to the positive-definite form $q_1^2 + q_2^2 + q_3^2$ there.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

An element of $\mathbb{H}_{\mathbb{B}}$ has the form

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R}.
$$

The biquaternion norm is

$$
N(\tilde{Q}) = q_0^2 + q_1^2 + q_2^2 + q_3^2.
$$

This is a sum of squares of real numbers, and it vanishes if and only if all $q_\mu = 0$, i.e. if and only if $\tilde{Q} = 0$. So every nonzero element of $\mathbb{H}_{\mathbb{B}}$ is invertible. This reflects the Frobenius theorem: $\mathbb{H}_{\mathbb{B}}$ is a copy of the division algebra $\mathbb{H}$, in which every nonzero element has an inverse.

### The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

An element of $i\mathbb{H}_{\mathbb{B}}$ is $i$ times a real quaternion, $\tilde{Q} = i\tilde{P}$ with $\tilde{P} = p_0 e_0 + p_1 e_1 + p_2 e_2 + p_3 e_3 \in \mathbb{H}_{\mathbb{B}}$. The biquaternion norm is

$$
N(i\tilde{P}) = \sum_{\mu=0}^{3} (i p_\mu)^2 = -\sum_{\mu=0}^{3} p_\mu^2 = -\left(p_0^2 + p_1^2 + p_2^2 + p_3^2\right).
$$

This is a **negative-definite** quadratic form on the four-dimensional real space $i\mathbb{H}_{\mathbb{B}}$, and it vanishes if and only if $\tilde{P} = 0$. So every nonzero element of $i\mathbb{H}_{\mathbb{B}}$ is invertible, and $i\mathbb{H}_{\mathbb{B}}$ contains no zero divisors. The subspace is not a subalgebra, so it is not itself a division algebra; but its nonzero elements are invertible in $\mathbb{B}$. Its signature is $(0,4)$, the exact negative of the $(4,0)$ of $\mathbb{H}_{\mathbb{B}}$, as the relation $N(i\tilde{Q}) = -N(\tilde{Q})$ requires.

### The Hermitian Subspace $\mathbb{M}_+$

An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_0 e_0 + i q'_1 e_1 + i q'_2 e_2 + i q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

The biquaternion norm is

$$
N(\tilde{Q}) = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2.
$$

This is an indefinite quadratic form of signature $(1, 3)$ on the four-dimensional real space $\mathbb{M}_+$. It vanishes on the **light cone**

$$
q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2,
$$

which is a double cone with apex at the origin. The nonzero elements of this cone are zero divisors. The elements of $\mathbb{M}_+$ **outside** the cone have $N(\tilde{Q}) \neq 0$ and are invertible.

The set of invertible elements of $\mathbb{M}_+$ is the complement of the light cone, which has three connected components:

- The **future region** $q_0 > 0$ and $q_0^2 > (q'_1)^2 + (q'_2)^2 + (q'_3)^2$, on which $N(\tilde{Q}) > 0$.
- The **past region** $q_0 < 0$ and $q_0^2 > (q'_1)^2 + (q'_2)^2 + (q'_3)^2$, on which $N(\tilde{Q}) > 0$.
- The **inside region** $q_0^2 < (q'_1)^2 + (q'_2)^2 + (q'_3)^2$, on which $N(\tilde{Q}) < 0$.

On all three components, the biquaternion norm is nonzero.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = i q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The biquaternion norm is

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2.
$$

This is an indefinite quadratic form of signature $(3, 1)$ on the four-dimensional real space $\mathbb{M}_-$. It vanishes on the **light cone**

$$
(q'_0)^2 = q_1^2 + q_2^2 + q_3^2,
$$

which is again a double cone with apex at the origin. The nonzero elements of this cone are zero divisors. The elements of $\mathbb{M}_-$ **outside** the cone have $N(\tilde{Q}) \neq 0$ and are invertible.

The set of invertible elements of $\mathbb{M}_-$ is the complement of the light cone, which has three connected components:

- The **spacelike region** $q_1^2 + q_2^2 + q_3^2 > (q'_0)^2$, on which $N(\tilde{Q}) > 0$.
- The **future timelike region** $q'_0 > 0$ and $(q'_0)^2 > q_1^2 + q_2^2 + q_3^2$, on which $N(\tilde{Q}) < 0$.
- The **past timelike region** $q'_0 < 0$ and $(q'_0)^2 > q_1^2 + q_2^2 + q_3^2$, on which $N(\tilde{Q}) < 0$.

On all three components, the biquaternion norm is nonzero.

### Summary of the Distribution

Of the six distinguished subspaces of $\mathbb{B}$:

- $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain **no** zero divisors: every nonzero element of each is invertible. The first two are subalgebras, and they are the division algebras among the six; $i\mathbb{H}_{\mathbb{B}}$ is an $\mathbb{H}_{\mathbb{B}}$-module and not a subalgebra, but its nonzero elements are invertible in $\mathbb{B}$.
- $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a light cone of zero divisors, and the invertible elements form the complement of the cone, with three connected components each.
- $\mathrm{Vect}(\mathbb{B})$ contains the nilpotent cone of zero divisors, and the invertible elements form a connected complement.

The two light cones in $\mathbb{M}_+$ and $\mathbb{M}_-$ have the same structure: each is defined by the vanishing of an indefinite quadratic form of signature $(1,3)$ or $(3,1)$, which has real codimension $1$ in the four-dimensional space, so the complement has three connected components. The cone in $\mathrm{Vect}(\mathbb{B})$ is different: the biquaternion norm is complex there, its vanishing imposes two real conditions, the cone has real codimension $2$ in the six-dimensional space, and the complement is connected.

## The Relation to the Hermitian Decomposition

The invertibility criterion is stated in terms of the biquaternion norm $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$. It is worth noting that the biquaternion norm is the complex analogue of the Hermitian form, and the two are related by the Hermitian decomposition

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-.
$$

Specifically:

- For $\tilde{Q} \in \mathbb{M}_+$, the biquaternion norm is real, and it is positive in the future and past regions (outside the light cone) and negative inside the light cone.
- For $\tilde{Q} \in \mathbb{M}_-$, the biquaternion norm is real, and it is positive in the spacelike region (outside the light cone) and negative in the timelike region (inside the light cone, which has two connected components).
- For a general $\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-$ with both components nonzero, the biquaternion norm need not be real, and the invertibility criterion is $N(\tilde{Q}) \neq 0$, which is a condition on both the real and imaginary parts of $N$.

The **scalar part** of the Hermitian form, by contrast, is always non-negative, and it is positive-definite on all of $\mathbb{B}$: it vanishes only at $\tilde{Q} = 0$. The full Hermitian form $\tilde{Q} \tilde{Q}^\dagger$ is a Hermitian biquaternion whose scalar part is this non-negative quantity; it does not detect the zero divisors, because its scalar part vanishes only at $\tilde{Q} = 0$.

## Summary

The biquaternion norm $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ is a complex-valued multiplicative quadratic form on the biquaternion algebra, the **semi-norm** of the literature. It is not positive-definite, and it vanishes on the zero divisors. Of the usual norm axioms only the sign axiom survives: the triangle inequality is inapplicable to a complex value, and the scaling axiom fails for complex scalars, since the square root of $\lambda^2$ lies in the right half-plane and not at $|\lambda|$. The absolute square root $r = \sqrt{|N(\tilde{Q})|}$ is, by contrast, the **unique** multiplicative real norm on the group of units normalised by $r(\lambda e_0) = |\lambda|$ for real $\lambda$. The Hermitian form $\tilde{Q} \tilde{Q}^\dagger$ is a Hermitian biquaternion whose scalar part is the non-negative quantity $\sum_\mu |Q_\mu|^2$; this scalar part defines the Euclidean norm on the underlying real vector space $\mathbb{B} \cong \mathbb{R}^8$. The full Hermitian form is not scalar-valued in general; its vector part vanishes precisely when $\tilde{Q}$ is a complex scalar multiple of a real quaternion, i.e. when $\tilde{Q} = (\alpha + i\beta) A$ with $\alpha, \beta \in \mathbb{R}$ and $A \in \mathbb{H}_{\mathbb{B}}$.

The invertibility criterion is: $\tilde{Q}$ is invertible if and only if $N(\tilde{Q}) \neq 0$. The inverse is $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$. The group of units $\mathbb{B}^\times$ is an open, connected subset of $\mathbb{B}$, and is a topological group of real dimension $8$ with center $\mathbb{C}^\times$; its topology is in *The Biquaternion Unit Group as a Topological Group* and its Lie structure in *Biquaternion Lie Group and Exponential Structure*.

The algebra $\mathbb{B}$ is partitioned into three classes: the zero element, the invertible elements, and the zero divisors. Of the six distinguished subspaces, $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain no zero divisors at all; $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a light cone of zero divisors, the invertible elements in each forming a complement of the cone with three connected components; and $\mathrm{Vect}(\mathbb{B})$ contains the nilpotent cone, whose complement is connected.

The zero divisors themselves are studied in the article on biquaternion zero divisors, and the classification of the roots of $-1$ that underlies the idempotent classification is studied in the article on biquaternion roots of minus one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient |
| $\bar{\tilde{Q}}$ | Quaternion conjugate |
| $\tilde{Q}^*$ | Complex conjugate |
| $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ | Anti-Hermitian conjugate |
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Biquaternion norm; the semi-norm of the literature |
| $r(\tilde{Q}) = \sqrt{|N(\tilde{Q})|}$ | The unique multiplicative real norm on the units |
| $\tilde{Q} \tilde{Q}^\dagger$ | Hermitian form (a Hermitian biquaternion); defined in *Biquaternion Algebra* |
| $\mathrm{Sc}(\tilde{Q} \tilde{Q}^\dagger) = \sum_\mu |Q_\mu|^2$ | Scalar part of the Hermitian form |
| $\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}(\tilde{Q} \tilde{Q}^\dagger)}$ | Euclidean norm |
| $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ | Inverse |
| $\mathbb{B}^\times$ | Group of units |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions and the zero divisors.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the semi-norm and its axioms, the unique real norm, and the Hermitian form.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the unique multiplicative real norm of the algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.

