# __Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra__

## Introduction

In the symmetric quaternionic block the square of an element is a scalar multiple of $e_0$, and the
multiple is the quaternion form, $\tilde x\star\tilde x=N(\tilde x)e_0$. The equation
$\tilde x\star\tilde x=0$ is therefore the vanishing of the sum of four squares, and the elements it
selects are the subject of this article. The block is one of the products on which the square and the
cube vanish at different elements: the origin is the only element whose square vanishes, while every
nonzero pure quaternion has a vanishing cube. This article reads the **roots of the central value $0$**
and then the **nilpotents** of the block, which are the nonzero elements some power of which vanishes.

The roots of $0$ are the origin alone, and the nilpotents are the nonzero pure quaternions, each of
index exactly three. The two classes are pulled apart by the definiteness of the coefficient: the cube
vanishes on the whole punctured vector subspace, the square only at the origin. The definitions of a
**nilpotent**, of a **square-zero element** and of the **index of nilpotency** are *Definitions for the
Study of the Algebraic Structures*, §*The Element Vocabulary*; the product, its scalar law and the
definiteness of its coefficient are *Introduction to the Symmetric Quaternionic Algebra of
Quaternions*.

**The results.** The root set of $0$ is the singleton $\{0\}$: the elements whose square vanishes are
the origin alone, there is no nonzero square-zero element, and the block has no nilpotent of index two.
The nilpotents of the block are exactly the nonzero pure elements, the punctured vector subspace
$\operatorname{Im}\mathbb{H}\setminus\{0\}$, and each of them has index exactly three; there is no
nilpotent of index two and none of index greater than three. The nilpotent set is strictly contained in
the zero-divisor set, which is the whole punctured space $\mathbb{H}\setminus\{0\}$, the strictness
being witnessed by $e_0$; the nilpotent set and the idempotent set are disjoint. In
the $2\times2$ model the nilpotents are the trace-free matrices, and the singular branch of the complex
chapter collapses because the determinant is definite.

**Boundaries.** The product, the square and the form are *Introduction to the Symmetric Quaternionic
Algebra of Quaternions* and *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*;
the roots of $+e_0$ and the idempotents of the block are *Square Roots of One and the Idempotents of the
Symmetric Quaternionic Algebra*, the companion of this article; the roots of a general central value,
with the classification by the sign, are *Square Roots of a General Element in the Symmetric Quaternionic
Algebra*; the diagonal and the non-isotropic class are *Norm and Invertibility in the Symmetric
Quaternionic Algebra*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Algebra*; the
isotropic elements and the radical are *The Radical and the Isotropic Elements of the Symmetric
Quaternionic Algebra*; the powers and the nilpotent class are also collected in *The Specificities of
the Symmetric Quaternionic Algebra*; the realization $\mathsf{M}_2$, its trace and its determinant are
*The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1e_2=e_3$; an element is $\tilde x=x_0e_0+\vec x$, with
$\vec x=x_1e_1+x_2e_2+x_3e_3$. The **quaternion conjugation** is
$\tilde x^{\natural}=x_0e_0-\vec x$; on $\mathbb{R}$ the bar is the identity and the star coincides
with the natural sign ${}^{\natural}$. The **quaternion form** is
$N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$, with diagonal
$N(\tilde x)=x_0^{2}+|\vec x|^{2}$, and the **symmetric quaternionic product** is
$\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$. The centre is the scalar line $\mathbb{R}e_0$ and the
vector subspace is
$\mathrm{Vect}(\mathbb{H})=\operatorname{Im}\mathbb{H}=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$. The
**powers** are left-nested, $\tilde x^{\star1}=\tilde x$ and
$\tilde x^{\star(k+1)}=\tilde x^{\star k}\star\tilde x$; the block is commutative, so the nesting is
immaterial. A root of a central value carries the lower-case xi $\tilde\xi$ of the quaternion layer, a
nilpotent the lower-case nu $\tilde\nu$, and a generic element the letter $\tilde x$.

## The Roots of Zero

### The Reduction

**Theorem (the reduction of the root equation of $0$).** The equation $\tilde\xi\star\tilde\xi=0$ has the
same solutions as the single scalar equation $N(\tilde\xi)=0$.

*Proof.* The square of the block is $\tilde\xi\star\tilde\xi=N(\tilde\xi)e_0$ by the governing formula,
and a multiple of $e_0$ vanishes exactly when its scalar coefficient does.

**Corollary (the vanishing square is the origin).** The elements whose square vanishes are the origin
alone, and there is no nonzero square-zero element of the block:

$$
\{\tilde\xi:\tilde\xi\star\tilde\xi=0\}=\{0\}.
$$

*Proof.* By the reduction the equation is $N(\tilde\xi)=x_0^{2}+x_1^{2}+x_2^{2}+x_3^{2}=0$, a sum of
four squares; a sum of squares vanishes exactly when every square vanishes, that is at
$x_0=x_1=x_2=x_3=0$.

### The Root Set

**Corollary (the root set of $0$).** The root set of the central value $0$ is the singleton $\{0\}$: it
is nonempty, of real dimension zero, and it is the set on which the sum of squares of the coordinates of
the element vanishes.

*Proof.* The preceding corollary gives the set; it is a single point, and a point has dimension zero.

**Remark (the square-zero set and the nilpotent of index two).** The elements whose square vanishes are
the origin alone, so the **square-zero set** of the block is the single point $\{0\}$; since the
definition of a square-zero element requires a nonzero element, the block has no square-zero element and
no nilpotent of index two. The distinction between a nilpotent and a square-zero element is visible in
this block, where the cube and not the square is what vanishes; the point is taken up in §*The
Nilpotents*, and the square-zero sets of the six structures are compared in §*The Comparison with the
Other Real Blocks*.

**Remark (the collapse of the isotropic cone).** In the biquaternion block the roots of $0$ form the
punctured isotropic cone $\{N=0\}\setminus\{0\}$, of complex dimension three, with two families of
generators; over $\mathbb{R}$ the coefficient $N(\tilde\xi)=x_0^{2}+|\vec x|^{2}$ is definite, the
isotropic locus $\{N=0\}$ collapses to the origin, and the punctured cone is empty. The block's
isotropic elements are none but the origin and its radical is $\{0\}$ (*The Radical and the Isotropic
Elements of the Symmetric Quaternionic Algebra*), so the root set of $0$ is a single point and not a
family. The roots of the value $0$ are the extreme case of the reduction of the companion article, whose
general central value $\lambda e_0$ has the root set $\{0\}$ at $\lambda=0$, the empty set for
$\lambda<0$ and the level set $\sqrt{\lambda}\,\mathrm{Sp}(1)$ for $\lambda>0$ (*Square Roots of a
General Element in the Symmetric Quaternionic Algebra*).

## The Powers of an Element

### The Powers Formula

**Theorem (the powers).** For every $\tilde x$ and every $k\geq2$,

$$
\tilde x^{\star k}=N(\tilde x)\,x_0^{\,k-2}\,e_0 .
$$

*Proof.* For $k=2$ this is the square, $\tilde x\star\tilde x=N(\tilde x)e_0$. The induction step uses
$\tilde x^{\star k}\star\tilde x=N(\tilde x)x_0^{k-2}e_0\star\tilde x=N(\tilde x)x_0^{k-2}(x_0e_0)=N(\tilde x)x_0^{k-1}e_0$,
where the middle equality is $e_0\star\tilde x=x_0e_0$; the formula at $k+1$ follows.

**Corollary (all powers from the square on are central).** From the second power on, every power of an
element is a real multiple of $e_0$: the square is $N(\tilde x)e_0$, the cube is $N(\tilde x)x_0e_0$, and
every higher power is $N(\tilde x)x_0^{k-2}e_0$. The vector part of the element disappears at the first
power and never returns.

**Corollary (the vanishing powers).** For an element with $x_0\neq0$ no power vanishes. For a nonzero
pure element the powers are $\tilde x,\ N(\tilde x)e_0,\ 0,\ 0,\dots$, so the cube is the only vanishing
power. The only vanishing power of any element other than the origin is the cube of a nonzero pure
element.

*Proof.* The power formula gives $N(\tilde x)x_0^{k-2}e_0$; the coefficient vanishes exactly when
$N(\tilde x)=0$, that is at $\tilde x=0$, or when $k\geq3$ and $x_0=0$.

### The Square-Zero Elements

**Corollary (the square-zero set).** The square-zero set of the block is the singleton $\{0\}$, and the
block has no nonzero square-zero element; equivalently, the elements whose square vanishes form the
origin alone, as §*The Roots of Zero* states, and the root set of $0$ is that same singleton.

*Proof.* The square is $N(\tilde x)e_0$, and $N(\tilde x)=x_0^{2}+|\vec x|^{2}$ vanishes only at the
origin; the origin has the vanishing square and is the only element that does.

## The Nilpotents

### The Definition and the Criterion

**Definition (nilpotent, square-zero, index).** A **nilpotent** of the block is a **nonzero** element
$\tilde\nu$ with $\tilde\nu^{\star k}=0$ for some $k\geq1$; the least such $k$ is the **index of
nilpotency**. The case $k=2$, $\tilde\nu\star\tilde\nu=0$, is a **square-zero** element, and the case
$k=3$, $\tilde\nu\star\tilde\nu\star\tilde\nu=0$, a **cube-zero** element. The origin satisfies every
power-zero equation, but it is excluded by the definition, which requires a nonzero element.

The vocabulary is quoted from *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the article
reads it on the block.

**Theorem (the nilpotents are the pure elements).** An element $\tilde x$ is a nilpotent of the block if
and only if it is nonzero and pure,

$$
\tilde x\ \text{nilpotent}\iff x_0=0\ \text{and}\ \tilde x\neq0,
$$

that is, if and only if $\tilde x\in\operatorname{Im}\mathbb{H}\setminus\{0\}$. Every nonzero pure
element is a nilpotent of index exactly three.

*Proof.* By the power formula the cube is $\tilde x^{\star3}=N(\tilde x)x_0e_0$. If $x_0=0$ the cube
vanishes, so the index is at most three. If $x_0\neq0$, then
$N(\tilde x)=x_0^{2}+|\vec x|^{2}\geq x_0^{2}>0$, so $N(\tilde x)x_0\neq0$ and the cube is nonzero;
by the formula $N(\tilde x)x_0^{k-2}\neq0$ for every $k\geq2$, so no power vanishes and $\tilde x$ is
not a nilpotent. Hence a nilpotent has $x_0=0$. Conversely a nonzero pure element has
$N(\tilde x)=|\vec x|^{2}>0$, so its square is $N(\tilde x)e_0\neq0$ and its cube is $0$: its index
is exactly three, and not two.

### The Index

**Corollary (the index is three, and is bounded by three).** Every nilpotent of the block has index
exactly three; there is no nilpotent of index two and none of index greater than three. The index is
therefore not bounded by two, and the block is one of the products on which the cube is the first
vanishing power.

*Proof.* The criterion gives that every nilpotent is a nonzero pure element, whose cube vanishes and
whose square does not; an index-two nilpotent would be a nonzero element whose square vanishes, which
§*The Roots of Zero* shows impossible; and a vanishing power of index greater than three would give a
vanishing cube, that is a pure element, whose cube vanishes exactly at index three.

### The Nilpotent Set

**Corollary (the nilpotent set).** The nilpotent set of the block is the punctured vector subspace

$$
\{\text{nilpotents}\}=\{\tilde x:x_0=0,\ \tilde x\neq0\}=\operatorname{Im}\mathbb{H}\setminus\{0\},
$$

the vector subspace
$\operatorname{Im}\mathbb{H}=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ with its origin removed, of real dimension three. Every
nonzero pure element, and only those, is a nilpotent, and each of them has index three.

*Proof.* The criterion gives the set and the index; the vector subspace has real dimension three.

## The Nilpotents against the Other Classes

### The Zero Divisors

**Proposition (against the zero divisors).** Every nilpotent is a zero divisor, since every nonzero
element of the block is a zero divisor (*Zero Divisors of the Symmetric Quaternionic Algebra*); but the
nilpotent set is strictly smaller than the zero-divisor set. The element $e_0$ is a zero divisor,
$e_0\star e_1=0$ with $e_1\neq0$, and it is not a nilpotent, its powers being $e_0$ at every index. So

$$
\operatorname{Im}\mathbb{H}\setminus\{0\}\subsetneq\mathbb{H}\setminus\{0\},
$$

the inclusion being strict at $e_0$.

*Proof.* The nilpotents are the nonzero pure elements, the vector subspace minus its origin; the zero
divisors are all the nonzero elements; $e_0$ is nonzero, central, hence not pure, and it is a zero
divisor by the displayed annihilation.

### The Idempotents

**Proposition (against the idempotents).** The idempotents of the block are $0$ and $e_0$, the
nilpotents are the nonzero pure elements, and the two sets are disjoint. The idempotent $e_0$ is not a
nilpotent, and a nonzero pure element $\tilde\nu$ is not an idempotent, its square $N(\tilde\nu)e_0$
being central while the element is not. The origin is the only element at which the two defining
equations $\tilde x\star\tilde x=\tilde x$ and $\tilde x\star\tilde x=0$ hold together, and it is
excluded from the nilpotent class by the definition.

*Proof.* The idempotents are classified in *Square Roots of One and the Idempotents of the Symmetric
Quaternionic Algebra*; the intersection of the two sets is empty because a pure element is not central
unless it is $0$, and $0$ is an idempotent but is excluded from the nilpotents by the definition; the
two equations together give $\tilde x=0$.

### The Meeting of the Three Classes

**Remark (the meeting of the three classes).** The idempotent set $\{0,e_0\}$, the nilpotent set
$\operatorname{Im}\mathbb{H}\setminus\{0\}$ and the square-zero set $\{0\}$ are pairwise almost disjoint:
the idempotents and the nilpotents meet nowhere, the square-zero set is the origin alone, and the origin
lies in the idempotent set and in the square-zero set but not in the nilpotent set. This is the element-theoretic content of the absence
of a unit and of the definiteness of the coefficient.

## The Conjugation

**Proposition (the single conjugation preserves the class).** Over $\mathbb{R}$ the natural conjugation
${}^{\natural}$ is the only nontrivial conjugation, the star coincides with it and the bar is the
identity. The natural conjugation preserves $x_0$ and $N$, hence preserves the nilpotent set and the
index: $\tilde\nu$ is a nilpotent of index $k$ if and only if $\tilde\nu^{\natural}$ is. The invariance
group of conjugations of the complex chapter collapses here to the invariance under the single natural
sign.

*Proof.* The natural conjugation reverses the vector part and fixes the scalar part, so
$N(\tilde\nu^{\natural})=N(\tilde\nu)$ and the power formula is unchanged; the collapse of the
conjugations is the convention of the real chapter.

## The Matrix Model

**Proposition (the nilpotents in the $2\times2$ model).** In the realization $\mathsf{M}_2$ of *The
Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* the
quaternion $\tilde x$ has the matrix with $\operatorname{Tr}\mathsf{M}_2(\tilde x)=2x_0$ and
$\det\mathsf{M}_2(\tilde x)=N(\tilde x)$. Therefore the nilpotents of the block are exactly the
matrices of the model that are trace-free, that is the images of the pure elements; a nonzero pure
element has a trace-free matrix of determinant $N(\tilde x)>0$ and is a nilpotent of index three; and
the square-zero elements are the trace-free matrices that are also singular, which over $\mathbb{R}$
reduces to the zero matrix, because a nonzero pure element has $N(\tilde x)>0$ while a singular matrix
of the model has $N(\tilde x)=0$ and is the image of the origin.

*Proof.* The trace and the determinant are the invariants of the model; a pure element has $x_0=0$,
hence a trace-free matrix, and $\det=N(\tilde x)=|\vec x|^{2}>0$ for a nonzero pure element, so the
matrix is not singular; a singular matrix of the model has $\det=N(\tilde x)=0$, hence $\tilde x=0$ by
definiteness. The criteria of the preceding sections give the index.

**Remark (the contrast with the complex parent).** In the biquaternion chapter the same model gives the
nilpotents as the matrices that are trace-free or singular, the singular ones being square-zero, of
index two, and the trace-free nonsingular ones of index three. Over $\mathbb{R}$ the singular branch
collapses: the determinant $N(\tilde x)$ is definite, the singular matrices of the model reduce to the
zero matrix, and only the trace-free branch survives.

## The Comparison with the Other Real Blocks

**Remark (the four square-zero sets).** The square-zero set is $\{0\}$ for the four structures of the
real chapter whose square vanishes only at the origin — the general and the
symmetric plain and the general and the symmetric quaternionic — and it is the whole space for the two
antisymmetric structures, whose squares vanish identically and whose nilpotent class is therefore the
whole space apart from the origin (*Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*;
*Square Roots of Zero and the Nilpotents of the General Plain Algebra*; *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*). Within the
four, the symmetric quaternionic block is distinguished by its nilpotent class: it is the one of the
four with a nonzero nilpotent family, the pure quaternions of index three, the other three having no
nonzero nilpotent. The distinction between a nilpotent and a square-zero element is therefore visible in
this block and invisible in the other three: here the cube, and not the square, is what vanishes.

## Summary

The powers of the symmetric quaternionic block obey $\tilde x^{\star k}=N(\tilde x)x_0^{k-2}e_0$ from
the square on, so the cube vanishes exactly on the pure elements and no higher power vanishes off the
origin. The roots of $0$ are the origin alone, since the square is the definite form
$N(\tilde x)e_0=(x_0^{2}+|\vec x|^{2})e_0$ and a sum of squares vanishes only at the origin; the
square-zero set is the single point $\{0\}$, there is no nonzero square-zero element, and the block has
no nilpotent of index two. The nilpotents are the nonzero pure quaternions,
$\operatorname{Im}\mathbb{H}\setminus\{0\}$, each of index exactly three; there is no nilpotent of index
two and none of index greater than three. The nilpotent set is strictly contained in the zero-divisor
set, the strictness witnessed by $e_0$, which annihilates $e_1$ and has no vanishing power; the
nilpotents and the idempotents are disjoint, and the origin is the only element at which the defining
equations of the three classes of element come together. In the $2\times2$ model the nilpotents are the
trace-free matrices, and the singular matrices of the model reduce to zero; over $\mathbb{R}$ the
singular branch of the complex chapter collapses, and the trace-free branch alone survives.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde x\star\tilde x=N(\tilde x)e_0$ | the square of the block, always central |
| $N(\tilde x)=x_0^{2}+|\vec x|^{2}$ | the definite quaternion form, the coefficient of the square |
| $\{\tilde\xi:\tilde\xi\star\tilde\xi=0\}=\{0\}$ | the root set of $0$, the square-zero set |
| $\tilde x^{\star k}=N(\tilde x)x_0^{k-2}e_0$, $k\geq2$ | the powers of the block |
| nilpotent $\tilde\nu$ | nonzero $\tilde x$ with $\tilde x^{\star k}=0$; here the nonzero pure elements |
| $\operatorname{Im}\mathbb{H}\setminus\{0\}$ | the nilpotent set, the punctured vector subspace |
| index three | the index of every nonzero pure element |
| $x_0\neq0$ | no vanishing power |
| $\mathbb{H}\setminus\{0\}$ | the zero-divisor set, which contains the nilpotent set strictly |
| $\operatorname{Tr}\mathsf{M}_2=2x_0$, $\det\mathsf{M}_2=N(\tilde x)$ | the matrix invariants; nilpotent $\iff$ trace-free |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the product $\star$, its scalar law and the form $N$
- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the nilpotent, the square-zero element and the index of nilpotency
- *Norm and Invertibility in the Symmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the definite form whose vanishing decides the square-zero set
- *Square Roots of a General Element in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the level sets of the diagonal and the radicand zero
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), the companion, for the roots of $+e_0$, the roots of $-e_0$ and the idempotents
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the maximal zero-divisor set that contains the nilpotent set strictly
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the vanishing radical and the isotropic locus, the origin alone
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), where the powers and the nilpotent class are collected
- *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-quaternioid.md`), for the realization $\mathsf{M}_2$, its trace and its determinant
- *Square Roots of Zero and the Nilpotents of the General Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra.md`) and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-algebra-of-quaternioid.md`), for the square-zero sets of the other division blocks of the real chapter
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for nilpotents, the index of nilpotency and the trace-free matrices.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the quaternion matrices, their trace and their determinant.
