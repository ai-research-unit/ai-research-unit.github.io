# __Zero Divisors of the Antisymmetric Plain Algebra__

## Introduction

The zero divisor is defined by an equation in which the product occurs, so it is a class of the
product and not of the space (*Definitions for the Study of the 12 Algebraic Structures*, §*The
Zero Divisor and the Annihilator*). The block of this article is the antisymmetric plain
multiplication
$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
$$
the cross product of the two vector parts; it is $\mathbb{C}$-bilinear, alternating, vector valued
and without a unit (*Introduction to the Antisymmetric Plain Algebra of Biquaternions*). The
article determines its zero-divisor set in full and compares the set with the sets of the
neighbouring products.

The answer is total and it is not the answer of the general products. Since the block is
**alternating**, $\tilde X\wedge\tilde X=0$ for every $\tilde X$, and an element may therefore be
annihilated by itself: **every nonzero element of $\mathbb{B}$ is a two-sided zero divisor of the
block**, with itself as the annihilating partner. The zero-divisor set of the block is the whole
punctured space $\mathbb{B}\setminus\{0\}$, strictly larger than the set of the four general
products, which is the zero set of the central square; and it coincides with the zero-divisor set
of $\mathrm{AQA}$, the only other alternating structure of the twelve. The classification into a
pure and a non-pure family, which the general products carry, degenerates here: the criterion is
met by every element and the two families merge. What the block keeps in place of that
classification is a dichotomy of the **annihilator**, read from the vector part, and it is
*Annihilators of the Antisymmetric Plain Algebra*, below this article in this category. Which pairs
of elements bracket to zero is owned by the remarkable-subspaces article of the block, and the
alternation itself by the introduction; both are cited.

**The results.** The zero divisor of the antisymmetric plain multiplication $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ is total: because the block is alternating, every nonzero element is a two-sided zero divisor with itself as annihilating partner, and the zero-divisor set is the punctured space $\mathbb{B}\setminus\{0\}$. It strictly contains the zero-divisor set $\{C(\tilde Q)=0\}\setminus\{0\}$ common to the four general products, the witness being $e_0$; among the twelve structures the punctured space is attained by exactly six. The pure and non-pure classification of the parent does not exist for the block, the criterion being met by both families alike, and what replaces it is the annihilator's dichotomy by the vector part.

## The Notion and Its Product

**Definition (zero divisor of a product).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when
$\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$; a **right zero
divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with
$\tilde R\star\tilde Q=0$; a **zero divisor of $\star$** when it is one or the other; and a
**two-sided zero divisor of $\star$** when it is both.

The set of partners of $\tilde Q$ is its **annihilator**, whose two sides, whose matrix and whose
rank are the companion article's (*Annihilators of the Antisymmetric Plain Algebra*, below this
article in this category).

Throughout this article the product is the **antisymmetric plain multiplication** $\wedge$, and
unqualified, *zero divisor* means the zero divisor of $\wedge$. The product is the antisymmetric
half of the general plain bilinear product $\tilde P\tilde Q$ (*The Symmetric and Antisymmetric
Parts of an Algebra Product*), and the zero divisors of the parent are *Zero Divisors of the
General Plain Algebra*; the two sets are compared at §*The Set and the Comparison*.

## The Criterion

**Every nonzero element of $\mathbb{B}$ is a two-sided zero divisor of the block, so the zero-divisor set is the punctured space $\mathbb{B}\setminus\{0\}$.**

**Theorem (the criterion for the block).** Every nonzero element of $\mathbb{B}$ is a two-sided
zero divisor of the antisymmetric plain multiplication; equivalently, the zero-divisor set of the
block is the punctured space
$$
\{\tilde Q\in\mathbb{B}:\tilde Q\text{ a zero divisor of }\wedge\}=\mathbb{B}\setminus\{0\}.
$$

*Proof.* The block is alternating, $\tilde X\wedge\tilde X=0$ for every $\tilde X$, by
*Introduction to the Antisymmetric Plain Algebra of Biquaternions*. Given a nonzero $\tilde Q$, the
element $\tilde R=\tilde Q$ is nonzero and it annihilates $\tilde Q$ on the left,
$\tilde Q\wedge\tilde R=\tilde Q\wedge\tilde Q=0$, so $\tilde Q$ is a left zero divisor of the
block; and it satisfies $\tilde R\wedge\tilde Q=\tilde Q\wedge\tilde Q=0$, so it is a right zero
divisor as well. The origin is excluded by the definition, its partner being required to be
nonzero.

The criterion is therefore the alternation of the product read as an element statement, and it is
met by **every** nonzero element. The element $\tilde Q$ is its own annihilating partner, so the
line $\mathbb{C}\tilde Q$ always lies in its annihilator on both sides.

## The Classification Collapses

**The pure and non-pure classification of the parent does not exist for the block: both the elements with a nonzero scalar part and the pure elements are zero divisors.**

The general plain product comes with a classification of its zero divisors into two families, the
pure and the non-pure, split by the vanishing of the scalar part $Q_0$ (*Zero Divisors of the
General Plain Algebra*, §*The Two Families of Zero Divisors*). That classification rests on the two
terms of the parent's square, $\tilde Q^{2}=[Q_0^{2}-(\mathbf Q,\mathbf Q)]e_0+2Q_0\mathbf Q$, the
central term and the vector term, both read from the scalar part. For the block it does not exist.

**Proposition (the classification of the zero divisors collapses).** For the block the criterion of
the zero divisor is met on the whole punctured space and not on the central-square cone alone; both
the elements with a nonzero scalar part and the pure elements are zero divisors, and the division
of the parent into a pure and a non-pure family does not exist for the zero-divisor criterion.

*Proof.* The criterion is the theorem of §*The Criterion*, which holds for every nonzero element
and mentions neither the scalar part nor the vector part; the pure elements $\tilde P=\mathbf P$
and the non-pure elements $\tilde P=P_0e_0+\mathbf P$ with $P_0\neq0$ satisfy it in the same way.

The collapse of the zero-divisor classification is the removal of the scalar part in the sharpest
form. In the block the square is a pure vector and vanishes for every element,
$\tilde Q\wedge\tilde Q=0$, so neither term that separated the parent's families survives, and the
equation of the zero divisor carries no classification at all. What replaces it is the annihilator
of the element, whose dichotomy is read from the vector part where the parent's is read from the
scalar part (*Annihilators of the Antisymmetric Plain Algebra*, §*The Dichotomy by the Vector
Part*).

## The Set and the Comparison

**The zero-divisor set of the block, the punctured space, strictly contains the zero-divisor set $\{\tilde Q\neq0:C(\tilde Q)=0\}$ of each of the four general products, and among the twelve structures the punctured space is attained by exactly six.**

The four general products give four definitions of the zero divisor, and for the biquaternion space
the four definitions select one and the same set,
$$
\{\tilde Q\neq0:\ C(\tilde Q)=0\},\qquad C(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2},
$$
a theorem about the algebra and not a property of the definitions (**Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space**, §*The Four General Products Coincide*). The set of the block differs from it,
and the difference is the content of the comparison.

**Proposition (the comparison).** The zero-divisor set of the block is the punctured space
$\mathbb{B}\setminus\{0\}$, and the zero-divisor set of each of the four general products is the
proper subset $\{\tilde Q\neq0:C(\tilde Q)=0\}$. The block's set strictly contains every one of
them, the witness being $e_0$, and it is as large as a zero-divisor set can be. Among the twelve
the punctured space occurs exactly for the six structures in which every nonzero element has a
nonzero annihilating partner: the two alternating products, the block and $\mathrm{AQA}$; the two
antisymmetric sesquilinear halves, $\mathrm{APS}$ and $\mathrm{AQS}$, whose elements are
annihilated by their conjugates $\overline{\tilde X}$; and the two symmetric halves whose value is
the central reading of a non-degenerate form, $\mathrm{SQA}$ and $\mathrm{SPS}$.

*Proof.* The block's set is the theorem of §*The Criterion*. The set of the four general products
is the cited theorem, and $C$ vanishes at $0$ and on a cone that is not the whole space, so the
inclusion is strict: the element $e_0$ has $c(e_0)=1$ and is a zero divisor of the block, with
partner itself, while it is not a zero divisor of the general products. For the six, the partners
are displayed. An element of the block or of $\mathrm{AQA}$ is annihilated by itself, the two
products being alternating. An element of $\mathrm{APS}$ or of $\mathrm{AQS}$ is annihilated by its
conjugate $\overline{\tilde X}$, since $\tilde X\star\overline{\tilde X}=0$ in the two. In
$\mathrm{SQA}$ and $\mathrm{SPS}$ the value is $N(\tilde X,\tilde Y)e_0$ and
$H(\tilde X,\tilde Y)e_0$ with $N$ and $H$ non-degenerate, so at a nonzero $\tilde X$ the
annihilating equation is a single nontrivial condition on $\tilde Y$, linear for $N$ and
conjugate-linear for $H$, and it has a nonzero solution. For the other six, $e_0$ has an injective
left multiplication: $e_0\star\tilde Y$ is $\tilde Y$ in $\mathrm{GPA}$, $\mathrm{GQA}$ and
$\mathrm{SPA}$ and the star of $\tilde Y$ in $\mathrm{GPS}$, $\mathrm{GQS}$ and $\mathrm{SQS}$, and
it vanishes only at $\tilde Y=0$; the element $e_0$ is therefore not a zero divisor of those six,
and their sets are strictly smaller than the punctured space.

The punctured space is therefore not the block's alone. It is the largest a zero-divisor class can
be, and the six structures above attain it, each by the pairing its own product carries: the
element itself for the two alternating products, the conjugate for the two antisymmetric
sesquilinear halves, and the solution of one linear equation for the two symmetric halves. The
difference from the four general products, on the other hand, is the whole content of the question
of the block: the block is not a product whose square is central, and the zero-divisor criterion of
the algebra is not its criterion.

## The Relation to the Remarkable Subspaces

**On each remarkable subspace the restriction of the block is again alternating, so every nonzero element of the subspace is a zero divisor with itself as partner.**

**Proposition (the restriction).** On each of the remarkable subspaces the block restricts to an
operation whose zero-divisor class is the same relative class: the nonzero elements of the centre
are zero divisors with themselves as partners, and likewise on the vector subspace, the quaternion
subspace, the anti-quaternion subspace and the two Hermitian subspaces.

*Proof.* On each subspace the restriction of the block is again alternating, the square of each of
its elements vanishing as the square of an element of the ambient algebra vanishes; the criterion
of §*The Criterion* is therefore met by every nonzero element of the subspace, and the partner is
the element itself.

The subspaces differ in the annihilator rather than in the zero-divisor class: on the centre the
operation vanishes identically and an annihilator is the whole space, whereas on the vector
subspace the annihilator of a nonzero vector is a plane of the ambient space. That reading, and the
elements whose bracket vanishes, are *Annihilators of the Antisymmetric Plain Algebra* and
*Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions*.

## Summary

For the antisymmetric plain multiplication $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ the
zero-divisor class is total: every nonzero element is a two-sided zero divisor, with itself as the
annihilating partner, because the block is alternating and the square of each element vanishes. The
zero-divisor set is the punctured space $\mathbb{B}\setminus\{0\}$, and it strictly contains the
common zero-divisor set $\{C(\tilde Q)=0\}\setminus\{0\}$ of the four general products; among the
twelve the same punctured space is attained by exactly six structures, the block, its alternating
sibling $\mathrm{AQA}$, the two antisymmetric sesquilinear halves and the two symmetric halves
whose value is the central reading of a non-degenerate form. The classification of the zero
divisors into two families, which the general products carry, does not exist for the block, the
criterion being met by the pure and the non-pure elements alike; what survives is the annihilator's
dichotomy, read from the vector part where the parent's is read from the scalar part, and it is
*Annihilators of the Antisymmetric Plain Algebra*. The annihilator itself, its rank and its shape
on the remarkable subspaces are that article's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the zero-divisor criterion of the four general products |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, on which the block is the cross product |
| $e_0$ | a zero divisor of the block, with partner itself, and not a zero divisor of the four general products |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the zero divisor and the annihilator of a general product and for the relativity of the definition
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *Annihilators of the Antisymmetric Plain Algebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-algebra.md`), below this article in this category, the companion article, for the annihilator of an element, the rank of the multiplication operator and the dichotomy by the vector part
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the coincidence of the four zero-divisor sets and the product-dependent annihilators
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the criterion, the two families and the structure of the zero divisors of the plain product
- *Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the elements whose bracket vanishes and for the reading on the subspaces
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), the sibling of this article, whose operator has the central-square cone of its parent as the locus of its rank drop
