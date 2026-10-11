# __Remarkable Subspaces and the Two Products__

## Introduction

The complex space carries two products, the **general plain bilinear product** $AC$ and the **general plain sesquilinear product** $A\bar C$, the reading on $\mathbb{C}$ of the four general products of the biquaternion algebra (*The Two Products of the Complex Space*). This article reads the two products on the two remarkable subspaces of the complex algebra, the real subspace $\mathbb{R}_{\mathbb{C}}$ and the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$, one subspace to a section, and collects the outcome in the table of the two.

The article is the complex counterpart of *Remarkable Subspaces and the Four General Products*, which reads the four general products of $\mathbb{B}$ on the six remarkable subspaces. Its result is a collapse, and it is written so that the collapse is visible: the four products become two, the six subspaces become two, and — the fact specific to $\mathbb{C}$ — the two products share one and the same closure table, so the closure of the subspaces cannot tell the two products apart.

The subspaces are those of *Complex Subspaces*; the two involutions and the field are those of *Complex Algebra*, below this article in this category; the products are those of *The Two Products of the Complex Space*; the forms the products carry are *The Two Forms and the Two Algebraic Norms of the Complex Space*, and their restriction to the two subspaces is *Remarkable Subspaces of the Complex Numbers and the Two Forms*, both below this article in this category. The multiplication $AC$ is owned by *Complex Algebra*, and the topological norm, the invertibility criterion and the group of units are *Complex Norm and Invertibility*, both below this article in this category.

**Conventions.** The complex space is read over itself and as the centre of the biquaternion algebra $\mathbb{B}$: **bar** is complex conjugation, the **natural sign** is the identity on a commutative base, and the **Hermitian** mark is the bar, ${}^{*}=\bar{\cdot}$. Elements are written $A=a+ia'$ and $C=c+ic'$, and the letter $B$ is not used for an element, since $B$, $N$, $H$, $K$ are the four forms, of which $B$ and $H$ survive. The complex block (*Complex Algebra*, *Complex Subspaces*) reads $\mathbb{C}$ over $\mathbb{R}$ and calls the bar "the natural conjugation"; here *natural* keeps its global sense of the biquaternion conjugation, which is the identity on $\mathbb{C}$.

## The Two Subspaces and the Two Products

The two subspaces are the fixed subspace and the anti-fixed subspace of the bar,

$$
\mathbb{R}_{\mathbb{C}}=\{A:\bar A=A\}=\mathbb{R}1,\qquad i\mathbb{R}_{\mathbb{C}}=\{A:\bar A=-A\}=\mathbb{R}i,
$$

each of real dimension one, with $\mathbb{C}=\mathbb{R}_{\mathbb{C}}\oplus i\mathbb{R}_{\mathbb{C}}$ (*Complex Subspaces*). On the coordinates $A=a+ia'$ and $C=c+ic'$, the two products are

$$
AC=(ac-a'c')+i(ac'+a'c'),\qquad A\bar C=(ac+a'c')+i(a'c-ac').
$$

The four general products of the biquaternion method are $(\mathrm{id},\mathrm{id})$, $(\natural,\mathrm{id})$, $(\mathrm{id},{}^{*})$ and $(\natural,{}^{*})$, the natural sign in the first slot and the Hermitian mark in the second; on $\mathbb{C}$ the natural sign is the identity and the Hermitian mark is the bar, so the pair $(\natural,\mathrm{id})$ gives $AC$ exactly as $(\mathrm{id},\mathrm{id})$ does, and the pair $(\natural,{}^{*})$ gives $A\bar C$ exactly as $(\mathrm{id},{}^{*})$ does. The four products therefore take two values, and no product of the space is a third operation (*The Two Products of the Complex Space*).

## The Real Subspace

An element of the real subspace is $A=a$, and the two products agree on the whole of it, since $\bar C=C$ for a real $C$. The product of two elements is $ac$, real, so the subspace is closed under both products; it is a subalgebra and a field, isomorphic to $\mathbb{R}$ (*Complex Subspaces*). Its units are all its nonzero elements, its idempotents are $0$ and $1$ alone, and neither product has a nonzero isotropic element in it, since $a^2=0$ and $a\bar a=a^2=0$ force $a=0$. The sesquilinear product reduces there to the plain one, $A\bar C=AC$, and the two products are told apart by no element of the subspace.

## The Imaginary Subspace

An element of the imaginary subspace is $A=ia'$, and each product sends a pair of its elements out of the subspace,

$$
(ia')(ic')=-a'c'\in\mathbb{R}_{\mathbb{C}},\qquad (ia')\overline{(ic')}=+a'c'\in\mathbb{R}_{\mathbb{C}},
$$

so the subspace is closed under neither product; the failure is not a defect of the sesquilinear product alone, since the plain product leaves the subspace exactly as the sesquilinear one does. The two products differ on the subspace by a sign, because $\bar C=-C$ for an imaginary $C$, and there they are opposite,

$$
A\bar C=-AC\qquad(A,C\in i\mathbb{R}_{\mathbb{C}}).
$$

The subspace contains no idempotent but $0$, because $A^2=-a'^2$ is real and can equal the imaginary $A=ia'$ only when $a'=0$; it contains no nonzero isotropic element, since $A^2=-a'^2$ and $A\bar A=+a'^2$ vanish only for $a'=0$; and every nonzero element is a unit of $\mathbb{C}$, with inverse $-i/a'$, which lies in the subspace again. The subspace is therefore closed under inversion and under neither product.

## The Table of the Two

The two products on the four pairs of subspaces. The values are written with the coordinates $A=a$ on the real subspace and $A=ia'$ on the imaginary one, and the closure is read as the subspace in which the value lands.

| first slot | second slot | the plain product $AC$ | the sesquilinear product $A\bar C$ |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{C}}$ | $ac\in\mathbb{R}_{\mathbb{C}}$ | $ac\in\mathbb{R}_{\mathbb{C}}$ |
| $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ | $iac'\in i\mathbb{R}_{\mathbb{C}}$ | $-iac'\in i\mathbb{R}_{\mathbb{C}}$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{C}}$ | $ia'c\in i\mathbb{R}_{\mathbb{C}}$ | $ia'c\in i\mathbb{R}_{\mathbb{C}}$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ | $-a'c'\in\mathbb{R}_{\mathbb{C}}$ | $a'c'\in\mathbb{R}_{\mathbb{C}}$ |

The two products have **the same closure table**: the real subspace is closed under both, the imaginary subspace under neither, the mixed products land in the imaginary subspace, and the product of two imaginary elements lands in the real subspace. The values differ only in the two cells whose second slot is imaginary, and there by a sign, because the bar acts on the second slot alone. The closure of the subspaces therefore does not separate the two products, and the separation needs the values, and with them the imaginary elements.

The element theory of the two subspaces is this.

| subspace | units | idempotents | isotropic elements |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | every nonzero element | $0$ and $1$ | $0$ alone |
| $i\mathbb{R}_{\mathbb{C}}$ | every nonzero element, inverse in the subspace | $0$ alone | $0$ alone |

Both products give the same table, since the isotropic sets are read from $B(A)=A^2$ and $H(A)=A\bar A$, and both vanish only at the origin on either subspace; the two vanishings are the anisotropy of the two forms (*Remarkable Subspaces of the Complex Numbers and the Two Forms*, below this article in this category).

## The Collapse of the Biquaternion Interpretation

On $\mathbb{B}$ the four general products are read on six remarkable subspaces, and on each subspace the four have one and the same value set, the span of the plain product (*Remarkable Subspaces and the Four General Products*). The complex reading is that article collapsed on both counts. **In the products:** the natural sign is the identity, so the plain and the quaternionic family of each pair carry the same operation and the four general products become two. **In the subspaces:** the lattice of the biquaternion algebra collapses to the two members $\mathbb{R}_{\mathbb{C}}$ and $i\mathbb{R}_{\mathbb{C}}$, a collapse read in *Decompositions and Comparison of the Remarkable Subspaces of the Complex Numbers*, above this article in this category, together with the closure, the units and the isotropic elements that the two subspaces hold. The two surviving products then share one and the same closure table, because the bar fixes the real line and negates the imaginary one and closure is blind to the sign: the closure of a subspace decides no product.

The collapse preserves one feature of the biquaternion table and destroys another. The multiplicative shape of the subspaces is preserved: one closed line, the real one, which is a field, against one line that is stable under inversion and closed under no product, the imaginary one. The distinction between a plain and a quaternionic product is destroyed: the trivial natural sign erases it, and the two families give one and the same operation.

## Summary

The complex space carries two products, $AC$ and $A\bar C$, and two remarkable subspaces, the real line $\mathbb{R}_{\mathbb{C}}$ and the imaginary line $i\mathbb{R}_{\mathbb{C}}$. The two products have the same closure table on the two subspaces: the real subspace is closed under both and is the field $\mathbb{R}_{\mathbb{C}}\cong\mathbb{R}$, the imaginary subspace is closed under neither and its products land in the real subspace, the mixed products land in the imaginary subspace. The values of the two products differ only in the two cells whose second slot is imaginary, and there by a sign, because the bar acts on the second slot alone; on the imaginary subspace the two products are opposite, $A\bar C=-AC$.

The real subspace carries the units all its nonzero elements, the idempotents $0$ and $1$, and no nonzero isotropic element; the imaginary subspace carries the units all its nonzero elements with the inverse in the subspace, the idempotent $0$ alone, and no nonzero isotropic element. The reading is the collapse of the biquaternion reading of the four general products on six subspaces: two products in place of four, one closure table in place of the two value sets, and two real lines in place of the six remarkable subspaces.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2=-1$ |
| $A=a+ia'$, $C=c+ic'$ | elements of the space |
| $\mathbb{R}_{\mathbb{C}}=\mathbb{R}1$ | the real subspace, fixed by the bar, real dimension $1$ |
| $i\mathbb{R}_{\mathbb{C}}=\mathbb{R}i$ | the imaginary subspace, anti-fixed by the bar, real dimension $1$ |
| $AC$ | the general plain bilinear product, the multiplication of the field |
| $A\bar C$ | the general plain sesquilinear product |
| $\bar{\cdot}$ | complex conjugation, the bar; the natural sign is the identity |
| $B$, $H$ | the two forms, $B(A,C)=AC$ and $H(A,C)=A\bar C$ |

## Further Reading

- *The Two Products of the Complex Space*, for the two products, their definitions and the collapse of the four general products to them.
- *Complex Subspaces* (`articles_maths/complex-subspaces.md`), for the two subspaces, their bases, their dimensions and the closure of the real subspace.
- *Complex Algebra* (`articles_maths/complex-algebra.md`), for the field structure of the real subspace and the multiplication $AC$.
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the biquaternion reading of the four general products on the six subspaces, of which this article is the collapse.
- *The Two Forms and the Two Algebraic Norms of the Complex Space* and *Remarkable Subspaces of the Complex Numbers and the Two Forms*, below this article in this category, for the two forms and their restriction to the two subspaces.
