# __The Element, the Coordinates and the Conjugations__

## Introduction

This article reads one element of the biquaternion algebra and the coordinates in which it is written. It is the second article of the block and it assumes the product, the basis and the axioms of *The Biquaternion Algebra*.

The first two sections give the element and its three readings: the scalar-vector split $\tilde Q=Q_te_t+\vec Q$, the real, complex and hyperbolic coordinate systems, and the complex structure $J$ that carries the difference between the real and the complex readings. The third section defines the four conjugations and separates them by their relation to $J$. The last two sections read the same element over the real scalars and through $J$.

The four conjugations are defined here and used throughout the block. Their group, its table, its orbits and the six fixed and anti-fixed subspaces are *The Group of Involutions*; the subspaces themselves are *The Six Subspaces*.

Nothing in this article pairs two different elements and takes a scalar part. The hyperbolic basis of the plain scalar part is a form statement and is filed with the plain product, after the forms; the matrices of the two models are *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant* and *$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant*.

## The Element and Its Coordinates

### The General Element

A general element of $\mathbb{B}$ is

$$
\tilde Q = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu = Q_t e_t + \vec Q , \qquad Q_\mu = q_\mu + i q'_\mu \in \mathbb{C} ,
$$

the **$\mathbb{C}$ scalar part** $Q_t e_t$ and the **$\mathbb{C}$ vector part** $\vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$. The four complex coefficients are eight real ones, $q_\mu$ the coefficient of $e_\mu$ and $q'_\mu$ the coefficient of $ie_\mu$. The element is also read as a pair of real quaternions, $\tilde Q = h_1 + i h_2$ with $h_1 = \sum_\mu q_\mu e_\mu$ and $h_2 = \sum_\mu q'_\mu e_\mu$, the three coordinate systems being the subject of §*The Element and Its Coordinates*, below.

### The Coordinate Systems

The same element is written in three coordinate systems, and all three are used below.

**Real coordinates.** Splitting each complex coefficient as $Q_\mu = q_\mu + iq'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$ gives a list of eight real numbers on the real basis:

$$
\tilde{Q} = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z + q'_t(ie_t) + q'_x(i\vec e_x) + q'_y(i\vec e_y) + q'_z(i\vec e_z).
$$

**Complex coordinates.** Collecting the eight real numbers into four complex ones gives the developed form, four complex coordinates $(Q_t, Q_x, Q_y, Q_z)$ on the complex basis $\{e_t, \vec e_x, \vec e_y, \vec e_z\}$.

**Quaternionic coordinates.** Collecting them by the scalar imaginary instead gives

$$
\tilde{Q} = h_1 + ih_2, \qquad h_1 = \sum_{\mu\in\{t,x,y,z\}} q_\mu e_\mu \in \mathbb{H}, \qquad h_2 = \sum_{\mu\in\{t,x,y,z\}} q'_\mu e_\mu \in \mathbb{H},
$$

a real quaternion plus $i$ times another real quaternion. The decomposition is unique, so in this view an element is a **pair of quaternions**.

| coordinates | basis | count | scalars |
|---|---|---|---|
| real | $e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ | $8$ | $\mathbb{R}$ |
| complex | $e_t, \vec e_x, \vec e_y, \vec e_z$ | $4$ | $\mathbb{C}$ |
| quaternionic | $e_t, ie_t$ | $2$ | $\mathbb{H}$ |

The three rows count the same element against three scalar systems, and all three are used below. The first row is the coordinate list of the real reading, developed in §*The Real Scalars*; the eight real coordinates and the four complex ones differ only in how the eight real numbers are gathered.


### The Scalar–Vector Split and the Two Products of Vector Parts

Writing $\vec Q_1 = \sum_k Q_{1k} \vec e_k$ and $\vec Q_2 = \sum_k Q_{2k} \vec e_k$, the two bilinear products of the vector parts are

$$
(\vec Q_1, \vec Q_2) = \sum_k Q_{1k} Q_{2k} , \qquad
\vec Q_1 \times \vec Q_2 = (Q_{1y} Q_{2z} - Q_{1z} Q_{2y})\vec e_x + (Q_{1z} Q_{2x} - Q_{1x} Q_{2z})\vec e_y + (Q_{1x} Q_{2y} - Q_{1y} Q_{2x})\vec e_z .
$$

The first is the complex bilinear **dot product**, a scalar; the second is the complex bilinear **cross product**, a vector part, alternating, $(\vec Q_2, \vec Q_1) = (\vec Q_1, \vec Q_2)$ and $\vec Q_2 \times \vec Q_1 = -\vec Q_1 \times \vec Q_2$. The two are the ingredients of the scalar–vector form of the multiplication, and they are those of *Quaternion Algebra*, read with complex coefficients.

## The Conjugations and the Classification

**Definition.** The **natural**, the **coefficient** and the **Hermitian** conjugations of $\tilde Q=Q_te_t+\vec Q$ are

$$
\tilde Q^{\natural}=Q_te_t-\vec Q , \qquad
(\overline{\tilde Q})_\mu=\bar Q_\mu , \qquad
\tilde Q^{*}=\bar Q_te_t-\overline{\vec Q} ,
$$

with $\tilde Q^{\flat}=-\tilde Q^{*}$ the **anti-Hermitian** one. They are involutions, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and $\{\mathrm{id},\natural,\bar{\cdot},{}^{*}\}\cong\mathbb{Z}_2\times\mathbb{Z}_2$; the group, its table, its orbits and the six fixed and anti-fixed subspaces are *The Group of Involutions*.

## The Real Scalars

**Definition.** The **real reading** of $\mathbb{B}$ is the same additive group over the subfield $\mathbb{R}$ of $\mathbb{C}$, obtained by restriction of scalars: the elements are unchanged and the scalar domain is cut from $\mathbb{C}$ down to the subfield $\mathbb{R}$. The general element is written in the eight real coordinates of §*The Element and Its Coordinates*, on the real basis

$$
e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z.
$$

Every element is a unique real combination of those eight, so the real dimension is the complex dimension doubled, $\dim_\mathbb{R}\mathbb{B} = 2\dim_\mathbb{C}\mathbb{B} = 8$, as recorded in §*The Element and Its Coordinates*.

**Remark.** No complex number is used as a scalar in this reading: the scalars are real, and the complex reading is the stronger structure rather than a different set. Every polynomial identity over $\mathbb{R}$ extends to $\mathbb{C}$ by scalar extension, and the real reading keeps the additive group, the basis and the product while dropping the complex scalars alone.

## The Complex Structure

The difference between the two readings is carried by one operator. Multiplication by the central imaginary,

$$
J : \tilde{Q} \mapsto i\tilde{Q}, \qquad J^2 = -\mathrm{id},
$$

is real-linear, and it is the **complex structure** of the real space, already met in *The Biquaternion Algebra*, §*The Scalars, the Centre and the Structure Map*. It carries the whole gap between the readings: for $\lambda = a + bi$, the centrality of the scalars gives

$$
\boxed{\;
\lambda\tilde{Q} = a\tilde{Q} + bJ(\tilde{Q})
\;},
$$

so the complex action is the real action together with $J$, and the real space together with $J$ is the complex space.

**Proposition (linearity is the commutator with $J$).** A real-linear map $T$ of $\mathbb{B}$ is $\mathbb{C}$-linear exactly when it commutes with $J$, and antilinear exactly when it anticommutes with it:

$$
\boxed{\;
T(\lambda\tilde{Q}) = \lambda T(\tilde{Q}) \text{ for all } \lambda \iff TJ = JT, \qquad T(\lambda\tilde{Q}) = \bar{\lambda} T(\tilde{Q}) \text{ for all } \lambda \iff TJ = -JT
\;}.
$$

**Proof.** Let $T$ be real-linear. Then $T(J\tilde{Q}) = T(i\tilde{Q})$ and $J(T\tilde{Q}) = iT(\tilde{Q})$, so the identity $T(i\tilde{Q}) = iT(\tilde{Q})$ is exactly $TJ = JT$; real-linearity then gives $T(\lambda\tilde{Q}) = T(a\tilde{Q} + bJ\tilde{Q}) = aT(\tilde{Q}) + bJT(\tilde{Q}) = \lambda T(\tilde{Q})$ for every $\lambda = a + bi$, and conversely $TJ = JT$ gives $T(i\tilde{Q}) = iT(\tilde{Q})$ and hence the same identity. The antilinear case is the same computation with the sign reversed, $T(i\tilde{Q}) = -iT(\tilde{Q})$, which is $TJ = -JT$.

### Linear and Antilinear Maps

The four conjugations of §*The Conjugations and the Classification* are all real-linear, and the proposition separates them into two classes: ${}^{\natural}$ commutes with $J$ and is $\mathbb{C}$-linear, while $\bar{\cdot}$, ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and $\flat = -{}^{*}$ anticommute with $J$ and are antilinear. The line between the two kinds of map is thus the commutation with one operator.

The real reading sees more linear maps than the complex one:

$$
\boxed{\;
\operatorname{End}_\mathbb{R}(\mathbb{B}) \cong M_8(\mathbb{R}), \qquad \operatorname{End}_\mathbb{C}(\mathbb{B}) \cong M_4(\mathbb{C})
\;},
$$

of real dimensions $64$ and $32$. The $\mathbb{C}$-linear maps are the real-linear ones commuting with $J$, a subspace of half the dimension; a real-linear map that anticommutes with $J$ is antilinear, an ordinary linear map of the real space that is not a complex-linear operator. The conjugations are the natural examples.

### The Real Form

A real subspace of $\mathbb{B}$ of real dimension four need not be closed under $J$; when it meets its image under $J$ only at zero, the two together fill $\mathbb{B}$ and the subspace is a **real form**.

**Proposition.** Let $V$ be a real subspace of $\mathbb{B}$ of real dimension four. Then $V \cap JV = 0$ if and only if $\mathbb{B} = V \oplus JV$, and in that case the complex reading is recovered from $V$ by extension of scalars, $\mathbb{C}\otimes_\mathbb{R}V\cong\mathbb{B}$.

**Proof.** If $\mathbb{B} = V \oplus JV$, then $V \cap JV = 0$ by the directness of the sum. Conversely let $V \cap JV = 0$. If $v + Jw = 0$ with $v, w \in V$, then $v = -Jw$ lies in $V \cap JV$, so $v = 0$ and $Jw = 0$, hence $w = 0$; the map $V \oplus JV \to \mathbb{B}$, $v + Jw \mapsto v + Jw$, is therefore injective, and since both sides have real dimension eight it is an isomorphism, $\mathbb{B} = V \oplus JV$. The map $\mathbb{C}\otimes_\mathbb{R}V \to \mathbb{B}$, $z \otimes v \mapsto zv$, is then $\mathbb{C}$-linear and surjective, because its image contains $V$ and $JV$, hence all of $\mathbb{B}$, and both spaces have complex dimension four, so it is an isomorphism.

**Example.** The elements with real coefficients, spanned by $e_t, \vec e_x, \vec e_y, \vec e_z$, form a real form; its image under $J$ is the subspace of elements with purely imaginary coefficients, the two meet at zero and their sum is $\mathbb{B}$. Real forms are not unique, and the choice of one is data beyond the real reading.

**Remark (the two real spaces, of dimensions eight and four).** The two dimensions must not be confused. The restriction of scalars of the complex reading is the eight-dimensional space above, whose extension of scalars back to $\mathbb{C}$ has complex dimension eight; the extension of scalars of a real form is the four-dimensional complex space $\mathbb{B}$ itself. What returns the complex reading from the eight-dimensional space is the operator $J$, not a scalar extension. The version of this caution for the algebra and its base rings, where $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$, is *The Realification and the Effect of the Change of Scalars*.

**Remark (the remarkable subspaces in the real reading).** The remarkable subspaces are real subspaces, and the complex structure sorts them: the centre and the vector subspace are carried to themselves by $J$ and are the only two that are complex subspaces, of complex dimensions one and three, while the other four are real forms, exchanged in two pairs by $J$. The remarkable subspaces are defined in *The Six Subspaces*, and the action of the central imaginary unit upon them is *The Lattice of the Subspaces*.

### What the View Adds

The real reading sees more subspaces than the complex one, since every complex subspace is a real subspace and the converse fails, and it makes the antilinear maps visible as ordinary linear maps. It drops the complex scalars, so the complex structure becomes an extra operator $J$ whenever the complex action is meant. The product stays $\mathbb{R}$-bilinear, so the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra* are read over $\mathbb{R}$ unchanged.

## Summary

- The element is $\tilde Q=Q_te_t+\vec Q$, with $Q_\mu\in\mathbb{C}$ and $\vec Q$ in the three-dimensional complex vector space.
- The real, complex and hyperbolic coordinate systems are three bases of the same eight-real-dimensional space; the complex structure $J(\tilde Q)=i\tilde Q$ carries the passage between the first two.
- The four conjugations are $\mathrm{id}$, $\natural$, $\bar{\cdot}$ and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, with $\flat=-{}^{*}$ beside them; $\natural$ is the unique $\mathbb{C}$-linear one.
- A real-linear map is $\mathbb{C}$-linear exactly when it commutes with $J$, and antilinear exactly when it anticommutes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | the general biquaternion |
| $Q_\mu=q_\mu+iq'_\mu$ | the complex coefficients |
| $J(\tilde Q)=i\tilde Q$ | the complex structure |
| $\natural,\ \bar{\cdot},\ {}^{*},\ \flat$ | natural, coefficient, Hermitian and anti-Hermitian conjugations |

The marks and their case rules are those of *Conventions in Mathematics*.

## Further Reading

- [The Biquaternion Algebra](the-biquaternion-algebra-and-its-vector-spaces.html), for the product and the axioms.
- [The Group of Involutions](the-group-of-involutions.html), for the Klein group and the orbits.
- [The Six Subspaces](introduction-to-the-remarkable-subspaces.html), for the fixed spaces.
