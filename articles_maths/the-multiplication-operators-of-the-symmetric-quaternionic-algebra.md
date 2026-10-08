# __The Multiplication Operators of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication is commutative, so its left multiplications and its right
multiplications coincide; the operator of the block is the single family

$$
L^{\star}_{\tilde A}: \mathbb{B}\longrightarrow\mathbb{C}e_0,\qquad
L^{\star}_{\tilde A}\tilde R = \tilde A\star\tilde R = B(\tilde A,\tilde R)e_0 ,
$$

of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*. This article reads the
family as the operator layer of the block: the matrices, the ranks and the traces of the operators, their
composition and the algebra they generate, their adjoints with respect to the form $B$, the derivations the
block produces, and the two groups of linear maps attached to it — the group that preserves the form and the
group that preserves the product. It follows the pattern of the operator articles of the parent row,
*The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *One-Sided Operators on
the General Quaternionic Algebra of Biquaternions*, and it cites rather than restates the general theory of
the left multiplications of an algebra.

The operation and its formula are *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*; the
form $B$ and its role as the coefficient are *The Quaternion Form as a Product on the Symmetric Quaternionic
Algebra*; the derivation layer of a general algebra is *Automorphisms and Derivations of Algebras*; the matrix models are
*The Symmetric Quaternionic Algebra in the Matrix Representations*. Nothing of the enriched layer of Part II is used.

**Conventions.** The basis is $e_0,e_1,e_2,e_3$; the product is $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$
with $B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$; an operator is written as a $4\times4$ matrix in the
basis when its entries are needed, and the matrix of a linear map $T$ is written $[T]$; the transpose of a
matrix is written with a superscript $\mathsf T$.

## The Operators, Their Matrices and Their Ranks

**Proposition (the matrix of a multiplication).** In the basis $e_0,e_1,e_2,e_3$ the matrix of
$L^{\star}_{\tilde A}$ has its first row equal to the coordinates of $\tilde A$ and every other entry zero:

$$
\bigl[L^{\star}_{\tilde A}\bigr]_{0\mu} = A_\mu, \qquad
\bigl[L^{\star}_{\tilde A}\bigr]_{\nu\mu}=0 \ (\nu\ne0),
$$

that is, the four columns are the four multiples $A_0e_0,A_1e_0,A_2e_0,A_3e_0$.

*Proof.* $L^{\star}_{\tilde A}e_\mu=B(\tilde A,e_\mu)e_0=A_\mu e_0$, so the $\mu$-th column is $A_\mu e_0$,
with coordinates $A_\mu$ at the first place and zero elsewhere. $\square$

**Corollary (rank and image).** For $\tilde A\ne0$ the rank of $L^{\star}_{\tilde A}$ is $1$ and its image is
the whole central line $\mathbb{C}e_0$; for $\tilde A=0$ it is the zero operator. The **kernel** is the
hyperplane

$$
\ker L^{\star}_{\tilde A} = \{\tilde R\in\mathbb{B}: B(\tilde A,\tilde R)=0\},
$$

of complex dimension $3$ for $\tilde A\ne0$; it is the hyperplane of the elements paired to zero with
$\tilde A$ by $B$, and it contains
$\tilde A$ exactly when $\tilde A$ is isotropic.

*Proof.* The columns span $\mathbb{C}e_0$ if some $A_\mu\ne0$, and the image is central; the kernel is the
kernel of the linear form $B(\tilde A,\cdot)$, whose rank is $1$ because the form is non-degenerate. The last
statement is $B(\tilde A,\tilde A)=N(\tilde A)=0$. $\square$

**Proposition (trace and determinant).** For every $\tilde A$,

$$
\operatorname{Tr}\bigl(L^{\star}_{\tilde A}\bigr) = A_0, \qquad
\det\bigl(L^{\star}_{\tilde A}\bigr) = 0 .
$$

*Proof.* The trace is the sum of the diagonal entries of the matrix above, and only the entry $(0,0)=A_0$ is
nonzero. The determinant vanishes because the rank is at most $1$ on a space of dimension $4$; for $\tilde A=0$
the operator is zero. $\square$

**Remark (a rank-one layer).** The operator layer of the block is a rank-one layer: every nonzero
multiplication has rank one, so the family is as far from the identity operator as a nonzero family can be, and
no element of the algebra is a unit. The trace detects the scalar part of the multiplier and nothing else: the
vector part of the multiplier is invisible to the trace, and the operator family separates the elements by the
kernel and not by the trace.

## Composition and the Algebra of Operators

**Proposition (the composition law).** The multiplication operators compose by

$$
L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B} = A_0\,L^{\star}_{\tilde B},
$$

and the family $\{L^{\star}_{\tilde A}:\tilde A\in\mathbb{B}\}$ is a complex vector space of dimension $4$, the
**monoid of multiplications** of the block.

*Proof.* $L^{\star}_{\tilde A}(L^{\star}_{\tilde B}\tilde R)=L^{\star}_{\tilde A}\bigl(B(\tilde B,\tilde R)e_0\bigr)=B(\tilde B,\tilde R)B(\tilde A,e_0)e_0=A_0B(\tilde B,\tilde R)e_0=A_0L^{\star}_{\tilde B}\tilde R$. $\square$

**Corollary (the map is faithful but not multiplicative).** The map $\tilde A\mapsto L^{\star}_{\tilde A}$ is
injective, its kernel being the radical $\{0\}$ of the operation, so the operator family represents the algebra
faithfully as a vector space. It is **not** a representation of the operation: the composition law compares
$L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}=A_0L^{\star}_{\tilde B}$ with
$L^{\star}_{\tilde A\star\tilde B}=B(\tilde A,\tilde B)L^{\star}_{e_0}$, and the two differ, as at
$\tilde A=e_1$, $\tilde B=e_1$, where the first is $0$ and the second is $L^{\star}_{e_0}\ne0$. The monoid of
multiplications is not commutative either, $L^{\star}_{e_0}\circ L^{\star}_{e_1}=L^{\star}_{e_1}$ while
$L^{\star}_{e_1}\circ L^{\star}_{e_0}=0$, although the operation is commutative.

**Remark (the operator algebra in the basis).** The four operators $L^{\star}_{e_\mu}$ are the matrices with a
single nonzero row: $L^{\star}_{e_\mu}$ has the entry $1$ at position $(0,\mu)$ and zeros elsewhere. Their
products are $L^{\star}_{e_0}\circ L^{\star}_{e_\nu}=L^{\star}_{e_\nu}$ and
$L^{\star}_{e_k}\circ L^{\star}_{e_\nu}=0$ for $k\ne0$, so the algebra generated by the family is the four
dimensional algebra of the matrices whose only possibly nonzero row is the first, and its multiplication is the
product of such row matrices. This is the shadow of the collapse: the operator family carries the four
coordinates of the multiplier in a single row, and no product of two multiplications can recover the vector
part of a multiplier.

## The Adjoint with Respect to the Form

**Definition.** The **adjoint** of a complex-linear map $T$ with respect to $B$ is the linear map $T^{\dagger}$
determined by

$$
B\bigl(T\tilde X,\tilde Y\bigr) = B\bigl(\tilde X,T^{\dagger}\tilde Y\bigr) \qquad
\text{for all } \tilde X,\tilde Y\in\mathbb{B},
$$

which exists and is unique because $B$ is non-degenerate.

**Proposition (the adjoint of a multiplication).** For every $\tilde A$,

$$
\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}\tilde Y = \sum_\mu A_\mu Y_0\,e_\mu ,
\qquad\text{and}\qquad
L^{\star}_{\tilde A}\ \text{is self-adjoint}\quad\Longleftrightarrow\quad \tilde A\in\mathbb{C}e_0 .
$$

*Proof.* $B(L^{\star}_{\tilde A}\tilde X,\tilde Y)=B\bigl(B(\tilde A,\tilde X)e_0,\tilde Y\bigr)=B(\tilde A,\tilde X)Y_0=\sum_\mu A_\mu X_\mu Y_0$, and $B(\tilde X,\sum_\mu A_\mu Y_0e_\mu)=\sum_\mu X_\mu A_\mu Y_0$; the two agree for all $\tilde X$, which gives the displayed adjoint. For
self-adjointness, compare the adjoint with $L^{\star}_{\tilde A}\tilde Y=B(\tilde A,\tilde Y)e_0$: the identity
$\sum_\mu A_\mu Y_0e_\mu=\bigl(\sum_\mu A_\mu Y_\mu\bigr)e_0$ for all $\tilde Y$ forces $A_k=0$ for
$k=1,2,3$. $\square$

**Remark (the adjoint is the operator of a linear form).** The adjoint
$\tilde Y\mapsto\sum_\mu A_\mu Y_0e_\mu$ scales the whole element $\tilde A$ by the scalar part of the
argument, so its value lies in the line $\mathbb{C}\tilde A$ and carries a vector part whenever $\tilde A$ is
not central; the multiplication, by contrast, has a central value for every argument. The two also read
different data: the adjoint depends on the argument through $Y_0$ alone, while the multiplication reads it
through the full pairing $B(\tilde A,\cdot)$, so the multiplication is self-adjoint exactly for a central
multiplier, the case $L^{\star}_{A_0e_0}\tilde X=A_0X_0e_0$, in which it too reads only the scalar part.

## The Two Groups of Linear Maps

**Definition.** The **group of linear maps preserving the form** is

$$
G_B = \{T\in GL(\mathbb{B}): B(T\tilde X,T\tilde Y)=B(\tilde X,\tilde Y)
\text{ for all } \tilde X,\tilde Y\},
$$

and the **group of transformations preserving the product** is

$$
G_{\star} = \{T\in GL(\mathbb{B}): T(\tilde X\star\tilde Y)=(T\tilde X)\star(T\tilde Y)
\text{ for all } \tilde X,\tilde Y\}.
$$

**Proposition (the two matrix conditions).** In the basis, with $G=I_4$ the Gram matrix of $B$,

$$
T\in G_B \quad\Longleftrightarrow\quad T^{\mathsf T}T=I_4, \qquad
T\in G_{\star} \quad\Longleftrightarrow\quad T^{\mathsf T}T=I_4 \ \text{and}\ T e_0=e_0 .
$$

*Proof.* The first equivalence is the invariant form written on the coordinates: $B(T\tilde X,T\tilde Y)=(T\tilde X)^{\mathsf T}(T\tilde Y)=\tilde X^{\mathsf T}T^{\mathsf T}T\tilde Y$, and this is $B(\tilde X,\tilde Y)$
for all $\tilde X,\tilde Y$ exactly when $T^{\mathsf T}T=I_4$. For the second, $T(\tilde X\star\tilde Y)=B(\tilde X,\tilde Y)Te_0$ must equal $(T\tilde X)\star(T\tilde Y)=B(T\tilde X,T\tilde Y)e_0$; taking
$\tilde X=\tilde Y=e_0$ gives $Te_0=B(Te_0,Te_0)e_0$, so $Te_0=\lambda e_0$ with $\lambda=\lambda^2$ and,
$T$ being invertible, $\lambda=1$; then $B(T\tilde X,T\tilde Y)=B(\tilde X,\tilde Y)$, which is
$T^{\mathsf T}T=I_4$. $\square$

**Corollary (dimensions and Lie algebras).** Over $\mathbb{C}$, the group $G_B$ has complex dimension $6$ and
its Lie algebra is $\{X:X^{\mathsf T}+X=0\}$, the space of antisymmetric matrices, of complex dimension $6$.
The group $G_{\star}$ has complex dimension $3$ and its Lie algebra is
$\{X:X^{\mathsf T}+X=0,\ Xe_0=0\}$, the antisymmetric matrices killing $e_0$, of complex dimension $3$. The
group $G_{\star}$ contains the maps $\operatorname{diag}(1,u_1,u_2,u_3)$ with $u_k=\pm1$, whose action negates
the chosen vector directions and fixes the unit.

*Proof.* A complex-linear $T$ preserving $B$ is a matrix with $T^{\mathsf T}T=I_4$; the Lie algebra is the
first-order form of this condition, $X^{\mathsf T}+X=0$, of dimension $4\cdot3/2=6$. Adding $Te_0=e_0$ to the
conditions of $G_{\star}$ kills the first column of $X$, which removes $3$ parameters and gives complex
dimension $3$. The diagonal sign maps satisfy $T^{\mathsf T}T=I_4$ and fix $e_0$. $\square$

**Remark (the structure group).** The **structure group** of the block is the group of invertible linear maps
that transport the product to a nonzero scalar multiple of itself,

$$
G^{\mathrm{str}}_{\star} = \{T\in GL(\mathbb{B}): T(\tilde X\star\tilde Y)=\lambda\,(T\tilde X)\star(T\tilde Y)
\text{ for some } \lambda\in\mathbb{C}^{\times}\}.
$$

The computation of the proposition gives the conditions $Te_0\in\mathbb{C}e_0$ and
$B(T\tilde X,T\tilde Y)=\mu B(\tilde X,\tilde Y)$ for a nonzero scalar $\mu$, that is
$T^{\mathsf T}T=\mu I_4$ together with the invariance of the central line. The form-preserving group is the
case $\mu=1$ of the rescaling condition, with no requirement on $Te_0$; the group preserving the product is
the intersection with $Te_0=e_0$, and there the value $\mu=1$ is forced back, since
$B(Te_0,Te_0)=\mu B(e_0,e_0)$ reads $1=\mu$. The three groups are related by

$$
G_{\star} \subset G^{\mathrm{str}}_{\star}, \qquad
G_{\star} = G^{\mathrm{str}}_{\star}\cap\{Te_0=e_0\}.
$$

The structure group contains maps that rescale the form, and the product-preserving group does not: rescaling
the product is not the same as preserving it, exactly as for a quadratic form.

## The Derivations of the Block

**Definition.** A **derivation** of the block is a complex-linear map $D$ with

$$
D(\tilde X\star\tilde Y) = (D\tilde X)\star\tilde Y + \tilde X\star(D\tilde Y)
\qquad\text{for all } \tilde X,\tilde Y\in\mathbb{B}.
$$

**Proposition (the weight, and its vanishing).** A derivation is the same thing as a complex-linear map
$D$ satisfying $D e_0=\delta e_0$ and

$$
B(D\tilde X,\tilde Y) + B(\tilde X,D\tilde Y) = \delta\,B(\tilde X,\tilde Y)
\qquad\text{for all } \tilde X,\tilde Y ,
$$

for one complex number $\delta$. The weight is forced to be zero: at $\tilde X=\tilde Y=e_0$ the identity
reads $De_0=2(De_0)_0e_0$, which with $De_0=\delta e_0$ is $\delta=2\delta$. Every derivation therefore has
$De_0=0$ and $D^{\mathsf T}+D=0$, and these maps, the Lie algebra of $G_B$ cut by $De_0=0$, form the whole
derivation algebra, of complex dimension $3$.

*Proof.* Writing the definition on the value, $D(\tilde X\star\tilde Y)=B(\tilde X,\tilde Y)De_0$ and
$(D\tilde X)\star\tilde Y+\tilde X\star(D\tilde Y)=\bigl(B(D\tilde X,\tilde Y)+B(\tilde X,D\tilde Y)\bigr)e_0$.
The vector part of the equality forces $De_0$ to be central, $De_0=\delta e_0$, and the central part is the
displayed identity. At $\tilde X=\tilde Y=e_0$ that identity gives
$De_0=B(De_0,e_0)e_0+B(e_0,De_0)e_0=2(De_0)_0e_0$, and $(De_0)_0=\delta$, so $\delta=0$. With $\delta=0$ the
identity is $B(D\tilde X,\tilde Y)+B(\tilde X,D\tilde Y)=0$, that is $D^{\mathsf T}+D=0$ in the basis, together
with $De_0=0$; antisymmetric matrices killing $e_0$ form the complex dimension $3$ space displayed. $\square$

**Remark (the inner derivations vanish).** The inner derivations of the operation are the maps
$\tilde X\mapsto \tilde A\star\tilde X-\tilde X\star\tilde A$, and they vanish identically because the
operation is commutative; the derivation algebra of the block is therefore entirely made of outer
derivations. The bracket of two multiplication operators,
$[L^{\star}_{\tilde A},L^{\star}_{\tilde B}]=A_0L^{\star}_{\tilde B}-B_0L^{\star}_{\tilde A}$, is **not** a derivation: its value on $\tilde X\star\tilde Y$
is zero, while the sum $(D\tilde X)\star\tilde Y+\tilde X\star(D\tilde Y)$ is
$\bigl(A_0B(\tilde B,\tilde X)-B_0B(\tilde A,\tilde X)\bigr)Y_0e_0+\bigl(A_0B(\tilde B,\tilde Y)-B_0B(\tilde A,\tilde Y)\bigr)X_0e_0$,
which does not vanish in general; the operator layer is not a Lie algebra of derivations here, in contrast with
the associative case.

## Summary

The operator layer of the symmetric quaternionic algebra is the single commutative family
$L^{\star}_{\tilde A}\tilde R=B(\tilde A,\tilde R)e_0$, with matrix in the basis equal to the row of the
coordinates of $\tilde A$ in the first row and zero elsewhere. Every nonzero multiplication has rank $1$, image
the central line $\mathbb{C}e_0$ and kernel the hyperplane $B(\tilde A,\cdot)=0$ of complex dimension $3$; its
trace is $A_0$ and its determinant is $0$. The multiplications compose by
$L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}=A_0L^{\star}_{\tilde B}$: the family is a faithful
$4$-dimensional vector space of operators, its operators are the matrices with a single nonzero row, and it is
neither commutative nor multiplicative. The adjoint of $L^{\star}_{\tilde A}$ with respect to $B$ is the map
$\tilde Y\mapsto\sum_\mu A_\mu Y_0e_\mu$, and the multiplication is self-adjoint exactly when the multiplier is
central. The group preserving the form is $\{T:T^{\mathsf T}T=I_4\}$, of complex dimension $6$, and the group
preserving the product is its subgroup with $Te_0=e_0$, of complex dimension $3$, containing the diagonal sign
maps; the structure group rescales the form and the product. A derivation is a map with $De_0=\delta e_0$ and
$B(D\tilde X,\tilde Y)+B(\tilde X,D\tilde Y)=\delta B(\tilde X,\tilde Y)$, where the weight $\delta$ is forced
to be $0$; the derivation algebra is the $3$-dimensional space $\{De_0=0,\ D^{\mathsf T}+D=0\}$, entirely outer.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\star}_{\tilde A}\tilde R=\tilde A\star\tilde R=B(\tilde A,\tilde R)e_0$ | the multiplication operator of the block |
| $\bigl[L^{\star}_{\tilde A}\bigr]_{0\mu}=A_\mu$ | its matrix in the basis, a single nonzero row |
| $\operatorname{Tr}(L^{\star}_{\tilde A})=A_0$, $\det(L^{\star}_{\tilde A})=0$, $\operatorname{rank}=1$ | its invariants for $\tilde A\ne0$ |
| $L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}=A_0L^{\star}_{\tilde B}$ | the composition law |
| $\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}$ | the adjoint with respect to $B$ |
| $G_B=\{T:T^{\mathsf T}T=I_4\}$ | the group of linear maps preserving the form, complex dimension $6$ |
| $G_{\star}=\{T:T^{\mathsf T}T=I_4,\ Te_0=e_0\}$ | the group of transformations preserving the product, complex dimension $3$ |
| $G^{\mathrm{str}}_{\star}$ | the structure group, transporting the product to a scalar multiple |
| $D(\tilde X\star\tilde Y)=(D\tilde X)\star\tilde Y+\tilde X\star(D\tilde Y)$ | the derivation condition |

## Further Reading

- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the multiplications and the radical
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form $B$, its Gram matrix and its non-degeneracy
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`) and *One-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the left multiplications of the parent product
- *Automorphisms and Derivations of Algebras* (`articles_maths/automorphisms-and-derivations-of-algebras.md`), for the general theory of a derivation and its inner part
- *The Symmetric Quaternionic Algebra in the Matrix Representations* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-matrix-representations.md`), for the same operators in the two matrix models
- *The Six Subspaces under the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the product on the six subspaces
