# __The Two Products of the Complex Space__

## Introduction

The complex space carries two products and not twelve. The general theory builds four general products by choosing, on each slot, between the identity and a conjugation, and then splits each of the four into a symmetric and an antisymmetric part. On the complex field the intrinsic conjugation is the identity, the four settings collapse two-and-two, and each of the two survivors is fixed by its own exchange, so no split occurs. The result is the field product $Q_1Q_2$ and the sesquilinear product $Q_1\bar Q_2$, and nothing else.

The article states the collapse, proves the two exchange identities, separates the two products by their slots, proves the laws that one keeps and the other loses, exhibits the two pairings and their two adjoints, and shows that the collapse is the degenerate case of the general theorem on the conjugate-symmetric and skew-conjugate-symmetric parts of a sesquilinear product.

The multiplication of the field and the definition of $\mathbb{C}$ are *Complex Algebra*. The classes of element read in the two products are *The Classes of Element of the Complex Algebra*, and the field property that forces the collapse is *The Specificities of the Complex Algebra*. The forms and norms carried by the two products are *The Two Forms and the Two Algebraic Norms of the Complex Space*; the ternary product forced by the failure of associativity is *The Ternary Product and the Associator of the Complex Space*; the two-sided operators are *The Enveloping Operator Algebra and the Collapse of the Two-Sided Action on the Complex Algebra*.

**Interpretation.** The element is $Q_1=q_1+iq'_1$ with real coordinates $q_1$ and $q'_1$, and a second element is $Q_2=q_2+iq'_2$. The base involution is the bar, $\bar Q_1=q_1-iq'_1$, and the Hermitian conjugation is the same map, ${}^{*}=\bar{\cdot}$; the intrinsic conjugation ${}^{\natural}$ is the identity, the algebra having no vector part. The four general products are written with the slots of *Product and Form Conventions*: the first slot read as it stands or through ${}^{\natural}$, the second as it stands or through ${}^{*}$.

## The Four Products of the General Theory

The general theory reads a product by the conjugation each slot carries. The table lists the four settings and their images on $\mathbb{C}$.

| the general product | the slots | its image on $\mathbb{C}$ |
|---|---|---|
| the general plain bilinear product | $(\mathrm{id},\mathrm{id})$ | $Q_1Q_2$ |
| the general intrinsic-bilinear product | $({}^{\natural},\mathrm{id})$ | $Q_1Q_2$ |
| the general plain sesquilinear product | $(\mathrm{id},{}^{*})$ | $Q_1\bar Q_2$ |
| the general intrinsic-sesquilinear product | $({}^{\natural},{}^{*})$ | $Q_1\bar Q_2$ |

**Proposition.** The four general products fall two-and-two onto two products.

*Proof.* The conjugation ${}^{\natural}$ is the identity map on $\mathbb{C}$, so the two settings of the first slot coincide, and the four settings give two distinct maps.

**Proposition.** The four symmetric parts coincide with their parents, and the four antisymmetric parts vanish identically.

*Proof.* The symmetric part is the half-sum of a product and of its image under the exchange that preserves the class of that product; a product fixed by its own exchange equals its own symmetric part. The next section proves that each of the two products is fixed by its own exchange, so each of the four symmetric parts is its parent. The antisymmetric part is the half-difference, and a difference of two equal terms is zero.

**Remark.** The four antisymmetric products have no object. The operator $\wedge$ of *Product and Form Conventions*, which names the antisymmetrised product $Q_1\wedge Q_2=\tfrac12(Q_1Q_2-Q_2Q_1)$ and its three siblings, names the zero map four times. The twelve names of the general theory therefore name two maps here, and four of the twelve names name the zero map.

## The Two Products

**Definition.** The **plain product** is the multiplication of the field,

$$
Q_1Q_2=(q_1q_2-q'_1q'_2)+i(q_1q'_2+q'_1q_2),
$$

and the **sesquilinear product** is the same multiplication with the second factor conjugated,

$$
Q_1\bar Q_2=(q_1q_2+q'_1q'_2)+i(q'_1q_2-q_1q'_2).
$$

The two read the same pair and differ in the sign of the term $q'_1q'_2$ in the real part and in the order of the factors in the imaginary part. They agree exactly when $q'_1q'_2=0$ and $q_1q'_2=q'_1q_2$, that is, when $Q_2$ is real or $Q_1$ is zero.

## The Two Exchanges

### The Interchange and the Plain Product

**Proposition.** The plain product is fixed by the interchange of its two arguments: $Q_1Q_2=Q_2Q_1$.

*Proof.* The multiplication of $\mathbb{C}$ is commutative, being the multiplication of a field. In coordinates the two displays of the preceding section are symmetric in the indices $1$ and $2$.

The interchange is the exchange that preserves the class of a bilinear product, and the proposition says that the plain product is fixed by it. Hence its symmetric part is the product and its antisymmetric part is zero.

### The Adapted Exchange and the Sesquilinear Product

**Proposition.** The sesquilinear product is fixed by the interchange composed with the conjugation of the value: $Q_1\bar Q_2=\overline{Q_2\bar Q_1}$.

*Proof.* $\overline{Q_2\bar Q_1}=\bar Q_2Q_1$, and the multiplication of the field is commutative, so $\bar Q_2Q_1=Q_1\bar Q_2$.

**Remark (the interchange alone does not fix it).** The plain interchange sends $Q_1\bar Q_2$ to $Q_2\bar Q_1$, and the two differ whenever the imaginary part of $Q_1\bar Q_2$ is non-zero. The sesquilinear product is therefore fixed by the adapted exchange and not by the plain one. This is the whole content of the section: the product does not split, but the exchange that shows it is not the naive one.

## The Collapse as a Degenerate Case

*The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product* proves the general theorem. A sesquilinear product $\star$ over a ring with a compatible involution $c$ is not fixed by the interchange of its arguments: the transposed product has the opposite parity and leaves the class. The exchange is therefore adapted, the arguments are exchanged and the value is conjugated, and with that exchange every sesquilinear product splits uniquely into the **conjugate-symmetric** half $\tfrac12(Q_1\star Q_2+\overline{Q_2\star Q_1})$ and the **skew-conjugate-symmetric** half $\tfrac12(Q_1\star Q_2-\overline{Q_2\star Q_1})$.

**Theorem.** The sesquilinear product of $\mathbb{C}$ is conjugate-symmetric, its skew-conjugate-symmetric half is zero, and its conjugate-symmetric half is the product itself.

*Proof.* Substitute the exchange identity of the preceding section in the two halves: the first becomes $\tfrac12(Q_1\bar Q_2+Q_1\bar Q_2)=Q_1\bar Q_2$ and the second becomes $\tfrac12(Q_1\bar Q_2-Q_1\bar Q_2)=0$.

**Remark (why the degeneration is forced).** In the general theorem the two halves are distinct objects because the value of the product and its conjugate under the exchange are distinct. Here they coincide, and the reason is the commutativity of the algebra: the exchange of the arguments of the multiplication is invisible, so the only thing the adapted exchange has to undo is the conjugation of the value, which it does exactly. The collapse is not a special feature of dimension two; it is the general feature of a sesquilinear product over a commutative algebra with the exchange of the factors.

**Remark (the difference that is not a part).** The quantity $Q_1\bar Q_2-Q_2\bar Q_1$ is non-zero in general, and it is not an antisymmetric part of the sesquilinear product. It equals $2i\operatorname{Im}(Q_1\bar Q_2)$, a purely imaginary value, so it is not a product of the class; and it is real-linear in the first slot without being $\mathbb{C}$-linear or conjugate-linear there, since at $(Q_1,Q_2)=(1,1)$ it vanishes and at $(i,1)$ it equals $2i$, whereas a $\mathbb{C}$-linear map would give $i\cdot0$ and a conjugate-linear one $\bar i\cdot0$. An antisymmetric part is by definition the difference of a product and its image under the exchange that preserves the class, and that difference is zero here. The quantity $Q_1\bar Q_2-Q_2\bar Q_1$ is the imaginary part of the Hermitian form, and it is studied as such in *The Two Forms and the Two Algebraic Norms of the Complex Space*, where it appears as $2i$ times the imaginary part of $H$.

## The Two Classes

**Proposition.** Both products are $\mathbb{C}$-linear in the first slot; in the second slot the plain product is $\mathbb{C}$-linear and the sesquilinear product is conjugate-linear.

*Proof.* For the first slot, $(\lambda Q_1)\bar Q_2=\lambda(Q_1\bar Q_2)$ and $(\lambda Q_1)Q_2=\lambda(Q_1Q_2)$ for every complex $\lambda$. For the second, $Q_1(\lambda Q_2)=\lambda(Q_1Q_2)$, whereas $Q_1\overline{\lambda Q_2}=\bar\lambda(Q_1\bar Q_2)$.

The table records the four slot rules.

| product | first slot | second slot | class over $\mathbb{C}$ |
|---|---|---|---|
| $Q_1Q_2$ | $\mathbb{C}$-linear | $\mathbb{C}$-linear | bilinear |
| $Q_1\bar Q_2$ | $\mathbb{C}$-linear | conjugate-linear | sesquilinear |

The two products belong to two different classes. That is why the general theory keeps them apart and why the antisymmetric parts of one class have no meaning in the other: the exchange that preserves a bilinear product and the exchange that preserves a sesquilinear one are different maps.

## The Laws

**Proposition.** The plain product is associative, commutative, and has the unit $1$ on both sides.

*Proof.* These are the field laws, proved in *Complex Algebra*; the two-sided unit is the multiplicative identity.

**Proposition.** The sesquilinear product is not associative, has the unit $1$ on the right and no unit on the left, and is commutative in the twisted sense $\overline{Q_2\bar Q_1}=Q_1\bar Q_2$.

*Proof.* The right unit is read at $Q_2=1$: $Q_1\bar 1=Q_1$. On the left, $1\bar Q_1=\bar Q_1$, which equals $Q_1$ only for real $Q_1$, so no left unit exists. The twisted commutativity is the exchange identity. The failure of associativity is computed in *The Ternary Product and the Associator of the Complex Space*; its value is $Q_1\bar Q_2(\bar Q_3-Q_3)$, which is not identically zero.

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

**Remark.** The two adjoints differ by the conjugation of the parameter. The plain pairing keeps the parameter and the Hermitian pairing conjugates it, and the reason is again the slot: an adjoint is read against a form, a form is the scalar part of a product, and the second slot of the Hermitian pairing carries the conjugation. In the matrix model $M_2(\mathbb{R})$ of *$M_2(\mathbb{R})$ Cayley Representation : Operators* the same difference appears as the identity of the transpose with the conjugate matrix.

## The Two Structures

The two products define two structures on one space. The plain product makes $\mathbb{C}$ the field it is: associative, commutative, with a two-sided unit, and with every non-zero element invertible. The sesquilinear product makes $\mathbb{C}$ the general plain sesqualgebra over $(\mathbb{C},\bar{\cdot})$: an abelian group with an operation that is additive, $\mathbb{C}$-linear in the first slot, conjugate-linear in the second, with a right unit alone.

**Remark (the second is derived from the first).** The sesquilinear product is the plain product with the conjugation inserted in the second slot, and the insertion is the whole difference. Nothing in the passage uses more than the commutativity of the multiplication and the fact that the bar is an involution. Hence every statement about the sesquilinear structure that is not about the conjugation is a statement about the field, which is why the sesquilinear article of the corpus is short and why the field article carries the weight.

## Summary

The complex space carries two products, $Q_1Q_2$ and $Q_1\bar Q_2$, because the intrinsic conjugation is the identity and the four settings of the general product collapse two-and-two. Each product is fixed by its own exchange, the plain one by the interchange and the sesquilinear one by the interchange composed with the conjugation of the value, so neither splits: the four symmetric parts coincide with their parents and the four antisymmetric parts vanish identically. Both products are $\mathbb{C}$-linear in the first slot and differ in the second, linear against conjugate-linear. The plain product is associative with a two-sided unit; the sesquilinear one is not associative, has the right unit alone, and is commutative only in the twisted sense. The plain pairing is symmetric with a self-adjoint multiplication, the Hermitian pairing is conjugate-symmetric with the adjoint $L_{Q_1}^{\dagger}=L_{\bar Q_1}$, and the collapse of the general split is exactly the degenerate case of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_1=q_1+iq'_1$, $Q_2=q_2+iq'_2$ | two complex elements, with real coordinates |
| $Q_1Q_2$ | the plain product, the multiplication of the field |
| $Q_1\bar Q_2$ | the sesquilinear product, the second factor conjugated |
| ${}^{\natural}$, ${}^{*}$ | the intrinsic conjugation, the identity here, and the Hermitian conjugation, the bar |
| $P(Q_1,Q_2)=Q_1Q_2$ | the plain pairing |
| $H(Q_1,Q_2)=Q_1\bar Q_2$ | the Hermitian pairing |
| $L_{Q_1}$, $R_{Q_1}$ | the left and right multiplications; they coincide |
| $L_{Q_1}^{\dagger}=L_{\bar Q_1}$ | the adjoint of the left multiplication for $H$ |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the slot conventions of a product with an involution and the class-preserving exchanges.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for bilinear and sesquilinear maps, their adjoints and the non-degenerate pairings.
- Serge Lang, *Algebra*, Graduate Texts in Mathematics 211 (Springer, third edition, 2002), for the field product, its laws and the construction of a sesquilinear form from a linear one.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the comparison of a bilinear and a sesquilinear multiplication over a commutative ring with an involution.
