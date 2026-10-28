# __The Specificities of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic multiplication
$$
\tilde Q_1\diamond\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr)
=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2
$$
is alternating, vector valued and without a unit, and it fails the Jacobi identity
(*Introduction to the Antisymmetric Quaternionic Algebra*, *The Jacobi Failure
and the Associator Defect of the Antisymmetric Quaternionic Algebra*). As an element-theoretic
object the block is poor: every element is a nilpotent, the origin is the only idempotent, there
is no root of $-1$ or of $+1$, and there is no unit and no inverse. As an **operator-theoretic**
object it has one sharp feature, and the feature is the whole of the present article.

The feature is the action of the algebra unit. For the block,
$$
L_{e_t}\tilde Q_1=e_t\diamond\tilde Q_1=\vec Q_1 , \qquad
R_{e_t}\tilde Q_1=\tilde Q_1\diamond e_t=-\vec Q_1 , \qquad
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
$L_{\tilde Q_1}^{2}=L_{\tilde Q_1}\Leftrightarrow\tilde Q_1\in\{0,e_t\}$, and it isolates the block among the
twelve structures. The model is *The Biquaternion Algebra*, which states
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
$\tilde Q_1\diamond\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)$;
the parent product is $\tilde Q_1^{\natural}\tilde Q_2$ and the symmetric half is $\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$. An element
is $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ with $\vec Q_1=Q_{1x}\vec e_x+Q_{1y}\vec e_y+Q_{1z}\vec e_z$; $\mathrm{Vect}(\mathbb{B})$ is the
vector subspace of the pure elements, of complex dimension three, and
$\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ is the centre. The **left multiplication** of the block
is $L_{\tilde Q_4}\tilde Q_1=\tilde Q_4\diamond\tilde Q_1$, and $L_{\tilde Q_4}^{2}=L_{\tilde Q_4}L_{\tilde Q_4}$
is the composite. A **projector** is an idempotent operator, and an **idempotent** is an element
equal to its own square; the two levels are never interchanged, and the block is the example
that makes the distinction visible: its idempotents are the origin alone, while the operator of
the element $e_t$ is a projector.

## The Governing Identity

**Proposition (the unit acts as the projection onto the vector subspace).** For every element
$\tilde Q_1$,
$$
\boxed{\; L_{e_t}\tilde Q_1=\vec Q_1 , \qquad R_{e_t}\tilde Q_1=-\vec Q_1 , \qquad L_{e_t}^{2}=L_{e_t} \;}.
$$
The image of $L_{e_t}$ is $\mathrm{Vect}(\mathbb{B})$, its kernel is $\mathbb{C}_{\mathbb{B}}$,
and $\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}}$.

*Proof.* The explicit form at $\tilde Q_1=e_t$, where $Q_{1t}=1$ and $\vec Q_1=\mathbf 0$, gives
$e_t\diamond\tilde Q_1=\vec Q_1$, and at $\tilde Q=e_t$ it gives
$\tilde Q_1\diamond e_t=-\vec Q_1$. The map $\tilde Q_1\mapsto\vec Q_1$ is the identity on the
vector subspace and vanishes on the centre, so it is a projector, its square is itself, its
image is $\mathrm{Vect}(\mathbb{B})$ and its kernel is $\mathbb{C}_{\mathbb{B}}$; the two are
complementary because every element is the sum of its scalar and vector parts.

**Remark (the element is not a unit).** The element $e_t$ satisfies $e_t\diamond\tilde Q_1=\vec Q_1$,
which is $\tilde Q_1$ only when $\tilde Q_1$ is pure; at a non-pure element the scalar part is
discarded. The block has no unit (*Introduction to the Antisymmetric Quaternionic Algebra of
Biquaternions*), and $e_t$ is a **left identity on the vector subspace** and not a unit: it acts
as the identity there and annihilates the centre, and its right action is the negative of its
left action. The identity $R_{e_t}=-L_{e_t}$ is the alternation of the block read at the unit.

## The Projector Classification

**Theorem (the criterion of the block).** The left multiplication of an element is a projector
exactly at the origin and at the algebra unit,
$$ \boxed{\; L_{\tilde Q_1}^{2}=L_{\tilde Q_1}\iff \tilde Q_1=0\ \text{or}\ \tilde Q_1=e_t \;}. $$
The two projectors are the zero operator and the projection onto the vector subspace.

*Proof.* Write $L_{\tilde Q_1}\tilde Q_2=\tilde{Q}_3$ with
$\tilde{Q}_3=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$; the value is pure, so
$L_{\tilde Q_1}^{2}\tilde Q_2=L_{\tilde Q_1}\tilde{Q}_3=Q_{1t}\tilde{Q}_3-\vec Q_1\times\tilde{Q}_3$, and the
projector condition reads $Q_{1t}\tilde{Q}_3-\vec Q_1\times\tilde{Q}_3=\tilde{Q}_3$ for every $\tilde Q_2$.
At $\tilde Q_2=e_t$, where $Q_{2t}=1$ and $\vec Q_2=\mathbf 0$, one has $\tilde{Q}_3=-\vec Q_1$, and
the condition becomes $(Q_{1t}-1)\vec Q_1=\mathbf 0$; so either $\vec Q_1=\mathbf 0$ or
$Q_{1t}=1$. If $\vec Q_1=\mathbf 0$, then $L_{\tilde Q_1}\tilde Q_2=Q_{1t}\vec Q_2$ and the projector
condition is $Q_{1t}^{2}=Q_{1t}$, giving $Q_{1t}=0$ or $Q_{1t}=1$, that is $\tilde Q_1=0$ or
$\tilde Q_1=e_t$. If $\vec Q_1\neq\mathbf 0$ and $Q_{1t}=1$, the condition reads
$\vec Q_1\times\tilde{Q}_3=0$ for every $\tilde Q_2$, so $\tilde{Q}_3$ is parallel to $\vec Q_1$ at
every $\tilde Q_2$; taking $\tilde Q_2$ pure with $\vec Q_2$ perpendicular to $\vec Q_1$ gives
$\tilde{Q}_3=\vec Q_2-\vec Q_1\times\vec Q_2$, a vector perpendicular to $\vec Q_1$ and nonzero,
against the requirement, so this case is impossible. The two admissible elements give
$L_0=0$ and $L_{e_t}=P_{\mathrm{Vect}}$ by the governing identity.

The classification is short and rigid: two projectors, the zero operator at the origin and the
projection onto the vector subspace at the unit, and nothing between. It is the **smallest
projector class a structure can have while carrying a nonzero projector**, and it is the exact
opposite of the general plain algebra, whose projector class is indexed by the whole idempotent family.

## The Splitting Realised by One Element

**Corollary (the splitting is a multiplication).** The canonical splitting of the space into
the vector subspace and the centre is realised by the multiplication of the single element
$e_t$:
$$
\boxed{\;
\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus\mathbb{C}_{\mathbb{B}},
\qquad
\mathrm{Vect}(\mathbb{B})=\operatorname{im}L_{e_t},
\qquad
\mathbb{C}_{\mathbb{B}}=\ker L_{e_t}
\;}.
$$
The vector subspace is the image of the block and a left ideal of the block, and the centre is
the kernel of $L_{e_t}$.

*Proof.* The splitting and the identifications are the governing identity. The image of the
block is $\mathrm{Vect}(\mathbb{B})$, and it is a left ideal because for $\vec A$ pure and
any $\tilde Q_2$ the value $\vec A\diamond\tilde Q_2=-Q_{2t}\vec A-\vec A\times\vec Q_2$ is
pure; the centre is the kernel of $L_{e_t}$ by the same identity.

The corollary is the useful form of the criterion. In the block the two subspaces the theory
names — the derived subalgebra, on which the operation is a Lie bracket, and the centre, on which
it vanishes — are the image and the kernel of the multiplication by one element, and the element
is the unit of the ambient algebra. No other structure of the twelve has this: elsewhere the
splitting, when it exists, is carried by an idempotent, a family, or not at all.

## The Isolation among the Twelve

The criterion of the block is the projector classification of §*The Projector Classification*: the only projectors are the zero operator and the projection onto the vector subspace, the latter at the unit $e_t$, and the splitting of §*The Splitting Realised by One Element* is carried by the multiplication of that one element.

**Theorem (the isolation).** Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the block is the only one in which the left multiplication by the algebra unit is the projection onto the vector subspace, and the only one admitting an element $\tilde E$ with $\tilde E\star\tilde Q_1=\vec Q_1$ for every $\tilde Q_1$; the element is $\tilde E=e_t$, uniquely.

*Proof.* The block's entry is the governing identity. For the other eleven, group them by the action of the unit. In GPA, GQA and SPA the unit acts as the identity, whose image is the whole space and not the vector subspace; in SQA it acts as the projection onto the centre; in APA and AQS it acts as zero. In the six sesquilinear structures the left multiplication by $e_t$ is conjugate-linear or zero, and a conjugate-linear map is not the $\mathbb{C}$-linear projection onto the vector subspace; a conjugate-linear $L$ with $L^{2}=L$ is linear and conjugate-linear at once, hence zero, so in the six the only projector is the zero operator. For the element $\tilde E$, the equation at $\tilde Q_1=e_t$ reads $\tilde E\star e_t=0$; in GPA, SPA and GPS this forces $\tilde E=0$, in GQA, GQS and SQS it forces $\tilde E^{\natural}=0$, and in SQA and SPS it forces $E_te_t=0$, none compatible with the value $\vec Q_1$ at a pure $\tilde Q_1$; in APA and AQS the value at $e_t$ vanishes identically and the pure values are the cross products $\vec E\times\vec Q_1$ and $\vec E\times\overline{\vec Q_1}$, which lie in the orthogonal plane of $\vec E$; and in APS the value at $e_t$, which is $\vec E$, forces $\tilde E=E_te_t$, after which the values at $\vec e_x$ and at $i\vec e_x$ force the contradictory $E_t=-1$ and $E_t=1$. Inside the block the element is unique: at $\tilde Q_1=e_t$ the equation gives $-\vec E=0$, so $\vec E=0$, and at a pure $\tilde Q_1$ it gives $E_t\tilde Q_1=\tilde Q_1$, so $E_t=1$.

| the action of the unit $e_t$ | the structures |
|---|---|
| the identity | GPA, GQA, SPA |
| the projection onto the centre | SQA, SPS |
| a nonzero conjugate-linear map | GPS, GQS, SQS, APS |
| zero | APA, AQS |
| **the projection onto the vector subspace** | **AQA** |

The block is alone in its class, and the reason is the two mixed terms $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ that it carries and that the plain antisymmetrisation does not: those terms make the unit act on the scalar direction and so turn its multiplication into a proper projection.

## The Other Criteria Fail Here

Two criteria adjacent to the block's are the criterion of the general plain algebra and the
criterion of the symmetric quaternionic algebra, and neither holds for the block.

**Remark (the alternativity criterion fails).** The criterion of the general plain algebra is
left alternativity, $L_{\tilde Q_1}^{2}=L_{\tilde Q_1\cdot\tilde Q_1}$ for every $\tilde Q_1$, the
square being read in the product at hand; read for the block it becomes
$L_{\tilde Q_1}^{2}=L_{\tilde Q_1\diamond\tilde Q_1}=L_0=0$, so the criterion would demand
$L_{\tilde Q_1}^{2}=0$ for every element; at $\tilde Q_1=e_t$ the operator is the projection onto
the vector subspace, whose square is itself and not zero. The criterion fails at the unit of the
algebra, and the block is one of the eleven structures on which it fails.

**Remark (the rank-one criterion fails).** The criterion of the symmetric quaternionic algebra
is the rank-one identity $L^{\bullet}_{\tilde Q_1}{}^{2}=Q_{1t}L^{\bullet}_{\tilde Q_1}$, in which the
scalar coordinate is the coefficient. For the block the corresponding display is false away from
the two elements of the classification: at $\tilde Q_1=\vec e_x$, where $Q_{1t}=0$, the right side is the
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
$L_{e_t}\tilde Q_1=\vec Q_1$, $L_{e_t}^{2}=L_{e_t}$, with $R_{e_t}=-L_{e_t}$; the projector
classification of the block is the pair $L_{\tilde Q_1}^{2}=L_{\tilde Q_1}\Leftrightarrow\tilde Q_1\in\{0,e_t\}$, so the projector class is the smallest a structure with a nonzero projector can
have. The projection is the canonical splitting $\mathbb{B}=\mathrm{Vect}(\mathbb{B})\oplus \mathbb{C}_{\mathbb{B}}$ realised by the multiplication of one element, the vector subspace
being the image of the block and a left ideal and the centre its kernel. The block is the only
one of the twelve in which the algebra unit multiplies as the projection onto the vector
subspace, and the only one admitting an element $\tilde E$ with $\tilde E\star\tilde Q_1=\vec Q_1$
for every $\tilde Q_1$, the element being $e_t$ uniquely; the other eleven give the identity, the projection onto the centre, the zero operator or a conjugate-linear map at the unit, and none of them gives this projection. The alternativity criterion of the plain algebra and the rank-one
criterion of the symmetric quaternionic algebra both fail for the block, and the criterion stated
here is its own. What the block delivers is two projectors, one splitting and one left ideal, and
no Peirce calculus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\diamond\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $L_{\tilde Q_4}\tilde Q_1=\tilde Q_4\diamond\tilde Q_1$, $R_{\tilde Q_4}\tilde Q_1=\tilde Q_1\diamond\tilde Q_4$ | the left and the right multiplication of the block |
| $L_{e_t}=P_{\mathrm{Vect}}$ | the criterion, the unit multiplying as the projection onto the vector subspace |
| $L_{\tilde Q_1}^{2}=L_{\tilde Q_1}$ | the projector equation; its solutions are $0$ and $e_t$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the image of $L_{e_t}$ and of the block, a left ideal |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the centre, the kernel of $L_{e_t}$ |
| GPA … AQS | the twelve structures, coded as in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* |

## Further Reading

- [The Biquaternion Algebra](the-biquaternion-algebra-and-its-vector-spaces.html), for the criterion of left alternativity, the model of the family
- [The Specificities of the General Quaternionic Algebra](the-specificities-of-the-general-quaternionic-algebra.html), for the first border case, where the projectors are indexed by the plain idempotents
- [The Specificities of the Symmetric Quaternionic Algebra](the-specificities-of-the-symmetric-quaternionic-algebra.html), for the second border case, the hyperplane of rank-one projections onto the centre
- [Introduction to the Antisymmetric Quaternionic Algebra](introduction-to-the-antisymmetric-quaternionic-algebra.html), for the operation, its image, the one-sided action of the unit and the absence of a unit
- [The Adjoint Operators of the Antisymmetric Quaternionic Algebra](the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.html), for the operators $L_{\tilde Q_4}$, their matrices, their ranks and the elements for which the rank drops
- [The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra](the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.html), for the form whose radical is the image of the projection
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve operations and their two alternating rows
