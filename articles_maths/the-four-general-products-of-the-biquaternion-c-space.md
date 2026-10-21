# __The Four General Products of the Biquaternion $\mathbb{C}$ Space__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products. Each is a rule that sends a pair of elements $(\tilde Q_1,\tilde Q_2)$ to an element of $\mathbb{B}$, and each is stated below on the coordinates of the two elements. The four sections that follow are independent: the first defines the general plain bilinear product, the second the general plain sesquilinear product, the third the general quaternionic bilinear product, and the fourth the general quaternionic sesquilinear product, and each section is complete in itself, with the coordinates of the product and its scalar–vector form. It opens the group *The Four General Products* and carries the four rules and their coordinate forms. In the four names, *complex* is the base ring, over which all four general products are written, and *quaternionic* marks a product whose first element is read through the natural conjugation ${}^{\natural}$.

The element is written
$$
\tilde Q_1=Q_{1,0}e_t+Q_{1,1}\vec e_x+Q_{1,2}\vec e_y+Q_{1,3}\vec e_z , \qquad Q_{1,0},Q_{1,1},Q_{1,2},Q_{1,3}\in\mathbb{C} ,
$$
and its scalar part and its vector part are $Q_{1,0}$ and $\vec Q_1=Q_{1,1}\vec e_x+Q_{1,2}\vec e_y+Q_{1,3}\vec e_z$. The four coordinates $Q_{1,0},\dots,Q_{1,3}$ are the ones written against the basis below; the element is recovered from them as the sum above.

The basis of $\mathbb{B}$ is multiplied by
$$
\vec e_x\vec e_y=\vec e_z , \qquad \vec e_y\vec e_z=\vec e_x , \qquad \vec e_z\vec e_x=\vec e_y , \qquad \vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t ,
$$
with $e_t$ the unit of the algebra and $i$ the central scalar imaginary, $i^2=-1$. This is the multiplication table used by all four rules: each of the four multiplies the coordinates of the two elements of the pair by the products $e_\mu e_\nu$ of the basis elements.

The four rules differ in one point alone: whether the coordinates of each of the two elements of the pair are used as they stand or taken from the conjugated element, the two elements being treated independently of one another. The two conjugations used are given in coordinates by
$$
\tilde Q_1^{\natural}=Q_{1,0}e_t-Q_{1,1}\vec e_x-Q_{1,2}\vec e_y-Q_{1,3}\vec e_z , \qquad
\tilde Q_1^{*}=\overline{Q_{1,0}}e_t-\overline{Q_{1,1}}\vec e_x-\overline{Q_{1,2}}\vec e_y-\overline{Q_{1,3}}\vec e_z .
$$

Two complex vectors are paired by the complex bilinear dot product and the complex bilinear cross product,
$$
(\vec Q_1,\vec Q_2)=\sum_{k=1}^{3}Q_{1,k}Q_{2,k} , \qquad
\vec Q_1\times\vec Q_2=(Q_{1,2}Q_{2z}-Q_{1,3}Q_{2y})\vec e_x+(Q_{1,3}Q_{2x}-Q_{1,1}Q_{2z})\vec e_y+(Q_{1,1}Q_{2y}-Q_{1,2}Q_{2x})\vec e_z ,
$$
and the coefficientwise conjugate of a vector is written $\overline{\vec Q}=\overline{Q_x}\vec e_x+\overline{Q_y}\vec e_y+\overline{Q_z}\vec e_z$. A conjugate of a vector is a complex vector like any other, so the same two pairings serve when one of their arguments is a conjugated vector.

The identities that link the four general products are collected in *Relations Between the Four General Products* and their properties compared in *Comparison Between the Four General Products*. The article assumes the basis and the conjugations from *The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$* and *The Group of Involutions*.

## The General Plain Bilinear Product $\tilde Q_1\tilde Q_2$

**Definition.** The **general plain bilinear product** multiplies the coordinates of the two elements on the basis,
$$
\tilde Q_1\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}Q_{1,\mu} Q_{2,\nu}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde Q_1\tilde Q_2=\bigl(Q_{1,0}Q_{2t}-Q_{1,1}Q_{2x}-Q_{1,2}Q_{2y}-Q_{1,3}Q_{2z}\bigr)
+\bigl(Q_{1,0}Q_{2x}+Q_{1,1}Q_{2t}+Q_{1,2}Q_{2z}-Q_{1,3}Q_{2y}\bigr)\vec e_x
+\bigl(Q_{1,0}Q_{2y}-Q_{1,1}Q_{2z}+Q_{1,2}Q_{2t}+Q_{1,3}Q_{2x}\bigr)\vec e_y
+\bigl(Q_{1,0}Q_{2z}+Q_{1,1}Q_{2y}-Q_{1,2}Q_{2x}+Q_{1,3}Q_{2t}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $Q_{1,0},\dots,Q_{1,3}$ and linear in the coordinates $Q_{2t},\dots,Q_{2z}$.

**The scalar–vector form.** Collecting the scalar part and the vector part of the two elements,
$$
\tilde Q_1\tilde Q_2=\bigl(Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr)+Q_{1,0}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2 .
$$

The scalar part is $\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1,\mu} Q_{2,\mu}$ with $\varepsilon=(1,-1,-1,-1)$, and the vector part is the one displayed.

## The General Plain Sesquilinear Product $\tilde Q_1\tilde Q_2^{*}$

**Definition.** The **general plain sesquilinear product** leaves the first element as it is and reads the second through the conjugation ${}^{*}$. The coordinates of the second element enter as
$$
Q^{*}_0=\overline{Q_t} , \qquad Q^{*}_1=-\overline{Q_x} , \qquad Q^{*}_2=-\overline{Q_y} , \qquad Q^{*}_3=-\overline{Q_z} ,
$$
and the product is
$$
\tilde Q_1\tilde Q_2^{*}=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}Q_{1,\mu} (Q_2^{*})_\nu\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\nu Q_{1,\mu} \overline{Q_{2,\nu}}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde Q_1\tilde Q_2^{*}=\bigl(Q_{1,0}\overline{Q_{2t}}+Q_{1,1}\overline{Q_{2x}}+Q_{1,2}\overline{Q_{2y}}+Q_{1,3}\overline{Q_{2z}}\bigr)
+\bigl(-Q_{1,0}\overline{Q_{2x}}+Q_{1,1}\overline{Q_{2t}}-Q_{1,2}\overline{Q_{2z}}+Q_{1,3}\overline{Q_{2y}}\bigr)\vec e_x
+\bigl(-Q_{1,0}\overline{Q_{2y}}+Q_{1,1}\overline{Q_{2z}}+Q_{1,2}\overline{Q_{2t}}-Q_{1,3}\overline{Q_{2x}}\bigr)\vec e_y
+\bigl(-Q_{1,0}\overline{Q_{2z}}-Q_{1,1}\overline{Q_{2y}}+Q_{1,2}\overline{Q_{2x}}+Q_{1,3}\overline{Q_{2t}}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $Q_{1,0},\dots,Q_{1,3}$ and conjugate-linear in the coordinates $Q_{2t},\dots,Q_{2z}$, conjugation of the coefficients happening inside the product.

**The scalar–vector form.** The scalar part of the second factor becomes $\overline{Q_t}$ and its vector part becomes $-\overline{\vec Q}$, so the two pairings change sign and are read against the conjugate vector,
$$
\tilde Q_1\tilde Q_2^{*}=\bigl(Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr)-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2} .
$$

The scalar part is $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_{\mu\in\{t,x,y,z\}}Q_{1,\mu}\overline{Q_{2,\mu}}$, conjugate-linear in the coordinates of the second element; the vector part is the one displayed.

## The General Quaternionic Bilinear Product $\tilde Q_1^{\natural}\tilde Q_2$

**Definition.** The **general quaternionic bilinear product** reads the first element through the conjugation ${}^{\natural}$ and leaves the second as it is. The coordinates of the first element enter as
$$
(Q_1^{\natural})_0=Q_{1,0} , \qquad (Q_1^{\natural})_1=-Q_{1,1} , \qquad (Q_1^{\natural})_2=-Q_{1,2} , \qquad (Q_1^{\natural})_3=-Q_{1,3} ,
$$
and the product is
$$
\tilde Q_1^{\natural}\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}(Q_1^{\natural})_\mu Q_{2,\nu}\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1,\mu} Q_{2,\nu}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde Q_1^{\natural}\tilde Q_2=\bigl(Q_{1,0}Q_{2t}+Q_{1,1}Q_{2x}+Q_{1,2}Q_{2y}+Q_{1,3}Q_{2z}\bigr)
+\bigl(Q_{1,0}Q_{2x}-Q_{1,1}Q_{2t}-Q_{1,2}Q_{2z}+Q_{1,3}Q_{2y}\bigr)\vec e_x
+\bigl(Q_{1,0}Q_{2y}+Q_{1,1}Q_{2z}-Q_{1,2}Q_{2t}-Q_{1,3}Q_{2x}\bigr)\vec e_y
+\bigl(Q_{1,0}Q_{2z}-Q_{1,1}Q_{2y}+Q_{1,2}Q_{2x}-Q_{1,3}Q_{2t}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $Q_{1,0},\dots,Q_{1,3}$ and linear in the coordinates $Q_{2t},\dots,Q_{2z}$.

**The scalar–vector form.** The scalar part of the first factor stays $Q_{1,0}$ and its vector part becomes $-\vec Q_1$, so the two pairings change sign where that vector part enters,
$$
\tilde Q_1^{\natural}\tilde Q_2=\bigl(Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr)+Q_{1,0}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 .
$$

The scalar part is $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=\sum_{\mu\in\{t,x,y,z\}}Q_{1,\mu} Q_{2,\mu}$, and the vector part is the one displayed.

## The General Quaternionic Sesquilinear Product $\tilde Q_1^{\natural}\tilde Q_2^{*}$

**Definition.** The **general quaternionic sesquilinear product** reads the first element through ${}^{\natural}$ and the second through ${}^{*}$, the two being read independently. The coordinates enter as $(Q_1^{\natural})_\mu$ in the first factor and $(Q_2^{*})_\nu$ in the second, and the product is
$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}(Q_1^{\natural})_\mu (Q_2^{*})_\nu\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\mu\varepsilon_\nu Q_{1,\mu} \overline{Q_{2,\nu}}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl(Q_{1,0}\overline{Q_{2t}}-Q_{1,1}\overline{Q_{2x}}-Q_{1,2}\overline{Q_{2y}}-Q_{1,3}\overline{Q_{2z}}\bigr)
+\bigl(-Q_{1,0}\overline{Q_{2x}}-Q_{1,1}\overline{Q_{2t}}+Q_{1,2}\overline{Q_{2z}}-Q_{1,3}\overline{Q_{2y}}\bigr)\vec e_x
+\bigl(-Q_{1,0}\overline{Q_{2y}}-Q_{1,1}\overline{Q_{2z}}-Q_{1,2}\overline{Q_{2t}}+Q_{1,3}\overline{Q_{2x}}\bigr)\vec e_y
+\bigl(-Q_{1,0}\overline{Q_{2z}}+Q_{1,1}\overline{Q_{2y}}-Q_{1,2}\overline{Q_{2x}}-Q_{1,3}\overline{Q_{2t}}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $Q_{1,0},\dots,Q_{1,3}$ and conjugate-linear in the coordinates $Q_{2t},\dots,Q_{2z}$.

**The scalar–vector form.** The scalar part of the first factor is $Q_{1,0}$ and its vector part is $-\vec Q_1$; the scalar part of the second is $\overline{Q_{2t}}$ and its vector part is $-\overline{\vec Q_2}$, so the dot product enters with a negative sign and the cross product with a positive one, read against the conjugate vector,
$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl(Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr)-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2} .
$$

The scalar part is $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$, conjugate-linear in the coordinates of the second element; the vector part is the one displayed.

## Summary

Four products are defined on the underlying $\mathbb{C}$-vector space of $\mathbb{B}$, each on the coordinates of the two elements of the pair and each with its scalar–vector form:

| product | scalar part | vector part |
|---|---|---|
| $\tilde Q_1\tilde Q_2$ | $Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2)$ | $Q_{1,0}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$ |
| $\tilde Q_1\tilde Q_2^{*}$ | $Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | $-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2)$ | $Q_{1,0}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | $-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$ |

The general plain bilinear product multiplies the coordinates $Q_{1,\mu}$ and $Q_{2,\nu}$ on the basis, $\tilde Q_1\tilde Q_2=\sum_{\mu,\nu}Q_{1,\mu} Q_{2,\nu} e_\mu e_\nu$, and is linear in both sets of coordinates. The general plain sesquilinear product multiplies $Q_{1,\mu}$ and $(Q_2^{*})_\nu$, that is, the second element is read through ${}^{*}$; it is linear in the coordinates of the first element and conjugate-linear in those of the second. The general quaternionic bilinear product multiplies $(Q_1^{\natural})_\mu$ and $Q_{2,\nu}$, that is, the first element is read through ${}^{\natural}$; it is linear in both sets of coordinates. The general quaternionic sesquilinear product multiplies $(Q_1^{\natural})_\mu$ and $(Q_2^{*})_\nu$, both elements being read through their conjugations, and is linear in the first set of coordinates and conjugate-linear in the second.

The four scalar parts are the four displayed in the table, and the four vector parts beside them are the four displayed beside them. The identities that link the four general products, and the relations among the four scalar parts and the four vector parts, are *Relations Between the Four General Products*. Which of the four general products is a multiplication in the sense of algebra is *Comparison Between the Four General Products*. The split of each of the four general products into a symmetric and an antisymmetric part, and the Jordan and the Lie structure that the two parts of the general plain bilinear product carry, are *The 12 Products of the Biquaternion Complex Space*, which takes the four general products from here.

Two exchanges act on the four general products. The **exchange by a conjugation** $c$, $\tilde Q_1\tilde Q_2^{*}\mapsto c(\tilde Q_2\tilde Q_1^{*})$, composes the swap with $c$ and is the one that keeps the class of the two sesquilinear products, whose parts under it are sesquilinear again, and it is the exchange the twelve names are read against; the **plain exchange**, which swaps the two elements of the pair, does not keep the class, a part of a sesquilinear product taken under it being only $\mathbb{R}$-bilinear. For the plain sesquilinear product and $c=\overline{\cdot}$ the two adapted parts are its scalar part and its vector part, displayed in the table above as the two halves of the second row; for the general quaternionic sesquilinear product they are the symmetrisation of $\tilde Q_1^{\natural}$ with $\tilde Q_2^{*}$ and half their commutator. Both exchanges and their two splits are read in *The 12 Products of the Biquaternion Complex Space*, §*The Other Exchange, and the Class It Keeps*, and the general construction is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*. The behaviour of the general plain bilinear product on each of the remarkable subspaces is tabulated in *Remarkable Subspaces and the Four General Products*; the operators of left and right multiplication are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; and the basis products written out one by one are in *Introduction to the Biquaternion Algebra*, §*The Multiplication Table*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1\tilde Q_2$ | the general plain bilinear product |
| $\tilde Q_1\tilde Q_2^{*}$ | the general plain sesquilinear product |
| $\tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquilinear product |
| $\tilde Q_1=Q_{1,0}e_t+\dots+Q_{1,3}\vec e_z$ | the element and its four complex coordinates |
| $\tilde Q_1^{\natural}$, $\tilde Q_1^{*}$ | the two conjugations, in coordinates |
| $\vec Q_1$ | the vector part $Q_{1,1}\vec e_x+Q_{1,2}\vec e_y+Q_{1,3}\vec e_z$ |
| $(\vec Q_1,\vec Q_2)$ | the complex bilinear dot product, $\sum_kQ_{1,k}Q_{2,k}$ |
| $\vec Q_1\times\vec Q_2$ | the complex bilinear cross product |
| $\overline{\vec Q}$ | the coefficientwise conjugate of the vector part |
| $\varepsilon$ | the sign vector $(1,-1,-1,-1)$ |
| $\mathrm{Sc}$, $\mathrm{Vec}$ | the scalar part and the vector part of an element |

## Further Reading

- [The Four General Products and Operators](the-four-general-products-and-operators.html), for what the four rules decide (the four pairings and their adjoints) and what they do not decide (an operator), read on one element through the four insertions
- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original product of the units whose coordinate rule the general plain bilinear product extends.
- [Relations Between the Four General Products](relations-between-the-four-general-products.html), for the identities that link the four.
- [Comparison Between the Four General Products](comparison-between-the-four-general-products.html), for the property table of the four.
- [The 12 Products of the Biquaternion Complex Space](the-12-products-of-the-biquaternion-complex-space.html), for the symmetric and the antisymmetric part of each of the four general products.
