# __The Specificities of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic multiplication
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)
=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q
$$
is alternating, vector valued and without a unit, and it fails the Jacobi identity
(*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*, *The Jacobi Failure
and the Associator Defect of the Antisymmetric Quaternionic Algebra*). As an element-theoretic
object the block is poor: every element is a nilpotent, the origin is the only idempotent, there
is no root of $-1$ or of $+1$, and there is no unit and no inverse. As an **operator-theoretic**
object it has one sharp feature, and the feature is the whole of the present article.

The feature is the action of the algebra unit. For the block,
$$
L_{e_0}\tilde X=e_0\diamond\tilde X=\mathbf X , \qquad
R_{e_0}\tilde X=\tilde X\diamond e_0=-\mathbf X , \qquad
L_{e_0}^{2}=L_{e_0},
$$
so the left multiplication by $e_0$ is the **projection onto the vector subspace** along the
centre, and the right multiplication is its negative. The block is the **only** one of the twelve
structures in which some element multiplies as the projection onto the vector subspace; the
element is necessarily $e_0$, and it is uniquely determined. Equivalently, the block is the only
one in which the canonical splitting
$$
\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}
$$
is realised by the multiplication by a single element, the element being the unit of the ambient
algebra, which is not a unit of the block. The criterion is stated as the identity
$L_{e_0}=P_{\mathrm{Vect}}$, it is proved equivalent to the projector classification
$L_{\tilde X}^{2}=L_{\tilde X}\Leftrightarrow\tilde X\in\{0,e_0\}$, and it is tested on the other
eleven structures. The model is *The Specificities of the General Plain Algebra*, which states
left alternativity as its criterion; the twinned articles are *The Specificities of the General
Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic Algebra*.

## Placement

The article is the closing entry of the block, after the introduction, the Jacobi failure, the
invariant forms, the remarkable subspaces, the adjoint operators and the two matrix models. It
uses the operation and its image of *Introduction to the Antisymmetric Quaternionic Algebra of
Biquaternions*, the classification of the operators of *The Adjoint Operators of the
Antisymmetric Quaternionic Algebra*, the invariant form of *The Invariant Bilinear Forms of the
Antisymmetric Quaternionic Algebra*, and the vanishing of the alternating centre of *The Jacobi
Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*; and it proves, for
the block, the row that *The Specificities of the General Plain Algebra* records in its table:
*the unit, whose operator is the projection onto the vector subspace*. The eleven comparisons
below are the other rows of that table read against this one.

## Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with
$e_1e_2=e_3$ and central scalar imaginary $i$. The operation of the block is $\diamond$,
$\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$;
the parent product is $\tilde P^{\natural}\tilde Q$ and the symmetric half is $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$. An element
is $\tilde P=P_0e_0+\mathbf P$ with $\mathbf P=\sum_kP_ke_k$; $\mathrm{Vect}(\mathbb{B})$ is the
vector subspace of the pure elements, of complex dimension three, and
$\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ is the centre. The **left multiplication** of the block
is $L_{\tilde A}\tilde X=\tilde A\diamond\tilde X$, and $L_{\tilde A}^{2}=L_{\tilde A}L_{\tilde A}$
is the composite. A **projector** is an idempotent operator, and an **idempotent** is an element
equal to its own square; the two levels are never interchanged, and the block is the example
that makes the distinction visible: its idempotents are the origin alone, while the operator of
the element $e_0$ is a projector.

## The Governing Identity

**Proposition (the unit acts as the projection onto the vector subspace).** For every element
$\tilde X$,
$$
L_{e_0}\tilde X=\mathbf X , \qquad R_{e_0}\tilde X=-\mathbf X , \qquad L_{e_0}^{2}=L_{e_0}.
$$
The image of $L_{e_0}$ is $\mathrm{Vect}(\mathbb{B})$, its kernel is $\mathbb{C}_{\mathbb{B}}$,
and $\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$.

*Proof.* The explicit form at $\tilde P=e_0$, where $P_0=1$ and $\mathbf P=\mathbf 0$, gives
$e_0\diamond\tilde X=\mathbf X$, and at $\tilde Q=e_0$ it gives
$\tilde X\diamond e_0=-\mathbf X$. The map $\tilde X\mapsto\mathbf X$ is the identity on the
vector subspace and vanishes on the centre, so it is a projector, its square is itself, its
image is $\mathrm{Vect}(\mathbb{B})$ and its kernel is $\mathbb{C}_{\mathbb{B}}$; the two are
complementary because every element is the sum of its scalar and vector parts.

**Remark (the element is not a unit).** The element $e_0$ satisfies $e_0\diamond\tilde X=\mathbf X$,
which is $\tilde X$ only when $\tilde X$ is pure; at a non-pure element the scalar part is
discarded. The block has no unit (*Introduction to the Antisymmetric Quaternionic Algebra of
Biquaternions*), and $e_0$ is a **left identity on the vector subspace** and not a unit: it acts
as the identity there and annihilates the centre, and its right action is the negative of its
left action. The identity $R_{e_0}=-L_{e_0}$ is the alternation of the block read at the unit.

## The Projector Classification

**Theorem (the criterion of the block).** The left multiplication of an element is a projector
exactly at the origin and at the algebra unit,
$$
L_{\tilde X}^{2}=L_{\tilde X}\iff \tilde X=0\ \text{or}\ \tilde X=e_0 .
$$
The two projectors are the zero operator and the projection onto the vector subspace.

*Proof.* Write $L_{\tilde X}\tilde Y=\tilde U$ with
$\tilde U=X_0\mathbf Y-Y_0\mathbf X-\mathbf X\times\mathbf Y$; the value is pure, so
$L_{\tilde X}^{2}\tilde Y=L_{\tilde X}\tilde U=X_0\tilde U-\mathbf X\times\tilde U$, and the
projector condition reads $X_0\tilde U-\mathbf X\times\tilde U=\tilde U$ for every $\tilde Y$.
At $\tilde Y=e_0$, where $Y_0=1$ and $\mathbf Y=\mathbf 0$, one has $\tilde U=-\mathbf X$, and
the condition becomes $(X_0-1)\mathbf X=\mathbf 0$; so either $\mathbf X=\mathbf 0$ or
$X_0=1$. If $\mathbf X=\mathbf 0$, then $L_{\tilde X}\tilde Y=X_0\mathbf Y$ and the projector
condition is $X_0^{2}=X_0$, giving $X_0=0$ or $X_0=1$, that is $\tilde X=0$ or
$\tilde X=e_0$. If $\mathbf X\neq\mathbf 0$ and $X_0=1$, the condition reads
$\mathbf X\times\tilde U=0$ for every $\tilde Y$, so $\tilde U$ is parallel to $\mathbf X$ at
every $\tilde Y$; taking $\tilde Y$ pure with $\mathbf Y$ perpendicular to $\mathbf X$ gives
$\tilde U=\mathbf Y-\mathbf X\times\mathbf Y$, a vector perpendicular to $\mathbf X$ and nonzero,
against the requirement, so this case is impossible. The two admissible elements give
$L_0=0$ and $L_{e_0}=P_{\mathrm{Vect}}$ by the governing identity.

The classification is short and rigid: two projectors, the zero operator at the origin and the
projection onto the vector subspace at the unit, and nothing between. It is the **smallest
projector class a structure can have while carrying a nonzero projector**, and it is the exact
opposite of the general plain algebra, whose projector class is the whole idempotent family.

## The Splitting Realised by One Element

**Corollary (the splitting is a multiplication).** The canonical splitting of the space into
the vector subspace and the centre is realised by the multiplication of the single element
$e_0$:
$$
\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}},
\qquad
\mathrm{Vect}(\mathbb{B})=\operatorname{im}L_{e_0},
\qquad
\mathbb{C}_{\mathbb{B}}=\ker L_{e_0}.
$$
The vector subspace is the image of the block and a left ideal of the block, and the centre is
the kernel of $L_{e_0}$.

*Proof.* The splitting and the identifications are the governing identity. The image of the
block is $\mathrm{Vect}(\mathbb{B})$, and it is a left ideal because for $\mathbf A$ pure and
any $\tilde Y$ the value $\mathbf A\diamond\tilde Y=-Y_0\mathbf A-\mathbf A\times\mathbf Y$ is
pure; the centre is the kernel of $L_{e_0}$ by the same identity.

The corollary is the useful form of the criterion. In the block the two subspaces the theory
names — the derived subalgebra, on which the operation is a Lie bracket, and the centre, on which
it vanishes — are the image and the kernel of the multiplication by one element, and the element
is the unit of the ambient algebra. No other structure of the twelve has this: elsewhere the
splitting, when it exists, is carried by an idempotent, a family, or not at all.

## The Eleven Comparisons

The table gives, for each of the twelve structures $\star$, the left multiplication by the
algebra unit $e_0$ and the elements whose left multiplication is a projector. The two columns are
read from the twelve operations of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$
Space*; the rows of $\mathrm{GPA}$, $\mathrm{GQA}$ and $\mathrm{SQA}$ are the theorems of *The
Specificities of the General Plain Algebra*, of *The Specificities of the General Quaternionic
Algebra* and of *The Specificities of the Symmetric Quaternionic Algebra*. The zero operator is a
projector, so the origin belongs to every row and is listed only where the whole class is trivial;
the structures in which the multiplication by the unit vanishes give the zero operator on a whole
subspace, and the row names that subspace.

| structure $\star$ | $L_{e_0}$ | the elements whose $L$ is a projector |
|---|---|---|
| GPA | the identity | every idempotent, by left alternativity |
| GQA | the identity | the plain idempotents, with the index conjugated |
| SPA | the identity | $e_0$ alone, with the origin |
| SQA | the projection onto the centre | the elements of scalar coordinate $1$, with the origin |
| APA | zero | the centre, whose operator is the zero operator |
| AQA | the projection onto the vector subspace | the origin and $e_0$ |
| GPS | the star, conjugate-linear | the origin alone |
| GQS | the star, conjugate-linear | the origin alone |
| SPS | a conjugate-linear map | the origin alone |
| SQS | the star, conjugate-linear | the origin alone |
| APS | a conjugate-linear map | the origin alone |
| AQS | zero | the centre, whose operator is the zero operator |

**Theorem (the uniqueness).** Of the twelve structures, the block is the only one in which the
left multiplication by the algebra unit is a projector whose image is the vector subspace, and
the only one admitting an element $\tilde E$ with
$$
\tilde E\star\tilde X=\mathbf X
$$
for every $\tilde X$. The element is $\tilde E=e_0$, and the image of the multiplication is the
vector subspace.

*Proof.* The block's entry is the governing identity. For the other eleven, read the table. In
GPA, GQA and SPA the unit acts as the identity, whose image is the whole space and not the vector
subspace; in SQA it acts as the projection onto the centre, whose image is the centre; in APA and
AQS it acts as zero. In the six sesquilinear structures the left multiplication by $e_0$ is
conjugate linear or zero, and a conjugate-linear map is not the $\mathbb{C}$-linear projection
onto the vector subspace; where it is zero, as in AQS, the image is not the vector subspace either.
A conjugate-linear map $L$ with $L^{2}=L$ would be linear and conjugate-linear at once, hence
zero, so in the six the only projector is the zero operator, and the elements whose operator
vanishes are the origin alone in the five products whose value reads a conjugate-linear slot and
the centre in AQS.

For the element $\tilde E$ the equation $\tilde E\star\tilde X=\mathbf X$ at $\tilde X=e_0$ reads
$\tilde E\star e_0=0$, and $\tilde E\star e_0$ is $\tilde E$ in GPA, SPA and GPS, $\tilde E^{\natural}$
in GQA, GQS and SQS, and $E_0e_0$ in SQA and SPS. In the eight the equation therefore forces
$\tilde E=0$, or $E_0=0$ with the image inside the centre, and at a pure $\tilde X$ the left side is
then zero or central where $\mathbf X$ is not; in APA and AQS the value at $e_0$ vanishes identically
and the pure values are the cross products $\mathbf E\times\mathbf X$
in APA and $\mathbf E\times\overline{\mathbf X}$ in AQS, which lie in the orthogonal plane of
$\mathbf E$; and in APS the value at $e_0$, which is $\mathbf E$, forces $\tilde E=E_0e_0$, after
which the values at $e_1$ and at $ie_1$ force the contradictory $E_0=-1$ and $E_0=1$. No structure other than the block admits $\tilde E$, and
inside the block the element is unique, as the faithfulness of its multiplication shows: at
$\tilde X=e_0$ the equation gives $-\mathbf E=0$, so $\mathbf E=0$, and at a pure vector
$\tilde X$ it gives $E_0\tilde X=\tilde X$, so $E_0=1$.

The comparison separates the twelve in one line. In five structures the unit acts as the identity
or as the zero operator, in one it acts as the projection onto the centre, in five it acts through
a conjugate-linear map, and in one — the block — it acts as the projection onto the vector
subspace. The
block is alone in its row, and the reason is the two mixed terms $P_0\mathbf Q-Q_0\mathbf P$ that
it carries and that the plain antisymmetrisation does not: those terms make the unit act on the
scalar direction and so turn its multiplication into a proper projection.

## The Other Criteria Fail Here

Two criteria adjacent to the block's are the criterion of the general plain algebra and the
criterion of the symmetric quaternionic algebra, and neither holds for the block.

**Remark (the alternativity criterion fails).** The criterion of the general plain algebra is
left alternativity, $L_{\tilde X}^{2}=L_{\tilde X\cdot\tilde X}$ for every $\tilde X$, the
square being read in the product at hand; read for the block it becomes
$L_{\tilde X}^{2}=L_{\tilde X\diamond\tilde X}=L_0=0$, so the criterion would demand
$L_{\tilde X}^{2}=0$ for every element; at $\tilde X=e_0$ the operator is the projection onto
the vector subspace, whose square is itself and not zero. The criterion fails at the unit of the
algebra, and the block is one of the eleven structures on which it fails.

**Remark (the rank-one criterion fails).** The criterion of the symmetric quaternionic algebra
is the rank-one identity $L^{\bullet}_{\tilde X}{}^{2}=X_0L^{\bullet}_{\tilde X}$, in which the
scalar coordinate is the coefficient. For the block the corresponding display is false away from
the two elements of the classification: at $\tilde X=e_1$, where $X_0=0$, the right side is the
zero operator while $L_{e_1}^{2}$ is nonzero. The block's criterion is therefore not a scalar
multiple of its own operator; it is the projector identity read at the two elements $0$ and
$e_0$.

## What the Criterion Delivers

The criterion is a classification and not a decomposition theory. What it delivers for the block
is the following short list, and the block carries nothing more.

- **Two projectors.** The zero operator and the projection onto the vector subspace, the latter
    at the element $e_0$.
- **One splitting.** $\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$, the
    image and the kernel of $L_{e_0}$.
- **One left ideal.** The vector subspace, which is the whole image of the block as well as a
    left ideal.
- **No Peirce calculus.** The decompositions indexed by an idempotent do not exist, there being
    no nontrivial idempotent; the ideal theory and the module theory of the plain product have no
    analogue here.

The block is thus the structure in which the projector survives as a single element and not as a
family, and in which the splitting of the space is a statement about one multiplication. This is
the exact sense of its row in the table of the twelve: the unit carries the projector, the
projector is the projection onto the vector subspace, and there is no other.

## Summary

The antisymmetric quaternionic multiplication is the alternating structure whose left
multiplication by the algebra unit is the projection onto the vector subspace,
$L_{e_0}\tilde X=\mathbf X$, $L_{e_0}^{2}=L_{e_0}$, with $R_{e_0}=-L_{e_0}$; the projector
classification of the block is the pair $L_{\tilde X}^{2}=L_{\tilde X}\Leftrightarrow\tilde X\in\{0,e_0\}$, so the projector class is the smallest a structure with a nonzero projector can
have. The projection is the canonical splitting $\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus \mathbb{C}_{\mathbb{B}}$ realised by the multiplication of one element, the vector subspace
being the image of the block and a left ideal and the centre its kernel. The block is the only
one of the twelve in which the algebra unit multiplies as the projection onto the vector
subspace, and the only one admitting an element $\tilde E$ with $\tilde E\star\tilde X=\mathbf X$
for every $\tilde X$, the element being $e_0$ uniquely; the other eleven give the identity, the
projection onto the centre, the zero operator or a conjugate-linear map at the unit, and none of
them gives this projection. The alternativity criterion of the plain algebra and the rank-one
criterion of the symmetric quaternionic algebra both fail for the block, and the criterion stated
here is its own. What the block delivers is two projectors, one splitting and one left ideal, and
no Peirce calculus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $L_{\tilde A}\tilde X=\tilde A\diamond\tilde X$, $R_{\tilde A}\tilde X=\tilde X\diamond\tilde A$ | the left and the right multiplication of the block |
| $L_{e_0}=P_{\mathrm{Vect}}$ | the criterion, the unit multiplying as the projection onto the vector subspace |
| $L_{\tilde X}^{2}=L_{\tilde X}$ | the projector equation; its solutions are $0$ and $e_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the image of $L_{e_0}$ and of the block, a left ideal |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the kernel of $L_{e_0}$ |
| GPA … AQS | the twelve structures, coded as in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* |

## Further Reading

- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), for the criterion of left alternativity, the table of the twelve and the row this article proves
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the first border case, where the projectors are indexed by the plain idempotents
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the second border case, the hyperplane of rank-one projections onto the centre
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its image, the one-sided action of the unit and the absence of a unit
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the operators $L_{\tilde A}$, their matrices, their ranks and the elements for which the rank drops
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the form whose radical is the image of the projection
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the twelve operations and their two alternating rows
