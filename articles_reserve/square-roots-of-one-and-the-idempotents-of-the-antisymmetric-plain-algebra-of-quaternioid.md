# __Square Roots of One and the Idempotents of the Antisymmetric Plain Algebra__

## Introduction

The root of a central value is defined by an equation in which the product occurs, so it is a class
of the product and not of the space (*Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*,
§*The Element Vocabulary*). The block of this article is the antisymmetric plain multiplication

$$
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\vec p\times\vec q,
$$

the cross product of the two vector parts, which is alternating and without a unit (*Introduction to
the Antisymmetric Plain Algebra of Quaternions*).

The article treats two subjects, and in this order. The first is the **square roots of the central
value $+1$**, the nonzero elements $\tilde\xi$ with $\tilde\xi\times\tilde\xi=+e_0$. The second is
the **idempotents of the block**, the elements $\tilde\pi$ with $\tilde\pi\times\tilde\pi=\tilde\pi$.
The two subjects are one subject, because the idempotent is the root of $+1$ in a scaled sense: in a
unital product the **halving map** $\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ carries the roots of
$+1$ onto the idempotents, with inverse $\tilde\pi\mapsto2\tilde\pi-e_0$. For the block the map is
degenerate, and its degeneration and the absence of the roots have one cause, the vanishing square:
the block is alternating, so $\tilde\xi\times\tilde\xi=0$ for every element, and neither the root
equation nor the scaled equation can be met off the origin.

The outcome is the extreme absence, and it is the sharpest form of the absence law. The block has
**no root of $+1$**, because the square of every element vanishes; and it has **one idempotent, the
origin**, because its idempotent equation reduces to $0=\tilde\pi$. It therefore has no nontrivial
idempotent, no orthogonal family, no primitive idempotent, no projection and no Peirce decomposition,
and the unit $e_0$ of the ambient algebra is not an idempotent of the block, the block being a
bracket and not a product. The roots of $-1$ are settled by the same reduction and are recorded in a
short remark at the end of §*The Roots of One*; the remark is used nowhere.

The article is algebraic. It does not treat the roots of $0$ and the nilpotents, which are *Square
Roots of Zero and the Nilpotents of the Antisymmetric Plain Algebra*; the square roots of a general
right side, which is *Square Roots of a General Element in the Antisymmetric Plain Algebra*; the
zero-divisor set, which is *Zero Divisors of the Antisymmetric Plain Algebra*; or the idempotent
families of the parent product, which are *Square Roots of One and the Idempotents of the General Plain Algebra*.

**The results.** For the antisymmetric plain multiplication $\tilde p\times\tilde q=\vec p\times\vec q$
the square of every element vanishes, $\tilde\xi\times\tilde\xi=0$, and the root equation of $+1$
therefore reduces to $0=+e_0$: the block has **no root of $+1$**, and **no root of $-1$** either, by
the same reduction. The idempotent equation $\tilde\pi\times\tilde\pi=\tilde\pi$ reduces to
$0=\tilde\pi$, so the block has **one idempotent, the origin**, and **no nontrivial idempotent**,
hence no orthogonal family, no primitive idempotent, no projection and no Peirce decomposition; the
unit $e_0$ of the ambient algebra is not an idempotent of the block. The comparison with the parent
plain product is the comparison of the origin alone with the two-point set $\{0,e_0\}$.

## The Notion and Its Product

**Definition (root of a central value).** Let $\star$ be a product on $\mathbb{H}$ and let
$\lambda\in\mathbb{R}$. A **root of $\lambda$ in $\star$** is a nonzero element $\tilde\xi$ with

$$
\tilde\xi\star\tilde\xi=\lambda e_0 .
$$

The three central values the quaternion algebra singles out are $-1$, $+1$ and $0$: the roots of $-1$
are the imaginary units, the roots of $+1$ are the involutions, and the roots of $0$ are the nonzero
nilpotents of the product. The general notion this specialises is the **square root of a central value** of the definitions
article, an element with $\tilde\xi^2=c$, the class being the set of the solutions, with no non-zero
requirement, so that the origin is counted there whenever it solves the equation (*Definitions for
the Study of the Algebraic Structures*, §*The Element Vocabulary*). A **root**, in this article and
in the articles of the block, is a nonzero element of that class, so that the roots of $0$ are the
class without the origin.

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{H}$. An element
$\tilde\pi$ is an **idempotent of $\star$** when $\tilde\pi\star\tilde\pi=\tilde\pi$; the definitions
article records that the idempotents contain the origin and every unit (*Definitions for the Study of
the Algebraic Structures*, §*The Element Vocabulary*), and the origin and the unit are the
**trivial idempotents** here, the other idempotents being **nontrivial**. In a unital product the
idempotent is the root of $+1$ in a scaled sense, through the halving map
$\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$, which carries the roots of $+1$ onto the idempotents, with
inverse $\tilde\pi\mapsto2\tilde\pi-e_0$, the two computations
$\tfrac12(e_0+\tilde\xi)^2=\tfrac12(e_0+\tilde\xi)$ and $(2\tilde\pi-e_0)^2=e_0$ reading the same
identity (the map of the roots/idempotents architecture, *Square Roots of One and the Idempotents in
the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*).

Throughout this article the product is the antisymmetric plain multiplication $\times$, and
unqualified, *root* means a root of the block and *idempotent* means an idempotent of the block. The
square of the block is the specialisation to the block of the general square of *The Symmetric and
Antisymmetric Parts of an Algebra Product*.

## The Roots of One

**Proposition (the reduction).** For every element $\tilde\xi$,

$$
\tilde\xi\times\tilde\xi=0 ,
$$

and the two central equations therefore reduce to the scalar equations

$$
\tilde\xi\times\tilde\xi=+e_0\quad\Longrightarrow\quad 0=+e_0 ,
\qquad
\tilde\xi\times\tilde\xi=-e_0\quad\Longrightarrow\quad 0=-e_0 .
$$

*Proof.* The block is alternating, $\tilde x\times\tilde x=0$ for every $\tilde x$, by *Introduction
to the Antisymmetric Plain Algebra of Quaternions*; read at $\tilde x=\tilde\xi$ this is the display.
Substituting the display into each central equation, whose left side is the square, gives the scalar
equation.

**Theorem (no root of $+1$).** The block has no root of $+1$:

$$
\{\tilde\xi:\tilde\xi\times\tilde\xi=+e_0\}=\varnothing .
$$

*Proof.* The reduction reads the equation as $0=+e_0$, a scalar equation failing for every
$\tilde\xi$: the left side is the origin and the right side the nonzero central value $+e_0$.

The criterion is the whole of the computation, because the left side of the equation is identically
zero and the equation constrains the right side alone. There is no exceptional element and no
exceptional central value.

**Remark (the roots of $-1$).** The other equation cancels in the same way and the block has no root
of $-1$ either:

$$
\tilde\xi\times\tilde\xi=-e_0\quad\Longrightarrow\quad 0=-e_0 ,
$$

with no solution. The remark is used nowhere in this article and is recorded for completeness. The
absence is not the failure of the parent algebra, where the roots of $-1$ are the pure unit
quaternions and those of $+1$ are the two units $\pm e_0$: the block has neither, because its square
is not a scalar at all but the zero element, whatever the coordinates of the alleged root. The
totality of the roots of $0$ is the same fact (*Square Roots of Zero and the Nilpotents of the
Antisymmetric Plain Algebra*).

## The Idempotents

**The block has one idempotent, the origin: the equation $\tilde\pi\times\tilde\pi=\tilde\pi$ reduces
to $0=\tilde\pi$, and the block therefore has no nontrivial idempotent, no nontrivial projector and no
Peirce decomposition.**

### The Criterion

**Theorem (the idempotent set).** The idempotent equation of the block is satisfied by the origin
alone,

$$
\{\tilde\pi:\tilde\pi\times\tilde\pi=\tilde\pi\}=\{0\}.
$$

*Proof.* Read the alternation $\tilde x\times\tilde x=0$ of *Introduction to the Antisymmetric Plain
Algebra of Quaternions* at $\tilde x=\tilde\pi$, giving $\tilde\pi\times\tilde\pi=0$. The idempotent
equation becomes $0=\tilde\pi$, whose only solution is the origin. The origin is an idempotent indeed,
$0\times0=0$.

The criterion is the whole of the computation, because the left side of the equation is identically
zero and the equation constrains the right side alone, and it is the same criterion as the one
recorded for the class of nonzero idempotents in *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The Criterion for an Empty Class*. Every candidate idempotent is excluded at once, and
no coordinate computation is needed.

**Corollary (no nontrivial idempotent).** The block has no nontrivial idempotent. In particular the
unit $e_0$ of the ambient algebra is not an idempotent of the block:
$e_0\times e_0=\mathbf 0\times\mathbf 0=0\neq e_0$.

*Proof.* A nontrivial idempotent is one different from the origin and, when the product is unital, from
the unit; the theorem says that the origin is the only idempotent, so there is none other. The element
$e_0$ satisfies $e_0\times e_0=0$ and $0\neq e_0$, so it is not an idempotent of the block, although
it is the unit of the parent product.

The equation is read in the product and not in the algebra, and the block is not the plain product.
The element $e_0$ is an idempotent of the parent and not of the block; the origin is an idempotent of
both, being the trivial idempotent of every product. The halving map of §*The Notion and Its Product*
degenerates here beyond the loss of the unit: the halving $\tfrac12(e_0+\tilde\xi)$ of an element of
the block is square-zero, $\tfrac12(e_0+\tilde\xi)\times\tfrac12(e_0+\tilde\xi)=0$, because every
square of the block vanishes, so no root of $+1$ produces a nontrivial idempotent, the root set being
empty; the origin is the sole idempotent, and it is the halving of $-e_0$.

### The Absence of the Projector and of the Peirce Calculus

**Proposition (no nontrivial projector).** The only idempotent of the block is the origin, whose left
multiplication operator is the zero operator. The block therefore carries no nontrivial projector:
there is no nonzero idempotent element whose multiplication operator is a nonzero idempotent operator.

*Proof.* By the theorem the only idempotent element is the origin, and $L_0=0$; the zero operator is a
projector, but there is no other idempotent element to produce one.

**Proposition (no Peirce decomposition).** The block has no Peirce decomposition relative to a
nontrivial idempotent, because it has no nontrivial idempotent, and the associativity the construction
also presupposes is unavailable in the block.

*Proof.* The Peirce decomposition is defined relative to a nontrivial idempotent of an associative
product; the block has none, and it is not associative (*The Specificities of the Antisymmetric Plain
Algebra*). The idempotent calculus of the parent — the left ideals, the direct sum decompositions and
the Peirce decomposition — has no entry point here.

**Remark.** The vanishing square makes the two levels of the idempotent theory collapse onto the
trivial one. An idempotent of an alternating product cannot exist off the origin, because the square
of every element vanishes; the block is the extreme case of the collapse, and the Peirce calculus,
the ideals and the module theory built from idempotents have no entry point in it. These constructions
belong to the plain product and to its blocks.

### The Comparison with the Parent Product

**Remark (the parent idempotents).** The parent general plain bilinear product is associative and
unital, and its idempotents are the two-point set $\{0,e_0\}$: the equation $\tilde x^2=\tilde x$
reads $\tilde x(\tilde x-e_0)=0$, and the parent is a division product, so $\tilde x=0$ or
$\tilde x=e_0$ (*The Specificities of the General Plain Algebra*; *Square Roots of One and the Idempotents of the General Plain
Algebra*). The block is the antisymmetric half of that product, and the comparison is the comparison
of a one-point set with a two-point set: the block keeps the trivial idempotent and loses $e_0$, and
it loses with it the entire idempotent calculus. The count is the point of the article — one
idempotent for the block against two for the parent — and it is decided by the single value of the
square at $e_0$, which is $e_0$ in the parent and $0$ in the block.

**Remark (the contrast with the biquaternion chapter).** Over $\mathbb{C}$ the same parent product
carries the idempotent family $\tfrac12(e_0+\tilde\Xi)$ over the roots $\tilde\Xi$ of $+1$, of real
dimension four, and the four general products of the biquaternion space carry four idempotent sets
whose sizes range from the trivial pair to the continuum (*Square Roots of One and the Idempotents in the Algebraic Structures
over the Biquaternion $\mathbb{C}$ Space*). The real block is poorer than any of them: it has the
origin alone, and the complexification does not enlarge its idempotent set, the equation
$0=\tilde\pi$ being independent of the field.

## The Comparison with the Other Five Structures

The idempotents of the six products, and the roots of the two signed central values against which they
are read, are the following.

| product | roots of $-1$ | roots of $+1$ | idempotents |
|---|---|---|---|
| GPA, $\tilde p\tilde q$ | the pure unit quaternions | $\pm e_0$ | $\{0,e_0\}$ |
| SPA, $\tilde p\bullet\tilde q$ | the pure unit quaternions | $\pm e_0$ | $\{0,e_0\}$ |
| APA, $\tilde p\times\tilde q$ | none | none | $\{0\}$ |
| GQA, $\tilde p^{\natural}\tilde q$ | none | the unit sphere | $\{0,e_0\}$ |
| SQA, $N(\tilde p,\tilde q)e_0$ | none | the unit sphere | $\{0,e_0\}$ |
| AQA, $\tilde p\wedge^{\natural}\tilde q$ | none | none | $\{0\}$ |

**Remark (the pairing of the blocks).** The two **general** products and their symmetric halves share
their root pattern, and the two **antisymmetric** halves share theirs: the splitting into symmetric
and antisymmetric parts is what decides the root theory, not the choice of the parent. The block is
one of the two members of the degenerate antisymmetric family, the other being *Introduction to the
Antisymmetric Quaternionic Algebra of Quaternions*, below this article in this category. The six
idempotent sets are read side by side in *Square Roots of One and the Idempotents in the Algebraic Structures over the
Quaternioid $\mathbb{R}$ Space*, and the four sets of the biquaternion chapter in *Idempotents in the
Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## Summary

For the antisymmetric plain multiplication $\tilde p\times\tilde q=\vec p\times\vec q$ the
square of every element vanishes, $\tilde\xi\times\tilde\xi=0$, so the root equation of $+1$ reduces
to the scalar equation $0=+e_0$ and the block has no root of $+1$; the root equation of $-1$ reduces
to $0=-e_0$ and the block has no root of $-1$ either. The idempotent equation
$\tilde\pi\times\tilde\pi=\tilde\pi$ reduces to $0=\tilde\pi$, because the block is alternating, so
the block has one idempotent, the origin, and no nontrivial idempotent. The unit $e_0$ of the ambient
algebra is not an idempotent of the block, the block being a bracket. No orthogonal family, no
primitive idempotent, no projection and no Peirce decomposition exists, and the only projector the
block carries is the zero operator, from the origin. The comparison with the parent product is the
comparison of the origin alone with the two-point set $\{0,e_0\}$, and the idempotent calculus — the
left ideals, the direct sum decompositions, the Peirce decomposition — belongs to the parent and not
to the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\tilde\xi\times\tilde\xi=+e_0$ | the root equation of $+1$, equivalent to $0=+e_0$ |
| $\tilde\xi\times\tilde\xi=-e_0$ | the root equation of $-1$, equivalent to $0=-e_0$ |
| $\varnothing$ | the roots of $+1$, and the roots of $-1$ |
| $\tilde\pi\times\tilde\pi=\tilde\pi$ | the idempotent equation, equivalent to $0=\tilde\pi$ |
| $\{0\}$ | the idempotent set of the block, the trivial idempotent alone |
| $L_{\tilde\pi}$ | the left multiplication operator of an idempotent, the zero operator at the origin |
| $\{0,e_0\}$ | the idempotents of the parent product, of which the block keeps only the origin |
| $\tfrac12(e_0+\tilde\xi)\mapsto$ idempotents | the halving map, onto in a unital product and degenerate in the block |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the root of a central value, the idempotent of a general product, the relativity of the definition and the criterion for an empty class
- *Introduction to the Antisymmetric Plain Algebra* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md`), for the operation, its alternation and its table
- *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-plain-algebra-of-quaternioid.md`), below this article in this category, for the roots of $0$ and the nilpotents, the other face of the same vanishing square
- *Square Roots of a General Element in the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-antisymmetric-plain-algebra-of-quaternioid.md`), below this article in this category, for the square map of the block and the absence of a root for every nonzero right side
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra-of-quaternioid.md`), below this article in this category, for the coincidence of the zero divisors with the roots of $0$
- *The Specificities of the Antisymmetric Plain Algebra* (`articles_maths/the-specificities-of-the-antisymmetric-plain-algebra-of-quaternioid.md`), below this article in this category, for the isolation of the block and the reading of its empty classes
- *The Specificities of the Quaternion Algebra* (`articles_maths/the-specificities-of-the-quaternion-algebra.md`), for the two-point idempotent set of the parent division product
- *Square Roots of One and the Idempotents of the Quaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.md`), for the idempotent families of the parent product
- *Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the idempotent sets of the six structures side by side
- *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the four idempotent sets of the biquaternion chapter, against which the real block's origin alone is read
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, the Peirce decomposition and the radical.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for idempotents and the ideal theory of a ring.
