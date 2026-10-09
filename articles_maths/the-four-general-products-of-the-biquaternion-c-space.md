# __The Four General Products of the Biquaternion $\mathbb{C}$ Space__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products. Each is a rule that sends a pair of elements $(\tilde P,\tilde Q)$ to an element of $\mathbb{B}$, and each is stated below on the coordinates of the two elements. The four sections that follow are independent: the first defines the general plain bilinear product, the second the general quaternionic bilinear product, the third the general plain sesquilinear product, and the fourth the general quaternionic sesquilinear product, and each section is complete in itself, with the coordinates of the product and its scalar–vector form. In the four names, *complex* is the base ring, over which all four general products are written, and *quaternionic* marks a product whose first element is read through the natural conjugation ${}^{\natural}$.

The element is written
$$
\tilde P=P_0e_0+P_1e_1+P_2e_2+P_3e_3 , \qquad P_0,P_1,P_2,P_3\in\mathbb{C} ,
$$
and its scalar part and its vector part are $P_0$ and $\mathbf P=P_1e_1+P_2e_2+P_3e_3$. The four coordinates $P_0,\dots,P_3$ are the ones written against the basis below; the element is recovered from them as the sum above.

The basis of $\mathbb{B}$ is multiplied by
$$
e_1e_2=e_3 , \qquad e_2e_3=e_1 , \qquad e_3e_1=e_2 , \qquad e_1^2=e_2^2=e_3^2=-e_0 ,
$$
with $e_0$ the unit of the algebra and $i$ the central scalar imaginary, $i^2=-1$. This is the multiplication table used by all four rules: each of the four multiplies the coordinates of the two elements of the pair by the products $e_\mu e_\nu$ of the basis elements.

The four rules differ in one point alone: whether the coordinates of each of the two elements of the pair are used as they stand or taken from the conjugated element, the two elements being treated independently of one another. The two conjugations used are given in coordinates by
$$
\tilde P^{\natural}=P_0e_0-P_1e_1-P_2e_2-P_3e_3 , \qquad
\tilde P^{*}=\overline{P_0}e_0-\overline{P_1}e_1-\overline{P_2}e_2-\overline{P_3}e_3 .
$$

Two complex vectors are paired by the complex bilinear dot product and the complex bilinear cross product,
$$
(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k , \qquad
\mathbf P\times\mathbf Q=(P_2Q_3-P_3Q_2)e_1+(P_3Q_1-P_1Q_3)e_2+(P_1Q_2-P_2Q_1)e_3 ,
$$
and the coefficientwise conjugate of a vector is written $\overline{\mathbf Q}=\overline{Q_1}e_1+\overline{Q_2}e_2+\overline{Q_3}e_3$. A conjugate of a vector is a complex vector like any other, so the same two pairings serve when one of their arguments is a conjugated vector.

The identities that link the four general products are collected in *Relations Between the Four General Products* and their properties compared in *Comparison Between the Four General Products*. The article assumes the basis and the conjugations from *Biquaternions as a Vector Space over $\mathbb{C}$* and *The Group of Involutions*.

## The General Plain Bilinear Product $\tilde P\tilde Q$

**Definition.** The **general plain bilinear product** multiplies the coordinates of the two elements on the basis,
$$
\tilde P\tilde Q=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}P_\mu Q_\nu\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde P\tilde Q=\bigl(P_0Q_0-P_1Q_1-P_2Q_2-P_3Q_3\bigr)
+\bigl(P_0Q_1+P_1Q_0+P_2Q_3-P_3Q_2\bigr)e_1
+\bigl(P_0Q_2-P_1Q_3+P_2Q_0+P_3Q_1\bigr)e_2
+\bigl(P_0Q_3+P_1Q_2-P_2Q_1+P_3Q_0\bigr)e_3 .
$$

The rule is linear in the coordinates $P_0,\dots,P_3$ and linear in the coordinates $Q_0,\dots,Q_3$.

**The scalar–vector form.** Collecting the scalar part and the vector part of the two elements,
$$
\tilde P\tilde Q=\bigl(P_0Q_0-(\mathbf P,\mathbf Q)\bigr)+P_0\mathbf Q+Q_0\mathbf P+\mathbf P\times\mathbf Q .
$$

The scalar part is $\mathrm{Sc}(\tilde P\tilde Q)=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu Q_\mu$ with $\varepsilon=(1,-1,-1,-1)$, and the vector part is the one displayed.

## The General Quaternionic Bilinear Product $\tilde P^{\natural}\tilde Q$

**Definition.** The **general quaternionic bilinear product** reads the first element through the conjugation ${}^{\natural}$ and leaves the second as it is. The coordinates of the first element enter as
$$
P^{\natural}_0=P_0 , \qquad P^{\natural}_1=-P_1 , \qquad P^{\natural}_2=-P_2 , \qquad P^{\natural}_3=-P_3 ,
$$
and the product is
$$
\tilde P^{\natural}\tilde Q=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}P^{\natural}_\mu Q_\nu\,e_\mu e_\nu
=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}\varepsilon_\mu P_\mu Q_\nu\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde P^{\natural}\tilde Q=\bigl(P_0Q_0+P_1Q_1+P_2Q_2+P_3Q_3\bigr)
+\bigl(P_0Q_1-P_1Q_0-P_2Q_3+P_3Q_2\bigr)e_1
+\bigl(P_0Q_2+P_1Q_3-P_2Q_0-P_3Q_1\bigr)e_2
+\bigl(P_0Q_3-P_1Q_2+P_2Q_1-P_3Q_0\bigr)e_3 .
$$

The rule is linear in the coordinates $P_0,\dots,P_3$ and linear in the coordinates $Q_0,\dots,Q_3$.

**The scalar–vector form.** The scalar part of the first factor stays $P_0$ and its vector part becomes $-\mathbf P$, so the two pairings change sign where that vector part enters,
$$
\tilde P^{\natural}\tilde Q=\bigl(P_0Q_0+(\mathbf P,\mathbf Q)\bigr)+P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q .
$$

The scalar part is $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_{\mu=0}^{3}P_\mu Q_\mu$, and the vector part is the one displayed.

## The General Plain Sesquilinear Product $\tilde P\tilde Q^{*}$

**Definition.** The **general plain sesquilinear product** leaves the first element as it is and reads the second through the conjugation ${}^{*}$. The coordinates of the second element enter as
$$
Q^{*}_0=\overline{Q_0} , \qquad Q^{*}_1=-\overline{Q_1} , \qquad Q^{*}_2=-\overline{Q_2} , \qquad Q^{*}_3=-\overline{Q_3} ,
$$
and the product is
$$
\tilde P\tilde Q^{*}=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}P_\mu Q^{*}_\nu\,e_\mu e_\nu
=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}\varepsilon_\nu P_\mu \overline{Q_\nu}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde P\tilde Q^{*}=\bigl(P_0\overline{Q_0}+P_1\overline{Q_1}+P_2\overline{Q_2}+P_3\overline{Q_3}\bigr)
+\bigl(-P_0\overline{Q_1}+P_1\overline{Q_0}-P_2\overline{Q_3}+P_3\overline{Q_2}\bigr)e_1
+\bigl(-P_0\overline{Q_2}+P_1\overline{Q_3}+P_2\overline{Q_0}-P_3\overline{Q_1}\bigr)e_2
+\bigl(-P_0\overline{Q_3}-P_1\overline{Q_2}+P_2\overline{Q_1}+P_3\overline{Q_0}\bigr)e_3 .
$$

The rule is linear in the coordinates $P_0,\dots,P_3$ and conjugate-linear in the coordinates $Q_0,\dots,Q_3$, conjugation of the coefficients happening inside the product.

**The scalar–vector form.** The scalar part of the second factor becomes $\overline{Q_0}$ and its vector part becomes $-\overline{\mathbf Q}$, so the two pairings change sign and are read against the conjugate vector,
$$
\tilde P\tilde Q^{*}=\bigl(P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})\bigr)-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q} .
$$

The scalar part is $\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_{\mu=0}^{3}P_\mu\overline{Q_\mu}$, conjugate-linear in the coordinates of the second element; the vector part is the one displayed.

## The General Quaternionic Sesquilinear Product $\tilde P^{\natural}\tilde Q^{*}$

**Definition.** The **general quaternionic sesquilinear product** reads the first element through ${}^{\natural}$ and the second through ${}^{*}$, the two being read independently. The coordinates enter as $P^{\natural}_\mu$ in the first factor and $Q^{*}_\nu$ in the second, and the product is
$$
\tilde P^{\natural}\tilde Q^{*}=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}P^{\natural}_\mu Q^{*}_\nu\,e_\mu e_\nu
=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}\varepsilon_\mu\varepsilon_\nu P_\mu \overline{Q_\nu}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde P^{\natural}\tilde Q^{*}=\bigl(P_0\overline{Q_0}-P_1\overline{Q_1}-P_2\overline{Q_2}-P_3\overline{Q_3}\bigr)
+\bigl(-P_0\overline{Q_1}-P_1\overline{Q_0}+P_2\overline{Q_3}-P_3\overline{Q_2}\bigr)e_1
+\bigl(-P_0\overline{Q_2}-P_1\overline{Q_3}-P_2\overline{Q_0}+P_3\overline{Q_1}\bigr)e_2
+\bigl(-P_0\overline{Q_3}+P_1\overline{Q_2}-P_2\overline{Q_1}-P_3\overline{Q_0}\bigr)e_3 .
$$

The rule is linear in the coordinates $P_0,\dots,P_3$ and conjugate-linear in the coordinates $Q_0,\dots,Q_3$.

**The scalar–vector form.** The scalar part of the first factor is $P_0$ and its vector part is $-\mathbf P$; the scalar part of the second is $\overline{Q_0}$ and its vector part is $-\overline{\mathbf Q}$, so the dot product enters with a negative sign and the cross product with a positive one, read against the conjugate vector,
$$
\tilde P^{\natural}\tilde Q^{*}=\bigl(P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})\bigr)-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P+\mathbf P\times\overline{\mathbf Q} .
$$

The scalar part is $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu\overline{Q_\mu}$, conjugate-linear in the coordinates of the second element; the vector part is the one displayed.

## Summary

Four products are defined on the underlying $\mathbb{C}$-vector space of $\mathbb{B}$, each on the coordinates of the two elements of the pair and each with its scalar–vector form:

| product | scalar part | vector part |
|---|---|---|
| $\tilde P\tilde Q$ | $P_0Q_0-(\mathbf P,\mathbf Q)$ | $P_0\mathbf Q+Q_0\mathbf P+\mathbf P\times\mathbf Q$ |
| $\tilde P^{\natural}\tilde Q$ | $P_0Q_0+(\mathbf P,\mathbf Q)$ | $P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ |
| $\tilde P\tilde Q^{*}$ | $P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$ | $-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$ | $-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P+\mathbf P\times\overline{\mathbf Q}$ |

The general plain bilinear product multiplies the coordinates $P_\mu$ and $Q_\nu$ on the basis, $\tilde P\tilde Q=\sum_{\mu,\nu}P_\mu Q_\nu e_\mu e_\nu$, and is linear in both sets of coordinates. The general quaternionic bilinear product multiplies $P^{\natural}_\mu$ and $Q_\nu$, that is, the first element is read through ${}^{\natural}$; it is linear in both sets of coordinates. The general plain sesquilinear product multiplies $P_\mu$ and $Q^{*}_\nu$, that is, the second element is read through ${}^{*}$; it is linear in the coordinates of the first element and conjugate-linear in those of the second. The general quaternionic sesquilinear product multiplies $P^{\natural}_\mu$ and $Q^{*}_\nu$, both elements being read through their conjugations, and is linear in the first set of coordinates and conjugate-linear in the second.

The four scalar parts are the four displayed in the table, and the four vector parts beside them are the four displayed beside them. The identities that link the four general products, and the relations among the four scalar parts and the four vector parts, are *Relations Between the Four General Products*. Which of the four general products is a multiplication in the sense of algebra is *Comparison Between the Four General Products*. The split of each of the four general products into a symmetric and an antisymmetric part, and the Jordan and the Lie structure that the two parts of the general plain bilinear product carry, are *The 12 Products of the Biquaternion Complex Space*, which takes the four general products from here.

Two exchanges act on the four general products. The **exchange by a conjugation** $c$, $\tilde{P}\tilde{Q}^{*}\mapsto c(\tilde{Q}\tilde{P}^{*})$, composes the swap with $c$ and is the one that keeps the class of the two sesquilinear products, whose parts under it are sesquilinear again, and it is the exchange the twelve names are read against; the **plain exchange**, which swaps the two elements of the pair, does not keep the class, a part of a sesquilinear product taken under it being only $\mathbb{R}$-bilinear. For the plain sesquilinear product and $c=\overline{\cdot}$ the two adapted parts are its scalar part and its vector part, displayed in the table above as the two halves of the third row; for the general quaternionic sesquilinear product they are the symmetrisation of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$ and half their commutator. Both exchanges and their two splits are read in *The 12 Products of the Biquaternion Complex Space*, §*The Other Exchange, and the Class It Keeps*, and the general construction is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*. The behaviour of the general plain bilinear product on each of the six distinguished subspaces is tabulated in *The Six Subspaces and the Four General Products*; the operators of left and right multiplication are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*; and the basis products written out one by one are in *Introduction to the General Plain Algebra of Biquaternions*, §*The Multiplication Table*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\tilde Q$ | the general plain bilinear product |
| $\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| $\tilde P\tilde Q^{*}$ | the general plain sesquilinear product |
| $\tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product |
| $\tilde P=P_0e_0+\dots+P_3e_3$ | the element and its four complex coordinates |
| $\tilde P^{\natural}$, $\tilde P^{*}$ | the two conjugations, in coordinates |
| $\mathbf P$ | the vector part $P_1e_1+P_2e_2+P_3e_3$ |
| $(\mathbf P,\mathbf Q)$ | the complex bilinear dot product, $\sum_kP_kQ_k$ |
| $\mathbf P\times\mathbf Q$ | the complex bilinear cross product |
| $\overline{\mathbf Q}$ | the coefficientwise conjugate of the vector part |
| $\varepsilon$ | the sign vector $(1,-1,-1,-1)$ |
| $\mathrm{Sc}$, $\mathrm{Vec}$ | the scalar part and the vector part of an element |

## Further Reading

- *The Four General Products and Operators* (`articles_maths/the-four-general-products-and-operators.md`), for what the four rules decide (the four pairings and their adjoints) and what they do not decide (an operator), read on one element through the four insertions
- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original product of the units whose coordinate rule the general plain bilinear product extends.
- *Relations Between the Four General Products* (`articles_maths/relations-between-the-four-general-products.md`), for the identities that link the four.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table of the four.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the symmetric and the antisymmetric part of each of the four general products.
