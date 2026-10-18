# __Remarkable Subspaces under the Antisymmetric Plain Sesqualgebra__

## Introduction

The space $\mathbb{B}$ carries remarkable real subspaces, $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$, defined and tabulated in *Introduction to the Remarkable Subspaces* and read by each of the four general products in the articles of the pattern *Remarkable Subspaces and the Four Forms* and *Remarkable Subspaces under the General Plain Sesqualgebra*. This article repeats the reading for the antisymmetric plain sesqualgebra and its operation

$$
\tilde Q_1\diamond\tilde Q_2=\mathrm{Vect}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2} ,
$$

one section to a subspace, and closes on the table of the remarkable subspaces. Two structural facts make this reading different from the readings of a product. The first is that the block is **pure vector**: every value lies in $\mathrm{Vect}(\mathbb{B})$, so the image is one of the remarkable subspaces and no value ever lies in the centre, and the reading of every subspace is a reading into $\mathrm{Vect}(\mathbb{B})$. The second is that the block is **conjugate-alternating**, not alternating, so the diagonal is not zero on every subspace and the notion of a square-zero element is a genuine one on three of the remarkable subspaces.

The subspace that carries the sharpest information is the **real span** of $e_t,\vec e_x,\vec e_y,\vec e_z$: on it the coefficientwise conjugation acts trivially, the block is $\tilde Q_1\diamond\tilde Q_2=-Q_{1t}\vec Q_2+Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$, its diagonal vanishes, and it is at the same time the reading of a cross product on the real vectors and, off them, the reading of $\mathrm{AQA}$ with the sign of the mixed term reversed. The two quaternion subspaces are the two halves of the real span, and the block reads them very differently: it is closed on the real span and not on the imaginary one. The Hermitian and anti-Hermitian subspaces are the two halves cut by the involution, and the block reads them by the form $H$ that the involution polarises; they are the only two subspaces on which the diagonal is a non-zero scalar multiple of the element's own vector part, $2iQ_{2t}\vec q$ on $\mathbb{M}_+$ and $-2iq_t\vec q$ on $\mathbb{M}_-$ — on the other four it either vanishes identically or is the cross product $-\vec Q_2\times\overline{\vec Q_2}$ — and the element $\vec e_x+i\vec e_y$ of the introduction lies in neither.

The setting is that of *Introduction to the Antisymmetric Plain Sesqualgebra*; the general split is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the subspaces and their bases are *Introduction to the Remarkable Subspaces* and *Decompositions Along the Remarkable Subspaces*; the form that the two halves cut is $H$ of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; the quaternion form $N$ and its comparison with $H$ are *Comparison Between the Four General Products*; the pattern of the reading is *Remarkable Subspaces under the General Plain Sesqualgebra*; and the action of the operation on pairs of subspaces is followed, in its form reading, in *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, above in this block.

**Conventions.** The remarkable subspaces and their real bases are

$$
\begin{aligned}
\mathbb{C}_{\mathbb{B}}&=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}, & \mathrm{Vect}(\mathbb{B})&=\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z,i\vec e_x,i\vec e_y,i\vec e_z\},\\
\mathbb{H}_{\mathbb{B}}&=\mathrm{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}, & i\mathbb{H}_{\mathbb{B}}&=\mathrm{span}_{\mathbb{R}}\{ie_t,i\vec e_x,i\vec e_y,i\vec e_z\},\\
\mathbb{M}_+&=\mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}, & \mathbb{M}_-&=\mathrm{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\},
\end{aligned}
$$

with $\mathbb{M}_+$ the Hermitian and $\mathbb{M}_-$ the anti-Hermitian half, the fixed and the anti-fixed sets of the involution. A vector part is written $\vec Q$ and its coefficientwise conjugate $\overline{\vec Q}$.

## The Centre

**Proposition (the action of the centre).** For a central element $\lambda e_t$ and any biquaternion,

$$
(\lambda e_t)\diamond\tilde Q_3=-\lambda\,\overline{\vec Q_3},\qquad
\tilde Q_3\diamond(\lambda e_t)=\overline{\lambda}\,\vec Q_3.
$$

*Proof.* The first is $\lambda\,(e_t\diamond\tilde Q_3)=\lambda\,\mathrm{Vect}(\tilde Q_3^{*})=-\lambda\overline{\vec Q_3}$; the second is $\tilde Q_3\diamond(\lambda e_t)=\mathrm{Vect}(\tilde Q_3(\lambda e_t)^{*})=\mathrm{Vect}(\overline{\lambda}\tilde Q_3)=\overline{\lambda}\vec Q_3$.

**Remark (the centre is not annihilating).** The two displays show that the centre is **not** in the kernel of the operation on either side: a nonzero central element sends every element with nonzero vector part to a nonzero vector part. What is true is the converse direction: the operation annihilates no value in the centre, and the **kernel of the left operator of the unit is the centre**,

$$
e_t\diamond\tilde Q_3=0\iff \overline{\vec Q_3}=0\iff \tilde Q_3\in\mathbb{C}_{\mathbb{B}},
$$

so the centre is the kernel of the operator $L^{\diamond}_{e_t}$ and not of the operation. The phrase of the scope of this article, *the vanishing on the centre*, is read here in that sense: the diagonal vanishes on the whole centre, no value lies in the centre, and the centre is the kernel of the operator of the unit; the centre is not dead in the arguments.

**Corollary (the diagonal on the centre).** At a central element, $(\lambda e_t)\diamond(\lambda e_t)=0$: the diagonal vanishes on the whole centre. The centre is therefore one of the subspaces on which the block looks alternating, and the value zero is reached there.

## The Vector Subspace

**Proposition (closure and the cross product).** For $\tilde Q_1=\vec Q_1$ and $\tilde Q_2=\vec Q_2$ pure vectors,

$$
\vec Q_1\diamond\vec Q_2=-\vec Q_1\times\overline{\vec Q_2},
$$

so the vector subspace is closed under the block, and its reading is the complex cross product of the first vector part with the conjugate of the second.

*Proof.* At $Q_{1t}=Q_{2t}=0$ the coordinate rule keeps the third term alone.

**Corollary (the diagonal and the square-zero elements).** The diagonal on the vector subspace is

$$
\vec Q\diamond\vec Q=-\vec Q\times\overline{\vec Q},
$$

which does not vanish in general: at $\vec Q=\vec e_x+i\vec e_y$ it is $2i\vec e_z$. It vanishes exactly when the two vectors are proportional over $\mathbb{C}$, $\vec Q\times\overline{\vec Q}=0$. In particular the **real** vectors and the **purely imaginary** vectors both have square zero, since there $\overline{\vec Q}=\pm\vec Q$ and the cross product of a vector with itself vanishes.

**Remark (the image).** The vector subspace is the image of the block, by *Introduction to the Antisymmetric Plain Sesqualgebra*, so the reading of every other subspace is a reading into the vector subspace. On the vector subspace itself the block is surjective: the left multiplication of the unit sends $\tilde Q_3$ to $-\overline{\vec Q_3}$, and the coefficientwise conjugation is a bijection of the vector subspace, so every $\vec Q_3$ is a value $e_t\diamond\tilde Q_3$.

## The Quaternion Subspace

**Proposition (closure and the bracket form).** Let $\tilde Q_1,\tilde Q_2$ have real coefficients, so that they lie in $\mathbb{H}_{\mathbb{B}}$. Then

$$
\tilde Q_1\diamond\tilde Q_2=-Q_{1t}\vec Q_2+Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2,
$$

whose coefficients are real: the value lies in the real vector triple $\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, and therefore in $\mathbb{H}_{\mathbb{B}}$. The quaternion subspace is closed under the block.

*Proof.* At real coefficients the coefficientwise conjugation is the identity, so the coordinate rule becomes the display; the three terms have real coefficients and no scalar part.

**Corollary (the diagonal vanishes on the whole subspace).** At a real element,

$$
\tilde Q\diamond\tilde Q=-Q_t\vec Q+Q_t\vec Q-\vec Q\times\vec Q=0 ,
$$

so the quaternion subspace is **wholly** contained in the set of the elements of square zero, and the block is alternating there. This is the same vanishing as on the real vectors of the preceding section, extended by the mixing of the scalar and vector parts, which cancels exactly.

**Remark (the bracket of the real part).** The display is the real reading of the block and it is the operation that the table of *The 12 Products of the Biquaternioid Complex Space* records, on the real part, as the block distinct from all others: it is $\mathrm{AQA}$ with the sign of the mixed term reversed, and it coincides with the cross product only on the real vectors. The ten operations of the real part, with the two coincidences $\mathrm{APA}=\mathrm{AQS}$ and $\mathrm{SQA}=\mathrm{SPS}$ that reduce the twelve to ten there, are tabulated in that article; the block is not one of the two coincidences.

## The Anti-Quaternion Subspace

**Proposition (the values leave the subspace).** Let $\tilde Q_1,\tilde Q_2$ have purely imaginary coefficients, so that they lie in $i\mathbb{H}_{\mathbb{B}}$. Write $Q_{1t}=ip_t$, $\vec Q_1=i\vec p$, $Q_{2t}=iq_t$, $\vec Q_2=i\vec q$ with $p_t,q_t$ real and $\vec p,\vec q$ real vectors. Then

$$
\tilde Q_1\diamond\tilde Q_2=-p_t\vec q+q_t\vec p-\vec p\times\vec q,
$$

a **real** vector: the value lies in the real vector triple of $\mathbb{H}_{\mathbb{B}}$ and not in $i\mathbb{H}_{\mathbb{B}}$. The anti-quaternion subspace is therefore **not closed** under the block.

*Proof.* Substitute the imaginary coordinates in the coordinate rule; $\overline{\vec Q_2}=-i\vec q$ and $\overline{Q_{2t}}=-iq_t$, the products of the two imaginary units being real, and the cross product of two real vectors being real.

**Corollary (the diagonal vanishes there too).** At a purely imaginary element the display with $\tilde Q_1=\tilde Q_2$ gives $p_t=q_t=p$, $\vec p=\vec q$, hence $-p_t\vec p+p_t\vec p-\vec p\times\vec p=0$. So the anti-quaternion subspace, like the quaternion one, is wholly contained in the set of the elements of square zero, and it is the second cell of the quadric cone of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*. The closure fails while the vanishing holds; the two facts are the two halves of the same conjugation.

## The Hermitian Subspace

**Proposition (the values leave both halves).** Let $\tilde Q_1,\tilde Q_2\in\mathbb{M}_+$, so that $Q_{1t},Q_{2t}$ are real and $\vec Q_1=i\vec p$, $\vec Q_2=i\vec q$ with $\vec p,\vec q$ real. Then

$$
\tilde Q_1\diamond\tilde Q_2=i\bigl(Q_{1t}\,\vec q+Q_{2t}\,\vec p\bigr)-\vec p\times\vec q,
$$

whose real part is the cross term and whose imaginary part is the mixed term. The value is neither Hermitian nor anti-Hermitian in general, so $\mathbb{M}_+$ is **not closed** under the block and its image meets neither half in general; the image is contained in $\mathrm{Vect}(\mathbb{B})$.

*Proof.* Substitute in the coordinate rule: $\vec Q_1=i\vec p$ and $\overline{\vec Q_2}=-i\vec q$ give $Q_{1t}i\vec q$, $\overline{Q_{2t}}=Q_{2t}$ real gives $Q_{2t}i\vec p$, and $(i\vec p)\times(-i\vec q)=\vec p\times\vec q$, with the sign of the coordinate rule. The scalar part of the value is zero, so the value is a vector part; it is Hermitian only when its real part vanishes, and anti-Hermitian only when its imaginary part vanishes, and neither holds in general.

**Corollary (the diagonal on the Hermitian subspace).** At a Hermitian element,

$$
\tilde Q\diamond\tilde Q=2i\,Q_t\,\vec q,
$$

with $Q_t$ real and $\vec q$ real. The diagonal vanishes exactly on the Hermitian elements with $Q_t=0$, that is the purely imaginary vectors, and on the central real elements $\vec q=0$. So the Hermitian subspace contributes to the quadric cone its purely imaginary vectors and its real centre, and not the mixed elements $e_t+i\vec e_x$, on which the diagonal is $2i\vec e_x$.

## The Anti-Hermitian Subspace

**Proposition (the values leave both halves).** Let $\tilde Q_1,\tilde Q_2\in\mathbb{M}_-$, so that $Q_{1t}=ip_t$, $Q_{2t}=iq_t$ are purely imaginary and $\vec Q_1=\vec p$, $\vec Q_2=\vec q$ are real. Then

$$
\tilde Q_1\diamond\tilde Q_2=-i\bigl(p_t\,\vec q+q_t\,\vec p\bigr)-\vec p\times\vec q,
$$

whose real part is the cross term and whose imaginary part is the mixed term, with the opposite assignment to the Hermitian case. The value is neither anti-Hermitian nor Hermitian in general, so $\mathbb{M}_-$ is **not closed** under the block either.

*Proof.* Substitute $Q_{1t}=ip_t$, $\overline{\vec Q_2}=\vec q$, $\overline{Q_{2t}}=-iq_t$ in the coordinate rule.

**Corollary (the diagonal on the anti-Hermitian subspace).** At an anti-Hermitian element,

$$
\tilde Q\diamond\tilde Q=-2i\,q_t\,\vec q,
$$

so the diagonal vanishes exactly on the real vectors of the subspace and on its imaginary centre. The two halves of the involution therefore fail closure in the same way and differ only by a sign in the diagonal, $2iQ_t\vec q$ against $-2iq_t\vec q$; the form $H$ is Hermitian on each, $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\overline{\langle\tilde Q_2,\tilde Q\rangle_{*}}$, and the pairing of the block is read on the two halves in *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*.

## The Table of the Remarkable Subspaces

| subspace | the reading of the block | closure | the diagonal | square-zero elements |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $(\lambda e_t)\diamond\tilde Q_3=-\lambda\overline{\vec Q_3}$, $\tilde Q_3\diamond(\lambda e_t)=\overline{\lambda}\vec Q_3$ | closed, the value of two central elements being $0$ | $(\lambda e_t)\diamond(\lambda e_t)=0$ | the whole centre |
| $\mathrm{Vect}(\mathbb{B})$ | $\vec Q_1\diamond\vec Q_2=-\vec Q_1\times\overline{\vec Q_2}$ | closed, and surjective | $-\vec Q\times\overline{\vec Q}$, $2i\vec e_z$ at $\vec e_x+i\vec e_y$ | the $\vec Q$ with $\vec Q\times\overline{\vec Q}=0$, in particular the real and the imaginary vectors |
| $\mathbb{H}_{\mathbb{B}}$ | $-Q_{1t}\vec Q_2+Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$, real | closed | $0$ | the whole subspace |
| $i\mathbb{H}_{\mathbb{B}}$ | $-p_t\vec q+q_t\vec p-\vec p\times\vec q$, real | not closed, image the real vector triple | $0$ | the whole subspace |
| $\mathbb{M}_+$ | $i(Q_{1t}\vec q+Q_{2t}\vec p)-\vec p\times\vec q$ | not closed | $2iQ_t\vec q$ | the purely imaginary vectors and the real centre |
| $\mathbb{M}_-$ | $-i(p_t\vec q+q_t\vec p)-\vec p\times\vec q$ | not closed | $-2iq_t\vec q$ | the real vectors and the imaginary centre |

**Remark (the two facts the table exhibits).** First, the block is surjective onto the vector subspace and reads every subspace into it, the centre included: this is the reading of the *pure-vector image* of the introduction. Second, the closure fails on the anti-quaternion subspace and on the two halves of the involution and holds on the centre, the vector subspace and the real span; the pattern is not the pattern of the symmetric half of the same row, where the closure holds exactly on the three subspaces that contain the idempotent $e_t$ — the centre, the quaternion subspace and the Hermitian subspace. The two patterns are the two halves of the product: the central half is closed where its value $\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ can live, and the vector half is closed exactly on the centre, on the vector subspace and on the real span, while on the anti-quaternion subspace and on the Hermitian subspace the vector part is purely imaginary, so its cross product with the conjugate of the other argument is real and leaves the subspace, and on the anti-Hermitian subspace the first term contributes a purely imaginary vector to a subspace whose vectors are real.

**Remark (the comparison with the sibling readings).** The same remarkable subspaces read by the general plain sesquilinear product, by the general plain algebra and by the general quaternionic structures are *Remarkable Subspaces under the General Plain Sesqualgebra*, *Remarkable Subspaces and the Four Forms*, *Remarkable Subspaces under the General Quaternionic Algebra* and *Remarkable Subspaces under the General Quaternionic Sesqualgebra*; the comparison of the readings side by side is *Comparison of the Remarkable Subspaces* and *Remarkable Subspaces and the Four General Products*. This article is the antisymmetric reading of the four, and it is the one whose image is a single one of the remarkable subspaces.

## Summary

On the remarkable subspaces the block is read as follows. It is central-free: no value lies in the centre, and the centre of the *operator* is the kernel of $L^{\diamond}_{e_t}$. Its image is the vector subspace, where it is $-\vec Q_1\times\overline{\vec Q_2}$ and is surjective. It is closed on the centre, on the real span $\mathbb{H}_{\mathbb{B}}$, where it is $-Q_{1t}\vec Q_2+Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ with real values, and on the vector subspace, and it is **not** closed on the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, whose reading is the real vector $-p_t\vec q+q_t\vec p-\vec p\times\vec q$, nor on the Hermitian and anti-Hermitian halves, whose readings are $i(Q_{1t}\vec q+Q_{2t}\vec p)-\vec p\times\vec q$ and $-i(p_t\vec q+q_t\vec p)-\vec p\times\vec q$ and leave both halves. The diagonal vanishes on the centre, on the real span and on the anti-quaternion subspace, and it does not vanish in general on the vector subspace, where it is $-\vec Q_2\times\overline{\vec Q_2}$ and equals $2i\vec e_z$ at $\vec e_x+i\vec e_y$, nor on the two halves of the involution, where it is $2iQ_{2t}\vec q$ on $\mathbb{M}_+$ and $-2iq_t\vec q$ on $\mathbb{M}_-$. The square-zero elements of the remarkable subspaces are the whole centre, the whole real span, the whole anti-quaternion subspace, the $\vec Q_2$ with $\vec Q_2\times\overline{\vec Q_2}=0$ in the vector subspace (in particular its real and its imaginary vectors), and the purely imaginary vectors of $\mathbb{M}_+$ and the real vectors of $\mathbb{M}_-$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable real subspaces |
| $\vec Q,\overline{\vec Q}$ | a vector part and its coefficientwise conjugate |
| $(\lambda e_t)\diamond\tilde Q_3=-\lambda\overline{\vec Q_3}$ | the action of the centre, not annihilating |
| $\vec Q_1\diamond\vec Q_2=-\vec Q_1\times\overline{\vec Q_2}$ | the block on the vector subspace |
| $-Q_{1t}\vec Q_2+Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | the block on the real span, with real values |
| $i(Q_{1t}\vec q+Q_{2t}\vec p)-\vec p\times\vec q$ | the block on $\mathbb{M}_+$, leaving the half |
| $-i(p_t\vec q+q_t\vec p)-\vec p\times\vec q$ | the block on $\mathbb{M}_-$, leaving the half |
| $2iQ_t\vec q$, $-2iq_t\vec q$ | the diagonal on $\mathbb{M}_+$ and on $\mathbb{M}_-$ |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra.md`), for the operation, the basis table and the pure-vector image
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the quadric cone of the square-zero elements, whose cells the two quaternion subspaces are
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the form reading of the same six
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`) and *Decompositions Along the Remarkable Subspaces* (`articles_maths/decompositions-along-the-remarkable-subspaces.md`), for the subspaces and their bases
- *Remarkable Subspaces under the General Plain Sesqualgebra* (`articles_maths/remarkable-subspaces-under-the-general-plain-sesqualgebra.md`), for the pattern of the reading and the indefinite sesquilinear form
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`) and *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the readings side by side
- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the ten operations of the real part and the coincidences there
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the form and the involution that cut the two halves
