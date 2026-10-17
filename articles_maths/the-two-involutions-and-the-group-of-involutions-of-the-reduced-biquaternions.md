# __The Two Involutions and the Group of Involutions__

## Introduction

The reduced biquaternion algebra carries **two** involutions of the coefficient sector and a group of four maps they generate. The **bar** conjugates the two complex coordinates, $\overline{Q_++jQ_-}=\bar Q_++j\bar Q_-$; the **natural sign** negates the second slot, $(Q_++jQ_-)^{\natural}=Q_+-jQ_-$. Their composite is the **star**, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, $(Q_++jQ_-)^{*}=\bar Q_+-j\bar Q_-$; and the negative of the star is the **flat**, ${}^{\flat}=-{}^{*}$. The star and the bar and the natural sign generate the **Klein four-group** $\{\mathrm{id},\bar{\cdot},{}^{\natural},{}^{*}\}$, and the flat stands outside it as the reversal of the star.

The two involutions are what make this layer richer than a single-conjugation algebra. The **natural sign** is the **intrinsic conjugate** of the space: it fixes the scalar line $\mathbb{C}$ and negates the $j$-line $\mathbb{C}j$ (*Conventions in Mathematics*, §*The Conjugations*). The **bar** is the coefficient conjugation, and it exists because the coefficients are complex; the split-complex numbers $\mathbb{D}$ have no coefficient conjugation, their coefficients being real, and the complex numbers $\mathbb{C}$ have no natural sign, so the reduced biquaternions are the first layer carrying the two maps independently. The two are independent, they commute, and their composite is a third involution, the star, which is the one the two sesquilinear products use.

This article fixes the four maps, their fixed and anti-fixed spaces and the group they generate, following *The Group of Involutions* of the biquaternion category article for article. The four general products and the forms and algebraic norms they carry are *The Four Products, Their Forms and Their Algebraic Norms*, below this article in this category; the four maps are named there and proved here. The remarkable subspaces as subspaces are *Introduction to the Remarkable Subspaces*, below this article in this category; the fixed spaces are computed here because they are what fixes the involutions.

**The results.** The bar, the natural sign and the star are involutions of the algebra; they commute pairwise, and $\{\mathrm{id},\bar{\cdot},{}^{\natural},{}^{*}\}$ is a Klein four-group with the multiplication ${}^{*}\circ{}^{*}=\mathrm{id}$, ${}^{*}\circ\bar{\cdot}={}^{\natural}$, ${}^{*}\circ{}^{\natural}=\bar{\cdot}$, so that each of the three non-identity marks is the composite of the other two. The bar and the star are $\mathbb{C}$-antilinear, the natural sign is $\mathbb{C}$-linear. Every one of the three is an **algebra automorphism**, because the algebra is commutative: the order-reversing character of the natural sign and of the star over the non-commutative biquaternions disappears. The flat is not an involution of the group; it is the negative of the star, it exchanges the star's fixed and anti-fixed spaces, and it is not multiplicative, $(\lambda Q_\pm)^{\flat}=\bar\lambda Q_\pm^{\flat}$ and $(Q_{\pm,1}Q_{\pm,2})^{\flat}=-Q_{\pm,1}^{\flat}Q_{\pm,2}^{\flat}$.

**Boundaries.** The space, the bases and the linear or antilinear character of the maps are *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*, above this article in this category. The idempotents $\Pi_{\pm}$ and their fixed or exchanged behaviour are *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*, below this article, and the idempotent decomposition is *Reduced Biquaternion Space*. The products are used here only as far as the multiplicativity of the maps requires.

## The Two Involutions

### The Bar

**The bar conjugates the two complex coordinates and is the coefficientwise complex conjugation of the algebra.**

**Definition.** The **bar** is the map
$$
\overline{Q_++jQ_-}=\bar Q_++j\bar Q_-,\qquad \bar Q_+=q_+-iq'_+,\quad \bar Q_-=q_--iq'_-.
$$

**Proposition.** The bar is an involution, it is $\mathbb{R}$-linear and $\mathbb{C}$-antilinear, it fixes $1$ and $j$ and negates $i$ and $ij$:
$$
\bar1=1,\qquad \bar i=-i,\qquad \bar j=j,\qquad \overline{ij}=-ij,\qquad \overline{\bar Q_\pm}=Q_\pm,\qquad \overline{Q_{\pm,1}Q_{\pm,2}}=\overline{Q_{\pm,1}}\,\overline{Q_{\pm,2}} .
$$

*Proof.* Applying the bar twice returns $Q_+$ and $Q_-$, so it is an involution; it is real-linear because the complex conjugation is; it is antilinear because $\overline{\lambda Q_+}=\bar\lambda\bar Q_+$; and on the basis $1=1+0j$, $i=i+0j$, $j=0+1j$, $ij=i\cdot j$ it gives $\bar1=1$, $\bar i=-i$, $\bar j=j$, $\overline{ij}=\bar i\bar j=(-i)j=-ij$. The multiplicativity is the multiplicativity of the complex conjugation on the two coordinates together with the commutativity of the product.

The bar is the involution of the **coefficient sector**. It is the only one of the four maps that has a sense over any complex algebra, and over the split-complex numbers $\mathbb{D}$ the coefficientwise conjugation degenerates to the identity because the coefficients are real.

### The Natural Sign

**The natural sign negates the second slot, and it is the intrinsic conjugate of the algebra: it fixes the scalar line $\mathbb{C}$ and negates the $j$-line $\mathbb{C}j$.**

**Definition.** The **natural sign** is the map
$$
(Q_++jQ_-)^{\natural}=Q_+-jQ_-.
$$

**Proposition.** The natural sign is an involution, it is $\mathbb{C}$-linear, it fixes $1$ and $i$ and negates $j$ and $ij$:
$$
1^{\natural}=1,\qquad i^{\natural}=i,\qquad j^{\natural}=-j,\qquad (ij)^{\natural}=-ij,\qquad (Q_\pm^{\natural})^{\natural}=Q_\pm,\qquad (Q_{\pm,1}Q_{\pm,2})^{\natural}=Q_{\pm,1}^{\natural}Q_{\pm,2}^{\natural}.
$$

*Proof.* Applying the natural sign twice returns $Q_++jQ_-$, so it is an involution; it is $\mathbb{C}$-linear because $\lambda(Q_++jQ_-)=(\lambda Q_+)+(\lambda Q_-)j$ maps to $(\lambda Q_+)-(\lambda Q_-)j=\lambda(Q_+-jQ_-)$; on the basis, $1^{\natural}=1$, $i^{\natural}=i$ (both have vanishing second coordinate), $j^{\natural}=-j$ and $(ij)^{\natural}=-ij$ (both have vanishing first coordinate). Multiplicativity follows from the commutativity of the product and the sign rule $j^{2}=+1$.

The natural sign is the **intrinsic conjugate** of the algebra in the sense of *Conventions in Mathematics*: it fixes the scalars — its fixed space is the scalar line $\mathbb{C}$ — and negates the vectors — its anti-fixed space is the $j$-line. It is the map that the engineering literature writes on a reduced biquaternion, and it is the analogue of the quaternion conjugation ${}^{\natural}$ of the biquaternion layer, with the second slot in place of the three vector coordinates.

### The Star and the Flat

**The star is the composite of the bar and the natural sign, it conjugates the two coordinates with the second negated, and the flat is its negative.**

**Definition.** The **star** is the composite ${}^{*}=\bar{\cdot}\circ{}^{\natural}={}^{\natural}\circ\bar{\cdot}$,
$$
(Q_++jQ_-)^{*}=\bar Q_+-j\bar Q_-,
$$
and the **flat** is its negative, ${}^{\flat}=-{}^{*}$,
$$
(Q_++jQ_-)^{\flat}=-\bar Q_++j\bar Q_-.
$$

**Proposition.** The star is an involution and is $\mathbb{C}$-antilinear; it fixes $1$ and $ij$ and negates $i$ and $j$:
$$
1^{*}=1,\qquad i^{*}=-i,\qquad j^{*}=-j,\qquad (ij)^{*}=ij,\qquad (Q_\pm^{*})^{*}=Q_\pm,\qquad (Q_{\pm,1}Q_{\pm,2})^{*}=Q_{\pm,1}^{*}Q_{\pm,2}^{*}.
$$
The flat is not multiplicative, so it is not an involution of the algebra, although its square is the identity; it is antilinear, it exchanges the star's fixed and anti-fixed spaces, and it twists the product by a sign:
$$
Q_\pm^{\flat}=-Q_\pm^{*},\qquad (Q_\pm^{\flat})^{\flat}=Q_\pm,\qquad (Q_{\pm,1}Q_{\pm,2})^{\flat}=-Q_{\pm,1}^{\flat}Q_{\pm,2}^{\flat}.
$$

*Proof.* The star is the composite of two commuting involutions, so it is an involution; it is antilinear as the composite of an antilinear and a linear map; on the basis, $1$ and $ij$ are fixed ($\overline{ij}=-ij$ while $(ij)^{\natural}=-ij$, so $(ij)^{*}=(-ij)^{\natural}=ij$), while $i$ and $j$ are negated. The multiplicativity of the star follows from that of the bar and the natural sign. For the flat, $Q_\pm^{\flat}=-Q_\pm^{*}$ is a scalar multiple of an involution, so its square is the identity, and $Q_\pm^{\flat}=Q_\pm$ is $Q_\pm^{*}=-Q_\pm$, which is the anti-fixed condition of the star read with the sign changed; the last display is $(-Q_{\pm,1}^{*}Q_{\pm,2}^{*})=-(Q_{\pm,1}^{*}Q_{\pm,2}^{*})$ and $Q_{\pm,1}^{\flat}Q_{\pm,2}^{\flat}=(+Q_{\pm,1}^{*}Q_{\pm,2}^{*})$, whose sum with $(Q_{\pm,1}Q_{\pm,2})^{\flat}=-Q_{\pm,1}^{*}Q_{\pm,2}^{*}$ is zero.

**Remark (why the star is the odd one).** The star is the only one of the three involutions of the group that negates one direction in each of the two lines $\mathbb{C}$ and $\mathbb{C}j$; the bar conjugates the coefficients and the natural sign negates the whole $j$-part. The star is the involution that the two sesquilinear products use in their second slot, and its fixed space is the plane $\mathbb{R}\{1,ij\}$, which is neither the scalar line nor the $j$-line.

## The Fixed and Anti-Fixed Spaces

**Each involution splits the real four-dimensional space into a fixed and an anti-fixed space, each of real dimension two, and the three splits are the three ways of cutting the space into a plane and its complement.**

**Definition.** For an involution $\sigma$ of $\mathbb{B}_{\mathrm{r}}$, the **fixed space** is $\{Q_\pm:\sigma(Q_\pm)=Q_\pm\}$ and the **anti-fixed space** is $\{Q_\pm:\sigma(Q_\pm)=-Q_\pm\}$.

**Theorem (the six spaces).** The fixed and anti-fixed spaces of the bar, the natural sign and the star are the following real subspaces, each of real dimension two:

| involution | fixed space | anti-fixed space |
|---|---|---|
| bar $\bar{\cdot}$ | $\mathbb{R}\{1,j\}$, the real subalgebra | $\mathbb{R}\{i,ij\}=i\mathbb{R}\{1,j\}$ |
| natural sign ${}^{\natural}$ | $\mathbb{C}=\mathbb{R}\{1,i\}$, the scalar line | $\mathbb{R}\{j,ij\}=j\mathbb{C}$, the $j$-line |
| star ${}^{*}$ | $\mathbb{R}\{1,ij\}$ | $\mathbb{R}\{i,j\}$ |

*Proof.* The action on the real basis $1,i,j,ij$ is read from the three displays above: the bar fixes $1,j$ and negates $i,ij$; the natural sign fixes $1,i$ and negates $j,ij$; the star fixes $1,ij$ and negates $i,j$. Each fixed space is therefore the real span of the two fixed basis elements, and each anti-fixed space the span of the two negated ones; a basis element is either fixed or negated, so the two spaces span the whole space and have real dimension two. The identifications with the real subalgebra, the scalar line and the $j$-line are the descriptions of *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*.

**Corollary (the flat reproduces the star's spaces).** The flat has the same fixed and anti-fixed spaces as the star with the two exchanged: the flat fixes $\mathbb{R}\{i,j\}$ and negates $\mathbb{R}\{1,ij\}$, so it adds no new space, exactly as in the biquaternion category.

*Proof.* $Q_\pm^{\flat}=Q_\pm$ reads $-Q_\pm^{*}=Q_\pm$, that is $Q_\pm^{*}=-Q_\pm$, the anti-fixed condition of the star; so the fixed space of the flat is the anti-fixed space of the star, and its anti-fixed space is the fixed space of the star.

## The Group of Involutions

### The Composition Table

**The bar, the natural sign and the star close with the identity under composition, and the composition is that of the Klein four-group.**

**Theorem (the group).** The four maps $\mathrm{id},\bar{\cdot},{}^{\natural},{}^{*}$ form a group under composition, isomorphic to $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$:

| $\circ$ | $\mathrm{id}$ | $\bar{\cdot}$ | ${}^{\natural}$ | ${}^{*}$ |
|---|---|---|---|---|
| $\mathrm{id}$ | $\mathrm{id}$ | $\bar{\cdot}$ | ${}^{\natural}$ | ${}^{*}$ |
| $\bar{\cdot}$ | $\bar{\cdot}$ | $\mathrm{id}$ | ${}^{*}$ | ${}^{\natural}$ |
| ${}^{\natural}$ | ${}^{\natural}$ | ${}^{*}$ | $\mathrm{id}$ | $\bar{\cdot}$ |
| ${}^{*}$ | ${}^{*}$ | ${}^{\natural}$ | $\bar{\cdot}$ | $\mathrm{id}$ |

so that each non-identity member is the composite of the other two,
$$
{}^{*}=\bar{\cdot}\circ{}^{\natural}={}^{\natural}\circ\bar{\cdot},\qquad
\bar{\cdot}={}^{\natural}\circ{}^{*}={}^{*}\circ{}^{\natural},\qquad
{}^{\natural}={}^{*}\circ\bar{\cdot}=\bar{\cdot}\circ{}^{*}.
$$

*Proof.* The maps commute pairwise, since the bar and the natural sign act on different data — the coefficients and the second slot — and the star is their composite; each is an involution; and no two of the three non-identity members are equal, as their actions on the basis differ (for instance the bar fixes $j$ while the star negates it). A group of three commuting involutions with the pairwise products the third is $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$.

### The Flat Stands Outside the Group

**The flat is not in the Klein group: it is the negative of the star, and it is closed under composition with itself but not with the others.**

The flat satisfies ${}^{\flat}=-{}^{*}$, so it is not one of the four maps of the group; the set $\{\mathrm{id},\bar{\cdot},{}^{\natural},{}^{*},{}^{\flat}\}$ is not closed, because ${}^{\flat}\circ{}^{\flat}=\mathrm{id}$ but the flat composed with the bar is $-\natural$, which is not in the list. The reversal is the same as in the biquaternion category: the flat is the anti-Hermitian conjugation, its role is to exchange the star's eigenspaces, and it is written on elements and never on operators, the **dagger** being reserved for the adjoint of an operator (*Conventions in Mathematics*, §*The Conjugations*).

### The Linear and Antilinear Characters

**The natural sign is $\mathbb{C}$-linear; the bar, the star and the flat are $\mathbb{C}$-antilinear; and this is the clause that separates the two slots of the four general products.**

The action on the scalar $\lambda\in\mathbb{C}$ is
$$
(\lambda Q_\pm)^{\natural}=\lambda\,Q_\pm^{\natural},\qquad
\overline{\lambda Q_\pm}=\bar\lambda\,\overline{Q_\pm},\qquad
(\lambda Q_\pm)^{*}=\bar\lambda\,Q_\pm^{*},\qquad
(\lambda Q_\pm)^{\flat}=\bar\lambda\,Q_\pm^{\flat}.
$$
The four displays are the four rows of *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*, §*Linear and Antilinear Maps*, read as maps of the algebra; the natural sign is the only linear one, and it is the reason a product with the natural sign in its first slot stays $\mathbb{C}$-linear in that slot.

## The Involutions and the Algebra

**Because the algebra is commutative, the bar, the natural sign and the star are algebra automorphisms, and the order-reversing character they have over the non-commutative biquaternions does not occur.**

**Theorem (the three marks are automorphisms).** Each of the bar, the natural sign and the star satisfies
$$
\sigma(Q_{\pm,1}Q_{\pm,2})=\sigma(Q_{\pm,1})\sigma(Q_{\pm,2}),\qquad \sigma(1)=1,\qquad \sigma(\lambda Q_\pm)=\lambda\sigma(Q_\pm)\ \text{or}\ \bar\lambda\sigma(Q_\pm),
$$
so each is a ring automorphism, the natural sign over $\mathbb{C}$ and the bar and the star over $\mathbb{C}$ with the conjugation.

*Proof.* The multiplicativity of each is the last display of the three propositions above. The identity is fixed by all three, as read on the basis. For the scalar action, the natural sign is linear and the bar and the star are antilinear. The word **automorphism** replaces the word **anti-automorphism** of the biquaternion category because $Q_{\pm,1}Q_{\pm,2}=Q_{\pm,2}Q_{\pm,1}$, so the order of the factors never has to be reversed.

**Remark (what the automorphism group of the algebra is).** The three involutions of the group are automorphisms, and they are not all the automorphisms of $\mathbb{B}_{\mathrm{r}}$: the componentwise permutations of the two copies of $\mathbb{C}$ in $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$ that are continuous, and the other automorphisms of the algebra, are *Reduced Biquaternion Automorphisms and Derivations*, below this article in this category. This article keeps only the four maps of the group and their eigenspaces.

**Corollary (the idempotents under the involutions).** The natural sign and the star both exchange the two idempotents, $\Pi_+^{\natural}=\Pi_-=\Pi_+^{*}$ and $\Pi_-^{\natural}=\Pi_+=\Pi_-^{*}$; only the bar fixes each idempotent, $\overline{\Pi_+}=\Pi_+$ and $\overline{\Pi_-}=\Pi_-$.

*Proof.* $\Pi_+^{\natural}=\tfrac12(1+j)^{\natural}=\tfrac12(1-j)=\Pi_-$, and $\Pi_-^{\natural}=\Pi_+$; the bar conjugates the coefficients of $\Pi_\pm=\tfrac12\pm\tfrac12 j$, which are $\pm\tfrac12$ and real, so it fixes each idempotent; and the star is $\bar{\cdot}\circ{}^{\natural}$, so $\Pi_+^{*}=\overline{\Pi_+^{\natural}}=\overline{\Pi_-}=\Pi_-$ and $\Pi_-^{*}=\Pi_+$, the star exchanging the two exactly as the natural sign does. The idempotents and their behaviour under the four maps are *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*, below this article.

## Summary

The reduced biquaternion algebra carries the **bar** $\overline{Q_++jQ_-}=\bar Q_++j\bar Q_-$, the **natural sign** $(Q_++jQ_-)^{\natural}=Q_+-jQ_-$, the **star** ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, $(Q_++jQ_-)^{*}=\bar Q_+-j\bar Q_-$, and the **flat** ${}^{\flat}=-{}^{*}$. The bar, the natural sign and the star are involutions of the algebra; they commute pairwise; and they form the **Klein four-group** $\{\mathrm{id},\bar{\cdot},{}^{\natural},{}^{*}\}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2}$, each non-identity member being the composite of the other two, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, $\bar{\cdot}={}^{\natural}\circ{}^{*}$ and ${}^{\natural}={}^{*}\circ\bar{\cdot}$. The flat stands outside the group: it is the negative of the star, it exchanges the star's fixed and anti-fixed spaces, it is not multiplicative in the strict sense, $(Q_{\pm,1}Q_{\pm,2})^{\flat}=-Q_{\pm,1}^{\flat}Q_{\pm,2}^{\flat}$, and it is the anti-Hermitian conjugation.

On the real basis the three involutions act by
$$
\bar{\cdot}:(1,i,j,ij)\mapsto(1,-i,j,-ij),\quad
{}^{\natural}:(1,i,j,ij)\mapsto(1,i,-j,-ij),\quad
{}^{*}:(1,i,j,ij)\mapsto(1,-i,-j,ij),
$$
and their fixed spaces — $\mathbb{R}\{1,j\}$ the real subalgebra, $\mathbb{C}=\mathbb{R}\{1,i\}$ the scalar line and $\mathbb{R}\{1,ij\}$ the star plane — are the planes of the three splits, with the anti-fixed spaces the complementary planes. Of the four maps the **natural sign is $\mathbb{C}$-linear** and the bar, the star and the flat are $\mathbb{C}$-antilinear, which is the clause that decides which slot of each of the four general products carries a conjugation. Because the algebra is **commutative**, the bar, the natural sign and the star are algebra **automorphisms**, with no order reversal, and the natural sign and the star exchange the two idempotents while only the bar fixes each of them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar{\cdot}$ | the bar, $\overline{Q_++jQ_-}=\bar Q_++j\bar Q_-$, the coefficient conjugation |
| ${}^{\natural}$ | the natural sign, $(Q_++jQ_-)^{\natural}=Q_+-jQ_-$, the intrinsic conjugate |
| ${}^{*}$ | the star, $(Q_++jQ_-)^{*}=\bar Q_+-j\bar Q_-$, the composite $\bar{\cdot}\circ{}^{\natural}$ |
| ${}^{\flat}$ | the flat, ${}^{\flat}=-{}^{*}$, $(Q_++jQ_-)^{\flat}=-\bar Q_++j\bar Q_-$ |
| $\{\mathrm{id},\bar{\cdot},{}^{\natural},{}^{*}\}$ | the Klein four-group of the involutions |
| $\mathbb{R}\{1,j\}$ | fixed space of the bar, the real subalgebra |
| $\mathbb{C}=\mathbb{R}\{1,i\}$ | fixed space of the natural sign, the scalar line |
| $\mathbb{R}\{1,ij\}$ | fixed space of the star |
| $\mathbb{R}\{i,ij\},\ \mathbb{R}\{j,ij\},\ \mathbb{R}\{i,j\}$ | the anti-fixed spaces of the bar, the natural sign and the star |
| ${}^{*}\circ{}^{*}=\mathrm{id}$, ${}^{*}\circ\bar{\cdot}={}^{\natural}$, ${}^{*}\circ{}^{\natural}=\bar{\cdot}$ | the composition rule of the group |
| linear / antilinear | the natural sign against the bar, the star and the flat |

## Further Reading

- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), above this article in this category, for the algebra, the basis and the idempotents.
- *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$* (`articles_maths/reduced-biquaternions-as-a-vector-space-over-r-and-c.md`), above this article, for the linear and antilinear characters of the four maps.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), §*The Conjugations*, for the bar, the natural sign, the star and the flat, the Klein group and the dagger.
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), the biquaternion counterpart, for the same group over the non-commutative algebra, where the natural sign and the star are anti-automorphisms.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), below this article, for the four general products whose slots carry the maps of this article.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), below this article in this category, for the fixed spaces as subspaces.
- *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the idempotents and their behaviour under the four maps.
