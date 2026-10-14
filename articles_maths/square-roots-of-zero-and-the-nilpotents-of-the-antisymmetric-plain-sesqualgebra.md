# __Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra__

## Introduction

A root of a central value is defined by an equation in which the product occurs, so it belongs to the product (*Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*). The block of this article is the antisymmetric plain sesquilinear product

$$
\tilde P\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)
=-P_0\overline{\vec Q}+\overline{Q_0}\vec P-\vec P\times\overline{\vec Q},
$$

the antisymmetric half of the general plain sesquilinear product, a product conjugate-linear in its second slot and without a unit (*Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*).

The article treats two subjects, and in this order. The first is the square roots of the central value $0$, the nonzero elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi\diamond\tilde\Xi=0 .
$$

The second is the nilpotents of the block, the elements $\tilde\Upsilon$ some power of which vanishes. The two subjects are one subject: the roots of $0$ are the square-zero elements, and the nonzero ones are exactly the nilpotents of index two. The reduction that produces all of it is one condition, the centrality of the plain product $\tilde\Xi\tilde\Xi^{*}$.

The outcome has two parts. The **roots of $0$** are the nonzero elements whose plain product with their star is central, $\tilde P\tilde P^{*}\in\mathbb{C}_{\mathbb{B}}$; they form the complex cone on the real unit sphere of the quaternion subspace, of real dimension five, and the block is the antisymmetric structure whose root of $0$ is neither the whole space nor the empty set but this quadric. The **index is two**: a vanishing left-nested cube forces a vanishing square, so the nilpotents are exactly the square-zero elements and there is no element of index greater than two. Every nilpotent is a two-sided zero divisor that annihilates itself, but the nilpotents are a thin subcone of the zero divisors, which are the whole space without the origin; the star and the natural conjugation both preserve the square-zero set.

The article is algebraic. It does not treat the roots of $+1$ and the idempotents, which are *Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra*; the square roots of a general right side, which is *Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra*; or the zero-divisor set in full, which is *Zero Divisors of the Antisymmetric Plain Sesqualgebra*.

**The results.** For the block $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ the roots of $0$ are exactly the nonzero square-zero elements, the elements with $\tilde P\tilde P^{*}\in\mathbb{C}_{\mathbb{B}}$; they form the complex cone on the real unit sphere of the quaternion subspace, of real dimension five, and they contain the centre, the real quaternion subspace and the anti-quaternion subspace. The **index is two**, the left-nested cube vanishing only when the square does, so the nilpotents are exactly the square-zero elements. The zero divisors are the whole punctured space and the nilpotents are a thin cone inside them; the star and the natural conjugation preserve the class, and on the Hermitian elements the square-zero ones are the real scalars and the purely imaginary vectors alone.

## The Notion and Its Product

**Definition (root of a central value).** Let $\star$ be a product on $\mathbb{B}$ and let $\lambda\in\mathbb{C}$. A **root of $\lambda$ in $\star$** is a nonzero element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 .
$$

The three central values the biquaternion algebra singles out are $-1$, $+1$ and $0$: the roots of $-1$ are the imaginary units, the roots of $+1$ are the involutions, and the roots of $0$ are the nonzero nilpotents of the product (*Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*).

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Upsilon$ is **nilpotent of $\star$** when some power of it vanishes,

$$
\tilde\Upsilon^{\star k}=0\quad\text{for some }k\geq1,
$$

the power being the **left-nested reading** $\tilde\Upsilon^{\star k}=\bigl(\cdots\bigl((\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon\bigr)\cdots\star\tilde\Upsilon\bigr)$ when $\star$ is not associative; the least such $k$ is the **index of nilpotency**, and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, is a **square-zero element of $\star$**. The origin is the trivial nilpotent, and the article is concerned with the others (*Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*).

Throughout this article the product is the **block** $\diamond$, and unqualified, *root* means a root in $\diamond$, *nilpotent* means a nilpotent of $\diamond$ and *power* is read in $\diamond$. The block is not associative, so the bracketing of a power is specified and the left-nested reading is taken; the square is bracketing-free, and with it the square-zero element, since the equation $\tilde\Upsilon\diamond\tilde\Upsilon=0$ involves one product and no choice of bracketing. The index-two theorem below says that for the block no higher power vanishes without a vanishing square, so the choice of bracketing does not matter for the nilpotent class.

## The Root of Zero

**The roots of $0$ are exactly the nonzero elements with $\tilde\Xi\tilde\Xi^{*}$ central**, the nonzero square-zero elements, and they form the complex cone on the real unit sphere of the quaternion subspace, of real dimension five, containing the centre, the real quaternion subspace and the anti-quaternion subspace.

**Theorem (the roots of $0$; the criterion quoted).** A nonzero element $\tilde\Xi$ satisfies $\tilde\Xi\diamond\tilde\Xi=0$ if and only if

$$
\tilde\Xi\tilde\Xi^{*}\in\mathbb{C}_{\mathbb{B}}
\iff
\operatorname{Vect}\bigl(\tilde\Xi\tilde\Xi^{*}\bigr)=0 ,
$$

and the roots of $0$ are exactly the nonzero elements of this set. The set is the **complex cone on the real unit sphere** of the quaternion subspace, of real dimension five, its nonzero elements are the complex multiples $\rho\tilde u$ of the real unit quaternions $\tilde u$, and it contains the centre $\mathbb{C}_{\mathbb{B}}$, the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$.

*Proof.* By definition $\tilde\Xi\diamond\tilde\Xi=\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})$, which vanishes exactly when $\tilde\Xi\tilde\Xi^{*}$ is central. The parametrisation, the dimension and the quadric are the theorem of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, where the criterion is computed; they are quoted here because the diagonal of the block is the object of that article.

### The Real Reading of the Criterion

The criterion has a real form, and the block shares its real splitting with the general value: write

$$
\tilde\Xi=\tilde\xi+i\tilde\xi',\qquad \tilde\xi=\xi_0e_0+\vec\xi,\quad \tilde\xi'=\xi'_0e_0+\vec\xi',\qquad \xi_0,\xi'_0\in\mathbb{R},\quad \vec\xi,\vec\xi'\in\mathbb{R}^{3},
$$

the two real quaternions of *Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra*. Then the plain product with the star reads

$$
\tilde\Xi\tilde\Xi^{*}=\bigl(\tilde\xi\tilde\xi^{\natural}+\tilde\xi'\tilde\xi'^{\natural}\bigr)+i\bigl(\tilde\xi'\tilde\xi^{\natural}-\tilde\xi\tilde\xi'^{\natural}\bigr),
$$

whose first term is a real scalar; the vector part of the second is $2\bigl(\xi_0\vec\xi'-\xi'_0\vec\xi+\vec\xi\times\vec\xi'\bigr)$, so the criterion $\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})=0$ is the real-linear dependence of the two real quaternions,

$$
\tilde\Xi\tilde\Xi^{*}\ \text{central}\iff \tilde\xi\ \text{and}\ \tilde\xi'\ \text{are real-linearly dependent}.
$$

The square-zero elements are therefore the elements whose real and imaginary quaternion parts lie on one real line through the origin, and the parametrisation $\rho\tilde u$ is that dependence read with a real unit quaternion $\tilde u$ on the line.

### The Shape of the Set

**The square-zero set is a complex cone, and it is a proper subset of the space.** If $\tilde\Xi$ is square-zero and $\rho\in\mathbb{C}$ then $\rho\tilde\Xi$ is square-zero, because the diagonal of $\rho\tilde\Xi$ is $\operatorname{Vect}(\rho\tilde\Xi(\rho\tilde\Xi)^{*})=|\rho|^{2}\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})=|\rho|^{2}\,\tilde\Xi\diamond\tilde\Xi=0$; scaling by a complex number moves a square-zero element along the complex line through it and inside the set, and the set is a union of complex lines through the origin. The centre lies inside it, its elements having vanishing vector part; the real quaternion subspace and the anti-quaternion subspace lie inside it as well; and the element $e_1+ie_2$ is not square-zero, its real parts $\vec\xi=e_1$ and $\vec\xi'=e_2$ being independent, so its diagonal is the nonzero $2ie_3$.

The criterion is not automatic, and it selects a proper subset of the space. The element $e_1+ie_2$ has the noncentral plain product $\tilde P\tilde P^{*}=2e_0+2ie_3$ and the nonzero diagonal $2ie_3$, and it is not a root of $0$; the centre, the real quaternion subspace and the anti-quaternion subspace are inside the set, and the elements outside it are the majority. The line of the argument is the subject of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

## The Nilpotents

**The nilpotents of the block are exactly its square-zero elements, and the index is two: the left-nested cube vanishes only when the square does, so no element has index greater than two.**

### The Nilpotent Class

**Proposition (a square-zero element is a nilpotent of index two).** Every nonzero square-zero element of the block is a nilpotent of index two, and the origin is the trivial nilpotent of index one.

*Proof.* An element of index two is by definition a square-zero element, and a nonzero element whose square vanishes is a nilpotent: the second power vanishes, and the definition asks that some power vanish. The origin has vanishing first power and is of index one.

**Theorem (index two).** If the left-nested cube $\tilde P\diamond\tilde P\diamond\tilde P$ vanishes, then the square $\tilde P\diamond\tilde P$ vanishes. The nilpotents of the block are therefore exactly the square-zero elements, and there is no element of index greater than two.

*Proof.* Work in the $2\times2$ realization of *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, in which the block is the traceless part of the conjugate-transposed product,

$$
\mathsf{M}_2(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)\,I ,
\qquad
M=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}.
$$

Write $M=\mathsf{M}_2(\tilde P)$, $A=MM^{\dagger}$, a Hermitian positive semidefinite matrix, $t=\operatorname{Tr}A$, and $N=A-\tfrac12t\,I$, the traceless part of $A$, which is $\mathsf{M}_2(\tilde P\diamond\tilde P)$. The left-nested cube is the traceless part of $NM^{\dagger}$, and it vanishes exactly when $NM^{\dagger}$ is a scalar matrix, $NM^{\dagger}=\mu I$.

If $M$ is singular and nonzero, then $A$ has a single nonzero eigenvalue $t>0$, so $N$ has the eigenvalues $\pm\tfrac12t$ and is invertible and nonzero; but then $\operatorname{rank}(NM^{\dagger})=\operatorname{rank}(M^{\dagger})=\operatorname{rank}M=1$, while a scalar matrix of rank one is the zero matrix, forcing $M^{\dagger}=0$, a contradiction. So a singular $M$ with $NM^{\dagger}$ scalar has $N=0$, and the theorem holds in that case.

If $M$ is invertible, then $N\neq0$ would give $N=\mu(M^{\dagger})^{-1}$ and, $N$ being Hermitian, $\mu(M^{\dagger})^{-1}=\bar\mu M^{-1}$, so $M=\nu M^{\dagger}$ with $|\nu|=1$. Writing $\nu=e^{i\theta}$ and $H=e^{-i\theta/2}M$, the matrix $H$ is Hermitian, $A=H^{2}$, $t=\operatorname{Tr}(H^{2})$ and $N=H^{2}-\tfrac12\operatorname{Tr}(H^{2})I$; the scalar condition becomes $H^{3}-\tfrac12\operatorname{Tr}(H^{2})H=\gamma I$, and the eigenvalues $h_1,h_2$ of $H$ satisfy

$$
h_1^{3}-h_2^{3}-\tfrac12\bigl(h_1^{2}+h_2^{2}\bigr)(h_1-h_2)
=\tfrac12(h_1-h_2)(h_1+h_2)^{2}=0 ,
$$

so $h_1=h_2$ or $h_1+h_2=0$. In the first case $H$ is scalar, hence $A=H^{2}$ is scalar and $N=0$; in the second $H$ is traceless, hence $H^{2}=\tfrac12\operatorname{Tr}(H^{2})I$ and again $N=0$. Both cases contradict $N\neq0$, so $N=0$ and $\tilde P\diamond\tilde P=0$.

The same argument applies to the other bracketing of the cube: a vanishing right-nested cube $\tilde P\diamond(\tilde P\diamond\tilde P)$ is the mirror statement, obtained by reading the model with the reversed product. The square is bracketing-free, and the cube certifies the index in either bracketing.

**Corollary (the nilpotent class).** The nilpotents of the block are exactly the square-zero elements, that is the elements with $\tilde P\tilde P^{*}$ central; and no element of the block has index greater than two.

*Proof.* The theorem gives a vanishing cube only when the square vanishes, so every nilpotent has a vanishing square and is square-zero; the converse is the proposition. The class is therefore the set of the previous section, the complex cone on the real unit sphere, of real dimension five.

### The Nilpotents and the Zero Divisors

**Every nonzero square-zero element is a two-sided zero divisor, and it is its own annihilating partner; but the nilpotents are a thin subcone of the zero divisors, which are the whole punctured space.**

**Proposition (a nilpotent is a two-sided zero divisor).** Every nonzero square-zero element $\tilde\Upsilon$ of the block is a two-sided zero divisor, with $\tilde\Upsilon$ itself as the annihilating partner.

*Proof.* The element satisfies $\tilde\Upsilon\diamond\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, so it is a nonzero element that annihilates the nonzero element $\tilde\Upsilon$ on the left and on the right; by the definition of the zero divisor of *Zero Divisors of the Antisymmetric Plain Sesqualgebra*, it is a two-sided zero divisor.

The converse fails, and the failure is extreme. The zero-divisor set of the block is the **whole space without the origin** (*Zero Divisors of the Antisymmetric Plain Sesqualgebra*): every nonzero element annihilates some nonzero partner, the partner of an element invertible in the plain product being $(\tilde P^{-1})^{*}$, and the partner of a singular element being read from its plain annihilator. The nilpotents are the five-dimensional cone inside that set, and the contrast is the sharpest difference from the plain algebra, where the zero divisors are generated by the nilpotents and the idempotents together without covering the space: here the idempotents are gone and the nilpotents do not cover. The block is the structure of the twelve in which the inclusion of the nilpotents in the zero divisors carries the least information.

### The Nilpotents and the Idempotents

**No nilpotent is an idempotent: the two classes are disjoint, and in the block one of them is trivial.**

**Proposition (the two classes meet only at the origin).** No nilpotent of the block is an idempotent, and the only idempotent of the block is the origin.

*Proof.* A nonzero element cannot satisfy $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ and $\tilde\Pi\diamond\tilde\Pi=0$ at once, so no nonzero nilpotent is an idempotent. The only idempotent of the block is the origin, by *Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra*, and the origin is the nilpotent of index one, so the two classes meet exactly there.

The disjointness is general and the triviality is not: in the plain algebra the two classes are disjoint but both are rich, the idempotents carrying the Peirce decomposition and the nilpotents the off-diagonal units. In the block the idempotent set has collapsed to the origin, and the nilpotent class is the whole of the square-zero cone; the two are read together in the dictionary of the classes.

### The Nilpotents and the Conjugations

**The star and the natural conjugation both preserve the square-zero set, and the star pairs its elements two by two.**

**Proposition (the conjugations preserve the class).** For every square-zero $\tilde\Upsilon$,

$$
(\tilde\Upsilon^{*})\diamond(\tilde\Upsilon^{*})=0,
\qquad
(\tilde\Upsilon^{\natural})\diamond(\tilde\Upsilon^{\natural})=0 .
$$

*Proof.* The criterion $\tilde\Upsilon\tilde\Upsilon^{*}\in\mathbb{C}_{\mathbb{B}}$ is carried to its star and to its natural conjugate by the identities $(\tilde\Upsilon\tilde\Upsilon^{*})^{*}=\tilde\Upsilon\tilde\Upsilon^{*}$ and, for a central element, $\lambda^{\natural}=\lambda$; the natural conjugation of a central element is central. So each of the two images satisfies the criterion.

The star therefore pairs the nilpotents two by two through the involution $\tilde\Upsilon\mapsto\tilde\Upsilon^{*}$, and it fixes those with $\tilde\Upsilon^{*}=\tilde\Upsilon$, the **Hermitian nilpotents**. For the block the Hermitian elements are $a e_0+i\vec u$ with $a\in\mathbb{R}$ and $\vec u\in\mathbb{R}^{3}$, and their diagonal is $2ia\vec u$, so the Hermitian nilpotents are the real scalars and the purely imaginary vectors,

$$
\mathbb{R}e_0\cup i\mathbb{R}^{3} .
$$

The natural conjugation stabilises the real quaternion subspace and fixes the centre.

### The Nilpotents and the Remarkable Subspaces

**The square-zero set contains the centre, the real quaternion subspace and the anti-quaternion subspace entire, and it meets the Hermitian and anti-Hermitian subspaces in the real scalars and the purely imaginary vectors alone.**

The centre $\mathbb{C}_{\mathbb{B}}$, the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ lie inside the cone, by the criterion, each being a subspace on which the vector part of $\tilde P\tilde P^{*}$ vanishes. It does not contain the Hermitian subspace $\mathbb{M}_+$ or the anti-Hermitian subspace $\mathbb{M}_-$; a Hermitian element is $a e_0+i\vec u$ with $a\in\mathbb{R}$ and $\vec u\in\mathbb{R}^{3}$, its diagonal is $2ia\vec u$, so it is square-zero exactly when $a=0$ or $\vec u=0$, and the intersection is the union of the real scalars and the purely imaginary vectors. The witness $e_0+ie_1$, a Hermitian element with both a scalar and a vector part, is not square-zero: its diagonal is the nonzero $2ie_1$. The reading of the classes on the remarkable subspaces, with the dimension of each intersection, is *Remarkable Subspaces under the Antisymmetric Plain Sesqualgebra of Biquaternions*.

### The Comparison with the Parent and the Siblings

**The block's nilpotents strictly contain the parent's pure isotropic cone, and among the three antisymmetrisations the root-of-$0$ set separates the block's five-dimensional cone from the six-dimensional sibling and the two whole spaces.**

**Remark (the parent plain product).** The general plain bilinear product $\tilde P\tilde Q$ is associative and unital, and its nilpotents are the pure elements with isotropic vector part,

$$
\tilde\Upsilon^{2}=0\iff P_0=0\ \text{and}\ (\vec P,\vec P)=0
$$

(*Nilpotents of the General Plain Algebra*). The parent's class is a proper cone of complex dimension two and the implication *nilpotent implies zero divisor* holds there with the pure isotropic cone as the set. The block's class is the whole square-zero cone, which strictly contains it: the element $e_0$ is a nilpotent of the block, $e_0\diamond e_0=0$, and it is not a nilpotent of the parent, $e_0^{2}=e_0\neq0$. The enlargement is the projection: the parent's criterion is a condition on the square, and the block discards the scalar part of the square, so more elements satisfy it.

**Remark (the three antisymmetrisations).** The root of $0$ separates the three antisymmetric structures. The bilinear sibling $\mathrm{APA}=\vec\Xi\times\vec Q$ and the quaternionic bilinear sibling $\mathrm{AQA}$ are alternating, so their diagonal vanishes identically and their root-of-$0$ set is the whole space with the origin removed, of real dimension eight. The quaternionic sesquilinear sibling $\mathrm{AQS}=\vec\Xi\times\overline{\vec Q}$ has the diagonal $\vec\Xi\times\overline{\vec\Xi}$, which vanishes exactly when the two real parts of $\vec\Xi$ are linearly dependent and leaves the scalar part free, so its root-of-$0$ set is the union of the complex planes $\mathbb{C}e_0\oplus\mathbb{C}\vec v$ over the real directions $\vec v$, of real dimension six. The block's set is the smaller one, the real five-dimensional cone on the real unit sphere, because the block's projection constrains the scalar part as well.

| block | $\tilde\Xi\star\tilde\Xi$ | roots of $0$ |
|---|---|---|
| $\mathrm{APA}$ | $0$ identically | all nonzero elements, real dimension eight |
| $\mathrm{AQA}$ | $0$ identically | all nonzero elements, real dimension eight |
| $\mathrm{AQS}$ | $\vec\Xi\times\overline{\vec\Xi}$ | dependent real parts, real dimension six |
| $\mathrm{APS}$ | $\operatorname{Vect}(\tilde\Xi\tilde\Xi^{*})$ | the cone on the real unit sphere, real dimension five |

The root of $0$ of the four general products, where the equations are not contradictory, is *Square Roots of Minus One, Zero and Plus One in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the square-zero sets of the twelve structures are *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## Summary

The roots of $0$ of the block are exactly the nonzero elements with $\tilde\Xi\tilde\Xi^{*}$ central, that is the nonzero square-zero elements; they form the complex cone on the real unit sphere of the quaternion subspace, of real dimension five, and the centre, the real quaternion subspace and the anti-quaternion subspace lie inside it. In the real splitting $\tilde\Xi=\tilde\xi+i\tilde\xi'$ the criterion is the real-linear dependence of the two real quaternions, that is the three real conditions $\xi_0\vec\xi'-\xi'_0\vec\xi+\vec\xi\times\vec\xi'=0$, and the set is a complex cone.

The **index is two**: the left-nested cube vanishes only when the square does, by the $2\times2$ model in which the block is the traceless part of $MM^{\dagger}$ and the cube is the traceless part of $NM^{\dagger}$ with $N$ the traceless part of $A=MM^{\dagger}$; the singularity of $M$ and, in the invertible case, the comparison of the two eigenvalues of the Hermitian matrix $H$ both force $N=0$. The nilpotents are therefore exactly the square-zero elements, and no element has index greater than two.

Every nilpotent is a two-sided zero divisor, here trivially, since a square-zero element annihilates itself; but the zero divisors are the whole space without the origin and the nilpotents are a thin cone inside them, which is the sharpest difference from the plain algebra, where the zero divisors are generated by the nilpotents and the idempotents. The block has one idempotent, the origin, so the two classes meet only there. The star preserves the square-zero set and pairs its elements through the involution $\tilde\Upsilon\mapsto\tilde\Upsilon^{*}$, its fixed points being the real scalars and the purely imaginary vectors; the natural conjugation preserves the set as well, stabilising the real quaternion subspace and fixing the centre. The block's nilpotents strictly contain the parent's pure isotropic cone, and among the three antisymmetrisations the root-of-$0$ set separates the block's five-dimensional cone from the six-dimensional sibling and the two whole spaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\diamond$ | the product of the block, $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ |
| $\tilde\Upsilon$ | a nilpotent of the block |
| $\tilde P\diamond\tilde P=0$ | the square-zero condition, equivalent to $\tilde P\tilde P^{*}\in\mathbb{C}_{\mathbb{B}}$ |
| $\rho\tilde u$, $\rho\in\mathbb{C}^{*}$, $\tilde u$ a real unit quaternion | the parametrisation of the nonzero square-zero elements |
| $\xi_0\vec\xi'-\xi'_0\vec\xi+\vec\xi\times\vec\xi'=0$ | the criterion in the real splitting $\tilde\Xi=\tilde\xi+i\tilde\xi'$ |
| index two | the statement that a vanishing cube forces a vanishing square |
| $A=MM^{\dagger}$, $N=A-\tfrac12\operatorname{Tr}(A)I$ | the Hermitian square and its traceless part in the $2\times2$ model |
| $\mathbb{R}e_0\cup i\mathbb{R}^{3}$ | the Hermitian nilpotents, the real scalars and the purely imaginary vectors |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*Powers, the Square and the Roots* and §*The Nilpotent*, for the root of a central value, the nilpotent and its index.
- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation, its conjugate-alternation and its table.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the criterion for the vanishing of the diagonal and the quadric it traces.
- *Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-antisymmetric-plain-sesqualgebra.md`), for the roots of $+1$ and the origin alone as the idempotent.
- *Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-antisymmetric-plain-sesqualgebra.md`), for the real splitting and the arbitrary right side.
- *Zero Divisors of the Antisymmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-sesqualgebra.md`), for the total zero-divisor set against which the cone is read.
- *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the model of the index-two theorem.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`), for the pure isotropic cone of the parent product.
- *Remarkable Subspaces under the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the reading of the class on the subspaces.
