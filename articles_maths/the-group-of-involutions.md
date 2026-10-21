# __The Group of Involutions__

## Introduction

The biquaternion algebra carries two distinguished involutive anti-automorphisms, the **Hermitian conjugation** ${}^{*}$ and the **quaternion conjugation** ${}^{\natural}$. They commute, and together with the identity and their composite, the complex conjugation $\bar{\cdot}$, they form a group of order four, the **Klein four-group** $V_{4}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2}$. This article treats the two maps and the group they generate: the two composition rules, the Cayley table, the subgroups, the place of the fourth conjugation, the reversal, outside the group, the composition table that includes the reversal, and the orbits of the group on the algebra.

The formulas of the four conjugations and the algebra itself are *The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$*; the lattice of the fixed spaces they produce is *Comparison of the Remarkable Subspaces*; and the remarkable subspaces, one to a section, are *Introduction to the Remarkable Subspaces*. None of these is repeated here.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$, the coefficients complex; units $e_t=1$ and $\vec e_k^{2}=-e_t$; central scalar imaginary $i$; sign vector $\varepsilon=(1,-1,-1,-1)$. On the coefficients the four involutions act by

$$
({\tilde Q}^{\mathrm{id}})_\mu=Q_\mu , \qquad (\tilde Q^{\natural})_\mu=\varepsilon_\mu Q_\mu , \qquad ({\tilde Q}^{*})_\mu=\varepsilon_\mu \bar Q_\mu , \qquad (\bar{\tilde Q})_\mu=\bar Q_\mu .
$$

An **antilinear involution** of $\mathbb{B}$ is a real-linear map $\sigma$ with $\sigma^{2}=\mathrm{id}$ and $\sigma(\lambda\tilde Q)=\bar\lambda\,\sigma(\tilde Q)$ for $\lambda\in\mathbb{C}$. On the eight real coordinates $q_t,q_x,q_y,q_z,q'_t,q'_x,q'_y,q'_z$ of $\tilde Q=\sum_\mu(q_\mu+iq'_\mu)e_\mu$ the four maps act by signed permutations:

| map | $(q_t,q_x,q_y,q_z,q'_t,q'_x,q'_y,q'_z)\mapsto$ |
|---|---|
| $\mathrm{id}$ | $(q_t,q_x,q_y,q_z,q'_t,q'_x,q'_y,q'_z)$ |
| ${}^{\natural}$ | $(q_t,-q_x,-q_y,-q_z,q'_t,-q'_x,-q'_y,-q'_z)$ |
| $\bar{\cdot}$ | $(q_t,q_x,q_y,q_z,-q'_t,-q'_x,-q'_y,-q'_z)$ |
| ${}^{*}$ | $(q_t,-q_x,-q_y,-q_z,-q'_t,q'_x,q'_y,q'_z)$ |
| $\flat$ | $(-q_t,q_x,q_y,q_z,q'_t,-q'_x,-q'_y,-q'_z)$ |

Only ${}^{*}$, $\bar{\cdot}$ and $\flat$ are antilinear in this sense; ${}^{\natural}$ is $\mathbb{C}$-linear, and $\mathrm{id}$ is the identity. The first three rows are the maps of the group studied below; the last is the reversal, treated with them and outside the group.

## The Extra Involution

**Definition.** The **Hermitian conjugation** is the antilinear involution

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z ,
$$

the C*-involution of the algebra, and the **quaternion conjugation** is the linear involution

$$
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z ,
$$

the **extra involution**: the second anti-automorphism of order two that the algebra carries.

**Proposition (both reverse the product).** For $\tilde Q_1,\tilde Q_2\in\mathbb{B}$,

$$
(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}, \qquad (\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}, \qquad \overline{\tilde Q_1\tilde Q_2}=\bar{\tilde Q_1}\,\bar{\tilde Q_2} .
$$

Thus ${}^{*}$ and ${}^{\natural}$ are anti-automorphisms, reversing the order of every product, while the complex conjugation is an automorphism, reversing nothing.

**Proof.** The formulas are read on the coefficients. The natural sign $\varepsilon$ multiplies the $\mu$-th coefficient of both factors, and $\varepsilon_\mu^{2}=1$, so the sign survives the expansion while the two factors exchange places; the bar is a ring homomorphism of $\mathbb{C}$ applied coefficient-wise, hence multiplicative and order-preserving.

**Proposition (order two, and they commute).** Each of the two is its own inverse, the two commute, and their composite is the complex conjugation:

$$
{}^{*}\circ{}^{*}=\mathrm{id}, \qquad {}^{\natural}\circ{}^{\natural}=\mathrm{id}, \qquad {}^{*}\circ{}^{\natural}={}^{\natural}\circ{}^{*}=\bar{\cdot} .
$$

**Proof.** On each coefficient the natural sign is an involution, the bar is an involution, and the two commute, one multiplying by $\pm1$ and the other conjugating the scalar; composing the two coefficient rules gives the bar alone. The order of the two factors makes no difference because the two coefficient operations commute.

**Remark (why the extra involution is not the C*-involution).** Two differences separate it from ${}^{*}$. First, ${}^{\natural}$ is **linear**, commuting with the scalars of $\mathbb{C}$, whereas a C*-involution is conjugate-linear and ${}^{*}$ is so, ${}^{*}(\lambda\tilde Q)=\bar\lambda\,\tilde Q^{*}$ for $\lambda\in\mathbb{C}$. Second, ${}^{\natural}$ fixes the centre pointwise while ${}^{*}$ fixes it only up to the coefficient conjugation. In the matrix picture the extra involution is the composition of the coefficient conjugation with the conjugate transpose, $\natural=\bar{\cdot}\circ{}^{*}$, the C*-involution read after the coefficients are conjugated (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*). **The extra involution is the second, independent anti-automorphism of order two that the algebra carries.**

## The Group of Involutions

**Theorem.** The set

$$
G=\{\mathrm{id},\,{}^{*},\,{}^{\natural},\,\bar{\cdot}\}
$$

is a group under composition, and it is the Klein four-group $V_{4}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2}$: every element is its own inverse, and the composite of two distinct non-identity elements is the third.

**Proof.** Closure is the six products ${}^{*}\circ{}^{\natural}={}^{\natural}\circ{}^{*}=\bar{\cdot}$, ${}^{*}\circ\bar{\cdot}=\bar{\cdot}\circ{}^{*}={}^{\natural}$ and ${}^{\natural}\circ\bar{\cdot}=\bar{\cdot}\circ{}^{\natural}={}^{*}$, which lie in $G$ by the propositions above, together with the squares, which are $\mathrm{id}$. Composition of maps is associative, $\mathrm{id}$ is the unit, and every element is its own inverse. A group of order four in which every element has order two has no element of order four, hence is not cyclic, and is therefore $V_{4}$.

The Cayley table, the entry being the map applied first in the row and then in the column, is

| $\circ$ | $\mathrm{id}$ | ${}^{*}$ | ${}^{\natural}$ | $\bar{\cdot}$ |
|---|---|---|---|---|
| $\mathrm{id}$ | $\mathrm{id}$ | ${}^{*}$ | ${}^{\natural}$ | $\bar{\cdot}$ |
| ${}^{*}$ | ${}^{*}$ | $\mathrm{id}$ | $\bar{\cdot}$ | ${}^{\natural}$ |
| ${}^{\natural}$ | ${}^{\natural}$ | $\bar{\cdot}$ | $\mathrm{id}$ | ${}^{*}$ |
| $\bar{\cdot}$ | $\bar{\cdot}$ | ${}^{\natural}$ | ${}^{*}$ | $\mathrm{id}$ |

**Remark (the group is abelian).** Every square is the identity and the table is symmetric, so the four maps may be applied in any order, and the conjugation action of the group on itself is trivial. **The group is abelian, and the four involutions commute pairwise.**

**Remark (the reversal is outside).** The fourth conjugation of the algebra, the reversal $\flat=-{}^{*}$, is not an element of $G$: its square is $\mathrm{id}$, but $\flat\circ{}^{*}=-\mathrm{id}$ is not one of the four, so the set $\{{}^{*},{}^{\natural},\bar{\cdot},\flat\}$ is not closed. The reversal is an anti-automorphism only up to the central sign, since $(\tilde Q_1\tilde Q_2)^{\flat}=-\tilde Q_2^{\flat}\tilde Q_1^{\flat}$, and its compositions with the group are read in the next table, where the entries are the maps of $G$ and their negatives.

## The Composition Table with the Reversal

The four conjugations together, including the reversal, do not form a group, but their compositions are still read on the four maps up to the central sign $\pm1$. With the entry the map applied first in the row and then in the column,

| $\circ$ | ${}^{\natural}$ | $\bar{\cdot}$ | ${}^{*}$ | $\flat$ |
|---|---|---|---|---|
| ${}^{\natural}$ | $\mathrm{id}$ | ${}^{*}$ | $\bar{\cdot}$ | $-\bar{\cdot}$ |
| $\bar{\cdot}$ | ${}^{*}$ | $\mathrm{id}$ | ${}^{\natural}$ | $-{}^{\natural}$ |
| ${}^{*}$ | $\bar{\cdot}$ | ${}^{\natural}$ | $\mathrm{id}$ | $-\mathrm{id}$ |
| $\flat$ | $-\bar{\cdot}$ | $-{}^{\natural}$ | $-\mathrm{id}$ | $\mathrm{id}$ |

The entry $-\bar{\cdot}$ denotes the map $\tilde Q\mapsto-\bar{\tilde Q}$, and similarly for $-{}^{\natural}$ and $-\mathrm{id}$. The table contains the two composition rules of §*The Group of Involutions* and shows where the group structure stops: the composite of two maps of $G$ is the third, while a composite involving the reversal is the negative of a map of $G$. The negative of the identity appears in the two entries $({}^{*},\flat)$ and $(\flat,{}^{*})$, and it is this central sign that keeps the reversal outside $G$ and makes the set $\{\natural,\bar{\cdot},{}^{*},\flat\}$ closed only up to $\pm1$.

## The Structure of the Group

**Proposition (the subgroups).** The group has exactly three subgroups of order two, one for each non-identity element,

$$
\{\mathrm{id},{}^{*}\}, \qquad \{\mathrm{id},{}^{\natural}\}, \qquad \{\mathrm{id},\bar{\cdot}\},
$$

and no subgroup of order three; its only subgroup of order four is $G$ itself. Each of the three is the subgroup generated by one of the three non-identity elements, and the three are the only proper subgroups.

**Proof.** A subgroup order divides the order of the group, so the orders available are one, two and four; an element of order two generates a subgroup of order two, and each of the three non-identity elements is its own inverse, so each generates one. No two of them generate the same subgroup, since the elements are distinct, and a subgroup of order two contains the identity and one further element. A subgroup of order three would have an element of order three by Lagrange applied to the prime $3$, and the group has none.

**Proposition (two generate the group).** Any two distinct non-identity elements of the group generate it. In particular the pair ${}^{\natural}$, ${}^{*}$ presented in the two Propositions of §*The Extra Involution* generates $G$, the third element being their composite $\bar{\cdot}$.

**Proof.** Each non-identity element has order two, and the composite of two distinct ones is the third, which is contained in the subgroup they generate; the subgroup therefore contains three non-identity elements and the identity, and is $G$.

**Remark (two choices of generators).** *The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$* writes the two generators as ${}^{\natural}$ and $\bar{\cdot}$; this article writes them as ${}^{\natural}$ and ${}^{*}$. The two choices describe the same group, since ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ and $\bar{\cdot}={}^{*}\circ{}^{\natural}$, and either pair generates the third element. The pair is a choice of presentation and not a property of the group.

**Remark (the group is elementary abelian).** The group is the direct product of the two subgroups $\{\mathrm{id},{}^{*}\}$ and $\{\mathrm{id},{}^{\natural}\}$, whose intersection is $\{\mathrm{id}\}$, so

$$
G=\{\mathrm{id},{}^{*}\}\times\{\mathrm{id},{}^{\natural}\}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2} ,
$$

with the third order-two subgroup the diagonal $\{\mathrm{id},\bar{\cdot}\}$. Every element has order two, so the exponent of the group is two and the group is generated by its involutions, which is the reason the group is called the group of involutions. **The group is elementary abelian of order four, and its three involutions together with the identity are the four maps of the table.**

**Proof.** The two subgroups are normal, being index two and of order two, their intersection is trivial and their product contains four elements; the diagonal subgroup is generated by their composites, which are all equal to $\bar{\cdot}$.

## The Orbits of the Group

The group acts on the algebra through its four maps, and the orbit of an element is the set of its four images.

**Theorem.** The orbit of $\tilde Q$ under $G=\{\mathrm{id},{}^{*},{}^{\natural},\bar{\cdot}\}$ has size

$$
1 \quad\text{or}\quad 2 \quad\text{or}\quad 4 ,
$$

the size being $1$ on the real line $\langle e_t\rangle$; $2$ on the elements that lie in the centre $\mathbb{C}_{\mathbb{B}}$, in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ or in the Hermitian subspace $\mathbb{M}_+$ but not on that line; and $4$ otherwise.

**Proof.** An element is fixed by the whole group exactly when it is fixed by ${}^{\natural}$ and by $\bar{\cdot}$, since ${}^{*}$ is their composite; that intersection is $\mathbb{C}_{\mathbb{B}}\cap\mathbb{H}_{\mathbb{B}}=\langle e_t\rangle$, which gives orbit size $1$. The stabilizer has order two exactly when the element is fixed by one of ${}^{\natural},\bar{\cdot},{}^{*}$ and by no second one — fixed by two it is fixed by the third and lies on the real line — and the three fixed spaces are $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$, whose pairwise intersections are all $\langle e_t\rangle$; this gives orbit size $2$ exactly on the stated set, and orbit size $4$ on its complement.

**Example (an element of each orbit size).** For $\tilde Q=e_t+2\vec e_x+3i\vec e_x+4i\vec e_y$ the images are

$$
\tilde Q^{\natural}=e_t-2\vec e_x-3i\vec e_x-4i\vec e_y,\quad \bar{\tilde Q}=e_t+2\vec e_x-3i\vec e_x-4i\vec e_y,\quad \tilde Q^{*}=e_t-2\vec e_x+3i\vec e_x+4i\vec e_y,
$$

and $\tilde Q^{\flat}=-e_t+2\vec e_x-3i\vec e_x-4i\vec e_y$; the four points are pairwise distinct, so the orbit has size $4$, the element lying in none of $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$. For the central but non-real element $\tilde Q=(1+3i)e_t$ the images are $(1+3i)e_t$ under $\mathrm{id}$ and ${}^{\natural}$, and $(1-3i)e_t$ under $\bar{\cdot}$ and ${}^{*}$, so the orbit is $\{(1+3i)e_t,(1-3i)e_t\}$ of size $2$. For $\tilde Q=2e_t$ every image is $2e_t$, so the orbit has size $1$.

**Example (the stabilizer of a vector).** For $\tilde Q=\vec e_x$ the maps ${}^{\natural}$ and ${}^{*}$ negate it, while $\bar{\cdot}$ fixes it, the coefficient being real:

$$
{}^{\natural}(\vec e_x)=-\vec e_x,\qquad \bar{\cdot}(\vec e_x)=\vec e_x,\qquad {}^{*}(\vec e_x)=-\vec e_x,\qquad \flat(\vec e_x)=\vec e_x,
$$

so the orbit is $\{\vec e_x,-\vec e_x\}$ of size two and the stabilizer of $\vec e_x$ is $\{\mathrm{id},\bar{\cdot}\}$, the subgroup that fixes $\mathbb{H}_{\mathbb{B}}$ pointwise.

**Example (a Hermitian element).** For $\tilde Q=e_t+i\vec e_x$ the images are

$$
\tilde Q^{\natural}=e_t-i\vec e_x,\qquad \bar{\tilde Q}=e_t-i\vec e_x,\qquad \tilde Q^{*}=e_t+i\vec e_x=\tilde Q,\qquad \tilde Q^{\flat}=-e_t-i\vec e_x,
$$

so the orbit is $\{e_t+i\vec e_x,\,e_t-i\vec e_x,\,-e_t-i\vec e_x,\,-e_t+i\vec e_x\}$ of size four.

## Summary

The biquaternion algebra carries two commuting involutive anti-automorphisms of order two, the Hermitian conjugation ${}^{*}$ and the quaternion conjugation ${}^{\natural}$; the first is the C*-involution, conjugate-linear, and the second is the extra involution, linear, both reversing the order of every product. With the identity and their composite, the complex conjugation $\bar{\cdot}$, they form the Klein four-group $G=\{\mathrm{id},{}^{*},{}^{\natural},\bar{\cdot}\}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2}$, in which every element is its own inverse, the composite of two distinct non-identity elements is the third, and the table is symmetric. The group has exactly three proper subgroups, the order-two subgroups generated by the three non-identity elements, any two of which generate the group; it is elementary abelian, the direct product of the subgroups of ${}^{*}$ and of ${}^{\natural}$, and its exponent is two. The reversal $\flat=-{}^{*}$ lies outside the group, being an anti-automorphism only up to the central sign; its compositions with the group are read, up to that sign, in the composition table with the reversal, in which every entry is a map of the group or its negative. The group acts on the algebra with orbits of size one, two or four, according as the element lies on the real line, in the centre, the quaternion subspace or the Hermitian subspace but off that line, or nowhere in particular; the orbit–stabilizer count reads these sizes from the fixed spaces of the three non-identity maps.

## Summary of Notation

| symbol | meaning |
|---|---|
| ${}^{*}$ | Hermitian conjugation, the C*-involution, $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$ |
| ${}^{\natural}$ | quaternion conjugation, the extra involution, linear of order two |
| $\bar{\cdot}$ | complex conjugation, the composite ${}^{*}\circ{}^{\natural}$ |
| $\flat=-{}^{*}$ | the reversal, outside the group |
| $G=\{\mathrm{id},{}^{*},{}^{\natural},\bar{\cdot}\}$ | the group of involutions, the Klein four-group |
| $\{\mathrm{id},{}^{*}\}$, $\{\mathrm{id},{}^{\natural}\}$, $\{\mathrm{id},\bar{\cdot}\}$ | the three subgroups of order two |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector of the natural conjugation |
| orbit | the set of the four conjugated images of an element, of size $1$, $2$ or $4$ |
| stabilizer | the subgroup of the group fixing an element |
| composition table with the reversal | the $4\times4$ table over $\{\natural,\bar{\cdot},{}^{*},\flat\}$, with entries the maps of $G$ and their negatives |

## Further Reading

- *The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$* (`articles_maths/the-biquaternion-algebra-as-a-vector-space-over-c-and-r.md`), for the algebra, its basis and its four conjugations
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable fixed spaces of the four involutions, one to a section
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`), for the relations between the remarkable fixed spaces and the lattice they form
- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the matrix picture in which the extra involution is the coefficient conjugation composed with the conjugate transpose
