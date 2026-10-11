# __The Killing Form of the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ is the real Lie algebra
$\mathfrak{g}=(\mathbb{H},\times)$ with the cross product
$\tilde p\times\tilde q=\mathbf p\times\mathbf q$ of *The Lie Algebra of the Antisymmetric Plain
Algebra*, below this article in this category. This article computes its Killing form, identifies the
space of invariant bilinear forms, exhibits the Casimir element and compares the form with the
biquaternion blocks.

The result is simple and rigid: the form is the Euclidean form of the vector subspace up to the factor
$-2$, with the scalar direction in its radical, so it is negative semidefinite, negative definite on
the derived algebra, and its radical is the centre. The space of invariant bilinear forms is the plane
spanned by the Killing form and the scalar-part form $\varphi(\tilde p,\tilde q)=p_0q_0$, and there is
no nonzero alternating invariant form.

**This is not the algebra $\mathbb{H}$.** The form belongs to the Lie bracket of the vector parts, not
to the associative multiplication. Throughout, the natural sign ${}^{\natural}$ is the quaternion
conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star
coincides with the natural sign and gives nothing new.

The Lie algebra, its centre and its derived algebra are *The Lie Algebra of the Antisymmetric Plain
Algebra*; the adjoint operators and the derivations are *The Adjoint Operators and the Derivations of
the Antisymmetric Plain Algebra*, both below this article in this category. The biquaternion
counterparts are *The Killing Form of the Antisymmetric Plain Algebra* and *Norm and Invertibility in
the Antisymmetric Plain Algebra* of the biquaternion chapter.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; $\mathbf p\cdot\mathbf q$ is the Euclidean dot product, $\mathbf p\times\mathbf q$
the vector product, and $C_{\mathbf p}$ the cross-product matrix. The **plain form** is
$B(\tilde p,\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p\tilde q)$, the **quaternion
form** is $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$, and the **scalar-part form** is
$\varphi(\tilde p,\tilde q)=p_0q_0$.

## The Adjoint Representation and the Killing Form

**Definition.** The **Killing form** of the Lie algebra $\mathfrak{g}=(\mathbb{H},\times)$ is

$$
\kappa(\tilde p,\tilde q)=\operatorname{Tr}\bigl(\operatorname{ad}_{\tilde p}\operatorname{ad}_{\tilde q}\bigr),
$$

where $\operatorname{ad}_{\tilde p}\tilde r=\tilde p\times\tilde r$ is the adjoint operator, of
*The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, below this article in
this category.

**Proposition.** In the basis $(e_0,e_1,e_2,e_3)$ the adjoint is the block matrix
$\operatorname{ad}_{\tilde p}=\operatorname{diag}(0,C_{\mathbf p})$ on
$\mathbb{H}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})$, its square is
$\operatorname{diag}(0,C_{\mathbf p}^2)$, and its trace is zero.

*Proof.* The bracket vanishes on the centre, so the centre is the kernel and the first block vanishes;
on the vector subspace the adjoint is the cross product by $\mathbf p$, whose matrix is $C_{\mathbf p}$;
a cross-product matrix is traceless, being skew-symmetric.

## The Computation of the Form

**Theorem (the form).** For all $\tilde p,\tilde q$,

$$
\kappa(\tilde p,\tilde q)=\operatorname{Tr}\bigl(C_{\mathbf p}C_{\mathbf q}\bigr)=-2\,\mathbf p\cdot\mathbf q .
$$

In the basis the Gram matrix is $\operatorname{diag}(0,-2,-2,-2)$.

*Proof.* The adjoint product is $\operatorname{diag}(0,C_{\mathbf p}C_{\mathbf q})$ and the scalar
block is zero, so the trace is $\operatorname{Tr}(C_{\mathbf p}C_{\mathbf q})$. Writing
$C_{\mathbf p}\mathbf q=\mathbf p\times\mathbf q$ and using
$\operatorname{Tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=-\sum_{i,j}A_{ij}B_{ij}$ for skew-symmetric $A,B$, the
trace is minus the Frobenius pairing of $C_{\mathbf p}$ and $C_{\mathbf q}$, which is
$2\,\mathbf p\cdot\mathbf q$, so $\kappa=-2\,\mathbf p\cdot\mathbf q$.

## The Invariance and the Two Forms

**Proposition (invariance).** The Killing form is symmetric and invariant,

$$
\kappa(\tilde p\times\tilde q,\tilde r)+\kappa(\tilde q,\tilde p\times\tilde r)=0 ,
$$

and it is the form of the vector subspace alone: it does not see the scalar coordinates.

*Proof.* A Killing form is symmetric and invariant by the general theory of Lie algebras
(*Structure of Lie Algebras*); on the block it is read as $-2\,\mathbf p\cdot\mathbf q$, which is zero
whenever one of the arguments is central.

**Theorem (the invariant bilinear forms).** The space of invariant bilinear forms of $\mathfrak{g}$ is
two-dimensional, spanned by the Killing form $\kappa$ and the scalar-part form
$\varphi(\tilde p,\tilde q)=p_0q_0$. There is no nonzero **alternating** invariant form. The plain
form is the combination

$$
B=\varphi+\tfrac12\kappa,\qquad B(\tilde p,\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q ,
$$

and it is nondegenerate, of signature $(1,3)$.

*Proof.* An invariant form is determined by its values on the two components and by the invariance,
which forces the vanishing of the coupling between the centre and the derived algebra; on the simple
derived algebra the invariant forms are the multiples of the Killing form, and on the abelian centre
the one-dimensional scalar-part form is free. The Killing form is negative definite on the derived
algebra and zero on the centre, the scalar-part form is positive definite on the centre and zero on the
derived algebra, and there is no alternating source, the forms of a simple algebra being the multiples
of the Killing form, which is symmetric. The plain form is the displayed combination and its
signature is the inertia of $p_0q_0-\mathbf p\cdot\mathbf q$, one positive and three negative
directions.

## The Radical and the Definiteness

**Theorem.** The radical of the Killing form is the centre,

$$
\{\tilde p:\kappa(\tilde p,\tilde q)=0\ \text{for every }\tilde q\}=\mathbb{R}e_0 ,
$$

of real dimension one; the form is negative semidefinite, $\kappa(\tilde p,\tilde p)=-2|\mathbf p|^2\le0$,
with equality exactly on the centre; and it is negative definite on the derived algebra.

*Proof.* $\kappa(\tilde p,\tilde q)=-2\,\mathbf p\cdot\mathbf q$ vanishes for every $\tilde q$ exactly
when $\mathbf p=0$, which is the centre. The diagonal value is $-2|\mathbf p|^2$, non-positive and zero
only for $\mathbf p=0$.

## The Casimir Element

**Definition.** Let $h^{ij}$ be the inverse of the Gram matrix $\kappa(e_i,e_j)=-2\delta_{ij}$, that is
$h^{ij}=-\tfrac12\delta^{ij}$. The **Casimir element** of the block is

$$
C=\sum_{i,j}h^{ij}e_ie_j=-\tfrac12\bigl(e_1^2+e_2^2+e_3^2\bigr),
$$

an element of the universal enveloping algebra $\mathrm{U}(\mathfrak{g})$.

**Theorem (the eigenvalue).** The Casimir acts as the identity on the adjoint representation, that is
on the derived algebra $\mathrm{Vect}(\mathbb{H})$, as the scalar $\tfrac38$ on the two-dimensional
module of $\mathfrak{su}(2)$, and as $0$ on the centre.

*Proof.* On the derived algebra the adjoint is $\mathbf p\mapsto C_{\mathbf p}$, and
$C_{\mathbf p}^2=\mathbf p\mathbf p^{\mathsf T}-|\mathbf p|^2\mathrm{I}_3$ gives
$\sum_k C_{e_k}^2=-2\mathrm{I}_3$; hence
$C$ acts as $-\tfrac12\sum_k C_{e_k}^2=\mathrm{I}_3$. The two-dimensional module sends $e_k$ to $-\tfrac{i}{2}\sigma_k$,
and $C$ acts as $-\tfrac12\sum_k(-\tfrac{i}{2}\sigma_k)^2=\tfrac18\sum_k\sigma_k^2=\tfrac38\mathrm{I}_2$ because
the Pauli matrices satisfy $\sigma_k^2=\mathrm{I}_2$. The centre is annihilated.

**Remark (the Casimir and the two norms).** The eigenvalue $\tfrac38$ on the two-dimensional module is
the value the biquaternion analogue carries, and the identity on the adjoint is the value the trace
form realizes; the two readings are the two available values of the Casimir, and they do not conflict,
being read on different representations.

## The Cartan Criterion

**Proposition.** The Lie algebra $\mathfrak{g}$ is not semisimple, and the degeneracy of its Killing
form exhibits it: by Cartan's criterion an algebra is semisimple exactly when its Killing form is
nondegenerate, and here the form degenerates on the centre. The semisimple part of $\mathfrak{g}$, the
derived algebra, has the negative definite form, as a compact real form must.

*Proof.* The radical is the centre, of dimension one; the form is nondegenerate exactly on the derived
algebra, where it is the negative definite form of $\mathfrak{su}(2)$.

## The Comparison with the Biquaternion Blocks

| | the biquaternion antisymmetric plain algebra | the antisymmetric plain algebra of $\mathbb{H}$ |
|---|---|---|
| the form | $\kappa(\tilde P,\tilde Q)=-2\,\mathbf P\cdot\mathbf Q$, complex | $\kappa(\tilde p,\tilde q)=-2\,\mathbf p\cdot\mathbf q$, real |
| the Gram matrix | $\operatorname{diag}(0,-2,-2,-2)$ over $\mathbb{C}$ | $\operatorname{diag}(0,-2,-2,-2)$ over $\mathbb{R}$ |
| the definiteness | indefinite, six real dimensions | negative semidefinite, three negative directions |
| the radical | $\mathbb{C}_{\mathbb{B}}$, the centre | $\mathbb{R}_{\mathbb{H}}$, the centre |
| the family of invariant forms | the Killing form and the scalar-part form | the same two |

**Remark (the collapse of the indefiniteness).** Over $\mathbb{C}$ the form is complex-valued and its
realification is indefinite; over $\mathbb{R}$ it is real and negative semidefinite on three
directions, the compact form of the complex one. The biquaternion antisymmetric quaternionic block has
no Killing form at all, the Jacobi identity failing; its substitute, the invariant bilinear form, is
*The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* of the quaternion chapter, below
this article in this category, and it is **not** a Killing form. The comparison is recorded here and not
re-derived.

## Summary

The Killing form of the antisymmetric plain algebra is $\kappa(\tilde p,\tilde q)=\operatorname{Tr}(C_{\mathbf p}C_{\mathbf q})=-2\,\mathbf p\cdot\mathbf q$,
of Gram matrix $\operatorname{diag}(0,-2,-2,-2)$: the Euclidean form of the vector subspace in the
negative direction, with the scalar direction in its radical. It is symmetric and invariant, negative
semidefinite, and negative definite on the derived algebra, whose compact form it is. The space of
invariant bilinear forms is two-dimensional, spanned by the Killing form and the scalar-part form
$p_0q_0$, and the plain form is their combination $B=\varphi+\tfrac12\kappa$, nondegenerate of
signature $(1,3)$; there is no nonzero alternating invariant form. The Casimir element
$C=-\tfrac12(e_1^2+e_2^2+e_3^2)$ acts as the identity on the adjoint and as $\tfrac38$ on the
two-dimensional module. By Cartan's criterion the algebra is not semisimple, the radical being the
centre. Over $\mathbb{C}$ the same computation gives an indefinite form; the antisymmetric
quaternionic block has no Killing form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\kappa(\tilde p,\tilde q)=\operatorname{Tr}(\operatorname{ad}_{\tilde p}\operatorname{ad}_{\tilde q})$ | the Killing form |
| $-2\,\mathbf p\cdot\mathbf q$, Gram $\operatorname{diag}(0,-2,-2,-2)$ | the computation |
| $\mathbb{R}e_0$ | the radical, the centre |
| $\varphi(\tilde p,\tilde q)=p_0q_0$ | the scalar-part form, the second invariant form |
| $B=\varphi+\tfrac12\kappa$ | the plain form, nondegenerate of signature $(1,3)$ |
| $C=-\tfrac12(e_1^2+e_2^2+e_3^2)$ | the Casimir element |

## Further Reading

- *The Lie Algebra of the Antisymmetric Plain Algebra*, below this article in this category, for the centre, the derived algebra and the structure constants.
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, below this article in this category, for the adjoint representation and the derivation algebra.
- *The Specificities of the Antisymmetric Plain Algebra*, below this article in this category, for the isolation of the block and the folded element classes.
- *Structure of Lie Algebras*, for the Killing form, the radical, the Cartan criterion and the Casimir element.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, for the plain and the quaternion forms of the space.
