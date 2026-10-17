# __Dual-Numbers Zero Divisors__

## Introduction

This article studies the zero divisors of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$. It follows *Dual-Numbers Algebra*, which fixed the algebra, the two conjugations and the two distinguished submodules, and *Dual-Numbers Ideals and the Maximal Ideal*, which established that over a field the algebra is local with unique maximal ideal $\mathrm{M} = (\varepsilon)$. The goal here is to characterise the zero divisors, to show that they form a single family, and to describe the nilpotent direction on which they live.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is an integral domain in which $2$ is invertible, and the algebra is $\mathbb{D}'_R$; the criterion is sharp over an integral domain, in particular over a field $k$. A general dual number is

$$
Q = q + \varepsilon q', \qquad q, q' \in R,
$$

with $q = \operatorname{Re} Q$ and $q' = \operatorname{Inf} Q$, and dual conjugation is $\bar Q = q - \varepsilon q'$. The two distinguished submodules are $R_{\mathbb{D}'}$ and $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$.

The scope boundaries are these. This article owns the classification of the zero divisors and their distribution. The maximal ideal *as an ideal*, and the Peirce-type decomposition, belong to *Dual-Numbers Ideals and the Maximal Ideal*; the unit criterion and the measure of size belong to *Dual-Numbers Norm and Invertibility*; the position of the zero-divisor set inside the Euclidean plane belongs to *Dual-Numbers Topology*. The zero-divisor set is the maximal ideal with the origin removed, and the ideals article and this one describe the same line from the two sides.

## Definition and Criterion

### Definition

**Definition.** A dual number $Q_1$ is a **zero divisor** if $Q_1 \neq 0$ and there exists a nonzero $Q_2$ with

$$
Q_1 Q_2 = 0.
$$

Because $\mathbb{D}'_R$ is commutative, left and right annihilation coincide and only one equation is needed. The requirement that both $Q_1$ and $Q_2$ be nonzero is essential: the element $0$ is **not** a zero divisor, even though $0 \cdot Q_2 = 0$ for every $Q_2$.

### Criterion

**Theorem.** Let $R$ be an integral domain and let $Q_1 = q_1 + \varepsilon q'_1 \in \mathbb{D}'_R$ be nonzero. Then $Q_1$ is a zero divisor if and only if its real part vanishes:

$$
Q_1 \text{ is a zero divisor} \iff q_1 = 0 \iff Q_1 \in \mathrm{M} \setminus \{0\}.
$$

**Proof.** Suppose $q_1 = 0$, so $Q_1 = \varepsilon q'_1$ with $q'_1 \neq 0$. Then

$$
Q_1 \cdot \varepsilon = \varepsilon q'_1 \cdot \varepsilon = \varepsilon^2 q'_1 = 0
$$

with $\varepsilon \neq 0$, so $Q_1$ is a zero divisor. Conversely, suppose $Q_1 Q_2 = 0$ with $Q_2 = q_2 + \varepsilon q'_2 \neq 0$. The real part of $Q_1 Q_2$ is $q_1 q_2$, so $q_1 q_2 = 0$. If $q_1 \neq 0$ then $q_2 = 0$, since $R$ is a domain; the $\varepsilon$-part is then $q_1 q'_2 + q'_1 q_2 = q_1 q'_2$, which vanishes with $q_1 \neq 0$ and forces $q'_2 = 0$, giving $Q_2 = 0$, a contradiction. Hence $q_1 = 0$.

**Corollary (explicit annihilation).** For $Q_1 = \varepsilon q'_1$ with $q'_1 \neq 0$ the element $Q_2 = \varepsilon$ is a nonzero annihilator, since $\varepsilon q'_1 \cdot \varepsilon = \varepsilon^2 q'_1 = 0$.

**Remark.** The criterion is a condition on the real part alone: a dual number is a zero divisor exactly when it is purely infinitesimal and nonzero. The infinitesimal part is invisible to the criterion. The same set is the vanishing locus of the norm $\langle Q\rangle = q^2$, so that $q = 0$ and $\langle Q\rangle = 0$ agree; the norm is a measure of size rather than an algebraic object, and it is treated in *Dual-Numbers Norm and Invertibility*.

### The Three-Way Classification

Over a field $k$ the elements of $\mathbb{D}'_k$ are partitioned into exactly three classes by the real part.

| Real part | Element | Conclusion |
|---|---|---|
| $q \neq 0$ | — | $Q$ is a unit |
| $q = 0$ | $q' = 0$ | $Q$ is the zero element |
| $q = 0$ | $q' \neq 0$ | $Q$ is a zero divisor |

The third class is exactly $\mathrm{M} \setminus \{0\}$; the ideals that organise the classification are studied in *Dual-Numbers Ideals and the Maximal Ideal*.

### The Algebra Is Not a Division Algebra

A **division algebra** is an algebra in which every nonzero element is invertible; for a finite-dimensional algebra over a field this is equivalent to the absence of zero divisors. The dual algebra contains the nonzero nilpotent $\varepsilon$, so it is not a division algebra. This contrasts with the fields $\mathbb{R}$ and $\mathbb{C}$, in which every nonzero element is invertible.

## The Single Family

### The Zero-Divisor Set

**Definition.** Over an integral domain $R$, the **zero-divisor set** of $\mathbb{D}'_R$ is

$$
\mathcal{Z} = \{Q \in \mathbb{D}'_R : Q \neq 0,\ \operatorname{Re} Q = 0\} = \mathrm{M} \setminus \{0\} = \{\varepsilon q' : q' \in R,\ q' \neq 0\}.
$$

Over a field it is the complement of the units inside the complement of the zero element:

$$
\mathcal{Z} = \mathbb{D}'_k \setminus \bigl(\{0\} \cup (\mathbb{D}'_k)^\times\bigr).
$$

### The Number of Families

An algebra that is a product of two fields has **two** families of zero divisors, one for each factor: a zero divisor is an element with one component zero, and it is killed by the projection onto the other factor. The dual algebra has **one** family, not two. In $\mathbb{D}'_R$ the only idempotents are $0$ and $1$ (by *Dual-Numbers Ideals and the Maximal Ideal*), so there is no nontrivial idempotent to produce a second family. Every zero divisor of $\mathbb{D}'_R$ is of the same kind: a nonzero nilpotent lying in the maximal ideal.

### Why the Second Family Is Not Available

The natural invariant here is the real part $q = \operatorname{Re} Q$, and the criterion is the single condition $q = 0$, not a dichotomy of two nonempty families. The complement of the condition, $q \neq 0$, consists entirely of units over a field; it is not a second zero-divisor family. So the classification collapses to the unit/zero-divisor dichotomy.

## The Nilpotent Direction

### Every Zero Divisor Is Nilpotent

**Theorem.** Every zero divisor of $\mathbb{D}'_R$ is nilpotent, and in fact squares to zero:

$$
Q \in \mathcal{Z} \implies Q^2 = 0.
$$

**Proof.** If $Q = \varepsilon q'$ then $Q^2 = q'^2 \varepsilon^2 = 0$.

So the zero divisors do not merely have a nonzero annihilator; each one is annihilated by itself. This is the *nilpotent direction*: the maximal ideal is a square-zero ideal, and its nonzero elements are the zero divisors.

### The Annihilator

**Definition.** The **annihilator** of a dual number $Q_1$ is

$$
\operatorname{Ann}(Q_1) = \{Q_2 : Q_1 Q_2 = 0\}.
$$

**Proposition.** For every nonzero $Q_1 = \varepsilon q'_1 \in \mathrm{M}$,

$$
\operatorname{Ann}(Q_1) = \mathrm{M} = (\varepsilon),
$$

the maximal ideal itself; the annihilator of a unit is $0$.

**Proof.** For $Q_2 = q_2 + \varepsilon q'_2$ one has $Q_1 Q_2 = q'_1 q_2 \varepsilon$, which vanishes exactly when $q'_1 q_2 = 0$, that is $q_2 = 0$ over an integral domain; so $\operatorname{Ann}(\varepsilon q'_1) = \mathrm{M}$. If $Q_1$ is a unit, $Q_1 Q_2 = 0$ forces $Q_2 = 0$.

**Corollary.** All nonzero zero divisors have the same annihilator, namely the maximal ideal; the annihilator of a zero divisor strictly contains the zero divisor itself, and it is the principal ideal generated by any one of them.

Here the annihilator is a fixed one-dimensional space, independent of which zero divisor is chosen, because every zero divisor lies in the same nilpotent direction.

### The Family Is a Punctured Line

Over $R = \mathbb{R}$ the zero-divisor set is the set of nonzero real multiples of $\varepsilon$,

$$
\mathcal{Z} = \{\varepsilon q' : q' \in \mathbb{R},\ q' \neq 0\} = \varepsilon\mathbb{R} \setminus \{0\}.
$$

It is one-dimensional as a real vector space with the origin removed, it is closed under multiplication by every nonzero real scalar, and it is parameterised bijectively by $\mathbb{R} \setminus \{0\}$. Its position as a subset of the Euclidean plane is established in *Dual-Numbers Topology*.

## The Relation to the Projections

### No Nontrivial Idempotents

**Proposition.** Let $R$ be connected (for instance an integral domain or a field). Then the idempotents of $\mathbb{D}'_R$ are exactly $0$ and $1$. In particular no zero divisor is idempotent, and no zero divisor is a nonzero multiple of a nontrivial idempotent.

**Proof.** Write $Q = q + \varepsilon q'$. From $Q^2 = Q$ one gets $q^2 = q$ and $2 q q' = q'$; connectedness gives $q = 0$ or $q = 1$. If $q = 0$ then $q' = 0$, giving $Q = 0$; if $q = 1$ then $q' = 0$ (since $2$ is invertible), giving $Q = 1$. Neither is a zero divisor.

### What Stands In for the Idempotent Classification

In an algebra that is a product of two fields the zero divisors are the nonzero multiples of the nontrivial idempotents, so the classification of the zero divisors is the classification of the idempotents. In $\mathbb{D}'_R$ there are no nontrivial idempotents, so the corresponding classification is empty, and the zero divisors are labelled instead by the single nonzero scalar: $\mathcal{Z} = \{\varepsilon q' : q' \neq 0\}$. The projection that survives is the conjugation projection

$$
Q \mapsto \operatorname{Inf}(Q)\,\varepsilon = \tfrac{1}{2}(Q - \bar Q) \in \varepsilon R_{\mathbb{D}'},
$$

which is the analogue of the Peirce projection but is associated to the involution rather than to an idempotent. Every zero divisor is the image of itself under this projection, and the image of a unit is its infinitesimal part, an element of $\mathrm{M}$ that is *not* a zero divisor unless the real part vanishes. So the projection does not map onto the zero divisors, and it does not classify them.

## Distribution of the Zero Divisors

The two distinguished submodules behave oppositely.

### The Real Submodule

An element of $R_{\mathbb{D}'}$ is $Q = q$ with real part $q$; it is nonzero whenever $q \neq 0$, so $R_{\mathbb{D}'}$ contains **no** zero divisors. Over a field every nonzero element of $R_{\mathbb{D}'}$ is a unit, reflecting that $R_{\mathbb{D}'}$ is a copy of the field and is the unique subalgebra of $\mathbb{D}'_R$ that is a division algebra.

### The Infinitesimal Submodule

An element of $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ is $Q = \varepsilon q'$ with real part $0$; every nonzero element of the infinitesimal submodule is a zero divisor. So the zero-divisor set is the punctured infinitesimal submodule:

$$
\mathcal{Z} = \varepsilon R_{\mathbb{D}'} \setminus \{0\}.
$$

### Summary of the Distribution

| Submodule | Elements | Real part | Zero divisors |
|---|---|---|---|
| $R_{\mathbb{D}'}$ | $q$, $q \in R$ | $q$ | none |
| $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ | $\varepsilon q'$, $q' \in R$ | $0$ | all $q' \neq 0$ |

So the zero divisors are concentrated in one of the two eigenspaces of dual conjugation and absent from the other. There is no intermediate distribution: every zero divisor lies in the single infinitesimal submodule.

## Comparison with the Split Complex Case

The comparison is the one with the split complex numbers, in which the family count is read from the idempotent structure.

**Split complex $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$.** The algebra has the two nontrivial idempotents

$$
\pi_{1,2} = \tfrac{1}{2}(1 \pm j), \qquad \pi_1 \pi_2 = 0, \qquad \pi_1 + \pi_2 = 1,
$$

giving the decomposition $\mathbb{D} = \mathbb{R}\pi_1 \oplus \mathbb{R}\pi_2$ into a product of two copies of $\mathbb{R}$. The zero divisors are the nonzero elements of the two ideals $\mathbb{D}\pi_1$ and $\mathbb{D}\pi_2$, so there are **two** families, one per idempotent; each family is the nonzero part of a one-dimensional ideal. The dual algebra is the contraction of this picture: the two idempotents coalesce into the single idempotent $1$, the decomposition into a product of two fields degenerates into the local ring with a square-zero maximal ideal, and the two families coalesce into one.

So the number of families is the number of independent ways of being a zero divisor: two for an algebra that is a product of two fields, and one for an algebra that is local with a square-zero maximal ideal. The dual-number algebra is the member of the family with a single zero-divisor family, and the reason is the local square-zero structure of its maximal ideal: it has no nontrivial idempotent to split it.

## Summary

Over an integral domain $R$ (in particular over a field $k$), a nonzero dual number $Q = q + \varepsilon q'$ is a zero divisor if and only if its real part vanishes, so the zero-divisor set is the punctured maximal ideal,

$$
\mathcal{Z} = \mathrm{M} \setminus \{0\} = \{\varepsilon q' : q' \neq 0\}.
$$

The zero divisors form a **single family**, against the two families of an algebra that is a product of two fields, such as the split complex numbers. The reason is that $\mathbb{D}'_R$ has no nontrivial idempotent — so the idempotent classification that produces the second family elsewhere is empty — and that its maximal ideal is square-zero. Every zero divisor is nilpotent, in fact squares to zero, and lies in the nilpotent direction of the maximal ideal; the annihilator of every nonzero zero divisor is the same space, namely $\mathrm{M}$, and the zero divisor generates that annihilator. The relation to the projections is through the conjugation projection onto $\varepsilon R_{\mathbb{D}'}$ rather than through any idempotent. Of the two distinguished submodules, $R_{\mathbb{D}'}$ contains no zero divisors and $\varepsilon R_{\mathbb{D}'}$ consists entirely of them, and there is no generic zero divisor outside the distinguished subspaces. The position of $\mathcal{Z}$ as a subset of the plane is the subject of *Dual-Numbers Topology*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $Q = q + \varepsilon q'$ | General dual number |
| $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$ | Real and infinitesimal parts |
| $\bar{Q} = q - \varepsilon q'$ | Dual conjugation |
| $\mathrm{M} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$ | Maximal ideal, square-zero |
| $R_{\mathbb{D}'}$, $\varepsilon R_{\mathbb{D}'}$ | Real and infinitesimal submodules |
| $\mathcal{Z} = \mathrm{M} \setminus \{0\}$ | Zero-divisor set, a single family |
| $\operatorname{Ann}(Q)$ | Annihilator of $Q$; equals $\mathrm{M}$ for $Q \in \mathcal{Z}$ |
| $\pi_{1,2} = \tfrac{1}{2}(1 \pm j)$ | The idempotents of the split complex algebra, two zero-divisor families |
| $\mathbb{D} = \mathbb{R}[j]$ | Split complex algebra, two families of zero divisors |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the dual numbers as an infinitesimal extension and the geometry of their radical.
- Michael F. Atiyah and Ian G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, Reading, 1969), for local rings, nilpotent ideals and the maximal ideal.
