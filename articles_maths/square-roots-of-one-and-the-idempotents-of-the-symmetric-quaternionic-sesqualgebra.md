# __Square Roots of One and the Idempotents of the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article reads two subjects of the block, the symmetric quaternionic sesquilinear product
$\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*, and in this order. The first is
the square roots of the central value $+1$, the elements $\tilde\Xi$ of
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with

$$
\tilde\Xi\star\tilde\Xi=e_0 .
$$

The second is the idempotents of the block, the elements $\tilde\Pi$ with
$\tilde\Pi\star\tilde\Pi=\tilde\Pi$.

In an associative algebra with a unit the two subjects are one, because the **halving map**
$\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents. The
block is not associative, and the map fails here: it carries the roots of $+1$ to idempotents only at the
two trivial roots $\pm e_0$. The two classes are therefore classified independently, each from the diagonal
of the block, and the failure of the map is stated and used nowhere.

The root is relative to a product, and the product is part of the definition: it is stated once for a
general product in *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the
Roots*, and the definition of an idempotent, with the orthogonal, complete and primitive families and the
Peirce decomposition, is the same article, §*The Idempotent, the Projection and the Peirce Decomposition*.
The unqualified word means the block.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the diagonal
$\tilde Q\star\tilde Q$ is *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic
Sesqualgebra*; the zero divisors and the regular elements are *Zero Divisors of the Symmetric Quaternionic
Sesqualgebra*; the roots of $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents of the
Symmetric Quaternionic Sesqualgebra*; the roots of a general value are *Square Roots of a General Element in
the Symmetric Quaternionic Sesqualgebra*; and the same classes in the plain product are *Square Roots of One
and the Idempotents of the General Plain Algebra*, where the halving map is a bijection.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\mathbf Q=\sum_kQ_ke_k$; $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes the coefficients, ${}^{*}={}^{\natural}\circ\bar{\cdot}$; and
$\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ is the real quaternion
subspace. The diagonal is
$\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf Q}-\overline{Q_0}\mathbf Q$ with
$K(\tilde Q,\tilde Q)=|Q_0|^2-\sum_k|Q_k|^2$, and it is a real quaternion for every $\tilde Q$. The
**central square** is $C(\tilde Q)=\sum_\mu Q_\mu^2$, the scalar of $\tilde Q\tilde Q^{\natural}=C(\tilde Q)e_0$.
A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), an
idempotent $\tilde\Pi$ (§*The Idempotent Convention*), and a generic element $\tilde P$ or $\tilde Q$.
Throughout this article the product is the block.

**The results.** The roots of $+1$ are the family $\mathcal R_{+1}$ of the elements
$\alpha e_0+\tfrac{i\alpha}{|\alpha|^2}\mathbf c$ with $\alpha\in\mathbb{C}^{\times}$, $|\alpha|\geq1$,
$\mathbf c\in\mathbb{R}^3$ and $\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2-1)$, of real dimension four;
there is no pure root of $+1$, and $e_0$ is the case $\alpha=1$, $\mathbf c=\mathbf 0$. The central imaginary
does not turn the roots of $+1$ into the roots of $-1$, because the product is sesquilinear and
$(i\tilde\Xi)\star(i\tilde\Xi)=\tilde\Xi\star\tilde\Xi$; the roots of $-1$ are separately the pure unit
vectors together with the family $\mathcal R_{-1}$, of real dimension five. The idempotents are $0$, $e_0$
and the family $-\tfrac12e_0+\boldsymbol\mu$ with $\boldsymbol\mu\in\mathbb{R}^3$ and
$\lVert\boldsymbol\mu\rVert^2=\tfrac34$, a two-sphere of radius $\tfrac{\sqrt3}{2}$ in the real quaternion
subspace. Every nonzero idempotent has central square $C(\tilde\Pi)=1$ and is regular, so no nonzero
idempotent is a zero divisor; no two nontrivial idempotents are orthogonal; and the two classes meet only at
$e_0$.

## The Roots of One

**The roots of $+1$ in the block are the elements $\alpha e_0+\tfrac{i\alpha}{|\alpha|^2}\mathbf c$ with
$\alpha\in\mathbb{C}^{\times}$, $|\alpha|\geq1$ and $\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2-1)$; there
is no pure root of $+1$, and $e_0$ is the case $\alpha=1$, $\mathbf c=\mathbf 0$.**

A **root of $+1$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi\star\tilde\Xi=e_0$, the square
being the one of the block.

### The Reduction

Let $\tilde\Xi=\alpha e_0+\mathbf x$ with $\alpha\in\mathbb{C}$ and $\mathbf x\in\mathbb{C}^3$. The diagonal
formula of the block is

$$
\tilde\Xi\star\tilde\Xi=K(\tilde\Xi,\tilde\Xi)e_0-2\,\mathrm{Re}\bigl(\alpha\overline{\mathbf x}\bigr),
\qquad K(\tilde\Xi,\tilde\Xi)=|\alpha|^2-\lVert\mathbf x\rVert^2,
$$

whose scalar part is real and whose vector part is a real vector. The right-hand side $e_0$ is central, so the
equation splits into the vector condition $\alpha\overline{\mathbf x}\in i\mathbb{R}^3$ and the scalar
condition $K(\tilde\Xi,\tilde\Xi)=1$. When the vector condition holds, $\alpha\overline{x_k}=-ic_k$ with
$c_k\in\mathbb{R}$, that is $x_k=i\alpha c_k/|\alpha|^2$ for $\alpha\neq0$, so
$\lVert\mathbf x\rVert^2=\lVert\mathbf c\rVert^2/|\alpha|^2$ and the scalar condition reads

$$
\lVert\mathbf c\rVert^2=|\alpha|^2\bigl(|\alpha|^2-1\bigr).
$$

This single real equation on the modulus of $\mathbf c$ is the whole reduction, and the same reduction serves
the roots of $0$ and the roots of $-1$.

### The Root Set

If $\alpha=0$ the vector condition holds automatically and the scalar condition reads
$-\lVert\mathbf x\rVert^2=1$, impossible; so there is no pure root of $+1$, in contrast with the plain
product, where the vector subspace carries the involutions.

Let $\alpha\neq0$. The equation $\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2-1)$ has a real solution
$\mathbf c$ exactly when its right-hand side is non-negative, that is $|\alpha|\geq1$, and for each
admissible $\alpha$ the parameter $\mathbf c$ runs over the sphere of radius
$|\alpha|\sqrt{|\alpha|^2-1}$ in $\mathbb{R}^3$.

### Statement of the Theorem

**Theorem (the roots of $+1$).** The roots of $+1$ in the block are the elements

$$
\tilde\Xi=\alpha e_0+\frac{i\alpha}{|\alpha|^2}\mathbf c,
\qquad
\alpha\in\mathbb{C}^{\times},\quad
|\alpha|\geq1,\quad
\mathbf c\in\mathbb{R}^3,\quad
\bigl\lVert\mathbf c\bigr\rVert^2=|\alpha|^2\bigl(|\alpha|^2-1\bigr).
$$

There is no pure root of $+1$.

### Verification

Each element of the display is a root of $+1$. The centrality holds because
$\alpha\overline{x_k}=-ic_k$ is purely imaginary for each $k$, and the scalar condition holds because

$$
K(\tilde\Xi,\tilde\Xi)=|\alpha|^2-\frac{\lVert\mathbf c\rVert^2}{|\alpha|^2}
=|\alpha|^2-\bigl(|\alpha|^2-1\bigr)=1 .
$$

Conversely the reduction shows that no other element is a root.

### Status of the Roots

Counting the free real parameters, the roots of $+1$ are a real manifold of dimension four: the admissible
$\alpha$ are the complement of the open unit disc in the complex line, of real dimension two, and the sphere
of $\mathbf c$ has real dimension two.

The unit candidate $e_0$ is the case $\alpha=1$, $\mathbf c=\mathbf 0$. Every root of $+1$ has $\alpha\neq0$,
so no root of $+1$ is a pure element and the vector subspace carries none; the root set meets the
idempotents only at $e_0$, as §*The Halving Map and the Roots of One* records.

**The roots of minus one.** The central imaginary does not turn the roots of $+1$ into the roots of $-1$
here. The product is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$: in $(i\tilde\Xi)\star(i\tilde\Xi)$ the
factor $i$ of the first slot passes through the product and the factor $i$ of the second slot is conjugated,
so the two cancel and $(i\tilde\Xi)\star(i\tilde\Xi)=\tilde\Xi\star\tilde\Xi$, with no sign change. The
roots of $-1$ are read from the same reduction as the disjoint union of the pure unit vectors
$\lVert\boldsymbol\Xi\rVert^2=1$, a real five-sphere, and the non-pure family $\mathcal R_{-1}$ with
$\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2+1)$, of real dimension four, so the root set of $-1$ has real
dimension five: the pure elements $e_1$, $e_2$ and $ie_1$ have $\lVert\boldsymbol\Xi\rVert^2=1$ and are roots
of $-1$, while the pure $e_1+ie_2$, of $\lVert\boldsymbol\Xi\rVert^2=2$, is a root of $-2$ and not of $-1$.
The roots of $-1$ are quoted here and are used nowhere in this article.

## The Idempotents

**Every idempotent of the block is $0$, $e_0$, or of the form $-\tfrac12e_0+\boldsymbol\mu$ with
$\boldsymbol\mu\in\mathbb{R}^3$ and $\lVert\boldsymbol\mu\rVert^2=\tfrac34$; the nontrivial idempotents form
a two-sphere of radius $\tfrac{\sqrt3}{2}$ in the real quaternion subspace, and no two of them are
orthogonal.**

The **idempotents** of the block are the elements satisfying $\tilde\Pi\star\tilde\Pi=\tilde\Pi$. The set is
the fixed set of the square map $\varphi(\tilde P)=\tilde P\star\tilde P$ of the block, and on each idempotent
the square map is the identity.

### The Definition

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$
is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$

The origin is an idempotent of every product, and so is the unit when there is one; these are the **trivial
idempotents**, and the others are **nontrivial**. The set of the idempotents of $\star$ is its **idempotent
set**.

This is *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the
Peirce Decomposition*. Unqualified, the product is the block, and the block has no unit, so the only trivial
idempotents are $0$ and the unit candidate $e_0$.

### The Reduction of the Idempotent Equation

Write $\tilde\Pi=\alpha e_0+\mathbf x$ with $\alpha\in\mathbb{C}$ and $\mathbf x\in\mathbb{C}^3$. The
diagonal formula splits the equation into the two displays

$$
K(\tilde\Pi,\tilde\Pi)=|\alpha|^2-\lVert\mathbf x\rVert^2=\alpha ,
\qquad
-2\,\mathrm{Re}\bigl(\alpha\overline{\mathbf x}\bigr)=\mathbf x ,
$$

the first the scalar part and the second the vector part of the equality.

**Proposition (the reduction).** The vector equation is equivalent to the pair

$$
\alpha\overline{\mathbf x}+(\overline{\alpha}+1)\mathbf x=\mathbf 0 ,
\qquad
\overline{\alpha}\,\mathbf x+(\alpha+1)\overline{\mathbf x}=\mathbf 0 ,
$$

the second being the conjugate of the first.

*Proof.* The vector equation $\alpha\overline{\mathbf x}+\overline{\alpha}\mathbf x=-\mathbf x$ is the first
display; conjugating it, coefficient by coefficient, gives the second.

**Corollary (the scalar part is forced).** If $\tilde\Pi$ is a nontrivial idempotent with $\alpha\neq0$ and
$\mathbf x\neq0$, then

$$
\mathrm{Re}\,\alpha=-\tfrac12 ,
\qquad
\mathbf x\in\mathbb{R}^3 ,
\qquad
\lVert\mathbf x\rVert^2=\tfrac34 .
$$

*Proof.* Multiply the first equation of the proposition by $1+\alpha$ and the second by $-\alpha$, and add:
the $\overline{\mathbf x}$-terms cancel, leaving
$\bigl[(1+\alpha)(1+\overline{\alpha})-\alpha\overline{\alpha}\bigr]\mathbf x=\mathbf 0$. Since
$(1+\alpha)(1+\overline{\alpha})-\alpha\overline{\alpha}=1+2\mathrm{Re}\,\alpha$ and $\mathbf x\neq0$, an
idempotent has $\mathrm{Re}\,\alpha=-\tfrac12$. Then $\alpha+1=-\overline{\alpha}$, and the second equation,
$(\alpha+1)\overline{\mathbf x}=-\overline{\alpha}\mathbf x$, reads $-\overline{\alpha}\bigl(\overline{\mathbf x}-\mathbf x\bigr)=\mathbf 0$,
so $\overline{\mathbf x}=\mathbf x$ and $\mathbf x$ is real. The scalar equation
$\alpha=K(\tilde\Pi,\tilde\Pi)=|\alpha|^2-\lVert\mathbf x\rVert^2$ now equates $\alpha$ with a real number, so
$\mathrm{Im}\,\alpha=0$; hence $\alpha=-\tfrac12$, and $\lVert\mathbf x\rVert^2=|\alpha|^2-\alpha=\tfrac34$.

### The Classification of the Idempotents

**Every idempotent of the block is either trivial ($0$ or $e_0$) or of the form
$-\tfrac12e_0+\boldsymbol\mu$ with $\boldsymbol\mu\in\mathbb{R}^3$ and $\lVert\boldsymbol\mu\rVert^2=\tfrac34$;
there are no others.**

**Theorem (the idempotent set of the block).** The idempotents of the block are

$$
0 ,
\qquad
e_0 ,
\qquad\text{and}\qquad
-\tfrac12e_0+\boldsymbol\mu ,
\qquad
\boldsymbol\mu\in\mathbb{R}^3,\quad
\lVert\boldsymbol\mu\rVert^2=\tfrac34 .
$$

*Proof.* Let $\tilde\Pi=\alpha e_0+\mathbf x$ be an idempotent.

If $\alpha=0$ the vector equation is $\mathbf x=\mathbf 0$, so $\tilde\Pi=0$.

If $\alpha\neq0$ and $\mathbf x=\mathbf 0$ the vector equation is void and the scalar equation reads
$|\alpha|^2=\alpha$, so $\alpha=1$ and $\tilde\Pi=e_0$.

If $\alpha\neq0$ and $\mathbf x\neq0$ the corollary of §*The Reduction of the Idempotent Equation* gives
$\alpha=-\tfrac12$ and $\mathbf x\in\mathbb{R}^3$ with $\lVert\mathbf x\rVert^2=\tfrac34$; conversely every
element of this form satisfies both displays, since $-\tfrac12$ is real and
$K=|\alpha|^2-\lVert\mathbf x\rVert^2=\tfrac14-\tfrac34=-\tfrac12=\alpha$, while the vector part
$-2\mathrm{Re}(\alpha\overline{\mathbf x})=-2\alpha\mathbf x=\mathbf x$ because $2\alpha=-1$.

**Corollary (the shape of the set).** The nontrivial idempotents are a two-sphere of radius
$\tfrac{\sqrt3}{2}$ in the real quaternion subspace, centred at $-\tfrac12e_0$, and the origin and $e_0$ are
the two isolated idempotents.

*Proof.* The family is the intersection of the affine hyperplane $\alpha=-\tfrac12$ of
$\mathbb{H}_{\mathbb{B}}$ with the sphere $\lVert\mathbf x\rVert^2=\tfrac34$.

### The Halving Map and the Roots of One

**The map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ carries the roots of $+1$ to idempotents only at
$\tilde\Xi=\pm e_0$, and no nontrivial idempotent returns a root of $+1$ under
$\tilde\Pi\mapsto2\tilde\Pi-e_0$; the two classifications are independent.**

The map is the one of the associative case, and it is tested on the block by computing the square. Using the
two one-sided actions $e_0\star\tilde\Xi=\tilde\Xi^{*}$, $\tilde\Xi\star e_0=\tilde\Xi^{\natural}$ and
$e_0\star e_0=e_0$, and the root relation $\tilde\Xi\star\tilde\Xi=e_0$,

$$
\Bigl(\tfrac12(e_0+\tilde\Xi)\Bigr)\star\Bigl(\tfrac12(e_0+\tilde\Xi)\Bigr)
=\tfrac14\bigl(e_0\star e_0+e_0\star\tilde\Xi+\tilde\Xi\star e_0+\tilde\Xi\star\tilde\Xi\bigr)
=\tfrac12 e_0+\tfrac14\bigl(\tilde\Xi^{*}+\tilde\Xi^{\natural}\bigr).
$$

The display equals $\tfrac12(e_0+\tilde\Xi)$ exactly when
$\tilde\Xi^{*}+\tilde\Xi^{\natural}=2\tilde\Xi$. Writing $\tilde\Xi=\Xi_0e_0+\boldsymbol\Xi$, this reads
$2\mathrm{Re}(\Xi_0)e_0-2\mathrm{Re}(\boldsymbol\Xi)=2\Xi_0e_0+2\boldsymbol\Xi$, which holds exactly when
$\Xi_0$ is real and $\boldsymbol\Xi=\mathbf 0$: the element is a real central scalar. With
$\tilde\Xi\star\tilde\Xi=e_0$ this forces $\tilde\Xi=\pm e_0$. So the map sends the roots of $+1$ to the two
trivial idempotents $e_0$ (from $+e_0$) and $0$ (from $-e_0$), and to nothing else.

In the other direction, a nontrivial idempotent $-\tfrac12e_0+\boldsymbol\mu$ gives
$2\tilde\Pi-e_0=-2e_0+2\boldsymbol\mu$, a real quaternion whose block square is, by the diagonal formula,
$e_0+8\boldsymbol\mu$, which differs from $e_0$ because $\boldsymbol\mu\neq\mathbf 0$. So the block carries
no bijection between its roots of $+1$ and its
idempotents, in contrast with the associative plain product, where the halving map is a bijection
(*Square Roots of One and the Idempotents of the General Plain Algebra*). The single element common to the
two sets is $e_0$: an element that is both satisfies $\tilde\Xi\star\tilde\Xi=e_0$ and
$\tilde\Xi\star\tilde\Xi=\tilde\Xi$, hence $\tilde\Xi=e_0$.

### Properties of the Idempotent Set

**Every idempotent of the block is a real quaternion, every nonzero idempotent has central square
$C(\tilde\Pi)=1$ and is regular, and no two nontrivial idempotents are orthogonal.**

**Theorem (the idempotents lie in the real quaternion subspace; the nonzero ones are regular).** Every
idempotent of the block is a real quaternion; every nonzero idempotent has central square $C(\tilde\Pi)=1$
and is regular.

*Proof.* Real quaternion: $0$, $e_0$ and $-\tfrac12e_0+\boldsymbol\mu$ are real by the classification. The
central square of $-\tfrac12e_0+\boldsymbol\mu$ is
$C=\tfrac14+\lVert\boldsymbol\mu\rVert^2=\tfrac14+\tfrac34=1$, and $C(e_0)=1$. Since a nonzero idempotent
has $Q_0\neq0$ (its scalar part is $1$ or $-\tfrac12$) and $C=1\neq0$, it is regular by the criterion of
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*.

So no nonzero idempotent of the block is a zero divisor, and every nonzero idempotent lies on the slice
$C=1$ of the central square, while the trivial idempotent $0$ lies at $C=0$.

**Theorem (no orthogonal pair).** For two nontrivial idempotents
$\tilde\Pi=-\tfrac12e_0+\boldsymbol\mu$ and $\tilde\Pi'=-\tfrac12e_0+\boldsymbol\nu$,

$$
\tilde\Pi\star\tilde\Pi'=\tfrac14-\boldsymbol\mu\!\cdot\!\boldsymbol\nu
+\tfrac12\bigl(\boldsymbol\mu+\boldsymbol\nu\bigr),
$$

whose scalar part is $\tfrac14-\boldsymbol\mu\!\cdot\!\boldsymbol\nu$ and whose vector part is
$\tfrac12(\boldsymbol\mu+\boldsymbol\nu)$; it vanishes for no pair, so the nontrivial idempotents are
pairwise non-orthogonal.

*Proof.* Both elements are real quaternions, and for real arguments the block reads
$\tilde P\star\tilde Q=[\mathrm{SPA}(\tilde P,\tilde Q)]^{\natural}$, the natural conjugate of the plain
symmetric product $\mathrm{SPA}(\tilde P,\tilde Q)=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$; computing
$\mathrm{SPA}$ of the two idempotents, whose vector-part term is
$-\tfrac12(\boldsymbol\mu+\boldsymbol\nu)$, and applying the natural conjugation, which reverses the vector
sign, gives the display. The scalar part vanishes only if $\boldsymbol\mu\!\cdot\!\boldsymbol\nu=\tfrac14$
and the vector part only if $\boldsymbol\nu=-\boldsymbol\mu$, which would give
$\boldsymbol\mu\!\cdot\!\boldsymbol\nu=-\lVert\boldsymbol\mu\rVert^2=-\tfrac34$, a contradiction.

**Remark (no complete family, no Peirce calculus).** The block has no unit, so the notion of an orthogonal
family summing to the unit has no content here, and no two nontrivial idempotents are orthogonal (only the
origin annihilates, and is annihilated, trivially). The Peirce decomposition relative to an idempotent is a
property of the plain product (*Ideals and Peirce Decomposition of the General Plain Algebra*) and is not
available in the block.

### The Idempotents and the Other Classes

**The nonzero idempotents of the block are regular, so no nonzero idempotent is a zero divisor or a
nilpotent, and the idempotents and the nilpotents meet only at $0$.**

The three named classes of the block meet in a way opposite to the plain product.

| class of the block | idempotents it contains |
|---|---|
| zero divisors, pure family $\{Q_0=0\}$ | none, every nonzero idempotent having $Q_0\neq0$ |
| zero divisors, non-pure family $\{Q_0\neq0,\ C=0\}$ | none, every nonzero idempotent having $C=1$ |
| regular elements $\{Q_0\neq0,\ C\neq0\}$ | $e_0$ and the sphere $-\tfrac12e_0+\boldsymbol\mu$ |
| nilpotents $\{\alpha(e_0+i\boldsymbol\mu)\}$ | none, the two classes meeting only at $0$ |

The last row is proved in *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic
Sesqualgebra*: an element cannot have both $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ and
$\tilde\Upsilon\star\tilde\Upsilon=0$ unless it is $0$. The contrast with the plain product is exact. There
the nontrivial idempotents are the halves of the roots of $+1$, $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ with
$\tilde\Xi\star\tilde\Xi=e_0$, their central square is $0$, and they are zero divisors
(*Square Roots of One and the Idempotents of the General Plain Algebra*); here the nontrivial idempotents
have central square $1$ and are regular. The reason is the shape of the diagonal: the block's diagonal
carries the Krein form in its scalar part, and the equation $K(\tilde\Pi,\tilde\Pi)=\alpha$ forces the scalar
coordinate $-\tfrac12$ rather than leaving it free.

## Worked Examples

**The unit candidate.** $\tilde\Pi=e_0$: $e_0\star e_0=e_0$ by the multiplication table, so $e_0$ is an
idempotent and also a root of $+1$; it is the unit candidate of the block and not a unit, since
$e_0\star e_1=-e_1$.

**A root of $+1$ that is not $e_0$.** $\tilde\Xi=\sqrt2\,e_0+ie_1$ has $\alpha=\sqrt2$, $|\alpha|^2=2$ and
$\mathbf x=ie_1=i\alpha\mathbf c/|\alpha|^2$ with $\mathbf c=(\sqrt2,0,0)$ of $\lVert\mathbf c\rVert^2=2$, so
$\tilde\Xi\star\tilde\Xi=e_0$.

**A nontrivial idempotent.** $\boldsymbol\mu=\tfrac12(1,1,1)$ has $\lVert\boldsymbol\mu\rVert^2=\tfrac34$, so
$\tilde\Pi=-\tfrac12e_0+\tfrac12e_1+\tfrac12e_2+\tfrac12e_3$ satisfies $\tilde\Pi\star\tilde\Pi=\tilde\Pi$, as
the classification states.

**An idempotent on the sphere that is not the previous one.**
$\tilde\Pi=-\tfrac12e_0+\tfrac{\sqrt3}{2}e_1$ is an idempotent; it is a real quaternion of central square one
and is regular, so it annihilates nothing.

**The origin.** $\tilde\Pi=0$: $0\star0=0$, the trivial idempotent, and the image of the trivial root
$-e_0$ under the halving map.

## Summary

The roots of $+1$ in the block are the solutions of $\tilde\Xi\star\tilde\Xi=e_0$, namely
$\tilde\Xi=\alpha e_0+\tfrac{i\alpha}{|\alpha|^2}\mathbf c$ with $\alpha\in\mathbb{C}^{\times}$,
$|\alpha|\geq1$ and $\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2-1)$, a real manifold of dimension four;
there is no pure root of $+1$, and $e_0$ is the case $\alpha=1$, $\mathbf c=\mathbf 0$. The central imaginary
does not carry the roots of $+1$ to the roots of $-1$, the product being sesquilinear with
$(i\tilde\Xi)\star(i\tilde\Xi)=\tilde\Xi\star\tilde\Xi$; the roots of $-1$ are separately the pure unit
vectors and the family $\mathcal R_{-1}$, of real dimension five.

The idempotents are the trivial elements $0$ and $e_0$ together with the elements
$-\tfrac12e_0+\boldsymbol\mu$ with $\lVert\boldsymbol\mu\rVert^2=\tfrac34$, a two-sphere of radius
$\tfrac{\sqrt3}{2}$ in the real quaternion subspace. Every nonzero idempotent has central square $1$ and is
regular, so none is a zero divisor; no two nontrivial idempotents are orthogonal, so the block carries no
complete orthogonal family and no Peirce decomposition; and the idempotents meet the nilpotents only at the
origin.

The halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ of the associative case is not a bijection here: it
carries the roots of $+1$ to idempotents only at the trivial roots $\pm e_0$, since its square is
$\tfrac12e_0+\tfrac14(\tilde\Xi^{*}+\tilde\Xi^{\natural})$ and equals $\tfrac12(e_0+\tilde\Xi)$ only for a
real central $\tilde\Xi$; and no nontrivial idempotent returns a root of $+1$ under
$\tilde\Pi\mapsto2\tilde\Pi-e_0$. The two classes are classified independently from the diagonal, and the
only element they share is $e_0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi\star\tilde\Xi=e_0$ | the root equation of $+1$ in the block |
| $\alpha\overline{\mathbf x}\in i\mathbb{R}^3,\ K(\tilde\Xi,\tilde\Xi)=1$ | the two conditions, from the diagonal |
| $\mathcal R_{+1}=\{\alpha e_0+\tfrac{i\alpha}{|\alpha|^2}\mathbf c:\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2-1)\}$ | the roots of $+1$, $|\alpha|\geq1$ |
| $\mathcal R_{-1}=\{\alpha e_0+\tfrac{i\alpha}{|\alpha|^2}\mathbf c:\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2+1)\}$ | the non-pure roots of $-1$ |
| $\{0\},\ \{e_0\}$ | the trivial idempotents, $e_0$ the unit candidate |
| $-\tfrac12e_0+\boldsymbol\mu,\ \lVert\boldsymbol\mu\rVert^2=\tfrac34$ | the nontrivial idempotents, a two-sphere |
| $\tilde\Pi\star\tilde\Pi'=\tfrac14-\boldsymbol\mu\!\cdot\!\boldsymbol\nu+\tfrac12(\boldsymbol\mu+\boldsymbol\nu)$ | no two nontrivial idempotents are orthogonal |
| $C(\tilde\Pi)=\sum_\mu\Pi_\mu^2=1$ | the central square, one on the nonzero idempotents |
| $\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace, carrying the whole idempotent set |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*Powers, the Square and the Roots* and §*The Idempotent, the Projection and the Peirce Decomposition*, for the definitions relative to a general product.
- *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the second central value and the class disjoint from the idempotents.
- *Square Roots of a General Element in the Symmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-sesqualgebra.md`), for the equation $\tilde\Xi\star\tilde\Xi=\tilde R$ for an arbitrary value, of which the central values here are the scalar case.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), for the criterion that makes every nonzero idempotent regular.
- *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-algebraic-norm-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal formula that carries the reduction.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, its table and its two one-sided actions.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra.md`), for the idempotents of the associative plain product, where the halving map is a bijection.
