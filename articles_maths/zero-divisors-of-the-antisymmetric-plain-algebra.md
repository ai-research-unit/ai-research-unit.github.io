# __Zero Divisors of the Antisymmetric Plain Algebra__

## Introduction

The zero divisor is defined by an equation in which the product occurs, so it is a class of the
product and not of the space (*Definitions for the Study of the 12 Algebraic Structures*,
§*The Zero Divisor and the Annihilator*). The block of this article is the antisymmetric plain
multiplication
$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
$$
the cross product of the two vector parts; it is $\mathbb{C}$-bilinear, alternating, vector
valued and without a unit (*Introduction to the Antisymmetric Plain Algebra of Biquaternions*).
The article determines its zero-divisor set in full and compares the set with the sets of the
neighbouring products.

The answer is total and it is not the answer of the general products. Since the block is
**alternating**, $\tilde X\wedge\tilde X=0$ for every $\tilde X$, and an element may therefore be
annihilated by itself: **every nonzero element of $\mathbb{B}$ is a two-sided zero divisor of the
block**, with itself as the annihilating partner. The zero-divisor set of the block is the whole
punctured space $\mathbb{B}\setminus\{0\}$, strictly larger than the set of the four general
products, which is the zero set of the central square; and it coincides with the zero-divisor set
of $\mathrm{AQA}$, the only other alternating structure of the twelve. The classification into a
pure and a non-pure family, which the general products carry, degenerates here: the criterion is
met by every element and the two families merge. The annihilator is not degenerate in the same
way: it is the kernel of the left multiplication operator, of dimension two on the non-central
elements and four on the central line, and on the non-central elements it is always the same
shape, the plane spanned by the centre and the element's own vector part. Which pairs of elements
bracket to zero is owned by the remarkable-subspaces article of the block, and the alternation
itself by the introduction; both are cited.

## The Notion and Its Product

**Definition (zero divisor of a product).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when
$\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$; a **right zero
divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with
$\tilde R\star\tilde Q=0$; a **zero divisor of $\star$** when it is one or the other; and a
**two-sided zero divisor of $\star$** when it is both.

**Definition (annihilator).** The **left annihilator** and the **right annihilator** of
$\tilde Q$ in $\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$

Throughout this article the product is the **antisymmetric plain multiplication** $\wedge$, and
unqualified, *zero divisor* and *annihilator* mean the zero divisor and the annihilator of
$\wedge$. The product is the antisymmetric half of the general plain bilinear product
$\tilde P\tilde Q$ (*The Symmetric and Antisymmetric Parts of an Algebra Product*), and the zero
divisors of the parent are *Zero Divisors of the General Plain Algebra*; the two sets are
compared at §*The Set and the Comparison*.

## The Criterion

**Theorem (the criterion for the block).** Every nonzero element of $\mathbb{B}$ is a two-sided
zero divisor of the antisymmetric plain multiplication; equivalently, the zero-divisor set of the
block is the punctured space
$$
\{\tilde Q\in\mathbb{B}:\tilde Q\text{ a zero divisor of }\wedge\}=\mathbb{B}\setminus\{0\}.
$$

*Proof.* The block is alternating, $\tilde X\wedge\tilde X=0$ for every $\tilde X$, by
*Introduction to the Antisymmetric Plain Algebra of Biquaternions*. Given a nonzero $\tilde Q$,
the element $\tilde R=\tilde Q$ is nonzero and it annihilates $\tilde Q$ on the left,
$\tilde Q\wedge\tilde R=\tilde Q\wedge\tilde Q=0$, so $\tilde Q$ is a left zero divisor of the
block; and it satisfies
$\tilde R\wedge\tilde Q=\tilde Q\wedge\tilde Q=0$, so it is a right zero divisor as well. The
origin is excluded by the definition, its partner being required to be nonzero.

The criterion is therefore the alternation of the product read as an element statement, and it is
met by **every** nonzero element. The element $\tilde Q$ is its own annihilating partner, and the
line $\mathbb{C}\tilde Q$ always lies in the annihilator of $\tilde Q$ on both sides.

## The Annihilator and the Rank

The annihilator of $\tilde Q$ is the kernel of a left or a right multiplication, and for an
alternating product the two multiplications are the negatives of one another, so the two
annihilators coincide.

**Proposition (the two annihilators coincide).** For every $\tilde P$,
$$
B_\wedge(\tilde P)=A_\wedge(\tilde P)=\ker L_{\tilde P},\qquad
L_{\tilde P}\tilde X=\tilde P\wedge\tilde X .
$$

*Proof.* Alternation gives $\tilde X\wedge\tilde P=-\tilde P\wedge\tilde X$, so
$\tilde X\wedge\tilde P=0$ exactly when $\tilde P\wedge\tilde X=0$; the two annihilators are
therefore one set, the kernel of $L_{\tilde P}$.

**Proposition (the operator and its characteristic polynomial).** In the basis
$e_0,e_1,e_2,e_3$ the operator $L_{\tilde P}$ of an element $\tilde P=P_0e_0+\mathbf P$ has
matrix
$$
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & -P_3 & P_2 \\
0 & P_3 & 0 & -P_1 \\
0 & -P_2 & P_1 & 0
\end{pmatrix},
$$
its trace is $0$, its determinant is $0$, and its characteristic polynomial is
$$
\chi_{L_{\tilde P}}(t)=t^{2}\bigl(t^{2}+(\mathbf P,\mathbf P)\bigr),\qquad
(\mathbf P,\mathbf P)=\sum_{k=1}^{3}P_k^{2} .
$$
The eigenvalues are $0$ with multiplicity two and the two roots of $t^{2}+(\mathbf P,\mathbf P)$;
the operator is never invertible, and it vanishes exactly on the central line, where
$\mathbf P=0$.

*Proof.* The first column is zero because the scalar direction of $\tilde P$ is invisible and
$e_0$ has zero vector part, $\tilde P\wedge e_0=\mathbf P\times\mathbf{0}=0$; the remaining three
columns are $\tilde P\wedge e_k=\mathbf P\times\mathbf{e}_k$, whose coordinates are the columns of
the cross-product matrix $C_{\mathbf P}$, the skew matrix displayed. The matrix is therefore
$\operatorname{diag}(0,C_{\mathbf P})$, of trace $0$ because $C_{\mathbf P}$ is skew, and of
determinant $0$ because the first row is zero. The characteristic polynomial of the skew matrix
$C_{\mathbf P}$ is $t^{3}+(\mathbf P,\mathbf P)t$, since its eigenvalues are $0$ and $\pm is$ with
$s^{2}=(\mathbf P,\mathbf P)$, and the extra zero of the scalar direction gives the displayed
fourth-degree polynomial. The operator vanishes exactly when $C_{\mathbf P}=0$, that is when
$\mathbf P=0$, the scalar coordinate being invisible. Computed exactly on general elements of
$\mathbb{Q}(i)$ coefficients and on the units.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde P}$ and the annihilator of
$\tilde P$ depend only on the vector part $\mathbf P$, and there are two cases,

| $\mathbf P$ | $\operatorname{rank}L_{\tilde P}$ | $\dim\ker L_{\tilde P}$ | $\ker L_{\tilde P}$ |
|---|---|---|---|
| $0$ | $0$ | $4$ | $\mathbb{B}$ |
| $\mathbf P\neq0$ | $2$ | $2$ | $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\mathbf P$ |

*Proof.* The cross-product matrix $C_{\mathbf P}$ of a nonzero vector $\mathbf P$ has rank two,
whatever the value of $(\mathbf P,\mathbf P)$: a skew matrix of odd size is singular, its rank is
even, and it is not zero, so its rank is two. The matrix of $L_{\tilde P}$ is
$\operatorname{diag}(0,C_{\mathbf P})$, of the same rank two, and its kernel is the direct sum of
the kernel $\mathbb{C}e_0$ of the scalar direction and the kernel of $C_{\mathbf P}$, which is
$\mathbb{C}\mathbf P$ because $\mathbf P\times\mathbf X=0$ if and only if $\mathbf X$ is parallel
to $\mathbf P$. At $\mathbf P=0$ the operator is zero and the kernel is the whole space. The
ancillary verification confirms the kernel equal to the span on random non-central elements.

**Remark (no rank drop on the isotropic locus).** On the non-central elements the rank of the
operator is two, so the annihilator is the same two-dimensional plane for all of them. The
isotropic locus of the vector form, $(\mathbf P,\mathbf P)=0$, does not change the rank; it only
merges the two nonzero eigenvalues $\pm is$ into the double zero. This is a difference from the
quaternionic sibling of the block, whose rank drops on the zero-divisor cone of its parent; here
the rank is constant on the complement of the central line.

**Remark (the rank drops on the central line).** The rank does drop, and it drops on the centre:
an element $\tilde P=P_0e_0$ has $\mathbf P=0$, so $L_{\tilde P}=0$, of rank zero, and its
annihilator is the whole space. The nonzero central elements are therefore left and right
annihilators of every element of the block, $\tilde P\wedge\tilde X=0$ and
$\tilde X\wedge\tilde P=0$ for all $\tilde X$; they are the elements whose annihilator is
everything. The annihilator thus separates two classes, the central elements, annihilated by the
whole space, and the non-central elements, whose annihilator is the plane
$\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\mathbf P$. An element of the vector subspace,
$\tilde P=\mathbf P\neq0$, lies in the second class, with annihilator
$\mathbb{C}e_0\oplus\mathbb{C}\mathbf P$.

## The Two Classes of the Annihilator

The general plain product comes with a classification of its zero divisors into two families, the
pure and the non-pure, split by the vanishing of the scalar part $Q_0$
(*Zero Divisors of the General Plain Algebra*, §*The Two Families of Zero Divisors*). For the
block the classification of the **zero divisors** collapses, and the classification the
annihilator carries is the transpose of the parent's.

**Proposition (the classification of the zero divisors collapses).** For the block the criterion
of the zero divisor is met on the whole punctured space and not on the central-square cone alone;
both the elements with a nonzero scalar part and the pure elements are zero divisors, and the
division of the parent into a pure and a non-pure family does not exist for the zero-divisor
criterion.

*Proof.* The criterion is the theorem of §*The Criterion*, which holds for every nonzero element
and mentions neither the scalar part nor the vector part; the pure elements $\tilde P=\mathbf P$
and the non-pure elements $\tilde P=P_0e_0+\mathbf P$ with $P_0\neq0$ satisfy it in the same way.

**Proposition (the classification of the annihilator is by the vector part).** The annihilator
does separate a dichotomy, and it is the dichotomy of the vector part: an element with
$\mathbf P=0$ has annihilator the whole space, and an element with $\mathbf P\neq0$ has annihilator
the plane $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\mathbf P$. The parent's dichotomy is by the
scalar part, so the block's is its transpose.

*Proof.* Both statements are the rank computation of §*The Annihilator and the Rank*; the parent's
dichotomy by the scalar part is the cited section.

The collapse of the zero-divisor classification is the removal of the scalar part in the sharpest
form. In the parent plain product the square of an element is
$\tilde Q^{2}=[Q_0^{2}-(\mathbf Q,\mathbf Q)]e_0+2Q_0\mathbf Q$, the zero divisor is the vanishing
of the central square and the two families are read from the scalar part; in the block the square
is a pure vector and vanishes for every element, so the equation of the zero divisor is satisfied
identically and the classification it used to carry is gone. What survives is the annihilator's
dichotomy, and it is read from the vector part instead.

## The Set and the Comparison

The four general products give four definitions of the zero divisor, and for the biquaternion
space the four definitions select one and the same set,
$$
\{\tilde Q\neq0:\ C(\tilde Q)=0\},\qquad C(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2},
$$
a theorem about the algebra and not a property of the definitions (*The Zero Divisors and the Twelve Structures*, §*The Four Zero-Divisor Sets Coincide*). The set of the block differs from it,
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
products being alternating. An element of $\mathrm{APS}$ or of $\mathrm{AQS}$ is annihilated by
its conjugate $\overline{\tilde X}$, since $\tilde X\star\overline{\tilde X}=0$ in the two. In
$\mathrm{SQA}$ and $\mathrm{SPS}$ the value is $N(\tilde X,\tilde Y)e_0$ and
$H(\tilde X,\tilde Y)e_0$ with $N$ and $H$ non-degenerate, so at a nonzero $\tilde X$ the
annihilating equation is a single nontrivial condition on $\tilde Y$, linear for $N$ and
conjugate-linear for $H$, and it has a nonzero solution. For the other six, $e_0$ has an injective
left multiplication: $e_0\star\tilde Y$ is $\tilde Y$ in $\mathrm{GPA}$, $\mathrm{GQA}$ and
$\mathrm{SPA}$ and the star of $\tilde Y$ in $\mathrm{GPS}$, $\mathrm{GQS}$ and $\mathrm{SQS}$,
and it vanishes only at $\tilde Y=0$; the element $e_0$ is therefore not a zero divisor of those
six, and their sets are strictly smaller than the punctured space.

The punctured space is therefore not the block's alone. It is the largest a zero-divisor class can
be, and the six structures above attain it, each by the pairing its own product carries: the
element itself for the two alternating products, the conjugate for the two antisymmetric
sesquilinear halves, and the solution of one linear equation for the two symmetric halves. The
difference from the four general products, on the other hand, is the whole content of the question
of the block: the block is not a product whose square is central, and the zero-divisor criterion
of the algebra is not its criterion.

## The Relation to the Remarkable Subspaces

**Proposition (the restriction).** On each of the remarkable subspaces the block restricts to an
operation whose zero-divisor class is the same relative class: the nonzero elements of the centre
are zero divisors with themselves as partners, and likewise on the vector subspace, the quaternion
subspace, the anti-quaternion subspace and the two Hermitian subspaces.

*Proof.* On each subspace the restriction of the block is again alternating, the square of each of
its elements vanishing as the square of an element of the ambient algebra vanishes; the criterion
of §*The Criterion* is therefore met by every nonzero element of the subspace, and the partner is
the element itself.

The subspaces differ in the annihilator, and the difference is the shape of the kernel. On the
centre the operation vanishes identically, so the annihilator of a nonzero central element is the
whole space and the operation is the zero operation; on the vector subspace, where the operation
is the cross product on $\mathbb{C}^{3}$, the annihilator of a nonzero vector meets the vector
subspace in the line through it and is the plane $\mathbb{C}e_0\oplus\mathbb{C}\mathbf P$ of the
ambient space. The reading of the operation on the six subspaces, and the elements whose bracket
vanishes, are *Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions*.

## Summary

For the antisymmetric plain multiplication $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$
the zero-divisor class is total: every nonzero element is a two-sided zero divisor, with itself as
the annihilating partner, because the block is alternating and the square of each element
vanishes. The zero-divisor set is the punctured space $\mathbb{B}\setminus\{0\}$, and it strictly
contains the common zero-divisor set $\{C(\tilde Q)=0\}\setminus\{0\}$ of the four general
products; among the twelve the same punctured space is attained by exactly six structures, the
block, its alternating sibling $\mathrm{AQA}$, the two antisymmetric sesquilinear halves and the
two symmetric halves whose value is the central reading of a non-degenerate form. The annihilators
of the two sides coincide and are the kernel of the left multiplication operator, whose matrix is
$\operatorname{diag}(0,C_{\mathbf P})$ and whose
characteristic polynomial is $t^{2}(t^{2}+(\mathbf P,\mathbf P))$; its rank is two on the
non-central elements, so their annihilator is the plane
$\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\mathbf P$, and it is zero on the central line, so the
nonzero central elements annihilate the whole block. The classification of the zero divisors into
two families, which the general products carry, does not exist for the block, the criterion being
met by the pure and the non-pure elements alike; the dichotomy that survives is the annihilator's,
and it is read from the vector part where the parent's is read from the scalar part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $A_\wedge(\tilde P),B_\wedge(\tilde P)$ | the left and the right annihilator of $\tilde P$ in the block, equal because the block is alternating |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=\tilde P\wedge\tilde X$ |
| $C_{\mathbf P}$ | the $3\times3$ skew matrix of the cross product $\mathbf X\mapsto\mathbf P\times\mathbf X$, so that the matrix of $L_{\tilde P}$ is $\operatorname{diag}(0,C_{\mathbf P})$ |
| $\chi_{L_{\tilde P}}(t)=t^{2}(t^{2}+(\mathbf P,\mathbf P))$ | the characteristic polynomial of the operator |
| $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\mathbf P$ | the annihilator of a non-central element $\tilde P$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the central line, on which the operator vanishes and the annihilator is the whole space |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the zero-divisor criterion of the four general products |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, on which the block is the cross product |
| $e_0$ | a zero divisor of the block, with partner itself, and not a zero divisor of the four general products |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the zero divisor and the annihilator of a general product and for the relativity of the definition
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *The Zero Divisors and the Twelve Structures* (`articles_maths/the-zero-divisors-and-the-twelve-structures.md`), for the coincidence of the four zero-divisor sets and the product-dependent annihilators
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the criterion, the two families and the structure of the zero divisors of the plain product
- *Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the elements whose bracket vanishes and for the reading on the subspaces
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), the sibling of this article, whose operator has the central-square cone of its parent as the locus of its rank drop
