# __The Four General Products of the Biquaternioid $\mathbb{C}$ Space__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products. Each is a rule that sends a pair of elements $(\tilde P,\tilde Q)$ to an element of $\mathbb{B}$, and each is stated below on the coordinates of the two elements. The four sections that follow are independent: the first defines the general plain bilinear product, the second the general plain sesquilinear product, the third the general quaternionic bilinear product, and the fourth the general quaternionic sesquilinear product, and each section is complete in itself, with the coordinates of the product and its scalar–vector form. In the four names, *complex* is the base ring, over which all four general products are written, and *quaternionic* marks a product whose first element is read through the natural conjugation ${}^{\natural}$.

The element is written
$$
\tilde P=P_0e_t+P_1\vec e_x+P_2\vec e_y+P_3\vec e_z , \qquad P_0,P_1,P_2,P_3\in\mathbb{C} ,
$$
and its scalar part and its vector part are $P_0$ and $\vec P=P_1\vec e_x+P_2\vec e_y+P_3\vec e_z$. The four coordinates $P_0,\dots,P_3$ are the ones written against the basis below; the element is recovered from them as the sum above.

The basis of $\mathbb{B}$ is multiplied by
$$
\vec e_x\vec e_y=\vec e_z , \qquad \vec e_y\vec e_z=\vec e_x , \qquad \vec e_z\vec e_x=\vec e_y , \qquad \vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t ,
$$
with $e_t$ the unit of the algebra and $i$ the central scalar imaginary, $i^2=-1$. This is the multiplication table used by all four rules: each of the four multiplies the coordinates of the two elements of the pair by the products $e_\mu e_\nu$ of the basis elements.

The four rules differ in one point alone: whether the coordinates of each of the two elements of the pair are used as they stand or taken from the conjugated element, the two elements being treated independently of one another. The two conjugations used are given in coordinates by
$$
\tilde P^{\natural}=P_0e_t-P_1\vec e_x-P_2\vec e_y-P_3\vec e_z , \qquad
\tilde P^{*}=\overline{P_0}e_t-\overline{P_1}\vec e_x-\overline{P_2}\vec e_y-\overline{P_3}\vec e_z .
$$

Two complex vectors are paired by the complex bilinear dot product and the complex bilinear cross product,
$$
(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k , \qquad
\vec P\times\vec Q=(P_2Q_z-P_3Q_y)\vec e_x+(P_3Q_x-P_1Q_z)\vec e_y+(P_1Q_y-P_2Q_x)\vec e_z ,
$$
and the coefficientwise conjugate of a vector is written $\overline{\vec Q}=\overline{Q_x}\vec e_x+\overline{Q_y}\vec e_y+\overline{Q_z}\vec e_z$. A conjugate of a vector is a complex vector like any other, so the same two pairings serve when one of their arguments is a conjugated vector.

The identities that link the four general products are collected in *Relations Between the Four General Products* and their properties compared in *Comparison Between the Four General Products*. The article assumes the basis and the conjugations from *The Biquaternioid as a Vector Space over $\mathbb{C}$* and *The Group of Involutions*.

## The General Plain Bilinear Product $\tilde P\tilde Q$

**Definition.** The **general plain bilinear product** multiplies the coordinates of the two elements on the basis,
$$
\tilde P\tilde Q=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}P_\mu Q_\nu\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde P\tilde Q=\bigl(P_0Q_t-P_1Q_x-P_2Q_y-P_3Q_z\bigr)
+\bigl(P_0Q_x+P_1Q_t+P_2Q_z-P_3Q_y\bigr)\vec e_x
+\bigl(P_0Q_y-P_1Q_z+P_2Q_t+P_3Q_x\bigr)\vec e_y
+\bigl(P_0Q_z+P_1Q_y-P_2Q_x+P_3Q_t\bigr)\vec e_z .
$$

The rule is linear in the coordinates $P_0,\dots,P_3$ and linear in the coordinates $Q_t,\dots,Q_z$.

**The scalar–vector form.** Collecting the scalar part and the vector part of the two elements,
$$
\tilde P\tilde Q=\bigl(P_0Q_t-(\vec P,\vec Q)\bigr)+P_0\vec Q+Q_t\vec P+\vec P\times\vec Q .
$$

The scalar part is $\mathrm{Sc}(\tilde P\tilde Q)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu P_\mu Q_\mu$ with $\varepsilon=(1,-1,-1,-1)$, and the vector part is the one displayed.

## The General Plain Sesquilinear Product $\tilde P\tilde Q^{*}$

**Definition.** The **general plain sesquilinear product** leaves the first element as it is and reads the second through the conjugation ${}^{*}$. The coordinates of the second element enter as
$$
Q^{*}_0=\overline{Q_t} , \qquad Q^{*}_1=-\overline{Q_x} , \qquad Q^{*}_2=-\overline{Q_y} , \qquad Q^{*}_3=-\overline{Q_z} ,
$$
and the product is
$$
\tilde P\tilde Q^{*}=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}P_\mu Q^{*}_\nu\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\nu P_\mu \overline{Q_\nu}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde P\tilde Q^{*}=\bigl(P_0\overline{Q_t}+P_1\overline{Q_x}+P_2\overline{Q_y}+P_3\overline{Q_z}\bigr)
+\bigl(-P_0\overline{Q_x}+P_1\overline{Q_t}-P_2\overline{Q_z}+P_3\overline{Q_y}\bigr)\vec e_x
+\bigl(-P_0\overline{Q_y}+P_1\overline{Q_z}+P_2\overline{Q_t}-P_3\overline{Q_x}\bigr)\vec e_y
+\bigl(-P_0\overline{Q_z}-P_1\overline{Q_y}+P_2\overline{Q_x}+P_3\overline{Q_t}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $P_0,\dots,P_3$ and conjugate-linear in the coordinates $Q_t,\dots,Q_z$, conjugation of the coefficients happening inside the product.

**The scalar–vector form.** The scalar part of the second factor becomes $\overline{Q_t}$ and its vector part becomes $-\overline{\vec Q}$, so the two pairings change sign and are read against the conjugate vector,
$$
\tilde P\tilde Q^{*}=\bigl(P_0\overline{Q_t}+(\vec P,\overline{\vec Q})\bigr)-P_0\overline{\vec Q}+\overline{Q_t}\vec P-\vec P\times\overline{\vec Q} .
$$

The scalar part is $\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_{\mu\in\{t,x,y,z\}}P_\mu\overline{Q_\mu}$, conjugate-linear in the coordinates of the second element; the vector part is the one displayed.

## The General Quaternionic Bilinear Product $\tilde P^{\natural}\tilde Q$

**Definition.** The **general quaternionic bilinear product** reads the first element through the conjugation ${}^{\natural}$ and leaves the second as it is. The coordinates of the first element enter as
$$
P^{\natural}_0=P_0 , \qquad P^{\natural}_1=-P_1 , \qquad P^{\natural}_2=-P_2 , \qquad P^{\natural}_3=-P_3 ,
$$
and the product is
$$
\tilde P^{\natural}\tilde Q=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}P^{\natural}_\mu Q_\nu\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\mu P_\mu Q_\nu\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde P^{\natural}\tilde Q=\bigl(P_0Q_t+P_1Q_x+P_2Q_y+P_3Q_z\bigr)
+\bigl(P_0Q_x-P_1Q_t-P_2Q_z+P_3Q_y\bigr)\vec e_x
+\bigl(P_0Q_y+P_1Q_z-P_2Q_t-P_3Q_x\bigr)\vec e_y
+\bigl(P_0Q_z-P_1Q_y+P_2Q_x-P_3Q_t\bigr)\vec e_z .
$$

The rule is linear in the coordinates $P_0,\dots,P_3$ and linear in the coordinates $Q_t,\dots,Q_z$.

**The scalar–vector form.** The scalar part of the first factor stays $P_0$ and its vector part becomes $-\vec P$, so the two pairings change sign where that vector part enters,
$$
\tilde P^{\natural}\tilde Q=\bigl(P_0Q_t+(\vec P,\vec Q)\bigr)+P_0\vec Q-Q_t\vec P-\vec P\times\vec Q .
$$

The scalar part is $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_{\mu\in\{t,x,y,z\}}P_\mu Q_\mu$, and the vector part is the one displayed.

## The General Quaternionic Sesquilinear Product $\tilde P^{\natural}\tilde Q^{*}$

**Definition.** The **general quaternionic sesquilinear product** reads the first element through ${}^{\natural}$ and the second through ${}^{*}$, the two being read independently. The coordinates enter as $P^{\natural}_\mu$ in the first factor and $Q^{*}_\nu$ in the second, and the product is
$$
\tilde P^{\natural}\tilde Q^{*}=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}P^{\natural}_\mu Q^{*}_\nu\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\mu\varepsilon_\nu P_\mu \overline{Q_\nu}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde P^{\natural}\tilde Q^{*}=\bigl(P_0\overline{Q_t}-P_1\overline{Q_x}-P_2\overline{Q_y}-P_3\overline{Q_z}\bigr)
+\bigl(-P_0\overline{Q_x}-P_1\overline{Q_t}+P_2\overline{Q_z}-P_3\overline{Q_y}\bigr)\vec e_x
+\bigl(-P_0\overline{Q_y}-P_1\overline{Q_z}-P_2\overline{Q_t}+P_3\overline{Q_x}\bigr)\vec e_y
+\bigl(-P_0\overline{Q_z}+P_1\overline{Q_y}-P_2\overline{Q_x}-P_3\overline{Q_t}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $P_0,\dots,P_3$ and conjugate-linear in the coordinates $Q_t,\dots,Q_z$.

**The scalar–vector form.** The scalar part of the first factor is $P_0$ and its vector part is $-\vec P$; the scalar part of the second is $\overline{Q_t}$ and its vector part is $-\overline{\vec Q}$, so the dot product enters with a negative sign and the cross product with a positive one, read against the conjugate vector,
$$
\tilde P^{\natural}\tilde Q^{*}=\bigl(P_0\overline{Q_t}-(\vec P,\overline{\vec Q})\bigr)-P_0\overline{\vec Q}-\overline{Q_t}\vec P+\vec P\times\overline{\vec Q} .
$$

The scalar part is $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu P_\mu\overline{Q_\mu}$, conjugate-linear in the coordinates of the second element; the vector part is the one displayed.

## Summary

Four products are defined on the underlying $\mathbb{C}$-vector space of $\mathbb{B}$, each on the coordinates of the two elements of the pair and each with its scalar–vector form:

| product | scalar part | vector part |
|---|---|---|
| $\tilde P\tilde Q$ | $P_0Q_t-(\vec P,\vec Q)$ | $P_0\vec Q+Q_t\vec P+\vec P\times\vec Q$ |
| $\tilde P\tilde Q^{*}$ | $P_0\overline{Q_t}+(\vec P,\overline{\vec Q})$ | $-P_0\overline{\vec Q}+\overline{Q_t}\vec P-\vec P\times\overline{\vec Q}$ |
| $\tilde P^{\natural}\tilde Q$ | $P_0Q_t+(\vec P,\vec Q)$ | $P_0\vec Q-Q_t\vec P-\vec P\times\vec Q$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $P_0\overline{Q_t}-(\vec P,\overline{\vec Q})$ | $-P_0\overline{\vec Q}-\overline{Q_t}\vec P+\vec P\times\overline{\vec Q}$ |

The general plain bilinear product multiplies the coordinates $P_\mu$ and $Q_\nu$ on the basis, $\tilde P\tilde Q=\sum_{\mu,\nu}P_\mu Q_\nu e_\mu e_\nu$, and is linear in both sets of coordinates. The general plain sesquilinear product multiplies $P_\mu$ and $Q^{*}_\nu$, that is, the second element is read through ${}^{*}$; it is linear in the coordinates of the first element and conjugate-linear in those of the second. The general quaternionic bilinear product multiplies $P^{\natural}_\mu$ and $Q_\nu$, that is, the first element is read through ${}^{\natural}$; it is linear in both sets of coordinates. The general quaternionic sesquilinear product multiplies $P^{\natural}_\mu$ and $Q^{*}_\nu$, both elements being read through their conjugations, and is linear in the first set of coordinates and conjugate-linear in the second.

The four scalar parts are the four displayed in the table, and the four vector parts beside them are the four displayed beside them. The identities that link the four general products, and the relations among the four scalar parts and the four vector parts, are *Relations Between the Four General Products*. Which of the four general products is a multiplication in the sense of algebra is *Comparison Between the Four General Products*. The split of each of the four general products into a symmetric and an antisymmetric part, and the Jordan and the Lie structure that the two parts of the general plain bilinear product carry, are *The 12 Products of the Biquaternioid Complex Space*, which takes the four general products from here.

Two exchanges act on the four general products. The **exchange by a conjugation** $c$, $\tilde{P}\tilde{Q}^{*}\mapsto c(\tilde{Q}\tilde{P}^{*})$, composes the swap with $c$ and is the one that keeps the class of the two sesquilinear products, whose parts under it are sesquilinear again, and it is the exchange the twelve names are read against; the **plain exchange**, which swaps the two elements of the pair, does not keep the class, a part of a sesquilinear product taken under it being only $\mathbb{R}$-bilinear. For the plain sesquilinear product and $c=\overline{\cdot}$ the two adapted parts are its scalar part and its vector part, displayed in the table above as the two halves of the second row; for the general quaternionic sesquilinear product they are the symmetrisation of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$ and half their commutator. Both exchanges and their two splits are read in *The 12 Products of the Biquaternioid Complex Space*, §*The Other Exchange, and the Class It Keeps*, and the general construction is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*. The behaviour of the general plain bilinear product on each of the remarkable subspaces is tabulated in *Remarkable Subspaces and the Four General Products*; the operators of left and right multiplication are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; and the basis products written out one by one are in *Introduction to the Biquaternion Algebra*, §*The Multiplication Table*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\tilde Q$ | the general plain bilinear product |
| $\tilde P\tilde Q^{*}$ | the general plain sesquilinear product |
| $\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| $\tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product |
| $\tilde P=P_0e_t+\dots+P_3\vec e_z$ | the element and its four complex coordinates |
| $\tilde P^{\natural}$, $\tilde P^{*}$ | the two conjugations, in coordinates |
| $\vec P$ | the vector part $P_1\vec e_x+P_2\vec e_y+P_3\vec e_z$ |
| $(\vec P,\vec Q)$ | the complex bilinear dot product, $\sum_kP_kQ_k$ |
| $\vec P\times\vec Q$ | the complex bilinear cross product |
| $\overline{\vec Q}$ | the coefficientwise conjugate of the vector part |
| $\varepsilon$ | the sign vector $(1,-1,-1,-1)$ |
| $\mathrm{Sc}$, $\mathrm{Vec}$ | the scalar part and the vector part of an element |

## Further Reading

- *The Four General Products and Operators* (`articles_maths/the-four-general-products-and-operators.md`), for what the four rules decide (the four pairings and their adjoints) and what they do not decide (an operator), read on one element through the four insertions
- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original product of the units whose coordinate rule the general plain bilinear product extends.
- *Relations Between the Four General Products* (`articles_maths/relations-between-the-four-general-products.md`), for the identities that link the four.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table of the four.
- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the symmetric and the antisymmetric part of each of the four general products.
