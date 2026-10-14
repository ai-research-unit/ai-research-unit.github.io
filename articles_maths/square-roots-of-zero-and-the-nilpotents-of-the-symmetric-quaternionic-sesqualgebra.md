# __Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article reads two subjects of the block, the symmetric quaternionic sesquilinear product
$\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*, and in this order. The first is
the square roots of the central value $0$, the elements $\tilde\Xi$ of
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with

$$
\tilde\Xi\star\tilde\Xi=0 .
$$

The second is the nilpotents of the block, the nonzero elements whose square vanishes. The two subjects are
one: the roots of $0$ are the origin together with the square-zero elements, and the nonzero square-zero
elements are exactly the nilpotents.

The nilpotent is the solution of an equation in the product, and the product is part of the definition: it
is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*,
§*Powers, the Square and the Roots* and §*The Nilpotent*, and read on the products of the space. The
unqualified word means the block. The block is not associative, so a power needs a bracketing, and the
left-nested reading is used throughout; the first statement of the article is that the ambiguity does not
matter here, because no element of the block has a vanishing cube without having a vanishing square. So the
block has nilpotents of index two only, and the nilpotent of the block is the **square-zero element**.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the diagonal
$\tilde Q\star\tilde Q$ is *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic
Sesqualgebra*; the roots of $+1$ and the idempotents are *Square Roots of One and the Idempotents of the
Symmetric Quaternionic Sesqualgebra*; the roots of a general value are *Square Roots of a General Element in
the Symmetric Quaternionic Sesqualgebra*; the zero divisors and the criterion are *Zero Divisors of the
Symmetric Quaternionic Sesqualgebra*; the isotropic elements of the Krein form are *The Isotropic Structure
of the General Quaternionic Sesqualgebra*; the nilpotents of the plain product are *Square Roots of Zero and
the Nilpotents of the General Plain Algebra*; and the square-zero sets of the four general products are
*Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\vec Q=\sum_kQ_ke_k$; $(\vec P,\vec Q)=\sum_kP_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes the coefficients, $\bar{\cdot}$ conjugates the coefficients, and
${}^{*}={}^{\natural}\circ\bar{\cdot}$; $\mathbb{H}_{\mathbb{B}}$ is the real quaternion subspace. The
diagonal is $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\vec Q}-\overline{Q_0}\vec Q$
with $K(\tilde Q,\tilde Q)=|Q_0|^2-\sum_k|Q_k|^2$, and it is a real quaternion for every $\tilde Q$. The
**central square** is $C(\tilde Q)=\sum_\mu Q_\mu^2$, the scalar of
$\tilde Q\tilde Q^{\natural}=C(\tilde Q)e_0$. A root of a central value is written $\tilde\Xi$ (§*The Root
Convention* of *Conventions in Mathematics*), a nilpotent $\tilde\Upsilon$ (§*The Nilpotent Convention*), and
a generic element $\tilde P$ or $\tilde Q$. Throughout this article the product is the block.

**The results.** Every nilpotent of the block has index two, so
$\tilde P\star(\tilde P\star\tilde P)=0$ exactly when $\tilde P\star\tilde P=0$, and the nonzero nilpotents
are the square-zero elements $\alpha(e_0+i\vec n)$ with $\alpha\in\mathbb{C}^{\times}$ and
$\vec n\in\mathbb{R}^3$ a unit vector. They form a real cone of real dimension four, and it contains
no pure element. Every nonzero nilpotent is a non-pure zero divisor that annihilates itself on both sides,
and the nilpotents are strictly smaller than the non-pure family, whose element $e_0+e_1+i\sqrt2\,e_2$ is not
square-zero. No nonzero nilpotent is an idempotent, the two classes meeting only at the origin, and the three
conjugations permute the cone.

## The Roots of Zero

**The roots of $0$ in the block are the origin and the elements $\alpha(e_0+i\vec n)$ with
$\alpha\in\mathbb{C}^{\times}$ and $\vec n\in\mathbb{R}^3$ a unit vector; they form a real cone of
dimension four that contains no pure element.**

A **root of $0$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi\star\tilde\Xi=0$, the square being
the one of the block.

### The Reduction

Let $\tilde\Xi=\alpha e_0+\vec x$ with $\alpha\in\mathbb{C}$ and $\vec x\in\mathbb{C}^3$. The diagonal
formula of the block is

$$
\tilde\Xi\star\tilde\Xi=K(\tilde\Xi,\tilde\Xi)e_0-2\,\mathrm{Re}\bigl(\alpha\overline{\vec x}\bigr),
\qquad K(\tilde\Xi,\tilde\Xi)=|\alpha|^2-\lVert\vec x\rVert^2,
$$

whose scalar part is real and whose vector part is a real vector. The right-hand side $0$ is central, so the
equation splits into the vector condition $\alpha\overline{\vec x}\in i\mathbb{R}^3$ and the scalar
condition $K(\tilde\Xi,\tilde\Xi)=0$. When the vector condition holds, $\alpha\overline{x_k}=-ic_k$ with
$c_k\in\mathbb{R}$, that is $x_k=i\alpha c_k/|\alpha|^2$ for $\alpha\neq0$, so
$\lVert\vec x\rVert^2=\lVert\vec c\rVert^2/|\alpha|^2$ and the scalar condition reads

$$
\lVert\vec c\rVert^2=|\alpha|^4 .
$$

This is the same reduction as for the roots of $+1$
(*Square Roots of One and the Idempotents of the Symmetric Quaternionic Sesqualgebra*), read at the central
value $0$.

### The Zero Element

If $\alpha=0$ the vector condition holds automatically, the diagonal is
$\tilde\Xi\star\tilde\Xi=K(\tilde\Xi,\tilde\Xi)e_0=-\lVert\vec x\rVert^2e_0$, and it vanishes only for
$\vec x=\mathbf 0$. So the origin is a root of $0$, and it is the only pure root: a pure element
$\vec P\neq0$ has $\tilde P\star\tilde P=-\lVert\vec P\rVert^2e_0\neq0$, in contrast with the plain
product, whose nilpotent cone lies in the vector subspace.

### The Square-Zero Cone

Let $\alpha\neq0$. The equation $\lVert\vec c\rVert^2=|\alpha|^4$ has the real solutions $\vec c$ of
modulus $|\alpha|^2$, and every one of them is written

$$
\vec c=|\alpha|^2\vec n,
\qquad
\vec n\in\mathbb{R}^3,\quad
\lVert\vec n\rVert=1 ,
$$

so the root is

$$
\tilde\Xi=\alpha e_0+\frac{i\alpha}{|\alpha|^2}\vec c
=\alpha e_0+i\alpha\vec n
=\alpha\bigl(e_0+i\vec n\bigr).
$$

For a fixed direction $\vec n$ the coefficient $\alpha$ runs over the whole punctured plane, so the
generator $e_0+i\vec n$ spans a complex line of square-zero elements; the union over the unit sphere
is the real cone of the next theorem.

### Statement of the Theorem

**Theorem (the roots of $0$).** The roots of $0$ in the block are the origin and the elements

$$
\alpha\bigl(e_0+i\vec n\bigr),
\qquad
\alpha\in\mathbb{C}^{\times},\quad
\vec n\in\mathbb{R}^3,\quad
\lVert\vec n\rVert=1 .
$$

### Verification

Each element of the display is a root of $0$: its scalar condition holds because

$$
K\bigl(\alpha(e_0+i\vec n),\alpha(e_0+i\vec n)\bigr)
=|\alpha|^2-\lVert i\alpha\vec n\rVert^2
=|\alpha|^2\bigl(1-\lVert\vec n\rVert^2\bigr)=0 ,
$$

and its vector condition holds because $\alpha\overline{(i\alpha n_k)}=-i|\alpha|^2n_k$ is purely
imaginary for each $k$. Conversely the reduction shows that no other element is a root.

### The Roots of Zero and the Nilpotents

**The nonzero roots of $0$ are exactly the square-zero elements, that is the nilpotents of the block.**

A nonzero element is a root of $0$ when its square vanishes and it is not the origin; that is the definition
of a square-zero element, and §*Index Two* shows that a square-zero element is the only kind of nilpotent the
block has. So the root set of $0$ is the origin together with the nilpotent cone, and the two names denote
the same objects.

## The Nilpotents

**The nonzero nilpotents of the block are the elements $\alpha(e_0+i\vec n)$ with
$\alpha\in\mathbb{C}^{\times}$ and $\vec n\in\mathbb{R}^3$ a unit vector; they form a real cone of
real dimension four, every one has index two, and none is an idempotent.**

### The Definition

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
product is the block, and the nilpotent of the block is the solution of $\tilde\Upsilon^{\star k}=0$ for some
$k$. The origin is the trivial nilpotent and is excluded from the classification.

### Index Two

**Every nilpotent of the block has index two: $\tilde P\star(\tilde P\star\tilde P)=0$ holds exactly when
$\tilde P\star\tilde P=0$, and the block carries no nilpotent of higher index.**

**Theorem (the only index is two).** For every element $\tilde P$ of the block,

$$
\tilde P\star(\tilde P\star\tilde P)=0
\qquad\Longleftrightarrow\qquad
(\tilde P\star\tilde P)\star\tilde P=0
\qquad\Longleftrightarrow\qquad
\tilde P\star\tilde P=0 .
$$

*Proof.* Suppose $\tilde P\star(\tilde P\star\tilde P)=0$ and put $\tilde S=\tilde P\star\tilde P$. The
diagonal formula gives $\tilde S=\sigma e_0+\vec V$ with $\sigma=K(\tilde P,\tilde P)$ a real number and
$\vec V=-P_0\overline{\vec P}-\overline{P_0}\vec P$ a real vector, so $\tilde S$ is a real quaternion:
$\tilde S^{\natural}=\tilde S$ and $\overline{\tilde S}=\tilde S$. The equation $\tilde P\star\tilde S=0$ is,
in the scalar–vector form with $\tilde S$ real,

$$
P_0\sigma=(\vec P,\vec V),
\qquad
P_0\vec V+\sigma\vec P=\mathbf 0 .
$$

If $P_0=0$ then the second display is $\sigma\vec P=\mathbf 0$; if $\vec P=\mathbf 0$ then $\tilde P=0$
and $\tilde S=0$, while if $\vec P\neq\mathbf 0$ then $\sigma=0$, but for $P_0=0$ the diagonal is
$\tilde S=K(\tilde P,\tilde P)e_0=-\lVert\vec P\rVert^2e_0$, whose vector part $\vec V$ vanishes and
whose scalar $\sigma$ is $-\lVert\vec P\rVert^2$, so $\sigma=0$ forces $\tilde P=0$. Hence there is no
solution with $P_0=0$ except $\tilde P=0$.

If $P_0\neq0$, substitute $\vec V=-P_0\overline{\vec P}-\overline{P_0}\vec P$ into the second
display: it reads $-P_0^2\overline{\vec P}+\bigl(\sigma-|P_0|^2\bigr)\vec P=\mathbf 0$, that is
$P_0^2\overline{\vec P}=\bigl(\sigma-|P_0|^2\bigr)\vec P=-\lVert\vec P\rVert^2\vec P$, the last
step because $\sigma=K(\tilde P,\tilde P)=|P_0|^2-\lVert\vec P\rVert^2$. If $\vec P=\mathbf 0$ then
$\tilde P=P_0e_0$ is central, the first display reads $P_0|P_0|^2=0$, and $P_0\neq0$ is a contradiction. If
$\vec P\neq\mathbf 0$, take the squared modulus of both sides of
$P_0^2\overline{\vec P}=-\lVert\vec P\rVert^2\vec P$: it gives
$|P_0|^4\lVert\vec P\rVert^2=\lVert\vec P\rVert^6$, hence $|P_0|^2=\lVert\vec P\rVert^2$, so
$\sigma=0$ and, from the second display, $P_0\vec V=-\sigma\vec P=\mathbf 0$, that is
$\vec V=\mathbf 0$; then $\tilde S=\sigma e_0+\vec V=0$. Hence $\tilde S=0$ in every case.

So $\tilde P\star(\tilde P\star\tilde P)=0$ forces $\tilde P\star\tilde P=0$; the converse is immediate. The
right-nested statement holds by conjugate-commutativity,
$(\tilde P\star\tilde P)\star\tilde P=\overline{\tilde P\star(\tilde P\star\tilde P)}$, so it vanishes
exactly when the left-nested product does.

**Corollary.** Every nilpotent of the block has index two, and the nonzero nilpotents of the block are
exactly its square-zero elements, the cone of §*Statement of the Theorem*.

*Proof.* By the theorem a vanishing left-nested cube is already a vanishing square, so the powers stop at two
and "some power vanishes" is the same as "the square vanishes".

**Corollary (the shape of the set).** The nonzero nilpotents are a real cone of real dimension four: the
parameter $\alpha$ runs over the punctured plane, of real dimension two, and the direction $\vec n$
over the unit sphere, of real dimension two.

### The Nilpotents and the Zero Divisors

**Every nonzero nilpotent is a non-pure zero divisor that annihilates itself on both sides,
$\tilde\Upsilon\star\tilde\Upsilon=0$, and the nilpotents are strictly smaller than the non-pure family, hence
strictly smaller than the zero-divisor set.**

**Theorem (a nilpotent is a zero divisor).** Every nonzero nilpotent of the block is a zero divisor, and it
annihilates itself on both sides: $\tilde\Upsilon\star\tilde\Upsilon=0$, so the pair
$(\tilde\Upsilon,\tilde\Upsilon)$ exhibits it as a two-sided zero divisor.

*Proof.* The relation $\tilde\Upsilon\star\tilde\Upsilon=0$ is the product of $\tilde\Upsilon$ with itself
on either side; both factors are nonzero by hypothesis. The two-sidedness is
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*.

**Theorem (the nilpotents are non-pure zero divisors).** A nilpotent
$\tilde\Upsilon=\alpha(e_0+i\vec n)$ has scalar part $\alpha\neq0$ and central square
$C(\tilde\Upsilon)=\alpha^2(1-\lVert\vec n\rVert^2)=0$; so it is a zero divisor of the block by the
non-pure criterion, and it is not in the pure family.

*Proof.* $C(\alpha(e_0+i\vec n))=\alpha^2(1+\lVert i\vec n\rVert^2)=\alpha^2(1-\lVert\vec n\rVert^2)=0$
because $\lVert\vec n\rVert=1$.

The inclusion is strict: $C$ vanishes on the whole non-pure family $\{Q_0\neq0,\ C(\tilde Q)=0\}$, and the
element

$$
e_0+e_1+i\sqrt2\,e_2
$$

has $Q_0=1$ and $C=1+1-2=0$, so it is a non-pure zero divisor, yet its square is $-2e_0-2e_1\neq0$;
equivalently it annihilates the nonzero $e_0-e_1+i\sqrt2\,e_2$ without being square-zero. So the square-zero
cone is a *proper* subset of the non-pure family, and the two must not be identified. The class is thus
strictly smaller than the zero-divisor set, whose pure family is the whole vector subspace, of real dimension
six, while the nilpotents are a real cone of real dimension four; the difference is the subject of the
comparison of *Zero Divisors of the Symmetric Quaternionic Sesqualgebra*.

### The Nilpotents and the Idempotents

**No nonzero element of the block is both a nilpotent and an idempotent: the two classes meet only at the
origin.**

*Proof.* If $\tilde X\star\tilde X=\tilde X$ and $\tilde X\star\tilde X=0$, then $\tilde X=0$.

The contrast with the plain product is exact: there the nontrivial idempotents are zero divisors and the
nilpotents are the pure family, while here the nilpotents are non-pure and the idempotents are regular and lie
outside the zero-divisor set altogether (*Square Roots of One and the Idempotents of the Symmetric
Quaternionic Sesqualgebra*).

### The Conjugations

**The three conjugations preserve the nilpotent cone and permute its parameters, each acting as a bijection
of the cone onto itself: the natural conjugation reverses the direction, the star fixes the direction and
conjugates the coefficient, and the complex conjugation does both; the star decomposes the cone into its
orbits by the real-valued coefficient.**

The three conjugations act on the nilpotent cone by permuting its parameters, and the cone is invariant under
each of them.

| conjugation | value on $\tilde\Upsilon=\alpha(e_0+i\vec n)$ |
|---|---|
| natural ${}^{\natural}$ | $\alpha(e_0-i\vec n)$, the direction reversed |
| complex $\bar{\cdot}$ | $\overline{\alpha}(e_0-i\vec n)$, the direction reversed and the coefficient conjugated |
| star ${}^{*}={}^{\natural}\circ\bar{\cdot}$ | $\overline{\alpha}(e_0+i\vec n)$, the coefficient conjugated |

Every value is again of the form $\alpha'(e_0+i\vec n')$ with $\alpha'\in\mathbb{C}^{\times}$ and
$\vec n'$ a real unit vector, so each conjugation is a bijection of the cone onto itself; the star
fixes the direction and conjugates the coefficient, and it fixes a nonzero nilpotent exactly when $\alpha$ is
real. The class is a real cone of real dimension four, and it is decomposed into the orbits of the star by the
real-valued coefficient.

## Worked Examples

**The simplest nilpotent.** $\tilde\Upsilon=e_0+ie_1$: $\tilde\Upsilon\star\tilde\Upsilon=0$, so the index is
two, and the left-nested cube is
$\tilde\Upsilon\star(\tilde\Upsilon\star\tilde\Upsilon)=\tilde\Upsilon\star0=0$.

**A nilpotent with a complex coefficient.** $\tilde\Upsilon=(1+i)(e_0+ie_2)$: by the theorem the square
vanishes; the scalar part is $1+i$ and the central square is $0$.

**A pure element of square zero inside the vector subspace.** The origin alone: a pure element
$\vec P\neq0$ has $\tilde P\star\tilde P=-\lVert\vec P\rVert^2e_0\neq0$, so the vector subspace contains
no nonzero nilpotent of the block, in contrast with the plain product, whose nilpotent cone lies there.

**A pure zero divisor that is not a nilpotent.** $\tilde P=e_1$: it is a zero divisor of the block, since
$e_1\star e_2=0$, and it is not a nilpotent, since $e_1\star e_1=-e_0$.

## Summary

The roots of $0$ in the block are the origin together with the nilpotent cone, the elements
$\alpha(e_0+i\vec n)$ with $\alpha\in\mathbb{C}^{\times}$ and $\vec n\in\mathbb{R}^3$ a unit
vector, a real cone of real dimension four; for a fixed direction $\vec n$ the generator
$e_0+i\vec n$ spans a complex line of square-zero elements. The vector subspace contains no nonzero
root of $0$.

The nilpotent of the block has index two and no other: $\tilde P\star(\tilde P\star\tilde P)=0$ holds exactly
when $\tilde P\star\tilde P=0$, so the nonzero nilpotents are exactly the nonzero roots of $0$. Every nonzero
nilpotent is a non-pure zero divisor that annihilates itself on both sides; the nilpotents are strictly
smaller than the non-pure family, whose element $e_0+e_1+i\sqrt2\,e_2$ is a non-pure zero divisor but not
square-zero, and strictly smaller than the zero-divisor set, whose pure family is the whole vector subspace.
No nonzero nilpotent is an idempotent, the two named classes of the block meeting only at the origin; the
nontrivial idempotents are regular and lie outside the zero-divisor set. The three conjugations permute the
cone, the star conjugating the coefficient and fixing the direction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Upsilon$ | a nilpotent of the block; index two, hence square-zero |
| $\tilde\Xi\star\tilde\Xi=0$ | the root equation of $0$ in the block |
| $\alpha\overline{\vec x}\in i\mathbb{R}^3,\ K(\tilde\Xi,\tilde\Xi)=0$ | the two conditions, from the diagonal |
| $\alpha(e_0+i\vec n)$ | the nonzero roots of $0$, the nilpotent cone, of real dimension four |
| $\tilde P\star(\tilde P\star\tilde P)=0\Leftrightarrow\tilde P\star\tilde P=0$ | the index-two theorem |
| $C(\tilde\Upsilon)=\sum_\mu\Upsilon_\mu^2=0$ | the central square, vanishing on the nilpotents |
| $\{Q_0=0\}$ | the pure zero divisors, containing no nonzero nilpotent |
| $K(\tilde Q,\tilde Q)=|Q_0|^2-\lVert\vec Q\rVert^2$ | the scalar part of the diagonal |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Nilpotent* and §*Powers, the Square and the Roots*, for the definition, the index and the left-nested power of a non-associative product.
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the first central value and the class disjoint from the nilpotents.
- *Square Roots of a General Element in the Symmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-sesqualgebra.md`), for the equation $\tilde\Xi\star\tilde\Xi=\tilde R$ for an arbitrary value, of which the central value here is the case $\tilde R=0$.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), for the criterion and the two families that the nilpotents sit inside.
- *Square Roots of Zero and the Nilpotents of the General Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra.md`), for the pure nilpotent cone of the plain product.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the square-zero set of the product whose symmetric part is the block.
- *The Isotropic Structure of the General Quaternionic Sesqualgebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.md`), for the isotropic set of the Krein form, which is strictly larger than the cone.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and its diagonal.
