# __The Group of Involutions__

## Introduction

The biquaternion algebra carries two distinguished involutive anti-automorphisms, the **Hermitian conjugation** ${}^{*}$ and the **quaternion conjugation** ${}^{\natural}$. They commute, and together with the identity and their composite, the complex conjugation $\bar{\cdot}$, they form a group of order four, the **Klein four-group** $V_{4}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2}$. This article treats the two maps and the group they generate: the two composition rules, the Cayley table, the subgroups, and the place of the fourth conjugation, the reversal, outside the group.

The article reads the maps as involutions of the algebra and nothing else. The formulas of the four conjugations, the composition table that includes the reversal, and the lattice of fixed spaces they produce are *Biquaternion Involution Lattice*; the algebra, its basis and its four conjugations are *Biquaternions as a Vector Space over $\mathbb{C}$*. Neither is repeated here.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$, the coefficients complex; units $e_0=1$ and $e_k^{2}=-e_0$; central scalar imaginary $i$; sign vector $\varepsilon=(1,-1,-1,-1)$. On the coefficients the four involutions act by

$$
({\tilde Q}^{\mathrm{id}})_\mu=Q_\mu , \qquad (\tilde Q^{\natural})_\mu=\varepsilon_\mu Q_\mu , \qquad ({\tilde Q}^{*})_\mu=\varepsilon_\mu \bar Q_\mu , \qquad (\bar{\tilde Q})_\mu=\bar Q_\mu .
$$

## The Extra Involution

**Definition.** The **Hermitian conjugation** is the antilinear involution

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_0e_0-\bar Q_1e_1-\bar Q_2e_2-\bar Q_3e_3 ,
$$

the C*-involution of the algebra, and the **quaternion conjugation** is the linear involution

$$
\tilde Q^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3 ,
$$

the **extra involution**: the second anti-automorphism of order two that the algebra carries.

**Proposition (both reverse the product).** For $\tilde Q,\tilde R\in\mathbb{B}$,

$$
(\tilde Q\tilde R)^{*}=\tilde R^{*}\tilde Q^{*}, \qquad (\tilde Q\tilde R)^{\natural}=\tilde R^{\natural}\tilde Q^{\natural}, \qquad \overline{\tilde Q\tilde R}=\bar{\tilde Q}\,\bar{\tilde R} .
$$

Thus ${}^{*}$ and ${}^{\natural}$ are anti-automorphisms, reversing the order of every product, while the complex conjugation is an automorphism, reversing nothing.

**Proof.** The formulas are read on the coefficients. The natural sign $\varepsilon$ multiplies the $\mu$-th coefficient of both factors, and $\varepsilon_\mu^{2}=1$, so the sign survives the expansion while the two factors exchange places; the bar is a ring homomorphism of $\mathbb{C}$ applied coefficient-wise, hence multiplicative and order-preserving.

**Proposition (order two, and they commute).** Each of the two is its own inverse, the two commute, and their composite is the complex conjugation:

$$
{}^{*}\circ{}^{*}=\mathrm{id}, \qquad {}^{\natural}\circ{}^{\natural}=\mathrm{id}, \qquad {}^{*}\circ{}^{\natural}={}^{\natural}\circ{}^{*}=\bar{\cdot} .
$$

**Proof.** On each coefficient the natural sign is an involution, the bar is an involution, and the two commute, one multiplying by $\pm1$ and the other conjugating the scalar; composing the two coefficient rules gives the bar alone. The order of the two factors makes no difference because the two coefficient operations commute.

**Remark (why the extra involution is not the C*-involution).** Two differences separate it from ${}^{*}$. First, ${}^{\natural}$ is **linear**, commuting with the scalars of $\mathbb{C}$, whereas a C*-involution is conjugate-linear and ${}^{*}$ is so, ${}^{*}(\lambda\tilde Q)=\bar\lambda\,\tilde Q^{*}$ for $\lambda\in\mathbb{C}$. Second, ${}^{\natural}$ fixes the centre pointwise while ${}^{*}$ fixes it only up to the coefficient conjugation. In the matrix picture the extra involution is the composition of the coefficient conjugation with the conjugate transpose, $\natural=\bar{\cdot}\circ{}^{*}$, the C*-involution read after the coefficients are conjugated (*Biquaternion 2×2 Matrix Element Representation*). **The extra involution is the second, independent anti-automorphism of order two that the algebra carries.**

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

**Remark (the reversal is outside).** The fourth conjugation of the algebra, the reversal $\flat=-{}^{*}$, is not an element of $G$: its square is $\mathrm{id}$, but $\flat\circ{}^{*}=-\mathrm{id}$ is not one of the four, so the set $\{{}^{*},{}^{\natural},\bar{\cdot},\flat\}$ is not closed. The reversal is an anti-automorphism only up to the central sign, since $(\tilde Q\tilde R)^{\flat}=-\tilde R^{\flat}\tilde Q^{\flat}$, and its compositions are read in the composition table of *Biquaternion Involution Lattice*.

## The Structure of the Group

**Proposition (the subgroups).** The group has exactly three subgroups of order two, one for each non-identity element,

$$
\{\mathrm{id},{}^{*}\}, \qquad \{\mathrm{id},{}^{\natural}\}, \qquad \{\mathrm{id},\bar{\cdot}\},
$$

and no subgroup of order three; its only subgroup of order four is $G$ itself. Each of the three is the subgroup generated by one of the three non-identity elements, and the three are the only proper subgroups.

**Proof.** A subgroup order divides the order of the group, so the orders available are one, two and four; an element of order two generates a subgroup of order two, and each of the three non-identity elements is its own inverse, so each generates one. No two of them generate the same subgroup, since the elements are distinct, and a subgroup of order two contains the identity and one further element. A subgroup of order three would have an element of order three by Lagrange applied to the prime $3$, and the group has none.

**Proposition (two generate the group).** Any two distinct non-identity elements of the group generate it. In particular the pair ${}^{\natural}$, ${}^{*}$ presented in the two Propositions of §*The Extra Involution* generates $G$, the third element being their composite $\bar{\cdot}$.

**Proof.** Each non-identity element has order two, and the composite of two distinct ones is the third, which is contained in the subgroup they generate; the subgroup therefore contains three non-identity elements and the identity, and is $G$.

**Remark (two choices of generators).** *Biquaternions as a Vector Space over $\mathbb{C}$* and *Biquaternion Involution Lattice* write the two generators as ${}^{\natural}$ and $\bar{\cdot}$; this article writes them as ${}^{\natural}$ and ${}^{*}$. The two choices describe the same group, since ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ and $\bar{\cdot}={}^{*}\circ{}^{\natural}$, and either pair generates the third element. The pair is a choice of presentation and not a property of the group.

**Remark (the group is elementary abelian).** The group is the direct product of the two subgroups $\{\mathrm{id},{}^{*}\}$ and $\{\mathrm{id},{}^{\natural}\}$, whose intersection is $\{\mathrm{id}\}$, so

$$
G=\{\mathrm{id},{}^{*}\}\times\{\mathrm{id},{}^{\natural}\}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2} ,
$$

with the third order-two subgroup the diagonal $\{\mathrm{id},\bar{\cdot}\}$. Every element has order two, so the exponent of the group is two and the group is generated by its involutions, which is the reason the group is called the group of involutions. **The group is elementary abelian of order four, and its three involutions together with the identity are the four maps of the table.**

**Proof.** The two subgroups are normal, being index two and of order two, their intersection is trivial and their product contains four elements; the diagonal subgroup is generated by their composites, which are all equal to $\bar{\cdot}$.

## Summary

The biquaternion algebra carries two commuting involutive anti-automorphisms of order two, the Hermitian conjugation ${}^{*}$ and the quaternion conjugation ${}^{\natural}$; the first is the C*-involution, conjugate-linear, and the second is the extra involution, linear, both reversing the order of every product. With the identity and their composite, the complex conjugation $\bar{\cdot}$, they form the Klein four-group $G=\{\mathrm{id},{}^{*},{}^{\natural},\bar{\cdot}\}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2}$, in which every element is its own inverse, the composite of two distinct non-identity elements is the third, and the table is symmetric. The group has exactly three proper subgroups, the order-two subgroups generated by the three non-identity elements, any two of which generate the group; it is elementary abelian, the direct product of the subgroups of ${}^{*}$ and of ${}^{\natural}$, and its exponent is two. The reversal $\flat=-{}^{*}$ lies outside the group, being an anti-automorphism only up to the central sign.

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

## Further Reading

- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, its basis and its four conjugations
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the formulas of the conjugations, the composition table and the lattice of fixed spaces
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the matrix picture in which the extra involution is the coefficient conjugation composed with the conjugate transpose
