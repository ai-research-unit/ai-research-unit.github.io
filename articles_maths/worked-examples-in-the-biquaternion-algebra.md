
# __Worked Examples in the Biquaternion Algebra__

## Introduction

*Biquaternion Algebra ($\mathbb{B}$)* developed the algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, its six distinguished real subspaces, its three decompositions and its quadratic forms. This article works the computations out on explicit elements. The aim is a reference of concrete facts: the multiplication table of the basis, the six subspaces exhibited on one element, the four conjugations applied to that element, the norm form and the unit criterion, and explicit zero-divisor pairs. The idempotents and the minimal left ideals are the subject of *Biquaternion Idempotents and Projections*, which owns the general construction.

Notation follows *Biquaternion Algebra ($\mathbb{B}$)*. A biquaternion is written in developed form

$$
\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3, \qquad Q_\mu \in \mathbb{C},
$$

with the quaternion basis $e_0 = 1$, $e_1, e_2, e_3$, and the central complex unit $i$, $i^2 = -1$, commuting with every $e_\mu$. The scalar part of $\tilde{Q}$ is $\mathrm{Sc}\,\tilde{Q} = Q_0$, its vector part is $\mathbf{Q} = Q_1e_1 + Q_2e_2 + Q_3e_3$, and the quaternion conjugate is $\bar{\tilde{Q}} = Q_0e_0 - \mathbf{Q}$. The fixed element used throughout is

$$
\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3 .
$$

## The Multiplication Table

The products of the quaternion basis elements follow the cyclic rule $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$, with $e_k^2 = -e_0$ and $e_je_k = -e_ke_j$ for $j\neq k$. Writing the products in a table, with the left factor as the row and the right factor as the column:

| | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

The table is the quaternion table, but the coefficients are now complex and the central element $i$ multiplies every entry: $i e_\mu = e_\mu i$. The full multiplication of $\mathbb{B}$ is therefore determined by the table above together with $i^2 = -1$ and centrality of $i$. As a $\mathbb{C}$-algebra the dimension is $4$; as a real algebra the basis may be taken as $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$ and the dimension is $8$.

**Example.** The products used below are

$$
e_1^2 = e_2^2 = e_3^2 = -e_0, \qquad e_1e_2 = e_3, \quad e_2e_1 = -e_3, \quad e_1e_3 = -e_2, \quad e_3e_2 = -e_1 .
$$

## The Six Subspaces on a Concrete Element

The six distinguished real subspaces are the fixed and anti-fixed spaces of the three commuting involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\dagger} = \bar{\cdot}\circ{}^{*}$; the fourth conjugation $\flat = -\dagger$ has the same two eigenspaces as ${}^{\dagger}$ with the roles of the fixed and anti-fixed space interchanged, so it contributes no further subspaces. On the fixed element the decompositions are as follows.

| Subspace | Defining condition | Component of $\tilde{Q}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | $\bar{\tilde{Q}} = \tilde{Q}$ | $(2+i)e_0$ |
| $\mathrm{Vect}(\mathbb{B})$ (vector) | $\bar{\tilde{Q}} = -\tilde{Q}$ | $(1-i)e_1 + 3e_2 + ie_3$ |
| $\mathbb{H}_{\mathbb{B}}$ (quaternion) | $\tilde{Q}^{*} = \tilde{Q}$ | $2e_0 + e_1 + 3e_2$ |
| $i\mathbb{H}_{\mathbb{B}}$ (anti-quaternion) | $\tilde{Q}^{*} = -\tilde{Q}$ | $ie_0 - ie_1 + ie_3$ |
| $\mathbb{M}_+$ (Hermitian) | $\tilde{Q}^{\dagger} = \tilde{Q}$ | $2e_0 - ie_1 + ie_3$ |
| $\mathbb{M}_-$ (anti-Hermitian) | $\tilde{Q}^{\flat} = \tilde{Q}$ | $ie_0 + e_1 + 3e_2$ |

The decomposition into scalar and vector parts reads $\tilde{Q} = (2+i)e_0 + \bigl((1-i)e_1 + 3e_2 + ie_3\bigr)$, and the decomposition into quaternion and anti-quaternion parts reads

$$
\tilde{Q} = \bigl(2e_0 + e_1 + 3e_2\bigr) + i\bigl(e_0 - e_1 + e_3\bigr) = \tilde{Q}_r + i\tilde{Q}_i,
$$

with $\tilde{Q}_r, \tilde{Q}_i \in \mathbb{H}_{\mathbb{B}}$, as the basis of the quaternion subspace consists of the basis elements with real coefficients. The Hermitian decomposition reads

$$
\tilde{Q} = \bigl(2e_0 - ie_1 + ie_3\bigr) + \bigl(ie_0 + e_1 + 3e_2\bigr) = \tilde{Q}_+ + \tilde{Q}_-,
$$

and the two pieces are distinguished by the signs of the scalar and vector coefficients: $\tilde{Q}_+$ has real scalar part and purely imaginary vector part, $\tilde{Q}_-$ has purely imaginary scalar part and real vector part. Each of the three decompositions is a direct sum of two of the six subspaces, and the components above are the concrete instances.

## The Four Conjugations on the Concrete Element

Applying the four conjugations to $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$ gives

$$
\bar{\tilde{Q}} = (2+i)e_0 - (1-i)e_1 - 3e_2 - ie_3,
$$

$$
\tilde{Q}^{*} = (2-i)e_0 + (1+i)e_1 + 3e_2 - ie_3,
$$

$$
\tilde{Q}^{\dagger} = \bar{\tilde{Q}}^{*} = (2-i)e_0 - (1+i)e_1 - 3e_2 + ie_3,
$$

$$
\tilde{Q}^{\flat} = -\tilde{Q}^{\dagger} = -(2-i)e_0 + (1+i)e_1 + 3e_2 - ie_3 .
$$

Each is an involution, and the Klein group is visible in the relations $\tilde{Q}^{\dagger} = \bar{\tilde{Q}}^{*} = \tilde{Q}^{*\bar{}}$; the fourth conjugation satisfies $(\tilde{Q}^{\dagger})^{\flat} = -\tilde{Q}$ and $(\tilde{Q}^{\flat})^{\dagger} = -\tilde{Q}$, so it is the composition of $\dagger$ with the central sign $-1$. The fixed points of each involution give one of the six subspaces tabulated above: for instance, the Hermitian part of $\tilde{Q}$ is $\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\dagger}) = 2e_0 - ie_1 + ie_3$, which agrees with the table.

## The Norm Form and the Unit Criterion

**Definition.** The **norm form** of a biquaternion is

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 \in \mathbb{C},
$$

a central element of $\mathbb{B}$. It is multiplicative: $N(\tilde{P}\tilde{Q}) = N(\tilde{P})N(\tilde{Q})$.

**Proposition (unit criterion).** A biquaternion $\tilde{Q}$ is a unit if and only if $N(\tilde{Q}) \neq 0$, and then

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})} .
$$

*Proof.* If $N(\tilde{Q}) \neq 0$ the displayed element is a two-sided inverse, since $\tilde{Q}\bar{\tilde{Q}} = \bar{\tilde{Q}}\tilde{Q} = N(\tilde{Q})$ is central. Conversely let $\tilde{Q} \neq 0$ with $N(\tilde{Q}) = 0$. Then $\tilde{Q}\bar{\tilde{Q}} = 0$; if $\bar{\tilde{Q}} \neq 0$ this exhibits $\tilde{Q}$ as a zero divisor, hence a non-unit; and if $\bar{\tilde{Q}} = 0$ then all four coefficients of $\tilde{Q}$ vanish, so $\tilde{Q} = 0$, contrary to hypothesis. Hence $\tilde{Q}$ is not a unit. $\square$

**Example (a unit).** For the fixed element,

$$
N(\tilde{Q}) = (2+i)^2 + (1-i)^2 + 3^2 + i^2 = (3+4i) + (-2i) + 9 - 1 = 11 + 2i \neq 0,
$$

so $\tilde{Q}$ is a unit, with inverse $\bar{\tilde{Q}}/(11+2i)$.

**Example (the norm under conjugation).** The conjugation rules give

$$
N(\bar{\tilde{Q}}) = N(\tilde{Q}) = 11+2i, \qquad N(\tilde{Q}^{*}) = N(\tilde{Q})^{*} = 11-2i, \qquad N(\tilde{Q}^{\dagger}) = 11-2i, \qquad N(\tilde{Q}^{\flat}) = 11-2i,
$$

because $N$ is invariant under $\bar{\cdot}$ and conjugate-linear in the complex coefficient under ${}^{*}$, and $\flat$ differs from $\dagger$ by the sign $-1$, whose square is $1$.

## Idempotents and the Two Minimal Left Ideals

The standard idempotents $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$ and $\tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3)$ satisfy $\tilde\Pi_1^2 = \tilde\Pi_1$, $\tilde\Pi_2^2 = \tilde\Pi_2$, $\tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = 0$ and $\tilde\Pi_1 + \tilde\Pi_2 = e_0$; they are primitive; and they give the decomposition $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ into two minimal left ideals of real dimension $4$. The verification is carried out in *Biquaternion Idempotents and Projections*, which owns the idempotents of the series.

## Explicit Zero Divisors

**Example (an explicit pair).** With the standard idempotents $\tilde\Pi_1, \tilde\Pi_2$ of *Biquaternion Idempotents and Projections*, $\tilde\Pi_1\tilde\Pi_2 = 0$ and both factors are nonzero: this is a zero-divisor pair. In unnormalised form, set $a = e_0 + ie_3$ and $b = e_0 - ie_3$. Then

$$
ab = e_0 - (ie_3)^2 = e_0 - 1 = 0, \qquad a \neq 0, \qquad b \neq 0,
$$

and the norms vanish: $N(a) = 1^2 + i^2 = 0$, $N(b) = 1 + i^2 = 0$. Both $a$ and $b$ have two nonzero complex coefficients, $a = e_0 + ie_3$ and $b = e_0 - ie_3$.

The zero divisors of $\mathbb{B}$ are exactly the nonzero elements of norm $0$, that is, the nonzero solutions of $Q_0^2+Q_1^2+Q_2^2+Q_3^2 = 0$, a quadric hypersurface in $\mathbb{C}^4$.

The computations show all the structural features asserted in *Biquaternion Algebra ($\mathbb{B}$)* on a single element and on the standard idempotents: the six subspaces split the element into its centre, vector, quaternion, anti-quaternion, Hermitian and anti-Hermitian parts; the four conjugations act as listed; the norm form decides invertibility; and the two primitive idempotents produce the decomposition $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ into minimal left ideals.

## Summary

The multiplication of $\mathbb{B}$ is the quaternion table with complex coefficients and central $i$, $i^2 = -1$. On the element $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$ the **norm form** is $N(\tilde{Q}) = Q_0^2+Q_1^2+Q_2^2+Q_3^2 = 11+2i$; the element is a unit because $N\neq0$, with inverse $\bar{\tilde{Q}}/N$. The six subspaces are exhibited by the scalar-vector, quaternion-anti-quaternion and Hermitian-anti-Hermitian decompositions of $\tilde{Q}$, and the four conjugations $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger}$ and ${}^{\flat} = -\dagger$ act on it as listed.

The idempotents $\tilde\Pi_1, \tilde\Pi_2$ of *Biquaternion Idempotents and Projections* satisfy $\tilde\Pi_1\tilde\Pi_2 = 0$ and give $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ with each summand minimal; the pair $a = e_0+ie_3$, $b = e_0-ie_3$ is an explicit zero-divisor pair of norm $0$; and the zero divisors of $\mathbb{B}$ are exactly the nonzero isotropic vectors of the complex quadratic form $Q_0^2+Q_1^2+Q_2^2+Q_3^2$. As a left module over itself, $\mathbb{B}$ has the decomposition $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ into minimal left ideals.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $i$ | Central complex unit, $i^2 = -1$ |
| $\mathrm{Sc}\,\tilde{Q} = Q_0$ | Scalar part |
| $\mathbf{Q} = \sum_{k=1}^3 Q_ke_k$ | Vector part |
| $\bar{\cdot}$ | Quaternion conjugation |
| ${}^{*}$ | Complex conjugation |
| ${}^{\dagger} = \bar{\cdot}\circ{}^{*}$ | Hermitian conjugation |
| ${}^{\flat} = -\dagger$ | Anti-Hermitian conjugation |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ | The six subspaces |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form, multiplicative |
| $\tilde\Pi_1 = \tfrac12(e_0+ie_3),\ \tilde\Pi_2 = \tfrac12(e_0-ie_3)$ | Orthogonal primitive idempotents |
| $\mathbb{B}\tilde\Pi_1,\ \mathbb{B}\tilde\Pi_2$ | The two minimal left ideals |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents and minimal left ideals in the structure theory of finite-dimensional algebras.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for idempotents, minimal ideals and the decomposition of a ring into simple modules.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion and biquaternion computations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2nd ed. 2001), for the complexification of the quaternions.
