# __Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra__

## Introduction

A root of a central value is defined by an equation in which the product occurs, so it belongs to the product (*Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*). The block of this article is the antisymmetric quaternionic multiplication

$$
\tilde\xi\diamond\tilde q=\tfrac12\bigl(\tilde\xi^{\natural}\tilde q-\tilde q^{\natural}\tilde\xi\bigr)
=\xi_0\vec q-q_0\vec\xi-\vec\xi\times\vec q,
$$

which is alternating and without a unit (*Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*). The article solves the three equations

$$
\tilde\xi\diamond\tilde\xi=-e_0,\qquad
\tilde\xi\diamond\tilde\xi=0,\qquad
\tilde\xi\diamond\tilde\xi=+e_0,
$$

and the solution sets are decided by one fact: the block is alternating, so the left side is zero for every element, and the three equations reduce to the three scalar equations $0=-e_0$, $0=0$ and $0=+e_0$.

The outcome is the sharpest form of the absence law. The block has **no root of $-1$** and **no root of $+1$**, because its square is never central and nonzero; its **roots of $0$ are all the elements of the space**, because its square vanishes identically. Of the three central values the block carries roots of one only, and that one totally. The nonzero roots of $0$ are the square-zero elements of the block, which are the subject of *Nilpotents of the Antisymmetric Quaternionic Algebra*, and they are also the zero divisors of the block (*Zero Divisors of the Antisymmetric Quaternionic Algebra*); the relation of the three sets to the idempotents is given at the end, where *Idempotents of the Antisymmetric Quaternionic Algebra* is cited.

**Conventions.** Throughout, $\tilde\xi=\xi_0e_0+\vec\xi$ and $\tilde q=q_0e_0+\vec q$ name elements of $\mathbb{H}$ with real coefficients, $(\vec\xi,\vec q)$ is the dot product and $\vec\xi\times\vec q$ the cross product of the vector parts, and $\tilde\xi^{\natural}=\xi_0e_0-\vec\xi$ is the quaternion conjugation; the bar is the identity and the star coincides with the natural conjugation, so no bare bar is written on an element of this block. The operation is written $\diamond$ and never $\wedge^{\natural}$ outside a citation. A **root** is read as in *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*: it is not required to be nonzero, and the nonzero roots are singled out when they are meant. The three values are the central real numbers $-1$, $0$ and $+1$, and each equation is read in the product $\diamond$ and not in the ambient algebra.

**Boundaries.** The operation and its alternation are *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*; the definitions of the square, the root of a central value and the square-zero element are *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; and the comparison of the six structures by the existence of a root is *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, whose companion for the whole chapter is *Square Roots of Minus One, Zero and Plus One in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The nilpotents of the block are *Nilpotents of the Antisymmetric Quaternionic Algebra*, its zero divisors are *Zero Divisors of the Antisymmetric Quaternionic Algebra*, and its idempotents are *Idempotents of the Antisymmetric Quaternionic Algebra*.

## The Notion and Its Product

**Definition (root of a central value).** Let $\star$ be a product on $\mathbb{H}$ and let $\lambda\in\mathbb{R}$. A **root of $\lambda$ in $\star$** is an element $\tilde\xi$ with

$$
\tilde\xi\star\tilde\xi=\lambda e_0 ,
$$

and the **root set of $\lambda$** is the set of all such $\tilde\xi$. The value is central, so the equation is an equality of quaternions with a real right-hand side. A root is not required to be nonzero; a nonzero root of $0$ is a square-zero element, and the square-zero elements are the subject of the nilpotent theory. The three central values the real algebra singles out are $-1$, $+1$ and $0$.

Throughout this article the product is the **antisymmetric quaternionic multiplication** $\diamond$, and unqualified, *root* means a root of the block. The square of the block is the specialisation to the block of the general square of *The 6 Products of the Quaternion Real Space*; the roots of the three values in the general plain product, to which the block is compared, are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

## The Common Reduction

**Proposition (the reduction).** For every element $\tilde\xi$,

$$
\tilde\xi\diamond\tilde\xi=0 ,
$$

and consequently the three equations $\tilde\xi\diamond\tilde\xi=-e_0$, $\tilde\xi\diamond\tilde\xi=0$ and $\tilde\xi\diamond\tilde\xi=+e_0$ are equivalent to the three scalar equations $0=-e_0$, $0=0$ and $0=+e_0$.

*Proof.* The block is alternating, $\tilde x\diamond\tilde x=0$ for every $\tilde x$, by *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*; read at $\tilde x=\tilde\xi$ this is the display. Substituting the display into each of the three equations gives the corresponding scalar equation. No coordinate computation is needed, the right side of each equation being central and the left side being the central element $0$.

The reduction is the whole of the computation. The three sets below are read off the three scalar equations alone, and they depend on the two facts that $e_0$ is nonzero and that the real field has characteristic zero.

## The Roots of Minus One

**Theorem (no roots of $-1$).** The block has no root of $-1$; equivalently, the equation $\tilde\xi\diamond\tilde\xi=-e_0$ has no solution.

*Proof.* The reduction gives $\tilde\xi\diamond\tilde\xi=0$ for every $\tilde\xi$, and $0\neq-e_0$ because $e_0$ is nonzero, the real field being of characteristic zero. Hence the equation fails at every element and the root set is empty.

The absence is the absence of a square that is central and negative. The block removes the scalar part of the parent product, and the root of $-1$ is a statement about the scalar part of a square; with the scalar part removed, the equation cannot be met. In particular the root sphere $S^2$ of the pure unit quaternions, which is the root set of $-1$ in the plain product, has no analogue in the block, and the parameter of the complex structures is not delivered here.

## The Roots of Zero

**Theorem (the roots of $0$ are all the elements).** The block's roots of $0$ are all the elements of $\mathbb{H}$,

$$
\{\tilde\xi:\ \tilde\xi\diamond\tilde\xi=0\}=\mathbb{H},
$$

and the nonzero roots of $0$ are the punctured space $\mathbb{H}\setminus\{0\}$.

*Proof.* The reduction gives $\tilde\xi\diamond\tilde\xi=0$ for every $\tilde\xi$, so the equation $\tilde\xi\diamond\tilde\xi=0$ holds at every element and the root set is the whole space; the origin is a root of $0$ and the nonzero roots are the elements other than the origin.

The root set of $0$ is therefore the whole space, and its nonzero part is at once the square-zero set of the block and its zero-divisor set: an element is a nonzero root of $0$ exactly when it is a nonzero square-zero element, and by *Zero Divisors of the Antisymmetric Quaternionic Algebra* it is then a two-sided zero divisor with itself as partner. The three names — nonzero root of $0$, square-zero element, zero divisor — select one and the same set for the block, and the set is as large as the space allows. This is the last of the readings of *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*: among the six structures of the real chapter the two antisymmetric ones are the only class whose root set is the whole space at the value $0$ and empty at every other value. The four remaining structures, whose square vanishes only at the origin, have the origin alone as roots of $0$; the plain family carries in addition the sphere of a negative value and the two central points of a positive value, and the quaternionic family the sphere of a positive value.

## The Roots of Plus One

**Theorem (no roots of $+1$).** The block has no root of $+1$; equivalently, the equation $\tilde\xi\diamond\tilde\xi=+e_0$ has no solution.

*Proof.* The reduction gives $\tilde\xi\diamond\tilde\xi=0$ for every $\tilde\xi$, and $0\neq+e_0$ because $e_0$ is nonzero. Hence the equation fails at every element and the root set is empty.

The roots of $+1$ are the involutions of the product, and the block has none. In particular the element $e_0$ is not a root of $+1$ of the block, although it is the unit of the ambient algebra and a root of $+1$ of the plain product; the equation is read in the product and not in the algebra, and the product is not the plain one. The element $e_0$ acts as the identity on the vector subspace and kills the centre, and it is not an involution of the block either, since $e_0\diamond e_0=0$.

## The Three Sets Compared

| central value $\lambda$ | the equation | the root set of the block |
|---|---|---|
| $-1$ | $\tilde\xi\diamond\tilde\xi=-e_0$ | $\varnothing$ |
| $0$ | $\tilde\xi\diamond\tilde\xi=0$ | $\mathbb{H}$, the whole space |
| $+1$ | $\tilde\xi\diamond\tilde\xi=+e_0$ | $\varnothing$ |

The table is the reduction read value by value. Two of the three sets are empty and the third is the whole space, and the table is the exact opposite of the table of the general plain algebra, where the three sets are three proper families: the roots of $-1$ there are the unit pure sphere, the roots of $0$ the origin alone, and the roots of $+1$ the two central units. The difference is the removal of the scalar part: the three equations of the plain product are three conditions on the central square, and the central square of the block is identically zero, so two conditions are impossible and the third is vacuous. The block is the one place of the six structures where the roots of $0$ are not the origin but the whole space.

## The Relation to the Idempotents and to the Zero Divisors

**Remark (the idempotents).** The idempotents of a product are its roots of $+1$ in a scaled sense, and for the block the two notions are both trivial: there is no root of $+1$ by the theorem, and the idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is met by the origin alone, since its left side is zero (*Idempotents of the Antisymmetric Quaternionic Algebra*). The coincidence is not a new fact; it is the same vanishing square read twice.

**Remark (the zero divisors and the nilpotents).** The nonzero roots of $0$ are the nonzero elements, and so are the nilpotents and the zero divisors of the block. The three classes are one class,

$$
\{\text{nonzero roots of }0\}=\{\text{square-zero elements}\}=\{\text{zero divisors}\}=\mathbb{H}\setminus\{0\},
$$

and the equalities are the content of the two companion articles of the block. In particular the implication *nilpotent implies zero divisor* holds for the block at every nonzero nilpotent, as it holds for the parent quaternionic product, where both classes are empty; it is the implication the criterion of *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* uses to empty the nilpotent class of the plain and quaternionic structures, and the block satisfies it trivially. Every nonzero element of the block is a nilpotent and every nonzero element is a zero divisor, so the only element at which the implication is not read is the origin, the trivial element, which is excluded from the zero divisors by their definition.

## The Relation to the Parent Product

**Remark (the parent squares).** The parent quaternionic product $\tilde\xi^{\natural}\tilde q$ has the square $\tilde\xi^{\natural}\tilde\xi=N(\tilde\xi)e_0$, a central value; its three root equations are the three conditions $N(\tilde\xi)=-1$, $N(\tilde\xi)=0$ and $N(\tilde\xi)=+1$ on the quaternion form $N(\tilde\xi)=\xi_0^2+\lvert\vec\xi\rvert^2$. Over $\mathbb{R}$ the form is a sum of four squares, hence nonnegative: the parent has **no root of $-1$**, the **origin alone as root of $0$**, and the **unit three-sphere $S^3$ as root of $+1$**. The block removes the scalar part of the parent, and with the scalar part removed the square loses the quaternion form: the three conditions become the single statement that the square is zero, and the non-vacuous condition of the parent at $0$ is replaced by the whole space. The block's root set of $0$, all of $\mathbb{H}$, strictly contains the parent's root set of $0$, the origin alone; the block's roots of $-1$ are empty as the parent's, while the block's roots of $+1$ are empty where the parent's are the unit sphere.

The difference between the two readings is the difference between a definite form and a vanishing one. The parent's zero divisor cone is empty over $\mathbb{R}$, its quaternion form being positive definite off the origin, so its root of $0$ and its nilpotent class are trivial; the block's square vanishes identically, so its root of $0$ is everything and its nilpotent class is everything apart from the origin. This is the contrast drawn in *Nilpotents of the Antisymmetric Quaternionic Algebra*.

## Summary

The root of a central value is an element whose square is the value times $e_0$, and for the antisymmetric quaternionic multiplication the square vanishes identically, so the three equations of $-1$, $0$ and $+1$ reduce to the scalar equations $0=-e_0$, $0=0$ and $0=+e_0$. The block has no root of $-1$, no root of $+1$, and all of $\mathbb{H}$ as its roots of $0$; of the three central values it carries roots of one only, and that one totally. The nonzero roots of $0$ are the square-zero elements, the nilpotents and the zero divisors of the block, all three being the punctured space; the idempotent set is the origin alone, the idempotent equation being the scaled root of $+1$ equation read at the vanishing square. The parent quaternionic product, whose square is the definite quaternion form times $e_0$, has the origin alone as root of $0$ and the unit three-sphere as root of $+1$; the removal of the scalar part replaces that pair by the whole space and the empty set.

## Summary of Notation

| symbol | meaning |
|---|---|
| root of $\lambda$ in $\star$ | $\tilde\xi\in\mathbb{H}$ with $\tilde\xi\star\tilde\xi=\lambda e_0$ |
| $\tilde\xi\diamond\tilde\xi=0$ | the square of the block vanishes identically |
| $\varnothing$ | the root sets of $-1$ and of $+1$ in the block |
| $\mathbb{H}$ | the root set of $0$ in the block |
| $\mathbb{H}\setminus\{0\}$ | the nonzero roots of $0$, the square-zero elements and the zero divisors |
| $N(\tilde\xi)=\xi_0^2+\lvert\vec\xi\rvert^2$ | the quaternion form, the square of the parent product |
| $\{0\}$, $S^3$ | the roots of $0$ and of $+1$ in the parent quaternionic product |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternion-r-space.md`), for the square, the root of a central value and the square-zero element.
- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the operation and its alternation.
- *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternion-r-space.md`), the companion of this article, for the root equation at a general central value and the six root sets.
- *Square Roots of Minus One, Zero and Plus One in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-algebraic-structures-over-the-quaternion-r-space.md`), for the three values read across the six structures of the real chapter.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the plain classification, to which the block is the counterpoint.
- *Nilpotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the square-zero elements of the block.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the zero divisors of the block.
- *Idempotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the idempotent set of the block.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the square of a quaternion and the pure roots of minus one.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the root problem on the quaternion sphere and the three named values.
