# __Dual-Numbers Zero Divisors__

## Introduction

This article studies the zero divisors of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$. It follows *Dual-Numbers Algebra*, which fixed the algebra, the two conjugations and the two distinguished submodules, and *Dual-Numbers Ideals and the Maximal Ideal*, which established that over a field the algebra is local with unique maximal ideal $\mathrm{M} = (\varepsilon)$. The goal here is to characterise the zero divisors, to show that they form a single family, and to describe the nilpotent direction on which they live.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is an integral domain in which $2$ is invertible, and the algebra is $\mathbb{D}'_R$; the criterion is sharp over an integral domain, in particular over a field $k$. A general dual number is

$$
A = a + \varepsilon a', \qquad a, a' \in R,
$$

with $a = \operatorname{Re} A$ and $a' = \operatorname{Inf} A$, and dual conjugation is $\bar A = a - \varepsilon a'$. The two distinguished submodules are $R_{\mathbb{D}'}$ and $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$.

The scope boundaries are these. This article owns the classification of the zero divisors and their distribution. The maximal ideal *as an ideal*, and the Peirce-type decomposition, belong to *Dual-Numbers Ideals and the Maximal Ideal*; the unit criterion and the measure of size belong to *Dual-Numbers Norm and Invertibility*; the position of the zero-divisor set inside the Euclidean plane belongs to *Dual-Numbers Topology*. The zero-divisor set is the maximal ideal with the origin removed, and the ideals article and this one describe the same line from the two sides.

## Definition and Criterion

### Definition

**Definition.** A dual number $A$ is a **zero divisor** if $A \neq 0$ and there exists a nonzero $B$ with

$$
A B = 0.
$$

Because $\mathbb{D}'_R$ is commutative, left and right annihilation coincide and only one equation is needed. The requirement that both $A$ and $B$ be nonzero is essential: the element $0$ is **not** a zero divisor, even though $0 \cdot B = 0$ for every $B$.

### Criterion

**Theorem.** Let $R$ be an integral domain and let $A = a + \varepsilon a' \in \mathbb{D}'_R$ be nonzero. Then $A$ is a zero divisor if and only if its real part vanishes:

$$
A \text{ is a zero divisor} \iff a = 0 \iff A \in \mathrm{M} \setminus \{0\}.
$$

**Proof.** Suppose $a = 0$, so $A = \varepsilon a'$ with $a' \neq 0$. Then

$$
A \cdot \varepsilon = \varepsilon a' \cdot \varepsilon = \varepsilon^2 a' = 0
$$

with $\varepsilon \neq 0$, so $A$ is a zero divisor. Conversely, suppose $A B = 0$ with $B = b + \varepsilon b' \neq 0$. The real part of $A B$ is $a b$, so $a b = 0$. If $a \neq 0$ then $b = 0$, since $R$ is a domain; the $\varepsilon$-part is then $a b' + a' b = a b'$, which vanishes with $a \neq 0$ and forces $b' = 0$, giving $B = 0$, a contradiction. Hence $a = 0$.

**Corollary (explicit annihilation).** For $A = \varepsilon a'$ with $a' \neq 0$ the element $B = \varepsilon$ is a nonzero annihilator, since $\varepsilon a' \cdot \varepsilon = \varepsilon^2 a' = 0$.

**Remark.** The criterion is a condition on the real part alone: a dual number is a zero divisor exactly when it is purely infinitesimal and nonzero. The infinitesimal part is invisible to the criterion. The same set is the vanishing locus of the norm $N(A) = a^2$, so that $a = 0$ and $N(A) = 0$ agree; the norm is a measure of size rather than an algebraic object, and it is treated in *Dual-Numbers Norm and Invertibility*.

### The Three-Way Classification

Over a field $k$ the elements of $\mathbb{D}'_k$ are partitioned into exactly three classes by the real part.

| Real part | Element | Conclusion |
|---|---|---|
| $a \neq 0$ | — | $A$ is a unit |
| $a = 0$ | $a' = 0$ | $A$ is the zero element |
| $a = 0$ | $a' \neq 0$ | $A$ is a zero divisor |

The third class is exactly $\mathrm{M} \setminus \{0\}$; the ideals that organise the classification are studied in *Dual-Numbers Ideals and the Maximal Ideal*.

### The Algebra Is Not a Division Algebra

A **division algebra** is an algebra in which every nonzero element is invertible; for a finite-dimensional algebra over a field this is equivalent to the absence of zero divisors. The dual algebra contains the nonzero nilpotent $\varepsilon$, so it is not a division algebra. This contrasts with the Frobenius theorem, which states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$.

## The Single Family

### The Zero-Divisor Set

**Definition.** Over an integral domain $R$, the **zero-divisor set** of $\mathbb{D}'_R$ is

$$
\mathcal{Z} = \{A \in \mathbb{D}'_R : A \neq 0,\ \operatorname{Re} A = 0\} = \mathrm{M} \setminus \{0\} = \{\varepsilon a' : a' \in R,\ a' \neq 0\}.
$$

Over a field it is the complement of the units inside the complement of the zero element:

$$
\mathcal{Z} = \mathbb{D}'_k \setminus \bigl(\{0\} \cup (\mathbb{D}'_k)^\times\bigr).
$$

### Compared with the Two Families of $\mathbb{B}$

In the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the zero divisors split into **two** families, distinguished by the vanishing of the scalar part: the *pure* zero divisors, which are the nonzero nilpotents of the vector subspace and satisfy $\tilde{Q}^2 = 0$, and the *non-pure* zero divisors, which have nonzero scalar part and are the nonzero complex multiples of the nontrivial idempotents, satisfying $\tilde{Q}^2 = 2Q_0\tilde{Q}$. The two families are disjoint and of different complex dimension. The organisation of that classification is the article *Biquaternion Zero Divisors*.

The dual algebra has **one** family, not two. The reason is structural: the biquaternion invariant that separates the two families is the scalar part $Q_0$, and the nontrivial idempotents it produces are what make the non-pure family possible. In $\mathbb{D}'_R$ the only idempotents are $0$ and $1$ (by *Dual-Numbers Ideals and the Maximal Ideal*), so there is no nontrivial idempotent to multiply, and no second family. Every zero divisor of $\mathbb{D}'_R$ is of the same kind: a nonzero nilpotent lying in the maximal ideal.

### Why the Split Is Not Available

The scalar part is unavailable as an invariant that separates families. The natural invariant here is the real part $a = \operatorname{Re} A$, and the criterion is the single condition $a = 0$, not a dichotomy of two nonempty families. The complement of the condition, $a \neq 0$, consists entirely of units over a field; it is not a second zero-divisor family. So the two-way split of the biquaternion case collapses to the unit/zero-divisor dichotomy.

## The Nilpotent Direction

### Every Zero Divisor Is Nilpotent

**Theorem.** Every zero divisor of $\mathbb{D}'_R$ is nilpotent, and in fact squares to zero:

$$
A \in \mathcal{Z} \implies A^2 = 0.
$$

**Proof.** If $A = \varepsilon a'$ then $A^2 = a'^2 \varepsilon^2 = 0$.

So the zero divisors do not merely have a nonzero annihilator; each one is annihilated by itself. This is the *nilpotent direction*: the maximal ideal is a square-zero ideal, and its nonzero elements are the zero divisors.

### The Annihilator

**Definition.** The **annihilator** of a dual number $A$ is

$$
\operatorname{Ann}(A) = \{B : A B = 0\}.
$$

**Proposition.** For every nonzero $A = \varepsilon a' \in \mathrm{M}$,

$$
\operatorname{Ann}(A) = \mathrm{M} = (\varepsilon),
$$

the maximal ideal itself; the annihilator of a unit is $0$.

**Proof.** For $B = b + \varepsilon b'$ one has $A B = a' b \varepsilon$, which vanishes exactly when $a' b = 0$, that is $b = 0$ over an integral domain; so $\operatorname{Ann}(\varepsilon a') = \mathrm{M}$. If $A$ is a unit, $A B = 0$ forces $B = 0$.

**Corollary.** All nonzero zero divisors have the same annihilator, namely the maximal ideal; the annihilator of a zero divisor strictly contains the zero divisor itself, and it is the principal ideal generated by any one of them.

This is the sharpest contrast with the biquaternion pure case, where the annihilator of a pure zero divisor is a cone over a line and contains the whole complex line through $\tilde{Q}$, and with the non-pure case, where the annihilator contains $\tilde{Q} - 2Q_0$. Here the annihilator is a fixed one-dimensional space, independent of which zero divisor is chosen.

### The Family Is a Punctured Line

Over $R = \mathbb{R}$ the zero-divisor set is the set of nonzero real multiples of $\varepsilon$,

$$
\mathcal{Z} = \{\varepsilon a' : a' \in \mathbb{R},\ a' \neq 0\} = \varepsilon\mathbb{R} \setminus \{0\}.
$$

It is one-dimensional as a real vector space with the origin removed, it is closed under multiplication by every nonzero real scalar, and it is parameterised bijectively by $\mathbb{R} \setminus \{0\}$. Its position as a subset of the Euclidean plane is established in *Dual-Numbers Topology*.

## The Relation to the Projections

### No Nontrivial Idempotents

**Proposition.** Let $R$ be connected (for instance an integral domain or a field). Then the idempotents of $\mathbb{D}'_R$ are exactly $0$ and $1$. In particular no zero divisor is idempotent, and no zero divisor is a nonzero multiple of a nontrivial idempotent.

**Proof.** Write $A = a + \varepsilon a'$. From $A^2 = A$ one gets $a^2 = a$ and $2 a a' = a'$; connectedness gives $a = 0$ or $a = 1$. If $a = 0$ then $a' = 0$, giving $A = 0$; if $a = 1$ then $a' = 0$ (since $2$ is invertible), giving $A = 1$. Neither is a zero divisor.

### What Stands In for the Idempotent Classification

In the biquaternion algebra the non-pure zero divisors are exactly the nonzero complex multiples of the nontrivial idempotents, so the classification of the zero divisors is the classification of the idempotents, which in turn is the classification of the roots of $-1$. In $\mathbb{D}'_R$ there are no nontrivial idempotents, so the corresponding classification is empty, and the zero divisors are labelled instead by the single nonzero scalar: $\mathcal{Z} = \{\varepsilon a' : a' \neq 0\}$. The projection that survives is the conjugation projection

$$
A \mapsto \operatorname{Inf}(A)\,\varepsilon = \tfrac{1}{2}(A - \bar A) \in \varepsilon R_{\mathbb{D}'},
$$

which is the analogue of the Peirce projection but is associated to the involution rather than to an idempotent. Every zero divisor is the image of itself under this projection, and the image of a unit is its infinitesimal part, an element of $\mathrm{M}$ that is *not* a zero divisor unless the real part vanishes. So the projection does not map onto the zero divisors, and it does not classify them.

## Distribution of the Zero Divisors

The two distinguished submodules behave oppositely.

### The Real Submodule

An element of $R_{\mathbb{D}'}$ is $A = a$ with real part $a$; it is nonzero whenever $a \neq 0$, so $R_{\mathbb{D}'}$ contains **no** zero divisors. Over a field every nonzero element of $R_{\mathbb{D}'}$ is a unit, reflecting that $R_{\mathbb{D}'}$ is a copy of the field and is the unique subalgebra of $\mathbb{D}'_R$ that is a division algebra.

### The Infinitesimal Submodule

An element of $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ is $A = \varepsilon a'$ with real part $0$; every nonzero element of the infinitesimal submodule is a zero divisor. So the zero-divisor set is the punctured infinitesimal submodule:

$$
\mathcal{Z} = \varepsilon R_{\mathbb{D}'} \setminus \{0\}.
$$

### Summary of the Distribution

| Submodule | Elements | Real part | Zero divisors |
|---|---|---|---|
| $R_{\mathbb{D}'}$ | $a$, $a \in R$ | $a$ | none |
| $\varepsilon R_{\mathbb{D}'} = \mathrm{M}$ | $\varepsilon a'$, $a' \in R$ | $0$ | all $a' \neq 0$ |

So the zero divisors are concentrated in one of the two eigenspaces of dual conjugation and absent from the other. There is no intermediate distribution: unlike the biquaternion case, where the zero divisors are spread over remarkable subspaces of dimensions three, four and six and a generic zero divisor lies in none of them, here every zero divisor lies in the single infinitesimal submodule.

## Comparison with the Split Complex and Split Biquaternion Cases

Three comparisons complete the picture, and in each the family count is read from the idempotent structure.

**Split complex $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$.** The algebra has the two nontrivial idempotents

$$
\pi_\pm = \tfrac{1}{2}(1 \pm j), \qquad \pi_+ \pi_- = 0, \qquad \pi_+ + \pi_- = 1,
$$

giving the decomposition $\mathbb{D} = \mathbb{R}\pi_+ \oplus \mathbb{R}\pi_-$ into a product of two copies of $\mathbb{R}$. The zero divisors are the nonzero elements of the two ideals $\mathbb{D}\pi_+$ and $\mathbb{D}\pi_-$, so there are **two** families, one per idempotent; each family is the nonzero part of a one-dimensional ideal. The dual algebra is the contraction of this picture: the two idempotents coalesce into the single idempotent $1$, the decomposition into a product of two fields degenerates into the local ring with a square-zero maximal ideal, and the two families coalesce into one.

**Split biquaternion $\mathbb{H}_{\mathbb{D}}$, $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$.** The algebra is a product of two copies of the quaternion division algebra, and its zero divisors are the nonzero elements with one component zero: the union of the two ideals $\mathbb{H} \oplus 0$ and $0 \oplus \mathbb{H}$. So there are again **two** families, one per simple factor; a zero divisor is killed by one of the two ring projections. The dual algebra, being local with a single minimal ideal rather than a product of two division factors, has only one such family.

**Biquaternion $\mathbb{B}$, $\mathbb{B} \cong M_2(\mathbb{C})$.** The zero divisors split by the scalar part into the pure nilpotents and the non-pure multiples of idempotents, again **two** families.

In each case the number of families is the number of independent ways of being a zero divisor: two for an algebra that is a product of two factors, or that carries a non-degenerate indefinite form whose null set is a pair of lines, and one for an algebra that is local with a square-zero maximal ideal. The dual-number algebra is the member of the family with a single zero-divisor family, and the reason is the local square-zero structure of its maximal ideal: it has no nontrivial idempotent to split it.

## Summary

Over an integral domain $R$ (in particular over a field $k$), a nonzero dual number $A = a + \varepsilon a'$ is a zero divisor if and only if its real part vanishes, so the zero-divisor set is the punctured maximal ideal,

$$
\mathcal{Z} = \mathrm{M} \setminus \{0\} = \{\varepsilon a' : a' \neq 0\}.
$$

The zero divisors form a **single family**, against the two families of the biquaternion algebra, the split complex algebra and the split biquaternion algebra. The reason is that $\mathbb{D}'_R$ has no nontrivial idempotent — so the idempotent classification that produces the second family elsewhere is empty — and that its maximal ideal is square-zero. Every zero divisor is nilpotent, in fact squares to zero, and lies in the nilpotent direction of the maximal ideal; the annihilator of every nonzero zero divisor is the same space, namely $\mathrm{M}$, and the zero divisor generates that annihilator. The relation to the projections is through the conjugation projection onto $\varepsilon R_{\mathbb{D}'}$ rather than through any idempotent. Of the two distinguished submodules, $R_{\mathbb{D}'}$ contains no zero divisors and $\varepsilon R_{\mathbb{D}'}$ consists entirely of them, and there is no generic zero divisor outside the distinguished subspaces, in contrast to the biquaternion case. The position of $\mathcal{Z}$ as a subset of the plane is the subject of *Dual-Numbers Topology*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $A = a + \varepsilon a'$ | General dual number |
| $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$ | Real and infinitesimal parts |
| $\bar{A} = a - \varepsilon a'$ | Dual conjugation |
| $\mathrm{M} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$ | Maximal ideal, square-zero |
| $R_{\mathbb{D}'}$, $\varepsilon R_{\mathbb{D}'}$ | Real and infinitesimal submodules |
| $\mathcal{Z} = \mathrm{M} \setminus \{0\}$ | Zero-divisor set, a single family |
| $\operatorname{Ann}(A)$ | Annihilator of $A$; equals $\mathrm{M}$ for $A \in \mathcal{Z}$ |
| $\pi_\pm = \tfrac{1}{2}(1 \pm j)$ | The idempotents of the split complex algebra, two zero-divisor families |
| $\mathbb{B}$ | Biquaternion algebra, two families of zero divisors |
| $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ | Split biquaternions, two families |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original appearance of nilpotents and zero divisors in hypercomplex algebra.
- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the dual numbers as an infinitesimal extension and the geometry of their radical.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the two-family classification in the biquaternion case.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- Michael F. Atiyah and Ian G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, Reading, 1969), for local rings, nilpotent ideals and the maximal ideal.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the classification of the two-dimensional real algebras and their zero divisors.
