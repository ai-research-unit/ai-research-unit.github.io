# __Biquaternions as a Vector Space over $\mathbb{R}$__

## Introduction

This article treats the biquaternions as a **real vector space**: the same set as *Biquaternions as a Vector Space over $\mathbb{C}$* with the scalars cut from $\mathbb{C}$ down to the subfield $\mathbb{R}$, the complex structure the complex reading rests on, the separation of the real-linear self-maps into the $\mathbb{C}$-linear and the antilinear ones, and the real forms from which the complex reading is recovered by extension of scalars. Restriction of scalars doubles the dimension, from four over $\mathbb{C}$ to eight over $\mathbb{R}$. The elements, the basis, the coordinate systems and the four conjugation formulas are those of the complex article and are cited, not restated: what is added here is the scalar reading itself, the operator that carries the gap between the two readings, and the linear algebra that the doubled dimension makes visible.

No form appears in this article: the Hermitian form and the inner product are *Biquaternion Norm and Invertibility*. The product read over the real scalars is *Biquaternions as an Algebra over $\mathbb{R}$*; the four general products themselves are *The Four General Products of the Biquaternion $\mathbb{C}$ Space*.

## The Real Scalars

**Definition.** The **real reading** of $\mathbb{B}$ is the same additive group over the subfield $\mathbb{R}$ of $\mathbb{C}$, obtained by restriction of scalars: the elements are unchanged and the scalar domain is cut from $\mathbb{C}$ down to the subfield $\mathbb{R}$. The general element is written in the eight real coordinates of *Biquaternions as a Vector Space over $\mathbb{C}$*, §*The Coordinate Systems*, on the real basis

$$
e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3 .
$$

Every element is a unique real combination of those eight, so the real dimension is the complex dimension doubled, $\dim_\mathbb{R}\mathbb{B} = 2\dim_\mathbb{C}\mathbb{B} = 8$, as recorded in the complex article, §*The Complex Vector Space*.

**Remark.** No complex number is used as a scalar in this reading: the scalars are real, and the complex reading is the stronger structure rather than a different set. Every statement made over $\mathbb{R}$ holds over $\mathbb{C}$, since a complex scalar is a pair of real ones, and the real reading keeps the additive group, the basis and the product while dropping the complex scalars alone.

## The Complex Structure

The difference between the two readings is carried by one operator. Multiplication by the central imaginary,

$$
J : \tilde{Q} \mapsto i\tilde{Q}, \qquad J^2 = -\mathrm{id},
$$

is real-linear, and it is the **complex structure** of the real space, already named in the complex article, §*Developed Form*. It carries the whole gap between the readings: for $\lambda = a + bi$, the centrality of the scalars gives

$$
\lambda\tilde{Q} = a\tilde{Q} + bJ(\tilde{Q}),
$$

so the complex action is the real action together with $J$, and the real space together with $J$ is the complex space.

**Proposition (linearity is the commutator with $J$).** A real-linear map $T$ of $\mathbb{B}$ is $\mathbb{C}$-linear exactly when it commutes with $J$, and antilinear exactly when it anticommutes with it:

$$
T(\lambda\tilde{Q}) = \lambda T(\tilde{Q}) \text{ for all } \lambda \iff TJ = JT, \qquad T(\lambda\tilde{Q}) = \bar{\lambda} T(\tilde{Q}) \text{ for all } \lambda \iff TJ = -JT .
$$

**Proof.** Let $T$ be real-linear. Then $T(J\tilde{Q}) = T(i\tilde{Q})$ and $J(T\tilde{Q}) = iT(\tilde{Q})$, so the identity $T(i\tilde{Q}) = iT(\tilde{Q})$ is exactly $TJ = JT$; real-linearity then gives $T(\lambda\tilde{Q}) = T(a\tilde{Q} + bJ\tilde{Q}) = aT(\tilde{Q}) + bJT(\tilde{Q}) = \lambda T(\tilde{Q})$ for every $\lambda = a + bi$, and conversely $TJ = JT$ gives $T(i\tilde{Q}) = iT(\tilde{Q})$ and hence the same identity. The antilinear case is the same computation with the sign reversed, $T(i\tilde{Q}) = -iT(\tilde{Q})$, which is $TJ = -JT$. $\square$

### Linear and Antilinear Maps

The four conjugations of *Biquaternions as a Vector Space over $\mathbb{C}$*, §*Conjugations*, are all real-linear, and the proposition separates them into two classes: ${}^{\natural}$ commutes with $J$ and is $\mathbb{C}$-linear, while $\bar{\cdot}$, ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and $\flat = -{}^{*}$ anticommute with $J$ and are antilinear. The line between the two kinds of map is thus the commutation with one operator.

The real reading sees more linear maps than the complex one:

$$
\operatorname{End}_\mathbb{R}(\mathbb{B}) \cong M_8(\mathbb{R}), \qquad \operatorname{End}_\mathbb{C}(\mathbb{B}) \cong M_4(\mathbb{C}),
$$

of real dimensions $64$ and $32$. The $\mathbb{C}$-linear maps are the real-linear ones commuting with $J$, a subspace of half the dimension; a real-linear map that anticommutes with $J$ is antilinear, an ordinary linear map of the real space that is not a complex-linear operator. The conjugations are the natural examples.

### The Real Form

A real subspace of $\mathbb{B}$ of real dimension four need not be closed under $J$; when it meets its image under $J$ only at zero, the two together fill $\mathbb{B}$ and the subspace is a **real form**.

**Proposition.** Let $V$ be a real subspace of $\mathbb{B}$ of real dimension four. Then $V \cap JV = 0$ if and only if $\mathbb{B} = V \oplus JV$, and in that case the complex reading is recovered from $V$ by extension of scalars, $\mathbb{C}\otimes_\mathbb{R}V\cong\mathbb{B}$.

**Proof.** If $\mathbb{B} = V \oplus JV$, then $V \cap JV = 0$ by the directness of the sum. Conversely let $V \cap JV = 0$. If $v + Jw = 0$ with $v, w \in V$, then $v = -Jw$ lies in $V \cap JV$, so $v = 0$ and $Jw = 0$, hence $w = 0$; the map $V \oplus JV \to \mathbb{B}$, $v + Jw \mapsto v + Jw$, is therefore injective, and since both sides have real dimension eight it is an isomorphism, $\mathbb{B} = V \oplus JV$. The map $\mathbb{C}\otimes_\mathbb{R}V \to \mathbb{B}$, $z \otimes v \mapsto zv$, is then $\mathbb{C}$-linear and surjective, because its image contains $V$ and $JV$, hence all of $\mathbb{B}$, and both spaces have complex dimension four, so it is an isomorphism. $\square$

**Example.** The elements with real coefficients, spanned by $e_0, e_1, e_2, e_3$, form a real form; its image under $J$ is the subspace of elements with purely imaginary coefficients, the two meet at zero and their sum is $\mathbb{B}$. Real forms are not unique, and the choice of one is data beyond the real reading.

**Remark (the two real spaces, of dimensions eight and four).** The two dimensions must not be confused. The restriction of scalars of the complex reading is the eight-dimensional space above, whose extension of scalars back to $\mathbb{C}$ has complex dimension eight; the extension of scalars of a real form is the four-dimensional complex space $\mathbb{B}$ itself. What returns the complex reading from the eight-dimensional space is the operator $J$, not a scalar extension. The version of this caution for the algebra and its base rings, where $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$, is *Biquaternions as an Algebra over $\mathbb{R}$*.

**Remark (the remarkable subspaces in the real reading).** The remarkable subspaces are real subspaces, and the complex structure sorts them: the centre and the vector subspace are carried to themselves by $J$ and are the only two that are complex subspaces, of complex dimensions one and three, while the other four are real forms, exchanged in two pairs by $J$. The remarkable subspaces are defined in *Introduction to the Remarkable Subspaces*, and the action of the central imaginary unit upon them is *Comparison of the Remarkable Subspaces*.

### What the View Adds

The real reading sees more subspaces than the complex one, since every complex subspace is a real subspace and the converse fails, and it makes the antilinear maps visible as ordinary linear maps. It costs the complex structure, which leaves the scalars and must be carried by $J$ whenever the complex action is meant. The product stays $\mathbb{R}$-bilinear, so the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are read over $\mathbb{R}$ unchanged; the two ring-based readings, the $\mathbb{H}$-bimodule and the module over $\mathbb{B}$ itself, are *Biquaternions as a Bimodule over $\mathbb{H}$* and *Modules over the General Plain Algebra of Biquaternions*.

## Summary

The biquaternion algebra read over the real scalars is the set $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the scalar domain cut down to the subfield $\mathbb{R}$: the same additive group as the complex reading, of real dimension eight on the basis $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$, twice the complex dimension.

The gap between the two readings is one operator: the multiplication $J : \tilde{Q} \mapsto i\tilde{Q}$ by the central imaginary, real-linear with $J^2 = -\mathrm{id}$, is the complex structure of the real space, and the complex action is the real action together with $J$. A real-linear map is $\mathbb{C}$-linear exactly when it commutes with $J$ and antilinear exactly when it anticommutes; the quaternion conjugation commutes and the other three conjugations anticommute. The real reading therefore sees more linear maps — $\operatorname{End}_\mathbb{R}(\mathbb{B}) \cong M_8(\mathbb{R})$ against $\operatorname{End}_\mathbb{C}(\mathbb{B}) \cong M_4(\mathbb{C})$, of real dimensions $64$ and $32$ — and more subspaces, since every complex subspace is a real one and not conversely.

A real form is a real subspace $V$ of dimension four meeting $JV$ only at zero; then $\mathbb{B} = V \oplus JV$ and $\mathbb{C}\otimes_\mathbb{R}V \cong \mathbb{B}$, so the complex reading is recovered from $V$ by extension of scalars, the choice of $V$ being data beyond the real reading. The remarkable subspaces are real; the centre and the vector subspace are the only two closed under $J$, and the other four are real forms exchanged in pairs.

The product stays $\mathbb{R}$-bilinear, so the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are read over $\mathbb{R}$ unchanged. The product as the multiplication of an algebra over $\mathbb{R}$ is *Biquaternions as an Algebra over $\mathbb{R}$*; the two ring-based readings, the $\mathbb{H}$-bimodule and the module over $\mathbb{B}$ itself, are *Biquaternions as a Bimodule over $\mathbb{H}$* and *Modules over the General Plain Algebra of Biquaternions*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}}\mathbb{B}$ | the real reading: the same additive group and the same elements over the scalars $\mathbb{R}$, dimension $8$ |
| $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$ | the real basis |
| $J : \tilde{Q} \mapsto i\tilde{Q}$ | the real-linear complex structure, $J^2 = -\mathrm{id}$ |
| $\lambda\tilde{Q} = a\tilde{Q} + bJ(\tilde{Q})$ | the complex action read over $\mathbb{R}$, for $\lambda = a + bi$ |
| $\operatorname{End}_\mathbb{R}(\mathbb{B})$ | the real-linear self-maps, $\cong M_8(\mathbb{R})$ |
| $\operatorname{End}_\mathbb{C}(\mathbb{B})$ | the $\mathbb{C}$-linear self-maps, $\cong M_4(\mathbb{C})$, the maps commuting with $J$ |
| real form of $\mathbb{B}$ | a real subspace $V$ of real dimension $4$ with $\mathbb{B} = V \oplus JV$, e.g. the elements with real coefficients |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Clifford-algebra reading of the biquaternions.
