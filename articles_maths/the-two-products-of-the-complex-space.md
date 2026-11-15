# __The Two Products of the Complex Space__

## Introduction

The complex space carries two products: the multiplication of the field, $Q_1Q_2$, and the same multiplication with the second argument conjugated, $Q_1\bar Q_2$. The field has one nontrivial involution, the bar, so a product read off the field is fixed by where the bar sits: it may sit on no argument, which gives the plain product, or on an argument, which gives a sesquilinear one. The two sesquilinear readings are not two operations, because the bar is an automorphism of the field and $\bar Q_1Q_2=\overline{Q_1\bar Q_2}$ is the conjugate of $Q_1\bar Q_2$; the space therefore carries the plain product, the sesquilinear product, and nothing else.

The article defines the two products on the coordinates, states the exact set of pairs on which they agree, proves the exchange identity that fixes each of them, separates them by the class of their slots, proves the laws that one keeps and the other loses, and exhibits the two pairings with their two adjoints.

The multiplication of the field and the definition of $\mathbb{C}$ are *Complex Algebra*. The classes of element read in the two products are *The Classes of Element of the Complex Algebra*, and the field property that keeps the count at two is *The Specificities of the Complex Algebra*. The forms and norms carried by the two products are *The Two Forms and the Two Algebraic Norms of the Complex Space*; the ternary product forced by the failure of associativity is *The Ternary Product and the Associator of the Complex Space*; the two-sided operators are *The Enveloping Operator Algebra and the Collapse of the Two-Sided Action on the Complex Algebra*.

**Interpretation.** The element is $Q_1=q_1+iq'_1$ with real coordinates $q_1$ and $q'_1$, and a second element is $Q_2=q_2+iq'_2$. The base involution is the bar, $\bar Q_1=q_1-iq'_1$, and the Hermitian conjugation is the same map, ${}^{*}=\bar{\cdot}$. The two products are written $Q_1Q_2$ and $Q_1\bar Q_2$, and they are the plain bilinear and the plain sesquilinear product of the space; the conjugation that separates them acts on the second slot.

## The Two Products

**Definition.** The **plain product** is the multiplication of the field,

$$
Q_1Q_2=(q_1q_2-q'_1q'_2)+i(q_1q'_2+q'_1q_2),
$$

and the **sesquilinear product** is the same multiplication with the second factor conjugated,

$$
Q_1\bar Q_2=(q_1q_2+q'_1q'_2)+i(q'_1q_2-q_1q'_2).
$$

The two read the same pair and differ in the sign of the term $q'_1q'_2$ in the real part and in the order of the factors in the imaginary part.

**Proposition.** The two products agree exactly when $Q_2$ is real or $Q_1$ is zero.

*Proof.* The difference is $Q_1\bar Q_2-Q_1Q_2=Q_1(\bar Q_2-Q_2)=-2iQ_1\operatorname{Im}Q_2$. The field has no zero divisors, so the difference vanishes exactly when $Q_1=0$ or $\operatorname{Im}Q_2=0$.

**Remark (no third product).** A product of the space is read on its two slots, and the only conjugation the field offers is the bar, so the choice is the bar on neither slot, on the second, or on the first. The first two give $Q_1Q_2$ and $Q_1\bar Q_2$; the third gives $\bar Q_1Q_2$, and $\overline{Q_1\bar Q_2}=\bar Q_1\bar{\bar Q_2}=\bar Q_1Q_2$, so it is the conjugate of the sesquilinear product and not a third operation. Two products, and no other.

## The Exchange That Fixes Each Product

### The Interchange and the Plain Product

**Proposition.** The plain product is fixed by the interchange of its two arguments: $Q_1Q_2=Q_2Q_1$.

*Proof.* The multiplication of $\mathbb{C}$ is commutative, being the multiplication of a field. In coordinates the two displays of the preceding section are symmetric in the indices $1$ and $2$.

The interchange is the exchange that preserves the class of a bilinear product, and the proposition says that the plain product is fixed by it. Hence its symmetric part, the half-sum of the product and its image, is the product itself, and its antisymmetric part, the half-difference, is zero.

### The Adapted Exchange and the Sesquilinear Product

**Proposition.** The sesquilinear product is fixed by the interchange composed with the conjugation of the value: $Q_1\bar Q_2=\overline{Q_2\bar Q_1}$.

*Proof.* $\overline{Q_2\bar Q_1}=\bar Q_2Q_1$, and the multiplication of the field is commutative, so $\bar Q_2Q_1=Q_1\bar Q_2$.

**Remark (the interchange alone does not fix it).** The plain interchange sends $Q_1\bar Q_2$ to $Q_2\bar Q_1$, and the two differ whenever $\operatorname{Im}(Q_1\bar Q_2)\neq0$. The sesquilinear product is therefore fixed by the adapted exchange and not by the plain one. It does not split either: its conjugate-symmetric half, the half-sum against the adapted exchange, is the product, and its skew-conjugate-symmetric half is zero. This is the whole content of the section: neither product has an antisymmetric part, but the exchange that shows it for the sesquilinear product is not the naive one.

**Remark (the difference that is not a part).** The quantity $Q_1\bar Q_2-Q_2\bar Q_1$ is non-zero in general, and it is not an antisymmetric part of the sesquilinear product. It equals $2i\operatorname{Im}(Q_1\bar Q_2)$, a purely imaginary value, so it is not a product of the class; and it is real-linear in the first slot without being $\mathbb{C}$-linear or conjugate-linear there, since at $(Q_1,Q_2)=(1,1)$ it vanishes and at $(i,1)$ it equals $2i$, whereas a $\mathbb{C}$-linear map vanishing at $1$ would give $i\cdot0$ and a conjugate-linear one $\bar i\cdot0$. An antisymmetric part is by definition the half-difference of a product and its image under the exchange that preserves the class, and that half-difference is zero here. The quantity $Q_1\bar Q_2-Q_2\bar Q_1$ is the imaginary part of the Hermitian form, and it is studied as such in *The Two Forms and the Two Algebraic Norms of the Complex Space*, where it appears as $2i$ times the imaginary part of $H$.

## The Two Classes

**Proposition.** Both products are $\mathbb{C}$-linear in the first slot; in the second slot the plain product is $\mathbb{C}$-linear and the sesquilinear product is conjugate-linear.

*Proof.* For the first slot, $(\lambda Q_1)\bar Q_2=\lambda(Q_1\bar Q_2)$ and $(\lambda Q_1)Q_2=\lambda(Q_1Q_2)$ for every complex $\lambda$. For the second, $Q_1(\lambda Q_2)=\lambda(Q_1Q_2)$, whereas $Q_1\overline{\lambda Q_2}=\bar\lambda(Q_1\bar Q_2)$.

The table records the two slot rules and the two classes they give.

| product | first slot | second slot | class over $\mathbb{C}$ |
|---|---|---|---|
| $Q_1Q_2$ | $\mathbb{C}$-linear | $\mathbb{C}$-linear | bilinear |
| $Q_1\bar Q_2$ | $\mathbb{C}$-linear | conjugate-linear | sesquilinear |

The two products belong to two different classes, and the classes must be kept apart: the exchange that preserves a bilinear product and the exchange that preserves a sesquilinear one are different maps.

## The Laws

**Proposition.** The plain product is associative, commutative, and has the unit $1$ on both sides.

*Proof.* These are the field laws, proved in *Complex Algebra*; the two-sided unit is the multiplicative identity.

**Proposition.** The sesquilinear product is not associative, has the unit $1$ on the right and no unit on the left, and is commutative in the twisted sense $\overline{Q_2\bar Q_1}=Q_1\bar Q_2$.

*Proof.* The right unit is read at $Q_2=1$: $Q_1\bar 1=Q_1$. On the left, a unit $E$ would satisfy $E\bar Q=Q$ for every $Q$; at $Q=1$ this gives $E=1$, and at $Q=i$ it gives $E\bar i=-iE=i$, that is $E=-1$, so the two values contradict and no left unit exists. The twisted commutativity is the exchange identity. The failure of associativity is computed in *The Ternary Product and the Associator of the Complex Space*; its value is $Q_1\bar Q_2(\bar Q_3-Q_3)$, which is not identically zero, the two sides at $(Q_1,Q_2,Q_3)=(1,1,i)$ being $-i$ and $i$.

The two products differ on exactly the laws the slot analysis predicts: the conjugation in the second slot is what destroys associativity and what removes the left unit. The plain product, whose second slot is linear, keeps both.

## The Two Pairings and the Two Adjoints

### The Plain Pairing and Its Adjoint

**Definition.** The **plain pairing** is $P(Q_1,Q_2)=Q_1Q_2$.

**Proposition.** The plain pairing is symmetric, and the left multiplication $L_{Q_1}(Q_3)=Q_1Q_3$ is self-adjoint for it: $P(L_{Q_1}Q_3,Q_2)=P(Q_3,L_{Q_1}Q_2)$.

*Proof.* The two sides are $Q_1Q_3Q_2$ and $Q_3Q_1Q_2$, and the multiplication is commutative.

### The Hermitian Pairing and Its Adjoint

**Definition.** The **Hermitian pairing** is $H(Q_1,Q_2)=Q_1\bar Q_2$.

**Proposition.** The Hermitian pairing is conjugate-symmetric, and the adjoint of the left multiplication is the left multiplication by the conjugate: $L_{Q_1}^{\dagger}=L_{\bar Q_1}$.

*Proof.* $H(L_{Q_1}Q_3,Q_2)=Q_1Q_3\bar Q_2$ and $H(Q_3,L_{\bar Q_1}Q_2)=Q_3\overline{\bar Q_1Q_2}=Q_3Q_1\bar Q_2$, and the two agree. The same computation with the roles of the slots exchanged gives $R_{Q_1}^{\dagger}=R_{\bar Q_1}$.

**Remark (the two adjoints differ by the conjugation of the parameter).** The plain pairing keeps the parameter and the Hermitian pairing conjugates it, and the reason is the slot: an adjoint is read against a form, a form is the scalar part of a product, and the second slot of the Hermitian pairing carries the conjugation. In the matrix model $M_2(\mathbb{R})$ of *$M_2(\mathbb{R})$ Cayley Representation : Operators* the multiplication by $Q=q+iq'$ is the matrix with rows $(q,-q')$ and $(q',q)$, whose transpose is the matrix of the multiplication by $\bar Q$; the conjugation of the parameter is the transposition. The Euclidean adjoint of $L_{Q_1}$ is therefore $L_{\bar Q_1}$, which is the Hermitian adjoint; the plain pairing is a different form, of realified signature $(1,1)$, and for it the adjoint keeps the parameter.

## The Two Structures

The two products define two structures on one space. The plain product makes $\mathbb{C}$ the field it is: associative, commutative, with a two-sided unit, and with every non-zero element invertible. The sesquilinear product makes $\mathbb{C}$ the general plain sesqualgebra over $(\mathbb{C},\bar{\cdot})$: an abelian group with an operation that is additive, $\mathbb{C}$-linear in the first slot, conjugate-linear in the second, with a right unit alone.

**Remark (the second is derived from the first).** The sesquilinear product is the plain product with the conjugation inserted in the second slot, and the insertion is the whole difference. Nothing in the passage uses more than the commutativity of the multiplication and the fact that the bar is an involution. Hence every statement about the sesquilinear structure that is not about the conjugation is a statement about the field, which is why the sesquilinear article of the corpus is short and why the field article carries the weight.

## Summary

The complex space carries two products, $Q_1Q_2$ and $Q_1\bar Q_2$, because the field has one nontrivial involution and the bar either acts on neither slot or on one of them, the two readings with the bar in an argument giving two conjugate operations and not two products. They agree exactly when the second element is real or the first is zero. Each product is fixed by its own exchange, the plain one by the interchange and the sesquilinear one by the interchange composed with the conjugation of the value, so neither splits: each symmetric part is its parent and each antisymmetric part vanishes identically. Both products are $\mathbb{C}$-linear in the first slot and differ in the second, linear against conjugate-linear. The plain product is associative with a two-sided unit; the sesquilinear one is not associative, has the right unit alone, and is commutative only in the twisted sense. The plain pairing is symmetric with a self-adjoint multiplication, and the Hermitian pairing is conjugate-symmetric with the adjoint $L_{Q_1}^{\dagger}=L_{\bar Q_1}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_1=q_1+iq'_1$, $Q_2=q_2+iq'_2$ | two complex elements, with real coordinates |
| $Q_1Q_2$ | the plain product, the multiplication of the field |
| $Q_1\bar Q_2$ | the sesquilinear product, the second factor conjugated |
| ${}^{*}$ | the Hermitian conjugation, the bar here |
| $P(Q_1,Q_2)=Q_1Q_2$ | the plain pairing |
| $H(Q_1,Q_2)=Q_1\bar Q_2$ | the Hermitian pairing |
| $L_{Q_1}$, $R_{Q_1}$ | the left and right multiplications; they coincide |
| $L_{Q_1}^{\dagger}=L_{\bar Q_1}$ | the adjoint of the left multiplication for $H$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for bilinear and sesquilinear maps, their adjoints and the non-degenerate pairings.
- Serge Lang, *Algebra*, Graduate Texts in Mathematics 211 (Springer, third edition, 2002), for the field product, its laws and the construction of a sesquilinear form from a linear one.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the comparison of a bilinear and a sesquilinear multiplication over a commutative ring with an involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the class-preserving exchanges of a product with an involution.
