# __Norm and Invertibility in the Antisymmetric Plain Algebra__

## Introduction

A norm and an inverse are read in a product, and the equations name it. The block of this
article is the antisymmetric plain multiplication
$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
$$
the cross product of the two vector parts, which is the antisymmetric half of the general plain
bilinear product; it is $\mathbb{C}$-bilinear, alternating, vector valued and without a unit
(*Introduction to the Antisymmetric Plain Algebra of Biquaternions*). The classical theory of the
norm and the inverse belongs to a unital associative product, and the block has neither a unit
nor an associativity; the present article states what that costs and what survives.

The answer is an absence and a substitute. The block has **no unit** on either side, hence **no
inverse** and an empty group of units; it has **no norm**, its square and its conjugated square
both vanishing identically. The quadratic objects it does carry are the operator trace form
$K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})$ and the scalar-part form
$\varphi(\tilde P,\tilde Q)=P_0Q_0$, and neither is multiplicative. The substitute the block
uses, and the form on which its whole Lie theory rests, is the operator trace form $K$, whose
identification with the invariant form of the block, its radical and its rank are owned by
*The Killing Form of the Antisymmetric Plain Algebra* and are cited here, not reproved. The
article closes with the comparison against the absent norm of the parent product and against the
invertibility criterion of the general plain algebra.

This article is algebraic throughout, and the word *norm* names the algebraic norm, an element of
the algebra and not a value in the reals. The general definitions of the unit and the inverse are *Definitions
for the Study of the 12 Algebraic Structures*; the product and its laws are *Introduction to the
Antisymmetric Plain Algebra of Biquaternions*; the norm of the general plain product, to which
the block is compared, is *Norm and Invertibility in the General Plain Algebra*.

## The Notion and Its Product

**Definition (unit of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is
a **left unit of $\star$** when $e\star x=x$ for every $x$; a **right unit of $\star$** when
$x\star e=x$ for every $x$; and a **two-sided unit of $\star$** when it is both
(*Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*).

**Definition (inverse).** Let $\star$ be a product with a two-sided unit $e$. An element $x$ is
**invertible of $\star$** when there is $y$ with $x\star y=y\star x=e$; such a $y$ is an
**inverse of $x$ of $\star$**.

Throughout this article the product is the **antisymmetric plain multiplication** $\wedge$ of the
block, $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$, and unqualified,
*unit* and *inverse* mean the unit and the inverse of $\wedge$. The product is written from the
general plain bilinear product $\tilde P\tilde Q$ by antisymmetrisation, the construction of
*The Symmetric and Antisymmetric Parts of an Algebra Product*. The reader is asked to keep the
reading relative: the unit $e_0$ of the algebra is a unit of the plain product and is not a unit
of the block, and no equation below is transferred across the exchange of the two products.

## The Absence of a Unit

**Proposition (no unit).** The operation $\wedge$ has no left unit and no right unit; there is
no $\tilde E$ with $\tilde E\wedge\tilde X=\tilde X$ for all $\tilde X$, and none with
$\tilde X\wedge\tilde E=\tilde X$ for all $\tilde X$.

*Proof.* Let $\tilde E$ be a left unit. Evaluating at $\tilde X=e_0$, whose vector part is zero,
gives
$$
\tilde E\wedge e_0=\mathbf{E}\times\mathbf{0}=0,
$$
which would have to equal $e_0$; the two differ, since $e_0$ is nonzero. Let $\tilde E$ be a
right unit. Evaluating at $\tilde X=e_0$ gives
$$
e_0\wedge\tilde E=\mathbf{0}\times\mathbf{E}=0,
$$
which would again have to equal $e_0$. Hence neither one-sided unit exists.

The absence is structural and not accidental: the value of the block is a pure vector for every
pair of arguments, and the equations that would name a unit require the central element $e_0$ on
the right. The scalar direction is invisible to the operation, and a unit is exactly an element
the operation cannot see.

## The Absence of an Inverse

**Corollary (no inverse).** No element of $\mathbb{B}$ is invertible of the block. Equivalently,
the group of units of $\wedge$, the set of elements that have an inverse of $\wedge$, is empty.

*Proof.* The inverse is defined by the pair of equations
$\tilde X\wedge\tilde Y=e$ and $\tilde Y\wedge\tilde X=e$, with $e$ a two-sided unit of the
product; the block has no two-sided unit by
the proposition above, so the equations have no solution, whatever the pair $(\tilde X,\tilde Y)$.
There is no one-sided notion either, the one-sided inverse being defined against a one-sided unit
and no one-sided unit existing.

**Remark (the equation to the centre).** A direct computation reaches the same conclusion
without naming a unit. The equation
$$
\tilde X\wedge\tilde Y=e_0
$$
has no solution in $\mathbb{B}$, because the left side is a pure vector, of scalar part zero, for
every pair $\tilde X,\tilde Y$, and the right side has scalar part one. The block cannot produce a
central value at all, so the equation that defines an inverse is unsolvable even before the
two-sided character of the unit is required.

## The Absence of a Norm

**Definition (norm of a product).** The **algebraic norm** attached to a product $\star$ with an
involution ${}^{\natural}$ is the quadratic map
$q_\star(\tilde X)=\tilde X\star\tilde X^{\natural}$, read as an element of $\mathbb{B}$ and not
as a real number; for the general plain bilinear product it is the central square
$N(\tilde X)e_0=\tilde X\tilde X^{\natural}$ with $N(\tilde X)=\sum_\mu X_\mu^{2}$
(*Norm and Invertibility in the General Plain Algebra*).

For the block the two quadratic maps available are the square and the conjugated square, and
neither is a norm.

**Proposition (the block has no norm).** For every element $\tilde X$,
$$
\tilde X\wedge\tilde X=0,\qquad
\tilde X\wedge\tilde X^{\natural}=0 .
$$
Both canonical quadratics of the block — the square and the conjugated square — vanish
identically, so neither is a norm.

*Proof.* The first identity is alternation, $\tilde X\wedge\tilde X=0$ for every $\tilde X$, by
*Introduction to the Antisymmetric Plain Algebra of Biquaternions*. For the second, the natural
conjugate is $\tilde X^{\natural}=X_0e_0-\mathbf{X}$, and the value of the block on a pair is the
cross product of the two vector parts, so
$$
\tilde X\wedge\tilde X^{\natural}
=\mathbf{X}\times(-\mathbf{X})=-\bigl(\mathbf{X}\times\mathbf{X}\bigr)=0 ,
$$

The failure is total, and it is stronger than the failure of the quaternionic sibling of this
block. The block removes the scalar part of the parent product; the parent's central-valued
quadratic form is the norm $N(\tilde X)=X_0^{2}+(\mathbf{X},\mathbf{X})$, read from the product
$\tilde X\tilde X^{\natural}$ with the conjugate, and the block, whose values are pure vectors,
produces no central value at all. The block inherits the square of the parent with the scalar part
removed, and with the scalar part removed from a square the central quadratic form
is gone. What replaces it is a pair of forms on the whole space, and an operator form, which are
the subject of the next section.

## The Two Forms and the Operator Form

**Definition (the operator trace form).** The **operator trace form** of the block is
$$
K(\tilde A,\tilde B)=\operatorname{Tr}\bigl(L_{\tilde A}L_{\tilde B}\bigr),
\qquad L_{\tilde A}\tilde R=\tilde A\wedge\tilde R ,
$$
the trace of the composition of the two left multiplication operators.

**Definition (the scalar-part form).** The **scalar-part form** of the block is
$$
\varphi(\tilde P,\tilde Q)=P_0Q_0 ,
$$
the product of the two scalar parts.

**Proposition (the operator trace form).** For all $\tilde A,\tilde B$,
$$
K(\tilde A,\tilde B)=-2\,\mathbf{A}\cdot\mathbf{B}=-2\,(A_1B_1+A_2B_2+A_3B_3),
$$
so on the diagonal $K(\tilde X,\tilde X)=-2(\mathbf{X},\mathbf{X})$, the Gram matrix of $K$ in the
basis is $\operatorname{diag}(0,-2,-2,-2)$, the rank of $K$ is three, its radical is the centre
$\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, and on the vector subspace $K$ is non-degenerate.

*Proof.* The operator $L_{\tilde A}$ kills the scalar direction and acts on the vector part by
$\mathbf{X}\mapsto\mathbf{A}\times\mathbf{X}$, so
$$
L_{\tilde A}L_{\tilde B}\mathbf{X}
=\mathbf{A}\times(\mathbf{B}\times\mathbf{X})
=\mathbf{B}\,(\mathbf{A}\cdot\mathbf{X})-(\mathbf{A}\cdot\mathbf{B})\,\mathbf{X} .
$$
The first summand is the rank-one operator $\mathbf{X}\mapsto\mathbf{B}(\mathbf{A}\cdot\mathbf{X})$,
of trace $\mathbf{A}\cdot\mathbf{B}$, and the second is $-(\mathbf{A}\cdot\mathbf{B})$ times the
identity of the three-dimensional vector part, of trace $-3(\mathbf{A}\cdot\mathbf{B})$; the
scalar direction contributes nothing. The trace is therefore $-2\,\mathbf{A}\cdot\mathbf{B}$. The
Gram entries are read at the units, $\mathbf{e}_i\cdot\mathbf{e}_j=\delta_{ij}$, and the radical
is the set orthogonal to every vector part, that is the centre. Computed exactly on general
elements with coefficients in $\mathbb{Q}(i)$ and on the sixteen pairs of the basis.

**Proposition (the invariance of the two forms).** Both forms are symmetric and invariant under
the block: for all $\tilde P,\tilde Q,\tilde X$,
$$
K\bigl(\tilde P\wedge\tilde X,\tilde Q\bigr)+K\bigl(\tilde X,\tilde P\wedge\tilde Q\bigr)=0,
\qquad
\varphi\bigl(\tilde P\wedge\tilde X,\tilde Q\bigr)+\varphi\bigl(\tilde X,\tilde P\wedge\tilde Q\bigr)=0 .
$$

*Proof.* For $K$ the invariance equation reads, by the formula of the previous proposition,
$$
-2\,(\mathbf{P}\times\mathbf{X})\cdot\mathbf{Q}-2\,\mathbf{X}\cdot(\mathbf{P}\times\mathbf{Q})=0,
$$
which is the alternation of the scalar triple product,
$(\mathbf{P}\times\mathbf{X})\cdot\mathbf{Q}=\mathbf{X}\cdot(\mathbf{P}\times\mathbf{Q})$ with a
sign; the centre contributes nothing to either slot. For $\varphi$ both terms vanish outright,
because $\tilde P\wedge\tilde X$ and $\tilde P\wedge\tilde Q$ are pure vectors and the
scalar-part form of an element with a central argument is zero. The symmetry of $K$ is the
symmetry of $\mathbf{A}\cdot\mathbf{B}$, and that of $\varphi$ is the symmetry of the product of
the two scalar parts.

**Remark (the two invariant forms).** The operator trace form $K$ and the scalar-part form
$\varphi$ are independent, and they span the invariant symmetric forms of the block: a
computation on the central direction forces every invariant form to annihilate the pairings of
the centre with the vector part, and on the vector subspace the form is proportional to
$\mathbf{P}\cdot\mathbf{Q}$, the vector subspace carrying the irreducible three-dimensional
representation of the block (*The Lie Algebra of the Antisymmetric Plain Algebra*). The two
extremes are $\varphi$, of rank one, whose radical and isotropic cone are the whole vector
subspace, and $K$, non-degenerate on the vector subspace, whose radical is the centre. The
combination $\varphi+\tfrac12K$ is the trace form $\operatorname{Sc}(\tilde P\tilde Q)$ of the
associative parent, invariant for the same reason.

**Remark (the substitute).** The form the block uses is $K$: it is the invariant form of the
block, identified with the Killing form of the bracket in *The Killing Form of the Antisymmetric
Plain Algebra*, and its radical, its rank, the reading of the Cartan criteria on it and the Casimir
element it produces are that article's subject. The present article only fixes the definition and
the diagonal value, and cites the rest. The scalar-part form $\varphi$ is the complementary rank-
one form; in the quaternionic sibling of this block the roles are exchanged, the rank-one form
being there the substitute and the operator trace form failing invariance, because there the
product is not a Lie bracket.

## Multiplicativity

**Definition (multiplicativity).** Let $\star$ be a product and let $q$ be a quadratic form on
$\mathbb{B}$, valued in $\mathbb{C}$ or in the centre. The form is **multiplicative of $\star$**
when
$$
q(x\star y)=q(x)\,q(y)
$$
for all $x,y$, the equation being read in the scalars.

**Proposition (no multiplicativity).** The square is the zero map and satisfies the
multiplicativity equation only because both sides vanish, so it is a norm in no sense. Of the
three nonzero quadratic forms available, none is multiplicative: the operator trace
form gives
$$
K(e_1\wedge e_2,e_1\wedge e_2)=K(e_3,e_3)=-2
\quad\text{against}\quad
K(e_1,e_1)K(e_2,e_2)=(-2)(-2)=4 ;
$$
the scalar-part form gives
$$
\varphi(e_0\wedge e_0,e_0\wedge e_0)=\varphi(0,0)=0
\quad\text{against}\quad
\varphi(e_0,e_0)^{2}=1 ;
$$
and the norm $N$ of the parent product gives
$$
N(e_1\wedge e_1)=N(0)=0
\quad\text{against}\quad
N(e_1)^{2}=1 .
$$

*Proof.* The square vanishes at every element, so both sides of its multiplicativity equation
vanish and the equation carries no information. Each displayed pair separates the two sides: the
values of the block are $e_1\wedge e_2=e_3$, $e_0\wedge e_0=0$ and $e_1\wedge e_1=0$, read from
the table of the block, and the three right sides are computed from $K=-2\,\mathbf{A}\cdot\mathbf{B}$,
$\varphi=P_0Q_0$ and $N(\tilde X)=\sum_\mu X_\mu^{2}$. A single pair separates the two sides in
each case, so no multiplicativity holds.

The failure at the pairs displayed is the same failure the absence
of a norm records: a multiplicative quadratic form of a product that has a unit takes the value
one at the unit, and the block has no unit, so the general multiplicativity equation has no reason
to hold and does not.

## The Comparison with the Parent Product

**Remark (what the removal of the scalar part costs).** The parent product, the general plain
bilinear product $\tilde P\tilde Q$, is associative and unital, with unit $e_0$, and it carries
the central square $N(\tilde X)e_0=\tilde X\tilde X^{\natural}$ with
$N(\tilde X)=\sum_\mu X_\mu^{2}$, the norm of the general plain algebra. Its antisymmetric half,
the block, is the parent with the scalar part removed, and the two losses are one loss: a norm is
a central-valued quadratic map, and the block's values are pure vectors, so the block carries no
central quadratic form. The scalar part of the parent contributes to the norm through its square
$X_0^{2}$, which in the block survives only as the rank-one form $\varphi$.

**Remark (the invertibility criterion is not transferred).** For the general plain algebra the
invertibility criterion is $N(\tilde Q)\neq0$, equivalently the central square nonzero
(*Norm and Invertibility in the General Plain Algebra*). The criterion names the product, and for
the block the corresponding statement is the absence of the previous sections: there is no unit
against which to invert, and the substitute equation $\tilde X\wedge\tilde Y=e_0$ has no
solution. No element of the block is invertible, and the empty group of units is the sharp form of
the statement.

## Summary

The antisymmetric plain multiplication $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ has no
unit on either side, hence no invertible element and an empty group of units, and the inverse
equation $\tilde X\wedge\tilde Y=e_0$ has no solution because every value of the block is a pure
vector. The block has no norm: its square vanishes identically by alternation, and its conjugated
square vanishes identically as well, $\tilde X\wedge\tilde X^{\natural}=\mathbf{X}\times(-\mathbf{X})=0$,
so neither canonical quadratic is a norm, and the central-valued norm of
the parent product is lost with the scalar part of the parent. The two quadratic objects that
survive are the operator trace form
$K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})=-2\,\mathbf{A}\cdot\mathbf{B}$,
of Gram matrix $\operatorname{diag}(0,-2,-2,-2)$, rank three and radical the centre, which is the
invariant form of the block and the Killing form of the bracket, and the rank-one scalar-part form
$\varphi(\tilde P,\tilde Q)=P_0Q_0$, whose radical and isotropic cone are the vector subspace;
the two are independent and span the invariant symmetric forms, and neither is multiplicative, the
pairs $(e_1,e_2)$, $(e_0,e_0)$ and $(e_1,e_1)$ separating the two sides of the multiplicativity
equation. The invertibility criterion of the general plain algebra is not transferred, and its
place is taken by the absence of a unit and of an inverse.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\tilde P\tilde Q$ | the parent general plain bilinear product, associative and unital |
| $L_{\tilde A}\tilde R=\tilde A\wedge\tilde R$ | the left multiplication operator of the block |
| $K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})=-2\,\mathbf{A}\cdot\mathbf{B}$ | the operator trace form, rank three, radical the centre, the invariant form of the block |
| $\varphi(\tilde P,\tilde Q)=P_0Q_0$ | the scalar-part form, rank one, radical the vector subspace |
| $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the norm of the general plain algebra, not a norm of the block |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the radical of $K$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the radical and the isotropic cone of $\varphi$ |
| $e_0$ | the unit of the parent product, not a unit of the block |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the unit, the inverse and the relativity of the definitions to the product
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the operation, its class, its image and the absence of a unit
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the identification of $K$ with the invariant form of the block, its radical, its rank, the Cartan criteria and the Casimir element
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the norm of the plain product, its multiplicativity and the invertibility criterion the block does not have
- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the antisymmetrisation from which the block is written
- *Norm and Invertibility in the Antisymmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-antisymmetric-quaternionic-algebra.md`), the sibling of this article, whose conjugated square is a pure vector where the block's vanishes
