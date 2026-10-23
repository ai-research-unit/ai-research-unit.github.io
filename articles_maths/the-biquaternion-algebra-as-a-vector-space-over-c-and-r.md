# __The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$__

## Introduction

This article treats the biquaternions as a **vector space** in its two scalar readings: over $\mathbb{C}$, where the set is four-dimensional and carries the complex scalars, the coordinates and the four conjugations; and over $\mathbb{R}$, where the same set has dimension eight, the scalars are cut down to the subfield $\mathbb{R}$, and the complex structure $J$ of multiplication by the central imaginary carries the gap between the two readings. Restriction of scalars doubles the dimension, from four over $\mathbb{C}$ to eight over $\mathbb{R}$, and adds no element. The complex reading is the stronger structure; the real reading is the same additive group with fewer scalars, and the complex action is recovered from it by the operator $J$.

The goal is to lay out both linear structures precisely and to name the **remarkable** real subspaces that arise from the conjugations: four of dimension four, together with the two-dimensional centre and the six-dimensional vector subspace. The remarkable subspaces are not developed here: they are defined one to a section in *Introduction to the Remarkable Subspaces*, and the three decompositions into pairs of them are *Decompositions Along the Remarkable Subspaces*. It closes the group *The Algebra and Its Vector Spaces* and carries the two scalar readings, the coordinates, the conjugations and the real forms, the real subspaces of dimension four from which the complex reading is recovered by extension of scalars. The product is the next group.

$\mathbb{B}$ carries its product as well, and the product makes it an algebra. That reading, with the product taken as the multiplication, is *Introduction to the Biquaternion Algebra*; here the product is used only to say that the scalar action is compatible with it. The four conjugations and the group they generate are *The Group of Involutions*; the product read over the real scalars is *The Realification and the Effect of the Change of Scalars*.

The treatment is elementary and self-contained: every claim is either proved or stated as a definition, and no physics is invoked. The anti-Hermitian subspace is defined algebraically. No form appears in this article; the Hermitian form and the inner product are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*. The product of the algebra — its definition, its two scalar–vector parts, and the dot and cross products they are built from — is *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and it is used here as given.

The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra, together with its basis, its multiplication and its conjugation. No facts about $\mathbb{H}$ are restated here. Beyond the scalar fields, the two readings whose base is a ring of operators rather than a field — the bimodule over $\mathbb{H}$ and the module over $\mathbb{B}$ itself — are *Modules over the Quaternion Algebra* and *Modules over the Biquaternion Algebra*.

## The Complex Vector Space

### Definition

The **biquaternion algebra** is the complexification of the quaternion algebra:

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H},
$$

read here as a $\mathbb{C}$-vector space: an additive group with a scalar multiplication by the complex numbers. It is therefore **four-dimensional** over $\mathbb{C}$, with complex basis $\{e_t, \vec e_x, \vec e_y, \vec e_z\}$. It also carries its product, the one defined and studied in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*; the product is $\mathbb{C}$-bilinear, so the scalars may be moved through it, and it makes $\mathbb{B}$ an algebra over $\mathbb{C}$, a reading developed in *Introduction to the Biquaternion Algebra*. Its centre is the scalar line $\mathbb{C}e_t$, spanned over $\mathbb{R}$ by $e_t$ and $ie_t$, and it is one of the remarkable real subspaces of the group.

### Developed Form

A general biquaternion is written in developed form as

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C}.
$$

We write

$$
\tilde{Q} = Q_t + \vec Q, \qquad \vec Q = \sum_{k=1}^{3} Q_k \vec e_k,
$$

where $Q_t$ is the **complex scalar part** and $\vec Q$ is the **complex vector part**. The tilde signals that $\tilde{Q}$ is an element of the algebra $\mathbb{B}$, not a four-vector.

Each complex coefficient is written in terms of its real and imaginary parts:

$$
Q_t = q_t + i q'_t, \qquad Q_k = q_k + i q'_k, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The scalar imaginary $i$ satisfies $i^2 = -1$ and commutes with all quaternion units: $i \vec e_k = \vec e_k i$. Multiplication by it is a real-linear map $J$ of $\mathbb{B}$ with $J^2 = -\mathrm{id}$, the complex structure of the real reading; the operator and the real reading it builds are treated in §*The Complex Structure*.

In the complex coordinates, $\tilde{Q}$ is the four-tuple $(Q_t, Q_x, Q_y, Q_z)$.

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

### Conjugations

There are **four** natural conjugations on $\mathbb{B}$. The first three are obtained from the quaternion conjugation ${}^{\natural}$ and the complex conjugation $\bar{\cdot}$; the fourth is defined as the negative of Hermitian conjugation:

**Quaternion conjugation** $\tilde{Q}^{\natural}$:

$$
\tilde{Q}^{\natural} = Q_t e_t - Q_x \vec e_x - Q_y \vec e_y - Q_z \vec e_z.
$$

**Complex conjugation** $\bar{\tilde{Q}}$:

$$
\bar{\tilde{Q}} = \bar{Q_t} e_t + \bar{Q_x} \vec e_x + \bar{Q_y} \vec e_y + \bar{Q_z} \vec e_z.
$$

**Hermitian conjugation** $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$:

$$
\tilde{Q}^{*} = \bar{Q_t} e_t - \bar{Q_x} \vec e_x - \bar{Q_y} \vec e_y - \bar{Q_z} \vec e_z.
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^{*}$:

$$
\tilde{Q}^\flat = -\bar{Q_t} e_t + \bar{Q_x} \vec e_x + \bar{Q_y} \vec e_y + \bar{Q_z} \vec e_z.
$$

Each conjugation is an involution: applying it twice returns the original biquaternion. Each therefore splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and each of the two is a real vector subspace of $\mathbb{B}$. The first three have distinct eigenspaces, six in all; the reversal $\flat = -{}^{*}$ reproduces the two eigenspaces of ${}^{*}$ with the signs exchanged and adds no new one. These are the **remarkable subspaces** of $\mathbb{B}$, defined one to a section in *Introduction to the Remarkable Subspaces* and tabulated in *Comparison of the Remarkable Subspaces*.

The two anti-automorphisms ${}^{\natural}$ and ${}^{*}$, the Klein four-group they generate with the identity and their composite $\bar{\cdot}$, the place of the reversal $\flat = -{}^{*}$ outside it and the composition table that includes the reversal are *The Group of Involutions*; the lattice of the fixed spaces is *Comparison of the Remarkable Subspaces*. Neither the group nor the remarkable subspaces are repeated here: this article keeps the four formulas above, and the three decompositions the conjugations cut out are *Decompositions Along the Remarkable Subspaces*.

## The Real Scalars

**Definition.** The **real reading** of $\mathbb{B}$ is the same additive group over the subfield $\mathbb{R}$ of $\mathbb{C}$, obtained by restriction of scalars: the elements are unchanged and the scalar domain is cut from $\mathbb{C}$ down to the subfield $\mathbb{R}$. The general element is written in the eight real coordinates of §*The Coordinate Systems*, on the real basis

$$
e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z.
$$

Every element is a unique real combination of those eight, so the real dimension is the complex dimension doubled, $\dim_\mathbb{R}\mathbb{B} = 2\dim_\mathbb{C}\mathbb{B} = 8$, as recorded in §*The Coordinate Systems*.

**Remark.** No complex number is used as a scalar in this reading: the scalars are real, and the complex reading is the stronger structure rather than a different set. Every statement made over $\mathbb{R}$ holds over $\mathbb{C}$, since a complex scalar is a pair of real ones, and the real reading keeps the additive group, the basis and the product while dropping the complex scalars alone.

## The Complex Structure

The difference between the two readings is carried by one operator. Multiplication by the central imaginary,

$$
J : \tilde{Q} \mapsto i\tilde{Q}, \qquad J^2 = -\mathrm{id},
$$

is real-linear, and it is the **complex structure** of the real space, already named in §*Developed Form*. It carries the whole gap between the readings: for $\lambda = a + bi$, the centrality of the scalars gives

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

The four conjugations of §*Conjugations* are all real-linear, and the proposition separates them into two classes: ${}^{\natural}$ commutes with $J$ and is $\mathbb{C}$-linear, while $\bar{\cdot}$, ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and $\flat = -{}^{*}$ anticommute with $J$ and are antilinear. The line between the two kinds of map is thus the commutation with one operator.

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

**Remark (the remarkable subspaces in the real reading).** The remarkable subspaces are real subspaces, and the complex structure sorts them: the centre and the vector subspace are carried to themselves by $J$ and are the only two that are complex subspaces, of complex dimensions one and three, while the other four are real forms, exchanged in two pairs by $J$. The remarkable subspaces are defined in *Introduction to the Remarkable Subspaces*, and the action of the central imaginary unit upon them is *Comparison of the Remarkable Subspaces*.

### What the View Adds

The real reading sees more subspaces than the complex one, since every complex subspace is a real subspace and the converse fails, and it makes the antilinear maps visible as ordinary linear maps. It costs the complex structure, which leaves the scalars and must be carried by $J$ whenever the complex action is meant. The product stays $\mathbb{R}$-bilinear, so the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are read over $\mathbb{R}$ unchanged; the two ring-based readings, the $\mathbb{H}$-bimodule and the module over $\mathbb{B}$ itself, are *Modules over the Quaternion Algebra* and *Modules over the Biquaternion Algebra*.

## Summary

The biquaternion algebra is read here with its two scalar systems. Over the complex scalars it is the set $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, a complex vector space of dimension four on the basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, with $\vec e_k^2 = -e_t$; the central element $i$ satisfies $i^2 = -1$ and commutes with the quaternion units, and its multiples form the scalar line $\mathbb{C}e_t$, the centre, one of the remarkable real subspaces. Over the real scalars it is the same additive group with the scalar domain cut down to the subfield $\mathbb{R}$, of real dimension eight on the basis $e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z$, twice the complex dimension.

The same element is written in three coordinate systems: eight real coordinates on the real basis, four complex coordinates on the complex basis, and two quaternionic coordinates as a pair of real quaternions. The complex action is the linear structure of the complex reading; the real reading keeps the additive group, the basis and the product and drops the complex scalars alone.

The gap between the two readings is one operator: the multiplication $J : \tilde{Q} \mapsto i\tilde{Q}$ by the central imaginary, real-linear with $J^2 = -\mathrm{id}$, is the complex structure of the real space, and the complex action is the real action together with $J$. A real-linear map is $\mathbb{C}$-linear exactly when it commutes with $J$ and antilinear exactly when it anticommutes; the quaternion conjugation commutes and the other three conjugations anticommute. The real reading therefore sees more linear maps — $\operatorname{End}_\mathbb{R}(\mathbb{B}) \cong M_8(\mathbb{R})$ against $\operatorname{End}_\mathbb{C}(\mathbb{B}) \cong M_4(\mathbb{C})$, of real dimensions $64$ and $32$ — and more subspaces, since every complex subspace is a real one and not conversely.

A real form is a real subspace $V$ of dimension four meeting $JV$ only at zero; then $\mathbb{B} = V \oplus JV$ and $\mathbb{C}\otimes_\mathbb{R}V \cong \mathbb{B}$, so the complex reading is recovered from $V$ by extension of scalars, the choice of $V$ being data beyond the real reading. The remarkable subspaces are real; the centre and the vector subspace are the only two closed under $J$, and the other four are real forms exchanged in pairs.

The algebra carries four natural conjugations, ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and $\flat = -{}^{*}$, of which the first three are commuting involutions; the group they form is *The Group of Involutions*. They define the remarkable real subspaces of $\mathbb{B}$, defined one to a section in *Introduction to the Remarkable Subspaces*, and the three direct-sum decompositions they cut out are *Decompositions Along the Remarkable Subspaces*; the coordinate blocks, the intersections, the sums and the action of the conjugations upon the remarkable subspaces are *Comparison of the Remarkable Subspaces*.

The product stays $\mathbb{R}$-bilinear, so the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are read over $\mathbb{R}$ unchanged. The product as the multiplication of an algebra is *Introduction to the Biquaternion Algebra*; the product as the multiplication of an algebra over $\mathbb{R}$ is *The Realification and the Effect of the Change of Scalars*. The two ring-based readings, the $\mathbb{H}$-bimodule and the module over $\mathbb{B}$ itself, are *Modules over the Quaternion Algebra* and *Modules over the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}}\mathbb{B}$ | the real reading: the same additive group and the same elements over the scalars $\mathbb{R}$, dimension $8$ |
| $e_t = 1$ | Identity |
| $\vec e_x, \vec e_y, \vec e_z$ | Quaternion units, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$, commutes with $\vec e_k$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| $Q_t$ | Complex scalar part |
| $\vec Q$ | Complex vector part |
| $J : \tilde{Q} \mapsto i\tilde{Q}$ | the real-linear complex structure, $J^2 = -\mathrm{id}$ |
| $\lambda\tilde{Q} = a\tilde{Q} + bJ(\tilde{Q})$ | the complex action read over $\mathbb{R}$, for $\lambda = a + bi$ |
| $\operatorname{End}_\mathbb{R}(\mathbb{B})$ | the real-linear self-maps, $\cong M_8(\mathbb{R})$ |
| $\operatorname{End}_\mathbb{C}(\mathbb{B})$ | the $\mathbb{C}$-linear self-maps, $\cong M_4(\mathbb{C})$, the maps commuting with $J$ |
| real form of $\mathbb{B}$ | a real subspace $V$ of real dimension $4$ with $\mathbb{B} = V \oplus JV$, e.g. the elements with real coefficients |
| $\tilde{Q}^{\natural} = Q_t e_t - \vec Q$ | Quaternion conjugate |
| $\bar{\tilde{Q}} = \bar{Q_t} e_t + \vec Q^*$ | Complex conjugate |
| $\tilde{Q}^{*} = \bar{Q_t} e_t - \vec Q^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\overline{\tilde{Q}^{\natural}} = -\tilde{Q}^{*}$ | Anti-Hermitian conjugate |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Clifford-algebra reading of the biquaternions.
