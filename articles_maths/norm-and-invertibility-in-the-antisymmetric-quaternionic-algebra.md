# __Norm and Invertibility in the Antisymmetric Quaternionic Algebra__

## Introduction

A norm and an inverse are read in a product, and the equations name it. The antisymmetric
quaternionic multiplication of the block is
$$
\tilde P\diamond\tilde Q = \tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)
= P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q ,
$$
the antisymmetric part of the general quaternionic product $\tilde P^{\natural}\tilde Q$; it is
$\mathbb{C}$-bilinear, alternating, vector valued and without a unit, and it fails the Jacobi
identity (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*). The
classical theory of the norm and the inverse is the theory of a unital associative product, and
the block has neither a unit nor associativity; the present article states what that costs and
what survives.

The answer is an absence and a substitute. The block has **no unit** on either side, hence **no
inverse** and an empty group of units; it has **no norm**, its own square vanishing identically
and its conjugated square being vector valued rather than central; and the quadratic forms it
does carry — the invariant form $\varphi(\tilde P,\tilde Q)=P_0Q_0$ and the trace form
$K(\tilde A,\tilde B)=3A_0B_0-2\sum_kA_kB_k$ of its multiplication operators — are examined here
for multiplicativity and are **not multiplicative**. The substitute the block uses, and the only
form on which its theory rests, is the degenerate invariant form $\varphi$, whose invariance,
radical and isotropic cone are owned by *The Invariant Bilinear Forms of the Antisymmetric
Quaternionic Algebra* and are cited, not reproved. The article closes with the comparison
against the absent norm of the parent product and against the invertibility criterion of the
general plain algebra.

This article is algebraic throughout: the norm it discusses is an algebraic quadratic form, and no
notion of the analysis or of the geometry of the chapter is used. The general definitions
of the unit and the inverse are *Definitions for the Study of the 12 Algebraic Structures*; the
product and its laws are *Introduction to the Antisymmetric Quaternionic Algebra of
Biquaternions*; the norm of the general plain product, to which the block is compared, is *Norm
and Invertibility in the General Plain Algebra*.

## The Notion and Its Product

**Definition (unit of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is
a **left unit of $\star$** when $e\star x=x$ for every $x$; a **right unit of $\star$** when
$x\star e=x$ for every $x$; and a **two-sided unit of $\star$** when it is both
(*Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*).

**Definition (inverse).** Let $\star$ be a product with a two-sided unit $e$. An element $x$ is
**invertible of $\star$** when there is $y$ with $x\star y=y\star x=e$; such a $y$ is an
**inverse of $x$ of $\star$**.

Throughout this article the product is the **antisymmetric quaternionic multiplication**
$\diamond$ of the block, $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$, and unqualified, *unit* and *inverse* mean the unit and the inverse of
$\diamond$. The product is written from the general quaternionic product $\tilde P^{\natural}\tilde Q$
by antisymmetrisation, the construction of *The Symmetric and Antisymmetric Parts of an Algebra
Product*. The reader is asked to keep the reading relative: an inverse of the parent product is
not an inverse of the block, and no equation below is transferred across the exchange of the two.

## The Absence of a Unit

**Proposition (no unit).** The operation $\diamond$ has no left unit and no right unit; there is
no $\tilde E$ with $\tilde E\diamond\tilde X=\tilde X$ for all $\tilde X$, and none with
$\tilde X\diamond\tilde E=\tilde X$ for all $\tilde X$.

*Proof.* A left unit $\tilde E$ gives at $\tilde X=e_0$ the value $\tilde E\diamond e_0=-\mathbf E$,
which would have to equal $e_0$; a right unit gives at $\tilde X=e_0$ the value
$e_0\diamond\tilde E=\mathbf E$, which would have to equal $e_0$; and neither $-\mathbf E$ nor
$\mathbf E$ is central for a nonzero value of $\mathbf E$, while $\mathbf E=0$ gives the value
$0$. The same computation is *Introduction to the Antisymmetric Quaternionic Algebra of
Biquaternions*, §*The Image and the Absence of a Unit*.

The absence is structural and not accidental: the value of the block is a pure vector for every
pair of arguments, and the equations that would name a unit require the central element $e_0$ on
one side. The block has, however, a one-sided identity on its own image: the element $e_0$
satisfies $e_0\diamond\tilde X=\mathbf X$, the vector part of $\tilde X$, and
$\tilde X\diamond e_0=-\mathbf X$. This one-sided action is the subject of the specificities of
the block and is used there; the operation itself remains without a two-sided unit.

## The Absence of an Inverse

**Corollary (no inverse).** No element of $\mathbb{B}$ is invertible of the block. Equivalently,
the group of units of $\diamond$, the set of elements that have an inverse of $\diamond$, is
empty.

*Proof.* The inverse is defined by the two equations $\tilde X\diamond\tilde Y=\tilde Y\diamond\tilde X=e$, with $e$ a two-sided unit of the product; the block has no two-sided unit
by the proposition above, so the equations have no solution, whatever the pair
$(\tilde X,\tilde Y)$. There is no one-sided notion either, the one-sided inverse being defined
against a one-sided unit and no one-sided unit existing.

**Remark (the equation to the centre).** A direct computation reaches the same conclusion
without naming a unit. The equation
$$
\tilde X\diamond\tilde Y = e_0
$$
has no solution in $\mathbb{B}$, because the left side has zero scalar part for every pair
$\tilde X,\tilde Y$ and the right side has scalar part one. The block cannot produce a central
value at all, so the equation that defines an inverse is unsolvable even before the two-sided
character of the unit is required.

## The Absence of a Norm

**Definition (norm of a product).** The **algebraic norm** attached to a product $\star$ with an
involution ${}^{\natural}$ is the quadratic map $q_\star(\tilde X)=\tilde X\star\tilde X^{\natural}$,
read as an element of $\mathbb{B}$ and not as a real number; for the general plain bilinear
product it is the central square $N(\tilde X)e_0=\tilde X\tilde X^{\natural}$ with
$N(\tilde X)=\sum_\mu X_\mu^{2}$ (*Norm and Invertibility in the General Plain Algebra*).

For the block the two quadratic maps available are the square and the conjugated square, and
neither is a norm.

**Proposition (the block has no norm).** For every element $\tilde X$,
$$
\tilde X\diamond\tilde X = 0 , \qquad \tilde X\diamond\tilde X^{\natural} = -2X_0\mathbf X .
$$
The square vanishes identically, and the conjugated square is a pure vector and is central
exactly at the two sets $X_0=0$ and $\mathbf X=0$, that is on the vector subspace and on the
centre. Neither of the two quadratic maps built from the product, the square and the conjugated
square, takes its values in the centre at every element; the only central-valued quadratic form
the block carries is the one attached to the invariant form $\varphi$, the square $X_0^{2}$ of
the scalar part, and it is read from the form and not from the product.

*Proof.* The vanishing of the square is alternation. For the conjugated square, the explicit
form with $\tilde Q$ replaced by $\tilde X^{\natural}=X_0e_0-\mathbf X$ gives
$X_0(-\mathbf X)-X_0\mathbf X-(-\mathbf X)\times\mathbf X=-2X_0\mathbf X$, the cross term
vanishing because a vector crosses itself to zero. A pure vector $2X_0\mathbf X$ is central
exactly when it is zero.

The failure is total: the block removes the scalar part of the parent product, and the only
central-valued quadratic form the parent carries, the norm $N(\tilde X)=X_0^{2}+(\mathbf X,\mathbf X)$, is built from the scalar part that the block discards. The block inherits the
square of the parent product with the scalar part removed, and with the scalar part removed from
a square the quadratic form is gone. What replaces it is a pair of forms on the whole space, and
an operator form, which are the subject of the next two sections.

## The Two Forms and the Operator Form

**Definition (the invariant form).** The **invariant form** of the block is
$$
\varphi(\tilde P,\tilde Q)=P_0Q_0 ,
$$
the product of the two scalar parts; it is the unique $\mathbb{C}$-bilinear form invariant under
the block, and its quadratic form, radical and isotropic cone are owned by *The Invariant
Bilinear Forms of the Antisymmetric Quaternionic Algebra*.

**Definition (the operator trace form).** The **operator trace form** of the block is
$$
K(\tilde A,\tilde B)=\operatorname{Tr}\bigl(L_{\tilde A}L_{\tilde B}\bigr),
\qquad L_{\tilde A}\tilde R=\tilde A\diamond\tilde R ,
$$
the trace of the composition of the two left multiplication operators.

**Proposition (the quadratic forms).** On the diagonal the two forms read
$$
\varphi(\tilde X,\tilde X)=X_0^{2} , \qquad K(\tilde X,\tilde X)=3X_0^{2}-2(\mathbf X,\mathbf X) .
$$
The quadratic form of $\varphi$ has rank one, radical the vector subspace
$\mathrm{Vect}(\mathbb{B})$ and isotropic cone the same subspace; the quadratic form of $K$ is
non-degenerate, of Gram matrix $\operatorname{diag}(3,-2,-2,-2)$. The form $K$ is not invariant
under the block.

*Proof.* The two formulas are the diagonal readings of the forms of *The Invariant Bilinear
Forms of the Antisymmetric Quaternionic Algebra*: the first is $\varphi(\tilde P,\tilde Q)=P_0Q_0$ at $\tilde P=\tilde Q=\tilde X$, and the second is that article's
$K(\tilde A,\tilde B)=3A_0B_0-2\sum_kA_kB_k$ at $\tilde A=\tilde B=\tilde X$. The rank, the
radical and the isotropic cone are that article's propositions, and the failure of invariance is
its computation $K(\tilde A\diamond\tilde B,\tilde C)+K(\tilde B,\tilde A\diamond\tilde C)=-4A_0(\mathbf B,\mathbf C)+2B_0(\mathbf A,\mathbf C)+2C_0(\mathbf A,\mathbf B)$.

The form $\varphi$ is the substitute the block uses: it is the only form the product preserves,
and it is as degenerate as a nonzero form can be, its radical being the three-dimensional image
of the block. The form $K$ is the natural candidate for a Killing form; it is non-degenerate and
canonical, and it fails invariance, and that failure is the form-theoretic statement of the
failure of the Jacobi identity (*The Jacobi Failure and the Associator Defect of the
Antisymmetric Quaternionic Algebra*).

## Multiplicativity

**Definition (multiplicativity).** Let $\star$ be a product and let $q$ be a quadratic form on
$\mathbb{B}$, valued in $\mathbb{C}$ or in the centre. The form is **multiplicative of $\star$**
when
$$
q(x\star y)=q(x)\,q(y)
$$
for all $x,y$, the equation being read in the scalars.

**Proposition (no multiplicativity).** The square is the zero map, so it satisfies the
multiplicativity equation only because both sides vanish and it is a norm in no sense. None of
the three nonzero quadratic forms the block carries is multiplicative: the quadratic form of
$\varphi$ gives $\varphi(e_0\diamond e_0,e_0\diamond e_0)=0$ against
$\varphi(e_0,e_0)^{2}=1$; the quadratic form of $K$ gives $K(e_0\diamond e_0,e_0\diamond e_0)=0$
against $K(e_0,e_0)^{2}=9$; and the norm $N$ of the parent product gives
$N(e_0\diamond e_0)=0$ against $N(e_0)^{2}=1$.

*Proof.* The square vanishes at every element, so both sides of the multiplicativity equation
vanish and the equation carries no information. For the three forms, the value at the pair
$(e_0,e_0)$ is read from $e_0\diamond e_0=0$: the left side is $q(0)=0$ in every case, and the
right side is $q(e_0)^{2}$, which is $1^{2}=1$, $3^{2}=9$ and
$\bigl(1+(\mathbf 0,\mathbf 0)\bigr)^{2}=1$ for $\varphi$, for $K$ and for $N$ respectively. A
single pair separates the two sides in each case, so no multiplicativity holds.

The failure at the pair $(e_0,e_0)$ is the same failure the proposition on the absence of a norm
records: a multiplicative quadratic map of a product that has a unit takes the value one at the
unit, and the block has no unit, so the general multiplicativity equation has no reason to hold
and does not. The two forms that survive are nevertheless the object of the block's form theory,
and the operator trace form $K$ is the only non-degenerate one of the three, the invariant form
$\varphi$ being of rank one and the coefficient form zero; it is the canonical candidate for a
Killing form, and it fails invariance.

## The Comparison with the Parent Product

**Remark (what the removal of the scalar part costs).** The parent product $\tilde P^{\natural}\tilde Q$ is not unital either — it has $e_0$ as a left unit only — and its
element-theoretic norm is the central square $N(\tilde Q)e_0=\tilde Q^{\natural}\tilde Q$ with
$N(\tilde Q)=\sum_\mu Q_\mu^{2}$, the norm of the general plain algebra. Its antisymmetric half,
the block, is the parent with the scalar part removed, and the two losses are the same loss: the
scalar part of a square is the norm, and a product whose values have no scalar part has no norm.
The norm the parent keeps is the one the block loses with the scalar part, and what the block
keeps in its place is exactly $\varphi$ read on the diagonal, the square of the scalar part.

**Remark (the invertibility criterion is not transferred).** For the general plain algebra the
invertibility criterion is $N(\tilde Q)\neq0$, equivalently the central square nonzero
(*Norm and Invertibility in the General Plain Algebra*). The criterion names the product, and
for the block the corresponding statement is the absence of the previous sections: there is no
unit against which to invert, and the substitute equation $\tilde X\diamond\tilde Y=e_0$ has no
solution. No element of the block is invertible, and the empty group of units is the sharp form
of the statement.

## Summary

The antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ has no unit on either side, hence no invertible element
and an empty group of units, and the inverse equation $\tilde X\diamond\tilde Y=e_0$ has no
solution because every value of the block is a pure vector. The block has no norm: its square
vanishes identically by alternation, and its conjugated square is the pure vector
$-2X_0\mathbf X$, never central for a general element, so the central-valued norm of the parent
product is lost with the scalar part of the parent. The two quadratic maps that survive are the
invariant form $\varphi(\tilde P,\tilde Q)=P_0Q_0$, of rank one, radical and isotropic cone the
vector subspace, the unique invariant form of the block, and the operator trace form
$K(\tilde A,\tilde B)=3A_0B_0-2\sum_kA_kB_k$, non-degenerate and not invariant; none of the
three is multiplicative, the pair $(e_0,e_0)$ separating the two sides of the multiplicativity
equation in every case. The substitute the block uses is $\varphi$; the invertibility criterion
of the general plain algebra is not transferred, and its place is taken by the absence of a unit
and of an inverse.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde P^{\natural}\tilde Q$ | the parent general quaternionic product |
| $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$ | the left multiplication operator of the block |
| $\varphi(\tilde P,\tilde Q)=P_0Q_0$ | the invariant form of the block, rank one |
| $K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})$ | the operator trace form, non-degenerate, not invariant |
| $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the norm of the general plain algebra, not a norm of the block |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the radical and the isotropic cone of $\varphi$ |
| $e_0$ | the algebra unit, not a unit of the block, the left identity on the vector subspace |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the unit, the inverse and the relativity of the definitions to the product
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its class, its image and the absence of a unit
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for $\varphi$, its rank, its radical and its isotropic cone, and for the operator trace form $K$ and its failure of invariance
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the norm of the plain product, its multiplicativity and the invertibility criterion the block does not have
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`), for the failure of the Jacobi identity that the non-invariance of $K$ echoes
