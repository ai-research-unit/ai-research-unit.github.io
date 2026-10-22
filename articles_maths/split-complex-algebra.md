
# __Split-Complex Algebra__

## Introduction

This article introduces the split complex algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real subspaces that arise from the conjugations: the real and split imaginary lines, and the two idempotent lines.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The idempotent decomposition is defined algebraically.

The split complex algebra is the two-dimensional real algebra $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, written in a generator $j$ with $j^2 = +1$. It is the indefinite member of the two-dimensional pair whose definite member is the field $\mathbb{C}$ of complex numbers; the two share their basis, their conjugation and their dimension and differ in the sign of the square of the imaginary unit. The complex numbers are assumed from *Complex Algebra*, together with their basis, their multiplication and their conjugation, and no facts about them are restated here except where the comparison is the point.

## The Split Complex Algebra

### Definition

The **split complex algebra** is the two-dimensional real algebra with basis

$$
1, \qquad j,
$$

and multiplication rules

$$
j^2 = +1.
$$

A general split complex number is written in developed form as

$$
Q = q + j q', \qquad q, q' \in \mathbb{R},
$$

in the basis $\{1, j\}$. The real number $q$ is the **real part** and the real number $q'$ is the **imaginary part**:

$$
q = \operatorname{Re} Q, \qquad q' = \operatorname{Im} Q.
$$

The notation $j$ is chosen deliberately. In the complex algebra the imaginary unit satisfies $i^2 = -1$. In the split complex algebra the unit satisfies $j^2 = +1$. Writing $j$ rather than $i$ makes the sign explicit and avoids confusion with the complex case; this is the notation used throughout the category.

### The Real Algebra View

The split complex algebra has a single ground field. It is a **two-dimensional algebra over $\mathbb{R}$**: its basis is $\{1, j\}$, every element is a real linear combination of the two basis elements, and the multiplication is $\mathbb{R}$-bilinear. The centre is all of $\mathbb{D}$, because the algebra is commutative.

There is no second ground field to pass to, and no scalar imaginary inside the algebra. This is the first of the systematic differences from the four-dimensional members of the family, and it is the reason the subspace lattice below collapses.

### Developed Form

Equivalently, $\mathbb{D}$ is the quotient ring

$$
\mathbb{D} = \mathbb{R}[x]/(x^2-1),
$$

the image of the generator $x$ being $j$. Since $x^2 - 1 = (x-1)(x+1)$ is not prime, the quotient is not a field but a product of two copies of $\mathbb{R}$; that product is exhibited explicitly in *The Isomorphism with $\mathbb{R}\oplus\mathbb{R}$* below.

### The Algebra Structure

The algebra $\mathbb{D}$ is a two-dimensional commutative, associative and unital algebra over $\mathbb{R}$, with unit $1$. As a ring it is a commutative ring with zero divisors. It is **not** a division algebra: the elements $1+j$ and $1-j$ are non-zero, but

$$
(1+j)(1-j) = 1 - j^2 = 0.
$$

So $\mathbb{D}$ is not a field, and not a division algebra. This is the fundamental difference from $\mathbb{C}$, and it is the source of everything that distinguishes the two theories.

**Frobenius theorem.** The finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. The split complex algebra is a commutative associative real algebra of dimension two that is not a division algebra, so it lies outside that list; it is not one of the three.

### Multiplication

The product of two split complex numbers is defined by extending the real multiplication bilinearly:

$$
Q B = (q + j q')(b + j b') = (q b + q' b') + (q b' + q' b) j, \qquad Q = q + j q', \quad B = b + j b'.
$$

In developed form,

$$
Q B = \sum_{\mu=0}^{1} \sum_{\nu=0}^{1} Q_\mu B_\nu \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the split complex algebra. The multiplication is commutative and associative, and $1$ is the two-sided unit.

### Conjugations

There are **two** conjugations on $\mathbb{D}$, and they turn out to coincide.

**Split complex conjugation** $\bar{Q}$:

$$
\bar{Q} = q - j q'.
$$

It is the extension of the identity on $\mathbb{R}$ that sends $j$ to $-j$, it is $\mathbb{R}$-linear, and it is an algebra involution: $\overline{Q B} = \bar{Q}\,\bar{B}$ and $\overline{\bar{Q}} = Q$.

**Idempotent conjugation** (the swap):

$$
\tilde{Q} = (q - q') \Pi_+ + (q + q') \Pi_-.
$$

In the basis $\{1, j\}$ the idempotent conjugation is

$$
\tilde{Q} = q - j q' = \bar{Q}.
$$

So in the split complex algebra the split complex conjugation and the idempotent conjugation coincide. The coincidence is a special feature of the two-dimensional case: the conjugation induced on $\mathbb{D}$ by the idempotent basis is the same map as the conjugation of the algebra, because the single non-trivial involution has only one non-trivial choice to make.

Each conjugation is an involution: applying it twice returns the original split complex number. Each therefore splits $\mathbb{D}$ into a fixed space and an anti-fixed space, and each of the two is a real vector subspace of $\mathbb{D}$; those subspaces are described in the following sections.

### The Group of Conjugations

The split complex conjugation $\bar{\cdot}$ is an involution distinct from the identity, so the conjugation group is

$$
\{\mathrm{id}, \bar{\cdot}\} \cong \mathbb{Z}/2.
$$

There is no second independent involution, hence no Klein four-group and no Hermitian or anti-Hermitian conjugation. There is one non-trivial involution, and it contributes the pair of lines below. The idempotent conjugation does not enlarge the group, since it is the same map.

## The Distinguished Subspaces

The single non-trivial involution $\bar{\cdot}$ splits $\mathbb{D}$ into its fixed space and its anti-fixed space, two real vector subspaces of dimension $1$. The idempotent basis, developed below, cuts the algebra into its two primitive lines; it is the finest decomposition of $\mathbb{D}$, and it names the two null directions in place of the two coordinate axes.

### The Real Subspace

The fixed points of split complex conjugation are the split complex numbers satisfying $\bar{Q} = Q$. In developed form,

$$
q - j q' = q + j q'.
$$

Comparing the coefficients of $1$ and $j$:

- coefficient of $1$: $q = q$, always satisfied;
- coefficient of $j$: $-q' = q'$, so $q' = 0$.

The fixed points are split complex numbers with vanishing imaginary part:

$$
Q = q, \qquad q \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{D}}$, a copy of the real line embedded in $\mathbb{D}$ as the real axis. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{D}$ isomorphic to $\mathbb{R}$, and as a ring it is a field. The form it carries is treated in *Norm and Invertibility in the General Split-Complex Algebra*.

### The Split Imaginary Subspace

The anti-fixed points of split complex conjugation are the split complex numbers satisfying $\bar{Q} = -Q$, which forces $q = 0$:

$$
Q = j q', \qquad q' \in \mathbb{R}.
$$

This is the **split imaginary subspace** $j\mathbb{R}_{\mathbb{D}}$, a real vector space of dimension $1$. It is not a subalgebra: $(j q')^2 = q'^2 \in \mathbb{R}_{\mathbb{D}}$, which is not in $j\mathbb{R}_{\mathbb{D}}$ unless $q' = 0$. The form it carries is treated in *Norm and Invertibility in the General Split-Complex Algebra*.

There is only one non-trivial fixed-point set and one non-trivial anti-fixed-point set, because there is only one non-trivial involution. The involution lattice of $\mathbb{D}$ is the single edge $\{0\}\subset\mathbb{Z}/2$ drawn on the two lines.

### The Idempotent Basis

Define the **idempotents**

$$
\Pi_+ = \frac{1 + j}{2}, \qquad \Pi_- = \frac{1 - j}{2}.
$$

They satisfy

$$
\Pi_+^2 = \Pi_+, \qquad \Pi_-^2 = \Pi_-, \qquad \Pi_+ \Pi_- = \Pi_- \Pi_+ = 0, \qquad \Pi_+ + \Pi_- = 1.
$$

A general split complex number is written uniquely in the idempotent basis as

$$
Q = q + j q' = (q + q') \Pi_+ + (q - q') \Pi_-.
$$

This is the **idempotent decomposition** of $Q$. It is the single most important structural fact about the split complex algebra, and the two lines $\mathbb{R}\Pi_+$ and $\mathbb{R}\Pi_-$ are the finest direct summands of the algebra.

### The Isomorphism with $\mathbb{R} \oplus \mathbb{R}$

The map

$$
\varphi : \mathbb{D} \to \mathbb{R} \oplus \mathbb{R}, \qquad \varphi(q + j q') = (q + q', q - q'),
$$

is an algebra isomorphism. It is bijective, and it satisfies

$$
\varphi(Q + B) = \varphi(Q) + \varphi(B), \qquad \varphi(Q B) = \varphi(Q) \varphi(B),
$$

where the multiplication on $\mathbb{R} \oplus \mathbb{R}$ is componentwise:

$$
(u_1, u_2)(v_1, v_2) = (u_1 v_1, u_2 v_2).
$$

So $\mathbb{D}$ is not a new algebra. It is $\mathbb{R} \oplus \mathbb{R}$ in disguise. Everything that can be said about $\mathbb{D}$ is a statement about pairs of real numbers, and everything that is surprising about $\mathbb{D}$ is a consequence of the fact that the disguise hides the zero divisors: the pairs with one coordinate zero are exactly the zero divisors.

## The Split Complex Decomposition

The real subspace $\mathbb{R}_{\mathbb{D}}$ and the split imaginary subspace $j\mathbb{R}_{\mathbb{D}}$ are the two eigenspaces of split complex conjugation. Every split complex number decomposes uniquely as the sum of a real part and an imaginary part:

$$
Q = Q_r + j Q_i, \qquad Q_r = q, \quad Q_i = q'.
$$

The two components are obtained from the split complex conjugation:

$$
Q_r = \frac{1}{2}(Q + \bar{Q}), \qquad Q_i = \frac{1}{2j}(Q - \bar{Q}) = q'.
$$

Indeed, $Q_r$ is fixed by split complex conjugation, so it lies in $\mathbb{R}_{\mathbb{D}}$, and $Q_i = q'$ is real, so $j Q_i$ lies in $j \mathbb{R}_{\mathbb{D}}$. The sum is $Q_r + j Q_i = Q$.

This gives the direct sum decomposition

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j \mathbb{R}_{\mathbb{D}},
$$

where $j \mathbb{R}_{\mathbb{D}}$ is the set of split complex numbers of the form $j q'$ with $q' \in \mathbb{R}$. Both are real vector spaces of dimension $1$, and their direct sum is the full algebra $\mathbb{D}$ of real dimension $2$.

This is the **split complex decomposition** of a split complex number. It expresses $Q$ as a real number plus $j$ times another real number. The two summands are the two eigenspaces of the unique non-trivial involution.

## The Idempotent Decomposition

The idempotent decomposition is the second natural decomposition of $\mathbb{D}$, and it is not the eigenspace decomposition of an involution:

$$
Q = Q_+ \Pi_+ + Q_- \Pi_-, \qquad Q_+ = q + q', \quad Q_- = q - q'.
$$

The two components are obtained from the idempotents:

$$
Q_+ = Q \Pi_+, \qquad Q_- = Q \Pi_-,
$$

which, since $\mathbb{D}$ is commutative, is unambiguous.

This gives the direct sum decomposition

$$
\mathbb{D} = \mathbb{D} \Pi_+ \oplus \mathbb{D} \Pi_-,
$$

where $\mathbb{D} \Pi_+$ and $\mathbb{D} \Pi_-$ are the two ideals of $\mathbb{D}$, each isomorphic to $\mathbb{R}$. Both are real vector spaces of dimension $1$, and their direct sum is the full algebra $\mathbb{D}$ of real dimension $2$.

The idempotent decomposition and the split complex decomposition are related by

$$
Q_+ = Q_r + Q_i, \qquad Q_- = Q_r - Q_i.
$$

So the idempotent components are the sum and difference of the real and imaginary parts.

## Zero Divisors

**Definition.** An element $Q \in \mathbb{D}$ is a **zero divisor** if $Q \neq 0$ and there exists $B \in \mathbb{D}$ with $B \neq 0$ and $QB = 0$; the **annihilator** of $Q$ is the ideal

$$
\operatorname{ann}(Q) = \{B \in \mathbb{D} : QB = 0\}.
$$

The algebra has zero divisors already among its primitive elements:

$$
(1+j)(1-j) = 1 - j^2 = 0,
$$

so $1+j$ and $1-j$ are non-zero elements with zero product, and $\mathbb{D}$ is not a domain.

**Proposition.** Write $Q = Q_+\Pi_+ + Q_-\Pi_-$ in the idempotent basis, with $Q$ not both coordinates zero. Then $Q$ is a zero divisor if and only if one of $Q_+, Q_-$ vanishes; if both are nonzero then $Q$ is a unit, with inverse

$$
Q^{-1} = Q_+^{-1}\Pi_+ + Q_-^{-1}\Pi_-.
$$

**Proof.** In the idempotent basis multiplication is componentwise, $QB = Q_+B_+\Pi_+ + Q_-B_-\Pi_-$. If $Q_+ = 0$ then $Q\Pi_+ = Q_-\Pi_-\Pi_+ = 0$ with $\Pi_+ \neq 0$, so $Q$ is a zero divisor, and symmetrically for $Q_- = 0$. If both coordinates are nonzero, the displayed formula gives $Q Q^{-1} = \Pi_+ + \Pi_- = 1$, so $Q$ is a unit, and a unit is never a zero divisor.

So the zero divisors are exactly the non-zero elements of the two idempotent lines $\mathbb{R}\Pi_+$ and $\mathbb{R}\Pi_-$, and the non-units of $\mathbb{D}$ are $0$ together with the zero divisors. The classification of the zero-divisor set, its two families and its relation to the isotropic cone are the subject of *Zero Divisors of the Split-Complex Algebra*; the criterion by the norm belongs to *Norm and Invertibility in the General Split-Complex Algebra*, where the norm, the Hermitian form and the inner product — a form and a distance — are treated.

## Summary

The split complex algebra $\mathbb{D}$ is the two-dimensional real algebra with basis $1$, $j$ and the relation $j^2 = +1$. It is commutative, associative and unital, and it is not a field: it has zero divisors. A general element is written $Q = q + j q'$, and the algebra is $\mathbb{R}[x]/(x^2-1)$.

Split complex conjugation sends $q + j q'$ to $q - j q'$; it is the unique non-trivial involution, and the idempotent conjugation coincides with it, so the conjugation group is $\mathbb{Z}/2$. Its fixed points form the real subspace $\mathbb{R}_{\mathbb{D}}$ and its anti-fixed points the split imaginary subspace $j\mathbb{R}_{\mathbb{D}}$; these are the eigenspaces for the eigenvalues $+1$ and $-1$, and every split complex number decomposes uniquely as a real part plus an imaginary part. The algebra carries a second natural decomposition, which the complex case does not have: the idempotent decomposition $Q = Q_+\Pi_+ + Q_-\Pi_-$, where $\Pi_\pm = (1 \pm j)/2$ are the two nontrivial idempotents and $Q_\pm = q \pm q'$. The two components are independent ring homomorphisms, so $\mathbb{D}$ is the direct sum $\mathbb{R} \oplus \mathbb{R}$.

The algebra has zero divisors: $(1+j)(1-j) = 0$, and in the idempotent basis a non-zero element $Q = Q_+\Pi_+ + Q_-\Pi_-$ is a zero divisor exactly when one of its two coordinates vanishes, while it is a unit with $Q^{-1} = Q_+^{-1}\Pi_+ + Q_-^{-1}\Pi_-$ exactly when both are nonzero. The zero divisors are therefore the non-zero elements of the two idempotent lines $\mathbb{R}\Pi_+$ and $\mathbb{R}\Pi_-$, classified in *Zero Divisors of the Split-Complex Algebra*. The norm, the Hermitian form and the inner product are a form and a distance and belong to *Norm and Invertibility in the General Split-Complex Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra, $\mathbb{R}[x]/(x^2-1)$ |
| $1$ | Identity |
| $j$ | Split imaginary unit, $j^2 = +1$ |
| $Q = q + j q'$ | General split complex number |
| $q = \operatorname{Re} Q$ | Real part |
| $q' = \operatorname{Im} Q$ | Imaginary part |
| $\bar{Q} = Q^{*} = q - j q'$ | Split complex conjugate (the unique non-trivial involution) |
| $\tilde{Q} = \bar{Q}$ | Idempotent conjugate; equal to $\bar{Q}$ |
| $\Pi_+ = (1 + j)/2$ | Positive idempotent |
| $\Pi_- = (1 - j)/2$ | Negative idempotent |
| $Q = Q_+ \Pi_+ + Q_- \Pi_-$ | Idempotent decomposition, $Q_\pm = q \pm q'$ |
| $\operatorname{ann}(Q)$ | Annihilator, the ideal $\{B : QB = 0\}$ |
| $\mathbb{R}_{\mathbb{D}}$ | Real subspace, fixed-point set of $\bar{\cdot}$ |
| $j \mathbb{R}_{\mathbb{D}}$ | Split imaginary subspace, $-1$ eigenspace of $\bar{\cdot}$ |
| $\mathbb{D} \Pi_+, \mathbb{D} \Pi_-$ | The two ideals, isomorphic to $\mathbb{R}$ |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.
