# __The Specificities of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic multiplication
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)
=P_t\vec Q-Q_t\vec P-\vec P\times\vec Q
$$
is alternating, vector valued and without a unit, and it fails the Jacobi identity
(*Introduction to the Antisymmetric Quaternionic Algebra*, *The Jacobi Failure
and the Associator Defect of the Antisymmetric Quaternionic Algebra*). As an element-theoretic
object the block is poor: every element is a nilpotent, the origin is the only idempotent, there
is no root of $-1$ or of $+1$, and there is no unit and no inverse. As an **operator-theoretic**
object it has one sharp feature, and the feature is the whole of the present article.

The feature is the action of the algebra unit. For the block,
$$
L_{e_t}\tilde X=e_t\diamond\tilde X=\vec X , \qquad
R_{e_t}\tilde X=\tilde X\diamond e_t=-\vec X , \qquad
L_{e_t}^{2}=L_{e_t},
$$
so the left multiplication by $e_t$ is the **projection onto the vector subspace** along the
centre, and the right multiplication is its negative. The block is the **only** one of the twelve
structures in which some element multiplies as the projection onto the vector subspace; the
element is necessarily $e_t$, and it is uniquely determined. Equivalently, the block is the only
one in which the canonical splitting
$$
\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}
$$
is realised by the multiplication by a single element, the element being the unit of the ambient
algebra, which is not a unit of the block. The criterion is stated as the identity
$L_{e_t}=P_{\mathrm{Vect}}$, it is proved equivalent to the projector classification
$L_{\tilde X}^{2}=L_{\tilde X}\Leftrightarrow\tilde X\in\{0,e_t\}$, and it isolates the block among the
twelve structures. The model is *The Specificities of the Biquaternion Algebra*, which states
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
the block, the criterion that isolates it, the unit multiplying as the projection onto the vector
subspace.

## Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with
$\vec e_x\vec e_y=\vec e_z$ and central scalar imaginary $i$. The operation of the block is $\diamond$,
$\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$;
the parent product is $\tilde P^{\natural}\tilde Q$ and the symmetric half is $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$. An element
is $\tilde P=P_te_t+\vec P$ with $\vec P=P_x\vec e_x+P_y\vec e_y+P_z\vec e_z$; $\mathrm{Vect}(\mathbb{B})$ is the
vector subspace of the pure elements, of complex dimension three, and
$\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ is the centre. The **left multiplication** of the block
is $L_{\tilde A}\tilde X=\tilde A\diamond\tilde X$, and $L_{\tilde A}^{2}=L_{\tilde A}L_{\tilde A}$
is the composite. A **projector** is an idempotent operator, and an **idempotent** is an element
equal to its own square; the two levels are never interchanged, and the block is the example
that makes the distinction visible: its idempotents are the origin alone, while the operator of
the element $e_t$ is a projector.

## The Governing Identity

**Proposition (the unit acts as the projection onto the vector subspace).** For every element
$\tilde X$,
$$
L_{e_t}\tilde X=\vec X , \qquad R_{e_t}\tilde X=-\vec X , \qquad L_{e_t}^{2}=L_{e_t}.
$$
The image of $L_{e_t}$ is $\mathrm{Vect}(\mathbb{B})$, its kernel is $\mathbb{C}_{\mathbb{B}}$,
and $\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$.

*Proof.* The explicit form at $\tilde P=e_t$, where $P_t=1$ and $\vec P=\mathbf 0$, gives
$e_t\diamond\tilde X=\vec X$, and at $\tilde Q=e_t$ it gives
$\tilde X\diamond e_t=-\vec X$. The map $\tilde X\mapsto\vec X$ is the identity on the
vector subspace and vanishes on the centre, so it is a projector, its square is itself, its
image is $\mathrm{Vect}(\mathbb{B})$ and its kernel is $\mathbb{C}_{\mathbb{B}}$; the two are
complementary because every element is the sum of its scalar and vector parts.

**Remark (the element is not a unit).** The element $e_t$ satisfies $e_t\diamond\tilde X=\vec X$,
which is $\tilde X$ only when $\tilde X$ is pure; at a non-pure element the scalar part is
discarded. The block has no unit (*Introduction to the Antisymmetric Quaternionic Algebra of
Biquaternions*), and $e_t$ is a **left identity on the vector subspace** and not a unit: it acts
as the identity there and annihilates the centre, and its right action is the negative of its
left action. The identity $R_{e_t}=-L_{e_t}$ is the alternation of the block read at the unit.

## The Projector Classification

**Theorem (the criterion of the block).** The left multiplication of an element is a projector
exactly at the origin and at the algebra unit,
$$
L_{\tilde X}^{2}=L_{\tilde X}\iff \tilde X=0\ \text{or}\ \tilde X=e_t .
$$
The two projectors are the zero operator and the projection onto the vector subspace.

*Proof.* Write $L_{\tilde X}\tilde Y=\tilde R$ with
$\tilde R=X_t\vec Y-Y_t\vec X-\vec X\times\vec Y$; the value is pure, so
$L_{\tilde X}^{2}\tilde Y=L_{\tilde X}\tilde R=X_t\tilde R-\vec X\times\tilde R$, and the
projector condition reads $X_t\tilde R-\vec X\times\tilde R=\tilde R$ for every $\tilde Y$.
At $\tilde Y=e_t$, where $Y_t=1$ and $\vec Y=\mathbf 0$, one has $\tilde R=-\vec X$, and
the condition becomes $(X_t-1)\vec X=\mathbf 0$; so either $\vec X=\mathbf 0$ or
$X_t=1$. If $\vec X=\mathbf 0$, then $L_{\tilde X}\tilde Y=X_t\vec Y$ and the projector
condition is $X_t^{2}=X_t$, giving $X_t=0$ or $X_t=1$, that is $\tilde X=0$ or
$\tilde X=e_t$. If $\vec X\neq\mathbf 0$ and $X_t=1$, the condition reads
$\vec X\times\tilde R=0$ for every $\tilde Y$, so $\tilde R$ is parallel to $\vec X$ at
every $\tilde Y$; taking $\tilde Y$ pure with $\vec Y$ perpendicular to $\vec X$ gives
$\tilde R=\vec Y-\vec X\times\vec Y$, a vector perpendicular to $\vec X$ and nonzero,
against the requirement, so this case is impossible. The two admissible elements give
$L_0=0$ and $L_{e_t}=P_{\mathrm{Vect}}$ by the governing identity.

The classification is short and rigid: two projectors, the zero operator at the origin and the
projection onto the vector subspace at the unit, and nothing between. It is the **smallest
projector class a structure can have while carrying a nonzero projector**, and it is the exact
opposite of the general plain algebra, whose projector class is the whole idempotent family.

## The Splitting Realised by One Element

**Corollary (the splitting is a multiplication).** The canonical splitting of the space into
the vector subspace and the centre is realised by the multiplication of the single element
$e_t$:
$$
\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}},
\qquad
\mathrm{Vect}(\mathbb{B})=\operatorname{im}L_{e_t},
\qquad
\mathbb{C}_{\mathbb{B}}=\ker L_{e_t}.
$$
The vector subspace is the image of the block and a left ideal of the block, and the centre is
the kernel of $L_{e_t}$.

*Proof.* The splitting and the identifications are the governing identity. The image of the
block is $\mathrm{Vect}(\mathbb{B})$, and it is a left ideal because for $\vec A$ pure and
any $\tilde Y$ the value $\vec A\diamond\tilde Y=-Y_t\vec A-\vec A\times\vec Y$ is
pure; the centre is the kernel of $L_{e_t}$ by the same identity.

The corollary is the useful form of the criterion. In the block the two subspaces the theory
names — the derived subalgebra, on which the operation is a Lie bracket, and the centre, on which
it vanishes — are the image and the kernel of the multiplication by one element, and the element
is the unit of the ambient algebra. No other structure of the twelve has this: elsewhere the
splitting, when it exists, is carried by an idempotent, a family, or not at all.

## The Isolation among the Twelve

The criterion of the block is the projector classification of §*The Projector Classification*: the only projectors are the zero operator and the projection onto the vector subspace, the latter at the unit $e_t$, and the splitting of §*The Splitting Realised by One Element* is carried by the multiplication of that one element.

**Theorem (the isolation).** Of the twelve structures of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, the block is the only one in which the left multiplication by the algebra unit is the projection onto the vector subspace, and the only one admitting an element $\tilde E$ with $\tilde E\star\tilde X=\vec X$ for every $\tilde X$; the element is $\tilde E=e_t$, uniquely.

*Proof.* The block's entry is the governing identity. For the other eleven, group them by the action of the unit. In GPA, GQA and SPA the unit acts as the identity, whose image is the whole space and not the vector subspace; in SQA it acts as the projection onto the centre; in APA and AQS it acts as zero. In the six sesquilinear structures the left multiplication by $e_t$ is conjugate-linear or zero, and a conjugate-linear map is not the $\mathbb{C}$-linear projection onto the vector subspace; a conjugate-linear $L$ with $L^{2}=L$ is linear and conjugate-linear at once, hence zero, so in the six the only projector is the zero operator. For the element $\tilde E$, the equation at $\tilde X=e_t$ reads $\tilde E\star e_t=0$; in GPA, SPA and GPS this forces $\tilde E=0$, in GQA, GQS and SQS it forces $\tilde E^{\natural}=0$, and in SQA and SPS it forces $E_te_t=0$, none compatible with the value $\vec X$ at a pure $\tilde X$; in APA and AQS the value at $e_t$ vanishes identically and the pure values are the cross products $\vec E\times\vec X$ and $\vec E\times\overline{\vec X}$, which lie in the orthogonal plane of $\vec E$; and in APS the value at $e_t$, which is $\vec E$, forces $\tilde E=E_te_t$, after which the values at $\vec e_x$ and at $i\vec e_x$ force the contradictory $E_t=-1$ and $E_t=1$. Inside the block the element is unique: at $\tilde X=e_t$ the equation gives $-\vec E=0$, so $\vec E=0$, and at a pure $\tilde X$ it gives $E_t\tilde X=\tilde X$, so $E_t=1$.

| the action of the unit $e_t$ | the structures |
|---|---|
| the identity | GPA, GQA, SPA |
| the projection onto the centre | SQA, SPS |
| a nonzero conjugate-linear map | GPS, GQS, SQS, APS |
| zero | APA, AQS |
| **the projection onto the vector subspace** | **AQA** |

The block is alone in its class, and the reason is the two mixed terms $P_t\vec Q-Q_t\vec P$ that it carries and that the plain antisymmetrisation does not: those terms make the unit act on the scalar direction and so turn its multiplication into a proper projection.

## The Other Criteria Fail Here

Two criteria adjacent to the block's are the criterion of the general plain algebra and the
criterion of the symmetric quaternionic algebra, and neither holds for the block.

**Remark (the alternativity criterion fails).** The criterion of the general plain algebra is
left alternativity, $L_{\tilde X}^{2}=L_{\tilde X\cdot\tilde X}$ for every $\tilde X$, the
square being read in the product at hand; read for the block it becomes
$L_{\tilde X}^{2}=L_{\tilde X\diamond\tilde X}=L_0=0$, so the criterion would demand
$L_{\tilde X}^{2}=0$ for every element; at $\tilde X=e_t$ the operator is the projection onto
the vector subspace, whose square is itself and not zero. The criterion fails at the unit of the
algebra, and the block is one of the eleven structures on which it fails.

**Remark (the rank-one criterion fails).** The criterion of the symmetric quaternionic algebra
is the rank-one identity $L^{\bullet}_{\tilde X}{}^{2}=X_tL^{\bullet}_{\tilde X}$, in which the
scalar coordinate is the coefficient. For the block the corresponding display is false away from
the two elements of the classification: at $\tilde X=\vec e_x$, where $X_t=0$, the right side is the
zero operator while $L_{\vec e_x}^{2}$ is nonzero. The block's criterion is therefore not a scalar
multiple of its own operator; it is the projector identity read at the two elements $0$ and
$e_t$.

## What the Criterion Delivers

The criterion is a classification and not a decomposition theory. What it delivers for the block
is the following short list, and the block carries nothing more.

- **Two projectors.** The zero operator and the projection onto the vector subspace, the latter
    at the element $e_t$.
- **One splitting.** $\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$, the
    image and the kernel of $L_{e_t}$.
- **One left ideal.** The vector subspace, which is the whole image of the block as well as a
    left ideal.
- **No Peirce calculus.** The decompositions indexed by an idempotent do not exist, there being
    no nontrivial idempotent; the ideal theory and the module theory of the plain product have no
    analogue here.

The block is thus the structure in which the projector survives as a single element and not as a
family, and in which the splitting of the space is a statement about one multiplication. This is
the exact sense of its isolation among the twelve: the unit carries the projector, the projector is the projection onto the vector subspace, and there is no other.

## Summary

The antisymmetric quaternionic multiplication is the alternating structure whose left
multiplication by the algebra unit is the projection onto the vector subspace,
$L_{e_t}\tilde X=\vec X$, $L_{e_t}^{2}=L_{e_t}$, with $R_{e_t}=-L_{e_t}$; the projector
classification of the block is the pair $L_{\tilde X}^{2}=L_{\tilde X}\Leftrightarrow\tilde X\in\{0,e_t\}$, so the projector class is the smallest a structure with a nonzero projector can
have. The projection is the canonical splitting $\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus \mathbb{C}_{\mathbb{B}}$ realised by the multiplication of one element, the vector subspace
being the image of the block and a left ideal and the centre its kernel. The block is the only
one of the twelve in which the algebra unit multiplies as the projection onto the vector
subspace, and the only one admitting an element $\tilde E$ with $\tilde E\star\tilde X=\vec X$
for every $\tilde X$, the element being $e_t$ uniquely; the other eleven give the identity, the projection onto the centre, the zero operator or a conjugate-linear map at the unit, and none of them gives this projection. The alternativity criterion of the plain algebra and the rank-one
criterion of the symmetric quaternionic algebra both fail for the block, and the criterion stated
here is its own. What the block delivers is two projectors, one splitting and one left ideal, and
no Peirce calculus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)=P_t\vec Q-Q_t\vec P-\vec P\times\vec Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $L_{\tilde A}\tilde X=\tilde A\diamond\tilde X$, $R_{\tilde A}\tilde X=\tilde X\diamond\tilde A$ | the left and the right multiplication of the block |
| $L_{e_t}=P_{\mathrm{Vect}}$ | the criterion, the unit multiplying as the projection onto the vector subspace |
| $L_{\tilde X}^{2}=L_{\tilde X}$ | the projector equation; its solutions are $0$ and $e_t$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the image of $L_{e_t}$ and of the block, a left ideal |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the centre, the kernel of $L_{e_t}$ |
| GPA … AQS | the twelve structures, coded as in *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* |

## Further Reading

- *The Specificities of the Biquaternion Algebra* (`articles_maths/the-specificities-of-the-biquaternion-algebra.md`), for the criterion of left alternativity, the model of the family
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the first border case, where the projectors are indexed by the plain idempotents
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the second border case, the hyperplane of rank-one projections onto the centre
- *Introduction to the Antisymmetric Quaternionic Algebra* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra.md`), for the operation, its image, the one-sided action of the unit and the absence of a unit
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the operators $L_{\tilde A}$, their matrices, their ranks and the elements for which the rank drops
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the form whose radical is the image of the projection
- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the twelve operations and their two alternating rows
