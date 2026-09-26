# __Biquaternion Norm and Invertibility__

## Introduction

This article studies the norm form of the biquaternion algebra and the invertibility of its elements. It follows the basic algebra article, which defined the algebra, its conjugations, and its six distinguished subspaces. The goal here is to define the norm form and the Hermitian form, to establish the criterion for invertibility, and to describe the group of units.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations and its six distinguished subspaces.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\bar{\tilde{Q}}$, the complex conjugate is denoted $\tilde{Q}^*$, the Hermitian conjugate is denoted $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is denoted $\tilde{Q}^\flat = -\tilde{Q}^\dagger$.

## The Norm Form

### Definition

The **norm form** of a biquaternion $\tilde{Q}$ is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2,
$$

where $\bar{\tilde{Q}}$ is the quaternion conjugate.

**Basic properties.**

- $N(\tilde{Q})$ is a complex scalar (a complex multiple of $e_0$) in general. It is real on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and on the imaginary translate $i \mathbb{H}_{\mathbb{B}}$; outside their union it need not be real.
- $N(\tilde{Q})$ is not positive-definite: it can vanish for a nonzero biquaternion. The nonzero elements with vanishing norm form are the zero divisors, studied in the article on biquaternion zero divisors.
- $N(\tilde{Q})$ is invariant under quaternion conjugation: $N(\bar{\tilde{Q}}) = N(\tilde{Q})$.
- $N(\tilde{Q})$ is complex-conjugated under complex conjugation: $N(\tilde{Q}^*) = N(\tilde{Q})^*$.
- $N(\tilde{Q})$ is complex-conjugated under Hermitian conjugation: $N(\tilde{Q}^\dagger) = N(\bar{\tilde{Q}}^*) = N(\tilde{Q})^*$.

### Multiplicativity

**Theorem.** The norm form is multiplicative:

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

$\square$

**Corollary.** If $N(\tilde{Q}) \neq 0$ and $N(\tilde{R}) \neq 0$, then $N(\tilde{Q} \circ \tilde{R}) \neq 0$.

**Corollary.** If $N(\tilde{Q}) = 0$ or $N(\tilde{R}) = 0$, then $N(\tilde{Q} \circ \tilde{R}) = 0$. In particular, the product of a zero divisor with any biquaternion is either zero or a zero divisor.

### The Norm Form as a Semi-Norm

The norm form of this article is the **semi-norm** of the biquaternion literature (Ward; Sangwine, Ell and Le Bihan). The name records two departures from a norm: the value is complex rather than real, and a non-zero element can have vanishing value, the vanishing locus being exactly the zero divisors. It is worth recording which of the usual norm axioms survive, because the article uses the symbol $N$ and the multiplicativity theorem speaks of a norm; the audit, following Sangwine, Ell and Le Bihan, is as follows.

- The sign axiom holds: $N(-\tilde{Q}) = N(\tilde{Q})$, because negating a complex number does not change its square and therefore does not change $\sum_\mu Q_\mu^2$.
- The triangle inequality has no content here: $\mathbb{C}$ carries no order, so there is no inequality to prove or to refute.
- The scaling axiom is **false**, in both the form usually written and the form the complex modulus suggests. For the norm form the homogeneity is quadratic, $N(\lambda\tilde{Q}) = \lambda^2N(\tilde{Q})$. For its square root, the complex modulus $\sqrt{N}$, one gets $\sqrt{N(\lambda\tilde{Q})} = \sqrt{\lambda^2}\,\sqrt{N(\tilde{Q})}$, and the principal square root $\sqrt{\lambda^2}$ lies in the right half-plane and not at $|\lambda|$: with $\lambda = i$ and $\tilde{Q} = e_0$, $\sqrt{N(\lambda\tilde{Q})} = \sqrt{-1} = i$ while $|\lambda|\sqrt{N(\tilde{Q})} = 1$. For real $\lambda$ the axiom is satisfied, $\sqrt{\lambda^2} = |\lambda|$, and it is precisely the complex case that the algebra is about.

So the norm form is a complex-valued multiplicative semi-norm: multiplicative, homogeneous of degree two over the complex scalars, indefinite, and vanishing exactly on the zero divisors. A reader who applies the scaling axiom with a complex scalar will be off by a factor lying in the right half-plane.

### The Unique Real Norm, and the Polar Scale

The positive statement about size is sharper than the audit, and Sangwine, Ell and Le Bihan quote it from Gürlebeck and Sprössig: there is a **unique** real norm that is multiplicative and normalised on the real scalars. In the notation of this article, let $\rho$ be a continuous multiplicative function from the group of units of $\mathbb{B}$ to the non-negative reals, normalised by

$$
\rho(\lambda e_0) = |\lambda| \qquad\text{for } \lambda \in \mathbb{R}.
$$

Then $\rho$ is uniquely determined, and it is

$$
r(\tilde{Q}) = \sqrt{|N(\tilde{Q})|} = \sqrt{|\det\Phi(\tilde{Q})|},
$$

where $\Phi$ is the $2\times2$ matrix realisation.

**Proof in one paragraph.** The group of units of $\mathbb{B}$ is $\mathrm{GL}_2(\mathbb{C})$ under $\Phi$. A continuous homomorphism from $\mathrm{GL}_2(\mathbb{C})$ to the multiplicative group $\mathbb{R}_{>0}$ is constant on the commutator subgroup; that subgroup is $\mathrm{SL}_2(\mathbb{C})$, which is perfect, so such a homomorphism factors through the determinant, $\mathrm{GL}_2(\mathbb{C}) \to \mathbb{C}^\times$. A continuous homomorphism $\mathbb{C}^\times \to \mathbb{R}_{>0}$ is $z \mapsto |z|^t$: on the positive reals it is a power, and the unit circle is compact and connected, so its image is trivial. Hence $\rho(\tilde{Q}) = |\det\Phi(\tilde{Q})|^t$ for some real $t$, and the normalisation $\rho(\lambda e_0) = |\det(\lambda I_2)|^t = |\lambda|^{2t} = |\lambda|$ forces $t = \tfrac12$. That value is $r$, since $|\det\Phi(\tilde{Q})| = |N(\tilde{Q})|$. $\square$

The function $r$ was verified to be multiplicative on random pairs, $r(\tilde{P}\tilde{Q}) = r(\tilde{P})r(\tilde{Q})$, and to satisfy $r(\tilde{Q})^2 = |\det\Phi(\tilde{Q})|$; it is defined by those two properties, vanishes on the zero divisors, and is therefore a semi-norm on $\mathbb{B}$ while remaining a genuine norm on the units. The corpus uses $r$ as the real factor of the polar representations, so the polar scale is not one convention among several: it is the only real size function compatible with multiplicativity and with $\rho(e_0) = 1$. The matrix face $\sqrt{|\det\Phi(\tilde{Q})|}$ also shows the statement in the realisation the physics articles use.

### The Norm Form from the Halves

Writing a biquaternion as $\tilde{Q} = q_r + iq_i$ with $q_r$ and $q_i$ real quaternions, the norm form splits as

$$
\Re N(\tilde{Q}) = N(q_r) - N(q_i), \qquad \Im N(\tilde{Q}) = 2\,\langle q_r, q_i\rangle,
$$

where $\langle q_r, q_i\rangle = \sum_\mu (q_r)_\mu (q_i)_\mu$ is the scalar product of the two real quaternions. The real part is a difference of two norms and the imaginary part is twice a scalar product, so the special cases of the norm form are read directly:

- $q_r \perp q_i$: the norm form is real, and it is negative whenever $N(q_i) > N(q_r)$.
- $N(q_r) = N(q_i)$: the norm form is purely imaginary.
- $q_r = 0$ (an imaginary biquaternion): the norm form is negative real, $-N(q_i)$, so its square root is imaginary.
- $q_r \perp q_i$ and $N(q_r) = N(q_i)$: the norm form vanishes. These are exactly the zero divisors, so the criterion $N(\tilde{Q}) = 0$ of the article on biquaternion zero divisors is the statement that the two halves have equal norms and vanishing scalar product; that article splits the same set into the pure and non-pure families by the vanishing of the scalar part.

## The Hermitian Form

### Definition

The **Hermitian form** of a biquaternion $\tilde{Q}$ is the biquaternion

$$
\tilde{Q} \tilde{Q}^\dagger,
$$

where $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$ is the Hermitian conjugate.

**Basic properties.**

- $\tilde{Q} \tilde{Q}^\dagger$ is a **biquaternion**, not a real scalar in general. Its **scalar part** is

$$
\mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^\dagger\right) = \sum_{\mu=0}^{3} |Q_\mu|^2 = \sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu),
$$

with $Q_\mu = q_\mu + i q'_\mu$. This scalar part is non-negative and vanishes if and only if $\tilde{Q} = 0$. The vector part of $\tilde{Q} \tilde{Q}^\dagger$ does not in general vanish: for example, for $\tilde{Q} = e_0 + ie_1$, one has $\tilde{Q}^\dagger = e_0 + ie_1$ and

$$
\tilde{Q} \tilde{Q}^\dagger = (e_0 + ie_1)^2 = 2e_0 + 2ie_1,
$$

which has a nonzero vector part $2ie_1$.

- The Hermitian form is **not** multiplicative with respect to the biquaternion product, and its scalar part does not in general equal the norm form $N(\tilde{Q}) = \sum_\mu Q_\mu^2$.
- The Hermitian form is **Hermitian** in the sense that $(\tilde{Q} \tilde{Q}^\dagger)^\dagger = \tilde{Q} \tilde{Q}^\dagger$: the Hermitian form of any biquaternion is a Hermitian element of $\mathbb{B}$.

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

The trace is the **Frobenius norm squared** of the matrix representing $\tilde{Q}$ under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$.

### Relation Between the Norm Form and the Hermitian Form

The two forms are related as follows:

- The **norm form** $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ is a complex scalar (a multiple of $e_0$), multiplicative, and can vanish for nonzero $\tilde{Q}$.
- The **Hermitian form** $\tilde{Q} \tilde{Q}^\dagger$ is a Hermitian biquaternion whose scalar part is $\sum_\mu |Q_\mu|^2$ (non-negative, vanishing only at $\tilde{Q} = 0$) and whose vector part need not vanish. It is not multiplicative.

They coincide as biquaternions if and only if $\tilde{Q}$ lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, i.e. if and only if all the coefficients $Q_\mu$ are real. On the imaginary translate $i \mathbb{H}_{\mathbb{B}}$, the Hermitian form is also scalar-valued, but it equals $+\sum_\mu q'^2_\mu \cdot e_0$, which is the negative of the norm form; on that subspace the two forms differ by a sign.

The two forms play different roles:

- The **norm form** controls the multiplicative structure: it determines invertibility, zero divisors, and the multiplicativity of the norm.
- The **scalar part of the Hermitian form** (equivalently, the diagonal value of the inner product $\langle \tilde{Q}, \tilde{Q}\rangle$) controls the topological structure: it defines the Euclidean norm, the topology of $\mathbb{B}$, and the completeness of the underlying real vector space.

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

**Theorem.** A biquaternion $\tilde{Q}$ is invertible if and only if its norm form is nonzero:

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

Conversely, suppose $\tilde{Q}$ is invertible. Applying the norm form to $\tilde{Q} \circ \tilde{Q}^{-1} = e_0$ and using multiplicativity gives

$$
N(\tilde{Q}) N(\tilde{Q}^{-1}) = N(e_0) = 1,
$$

so $N(\tilde{Q}) \neq 0$. $\square$

### The Inverse Formula

When $N(\tilde{Q}) \neq 0$, the inverse is

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})}.
$$

This is the biquaternionic analogue of the formula $q^{-1} = \bar{q}/|q|^2$ for quaternions.

**Proof.** The verification is the computation in the first part of the proof of the criterion. $\square$

**Corollary.** If $\tilde{Q}$ is invertible, then so is $\bar{\tilde{Q}}$, and $(\bar{\tilde{Q}})^{-1} = \overline{\tilde{Q}^{-1}}$.

## The Group of Units

### Definition

The **group of units** of $\mathbb{B}$ is the set of invertible elements:

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\}.
$$

It is a group under multiplication, with identity $e_0$.

### Basic Properties

**Openness.** The group of units is an open subset of $\mathbb{B}$ in the Euclidean topology. Indeed, the norm form $N : \mathbb{B} \to \mathbb{C}$ is a continuous map, and $\mathbb{B}^\times = N^{-1}(\mathbb{C} \setminus \{0\})$ is the preimage of an open set.

**Non-compactness.** The group of units is not compact, because it contains the real line $\{a e_0 : a \in \mathbb{R}, a \neq 0\}$, which is unbounded.

**Connected components.** The group of units is **connected**. To see this, use the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ of the basic algebra article. Under this isomorphism, $\mathbb{B}^\times$ corresponds to the group $GL(2, \mathbb{C})$ of invertible $2 \times 2$ complex matrices. The group $GL(n, \mathbb{C})$ is connected for every $n \geq 1$: every invertible complex matrix can be continuously deformed to the identity, for instance via the Gram–Schmidt process, which gives a continuous retraction of $GL(n, \mathbb{C})$ onto the unitary group $U(n)$, and $U(n)$ is connected. Hence $\mathbb{B}^\times \cong GL(2, \mathbb{C})$ is connected.

**Lie group structure.** The group of units is a Lie group of real dimension $8$ over $\mathbb{R}$. Under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$, it corresponds to $GL(2, \mathbb{C})$, which is a complex Lie group of complex dimension $4$, hence a real Lie group of real dimension $8$. Its Lie algebra is $\mathbb{B}$ itself (as a real vector space), with the commutator bracket

$$
[\tilde{P}, \tilde{Q}] = \tilde{P} \tilde{Q} - \tilde{Q} \tilde{P}.
$$

**Center.** The center of $\mathbb{B}^\times$ is $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$, the group of nonzero complex scalars. This follows from the fact that the center of $\mathbb{B}$ is $\mathbb{C}$.

### The Inverse Map

The **inverse map**

$$
\iota : \mathbb{B}^\times \to \mathbb{B}^\times, \qquad \iota(\tilde{Q}) = \tilde{Q}^{-1},
$$

is a smooth involution. Its differential at the identity is $-\mathrm{id}_\mathbb{B}$, which is the reason the Lie algebra bracket is antisymmetric.

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

We now examine how the invertible elements are distributed among the six distinguished subspaces of $\mathbb{B}$ defined in the basic algebra article. The criterion is the same in all cases: an element is invertible if and only if its norm form is nonzero.

### The Complex Subspace $\mathbb{C}_{\mathbb{B}}$

An element of $\mathbb{C}_{\mathbb{B}}$ has the form

$$
\tilde{Q} = Q_0 e_0, \qquad Q_0 \in \mathbb{C}.
$$

The norm form is

$$
N(\tilde{Q}) = Q_0^2.
$$

This vanishes if and only if $Q_0 = 0$, i.e. if and only if $\tilde{Q} = 0$. So every nonzero element of $\mathbb{C}_{\mathbb{B}}$ is invertible. This reflects the fact that $\mathbb{C}_{\mathbb{B}}$ is a copy of the field $\mathbb{C}$, in which every nonzero element has an inverse.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

An element of $\mathrm{Vect}(\mathbb{B})$ has vanishing scalar part, $\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_k = q_k + i q'_k$. The norm form is

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

The norm form is

$$
N(\tilde{Q}) = q_0^2 + q_1^2 + q_2^2 + q_3^2.
$$

This is a sum of squares of real numbers, and it vanishes if and only if all $q_\mu = 0$, i.e. if and only if $\tilde{Q} = 0$. So every nonzero element of $\mathbb{H}_{\mathbb{B}}$ is invertible. This reflects the Frobenius theorem: $\mathbb{H}_{\mathbb{B}}$ is a copy of the division algebra $\mathbb{H}$, in which every nonzero element has an inverse.

### The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

An element of $i\mathbb{H}_{\mathbb{B}}$ is $i$ times a real quaternion, $\tilde{Q} = i\tilde{P}$ with $\tilde{P} = p_0 e_0 + p_1 e_1 + p_2 e_2 + p_3 e_3 \in \mathbb{H}_{\mathbb{B}}$. The norm form is

$$
N(i\tilde{P}) = \sum_{\mu=0}^{3} (i p_\mu)^2 = -\sum_{\mu=0}^{3} p_\mu^2 = -\left(p_0^2 + p_1^2 + p_2^2 + p_3^2\right).
$$

This is a **negative-definite** quadratic form on the four-dimensional real space $i\mathbb{H}_{\mathbb{B}}$, and it vanishes if and only if $\tilde{P} = 0$. So every nonzero element of $i\mathbb{H}_{\mathbb{B}}$ is invertible, and $i\mathbb{H}_{\mathbb{B}}$ contains no zero divisors. The subspace is not a subalgebra, so it is not itself a division algebra; but its nonzero elements are invertible in $\mathbb{B}$. Its signature is $(0,4)$, the exact negative of the $(4,0)$ of $\mathbb{H}_{\mathbb{B}}$, as the relation $N(i\tilde{Q}) = -N(\tilde{Q})$ requires.

### The Hermitian Subspace $\mathbb{M}_+$

An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_0 e_0 + i q'_1 e_1 + i q'_2 e_2 + i q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

The norm form is

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

On all three components, the norm form is nonzero.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = i q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The norm form is

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

On all three components, the norm form is nonzero.

### Summary of the Distribution

Of the six distinguished subspaces of $\mathbb{B}$:

- $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain **no** zero divisors: every nonzero element of each is invertible. The first two are subalgebras, and they are the division algebras among the six; $i\mathbb{H}_{\mathbb{B}}$ is an $\mathbb{H}_{\mathbb{B}}$-module and not a subalgebra, but its nonzero elements are invertible in $\mathbb{B}$.
- $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a light cone of zero divisors, and the invertible elements form the complement of the cone, with three connected components each.
- $\mathrm{Vect}(\mathbb{B})$ contains the nilpotent cone of zero divisors, and the invertible elements form a connected complement.

The two light cones in $\mathbb{M}_+$ and $\mathbb{M}_-$ have the same structure: each is defined by the vanishing of an indefinite quadratic form of signature $(1,3)$ or $(3,1)$, which has real codimension $1$ in the four-dimensional space, so the complement has three connected components. The cone in $\mathrm{Vect}(\mathbb{B})$ is different: the norm form is complex there, its vanishing imposes two real conditions, the cone has real codimension $2$ in the six-dimensional space, and the complement is connected.

## The Relation to the Hermitian Decomposition

The invertibility criterion is stated in terms of the norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$. It is worth noting that the norm form is the complex analogue of the Hermitian form, and the two are related by the Hermitian decomposition

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-.
$$

Specifically:

- For $\tilde{Q} \in \mathbb{M}_+$, the norm form is real, and it is positive in the future and past regions (outside the light cone) and negative inside the light cone.
- For $\tilde{Q} \in \mathbb{M}_-$, the norm form is real, and it is positive in the spacelike region (outside the light cone) and negative in the timelike region (inside the light cone, which has two connected components).
- For a general $\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-$ with both components nonzero, the norm form need not be real, and the invertibility criterion is $N(\tilde{Q}) \neq 0$, which is a condition on both the real and imaginary parts of $N$.

The **scalar part** of the Hermitian form, by contrast, is always non-negative, and it is positive-definite on all of $\mathbb{B}$: it vanishes only at $\tilde{Q} = 0$. The full Hermitian form $\tilde{Q} \tilde{Q}^\dagger$ is a Hermitian biquaternion whose scalar part is this non-negative quantity; it does not detect the zero divisors, because its scalar part vanishes only at $\tilde{Q} = 0$.

## Summary

The norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ is a complex-valued multiplicative quadratic form on the biquaternion algebra, the **semi-norm** of the literature. It is not positive-definite, and it vanishes on the zero divisors. Of the usual norm axioms only the sign axiom survives: the triangle inequality is inapplicable to a complex value, and the scaling axiom fails for complex scalars, since the square root of $\lambda^2$ lies in the right half-plane and not at $|\lambda|$. The absolute square root $r = \sqrt{|N(\tilde{Q})|} = \sqrt{|\det\Phi(\tilde{Q})|}$ is, by contrast, the **unique** multiplicative real norm on the group of units normalised by $r(\lambda e_0) = |\lambda|$ for real $\lambda$, and it is the real scale the polar representations use. The Hermitian form $\tilde{Q} \tilde{Q}^\dagger$ is a Hermitian biquaternion whose scalar part is the non-negative quantity $\sum_\mu |Q_\mu|^2$; this scalar part defines the Euclidean norm on the underlying real vector space $\mathbb{B} \cong \mathbb{R}^8$. The full Hermitian form is not scalar-valued in general; its vector part vanishes precisely when $\tilde{Q}$ is a complex scalar multiple of a real quaternion, i.e. when $\tilde{Q} = (\alpha + i\beta) A$ with $\alpha, \beta \in \mathbb{R}$ and $A \in \mathbb{H}_{\mathbb{B}}$.

The invertibility criterion is: $\tilde{Q}$ is invertible if and only if $N(\tilde{Q}) \neq 0$. The inverse is $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$. The group of units $\mathbb{B}^\times$ is an open, connected subset of $\mathbb{B}$, isomorphic to $GL(2, \mathbb{C})$, and is a Lie group of real dimension $8$, with Lie algebra $\mathbb{B}$ and center $\mathbb{C}^\times$.

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
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form; the semi-norm of the literature |
| $r(\tilde{Q}) = \sqrt{|N(\tilde{Q})|} = \sqrt{|\det\Phi(\tilde{Q})|}$ | The unique multiplicative real norm on the units |
| $\tilde{Q} \tilde{Q}^\dagger$ | Hermitian form (a Hermitian biquaternion) |
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

