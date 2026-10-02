# __Formally Real Algebras and the Sum of Squares__

## Introduction

A field is **formally real** when $-1$ is not a sum of squares, equivalently when no nontrivial sum of squares vanishes; the classical theorem of Artin and Schreier says that a field is formally real exactly when it carries an ordering, that is, a total order compatible with the field operations. For an algebra with involution the same condition is imposed on the **self-adjoint part**: the involution is formally real when a sum of squares of self-adjoint elements vanishes only trivially. The structure the condition singles out is the **sum of squares** $\Sigma^2 A$, the set of the finite sums $a_1^2+\cdots+a_n^2$; it is closed under addition and under multiplication by squares, and the **preorder** $a\le b \iff b-a \in \Sigma^2 A$ is a partial order precisely when the algebra is formally real. The set of the total orders compatible with the structure is the **real spectrum** $\operatorname{Sper}(A)$, and a formally real field has nonempty real spectrum; a field whose real spectrum has one element and which is real closed is the algebraic model of the real numbers.

The article defines the sum of squares and the preorder it generates, proves that the preorder is a partial order exactly for the formally real algebras, states the Artin–Schreier characterisation for fields and its algebra analogue, and introduces the real spectrum as the set of the orderings carried by the formally real structure. It gives the Jordan case, where the self-adjoint part of a formally real Jordan algebra is the ordered Jordan algebra that the structure theory of Part IV uses, and it exhibits the real and rational fields, the polynomial ring, the real matrix algebras and the spin factor. The order-theoretic and topological theory of the real spectrum, with the spectral spaces and the Positivstellensätze, is the subject of the real algebraic geometry of Part III and of Part IV; this article is the algebraic entry, and it uses no norm, distance or form.

The article assumes *Real Forms and the Descent of an Algebra* for the conjugation, *Jordan Algebras with an Involution* for the self-adjoint part $H(J)$, *Commutative Algebras with an Involution* for the commutative case, *Ordinary and Real Closed Fields* and *Orderings of a Field* for the field theory, and *Jordan Algebras* for the squares. The symmetric algebra with an involution is *The Symmetric Algebra with an Involution*, and the invariants of the symmetric algebra under the involution are *Involution-Invariant Ideals of the Symmetric Algebra*. Throughout, $F$ is a field, $A$ is a unital $R$-algebra with involution $\sigma$, $H(A)$ is its self-adjoint part, and $\Sigma^2 A$ is the set of the sums of squares; no form, norm, length, distance or spectrum of operators occurs.

## Formally Real Fields and Algebras

### The Field Case

**Definition.** A field $F$ is **formally real** when $-1$ is not a sum of squares of elements of $F$, equivalently when the equation $\sum_{i=1}^n x_i^2 = 0$ has only the trivial solution $x_1 = \cdots = x_n = 0$.

**Theorem (Artin–Schreier).** A field $F$ is formally real if and only if it carries an **ordering**, a total order $\le$ with

$$
x\le y \Rightarrow x+z\le y+z, \qquad 0\le x, \ 0\le y \Rightarrow 0\le xy, \qquad 0\le x^2 .
$$

In that case every sum of squares is $\ge 0$, and the ordering is exactly a choice of the signs; the field is **real closed** when it admits one ordering and no proper algebraic extension with the same property, and then every element has a square root or its negative does.

*Proof.* If $F$ is formally real, the set $\Sigma^2 F$ of the sums of squares is a cone containing $1$ and not $-1$, and a maximal cone containing $\Sigma^2F$ and excluding $-1$ (existence by Zorn's lemma) defines an ordering by $x \le y \iff y - x \in P$ for the corresponding positive cone $P$; conversely an ordering has $x^2 \ge 0$ and hence $\sum x_i^2 \ge 0$, so no nontrivial sum vanishes. The real-closed characterisation is the standard maximality statement. $\square$

### The Algebra Case

**Definition.** Let $A$ be a unital algebra with involution $\sigma$ over a field of characteristic not two, and let $H(A)$ be the self-adjoint part. The involution is **formally real** when

$$
\sum_{i=1}^n h_i^2 = 0, \qquad h_i \in H(A) \ \Longrightarrow \ h_1 = \cdots = h_n = 0 .
$$

The algebra is **formally real** when its involution is.

**Proposition.** The condition depends only on $H(A)$: it says that the quadratic map $h\mapsto h^2$ has no nontrivial zero sum on $H(A)$, and it is equivalent to the condition that $-1$ is not a sum of squares in $H(A)$ when $1 \in H(A)$.

*Proof.* If $\sum h_i^2 = 0$ nontrivially then $\sum h_i^2 = 0$, so $(-1)$ is not needed; conversely $-1 = \sum h_i^2$ gives the nontrivial sum $\sum h_i^2 + 1 = 0$ with $1 \in H(A)$. $\square$

**Theorem (the Jordan case).** Let $J$ be a Jordan algebra with a formally real involution $\sigma$, so that $H(J)$ is a Jordan subalgebra. Then $H(J)$ with the restricted product is a formally real Jordan algebra, and the map $h\mapsto h^2$ on $H(J)$ has no nontrivial zero sum; conversely a formally real Jordan algebra $J$ with the identity involution is formally real in this sense.

*Proof.* The self-adjoint part is closed under the Jordan product and the squares $h^2 = h\circ h$ lie in it by the involution property; the two conditions are the same written with the Jordan product. $\square$

## The Sum of Squares

### The Cone of the Sums of Squares

**Definition.** The **sums of squares** of $H(A)$ form the set

$$
\Sigma^2 H(A) = \left\{ \sum_{i=1}^n h_i^2 : n\ge 0, \ h_i \in H(A) \right\},
$$

a subset of $H(A)$ containing $0$ and every square, closed under addition, and closed under multiplication by squares: $h^2\cdot (h')^2 = (hh')^2$.

**Proposition.** $\Sigma^2 H(A)$ is a **cone**: closed under addition and under multiplication by squares, and containing $1$ when the involution fixes the unit; the algebra is formally real exactly when

$$
\Sigma^2 H(A) \cap \bigl(-\Sigma^2 H(A)\bigr) = \{0\} .
$$

*Proof.* Closedness is by the definition of a sum and the multiplicativity of the square; the intersection condition says that a sum of squares and its negative can both be sums of squares only if both are $0$, which is the formal reality read on differences. $\square$

### The Preorder

**Definition.** The **preorder** carried by the involution is

$$
a \le b \iff b - a \in \Sigma^2 H(A) .
$$

It is reflexive and transitive because the sum of two sums of squares is a sum of squares.

**Theorem.** The preorder is a partial order, that is $\le$ is antisymmetric, if and only if the involution is formally real. In that case $h^2 \ge 0$ for every self-adjoint $h$, $1 \ge 0$, and the order is compatible with the addition; it is compatible with the product on the self-adjoint elements under the additional condition that the product of two positive elements is positive, which holds for the commutative formally real algebras and for the Jordan algebras of the self-adjoint part.

*Proof.* Antisymmetry says $a\le b$ and $b\le a$ force $a = b$, that is $b-a\in\Sigma^2$ and $a-b\in\Sigma^2$ force $a = b$; this is the intersection condition. The positivity of the squares is the definition of the cone, and the compatibility with the product is the multiplicativity of the cone under the squares. $\square$

## The Real Spectrum and the Order

### Orderings and the Real Spectrum

**Definition.** An **ordering** of a commutative formally real algebra $A$ is a total order on $H(A)$ extending the preorder generated by the sums of squares and making $H(A)$ an ordered ring; the **real spectrum** is

$$
\operatorname{Sper}(A) = \{\text{orderings of } A\} .
$$

**Theorem.** A commutative formally real algebra has nonempty real spectrum; for a field the orderings of $F$ are in bijection with the maximal cones $P \subseteq F$ with $P\cup(-P) = F$ and $P\cap(-P) = \{0\}$, and the real-closed fields are those with a unique ordering and no proper real extension.

*Proof.* The orderings correspond to the positive cones, which are exactly the maximal cones excluding $-1$; a formally real algebra has such cones by Zorn's lemma as in the field case, hence a nonempty real spectrum. The real-closed statement is the maximality of the ordering. $\square$

**Remark.** The real spectrum carries a topology and a structure sheaf, the real algebraic geometry of Part III; here it is only the set of the orders the formally real structure admits, and no topology and no spectrum of an operator is used.

### The Order Carried by the Self-Adjoint Part

**Corollary.** In a formally real algebra the self-adjoint part $H(A)$ carries a partial order by the sums of squares, the squares are positive, and every sum of squares is positive; the order is **archimedean** when for every $h$ there is an integer $n$ with $h \le n\cdot1$, and the archimedean formally real fields are the subfields of $\mathbb{R}$ by the classical theory of real closed fields.

## Examples

**Example (the rational and real fields).** $\mathbb{R}$ is formally real and real closed: its real spectrum has one point, the usual order, and every sum of squares is positive. $\mathbb{Q}$ is formally real with a unique ordering, the restriction of the order of $\mathbb{R}$; a number field has one ordering for each of its embeddings into $\mathbb{R}$, and the ordering is the pullback of the usual one.

**Example (the polynomial ring).** $A = \mathbb{R}[x]$ is formally real, and its real spectrum has the points corresponding to the real numbers $t$, with the two signs at each point, together with the infinitesimal neighbourhoods; the orderings are the substitutions $x\mapsto t$ with a choice of the sign of a small perturbation. The sum of squares is the cone of the polynomials non-negative on $\mathbb{R}$ when the ordering is the one of the real points, and the question of which non-negative polynomials are sums of squares is Hilbert's seventeenth problem, answered by the Positivstellensätze of Part III.

**Example (the real matrix algebra).** Let $A = M_n(\mathbb{R})$ with the transpose involution $X\mapsto X^{\mathsf{T}}$; the self-adjoint part is the symmetric matrices. A sum of squares of symmetric matrices is a sum of matrices $H_i^2$, and it vanishes only if every $H_i$ vanishes, because the trace of a sum of squares is the sum of the traces of the squares and the trace of the square of a symmetric matrix is a sum of squares of the entries; hence the transpose involution is formally real. The self-adjoint part with the order of the sums of squares is the ordered Jordan algebra of the symmetric matrices, the model of the formally real Jordan algebra that Part IV uses.

*Proof of the matrix case.* For a symmetric matrix $H$ the trace of $H^2$ is $\sum_{i,j}H_{ij}H_{ji} = \sum_{i,j}H_{ij}^2 \ge 0$, and it vanishes only when $H = 0$. If $\sum_i H_i^2 = 0$ with the $H_i$ symmetric, taking the trace gives $\sum_i \mathrm{tr}(H_i^2) = 0$, a sum of non-negative terms, so each $\mathrm{tr}(H_i^2) = 0$ and hence each $H_i = 0$. $\square$

**Example (formally real Jordan algebras).** More generally the self-adjoint part of a formally real algebra with involution is an ordered Jordan algebra, and the finite-dimensional formally real Jordan algebras are the ordered objects of the structure theory of Part IV; the spin factor built in *Jordan Algebras* is the basic instance, and the reality condition on its defining symmetric structure belongs to the forms of Part II.

## Summary

A field is **formally real** when no nontrivial sum of squares vanishes, and by Artin–Schreier this is exactly the existence of an **ordering**. For an algebra with involution the same condition is imposed on the **self-adjoint part** $H(A)$: the sums of squares $\Sigma^2 H(A)$ form a cone, and the **preorder** $a\le b \iff b-a\in\Sigma^2 H(A)$ is a partial order exactly in the formally real case. The **real spectrum** $\operatorname{Sper}(A)$ is the set of the orderings, nonempty for a commutative formally real algebra and a single point for the real-closed fields. The self-adjoint part of a formally real algebra is an ordered Jordan algebra, and the real matrix algebra with the transpose involution and the spin factor are the standard examples; the order-theoretic and topological theory is Part III. No norm, distance or operator spectrum occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sum x_i^2 = 0 \Rightarrow x_i = 0$ | Formal reality |
| $H(A)$ | Self-adjoint part (with respect to $\sigma$) |
| $\Sigma^2 H(A)$ | Cone of the sums of squares |
| $a\le b \iff b-a\in\Sigma^2 H(A)$ | The preorder carried by the involution |
| $\Sigma^2\cap(-\Sigma^2) = \{0\}$ | The preorder is a partial order $=$ formal reality |
| $\operatorname{Sper}(A)$ | Real spectrum, the set of the orderings |
| $P\cup(-P) = F$, $P\cap(-P) = \{0\}$ | Positive cone of an ordering |

## Further Reading

- Serge Lang, *Algebra* (Springer, revised third edition, 2002), for the formally real fields, the orderings and the Artin–Schreier theorem.
- Alexander Prestel and Charles Delzell, *Positive Polynomials* (Springer, 2001), for the real spectrum, the sums of squares and the Positivstellensätze.
- Eberhard Becker, *Valuations and Orderings* (Birkhäuser, 1998), for the cones, the preorders and the formally real algebras.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the formally real Jordan algebras and the ordered self-adjoint part.
- Hel Braun and Max Koecher, *The Jordan Algebra Approach to Bounded Symmetric Domains* (Springer, 1966), for the formally real Jordan algebras and the order of the self-adjoint part.
