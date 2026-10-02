
# __The Skew Field of a Ring with Involution__

## Introduction

For a ring $A$ with an involution $\sigma$ the **skew elements** are those with $\sigma(x) = -x$, and they stand against the **symmetric** elements, the fixed ones. When $2$ is invertible the two sets are the eigenspaces of $\sigma$ for $-1$ and $+1$, and they decompose the ring, $A = \mathrm{Sym}(A,\sigma)\oplus\mathrm{Skew}(A,\sigma)$; what makes the pair interesting is that the two sets do not multiply among themselves in the naive way and that, with the commutator and the anti-commutator, they form exactly the two halves of a graded Lie structure. The word **skew field** in the title names this set of skew elements; it is not a division ring, and the collision with the established meaning of the phrase is flagged and avoided below, where the set is written $\mathrm{Skew}(A,\sigma)$.

This article reads the skew elements against the symmetric ones, computes the products of two skew elements (their anti-commutator is symmetric and their commutator skew), records the resulting graded Lie and Jordan structure, and derives the vanishing of a trace on the skew elements for a trace-preserving involution. It assumes *Involutive Rings* for the involution, the fixed set and the eigenspace decomposition, and *Lie Algebras* and *Jordan Algebras* only as the names of the structures that the products suggest, since those categories come later in this Part. Throughout, $A$ is a ring with $1 \neq 0$, $\sigma$ is an involution, $2$ is invertible in $A$ when the eigenspace decomposition is used, and

$$
\mathrm{Sym}(A,\sigma) = \{x : \sigma(x) = x\}, \qquad \mathrm{Skew}(A,\sigma) = \{x : \sigma(x) = -x\}.
$$

## The Two Eigenspaces

**Proposition.** $\mathrm{Sym}(A,\sigma)$ and $\mathrm{Skew}(A,\sigma)$ are additive subgroups of $A$, they intersect in $\{0\}$, and for $2$ invertible

$$
A = \mathrm{Sym}(A,\sigma)\oplus\mathrm{Skew}(A,\sigma), \qquad x = \tfrac12(x+\sigma(x)) + \tfrac12(x-\sigma(x)).
$$

An element is symmetric and skew at once exactly when $2x = 0$; in particular the intersection is trivial in characteristic not two and equals $\{x : 2x = 0\}$ in general.

**Proof.** This is the eigenspace decomposition of the order-two additive map $\sigma$ of *Involutive Rings*: the sum of the two projections is the identity, each projection lands in the named set, and an element in both satisfies $x = -x$.

**Remark (the name).** The set $\mathrm{Skew}(A,\sigma)$ is not a field or a division ring, and the phrase "skew field" is used here in the sense of "the skew elements" only. To avoid the collision with the standard meaning, the article writes $\mathrm{Skew}(A,\sigma)$ throughout and never calls it a field.

## The Products

**Proposition.** For homogeneous $x, y$ the symmetry of a product is governed by the parities:

$$
\mathrm{Sym}\cdot\mathrm{Sym}\subseteq\mathrm{Sym} \iff \text{the factors commute}, \qquad \mathrm{Sym}\cdot\mathrm{Skew}\subseteq\mathrm{Skew} \iff \text{the factors commute},
$$

and the two products of a symmetric and a skew element have a fixed behaviour through the commutator and the anti-commutator, not through the product itself.

**Proof.** For $x, y$ symmetric, $\sigma(xy) = \sigma(y)\sigma(x) = yx$, which equals $xy$ exactly when they commute. For $x$ symmetric and $y$ skew, $\sigma(xy) = \sigma(y)\sigma(x) = -yx$, which equals $-xy$, the skew condition, exactly when $yx = xy$.

**Theorem (the commutator and the anti-commutator).** For all homogeneous pairs the following hold with no commutativity hypothesis:

$$
[x,y] = xy-yx \in \mathrm{Skew} \ \text{if } x, y \in \mathrm{Skew}, \qquad [x,y] \in \mathrm{Sym} \ \text{if } x \in \mathrm{Sym},\ y \in \mathrm{Skew},
$$

$$
\{x,y\} = xy+yx \in \mathrm{Sym} \ \text{if } x, y \in \mathrm{Skew}, \qquad \{x,y\} \in \mathrm{Skew} \ \text{if } x \in \mathrm{Sym},\ y \in \mathrm{Skew} .
$$

In particular $\mathrm{Skew}(A,\sigma)$ is closed under the commutator and is a **Lie subalgebra** of $A$ under $[x,y] = xy-yx$, while $\mathrm{Sym}(A,\sigma)$ is closed under the anti-commutator and is a **Jordan subalgebra** under $x\circ y = xy+yx$.

**Proof.** In each case apply $\sigma$ to the combination. For skew $x, y$: $\sigma(xy-yx) = \sigma(y)\sigma(x)-\sigma(x)\sigma(y) = (-y)(-x)-(-x)(-y) = yx-xy = -(xy-yx)$, so the commutator is skew; and $\sigma(xy+yx) = yx+xy$, so the anti-commutator is symmetric. For symmetric $x$ and skew $y$: $\sigma(xy-yx) = (-y)x-x(-y) = -yx+xy = xy-yx$, symmetric; and $\sigma(xy+yx) = -yx-xy = -(xy+yx)$, skew. The closure statements are the two rows.

**Corollary (the graded structure).** With $\mathrm{Sym}$ in even parity and $\mathrm{Skew}$ in odd parity, the two brackets $[\,,\,]$ and $\{\,,\,\}$ make $A$ a graded Lie-and-Jordan structure: the bracket of two even or two odd elements is odd, the bracket of an even and an odd element is even, the anti-commutator of two odd or of an even and an odd element is odd, and the anti-commutator of two even elements is even. This is the sign structure recorded in *Superalgebras and Graded Structures*, read on the symmetric and the skew parts rather than on a $\mathbb{Z}/2$-grading of the ring.

## The Trace

**Definition.** A **trace** on $A$ is an additive map $\tau : A \to k$ into a commutative ring $k$ with $\tau(ab) = \tau(ba)$ for all $a, b$. It is **$\sigma$-invariant** when $\tau(\sigma(a)) = \tau(a)$.

**Proposition.** Let $\tau$ be a $\sigma$-invariant trace and let $2$ be invertible in $A$ and in $k$. Then

$$
\tau(\mathrm{Skew}(A,\sigma)) = 0, \qquad \tau\bigl(\mathrm{Sym}(A,\sigma)\cdot\mathrm{Skew}(A,\sigma)\bigr) = 0 .
$$

**Proof.** For skew $x$ one has $\tau(x) = \tau(\sigma(x)) = \tau(-x) = -\tau(x)$, so $2\tau(x) = 0$ and $\tau(x) = 0$. For symmetric $x$ and skew $y$, $\tau(xy) = \tau(\sigma(xy)) = \tau(\sigma(y)\sigma(x)) = \tau((-y)x) = -\tau(yx) = -\tau(xy)$, so again $2\tau(xy) = 0$.

**Corollary.** For the matrix ring $M_n(k)$ with the transpose and $\tau = $ the matrix trace, which is invariant under the transpose, the skew-symmetric matrices have trace zero and the product of a symmetric and a skew matrix has trace zero; the latter is the orthogonality of the symmetric and the skew parts under the trace pairing $(X,Y)\mapsto \operatorname{tr}(XY)$. The same computation gives the vanishing of the trace on the pure quaternions for the conjugation of the quaternion algebra and on the odd part of a graded matrix algebra with the graded trace.

## Examples

**(a) The transpose.** In $M_n(k)$ with the transpose the skew elements are the skew-symmetric matrices and the symmetric elements the symmetric matrices; the commutator of two skew-symmetric matrices is skew-symmetric, the anti-commutator is symmetric, and the trace vanishes on the skew part. For $n = 3$ the skew-symmetric matrices have dimension $3$ and form, under the commutator and the identification with $k^3$, the cross-product Lie algebra.

**(b) The quaternion conjugation.** In the quaternion algebra $\mathbb{H}$ over $\mathbb{R}$ with the conjugation the symmetric part is the real line and the skew part is the space of pure quaternions; the commutator of two pure quaternions is pure, $[i,j] = 2k$, and the anti-commutator is real, $\{i,j\} = 0$, so the pure quaternions form a three-dimensional Lie algebra.

**(c) The group ring.** In $K[G]$ with the standard involution the skew elements are those with $a_g = -\sigma(a_{g^{-1}})$, and the commutator of two of them is skew; for a finite group the symmetric part contains the inversion-stable class sums, as in *Involutions of a Group Ring*.

**(d) A noncommutative failure.** In $M_2(F)$ with the transpose the symmetric matrices $\begin{pmatrix}1&1\\1&0\end{pmatrix}$ and $\begin{pmatrix}0&1\\1&1\end{pmatrix}$ have a non-symmetric product, so $\mathrm{Sym}$ is not closed under multiplication; the closure is restored by the anti-commutator of the theorem.

## Summary

For an involution $\sigma$ of a ring $A$ with $2$ invertible, the symmetric and the skew elements are the eigenspaces and $A = \mathrm{Sym}(A,\sigma)\oplus\mathrm{Skew}(A,\sigma)$; the two sets meet in $\{x : 2x = 0\}$ and the word **skew field** names the set of skew elements and not a division ring. The product of two elements is governed by the commutator and the anti-commutator rather than by the product itself: for two skew elements the commutator is skew and the anti-commutator is symmetric, for a symmetric and a skew element the commutator is symmetric and the anti-commutator is skew, so that $\mathrm{Skew}(A,\sigma)$ is a **Lie subalgebra** under $[x,y] = xy-yx$ and $\mathrm{Sym}(A,\sigma)$ is a **Jordan subalgebra** under $x\circ y = xy+yx$, the two forming the halves of a graded structure. A $\sigma$-invariant trace vanishes on the skew elements and on every product of a symmetric and a skew element, so for the transpose the symmetric and the skew matrices are orthogonal under the trace pairing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | Involution of the ring $A$ |
| $\mathrm{Sym}(A,\sigma)$ | Fixed elements; the $+1$ eigenspace of $\sigma$ |
| $\mathrm{Skew}(A,\sigma)$ | Skew elements $\{x : \sigma(x) = -x\}$; the $-1$ eigenspace |
| $A = \mathrm{Sym}\oplus\mathrm{Skew}$ | Eigenspace decomposition, $2$ invertible |
| $[x,y] = xy-yx$ | Commutator; makes $\mathrm{Skew}$ a Lie subalgebra |
| $\{x,y\} = xy+yx$ | Anti-commutator; makes $\mathrm{Sym}$ a Jordan subalgebra |
| $[\,\mathrm{Sym},\mathrm{Skew}\,]\subseteq\mathrm{Sym}$ | Graded Lie structure |
| $\{\mathrm{Sym},\mathrm{Skew}\}\subseteq\mathrm{Skew}$ | Graded Jordan structure |
| $\tau$, $\sigma$-invariant trace | $\tau(ab) = \tau(ba)$, $\tau(\sigma(a)) = \tau(a)$ |
| $\tau(\mathrm{Skew}) = 0$, $\tau(\mathrm{Sym}\cdot\mathrm{Skew}) = 0$ | Vanishing of the trace, $2$ invertible |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and skew elements, their products and the trace conditions.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the Lie structure of the skew elements and the Jordan structure of the symmetric ones.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan product $x\circ y = xy+yx$ and the symmetric part of an associative algebra.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for traces, the trace pairing and the graded structures of an algebra with involution.
