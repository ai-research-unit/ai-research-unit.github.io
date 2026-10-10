# __Remarkable Subspaces under the Antisymmetric Plain Sesqualgebra of Biquaternions__

## Introduction

The space $\mathbb{B}$ carries remarkable real subspaces, $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$, defined and tabulated in *Introduction to the Remarkable Subspaces* and read by each of the four general products in the articles of the pattern *Remarkable Subspaces under the General Plain Algebra of Biquaternions* and *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions*. This article repeats the reading for the antisymmetric plain sesqualgebra and its operation

$$
\tilde P\diamond\tilde Q=\mathrm{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}} ,
$$

one section to a subspace, and closes on the table of the remarkable subspaces. Two structural facts make this reading different from the readings of a product. The first is that the block is **pure vector**: every value lies in $\mathrm{Vect}(\mathbb{B})$, so the image is one of the remarkable subspaces and no value ever lies in the centre, and the reading of every subspace is a reading into $\mathrm{Vect}(\mathbb{B})$. The second is that the block is **conjugate-alternating**, not alternating, so the diagonal is not zero on every subspace and the notion of a square-zero element is a genuine one on three of the remarkable subspaces.

The subspace that carries the sharpest information is the **real span** of $e_0,e_1,e_2,e_3$: on it the coefficientwise conjugation acts trivially, the block is $\tilde P\diamond\tilde Q=-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$, its diagonal vanishes, and it is at the same time the reading of a cross product on the real vectors and, off them, the reading of $\mathrm{AQA}$ with the sign of the mixed term reversed. The two quaternion subspaces are the two halves of the real span, and the block reads them very differently: it is closed on the real span and not on the imaginary one. The Hermitian and anti-Hermitian subspaces are the two halves cut by the involution, and the block reads them by the form $H$ that the involution polarises; they are the only two subspaces on which the diagonal is a non-zero scalar multiple of the element's own vector part, $2iQ_0\mathbf{q}$ on $\mathbb{M}_+$ and $-2iq_0\mathbf{q}$ on $\mathbb{M}_-$ — on the other four it either vanishes identically or is the cross product $-\mathbf{Q}\times\overline{\mathbf{Q}}$ — and the element $e_1+ie_2$ of the introduction lies in neither.

The setting is that of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*; the general split is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the subspaces and their bases are *Introduction to the Remarkable Subspaces* and *Decompositions Along the Remarkable Subspaces*; the form that the two halves cut is $H$ of *Biquaternion Norm and Invertibility*; the quaternion form $B$ and its comparison with $H$ are *Comparison Between the Four General Products*; the pattern of the reading is *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions*; and the action of the operation on pairs of subspaces is followed, in its form reading, in *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, above in this block.

**Conventions.** The remarkable subspaces and their real bases are

$$
\begin{aligned}
\mathbb{C}_{\mathbb{B}}&=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}, & \mathrm{Vect}(\mathbb{B})&=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3,ie_1,ie_2,ie_3\},\\
\mathbb{H}_{\mathbb{B}}&=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}, & i\mathbb{H}_{\mathbb{B}}&=\mathrm{span}_{\mathbb{R}}\{ie_0,ie_1,ie_2,ie_3\},\\
\mathbb{M}_+&=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\}, & \mathbb{M}_-&=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\},
\end{aligned}
$$

with $\mathbb{M}_+$ the Hermitian and $\mathbb{M}_-$ the anti-Hermitian half, the fixed and the anti-fixed sets of the involution. A vector part is written $\mathbf{P}$ and its coefficientwise conjugate $\overline{\mathbf{P}}$.

## The Centre

**Proposition (the action of the centre).** For a central element $\lambda e_0$ and any biquaternion,

$$
(\lambda e_0)\diamond\tilde R=-\lambda\,\overline{\mathbf{R}},\qquad
\tilde R\diamond(\lambda e_0)=\overline{\lambda}\,\mathbf{R}.
$$

*Proof.* The first is $\lambda\,(e_0\diamond\tilde R)=\lambda\,\mathrm{Vect}(\tilde R^{*})=-\lambda\overline{\mathbf{R}}$; the second is $\tilde R\diamond(\lambda e_0)=\mathrm{Vect}(\tilde R(\lambda e_0)^{*})=\mathrm{Vect}(\overline{\lambda}\tilde R)=\overline{\lambda}\mathbf{R}$. $\square$

**Remark (the centre is not annihilating).** The two displays show that the centre is **not** in the kernel of the operation on either side: a nonzero central element sends every element with nonzero vector part to a nonzero vector part. What is true is the converse direction: the operation annihilates no value in the centre, and the **kernel of the left operator of the unit is the centre**,

$$
e_0\diamond\tilde R=0\iff \overline{\mathbf{R}}=0\iff \tilde R\in\mathbb{C}_{\mathbb{B}},
$$

so the centre is the kernel of the operator $L^{\diamond}_{e_0}$ and not of the operation. The phrase of the scope of this article, *the vanishing on the centre*, is read here in that sense: the diagonal vanishes on the whole centre, no value lies in the centre, and the centre is the kernel of the operator of the unit; the centre is not dead in the arguments.

**Corollary (the diagonal on the centre).** At a central element, $(\lambda e_0)\diamond(\lambda e_0)=0$: the diagonal vanishes on the whole centre. The centre is therefore one of the subspaces on which the block looks alternating, and the value zero is reached there.

## The Vector Subspace

**Proposition (closure and the cross product).** For $\tilde P=\mathbf{P}$ and $\tilde Q=\mathbf{Q}$ pure vectors,

$$
\mathbf{P}\diamond\mathbf{Q}=-\mathbf{P}\times\overline{\mathbf{Q}},
$$

so the vector subspace is closed under the block, and its reading is the complex cross product of the first vector part with the conjugate of the second.

*Proof.* At $P_0=Q_0=0$ the coordinate rule keeps the third term alone. $\square$

**Corollary (the diagonal and the square-zero elements).** The diagonal on the vector subspace is

$$
\mathbf{Q}\diamond\mathbf{Q}=-\mathbf{Q}\times\overline{\mathbf{Q}},
$$

which does not vanish in general: at $\mathbf{Q}=e_1+ie_2$ it is $2ie_3$. It vanishes exactly when the two vectors are proportional over $\mathbb{C}$, $\mathbf{Q}\times\overline{\mathbf{Q}}=0$. In particular the **real** vectors and the **purely imaginary** vectors both have square zero, since there $\overline{\mathbf{Q}}=\pm\mathbf{Q}$ and the cross product of a vector with itself vanishes.

**Remark (the image).** The vector subspace is the image of the block, by *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*, so the reading of every other subspace is a reading into the vector subspace. On the vector subspace itself the block is surjective: the left multiplication of the unit sends $\tilde R$ to $-\overline{\mathbf{R}}$, and the coefficientwise conjugation is a bijection of the vector subspace, so every $\mathbf{R}$ is a value $e_0\diamond\tilde R$.

## The Quaternion Subspace

**Proposition (closure and the bracket form).** Let $\tilde P,\tilde Q$ have real coefficients, so that they lie in $\mathbb{H}_{\mathbb{B}}$. Then

$$
\tilde P\diamond\tilde Q=-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q},
$$

whose coefficients are real: the value lies in the real vector triple $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$, and therefore in $\mathbb{H}_{\mathbb{B}}$. The quaternion subspace is closed under the block.

*Proof.* At real coefficients the coefficientwise conjugation is the identity, so the coordinate rule becomes the display; the three terms have real coefficients and no scalar part. $\square$

**Corollary (the diagonal vanishes on the whole subspace).** At a real element,

$$
\tilde Q\diamond\tilde Q=-Q_0\mathbf{Q}+Q_0\mathbf{Q}-\mathbf{Q}\times\mathbf{Q}=0 ,
$$

so the quaternion subspace is **wholly** contained in the set of the elements of square zero, and the block is alternating there. This is the same vanishing as on the real vectors of the preceding section, extended by the mixing of the scalar and vector parts, which cancels exactly.

**Remark (the bracket of the real part).** The display is the real reading of the block and it is the operation that the table of *The 12 Products of the Biquaternion Complex Space* records, on the real part, as the block distinct from all others: it is $\mathrm{AQA}$ with the sign of the mixed term reversed, and it coincides with the cross product only on the real vectors. The ten operations of the real part, with the two coincidences $\mathrm{APA}=\mathrm{AQS}$ and $\mathrm{SQA}=\mathrm{SPS}$ that reduce the twelve to ten there, are tabulated in that article; the block is not one of the two coincidences.

## The Anti-Quaternion Subspace

**Proposition (the values leave the subspace).** Let $\tilde P,\tilde Q$ have purely imaginary coefficients, so that they lie in $i\mathbb{H}_{\mathbb{B}}$. Write $P_0=ip_0$, $\mathbf{P}=i\mathbf{p}$, $Q_0=iq_0$, $\mathbf{Q}=i\mathbf{q}$ with $p_0,q_0$ real and $\mathbf{p},\mathbf{q}$ real vectors. Then

$$
\tilde P\diamond\tilde Q=-p_0\mathbf{q}+q_0\mathbf{p}-\mathbf{p}\times\mathbf{q},
$$

a **real** vector: the value lies in the real vector triple of $\mathbb{H}_{\mathbb{B}}$ and not in $i\mathbb{H}_{\mathbb{B}}$. The anti-quaternion subspace is therefore **not closed** under the block.

*Proof.* Substitute the imaginary coordinates in the coordinate rule; $\overline{\mathbf{Q}}=-i\mathbf{q}$ and $\overline{Q_0}=-iq_0$, the products of the two imaginary units being real, and the cross product of two real vectors being real. $\square$

**Corollary (the diagonal vanishes there too).** At a purely imaginary element the display with $\tilde P=\tilde Q$ gives $p_0=q_0=p$, $\mathbf{p}=\mathbf{q}$, hence $-p_0\mathbf{p}+p_0\mathbf{p}-\mathbf{p}\times\mathbf{p}=0$. So the anti-quaternion subspace, like the quaternion one, is wholly contained in the set of the elements of square zero, and it is the second cell of the quadric cone of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*. The closure fails while the vanishing holds; the two facts are the two halves of the same conjugation.

## The Hermitian Subspace

**Proposition (the values leave both halves).** Let $\tilde P,\tilde Q\in\mathbb{M}_+$, so that $P_0,Q_0$ are real and $\mathbf{P}=i\mathbf{p}$, $\mathbf{Q}=i\mathbf{q}$ with $\mathbf{p},\mathbf{q}$ real. Then

$$
\tilde P\diamond\tilde Q=i\bigl(P_0\,\mathbf{q}+Q_0\,\mathbf{p}\bigr)-\mathbf{p}\times\mathbf{q},
$$

whose real part is the cross term and whose imaginary part is the mixed term. The value is neither Hermitian nor anti-Hermitian in general, so $\mathbb{M}_+$ is **not closed** under the block and its image meets neither half in general; the image is contained in $\mathrm{Vect}(\mathbb{B})$.

*Proof.* Substitute in the coordinate rule: $\mathbf{P}=i\mathbf{p}$ and $\overline{\mathbf{Q}}=-i\mathbf{q}$ give $P_0i\mathbf{q}$, $\overline{Q_0}=Q_0$ real gives $Q_0i\mathbf{p}$, and $(i\mathbf{p})\times(-i\mathbf{q})=\mathbf{p}\times\mathbf{q}$, with the sign of the coordinate rule. The scalar part of the value is zero, so the value is a vector part; it is Hermitian only when its real part vanishes, and anti-Hermitian only when its imaginary part vanishes, and neither holds in general. $\square$

**Corollary (the diagonal on the Hermitian subspace).** At a Hermitian element,

$$
\tilde Q\diamond\tilde Q=2i\,Q_0\,\mathbf{q},
$$

with $Q_0$ real and $\mathbf{q}$ real. The diagonal vanishes exactly on the Hermitian elements with $Q_0=0$, that is the purely imaginary vectors, and on the central real elements $\mathbf{q}=0$. So the Hermitian subspace contributes to the quadric cone its purely imaginary vectors and its real centre, and not the mixed elements $e_0+ie_1$, on which the diagonal is $2ie_1$.

## The Anti-Hermitian Subspace

**Proposition (the values leave both halves).** Let $\tilde P,\tilde Q\in\mathbb{M}_-$, so that $P_0=ip_0$, $Q_0=iq_0$ are purely imaginary and $\mathbf{P}=\mathbf{p}$, $\mathbf{Q}=\mathbf{q}$ are real. Then

$$
\tilde P\diamond\tilde Q=-i\bigl(p_0\,\mathbf{q}+q_0\,\mathbf{p}\bigr)-\mathbf{p}\times\mathbf{q},
$$

whose real part is the cross term and whose imaginary part is the mixed term, with the opposite assignment to the Hermitian case. The value is neither anti-Hermitian nor Hermitian in general, so $\mathbb{M}_-$ is **not closed** under the block either.

*Proof.* Substitute $P_0=ip_0$, $\overline{\mathbf{Q}}=\mathbf{q}$, $\overline{Q_0}=-iq_0$ in the coordinate rule. $\square$

**Corollary (the diagonal on the anti-Hermitian subspace).** At an anti-Hermitian element,

$$
\tilde Q\diamond\tilde Q=-2i\,q_0\,\mathbf{q},
$$

so the diagonal vanishes exactly on the real vectors of the subspace and on its imaginary centre. The two halves of the involution therefore fail closure in the same way and differ only by a sign in the diagonal, $2iQ_0\mathbf{q}$ against $-2iq_0\mathbf{q}$; the form $H$ is Hermitian on each, $H(\tilde P,\tilde Q)=\overline{H(\tilde Q,\tilde P)}$, and the pairing of the block is read on the two halves in *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*.

## The Table of the Remarkable Subspaces

| subspace | the reading of the block | closure | the diagonal | square-zero elements |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $(\lambda e_0)\diamond\tilde R=-\lambda\overline{\mathbf{R}}$, $\tilde R\diamond(\lambda e_0)=\overline{\lambda}\mathbf{R}$ | closed, the value of two central elements being $0$ | $(\lambda e_0)\diamond(\lambda e_0)=0$ | the whole centre |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf{P}\diamond\mathbf{Q}=-\mathbf{P}\times\overline{\mathbf{Q}}$ | closed, and surjective | $-\mathbf{Q}\times\overline{\mathbf{Q}}$, $2ie_3$ at $e_1+ie_2$ | the $\mathbf{Q}$ with $\mathbf{Q}\times\overline{\mathbf{Q}}=0$, in particular the real and the imaginary vectors |
| $\mathbb{H}_{\mathbb{B}}$ | $-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$, real | closed | $0$ | the whole subspace |
| $i\mathbb{H}_{\mathbb{B}}$ | $-p_0\mathbf{q}+q_0\mathbf{p}-\mathbf{p}\times\mathbf{q}$, real | not closed, image the real vector triple | $0$ | the whole subspace |
| $\mathbb{M}_+$ | $i(P_0\mathbf{q}+Q_0\mathbf{p})-\mathbf{p}\times\mathbf{q}$ | not closed | $2iQ_0\mathbf{q}$ | the purely imaginary vectors and the real centre |
| $\mathbb{M}_-$ | $-i(p_0\mathbf{q}+q_0\mathbf{p})-\mathbf{p}\times\mathbf{q}$ | not closed | $-2iq_0\mathbf{q}$ | the real vectors and the imaginary centre |

**Remark (the two facts the table exhibits).** First, the block is surjective onto the vector subspace and reads every subspace into it, the centre included: this is the reading of the *pure-vector image* of the introduction. Second, the closure fails on the anti-quaternion subspace and on the two halves of the involution and holds on the centre, the vector subspace and the real span; the pattern is not the pattern of the symmetric half of the same row, where the closure holds exactly on the three subspaces that contain the idempotent $e_0$ — the centre, the quaternion subspace and the Hermitian subspace. The two patterns are the two halves of the product: the central half is closed where its value $H(\tilde P,\tilde Q)e_0$ can live, and the vector half is closed exactly on the centre, on the vector subspace and on the real span, while on the anti-quaternion subspace and on the Hermitian subspace the vector part is purely imaginary, so its cross product with the conjugate of the other argument is real and leaves the subspace, and on the anti-Hermitian subspace the first term contributes a purely imaginary vector to a subspace whose vectors are real.

**Remark (the comparison with the sibling readings).** The same remarkable subspaces read by the general plain sesquilinear product, by the general plain algebra and by the general quaternionic structures are *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions*, *Remarkable Subspaces under the General Plain Algebra of Biquaternions*, *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* and *Remarkable Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*; the comparison of the readings side by side is *Comparison of the Remarkable Subspaces* and *Remarkable Subspaces and the Four General Products*. This article is the antisymmetric reading of the four, and it is the one whose image is a single one of the remarkable subspaces.

## Summary

On the remarkable subspaces the block is read as follows. It is central-free: no value lies in the centre, and the centre of the *operator* is the kernel of $L^{\diamond}_{e_0}$. Its image is the vector subspace, where it is $-\mathbf{P}\times\overline{\mathbf{Q}}$ and is surjective. It is closed on the centre, on the real span $\mathbb{H}_{\mathbb{B}}$, where it is $-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ with real values, and on the vector subspace, and it is **not** closed on the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, whose reading is the real vector $-p_0\mathbf{q}+q_0\mathbf{p}-\mathbf{p}\times\mathbf{q}$, nor on the Hermitian and anti-Hermitian halves, whose readings are $i(P_0\mathbf{q}+Q_0\mathbf{p})-\mathbf{p}\times\mathbf{q}$ and $-i(p_0\mathbf{q}+q_0\mathbf{p})-\mathbf{p}\times\mathbf{q}$ and leave both halves. The diagonal vanishes on the centre, on the real span and on the anti-quaternion subspace, and it does not vanish in general on the vector subspace, where it is $-\mathbf{Q}\times\overline{\mathbf{Q}}$ and equals $2ie_3$ at $e_1+ie_2$, nor on the two halves of the involution, where it is $2iQ_0\mathbf{q}$ on $\mathbb{M}_+$ and $-2iq_0\mathbf{q}$ on $\mathbb{M}_-$. The square-zero elements of the remarkable subspaces are the whole centre, the whole real span, the whole anti-quaternion subspace, the $\mathbf{Q}$ with $\mathbf{Q}\times\overline{\mathbf{Q}}=0$ in the vector subspace (in particular its real and its imaginary vectors), and the purely imaginary vectors of $\mathbb{M}_+$ and the real vectors of $\mathbb{M}_-$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable real subspaces |
| $\mathbf{P},\overline{\mathbf{P}}$ | a vector part and its coefficientwise conjugate |
| $(\lambda e_0)\diamond\tilde R=-\lambda\overline{\mathbf{R}}$ | the action of the centre, not annihilating |
| $\mathbf{P}\diamond\mathbf{Q}=-\mathbf{P}\times\overline{\mathbf{Q}}$ | the block on the vector subspace |
| $-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | the block on the real span, with real values |
| $i(P_0\mathbf{q}+Q_0\mathbf{p})-\mathbf{p}\times\mathbf{q}$ | the block on $\mathbb{M}_+$, leaving the half |
| $-i(p_0\mathbf{q}+q_0\mathbf{p})-\mathbf{p}\times\mathbf{q}$ | the block on $\mathbb{M}_-$, leaving the half |
| $2iQ_0\mathbf{q}$, $-2iq_0\mathbf{q}$ | the diagonal on $\mathbb{M}_+$ and on $\mathbb{M}_-$ |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation, the basis table and the pure-vector image
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the quadric cone of the square-zero elements, whose cells the two quaternion subspaces are
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the form reading of the same six
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`) and *Decompositions Along the Remarkable Subspaces* (`articles_maths/decompositions-along-the-remarkable-subspaces.md`), for the subspaces and their bases
- *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), for the pattern of the reading and the indefinite sesquilinear form
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`) and *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the readings side by side
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the ten operations of the real part and the coincidences there
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form and the involution that cut the two halves
