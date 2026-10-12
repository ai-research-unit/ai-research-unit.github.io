# __Nilpotents of the Antisymmetric Plain Algebra__

## Introduction

The nilpotent is defined by an equation in which the product occurs, so it is a class of the
product and not of the space (*Definitions for the Study of the 12 Algebraic Structures*,
§*The Nilpotent*). The block of this article is the antisymmetric plain multiplication
$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
$$
the cross product of the two vector parts, which is alternating (*Introduction to the
Antisymmetric Plain Algebra of Biquaternions*). The article determines its nilpotent class and
states the two coincidences the vanishing square produces.

The answer is total. The square of every element of the block is zero,
$\tilde P\wedge\tilde P=0$, so **every element of the space is a nilpotent**: the origin is the
trivial one, of index one, and every other element is of index two, its square vanishing while it
does not. The nilpotent class is the whole space, and the nonzero nilpotents are the punctured
space; the class coincides with the zero-divisor set and with the root set of $0$, and the
implication *nilpotent implies zero divisor* holds for the block in the total form, with the
origin as its only excluded element. The conjugations preserve the class, the remarkable subspaces
inherit it, and the comparison with the parent product is the comparison of the whole space with
the pure isotropic cone. The two companion articles are *Zero Divisors of the Antisymmetric Plain
Algebra* and *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra*,
and the parent class is *Nilpotents of the General Plain Algebra*.

## The Notion and Its Product

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element
$\tilde\Upsilon$ is **nilpotent of $\star$** when some power of it vanishes,
$$
\tilde\Upsilon^{\star k}=0\quad\text{for some }k\geq1,
$$
the power being the left-nested reading
$\tilde\Upsilon^{\star k}=\bigl(\cdots\bigl((\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon\bigr)\cdots\star\tilde\Upsilon\bigr)$
when the product is not associative. The least such $k$ is the **index of nilpotency**, and an
element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, is a
**square-zero element of $\star$**. The origin is the trivial nilpotent, of index one
(*Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*).

Throughout this article the product is the **antisymmetric plain multiplication** $\wedge$, and
unqualified, *nilpotent* means a nilpotent of $\wedge$. The nilpotent is the root of $0$ in the
sense of the definitions article; the general square and the powers of a non-associative product
are *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the nilpotents of the
parent plain product, to which the block is compared, are *Nilpotents of the General Plain
Algebra*.

## The Criterion

**Theorem (every element is a nilpotent).** For every element $\tilde\Upsilon$,
$$
\tilde\Upsilon\wedge\tilde\Upsilon=0 ,
$$
and consequently every element of $\mathbb{B}$ is a nilpotent of the block: the origin is of index
one and every other element is of index two.

*Proof.* The block is alternating, $\tilde X\wedge\tilde X=0$ for every $\tilde X$, by
*Introduction to the Antisymmetric Plain Algebra of Biquaternions*. Hence the second power of
every element vanishes. An element whose square vanishes has every higher power zero, the powers
being read from the square, so the index of a nonzero element is exactly two; the origin is the
only element whose first power vanishes, and its index is one.

The criterion is the alternation of the product read as an element statement. There is no
stratification by index: the index is one at the origin and two everywhere else, and no element of
the block is of index three or more, because the square has already vanished.

## The Nilpotent Class

**Proposition (the class is the whole space).** The nilpotent set of the block is the whole space,
and the nonzero nilpotents are the punctured space:
$$
\{\tilde\Upsilon:\tilde\Upsilon\text{ nilpotent of }\wedge\}=\mathbb{B},\qquad
\{\tilde\Upsilon\neq0:\tilde\Upsilon\text{ nilpotent}\}=\mathbb{B}\setminus\{0\}.
$$

*Proof.* The theorem gives the vanishing of the square at every element, so every element satisfies
the defining condition with $k=2$ (the origin with $k=1$). The nonzero nilpotents are obtained by
excluding the origin.

The class is as large as the space allows, and it is stable under every operation that preserves
the product: the sum of two nilpotents is a nilpotent, the scalar multiple of a nilpotent is a
nilpotent, and the bracket of two nilpotents is a nilpotent, all three being elements of the
space and every element being a nilpotent. The class is therefore the whole space and not a proper
subset of it.

## The Relation to the Zero Divisors and to the Roots of Zero

**Proposition (the three classes coincide).** The nonzero nilpotents, the zero divisors and the
roots of $0$ are one and the same set,
$$
\{\text{nonzero nilpotents}\}=\{\text{zero divisors}\}=\{\text{roots of }0\}=\mathbb{B}\setminus\{0\}.
$$

*Proof.* The nonzero nilpotents are the punctured space by the previous proposition; the zero
divisors are the punctured space by *Zero Divisors of the Antisymmetric Plain Algebra*, because
the block is alternating and every nonzero element is its own annihilating partner; and the roots
of $0$ are the punctured space by *Square Roots of Minus One, Zero and Plus One in the
Antisymmetric Plain Algebra*. The three descriptions select one set.

**Corollary (the implication *nilpotent implies zero divisor*).** For the block the implication
holds in the total form: every nonzero nilpotent is a two-sided zero divisor, with itself as the
annihilating partner; the origin is the only nilpotent that is not a zero divisor, and it is
excluded by the definition of the zero divisor, which requires both the element and its partner to
be nonzero.

*Proof.* A nonzero nilpotent $\tilde\Upsilon$ satisfies $\tilde\Upsilon\wedge\tilde\Upsilon=0$,
and the element $\tilde\Upsilon$ itself is a nonzero partner for both sides; the element is
therefore a two-sided zero divisor. The origin satisfies $0\wedge0=0$ and is not a zero divisor,
the definition requiring nonzero elements.

The implication is one of the rows of the dictionary of the four general products, where it holds
for the plain product and the natural product and fails for the plain sesquilinear product
(*Definitions for the Study of the 12 Algebraic Structures*, §9; *The Zero Divisors and the Twelve Structures*). For the block it holds without exception on the punctured space, and the
exception is the origin alone.

## The Conjugations and the Remarkable Subspaces

**Proposition (the conjugations preserve the class).** The nilpotent class of the block is
preserved by the bar, the natural conjugation and the star; the conjugates of a nilpotent are
nilpotents.

*Proof.* For the block the statement is immediate from the criterion, every element being a
nilpotent, so every conjugate is one; the compatibility of each conjugation with the bracket is
recorded here for the comparison with the other products, where the class is proper and the
preservation is a computation. The bar is an automorphism of the block,
$\overline{\tilde P\wedge\tilde Q}=\bar{\tilde P}\wedge\bar{\tilde Q}$, so it carries a vanishing
square to a vanishing square. The natural conjugation and the star are anti-automorphisms of the
plain product and they reverse the bracket,
$\tilde P^{\natural}\wedge\tilde Q^{\natural}=-(\tilde P\wedge\tilde Q)^{\natural}$ and likewise
for the star, so they carry a vanishing square to the negative of a vanishing square, which
vanishes as well.

**Proposition (the restriction to the remarkable subspaces).** On each of the remarkable subspaces
the restriction of the block is again alternating, so every element of every subspace is a
nilpotent of the restriction.

*Proof.* The square of an element of the subspace vanishes as the square of an element of the
ambient algebra vanishes, and the subspace is stable under the block only where the operation
stays inside it; the criterion applies to the elements in every case. The stable subspaces and
their readings are *Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions*.

## The Comparison with the Parent Product

**Remark (the parent nilpotents).** The parent general plain bilinear product is associative and
unital, and its nilpotents are the pure elements with isotropic vector part,
$$
\tilde\Upsilon^{2}=0\iff P_0=0\ \text{and}\ (\mathbf P,\mathbf P)=0
$$
(*Nilpotents of the General Plain Algebra*). The parent's nilpotent class is therefore a proper
cone of the space, of complex dimension two, and the implication *nilpotent implies zero divisor*
holds there with the pure isotropic cone as the set. The block is the antisymmetric half of the
parent, and the comparison is the comparison of a proper cone with the whole space: the block's
nilpotents strictly contain the parent's, the element $e_0$ being a nilpotent of the block
($e_0\wedge e_0=0$) and not of the parent ($e_0^{2}=e_0$). The enlargement is the removal of the
scalar part: the parent's criterion is a condition on the square, and the block's square is
identically zero, so the condition is satisfied by every element.

## Summary

For the antisymmetric plain multiplication $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ the
square of every element vanishes, so every element is a nilpotent: the origin of index one and
every other element of index two. The nilpotent class is the whole space, the nonzero nilpotents
are the punctured space, and the class coincides with the zero-divisor set and with the root set
of $0$, the three descriptions selecting one set. The implication *nilpotent implies zero divisor*
holds in the total form, the origin being the only nilpotent excluded by the definition of the zero
divisor; the conjugations preserve the class and every remarkable subspace inherits it. The
comparison with the parent product is the comparison of the whole space with the pure isotropic
cone, and the enlargement is the removal of the scalar part from the square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\tilde\Upsilon\wedge\tilde\Upsilon=0$ | the square of every element vanishes |
| $\mathbb{B}$ | the nilpotent class of the block, the whole space |
| $\mathbb{B}\setminus\{0\}$ | the nonzero nilpotents, at once the zero divisors and the roots of $0$ |
| index one / index two | the origin / every other element |
| $P_0=0,\ (\mathbf P,\mathbf P)=0$ | the nilpotents of the parent plain product, a proper cone |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the nilpotent of a general product, its index and the square-zero element, and for the relativity of the definition
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra.md`), for the coincidence of the nonzero nilpotents with the zero divisors
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-plain-algebra.md`), for the roots of $0$, which are the nonzero nilpotents
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), for the pure isotropic cone of the parent product, against which the whole space is read
- *The Zero Divisors and the Twelve Structures* (`articles_maths/the-zero-divisors-and-the-twelve-structures.md`), for the square-zero sets of the four general products and the failure of the implication for the plain sesquilinear one
