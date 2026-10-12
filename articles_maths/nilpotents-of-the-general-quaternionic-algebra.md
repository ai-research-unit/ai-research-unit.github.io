# __Nilpotents of the General Quaternionic Algebra__

## Introduction

This article studies the **nilpotents** of the biquaternion algebra $\mathbb{B}$ read through the general quaternionic bilinear product, the elements some power of which vanishes in that product.

The word names a product, and the definition is stated once in *Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*; throughout this article the product is the general quaternionic product $\tilde P^{\natural}\tilde Q$, and the unqualified "nilpotent" means a nilpotent of it. The quaternionic product has one property that settles the whole article: its square is the central element $N(\tilde Q)e_0$, so a nilpotent of index two is an element of vanishing algebraic norm, and no element has a higher index — a vanishing cube already forces a vanishing square. The article establishes four things. First, the **criterion**: the nilpotents of the product are the nonzero elements of algebraic norm zero, so the nilpotent set is the whole zero-divisor cone and not a proper part of it. Second, the **index is two and only two**, with the power string computed. Third, the difference from the plain product, where the nilpotents are the pure isotropic elements alone, is exactly the cancellation of the scalar term by the conjugation in the first slot; here every zero divisor is a nilpotent, the non-pure family included. Fourth, the nilpotents meet the idempotents of the product at the origin alone, and the nontrivial idempotents of the plain product are nilpotents of this one — the displacement the article makes precise.

**Boundaries.** The nilpotents of the plain product, their cone and their index are *Nilpotents of the General Plain Algebra*; the zero divisors and their two families are *Zero Divisors of the General Quaternionic Algebra*; the algebraic norm is *Norm and Invertibility in the General Quaternionic Algebra*; the idempotents of the product are *Idempotents of the General Quaternionic Algebra*; and the square-zero elements of the four general products side by side are *The Square-Zero Elements of the Twelve Structures*, which owns the comparison. The matrix representation is *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, and the ideals and the operator theory are *Ideals and Peirce Decomposition of the General Plain Algebra* and *The Specificities of the General Quaternionic Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$. Juxtaposition is the plain product and $\star$ the general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_0-\mathbf Q$. An element is $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$, the **algebraic norm** is $N(\tilde Q)=\sum_\mu Q_\mu^2=Q_0^2+(\mathbf Q,\mathbf Q)$, and $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ is the complex bilinear form of the vector parts. An element is **pure** when $Q_0=0$, and $\tilde\Pi(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ is the Hermitian idempotent over a real unit vector $\hat\mu$.

## Definition

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde\Upsilon\in\mathbb{B}$. The element $\tilde\Upsilon$ is **nilpotent of $\star$** when some power of it vanishes,

$$
\tilde\Upsilon^{\star k}=0 \quad\text{for some } k\geq1 ,
$$

the powers being read with the left-nested bracketing $\tilde\Upsilon^{\star1}=\tilde\Upsilon$ and $\tilde\Upsilon^{\star(k+1)}=\tilde\Upsilon^{\star k}\star\tilde\Upsilon$. The least such $k$ is the **index of nilpotency**; an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, is a **square-zero element of $\star$**. The definition is *Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*, and the origin is the trivial nilpotent.

Throughout this article the product is the general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$. For this product the bracketing in the definition does not matter, because the square is central and absorbs every partial product; the next section computes the string and shows that the index is two whenever it is finite.

## The Criterion

**Theorem (the criterion).** For a nonzero $\tilde\Upsilon\in\mathbb{B}$ the following are equivalent:

1. $\tilde\Upsilon$ is a nilpotent of $\star$;
2. $N(\tilde\Upsilon)=0$;
3. $\tilde\Upsilon\star\tilde\Upsilon=0$;
4. $\tilde\Upsilon$ is a zero divisor of the algebra.

**Proof.** The equivalence of (2), (3) and (4) is the criterion of *Zero Divisors of the General Quaternionic Algebra*, the square of the product being $N(\tilde\Upsilon)e_0$. For (3) implies (1) the index is two, so the element is nilpotent. For (1) implies (2), suppose $\tilde\Upsilon^{\star k}=0$ for some $k$. If $N=N(\tilde\Upsilon)$ vanished the statement (2) would hold; if $N\neq0$ then every partial product of a string of copies of $\tilde\Upsilon$ is a nonzero multiple of $e_0$ or of $\tilde\Upsilon$, by the computation of §*Index Two*, so no power vanishes, a contradiction. Hence $N=0$.

The criterion says that the nilpotents of the quaternionic product are **the whole zero-divisor set of the algebra**, and not a proper part of it. This is the sharpest difference from the plain product, whose nilpotents are the pure isotropic elements and form a proper subset of its zero divisors (*Nilpotents of the General Plain Algebra*).

## The Nilpotent Cone

**Definition.** The **nilpotent cone** of the quaternionic product is the set of its nilpotents together with the origin,

$$
C=\{\tilde\Upsilon\in\mathbb{B}:\tilde\Upsilon\star\tilde\Upsilon=0\}=\{\tilde Q:N(\tilde Q)=0\} .
$$

**Proposition (shape).** The set $C$ is a real cone of real dimension $6$ in the real eight-dimensional space $\mathbb{B}$, and it is not a real subspace.

**Proof.** The set is the vanishing set of the quadratic form $N$, one complex equation, hence two independent real equations off the origin, homogeneous of degree two; the dimension is $8-2=6$. The elements $e_1+ie_2$ and $e_1-ie_2$ lie in $C$ and their sum $2e_1$ does not, so $C$ is not a subspace.

**Corollary.** The cone is a multiplicative set: for every $\tilde P$ and every $\tilde\Upsilon$ with $N(\tilde\Upsilon)=0$, the products $\tilde P\star\tilde\Upsilon$ and $\tilde\Upsilon\star\tilde P$ lie in $C$.

**Proof.** The multiplicativity of the algebraic norm, $N(\tilde P\star\tilde\Upsilon)=N(\tilde P)N(\tilde\Upsilon)=0$, and the same in the other order.

The cone is the same set as the zero-divisor cone of *Zero Divisors of the General Quaternionic Algebra*, and it is the union of the pure family, the isotropic cone of the vector subspace of real dimension four, and the non-pure family, the complex multiples of the nontrivial plain idempotents, which fills the rest.

## Index Two

**Theorem (the power string).** Let $\tilde\Upsilon\in\mathbb{B}$ and put $N=N(\tilde\Upsilon)$. Then

$$
\tilde\Upsilon^{\star2}=N\,e_0 , \qquad
\tilde\Upsilon^{\star3}=N\,\tilde\Upsilon , \qquad
\tilde\Upsilon^{\star4}=N^{2}\,e_0 , \qquad
\tilde\Upsilon^{\star5}=N^{2}\,\tilde\Upsilon , \qquad \dots ,
$$

so the powers alternate between a central multiple of $e_0$ and a central multiple of $\tilde\Upsilon$.

**Proof.** The square is $\tilde\Upsilon^{\star2}=N(\tilde\Upsilon)e_0$ by the definition of the product. Multiplying on the right by $\tilde\Upsilon$, the left unit $e_0$ gives $\tilde\Upsilon^{\star3}=Ne_0\star\tilde\Upsilon=N\tilde\Upsilon$; multiplying again, $\tilde\Upsilon^{\star4}=(N\tilde\Upsilon)\star\tilde\Upsilon=N(\tilde\Upsilon\star\tilde\Upsilon)=N\cdot Ne_0=N^2e_0$; and the pattern repeats. The bracketing is immaterial because every partial product is one of the two forms displayed, by the same induction.

**Theorem (the index).** The only index of nilpotency in the general quaternionic product is two. If $\tilde\Upsilon^{\star k}=0$ for some $k\geq1$ and $\tilde\Upsilon\neq0$, then $k=2$ and $\tilde\Upsilon\star\tilde\Upsilon=0$.

**Proof.** By the power string, if $N\neq0$ and $\tilde\Upsilon\neq0$ then every power $\tilde\Upsilon^{\star k}$ with $k\geq2$ is a nonzero multiple of $e_0$ or of $\tilde\Upsilon$, so none vanishes; and if $N=0$ then $\tilde\Upsilon^{\star2}=0$, so the least index is two. The origin has index one.

The quaternionic product therefore has the same bounded index as the plain product, and the two differ in the **extent** of the index-two set: here it is the whole cone, there the pure isotropic cone alone.

## The Nilpotents and the Zero Divisors

**Theorem.** A nonzero nilpotent $\tilde\Upsilon$ satisfies $\tilde\Upsilon\star\tilde\Upsilon=0$ on both sides, so it lies in its own left annihilator and in its own right annihilator; it is a two-sided zero divisor of $\star$.

**Proof.** The relation $\tilde\Upsilon\star\tilde\Upsilon=0$ is the product of $\tilde\Upsilon$ with itself, and $\mathrm{Ann}_\ell(\tilde\Upsilon)=\mathrm{Ann}_r(\tilde\Upsilon)$ contains the elements that annihilate it on either side (*Zero Divisors of the General Quaternionic Algebra*).

**Theorem (the converse, which the plain product does not have).** Every zero divisor of $\star$ is a nilpotent of $\star$.

**Proof.** A zero divisor of $\star$ is a nonzero element with $N=0$, by the criterion of *Zero Divisors of the General Quaternionic Algebra*; the criterion above makes it a nilpotent.

This double statement is the displacement that organises the article. In the plain product the inclusion runs one way: every nilpotent is a zero divisor, but a non-pure zero divisor, being a multiple of a nontrivial idempotent, has a nonzero square and is not nilpotent. The quaternionic product removes the obstruction, because the conjugation in the first slot cancels the scalar term of the square; the two classes therefore coincide, at the nonzero level, and the nilpotent cone is the whole zero-divisor cone.

## The Nilpotents and the Idempotents

**Theorem (the two classes meet at the origin).** Let $\tilde\Pi$ be an idempotent of $\star$, $\tilde\Pi\star\tilde\Pi=\tilde\Pi$, and let $\tilde\Upsilon$ be a nilpotent of $\star$. If $\tilde\Pi=\tilde\Upsilon$ then $\tilde\Pi=0$.

**Proof.** The idempotents of $\star$ are $0$ and $e_0$ (*Idempotents of the General Quaternionic Algebra*), and $e_0\star e_0=e_0\neq0$, so $e_0$ is not a nilpotent; hence an element which is both is $0$.

**Remark (the plain idempotents are nilpotents here).** The disjointness is a statement about the idempotents **of this product**, and it does not extend to the idempotents of the algebra. A nontrivial plain idempotent $\tilde\Pi$ is a zero divisor of the plain product, so $N(\tilde\Pi)=0$, and therefore

$$
\tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=0 .
$$

The plain idempotents are thus nilpotents of the quaternionic product, and the plain product's theorem that an idempotent and a nonzero nilpotent never coincide (*Nilpotents of the General Plain Algebra*) has no analogue here; the only element that is both an idempotent of $\star$ and a nilpotent of $\star$ is the origin.

## The Conjugations

The four conjugations of the algebra act on the nilpotent cone, and their action is read from the algebraic norm.

| conjugation | effect on the algebraic norm | effect on the cone |
|---|---|---|
| natural, ${}^{\natural}$ | $N(\tilde Q^{\natural})=N(\tilde Q)$ | preserves $C$ |
| coefficientwise, $\bar{\cdot}$ | $N(\overline{\tilde Q})=\overline{N(\tilde Q)}$ | preserves $C$ |
| Hermitian, the composite of the two | $N$ is sent to its complex conjugate | preserves $C$ |
| complex structure, $\tilde Q\mapsto i\tilde Q$ | $N(i\tilde Q)=-N(\tilde Q)$ | preserves $C$ |

**Proof.** The natural conjugation is a plain anti-automorphism and an involution, so $N(\tilde Q^{\natural})=\tilde Q^{\natural}(\tilde Q^{\natural})^{\natural}=\tilde Q^{\natural}\tilde Q=N(\tilde Q)$. The coefficientwise conjugation conjugates every coefficient, hence the sum of their squares. The Hermitian conjugation is the composite of the two, so it sends $N$ to its complex conjugate, and the complex structure multiplies the algebraic norm by $i^2=-1$. In each case the vanishing set is preserved.

**Remark.** The complex structure sends a pure element to a pure element and exchanges no family, while the natural conjugation fixes the scalar part and negates the vector part, so it fixes the pure family and sends a non-pure nilpotent to a non-pure nilpotent. The two Hermitian subspaces $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ are exchanged by the natural conjugation, which is why the nilpotents they carry are parametrised in the same way; the coefficientwise conjugation fixes $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ and fixes no nonzero nilpotent of the vector subspace.

## The Matrix Model

In the model $\mathbb{B}\cong M_2(\mathbb{C})$ of *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, the criterion becomes the singularity of a two-by-two complex matrix.

**Theorem.** Under the isomorphism $\mathsf{M}_2$ of the algebra the following coincide: $\tilde Q$ is a nilpotent of $\star$; $\mathsf{M}_2(\tilde Q)$ is singular, $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)=0$; and $\mathsf{M}_2(\tilde Q)$ is not invertible.

**Proof.** The determinant of the matrix model is the algebraic norm of the element (*The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*), and the criterion is $N=0$.

**Corollary.** The nilpotents of $\star$ are the **singular** matrices; the nilpotents of the plain product are the singular matrices that are also **trace-free**, of trace $2Q_0$ and determinant $N(\tilde Q)$, since the criterion of the plain product is $Q_0=0$ together with $N(\tilde Q)=0$ (*Nilpotents of the General Plain Algebra*). The plain nilpotents are therefore the trace-free part of the nilpotents of $\star$, and the augmentation is the non-pure family, the matrices with non-zero trace that are singular.

## The Nilpotents and the Ideals

Since $\star$ is not associative, the ideal theory of the product is the left-module theory of the plain product, and the nilpotents enter it through the plain families.

**Theorem.** Let $\tilde\Upsilon\neq0$ be a nilpotent of $\star$ and let $I_{\tilde\Upsilon}=\{\tilde X:\tilde X\tilde\Upsilon=0\}$ and $J_{\tilde\Upsilon}=\{\tilde X:\tilde\Upsilon\tilde X=0\}$ be its plain left and right annihilators. The $\star$-left ideal generated by $\tilde\Upsilon$ is the plain left ideal $\mathbb{B}\tilde\Upsilon$, and the $\star$-left annihilator is $\mathrm{Ann}_\ell(\tilde\Upsilon)=\{\tilde X:\tilde\Upsilon^{\natural}\tilde X=0\}$, the plain right annihilator $J_{\tilde\Upsilon^{\natural}}$ of the conjugated element, which is the plain right ideal $\tilde\Upsilon\mathbb{B}$; both are of complex dimension two. The plain left ideal and the plain left annihilator of $\tilde\Upsilon$ coincide, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$, exactly when $\tilde\Upsilon$ is **pure**, and they are complementary planes when it is not; the same dichotomy holds on the right, $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$ exactly when $\tilde\Upsilon$ is pure. The $\star$-left ideal $\mathbb{B}\tilde\Upsilon$ and the $\star$-annihilator $\tilde\Upsilon\mathbb{B}$ are **distinct** planes, and they meet in the line $\mathbb{C}\tilde\Upsilon$.

**Proof.** $\mathbb{B}\star\tilde\Upsilon=\{\tilde X^{\natural}\tilde\Upsilon:\tilde X\in\mathbb{B}\}=\mathbb{B}\tilde\Upsilon$, because $\natural$ is a bijection, and this is the plain left ideal. For the annihilator, $\tilde X^{\natural}\tilde\Upsilon=0$ if and only if its conjugate $\tilde\Upsilon^{\natural}\tilde X$ vanishes, so $\mathrm{Ann}_\ell(\tilde\Upsilon)=\{\tilde X:\tilde\Upsilon^{\natural}\tilde X=0\}=J_{\tilde\Upsilon^{\natural}}$, the conjugate $\natural(I_{\tilde\Upsilon})$ of the plain left annihilator, of complex dimension two like it. This annihilator contains the plain right ideal $\tilde\Upsilon\mathbb{B}$, because $\tilde\Upsilon^{\natural}(\tilde\Upsilon\tilde X)=(\tilde\Upsilon^{\natural}\tilde\Upsilon)\tilde X=0$; the right ideal is also of complex dimension two, so $\mathrm{Ann}_\ell(\tilde\Upsilon)=\tilde\Upsilon\mathbb{B}$. The element $\tilde\Upsilon$ lies in both spaces, since $\tilde\Upsilon^{\natural}\tilde\Upsilon=N(\tilde\Upsilon)e_0=0$, so the line $\mathbb{C}\tilde\Upsilon$ lies in their intersection. The two planes are distinct: were they equal, their common value would be at once a left ideal and a right ideal of the plain product, hence a two-sided ideal, nonzero because it contains $\tilde\Upsilon$ and proper because its dimension is two; but the plain algebra is the simple matrix algebra $M_2(\mathbb{C})$, which has no such ideal. The intersection is therefore exactly the line $\mathbb{C}\tilde\Upsilon$. For a pure $\tilde\Upsilon$ the plain nilpotent identities $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ and $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$ hold (*Nilpotents of the General Plain Algebra*); for a non-pure $\tilde\Upsilon$, a multiple of a plain idempotent, the plain ideal and the plain annihilator are distinct complementary planes on each side (*Ideals and Peirce Decomposition of the General Plain Algebra*).

The nilpotents therefore split, in the ideal theory, exactly as the zero divisors split: the pure ones behave as the plain nilpotents do, with the plain ideal equal to the plain annihilator, and the non-pure ones behave as the idempotent multiples do, with the plain ideal and the plain annihilator complementary.

## The Nilpotents and the Remarkable Subspaces

The nilpotents are the elements of algebraic norm zero, so their distribution among the remarkable subspaces is the distribution of the zeros of $N$, whose signatures are *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*.

| remarkable subspace | nilpotents of $\star$ |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | none |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | none |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | none |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | the pure nilpotents, an isotropic cone of real dimension four |
| $\mathbb{M}_{+}$, the Hermitian subspace | the isotropic cone of $\mathbb{M}_{+}$, of real dimension three, all of it non-pure |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | the isotropic cone of $\mathbb{M}_{-}$, of real dimension three, all of it non-pure |

The entries are forced by the definiteness of the algebraic norm: it is positive definite on the quaternion subspace and negative definite on the anti-quaternion subspace, so neither carries a nonzero nilpotent, and it vanishes on the centre only at the origin. The vector subspace carries the whole pure family, and the two Hermitian subspaces carry the non-pure nilpotents whose scalar and vector contributions cancel, the elements $e_0\pm ie_1$ in $\mathbb{M}_{+}$ and the elements $e_1\pm ie_0$ in $\mathbb{M}_{-}$ being the standard witnesses.

**Remark (the nilpotents outside the six subspaces).** Unlike the plain nilpotents, which all lie in the vector subspace, the nilpotents of $\star$ are not confined to the six remarkable subspaces. The elements $e_1+ie_2$ and $e_0+ie_1$ lie in the vector and in the Hermitian subspace respectively, but the element $\tilde Q=e_0+ie_1+e_2+ie_3$ has $N=1-1+1-1=0$ and is neither pure, its scalar part being $1$, nor Hermitian, its vector part having the real coordinate $1$ in the second place, nor anti-Hermitian, its scalar part being real; so it lies in none of the six. The cone is strictly larger than the union of its traces on the remarkable subspaces, and the plain picture, in which the vector subspace contains the cone, does not extend.

## Summary

In the general quaternionic bilinear product the square is the central element $N(\tilde Q)e_0$, so a nonzero element is nilpotent exactly when its algebraic norm vanishes, and the nilpotent set is the whole zero-divisor cone: a real cone of dimension six that is not a subspace and is stable under the product. The index of nilpotency is two and only two, the powers running $\tilde\Upsilon,\tilde\Upsilon^{\star2}=Ne_0,\tilde\Upsilon^{\star3}=N\tilde\Upsilon,\dots$ with $N=N(\tilde\Upsilon)$, so a vanishing cube already forces a vanishing square. Every nilpotent annihilates itself, and, in contrast to the plain product, every zero divisor is a nilpotent; the plain idempotents are nilpotents of this product, and the only element that is both an idempotent of the product and a nilpotent is the origin. The natural, the coefficientwise and the Hermitian conjugations preserve the cone, and the complex structure does too, multiplying the algebraic norm by $-1$; in the matrix model the nilpotents are the singular matrices, of which the plain nilpotents are the trace-free ones; in the ideal theory the pure nilpotents have their plain ideal equal to their plain annihilator and the non-pure ones do not, while in the product the $\star$-left ideal generated by a nilpotent and its $\star$-annihilator are distinct planes meeting in the line $\mathbb{C}\tilde\Upsilon$; and among the remarkable subspaces the vector, the Hermitian and the anti-Hermitian carry nilpotents while the centre, the quaternion and the anti-quaternion carry none, the element $e_0+ie_1+e_2+ie_3$ lying outside all six.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| $\tilde\Upsilon$ | a nilpotent of the product |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the algebraic norm, $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ |
| $\tilde Q^{\star k}$ | the $k$-th power, left-nested; the index is two |
| $C=\{N=0\}$ | the nilpotent cone, the zero-divisor cone, real dimension six |
| $\tilde\Pi(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ | the Hermitian idempotent, a nilpotent of $\star$ |
| $\mathsf{M}_2(\tilde Q)$ | the two-by-two matrix model, with $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$ |
| $\mathbb{M}_{+},\mathbb{M}_{-}$ | the Hermitian and the anti-Hermitian subspaces, each carrying an isotropic cone |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the index of nilpotency and the square-zero elements of a non-associative algebra.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Nilpotent*, for the general definition of a nilpotent, of its index and of a square-zero element.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for isotopes and the way a change of product moves the nilpotents.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), for the plain nilpotents, their isotropic cone of real dimension four and the index two.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the criterion, the two families and the annihilators.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the algebraic norm, its multiplicativity and the criterion.
- *Idempotents of the General Quaternionic Algebra* (`articles_maths/idempotents-of-the-general-quaternionic-algebra.md`), for the idempotents $0$ and $e_0$ and the displacement of the plain idempotents.
- *The Square-Zero Elements of the Twelve Structures* (`articles_maths/the-square-zero-elements-of-the-twelve-structures.md`), for the square-zero sets of the four general products side by side.
- *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-quaternionic-algebra-in-the-2x2-matrix-element-representation.md`), for the isomorphism $\mathsf{M}_2$ and its determinant.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the left ideals of the product and the operator theory.
