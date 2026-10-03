
# __Dual-Numbers Norm and Invertibility__

## Introduction

This article studies the norm of the dual-number algebra and the invertibility of its elements. It follows the base article *Dual-Numbers Algebra*, which fixed the ring $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$, the two conjugations, the two distinguished submodules and the maximal ideal $\mathrm{M} = (\varepsilon)$. The goal here is to define the norm and the Euclidean form, to establish the criterion for invertibility, to describe the group of units and its structure, and to record the three-way classification of the elements.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible, the algebra is $\mathbb{D}'_R$, and $\mathbb{D}$ denotes the split complex algebra $\mathbb{R}[j]$, $j^2 = +1$. A general dual number is written

$$
A = a + \varepsilon a', \qquad a, a' \in R,
$$

with real part $a = \operatorname{Re} A$ and infinitesimal part $a' = \operatorname{Inf} A$. Dual conjugation is written $\bar A = a - \varepsilon a'$ and the identity conjugation $\operatorname{id}(A) = A$. When $R = \mathbb{R}$ we write $\mathbb{D}'$ for $\mathbb{D}'_{\mathbb{R}}$, and $\mathrm{M} = \varepsilon\mathbb{R}$ is the maximal ideal. Every numerical value displayed below was recomputed in exact rational arithmetic.

The base is the commutative ring, not the field: the criterion for invertibility is stated for an arbitrary commutative $R$, and the places where a field, or invertibility of $2$, is needed are flagged. The default specialisation for the geometric statements is $R = \mathbb{R}$.

## The Norm

### Definition

**Definition.** The **norm** of a dual number $A = a + \varepsilon a'$ is

$$
N(A) = A\bar A = (a + \varepsilon a')(a - \varepsilon a') = a^2.
$$

It is an element of $R$, and it takes its value in the real submodule $R_{\mathbb{D}'}$.

### Basic Properties

**Proposition.** Let $A = a + \varepsilon a'$ and $B = b + \varepsilon b'$.

- **Dependence on the real part alone.** $N(A) = a^2$ does not involve the infinitesimal part $a'$; equivalently, $N(A + \eta) = N(A)$ for every $\eta \in \mathrm{M}$.
- **Invariance under dual conjugation.** $N(\bar A) = N(A)$, since $(-a')^2 = a'^2$ plays no role and the real part is unchanged.
- **Sign.** Over an ordered ring $R$ the value $a^2$ is non-negative, and $N(A) = 0$ if and only if $a = 0$.
- **Vanishing locus.** Over a field, $N(A) = 0$ if and only if $A \in \mathrm{M} = (\varepsilon)$.

**Proof.** The first two are immediate from $N(A) = a^2$. For the third, $a^2 \ge 0$ in an ordered ring and $a^2 = 0$ forces $a = 0$ in a domain. For the fourth, $a^2 = 0$ with $a$ in a field gives $a = 0$, that is $A = \varepsilon a' \in \mathrm{M}$.

The norm is **degenerate**: it is a quadratic form of rank one on the two-dimensional free module $\mathbb{D}'_R$, and its radical is the line $\mathrm{M} = \varepsilon R_{\mathbb{D}'}$. Degeneracy in this article always means that the associated bilinear form has nonzero radical, and the radical is the maximal ideal.

### Multiplicativity

**Theorem.** The norm is multiplicative:

$$
N(AB) = N(A)\,N(B).
$$

**Proof.** With $A = a + \varepsilon a'$ and $B = b + \varepsilon b'$ one has $AB = a b + (a b' + a' b)\varepsilon$, so

$$
N(AB) = (a b)^2 = a^2b^2 = N(A)N(B).
$$

The identity $(a b)^2 = a^2b^2$ holds in every commutative ring.

**Corollary.** If $N(A) \neq 0$ and $N(B) \neq 0$, then $N(AB) \neq 0$.

**Corollary.** If $N(A) = 0$ or $N(B) = 0$, then $N(AB) = 0$. In particular the product of an element of the maximal ideal with any dual number lies in the maximal ideal, since $\mathrm{M}$ is a two-sided ideal.

**Remark.** Multiplicativity is the reason for the name, and it survives the degeneracy: the norm is a *ring homomorphism* from $\mathbb{D}'_R$ to the multiplicative monoid of $R$, whose kernel is the maximal ideal. It is the degenerate analogue of the modulus of a complex number.

### The Norm as a Degenerate Form

The word *norm* is used here only in a qualified sense, and it is worth recording which of the usual axioms survive.

- The **sign axiom** holds: $N(-A) = N(A)$ over any commutative ring.
- The **triangle inequality** has no content: $N$ takes values in $R$, which carries no order in general, and even over $\mathbb{R}$ the value $N(A)$ is a square, not a length.
- The **scaling axiom** holds in its quadratic form, $N(\lambda A) = \lambda^2 N(A)$ for $\lambda \in R$, and this is the only homogeneity the form has.
- The **non-degeneracy axiom fails**: $N(A) = 0$ for every nonzero $A \in \mathrm{M}$.

So the norm is a degenerate multiplicative quadratic form, homogeneous of degree two, whose vanishing locus is the maximal ideal. It fails to be a norm in the analytic sense, and the Euclidean form of the next section supplies that analytic quantity.

### The Reduction of the Scale to $|a|$

There is nevertheless a genuine real size function on the units, singled out by the norm. Let $\rho : (\mathbb{D}'_{\mathbb{R}})^\times \to \mathbb{R}_{>0}$ be a continuous multiplicative function, normalised on the real scalars by

$$
\rho(\lambda) = |\lambda| \qquad \text{for } \lambda \in \mathbb{R}^\times.
$$

**Theorem.** The function

$$
r(A) = |a| = \sqrt{|N(A)|}
$$

is a continuous multiplicative real size function on the units, normalised on the real scalars, and it is invariant under the parabolic one-parameter subgroup, $r(A(1 + t\varepsilon)) = r(A)$ for every $t \in \mathbb{R}$. It is the unique such function with that invariance.

**Proof.** Multiplicativity is $N(AB) = N(A)N(B)$ together with $r = \sqrt{|N|}$, and continuity is the continuity of $a \mapsto |a|$. At a real scalar $\lambda$ one has $r(\lambda) = \sqrt{\lambda^2} = |\lambda|$. For the shear invariance, $A(1 + t\varepsilon) = a + (a' + ta)\varepsilon$ has the same real part $a$, so $r(A(1 + t\varepsilon)) = |a| = r(A)$. For uniqueness, by *Shears and Parabolic Rotations* every unit is $a(1 + s\varepsilon)$ with $a \in \mathbb{R}^\times$ and $s = a^{-1}a'$; the shear invariance gives $r(a + \varepsilon a') = r(a)$, so $r$ is determined on the whole unit group by its values on the real scalars, and the normalisation fixes those to be $|\cdot|$.

So the multiplicative scale on the units reduces to the absolute value of the real part: on the units the norm supplies a genuine positive scale via $r = \sqrt{|N|}$, and it is the only scale fixed by the shear. The biquaternion article *Biquaternion Norm and Invertibility* proves the analogous statement with $r(\tilde{Q}) = \sqrt{|N(\tilde{Q})|}$; the dual case is the rank-one degeneration of it, in which the square root is the square root of a square.

**Remark (the shear condition is needed).** Invariance under the shear is not automatic, and without it the scale is not unique. For each real $c$, the function

$$
\rho_c(a + \varepsilon a') = |a|\,\exp\!\Bigl(c\,\frac{a'}{a}\Bigr)
$$

is continuous on the units, multiplicative because the shear parameter is additive, $\rho_c(AB) = \rho_c(A)\rho_c(B)$, and normalised on the real scalars, where $a' = 0$. These functions form a one-parameter family with $r = \rho_0$, and $r(A) = |a|$ is exactly the member that is constant along the orbits of the parallel one-parameter subgroup $1 + \mathrm{M}$. So the reduction of the scale to $|a|$ is the statement that the norm fixes the scale to be blind to the nilpotent direction, which is the analytic face of the degeneracy of the form.

### The Norm from the Two Components

Writing $A = A_r + A_i\varepsilon$ with $A_r = a$ and $A_i = a'$ in $R$, the norm depends on the two components only through the first:

$$
N(A) = A_r^2.
$$

The Euclidean form of the next section is the sum of squares of the two components, and the contrast between the two is the whole content of the degeneracy.

## The Euclidean Form

### Definition

**Definition.** The **Euclidean form** of a dual number is the real quadratic form

$$
q(A) = a^2 + a'^2,
$$

the **Euclidean inner product** of two dual numbers $A = a + \varepsilon a'$ and $B = b + \varepsilon b'$ is

$$
\langle A, B \rangle = a b + a' b',
$$

and the **Euclidean norm** is

$$
\|A\|_E = \sqrt{a^2 + a'^2}.
$$

Over $R = \mathbb{R}$ this is the ordinary Euclidean structure of the plane $\mathbb{D}' \cong \mathbb{R}^2$ in dual coordinates.

### Properties

**Proposition.** The Euclidean form is positive-definite over an ordered ring and satisfies $\langle A, A \rangle = q(A)$. It is **not** multiplicative with respect to the dual product:

$$
q(AB) = (a b)^2 + (a b' + a' b)^2, \qquad q(A)q(B) = (a^2 + a'^2)(b^2 + b'^2),
$$

and the two agree only when $a b' + a' b = \pm(a b - a' b')$, which is not an identity.

**Proof.** Substituting the components of $AB$ gives the first expression; it is not the product of the two squares, as the example $A = B = 1 + \varepsilon$ shows: $q(AB) = q(1 + 2\varepsilon) = 5$ while $q(A)q(B) = 2 \cdot 2 = 4$.

### Relation Between the Norm and the Euclidean Form

The two forms are distinct and play different roles.

| | Norm $N$ | Euclidean form $q$ |
|---|---|---|
| Value | $a^2$ | $a^2 + a'^2$ |
| Multiplicative | yes | no |
| Degenerate | yes, radical $\mathrm{M}$ | no |
| Sign over $\mathbb{R}$ | non-negative | positive-definite |
| Controls | the multiplicative structure | the topology |

The inner product is **not** the real part of $A\bar B$; indeed

$$
A\bar B = (a + \varepsilon a')(b - \varepsilon b') = a b + (a' b - a b')\varepsilon, \qquad \operatorname{Re}(A\bar B) = a b,
$$

which is the polarisation of the degenerate norm $N$ and not of the Euclidean form. The distinction between $a b$ and $a b + a' b'$ is the distinction between the multiplicative and the topological structures on the plane.

## Invertibility

### Definition

**Definition.** A dual number $A$ is **invertible** if there exists $B$ with $AB = BA = 1$. The element $B$, if it exists, is the **inverse** of $A$ and is denoted $A^{-1}$.

Since $\mathbb{D}'_R$ is commutative there is no distinction between left, right and two-sided inverses.

### Criterion for Invertibility

**Theorem.** Let $A = a + \varepsilon a' \in \mathbb{D}'_R$. The following are equivalent.

1. $A$ is invertible.
2. $a$ is a unit of $R$.
3. $N(A) = a^2$ is a unit of $R$.
4. The residue class of $A$ in the quotient ring $\mathbb{D}'_R/\mathrm{M} \cong R$ is a unit of $R$.

Over a field, the criterion reads: $A$ is invertible if and only if $a \neq 0$, that is, if and only if $N(A) \neq 0$.

**Proof.** If $a \in R^\times$, set $B = a^{-1} - a^{-2}\varepsilon a'$. Then

$$
AB = (a + \varepsilon a')(a^{-1} - a^{-2}\varepsilon a') = a a^{-1} + \bigl(-a^{-1}a' + a' a^{-1}\bigr)\varepsilon = 1,
$$

so $A$ is invertible, and (1) follows from (2). Since $a^2 \in R^\times$ exactly when $a \in R^\times$, (2) and (3) are equivalent. Conversely, if $AB = 1$ for some $B = b + \varepsilon b'$, then comparing real parts gives $a b = 1$, so $a \in R^\times$, giving (2) from (1). The equivalence with the residue condition is the definition of $\mathrm{M} = (\varepsilon)$ together with the computation just made. Over a field, $a \in R^\times$ means $a \neq 0$.

### The Inverse Formula

**Corollary.** When $A$ is invertible,

$$
A^{-1} = \frac{1}{a} - \frac{a'}{a^2}\,\varepsilon.
$$

This is the degeneration of the complex formula $A^{-1} = \bar A/|A|^2$: the conjugate is $\bar A = a - \varepsilon a'$ and the "modulus squared" is $N(A) = a^2$, so $\bar A/N(A) = (a - \varepsilon a')/a^2$, which is the inverse above.

**Corollary.** If $A$ is invertible then so is $\bar A$, and $\overline{A^{-1}} = (\bar A)^{-1}$.

**Proof.** Direct from the formula.

## The Group of Units

### Definition

**Definition.** The **group of units** of $\mathbb{D}'_R$ is

$$
(\mathbb{D}'_R)^\times = \{a + \varepsilon a' : a \in R^\times\}.
$$

It is a group under multiplication with identity $1$.

### Basic Properties

**Proposition.** Over a field, the group of units is the complement of the maximal ideal, $(\mathbb{D}'_k)^\times = \mathbb{D}'_k \setminus \mathrm{M}$, and over $R = \mathbb{R}$ it is an open, dense subset of the plane $\mathbb{D}'$ with exactly two connected components, distinguished by the sign of the real part.

**Proof.** Over a field the complement statement is the invertibility criterion $a \neq 0$. Over a general commutative ring the unit group is the smaller set $\{a + \varepsilon a' : a \in R^\times\}$, the preimage of $R^\times$ under $\operatorname{Re}$. Openness and density over $\mathbb{R}$ follow from $\{a \neq 0\}$ being the complement of a line. The map $A \mapsto \operatorname{sgn}(a)$ is a continuous surjection onto $\{\pm 1\}$ that is multiplicative, so there are at least two components; $\{a > 0\}$ and $\{a < 0\}$ are each homeomorphic to a half-plane and hence connected.

### The Structure as a Semidirect Product

**Theorem.** Let $R$ be a commutative ring with $2$ invertible. The map

$$
\Theta : R^\times \times (R, +) \longrightarrow (\mathbb{D}'_R)^\times, \qquad \Theta(a, s) = a(1 + s\varepsilon),
$$

is an isomorphism of groups.

**Proof.** Every unit is $a(1 + s\varepsilon)$ with $a \in R^\times$ and $s = a^{-1}a'$, uniquely, so $\Theta$ is a bijection. It is a homomorphism because

$$
\Theta(a,s)\Theta(c,t) = a(1 + s\varepsilon)\,c(1 + t\varepsilon) = a c\bigl(1 + (s + t)\varepsilon\bigr) = \Theta\bigl(a c,\, s + t\bigr),
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

is split by $a \mapsto a$, and its kernel $1 + \mathrm{M} = \{1 + s\varepsilon\}$ is the **shear group**, isomorphic to $(R, +)$ through $s \mapsto 1 + s\varepsilon$. Over $\mathbb{R}$ the group of units is $\mathbb{R}^\times \times \mathbb{R}$: abelian, two-dimensional, with two contractible components.

### The Norm-One Group

**Definition.** The **norm-one group** is $H = \{A \in \mathbb{D}'_{\mathbb{R}} : N(A) = 1\}$.

**Proposition.** $H = \{a + \varepsilon a' : a = \pm 1\}$ is the union of the two parallel lines of real part $\pm 1$; its identity component is $H_0 = 1 + \mathrm{M}$, the shear group.

**Proof.** $N(a + \varepsilon a') = a^2 = 1$ gives $a = \pm 1$ and leaves $a'$ free; the line $a = 1$ is $1 + \mathrm{M}$, the component through the identity.

## The Three-Way Classification

### The Table

Over a field $k$, combining the criterion for invertibility with the vanishing of the norm, the elements of $\mathbb{D}'_k$ fall into exactly three classes.

| Condition on $N(A)$ | Condition on $A$ | Conclusion |
|---|---|---|
| $N(A) \neq 0$ | (automatically $A \neq 0$) | $A$ is invertible |
| $N(A) = 0$ | $A = 0$ | $A$ is the zero element |
| $N(A) = 0$ | $A \neq 0$ | $A$ is a zero divisor |

The third class is exactly $\mathrm{M} \setminus \{0\}$; its elements are studied in *Dual-Numbers Zero Divisors*, and the ideals that organize the classification are studied in *Dual-Numbers Ideals and the Maximal Ideal*.

### The Algebra Is Not a Division Algebra

By definition, a **division algebra** is an algebra in which every nonzero element is invertible; for a finite-dimensional algebra this is equivalent to the absence of zero divisors. The dual algebra contains the nonzero nilpotent $\varepsilon$, which is a zero divisor; hence $\mathbb{D}'_R$ is **not** a division algebra whenever $\mathrm{M} \neq 0$ (that is, whenever $\varepsilon \neq 0$ in the algebra).

This is in contrast to the Frobenius theorem, which states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. The dual algebra is a two-dimensional commutative associative real algebra, and it is not among them because it is not a field.

## Distribution of the Invertible Elements

The two distinguished submodules of $\mathbb{D}'_R$ behave oppositely with respect to invertibility.

### The Real Submodule

An element of $R_{\mathbb{D}'}$ is $A = a$ with $a' = 0$, and $N(A) = a^2$. Over a field, every nonzero element of $R_{\mathbb{D}'}$ is invertible, and $R_{\mathbb{D}'}$ is a subalgebra isomorphic to the field; it is the unique subalgebra of $\mathbb{D}'_R$ that is a division algebra.

### The Infinitesimal Submodule

An element of $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ is $A = \varepsilon a'$ with $a = 0$, and $N(A) = 0$. Hence **every** element of the infinitesimal submodule is a non-unit; the invertible elements meet $\mathrm{M}$ in the empty set, and the zero divisors are exactly $\mathrm{M} \setminus \{0\}$.

### Summary of the Distribution

Over a field $k$ the distribution is as follows, the units being read off from $R^\times = k^\times$ and the zero-divisor column from the criterion of *Dual-Numbers Zero Divisors*.

| Submodule | Elements | $N$ | Units | Zero divisors |
|---|---|---|---|---|
| $R_{\mathbb{D}'}$ | $a$, $a \in R$ | $a^2$ | all $a \in R^\times$ | none |
| $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ | $\varepsilon a'$, $a' \in R$ | $0$ | none | all $a' \neq 0$ |

The two submodules are the eigenspaces of dual conjugation, and the distribution table is the algebraic statement that the norm is a homomorphism whose kernel is exactly one of the two eigenspaces.

## Relation to the Conjugate Decomposition

The criterion is stated in terms of the norm and the real part. In the conjugate decomposition

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}, \qquad A = a + \varepsilon a',
$$

the norm reads $N(A) = (\operatorname{Re} A)^2$, and invertibility depends only on the component in the real submodule. This is why the group of units is a direct product: the multiplicative structure of $\mathbb{D}'_R$ is that of $R$ on the real submodule, with the infinitesimal submodule carried along as a nilpotent, invisible addition. The biquaternion analogue, in which the four conjugations and their six subspaces control the distribution, is in *Biquaternion Norm and Invertibility*; in the dual algebra only one nontrivial conjugation exists, and the distribution collapses to the two-row table above.

## Comparison with the Split Complex and Biquaternion Cases

The three norms of the family are

$$
N_{\mathbb{C}}(A) = a^2 + a'^2, \qquad N_{\mathbb{D}}(A) = a^2 - a'^2, \qquad N_{\mathbb{D}'}(A) = a^2,
$$

for $\mathbb{C}$, the split complex numbers $\mathbb{D} = \mathbb{R}[j]$ and the dual numbers. They are the three real binary quadratic forms of rank two, two and one respectively: positive-definite, indefinite non-degenerate, and degenerate.

- In $\mathbb{C}$ the norm never vanishes away from the origin, and every nonzero element is a unit; the norm-one group is the circle.
- In the split complex $\mathbb{D}$ the norm is indefinite, its null set is the pair of linear null directions on which the zero divisors live, and the norm-one group is a hyperbola, with two branches.
- In $\mathbb{D}'$ the norm is degenerate, its null set is the maximal ideal, a whole line, and the norm-one group is a pair of parallel lines.

In the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ the norm is complex-valued and multiplicative, and its vanishing locus is the zero-divisor cone, of real codimension two; the invertibility criterion is $N(\tilde{Q}) \neq 0$ and the group of units is $GL(2, \mathbb{C})$. The dual case is the rank-one member of this family: complex, split complex, dual, quaternion, split quaternion, biquaternion, split biquaternion. In every case the criterion for invertibility is the non-vanishing of a single multiplicative form, and the differences among the members lie in the rank, the signature and the value ring of that form.

## Summary

The norm $N(A) = A\bar A = a^2$ of the dual-number algebra is a degenerate multiplicative quadratic form of rank one, depending only on the real part, with radical the maximal ideal $\mathrm{M} = (\varepsilon)$. It fails to be a norm in the analytic sense, and the Euclidean form $a^2 + a'^2$ is the positive-definite but non-multiplicative quantity that carries the topology. The continuous multiplicative real size function on the units, normalised on the real scalars and invariant under the parabolic one-parameter subgroup, is $r(A) = |a| = \sqrt{|N(A)|}$, the multiplicative scale on the units; without the shear-invariance requirement the normalised multiplicative size functions form the one-parameter family $\rho_c = |a|\exp(c\,a'/a)$.

A dual number $A = a + \varepsilon a'$ is invertible if and only if its real part is a unit of $R$; over a field, if and only if $a \neq 0$, equivalently if and only if $N(A) \neq 0$. The inverse is $A^{-1} = a^{-1} - a^{-2}\varepsilon a'$. Over a field the group of units is $\mathbb{D}'_k \setminus \mathrm{M}$; it is the split extension $1 \to (1 + \mathrm{M}) \to (\mathbb{D}'_k)^\times \to k^\times \to 1$, and since $\mathbb{D}'_k$ is commutative the extension is the direct product $k^\times \times (k, +)$ with the shear group $1 + \mathrm{M}$ as second factor. The elements of $\mathbb{D}'_k$ over a field fall into three classes: the invertible elements, the zero element, and the zero divisors $\mathrm{M} \setminus \{0\}$; the algebra is therefore not a division algebra, in contrast to $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. The invertible elements occupy the real submodule and avoid the infinitesimal submodule entirely, and this asymmetry of the two eigenspaces of dual conjugation is the shape the norm imposes on the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $A = a + \varepsilon a'$ | General dual number |
| $a = \operatorname{Re} A$ | Real part |
| $a' = \operatorname{Inf} A$ | Infinitesimal part |
| $\bar{A} = a - \varepsilon a'$ | Dual conjugation |
| $N(A) = A\bar A = a^2$ | Norm, degenerate, radical $\mathrm{M}$ |
| $q(A) = a^2 + a'^2$ | Euclidean form |
| $\langle A, B \rangle = a b + a' b'$ | Euclidean inner product |
| $\|A\|_E = \sqrt{a^2 + a'^2}$ | Euclidean norm |
| $r(A) = |a| = \sqrt{|N(A)|}$ | Continuous multiplicative real size on the units, normalised on the scalars and shear-invariant |
| $\rho_c(A) = |a|\exp(c\,a'/a)$ | The normalised multiplicative size functions; $r = \rho_0$ |
| $\mathrm{M} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$ | Maximal ideal, kernel of $N$ |
| $R_{\mathbb{D}'}$ | Real submodule |
| $(\mathbb{D}'_k)^\times = \mathbb{D}'_k \setminus \mathrm{M}$ | Group of units, over a field $k$ |
| $1 + \mathrm{M}$ | Shear group, kernel of $(\mathbb{D}'_R)^\times \to R^\times$ |
| $\Theta : R^\times \times (R,+) \to (\mathbb{D}'_R)^\times$ | Unit-group isomorphism, $\Theta(a,s) = a(1 + s\varepsilon)$ |
| $H = \{A : N(A) = 1\}$ | Norm-one group, lines $a = \pm 1$ |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395, for the origin of the dual numbers as a degenerate extension.
- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the degeneracy of the dual-number form and its geometry.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for the dual numbers and their degenerate quadratic form alongside the complex and split-complex cases.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the classification of the two-dimensional real algebras by the sign of the square of the generator.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Berlin, 1991), for the theory of degenerate quadratic forms, their radical, and their isometry groups.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, Providence, 2005), for the classification of quadratic forms by their radical.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the complex-valued semi-norm and the unique real norm in the biquaternion case.
