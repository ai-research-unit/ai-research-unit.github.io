# __The Two General Products and the Reason There Are Only Two__

## Introduction

The quaternion algebra $\mathbb{H}$ carries, besides the algebra product of the *Quaternions* category, the companion products of this category, and they all descend from two multiplications. This article states the general construction that produces those multiplications, proves that exactly two general products arise over $\mathbb{R}$, and reads the companion products the two generate. It is the synthesis article of the block. The two general products, with their laws and their tables, are *The Two General Products of the Quaternioid $\mathbb{R}$ Space*; the six products their halves produce are *The 6 Products of the Quaternioid Real Space*; the three companion structures and their names are *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; this article re-derives none of them. What it owns is the construction, the count, and the passage from the two general products to the companion products. The forms the products carry are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*; the norms are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*; both are below this article in this category.

## The General Construction

A **general product** on the quaternion algebra $\mathbb{H}$ is a bilinear or sesquilinear map obtained by choosing, independently, how each of its two slots reads its argument: through the identity or through the natural conjugation ${}^{\natural}$. The two choices are the two **slot pairings** of each side, and the products are the four pairings

$$
(\mathrm{id},\mathrm{id}) ,\quad (\mathrm{id},{}^{\natural}) ,\quad ({}^{\natural},\mathrm{id}) ,\quad ({}^{\natural},{}^{\natural}) .
$$

The choice is the insertion of the conjugation in one slot, in the other, in both, or in none. The algebra $\mathbb{H}$ and its conjugation are the only data; there is no further involution of the coefficients to insert, because the base field $\mathbb{R}$ carries a single involution, the identity.

## The Coincidence of the Two Slots over $\mathbb{R}$

**Theorem.** The two slot pairings with the conjugation in the second slot are the two pairings with the conjugation in the first slot, read with both arguments conjugated. Exactly two distinct products therefore arise from the four pairings.

**Proof.** The conjugation in the second slot and the conjugation in the first slot are the same map ${}^{\natural}$, because the base field $\mathbb{R}$ has a single involution, the identity, so the coefficientwise bar is the identity and the only conjugation available is ${}^{\natural}$. Hence

$$
(\mathrm{id},{}^{\natural})\ \text{is}\ ({}^{\natural},\mathrm{id})\ \text{read at}\ (\tilde q_1^{\natural},\tilde q_2^{\natural}) , \qquad
({}^{\natural},{}^{\natural})\ \text{is}\ (\mathrm{id},\mathrm{id})\ \text{read at}\ (\tilde q_1^{\natural},\tilde q_2^{\natural}) ,
$$

that is, the quaternionic product and the plain product with both arguments conjugated. The four pairings therefore carry the two products

$$
\tilde q_1\tilde q_2\quad(\text{general plain}) , \qquad \tilde q_1^{\natural}\tilde q_2\quad(\text{general quaternionic}) .
$$

**Table (the four pairings, the two products).**

| pairing | product |
|---|---|
| $(\mathrm{id},\mathrm{id})$ | $\tilde q_1\tilde q_2$ |
| $({}^{\natural},\mathrm{id})$ | $\tilde q_1^{\natural}\tilde q_2$ |
| $(\mathrm{id},{}^{\natural})$ | $\tilde q_1\tilde q_2^{\natural}$, the quaternionic product read at $(\tilde q_1^{\natural},\tilde q_2^{\natural})$ |
| $({}^{\natural},{}^{\natural})$ | $\tilde q_1^{\natural}\tilde q_2^{\natural}$, the plain product read at $(\tilde q_1^{\natural},\tilde q_2^{\natural})$ |

## The Reason There Are Only Two

The count is two because the algebra has a single non-trivial conjugation and the base field none. A general product inserts a conjugation into a slot; the conjugations available are the identity and ${}^{\natural}$; inserting ${}^{\natural}$ in the second slot gives the first-slot products read at conjugated arguments, not a new product. A third product would require a second independent conjugation on the elements, which the quaternion algebra over $\mathbb{R}$ does not have. The two products $\tilde q_1\tilde q_2$ and $\tilde q_1^{\natural}\tilde q_2$ are thus the whole list of general products, and the whole operational vocabulary of the chapter is built from them.

## The Companion Structures the Two Products Generate

Each general product splits into a **symmetric part** and an **antisymmetric part** under the exchange of its two slots. Over $\mathbb{R}$ the base ring has no nontrivial involution, the two slots are both linear, and the exchange is the bare interchange of the two arguments, so the split is

$$
\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2 ,\qquad
\tilde q_1^{\natural}\tilde q_2=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t+\tilde q_1\wedge^{\natural}\tilde q_2 ,
$$

with the four halves

$$
\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1) ,\qquad
\tilde q_1\wedge\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2 ,
$$

$$
\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t=\tfrac12(\tilde q_1^{\natural}\tilde q_2+\tilde q_2^{\natural}\tilde q_1) ,\qquad
\tilde q_1\wedge^{\natural}\tilde q_2=\tfrac12(\tilde q_1^{\natural}\tilde q_2-\tilde q_2^{\natural}\tilde q_1) .
$$

The two general products and their four halves are the six products of the chapter, and three of them — the symmetric plain, the antisymmetric plain and the general quaternionic — carry the companion structures. The two indices that name them are the **family**, plain or quaternionic, and the **half**, general, symmetric or antisymmetric:

| half | plain | quaternionic |
|---|---|---|
| general | $\tilde q_1\tilde q_2$, the *Quaternions* algebra product | $\mathrm{GQA}$, $\tilde q_1^{\natural}\tilde q_2$ |
| symmetric | $\mathrm{SPA}$, $\tilde q_1\bullet\tilde q_2$ | $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$, the scalar-valued symmetrisation |
| antisymmetric | $\mathrm{APA}$, $\tilde q_1\wedge\tilde q_2$ | $\tilde q_1\wedge^{\natural}\tilde q_2$, the quaternionic cross product |

**Theorem (the two general products generate the companion products, and no more).** The split of the two general products under the interchange of their slots produces exactly four halves, the two general products together with the four halves are six distinct products, and the three companion structures of the category are the symmetric plain, the antisymmetric plain and the general quaternionic one.

*Proof.* The reconstruction above writes each general product as the sum of its symmetric and antisymmetric part, so the four halves are determined by the two general products, and conversely each general product is recovered as the sum of its two halves. The four halves are distinct from the two general products and from one another. The Jordan product differs from the plain product by the cross term, $\tilde q_1\bullet\tilde q_2=\tilde q_1\tilde q_2-\vec q_1\times\vec q_2$, which is nonzero on $(\vec e_x,\vec e_y)$; the symmetric quaternionic product is scalar, valued in $\mathbb{R}e_t$, while the general quaternionic product is not, its value on $(e_t,\vec e_x)$ being $\vec e_x$; the cross product is pure vector while the plain product is not; and the quaternionic cross product is pure vector, its value on $(e_t,\vec e_x)$ being $\vec e_x$ while its scalar part vanishes. Together these witnesses separate the four halves from the two general products and from one another, and no bilinear rule has more than its symmetric and its antisymmetric part. Hence the split produces no seventh product, and no companion product is missed.

**Remark (the plain triple and the quaternionic triple).** The plain triple is the multiplication of $\mathbb{H}$, its Jordan symmetrisation and its commutator; the quaternionic triple is the same three-fold split of the product whose first factor carries the conjugation, and the conjugation changes the sign of the antisymmetric term and turns the dot product of the symmetric term into its negative, which is why the symmetric half of the quaternionic product is the scalar $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$ and not the Jordan product. In the two triples the antisymmetric half is alternating in each, and the two triples separate on the symmetric side: the plain symmetric half $\mathrm{SPA}$ is a Jordan algebra, the scalar-valued symmetrisation of the quaternionic product $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$ is not.

**Remark (the count of the chapter).** The reason there are two general products is the reason the category keeps three companion structures. The algebra has one nontrivial conjugation and the base field none, so the slot construction yields two general products; each general product yields exactly two halves; two general products therefore yield four halves, of which three carry the companion structures. A third general product would need a second independent conjugation on the elements, and a seventh structure would need a bilinear rule with more than a symmetric and an antisymmetric part; neither exists over $\mathbb{R}$.

## Summary

A general product on $\mathbb{H}$ is a slot pairing of the identity and the natural conjugation. Since the two slots read the same conjugation, the pairings with the conjugation in the second slot repeat those with it in the first, read with both arguments conjugated, and exactly two general products arise: the general plain product $\tilde q_1\tilde q_2$ and the general quaternionic product $\tilde q_1^{\natural}\tilde q_2$.

Each general product splits under the interchange of its slots into a symmetric and an antisymmetric part, and the split produces the four halves: the Jordan product $\tilde q_1\bullet\tilde q_2$, the quaternion form read as a product $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$, the cross product $\tilde q_1\wedge\tilde q_2=\vec q_1\times\vec q_2$, and the quaternionic cross product $\tilde q_1\wedge^{\natural}\tilde q_2$. The two general products and the four halves are six distinct products; three of them carry the companion structures, $\mathrm{SPA}$, $\mathrm{APA}$ and $\mathrm{GQA}$, indexed by the family and the half; the reconstruction $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$ and $\tilde q_1^{\natural}\tilde q_2=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t+\tilde q_1\wedge^{\natural}\tilde q_2$ recovers the two general products, and no seventh product exists. The count is two because the algebra carries one nontrivial conjugation and the base field none.

## Summary of Notation

| symbol | meaning |
|---|---|
| ${}^{\natural}$ | the natural conjugation, the anti-involution of the algebra |
| $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{\natural})$, $({}^{\natural},{}^{\natural})$ | the four slot pairings |
| $\tilde q_1\tilde q_2$, $\tilde q_1^{\natural}\tilde q_2$ | the two general products |
| $\tilde q_1\bullet\tilde q_2$, $\tilde q_1\wedge\tilde q_2$ | the symmetric and the antisymmetric half of the plain product |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$, $\tilde q_1\wedge^{\natural}\tilde q_2$ | the symmetric and the antisymmetric half of the quaternionic product |
| $\mathrm{SPA},\mathrm{APA},\mathrm{GQA}$ | the three companion structures of the category |

## Further Reading

- [The Two General Products of the Quaternioid $\mathbb{R}$ Space](the-two-general-products-of-the-quaternioid-r-space.html), for the two products in coordinates.
- [The 6 Products of the Quaternioid Real Space](the-6-products-of-the-quaternioid-real-space.html), for the split and the four halves on the coordinates.
- [The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](the-algebraic-structures-over-the-quaternioid-r-space.html), for the names and the law table.
- [Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.html), below this article in this category, for the first of the element theories read across the companion products.
