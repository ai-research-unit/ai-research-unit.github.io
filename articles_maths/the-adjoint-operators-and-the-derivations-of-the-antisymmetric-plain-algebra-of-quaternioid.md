# __The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ is the real Lie algebra
$\mathfrak{g}=(\mathbb{H},\times)$ with the cross product
$\tilde q_1\times\tilde q_2=\vec q_1\times\vec q_2$ of *The Lie Algebra of the Antisymmetric Plain
Algebra*, below this article in this category. This article reads its adjoint operators, proves that
they are derivations, computes the whole derivation algebra and the automorphism group, and compares

The two structural facts of the block give the answer at once. Alternation makes the adjoint the cross
product by the vector part; the Jacobi identity is exactly the statement that the adjoint operators
are derivations. The derivations are the adjoints, an algebra isomorphic to the vector subspace with
the cross product, together with one outer derivation scaling the centre; the automorphism group is the
product of the nonzero scalings of the centre and the group of linear maps of the vector subspace
preserving the cross product.

**This is not the algebra $\mathbb{H}$.** The operators are read on the Lie bracket, not on the
associative product. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the
bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the
natural sign and gives nothing new.

The operation and the Jacobi identity are *The Specificities of the Antisymmetric Plain Algebra*; the
Lie structure is *The Lie Algebra of the Antisymmetric Plain Algebra* and the form is *The Killing Form
of the Antisymmetric Plain Algebra*, both below this article in this category.
counterpart is *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* of the

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and
$\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$; the centre is $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_t$, the vector subspace is
$\mathrm{Vect}(\mathbb{H})=\{\vec q\}=\mathbb{R}^3$, and $C_{\vec q_1}$ is the cross-product matrix
$C_{\vec q_1}\vec q_2=\vec q_1\times\vec q_2$. The bracket of two endomorphisms is
$[A,B]=AB-BA$; a **derivation** of the block is an endomorphism $D$ with
$D(\tilde q_1\times\tilde q_2)=D\tilde q_1\times\tilde q_2+\tilde q_1\times D\tilde q_2$.

## The Adjoint Operators

**Definition.** The **adjoint operator** of $\tilde q_1$ is the left multiplication

$$
\operatorname{ad}_{\tilde q_1}\tilde q_2=\tilde q_1\times\tilde q_2 .
$$

### The Matrix and the Invariants

**Proposition.** In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the adjoint is the block matrix

$$
\operatorname{ad}_{\tilde q}=\operatorname{diag}(0,C_{\vec q})
\quad\text{on}\quad \mathbb{H}=\mathbb{R}e_t\oplus\mathrm{Vect}(\mathbb{H}),
$$

with the invariants

$$
\operatorname{Tr}\operatorname{ad}_{\tilde q}=0,\qquad
\det\operatorname{ad}_{\tilde q}=0,\qquad
\operatorname{rank}\operatorname{ad}_{\tilde q}=\begin{cases}2,&\vec q\neq0,\\0,&\vec q=0,\end{cases}
$$

and the characteristic polynomial $\chi(t)=t^2(t^2+|\vec q|^2)$.

*Proof.* The bracket vanishes on the scalar direction and the pure part is the cross product by
$\vec q$, so the matrix is $\operatorname{diag}(0,C_{\vec q})$; the invariants descend from
$C_{\vec q}^2=\vec q\vec q^{\mathsf T}-|\vec q|^2\mathrm{I}_3$, of characteristic
polynomial $t(t^2+|\vec q|^2)$, and from the vanishing scalar block.

### The Kernel and the Image

**Proposition.** For a noncentral element the kernel and the image of the adjoint are

$$
\ker\operatorname{ad}_{\tilde q_1}=\mathbb{R}e_t\oplus\mathbb{R}\vec q_1,\qquad
\operatorname{im}\operatorname{ad}_{\tilde q_1}=\vec q_1^{\perp}\cap\mathrm{Vect}(\mathbb{H}),
$$

the kernel being the two-dimensional plane spanned by the centre and the element, and the image the
two-dimensional plane of the vector subspace orthogonal to $\vec q_1$. For a central element the
adjoint is zero.

*Proof.* The kernel is the annihilator of the element for the block, computed in *Zero Divisors of the
Antisymmetric Plain Algebra*, below this article in this category, as the plane
$\mathbb{R}e_t\oplus\mathbb{R}\vec q_1$; the image is $\{\vec q_1\times\vec q_2\}$, which is the
plane orthogonal to $\vec q_1$ when $\vec q_1\neq0$.

## The Adjoints Are Derivations

**Theorem (the Jacobi identity is the derivation property).** For every $\tilde q_1$ the adjoint
$\operatorname{ad}_{\tilde q_1}$ is a derivation of the block,

$$
\operatorname{ad}_{\tilde q_1}(\tilde q_2\times\tilde q_3)
=\operatorname{ad}_{\tilde q_1}\tilde q_2\times\tilde q_3+\tilde q_2\times\operatorname{ad}_{\tilde q_1}\tilde q_3 ,
$$

and the identity is exactly the Jacobi identity of the block; equivalently the adjoint representation is
a Lie homomorphism,

$$
\operatorname{ad}_{\tilde q_1\times\tilde q_2}=[\operatorname{ad}_{\tilde q_1},\operatorname{ad}_{\tilde q_2}],
\qquad\text{that is}\qquad
\operatorname{ad}_{[\tilde q_1,\tilde q_2]}=[\operatorname{ad}_{\tilde q_1},\operatorname{ad}_{\tilde q_2}].
$$

*Proof.* Expanded, the derivation identity is
$\tilde q_1\times(\tilde q_2\times\tilde q_3)=(\tilde q_1\times\tilde q_2)\times\tilde q_3+\tilde q_2\times(\tilde q_1\times\tilde q_3)$,
which is the Jacobi identity rearranged with the antisymmetry of the block. The homomorphism form is
the same identity read on the commutator of the endomorphisms.

**Remark (the block is the privileged one).** The equivalence of the two properties is the content of
the Jacobi identity, and it holds for the block alone among the two antisymmetric products of the
space: for the antisymmetric quaternionic operation the adjoint is not a derivation, and the failure is
the same defect as the failure of Jacobi (*The Adjoint Operators of the Antisymmetric Quaternionic
Algebra*, below this article in this category).

## The Derivation Algebra

**Theorem (the derivations).** The derivation algebra of the block is

$$
\operatorname{Der}(\mathfrak{g})=\operatorname{ad}(\mathfrak{g})\oplus\mathbb{R}D_0,
$$

of real dimension four, where $\operatorname{ad}(\mathfrak{g})$ is the three-dimensional algebra of
inner derivations, isomorphic to the derived algebra $\mathrm{Vect}(\mathbb{H})$ and to
$\mathfrak{so}(3)$, and $D_0$ is the derivation

$$
D_0(e_t)=e_t,\qquad D_0(\vec q)=0 ,
$$

which scales the centre and is outer. The kernel of the adjoint representation is the centre, so
$\operatorname{ad}(\mathfrak{g})\cong\mathfrak{g}/\mathbb{R}e_t\cong\mathfrak{so}(3)$.

*Proof.* Every adjoint is a derivation by the Jacobi identity, and the map
$\tilde q\mapsto\operatorname{ad}_{\tilde q}$ has kernel the centre; its image is therefore
$\mathfrak{g}/\mathbb{R}e_t$, the derived algebra, of dimension three. The map $D_0$ is a derivation:
$D_0(\tilde q_1\times\tilde q_2)=0$ and
$D_0\tilde q_1\times\tilde q_2+\tilde q_1\times D_0\tilde q_2=(q_{1t}e_t)\times\tilde q_2+\tilde q_1\times(q_{2t}e_t)=0$.
It is not inner, because every inner derivation annihilates the centre and $D_0$ does not. The
dimension count $\dim\operatorname{Der}(\mathfrak{g})=4$ is obtained by solving the derivation system on
the basis.

**Remark (the outer derivation and the centre).** The algebra $\mathfrak{g}$ is the direct sum of its
centre and its derived algebra, so its derivations split into the derivations of the simple derived
algebra, which are inner, and the derivations of the abelian centre, which are the scalings; the
inner ones are the adjoints and the scaling of the centre is the one outer direction.

## The Automorphism Group

**Theorem (the automorphisms).** The automorphism group of the block is

$$
\operatorname{Aut}(\mathfrak{g})=\mathbb{R}^{\times}\times\operatorname{SO}(3),
$$

of real dimension four: an automorphism fixes the centre setwise, acts on it by a nonzero scalar, and
acts on the vector subspace by a linear map preserving the cross product.

*Proof.* Let $T$ be a linear automorphism with $T(\tilde q_1\times\tilde q_2)=T\tilde q_1\times T\tilde q_2$.
The centre is characteristic, being the set of elements that annihilate every element on the left, so
$T$ preserves $\mathbb{R}e_t$ and $Te_t=c e_t$ with $c\neq0$. Then $T$ preserves the vector subspace,
which is the image of the block, and on it $A=T|_{\mathrm{Vect}(\mathbb{H})}$ satisfies
$A(\vec q_a\times\vec v)=A\vec q_a\times A\vec v$, because the two sides are the images of
$\vec q_a\times\vec v$ and of $\vec q_a,\vec v$. Every such $A$ is a linear map of
$\mathbb{R}^3$ preserving the cross product, which is the special orthogonal group
$\operatorname{SO}(3)$; its dimension is three, the scalar $c$ contributes one, and the two choices are
independent and commute. The group is therefore $\mathbb{R}^{\times}\times\operatorname{SO}(3)$ of
dimension four.

**Remark (the relation to the rotations).** The group of the vector subspace preserving the cross
product is the group the menu calls the rotations of the vector subspace; it is the realisation of
$\operatorname{SO}(3)$, named algebraically here and read as linear maps of $\mathbb{R}^3$ without a
metric statement. The Lie algebra of $\operatorname{Aut}(\mathfrak{g})$ is $\operatorname{Der}(\mathfrak{g})$,
generated by the inner derivations and by $D_0$.

## Summary

The adjoint operators of the antisymmetric plain algebra are the left multiplications by the cross
product, of matrix $\operatorname{diag}(0,C_{\vec q})$, trace zero, determinant zero, rank two off
the centre, with the characteristic polynomial $t^2(t^2+|\vec q|^2)$ and the kernel plane
$\mathbb{R}e_t\oplus\mathbb{R}\vec q$. They are derivations, and the Jacobi identity is exactly that
statement, equivalently the homomorphism property of the adjoint representation. The derivation
algebra is the inner algebra $\mathfrak{so}(3)$ together with the outer scaling of the centre, of real
dimension four; the inner derivations are the image of the adjoint representation, whose kernel is the
centre. The automorphism group is $\mathbb{R}^{\times}\times\operatorname{SO}(3)$: the scalings of the
centre and the linear maps of the vector subspace preserving the cross product. Over $\mathbb{C}$ the
same structure has $\mathfrak{sl}(2,\mathbb{C})$ and $\mathbb{C}^{\times}\times\operatorname{PGL}(2,\mathbb{C})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ad}_{\tilde q_1}\tilde q_2=\tilde q_1\times\tilde q_2$ | the adjoint operator |
| $\operatorname{ad}_{\tilde q}=\operatorname{diag}(0,C_{\vec q})$ | its matrix |
| $\ker\operatorname{ad}_{\tilde q}=\mathbb{R}e_t\oplus\mathbb{R}\vec q$ | the kernel, the annihilator plane |
| $\operatorname{ad}_{\tilde q_1\times\tilde q_2}=[\operatorname{ad}_{\tilde q_1},\operatorname{ad}_{\tilde q_2}]$ | the derivation property as the Jacobi identity |
| $\operatorname{Der}(\mathfrak{g})=\operatorname{ad}(\mathfrak{g})\oplus\mathbb{R}D_0$ | the derivation algebra |
| $\operatorname{Aut}(\mathfrak{g})=\mathbb{R}^{\times}\times\operatorname{SO}(3)$ | the automorphism group |

## Further Reading

- [Introduction to the Antisymmetric Plain Algebra](introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.html), for the bracket, its table and the Jacobi identity.
- [The Lie Algebra of the Antisymmetric Plain Algebra](the-lie-algebra-of-the-antisymmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the centre, the derived algebra and the structure constants.
- [The Killing Form of the Antisymmetric Plain Algebra](the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the form and the Casimir element.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), below this article in this category, for the annihilator that is the kernel of the adjoint.
- [The Adjoint Operators of the Antisymmetric Quaternionic Algebra](the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.html), below this article in this category, for the block whose adjoint is not a derivation.
