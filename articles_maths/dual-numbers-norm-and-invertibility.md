
# __Dual-Numbers Norm and Invertibility__

## Introduction

This article studies the norm of the dual-number algebra and the invertibility of its elements. It follows the base article *Dual-Numbers Algebra*, which fixed the ring $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$, the two conjugations, the two distinguished submodules and the maximal ideal $\mathrm{M} = (\varepsilon)$. The goal here is to define the norm and the Euclidean form, to establish the criterion for invertibility, to describe the group of units and its structure, and to record the three-way classification of the elements.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible, the algebra is $\mathbb{D}'_R$, and $\mathbb{D}$ denotes the split complex algebra $\mathbb{R}[j]$, $j^2 = +1$. A general dual number is written

$$
Z = a + \varepsilon b, \qquad a, b \in R,
$$

with real part $a = \operatorname{Re} Z$ and infinitesimal part $b = \operatorname{Inf} Z$. Dual conjugation is written $\bar{Z} = a - \varepsilon b$ and the identity conjugation $\operatorname{id}(Z) = Z$. When $R = \mathbb{R}$ we write $\mathbb{D}'$ for $\mathbb{D}'_{\mathbb{R}}$, and $\mathrm{M} = \varepsilon\mathbb{R}$ is the maximal ideal. Every numerical value displayed below was recomputed in exact rational arithmetic.

The base is the commutative ring, not the field: the criterion for invertibility is stated for an arbitrary commutative $R$, and the places where a field, or invertibility of $2$, is needed are flagged. The default specialisation for the geometric statements is $R = \mathbb{R}$.

## The Norm

### Definition

**Definition.** The **norm** of a dual number $Z = a + \varepsilon b$ is

$$
N(Z) = Z\bar{Z} = (a + \varepsilon b)(a - \varepsilon b) = a^2.
$$

It is an element of $R$, and it takes its value in the real submodule $R_{\mathbb{D}'}$.

### Basic Properties

**Proposition.** Let $Z = a + \varepsilon b$ and $W = c + \varepsilon d$.

- **Dependence on the real part alone.** $N(Z) = a^2$ does not involve the infinitesimal part $b$; equivalently, $N(Z + \eta) = N(Z)$ for every $\eta \in \mathrm{M}$.
- **Invariance under dual conjugation.** $N(\bar{Z}) = N(Z)$, since $(-b)^2 = b^2$ plays no role and the real part is unchanged.
- **Sign.** Over an ordered ring $R$ the value $a^2$ is non-negative, and $N(Z) = 0$ if and only if $a = 0$.
- **Vanishing locus.** Over a field, $N(Z) = 0$ if and only if $Z \in \mathrm{M} = (\varepsilon)$.

**Proof.** The first two are immediate from $N(Z) = a^2$. For the third, $a^2 \ge 0$ in an ordered ring and $a^2 = 0$ forces $a = 0$ in a domain. For the fourth, $a^2 = 0$ with $a$ in a field gives $a = 0$, that is $Z = \varepsilon b \in \mathrm{M}$.

The norm is **degenerate**: it is a quadratic form of rank one on the two-dimensional free module $\mathbb{D}'_R$, and its radical is the line $\mathrm{M} = \varepsilon R_{\mathbb{D}'}$. Degeneracy in this article always means that the associated bilinear form has nonzero radical, and the radical is the maximal ideal.

### Multiplicativity

**Theorem.** The norm is multiplicative:

$$
N(ZW) = N(Z)\,N(W).
$$

**Proof.** With $Z = a + \varepsilon b$ and $W = c + \varepsilon d$ one has $ZW = a c + (a d + b c)\varepsilon$, so

$$
N(ZW) = (a c)^2 = a^2c^2 = N(Z)N(W).
$$

The identity $(a c)^2 = a^2c^2$ holds in every commutative ring.

**Corollary.** If $N(Z) \neq 0$ and $N(W) \neq 0$, then $N(ZW) \neq 0$.

**Corollary.** If $N(Z) = 0$ or $N(W) = 0$, then $N(ZW) = 0$. In particular the product of an element of the maximal ideal with any dual number lies in the maximal ideal, since $\mathrm{M}$ is a two-sided ideal.

**Remark.** Multiplicativity is the reason for the name, and it survives the degeneracy: the norm is a *ring homomorphism* from $\mathbb{D}'_R$ to the multiplicative monoid of $R$, whose kernel is the maximal ideal. It is the degenerate analogue of the modulus of a complex number.

### The Norm as a Degenerate Form

The word *norm* is used here only in a qualified sense, and it is worth recording which of the usual axioms survive.

- The **sign axiom** holds: $N(-Z) = N(Z)$ over any commutative ring.
- The **triangle inequality** has no content: $N$ takes values in $R$, which carries no order in general, and even over $\mathbb{R}$ the value $N(Z)$ is a square, not a length.
- The **scaling axiom** holds in its quadratic form, $N(\lambda Z) = \lambda^2 N(Z)$ for $\lambda \in R$, and this is the only homogeneity the form has.
- The **non-degeneracy axiom fails**: $N(Z) = 0$ for every nonzero $Z \in \mathrm{M}$.

So the norm is a degenerate multiplicative quadratic form, homogeneous of degree two, whose vanishing locus is the maximal ideal. It fails to be a norm in the analytic sense, and the Euclidean form of the next section supplies that analytic quantity.

### The Reduction of the Scale to $|a|$

There is nevertheless a genuine real size function on the units, singled out by the norm. Let $\rho : (\mathbb{D}'_{\mathbb{R}})^\times \to \mathbb{R}_{>0}$ be a continuous multiplicative function, normalised on the real scalars by

$$
\rho(\lambda) = |\lambda| \qquad \text{for } \lambda \in \mathbb{R}^\times.
$$

**Theorem.** The function

$$
r(Z) = |a| = \sqrt{|N(Z)|}
$$

is a continuous multiplicative real size function on the units, normalised on the real scalars, and it is invariant under the parabolic one-parameter subgroup, $r(Z(1 + t\varepsilon)) = r(Z)$ for every $t \in \mathbb{R}$. It is the unique such function with that invariance.

**Proof.** Multiplicativity is $N(ZW) = N(Z)N(W)$ together with $r = \sqrt{|N|}$, and continuity is the continuity of $a \mapsto |a|$. At a real scalar $\lambda$ one has $r(\lambda) = \sqrt{\lambda^2} = |\lambda|$. For the shear invariance, $Z(1 + t\varepsilon) = a + (b + ta)\varepsilon$ has the same real part $a$, so $r(Z(1 + t\varepsilon)) = |a| = r(Z)$. For uniqueness, by *Shears and Parabolic Rotations* every unit is $a(1 + s\varepsilon)$ with $a \in \mathbb{R}^\times$ and $s = a^{-1}b$; the shear invariance gives $r(a + \varepsilon b) = r(a)$, so $r$ is determined on the whole unit group by its values on the real scalars, and the normalisation fixes those to be $|\cdot|$.

So the multiplicative scale on the units reduces to the absolute value of the real part: on the units the norm supplies a genuine positive scale via $r = \sqrt{|N|}$, and it is the only scale fixed by the shear. The biquaternion article *Biquaternion Norm and Invertibility* proves the analogous statement with $r(\tilde{Q}) = \sqrt{|N(\tilde{Q})|}$; the dual case is the rank-one degeneration of it, in which the square root is the square root of a square.

**Remark (the shear condition is needed).** Invariance under the shear is not automatic, and without it the scale is not unique. For each real $c$, the function

$$
\rho_c(a + \varepsilon b) = |a|\,\exp\!\Bigl(c\,\frac{b}{a}\Bigr)
$$

is continuous on the units, multiplicative because the shear parameter is additive, $\rho_c(ZW) = \rho_c(Z)\rho_c(W)$, and normalised on the real scalars, where $b = 0$. These functions form a one-parameter family with $r = \rho_0$, and $r(Z) = |a|$ is exactly the member that is constant along the orbits of the parallel one-parameter subgroup $1 + \mathrm{M}$. So the reduction of the scale to $|a|$ is the statement that the norm fixes the scale to be blind to the nilpotent direction, which is the analytic face of the degeneracy of the form.

### The Norm from the Two Components

Writing $Z = Z_r + Z_i\varepsilon$ with $Z_r = a$ and $Z_i = b$ in $R$, the norm depends on the two components only through the first:

$$
N(Z) = Z_r^2.
$$

The Euclidean form of the next section is the sum of squares of the two components, and the contrast between the two is the whole content of the degeneracy.

## The Euclidean Form

### Definition

**Definition.** The **Euclidean form** of a dual number is the real quadratic form

$$
q(Z) = a^2 + b^2,
$$

the **Euclidean inner product** of two dual numbers $Z = a + \varepsilon b$ and $W = c + \varepsilon d$ is

$$
\langle Z, W \rangle = a c + b d,
$$

and the **Euclidean norm** is

$$
\|Z\|_E = \sqrt{a^2 + b^2}.
$$

Over $R = \mathbb{R}$ this is the ordinary Euclidean structure of the plane $\mathbb{D}' \cong \mathbb{R}^2$ in dual coordinates.

### Properties

**Proposition.** The Euclidean form is positive-definite over an ordered ring and satisfies $\langle Z, Z \rangle = q(Z)$. It is **not** multiplicative with respect to the dual product:

$$
q(ZW) = (a c)^2 + (a d + b c)^2, \qquad q(Z)q(W) = (a^2 + b^2)(c^2 + d^2),
$$

and the two agree only when $a d + b c = \pm(a c - b d)$, which is not an identity.

**Proof.** Substituting the components of $ZW$ gives the first expression; it is not the product of the two squares, as the example $Z = W = 1 + \varepsilon$ shows: $q(ZW) = q(1 + 2\varepsilon) = 5$ while $q(Z)q(W) = 2 \cdot 2 = 4$.

### Relation Between the Norm and the Euclidean Form

The two forms are distinct and play different roles.

| | Norm $N$ | Euclidean form $q$ |
|---|---|---|
| Value | $a^2$ | $a^2 + b^2$ |
| Multiplicative | yes | no |
| Degenerate | yes, radical $\mathrm{M}$ | no |
| Sign over $\mathbb{R}$ | non-negative | positive-definite |
| Controls | the multiplicative structure | the topology |

The inner product is **not** the real part of $Z\bar{W}$; indeed

$$
Z\bar{W} = (a + \varepsilon b)(c - \varepsilon d) = a c + (b c - a d)\varepsilon, \qquad \operatorname{Re}(Z\bar{W}) = a c,
$$

which is the polarisation of the degenerate norm $N$ and not of the Euclidean form. The distinction between $a c$ and $a c + b d$ is the distinction between the multiplicative and the topological structures on the plane.

## Invertibility

### Definition

**Definition.** A dual number $Z$ is **invertible** if there exists $W$ with $ZW = WZ = 1$. The element $W$, if it exists, is the **inverse** of $Z$ and is denoted $Z^{-1}$.

Since $\mathbb{D}'_R$ is commutative there is no distinction between left, right and two-sided inverses.

### Criterion for Invertibility

**Theorem.** Let $Z = a + \varepsilon b \in \mathbb{D}'_R$. The following are equivalent.

1. $Z$ is invertible.
2. $a$ is a unit of $R$.
3. $N(Z) = a^2$ is a unit of $R$.
4. The residue class of $Z$ in the quotient ring $\mathbb{D}'_R/\mathrm{M} \cong R$ is a unit of $R$.

Over a field, the criterion reads: $Z$ is invertible if and only if $a \neq 0$, that is, if and only if $N(Z) \neq 0$.

**Proof.** If $a \in R^\times$, set $W = a^{-1} - a^{-2}\varepsilon b$. Then

$$
ZW = (a + \varepsilon b)(a^{-1} - a^{-2}\varepsilon b) = a a^{-1} + \bigl(-a^{-1}b + b a^{-1}\bigr)\varepsilon = 1,
$$

so $Z$ is invertible, and (1) follows from (2). Since $a^2 \in R^\times$ exactly when $a \in R^\times$, (2) and (3) are equivalent. Conversely, if $ZW = 1$ for some $W = c + \varepsilon d$, then comparing real parts gives $a c = 1$, so $a \in R^\times$, giving (2) from (1). The equivalence with the residue condition is the definition of $\mathrm{M} = (\varepsilon)$ together with the computation just made. Over a field, $a \in R^\times$ means $a \neq 0$.

### The Inverse Formula

**Corollary.** When $Z$ is invertible,

$$
Z^{-1} = \frac{1}{a} - \frac{b}{a^2}\,\varepsilon.
$$

This is the degeneration of the complex formula $Z^{-1} = \bar{Z}/|Z|^2$: the conjugate is $\bar{Z} = a - \varepsilon b$ and the "modulus squared" is $N(Z) = a^2$, so $\bar{Z}/N(Z) = (a - \varepsilon b)/a^2$, which is the inverse above.

**Corollary.** If $Z$ is invertible then so is $\bar{Z}$, and $\overline{Z^{-1}} = (\bar{Z})^{-1}$.

**Proof.** Direct from the formula.

## The Group of Units

### Definition

**Definition.** The **group of units** of $\mathbb{D}'_R$ is

$$
(\mathbb{D}'_R)^\times = \{a + \varepsilon b : a \in R^\times\}.
$$

It is a group under multiplication with identity $1$.

### Basic Properties

**Proposition.** Over a field, the group of units is the complement of the maximal ideal, $(\mathbb{D}'_k)^\times = \mathbb{D}'_k \setminus \mathrm{M}$, and over $R = \mathbb{R}$ it is an open, dense subset of the plane $\mathbb{D}'$ with exactly two connected components, distinguished by the sign of the real part.

**Proof.** Over a field the complement statement is the invertibility criterion $a \neq 0$. Over a general commutative ring the unit group is the smaller set $\{a + \varepsilon b : a \in R^\times\}$, the preimage of $R^\times$ under $\operatorname{Re}$. Openness and density over $\mathbb{R}$ follow from $\{a \neq 0\}$ being the complement of a line. The map $Z \mapsto \operatorname{sgn}(a)$ is a continuous surjection onto $\{\pm 1\}$ that is multiplicative, so there are at least two components; $\{a > 0\}$ and $\{a < 0\}$ are each homeomorphic to a half-plane and hence connected.

### The Structure as a Semidirect Product

**Theorem.** Let $R$ be a commutative ring with $2$ invertible. The map

$$
\Theta : R^\times \times (R, +) \longrightarrow (\mathbb{D}'_R)^\times, \qquad \Theta(a, s) = a(1 + s\varepsilon),
$$

is an isomorphism of groups.

**Proof.** Every unit is $a(1 + s\varepsilon)$ with $a \in R^\times$ and $s = a^{-1}b$, uniquely, so $\Theta$ is a bijection. It is a homomorphism because

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

**Definition.** The **norm-one group** is $H = \{Z \in \mathbb{D}'_{\mathbb{R}} : N(Z) = 1\}$.

**Proposition.** $H = \{a + \varepsilon b : a = \pm 1\}$ is the union of the two parallel lines of real part $\pm 1$; its identity component is $H_0 = 1 + \mathrm{M}$, the shear group.

**Proof.** $N(a + \varepsilon b) = a^2 = 1$ gives $a = \pm 1$ and leaves $b$ free; the line $a = 1$ is $1 + \mathrm{M}$, the component through the identity.

## The Three-Way Classification

### The Table

Over a field $k$, combining the criterion for invertibility with the vanishing of the norm, the elements of $\mathbb{D}'_k$ fall into exactly three classes.

| Condition on $N(Z)$ | Condition on $Z$ | Conclusion |
|---|---|---|
| $N(Z) \neq 0$ | (automatically $Z \neq 0$) | $Z$ is invertible |
| $N(Z) = 0$ | $Z = 0$ | $Z$ is the zero element |
| $N(Z) = 0$ | $Z \neq 0$ | $Z$ is a zero divisor |

The third class is exactly $\mathrm{M} \setminus \{0\}$; its elements are studied in *Dual-Numbers Zero Divisors*, and the ideals that organize the classification are studied in *Dual-Numbers Ideals and the Maximal Ideal*.

### The Algebra Is Not a Division Algebra

By definition, a **division algebra** is an algebra in which every nonzero element is invertible; for a finite-dimensional algebra this is equivalent to the absence of zero divisors. The dual algebra contains the nonzero nilpotent $\varepsilon$, which is a zero divisor; hence $\mathbb{D}'_R$ is **not** a division algebra whenever $\mathrm{M} \neq 0$ (that is, whenever $\varepsilon \neq 0$ in the algebra).

This is in contrast to the Frobenius theorem, which states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. The dual algebra is a two-dimensional commutative associative real algebra, and it is not among them because it is not a field.

## Distribution of the Invertible Elements

The two distinguished submodules of $\mathbb{D}'_R$ behave oppositely with respect to invertibility.

### The Real Submodule

An element of $R_{\mathbb{D}'}$ is $Z = a$ with $b = 0$, and $N(Z) = a^2$. Over a field, every nonzero element of $R_{\mathbb{D}'}$ is invertible, and $R_{\mathbb{D}'}$ is a subalgebra isomorphic to the field; it is the unique subalgebra of $\mathbb{D}'_R$ that is a division algebra.

### The Infinitesimal Submodule

An element of $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ is $Z = \varepsilon b$ with $a = 0$, and $N(Z) = 0$. Hence **every** element of the infinitesimal submodule is a non-unit; the invertible elements meet $\mathrm{M}$ in the empty set, and the zero divisors are exactly $\mathrm{M} \setminus \{0\}$.

### Summary of the Distribution

Over a field $k$ the distribution is as follows, the units being read off from $R^\times = k^\times$ and the zero-divisor column from the criterion of *Dual-Numbers Zero Divisors*.

| Submodule | Elements | $N$ | Units | Zero divisors |
|---|---|---|---|---|
| $R_{\mathbb{D}'}$ | $a$, $a \in R$ | $a^2$ | all $a \in R^\times$ | none |
| $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ | $\varepsilon b$, $b \in R$ | $0$ | none | all $b \neq 0$ |

The two submodules are the eigenspaces of dual conjugation, and the distribution table is the algebraic statement that the norm is a homomorphism whose kernel is exactly one of the two eigenspaces.

## Relation to the Conjugate Decomposition

The criterion is stated in terms of the norm and the real part. In the conjugate decomposition

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}, \qquad Z = a + \varepsilon b,
$$

the norm reads $N(Z) = (\operatorname{Re} Z)^2$, and invertibility depends only on the component in the real submodule. This is why the group of units is a direct product: the multiplicative structure of $\mathbb{D}'_R$ is that of $R$ on the real submodule, with the infinitesimal submodule carried along as a nilpotent, invisible addition. The biquaternion analogue, in which the four conjugations and their six subspaces control the distribution, is in *Biquaternion Norm and Invertibility*; in the dual algebra only one nontrivial conjugation exists, and the distribution collapses to the two-row table above.

## Comparison with the Split Complex and Biquaternion Cases

The three norms of the family are

$$
N_{\mathbb{C}}(Z) = a^2 + b^2, \qquad N_{\mathbb{D}}(Z) = a^2 - b^2, \qquad N_{\mathbb{D}'}(Z) = a^2,
$$

for $\mathbb{C}$, the split complex numbers $\mathbb{D} = \mathbb{R}[j]$ and the dual numbers. They are the three real binary quadratic forms of rank two, two and one respectively: positive-definite, indefinite non-degenerate, and degenerate.

- In $\mathbb{C}$ the norm never vanishes away from the origin, and every nonzero element is a unit; the norm-one group is the circle.
- In the split complex $\mathbb{D}$ the norm is indefinite, its null set is the pair of linear null directions on which the zero divisors live, and the norm-one group is a hyperbola, with two branches.
- In $\mathbb{D}'$ the norm is degenerate, its null set is the maximal ideal, a whole line, and the norm-one group is a pair of parallel lines.

In the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ the norm is complex-valued and multiplicative, and its vanishing locus is the zero-divisor cone, of real codimension two; the invertibility criterion is $N(\tilde{Q}) \neq 0$ and the group of units is $GL(2, \mathbb{C})$. The dual case is the rank-one member of this family: complex, split complex, dual, quaternion, split quaternion, biquaternion, split biquaternion. In every case the criterion for invertibility is the non-vanishing of a single multiplicative form, and the differences among the members lie in the rank, the signature and the value ring of that form.

## Summary

The norm $N(Z) = Z\bar{Z} = a^2$ of the dual-number algebra is a degenerate multiplicative quadratic form of rank one, depending only on the real part, with radical the maximal ideal $\mathrm{M} = (\varepsilon)$. It fails to be a norm in the analytic sense, and the Euclidean form $a^2 + b^2$ is the positive-definite but non-multiplicative quantity that carries the topology. The continuous multiplicative real size function on the units, normalised on the real scalars and invariant under the parabolic one-parameter subgroup, is $r(Z) = |a| = \sqrt{|N(Z)|}$, the multiplicative scale on the units; without the shear-invariance requirement the normalised multiplicative size functions form the one-parameter family $\rho_c = |a|\exp(c\,b/a)$.

A dual number $Z = a + \varepsilon b$ is invertible if and only if its real part is a unit of $R$; over a field, if and only if $a \neq 0$, equivalently if and only if $N(Z) \neq 0$. The inverse is $Z^{-1} = a^{-1} - a^{-2}\varepsilon b$. Over a field the group of units is $\mathbb{D}'_k \setminus \mathrm{M}$; it is the split extension $1 \to (1 + \mathrm{M}) \to (\mathbb{D}'_k)^\times \to k^\times \to 1$, and since $\mathbb{D}'_k$ is commutative the extension is the direct product $k^\times \times (k, +)$ with the shear group $1 + \mathrm{M}$ as second factor. The elements of $\mathbb{D}'_k$ over a field fall into three classes: the invertible elements, the zero element, and the zero divisors $\mathrm{M} \setminus \{0\}$; the algebra is therefore not a division algebra, in contrast to $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. The invertible elements occupy the real submodule and avoid the infinitesimal submodule entirely, and this asymmetry of the two eigenspaces of dual conjugation is the shape the norm imposes on the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$ | Real part |
| $b = \operatorname{Inf} Z$ | Infinitesimal part |
| $\bar{Z} = a - \varepsilon b$ | Dual conjugation |
| $N(Z) = Z\bar{Z} = a^2$ | Norm, degenerate, radical $\mathrm{M}$ |
| $q(Z) = a^2 + b^2$ | Euclidean form |
| $\langle Z, W \rangle = a c + b d$ | Euclidean inner product |
| $\|Z\|_E = \sqrt{a^2 + b^2}$ | Euclidean norm |
| $r(Z) = |a| = \sqrt{|N(Z)|}$ | Continuous multiplicative real size on the units, normalised on the scalars and shear-invariant |
| $\rho_c(Z) = |a|\exp(c\,b/a)$ | The normalised multiplicative size functions; $r = \rho_0$ |
| $\mathrm{M} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$ | Maximal ideal, kernel of $N$ |
| $R_{\mathbb{D}'}$ | Real submodule |
| $(\mathbb{D}'_k)^\times = \mathbb{D}'_k \setminus \mathrm{M}$ | Group of units, over a field $k$ |
| $1 + \mathrm{M}$ | Shear group, kernel of $(\mathbb{D}'_R)^\times \to R^\times$ |
| $\Theta : R^\times \times (R,+) \to (\mathbb{D}'_R)^\times$ | Unit-group isomorphism, $\Theta(a,s) = a(1 + s\varepsilon)$ |
| $H = \{Z : N(Z) = 1\}$ | Norm-one group, lines $a = \pm 1$ |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395, for the origin of the dual numbers as a degenerate extension.
- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the degeneracy of the dual-number form and its geometry.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for the dual numbers and their degenerate quadratic form alongside the complex and split-complex cases.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the classification of the two-dimensional real algebras by the sign of the square of the generator.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Berlin, 1991), for the theory of degenerate quadratic forms, their radical, and their isometry groups.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, Providence, 2005), for the classification of quadratic forms by their radical.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the complex-valued semi-norm and the unique real norm in the biquaternion case.
