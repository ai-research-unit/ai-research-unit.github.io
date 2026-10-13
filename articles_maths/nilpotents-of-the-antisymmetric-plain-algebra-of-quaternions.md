# __Nilpotents of the Antisymmetric Plain Algebra__

## Introduction

The nilpotent is defined by an equation in which the product occurs, so it is a class of the
product and not of the space (*Definitions for the Study of the 6 Algebraic Structures*, §*The
Element Vocabulary*). The block of this article is the antisymmetric plain multiplication

$$
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\mathbf p\times\mathbf q,
$$

the cross product of the two vector parts, which is alternating (*Introduction to the Antisymmetric
Plain Algebra of Quaternions*). The article determines its nilpotent class and states the two
coincidences the vanishing square produces.

The answer is total. The square of every element of the block is zero,
$\tilde p\times\tilde p=0$, so **the nilpotent class is the whole space**: the origin is its trivial
member, of index one, and every other element is of index two, its square vanishing while it does
not. The nilpotents, the nonzero elements of the class, are the punctured space; they coincide with
the zero-divisor set and with the root set of $0$, and the implication *nilpotent implies zero
divisor* holds for the block in the total form, the origin being the class's only element outside the
zero divisors. Every element lies in its own annihilator on both sides, and the square detects no
zero divisor here, vanishing on everything. The comparison with the parent product is the comparison
of the whole space with the origin alone, the parent being a division product. The two companion
articles are *Zero Divisors of the Antisymmetric Plain Algebra* and *Square Roots of Minus One, Zero
and Plus One in the Antisymmetric Plain Algebra*, and the parent class is *Nilpotents of the General
Plain Algebra*.

## The Notion and Its Product

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{H}$. An element is in
the **nilpotent class of $\star$** when some power of it vanishes,
$\tilde\upsilon^{\star k}=0$ for some $k\geq1$, the powers being read $x^1=x$ and
$x^{k+1}=x\star x^k$; the least such $k$ is the **index of nilpotency**. A **nilpotent of $\star$**
is a nonzero element of the class, a **square-zero element** is a nonzero element with
$\tilde\upsilon\star\tilde\upsilon=0$, and a **cube-zero element** is a nonzero element with
$f(\tilde\upsilon,f(\tilde\upsilon,\tilde\upsilon))=0$; a nilpotent of index two is exactly a
square-zero element. The origin lies in the class of every product, of index one, and it is not a
nilpotent (*Definitions for the Study of the 6 Algebraic Structures*, §*The Element Vocabulary*).

Throughout this article the product is the antisymmetric plain multiplication $\times$, and
unqualified, *nilpotent* and *class* are read in $\times$. The nilpotent is the root of $0$ in the
sense of the definitions article, and the nilpotent classes of the six structures, against which the
block is read, are *Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

## The Criterion

**Theorem (the class is the whole space).** For every element $\tilde\upsilon$,

$$
\tilde\upsilon\times\tilde\upsilon=0 ,
$$

so the nilpotent class of the block is the whole space, its nonzero elements, the nilpotents, are the
punctured space, and every nilpotent is of index two; no element is of index three or more. The
origin is the trivial member of the class, of index one.

*Proof.* The block is alternating, $\tilde x\times\tilde x=0$ for every $\tilde x$, by
*Introduction to the Antisymmetric Plain Algebra of Quaternions*. Hence the second power of every
element vanishes and the class, the set of elements some power of which vanishes, is the whole space.
An element whose square vanishes has every higher power zero, the powers being read from the square,
so its index is two when the element is nonzero and one at the origin. No element has index three or
more, the square having already vanished.

The criterion is the alternation of the product read as an element statement. There is no
stratification by index: the index is two on the punctured space and one at the origin, and none is
of index three or more.

## The Nilpotent Class

**Proposition (the class and its nonzero part).** The nilpotent class of the block is the whole
space, and the nilpotents are the punctured space,

$$
\{\tilde\upsilon:\tilde\upsilon^{\times k}=0\text{ for some }k\}=\mathbb{H},
\qquad
\{\tilde\upsilon\neq0:\tilde\upsilon\text{ nilpotent}\}=\mathbb{H}\setminus\{0\}.
$$

*Proof.* The theorem gives the vanishing of the square at every element, so every element satisfies
the defining condition with $k=2$ and lies in the class; the origin does so with $k=1$ and is the
trivial member, of index one; the nonzero elements are the nilpotents, and the punctured space is
their set.

The class is as large as the space allows, and it is stable under every operation of the space: the
sum of two nilpotents is square zero, and so are the scalar multiple of a nilpotent and the bracket
of two nilpotents, all three being elements of the space. The punctured space is therefore closed
under the product, and the class is not a proper cone of the space.

## The Relation to the Zero Divisors and to the Roots of Zero

**Proposition (the four classes coincide).** The nilpotents, the square-zero elements, the zero
divisors and the roots of $0$ are one and the same set,

$$
\{\text{nilpotents}\}=\{\text{square-zero elements}\}=\{\text{zero divisors}\}=\{\text{roots of }0\}=\mathbb{H}\setminus\{0\}.
$$

*Proof.* The nilpotents are the punctured space by the previous proposition, and every nilpotent is
square zero, of index two. The zero divisors are the punctured space by *Zero Divisors of the
Antisymmetric Plain Algebra*, because the block is alternating and every nonzero element is its own
annihilating partner; and the roots of $0$ are the punctured space by *Square Roots of Minus One,
Zero and Plus One in the Antisymmetric Plain Algebra*. The four descriptions select one set.

**Corollary (the implication *nilpotent implies zero divisor*).** For the block the implication holds
in the total form: every nilpotent is a two-sided zero divisor, with itself as the annihilating
partner. The origin is the class's only element that is not a zero divisor, the definition of the
zero divisor requiring nonzero elements.

*Proof.* A nilpotent $\tilde\upsilon$ satisfies $\tilde\upsilon\times\tilde\upsilon=0$, and the
element $\tilde\upsilon$ itself is a nonzero partner for both sides; the element is therefore a
two-sided zero divisor. The origin lies in the class and is not a zero divisor, the definition
requiring nonzero elements.

**Remark (the square detects no zero divisor).** The implication *nilpotent implies zero divisor* has
no converse here: the square vanishes on everything, so the vanishing of a square carries no
information about an element, and the class the square detects is the whole space rather than a
proper subfamily of the zero divisors. The zero-divisor set is the punctured space as well (*Zero
Divisors of the Antisymmetric Plain Algebra*), and the two sets agree; what fails is the
discrimination, not the coincidence.

**Corollary (self-annihilation).** Every element lies in its own annihilator on both sides: for every
$\tilde\upsilon$,

$$
\tilde\upsilon\in A_\times(\tilde\upsilon)\quad\text{and}\quad \tilde\upsilon\in B_\times(\tilde\upsilon),
$$

the left and the right annihilator being read in the block.

*Proof.* The square vanishes, $\tilde\upsilon\times\tilde\upsilon=0$, and the left annihilator
$A_\times(\tilde\upsilon)$ is the set of $\tilde x$ with $\tilde\upsilon\times\tilde x=0$; the choice
$\tilde x=\tilde\upsilon$ gives the left membership. The right membership is the same display read in
the other order, and the two sides coincide for the block, the product being alternating
(*Annihilators of the Antisymmetric Plain Algebra*). Hence every element is its own annihilating
partner, on the left and on the right.

The self-annihilation is the element-level form of the totality of the class. For a noncentral
element the annihilator is the plane $\mathbb{R}e_0\oplus\mathbb{R}\mathbf\upsilon$ of real dimension
two, which contains the element; for a central element it is the whole space. The element lies in its
annihilator in every case, which is the statement that the square vanishes.

## The Conjugations and the Remarkable Subspaces

**Proposition (the conjugations preserve the class).** The nilpotent class of the block is preserved
by the bar, the natural conjugation and the star; the conjugates of an element of the class are
elements of the class.

*Proof.* For the block the statement is immediate from the criterion, every element lying in the
class, so every conjugate lies in it; the compatibility of each conjugation with the bracket is
recorded here for the comparison with the other structures, where the class is proper and the
preservation is a computation. The bar is the identity over $\mathbb{R}$ and so preserves the class
trivially. The natural conjugation is an anti-automorphism of the parent product and it reverses the
bracket, $\tilde p^{\natural}\times\tilde q^{\natural}=-(\tilde p\times\tilde q)^{\natural}$, so it
carries a vanishing square to the negative of a vanishing square, which vanishes as well; the star
coincides with the natural conjugation over $\mathbb{R}$.

**Proposition (the restriction to the remarkable subspaces).** On each of the remarkable subspaces the
restriction of the block is again alternating, so every element of every subspace lies in the class
of the restriction and every nonzero element of it is a nilpotent of the restriction.

*Proof.* The square of an element of the subspace vanishes as the square of an element of the ambient
algebra vanishes, and the criterion applies to the elements in every case. The subspaces and their
readings are *Comparison of the Remarkable Subspaces of the Quaternions*.

## The Comparison with the Parent Product

**Remark (the parent class).** The parent general plain bilinear product is associative and unital,
and it carries no nilpotent: it is a division product, so a nonzero $\tilde\upsilon$ is invertible and
$\tilde\upsilon^2=0$ would give $\tilde\upsilon=0$ (*Norm and Invertibility in the General Plain
Algebra*; *The Specificities of the General Plain Algebra*). The parent's class is therefore the
origin alone, that is the empty set off the origin. Over $\mathbb{R}$ the plain square has no
isotropic direction, its isotropic cone being real only after complexification, so the pure elements
that would be square zero over $\mathbb{C}$ are not available. The block is the antisymmetric half of
the parent, and the comparison is the comparison of the whole space with the origin alone: the
block's class strictly contains the parent's, the element $e_0$ lying in the class of the block
($e_0\times e_0=0$) and not of the parent ($e_0^2=e_0$). The enlargement is the removal of the scalar
part: the parent's criterion is a condition on the square, and the block's square is identically
zero, so the condition is satisfied by every element.

**Remark (the reading among the six structures).** The nilpotent class of the six structures is the
origin alone for the general plain, the symmetric plain, the general quaternionic and the symmetric
quaternionic structures, and it is the whole space for the antisymmetric plain and the antisymmetric
quaternionic structures; only two sets occur, and no structure of the six has an intermediate one
(*Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*). The block is one of the two structures whose square vanishes identically, and among
the six it is the only one whose nilpotents all have index two. In the biquaternion chapter the class
of the two antisymmetric biquaternion structures is likewise the whole space (*Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*), so the
totality for an antisymmetric block is not an artefact of the real field.

## Summary

For the antisymmetric plain multiplication $\tilde p\times\tilde q=\mathbf p\times\mathbf q$ the
square of every element vanishes, so the nilpotent class is the whole space: the origin is its trivial
member, of index one, and every other element is of index two. The nilpotents, the nonzero elements
of the class, are the punctured space, and they coincide with the square-zero elements, the zero
divisors and the root set of $0$, the four descriptions selecting one set. The implication *nilpotent
implies zero divisor* holds in the total form, the origin being the only element of the class outside
the zero divisors; every element lies in its own annihilator on both sides, the self-annihilation
being the element-level form of the totality; and the square detects no zero divisor, vanishing on
everything. The conjugations preserve the class and every remarkable subspace inherits it. The
comparison with the parent product is the comparison of the whole space with the origin alone, the
enlargement being the removal of the scalar part from the square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\mathbf p\times\mathbf q$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\tilde\upsilon\times\tilde\upsilon=0$ | the square of every element vanishes |
| $\mathbb{H}$ | the nilpotent class of the block, the trivial origin included |
| $\mathbb{H}\setminus\{0\}$ | the nilpotents, at once the square-zero elements, the zero divisors and the roots of $0$ |
| index two | every nilpotent; the origin is the trivial member, of index one |
| $A_\times(\tilde\upsilon)$, $B_\times(\tilde\upsilon)$ | the two one-sided annihilators of $\tilde\upsilon$, both containing $\tilde\upsilon$ |
| $\{0\}$ | the nilpotent class of the parent plain product, the empty set off the origin |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the nilpotent of a general product, its index, the square-zero element and the relativity of the definition
- *Introduction to the Antisymmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternions.md`), for the operation, its alternation and its table
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra-of-quaternions.md`), for the coincidence of the nilpotents with the zero divisors
- *Annihilators of the Antisymmetric Plain Algebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-algebra-of-quaternions.md`), for the annihilator of an element and the self-annihilation
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-plain-algebra-of-quaternions.md`), for the roots of $0$, which are the nilpotents
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`), for the division property that empties the parent's class
- *Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/nilpotents-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the nilpotent classes of the six structures side by side
- *Comparison of the Remarkable Subspaces of the Quaternions* (`articles_maths/comparison-of-the-remarkable-subspaces-of-the-quaternions.md`), for the subspaces on which the class is read
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for nilpotents, the index of nilpotency and the nilradical.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the nilpotent elements of a Lie algebra and the Engel theorem.
