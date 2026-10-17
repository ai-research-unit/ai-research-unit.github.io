# __The Multiplication Operators of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication is commutative, so its left multiplications and its right
multiplications coincide; the operator of the block is the single family

$$
L^{\star}_{\tilde A}: \mathbb{B}\longrightarrow\mathbb{C}e_t,\qquad
L^{\star}_{\tilde A}\tilde R = \tilde A\star\tilde R = \langle\tilde A,\tilde R\rangle_{\natural}e_t ,
$$

of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*. This article reads the
family as the operator layer of the block: the matrices, the ranks and the traces of the operators, their
composition and the algebra they generate, their adjoints with respect to the form $\langle\cdot\rangle_{\natural}$, the derivations the
block produces, and the two groups of linear maps attached to it — the group that preserves the form and the
group that preserves the product. It follows the pattern of the operator articles of the parent row,
*The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *One-Sided Operators on
the General Quaternionic Algebra of Biquaternions*, and it cites rather than restates the general theory of
the left multiplications of an algebra.

The operation and its formula are *Introduction to the Symmetric Quaternionic Algebra*; the
form $\langle\cdot\rangle_{\natural}$ and its role as the coefficient are *The Quaternion Form as a Product on the Symmetric Quaternionic
Algebra*; the derivation layer of a general algebra is *Automorphisms and Derivations of Algebras*; the matrix models are
*Introduction to the Symmetric Quaternionic Algebra*. Nothing of the enriched layer of Part II is used.

**Conventions.** The basis is $e_t,\vec e_x,\vec e_y,\vec e_z$; the product is $\tilde P\star\tilde Q=\langle\tilde P,\tilde Q\rangle_{\natural}e_t$
with $\langle\tilde P,\tilde Q\rangle_{\natural}=P_tQ_t+(\vec P,\vec Q)$; an operator is written as a $4\times4$ matrix in the
basis when its entries are needed, and the matrix of a linear map $T$ is written $[T]$; the transpose of a
matrix is written with a superscript $\mathsf T$.

## The Operators, Their Matrices and Their Ranks

**Proposition (the matrix of a multiplication).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the matrix of
$L^{\star}_{\tilde A}$ has its first row equal to the coordinates of $\tilde A$ and every other entry zero:

$$
\bigl[L^{\star}_{\tilde A}\bigr]_{t\mu} = A_\mu, \qquad
\bigl[L^{\star}_{\tilde A}\bigr]_{\nu\mu}=0 \ (\nu\in\{x,y,z\}),
$$

that is, the four columns are the four multiples $A_te_t,A_xe_t,A_ye_t,A_ze_t$.

*Proof.* $L^{\star}_{\tilde A}e_\mu=\langle\tilde A,e_\mu\rangle_{\natural}e_t=A_\mu e_t$, so the $\mu$-th column is $A_\mu e_t$,
with coordinates $A_\mu$ at the first place and zero elsewhere.

**Corollary (rank and image).** For $\tilde A\ne0$ the rank of $L^{\star}_{\tilde A}$ is $1$ and its image is
the whole central line $\mathbb{C}e_t$; for $\tilde A=0$ it is the zero operator. The **kernel** is the
hyperplane

$$
\ker L^{\star}_{\tilde A} = \{\tilde R\in\mathbb{B}: \langle\tilde A,\tilde R\rangle_{\natural}=0\},
$$

of complex dimension $3$ for $\tilde A\ne0$; it is the hyperplane of the elements paired to zero with
$\tilde A$ by $N$, and it contains
$\tilde A$ exactly when $\tilde A$ is isotropic.

*Proof.* The columns span $\mathbb{C}e_t$ if some $A_\mu\ne0$, and the image is central; the kernel is the
kernel of the linear form $\langle\tilde A,\cdot\rangle_{\natural}$, whose rank is $1$ because the form is non-degenerate. The last
statement is $\langle\tilde A,\tilde A\rangle_{\natural}=\langle\tilde A\rangle_{\natural}=0$.

**Proposition (trace and determinant).** For every $\tilde A$,

$$
\operatorname{Tr}\bigl(L^{\star}_{\tilde A}\bigr) = A_t, \qquad
\det\bigl(L^{\star}_{\tilde A}\bigr) = 0 .
$$

*Proof.* The trace is the sum of the diagonal entries of the matrix above, and only the entry $(t,t)=A_t$ is
nonzero. The determinant vanishes because the rank is at most $1$ on a space of dimension $4$; for $\tilde A=0$
the operator is zero.

**Remark (a rank-one layer).** The operator layer of the block is a rank-one layer: every nonzero
multiplication has rank one, so the family is as far from the identity operator as a nonzero family can be, and
no element of the algebra is a unit. The trace detects the scalar part of the multiplier and nothing else: the
vector part of the multiplier is invisible to the trace, and the operator family separates the elements by the
kernel and not by the trace.

## Composition and the Algebra of Operators

**Proposition (the composition law).** The multiplication operators compose by

$$
L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B} = A_t\,L^{\star}_{\tilde B},
$$

and the family $\{L^{\star}_{\tilde A}:\tilde A\in\mathbb{B}\}$ is a complex vector space of dimension $4$, the
**monoid of multiplications** of the block.

*Proof.* $L^{\star}_{\tilde A}(L^{\star}_{\tilde B}\tilde R)=L^{\star}_{\tilde A}\bigl(\langle\tilde B,\tilde R\rangle_{\natural}e_t\bigr)=\langle\tilde B,\tilde R\rangle_{\natural}\langle\tilde A,e_t\rangle_{\natural}e_t=A_t\langle\tilde B,\tilde R\rangle_{\natural}e_t=A_tL^{\star}_{\tilde B}\tilde R$.

**Corollary (the map is faithful but not multiplicative).** The map $\tilde A\mapsto L^{\star}_{\tilde A}$ is
injective, its kernel being the radical $\{0\}$ of the operation, so the operator family represents the algebra
faithfully as a vector space. It is **not** a representation of the operation: the composition law compares
$L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}=A_tL^{\star}_{\tilde B}$ with
$L^{\star}_{\tilde A\star\tilde B}=\langle\tilde A,\tilde B\rangle_{\natural}L^{\star}_{e_t}$, and the two differ, as at
$\tilde A=\vec e_x$, $\tilde B=\vec e_x$, where the first is $0$ and the second is $L^{\star}_{e_t}\ne0$. The monoid of
multiplications is not commutative either, $L^{\star}_{e_t}\circ L^{\star}_{\vec e_x}=L^{\star}_{\vec e_x}$ while
$L^{\star}_{\vec e_x}\circ L^{\star}_{e_t}=0$, although the operation is commutative.

**Remark (the operator algebra in the basis).** The four operators $L^{\star}_{e_\mu}$ are the matrices with a
single nonzero row: $L^{\star}_{e_\mu}$ has the entry $1$ at position $(t,\mu)$ and zeros elsewhere. Their
products are $L^{\star}_{e_t}\circ L^{\star}_{e_\nu}=L^{\star}_{e_\nu}$ and
$L^{\star}_{\vec e_k}\circ L^{\star}_{e_\nu}=0$ for $k\in\{x,y,z\}$, so the algebra generated by the family is the four
dimensional algebra of the matrices whose only possibly nonzero row is the first, and its multiplication is the
product of such row matrices. This is the shadow of the collapse: the operator family carries the four
coordinates of the multiplier in a single row, and no product of two multiplications can recover the vector
part of a multiplier.

## The Adjoint with Respect to the Form

**Definition.** The **adjoint** of a complex-linear map $T$ with respect to $\langle\cdot\rangle_{\natural}$ is the linear map $T^{\dagger}$
determined by

$$
N\bigl(T\tilde X,\tilde Y\bigr) = N\bigl(\tilde X,T^{\dagger}\tilde Y\bigr) \qquad
\text{for all } \tilde X,\tilde Y\in\mathbb{B},
$$

which exists and is unique because $\langle\cdot\rangle_{\natural}$ is non-degenerate.

**Proposition (the adjoint of a multiplication).** For every $\tilde A$,

$$
\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}\tilde Y = \sum_\mu A_\mu Y_t\,e_\mu ,
\qquad\text{and}\qquad
L^{\star}_{\tilde A}\ \text{is self-adjoint}\quad\Longleftrightarrow\quad \tilde A\in\mathbb{C}e_t .
$$

*Proof.* $\langle L^{\star}_{\tilde A}\tilde X,\tilde Y\rangle_{\natural}=N\bigl(\langle\tilde A,\tilde X\rangle_{\natural}e_t,\tilde Y\bigr)=\langle\tilde A,\tilde X\rangle_{\natural}Y_t=\sum_\mu A_\mu X_\mu Y_t$, and $\langle\tilde X,\sum_\mu A_\mu Y_te_\mu\rangle_{\natural}=\sum_\mu X_\mu A_\mu Y_t$; the two agree for all $\tilde X$, which gives the displayed adjoint. For
self-adjointness, compare the adjoint with $L^{\star}_{\tilde A}\tilde Y=\langle\tilde A,\tilde Y\rangle_{\natural}e_t$: the identity
$\sum_\mu A_\mu Y_te_\mu=\bigl(\sum_\mu A_\mu Y_\mu\bigr)e_t$ for all $\tilde Y$ forces $A_\mu=0$ for
$\mu\in\{x,y,z\}$.

**Remark (the adjoint is the operator of a linear form).** The adjoint
$\tilde Y\mapsto\sum_\mu A_\mu Y_te_\mu$ scales the whole element $\tilde A$ by the scalar part of the
argument, so its value lies in the line $\mathbb{C}\tilde A$ and carries a vector part whenever $\tilde A$ is
not central; the multiplication, by contrast, has a central value for every argument. The two also read
different data: the adjoint depends on the argument through $Y_t$ alone, while the multiplication reads it
through the full pairing $\langle\tilde A,\cdot\rangle_{\natural}$, so the multiplication is self-adjoint exactly for a central
multiplier, the case $L^{\star}_{A_te_t}\tilde X=A_tX_te_t$, in which it too reads only the scalar part.

## The Two Groups of Linear Maps

**Definition.** The **group of linear maps preserving the form** is

$$
G_N = \{T\in GL(\mathbb{B}): \langle T\tilde X,T\tilde Y\rangle_{\natural}=\langle\tilde X,\tilde Y\rangle_{\natural}
\text{ for all } \tilde X,\tilde Y\},
$$

and the **group of transformations preserving the product** is

$$
G_{\star} = \{T\in GL(\mathbb{B}): T(\tilde X\star\tilde Y)=(T\tilde X)\star(T\tilde Y)
\text{ for all } \tilde X,\tilde Y\}.
$$

**Proposition (the two matrix conditions).** In the basis, with $G=I_4$ the Gram matrix of $N$,

$$
T\in G_N \quad\Longleftrightarrow\quad T^{\mathsf T}T=I_4, \qquad
T\in G_{\star} \quad\Longleftrightarrow\quad T^{\mathsf T}T=I_4 \ \text{and}\ T e_t=e_t .
$$

*Proof.* The first equivalence is the invariant form written on the coordinates: $\langle T\tilde X,T\tilde Y\rangle_{\natural}=(T\tilde X)^{\mathsf T}(T\tilde Y)=\tilde X^{\mathsf T}T^{\mathsf T}T\tilde Y$, and this is $\langle\tilde X,\tilde Y\rangle_{\natural}$
for all $\tilde X,\tilde Y$ exactly when $T^{\mathsf T}T=I_4$. For the second, $T(\tilde X\star\tilde Y)=\langle\tilde X,\tilde Y\rangle_{\natural}Te_t$ must equal $(T\tilde X)\star(T\tilde Y)=\langle T\tilde X,T\tilde Y\rangle_{\natural}e_t$; taking
$\tilde X=\tilde Y=e_t$ gives $Te_t=\langle Te_t,Te_t\rangle_{\natural}e_t$, so $Te_t=\lambda e_t$ with $\lambda=\lambda^2$ and,
$T$ being invertible, $\lambda=1$; then $\langle T\tilde X,T\tilde Y\rangle_{\natural}=\langle\tilde X,\tilde Y\rangle_{\natural}$, which is
$T^{\mathsf T}T=I_4$.

**Corollary (dimensions and Lie algebras).** Over $\mathbb{C}$, the group $G_N$ has complex dimension $6$ and
its Lie algebra is $\{X:X^{\mathsf T}+X=0\}$, the space of antisymmetric matrices, of complex dimension $6$.
The group $G_{\star}$ has complex dimension $3$ and its Lie algebra is
$\{X:X^{\mathsf T}+X=0,\ Xe_t=0\}$, the antisymmetric matrices killing $e_t$, of complex dimension $3$. The
group $G_{\star}$ contains the maps $\operatorname{diag}(1,u_x,u_y,u_z)$ with $u_k=\pm1$, whose action negates
the chosen vector directions and fixes the unit.

*Proof.* A complex-linear $T$ preserving $\langle\cdot\rangle_{\natural}$ is a matrix with $T^{\mathsf T}T=I_4$; the Lie algebra is the
first-order form of this condition, $X^{\mathsf T}+X=0$, of dimension $4\cdot3/2=6$. Adding $Te_t=e_t$ to the
conditions of $G_{\star}$ kills the first column of $X$, which removes $3$ parameters and gives complex
dimension $3$. The diagonal sign maps satisfy $T^{\mathsf T}T=I_4$ and fix $e_t$.

**Remark (the structure group).** The **structure group** of the block is the group of invertible linear maps
that transport the product to a nonzero scalar multiple of itself,

$$
G^{\mathrm{str}}_{\star} = \{T\in GL(\mathbb{B}): T(\tilde X\star\tilde Y)=\lambda\,(T\tilde X)\star(T\tilde Y)
\text{ for some } \lambda\in\mathbb{C}^{\times}\}.
$$

The computation of the proposition gives the conditions $Te_t\in\mathbb{C}e_t$ and
$\langle T\tilde X,T\tilde Y\rangle_{\natural}=\mu \langle\tilde X,\tilde Y\rangle_{\natural}$ for a nonzero scalar $\mu$, that is
$T^{\mathsf T}T=\mu I_4$ together with the invariance of the central line. The form-preserving group is the
case $\mu=1$ of the rescaling condition, with no requirement on $Te_t$; the group preserving the product is
the intersection with $Te_t=e_t$, and there the value $\mu=1$ is forced back, since
$\langle Te_t,Te_t\rangle_{\natural}=\mu \langle e_t,e_t\rangle_{\natural}$ reads $1=\mu$. The three groups are related by

$$
G_{\star} \subset G^{\mathrm{str}}_{\star}, \qquad
G_{\star} = G^{\mathrm{str}}_{\star}\cap\{Te_t=e_t\}.
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
$D$ satisfying $D e_t=\delta e_t$ and

$$
\langle D\tilde X,\tilde Y\rangle_{\natural} + \langle\tilde X,D\tilde Y\rangle_{\natural} = \delta\,\langle\tilde X,\tilde Y\rangle_{\natural}
\qquad\text{for all } \tilde X,\tilde Y ,
$$

for one complex number $\delta$. The weight is forced to be zero: at $\tilde X=\tilde Y=e_t$ the identity
reads $De_t=2(De_t)_te_t$, which with $De_t=\delta e_t$ is $\delta=2\delta$. Every derivation therefore has
$De_t=0$ and $D^{\mathsf T}+D=0$, and these maps, the Lie algebra of $G_N$ cut by $De_t=0$, form the whole
derivation algebra, of complex dimension $3$.

*Proof.* Writing the definition on the value, $D(\tilde X\star\tilde Y)=\langle\tilde X,\tilde Y\rangle_{\natural}De_t$ and
$(D\tilde X)\star\tilde Y+\tilde X\star(D\tilde Y)=\bigl(\langle D\tilde X,\tilde Y\rangle_{\natural}+\langle\tilde X,D\tilde Y\rangle_{\natural}\bigr)e_t$.
The vector part of the equality forces $De_t$ to be central, $De_t=\delta e_t$, and the central part is the
displayed identity. At $\tilde X=\tilde Y=e_t$ that identity gives
$De_t=\langle De_t,e_t\rangle_{\natural}e_t+\langle e_t,De_t\rangle_{\natural}e_t=2(De_t)_te_t$, and $(De_t)_t=\delta$, so $\delta=0$. With $\delta=0$ the
identity is $\langle D\tilde X,\tilde Y\rangle_{\natural}+\langle\tilde X,D\tilde Y\rangle_{\natural}=0$, that is $D^{\mathsf T}+D=0$ in the basis, together
with $De_t=0$; antisymmetric matrices killing $e_t$ form the complex dimension $3$ space displayed.

**Remark (the inner derivations vanish).** The inner derivations of the operation are the maps
$\tilde X\mapsto \tilde A\star\tilde X-\tilde X\star\tilde A$, and they vanish identically because the
operation is commutative; the derivation algebra of the block is therefore entirely made of outer
derivations. The bracket of two multiplication operators,
$[L^{\star}_{\tilde A},L^{\star}_{\tilde B}]=A_tL^{\star}_{\tilde B}-B_tL^{\star}_{\tilde A}$, is **not** a derivation: its value on $\tilde X\star\tilde Y$
is zero, while the sum $(D\tilde X)\star\tilde Y+\tilde X\star(D\tilde Y)$ is
$\bigl(A_t\langle\tilde B,\tilde X\rangle_{\natural}-B_t\langle\tilde A,\tilde X\rangle_{\natural}\bigr)Y_te_t+\bigl(A_t\langle\tilde B,\tilde Y\rangle_{\natural}-B_t\langle\tilde A,\tilde Y\rangle_{\natural}\bigr)X_te_t$,
which does not vanish in general; the operator layer is not a Lie algebra of derivations here, in contrast with
the associative case.

## Summary

The operator layer of the symmetric quaternionic algebra is the single commutative family
$L^{\star}_{\tilde A}\tilde R=\langle\tilde A,\tilde R\rangle_{\natural}e_t$, with matrix in the basis equal to the row of the
coordinates of $\tilde A$ in the first row and zero elsewhere. Every nonzero multiplication has rank $1$, image
the central line $\mathbb{C}e_t$ and kernel the hyperplane $\langle\tilde A,\cdot\rangle_{\natural}=0$ of complex dimension $3$; its
trace is $A_t$ and its determinant is $0$. The multiplications compose by
$L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}=A_tL^{\star}_{\tilde B}$: the family is a faithful
$4$-dimensional vector space of operators, its operators are the matrices with a single nonzero row, and it is
neither commutative nor multiplicative. The adjoint of $L^{\star}_{\tilde A}$ with respect to $\langle\cdot\rangle_{\natural}$ is the map
$\tilde Y\mapsto\sum_\mu A_\mu Y_te_\mu$, and the multiplication is self-adjoint exactly when the multiplier is
central. The group preserving the form is $\{T:T^{\mathsf T}T=I_4\}$, of complex dimension $6$, and the group
preserving the product is its subgroup with $Te_t=e_t$, of complex dimension $3$, containing the diagonal sign
maps; the structure group rescales the form and the product. A derivation is a map with $De_t=\delta e_t$ and
$\langle D\tilde X,\tilde Y\rangle_{\natural}+\langle\tilde X,D\tilde Y\rangle_{\natural}=\delta \langle\tilde X,\tilde Y\rangle_{\natural}$, where the weight $\delta$ is forced
to be $0$; the derivation algebra is the $3$-dimensional space $\{De_t=0,\ D^{\mathsf T}+D=0\}$, entirely outer.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\star}_{\tilde A}\tilde R=\tilde A\star\tilde R=\langle\tilde A,\tilde R\rangle_{\natural}e_t$ | the multiplication operator of the block |
| $\bigl[L^{\star}_{\tilde A}\bigr]_{t\mu}=A_\mu$ | its matrix in the basis, a single nonzero row |
| $\operatorname{Tr}(L^{\star}_{\tilde A})=A_t$, $\det(L^{\star}_{\tilde A})=0$, $\operatorname{rank}=1$ | its invariants for $\tilde A\ne0$ |
| $L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}=A_tL^{\star}_{\tilde B}$ | the composition law |
| $\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}$ | the adjoint with respect to $N$ |
| $G_N=\{T:T^{\mathsf T}T=I_4\}$ | the group of linear maps preserving the form, complex dimension $6$ |
| $G_{\star}=\{T:T^{\mathsf T}T=I_4,\ Te_t=e_t\}$ | the group of transformations preserving the product, complex dimension $3$ |
| $G^{\mathrm{str}}_{\star}$ | the structure group, transporting the product to a scalar multiple |
| $D(\tilde X\star\tilde Y)=(D\tilde X)\star\tilde Y+\tilde X\star(D\tilde Y)$ | the derivation condition |

## Further Reading

- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the multiplications and the radical
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form $\langle\cdot\rangle_{\natural}$, its Gram matrix and its non-degeneracy
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`) and *One-Sided Operators on the General Quaternionic Algebra* (`articles_maths/one-sided-operators-on-the-general-quaternionic-algebra.md`), for the left multiplications of the parent product
- *Automorphisms and Derivations of Algebras* (`articles_maths/automorphisms-and-derivations-of-algebras.md`), for the general theory of a derivation and its inner part
- *Introduction to the Symmetric Quaternionic Algebra* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra.md`), for the same operators in the realization
- *Introduction to the Symmetric Quaternionic Algebra* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra.md`), for the same operators in the regular model
- *Remarkable Subspaces under the Symmetric Quaternionic Algebra* (`articles_maths/remarkable-subspaces-under-the-symmetric-quaternionic-algebra.md`), for the product on the remarkable subspaces
