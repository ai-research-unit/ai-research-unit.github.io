# __Zero Divisors of the General Quaternionic Algebra__

## Introduction

This article studies the **zero divisors** of the quaternion algebra $\mathbb{H}$ read through the
general quaternionic bilinear product, and it is the real member of the general quaternionic family
whose complex sibling is *Zero Divisors of the General Quaternionic Algebra*.

A divisor is relative to a product, and the definition is stated once in *Definitions for the Study
of the Algebraic Structures*, §*The Element Vocabulary*; the unqualified "zero divisor" means the
zero divisor of the general quaternionic product throughout, and every other product is named. The
article establishes four things. First, the **criterion**: a nonzero $\tilde p$ is a zero divisor of
$\star$ exactly when its algebraic norm vanishes, $N(\tilde p)=0$, the criterion of the complex
counterpart read letter for letter. Second, the criterion is never met over $\mathbb{R}$: the
quaternionic norm is a sum of four squares, so it is positive definite and vanishes at $\tilde p=0$
alone, and the **zero-divisor set is empty**. Third, the solution set of the norm equation, which is
the zero-divisor cone of real dimension six over $\mathbb{C}$, degenerates to its apex
$\{0\}$ over $\mathbb{R}$; the striking object of the complex block is a single point here. Fourth,
every nonzero element is **regular**, with the single two-sided inverse
$\zeta(\tilde p)=\tilde p/N(\tilde p)$ against the left unit, so the two annihilators of an element
are $\{0\}$ at every nonzero element and the whole space at the origin.

The contrast with the complex sibling organises the article. There the norm is isotropic, the
zero-divisor set is the punctured cone $\{N=0\}$ of real dimension six, and the two families of
divisors, pure and non-pure, fill it; here the norm is definite, the cone shrinks to its apex, and
both families are empty. The difference is not a difference of the product, which is the same rule
read over the two fields, but of the base field: over $\mathbb{R}$ a sum of squares has no nontrivial
zero.

**Boundaries.** The norm, its multiplicativity and the two one-sided inverse equations are *Norm and
Invertibility in the General Quaternionic Algebra*; the element vocabulary is *Definitions for the
Study of the Algebraic Structures*; the annihilators and their coincidence are *Annihilators of
the General Quaternionic Algebra*; the definiteness of the form and the emptiness of the isotropic
structure are *The Isotropic Structure of the General Quaternionic Algebra*; the nilpotents of the
product are *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* and the idempotents *Square Roots of One and the Idempotents of the
General Quaternionic Algebra*, both below this article in this category; the structure-level
comparison of the six zero-divisor sets is *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; and the complex sibling, which carries
the cone and the two families, is *Zero Divisors of the General Quaternionic Algebra*.

## Conventions

$\mathbb{H}$ is the real quaternion algebra with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, the rules
$\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$. Over $\mathbb{R}$ the coefficientwise conjugation is the identity and
the Hermitian star coincides with the natural conjugation, so the block carries the single
involution

$$
\tilde p^{\natural}=p_0-\vec p,\qquad \tilde p=p_0e_t+\vec p,\quad
\vec p=p_1\vec e_x+p_2\vec e_y+p_3\vec e_z .
$$

Juxtaposition is the plain product $\tilde p\tilde q$ of the general plain algebra of the same space
and $\star$ is the general quaternionic bilinear product

$$
\tilde p\star\tilde q=\tilde p^{\natural}\tilde q ,
$$

the plain product with the first factor read through the conjugation. The **quaternionic bilinear
algebraic norm** is

$$
N(\tilde p)=\tilde p^{\natural}\tilde p=p_0^2+|\vec p|^2=\sum_{\mu\in\{t,x,y,z\}}p_\mu^2 ,
$$

and $\beta(\tilde p,\tilde q)=p_0q_t+\vec p\cdot\vec q$ is its polar form, the quaternionic
bilinear form of the space. An element is **pure** when $p_0=0$ and **non-pure** when $p_0\neq0$; the
centre is the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_t$ and the vector subspace is
$\mathrm{Vect}(\mathbb{H})=\{\vec p\}$.

## Definition

The word names a product, so the definition is stated for a general product and then read on
$\star$.

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\tilde p\in\mathbb{H}$. The element
$\tilde p$ is a **left zero divisor of $\star$** when $\tilde p\neq0$ and there is a nonzero
$\tilde q$ with $\tilde p\star\tilde q=0$; a **right zero divisor of $\star$** when $\tilde p\neq0$
and there is a nonzero $\tilde q$ with $\tilde q\star\tilde p=0$; and a **zero divisor of $\star$**
when it is one or the other. It is a **two-sided zero divisor** when it is both, and **regular** when
it is neither. The definition is *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*,
§*The Element Vocabulary*; the origin is not a zero divisor, both factors being required to be
nonzero.

Throughout this article the product is the general quaternionic bilinear product
$\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$. On it the two defining equations are

$$
\tilde p^{\natural}\tilde q=0 \quad\text{(left)},\qquad \tilde q^{\natural}\tilde p=0
\quad\text{(right)} ,
$$

which are plain-product equations in the conjugated first factor.

## The Criterion

**Theorem (the criterion).** For a nonzero $\tilde p\in\mathbb{H}$, $\tilde p$ is a zero divisor of
$\star$ if and only if

$$
N(\tilde p)=\sum_{\mu\in\{t,x,y,z\}}p_\mu^2=0 .
$$

**Proof.** Suppose that $\tilde p$ is a zero divisor. If it is a left one, there is a nonzero
$\tilde q$ with $\tilde p^{\natural}\tilde q=0$; taking norms and using the multiplicativity of the
norm,

$$
0=N(\tilde p^{\natural}\tilde q)=N(\tilde p^{\natural})N(\tilde q)=N(\tilde p)N(\tilde q) ,
$$

so $N(\tilde p)=0$ or $N(\tilde q)=0$. The factor $N(\tilde q)$ is positive, $\tilde q$ being
nonzero and the norm positive definite, so $N(\tilde p)=0$. The mirror computation with the factors
exchanged treats the right equation, $\tilde q^{\natural}\tilde p=0$. Conversely, if $N(\tilde p)=0$
then

$$
\tilde p\star\tilde p=\tilde p^{\natural}\tilde p=N(\tilde p)e_t=0 ,
$$

so $\tilde q=\tilde p$ is a nonzero witness for the left equation and $\tilde p$ is a left zero
divisor; the mirror computation gives the right statement.

The criterion is the criterion of the complex sibling, and it is the norm equation read on the
product whose square is the norm. The two products that share the norm are distinguished by the
object that turns the equation into a statement: in the plain algebra it is the plain inverse, here
it is the conjugated one-sided solution of §*Every Nonzero Element Is Regular*.

**Corollary (the criterion is never met).** Over $\mathbb{R}$ the sum of the four squares
$N(\tilde p)$ vanishes only at $\tilde p=0$, so a **nonzero** element never satisfies the criterion.
The general quaternionic product has **no zero divisor**, and its zero-divisor set is the empty set
$\varnothing$.

**Proof.** A sum of squares of real numbers vanishes exactly when every term vanishes, that is when
$p_0=p_1=p_2=p_3=0$. The criterion asks of a nonzero element that its norm vanish, and no such
element exists. The same statement is the row of the general quaternionic product in *Zero
Divisors*, where the zero-divisor set of the structure is the empty set.

## The Zero Set of the Norm

**Definition.** The **zero set of the norm** of the quaternionic product is

$$
C=\{\tilde p\in\mathbb{H}:N(\tilde p)=0\}=\{\tilde p:\tilde p\star\tilde p=0\} .
$$

**Proposition (the zero set is the origin).** Over $\mathbb{R}$ the set $C$ is the single point
$\{0\}$, of dimension zero, and it is at once the trivial real cone and the trivial real subspace.

**Proof.** $N$ is positive definite, so $N(\tilde p)=0$ is $\tilde p=0$; the origin is a cone and a
subspace of dimension zero, and it is the only one.

**Remark (the contrast with the complex block).** Over $\mathbb{C}$ the very same equation $N=0$,
with $N$ now complex valued, is two independent real equations on the eight real coordinates, and
its solution set is the zero-divisor cone of real dimension six that the complex sibling describes.
Over $\mathbb{R}$ the equation is a single sum of four real squares, whose only solution is the
origin; the cone of the complex block shrinks to its apex, and the punctured set that carries the
complex zero divisors becomes empty. The collapse is the definiteness of the quaternionic form
(*The Isotropic Structure of the General Quaternionic Algebra*), and it is the same fact that makes
$\mathbb{H}$ a division algebra for the plain product.

## The Two Families, Empty

The complex sibling splits its zero divisors into a **pure** family and a **non-pure** family: the
pure family is the isotropic cone of the vector subspace, of real dimension four, and the non-pure
family is the set of complex multiples of the nontrivial idempotents of the plain product. Over
$\mathbb{R}$ both families are empty, for the definiteness of the norm in the first case and the
division property of the plain algebra in the second.

**Proposition (the pure family is absent).** On the vector subspace
$\mathrm{Vect}(\mathbb{H})$ the norm is $N(\vec p)=|\vec p|^2$, positive definite, so the
isotropic equation $(\vec p,\vec p)=0$ has the single solution $\vec p=0$ and the pure
family of zero divisors is empty.

**Proof.** A sum of three real squares vanishes only at the origin; the criterion then excludes every
nonzero pure element.

**Proposition (the non-pure family is absent).** The non-pure zero divisors of the complex block are
the nonzero multiples of the nontrivial idempotents of the plain product. Over $\mathbb{R}$ the plain
product has no nontrivial idempotent: its idempotents are $0$ and $e_t$ alone, so the non-pure family
is empty.

**Proof.** The plain algebra is a division algebra. If $\tilde p^2=\tilde p$ and $\tilde p\neq0$,
left multiplication by the plain inverse $\tilde p^{-1}$ gives $\tilde p=e_t$. The Hermitian family
$\tfrac12(e_t+\tilde\Xi)$ that carries the complex family does not exist over $\mathbb{R}$, there
being no central imaginary unit; the idempotents of the block and the contrast with the complex
counterpart are *Square Roots of One and the Idempotents of the General Quaternionic Algebra*, below this article in this
category.

## Every Nonzero Element Is Regular

**Theorem (the two one-sided equations).** Let $\tilde p\in\mathbb{H}$ with $N(\tilde p)\neq0$, and
put $\zeta(\tilde p)=\tilde p/N(\tilde p)$. Then $\zeta(\tilde p)$ is the unique solution of each of
the equations $\tilde p\star\tilde x=e_t$ and $\tilde y\star\tilde p=e_t$, and

$$
\tilde p\star\zeta(\tilde p)=e_t=\zeta(\tilde p)\star\tilde p .
$$

The statement is *Norm and Invertibility*,
§*The One-Sided Inverse Equations*.

The remark is the one the block demands, and it is stated in the block's own terms. The algebra has
the left unit $e_t$ and no right one, so the two-sided inverse of the unital theory has no referent;
what the two equations compute is an element that inverts $\tilde p$ against the one-sided unit.
Their content is that the left and the right such elements are not merely both present, they are the
same, and that they exist exactly when the norm does not vanish.

**Corollary (regularity).** Every nonzero element of $\mathbb{H}$ is regular, with the single
two-sided inverse $\zeta(\tilde p)$ against the left unit $e_t$. The criterion of §*The Criterion* is
the statement that an element with a one-sided inverse is not a zero divisor.

**Proof.** Over $\mathbb{R}$ the criterion $N(\tilde p)\neq0$ is $\tilde p\neq0$, so the theorem
applies to every nonzero element. The last sentence is the contrapositive of the criterion, read with
the one-sided equations in place of the plain inverse.

**Remark (the invertibility is that of the parent algebra).** The invertible elements of the block are
therefore all the nonzero elements, the same set as the unit group of the parent plain algebra; the
left multiplication $L_{\tilde p}$ by such an element is the plain left multiplication by the nonzero
element $\tilde p^{\natural}$ and is a bijection of $\mathbb{H}$, so the unit group acts on the
elements of the block by the left multiplications. The block adds no inverse of its own: its single
inverse $\zeta(\tilde p)=\tilde p/N(\tilde p)$ is the plain inverse of $\tilde p^{\natural}$, and the
criterion it inverts is the criterion of the parent norm.

## The Block and the Division Property

The general quaternionic product and the general plain product are the two **division structures** of
the space, the two with an empty zero-divisor set (*Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The General Plain Algebra (GPA)* and §*The General Quaternionic Algebra (GQA)*);
they are the only ones of the six whose product leaves no zero divisor, the symmetric structures
having the pure cone and the punctured space and the two antisymmetric structures having the whole
punctured space.

**Remark (the unit is one-sided).** In the strict sense of *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The Element Vocabulary*, a **division rule** asks beside the absence of zero
divisors for a two-sided unit, and only the general plain product of the six has one; the general
quaternionic product has the left unit $e_t$ alone. Over the complex block the product fails the
division property for the stronger reason that it contains zero divisors; over the real block the
zero divisors are absent and the only defect is the missing right unit (*The Specificities of the
General Quaternionic Algebra*). The two defects are independent, and this article exhibits the
second alone.

## The Annihilators

The annihilator of an element is the kernel of the left or the right multiplication, and it is the
finer object than the zero divisor: it names the partners. Over $\mathbb{R}$ the two annihilators
coincide, and the answer is the smallest possible away from the origin.

**Theorem (the common annihilator).** For every $\tilde p\in\mathbb{H}$,

$$
A_\star(\tilde p)=\{\tilde x:\tilde p\star\tilde x=0\},\qquad
B_\star(\tilde p)=\{\tilde x:\tilde x\star\tilde p=0\} ,
$$

coincide, and

$$
A_\star(\tilde p)=B_\star(\tilde p)=\{0\}\ \text{for}\ \tilde p\neq0 ,\qquad
A_\star(\tilde p)=B_\star(\tilde p)=\mathbb{H}\ \text{for}\ \tilde p=0 .
$$

The statement and its proof are *Annihilators of the General Quaternionic Algebra*; the coincidence
is the anti-automorphism property of ${}^{\natural}$, the same reason as over $\mathbb{C}$, and over
$\mathbb{R}$ it is vacuous, both sides being $\{0\}$ at every nonzero element. The operator behind
the annihilator is the left multiplication $L_{\tilde p}\tilde x=\tilde p^{\natural}\tilde x$, of
determinant $\det L_{\tilde p}=N(\tilde p)^2$, nonzero at every nonzero element.

## The Zero Divisors and the Remarkable Subspaces

The element theory of the block is read on the two remarkable real subspaces of $\mathbb{H}$, the
scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_t$, which is the centre, and the vector subspace
$\mathrm{Vect}(\mathbb{H})$ (*Introduction to the Remarkable Subspaces of the Quaternions*). Neither
carries a zero divisor.

| remarkable subspace | element | norm | zero divisors |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$, the centre | $se_t$ | $s^2$ | none |
| $\mathrm{Vect}(\mathbb{H})$, the vector subspace | $\vec p$ | $\lvert\vec p\rvert^2$ | none |

**Proposition.** On the centre and on the vector subspace the norm of a nonzero element is strictly
positive, so neither subspace contains an isotropic direction and neither contains a zero divisor;
in each the origin alone is of norm zero.

**Proof.** $N(se_t)=s^2$ vanishes only at $s=0$ and $N(\vec p)=|\vec p|^2$ only at
$\vec p=0$, and a nonzero central element is a unit, $\zeta(se_t)=e_t/s$; the criterion then
excludes every nonzero element of either subspace. The definiteness of the form on the two subspaces
is *The Isotropic Structure of the General Quaternionic Algebra*.

## The Zero Divisors and the Other Structures of the Space

The comparison of the six zero-divisor sets is *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, and its verdict for the block is the
empty set; the article states the contrast in one theorem and does not reproduce the other rows.

**Theorem.** Among the six structures of the quaternion real space the zero-divisor set is empty for
the general plain algebra and for the general quaternionic algebra, is the pure cone
$\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ for the symmetric plain algebra, is the punctured space
$\mathbb{H}\setminus\{0\}$ for the symmetric quaternionic algebra, and is the punctured space for
the two antisymmetric structures.

**Proof.** The two general structures are the theorem of *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*,
§*The Two General Products Coincide*; the symmetric rows are its §*The Symmetric Plain Algebra (SPA)*
and §*The Symmetric Quaternionic Algebra (SQA)*, where the Jordan product kills a pair of orthogonal
pure vectors and the scalar-valued product kills the orthogonal hyperplane of every nonzero element;
the antisymmetric rows are its §*The Antisymmetric Plain Algebra (APA)* and §*The Antisymmetric
Quaternionic Algebra (AQA)*, the products being alternating. The two division structures are the two
bilinear general products of the space.

**Remark.** The complex block carries four general products, and their zero-divisor sets coincide at
the punctured cone; the real block carries two bilinear general products, and their zero-divisor sets
coincide at the empty set. The coincidence is the same in form and opposite in content, and in both
cases the product is not what selects the set: the norm is.

## Summary

For the general quaternionic bilinear product $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$
over $\mathbb{R}$, a nonzero element is a zero divisor exactly when its algebraic norm vanishes,
$N(\tilde p)=\sum_\mu p_\mu^2=0$. The criterion is the criterion of the complex sibling, but over
$\mathbb{R}$ the norm is a sum of four squares, hence positive definite, so the criterion is never
met: the zero-divisor set is the **empty set**, and the zero-divisor cone of the complex block, of
real dimension six, shrinks to its apex $\{0\}$. The two families of the complex block, the pure
family of the isotropic vector subspace and the non-pure family of the multiples of the nontrivial
plain idempotents, are both empty, for the norm is definite on the vector subspace and the plain
algebra is a division algebra with the idempotents $0$ and $e_t$ alone. Every nonzero element is
regular, with the single two-sided inverse $\zeta(\tilde p)=\tilde p/N(\tilde p)$ against the left
unit $e_t$; the two annihilators of an element coincide and are $\{0\}$ at every nonzero element and
the whole space at the origin; and neither remarkable subspace, the centre nor the vector subspace,
carries a zero divisor. The general quaternionic product is one of the two division structures of the
space, the other being the general plain product, and it differs from it in the unit, which is
one-sided here and two-sided there.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, the real space of the block |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity, $\vec e_k^2=-e_t$ |
| $\tilde p=p_0e_t+\vec p$ | an element and its scalar–vector split |
| $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| ${}^{\natural}$ | the conjugation $\tilde p^{\natural}=p_0-\vec p$ |
| $N(\tilde p)=\tilde p^{\natural}\tilde p=\sum_\mu p_\mu^2$ | the quaternionic bilinear algebraic norm, positive definite |
| $\beta(\tilde p,\tilde q)=p_0q_t+\vec p\cdot\vec q$ | the quaternionic bilinear form, the polar form of $N$ |
| $\varnothing$ | the zero-divisor set of the block |
| $C=\{N=0\}=\{0\}$ | the zero set of the norm, the apex of the complex cone |
| $\zeta(\tilde p)=\tilde p/N(\tilde p)$ | the two-sided inverse against the left unit |
| $A_\star(\tilde p),B_\star(\tilde p)$ | the left and the right annihilator, coinciding and equal to $\{0\}$ off the origin |
| $\mathbb{R}_{\mathbb{H}},\mathrm{Vect}(\mathbb{H})$ | the centre and the vector subspace, neither carrying a zero divisor |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for zero divisors, annihilators and the division property in a non-associative algebra.
- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), §*The Element Vocabulary*, for the product-relative definition of the zero divisor, of the regular element and of a division rule.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for isotopes and the way a change of product moves the zero divisors.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the division property of the quaternion algebra and the multiplicative norm.
- *Norm and Invertibility* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternioid.md`), for the definite norm, its multiplicativity and the two one-sided equations.
- *Annihilators of the General Quaternionic Algebra* (`articles_maths/annihilators-of-the-general-quaternionic-algebra-of-quaternioid.md`), for the coincidence of the two annihilators and their size.
- *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the six zero-divisor sets of the space and the two division structures.
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra-of-quaternioid.md`), for the definiteness of the quaternionic form and the emptiness of the isotropic structure.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-quaternioid.md`) and *Square Roots of One and the Idempotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra-of-quaternioid.md`), below this article in this category, for the square-zero elements and the idempotents of the block.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), the complex sibling, whose zero-divisor set is the punctured cone that the passage to $\mathbb{R}$ removes.
