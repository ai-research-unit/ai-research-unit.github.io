# __Zero Divisors of the Symmetric Quaternionic Algebra__

## Introduction

The general plain algebra, the general quaternionic algebra and their two sesquilinear companions share one zero-divisor set on the biquaternion space, the vanishing of the constant term of the characteristic polynomial, and that set is a proper subset of the space (*Zero Divisors of the General Plain Algebra*). The symmetric quaternionic multiplication behaves differently: **every nonzero element is a zero divisor of it**. That is the point of this article, and it is the sharpest of the divergences of the block from its parent.

The article states the definition of the zero divisor relative to the product, proves the criterion that makes the whole punctured space the zero-divisor set, computes the annihilator of an element as an explicit hyperplane, separates the two families the block uses, places the set with respect to the remarkable subspaces, and compares it with the set of the four general products, which is strictly smaller. The block has no regular element apart from $0$; the two-sided annihilator of the product is nevertheless $\{0\}$, because the product is non-degenerate, and the distinction between *the annihilator of an element* and *the annihilator of the product* is the technical heart of the article.

**Boundaries.** The general definition of the zero divisor, of the annihilator and of the regular element is *Definitions for the Study of the 12 Algebraic Structures* §*The Zero Divisor and the Annihilator*; the zero-divisor sets of the four general products are *Zero Divisors of the General Plain Algebra* and *Comparison Between the Four General Products*; the square-zero elements are *Nilpotents of the Symmetric Quaternionic Algebra*; the isotropic cone and its two families are *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the subspaces are *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$ and $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$. The **symmetric quaternionic multiplication** is $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)=N(\tilde P,\tilde Q)e_0$ with $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$, and its diagonal is $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2$; the operation is also written $\bullet$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$, and the Hermitian subspaces are $\mathbb{M}_+$ and $\mathbb{M}_-$.

## The General Definition

**Definition (zero divisor of a product).** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$; a **right zero divisor** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde R\star\tilde Q=0$; a **zero divisor** when it is one or the other; and a **two-sided zero divisor** when it is both. An element of a unital product that is neither a left nor a right zero divisor is **regular**.

Throughout this article the product is the **symmetric quaternionic product** of the block; a zero divisor, an annihilator or a regular element, written without qualification, is one of that product. Since the product is commutative, its left and right notions coincide, and every zero divisor of the block is two-sided; the words are kept nonetheless, because the comparison with the parent uses them.

## The Criterion and the Annihilator

**Theorem (everything nonzero is a zero divisor).** The zero-divisor set of the block is the whole punctured space,

$$
\mathcal{Z}_{\star}=\mathbb{B}\setminus\{0\},
$$

and the block has no regular element apart from $0$.

*Proof.* Let $\tilde Q\neq0$. The form is non-degenerate with radical $\{0\}$ (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*), so there is an $\tilde R$ with $N(\tilde Q,\tilde R)\neq0$. If $N(\tilde Q)=0$ then $\tilde Q\star\tilde Q=N(\tilde Q)e_0=0$, and $\tilde Q$ annihilates itself. If $N(\tilde Q)\neq0$, put

$$
\tilde X=\tilde R-\frac{N(\tilde Q,\tilde R)}{N(\tilde Q)}\,\tilde Q .
$$

Then $N(\tilde Q,\tilde X)=N(\tilde Q,\tilde R)-\frac{N(\tilde Q,\tilde R)}{N(\tilde Q)}N(\tilde Q,\tilde Q)=0$, so $\tilde Q\star\tilde X=0$, and $\tilde X\neq0$ because $N(\tilde Q,\tilde X)=0\neq N(\tilde Q,\tilde R)$. In both cases $\tilde Q$ is a zero divisor. Conversely $0$ is excluded by the definition, and no other element is excluded.

**Corollary (the annihilator is a hyperplane).** For $\tilde Q\neq0$ the left and right annihilators coincide and are

$$
\operatorname{Ann}(\tilde Q)=\{\tilde X: N(\tilde Q,\tilde X)=0\}=\tilde Q^{\perp},
$$

a $\mathbb{C}$-linear hyperplane of complex dimension three and real dimension six; the element $\tilde Q$ belongs to it exactly when $N(\tilde Q)=0$, that is exactly when it is isotropic. The annihilator of the product in the space,

$$
\{\tilde Q:\tilde Q\star\tilde X=0\ \text{for every }\tilde X\}=\{0\},
$$

is zero, and the two annihilators must not be confused: the product is non-degenerate, every element is nonetheless a zero divisor, and the reason is that a non-degenerate form on a space of dimension greater than one always has a nonzero orthogonal for a given nonzero element.

*Proof.* The annihilator is the orthogonal of $\tilde Q$ for $N$, and the orthogonal of a nonzero element of a non-degenerate form is a hyperplane; $\tilde Q\in\tilde Q^{\perp}$ is the equation $N(\tilde Q,\tilde Q)=N(\tilde Q)=0$; the annihilator of the product is the radical of the form, which is $\{0\}$.

**Corollary (the product is a perfect pairing).** The blocked multiplication $\mathbb{B}\times\mathbb{B}\to\mathbb{C}e_0$, $(\tilde P,\tilde Q)\mapsto\tilde P\star\tilde Q$, has rank one in the sense of the image and full rank four in the sense of the pairing: its image is the central line, and its left radical and right radical are both $\{0\}$.

## The Two Families

The set is the whole punctured space, and the block classifies its elements by the two families of the isotropic structure.

**Definition.** The **isotropic family** is the set $\{\tilde Q: N(\tilde Q)=0,\ \tilde Q\neq0\}$; the **non-isotropic family** is its complement in the set, $\{\tilde Q: N(\tilde Q)\neq0\}$.

| the family | the defining equation | the annihilator | the self-product |
|---|---|---|---|
| isotropic | $N(\tilde Q)=0$ | a hyperplane through $\tilde Q$ | $\tilde Q\star\tilde Q=0$ |
| non-isotropic | $N(\tilde Q)\neq0$ | a hyperplane not through $\tilde Q$ | $\tilde Q\star\tilde Q\neq0$, central |

The two families behave differently in the product: an isotropic element annihilates itself and is a nilpotent of index two (*Nilpotents of the Symmetric Quaternionic Algebra*), while a non-isotropic element is annihilated by the hyperplane orthogonal to it and by nothing outside it, and its square is the nonzero central element $N(\tilde Q)e_0$.

**Remark (the other split, and the one the block uses).** A second split suggests itself by analogy with the parent, the split by the scalar part into the elements with $Q_0=0$ and those with $Q_0\neq0$. The two splits are different here, and the block uses the isotropic one. In the parent the pure family *is* the nilpotent family (*Zero Divisors of the General Plain Algebra*); in the block a pure element $\tilde Q=\mathbf Q$ is a zero divisor like every other, but it is square-zero only when it is isotropic, $\tilde Q\star\tilde Q=(\mathbf Q,\mathbf Q)e_0$, and otherwise its square is a nonzero central element. The pure family is therefore not the nilpotent family of the block, and the identification of the two, valid in the parent, fails here.

## The Set and the Remarkable Subspaces

**Proposition (the set and its size).** The zero-divisor set $\mathcal{Z}_{\star}=\mathbb{B}\setminus\{0\}$ is of complex dimension four and real dimension eight; its isotropic part is the punctured cone $\{N=0\}\setminus\{0\}$ of complex dimension three and real dimension six, and its non-isotropic part is the complement of the cone.

**The map to the hyperplanes.** The assignment $\tilde Q\mapsto\operatorname{Ann}(\tilde Q)=\tilde Q^{\perp}$ is a surjection of the punctured space onto the set of hyperplanes of $\mathbb{B}$, with fibres the punctured complex lines, since a non-degenerate form identifies $\mathbb{B}$ with its dual: the family of zero divisors of the block is not a proper subvariety but the space itself, endowed with the map to its hyperplanes.

**The remarkable subspaces.**

| the subspace | the isotropic elements | the zero divisors |
|---|---|---|
| the centre $\mathbb{C}_{\mathbb{B}}$ | none but $0$ | all nonzero: $\lambda e_0\star e_k=0$ for every $k$ |
| the vector subspace $\mathrm{Vect}(\mathbb{B})$ | the cone $(\mathbf Q,\mathbf Q)=0$ | all nonzero |
| the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | none but $0$, the diagonal being definite there | all nonzero |
| the Hermitian subspaces $\mathbb{M}_+$, $\mathbb{M}_-$ | the light cones, of real dimension three | all nonzero |

A nonzero central element annihilates the whole vector subspace, since $\lambda e_0\star\mathbf Q=\lambda\mathbf Q_0e_0=0$; the centre is accordingly contained in the set not merely as a subset but as its most degenerate part. The subspaces and their isotropic cones are *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions* and *Introduction to the Remarkable Subspaces*.

## The Comparison with the Other Products

**Theorem (the four general products share a proper set).** The four general products of the space have one and the same zero-divisor set, the set of elements of vanishing constant term of the characteristic polynomial, equivalently $\{\tilde Q: N(\tilde Q)=0\}\setminus\{0\}$ for the plain product, and it contains no non-isotropic element (*Zero Divisors of the General Plain Algebra*, *Comparison Between the Four General Products*).

**Corollary (the block's set strictly contains the parent's).**

$$
\{N=0\}\setminus\{0\}=\mathcal{Z}_{\tilde P\tilde Q}=\mathcal{Z}_{\tilde P^{\natural}\tilde Q}=\mathcal{Z}_{\tilde P\tilde Q^{*}}=\mathcal{Z}_{\tilde P^{\natural}\tilde Q^{*}}\subsetneq\mathbb{B}\setminus\{0\}=\mathcal{Z}_{\star},
$$

the inclusion being strict. The witness of the strictness is the element $e_0$: it is a unit of the plain product, hence not a zero divisor of it, and it is a zero divisor of the block, because $e_0\star e_1=0$ with $e_1\neq0$. The difference is thus not a borderline effect but the statement that the block has no regular element at all.

**The other halves, for the record.** The block is not alone in the maximal case: six of the twelve structures have the whole punctured space as their zero-divisor set. The two antisymmetrisations of the algebra family, $\mathrm{APA}$ and $\mathrm{AQA}$, are alternating, $\tilde X\star\tilde X=0$ for the operation of the row, so every nonzero element is a zero divisor of them. The two sesquilinear partners $\mathrm{APS}$ and $\mathrm{AQS}$ are maximal for an explicit witness for every nonzero $\tilde P$: the element $\tilde Q=\overline{\tilde P}$ gives $\tilde P\tilde Q^{*}=\tilde P\tilde P^{\natural}=N(\tilde P)e_0$ for $\mathrm{APS}$, and the element $\tilde Q=\tilde P^{*}$ gives $\tilde P^{\natural}\tilde Q^{*}=\tilde P^{\natural}\tilde P=N(\tilde P)e_0$ for $\mathrm{AQS}$, both values central, which the vector-part reading of $\mathrm{APS}$ and of $\mathrm{AQS}$ sends to $0$; and the two central-valued operations, the block and the symmetric plain sesquilinear product $\mathrm{SPS}$, whose value is $H(\tilde P,\tilde Q)e_0$ with $H$ non-degenerate, are maximal by the argument of §*The Criterion*. The other six hold a proper set: the four general products share $\{N=0\}\setminus\{0\}$, the symmetric plain product has $e_0$ regular, since $\tilde P\bullet e_0=\tilde P$ never vanishes for $\tilde P\neq0$, and the symmetric quaternionic sesquilinear product, whose value carries a vector part, is read in its own article. The reading structure by structure is *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the exact column of the definitions is *Definitions for the Study of the 12 Algebraic Structures* §*The Dictionary: The Classes and the Four General Products*.

## Summary

Relative to the symmetric quaternionic product, an element is a zero divisor exactly when it is nonzero: $\mathcal{Z}_{\star}=\mathbb{B}\setminus\{0\}$, and the block has no regular element apart from $0$. The criterion is the non-degeneracy of the form $N$: for $\tilde Q\neq0$ the element $\tilde X=\tilde R-\frac{N(\tilde Q,\tilde R)}{N(\tilde Q)}\tilde Q$, or $\tilde X=\tilde Q$ when $N(\tilde Q)=0$, is a nonzero annihilator. The annihilator of a nonzero element is the hyperplane $\tilde Q^{\perp}$ of complex dimension three, the element lies in its own annihilator exactly when it is isotropic, and the annihilator of the product is $\{0\}$ because the form has no radical; the product is a perfect pairing with image the central line. The two families are the isotropic one, $N=0$, whose elements are square-zero and which is the block's second family of nilpotents, and the non-isotropic one, $N\neq0$; the split by the scalar part, valid in the parent, is not the split the block uses. The four general products share the proper set $\{N=0\}\setminus\{0\}$, which the block's set strictly contains, the witness of the strictness being the unit $e_0$ of the parent, which is a zero divisor of the block; the block is not the only one of the twelve in the maximal case, the antisymmetrisations of the algebra family and the sesquilinear partners $\mathrm{APS}$ and $\mathrm{AQS}$ being maximal too, and the symmetric plain product is not among them.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | the form of the block |
| $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$ | the diagonal of the form, the norm of the parent |
| $\mathcal{Z}_{\star}=\mathbb{B}\setminus\{0\}$ | the zero-divisor set of the block |
| $\operatorname{Ann}(\tilde Q)=\tilde Q^{\perp}$ | the two-sided annihilator of a nonzero element, a hyperplane |
| $N=0$, $N\neq0$ | the isotropic family, the non-isotropic family |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of the zero divisor, the annihilator and the regular element.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the zero-divisor set of the parent and its two families.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the coincidence of the four sets.
- *Norm and Invertibility in the Symmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-algebra.md`), for the form, its non-degeneracy and the non-isotropic class.
- *Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-symmetric-quaternionic-algebra.md`), for the isotropic family as the square-zero elements.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the radical of the product and the isotropic cone.
- *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the isotropic elements of the subspaces.
