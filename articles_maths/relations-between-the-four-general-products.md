# __Relations Between the Four General Products__

## Introduction

The four general products of the underlying $\mathbb{C}$-vector space of $\mathbb{B}$ are defined independently in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, each on the coordinates of the two elements of a pair, and each with its scalar–vector form:

$$
\tilde P\tilde Q , \qquad \tilde P^{\natural}\tilde Q , \qquad \tilde P\tilde Q^{*} , \qquad \tilde P^{\natural}\tilde Q^{*} .
$$

This article collects the identities that link the four. They are not four unrelated rules: the first factor is read plain in the first two and through ${}^{\natural}$ in the last two, the second factor plain in the first and the third and through ${}^{*}$ in the second and the fourth, the two choices being made independently. Every link below is a consequence of that single distinction, read on the coordinates: the four scalar parts are related to one another by the two identities that split a factor into its scalar and its vector part; the four vector parts obey the same pair of identities; the left multiplications of the four are the general plain bilinear ones read through the two conjugations, and that reading decides which of them form a monoid. Finally, on the real quaternion subspace, where the complex conjugation is the identity and the star is the natural sign, the four scalar parts collapse onto two, the two sesquilinear ones becoming the two bilinear ones.

Which of the four general products is a multiplication in the sense of algebra is *Comparison Between the Four General Products*, and the properties of each are tabulated there. The behaviour of the general plain bilinear product on the six distinguished subspaces is *The Six Subspaces and the Four General Products*, and its split into a symmetric and an antisymmetric half is *The 12 Products of the Biquaternion Complex Space*.

The article assumes the four general products and their scalar–vector forms from *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and the conjugations from *Biquaternions as a Vector Space over $\mathbb{C}$* and *The Group of Involutions*. Throughout, $\tilde P=P_0+\mathbf P$ and $\tilde Q=Q_0+\mathbf Q$ separate the complex scalar part from the complex vector part, $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ and $\mathbf P\times\mathbf Q$ are the complex bilinear dot and cross products, and $\overline{\mathbf Q}$ is the coefficientwise conjugate of the vector part.

## The Two Choices, and the Four General Products

Write ${}^{\natural}$, ${}^{*}$ for the two conjugations. The four rules are read on one and the same pair $(\tilde P,\tilde Q)$, and the three after the first are obtained from the general plain bilinear product $\tilde P\tilde Q$ by replacing the first element, the second element, or both, by its conjugate:

$$
\tilde P\tilde Q , \qquad
\tilde P^{\natural}\tilde Q , \qquad
\tilde P\tilde Q^{*} , \qquad
\tilde P^{\natural}\tilde Q^{*} .
$$

Conjugating the first element of the pair and conjugating the second are two involutions of the pair, and they commute, ${}^{\natural}$ and ${}^{*}$ being involutions of the element that commute with each other. The two choices made independently are exactly what produces four rules, and the four are pairwise distinct: no two of the four agree on every pair of elements.

**The two remaining conjugations add nothing new here.** The complex conjugation $\bar{\cdot}$ is an automorphism of the algebra, and the anti-Hermitian conjugation is $-\,{}^{*}$, so neither is one of the two conjugations carried by the four rules. A scalar part read with the complex conjugation in one slot is one of the four scalar parts with the slots exchanged,

$$
\mathrm{Sc}\bigl(\bar{\tilde P}\tilde Q\bigr)=\mathrm{Sc}\bigl(\tilde Q^{\natural}\tilde P^{*}\bigr) , \qquad
\mathrm{Sc}\bigl(\tilde P\bar{\tilde Q}\bigr)=\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde Q^{*}\bigr) ,
$$

and the conjugation $\flat=-\,{}^{*}$ multiplies the corresponding scalar part by $-1$. The four general products therefore carry the four scalar parts between them, and the two conjugations left out of the list add no new one.

## How Each Factor Enters

The ${}^{\natural}$ in the first slot and the ${}^{*}$ in the second are what distinguish the four from one another, and the two conjugations act on the two factors in the same way: each reverses the sign of the vector part and leaves the scalar part alone, the star conjugating the coefficients on the way. The splitting identities of this section are read on each of the four.

Separating the scalar part of the first factor from its vector part, the general plain bilinear product and the ${}^{\natural}$-product are

$$
\tilde P\tilde Q=(P_0e_0)\tilde Q+\mathbf P\tilde Q , \qquad
\tilde P^{\natural}\tilde Q=(P_0e_0)\tilde Q-\mathbf P\tilde Q ,
$$

the vector part being read as an element where it multiplies. Adding and subtracting,

$$
\tilde P\tilde Q+\tilde P^{\natural}\tilde Q=2P_0\tilde Q , \qquad
\tilde P\tilde Q-\tilde P^{\natural}\tilde Q=2\,\mathbf P\tilde Q .
$$

The same separation applied to the two sesquilinear products gives

$$
\tilde P\tilde Q^{*}+\tilde P^{\natural}\tilde Q^{*}=2P_0\tilde Q^{*} , \qquad
\tilde P\tilde Q^{*}-\tilde P^{\natural}\tilde Q^{*}=2\,\mathbf P\tilde Q^{*} .
$$

So the ${}^{\natural}$ in the first slot separates the scalar part of the first factor from its vector part, and the four general products are the two pairs of that separation: the general plain bilinear product and the ${}^{\natural}$-product are separated by the vector part of $\tilde P$, the two sesquilinear ones by the same vector part after the second factor has been conjugated. The two pairs differ from one another by the ${}^{*}$ in the second slot.

One reading follows. The ${}^{\natural}$-product agrees with the general plain bilinear product in its first argument exactly when the vector part of that argument annihilates the second factor,

$$
\tilde P^{\natural}\tilde Q=\tilde P\tilde Q \quad\Longleftrightarrow\quad \mathbf P\tilde Q=0 ,
$$

which holds in particular for every central $\tilde P$, the vector part being zero; no two of the four general products agree on every pair, since the vector part of a general element is different from zero.

## The Conjugate of a Product

Conjugating a product conjugates the factors and reverses their order, by the two anti-automorphism rules $(\tilde X\tilde Y)^{\natural}=\tilde Y^{\natural}\tilde X^{\natural}$ and $(\tilde X\tilde Y)^{*}=\tilde Y^{*}\tilde X^{*}$. Applied to the four general products,

$$
(\tilde P\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural} , \qquad
(\tilde P^{\natural}\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P , \qquad
(\tilde P\tilde Q^{*})^{\natural}=\bar{\tilde Q}\tilde P^{\natural} , \qquad
(\tilde P^{\natural}\tilde Q^{*})^{\natural}=\bar{\tilde Q}\tilde P ,
$$

$$
(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*} , \qquad
(\tilde P^{\natural}\tilde Q)^{*}=\tilde Q^{*}\bar{\tilde P} , \qquad
(\tilde P\tilde Q^{*})^{*}=\tilde Q\tilde P^{*} , \qquad
(\tilde P^{\natural}\tilde Q^{*})^{*}=\tilde Q\bar{\tilde P} .
$$

Two of the eight identities exchange the two slots between two of the products, and they are the ones worth keeping. The ${}^{\natural}$ of the ${}^{\natural}$-product, and the ${}^{*}$ of the ${}^{*}$-product, return the same product with the two slots exchanged:

$$
(\tilde P^{\natural}\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P , \qquad
(\tilde P\tilde Q^{*})^{*}=\tilde Q\tilde P^{*} .
$$

That is exactly the symmetry the corresponding scalar parts have, and it explains them: conjugating the first identity and taking the scalar part gives $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\mathrm{Sc}(\tilde Q^{\natural}\tilde P)$, and conjugating the second gives $\mathrm{Sc}(\tilde P\tilde Q^{*})=\overline{\mathrm{Sc}(\tilde Q\tilde P^{*})}$. The scalar part of the ${}^{\natural}$-product is symmetric and the scalar part of the ${}^{*}$-product is conjugate-symmetric, and in each case the reason is the identity above.

## The Four Scalar Parts

The scalar part of each of the four general products is read on the coordinates in one of four ways,

| product | scalar part | signs and conjugation |
|---|---|---|
| $\tilde P\tilde Q$ | $\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the signs $\varepsilon_\mu$ in both factors |
| $\tilde P^{\natural}\tilde Q$ | $\sum_\mu P_\mu Q_\mu$ | no sign at all |
| $\tilde P\tilde Q^{*}$ | $\sum_\mu P_\mu\overline{Q_\mu}$ | the conjugate in the second factor |
| $\tilde P^{\natural}\tilde Q^{*}$ | $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the signs in the first factor and the conjugate in the second |

with $\varepsilon=(1,-1,-1,-1)$; the first two are linear in the coordinates of both factors and the last two are conjugate-linear in the coordinates of the second. The four are related two by two, the first pair by the bilinear dot product and the second by its Hermitian companion:

$$
\mathrm{Sc}(\tilde P\tilde Q)+\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=2P_0Q_0 , \qquad
\mathrm{Sc}(\tilde P\tilde Q)-\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=-2(\mathbf P,\mathbf Q) ,
$$

$$
\mathrm{Sc}(\tilde P\tilde Q^{*})+\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=2P_0\overline{Q_0} , \qquad
\mathrm{Sc}(\tilde P\tilde Q^{*})-\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=2(\mathbf P,\overline{\mathbf Q}) .
$$

The sums separate the scalar parts of the two factors, the differences the vector part of the first factor against the second: the two scalar parts of a pair are the same reading with the sign of the vector part of the first factor flipped, and their mean and their half-difference are the two extreme readings.

Three identities move a scalar part from one writing to another. The natural sign may be carried from one factor to the other,

$$
\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{\natural}) ,
$$

and the same holds with the star, $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\mathrm{Sc}(\tilde P\bar{\tilde Q})$, while the scalar part is unchanged when both factors are conjugated by the natural sign,

$$
\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{\natural})=\mathrm{Sc}(\tilde P\tilde Q) .
$$

The symmetry in the two slots follows from the conjugates of the previous section and is stated here with the four scalar parts: the two bilinear scalar parts are symmetric,

$$
\mathrm{Sc}(\tilde P\tilde Q)=\mathrm{Sc}(\tilde Q\tilde P) , \qquad
\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\mathrm{Sc}(\tilde Q^{\natural}\tilde P) ,
$$

and the two sesquilinear ones are conjugate-symmetric,

$$
\mathrm{Sc}(\tilde P\tilde Q^{*})=\overline{\mathrm{Sc}(\tilde Q\tilde P^{*})} , \qquad
\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\overline{\mathrm{Sc}(\tilde Q^{\natural}\tilde P^{*})} .
$$

The two sesquilinear identities are the conjugate-symmetry of the last two scalar parts; that symmetry is a property of the scalar part and not of the product, since none of the four general products is commutative.

## The Four Vector Parts

The vector parts obey the same two splitting identities as the scalar parts. The splitting holds first at the level of the elements,

$$
\tilde P^{\natural}\tilde Q=2P_0\tilde Q-\tilde P\tilde Q , \qquad
\tilde P^{\natural}\tilde Q^{*}=2P_0\tilde Q^{*}-\tilde P\tilde Q^{*} ,
$$

and reading the vector part of each side gives

$$
\mathrm{Vec}(\tilde P^{\natural}\tilde Q)=2P_0\mathbf Q-\mathrm{Vec}(\tilde P\tilde Q) , \qquad
\mathrm{Vec}(\tilde P^{\natural}\tilde Q^{*})=-2P_0\overline{\mathbf Q}-\mathrm{Vec}(\tilde P\tilde Q^{*}) .
$$

The first says that the vector part of the ${}^{\natural}$-product is the reflection of the vector part of the general plain bilinear product in $P_0\mathbf Q$; the second, that the vector part of the sesquilinear pair reflects in $-P_0\overline{\mathbf Q}$. In full, the four vector parts of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are two mixed terms and a cross term in each case, and the two signs — the sign of the cross term and the sign of the vector part of the first factor — are what tell the four apart:

| product | vector part | cross term |
|---|---|---|
| $\tilde P\tilde Q$ | $P_0\mathbf Q+Q_0\mathbf P+\mathbf P\times\mathbf Q$ | $+$ |
| $\tilde P^{\natural}\tilde Q$ | $P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | $-$ |
| $\tilde P\tilde Q^{*}$ | $-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q}$ | $-$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P+\mathbf P\times\overline{\mathbf Q}$ | $+$ |

Deleting the cross term, the first and the second rows are reflections of each other in $P_0\mathbf Q$, and the third and the fourth in $-P_0\overline{\mathbf Q}$; the cross term then distinguishes within each pair, and the ${}^{*}$ in the second slot conjugates the coordinates of $\mathbf Q$, reverses the sign of the $P_0$-term and of the cross term, and leaves the sign of the $Q_0$-term alone.

## The Left Multiplications

The left multiplications of the four general products are the general plain bilinear ones read through the two conjugations. Writing $L_{\tilde P}$ and $R_{\tilde P}$ for the left and right multiplications of the general plain bilinear product, $\tilde X\mapsto\tilde P\tilde X$ and $\tilde X\mapsto\tilde X\tilde P$,

$$
\tilde P^{\natural}\tilde X=L_{\tilde P^{\natural}}(\tilde X) , \qquad
\tilde P\tilde X^{*}=\bigl(R_{\tilde P^{*}}(\tilde X)\bigr)^{*} , \qquad
\tilde P^{\natural}\tilde X^{*}=\bigl(R_{\bar{\tilde P}}(\tilde X)\bigr)^{*} .
$$

The first is the left multiplication of the general plain bilinear product re-indexed by the natural sign; the other two are the conjugates of the right multiplications of the general plain bilinear product by the star and by the conjugate of the first factor. The distinction decides which of the four general products have a monoid of left multiplications, and it is worth recording, although the property table itself is *Comparison Between the Four General Products*.

For the general plain bilinear product the left multiplications compose by $L_{\tilde P}\circ L_{\tilde R}=L_{\tilde P\tilde R}$, the associativity of the product, so they form a monoid, the image of $\mathbb{B}$ in its endomorphism ring. For the ${}^{\natural}$-product,

$$
L^{\natural}_{\tilde P}\circ L^{\natural}_{\tilde R}
=L_{\tilde P^{\natural}}\circ L_{\tilde R^{\natural}}
=L_{\tilde P^{\natural}\tilde R^{\natural}}
=L^{\natural}_{\tilde R\tilde P} ,
$$

since $\tilde P^{\natural}\tilde R^{\natural}=(\tilde R\tilde P)^{\natural}$; the left multiplications are again closed under composition, in reversed order, and they form a monoid isomorphic to the opposite of the multiplicative monoid of $\mathbb{B}$.

For the two sesquilinear products the composition leaves the class. For the ${}^{*}$-product,

$$
L^{*}_{\tilde P}\circ L^{*}_{\tilde R}(\tilde X)
=\tilde P\bigl(\tilde R\tilde X^{*}\bigr)^{*}
=\tilde P\tilde X\tilde R^{*} ,
$$

which is $\mathbb{C}$-linear in $\tilde X$; every left multiplication of the ${}^{*}$-product is conjugate-linear, so the composition is not one of them, and the left multiplications of the ${}^{*}$-product do not form a monoid. The same computation with $\overline{\tilde P}$ in place of $\tilde P$ settles the fourth operation, whose left multiplications are the conjugates of the right multiplications of the general plain bilinear product: the composition of two of them is linear and the class is not closed.

## The Restriction to the Quaternion Subspace

On the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the elements whose coefficients are real, the complex conjugation is the identity, so the star coincides with the natural sign: the two sesquilinear rules then read as the natural conjugates of the two bilinear ones with the slots exchanged, and the two conjugate-linear scalar parts become linear.

For $\bar{\tilde P}=\tilde P$ and $\bar{\tilde Q}=\tilde Q$, the two sesquilinear products coincide with the natural twists of the two bilinear ones,

$$
\tilde P\tilde Q^{*}=\tilde P\tilde Q^{\natural} , \qquad
\tilde P^{\natural}\tilde Q^{*}=\tilde P^{\natural}\tilde Q^{\natural}=(\tilde Q\tilde P)^{\natural} ,
$$

so the four general products take the four values $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{\natural}$ and $(\tilde Q\tilde P)^{\natural}$, of which the last two are the natural conjugates of the two products in the reversed order. The scalar parts follow: the third scalar part restricts to the second,

$$
\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu Q_\mu=\mathrm{Sc}(\tilde P^{\natural}\tilde Q) \qquad (\bar{\tilde P}=\tilde P,\ \bar{\tilde Q}=\tilde Q),
$$

and the fourth restricts to the first. The four scalar parts therefore come in two linear and two conjugate-linear pairs off the subspace and in two linear pairs on it: on the subspace the coefficients are fixed by the complex conjugation, so the star is the natural sign and only the signs $\varepsilon_\mu$ remain.

## Summary

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are read on one and the same pair $(\tilde P,\tilde Q)$, each with either element replaced by its conjugate, the two choices being independent, and they are pairwise distinct. The two remaining conjugations of the algebra add no new scalar part: $\mathrm{Sc}(\bar{\tilde P}\tilde Q)=\mathrm{Sc}(\tilde Q^{\natural}\tilde P^{*})$ and $\mathrm{Sc}(\tilde P\bar{\tilde Q})=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$.

The two conjugations in the slots separate the scalar part of a factor from its vector part,

$$
\tilde P\tilde Q\pm\tilde P^{\natural}\tilde Q=2P_0\tilde Q \ \text{and}\ 2\mathbf P\tilde Q , \qquad
\tilde P\tilde Q^{*}\pm\tilde P^{\natural}\tilde Q^{*}=2P_0\tilde Q^{*} \ \text{and}\ 2\mathbf P\tilde Q^{*} ,
$$

and the same identities hold for the vector parts. The ${}^{\natural}$ of the ${}^{\natural}$-product and the ${}^{*}$ of the ${}^{*}$-product return the same product with the slots exchanged, which is why the scalar parts of those two are symmetric and conjugate-symmetric respectively, while no one of the four general products is commutative.

The four scalar parts are related pairwise by the two splitting identities above; their sums and half-differences separate the scalar parts of the two factors from the vector part of the first. On the real quaternion subspace the complex conjugation is the identity, the star is the natural sign, and the four scalar parts collapse onto two pairs.

The left multiplications of the four are the general plain bilinear ones read through the conjugations: $L^{\natural}_{\tilde P}=L_{\tilde P^{\natural}}$, $L^{*}_{\tilde P}=(\cdot)^{*}\circ R_{\tilde P^{*}}$ and $L^{\natural*}_{\tilde P}=(\cdot)^{*}\circ R_{\bar{\tilde P}}$, so the general plain bilinear and the ${}^{\natural}$-product have a monoid of left multiplications and the two sesquilinear ones do not. Which of the four general products is a multiplication in the sense of algebra is *Comparison Between the Four General Products*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\tilde Q, \tilde P^{\natural}\tilde Q, \tilde P\tilde Q^{*}, \tilde P^{\natural}\tilde Q^{*}$ | the four general products, defined in *The Four General Products of the Biquaternion $\mathbb{C}$ Space* |
| $\mathbf P$ | the vector part of $\tilde P$, $P_1e_1+P_2e_2+P_3e_3$, read as an element where it multiplies |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector, the signs of the first and of the fourth scalar parts |
| $L_{\tilde P}$, $R_{\tilde P}$ | the left and right multiplications of the general plain bilinear product by $\tilde P$ |
| $L^{\natural}_{\tilde P}$, $L^{*}_{\tilde P}$, $L^{\natural*}_{\tilde P}$ | the left multiplications of the three other products |
| $\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace, the elements with real coefficients |

## Further Reading

- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four definitions and their scalar–vector forms.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table of the four.
- *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for the left and right multiplications as operators.
