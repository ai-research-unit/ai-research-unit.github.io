# __Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra__

## Introduction

In the symmetric quaternionic block the square of an element is a scalar multiple of $e_0$, and the
multiple is the quaternion form:

$$
\tilde x\star\tilde x=N(\tilde x)e_0=\bigl(x_0^{2}+|\vec x|^{2}\bigr)e_0 .
$$

This article reads the two classes of element that the squaring map of the block keeps or returns: the
**square roots of the central value $+e_0$**, the elements the map sends to $e_0$, and the
**idempotents**, the elements the map keeps on their own square. In the plain product of the same space
both classes are large, the roots of $+1$ indexing the idempotents by the halving map; in the block the
same reduction is one scalar equation in the four coordinates and both classes are small: the root set
of $+e_0$ is the level set $\{N=1\}$, the unit sphere $\mathrm{Sp}(1)$ of real dimension three, and the
idempotents are the two central elements $0$ and $e_0$.

The whole problem is decided by one identity. The square of every element of the block is the central
element $N(\tilde x)e_0$, so the root equation of the value $\lambda$ reduces to the single real equation
$N(\tilde x)=\lambda$, and the idempotent equation collapses to a quadratic on the scalar line. The
general definition of a **square root of a central value** and of an **idempotent**, and the definition
of the orthogonality and of the complement of an idempotent, are *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*; the product, its scalar law and the definiteness of
its coefficient are *Introduction to the Symmetric Quaternionic Algebra of Quaternions*.

**The results.** The roots of $+e_0$ in the block are the elements of the level set $N=1$, the unit
sphere $\mathrm{Sp}(1)$ of the quaternion algebra, of real dimension three; they contain the central
pair $\pm e_0$, the units $e_1,e_2,e_3$ and their negatives, and every element $x_0e_0+\vec x$ with
$x_0^{2}+|\vec x|^{2}=1$, and they are the orbit of $e_0$ under the group $\mathrm{Sp}(1)$ of the
parent plain product. The idempotents of the block are $0$ and $e_0$ alone, and the block has no
non-trivial idempotent. The two sets are not related by the halving map that carries the roots of $+1$
onto the idempotents of the parent: the map $\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ produces an
idempotent only at $\tilde\xi=\pm e_0$, and every other root of $+e_0$ is sent out of the idempotent
set. On the operator side the idempotent $e_0$ gives the projection $E=L_{e_0}$ onto the centre along the
vector subspace, which is not the identity, the block having no unit; the idempotent endomorphisms form
a strictly larger family, treated in *The Specificities of the Symmetric Quaternionic Algebra*. The
roots of $-e_0$ are empty, and they are quoted in one paragraph at the end of the roots-of-one part and
used nowhere below.

**Boundaries.** The product, the square and the form are *Introduction to the Symmetric Quaternionic
Algebra of Quaternions* and *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*;
the roots of $0$ and the nilpotents of the block are *Square Roots of Zero and the Nilpotents of the
Symmetric Quaternionic Algebra*, the companion of this article; the roots of a general central value,
with the classification by the sign, are *Square Roots of a General Element in the Symmetric Quaternionic
Algebra*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Algebra*; the diagonal and
the non-isotropic class are *Norm and Invertibility in the Symmetric Quaternionic Algebra*; the operator
theory and the idempotent endomorphisms are *The Multiplication Operators of the Symmetric Quaternionic
Algebra*; the collected element classes are *The Specificities of the Symmetric Quaternionic Algebra*.
The parent's continuum of idempotents, over the complexified plain product, is *Square Roots of One and
the Idempotents of the General Plain Algebra*; the twin of this article in the biquaternion chapter is
its namesake, which records the same pair $\{0,e_0\}$ for the block over $\mathbb{C}$ and locates the
continuum in the parent.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1e_2=e_3$; an element is $\tilde x=x_0e_0+\vec x$, with
$\vec x=x_1e_1+x_2e_2+x_3e_3$. The **quaternion conjugation** is
$\tilde x^{\natural}=x_0e_0-\vec x$; on $\mathbb{R}$ the bar is the identity and the star coincides
with the natural sign ${}^{\natural}$. The **quaternion form** is
$N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$, with diagonal
$N(\tilde x)=x_0^{2}+|\vec x|^{2}=(x_0,x_1,x_2,x_3)\cdot(x_0,x_1,x_2,x_3)$, and the **symmetric
quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$. The centre is the scalar line
$\mathbb{R}e_0$ and the vector subspace is
$\mathrm{Vect}(\mathbb{H})=\operatorname{Im}\mathbb{H}=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$. A
root of a central value carries the lower-case xi $\tilde\xi$ of the quaternion layer, an idempotent the
lower-case pi $\tilde\pi$, and a generic element the letter $\tilde x$; the vector part of a root is written $\vec\xi$.

## The Square and Its Reduction

**Proposition (the square and its polarisation).** For every $\tilde x$,

$$
\tilde x\star\tilde x=N(\tilde x)e_0=\bigl(x_0^{2}+x_1^{2}+x_2^{2}+x_3^{2}\bigr)e_0,
$$

and the square is the polarisation of the form on the diagonal,
$2N(\tilde p,\tilde q)e_0=\tilde p\star\tilde p+\tilde q\star\tilde q-(\tilde p-\tilde q)\star(\tilde p-\tilde q)$.

*Proof.* The first display is the governing formula $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$ at
$\tilde p=\tilde q=\tilde x$, and the diagonal of the form is the sum of the four squares. For the
polarisation, the block is $\mathbb{R}$-bilinear and commutative, so
$(\tilde p+\tilde q)\star(\tilde p+\tilde q)$ expands as
$\tilde p\star\tilde p+2\,\tilde p\star\tilde q+\tilde q\star\tilde q$, and the square of
$\tilde p-\tilde q$ is the same display with the middle sign reversed; subtracting the two displays
gives the stated identity.

**Corollary (the square is nonnegative).** Every square of the block is a nonnegative multiple of
$e_0$, and the only element whose square vanishes is the origin: the map
$\tilde x\mapsto N(\tilde x)$ is a sum of four squares.

*Proof.* $N(\tilde x)=x_0^{2}+|\vec x|^{2}\geq0$, and a sum of squares vanishes only when every
coordinate vanishes.

**Theorem (the reduction of the root equation).** Let $\lambda$ be real. The equation
$\tilde\xi\star\tilde\xi=\lambda e_0$ has the same solutions as the single scalar equation
$N(\tilde\xi)=\lambda$, so the root set of the central value $\lambda e_0$ is the level set
$\{\tilde\xi:N(\tilde\xi)=\lambda\}$ of the diagonal of the form.

*Proof.* The left side of the equation is $N(\tilde\xi)e_0$ by the square formula, and two elements of
$\mathbb{H}$ written in the basis $e_0,e_1,e_2,e_3$ are equal exactly when their four coordinates are
equal; a multiple of $e_0$ is the central value with that scalar and vanishing vector part, so the
equation is the single equation on the scalar.

The reduction is the lever of the article: a root equation in four real unknowns is one real equation,
and its solution set is a level set of the form.

## The Roots of One

### The Level Set of Plus One

**Theorem (the roots of $+e_0$).** The solutions of $\tilde\xi\star\tilde\xi=e_0$ are the elements of
the level set at $1$ of the definite form,

$$
\{\tilde\xi:\tilde\xi\star\tilde\xi=e_0\}=\{\tilde\xi:N(\tilde\xi)=1\}=\mathrm{Sp}(1),
$$

the set of unit quaternions of the algebra; it is nonempty, it is the level set of the one polynomial
condition $N(\tilde\xi)=1$, and it is a real algebraic set of real dimension $3$.

*Proof.* By the reduction the equation is $N(\tilde\xi)=1$. The element $e_0$ satisfies $N(e_0)=1$, so
the set is nonempty; the condition is not the condition $0=0$, and the level set is cut by that one
condition on the four coordinates, so its real dimension is the dimension of the ambient space, four,
minus one. The set is stable under the plain product by the multiplicativity
$N(\tilde p\tilde q)=N(\tilde p)N(\tilde q)$, so it is the group of unit quaternions.

**Corollary (the members of the class).** The root set contains the two central roots $\pm e_0$, the
three units $e_1,e_2,e_3$ and their negatives, and every element $x_0e_0+\vec x$ with
$x_0^{2}+|\vec x|^{2}=1$; read over the vector part, it is the two graphs
$x_0=\pm\sqrt{1-|\vec x|^{2}}$ over the set $|\vec x|\leq1$ of the vector subspace.

*Proof.* $N(e_0)=N(e_k)=1$ for the four units, and $N(-\tilde x)=N(\tilde x)$ for the sign; the
displayed elements are exactly the elements with $N(\tilde x)=1$, and solving for $x_0$ gives the two
graphs, which meet at the set $|\vec x|=1$ of the vector subspace.

**Remark (the root set is the unit group of the parent, not a group of the block).** The level set
$\{N=1\}$ is the group $\mathrm{Sp}(1)$ of unit quaternions under the plain product of $\mathbb{H}$, of
real dimension three; the two forms and the plain product are those of *The 2 Forms over the Quaternion
$\mathbb{R}$ Space*. For the block it is the root set of $+e_0$ and nothing more: the block has no two-sided
unit and no inverse (*The Specificities of the Symmetric Quaternionic Algebra*), so its roots of $+e_0$
are not units of the block, and the group law they carry is the group law of the parent and not of the
product $\star$.

### The Free Parameters

**Corollary (the roots of $+e_0$ as an orbit).** The root set of $+e_0$ is the orbit of the canonical
root $e_0$ under multiplication by the unit quaternions in the parent plain product: every root is
$\tilde\xi=\tilde u$ with $\tilde u\in\mathrm{Sp}(1)$, and the three coordinates of the vector part of
$\tilde u$, subject to $x_0^{2}+|\vec x|^{2}=1$, are the three free parameters of the solution.

*Proof.* The root set is $\{N=1\}=\mathrm{Sp}(1)$, and $\tilde u\cdot e_0=\tilde u$ in the parent plain
product, so the orbit is the whole set; the parameters are the coordinates of the vector part, with the
scalar coordinate determined up to sign by the condition $N(\tilde\xi)=1$.

**Remark (the same reduction, the general central value).** The reduction is stated for an arbitrary
real $\lambda$ and is the content of the companion article on the general element: the equation
$\tilde\xi\star\tilde\xi=\lambda e_0$ has the root set $\{0\}$ for $\lambda=0$, the empty set for
$\lambda<0$, and the level set $\{N=\lambda\}=\sqrt{\lambda}\,\mathrm{Sp}(1)$, of real dimension three,
for $\lambda>0$ (*Square Roots of a General Element in the Symmetric Quaternionic Algebra*). The value
$+1$ is the case $\lambda=1$, whose level set is the root set of this article; the value $0$ is the
subject of the companion article on the nilpotents.

### The Roots of Minus One

**The roots of minus one.** A **central imaginary**, an element $i$ of the centre with $i^{2}=-e_0$,
would flip the sign of a central value by multiplication,
$(i\tilde\xi)\star(i\tilde\xi)=i^{2}(\tilde\xi\star\tilde\xi)=-\tilde\xi\star\tilde\xi$. Over
$\mathbb{R}$ the centre is the scalar line $\mathbb{R}e_0$ and no central element has square $-e_0$, so
no such flip exists and the roots of $-e_0$ are **not** the image of the roots of $+e_0$. They follow from the same reduction, and the reduction gives the empty set: a square
of the block is a nonnegative multiple of $e_0$, $N(\tilde\xi)\ge0$, and no element squares to the
negative central element $-e_0$. The class is empty, it is quoted here and used nowhere below, and in
particular no idempotent of the block arises from a root of $-e_0$.

## The Idempotents

### The Definition and the Equation

**Definition (idempotent).** An **idempotent** of the block is an element $\tilde\pi$ with
$\tilde\pi\star\tilde\pi=\tilde\pi$. Two idempotents are **orthogonal** when their products vanish, and
the **complement** of an idempotent is defined only when the rule has a two-sided unit, the complement
of $\tilde\pi$ being $e-\tilde\pi$. The set of the idempotents contains $0$ and every two-sided unit;
an idempotent different from $0$ is **non-trivial**.

The definition is quoted from *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the block has
no two-sided unit, so the complement and a complete orthogonal system are not available in it.

### The Classification

**Theorem (the idempotents).** An element $\tilde\pi$ satisfies
$\tilde\pi\star\tilde\pi=\tilde\pi$ if and only if $\tilde\pi\in\{0,e_0\}$.

*Proof.* The square of the block is
$\tilde\pi\star\tilde\pi=N(\tilde\pi)e_0=(x_0^{2}+|\vec x|^{2})e_0$, while
$\tilde\pi=x_0e_0+\vec x$; the equality of the two elements forces the vector part of the right-hand
side to vanish, hence $\vec x=0$, and then the scalar equation $x_0^{2}=x_0$, whose solutions are
$x_0=0$ and $x_0=1$. Both values are idempotents: $0\star0=0$ and
$e_0\star e_0=N(e_0)e_0=e_0$.

**Corollary (no non-trivial idempotent).** The block has exactly two idempotents, and both are central.
There is no idempotent in the vector subspace and none outside the centre; every idempotent of the block
lies on the scalar line.

*Proof.* The classification gives the pair, and the scalar line is the centre.

**Remark (the same pair, reached differently in the companion block).** The symmetric plain algebra has
the same two idempotents, $0$ and $e_0$, but reaches them by the square of the plain product and not by
the diagonal of the form; the block's proof is short because its square is scalar, the vector part being
annihilated at the first step (*The Square, the Idempotents and the Jordan Inverse of the Symmetric
Plain Algebra*).

### The Halving Map and Its Failure

**Proposition (the halving map on the roots of $+e_0$).** Let $\tilde\xi$ be a root of $+e_0$ and put
$\tilde\pi=\tfrac12(e_0+\tilde\xi)$. Then

$$
\tilde\pi\star\tilde\pi=\tfrac14\bigl(1+2\xi_0+N(\tilde\xi)\bigr)e_0=\tfrac14(2+2\xi_0)e_0=\tfrac{1+\xi_0}{2}e_0 ,
$$

the element $\tilde\pi$ is idempotent exactly when $\tilde\xi=\pm e_0$, and then $\tilde\pi$ is $e_0$
for $\tilde\xi=e_0$ and $0$ for $\tilde\xi=-e_0$.

*Proof.* The square is computed from the governing formula,
$N(\tilde\pi)=\tfrac14N(e_0+\tilde\xi)=\tfrac14(1+2\xi_0+N(\tilde\xi))$, and $N(\tilde\xi)=1$ at a root;
so $\tilde\pi\star\tilde\pi=\tfrac{1+\xi_0}{2}e_0$. But the element $\tilde\pi$ itself is
$\tfrac{1+\xi_0}{2}e_0+\tfrac12\vec\xi$, which is a multiple of $e_0$ only when
$\vec\xi=0$; then $N(\tilde\xi)=\xi_0^{2}=1$, so $\xi_0=\pm1$, and the two values give
$\tilde\pi=e_0$ and $\tilde\pi=0$. The identity $\tilde\pi\star\tilde\pi=\tilde\pi$ therefore holds
exactly at $\tilde\xi=\pm e_0$.

**Corollary (the failure of the bijection).** The halving map is a map from the roots of $+e_0$ onto
the idempotents of the block only at the two central roots: a noncentral root of $+e_0$, for instance
$\tilde\xi=e_1$, gives $\tilde\pi=\tfrac12(e_0+e_1)$ with
$\tilde\pi\star\tilde\pi=\tfrac12e_0\neq\tilde\pi$, and the difference is the vector part
$\tfrac12e_1$. The map is not injective onto the idempotent set and not a bijection of the two classes;
the failure is the failure of the centrality of $\tilde\pi$.

*Proof.* The proposition gives that only $\tilde\xi=\pm e_0$ reach an idempotent, and both roots of
$+e_0$ that are central give idempotents; the two classes have three dimensions and two points, so no
bijection exists and the displayed witness shows the failure element by element.

**Remark (the parent's continuum has no counterpart).** In the parent plain product the halving map
$\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ is a bijection from the roots of $+e_0$ onto the idempotents,
and the roots of $-e_0$ feed the continuum $\tfrac12(e_0+\tilde\Xi i)$ of idempotents, of real dimension
four, the complexified plain algebra carrying the imaginary coordinate $i$ (*Square Roots of One and the
Idempotents of the General Plain Algebra*). Over $\mathbb{R}$ the coordinate $i$ is gone, the block has no root of $-e_0$ at all,
and of the roots of $+e_0$ only the two central ones reach an idempotent; both the bijection and the
continuum are absent, and the two idempotents of the block are the two degenerate images $\tilde\xi=\pm e_0$.
The biquaternion twin *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*
records the same pair $\{0,e_0\}$ for the block over $\mathbb{C}$, the continuum being the parent's and
not the block's.

### The Idempotents as Projections

**Definition (left multiplication).** For an element $\tilde x$ the **left multiplication** is the
endomorphism $L_{\tilde x}$ of $\mathbb{H}$ given by
$L_{\tilde x}(\tilde y)=\tilde x\star\tilde y=N(\tilde x,\tilde y)e_0$.

**Theorem (the operator of an idempotent).** For every $\tilde x$ the operator $L_{\tilde x}$ has the
square $L_{\tilde x}^{2}=x_0L_{\tilde x}$, so it is idempotent exactly when $\tilde x=0$ or when
$x_0=1$; among the nonzero elements, exactly the elements of scalar coordinate $1$. The idempotent
element $e_0$ gives the operator

$$
L_{e_0}=E:\tilde y\mapsto y_0e_0,
$$

the projection onto the centre along the vector subspace: $E^{2}=E$, the image of $E$ is
$\mathbb{R}e_0$, its kernel is $\mathrm{Vect}(\mathbb{H})$, and it is not the identity.

*Proof.* The composition is
$L_{\tilde x}(L_{\tilde x}\tilde y)=N(\tilde x,y_0e_0)e_0=x_0y_0e_0=x_0L_{\tilde x}\tilde y$, using
$N(\tilde x,e_0)=x_0$; hence $L_{\tilde x}^{2}=x_0L_{\tilde x}$, which equals $L_{\tilde x}$ exactly
when $x_0=1$ or when $L_{\tilde x}=0$, the latter only at $\tilde x=0$. For $\tilde x=e_0$ the operator
is $E(\tilde y)=N(e_0,\tilde y)e_0=y_0e_0$, with the image and the kernel displayed; it is not the
identity because $E(e_1)=0\neq e_1$, the block having no unit.

**Remark (idempotent elements against idempotent endomorphisms).** The idempotent elements are only $0$
and $e_0$, and their operators are the zero operator and $E$. The idempotent **endomorphisms** of the
block are a different and larger family, made of the zero operator $L_0$ together with the operators
$L_{\tilde x}$ of scalar coordinate $1$; the latter form a hyperplane, parallel to the vector subspace,
of pairwise distinct rank-one projections onto the centre, and they are classified in *The
Multiplication Operators of the Symmetric Quaternionic Algebra*. The two families are not the same, and
the distinction is kept in *The Specificities of the Symmetric Quaternionic Algebra*.

### The Absent Peirce Decomposition and the Absent Classification of the Zero Divisors

**Proposition (no classification of the zero divisors by idempotents).** Every nonzero element of the
block is a zero divisor, the zero-divisor set being the whole punctured space
$\mathbb{H}\setminus\{0\}$ (*Zero Divisors of the Symmetric Quaternionic Algebra*); the block has only
the two trivial idempotents, so no idempotent can distinguish one zero divisor from another. The
classification by non-trivial idempotents is empty because the idempotents are trivial, while the
zero-divisor set is maximal: the two extremes occur together.

*Proof.* The idempotents are $0$ and $e_0$, so a classification by non-trivial idempotents has no
entry; the zero-divisor set is the punctured space, which contains every nonzero element.

**Remark (the absent complementation and the absent Peirce decomposition).** The complementation
$\tilde\pi\mapsto e_0-\tilde\pi$ and the orthogonality of idempotents are not defined for the block: the
complement of an idempotent requires a two-sided unit, and the block has none. The two idempotents do
satisfy $0\star e_0=0$, but there is no complete orthogonal system of idempotents and no Peirce
decomposition; the available splitting

$$
\mathbb{H}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})
$$

is the image–kernel splitting of the operator $E$ and not a decomposition into corner algebras. This is
the idempotent reading of the absence of a unit, and it is the reason the block has no idempotent
calculus beyond its two elements.

## Summary

The square of the block is the definite form, $\tilde x\star\tilde x=N(\tilde x)e_0$, nonnegative at
every element and vanishing only at the origin, so the root equation of a central value reduces to the
single scalar equation $N(\tilde x)=\lambda$. The roots of $+e_0$ are the level set $\{N=1\}$, the unit
sphere $\mathrm{Sp}(1)$ of the quaternion algebra, of real dimension three; it contains the central pair
$\pm e_0$, the units $e_1,e_2,e_3$ and their negatives, and every element with $N(\tilde x)=1$, and it is the
orbit of $e_0$ under the group of unit quaternions of the parent plain product, with three free
parameters. The roots of $-e_0$ are empty: over $\mathbb{R}$ the centre has no element of square
$-e_0$, so the sign of a central value cannot be flipped by a central imaginary, and no element squares
to the negative central value.

The idempotents of the block are exactly $0$ and $e_0$: the equation
$\tilde\pi\star\tilde\pi=N(\tilde\pi)e_0=\tilde\pi$ forces the vector part of $\tilde\pi$ to vanish and
the scalar part to satisfy $\pi_0^{2}=\pi_0$, so both idempotents are central and there is no non-trivial
one. The continuum of idempotents of the complexified parent plain algebra, the family
$\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$, has no counterpart in the block: the
halving map $\tilde\pi=\tfrac12(e_0+\tilde\xi)$ carries no root of $-e_0$, because the block has none,
and of the roots of $+e_0$ only the two central ones, $\pm e_0$, to the pair $e_0$ and $0$; a noncentral
root gives only a scalar square and not an idempotent. The idempotent $e_0$ acts by the projection $E$
onto the centre along the vector subspace, which is not the identity, and the idempotent endomorphisms
are a strictly larger family than the idempotent elements. The block has no Peirce decomposition, no
complementation and no classification of the zero divisors by idempotents; the complementation and the
orthogonality that the parent's theory uses require the unit that the block does not have.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde x\star\tilde x=N(\tilde x)e_0$ | the square of the block, always central |
| $N(\tilde x)=x_0^{2}+|\vec x|^{2}$ | the definite quaternion form, the coefficient of the square |
| $\{\tilde\xi:\tilde\xi\star\tilde\xi=e_0\}=\{N=1\}=\mathrm{Sp}(1)$ | the roots of $+e_0$, the unit sphere of real dimension three |
| $\tilde\xi=\tilde u$, $\tilde u\in\mathrm{Sp}(1)$ | the roots of $+e_0$ as an orbit, with three free parameters |
| $\{\tilde\xi:\tilde\xi\star\tilde\xi=-e_0\}=\varnothing$ | the roots of $-e_0$, empty by definiteness |
| $\{\tilde\pi:\tilde\pi\star\tilde\pi=\tilde\pi\}=\{0,e_0\}$ | the idempotents of the block |
| $\tilde\pi=\tfrac12(e_0+\tilde\xi)$ | the halving map, idempotent only at $\tilde\xi=\pm e_0$ |
| $L_{\tilde x}^{2}=x_0L_{\tilde x}$ | the square of a left multiplication |
| $E=L_{e_0}:\tilde y\mapsto y_0e_0$ | the projection onto the centre, not the identity |
| $\mathbb{H}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})$ | the image–kernel splitting of $E$, not a Peirce decomposition |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the product $\star$, its scalar law and the form $N$
- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the square root of a central value, the idempotent, the orthogonality and the complement
- *Square Roots of a General Element in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the general central value and the classification by the sign
- *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), the companion, for the value $0$ and the nilpotents
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the maximal zero-divisor set that makes the classification by idempotents vacuous
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the operators $L_{\tilde x}$, the projection $E$ and the idempotent endomorphisms
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), where the idempotents and the nilpotents are collected
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra-of-quaternioid.md`), for the same pair reached by the plain square
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.md`), the complexified parent, for the continuum $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra.md`), the biquaternion twin, which records the same pair $\{0,e_0\}$ and locates the continuum in the parent
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), for the quaternion form $N$ and the plain form
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, orthogonality and the Peirce decomposition.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, Universitext, 2004), for the flexibility and power-associativity of a symmetric product.
