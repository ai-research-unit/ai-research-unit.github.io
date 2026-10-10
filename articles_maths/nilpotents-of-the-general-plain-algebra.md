# __Nilpotents of the General Plain Algebra__

## Introduction

The general plain bilinear product $\tilde P\tilde Q$ is the one of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* that makes the underlying complex space of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ an associative unital $\mathbb{C}$-algebra, and that algebra is the subject of *Introduction to the General Plain Algebra of Biquaternions*. This article studies its **nilpotents**: the nonzero elements whose square vanishes.

The class is small and rigid. A nilpotent has vanishing scalar part, so it is a *pure* biquaternion; its vector part is isotropic for the complex bilinear form $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$; and those two conditions together are equivalent to the vanishing of the square. Nothing of the kind happens at index three: an element whose cube vanishes already has vanishing square, so the algebra carries no nilpotent of higher index. Each nonzero nilpotent annihilates itself, $\tilde\Upsilon\tilde\Upsilon=0$, and is therefore a zero divisor of a particularly simple kind — it is its own two-sided annihilating partner. The nilpotents are exactly the *pure* family of the zero divisors of *Zero Divisors of the General Plain Algebra*, the other family being the complex multiples of the nontrivial idempotents.

The two neighbouring element theories are elsewhere. The zero divisors of the algebra, both families and the criterion $c(\tilde P)=0$ on the central square, are the subject of *Zero Divisors of the General Plain Algebra*, and the same criterion read against the four general products is *The Zero Divisors and the Four General Products*. The idempotents, the second family and its classification, are *Idempotents of the General Plain Algebra*. The nilpotents appear in the classification of the three central values as the nonzero roots of $0$ in *Biquaternion Square Roots of Minus One, Zero and Plus One*; they generate the minimal ideals in *Biquaternion Ideals and Peirce Decomposition*; and they are the square-zero elements of the plain product in the four-product comparison of *The Square-Zero Elements of the Four General Products* and *Comparison Between the Four General Products*. The model used here is *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and the position of the class in the remarkable subspaces is *Introduction to the Remarkable Subspaces*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$, $i^2=-1$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with $Q_0\in\mathbb{C}$ and $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$ and the star is $\tilde Q^{*}=\overline{Q_0}-\overline{\mathbf Q}$. The unit is written $e_0$ and is fixed by both conjugations. The **central square** is

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=c(\tilde Q)e_0,\qquad c(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2},
$$

and $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$ is the general plain bilinear form of the two vector parts. A nilpotent is written $\tilde\Upsilon$ (§*The nilpotent convention* of *Conventions in Mathematics*), a generic element $\tilde P$ or $\tilde Q$, and an idempotent $\tilde\Pi$.

## Definition

**Definition.** A **nilpotent** of the general plain algebra is an element $\tilde\Upsilon\in\mathbb{B}$ with vanishing square,

$$
\tilde\Upsilon^{2}=0 .
$$

The element $0$ is a nilpotent, the trivial one, and the article is concerned with the nonzero ones. A nilpotent is of **index two**: its square vanishes while it does not, and no higher power is needed. The equation names a product, and the notion is relative to it; the general definition, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the 12 Algebraic Structures*. Throughout, the product is the general plain bilinear product, the multiplication of the algebra, and where another of the four general products is meant it is named.

The square is the only power that has to be checked. Since $\tilde\Upsilon^{3}=\tilde\Upsilon\tilde\Upsilon^{2}=\tilde\Upsilon^{2}\tilde\Upsilon$, a square-zero element has every higher power zero, and the next section shows conversely that a vanishing cube already forces a vanishing square. Index two is therefore the only index the algebra carries, and the two clauses of the definition are exhaustive: the nilpotents are exactly the nonzero square-zero elements, with no further stratification.

The star and the natural conjugation preserve nilpotency, since conjugation is multiplicative and therefore carries a vanishing square to a vanishing square,

$$
(\tilde\Upsilon^{*})^{2}=(\tilde\Upsilon^{2})^{*}=0 ,\qquad (\tilde\Upsilon^{\natural})^{2}=(\tilde\Upsilon^{2})^{\natural}=0 .
$$

The nilpotents are thus a conjugation-stable class, and a statement about one nilpotent is a statement about its two conjugates.

## The Criterion

The square of a general element closes in two terms, one central and one along the vector part, because the vector part is a pure quaternion combination and its own square is central:

$$
\tilde Q^{2}=\bigl[Q_0^{2}-(\mathbf Q,\mathbf Q)\bigr]e_0+2Q_0\mathbf Q .
$$

**Theorem (the criterion for a nilpotent).** For $\tilde P\in\mathbb{B}$ the following are equivalent: $\tilde P^{2}=0$; $\tilde P$ is pure, $P_0=0$, and its vector part is isotropic, $(\mathbf P,\mathbf P)=0$; and $P_0=0$ and $c(\tilde P)=0$.

**Proof.** The displayed formula expands the square. If $P_0\neq0$ then the vector part $2P_0\mathbf P$ vanishes only for $\mathbf P=0$, and then the scalar part is $P_0^{2}\neq0$; so a nilpotent is pure. For a pure $\tilde P$ the formula reads $\tilde P^{2}=-(\mathbf P,\mathbf P)e_0$, a central element, which vanishes exactly when $(\mathbf P,\mathbf P)=0$. Finally, for pure $\tilde P$ the central square is $c(\tilde P)=P_0^{2}+(\mathbf P,\mathbf P)=(\mathbf P,\mathbf P)$, so the two conditions agree. $\square$

**Corollary.** Every nilpotent is pure, and every nonzero nilpotent is a zero divisor. Its only nonzero power relation is $\tilde\Upsilon^{2}=0$, the central zero, so its powers stop at the second.

The criterion separates the class sharply: the nilpotents are the elements of the vector subspace (the kernel of the scalar part) whose vector part is isotropic for the complex bilinear form. An element with a nonzero scalar part is never nilpotent, however small its central square.

## The Nilpotent Cone

The set of nilpotents is the vanishing set of the two conditions of the criterion, and it is a cone. In the complex coordinates $\mathbf P=(P_1,P_2,P_3)$ the single complex equation $(\mathbf P,\mathbf P)=P_1^{2}+P_2^{2}+P_3^{2}=0$ is two real equations, and writing $P_k=p_k+ip_k'$ with real $p_k,p_k'$ they are

$$
p_1^{2}+p_2^{2}+p_3^{2}=p_1'^{2}+p_2'^{2}+p_3'^{2},\qquad p_1p_1'+p_2p_2'+p_3p_3'=0 .
$$

**Proposition (the cone).** The nilpotents form the **nilpotent cone**

$$
\{\tilde\Upsilon=P_1e_1+P_2e_2+P_3e_3 : P_1^{2}+P_2^{2}+P_3^{2}=0\},
$$

a complex cone of complex dimension two and real dimension four, a four-real-parameter family. Its nonzero elements are written

$$
\tilde\Upsilon=r(\hat u+i\hat v),\qquad r>0,
$$

where $\hat u,\hat v$ is an orthonormal pair of real unit vectors and $(\hat u,\hat v)$ is read in the real Euclidean sense.

**Proof.** The first is the criterion. The complex equation cuts a complex-quadric cone in $\mathbb{C}^{3}$, of complex dimension two; as a real cone it is the two real equations displayed, whose independence away from the origin gives real dimension four. For the parametrisation, the two real equations say that the real part $\boldsymbol{\rho}=r\hat u$ and the imaginary part $\boldsymbol{\rho}'=r\hat v$ have equal length and are orthogonal, which is the stated form; conversely such a pair satisfies both. $\square$

The cone is stable under complex scaling, $\tilde\Upsilon\mapsto\lambda\tilde\Upsilon$ for $\lambda\in\mathbb{C}$, because the isotropy condition is homogeneous of degree two; it is stable under the star, which conjugates the two real parts; and the natural conjugation sends $\tilde\Upsilon$ to $-\tilde\Upsilon$, the other element of the same line. The parameter $r$ is the common length of the two real parts, and the pair $(\hat u,\hat v)$ is determined up to the simultaneous sign change $(\hat u,\hat v)\mapsto(-\hat u,-\hat v)$.

## Index Two

**Theorem (no higher index).** For the general plain algebra, $\tilde P^{3}=0$ exactly when $\tilde P^{2}=0$. Every nilpotent is of index two, and the algebra carries none of index three or more.

**Proof.** The cube follows from the displayed square,

$$
\tilde P^{3}=\tilde P\,\tilde P^{2}=P_0\bigl[P_0^{2}-3(\mathbf P,\mathbf P)\bigr]e_0+\bigl[3P_0^{2}-(\mathbf P,\mathbf P)\bigr]\mathbf P .
$$

If $\mathbf P=0$ then $\tilde P=P_0e_0$ and $\tilde P^{3}=P_0^{3}e_0$, which vanishes only for $P_0=0$, that is for $\tilde P=0$, and then $\tilde P^{2}=0$ as well. If $\mathbf P\neq0$ then the vanishing of the vector part of $\tilde P^{3}$ forces $(\mathbf P,\mathbf P)=3P_0^{2}$, and the scalar part is then $P_0[P_0^{2}-3\cdot3P_0^{2}]=-8P_0^{3}$, which vanishes only for $P_0=0$, whereupon $(\mathbf P,\mathbf P)=0$. In both cases $\tilde P^{3}=0$ gives $P_0=0$ and $(\mathbf P,\mathbf P)=0$, which is $\tilde P^{2}=0$. The converse is immediate. $\square$

The theorem is the reason the word "nilpotent" needs no index qualifier here. It also fixes the shape of the powers of an element: a nilpotent has the two-term power string $\tilde\Upsilon,\tilde\Upsilon^{2}=0$ and no longer one, whereas a non-pure zero divisor has the infinite string $\tilde P^{k}=2^{k-1}P_0^{k-1}\tilde P$ of *Zero Divisors of the General Plain Algebra*.

## The Nilpotents and the Zero Divisors

A nonzero nilpotent is a zero divisor, and in the strongest possible way: it annihilates itself.

**Proposition.** A nonzero nilpotent $\tilde\Upsilon$ satisfies $\tilde\Upsilon\tilde\Upsilon=0$ on both sides, so it lies in its own left annihilator and in its own right annihilator; the pair $(\tilde\Upsilon,\tilde\Upsilon)$ is a pair of nonzero elements with vanishing product, and $\tilde\Upsilon$ is a two-sided zero divisor.

**Proof.** The relation $\tilde\Upsilon^{2}=0$ is the product of $\tilde\Upsilon$ with itself, on either side, which is exactly the statement. $\square$

This is the property that singles the nilpotents out among the zero divisors. A non-pure zero divisor $\tilde P$ with $P_0\neq0$ has $\tilde P^{2}=2P_0\tilde P\neq0$, so it never annihilates itself; it annihilates only the complementary idempotent direction, and its annihilator is a plane transverse to it. A nilpotent, by contrast, is its own annihilating partner: the minimal left ideal it generates is its own annihilator, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$, whereas for a non-pure zero divisor the ideal generated and the annihilator are distinct and complementary (*Biquaternion Ideals and Peirce Decomposition*).

The nilpotents are one of the two families of the zero-divisor set, and the family split is the vanishing of the scalar part: *Zero Divisors of the General Plain Algebra* calls the elements with $P_0=0$ the **pure** family and those with $P_0\neq0$ the **non-pure** family, and the pure family is exactly the nonzero nilpotents. The zero-divisor set of the algebra is the union of the two, a complex cone of complex dimension three and real dimension six, of which the nilpotent cone is the two-dimensional complex part carried by the vector subspace and the non-pure family is the rest.

## The Nilpotents and the Idempotents

The two named element classes of the algebra, nilpotents and idempotents, do not mix.

**Theorem.** No element of $\mathbb{B}$ is both an idempotent and a nonzero nilpotent. The two classes meet only at $0$.

**Proof.** If $\tilde X^{2}=\tilde X$ and $\tilde X^{2}=0$ then $\tilde X=0$. $\square$

The disjointness is the two-family statement in another dress. The zero-divisor set splits into the nilpotents, whose square vanishes, and the complex multiples of the nontrivial idempotents, whose square is $2P_0\tilde P$ and does not vanish; the nontrivial idempotents themselves are the second family with the scalar part fixed to $\tfrac12$, and they are the elements of the algebra that are simultaneously idempotent and a zero divisor (*Idempotents of the General Plain Algebra*). A nilpotent is a zero divisor that is never a projector; a nontrivial idempotent is a zero divisor that is never nilpotent; and the trivial idempotents $0$ and $e_0$ are the only idempotents of the algebra that are not zero divisors, $e_0$ being a unit.

## The Conjugations

The four conjugations act on the nilpotent cone in a simple way, and the action is worth recording because the two families of the zero divisors are separated by it.

| conjugation | effect on a nilpotent $\tilde\Upsilon=r(\hat u+i\hat v)$ |
|---|---|
| natural, ${}^{\natural}$ | $-\tilde\Upsilon=-r(\hat u+i\hat v)$, a nilpotent |
| star, ${}^{*}$ | $\overline{\tilde\Upsilon}=r(\hat u-i\hat v)$, a nilpotent |
| Hermitian, ${}^{\natural}\circ{}^{*}={}^{*}\circ{}^{\natural}=\overline{\cdot}$ | $-\overline{\tilde\Upsilon}=-r(\hat u-i\hat v)$, a nilpotent |
| reversal | $\widetilde\Upsilon$ and the three above according to the layer |

The star fixes no nonzero nilpotent: a star-fixed element has real coefficients, and a pure real vector with $(\mathbf P,\mathbf P)=p_1^{2}+p_2^{2}+p_3^{2}=0$ vanishes, since the three squares are nonnegative. So the star pairs the nilpotents two by two, exactly as it pairs the nonzero roots of $-1$ that are not Hermitian (*Biquaternion Square Roots of Minus One, Zero and Plus One*). The class is a cone, and each conjugation is a real-linear bijection of the cone onto itself.

The real and imaginary parts make the same point. Writing $\tilde\Upsilon=\boldsymbol{\rho}+i\boldsymbol{\rho}'$ with $\boldsymbol{\rho},\boldsymbol{\rho}'$ real pure vectors, the nilpotency is the pair of real equations of §*The Nilpotent Cone*: the two real parts of a nilpotent are orthogonal and of equal length. This is a real condition, and the class is real-algebraically defined even though the algebra is complex.

## The Matrix Model

In the model $\mathbb{B}\cong M_2(\mathbb{C})$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* the criterion becomes the linear algebra of a trace-free singular matrix.

**Theorem.** Under the isomorphism $\Phi$ with $\Phi(\tilde P)=P_0\mathrm{I}_2-iP_1\sigma_1-iP_2\sigma_2-iP_3\sigma_3$ the following coincide: $\tilde P$ is a nilpotent; $\Phi(\tilde P)$ is a nonzero nilpotent matrix; $\Phi(\tilde P)$ is trace-free, $\mathrm{tr}\,\Phi(\tilde P)=2P_0=0$, and singular, $\det\Phi(\tilde P)=c(\tilde P)=0$.

**Proof.** The trace is $2P_0$ and the determinant is $c(\tilde P)$; the criterion is $P_0=0$ and $c(\tilde P)=0$, which is the stated pair. A nonzero two-by-two complex matrix that is singular and trace-free has only the eigenvalue $0$ and is nilpotent, and conversely a nilpotent matrix is singular and trace-free. $\square$

So the nilpotents are the nonzero rank-one trace-free complex matrices, that is the matrices conjugate to the single Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, the strictly triangular form. The two standard nilpotents are the off-diagonal Peirce units

$$
\tilde\Upsilon_1=\frac{ie_1-e_2}{2},\qquad \tilde\Upsilon_2=\frac{ie_1+e_2}{2},
$$

with $\tilde\Upsilon_1^{2}=\tilde\Upsilon_2^{2}=0$, which are exchanged by the star and which, together with the two primitive idempotents $\tilde\Pi_1,\tilde\Pi_2$, form a $\mathbb{C}$-basis of $\mathbb{B}$ with the multiplication table $\tilde\Upsilon_1\tilde\Upsilon_2=\tilde\Pi_1$ and $\tilde\Upsilon_2\tilde\Upsilon_1=\tilde\Pi_2$ (*Biquaternion Ideals and Peirce Decomposition*). Every nilpotent is a complex multiple of a conjugate of one of these two, and the cone is the orbit of $\tilde\Upsilon_1$ under the group of invertible elements.

## The Nilpotents and the Ideals

The nilpotents are the elements on which the ideal theory of the algebra is simplest, because the ideal they generate and the annihilator they determine coincide.

**Theorem.** Let $\tilde\Upsilon\neq0$ be a nilpotent and let $I_{\tilde\Upsilon}=\{\tilde X:\tilde X\tilde\Upsilon=0\}$ and $J_{\tilde\Upsilon}=\{\tilde X:\tilde\Upsilon\tilde X=0\}$ be its left and right annihilators. Then $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ and $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$; each is a minimal one-sided ideal of real dimension four, and the two coincide exactly for the nilpotents.

**Proof.** If $\tilde\Upsilon^{2}=0$ then $(\tilde X\tilde\Upsilon)\tilde\Upsilon=\tilde X\tilde\Upsilon^{2}=0$ for every $\tilde X$, so $\mathbb{B}\tilde\Upsilon\subseteq I_{\tilde\Upsilon}$; both are nonzero proper left ideals and both are minimal of real dimension four, hence equal. The right statement is the mirror image. The converse, that coincidence forces nilpotency, is the statement for the other class in *Introduction to the Remarkable Subspaces*. $\square$

The deeper ideal theory, the Peirce decomposition, the minimal left and right ideals $\mathbb{B}\tilde\Pi_1,\mathbb{B}\tilde\Pi_2$ and the module structure of the algebra over itself, is *Biquaternion Ideals and Peirce Decomposition* and *Modules over the General Plain Algebra of Biquaternions*; the nilpotents enter it as the off-diagonal units $\tilde\Upsilon_1,\tilde\Upsilon_2$.

## The Nilpotents and the Remarkable Subspaces

Since a nilpotent is pure, its scalar part vanishes, and the vanishing of the scalar part is the defining condition of the vector subspace $\mathrm{Vect}(\mathbb{B})$, the kernel of the scalar part (*Introduction to the Remarkable Subspaces*). The nilpotents therefore lie in $\mathrm{Vect}(\mathbb{B})$ and nowhere else.

| remarkable subspace | nilpotents |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | none |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | none |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | none |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | the nilpotent cone, of real dimension four |
| $\mathbb{M}_{+}$, the Hermitian subspace | none |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | none |

The entries are forced: the centre, the quaternion subspace and the anti-quaternion subspace consist of units and $0$ and carry no zero divisor; in the two Hermitian subspaces the square of an element is $2a_0\tilde Q$ and the Hermitian part of a nilpotent is $0$, so a Hermitian nilpotent vanishes. The vector subspace is thus the only remarkable subspace with a nonzero nilpotent, and every nonzero nilpotent lies in it. The vector subspace is not a subalgebra, but it is exactly the union of the scalar multiples of the nilpotents together with the origin, as the criterion shows.

## Summary

The nilpotents of the general plain algebra are the nonzero elements of vanishing square. The criterion is $P_0=0$ and $(\mathbf P,\mathbf P)=0$, so every nilpotent is pure and its vector part is isotropic for the complex bilinear form; the class is the nilpotent cone, a complex cone of complex dimension two and real dimension four, parametrised as $r(\hat u+i\hat v)$ over orthonormal pairs of real unit vectors. The algebra has no nilpotent of index three: $\tilde P^{3}=0$ exactly when $\tilde P^{2}=0$, so index two is the only index, and the powers of a nilpotent stop at the second.

Every nonzero nilpotent annihilates itself, so it is a two-sided zero divisor and the ideal it generates is its own annihilator; the nilpotents are the pure family of the zero-divisor set, the non-pure family being the complex multiples of the nontrivial idempotents, and the two classes meet only at $0$. The star preserves the nilpotent set and fixes none of it, the natural conjugation sends $\tilde\Upsilon$ to $-\tilde\Upsilon$, and in the model $M_2(\mathbb{C})$ the nilpotents are the nonzero trace-free singular matrices, the conjugates of the strictly triangular Jordan block, with the two off-diagonal Peirce units as the standard pair. Of the remarkable subspaces only the vector subspace contains one, and it contains all of them.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Upsilon$ | a nilpotent, $\tilde\Upsilon^{2}=0$ (§*The nilpotent convention*) |
| $\tilde\Upsilon_1,\tilde\Upsilon_2$ | the two off-diagonal Peirce units $\tfrac{ie_1-e_2}{2}$, $\tfrac{ie_1+e_2}{2}$ |
| $\tilde\Pi$ | an idempotent |
| $c(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, $\det\Phi(\tilde P)$ |
| $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ | the general plain bilinear form of the vector parts |
| $\{\tilde\Upsilon\}$ | the nilpotent cone, $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ |
| $r(\hat u+i\hat v)$ | the parametrisation of the cone over orthonormal real unit pairs |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of the nilpotent and the square-zero element, and the dictionary of the classes against the four general products.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the two families of the zero-divisor set, the pure family being exactly these nilpotents, and the criterion in terms of the scalar part.
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the nilpotents as the nonzero roots of $0$ and their place among the three central values.
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the off-diagonal units $\tilde\Upsilon_1,\tilde\Upsilon_2$, the minimal ideals they generate and the Peirce basis.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the second family, the idempotents, and the disjointness of the two classes.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the vector subspace, the nilpotent cone it carries and the absence of a nilpotent in the other five subspaces.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism $\Phi$, the trace and determinant and the triangular Jordan form.
- *The Zero Divisors and the Four General Products* (`articles_maths/the-zero-divisors-and-the-four-general-products.md`) and *The Square-Zero Elements of the Four General Products* (`articles_maths/the-square-zero-elements-of-the-four-general-products.md`), for the same class read against the four general products, where only the plain product has this square-zero set.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), §*The nilpotent convention*, for the symbol $\tilde\Upsilon$.
