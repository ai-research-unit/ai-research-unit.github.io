
# __Dual-Numbers Norm and Invertibility__

## Introduction

This article studies the norm of the dual-number algebra and the invertibility of its elements. It follows the base article *Dual-Numbers Algebra*, which fixed the ring $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$, the two conjugations, the two distinguished submodules and the maximal ideal $\mathrm{M} = (\varepsilon)$. The goal here is to define the norm and the Euclidean form, to establish the criterion for invertibility, to describe the group of units and its structure, and to record the three-way classification of the elements.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible, the algebra is $\mathbb{D}'_R$, and $\mathbb{D}$ denotes the split complex algebra $\mathbb{R}[j]$, $j^2 = +1$. A general dual number is written

$$
Q = q + \varepsilon q', \qquad q, q' \in R,
$$

with real part $q = \operatorname{Re} Q$ and infinitesimal part $q' = \operatorname{Inf} Q$. Dual conjugation is written $\bar Q = q - \varepsilon q'$ and the identity conjugation $\operatorname{id}(Q) = Q$. When $R = \mathbb{R}$ we write $\mathbb{D}'$ for $\mathbb{D}'_{\mathbb{R}}$, and $\mathrm{M} = \varepsilon\mathbb{R}$ is the maximal ideal. Every numerical value displayed below was recomputed in exact rational arithmetic.

The base is the commutative ring, not the field: the criterion for invertibility is stated for an arbitrary commutative $R$, and the places where a field, or invertibility of $2$, is needed are flagged. The default specialisation for the geometric statements is $R = \mathbb{R}$.

## The Norm

### Definition

**Definition.** The **norm** of a dual number $Q = q + \varepsilon q'$ is

$$
\langle Q\rangle = Q\bar Q = (q + \varepsilon q')(q - \varepsilon q') = q^2.
$$

It is an element of $R$, and it takes its value in the real submodule $R_{\mathbb{D}'}$.

### Basic Properties

**Proposition.** Let $Q_1 = q_1 + \varepsilon q'_1$ and $Q_2 = q_2 + \varepsilon q'_2$.

- **Dependence on the real part alone.** $\langle Q_1\rangle = q_1^2$ does not involve the infinitesimal part $q'_1$; equivalently, $\langle Q_1 + \eta\rangle = \langle Q_1\rangle$ for every $\eta \in \mathrm{M}$.
- **Invariance under dual conjugation.** $\langle \bar Q_1\rangle = \langle Q_1\rangle$, since $(-q'_1)^2 = q_1'^2$ plays no role and the real part is unchanged.
- **Sign.** Over an ordered ring $R$ the value $q_1^2$ is non-negative, and $\langle Q_1\rangle = 0$ if and only if $q_1 = 0$.
- **Vanishing locus.** Over a field, $\langle Q_1\rangle = 0$ if and only if $Q_1 \in \mathrm{M} = (\varepsilon)$.

**Proof.** The first two are immediate from $\langle Q_1\rangle = q_1^2$. For the third, $q_1^2 \ge 0$ in an ordered ring and $q_1^2 = 0$ forces $q_1 = 0$ in a domain. For the fourth, $q_1^2 = 0$ with $q_1$ in a field gives $q_1 = 0$, that is $Q_1 = \varepsilon q'_1 \in \mathrm{M}$.

The norm is **degenerate**: it is a quadratic form of rank one on the two-dimensional free module $\mathbb{D}'_R$, and its radical is the line $\mathrm{M} = \varepsilon R_{\mathbb{D}'}$. Degeneracy in this article always means that the associated bilinear form has nonzero radical, and the radical is the maximal ideal.

### Multiplicativity

**Theorem.** The norm is multiplicative:

$$
\langle Q_1 Q_2\rangle = \langle Q_1\rangle\,\langle Q_2\rangle.
$$

**Proof.** With $Q_1 = q_1 + \varepsilon q'_1$ and $Q_2 = q_2 + \varepsilon q'_2$ one has $Q_1 Q_2 = q_1 q_2 + (q_1 q'_2 + q'_1 q_2)\varepsilon$, so

$$
\langle Q_1 Q_2\rangle = (q_1 q_2)^2 = q_1^2q_2^2 = \langle Q_1\rangle\langle Q_2\rangle.
$$

The identity $(q_1 q_2)^2 = q_1^2q_2^2$ holds in every commutative ring.

**Corollary.** If $\langle Q_1\rangle \neq 0$ and $\langle Q_2\rangle \neq 0$, then $\langle Q_1 Q_2\rangle \neq 0$.

**Corollary.** If $\langle Q_1\rangle = 0$ or $\langle Q_2\rangle = 0$, then $\langle Q_1 Q_2\rangle = 0$. In particular the product of an element of the maximal ideal with any dual number lies in the maximal ideal, since $\mathrm{M}$ is a two-sided ideal.

**Remark.** Multiplicativity is the reason for the name, and it survives the degeneracy: the norm is a *ring homomorphism* from $\mathbb{D}'_R$ to the multiplicative monoid of $R$, whose kernel is the maximal ideal. It is the degenerate analogue of the modulus of a complex number.

### The Norm as a Degenerate Form

The word *norm* is used here only in a qualified sense, and it is worth recording which of the usual axioms survive.

- The **sign axiom** holds: $\langle -Q\rangle = \langle Q\rangle$ over any commutative ring.
- The **triangle inequality** has no content: $\langle Q\rangle$ takes values in $R$, which carries no order in general, and even over $\mathbb{R}$ the value $\langle Q\rangle$ is a square, not a length.
- The **scaling axiom** holds in its quadratic form, $\langle \lambda Q\rangle = \lambda^2 \langle Q\rangle$ for $\lambda \in R$, and this is the only homogeneity the form has.
- The **non-degeneracy axiom fails**: $\langle Q\rangle = 0$ for every nonzero $Q \in \mathrm{M}$.

So the norm is a degenerate multiplicative quadratic form, homogeneous of degree two, whose vanishing locus is the maximal ideal. It fails to be a norm in the analytic sense, and the Euclidean form of the next section supplies that analytic quantity.

### The Reduction of the Scale to $|q|$

There is nevertheless a genuine real size function on the units, singled out by the norm. Let $\rho : (\mathbb{D}'_{\mathbb{R}})^\times \to \mathbb{R}_{>0}$ be a continuous multiplicative function, normalised on the real scalars by

$$
\rho(\lambda) = |\lambda| \qquad \text{for } \lambda \in \mathbb{R}^\times.
$$

**Theorem.** The function

$$
r(Q) = |q| = \sqrt{|\langle Q\rangle|}
$$

is a continuous multiplicative real size function on the units, normalised on the real scalars, and it is invariant under the parabolic one-parameter subgroup, $r(Q(1 + t\varepsilon)) = r(Q)$ for every $t \in \mathbb{R}$. It is the unique such function with that invariance.

**Proof.** Multiplicativity is $\langle Q_1 Q_2\rangle = \langle Q_1\rangle\langle Q_2\rangle$ together with $r = \sqrt{\lvert\langle\cdot\rangle\rvert}$, and continuity is the continuity of $q \mapsto |q|$. At a real scalar $\lambda$ one has $r(\lambda) = \sqrt{\lambda^2} = |\lambda|$. For the shear invariance, $Q(1 + t\varepsilon) = q + (q' + tq)\varepsilon$ has the same real part $q$, so $r(Q(1 + t\varepsilon)) = |q| = r(Q)$. For uniqueness, by *Shears and Parabolic Rotations* every unit is $q(1 + s\varepsilon)$ with $q \in \mathbb{R}^\times$ and $s = q^{-1}q'$; the shear invariance gives $r(q + \varepsilon q') = r(q)$, so $r$ is determined on the whole unit group by its values on the real scalars, and the normalisation fixes those to be $|\cdot|$.

So the multiplicative scale on the units reduces to the absolute value of the real part: on the units the norm supplies a genuine positive scale via $r = \sqrt{\lvert\langle\cdot\rangle\rvert}$, and it is the only scale fixed by the shear, the square root being the square root of a square.

**Remark (the shear condition is needed).** Invariance under the shear is not automatic, and without it the scale is not unique. For each real $c$, the function

$$
\rho_c(q + \varepsilon q') = |q|\,\exp\!\Bigl(c\,\frac{q'}{q}\Bigr)
$$

is continuous on the units, multiplicative because the shear parameter is additive, $\rho_c(Q_1 Q_2) = \rho_c(Q_1)\rho_c(Q_2)$, and normalised on the real scalars, where $q' = 0$. These functions form a one-parameter family with $r = \rho_0$, and $r(Q) = |q|$ is exactly the member that is constant along the orbits of the parallel one-parameter subgroup $1 + \mathrm{M}$. So the reduction of the scale to $|q|$ is the statement that the norm fixes the scale to be blind to the nilpotent direction, which is the analytic face of the degeneracy of the form.

### The Norm from the Two Components

Writing $Q = q + \varepsilon q'$ with $q, q' \in R$, the norm depends on the two components only through the first:

$$
\langle Q\rangle = q^2.
$$

The Euclidean form of the next section is the sum of squares of the two components, and the contrast between the two is the whole content of the degeneracy.

## The Euclidean Form

### Definition

**Definition.** The **Euclidean form** of a dual number is the real quadratic form

$$
\mathfrak{Q}(Q) = q^2 + q'^2,
$$

the **Euclidean inner product** of two dual numbers $Q_1 = q_1 + \varepsilon q'_1$ and $Q_2 = q_2 + \varepsilon q'_2$ is

$$
\langle Q_1, Q_2 \rangle = q_1 q_2 + q'_1 q'_2,
$$

and the **Euclidean norm** is

$$
\|Q\|_E = \sqrt{q^2 + q'^2}.
$$

Over $R = \mathbb{R}$ this is the ordinary Euclidean structure of the plane $\mathbb{D}' \cong \mathbb{R}^2$ in dual coordinates.

### Properties

**Proposition.** The Euclidean form is positive-definite over an ordered ring and satisfies $\langle Q_1, Q_1 \rangle = \mathfrak{Q}(Q_1)$. It is **not** multiplicative with respect to the dual product:

$$
\mathfrak{Q}(Q_1 Q_2) = (q_1 q_2)^2 + (q_1 q'_2 + q'_1 q_2)^2, \qquad \mathfrak{Q}(Q_1)\mathfrak{Q}(Q_2) = (q_1^2 + q_1'^2)(q_2^2 + q_2'^2),
$$

and the two agree only when $q_1 q'_2 + q'_1 q_2 = \pm(q_1 q_2 - q'_1 q'_2)$, which is not an identity.

**Proof.** Substituting the components of $Q_1 Q_2$ gives the first expression; it is not the product of the two squares, as the example $Q_1 = Q_2 = 1 + \varepsilon$ shows: $\mathfrak{Q}(Q_1 Q_2) = \mathfrak{Q}(1 + 2\varepsilon) = 5$ while $\mathfrak{Q}(Q_1)\mathfrak{Q}(Q_2) = 2 \cdot 2 = 4$.

### Relation Between the Norm and the Euclidean Form

The two forms are distinct and play different roles.

| | Norm $\langle\cdot\rangle$ | Euclidean form $\mathfrak{Q}$ |
|---|---|---|
| Value | $q^2$ | $q^2 + q'^2$ |
| Multiplicative | yes | no |
| Degenerate | yes, radical $\mathrm{M}$ | no |
| Sign over $\mathbb{R}$ | non-negative | positive-definite |
| Controls | the multiplicative structure | the topology |

The inner product is **not** the real part of $Q_1\bar Q_2$; indeed

$$
Q_1\bar Q_2 = (q_1 + \varepsilon q'_1)(q_2 - \varepsilon q'_2) = q_1 q_2 + (q'_1 q_2 - q_1 q'_2)\varepsilon, \qquad \operatorname{Re}(Q_1\bar Q_2) = q_1 q_2,
$$

which is the polarisation of the degenerate norm $\langle\cdot\rangle$ and not of the Euclidean form. The distinction between $q_1 q_2$ and $q_1 q_2 + q'_1 q'_2$ is the distinction between the multiplicative and the topological structures on the plane.

## Invertibility

### Definition

**Definition.** A dual number $Q_1$ is **invertible** if there exists $Q_2$ with $Q_1 Q_2 = Q_2 Q_1 = 1$. The element $Q_2$, if it exists, is the **inverse** of $Q_1$ and is denoted $Q_1^{-1}$.

Since $\mathbb{D}'_R$ is commutative there is no distinction between left, right and two-sided inverses.

### Criterion for Invertibility

**Theorem.** Let $Q = q + \varepsilon q' \in \mathbb{D}'_R$. The following are equivalent.

1. $Q$ is invertible.
2. $q$ is a unit of $R$.
3. $\langle Q\rangle = q^2$ is a unit of $R$.
4. The residue class of $Q$ in the quotient ring $\mathbb{D}'_R/\mathrm{M} \cong R$ is a unit of $R$.

Over a field, the criterion reads: $Q$ is invertible if and only if $q \neq 0$, that is, if and only if $\langle Q\rangle \neq 0$.

**Proof.** If $q \in R^\times$, set $Q^{-1} = q^{-1} - q^{-2}\varepsilon q'$. Then

$$
Q Q^{-1} = (q + \varepsilon q')(q^{-1} - q^{-2}\varepsilon q') = q q^{-1} + \bigl(-q^{-1}q' + q' q^{-1}\bigr)\varepsilon = 1,
$$

so $Q$ is invertible, and (1) follows from (2). Since $q^2 \in R^\times$ exactly when $q \in R^\times$, (2) and (3) are equivalent. Conversely, if $Q Q_2 = 1$ for some $Q_2 = q_2 + \varepsilon q'_2$, then comparing real parts gives $q q_2 = 1$, so $q \in R^\times$, giving (2) from (1). The equivalence with the residue condition is the definition of $\mathrm{M} = (\varepsilon)$ together with the computation just made. Over a field, $q \in R^\times$ means $q \neq 0$.

### The Inverse Formula

**Corollary.** When $Q$ is invertible,

$$
Q^{-1} = \frac{1}{q} - \frac{q'}{q^2}\,\varepsilon.
$$

This is the degeneration of the complex formula $Q^{-1} = \bar Q/|Q|^2$: the conjugate is $\bar Q = q - \varepsilon q'$ and the "modulus squared" is $\langle Q\rangle = q^2$, so $\bar Q/\langle Q\rangle = (q - \varepsilon q')/q^2$, which is the inverse above.

**Corollary.** If $Q$ is invertible then so is $\bar Q$, and $\overline{Q^{-1}} = (\bar Q)^{-1}$.

**Proof.** Direct from the formula.

## The Group of Units

### Definition

**Definition.** The **group of units** of $\mathbb{D}'_R$ is

$$
(\mathbb{D}'_R)^\times = \{q + \varepsilon q' : q \in R^\times\}.
$$

It is a group under multiplication with identity $1$.

### Basic Properties

**Proposition.** Over a field, the group of units is the complement of the maximal ideal, $(\mathbb{D}'_k)^\times = \mathbb{D}'_k \setminus \mathrm{M}$, and over $R = \mathbb{R}$ it is an open, dense subset of the plane $\mathbb{D}'$ with exactly two connected components, distinguished by the sign of the real part.

**Proof.** Over a field the complement statement is the invertibility criterion $q \neq 0$. Over a general commutative ring the unit group is the smaller set $\{q + \varepsilon q' : q \in R^\times\}$, the preimage of $R^\times$ under $\operatorname{Re}$. Openness and density over $\mathbb{R}$ follow from $\{q \neq 0\}$ being the complement of a line. The map $Q \mapsto \operatorname{sgn}(q)$ is a continuous surjection onto $\{\pm 1\}$ that is multiplicative, so there are at least two components; $\{q > 0\}$ and $\{q < 0\}$ are each homeomorphic to a half-plane and hence connected.

### The Structure as a Semidirect Product

**Theorem.** Let $R$ be a commutative ring with $2$ invertible. The map

$$
\Theta : R^\times \times (R, +) \longrightarrow (\mathbb{D}'_R)^\times, \qquad \Theta(q, s) = q(1 + s\varepsilon),
$$

is an isomorphism of groups.

**Proof.** Every unit is $q(1 + s\varepsilon)$ with $q \in R^\times$ and $s = q^{-1}q'$, uniquely, so $\Theta$ is a bijection. It is a homomorphism because

$$
\Theta(q_1,s)\Theta(q_2,t) = q_1(1 + s\varepsilon)\,q_2(1 + t\varepsilon) = q_1 q_2\bigl(1 + (s + t)\varepsilon\bigr) = \Theta\bigl(q_1 q_2,\, s + t\bigr),
$$

using $\varepsilon^2 = 0$ and the commutativity of $R$.

So the group of units is the **direct product** $R^\times \times (R, +)$. Read as a semidirect product $R^\times \ltimes (R, +)$, the action of $R^\times$ on $(R, +)$ is trivial — because $\mathbb{D}'_R$ is commutative, the conjugation action of the first factor on the shear group $1 + \mathrm{M}$ is trivial — so the semidirect structure degenerates to the direct product:

$$
(\mathbb{D}'_R)^\times \cong R^\times \times (R, +).
$$

The extension

$$
1 \longrightarrow (1 + \mathrm{M}) \longrightarrow (\mathbb{D}'_R)^\times \longrightarrow R^\times \longrightarrow 1
$$

is split by $q \mapsto q$, and its kernel $1 + \mathrm{M} = \{1 + s\varepsilon\}$ is the **shear group**, isomorphic to $(R, +)$ through $s \mapsto 1 + s\varepsilon$. Over $\mathbb{R}$ the group of units is $\mathbb{R}^\times \times \mathbb{R}$: abelian, two-dimensional, with two contractible components.

### The Norm-One Group

**Definition.** The **norm-one group** is $H = \{Q \in \mathbb{D}'_{\mathbb{R}} : \langle Q\rangle = 1\}$.

**Proposition.** $H = \{q + \varepsilon q' : q = \pm 1\}$ is the union of the two parallel lines of real part $\pm 1$; its identity component is $H_0 = 1 + \mathrm{M}$, the shear group.

**Proof.** $\langle q + \varepsilon q'\rangle = q^2 = 1$ gives $q = \pm 1$ and leaves $q'$ free; the line $q = 1$ is $1 + \mathrm{M}$, the component through the identity.

## The Three-Way Classification

### The Table

Over a field $k$, combining the criterion for invertibility with the vanishing of the norm, the elements of $\mathbb{D}'_k$ fall into exactly three classes.

| Condition on $\langle Q\rangle$ | Condition on $Q$ | Conclusion |
|---|---|---|
| $\langle Q\rangle \neq 0$ | (automatically $Q \neq 0$) | $Q$ is invertible |
| $\langle Q\rangle = 0$ | $Q = 0$ | $Q$ is the zero element |
| $\langle Q\rangle = 0$ | $Q \neq 0$ | $Q$ is a zero divisor |

The third class is exactly $\mathrm{M} \setminus \{0\}$; its elements are studied in *Dual-Numbers Zero Divisors*, and the ideals that organize the classification are studied in *Dual-Numbers Ideals and the Maximal Ideal*.

### The Algebra Is Not a Division Algebra

By definition, a **division algebra** is an algebra in which every nonzero element is invertible; for a finite-dimensional algebra this is equivalent to the absence of zero divisors. The dual algebra contains the nonzero nilpotent $\varepsilon$, which is a zero divisor; hence $\mathbb{D}'_R$ is **not** a division algebra whenever $\mathrm{M} \neq 0$ (that is, whenever $\varepsilon \neq 0$ in the algebra).

This is in contrast to $\mathbb{R}$ and $\mathbb{C}$, which are fields; the dual algebra is a two-dimensional commutative associative real algebra, and it is not a field.

## Distribution of the Invertible Elements

The two distinguished submodules of $\mathbb{D}'_R$ behave oppositely with respect to invertibility.

### The Real Submodule

An element of $R_{\mathbb{D}'}$ is $Q = q$ with $q' = 0$, and $\langle Q\rangle = q^2$. Over a field, every nonzero element of $R_{\mathbb{D}'}$ is invertible, and $R_{\mathbb{D}'}$ is a subalgebra isomorphic to the field; it is the unique subalgebra of $\mathbb{D}'_R$ that is a division algebra.

### The Infinitesimal Submodule

An element of $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ is $Q = \varepsilon q'$ with $q = 0$, and $\langle Q\rangle = 0$. Hence **every** element of the infinitesimal submodule is a non-unit; the invertible elements meet $\mathrm{M}$ in the empty set, and the zero divisors are exactly $\mathrm{M} \setminus \{0\}$.

### Summary of the Distribution

Over a field $k$ the distribution is as follows, the units being read off from $R^\times = k^\times$ and the zero-divisor column from the criterion of *Dual-Numbers Zero Divisors*.

| Submodule | Elements | $\langle\cdot\rangle$ | Units | Zero divisors |
|---|---|---|---|---|
| $R_{\mathbb{D}'}$ | $q$, $q \in R$ | $q^2$ | all $q \in R^\times$ | none |
| $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ | $\varepsilon q'$, $q' \in R$ | $0$ | none | all $q' \neq 0$ |

The two submodules are the eigenspaces of dual conjugation, and the distribution table is the algebraic statement that the norm is a homomorphism whose kernel is exactly one of the two eigenspaces.

## Relation to the Conjugate Decomposition

The criterion is stated in terms of the norm and the real part. In the conjugate decomposition

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}, \qquad Q = q + \varepsilon q',
$$

the norm reads $\langle Q\rangle = (\operatorname{Re} Q)^2$, and invertibility depends only on the component in the real submodule. This is why the group of units is a direct product: the multiplicative structure of $\mathbb{D}'_R$ is that of $R$ on the real submodule, with the infinitesimal submodule carried along as a nilpotent, invisible addition. In the dual algebra only one nontrivial conjugation exists, and the distribution collapses to the two-row table above.

## Comparison with the Split Complex Case

The three norms of the family are

$$
N_{\mathbb{C}}(A) = a^2 + a'^2, \qquad N_{\mathbb{D}}(A) = a^2 - a'^2, \qquad N_{\mathbb{D}'}(Q) = q^2,
$$

for $\mathbb{C}$, the split complex numbers $\mathbb{D} = \mathbb{R}[j]$ and the dual numbers. They are the three real binary quadratic forms of rank two, two and one respectively: positive-definite, indefinite non-degenerate, and degenerate.

- In $\mathbb{C}$ the norm never vanishes away from the origin, and every nonzero element is a unit; the norm-one group is the circle.
- In the split complex $\mathbb{D}$ the norm is indefinite, its null set is the pair of linear null directions on which the zero divisors live, and the norm-one group is a hyperbola, with two branches.
- In $\mathbb{D}'$ the norm is degenerate, its null set is the maximal ideal, a whole line, and the norm-one group is a pair of parallel lines.

The three cases form the family of the two-dimensional real algebras: complex, split complex, dual. In every case the criterion for invertibility is the non-vanishing of a single multiplicative form, and the differences among the members lie in the rank, the signature and the value ring of that form.

## Summary

The norm $\langle Q\rangle = Q\bar Q = q^2$ of the dual-number algebra is a degenerate multiplicative quadratic form of rank one, depending only on the real part, with radical the maximal ideal $\mathrm{M} = (\varepsilon)$. It fails to be a norm in the analytic sense, and the Euclidean form $q^2 + q'^2$ is the positive-definite but non-multiplicative quantity that carries the topology. The continuous multiplicative real size function on the units, normalised on the real scalars and invariant under the parabolic one-parameter subgroup, is $r(Q) = |q| = \sqrt{|\langle Q\rangle|}$, the multiplicative scale on the units; without the shear-invariance requirement the normalised multiplicative size functions form the one-parameter family $\rho_c = |q|\exp(c\,q'/q)$.

A dual number $Q = q + \varepsilon q'$ is invertible if and only if its real part is a unit of $R$; over a field, if and only if $q \neq 0$, equivalently if and only if $\langle Q\rangle \neq 0$. The inverse is $Q^{-1} = q^{-1} - q^{-2}\varepsilon q'$. Over a field the group of units is $\mathbb{D}'_k \setminus \mathrm{M}$; it is the split extension $1 \to (1 + \mathrm{M}) \to (\mathbb{D}'_k)^\times \to k^\times \to 1$, and since $\mathbb{D}'_k$ is commutative the extension is the direct product $k^\times \times (k, +)$ with the shear group $1 + \mathrm{M}$ as second factor. The elements of $\mathbb{D}'_k$ over a field fall into three classes: the invertible elements, the zero element, and the zero divisors $\mathrm{M} \setminus \{0\}$; the algebra is therefore not a division algebra, in contrast to $\mathbb{R}$ and $\mathbb{C}$. The invertible elements occupy the real submodule and avoid the infinitesimal submodule entirely, and this asymmetry of the two eigenspaces of dual conjugation is the shape the norm imposes on the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $Q = q + \varepsilon q'$ | General dual number |
| $q = \operatorname{Re} Q$ | Real part |
| $q' = \operatorname{Inf} Q$ | Infinitesimal part |
| $\bar{Q} = q - \varepsilon q'$ | Dual conjugation |
| $\langle Q\rangle = Q\bar Q = q^2$ | Norm, degenerate, radical $\mathrm{M}$ |
| $\mathfrak{Q}(Q) = q^2 + q'^2$ | Euclidean form |
| $\langle Q_1, Q_2 \rangle = q_1 q_2 + q'_1 q'_2$ | Euclidean inner product |
| $\|Q\|_E = \sqrt{q^2 + q'^2}$ | Euclidean norm |
| $r(Q) = |q| = \sqrt{|\langle Q\rangle|}$ | Continuous multiplicative real size on the units, normalised on the scalars and shear-invariant |
| $\rho_c(Q) = |q|\exp(c\,q'/q)$ | The normalised multiplicative size functions; $r = \rho_0$ |
| $\mathrm{M} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$ | Maximal ideal, kernel of $\langle\cdot\rangle$ |
| $R_{\mathbb{D}'}$ | Real submodule |
| $(\mathbb{D}'_k)^\times = \mathbb{D}'_k \setminus \mathrm{M}$ | Group of units, over a field $k$ |
| $1 + \mathrm{M}$ | Shear group, kernel of $(\mathbb{D}'_R)^\times \to R^\times$ |
| $\Theta : R^\times \times (R,+) \to (\mathbb{D}'_R)^\times$ | Unit-group isomorphism, $\Theta(q,s) = q(1 + s\varepsilon)$ |
| $H = \{Q : \langle Q\rangle = 1\}$ | Norm-one group, lines $q = \pm 1$ |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the degeneracy of the dual-number form and its geometry.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for the dual numbers and their degenerate quadratic form alongside the complex and split-complex cases.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Berlin, 1991), for the theory of degenerate quadratic forms, their radical, and their isometry groups.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, Providence, 2005), for the classification of quadratic forms by their radical.
