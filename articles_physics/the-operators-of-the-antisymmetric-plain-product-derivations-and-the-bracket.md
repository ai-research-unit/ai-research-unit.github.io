# __The Operators of the Antisymmetric Plain Product: Derivations and the Bracket__

## Introduction

This article is the operator article of the antisymmetric plain algebra, the algebra of *The Cross Product as a
Lie Bracket: Rotations and the Jacobi Identity*. Its product is the bracket

$$
\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf P\times\mathbf Q,
$$

the antisymmetrisation of the ordinary product, of scalar part zero and values in the vector subspace
$\mathrm{Vect}(\mathbb{B})$, and the operators of the block are the maps that attach an element to an argument:

$$
L^{\wedge}_{\tilde Q}(\tilde R)=\tilde Q\wedge\tilde R,\qquad
R^{\wedge}_{\tilde P}(\tilde R)=\tilde R\wedge\tilde P .
$$

The left and the right multiplication of the bracket are the two one-sided operators, and the **multiplication
operators of a bracket are its inner derivations**. The interpretation of the bracket as the algebra of rotations, its
alternation, the Jacobi identity and the cross-product identity belong to *The Cross Product as a Lie Bracket:
Rotations and the Jacobi Identity*; the material-sector Lie algebra and the invariant form read on it belong to
*Angular Momentum and the Lie Algebra of the Material Sector*; the derivations and the adjoint of the block are the
mathematics of *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, and the general theory
of derivations and of the adjoint action is *The Commutator Operator*, *Derivations of a Ring*, *Derivations of a Lie
Algebra* and *The Adjoint Action of a Lie Algebra*. This article states the one thing those composition laws do not:
**which form the operators are adjoint for, and what that adjoint does**.

The answer is one sentence. The bilinear form of the block is its own invariant form, the **Killing form**
$\kappa$ of the bracket, and the adjoint **negates the operator**:

$$
\kappa\bigl(L^{\wedge}_{\tilde A}\tilde X,\tilde Y\bigr)+\kappa\bigl(\tilde X,L^{\wedge}_{\tilde A}\tilde Y\bigr)=0,
\qquad
\bigl(L^{\wedge}_{\tilde A}\bigr)^{\kappa}=-L^{\wedge}_{\tilde A}=L^{\wedge}_{-\tilde A}.
$$

The adjoint **keeps the side and negates the parameter**, and it conjugates nothing. Because the product is
alternating, the right multiplication is the negative of the left,
$R^{\wedge}_{\tilde A}=-L^{\wedge}_{\tilde A}$, so the two-sided family collapses onto signed products of the
one-sided one and the swapping of the side and the change of sign are the same statement. Every type criterion is a
consequence: **every** operator of the one-sided family is skew-adjoint, with the self-adjoint ones exactly the
central parameters, on which the operator vanishes; the diagonal two-sided operator is self-adjoint for every
parameter; and a product of two one-sided operators is self-adjoint exactly when their parameters bracket to zero.
The inner derivations are the multiplication operators, of complex dimension three and isomorphic to
$\mathfrak{sl}(2,\mathbb{C})$, and the whole derivation algebra is $\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$,
with one outer derivation, the dilation of the centre. Read under the job word **rotation**, the operators are the
infinitesimal rotations, they are skew-adjoint precisely because a generator is, and the observable angular momentum
is $i$ times a generator.

The **normalisation** is fixed before anything else, because two conventions of the corpus differ by a factor two and
both are in use. This article writes the block's own operator as the **halved adjoint**

$$
\operatorname{ad}^{\wedge}_{\tilde A}(\tilde X)=\tilde A\wedge\tilde X,\qquad
\operatorname{ad}^{\wedge}_{\tilde A}=\tfrac12\operatorname{ad}_{\tilde A},
$$

and calls $\operatorname{ad}_{\tilde A}=[\tilde A,\ \cdot\ ]=2\operatorname{ad}^{\wedge}_{\tilde A}$ the
**commutator adjoint**. The block's bracket is the halved one and the Killing form is taken with the halved adjoint,
$\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\operatorname{ad}^{\wedge}_{\tilde P}\operatorname{ad}^{\wedge}_{\tilde Q})$;
the multiplication operators of this article are the halved adjoints $L^{\wedge}_{\tilde A}=\operatorname{ad}^{\wedge}_{\tilde A}$.
Every statement below is written in that convention and the factor is displayed whenever a reader could mistake it.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$,
$e_1e_2=e_3$, $e_k^{2}=-e_0$ and central imaginary $i$; a general element is
$\tilde Q=Q_0e_0+\mathbf Q$ with vector part $\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$. The centre is
$\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the derived subspace is $\mathrm{Vect}(\mathbb{B})=\{ \mathrm{Sc}=0 \}$, the
sectors are $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$, and the conjugations are the complex
$\bar{\cdot}$, the natural ${\natural}$ and the Hermitian ${}^{*}=\bar{\cdot}\circ{\natural}$ of *Conventions in the
Biquaternion Universe*. The bracket is written $\tilde P\wedge\tilde Q$ and its result is also written
$\mathbf P\times\mathbf Q$; the commutator is $[\tilde P,\tilde Q]=\tilde P\tilde Q-\tilde Q\tilde P=2\,\tilde P\wedge\tilde Q$.

## The Multiplication Operators and Their Composition

### The One-Sided Operators Are the Inner Derivations

**Definition.** For $\tilde A\in\mathbb{B}$ the **left multiplication** of the bracket is the $\mathbb{C}$-linear
operator $L^{\wedge}_{\tilde A}(\tilde X)=\tilde A\wedge\tilde X$, and the **right multiplication** is
$R^{\wedge}_{\tilde A}(\tilde X)=\tilde X\wedge\tilde A$.

**Theorem (the operators and their normalisation).** For every $\tilde A$,

$$
R^{\wedge}_{\tilde A}=-L^{\wedge}_{\tilde A},\qquad
L^{\wedge}_{\tilde A}=\operatorname{ad}^{\wedge}_{\tilde A}=\tfrac12\operatorname{ad}_{\tilde A},
\qquad
\operatorname{ad}_{\tilde A}=2L^{\wedge}_{\tilde A},
$$

so the left multiplications of the bracket are exactly its **inner derivations**, and the halved adjoint coincides
with the cross-product operator $\mathbf A\times$ on the vector subspace and vanishes on the centre.

*Proof.* Alternation gives $\tilde X\wedge\tilde A=-\tilde A\wedge\tilde X$, hence $R^{\wedge}=-L^{\wedge}$; the
definition $\operatorname{ad}^{\wedge}_{\tilde A}(\tilde X)=\tilde A\wedge\tilde X$ gives the second identity, and
$[\tilde A,\tilde X]=2\,\tilde A\wedge\tilde X$ the third. The cross-product identity and the vanishing on the centre
are *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*; the alternation is *Introduction
to the Antisymmetric Plain Algebra of Biquaternions*.

**Read as a physical statement.** The bracket cannot tell an attachment on the left from one on the right except by a
sign, and its multiplication operators are not built from the product by a composite as in the ordinary row but are
the **adjoint action** of the algebra on itself. The band is the algebra of its own adjoint representation, which is
why it is the rotation band and not the composition band.

### The Composition of the Operators Is the Bracket

**Theorem (the bracket law of the multiplication operators).** For all $\tilde A,\tilde B$,

$$
\bigl[L^{\wedge}_{\tilde A},L^{\wedge}_{\tilde B}\bigr]
=L^{\wedge}_{\tilde A\wedge\tilde B}
=\tfrac12\,L^{\wedge}_{[\tilde A,\tilde B]},
\qquad
\bigl[\operatorname{ad}_{\tilde A},\operatorname{ad}_{\tilde B}\bigr]
=\operatorname{ad}_{[\tilde A,\tilde B]},
$$

the bracket of the operators being the commutator in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.

*Proof.* The adjoint map is a homomorphism,
$\operatorname{ad}_{\tilde A\wedge\tilde B}=[\operatorname{ad}_{\tilde A},\operatorname{ad}_{\tilde B}]$, by the
Jacobi identity (*The Adjoint Action of a Lie Algebra*, *The Adjoint Operators and the Derivations of the
Antisymmetric Plain Algebra*); halving both sides with $\operatorname{ad}^{\wedge}=L^{\wedge}$ gives the first
display, and the second is the unhalved property. The factor is $1$ for the halved operators and $\tfrac12$ when the
right side carries the commutator parameter, because $\tilde A\wedge\tilde B=\tfrac12[\tilde A,\tilde B]$.

**Read as a physical statement.** This is the analogue of the multiplicative law $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$
of the ordinary row: **the composition law of the operators is the commutator, and its closure reproduces the bracket
of the parameters**, so the acting maps close with the same structure constants as the bracket, which is the operator
form of the Jacobi identity. The composition is not multiplicative — the composite $L^{\wedge}_{\tilde A}L^{\wedge}_{\tilde B}$
is a second-order operator, in general no $L^{\wedge}_{\tilde C}$ — so the calculus is a **Lie algebra of operators**
and not an associative one. A frequent error writes $[L^{\wedge}_{\tilde A},L^{\wedge}_{\tilde B}]=L^{\wedge}_{[\tilde A,\tilde B]}$,
which is twice the truth because $[\tilde A,\tilde B]=2\,\tilde A\wedge\tilde B$; the factors displayed are correct.

**Corollary (the image and the kernel).** The map $\tilde A\mapsto L^{\wedge}_{\tilde A}$ is a homomorphism of Lie
algebras from the bracket onto the inner derivations with kernel the centre $\mathbb{C}e_0$, so
$\mathrm{Inn}(\mathfrak{g})=\{L^{\wedge}_{\tilde A}\}\cong\mathbb{B}/\mathbb{C}e_0\cong\mathfrak{sl}(2,\mathbb{C})$,
of complex dimension three: the adjoint representation is faithful on the derived algebra and invisible on the centre.

*Proof.* The kernel is the set of $\tilde A$ with $\mathbf A\times=0$, that is $\tilde A$ central; the quotient is the
vector subspace, whose cross-product algebra is $\mathfrak{so}(3,\mathbb{C})\cong\mathfrak{sl}(2,\mathbb{C})$ by *The
Lie Algebra of the Antisymmetric Plain Algebra*.

**Read as a physical statement.** The centre is the direction no rotation sees, and the acting maps are exactly the
rotations of the derived subspace. The interpretation is that the generator space is the traceless part and the central
direction is a phase the bracket cannot rotate, the operator form of the centre as the radical of the invariant form.

## The Adjoint of the Invariant Form Negates the Parameter

### The Invariant Form of the Band

**Definition.** The **invariant form** of the bracket is the Killing form
$\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\operatorname{ad}^{\wedge}_{\tilde P}\operatorname{ad}^{\wedge}_{\tilde Q})$,
computed with the halved adjoints; on general elements $\kappa(\tilde P,\tilde Q)=-2\,\mathbf P\!\cdot\!\mathbf Q$,
with Gram matrix $\operatorname{diag}(0,-2,-2,-2)$ in the basis $(e_0,e_1,e_2,e_3)$. It kills the scalar part, is
symmetric, is degenerate with radical the centre, and its restriction to the vector subspace is non-degenerate of real
signature $(3,3)$.

*Proof.* This is *The Killing Form of the Antisymmetric Plain Algebra*: the value $-2\,\mathbf P\!\cdot\!\mathbf Q$,
the Gram matrix, the radical and the signature are its first section, and the invariance
$\kappa(\operatorname{ad}_{\tilde P}\tilde X,\tilde Q)+\kappa(\tilde X,\operatorname{ad}_{\tilde P}\tilde Q)=0$ is
its invariance theorem.

**Read as a physical statement.** The band carries its own bilinear form, not imported from the ordinary product: the
invariant pairing of a Lie algebra is the trace of two adjoint actions, here the complex Euclidean form on the vector
subspace, negative on the real directions and positive on the imaginary ones. The sign as the compact-non-compact
split is *Angular Momentum and the Lie Algebra of the Material Sector*; this article uses the form only as the pairing
the operators are adjoint for.

### The Adjoint of the Multiplication Operators

**Theorem (the multiplication operators are skew-adjoint).** For all $\tilde A,\tilde X,\tilde Y$,

$$
\kappa\bigl(L^{\wedge}_{\tilde A}\tilde X,\tilde Y\bigr)
+\kappa\bigl(\tilde X,L^{\wedge}_{\tilde A}\tilde Y\bigr)=0,
$$

equivalently $\bigl(L^{\wedge}_{\tilde A}\bigr)^{\kappa}=-L^{\wedge}_{\tilde A}$ and, in the commutator adjoint,
$\bigl(\operatorname{ad}_{\tilde A}\bigr)^{\kappa}=-\operatorname{ad}_{\tilde A}$.

*Proof.* The invariance of $\kappa$,
$\kappa(\operatorname{ad}_{\tilde P}\tilde X,\tilde Q)+\kappa(\tilde X,\operatorname{ad}_{\tilde P}\tilde Q)=0$,
is *The Killing Form of the Antisymmetric Plain Algebra*; substituting
$\operatorname{ad}_{\tilde A}=2\operatorname{ad}^{\wedge}_{\tilde A}$ gives the display.

**Read as a physical statement.** The adjoint of a bracket multiplication is the **negative of the operator
itself**: it neither keeps nor conjugates the parameter nor swaps the two sides, it negates, which is the same as
negating the parameter, $\bigl(L^{\wedge}_{\tilde A}\bigr)^{\kappa}=L^{\wedge}_{-\tilde A}$. The interpretation is that a
bracket multiplication is a **generator**, the infinitesimal form of an orthogonal transformation and not the
operator of an observable; the observable is the Hermitian multiple, a dictionary read in the next section.

**Theorem (the ordinary form agrees in sign on the family).** For the plain form of the ordinary row,
$B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-\mathbf P\!\cdot\!\mathbf Q$,

$$
B\bigl(L^{\wedge}_{\tilde A}\tilde X,\tilde Y\bigr)+B\bigl(\tilde X,L^{\wedge}_{\tilde A}\tilde Y\bigr)=0,
\qquad
\bigl(L^{\wedge}_{\tilde A}\bigr)^{\approx}=-L^{\wedge}_{\tilde A}.
$$

*Proof.* The scalar part is cyclic, $\mathrm{Sc}(\tilde A\tilde X\tilde Y)=\mathrm{Sc}(\tilde X\tilde Y\tilde A)$,
so $B(\tilde A\tilde X,\tilde Y)-B(\tilde X,\tilde Y\tilde A)=0$; antisymmetrising in the first slot and using
non-degeneracy gives the display.

**Read as a physical statement.** The band's own invariant form and the ordinary scalar-part form agree in **sign**
on the family: for both, the adjoint is the negative. The interpretation is that the skew-adjointness of a bracket
multiplication is no artefact of the choice of form but a property of the operator, visible to every non-degenerate
bilinear form that is cyclic on one side, and it is the algebraic statement that the bracket is antisymmetric.

## The Types of the Operators

### The One-Sided Types

**Theorem (the self-adjoint and skew-adjoint criteria of the family).** For $\tilde A\in\mathbb{B}$,

$$
L^{\wedge}_{\tilde A}\ \text{is skew-adjoint for }\kappa\ \text{for every }\tilde A,
\qquad
L^{\wedge}_{\tilde A}\ \text{is self-adjoint for }\kappa\iff \tilde A\ \text{central}\iff L^{\wedge}_{\tilde A}=0 .
$$

The same two statements hold for the right multiplication, and they hold for the ordinary form $B$ in place of
$\kappa$.

*Proof.* Skew-adjointness is the adjoint theorem of the previous section. Self-adjointness is
$L^{\wedge}_{\tilde A}=-L^{\wedge}_{\tilde A}$, which is $L^{\wedge}_{\tilde A}=0$, which by the corollary on the
kernel is exactly $\tilde A$ central; by the previous theorem the ordinary form gives the same verdict.

**Read as a physical statement.** The family of bracket multiplications contains **no observable**: it is
entirely the family of generators. The interpretation is that the band supplies the infinitesimal structure of the
internal symmetry and not its observables, and the observables are obtained by the multiplication by $i$ — the
angular-momentum operators are $i$ times the generators, which is the interpretation of *Angular Momentum and the Lie
Algebra of the Material Sector* and the reason the imaginary vector units are the boost generators. The criterion is
a criterion on the parameter's being central, that is on the parameter being invisible; apart from the centre no
parameter is self-adjoint, and the central parameters give the zero operator.

**Corollary (the Hermitian multiples).** For every $\tilde A$, the operator $iL^{\wedge}_{\tilde A}$ is self-adjoint
for $\kappa$, and the map $\tilde A\mapsto iL^{\wedge}_{\tilde A}$ is $\mathbb{R}$-linear; the Hermitian operators
$\{iL^{\wedge}_{\tilde A}\}$ are the observables carried by this band.

*Proof.* Multiplying a skew-adjoint operator by the central imaginary $i$ makes it self-adjoint because
$\overline{i}=-i$; the $\mathbb{R}$-linearity is the $\mathbb{C}$-linearity of $\tilde A\mapsto L^{\wedge}_{\tilde A}$
together with the reality of the scalar $i$ in the adjoint relation.

**Read as a physical statement.** The interpretation is the **observable-generator dictionary** in its operator form: a
skew-adjoint operator generates a one-parameter group of form-preserving transformations, and its Hermitian
multiple is the quantity measured. The angular momentum $J_k=iL^{\wedge}_{ie_k}$ is the Hermitian multiple of the
generator $L^{\wedge}_{ie_k}$, and the corpus states the same relation at the level of elements; no new physical claim
is made here.

### The Two-Sided Types

**Theorem (the types of a product of two multiplications).** For $\tilde A,\tilde B$,

$$
L^{\wedge}_{\tilde A}L^{\wedge}_{\tilde B}\ \text{is self-adjoint for }\kappa
\iff \tilde A\wedge\tilde B=0
\iff \bigl[L^{\wedge}_{\tilde A},L^{\wedge}_{\tilde B}\bigr]=0 .
$$

*Proof.* Using $\bigl(L^{\wedge}_{\tilde A}\bigr)^{\kappa}=-L^{\wedge}_{\tilde A}$ and the reversal of the adjoint
under composition, $\bigl(FG\bigr)^{\kappa}=G^{\kappa}F^{\kappa}$, one gets
$\bigl(L^{\wedge}_{\tilde A}L^{\wedge}_{\tilde B}\bigr)^{\kappa}=L^{\wedge}_{\tilde B}L^{\wedge}_{\tilde A}$;
self-adjointness is therefore $L^{\wedge}_{\tilde A}L^{\wedge}_{\tilde B}=L^{\wedge}_{\tilde B}L^{\wedge}_{\tilde A}$,
that is the vanishing of the commutator, which by the bracket law is $L^{\wedge}_{\tilde A\wedge\tilde B}=0$, which by
the kernel of the adjoint is $\tilde A\wedge\tilde B=0$.

**Read as a physical statement.** Two successive rotations compose into an operator that is symmetric exactly when
the two rotations commute, that is when their parameters bracket to zero, that is when their vector parts are
proportional. The interpretation is that the order-dependence of two rotations is the **same** quantity as the
non-symmetry of their composite: the commutator is simultaneously the failure of the operators to commute and the
failure of the composite to be self-adjoint. No such identification is available in the ordinary row, whose
two-sided types are criteria on the product of the parameters and not on their commutator.

## The Symmetries of the Form and of the Product

### The Symmetries of the Invariant Form

**Definition.** An operator $T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ **preserves** the invariant form when
$\kappa(T\tilde P,T\tilde Q)=\kappa(\tilde P,\tilde Q)$ for all $\tilde P,\tilde Q$.

**Theorem (the form-preserving operators).** The operators preserving $\kappa$ are exactly the products
$C_\lambda A$ of a **central scaling** $C_\lambda$ ($e_0\mapsto\lambda e_0$, $\mathrm{Vect}(\mathbb{B})$ fixed,
$\lambda\in\mathbb{C}^{\times}$) and a **complex-orthogonal map** $A\in O(3,\mathbb{C})$ of the vector subspace. In
particular every conjugation by a unit, $T_{\tilde U}(\tilde P)=\tilde U\tilde P\tilde U^{-1}$, preserves $\kappa$ and
the bracket.

*Proof.* The radical of $\kappa$ is the centre, so a form-preserving operator preserves the centre and acts on it by
an invertible scalar $C_\lambda$; on the vector subspace, where $\kappa=-2\,\mathbf P\!\cdot\!\mathbf Q$ is
non-degenerate, it acts by a complex-orthogonal map, and non-degeneracy forbids a component carrying the centre into
the vector subspace. A conjugation is an algebra automorphism, so it preserves the bracket and the form built from
it; the automorphism group is $\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$ by
*The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, with
$PGL(2,\mathbb{C})\cong SO(3,\mathbb{C})$ the orientation-preserving orthogonal group of *Biquaternion Automorphisms
and Derivations*.

**Read as a physical statement.** The symmetries of the band's form are the rotations and the reflections of the
complex vector subspace together with the scalings of the central direction. The interpretation is that the invariant form
is preserved by the rotation group and by the reflections, and that the reflections are the form-preserving
operators the product cannot use, a reflection reversing the orientation and so the sign of a cross product.

### The Symmetries of the Product

**Definition.** An operator $T$ **preserves the bracket**, or is **multiplicative**, when
$T(\tilde P\wedge\tilde Q)=T\tilde P\wedge T\tilde Q$ for all $\tilde P,\tilde Q$; these form the group
$\operatorname{Aut}(\mathfrak{g})$.

**Theorem (the multiplicative operators).** The multiplicative operators are exactly the products $C_\lambda A$ with
$\lambda\in\mathbb{C}^{\times}$ and $A\in SO(3,\mathbb{C})$ **orientation-preserving**, and
$\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$, generated by the conjugation by
a unit and the central scaling; the inner derivations are **not** multiplicative.

*Proof.* The automorphism group and its two generators are *The Adjoint Operators and the Derivations of the
Antisymmetric Plain Algebra*; the central scaling fixes the derived algebra, on which the bracket lives, and scales
the centre, on which the bracket is zero, so it is an automorphism for every $\lambda$. An inner derivation satisfies
the Leibniz rule and not the multiplicativity, so it is no automorphism.

**Read as a physical statement.** The operators preserving the product are the **finite** rotations, and those
preserving the form but not the product are the reflections. The interpretation is the separation of the group from its Lie
algebra: the finite rotations are the multiplicative operators and the infinitesimal rotations the derivations, the
two related by the exponential, a forward reference to *Biquaternion Lie Group and Exponential Structure*. The central
scaling is the automorphism the rotation algebra carries on its invisible direction, and its generator is the one
outer derivation of the next theorem.

**Corollary (the derivation algebra).** The derivations of the bracket are the inner ones together with the one outer
line spanned by the **dilation of the centre** $D_0$ ($e_0\mapsto e_0$, $\mathrm{Vect}(\mathbb{B})\mapsto0$):

$$
\operatorname{Der}(\mathfrak{g})=\mathrm{Inn}(\mathfrak{g})\oplus\mathbb{C}D_0\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C},
\qquad
\dim_{\mathbb{C}}\operatorname{Der}(\mathfrak{g})=4,
$$

and $D_0$ is not inner because every inner derivation vanishes on the centre while $D_0(e_0)=e_0$.

*Proof.* This is *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*; the general theory
is *Derivations of a Lie Algebra*.

**Remark (the two derivation algebras).** The derivations of the associative algebra $\mathbb{B}$ itself are **all
inner**, $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$, of complex dimension three,
because $\mathbb{B}$ is central simple (*Biquaternion Automorphisms and Derivations*); the derivation algebra of the
**bracket** is this one enlarged by the single outer line $\mathbb{C}D_0$, which is a derivation of the bracket and
**not** of the associative product.

**Read as a physical statement.** The internal infinitesimal transformations of the band are the rotations of the
derived subspace together with the scaling of the central direction, and the scaling is the one that does not come
from an element. The interpretation is that the central phase is an outer generator, whose finite form is the central
scaling automorphism: the one internal transformation the adjoint representation cannot see.

## The Operators Acting on the State Space

Let $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde\Upsilon_2\}$ be the spinor space of *The Spinor Space
as a Module and as a Hilbert Space*, $\tilde\Pi_1=\tfrac12(e_0+ie_3)$, a complex two-dimensional left module of the
algebra and the carrier of the state space; on it the algebra acts by the matrix representation
$\mathsf{M}_2(e_k)=-i\sigma_k$, and on the algebra itself the derivation $L^{\wedge}_{\tilde A}$ is the matrix commutator
$\tfrac12[\mathsf{M}_2(\tilde A),\ \cdot\ ]$ whose kernel is the central line and whose action on the traceless part is the
three-dimensional **adjoint representation** of $\mathfrak{sl}(2,\mathbb{C})$.

**Theorem (the generators on the state space).** The halved real units $T_a=\tfrac12 e_a$, $a=1,2,3$, read on $S$
as the matrices $T_a=\tfrac12\mathsf{M}_2(e_a)=-\tfrac{i}{2}\sigma_a$, satisfy $[T_i,T_j]=\epsilon_{ijk}T_k$; the
Hermitian angular-momentum operators $J_k=iT_k=\tfrac12\sigma_k$ satisfy $[J_i,J_j]=i\,\epsilon_{ijk}J_k$ and have
Casimir $\sum_k J_k^2=\tfrac34\mathrm{id}$ on $S$. The one-parameter group generated by the derivation
$L^{\wedge}_{\tilde A}$ is the inner automorphism $\exp(tL^{\wedge}_{\tilde A})=\mathrm{Ad}_{\exp(t\tilde A)}$ of the
unit $\exp(t\tilde A)$, and it acts on $S$ by left multiplication.

*Proof.* The commutator of the halved real units is the action of the derived algebra through
$\tfrac12\mathsf{M}_2(e_k)=-\tfrac{i}{2}\sigma_k$, which is the two-dimensional defining representation of
$\mathfrak{sl}(2,\mathbb{C})$ of *The Killing Form of the Antisymmetric Plain Algebra* and *Angular Momentum and
Spin in Biquaternionic Form*; the matrix identity
$\mathsf{M}_2(\tilde A\wedge\tilde X)=\tfrac12[\mathsf{M}_2(\tilde A),\mathsf{M}_2(\tilde X)]$ is *The Antisymmetric Plain Algebra in the
$2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the identification
$\exp(tL^{\wedge}_{\tilde A})=\mathrm{Ad}_{\exp(t\tilde A)}$ is the standard correspondence between a derivation
and the one-parameter group of automorphisms it generates (algebraic statement in *Derivations of a Ring*, the
exponential a forward reference), and the left action of the algebra on its simple module is *The Spinor Space as a
Module and as a Hilbert Space*.

**Read as a physical statement.** On the state space the state carries the **fundamental, spin-$\tfrac12$**
representation of the rotation algebra, while on the operator space the traceless part carries the adjoint,
spin-one representation; both are the same band read on two carriers. The interpretation is that the generators of the band
are at once the angular momenta of the spinor and the infinitesimal rotations of the operators, and that the state
carries the two-valued form of the rotation while the operator space carries its vector form. The ladder operators,
the eigenvalues and the Clebsch–Gordan structure are the business of *Angular Momentum and Spin in Biquaternionic
Form* and are not derived here.

## The Two-Sided Operators, the Sandwich and the Inner Automorphism

### The Two-Sided Family

**Definition.** A **two-sided operator** of the band is a composite $L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde B}$ of
one left and one right multiplication; the **sandwich** is its diagonal case
$\Theta^{\wedge}_{\tilde A}=L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde A}$.

**Theorem (the collapse of the two-sided family).** For all $\tilde A,\tilde B$,
$L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde B}=-L^{\wedge}_{\tilde A}L^{\wedge}_{\tilde B}$ and
$\Theta^{\wedge}_{\tilde A}=-\bigl(L^{\wedge}_{\tilde A}\bigr)^{2}$.

*Proof.* The right multiplication is the negative of the left, $R^{\wedge}_{\tilde B}=-L^{\wedge}_{\tilde B}$, by the
alternation theorem; substituting gives both displays.

**Read as a physical statement.** Unlike the ordinary row, the bracket has no genuinely two-sided operator: every
two-sided operator is a signed square of a one-sided one, and the sandwich carries a single parameter and no
conjugate, because the two slots of an alternating product already differ by a sign. The band knows only the
**one-parameter rotations** and not the two-parameter congruences of the ordinary row, and the conjugate the ordinary
sandwich attaches to the right slot is absent because the bracket is invariant under both conjugations and changes
sign under the exchange of the slots.

### The Adjoint of the Sandwich

**Theorem (the adjoint of a two-sided operator).** For all $\tilde A,\tilde B$,

$$
\bigl(L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde B}\bigr)^{\kappa}=L^{\wedge}_{\tilde B}R^{\wedge}_{\tilde A}
$$

for the invariant form, and the same for the ordinary form $B$ with $\approx$ in place of $\kappa$.

*Proof.* The adjoint of a composite reverses the order and negates each factor,
$(FG)^{\kappa}=G^{\kappa}F^{\kappa}$, with $(L^{\wedge}_{\tilde A})^{\kappa}=-L^{\wedge}_{\tilde A}$ and
$(R^{\wedge}_{\tilde B})^{\kappa}=-(L^{\wedge}_{\tilde B})^{\kappa}=L^{\wedge}_{\tilde B}$. Hence
$(L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde B})^{\kappa}=L^{\wedge}_{\tilde B}(-L^{\wedge}_{\tilde A})=L^{\wedge}_{\tilde B}R^{\wedge}_{\tilde A}$:
the two parameters exchange places with no conjugate and no residual sign.

**Read as a physical statement.** The adjoint of a two-sided bracket operator swaps the two slots, as in the ordinary
row, and here the swap is the whole adjoint because there is no conjugation to carry. The interpretation is that the
transport across the invariant form exchanges the two attachments of the bracket, the exchange being the alternation
of the product read on the operators.

**Corollary (the sandwich is self-adjoint for every parameter).** For every $\tilde A$,
$\bigl(\Theta^{\wedge}_{\tilde A}\bigr)^{\kappa}=\Theta^{\wedge}_{\tilde A}$: the sandwich is self-adjoint for
**every** parameter, without a sector condition.

*Proof.* Apply the two-sided theorem with $\tilde B=\tilde A$; the swapped operator is
$L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde A}=\Theta^{\wedge}_{\tilde A}$.

**Read as a physical statement.** This is the sharpest contrast with the ordinary row, where the sandwich is
self-adjoint exactly on the sector parameters. On the bracket band the sandwich is symmetric for every parameter,
because the square of a skew-adjoint operator is self-adjoint and the sandwich is minus that square; the sector
condition has collapsed, the two slots of an alternating product being already exchanged by a sign. The interpretation is
the operator form of the statement that the antisymmetric square is symmetric, a naming of the algebraic fact and not
a new physics claim.

### The Sandwich Against the Inner Automorphism

**Proposition (the inner automorphism is the exponential of the operator, the sandwich its square).** For every
element $\tilde A$ and every unit $\tilde U$, $\mathrm{Ad}_{\tilde U}(\tilde P)=\tilde U\tilde P\tilde U^{-1}$ and

$$
\mathrm{Ad}_{\exp(\tilde A)}=\exp\bigl(\operatorname{ad}_{\tilde A}\bigr)=\exp\bigl(2L^{\wedge}_{\tilde A}\bigr),
\qquad
\Theta^{\wedge}_{\tilde A}=-\bigl(L^{\wedge}_{\tilde A}\bigr)^{2}
=-\tfrac14\bigl(\operatorname{ad}_{\tilde A}\bigr)^{2}.
$$

Both the sandwich and the exponential inner automorphism act through $\operatorname{ad}^{\wedge}_{\tilde A}$ alone, so
both are invisible on the centre and depend only on $\tilde A$ modulo $\mathbb{C}e_0$; $\mathrm{Ad}_{\exp(\tilde A)}$
is multiplicative and preserves $\kappa$, while $\Theta^{\wedge}_{\tilde A}$ is neither multiplicative nor
form-preserving and is self-adjoint for $\kappa$ for every parameter.

*Proof.* The identification $\exp(\operatorname{ad}_{\tilde A})(\tilde P)=e^{\tilde A}\tilde P e^{-\tilde A}$ is the
correspondence between a derivation and its one-parameter group (*Derivations of a Ring*); substituting
$\operatorname{ad}_{\tilde A}=2L^{\wedge}_{\tilde A}$ and the collapse theorem gives the displays. The vanishing on
the centre, the multiplicativity and form-preservation of $\mathrm{Ad}_{\tilde U}$, and the self-adjointness of the
sandwich are the corollary on the image and the kernel, the theorem on the multiplicative operators and the corollary
on the sandwich; $\Theta^{\wedge}_{\tilde A}$ fails multiplicativity because it is the square of an inner derivation,
which satisfies the Leibniz rule and not the multiplicativity.

**Read as a physical statement.** The two-sided operator of the bracket and the inner automorphism are the **same
band at two orders**: the sandwich is the square of the generator and the inner automorphism its exponential. The
interpretation is that the alternating product cannot tell a conjugation from its derivative — it has one two-sided
operator, built from one generator, and the finite rotation is what that generator exponentiates to. This is the
sharp difference from the ordinary row, whose sandwich and inner automorphism are two genuinely different
conjugations, by the conjugate and by the inverse of the parameter, agreeing only on the unitary slice; on the
bracket band the right multiplication carries no independent parameter, the distinction has no slot to live in, and
the two operators differ only as the square and the exponential of one and the same adjoint.

## A Worked Case

Take the generator $\tilde A=e_1$, of invariant norm $\kappa(e_1,e_1)=-2$ and scalar-part value $B(e_1,e_1)=-1$. Its
multiplication operator is computed on the basis:

$$
L^{\wedge}_{e_1}(e_0)=0,\quad
L^{\wedge}_{e_1}(e_1)=0,\quad
L^{\wedge}_{e_1}(e_2)=e_1\wedge e_2=e_3,\quad
L^{\wedge}_{e_1}(e_3)=e_1\wedge e_3=-e_2,
$$

so in the basis $(e_0,e_1,e_2,e_3)$ its matrix is block diagonal, with a zero $2\times2$ block on $(e_0,e_1)$ and the
skew block $\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ on $(e_2,e_3)$. The operator is skew-adjoint for $\kappa$, and the
adjoint theorem is visible on one pair: $\kappa(L^{\wedge}_{e_1}e_2,e_3)=\kappa(e_3,e_3)=-2$ equals
$-\kappa(e_2,L^{\wedge}_{e_1}e_3)=-\kappa(e_2,-e_2)=-2$, while the self-adjointness defect
$\kappa(L^{\wedge}_{e_1}e_2,e_3)-\kappa(e_2,L^{\wedge}_{e_1}e_3)=-4$ is nonzero, so the operator is not self-adjoint.
For the ordinary form the same pair gives $B(L^{\wedge}_{e_1}e_2,e_3)=B(e_3,e_3)=-1=-B(e_2,-e_2)$, the same verdict.

The bracket law is checked on the pair $(e_1,e_2)$, whose bracket is $e_3$:
$[L^{\wedge}_{e_1},L^{\wedge}_{e_2}]=L^{\wedge}_{e_1\wedge e_2}=L^{\wedge}_{e_3}$. Column by column the composite
sends $e_1\mapsto e_2$ and $e_2\mapsto-e_1$, exactly the columns of $L^{\wedge}_{e_3}$; the factor is one for the
halved operators, and the same pair written with the commutator parameters carries the factor $\tfrac12$ because
$[e_1,e_2]=2e_3$.

A **finite rotation** is the conjugation by the unit $\tilde U=e_1$, $\mathrm{Ad}_{e_1}(\tilde P)=-e_1\tilde P e_1$,
which fixes $e_1$ and reverses the signs of $e_2$ and $e_3$, a rotation by $\pi$ about the $e_1$ axis; it preserves
the bracket and the invariant form, as an automorphism must. The **reflection** $T_{\mathrm{r}}$ fixing $e_1,e_2$ and
sending $e_3\mapsto-e_3$ preserves the invariant form but **anti-preserves** the bracket,
$T_{\mathrm{r}}(\tilde P\wedge\tilde Q)=-(T_{\mathrm{r}}\tilde P\wedge T_{\mathrm{r}}\tilde Q)$: the form-preserving
operators that are not multiplicative are exactly the orientation-reversing ones. The **outer derivation** $D_0$
($e_0\mapsto e_0$, vector part to zero) is a derivation of the bracket and is not inner, since $D_0(e_0)=e_0$ while
every $L^{\wedge}_{\tilde A}$ kills $e_0$. The **sandwich** $\Theta^{\wedge}_{e_1}=-(L^{\wedge}_{e_1})^{2}$ acts as
the identity on the plane $(e_2,e_3)$ and as zero on $(e_0,e_1)$, and is self-adjoint for $\kappa$ and for $B$. A
**null** parameter, $\tilde A=e_1+ie_2$, has $\kappa(\tilde A,\tilde A)=-2(1+i^2)=0$, so the parameter is isotropic
for the band's form; the alternation gives $\tilde A\wedge\tilde A=0$ for *every* parameter, so every parameter lies
in the kernel of its own multiplication operator, and the worked case displays the isotropic direction the sibling
article reads as the complex null cone.

**A numerical check.** For random complex elements the identities $R^{\wedge}_{\tilde A}=-L^{\wedge}_{\tilde A}$,
$\operatorname{ad}_{\tilde A}=2L^{\wedge}_{\tilde A}$,
$[L^{\wedge}_{\tilde A},L^{\wedge}_{\tilde B}]=L^{\wedge}_{\tilde A\wedge\tilde B}=\tfrac12L^{\wedge}_{[\tilde A,\tilde B]}$
and $[\operatorname{ad}_{\tilde A},\operatorname{ad}_{\tilde B}]=\operatorname{ad}_{[\tilde A,\tilde B]}$ were
checked to machine precision (deviation below $10^{-14}$) on $80$ random triples, together with the Leibniz rule for
$L^{\wedge}_{\tilde A}$ on the bracket. The skew-adjointness of $L^{\wedge}_{\tilde A}$ for $\kappa$ and for $B$, the
negating adjoint $(L^{\wedge}_{\tilde A})^{\kappa}=L^{\wedge}_{-\tilde A}$, the Gram matrix
$\operatorname{diag}(0,-2,-2,-2)$, the value $\kappa=-2\,\mathbf P\!\cdot\!\mathbf Q$, the self-adjointness of the
diagonal sandwich, the self-adjointness criterion of a composite, the preservation of $\kappa$ and of the bracket by
the conjugations by units, the form-preservation and the anti-preservation of the bracket by the reflection, the
derivation property of $D_0$ and the matrix identity
$\mathsf{M}_2(\tilde A\wedge\tilde X)=\tfrac12[\mathsf{M}_2(\tilde A),\mathsf{M}_2(\tilde X)]$ were all checked on random parameters, all to
machine precision. The identification of the inner automorphism with the exponential of the operator,
$\mathrm{Ad}_{\exp(\tilde A)}=\exp(\operatorname{ad}_{\tilde A})=\exp(2L^{\wedge}_{\tilde A})$, and the collapse
$\Theta^{\wedge}_{\tilde A}=-\tfrac14(\operatorname{ad}_{\tilde A})^{2}$ were checked on random parameters to
$2\times10^{-14}$ and exactly. The non-preservation of $\kappa$ by the sandwich was checked by exhibiting a nonzero
difference $\kappa(\Theta^{\wedge}_{\tilde A}\tilde X,\Theta^{\wedge}_{\tilde A}\tilde Y)-\kappa(\tilde X,\tilde Y)$
for random $\tilde A,\tilde X,\tilde Y$: the difference vanishes for no parameter tested, because the square of a
generator drops the direction of the parameter and cannot be orthogonal. On $S$ the generators
$T_a=\tfrac12\mathsf{M}_2(e_a)$ satisfy $[T_i,T_j]=\epsilon_{ijk}T_k$ and
$\sum_aT_a^2=-\tfrac34\mathrm{id}$, whence $J_a=iT_a$ satisfies $[J_i,J_j]=i\epsilon_{ijk}J_k$ and
$\sum_aJ_a^2=\tfrac34\mathrm{id}$, exactly.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must
declare.

- **The bracket is not re-read here.** Its alternation, the cross-product identity, the Jacobi identity and the
  rotation interpretation are *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*; the material-sector
  Lie algebra and the invariant form read on the sectors are *Angular Momentum and the Lie Algebra of the Material
  Sector*.
- **The invariant form is not re-proved here.** The Killing form, its value, its Gram matrix, its radical, its
  signature and its invariance are *The Killing Form of the Antisymmetric Plain Algebra*; the general statement is
  *The Killing Form Operator*.
- **The derivations are not re-derived here.** The inner derivations, the outer line and the automorphism group are
  *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, and the general theory is
  *Derivations of a Ring*, *Derivations of a Lie Algebra* and *The Adjoint Action of a Lie Algebra*.
- **The commutator operator is not the subject here.** The operator $[\tilde A,\ \cdot\ ]$ and the identity
  $\operatorname{ad}_a=L_a-R_a$ are *The Commutator Operator*; this article uses only the halved form and records
  the factor of the halving.
- **The physical angular momentum is not this article's.** The ladder operators, the eigenvalues, the Casimir and
  the Clebsch–Gordan structure are *Angular Momentum and Spin in Biquaternionic Form*; the module and the Hilbert
  structure of the state space are *The Spinor Space as a Module and as a Hilbert Space*; the observable-generator
  dictionary is *Observables, Gauge Generators and the Chirality of the Internal Action*.
- **The twelve rows are not compared here.** The comparison, block against block, is the crossing reader *The
  Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve; this
  article declares only the antisymmetric-plain column.
- **The exponential is not read here.** The correspondence between a derivation and its one-parameter group is named
  only at the level of the algebraic statement that a derivation is the linear part of an automorphism
  (*Derivations of a Ring*); the exponential map is a forward reference.

**What the framework does not claim.** The interpretation does not derive the rotation group or the Lorentz group from the
operator calculus; the correspondence between the derivations and the finite rotations is cited, not constructed
here. It does not identify $\kappa$ with a physical metric; the interval and the metric are the quaternionic-level
data of *Biquaternion Norm and Invertibility*. It does not claim that the inner and outer derivations together form
the algebra of a physical gauge group; the obstruction to enlarging the gauge group is *Grand Unification and the Biquaternion Algebra Ceiling*. And it does
not claim that the operator calculus of the twelve rows is one calculus: each row has its own form and its own
adjoint, and the antisymmetric-plain row is the one whose multiplication operators are its inner derivations.

## The Ledger

**Proved.** The multiplication operators of the bracket are the left and right multiplications with
$R^{\wedge}_{\tilde A}=-L^{\wedge}_{\tilde A}$, and they are the inner derivations
$L^{\wedge}_{\tilde A}=\operatorname{ad}^{\wedge}_{\tilde A}=\tfrac12\operatorname{ad}_{\tilde A}$, equal to the
cross-product operator on the vector subspace and vanishing on the centre; the naive composition law fails, while the
bracket law $[L^{\wedge}_{\tilde A},L^{\wedge}_{\tilde B}]=L^{\wedge}_{\tilde A\wedge\tilde B}=\tfrac12L^{\wedge}_{[\tilde A,\tilde B]}$
holds exactly, and $[\operatorname{ad}_{\tilde A},\operatorname{ad}_{\tilde B}]=\operatorname{ad}_{[\tilde A,\tilde B]}$;
the map $\tilde A\mapsto L^{\wedge}_{\tilde A}$ has kernel the centre and image $\mathfrak{sl}(2,\mathbb{C})$; the
invariant form $\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\operatorname{ad}^{\wedge}_{\tilde P}\operatorname{ad}^{\wedge}_{\tilde Q})=-2\,\mathbf P\!\cdot\!\mathbf Q$
of Gram matrix $\operatorname{diag}(0,-2,-2,-2)$ makes every multiplication operator **skew-adjoint**, the adjoint
negating the parameter, and the ordinary form $B$ agrees in sign on the family; the one-sided self-adjoint operators
are exactly the central parameters, on which the operator vanishes, the Hermitian multiples $iL^{\wedge}_{\tilde A}$
are the observables, and a composite $L^{\wedge}_{\tilde A}L^{\wedge}_{\tilde B}$ is self-adjoint exactly when
$\tilde A\wedge\tilde B=0$; the form-preserving operators are the central scalings times the complex-orthogonal
maps, the multiplicative ones the central scalings times the orientation-preserving ones, with
$\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$, and the derivation algebra is
$\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ with the outer line the dilation of the centre; the two-sided operators
collapse onto signed squares, the adjoint of $L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde B}$ is
$L^{\wedge}_{\tilde B}R^{\wedge}_{\tilde A}$, and the sandwich $\Theta^{\wedge}_{\tilde A}$ is self-adjoint for every
parameter and equal to $-\tfrac14(\operatorname{ad}_{\tilde A})^{2}$, while the inner automorphism is its exponential
$\mathrm{Ad}_{\exp(\tilde A)}=\exp(\operatorname{ad}_{\tilde A})$; on the operator space the derivation is the
commutator $\tfrac12[\mathsf{M}_2(\tilde A),\ \cdot\ ]$ with the adjoint representation on the traceless part, and on the
spinor space the generators $T_a=\tfrac12e_a$ give the fundamental representation with Casimir sums
$\sum_aT_a^2=-\tfrac34\mathrm{id}$ and $\sum_aJ_a^2=\tfrac34\mathrm{id}$ for $J_a=iT_a$.

**Interpretations.** That the multiplication operators of the bracket are its inner derivations, so the band is the
**adjoint representation** of its own algebra; that the composition law of the operators is the **commutator**,
closing on the bracket of the parameters; that the adjoint **negates the parameter**, keeping the side and
conjugating nothing, so a bracket multiplication is a generator and not an observable; that the band contains no
self-adjoint one-sided operator, so the observables are the Hermitian multiples; that the finite rotations are the
multiplicative operators and the infinitesimal ones the derivations; that the central direction is invisible to
every rotation and its scaling is the one outer derivation; that the sandwich is self-adjoint for every parameter,
the sector condition of the ordinary row having collapsed; and that the state space carries the spin-$\tfrac12$
representation while the operator space carries the spin-one one. Each is the framework's naming of a proved
algebraic fact and is labelled as such.

## Physical Readings

The operators of the antisymmetric plain product read as the infinitesimal rotations of the material sector and as
the adjoint action of the rotation algebra on itself. Three interpretations organise the rest. The **composition law being
the commutator** is read as the closure of the rotation algebra: the acting maps close on the bracket of their
parameters, which is the operator form of the Jacobi identity and the reason a Lie algebra, and not an associative
algebra, is the structure of the band. The **adjoint negating the parameter** is read as the generator-observable
dictionary: a skew-adjoint operator generates a form-preserving flow, and its Hermitian multiple is what is
measured, so the angular momentum is $i$ times a generator and the band supplies the generators and not the
observables. The **sandwich being self-adjoint for every parameter** is read as the symmetry of the antisymmetric
square, the sector condition of the ordinary row having collapsed because the two slots of an alternating product
already differ by a sign, and as the **square of the finite rotation**: the sandwich and the inner automorphism are
the same generator read at order two and at all orders. Read on the algebra, the finite rotations are the
multiplicative operators and the reflections are the form-preserving operators that the product cannot use; read on
the centre, the one derivation that does not come from an element is the scaling of the central direction, which is
the operator form of the central phase as the generator the adjoint representation cannot see. Each interpretation is a
name for a proved algebraic fact and not a new physical claim.

## Summary

The operators of the antisymmetric plain algebra are the left and the right multiplications of the bracket,
$L^{\wedge}_{\tilde A}(\tilde X)=\tilde A\wedge\tilde X$ and $R^{\wedge}_{\tilde B}(\tilde X)=\tilde X\wedge\tilde B$,
and they are the **inner derivations** of the algebra:
$L^{\wedge}_{\tilde A}=\operatorname{ad}^{\wedge}_{\tilde A}=\tfrac12\operatorname{ad}_{\tilde A}$, the halved
adjoint, equal to the cross-product operator on the vector subspace and vanishing on the centre. The right
multiplication is the negative of the left, $R^{\wedge}_{\tilde A}=-L^{\wedge}_{\tilde A}$, so the two-sided family
collapses onto signed squares and there is no genuinely two-sided operator. The composition of the operators is
**not** multiplicative; the correct law is the bracket law
$[L^{\wedge}_{\tilde A},L^{\wedge}_{\tilde B}]=L^{\wedge}_{\tilde A\wedge\tilde B}=\tfrac12L^{\wedge}_{[\tilde A,\tilde B]}$,
equivalently $[\operatorname{ad}_{\tilde A},\operatorname{ad}_{\tilde B}]=\operatorname{ad}_{[\tilde A,\tilde B]}$,
with the factor of the halving displayed; this closes the acting maps on the bracket of their parameters, with kernel
the centre and image $\mathfrak{sl}(2,\mathbb{C})$.

The bilinear form of the band is its own invariant form, the Killing form
$\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\operatorname{ad}^{\wedge}_{\tilde P}\operatorname{ad}^{\wedge}_{\tilde Q})=-2\,\mathbf P\!\cdot\!\mathbf Q$
of Gram matrix $\operatorname{diag}(0,-2,-2,-2)$, and the adjoint **negates the parameter**,
$(L^{\wedge}_{\tilde A})^{\kappa}=L^{\wedge}_{-\tilde A}$; it keeps the side, neither conjugating nor swapping, and
the ordinary form $B$ agrees in sign on the family. Every type criterion follows: every multiplication operator is
skew-adjoint, the self-adjoint ones are exactly the central parameters, on which the operator vanishes, the
Hermitian multiples $iL^{\wedge}_{\tilde A}$ are the observables, a composite of two is self-adjoint exactly when
$\tilde A\wedge\tilde B=0$, and the sandwich is self-adjoint for every parameter and equals
$-\tfrac14(\operatorname{ad}_{\tilde A})^{2}$, while the inner automorphism is its exponential. The form-preserving
operators are the central scalings times the complex-orthogonal maps, the multiplicative ones the central scalings
times the orientation-preserving ones with $\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$,
and the derivation algebra is $\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ with the outer line the dilation of the
centre.

On the operator space the generators act by the commutator and carry the adjoint representation; on the spinor space
they carry the fundamental representation, with $T_a=\tfrac12e_a$ read on $S$ satisfying
$[T_i,T_j]=\epsilon_{ijk}T_k$ and $\sum_aT_a^2=-\tfrac34\mathrm{id}$. Read under the job word **rotation**, the
operators are the infinitesimal rotations, skew-adjoint because a generator is, and the observable angular momentum
is their Hermitian multiple. What is proved is the algebra; what is named is the interpretation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^{2}=-e_0$, $e_1e_2=e_3$ |
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf P\times\mathbf Q$ | The bracket, the band's product |
| $L^{\wedge}_{\tilde A}(\tilde X)=\tilde A\wedge\tilde X$ | Left multiplication; the halved adjoint |
| $R^{\wedge}_{\tilde A}(\tilde X)=\tilde X\wedge\tilde A$ | Right multiplication; $R^{\wedge}_{\tilde A}=-L^{\wedge}_{\tilde A}$ |
| $\operatorname{ad}^{\wedge}_{\tilde A}=\tfrac12\operatorname{ad}_{\tilde A}$ | The halving that separates the block's adjoint from the commutator adjoint |
| $\operatorname{ad}_{\tilde A}=[\tilde A,\ \cdot\ ]=2L^{\wedge}_{\tilde A}$ | The commutator adjoint |
| $\kappa(\tilde P,\tilde Q)=-2\,\mathbf P\!\cdot\!\mathbf Q$ | The invariant (Killing) form; $\operatorname{diag}(0,-2,-2,-2)$ |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-\mathbf P\!\cdot\!\mathbf Q$ | The ordinary plain form; agrees in sign on the family |
| $\bigl[L^{\wedge}_{\tilde A},L^{\wedge}_{\tilde B}\bigr]=L^{\wedge}_{\tilde A\wedge\tilde B}=\tfrac12L^{\wedge}_{[\tilde A,\tilde B]}$ | The bracket law of the operators |
| $\bigl(L^{\wedge}_{\tilde A}\bigr)^{\kappa}=-L^{\wedge}_{\tilde A}=L^{\wedge}_{-\tilde A}$ | The adjoint negates the parameter |
| $L^{\wedge}_{\tilde A}$ skew-adjoint for all $\tilde A$; self-adjoint $\iff\tilde A$ central | The one-sided type criterion |
| $iL^{\wedge}_{\tilde A}$ self-adjoint | The observables are the Hermitian multiples |
| $L^{\wedge}_{\tilde A}L^{\wedge}_{\tilde B}$ self-adjoint $\iff\tilde A\wedge\tilde B=0$ | The two-sided type criterion |
| $\bigl(L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde B}\bigr)^{\kappa}=L^{\wedge}_{\tilde B}R^{\wedge}_{\tilde A}$ | The adjoint of a two-sided operator swaps the slots |
| $\Theta^{\wedge}_{\tilde A}=L^{\wedge}_{\tilde A}R^{\wedge}_{\tilde A}=-(L^{\wedge}_{\tilde A})^{2}=-\tfrac14(\operatorname{ad}_{\tilde A})^{2}$ | The sandwich; self-adjoint for every parameter |
| $\mathrm{Ad}_{\tilde U}(\tilde P)=\tilde U\tilde P\tilde U^{-1}$; $\mathrm{Ad}_{\exp(\tilde A)}=\exp(\operatorname{ad}_{\tilde A})$ | The inner automorphism, the exponential of the operator |
| $C_\lambda$; $O(3,\mathbb{C})$, $SO(3,\mathbb{C})$ | Central scaling; complex-orthogonal and orientation-preserving maps |
| $\operatorname{Aut}(\mathfrak{g})\cong\mathbb{C}^{\times}\times PGL(2,\mathbb{C})$ | The multiplicative operators, $(2,3)$-dimensional split |
| $D_0$; $\operatorname{Der}(\mathfrak{g})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}$ | The outer derivation (dilation of the centre) and the derivation algebra |
| $\mathsf{M}_2(e_k)=-i\sigma_k$ | The matrix representation; $\mathsf{M}_2(\tilde A\wedge\tilde X)=\tfrac12[\mathsf{M}_2(\tilde A),\mathsf{M}_2(\tilde X)]$ |
| $S=\mathbb{B}\tilde\Pi_1$, $T_a=\tfrac12e_a$, $J_a=iT_a=\tfrac12\sigma_a$ | The spinor space and the generators on it |

## Further Reading

- Mathematics article *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*
  (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra.md`), for the adjoint
  map, the halving $\operatorname{ad}=2\operatorname{ad}^{\wedge}$, the cross-product identity, the inner
  derivations and $\mathfrak{sl}(2,\mathbb{C})$, the outer derivation, the automorphism group and the structure group.
- Mathematics article *The Commutator Operator* (`articles_maths/the-commutator-operator.md`), for the operator
  $[\tilde A,\ \cdot\ ]$ as the antisymmetrisation $L-R$ of the two multiplications and the homomorphism property.
- Mathematics article *Derivations of a Ring* (`articles_maths/derivations-of-a-ring.md`), for the Leibniz rule, the
  inner derivations and the derivation as the linear part of an automorphism.
- Mathematics article *Derivations of a Lie Algebra* (`articles_maths/derivations-of-a-lie-algebra.md`), for the
  derivation algebra, the inner and outer parts, and the theorem that a semisimple algebra has no outer derivation.
- Mathematics article *The Adjoint Action of a Lie Algebra* (`articles_maths/the-adjoint-action-of-a-lie-algebra.md`),
  for the adjoint map as a homomorphism with kernel the centre, the inner derivations as its image, and
  $\operatorname{ad}_{[x,y]}=[\operatorname{ad}_x,\operatorname{ad}_y]$.
- Mathematics article *The Killing Form of the Antisymmetric Plain Algebra*
  (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for $\kappa=-2\,\mathbf P\!\cdot\!\mathbf Q$,
  its Gram matrix, its radical and signature, its invariance and the Casimir.
- Mathematics article *The Lie Algebra of the Antisymmetric Plain Algebra*
  (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the derived algebra, the
  ideals and the isomorphism $\mathfrak{so}(3,\mathbb{C})\cong\mathfrak{sl}(2,\mathbb{C})$.
- Mathematics article *Biquaternion Automorphisms and Derivations*
  (`articles_maths/biquaternion-automorphisms-and-derivations.md`), for the algebra automorphism group
  $PGL(2,\mathbb{C})\cong SO(3,\mathbb{C})$ and the difference between automorphisms and isometries.
- Physics article *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*
  (`articles_physics/the-cross-product-as-a-lie-bracket-rotations-and-the-jacobi-identity.md`), the framing article
  of this group, for the bracket, its alternation and the Jacobi identity.
- Physics article *Angular Momentum and the Lie Algebra of the Material Sector*
  (`articles_physics/angular-momentum-and-the-lie-algebra-of-the-material-sector.md`), for the Killing form and its
  signature, the compact-non-compact split and the angular-momentum interpretation of the band.
- Physics article *Angular Momentum and Spin in Biquaternionic Form*
  (`articles_physics/angular-momentum-and-spin-in-biquaternionic-form.md`), for the angular-momentum algebra, the
  ladder operators, the Casimir and the spin representations.
- Physics article *The Spinor Space as a Module and as a Hilbert Space*
  (`articles_physics/the-spinor-space-as-a-module-and-as-a-hilbert-space.md`), for the ideal $S$, its basis and the
  module picture of the state space.
- Physics article *Observables, Gauge Generators and the Chirality of the Internal Action*
  (`articles_physics/observables-gauge-generators-and-the-chirality-of-the-internal-action.md`), for the
  observable-generator dictionary at the level of the framework.
- Physics article *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*
  (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing
  reader of the twelve operator rows, for the comparison of the adjoints and the division of the twelve rows.
