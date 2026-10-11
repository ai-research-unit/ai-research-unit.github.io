# __Square Roots of a General Element in the Antisymmetric Plain Algebra__

## Introduction

The equation $\tilde P\wedge\tilde P=\tilde A$ names the product in which the square is read, so
the square root is relative to it (*Definitions for the Study of the 12 Algebraic Structures*,
§*Powers, the Square and the Roots*). The block of this article is the antisymmetric plain
multiplication
$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
$$
the cross product of the two vector parts, which is alternating (*Introduction to the
Antisymmetric Plain Algebra of Biquaternions*). The article solves the equation for every right
side $\tilde A$ and determines the image of the square map of the block.

The outcome is the extreme degeneration of the equation. Since the block is alternating, the
square of every element is zero, $\tilde P\wedge\tilde P=0$, so the equation reads $0=\tilde A$.
It has a solution exactly when $\tilde A=0$, and then **every** element of $\mathbb{B}$ is a square
root; for every nonzero $\tilde A$ it has no solution. **The square map of the block is the zero
map**: its image is the origin alone and its kernel is the whole space. The special case of a
central right side, the roots of $-1$, of $0$ and of $+1$, is *Square Roots of Minus One, Zero and
Plus One in the Antisymmetric Plain Algebra*; the square-zero elements, which are the square roots
of the origin, are *Nilpotents of the Antisymmetric Plain Algebra*; and the theory of the general
plain product, to which the block is compared, is *Square Roots of a General Element in the
General Plain Algebra*.

## The Notion and Its Product

**Definition (square root of an element).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde A\in\mathbb{B}$. A **square root of $\tilde A$ in $\star$** is an element $\tilde P$ with
$$
\tilde P\star\tilde P=\tilde A .
$$
The roots of a central value are the special case $\tilde A=\lambda e_0$
(*Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*).

Throughout this article the product is the **antisymmetric plain multiplication** $\wedge$, and
unqualified, *square root* means a square root of the block. The right side is an arbitrary
element of $\mathbb{B}$, and the article determines, for each $\tilde A$, whether the set
$\{\tilde P:\tilde P\wedge\tilde P=\tilde A\}$ is empty or not. The square map of the block is the
specialisation to the block of the general square of *The Symmetric and Antisymmetric Parts of an
Algebra Product*; it is the map
$$
\mathrm{sq}:\mathbb{B}\longrightarrow\mathbb{B},\qquad \mathrm{sq}(\tilde P)=\tilde P\wedge\tilde P .
$$

## The Reduction

**Proposition (the reduction).** For every element $\tilde P$,
$$
\mathrm{sq}(\tilde P)=\tilde P\wedge\tilde P=0 ,
$$
so the equation $\tilde P\wedge\tilde P=\tilde A$ is equivalent to the equation $0=\tilde A$,
uniformly in $\tilde P$.

*Proof.* The block is alternating, $\tilde X\wedge\tilde X=0$ for every $\tilde X$, by
*Introduction to the Antisymmetric Plain Algebra of Biquaternions*; read at $\tilde X=\tilde P$
this is the display. Substituting the display into the square-root equation, whose left side is
$\mathrm{sq}(\tilde P)$, gives $0=\tilde A$.

The reduction is the whole of the computation, because the left side takes no value other than
zero. No coordinate computation is needed, and the equation carries no information about the
unknown $\tilde P$: it constrains the right side alone.

## The Square Roots of the Origin

**Theorem (the square roots of $0$).** The square roots of the origin are all the elements of the
space,
$$
\{\tilde P:\mathrm{sq}(\tilde P)=0\}=\mathbb{B}.
$$

*Proof.* The reduction gives $\mathrm{sq}(\tilde P)=0$ for every $\tilde P$, so every element is a
square root of the origin, and the set is the whole space.

The set is the kernel of the square map, and it is the whole space; it contains the origin, which
is a square root of itself. Its nonzero elements are the square-zero elements of the block, which
are the nilpotents of *Nilpotents of the Antisymmetric Plain Algebra* and the zero divisors of
*Zero Divisors of the Antisymmetric Plain Algebra*. The origin is the only value of which the
block has square roots at all, and it has as many as the space allows.

## The Square Roots of the Nonzero Elements

**Theorem (the square roots of a nonzero element).** Let $\tilde A\neq0$. The equation
$\tilde P\wedge\tilde P=\tilde A$ has no solution; equivalently, no nonzero element of
$\mathbb{B}$ has a square root in the block.

*Proof.* The reduction reads the equation as $0=\tilde A$, and $0\neq\tilde A$ by hypothesis, so
the equation fails for every $\tilde P$. Every element is therefore a square root of the origin
and of nothing else.

The absence is the absence of a nonzero value of the square map. The block removes the scalar part
of the parent product, and a square root equation is a statement about the square of an element,
whose scalar part the block discards. The two nonzero central values $-1$ and $+1$ have no square
roots either, as the central case records, and neither has any other element of the space.

## The Image and the Kernel of the Square Map

**Proposition (the square map).** The square map of the block is the zero map:
$$
\mathrm{sq}=0,\qquad \operatorname{Im}\mathrm{sq}=\{0\},\qquad \ker\mathrm{sq}=\mathbb{B} .
$$
It is neither injective nor surjective, its image is the origin and its kernel the whole space.

*Proof.* The first statement is the reduction; the image is the set of values it takes, which is
the origin alone; and the kernel is the preimage of the origin, which by the theorem on the square
roots of the origin is the whole space. A map of a nonzero space to itself whose image is the
origin and whose kernel is the whole space is neither injective, the kernel being the whole space
and not the origin, nor surjective, the image being the origin and not the whole space.

The square map is thus as degenerate as a map of the space to itself can be. Its image is the
origin, of complex dimension zero, and its kernel is the space, of complex dimension four. The
rank of the map is zero, and the index of nilpotency of every nonzero element is two: the square
vanishes and the element does not, and no higher power is needed.

## The Comparison with the Parent Product

**Remark (the parent square roots).** The parent general plain bilinear product is associative and
unital, and its square-root equation $\tilde P^{2}=\tilde A$ is a genuine classification, whose
central case has three proper families
(*Square Roots of a General Element in the General Plain Algebra*; *Square Roots of Minus One,
Zero and Plus One in the General Plain Algebra*). The block is the antisymmetric half of that
product, and the comparison is the comparison of a square map that is zero with a square map that
is not: the parent's square map is the identity-block combination
$\tilde P^{2}=2P_0\tilde P-\bigl[P_0^{2}+(\mathbf P,\mathbf P)\bigr]e_0$, whose image and kernel
are proper, and the block's square map is the zero map, whose image is the origin and whose kernel
is the whole space. The only right side of which the block has square roots is the origin, and
there it has more than the parent: the parent's square roots of the origin are the origin together
with the pure isotropic cone, while the block's are the whole space.

**Remark (the removal of the scalar part).** The parent's square carries a central part,
$P_0^{2}-(\mathbf P,\mathbf P)$, and a vector part $2P_0\mathbf P$; the block removes the scalar
part of the product, and with it the central part of the square. The equation
$\tilde P\wedge\tilde P=\tilde A$ is the parent's square-root equation
with the central coordinate deleted, and with the central coordinate deleted the equation collapses
to the statement that $\tilde A$ has no central coordinate. This is the same degeneration the
root sets of the three central values record, read for an arbitrary right side.

## Summary

For the antisymmetric plain multiplication $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ the
square of every element vanishes, so the equation $\tilde P\wedge\tilde P=\tilde A$ reads
$0=\tilde A$ and is independent of the unknown. It has a solution exactly when $\tilde A=0$, and
then every element of $\mathbb{B}$ is a square root; for every nonzero $\tilde A$ it has no
solution. The square map of the block is the zero map, of image the origin and kernel the whole
space, so it is neither injective nor surjective, and every nonzero element is nilpotent of index
two. The comparison with the parent product is the comparison of a zero square map with a proper
one: the parent's square roots of the origin are the origin together with the pure isotropic cone
and the block's are the whole space, and the parent's roots of $-1$ and $+1$, its three families,
have no counterpart in the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\mathrm{sq}(\tilde P)=\tilde P\wedge\tilde P=0$ | the square map of the block, the zero map |
| $\tilde P\wedge\tilde P=\tilde A$ | the square-root equation, equivalent to $0=\tilde A$ |
| $\mathbb{B}$ | the square roots of the origin, the kernel of the square map |
| $\{0\}$ | the image of the square map, the only right side with square roots |
| $N(\tilde P)=P_0^{2}+(\mathbf P,\mathbf P)$ | the norm of the parent product, the central part of $\tilde P\tilde P^{\natural}$; the parent square's own central part is $P_0^{2}-(\mathbf P,\mathbf P)$ |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the square root of an element, the root of a central value and the relativity of the definitions to the product
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-plain-algebra.md`), for the special case of a central right side
- *Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-plain-algebra.md`), for the square-zero elements, which are the square roots of the origin
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the classification of the parent product, against which the zero square map is read
- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the square of a product and its split into the two halves
