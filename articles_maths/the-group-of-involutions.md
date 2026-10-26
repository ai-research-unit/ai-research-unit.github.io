# __The Group of Involutions__

## Introduction

The biquaternion algebra carries two conjugations. The **quaternion conjugation** ${}^{\natural}$ is $\mathbb{C}$-linear and changes the sign of the vector part. The **Hermitian conjugation** ${}^{*}$ is antilinear and conjugates the coefficients as well. Both are involutions, both reverse the order of a product, and they commute. The identity, the two maps and their composite therefore make a set of four that is closed under composition. That set is the Klein four-group $V_{4}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2}$.

This article fixes the group: the two definitions, the composition rules, the Cayley table, the three subgroups, the three splittings that the subgroups induce, and the orbits. It closes with the map $\flat=-{}^{*}$, which *The Element, the Coordinates and the Conjugations* records beside the four and which is not in the group.

The algebra is *The Biquaternion Algebra*; the element, its coordinates and the definitions of the conjugations are *The Element, the Coordinates and the Conjugations*. Only what the group needs is recalled here.

## The Two Conjugations

**Definition.** For $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$,

$$
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z,\qquad
\bar{\tilde Q}=\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z,
$$

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z .
$$

The first is $\mathbb{C}$-linear; the second, the **coefficient conjugation**, is antilinear; the third is their composite and is antilinear. A bijection of $\mathbb{B}$ is an **anti-automorphism** when it reverses the order of every product. On the basis, ${}^{\natural}$ fixes $e_t$ and negates each $\vec e_k$, $\bar{\cdot}$ fixes every basis element and conjugates every coefficient, and ${}^{*}$ does both.

**Proposition (the product rules).** For $\tilde Q_1,\tilde Q_2\in\mathbb{B}$,

$$
(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural},\qquad
(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*},\qquad
\overline{\tilde Q_1\tilde Q_2}=\bar{\tilde Q_1}\,\bar{\tilde Q_2}.
$$

*Proof.* Write $\tilde Q_i=a_i+\vec u_i$, with $a_i$ the scalar coefficient and $\vec u_i$ the vector part. By the scalar–vector form of the product,

$$
\tilde Q_1\tilde Q_2=\bigl(a_1a_2-(\vec u_1,\vec u_2)\bigr)+\bigl(a_1\vec u_2+a_2\vec u_1+\vec u_1\times\vec u_2\bigr).
$$

Applying ${}^{\natural}$ keeps the scalar and changes the sign of the vector part. On the other side,

$$
\tilde Q_2^{\natural}\tilde Q_1^{\natural}=(a_2-\vec u_2)(a_1-\vec u_1)
=\bigl(a_2a_1-(\vec u_2,\vec u_1)\bigr)+\bigl(-a_2\vec u_1-a_1\vec u_2+\vec u_2\times\vec u_1\bigr),
$$

and $(\vec u_2,\vec u_1)=(\vec u_1,\vec u_2)$ while $\vec u_2\times\vec u_1=-\vec u_1\times\vec u_2$; the vector part is the negative of the one above. Hence ${}^{\natural}$ reverses the product. The coefficient conjugation is a field automorphism applied to the coefficients, hence preserves the product. Finally ${}^{*}={}^{\natural}\circ\bar{\cdot}$, the composite of an anti-automorphism and an automorphism, and it reverses the product as ${}^{\natural}$ does.

**Proposition (order two and commutation).** Each map is its own inverse, the three commute, and ${}^{*}$ is the composite of the other two:

$$
{}^{\natural}\circ{}^{\natural}=\mathrm{id},\qquad
\bar{\cdot}\circ\bar{\cdot}=\mathrm{id},\qquad
{}^{\natural}\circ\bar{\cdot}=\bar{\cdot}\circ{}^{\natural}={}^{*}.
$$

*Proof.* On a coefficient, ${}^{\natural}$ multiplies by the sign of the basis element, $\bar{\cdot}$ conjugates the coefficient, and the two operations commute and are involutions; the composite conjugates every coefficient and multiplies by the sign of the basis element, which is ${}^{*}$.

On the eight real coordinates $q_t,q_x,q_y,q_z,q'_t,q'_x,q'_y,q'_z$ of $\tilde Q=(q_t+iq'_t)e_t+(q_x+iq'_x)\vec e_x+(q_y+iq'_y)\vec e_y+(q_z+iq'_z)\vec e_z$ the four maps act by sign changes:

| map | $(q_t,q_x,q_y,q_z,q'_t,q'_x,q'_y,q'_z)\mapsto$ |
|---|---|
| $\mathrm{id}$ | $(q_t,q_x,q_y,q_z,q'_t,q'_x,q'_y,q'_z)$ |
| ${}^{\natural}$ | $(q_t,-q_x,-q_y,-q_z,q'_t,-q'_x,-q'_y,-q'_z)$ |
| ${}^{*}$ | $(q_t,-q_x,-q_y,-q_z,-q'_t,q'_x,q'_y,q'_z)$ |
| ${}^{\natural}{}^{*}$ | $(q_t,q_x,q_y,q_z,-q'_t,-q'_x,-q'_y,-q'_z)$ |

The four rows are distinct, and the last is the coefficient conjugation: ${}^{\natural}{}^{*}=\bar{\cdot}$.

| | automorphism | anti-automorphism |
|---|---|---|
| $\mathbb{C}$-linear | $\mathrm{id}$ | ${}^{\natural}$ |
| antilinear | $\bar{\cdot}$ | ${}^{*}$ |

The table describes the four maps and does not classify every involution of the algebra; it records that the two independent choices, linear or antilinear and preserving or reversing the order, are both realized and give the four.

**Remark (why four).** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, and each tensor factor carries one nontrivial conjugation: the coefficient conjugation on the $\mathbb{C}$ factor and the quaternion conjugation on the $\mathbb{H}$ factor. Acting with the identity or with the conjugation on each factor gives the four maps

$$
\mathrm{id}\otimes\mathrm{id}=\mathrm{id},\qquad
\mathrm{id}\otimes\mathrm{conj}={}^{\natural},\qquad
\mathrm{conj}\otimes\mathrm{id}=\bar{\cdot},\qquad
\mathrm{conj}\otimes\mathrm{conj}={}^{*}.
$$

Two factors with two choices each give $2\times2=4$ combinations, and the list is complete for maps built from the two factor structures.

## The Group

**Theorem.** The set

$$
\boxed{\; G=\{\mathrm{id},\,{}^{\natural},\,{}^{*},\,{}^{\natural}{}^{*}\} \;}
$$

is a group under composition, and it is the Klein four-group $V_{4}\cong\mathbb{Z}_{2}\times\mathbb{Z}_{2}$.

*Proof.* By the propositions above every composite of two elements is again one of the four, every element is its own inverse, and $\mathrm{id}$ is the unit; composition of maps is associative. A group of order four in which every element has order two is not cyclic, hence is $V_{4}$.

The Cayley table, the entry being the map applied first in the row and then in the column, is

| $\circ$ | $\mathrm{id}$ | ${}^{\natural}$ | ${}^{*}$ | ${}^{\natural}{}^{*}$ |
|---|---|---|---|---|
| $\mathrm{id}$ | $\mathrm{id}$ | ${}^{\natural}$ | ${}^{*}$ | ${}^{\natural}{}^{*}$ |
| ${}^{\natural}$ | ${}^{\natural}$ | $\mathrm{id}$ | ${}^{\natural}{}^{*}$ | ${}^{*}$ |
| ${}^{*}$ | ${}^{*}$ | ${}^{\natural}{}^{*}$ | $\mathrm{id}$ | ${}^{\natural}$ |
| ${}^{\natural}{}^{*}$ | ${}^{\natural}{}^{*}$ | ${}^{*}$ | ${}^{\natural}$ | $\mathrm{id}$ |

The table is symmetric, so the group is abelian: the four maps may be applied in any order.

**Remark (generators).** Any two distinct non-identity elements generate the group, the composite of the two being the third. With the pair ${}^{\natural}$, ${}^{*}$ the third element is ${}^{\natural}{}^{*}$, and

$$
G=\{\mathrm{id},{}^{\natural}\}\times\{\mathrm{id},{}^{*}\},
$$

the two order-two subgroups meeting in the identity.

## The Subgroups and the Three Splittings

**Proposition (the subgroups).** The group has exactly three subgroups of order two,

$$
\{\mathrm{id},{}^{\natural}\},\qquad \{\mathrm{id},{}^{*}\},\qquad \{\mathrm{id},{}^{\natural}{}^{*}\},
$$

one for each non-identity element, and no other proper subgroup.

*Proof.* A subgroup has order dividing four, an element of order two generates a subgroup of order two, and each non-identity element is the only non-identity element of the subgroup it generates. A subgroup of order three would contain an element of order three, and there is none.

**Proposition (an involution splits the algebra).** Let $\sigma$ be one of the three non-identity elements. Then every $\tilde Q$ is the sum of an element fixed by $\sigma$ and an element sent to its negative:

$$
\tilde Q=\frac{\tilde Q+\sigma\tilde Q}{2}+\frac{\tilde Q-\sigma\tilde Q}{2},\qquad
\sigma\!\left(\frac{\tilde Q+\sigma\tilde Q}{2}\right)=\frac{\tilde Q+\sigma\tilde Q}{2},\qquad
\sigma\!\left(\frac{\tilde Q-\sigma\tilde Q}{2}\right)=-\frac{\tilde Q-\sigma\tilde Q}{2}.
$$

The two subspaces meet only in $0$, and their sum is $\mathbb{B}$.

*Proof.* The identities follow from $\sigma^{2}=\mathrm{id}$ and the real-linearity of $\sigma$; an element of the intersection satisfies $\tilde Q=-\tilde Q$, hence $\tilde Q=0$. The two parts are the fixed and the anti-fixed subspace of $\sigma$.

The fixed space and the anti-fixed space of each of the three are the six subspaces that *The Six Subspaces* takes one by one:

| subgroup | involution | fixed space | anti-fixed space |
|---|---|---|---|
| $\{\mathrm{id},{}^{\natural}\}$ | ${}^{\natural}$ | the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the vector part |
| $\{\mathrm{id},{}^{\natural}{}^{*}\}$ | ${}^{\natural}{}^{*}$ | the quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t+\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$ | the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ |
| $\{\mathrm{id},{}^{*}\}$ | ${}^{*}$ | the Hermitian elements | the anti-Hermitian elements |

The Hermitian elements are those with real scalar coefficient and purely imaginary vector coefficients; the anti-Hermitian ones have purely imaginary scalar coefficient and real vector coefficients. The three fixed spaces meet pairwise in the real line $\mathbb{R}e_t$.

## The Orbits

The group acts on the algebra through its four maps, and the orbit of an element is the set of its four images.

**Theorem.** The orbit of $\tilde Q$ under $G$ has size $1$, $2$ or $4$. The size is $1$ on the real line $\mathbb{R}e_t$; it is $2$ on the elements of the centre, of the quaternion subspace or of the Hermitian elements that are not on that line; and it is $4$ on all other elements.

*Proof.* The stabilizer of $\tilde Q$ is the set of maps of $G$ fixing it, a subgroup, so its order is $1$, $2$ or $4$ and the orbit has size $4$, $2$ or $1$ by orbit–stabilizer. The element is fixed by the whole group exactly when it is fixed by ${}^{\natural}$ and by ${}^{\natural}{}^{*}$, since ${}^{*}$ is their composite; that intersection is $\mathbb{C}_{\mathbb{B}}\cap\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t$, which gives orbit size $1$. The stabilizer has order two exactly when the element is fixed by one of the three non-identity maps and by no second one; the three fixed spaces are $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and the Hermitian elements, and their pairwise intersections are all $\mathbb{R}e_t$. This gives orbit size $2$ on the stated set and orbit size $4$ on its complement.

**Example.** For $\tilde Q=e_t+2\vec e_x+3i\vec e_x+4i\vec e_y$ the images are

$$
\tilde Q^{\natural}=e_t-2\vec e_x-3i\vec e_x-4i\vec e_y,\quad
\tilde Q^{\natural*}=e_t+2\vec e_x-3i\vec e_x-4i\vec e_y,\quad
\tilde Q^{*}=e_t-2\vec e_x+3i\vec e_x+4i\vec e_y,
$$

four distinct elements, so the orbit has size $4$. For $\tilde Q=(1+3i)e_t$ the images are $(1+3i)e_t$ under $\mathrm{id}$ and ${}^{\natural}$ and $(1-3i)e_t$ under ${}^{*}$ and ${}^{\natural}{}^{*}$, an orbit of size $2$. For $\tilde Q=2e_t$ every image is $2e_t$, an orbit of size $1$.

## The Sign-Twisted Adjoint

*The Element, the Coordinates and the Conjugations* records a further map beside the four, the **anti-Hermitian conjugation** $\flat=-{}^{*}$:

$$
\tilde Q^{\flat}=-\tilde Q^{*}=-\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z .
$$

It is real-linear and $\flat^{2}=\mathrm{id}$, and its fixed space is the anti-Hermitian elements. It is not in $G$, and the reason is the product rule. From $(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}$,

$$
(\tilde Q_1\tilde Q_2)^{\flat}=-\tilde Q_2^{*}\tilde Q_1^{*}=-\bigl(-\tilde Q_2^{\flat}\bigr)\bigl(-\tilde Q_1^{\flat}\bigr)=-\tilde Q_2^{\flat}\tilde Q_1^{\flat},
$$

so $\flat$ reverses the product only up to the central sign $-1$; it is not an anti-automorphism, and its fixed space is not the fixed space of a conjugation of the algebra. Adjoining the central sign to the group gives the order-eight group

$$
\{\pm\mathrm{id},\ \pm{}^{\natural},\ \pm{}^{*},\ \pm{}^{\natural}{}^{*}\}=\{\pm1\}\times G,
$$

in which $\flat=-{}^{*}$ is one of the new elements; the factor $\pm1$ is central and scalar, and it adds no conjugation of the vector part.

## Summary

The algebra carries the quaternion conjugation ${}^{\natural}$, $\mathbb{C}$-linear, and the Hermitian conjugation ${}^{*}$, antilinear; both are involutions, both reverse the product, and they commute. With the identity and the composite ${}^{\natural}{}^{*}=\bar{\cdot}$ they form the Klein four-group $G=\{\mathrm{id},{}^{\natural},{}^{*},{}^{\natural}{}^{*}\}$, abelian, of exponent two. The four are the four combinations of the two factor conjugations of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, one per tensor factor, which is why there are four. The group has three subgroups of order two, and each gives a splitting of the algebra into a fixed space and an anti-fixed space: the centre and the vector subspace, the quaternion and anti-quaternion subspaces, the Hermitian and anti-Hermitian elements. The orbits have size one, two or four, according as the element lies on the real line, in one of the three fixed spaces off that line, or nowhere. The sign-twisted adjoint $\flat=-{}^{*}$ is not in the group: it reverses the product only up to the central sign.

## Summary of Notation

| symbol | meaning |
|---|---|
| ${}^{\natural}$ | quaternion conjugation, $\mathbb{C}$-linear, $Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$ |
| ${}^{*}$ | Hermitian conjugation, antilinear, $\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z$ |
| $\bar{\cdot}={}^{\natural}{}^{*}$ | coefficient conjugation, $\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z$ |
| $G=\{\mathrm{id},{}^{\natural},{}^{*},{}^{\natural}{}^{*}\}$ | the group of the two conjugations, the Klein four-group |
| $\{\mathrm{id},{}^{\natural}\}$, $\{\mathrm{id},{}^{*}\}$, $\{\mathrm{id},{}^{\natural}{}^{*}\}$ | the three subgroups of order two |
| fixed, anti-fixed | the subspaces where an involution acts as $+1$ and as $-1$ |
| $\flat=-{}^{*}$ | the sign-twisted adjoint, outside $G$ |
| orbit | the set of the four images of an element, of size $1$, $2$ or $4$ |

## Further Reading

- [The Biquaternion Algebra](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra, its basis and its tensor product
- [The Element, the Coordinates and the Conjugations](the-element-the-coordinates-and-the-conjugations.html), for the four maps and the scalar–vector form of the product
- [The Six Subspaces](introduction-to-the-remarkable-subspaces.html), for the six subspaces of the three splittings, one to a section
- [The Lattice of the Subspaces](comparison-of-the-remarkable-subspaces.html), for the relations between the six and the lattice they form
- [$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints](m2c-representation-the-conjugations-and-the-adjoints.html), for the matrix images of the four maps
