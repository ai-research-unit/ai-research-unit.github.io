# __Square Roots of a General Element in the Antisymmetric Plain Algebra__

## Introduction

The equation $\tilde\xi\times\tilde\xi=\tilde a$ names the product in which the square is read, so
the square root is relative to it (*Definitions for the Study of the 6 Algebraic Structures*,
§*The Element Vocabulary*). The block of this article is the antisymmetric plain multiplication

$$
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\mathbf p\times\mathbf q,
$$

the cross product of the two vector parts, which is alternating (*Introduction to the Antisymmetric
Plain Algebra of Quaternions*). The article solves the equation for every right side $\tilde a$ and
determines the image and the kernel of the square map of the block.

The outcome is the extreme degeneration of the equation. Since the block is alternating, the square
of every element vanishes, $\tilde\xi\times\tilde\xi=0$, so the equation reads $0=\tilde a$. It has a
solution exactly when $\tilde a=0$, and then **every** element of $\mathbb{H}$ is a square root; for
every nonzero $\tilde a$ it has no solution. **The square map of the block is the zero map**: its
image is the origin alone and its kernel is the whole space. The special case of a central right
side, the roots of $-1$, of $0$ and of $+1$, is *Square Roots of Minus One, Zero and Plus One in the
Antisymmetric Plain Algebra*; the square-zero elements, which are the square roots of the origin,
are *Nilpotents of the Antisymmetric Plain Algebra*; the centred reading of the six structures is
*Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; and the theory of the general plain product, to which the block
is compared, is *Square Roots of a General Element in the General Plain Algebra*.

## The Notion and Its Product

**Definition (square root of an element).** Let $\star$ be a product on $\mathbb{H}$ and let
$\tilde a\in\mathbb{H}$. A **square root of $\tilde a$ in $\star$** is an element $\tilde\xi$ with
$\tilde\xi\star\tilde\xi=\tilde a$. The roots of a central value are the special case
$\tilde a=\lambda e_0$ (*Definitions for the Study of the 6 Algebraic Structures*, §*The Element
Vocabulary*).

Throughout this article the product is the antisymmetric plain multiplication $\times$, and
unqualified, *square root* means a square root of the block. The right side is an arbitrary element
of $\mathbb{H}$, and the article determines, for each $\tilde a$, whether the set
$\{\tilde\xi:\tilde\xi\times\tilde\xi=\tilde a\}$ is empty or not. The square map of the block is the
map

$$
\mathrm{sq}:\mathbb{H}\longrightarrow\mathbb{H},\qquad \mathrm{sq}(\tilde\xi)=\tilde\xi\times\tilde\xi .
$$

## The Reduction

**Proposition (the reduction).** For every element $\tilde\xi$,

$$
\mathrm{sq}(\tilde\xi)=\tilde\xi\times\tilde\xi=0 ,
$$

so the equation $\tilde\xi\times\tilde\xi=\tilde a$ is equivalent to the equation $0=\tilde a$,
uniformly in $\tilde\xi$.

*Proof.* The block is alternating, $\tilde x\times\tilde x=0$ for every $\tilde x$, by
*Introduction to the Antisymmetric Plain Algebra of Quaternions*; read at $\tilde x=\tilde\xi$ this
is the display. Substituting the display into the square-root equation, whose left side is
$\mathrm{sq}(\tilde\xi)$, gives $0=\tilde a$.

The reduction is the whole of the computation, because the left side takes no value other than zero.
No coordinate computation is needed, and the equation carries no information about the unknown
$\tilde\xi$: it constrains the right side alone.

## The Square Roots of the Origin

**Theorem (the square roots of $0$).** The square roots of the origin are all the elements of the
space,

$$
\{\tilde\xi:\mathrm{sq}(\tilde\xi)=0\}=\mathbb{H}.
$$

*Proof.* The reduction gives $\mathrm{sq}(\tilde\xi)=0$ for every $\tilde\xi$, so every element is a
square root of the origin and the set is the whole space.

The set is the kernel of the square map, and it is the whole space; it contains the origin, which is
a square root of itself. Its nonzero elements are the square-zero elements of the block, which are
the nilpotents of *Nilpotents of the Antisymmetric Plain Algebra* and the zero divisors of *Zero
Divisors of the Antisymmetric Plain Algebra*. The origin is the only value of which the block has
square roots at all, and it has as many as the space allows.

## The Square Roots of a Nonzero Element

**Theorem (the square roots of a nonzero element).** Let $\tilde a\neq0$. The equation
$\tilde\xi\times\tilde\xi=\tilde a$ has no solution; equivalently, no nonzero element of $\mathbb{H}$
has a square root in the block.

*Proof.* The reduction reads the equation as $0=\tilde a$, and $0\neq\tilde a$ by hypothesis, so the
equation fails for every $\tilde\xi$. Every element is therefore a square root of the origin and of
nothing else.

The absence is the absence of a nonzero value of the square map. The block removes the scalar part
of the parent product, and a square-root equation is a statement about the square of an element,
whose scalar part the block discards. The two nonzero central values $-1$ and $+1$ have no square
roots either, as the central case records, and neither has any other element of the space.

## The Image and the Kernel of the Square Map

**Proposition (the square map).** The square map of the block is the zero map:

$$
\mathrm{sq}=0,\qquad \operatorname{Im}\mathrm{sq}=\{0\},\qquad \ker\mathrm{sq}=\mathbb{H}.
$$

It is neither injective nor surjective, its image is the origin and its kernel the whole space.

*Proof.* The first statement is the reduction; the image is the set of values it takes, which is the
origin alone; and the kernel is the preimage of the origin, which by the theorem on the square roots
of the origin is the whole space. A map of a nonzero space to itself whose image is the origin and
whose kernel is the whole space is neither injective, the kernel being the whole space and not the
origin, nor surjective, the image being the origin and not the whole space.

The square map is thus as degenerate as a map of the space to itself can be. Its image is the origin,
of real dimension zero, and its kernel is the space, of real dimension four. The rank of the map is
zero, and the index of nilpotency of every nonzero element is two: the square vanishes and the
element does not, and no higher power is needed.

## The Comparison with the Parent Product

**Remark (the parent square roots).** The parent general plain bilinear product is associative and
unital, and its square-root equation $\tilde\xi^2=\tilde a$ is a genuine classification
(*Square Roots of a General Element in the General Plain Algebra*; *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*).
The block is the antisymmetric half of that product, and the comparison is the comparison of a square
map that is zero with a square map that is not. The parent's square is
$\tilde\xi^2=2\xi_0\tilde\xi-\bigl[\xi_0^2+\lvert\boldsymbol\xi\rvert^2\bigr]e_0$, whose image and
kernel are proper; the block's square map is the zero map, whose image is the origin and whose kernel
is the whole space. Over $\mathbb{R}$ the parent's square roots of the origin are the origin alone,
the plain product being a division product, while the block's are the whole space; and the parent's
roots of a negative value form the two-sphere of the vector subspace, whose block counterpart is
empty. In the centred comparison *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* the same fact is one row of the
six-structure table: the two antisymmetric structures have the whole space as their root set of $0$
and no root of any other central value.

**Remark (the removal of the scalar part).** The parent's square carries a central part
$\xi_0^2-\lvert\boldsymbol\xi\rvert^2$ and a vector part $2\xi_0\boldsymbol\xi$; the block removes the
scalar part of the product, and with it the central part of the square. The equation
$\tilde\xi\times\tilde\xi=\tilde a$ is the parent's square-root equation with the central coordinate
deleted, and with the central coordinate deleted the equation collapses to the statement that
$\tilde a$ has no central coordinate. This is the same degeneration the root sets of the three
central values record, read for an arbitrary right side.

## Summary

For the antisymmetric plain multiplication $\tilde\xi\times\tilde q=\boldsymbol\xi\times\mathbf q$ the
square of every element vanishes, so the equation $\tilde\xi\times\tilde\xi=\tilde a$ reads
$0=\tilde a$ and is independent of the unknown. It has a solution exactly when $\tilde a=0$, and then
every element of $\mathbb{H}$ is a square root; for every nonzero $\tilde a$ it has no solution. The
square map of the block is the zero map, of image the origin and kernel the whole space, so it is
neither injective nor surjective, and every nonzero element is nilpotent of index two. The comparison
with the parent product is the comparison of a zero square map with a proper one: the parent's square
roots of the origin are the origin alone over $\mathbb{R}$ and the block's are the whole space, and
the parent's two-point and two-sphere families have no counterpart in the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\xi\times\tilde q=\tfrac12(\tilde\xi\tilde q-\tilde q\tilde\xi)=\boldsymbol\xi\times\mathbf q$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\mathrm{sq}(\tilde\xi)=\tilde\xi\times\tilde\xi=0$ | the square map of the block, the zero map |
| $\tilde\xi\times\tilde\xi=\tilde a$ | the square-root equation, equivalent to $0=\tilde a$ |
| $\mathbb{H}$ | the square roots of the origin, the kernel of the square map |
| $\{0\}$ | the image of the square map, the only right side with square roots |
| $\tilde\xi^2=2\xi_0\tilde\xi-\bigl[\xi_0^2+\lvert\boldsymbol\xi\rvert^2\bigr]e_0$ | the square of the parent plain product, with its central part and its vector part |
| $\boldsymbol\xi\times\mathbf q$ | the cross product of the two vector parts, the value of the block |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the square root of an element, the root of a central value and the relativity of the definitions to the product
- *Introduction to the Antisymmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternions.md`), for the operation, its alternation and its table
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-plain-algebra-of-quaternions.md`), for the special case of a central right side
- *Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-plain-algebra-of-quaternions.md`), for the square-zero elements, which are the square roots of the origin
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra-of-quaternions.md`), for the coincidence of the square-zero set, the root set of $0$ and the zero-divisor set
- *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the centred reading of the six structures, against which the zero square map of the block is placed
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra-of-quaternions.md`), for the classification of the parent product
- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the square of a product and its split into the two halves
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the square roots, the idempotents and the nilpotents of an algebra.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the quadratic equation and its solutions in a real algebra.
