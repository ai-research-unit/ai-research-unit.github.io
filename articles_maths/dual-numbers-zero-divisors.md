
# __Dual-Numbers Zero Divisors__

## Introduction

This article studies the zero divisors of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$. It follows *Dual-Numbers Norm and Invertibility*, which established the norm form $N(Z) = a^2$ and the criterion for invertibility, and *Dual-Numbers Ideals and the Maximal Ideal*, which established that over a field the algebra is local with unique proper nonzero ideal $\mathfrak{m} = (\varepsilon)$. The goal here is to characterize the zero divisors, to show that they form a single family, and to describe the nilpotent direction on which they live.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible, and the algebra is $\mathbb{D}'_R$; the zero-divisor criterion is proved for an integral domain $R$ and is sharp there (in particular for a field $k$), and the geometric specialisation is $R = \mathbb{R}$. A general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in R,
$$

with $a = \operatorname{Re} Z$ and $b = \operatorname{Inf} Z$, dual conjugation is $\bar{Z} = a - \varepsilon b$, the norm form is $N(Z) = Z\bar{Z} = a^2$, and $\mathfrak{m} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$ is the maximal ideal. The two distinguished submodules are $R_{\mathbb{D}'}$ and $\varepsilon R_{\mathbb{D}'}$.

The scope boundaries are these. This article owns the classification of the zero divisors and their distribution. The ideals, the Peirce-type decomposition and the maximal ideal *as an ideal* belong to *Dual-Numbers Ideals and the Maximal Ideal*; the norm form and the unit criterion belong to *Dual-Numbers Norm and Invertibility*. The maximal ideal is the same object as the zero-divisor set with the origin removed, and the two articles describe the same line from the two sides.

## Definition and Criterion

### Definition

**Definition.** A dual number $Z$ is a **zero divisor** if it is nonzero and there exists a nonzero dual number $W$ such that

$$
zw = 0.
$$

Because $\mathbb{D}'_R$ is commutative, left and right annihilation coincide, and only one equation is needed. The requirement that both $Z$ and $W$ be nonzero is essential: the element $0$ is **not** a zero divisor, even though $0 \cdot W = 0$ for every $W$.

### Criterion

**Theorem.** Let $R$ be an integral domain and let $Z = a + \varepsilon b \in \mathbb{D}'_R$ be nonzero. Then $Z$ is a zero divisor if and only if its norm form vanishes, equivalently if and only if its real part vanishes:

$$
Z \text{ is a zero divisor} \iff N(Z) = 0 \iff a = 0 \iff Z \in \mathfrak{m} \setminus \{0\}.
$$

**Proof.** Suppose $Z \neq 0$ and $N(Z) = a^2 = 0$. In a domain this gives $a = 0$, so $Z = \varepsilon b$ with $b \neq 0$; then $Z \cdot \varepsilon = \varepsilon b^2 = 0$, and $\varepsilon \neq 0$, so $Z$ is a zero divisor. Conversely, suppose that $Z$ is a zero divisor, so that $zw = 0$ for some $W = c + \varepsilon d \neq 0$. The real part of $zw$ is $a c$, so $a c = 0$; if $a \neq 0$ then $c = 0$ because $R$ is a domain, and then the $\varepsilon$-part $a d + b c = a d$ vanishes with $a \neq 0$, forcing $d = 0$ and hence $W = 0$, a contradiction. Therefore $a = 0$, and over a domain the equivalence with $N(Z) = 0$ is the identity $N(Z) = a^2$. $\square$

**Corollary (the explicit annihilation).** For $Z = \varepsilon b$ with $b \neq 0$, the element $W = \varepsilon$ is a nonzero annihilator, since $\varepsilon b \cdot \varepsilon = \varepsilon b^2 = 0$.

**Remark.** The criterion makes the zero-divisor condition a condition on the *real part* alone: a dual number is a zero divisor exactly when it is purely infinitesimal and nonzero. The infinitesimal part is invisible to the criterion, as it is invisible to the norm form.

### The Three-Way Classification

Over a field $k$, combining the invertibility criterion with the vanishing criterion, the elements of $\mathbb{D}'_k$ are partitioned into three classes:

| Condition on $N(Z)$ | Condition on $Z$ | Conclusion |
|---|---|---|
| $N(Z) \neq 0$ | (automatically $Z \neq 0$) | $Z$ is invertible |
| $N(Z) = 0$ | $Z = 0$ | $Z$ is the zero element |
| $N(Z) = 0$ | $Z \neq 0$ | $Z$ is a zero divisor |

The zero divisors are exactly the nonzero elements on which the norm form vanishes, and they are exactly the nonzero elements of the maximal ideal.

### The Algebra Is Not a Division Algebra

A **division algebra** is an algebra in which every nonzero element is invertible; for a finite-dimensional algebra over a field this is equivalent to the absence of zero divisors. The dual algebra contains the nonzero nilpotent $\varepsilon$, so it is not a division algebra. This contrasts with the Frobenius theorem, which states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$.

## The Single Family

### The Zero-Divisor Set

**Definition.** Over an integral domain $R$, the **zero-divisor set** of $\mathbb{D}'_R$ is

$$
\mathcal{Z} = \{Z \in \mathbb{D}'_R : Z \neq 0,\; N(Z) = 0\} = \mathfrak{m} \setminus \{0\}.
$$

Over a field it is the complement of the units inside the complement of the zero element:

$$
\mathcal{Z} = \mathbb{D}'_R \setminus \bigl(\{0\} \cup (\mathbb{D}'_R)^\times\bigr).
$$

### Compared with the Two Families of $\mathbb{B}$

In the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the zero divisors split into **two** families, distinguished by the vanishing of the scalar part: the *pure* zero divisors, which are the nonzero nilpotents of the vector subspace and satisfy $\tilde{Q}^2 = 0$, and the *non-pure* zero divisors, which have nonzero scalar part and are the nonzero complex multiples of the nontrivial idempotents, satisfying $\tilde{Q}^2 = 2Q_0\tilde{Q}$. The two families are disjoint and of different complex dimension. The organization of that classification is the article *Biquaternion Zero Divisors*.

The dual algebra has **one** family, not two. The reason is structural: the biquaternion invariant that separates the two families is the scalar part $Q_0$, and the nontrivial idempotents it produces are what make the non-pure family possible. In $\mathbb{D}'_R$ the only idempotents are $0$ and $1$ (by *Dual-Numbers Ideals and the Maximal Ideal*), so there is no nontrivial idempotent to multiply, and no second family. Every zero divisor of $\mathbb{D}'_R$ is of the same kind: a nonzero nilpotent lying in the maximal ideal.

### Why the Split Is Not Available

The scalar part is unavailable as an invariant here in the sense that separates families. The natural invariant is the real part $a = \operatorname{Re} Z$, and the criterion is $a = 0$; this is a single condition, not a dichotomy of two nonempty families. The complement of the condition, $a \neq 0$, consists entirely of units, not of a second zero-divisor family. So the two-way split of the biquaternion case collapses to the unit/zero-divisor dichotomy.

## The Nilpotent Direction

### Every Zero Divisor Is Nilpotent

**Theorem.** Every zero divisor of $\mathbb{D}'_R$ is nilpotent, and in fact squares to zero:

$$
Z \in \mathcal{Z} \implies Z^2 = 0, \qquad Z \in \mathfrak{m} \implies Z^2 = 0.
$$

**Proof.** If $Z = \varepsilon b$ then $Z^2 = b^2\varepsilon^2 = 0$. $\square$

So the zero divisors do not merely have a nonzero annihilator; each one is annihilated by itself. This is the *nilpotent direction*: the maximal ideal is a square-zero ideal, and its nonzero elements are the zero divisors.

### The Annihilator

**Definition.** The **annihilator** of a dual number $Z$ is $\operatorname{Ann}(Z) = \{W : zw = 0\}$.

**Proposition.** For every nonzero $Z = \varepsilon b \in \mathfrak{m}$,

$$
\operatorname{Ann}(Z) = \mathfrak{m} = (\varepsilon),
$$

the maximal ideal itself; the annihilator of a unit is $0$.

**Proof.** For $W = c + \varepsilon d$, $zw = b \varepsilon c$, which vanishes exactly when $b c = 0$, that is $c = 0$ over an integral domain; so $\operatorname{Ann}(\varepsilon b) = \mathfrak{m}$. If $Z$ is a unit, $zw = 0$ forces $W = 0$. $\square$

**Corollary.** All nonzero zero divisors have the same annihilator, namely the maximal ideal; the annihilator of a zero divisor strictly contains the zero divisor itself, and it is the principal ideal generated by any one of them.

This is the sharpest contrast with the biquaternion pure case, where the annihilator of a pure zero divisor is a cone over a line and contains the whole complex line through $\tilde{Q}$, and with the non-pure case, where the annihilator contains $\tilde{Q} - 2Q_0$. Here the annihilator is a fixed one-dimensional space, independent of which zero divisor is chosen.

### The Family Is a Line Minus a Point

Over $R = \mathbb{R}$ the zero-divisor set is

$$
\mathcal{Z} = \{\varepsilon b : b \in \mathbb{R},\; b \neq 0\},
$$

the punctured line $\varepsilon\mathbb{R} \setminus \{0\}$ in the dual plane. It is a one-dimensional real submanifold with two connected components, the two open rays $b > 0$ and $b < 0$. It is neither open nor closed in the plane: its closure is the whole line $\mathfrak{m}$, and its complement is dense.

## The Relation to the Norm Form

The zero divisors are the vanishing locus of the norm form, with the origin removed. The norm form $N : \mathbb{D}'_R \to R$, $N(Z) = a^2$, is a polynomial map, and

$$
\mathcal{Z} = N^{-1}(0) \setminus \{0\} = \mathfrak{m} \setminus \{0\}.
$$

Since $N$ depends only on the real part, its zero fibre is a full line and not a pair of points or a cone of higher dimension. In the language of quadratic forms, the zero-divisor set is the **radical** $\operatorname{rad}(N) = \mathfrak{m}$ of the degenerate form, punctured at the origin: the form loses its non-degenerate directions, and the lost directions are exactly the zero divisors.

**Remark (the norm form vanishes on a subspace, not on a cone).** Over the split complex numbers the norm form $a^2 - b^2$ is indefinite and non-degenerate, and its zero set is the union of the two null lines $a = \pm b$, each a closed one-dimensional cone. Over the dual numbers the zero set is the single line $a = 0$, and it is the radical of the form rather than a union of null directions. The distinction is the distinction between a zero divisor that is *isotropic but off-radical* (split complex) and a zero divisor that is *radical* (dual).

### The Multiplicativity and the Annihilator

Multiplicativity, $N(zw) = N(Z)N(W)$, forces the zero-divisor set to be closed under multiplication by arbitrary elements: if $N(Z) = 0$ then $N(zw) = 0$ for all $W$. This is the ideal property of $\mathfrak{m}$ read through the norm form.

## The Relation to the Projections

### No Nontrivial Idempotents

**Proposition.** Let $R$ be connected (for instance an integral domain or a field). Then the idempotents of $\mathbb{D}'_R$ are exactly $0$ and $1$. In particular no zero divisor is idempotent, and no zero divisor is a nonzero multiple of a nontrivial idempotent.

**Proof.** Write $Z = a + \varepsilon b$. From $Z^2 = Z$ one gets $a^2 = a$ and $2a b = b$; connectedness gives $a = 0$ or $a = 1$. If $a = 0$ then $b = 0$, giving $Z = 0$; if $a = 1$ then $b = 0$ (since $2$ is invertible), giving $Z = 1$. Both are units or zero, not zero divisors. $\square$

### What Stands In for the Idempotent Classification

In the biquaternion algebra the non-pure zero divisors are exactly the nonzero complex multiples of the nontrivial idempotents, so the classification of the zero divisors is the classification of the idempotents, which in turn is the classification of the roots of $-1$. In $\mathbb{D}'_R$ there are no nontrivial idempotents, so the corresponding classification is empty, and the zero divisors are instead labelled by the single nonzero scalar: $\mathcal{Z} = \{\varepsilon b : b \neq 0\}$. The "projection" that survives is the conjugation projection

$$
Z \mapsto \operatorname{Inf}(Z)\,\varepsilon = \tfrac{1}{2}(Z - \bar{Z}) \in \varepsilon R_{\mathbb{D}'},
$$

which is the analogue of the Peirce projection but is associated to the involution, not to an idempotent. Every zero divisor is the image of itself under this projection, and the image of a unit is its infinitesimal part, an element of $\mathfrak{m}$ that is *not* a zero divisor (unless the real part vanishes). So the projection does not map onto the zero divisors, and it does not classify them.

## Distribution of the Zero Divisors

The two distinguished submodules behave oppositely.

### The Real Submodule

An element of $R_{\mathbb{D}'}$ is $Z = a$, and $N(Z) = a^2$, which vanishes only at $Z = 0$. So the real submodule contains **no** zero divisors: every nonzero element of $R_{\mathbb{D}'}$ is a unit when $R$ is a field, reflecting that $R_{\mathbb{D}'}$ is a copy of the field.

### The Infinitesimal Submodule

An element of $\varepsilon R_{\mathbb{D}'} = \mathfrak{m}$ is $Z = \varepsilon b$, and $N(Z) = 0$; every nonzero element of the infinitesimal submodule is a zero divisor. So the zero-divisor set is the punctured infinitesimal submodule:

$$
\mathcal{Z} = \varepsilon R_{\mathbb{D}'} \setminus \{0\}.
$$

### Summary of the Distribution

| Submodule | Elements | $N$ | Zero divisors |
|---|---|---|---|
| $R_{\mathbb{D}'}$ | $a$, $a \in R$ | $a^2$ | none |
| $\varepsilon R_{\mathbb{D}'} = \mathfrak{m}$ | $\varepsilon b$, $b \in R$ | $0$ | all $b \neq 0$ |

So the zero divisors are concentrated in one of the two eigenspaces of dual conjugation and absent from the other. There is no intermediate distribution: unlike the biquaternion case, where the zero divisors are spread over six distinguished subspaces with dimensions ranging over three, four and six, and a generic zero divisor lies in none of them, here every zero divisor lies in the single infinitesimal submodule.

## The Zero Divisor Set

### Basic Properties

**Proposition.** Over $R = \mathbb{R}$ the zero-divisor set $\mathcal{Z} = \mathfrak{m} \setminus \{0\}$ has the following properties.

- It is **not closed**: it is the closed line $\mathfrak{m}$ with its apex removed.
- It is **not open**: every neighbourhood of a point of $\mathcal{Z}$ meets the units.
- It is a **cone**: if $Z \in \mathcal{Z}$ and $\lambda \in \mathbb{R} \setminus \{0\}$ then $\lambda Z \in \mathcal{Z}$, because $N(\lambda Z) = \lambda^2 N(Z) = 0$.
- It has **real dimension one**, and two connected components.

**Proof.** The closure of a punctured line is the line; a punctured line has empty interior; homogeneity is clear; the dimension and the component count are read off from $\mathcal{Z} = \{\varepsilon b : b \neq 0\}$. $\square$

### Dimension

The zero-divisor set has real dimension one in the two-dimensional algebra, so it has real codimension one. The biquaternion zero-divisor set has real dimension six in the eight-dimensional algebra, with real codimension two, because it is cut out by two real equations. The rank drop of the norm form from two (split complex) to one (dual) is what lowers the codimension to one and makes the vanishing locus a line rather than a cone.

### The Boundary of the Unit Group

Over $\mathbb{R}$ the group of units $(\mathbb{D}')^\times = \mathbb{D}' \setminus \mathfrak{m}$ is open and dense in the plane, and its boundary is the maximal ideal $\mathfrak{m}$. The zero-divisor set $\mathcal{Z} = \mathfrak{m} \setminus \{0\}$ is that boundary with the origin removed, so the zero divisors are exactly the nonzero elements at which the norm form vanishes. The maximal ideal is the closure of $\mathcal{Z}$, namely the boundary together with the origin.

## Comparison with the Split Complex and Split Biquaternion Cases

Three comparisons complete the picture.

**Split complex $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$.** The norm form $N(a + j b) = a^2 - b^2$ is non-degenerate and indefinite. Its zero set is the union of the two null lines $a = \pm b$, and the zero divisors are the nonzero elements of those two lines; equivalently they are the nonzero elements of the two ideals generated by the idempotents $\Pi_\pm = \frac{1}{2}(1 \pm j)$. So $\mathbb{D}$ has **two** families of zero divisors, indexed by the two idempotents, and both are isotropic but off-radical, since the form is non-degenerate. The dual algebra is the contraction of this picture: the two null lines coalesce into the radical line, the two idempotents coalesce into the single idempotent $1$, and the two families coalesce into one.

**Split biquaternion $\mathbb{H}_{\mathbb{D}}$, $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$.** The algebra is a product of two copies of the quaternion division algebra, and its zero divisors are the nonzero elements with one component zero: the union of the two ideals $\mathbb{H} \oplus 0$ and $0 \oplus \mathbb{H}$. So there are again **two** families, one per simple factor; the zero divisors are the elements killed by one of the two ring projections. The dual algebra, being local with a single minimal ideal rather than a product of two fields-like factors, has only one such family.

**Biquaternion $\mathbb{B}$, $\mathbb{B} \cong M_2(\mathbb{C})$.** The zero divisors split by the scalar part into the pure nilpotents and the non-pure multiples of idempotents, again **two** families.

In each case the number of families is the number of independent ways of being a zero divisor: two for an algebra that is a product of two factors or carries a non-degenerate indefinite form, one for an algebra that is local with a square-zero maximal ideal. The dual-number algebra is the unique member of the family with a single zero-divisor family, and the reason is the degeneracy of its norm form: the norm form has rank one, its radical is a line, and the whole punctured radical is the zero-divisor set.

## Summary

Over an integral domain $R$ (in particular over a field), a nonzero dual number $Z = a + \varepsilon b$ is a zero divisor if and only if its norm form vanishes, that is, if and only if its real part vanishes: the zero-divisor set is the punctured maximal ideal,

$$
\mathcal{Z} = \mathfrak{m} \setminus \{0\} = \{\varepsilon b : b \neq 0\}.
$$

The zero divisors form a **single family**, against the two families of the biquaternion algebra, the split complex algebra and the split biquaternion algebra; the reason is that $\mathbb{D}'_R$ has no nontrivial idempotent, so the idempotent classification that produces the second family in the other cases is empty. Every zero divisor is nilpotent, in fact squares to zero, and lies in the nilpotent direction of the maximal ideal; the annihilator of every nonzero zero divisor is the same space, namely $\mathfrak{m}$, and the zero divisor is its own annihilator's generator. The relation to the norm form is that the zero-divisor set is the radical of the degenerate form, punctured; the relation to the projections is through the conjugation projection onto $\varepsilon R_{\mathbb{D}'}$ rather than through any idempotent. Of the two distinguished submodules, $R_{\mathbb{D}'}$ contains no zero divisors and $\varepsilon R_{\mathbb{D}'}$ consists entirely of them; there is no generic zero divisor outside the distinguished subspaces, in contrast to the biquaternion case. Over $\mathbb{R}$ the set $\mathcal{Z}$ is a punctured line, of real dimension one and real codimension one, neither open nor closed, and it is the boundary of the group of units with the origin removed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $\bar{Z} = a - \varepsilon b$ | Dual conjugation |
| $N(Z) = Z\bar{Z} = a^2$ | Norm form, degenerate, radical $\mathfrak{m}$ |
| $\mathfrak{m} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$ | Maximal ideal |
| $R_{\mathbb{D}'}$, $\varepsilon R_{\mathbb{D}'}$ | Real and infinitesimal submodules |
| $\mathcal{Z} = \mathfrak{m} \setminus \{0\}$ | Zero-divisor set, a single family |
| $\operatorname{Ann}(Z)$ | Annihilator of $Z$; equals $\mathfrak{m}$ for $Z \in \mathcal{Z}$ |
| $\mathbb{B}$ | Biquaternion algebra, two families of zero divisors |
| $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ | Split biquaternions, two families |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original appearance of nilpotents and zero divisors in hypercomplex algebra.
- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the dual numbers as an infinitesimal extension and the geometry of their radical.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the two-family classification in the biquaternion case.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Berlin, 1991), for the radical of a degenerate quadratic form and its isotropic subspaces.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the classification of the two-dimensional real algebras and their zero divisors.
