
# __The Order Projection__

## Introduction

An **order projection** is a positive operator that is idempotent and dominated by the identity. In an arbitrary ordered vector space such an operator is only an algebraic curiosity; in a **Riesz space** — an ordered vector space in which every pair of elements has a least upper bound — it is a structural invariant with a canonical description: the range of an order projection is a **band**, the projections are in bijection with the bands, and two bands give a direct sum decomposition

$$
E = B\oplus B^{\perp}, \qquad x = P_B x + (I - P_B)x,
$$

that refines the order and is recovered from it. This article introduces the Riesz space, the lattice terms that come with it, the ideals and the bands, and the order projections, and it proves the Riesz decomposition theorem that every band of a Dedekind complete Riesz space is a **projection band**. The order projections of such a space form a Boolean algebra, and that algebra is the order-theoretic counterpart of the algebra of idempotents of a function space.

Riesz spaces are the structure the whole of the previous part of this category has been approaching without assuming: the Riesz–Kantorovich theorem of *Positive Operators on an Ordered Space*, the lattice condition in the Choquet–Meyer theorem of *Cones, Extremal Rays and the Choquet Theory*, and the existence of the modulus of an operator are all statements about Riesz spaces, and they are all proved here, in the special form the corpus needs. The order and the order topology are *Ordered Vector Spaces and the Order Unit*; the positive operators, the cone and the operator order are *Positive Operators on an Ordered Space* and *The Cone of Positive Operators*; the extreme points and the Choquet theory are *Cones, Extremal Rays and the Choquet Theory*; and the lattice as an abstract object is *Order Theory and Lattices*. The normed theory of a Riesz space — its lattice norms, its completeness and the bands of a $C(X)$ under the supremum norm — is not entered here, and the topology that makes the norm available is *Locally Convex Spaces* and *Normed and Banach Spaces* of Part II; the order projections of an operator algebra are *Operator Algebras* and are not used here.

## Riesz Spaces

### Definition and Lattice Identities

**Definition.** A **Riesz space**, or **vector lattice**, is an ordered vector space $E$ in which every pair $x,y$ has a least upper bound $x\vee y$ and a greatest lower bound $x\wedge y$. The **absolute value** and the **positive and negative parts** are

$$
\lvert x\rvert = x\vee(-x), \qquad x^+ = x\vee0, \qquad x^- = (-x)\vee0 .
$$

**Proposition (the lattice operations are compatible with the linear structure).** In a Riesz space, for all $x,y,z$ and every scalar $\lambda\geq0$,

$$
(x+z)\vee(y+z) = (x\vee y) + z, \qquad (\lambda x)\vee(\lambda y) = \lambda(x\vee y), \qquad x\vee y + x\wedge y = x + y .
$$

*Proof.* For the first, $(x\vee y)+z$ is an upper bound of $x+z$ and $y+z$, and if $w$ is any upper bound of those then $w - z$ is an upper bound of $x$ and $y$, so $w - z\geq x\vee y$. The second is the translation invariance applied to the positive scaling, which preserves the order. For the third, both sides are handled by the identity $x\vee y = \tfrac12(x+y+\lvert x - y\rvert)$, which follows from the first two identities applied after showing that $u\vee v = \tfrac12(u+v+\lvert u-v\rvert)$ for $u = x-y$ and $v = 0$.

**Proposition (the absolute value).** For every $x$, the three elements $x^+$, $x^-$ and $\lvert x\rvert$ satisfy

$$
x = x^+ - x^-, \qquad \lvert x\rvert = x^+ + x^-, \qquad x^+\wedge x^- = 0, \qquad x^+\vee x^- = \lvert x\rvert .
$$

*Proof.* From $x\vee0 - ((-x)\vee0) = x\vee0 + x\wedge0 = x$ by the third identity above, giving the first; adding gives the second by the same identity applied to $x$ and $-x$. For the third, $x^+\wedge x^- = (x\vee0)\wedge(-x\vee0) = 0$ because the two arguments cannot both exceed zero; the fourth is the definition.

**Proposition (the triangle inequality).** For all $x,y$ and every scalar $\lambda$,

$$
\lvert x+y\rvert\leq\lvert x\rvert + \lvert y\rvert, \qquad \lvert\lambda x\rvert = \lvert\lambda\rvert\,\lvert x\rvert, \qquad \bigl\lvert\lvert x\rvert - \lvert y\rvert\bigr\rvert\leq\lvert x-y\rvert .
$$

*Proof.* $\pm x\leq\lvert x\rvert$ and $\pm y\leq\lvert y\rvert$ give $\pm(x+y)\leq\lvert x\rvert+\lvert y\rvert$, which is the first; the second is the homogeneity of the lattice operations; the third is the first applied to $x = (x-y)+y$ and to $y$, in both directions.

**Definition.** Two elements $x,y$ are **disjoint**, written $x\perp y$, when $\lvert x\rvert\wedge\lvert y\rvert = 0$. A subset $A$ is disjoint from a set $D$ when every element of $A$ is disjoint from every element of $D$.

**Proposition (disjointness and addition).** Disjointness is symmetric and compatible with the lattice: if $x\perp y$ then $\lvert x+y\rvert = \lvert x\rvert + \lvert y\rvert$, and if additionally $\lvert u\rvert\leq\lvert x\rvert$ then $u\perp y$.

*Proof.* For the absolute value, $\lvert x+y\rvert\leq\lvert x\rvert+\lvert y\rvert$ always; the reverse inequality is $x+y = (x^+-x^-)+(y^+-y^-)$ with the four terms of disjoint support, and the lattice identity of the first proposition gives $\lvert x+y\rvert = x^++x^-+y^++y^-$ when the supports separate. The second statement is the definition of the order interval in the lattice.

### Ideals and Bands

**Definition.** An **order ideal** is a linear subspace $I\subseteq E$ with the interval property: if $y\in I$ and $\lvert x\rvert\leq\lvert y\rvert$ then $x\in I$. A **band** is an order ideal $B$ closed under existing suprema: if $D\subseteq B$ has a supremum in $E$, then that supremum lies in $B$.

**Proposition.** Every band is an order ideal; an intersection of bands is a band; the set

$$
B^{\perp} = \{x : x\perp b \ \text{for every } b\in B\}
$$

is a band, the **disjoint complement** of $B$, and $B\cap B^{\perp} = \{0\}$.

*Proof.* The ideal property is part of the definition of a band. For the intersection, the interval property and the closure under suprema pass to intersections. For the disjoint complement, the interval property is the second statement of the disjointness proposition, and the closure under suprema holds because a supremum of elements disjoint from $b$ is disjoint from $b$ when it exists; the intersection is zero because a nonzero $x$ with $x\perp x$ would give $\lvert x\rvert = 0$.

**Definition.** The ordered vector space is **Dedekind complete** when every nonempty subset that is bounded above has a supremum, and **Dedekind $\sigma$-complete** when every countable bounded above subset does.

## Order Projections

### Definition and First Properties

**Definition.** An **order projection** of a Riesz space $E$ is a **band projection**: a positive idempotent $P : E\to E$ whose range is a band and whose kernel is its disjoint complement. In a Dedekind complete Riesz space the order projections are exactly the positive idempotents dominated by the identity,

$$
P\geq0, \qquad P^2 = P, \qquad 0\leq P\leq I ,
$$

a characterisation proved by the Riesz decomposition theorem below.

**Proposition.** An order projection $P$ satisfies $P(x^+) = (Px)^+$ and $P(x\vee y) = Px\vee Py$, so it is a **lattice homomorphism**; it leaves its range pointwise fixed, $P(Px) = Px$; and the complementary idempotent $I - P$ is again an order projection, onto the disjoint complement of the range.

*Proof.* The decomposition $x = Px + (I-P)x$ writes $x$ as a sum of an element of the range band and an element disjoint from it. For $x^+$ the summands are $P(x^+)\in\operatorname{ran}P$ and $(I-P)(x^+)\perp\operatorname{ran}P$, so the decomposition of $x^+$ is the positive part of the decomposition of $x$, because the positive part of a sum of two disjoint elements is the sum of their positive parts; hence $P(x^+) = (Px)^+$. The same argument applied to $x\vee y$ instead of $x^+$ gives the lattice property. The fixed-point claim is idempotence, and the complementary idempotent is positive because $I - P\geq0$, idempotent because $(I-P)^2 = I - 2P + P^2 = I - P$, and dominated by the identity.

**Proposition (order projections on an interval).** For an order projection $P$ and $x\geq0$,

$$
Px = \sup\{Pz : 0\leq z\leq x\} = \sup\{y\in \operatorname{ran} P : 0\leq y\leq x\},
$$

the supremum existing in $\operatorname{ran} P$ when $E$ is Dedekind complete.

*Proof.* Both suprema are over the same set after the substitution $y = Pz$, which is bijective from the interval $[0,x]$ onto its image because $P$ is a lattice homomorphism with $Px$ fixed; the identity is then the lattice property.

### The Band Decomposition

**Theorem (Riesz decomposition).** Let $E$ be a Dedekind complete Riesz space and let $B$ be a band. Then every $x\in E$ has a unique decomposition

$$
x = x_B + x_{B^{\perp}}, \qquad x_B\in B, \quad x_{B^{\perp}}\in B^{\perp},
$$

and the map $P_B : x\mapsto x_B$ is an order projection with range $B$ and kernel $B^{\perp}$. Consequently every band of a Dedekind complete Riesz space is a projection band, and the map $B\mapsto P_B$ is a bijection between the bands and the order projections.

*Proof.* It is enough to decompose a positive $x$, since $x = x^+ - x^-$ and the decomposition of each part can be added. Let $S = \{y\in B : 0\leq y\leq x\}$. It is nonempty and bounded above by $x$, and $B$, being a band in a Dedekind complete space, is Dedekind complete in the induced order, so $s = \sup S$ exists in $B$ and $0\leq s\leq x$. Put $t = x - s\geq0$. If $0\leq b\leq t$ with $b\in B$ then $s + b\in B$ and $s+b\leq x$, so $b+s\in S$ and $b+s\leq s$, whence $b\leq0$ and $b = 0$; thus $t\perp B$ on the positive elements, hence $t\perp B$. Uniqueness: if $x = x_1 + x_2 = x_1' + x_2'$ with $x_1,x_1'\in B$ and $x_2,x_2'\in B^{\perp}$, then $x_1 - x_1' = x_2' - x_2$ lies in $B\cap B^{\perp} = \{0\}$. The map $P_B$ is linear and idempotent by the uniqueness, positive because $x\geq0$ gives $P_B x = s\geq0$, and $0\leq P_B\leq I$ because $0\leq s\leq x$; its range is $B$ and its kernel is $B^{\perp}$. Conversely a band is the range of its projection, so the map is a bijection.

**Corollary (the Riesz–Kantorovich theorem).** Let $E$ be a Riesz space and let $F$ be a Dedekind complete Riesz space. Then the regular operators $L^r(E,F)$ of *Positive Operators on an Ordered Space* are a Dedekind complete Riesz space, the lattice operations are pointwise on the positive cone, and every order-bounded operator is regular; the modulus is $\lvert T\rvert x = \sup\{\lvert Ty\rvert : \lvert y\rvert\leq x\}$ for $x\geq0$.

*Proof.* For $S,T\in L^r(E,F)$ the pointwise supremum $(S\vee T)x = \sup\{Sy\vee Ty' : \dots\}$ is well defined and finite by the order boundedness and the Dedekind completeness of $F$, and it is linear because the lattice operations of $F$ are compatible with addition; this exhibits $L^r(E,F)$ as a Riesz space, and the modulus formula is the pointwise supremum of the two signs. The completeness and the regularity of the order-bounded operators are the standard Riesz–Kantorovich theorem, of which the present argument is the finite-supremum part.

### The Boolean Algebra of Order Projections

**Theorem.** The order projections of a Riesz space commute, and with

$$
P\wedge Q = PQ, \qquad P\vee Q = P + Q - PQ, \qquad P^{\perp} = I - P,
$$

they form a Boolean algebra, in which the order is the order of the operators, the meet is the projection onto the intersection of the ranges and the join is the projection onto the band generated by the union.

*Proof.* For order projections $P,Q$ the composites $PQ$ and $QP$ are positive idempotents with $0\leq PQ\leq I$, and $PQ$ has range $\operatorname{ran}P\cap\operatorname{ran}Q$, a band: hence $PQ$ is the order projection onto the intersection, and it is symmetric in $P,Q$, so $PQ = QP$ and $P\wedge Q = PQ$. The operator $P + Q - PQ$ is an idempotent with range the band generated by the two ranges, so it is $P\vee Q$. The complement is the projection onto the disjoint complement, already computed. The Boolean laws follow from the band interpretation.

## Worked Cases

### The Sequence Space

Let $E = \ell^\infty$ with the pointwise order, a Dedekind complete Riesz space. Its bands are exactly the sets $\{x : x_n = 0 \text{ for } n\notin A\}$ for a subset $A\subseteq\mathbb{N}$, and they correspond to the measurable subsets of $\mathbb{N}$; the projection band $P_A$ is the multiplication by the indicator of $A$, and the Boolean algebra of projections is the algebra of subsets of $\mathbb{N}$ modulo the presentation. This is the smallest complete example and the model for the multiplicative projections of a function space.

### The Lebesgue Space

Let $E = L^p(X,\mu)$ for $1<p<\infty$ with the almost-everywhere order, a Dedekind complete Riesz space. Its bands are the subspaces $L^p(A)$ of functions supported on a measurable set $A$; the order projections are the conditional expectations $P_A f = \mathbb{E}(f\mid A)\mathbf{1}_A = f\mathbf{1}_A$, and the Boolean algebra of projections is the measure algebra of $(X,\mu)$. For $p = 1$ and $p = \infty$ the lattice is still complete, and the norm is not a lattice norm in the same strict sense; the normed theory is not entered here.

### The Continuous Functions

Let $E = C(X)$ for a compact Hausdorff $X$, with the pointwise order. It is generally **not** Dedekind complete: a bounded set of continuous functions need not have a continuous supremum. Its projection bands are the bands generated by the **clopen** subsets of $X$, with the projections the multiplications by the characteristic functions of clopen sets, and the order projections form the Boolean algebra of the clopen subsets. The order projections of the ordered space $C(X)$ are therefore the identifications of the connected components of $X$, and the norm is not used in their description.

## Summary

A **Riesz space** is an ordered vector space in which every pair has a supremum and an infimum; the lattice operations are compatible with addition and nonnegative scaling, the absolute value and the positive and negative parts satisfy $x = x^+ - x^-$ and $\lvert x\rvert = x^+ + x^-$ with $x^+\wedge x^- = 0$, the triangle inequality holds, and the disjointness $\lvert x\rvert\wedge\lvert y\rvert = 0$ behaves as an orthogonal relation. The **order ideals** have the interval property and the **bands** are the order ideals closed under existing suprema; the disjoint complement $B^{\perp}$ is a band disjoint from $B$. An **order projection** is a positive idempotent $P$ with $0\leq P\leq I$; it is a lattice homomorphism, its range is a band, and the **Riesz decomposition theorem** states that in a Dedekind complete space every band is a projection band, so that $E = B\oplus B^{\perp}$ and the bands are in bijection with the order projections through $B\mapsto P_B$. The same theorem in the form of an operator statement is the **Riesz–Kantorovich theorem**: the regular operators into a Dedekind complete space form a Dedekind complete Riesz space. The order projections commute and form a **Boolean algebra** under composition, union and complement. The lattice as an abstract object is *Order Theory and Lattices*; the order and the topology are *Ordered Vector Spaces and the Order Unit*; the positive operators are *Positive Operators on an Ordered Space*; and the norm of a Riesz space is *Normed and Banach Spaces* of Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x\vee y$, $x\wedge y$ | Supremum and infimum in the Riesz space |
| $\lvert x\rvert$, $x^+$, $x^-$ | Absolute value, positive and negative parts |
| $x\perp y$ | Disjointness, $\lvert x\rvert\wedge\lvert y\rvert = 0$ |
| Order ideal, band | Subspace with the interval property; ideal closed under suprema |
| $B^{\perp}$ | Disjoint complement of the band $B$ |
| Dedekind complete | Every nonempty set bounded above has a supremum |
| $P_B$ | Order projection onto the band $B$, $0\leq P_B\leq I$ |
| $\lvert T\rvert$ | Modulus of a regular operator, Riesz–Kantorovich |
| $P\wedge Q = PQ$, $P\vee Q = P+Q-PQ$ | Boolean algebra of order projections |

## Further Reading

- Frigyes Riesz, *Les systèmes d'équations linéaires à une infinité d'inconnues* (Gauthier-Villars, 1913), for the origin of the order-theoretic decomposition.
- Leonid V. Kantorovich, "Lineare halbgeordnete Räume", *Recueil Mathématique* **2** (1937), 121–168, for the vector lattice and the regular operators.
- W. A. J. Luxemburg and A. C. Zaanen, *Riesz Spaces*, vol. 1 (North-Holland, 1971), for bands, projection bands and the Riesz decomposition theorem.
- Bernhard Banaschewski, "Über den Satz von Riesz über die Zerlegung von Vektorverbänden", *Mathematische Nachrichten* **10** (1953), 59–76, for the Boolean algebra of order projections.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the Riesz–Kantorovich theorem and the regular operators.
- Peter Meyer-Nieberg, *Banach Lattices* (Springer, 1991), for the normed theory of a Riesz space and its bands.
