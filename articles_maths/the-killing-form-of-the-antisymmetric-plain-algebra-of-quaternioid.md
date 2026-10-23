# __The Killing Form of the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ is the real Lie algebra
$\mathfrak{g}=(\mathbb{H},\times)$ with the cross product
$\tilde q_1\times\tilde q_2=\vec q_1\times\vec q_2$ of *The Lie Algebra of the Antisymmetric Plain
Algebra*, below this article in this category. This article computes its Killing form, identifies the
space of invariant bilinear forms, exhibits the Casimir element and compares the form with the

The result is simple and rigid: the form is the Euclidean form of the vector subspace up to the factor
$-2$, with the scalar direction in its radical, so it is negative semidefinite, negative definite on
the derived algebra, and its radical is the centre. The space of invariant bilinear forms is the plane
spanned by the Killing form and the scalar-part form $\varphi(\tilde q_1,\tilde q_2)=q_{1t}q_{2t}$, and there is
no nonzero alternating invariant form.

**This is not the algebra $\mathbb{H}$.** The form belongs to the Lie bracket of the vector parts, not
to the associative multiplication. Throughout, the natural sign ${}^{\natural}$ is the quaternion
conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star
coincides with the natural sign and gives nothing new.

The Lie algebra, its centre and its derived algebra are *The Lie Algebra of the Antisymmetric Plain
Algebra*; the adjoint operators and the derivations are *The Adjoint Operators and the Derivations of
the Antisymmetric Plain Algebra*, both below this article in this category.
counterparts are *The Killing Form of the Antisymmetric Plain Algebra* and *Norm and Invertibility in

## The Adjoint Representation and the Killing Form

**Definition.** The **Killing form** of the Lie algebra $\mathfrak{g}=(\mathbb{H},\times)$ is

$$
\kappa(\tilde q_1,\tilde q_2)=\operatorname{Tr}\bigl(\operatorname{ad}_{\tilde q_1}\operatorname{ad}_{\tilde q_2}\bigr),
$$

where $\operatorname{ad}_{\tilde q_1}\tilde q_2=\tilde q_1\times\tilde q_2$ is the adjoint operator, of
*The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, below this article in
this category.

**Proposition.** In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the adjoint is the block matrix
$\operatorname{ad}_{\tilde q}=\operatorname{diag}(0,C_{\vec q})$ on
$\mathbb{H}=\mathbb{R}e_t\oplus\mathrm{Vect}(\mathbb{H})$, its square is
$\operatorname{diag}(0,C_{\vec q}^2)$, and its trace is zero.

*Proof.* The bracket vanishes on the centre, so the centre is the kernel and the first block vanishes;
on the vector subspace the adjoint is the cross product by $\vec q$, whose matrix is $C_{\vec q}$;
a cross-product matrix is traceless, being skew-symmetric.

## The Computation of the Form

**Theorem (the form).** For all $\tilde q_1,\tilde q_2$,

$$
\boxed{\;\kappa(\tilde q_1,\tilde q_2)=\operatorname{Tr}\bigl(C_{\vec q_1}C_{\vec q_2}\bigr)=-2\,\vec q_1\cdot\vec q_2\;}.
$$

In the basis the Gram matrix is $\operatorname{diag}(0,-2,-2,-2)$.

*Proof.* The adjoint product is $\operatorname{diag}(0,C_{\vec q_1}C_{\vec q_2})$ and the scalar
block is zero, so the trace is $\operatorname{Tr}(C_{\vec q_1}C_{\vec q_2})$. Writing
$C_{\vec q_1}\vec q_2=\vec q_1\times\vec q_2$ and using
$\operatorname{Tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=-\sum_{i,j}A_{ij}B_{ij}$ for skew-symmetric $A,B$, the
trace is minus the Frobenius pairing of $C_{\vec q_1}$ and $C_{\vec q_2}$, which is
$2\,\vec q_1\cdot\vec q_2$, so $\kappa=-2\,\vec q_1\cdot\vec q_2$.

## The Invariance and the Two Forms

**Proposition (invariance).** The Killing form is symmetric and invariant,

$$
\boxed{\;\kappa(\tilde q_1\times\tilde q_2,\tilde q_3)+\kappa(\tilde q_2,\tilde q_1\times\tilde q_3)=0\;},
$$

and it is the form of the vector subspace alone: it does not see the scalar coordinates.

*Proof.* A Killing form is symmetric and invariant by the general theory of Lie algebras
(*Structure of Lie Algebras*); on the block it is read as $-2\,\vec q_1\cdot\vec q_2$, which is zero
whenever one of the arguments is central.

**Theorem (the invariant bilinear forms).** The space of invariant bilinear forms of $\mathfrak{g}$ is
two-dimensional, spanned by the Killing form $\kappa$ and the scalar-part form
$\varphi(\tilde q_1,\tilde q_2)=q_{1t}q_{2t}$. There is no nonzero **alternating** invariant form. The plain
form is the combination

$$
\boxed{\;B=\varphi+\tfrac12\kappa,\qquad \langle\tilde q_1,\tilde q_2\rangle=q_{1t}q_{2t}-\vec q_1\cdot\vec q_2\;},
$$

and it is nondegenerate, of signature $(1,3)$.

*Proof.* An invariant form is determined by its values on the two components and by the invariance,
which forces the vanishing of the coupling between the centre and the derived algebra; on the simple
derived algebra the invariant forms are the multiples of the Killing form, and on the abelian centre
the one-dimensional scalar-part form is free. The Killing form is negative definite on the derived
algebra and zero on the centre, the scalar-part form is positive definite on the centre and zero on the
derived algebra, and there is no alternating source, the forms of a simple algebra being the multiples
of the Killing form, which is symmetric. The plain form is the displayed combination and its
signature is the inertia of $q_{1t}q_{2t}-\vec q_1\cdot\vec q_2$, one positive and three negative
directions.

## The Radical and the Definiteness

**Theorem.** The radical of the Killing form is the centre,

$$
\boxed{\;\{\tilde q_1:\kappa(\tilde q_1,\tilde q_2)=0\ \text{for every }\tilde q_2\}=\mathbb{R}e_t\;},
$$

of real dimension one; the form is negative semidefinite, $\kappa(\tilde q,\tilde q)=-2|\vec q|^2\le0$,
with equality exactly on the centre; and it is negative definite on the derived algebra.

*Proof.* $\kappa(\tilde q_1,\tilde q_2)=-2\,\vec q_1\cdot\vec q_2$ vanishes for every $\tilde q_2$ exactly
when $\vec q_1=0$, which is the centre. The diagonal value is $-2|\vec q|^2$, non-positive and zero
only for $\vec q=0$.

## The Casimir Element

**Definition.** Let $h^{\mu\nu}$ be the inverse of the Gram matrix $\kappa(\vec e_\mu,\vec e_\nu)=-2\delta_{\mu\nu}$, that is
$h^{\mu\nu}=-\tfrac12\delta^{\mu\nu}$. The **Casimir element** of the block is

$$
\Omega=\sum_{\mu,\nu}h^{\mu\nu}\vec e_\mu \vec e_\nu=-\tfrac12\bigl(\vec e_x^2+\vec e_y^2+\vec e_z^2\bigr),
$$

an element of the universal enveloping algebra $\mathrm{U}(\mathfrak{g})$.

**Theorem (the eigenvalue).** The Casimir acts as the identity on the adjoint representation, that is
on the derived algebra $\mathrm{Vect}(\mathbb{H})$, as the scalar $\tfrac38$ on the two-dimensional
module of $\mathfrak{su}(2)$, and as $0$ on the centre.

*Proof.* On the derived algebra the adjoint is $\vec q\mapsto C_{\vec q}$, and
$C_{\vec q}^2=\vec q\vec q^{\mathsf T}-|\vec q|^2\mathrm{I}_3$ gives
$\sum_k C_{\vec e_k}^2=-2\mathrm{I}_3$; hence
$\Omega$ acts as $-\tfrac12\sum_k C_{\vec e_k}^2=\mathrm{I}_3$. The two-dimensional module sends $\vec e_k$ to $-\tfrac{i}{2}\sigma_k$,
and $\Omega$ acts as $-\tfrac12\sum_k(-\tfrac{i}{2}\sigma_k)^2=\tfrac18\sum_k\sigma_k^2=\tfrac38\mathrm{I}_2$ because
the Pauli matrices satisfy $\sigma_k^2=\mathrm{I}_2$. The centre is annihilated.

**Remark (the Casimir and the two norms).** The eigenvalue $\tfrac38$ on the two-dimensional module is
form realizes; the two readings are the two available values of the Casimir, and they do not conflict,
being read on different representations.

## The Cartan Criterion

**Proposition.** The Lie algebra $\mathfrak{g}$ is not semisimple, and the degeneracy of its Killing
form exhibits it: by Cartan's criterion an algebra is semisimple exactly when its Killing form is
nondegenerate, and here the form degenerates on the centre. The semisimple part of $\mathfrak{g}$, the
derived algebra, has the negative definite form, as a compact real form must.

*Proof.* The radical is the centre, of dimension one; the form is nondegenerate exactly on the derived
algebra, where it is the negative definite form of $\mathfrak{su}(2)$.

## Summary

The Killing form of the antisymmetric plain algebra is $\kappa(\tilde q_1,\tilde q_2)=\operatorname{Tr}(C_{\vec q_1}C_{\vec q_2})=-2\,\vec q_1\cdot\vec q_2$,
of Gram matrix $\operatorname{diag}(0,-2,-2,-2)$: the Euclidean form of the vector subspace in the
negative direction, with the scalar direction in its radical. It is symmetric and invariant, negative
semidefinite, and negative definite on the derived algebra, whose compact form it is. The space of
invariant bilinear forms is two-dimensional, spanned by the Killing form and the scalar-part form
$q_{1t}q_{2t}$, and the plain form is their combination $\langle\cdot,\cdot\rangle=\varphi+\tfrac12\kappa$, nondegenerate of
signature $(1,3)$; there is no nonzero alternating invariant form. The Casimir element
$\Omega=-\tfrac12(\vec e_x^2+\vec e_y^2+\vec e_z^2)$ acts as the identity on the adjoint and as $\tfrac38$ on the
two-dimensional module. By Cartan's criterion the algebra is not semisimple, the radical being the
centre. Over $\mathbb{C}$ the same computation gives an indefinite form; the antisymmetric
quaternionic block has no Killing form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\kappa(\tilde q_1,\tilde q_2)=\operatorname{Tr}(\operatorname{ad}_{\tilde q_1}\operatorname{ad}_{\tilde q_2})$ | the Killing form |
| $-2\,\vec q_1\cdot\vec q_2$, Gram $\operatorname{diag}(0,-2,-2,-2)$ | the computation |
| $\mathbb{R}e_t$ | the radical, the centre |
| $\varphi(\tilde q_1,\tilde q_2)=q_{1t}q_{2t}$ | the scalar-part form, the second invariant form |
| $\langle\cdot,\cdot\rangle=\varphi+\tfrac12\kappa$ | the plain form, nondegenerate of signature $(1,3)$ |
| $\Omega=-\tfrac12(\vec e_x^2+\vec e_y^2+\vec e_z^2)$ | the Casimir element |

## Further Reading

- [The Lie Algebra of the Antisymmetric Plain Algebra](the-lie-algebra-of-the-antisymmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the centre, the derived algebra and the structure constants.
- [The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra](the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the adjoint representation and the derivation algebra.
- [The Specificities of the Antisymmetric Plain Algebra](the-specificities-of-the-antisymmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the isolation of the block and the folded element classes.
- [Structure of Lie Algebras](structure-of-lie-algebras.html), for the Killing form, the radical, the Cartan criterion and the Casimir element.
- [The 2 Forms over the Quaternioid $\mathbb{R}$ Space](the-2-forms-over-the-quaternioid-r-space.html), for the plain and the quaternion forms of the space.
