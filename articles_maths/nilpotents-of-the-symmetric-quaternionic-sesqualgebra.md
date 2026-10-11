# __Nilpotents of the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article classifies the nilpotents of the block, the symmetric quaternionic sesquilinear product
$\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*. It follows
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra* and reads the first named class of the block; the
second, the idempotents, is *Idempotents of the Symmetric Quaternionic Sesqualgebra*.

The nilpotent is the solution of an equation in the product, and the product is part of the definition: it
is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*,
§*The Nilpotent*, and read on the products of the space. The unqualified word means the nilpotent of the
block. The block is not associative, so a power needs a bracketing, and the left-nested reading is used
throughout; the first statement of the article is that the ambiguity does not matter here, because no
element of the block has a vanishing cube without having a vanishing square. So the block has nilpotents of
index two only, and the nilpotent of the block is the **square-zero element**.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the diagonal
$\tilde Q\star\tilde Q$ is *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic
Sesqualgebra*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Sesqualgebra*; the roots
of the central value $0$ are read in *Square Roots of Minus One, Zero and Plus One in the Symmetric
Quaternionic Sesqualgebra*; the nilpotents of the plain product are *Nilpotents of the General Plain
Algebra*; and the square-zero sets of the four general products are *The Square-Zero Elements of the Four
General Products*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\mathbf Q=\sum_kQ_ke_k$; $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes the coefficients, $\bar{\cdot}$ conjugates the coefficients, and
${}^{*}={}^{\natural}\circ\bar{\cdot}$; $\mathbb{H}_{\mathbb{B}}$ is the real quaternion subspace. The
diagonal is $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf Q}-\overline{Q_0}\mathbf Q$
with $K(\tilde Q,\tilde Q)=|Q_0|^2-\sum_k|Q_k|^2$, and it is a real quaternion for every $\tilde Q$.
Throughout this article the product is the block.

## Definition

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde\Upsilon$
be an element. It is **nilpotent of $\star$** when some power vanishes,

$$
\tilde\Upsilon^{\star k}=0 \quad\text{for some } k\geq1 ,
$$

the power being the left-nested reading
$\tilde\Upsilon^{\star k}=(\cdots((\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon)\cdots\star\tilde\Upsilon)$
of *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*. The
least such $k$ is the **index of nilpotency**; an element of index two,
$\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, is a **square-zero element of $\star$**.

This is *Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*. Unqualified, the
product is the block, and the nilpotent of the block is the solution of
$\tilde\Upsilon^{\star k}=0$ for some $k$. The origin is the trivial nilpotent and is excluded from the
classification.

## The Index Is Two

**Theorem (the only index is two).** For every element $\tilde P$ of the block,

$$
\tilde P\star(\tilde P\star\tilde P)=0
\qquad\Longleftrightarrow\qquad
(\tilde P\star\tilde P)\star\tilde P=0
\qquad\Longleftrightarrow\qquad
\tilde P\star\tilde P=0 .
$$

*Proof.* Suppose $\tilde P\star(\tilde P\star\tilde P)=0$ and put
$\tilde S=\tilde P\star\tilde P$. The diagonal formula gives $\tilde S=\sigma e_0+\mathbf V$ with
$\sigma=K(\tilde P,\tilde P)$ a real number and
$\mathbf V=-P_0\overline{\mathbf P}-\overline{P_0}\mathbf P$ a real vector, so $\tilde S$ is a real
quaternion: $\tilde S^{\natural}=\tilde S$ and $\overline{\tilde S}=\tilde S$. The equation
$\tilde P\star\tilde S=0$ is, in the scalar–vector form with $\tilde S$ real,

$$
P_0\sigma=(\mathbf P,\mathbf V),
\qquad
P_0\mathbf V+\sigma\mathbf P=\mathbf 0 ,
$$

where $(\mathbf P,\mathbf V)$ is the complex bilinear dot product of the two vectors.

If $P_0=0$ then the second display is $\sigma\mathbf P=\mathbf 0$; if $\mathbf P=\mathbf 0$ then
$\tilde P=0$ and $\tilde S=0$, while if $\mathbf P\neq\mathbf 0$ then $\sigma=0$, but for $P_0=0$ the
diagonal is $\tilde S=K(\tilde P,\tilde P)e_0=-\lVert\mathbf P\rVert^2e_0$, whose vector part
$\mathbf V$ vanishes and whose scalar $\sigma$ is $-\lVert\mathbf P\rVert^2$, so $\sigma=0$ forces
$\tilde P=0$. Hence no solution with $P_0=0$ except $\tilde P=0$.

If $P_0\neq0$, substitute $\mathbf V=-P_0\overline{\mathbf P}-\overline{P_0}\mathbf P$ into the second
display: it reads $-P_0^2\overline{\mathbf P}+\bigl(\sigma-|P_0|^2\bigr)\mathbf P=\mathbf 0$, that is
$P_0^2\overline{\mathbf P}=\bigl(\sigma-|P_0|^2\bigr)\mathbf P=-\lVert\mathbf P\rVert^2\mathbf P$,
the last step because $\sigma=K(\tilde P,\tilde P)=|P_0|^2-\lVert\mathbf P\rVert^2$. If $\mathbf P=\mathbf 0$
then $\tilde P=P_0e_0$ is central, the first display reads $P_0|P_0|^2=0$, and $P_0\neq0$ is a
contradiction. If $\mathbf P\neq\mathbf 0$, take the Hermitian norm of both sides of
$P_0^2\overline{\mathbf P}=-\lVert\mathbf P\rVert^2\mathbf P$: it gives
$|P_0|^4\lVert\mathbf P\rVert^2=\lVert\mathbf P\rVert^6$, hence $|P_0|^2=\lVert\mathbf P\rVert^2$, so
$\sigma=0$ and, from the second display, $P_0\mathbf V=-\sigma\mathbf P=\mathbf 0$, that is
$\mathbf V=\mathbf 0$; then $\tilde S=\sigma e_0+\mathbf V=0$. Hence $\tilde S=0$ in every case.

So $\tilde P\star(\tilde P\star\tilde P)=0$ forces $\tilde P\star\tilde P=0$; the converse is immediate.
The right-nested statement is conjugate-commutative, $(\tilde P\star\tilde P)\star\tilde P=\overline{\tilde P\star(\tilde P\star\tilde P)}$, so it vanishes exactly when the left-nested product
does.

**Corollary.** Every nilpotent of the block has index two, and the nonzero nilpotents of the block are
exactly its square-zero elements.

*Proof.* By the theorem a vanishing left-nested cube is already a vanishing square, so the powers stop at
two and "some power vanishes" is the same as "the square vanishes".

## The Square-Zero Elements

**Theorem (the square-zero set of the block).** The square-zero elements of the block are

$$
\alpha\bigl(e_0+i\boldsymbol\mu\bigr),
\qquad
\alpha\in\mathbb{C}^{\times},\quad
\boldsymbol\mu\in\mathbb{R}^3,\quad
\lVert\boldsymbol\mu\rVert=1 ,
$$

together with the origin.

*Proof.* Let $\tilde P=\alpha e_0+\mathbf x$. If $\alpha=0$ the diagonal is
$\tilde P\star\tilde P=K(\tilde P,\tilde P)e_0=-\lVert\mathbf x\rVert^2e_0$, which vanishes only for
$\mathbf x=\mathbf 0$. If $\alpha\neq0$, the diagonal is central exactly when
$\alpha\overline{\mathbf x}\in i\mathbb{R}^3$; write $\alpha\overline{x_k}=-ic_k$ with $c_k\in\mathbb{R}$,
so $x_k=i c_k/\overline{\alpha}=i\alpha c_k/|\alpha|^2$ and
$\lVert\mathbf x\rVert^2=\lVert\mathbf c\rVert^2/|\alpha|^2$. Then
$\tilde P\star\tilde P=K(\tilde P,\tilde P)e_0$ with
$K(\tilde P,\tilde P)=|\alpha|^2-\lVert\mathbf x\rVert^2$, which vanishes exactly when
$\lVert\mathbf c\rVert^2=|\alpha|^4$. Writing $\mathbf c=|\alpha|^2\boldsymbol\mu$ with
$\boldsymbol\mu\in\mathbb{R}^3$ a unit vector, the element is
$\tilde P=\alpha e_0+i\alpha\boldsymbol\mu=\alpha(e_0+i\boldsymbol\mu)$, and every such element has
$K=|\alpha|^2(1-\lVert\boldsymbol\mu\rVert^2)=0$ and vanishing vector part.

**Corollary (the shape of the set).** The nonzero nilpotents are a real cone of real dimension four: the
parameter $\alpha$ runs over the punctured plane, of real dimension two, and the direction
$\boldsymbol\mu$ over the unit sphere, of real dimension two.

**Corollary (the diagonal witness).** $\tilde P=e_0+ie_1$ is a nilpotent, the simplest one with $\alpha=1$
and $\boldsymbol\mu=e_1$; it has $\lVert\boldsymbol\mu\rVert=1$. The element $e_1$ is not a nilpotent, since
$e_1\star e_1=-e_0$, though it is a pure zero divisor.

## The Nilpotents and the Zero Divisors

**Theorem (a nilpotent is a zero divisor).** Every nonzero nilpotent of the block is a zero divisor, and it
annihilates itself on both sides: $\tilde\Upsilon\star\tilde\Upsilon=0$, so the pair
$(\tilde\Upsilon,\tilde\Upsilon)$ exhibits it as a two-sided zero divisor.

*Proof.* The relation $\tilde\Upsilon\star\tilde\Upsilon=0$ is the product of $\tilde\Upsilon$ with itself
on either side; both factors are nonzero by hypothesis. The two-sidedness is
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*.

**Theorem (the nilpotents are non-pure zero divisors).** A nilpotent
$\tilde\Upsilon=\alpha(e_0+i\boldsymbol\mu)$ has scalar part $\alpha\neq0$ and central square
$c(\tilde\Upsilon)=\alpha^2(1-\lVert\boldsymbol\mu\rVert^2)=0$; so it is a zero divisor of the block by the
non-pure criterion, and it is not in the pure family.

*Proof.* $c(\alpha(e_0+i\boldsymbol\mu))=\alpha^2\bigl(1+\lVert i\boldsymbol\mu\rVert^2\bigr)=\alpha^2(1-\lVert\boldsymbol\mu\rVert^2)=0$ because $\lVert\boldsymbol\mu\rVert=1$.

The inclusion is strict: $c$ vanishes on the whole non-pure family $\{Q_0\neq0,\ c(\tilde Q)=0\}$, and the
element

$$
e_0+e_1+i\sqrt2\,e_2
$$

has $Q_0=1$ and $c=1+1-2=0$, so it is a non-pure zero divisor, yet its square is $-2e_0-2e_1\neq0$;
equivalently it annihilates the nonzero $e_0-e_1+i\sqrt2\,e_2$ without being square-zero. So the
square-zero cone is a *proper* subset of the non-pure family, and the two must not be identified.

The class is thus strictly smaller than the zero-divisor set: the zero divisors include the whole vector
subspace, of real dimension six, while the nilpotents are a real cone of real dimension four. The
difference is the subject of §*Comparison* of *Zero Divisors of the Symmetric Quaternionic Sesqualgebra*.

## The Nilpotents and the Idempotents

**Theorem (the two classes meet only at the origin).** No nonzero element of the block is both a nilpotent
and an idempotent.

*Proof.* If $\tilde X\star\tilde X=\tilde X$ and $\tilde X\star\tilde X=0$, then $\tilde X=0$.

This is the two-family statement of the block. The zero-divisor set splits into the nilpotents
$\alpha(e_0+i\boldsymbol\mu)$, whose square vanishes, and the remaining elements of the non-pure family,
$Q_0\neq0$, $c(\tilde Q)=0$, whose square does not vanish (the witness $e_0+e_1+i\sqrt2\,e_2$); while the idempotents
$-\tfrac12e_0+\boldsymbol\mu$ are regular and lie outside the zero-divisor set altogether. The contrast
with the plain product is exact: there the nontrivial idempotents are zero divisors and the nilpotents are
the pure family, while here the nilpotents are non-pure and the idempotents are regular.

## The Conjugations

The three conjugations act on the nilpotent cone by permuting its parameters, and the cone is invariant
under each of them.

| conjugation | value on $\tilde\Upsilon=\alpha(e_0+i\boldsymbol\mu)$ |
|---|---|
| natural ${}^{\natural}$ | $\alpha(e_0-i\boldsymbol\mu)$, the direction reversed |
| complex $\bar{\cdot}$ | $\overline{\alpha}(e_0-i\boldsymbol\mu)$, the direction reversed and the coefficient conjugated |
| star ${}^{*}={}^{\natural}\circ\bar{\cdot}$ | $\overline{\alpha}(e_0+i\boldsymbol\mu)$, the coefficient conjugated |

Every value is again of the form $\alpha'(e_0+i\boldsymbol\mu')$ with $\alpha'\in\mathbb{C}^{\times}$ and
$\boldsymbol\mu'$ a real unit vector, so each conjugation is a bijection of the cone onto itself; the star
fixes the direction and conjugates the coefficient, and it fixes a nonzero nilpotent exactly when $\alpha$
is real. The class is a real cone of real dimension four, and it is decomposed into the orbits of the star
by the real-valued coefficient.

## Worked Examples

**The simplest nilpotent.** $\tilde\Upsilon=e_0+ie_1$: $\tilde\Upsilon\star\tilde\Upsilon=0$, so the index
is two; the left-nested cube is $\tilde\Upsilon\star(\tilde\Upsilon\star\tilde\Upsilon)=\tilde\Upsilon\star0=0$.

**A nilpotent with a complex coefficient.** $\tilde\Upsilon=(1+i)(e_0+ie_2)$: by the theorem the square
vanishes; the scalar part is $1+i$ and the central square is $0$.

**A pure element of square zero inside the vector subspace.** The origin alone: a pure element
$\mathbf P\neq0$ has $\tilde P\star\tilde P=-\lVert\mathbf P\rVert^2e_0\neq0$, so the vector subspace
contains no nonzero nilpotent of the block, in contrast with the plain product, whose nilpotent cone lies
there.

**A pure zero divisor that is not a nilpotent.** $\tilde P=e_1$: it is a zero divisor of the block, since
$e_1\star e_2=0$, and it is not a nilpotent, since $e_1\star e_1=-e_0$.

## Summary

The nilpotent of the block has index two and no other: $\tilde P\star(\tilde P\star\tilde P)=0$ holds
exactly when $\tilde P\star\tilde P=0$, so the nonzero nilpotents are the square-zero elements, and they are

$$
\alpha(e_0+i\boldsymbol\mu),
\qquad
\alpha\in\mathbb{C}^{\times},\quad
\boldsymbol\mu\in\mathbb{R}^3,\quad
\lVert\boldsymbol\mu\rVert=1 ,
$$

a real cone of real dimension four. Every nonzero nilpotent is a non-pure zero divisor that annihilates
itself on both sides; the nilpotents are strictly smaller than the zero-divisor set, whose pure family is
the whole vector subspace. No nonzero nilpotent is an idempotent, the two named classes of the block meeting
only at the origin; the nontrivial idempotents are regular and lie outside the zero-divisor set. The three
conjugations permute the cone, the star conjugating the coefficient and fixing the direction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Upsilon$ | a nilpotent of the block; index two, hence square-zero |
| $\tilde P\star(\tilde P\star\tilde P)=0\Leftrightarrow\tilde P\star\tilde P=0$ | the index-two theorem |
| $\alpha(e_0+i\boldsymbol\mu)$ | the nonzero nilpotents, a real cone of dimension four |
| $c(\tilde\Upsilon)=\sum_\mu\Upsilon_\mu^2=0$ | the central square, vanishing on the nilpotents |
| $\{\tilde Q\neq0:Q_0=0\}$ | the pure zero divisors, containing no nonzero nilpotent |
| $K(\tilde Q,\tilde Q)=|Q_0|^2-\lVert\mathbf Q\rVert^2$ | the scalar part of the diagonal |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Nilpotent* and §*Powers, the Square and the Roots*, for the definition, the index and the left-nested power of a non-associative product.
- *The Square-Zero Elements of the Four General Products* (`articles_maths/the-square-zero-elements-of-the-four-general-products.md`), for the square-zero set of the product whose symmetric part is the block.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), for the pure nilpotent cone of the plain product.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), for the criterion and the two families that the nilpotents sit inside.
- *Idempotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/idempotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the class disjoint from the nilpotents.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and its diagonal.
