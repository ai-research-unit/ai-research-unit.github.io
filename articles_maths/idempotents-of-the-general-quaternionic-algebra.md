# __Idempotents of the General Quaternionic Algebra__

## Introduction

This article classifies the **idempotents** of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ read through the general quaternionic bilinear product.

An idempotent is relative to a product, and the definition is stated once in *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*; throughout this article the product is the general quaternionic product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, and the unqualified "idempotent" means an idempotent of it. The article rests on one computation: the quaternionic square of every element is the central element $N(\tilde Q)e_0$, so an idempotent is central and the idempotent equation collapses to $A^2=A$ on the scalar line. The answer is as small as it could be: **the idempotents of the product are $0$ and $e_0$ alone**, and the product has no nontrivial idempotent.

The companion article *Idempotents of the General Plain Algebra* gives the other answer, and the contrast organises this one. There the nontrivial idempotents are the **Hermitian idempotents** $\tilde\Pi(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$, a family of complex dimension two, and they carry the Peirce decomposition and the minimal left ideals of the associative theory. Here the family is displaced: reading the first slot of this product through the natural conjugation converts each Hermitian idempotent into a **square-zero** element, so the idempotents of the algebra become nilpotents of the product. The article gives the classification, names the absent bijection with the roots of $-1$, reads the idempotents as projectors on the operator side, and records the displacement into the nilpotent cone.

**Boundaries.** The idempotents of the plain product, the Hermitian idempotents, the orthogonality relations and the Peirce decomposition are *Idempotents of the General Plain Algebra* and *Ideals and Peirce Decomposition of the General Plain Algebra*; the square, the norm and the isotope reading are *Introduction to the General Quaternionic Algebra of Biquaternions* and *Norm and Invertibility in the General Quaternionic Algebra*; the nilpotents are *Nilpotents of the General Quaternionic Algebra*; the zero divisors are *Zero Divisors of the General Quaternionic Algebra*; the square-zero elements of the four general products side by side are *The Square-Zero Elements of the Four General Products*; and the projectors and the operator theory are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *The Specificities of the General Quaternionic Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$. Juxtaposition is the plain product and $\star$ the general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_0-\mathbf Q$. An element is $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$, the **norm** is $N(\tilde Q)=\sum_\mu Q_\mu^2=Q_0^2+(\mathbf Q,\mathbf Q)$, and $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ is the complex bilinear form of the vector parts. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, and $\tilde\Pi(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ is the Hermitian idempotent over a real unit vector $\hat\mu$.

## Definition, and the Square

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde\Pi\in\mathbb{B}$. The element $\tilde\Pi$ is **idempotent of $\star$** when $\tilde\Pi\star\tilde\Pi=\tilde\Pi$; the **trivial idempotents** are $0$ and the left unit $e_0$, and an idempotent different from both is **nontrivial**. The definition is *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*, and it names the product.

**Lemma (the square is central).** For every $\tilde Q\in\mathbb{B}$,

$$
\tilde Q\star\tilde Q=\tilde Q^{\natural}\tilde Q=N(\tilde Q)\,e_0 , \qquad N(\tilde Q)=Q_0^2+Q_1^2+Q_2^2+Q_3^2 .
$$

**Proof.** With $\tilde Q=Q_0e_0+\mathbf Q$ the product has scalar part $Q_0^2+(\mathbf Q,\mathbf Q)$ and vector part $Q_0\mathbf Q-Q_0\mathbf Q-\mathbf Q\times\mathbf Q=0$ at equal arguments; the statement is §*The Square Lies in the Scalar Line* of *Introduction to the General Quaternionic Algebra of Biquaternions*.

The lemma is the reason the idempotent equation is trivial here and nontrivial for the plain product. The plain square of the same element is $Q_0^2e_0+2Q_0\mathbf Q+\mathbf Q^2$, whose vector part is not obliged to vanish, and its idempotents are the Hermitian idempotents; the quaternionic square carries no vector part at all, and the equation is a quadratic in one complex variable.

## The Classification

**Theorem (idempotents).** The solutions of $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ are $\tilde\Pi=0$ and $\tilde\Pi=e_0$; the general quaternionic product has no nontrivial idempotent.

**Proof.** By the lemma the left-hand side is $N(\tilde\Pi)e_0$, an element of the centre, so an idempotent is central, $\tilde\Pi=Ae_0$ with $A\in\mathbb{C}$. For a central element the equation reads $A^2e_0=Ae_0$, that is $A^2=A$, or $A(A-1)=0$; the field $\mathbb{C}$ gives $A\in\{0,1\}$. Both values satisfy the equation.

**Remark (the equation is weaker than centrality).** The single equation $N(\tilde\Pi)=\Pi_0$ is not idempotence; it must be read with centrality attached. Every **pure** isotropic element, an element with $\mathbf Q\neq0$, $Q_0=0$ and $(\mathbf Q,\mathbf Q)=0$, satisfies $N(\tilde Q)=Q_0=0$ and is not an idempotent, its square being $0$ while it is itself neither $0$ nor central; and a non-pure element of norm zero, with $Q_0\neq0$, satisfies no scalar equation of the kind at all, since $N(\tilde Q)=0$ and $Q_0\neq0$. The nilpotents are the subject of *Nilpotents of the General Quaternionic Algebra*; here they matter as the warning that the scalar equation is necessary and not sufficient.

**Corollary.** The image of the squaring map is the scalar line and contains every idempotent; the idempotents of the product are exactly the central elements whose scalar coordinate is a root of $X^2-X$, and the central element $-e_0$, of norm $1$, shows that the norm alone does not decide idempotence.

## The Standard Idempotents of the Algebra

The idempotents of the plain product are the standard family of the algebra, and they are the elements the product fails to keep.

**Definition.** For a **real unit vector** $\hat\mu=\mu_1e_1+\mu_2e_2+\mu_3e_3$, $\mu_1^2+\mu_2^2+\mu_3^2=1$, the **Hermitian idempotent** is

$$
\tilde\Pi(\hat\mu)=\tfrac12\bigl(e_0+i\hat\mu\bigr) .
$$

**Proposition.** Every Hermitian idempotent is a nontrivial idempotent of the plain product and lies in the Hermitian subspace: $\tilde\Pi(\hat\mu)\tilde\Pi(\hat\mu)=\tilde\Pi(\hat\mu)$ and $\tilde\Pi(\hat\mu)\in\mathbb{M}_{+}$.

**Proof.** The vector $i\hat\mu$ has $(i\hat\mu)^2=i^2\hat\mu^2=(-1)(-e_0)=e_0$, so $\tilde\Pi^2=\tfrac14(e_0+2i\hat\mu+e_0)=\tilde\Pi$; and the element has real scalar part and purely imaginary vector part, which is the coordinate condition of $\mathbb{M}_{+}$ (*Introduction to the Remarkable Subspaces*). It is not $0$ and not $e_0$.

By *Idempotents of the General Plain Algebra* the nontrivial idempotents of the plain product are exactly these, one for each real unit vector, so the plain idempotent set is the family $\tilde\Pi(\hat\mu)$, a quadric of complex dimension two, together with $0$ and $e_0$. The general quaternionic product answers differently.

**Proposition (the standard idempotents are square-zero here).** For every real unit vector $\hat\mu$,

$$
\tilde\Pi(\hat\mu)\star\tilde\Pi(\hat\mu)=0 .
$$

**Proof.** The natural conjugation negates the vector part, $\tilde\Pi(\hat\mu)^{\natural}=\tfrac12(e_0-i\hat\mu)=e_0-\tilde\Pi(\hat\mu)$, the **complementary idempotent**. Hence

$$
\tilde\Pi(\hat\mu)\star\tilde\Pi(\hat\mu)=\tilde\Pi(\hat\mu)^{\natural}\tilde\Pi(\hat\mu)=\tfrac14\bigl(e_0-(i\hat\mu)^2\bigr)=\tfrac14(e_0-e_0)=0 .
$$

## The Bijection with the Roots of Minus One, and Its Absence

The plain classification of the idempotents is a **bijection** from the plain roots of $-1$ to the idempotents,

$$
\xi\longmapsto\tfrac12(e_0+\xi i) ,
$$

with inverse $\tilde\Pi\mapsto(2\tilde\Pi-e_0)/i$ (*Idempotents of the General Plain Algebra*). In the general quaternionic product this bijection has no analogue, and the article records the two statements that replace it.

**Proposition (the roots of $-1$ are not the idempotent parameters).** No root of $-1$ of the quaternionic product is an idempotent of the product.

**Proof.** An idempotent of the product is $0$ or $e_0$, of norm $0$ or $1$; a root of $-1$ has norm $-1$. The statements are §*The Roots of Minus One* of *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra* and the classification above.

**Proposition (the plain idempotents are roots of $0$).** For every real unit vector $\hat\mu$, the Hermitian idempotent is a root of $0$ of the quaternionic product, $\tilde\Pi(\hat\mu)\star\tilde\Pi(\hat\mu)=0$, and its norm vanishes. More generally every nontrivial plain idempotent $\tilde\Pi$ satisfies $\tilde\Pi\star\tilde\Pi=0$.

**Proof.** The first statement is the preceding proposition. A nontrivial plain idempotent is a zero divisor of the plain product, so $N(\tilde\Pi)=0$ (*Zero Divisors of the General Plain Algebra*), and the square in the product is $N(\tilde\Pi)e_0=0$.

The plain bijection therefore carries the plain roots of $-1$ to the **roots of $0$** of the quaternionic product, and not to its roots of $-1$; the parameter set of the plain idempotents is invisible to the quaternionic idempotent equation and reappears as the nilpotent cone.

## Idempotents as Projections

On the operator side the idempotents of the algebra recover their usual role, with the index conjugated.

**Theorem (the projector criterion).** The left multiplication $L_{\tilde P}(\tilde X)=\tilde P\star\tilde X$ is a projector, $L_{\tilde P}^{2}=L_{\tilde P}$, if and only if $\tilde P$ is an idempotent of the plain product. Consequently the product has a family of projectors of complex dimension two, indexed by the plain idempotents, while its own idempotents are $0$ and $e_0$ alone.

**Proof.** $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$ by the isotope identity, and the plain left multiplications are faithful; so $L_{\tilde P}^{2}=L_{\tilde P}$ exactly when $(\tilde P^{\natural})^2=\tilde P^{\natural}$, that is when $\tilde P$ is a plain idempotent. The family is the plain family of complex dimension two. The theorem and the monoid law $L_{\tilde P}L_{\tilde R}=L_{\tilde R\tilde P}$ are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *The Specificities of the General Quaternionic Algebra*.

**Corollary (a projector on a square-zero element).** Every nontrivial plain idempotent is a nilpotent of $\star$ whose left multiplication is a projector,

$$
\tilde\Pi\star\tilde\Pi=0 , \qquad L_{\tilde\Pi}^{2}=L_{\tilde\Pi}\neq0 ,
$$

so the element is square-zero and the operator it defines is a projector with a two-dimensional image.

**Proof.** The element statement is §*The Bijection with the Roots of Minus One, and Its Absence*; the operator statement is the theorem at the element $\tilde\Pi$.

**Remark (the two levels).** The plain product forbids the combination: there an idempotent and a nonzero nilpotent are disjoint, so no element is square-zero with an idempotent left multiplication (*Nilpotents of the General Plain Algebra*). The quaternionic product separates the two properties and assigns them to different levels: the element $\tilde\Pi$ has vanishing square, and the operator $L_{\tilde\Pi}$ is a projector. The pair $\tilde\Pi$ and $e_0-\tilde\Pi$ gives the orthogonal decomposition $\mathbb{B}=(\tilde\Pi\star\mathbb{B})\oplus((e_0-\tilde\Pi)\star\mathbb{B})$ into minimal left ideals of the plain algebra, which is the left-ideal theory of *The Specificities of the General Quaternionic Algebra*.

## Idempotents and the Non-Pure Zero Divisors

The displacement of the Hermitian idempotents is a statement about the zero divisors of the product.

**Theorem.** Let $\tilde Q=Q_0e_0+\mathbf Q$ with $Q_0\neq0$. Then $\tilde Q$ is a zero divisor of the product if and only if it is a complex multiple of a nontrivial plain idempotent, $\tilde Q=2Q_0\tilde\Pi$ with $\tilde\Pi$ a plain idempotent; and then

$$
\tilde Q\star\tilde Q=0 , \qquad \tilde Q\tilde Q=2Q_0\tilde Q\neq0 .
$$

**Proof.** The non-pure zero divisors are exactly the multiples of the nontrivial plain idempotents (*Zero Divisors of the General Quaternionic Algebra*, §*Non-Pure Zero Divisors*): the criterion $N(\tilde Q)=0$ is $(\mathbf Q,\mathbf Q)=-Q_0^2$, and the plain square is $(Q_0^2-(\mathbf Q,\mathbf Q))e_0+2Q_0\mathbf Q=2Q_0\tilde Q$, which makes $\tilde Q/(2Q_0)$ a plain idempotent.

**Corollary (the two products on the same element).** A nontrivial plain idempotent is an idempotent of the plain product and a nilpotent of the quaternionic product; and conversely a nonzero nilpotent of the quaternionic product which is non-pure is, up to a complex scalar, an idempotent of the plain product. No element is a nontrivial idempotent of both products.

**Proof.** The first clause is the theorem with $Q_0=\tfrac12$, and the second is the same reading. A nontrivial idempotent of $\star$ does not exist, by the classification.

## The Idempotent Equation on the Remarkable Subspaces

Since the square is always central, the equation $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ can hold inside a subspace only when the subspace contains the two trivial idempotents; reading it on each remarkable subspace records which ones do.

| subspace | element | $\tilde\Pi\star\tilde\Pi$ | idempotents |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $Ae_0$ | $A^2e_0$ | $0$, $e_0$ |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $\mathbf P$ | $(\mathbf P,\mathbf P)e_0$ | $0$ |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $h$ | $\bigl(h_0^2+h_1^2+h_2^2+h_3^2\bigr)e_0$ | $0$, $e_0$ |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $ih$ | $-\bigl(h_0^2+h_1^2+h_2^2+h_3^2\bigr)e_0$ | $0$ |
| $\mathbb{M}_{+}$, the Hermitian subspace | $a_0e_0+i\mathbf p$ | $\bigl(a_0^2-(\mathbf p,\mathbf p)\bigr)e_0$ | $0$, $e_0$ |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $ib_0e_0+\mathbf q$ | $\bigl(-b_0^2+(\mathbf q,\mathbf q)\bigr)e_0$ | $0$ |

**Proof.** Each entry is the norm on the subspace of the same row, by the norm table of *Norm and Invertibility in the General Quaternionic Algebra*. In the centre the equation leaves $A^2=A$, hence $A\in\{0,1\}$. In the vector subspace a central element equals a vector only at $0$; a nonzero isotropic element has square $0$ and is not idempotent. In the quaternion subspace the square is a **real** scalar multiple of $e_0$, so an idempotent is a real multiple of $e_0$ with $h_0^2=h_0$. In the anti-quaternion subspace the square is a real multiple of $e_0$ with the opposite sign, so $h=0$. In $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ the scalar parts are constrained to be real combinations, and the equation forces the vector part to vanish, then leaves the trivial pair or the origin as displayed.

**Remark.** Three subspaces, the centre, the quaternion subspace and the Hermitian subspace, carry the two trivial idempotents, and three, the vector, the anti-quaternion and the anti-Hermitian subspaces, carry only $0$; no remarkable subspace carries a nontrivial idempotent. The plain reading is the opposite: there the nontrivial idempotents are the Hermitian idempotents and lie in $\mathbb{M}_{+}$. The change of product moves them out of the idempotent set altogether.

## The Peirce Decomposition It Does Not Carry

A nonzero idempotent of an associative unital algebra carries the Peirce decomposition $A=A_1\oplus A_{1/2}\oplus A_0$ with $A_\lambda=\{x:\Pi x=\lambda x\}$, and the decomposition is the source of the minimal ideals and the matrix units (*Ideals and Peirce Decomposition of the General Plain Algebra*). The construction uses associativity twice, in reading the two maps as projections and in verifying that their images add.

For the quaternionic product there is nothing to attach it to. The only nonzero idempotent is the left unit $e_0$, and $L_{e_0}$ is the identity, so the only Peirce piece is the whole algebra. The nontrivial decomposition of the algebra — the frame of two orthogonal idempotents, the four Peirce lines, the minimal left ideals — is a property of the plain product alone, and what the quaternionic product has in its place is the centrality of the square and the projectors of §*Idempotents as Projections*, which are indexed by the plain idempotents rather than computed from the idempotents of the product.

## Summary

In the general quaternionic bilinear product the square of every element is the central element $N(\tilde Q)e_0$, so the idempotent equation forces centrality and reduces to $A^2=A$ on the scalar line. The idempotents of the product are $0$ and $e_0$ alone, and the product has no nontrivial idempotent; the plain bijection from the roots of $-1$ to the idempotents has no analogue, because the plain idempotents satisfy $\tilde\Pi\star\tilde\Pi=0$ and are roots of $0$ of the product. On the operator side the plain idempotents recover their role: $L_{\tilde P}$ is a projector exactly when $\tilde P$ is a plain idempotent, so the product has a family of projectors of complex dimension two indexed by elements that are not its idempotents, and each of them is a square-zero element whose operator is a projector. The non-pure zero divisors of the product are exactly the complex multiples of the nontrivial plain idempotents, so a nontrivial plain idempotent is an idempotent of the plain product and a nilpotent of this one. Read on the remarkable subspaces, the idempotent equation leaves the two trivial idempotents in the centre, the quaternion subspace and the Hermitian subspace, and only $0$ in the vector, anti-quaternion and anti-Hermitian subspaces.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2=-e_0$ |
| $\tilde Q=Q_0e_0+\mathbf Q$ | an element and its scalar–vector split |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| ${}^{\natural}$ | the natural conjugation $\tilde Q^{\natural}=Q_0-\mathbf Q$ |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the norm, $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ |
| $\tilde\Pi$ | an idempotent of the product; the nonzero ones are $e_0$ alone |
| $\tilde\Pi(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ | the Hermitian idempotent over a real unit vector $\hat\mu$ |
| $L_{\tilde P}$ | the left multiplication $\tilde X\mapsto\tilde P\star\tilde X$, a projector iff $\tilde P$ is a plain idempotent |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_{+},\mathbb{M}_{-}$ | the remarkable subspaces |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for idempotents and square-zero elements in a non-associative algebra.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Idempotent, the Projection and the Peirce Decomposition*, for the general definition of an idempotent and of a projector.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the idempotent equation and the Peirce decomposition in the absence of associativity.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for idempotents and their order in a ring with an involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the conjugations of an algebra and the elements they fix.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the Hermitian idempotents, the orthogonality, the bijection with the roots of $-1$ and the non-pure zero divisors.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the norm, its table on the remarkable subspaces and the one-sided equations.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the criterion, the two families and the annihilators.
- *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra.md`), for the square-zero elements, the cone and the index two.
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for the monoid law and the projectors.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the projectors, the left ideals and the decomposition.
