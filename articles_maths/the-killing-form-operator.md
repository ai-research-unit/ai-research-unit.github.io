
# __The Killing Form Operator__

## Introduction

The Killing form $\kappa(x,y)=\operatorname{tr}(\operatorname{ad}_x\operatorname{ad}_y)$ is a symmetric bilinear form on a finite-dimensional Lie algebra $\mathrm{G}$, and through its nondegeneracy it decides whether $\mathrm{G}$ is semisimple. The form also **defines operators**, and this article is the operator layer of that theory: the linear map $\kappa^{\flat}:\mathrm{G}\to\mathrm{G}^*$, $x\mapsto\kappa(x,-)$, called the **Killing form operator**, the invariance identity read as the statement that the operators $\operatorname{ad}_x$ are skew with respect to the form, the semisimplicity criterion read as the invertibility of $\kappa^{\flat}$, the Casimir operator and the Laplacian that the form produces, and the embedding of $\operatorname{ad}(\mathrm{G})$ into the operators preserving $\kappa$. The form itself, its symmetry, its radical, Cartan's criteria and the Levi decomposition are the subject of *Structure of Lie Algebras* and are cited, not restated; the Casimir operator is *The Casimir Operator*, and the derivations are *Derivations of a Lie Algebra*.

The base is a field $K$ of characteristic zero, as in the structure theory, and $\mathrm{G}$ is finite-dimensional over $K$. The Killing form is written $\kappa$, the operator it defines by $\kappa^{\flat}$, the adjoint operators by $\operatorname{ad}_x$, the dual by $\mathrm{G}^*$, the Casimir operator by $C$ and the Laplacian by $\Omega$. The article reasons with linear algebra over $K$ only: no length, no sign and no metric decomposition is formed from the form, whose kernel and nondegeneracy are the objects used.

## The Operator Defined by the Killing Form

### The Killing Form Operator

**Definition.** The **Killing form operator** is the $K$-linear map

$$
\kappa^{\flat}:\mathrm{G}\longrightarrow\mathrm{G}^*,\qquad \kappa^{\flat}(x)=\kappa(x,-),
$$

sending $x$ to the functional $y\mapsto\kappa(x,y)$. Its kernel is the **radical of the form**, $\ker\kappa^{\flat}=\{x:\kappa(x,y)=0\text{ for all }y\}=\mathrm{G}^{\perp}$.

**Proposition.** The operator $\kappa^{\flat}$ is linear, and it is injective exactly when $\kappa$ is nondegenerate; when it is injective it is an isomorphism because $\dim\mathrm{G}=\dim\mathrm{G}^*$.

**Proof.** Linearity is bilinearity; the kernel is the radical by definition, and injectivity of a linear map between spaces of equal finite dimension is bijectivity. $\square$

### Equivariance for the Adjoint and the Coadjoint Actions

**Proposition.** The operator $\kappa^{\flat}$ is a morphism of $\mathrm{G}$-modules for the adjoint action on $\mathrm{G}$ and the coadjoint action on $\mathrm{G}^*$:

$$
\kappa^{\flat}(\operatorname{ad}_x y)=-\operatorname{ad}_x^{*}\,\kappa^{\flat}(y),
$$

where $\operatorname{ad}_x^{*}$ is the transpose of $\operatorname{ad}_x$.

**Proof.** Evaluate both sides on $z$: the left is $\kappa([x,y],z)$, the right is $-\kappa(y,[x,z])$, and the invariance $\kappa([x,y],z)=\kappa(x,[y,z])$ gives their equality. $\square$

**Corollary.** The kernel and the image of $\kappa^{\flat}$ are stable, respectively, under the adjoint and the coadjoint actions; in particular the radical is an ideal of $\mathrm{G}$, which is the statement recorded in *Structure of Lie Algebras*.

## Invariance as an Operator Identity

**Theorem.** For every $x\in\mathrm{G}$ the operator $\operatorname{ad}_x$ is skew with respect to $\kappa$:

$$
\kappa(\operatorname{ad}_x y,z)+\kappa(y,\operatorname{ad}_x z)=0\qquad\text{for all }y,z .
$$

Equivalently, the following square commutes with a sign:

$$
\kappa^{\flat}\circ\operatorname{ad}_x=-\operatorname{ad}_x^{*}\circ\kappa^{\flat}.
$$

**Proof.** The invariance identity gives $\kappa([x,y],z)=\kappa(x,[y,z])$ and $\kappa(y,[x,z])=\kappa([y,x],z)=-\kappa([x,y],z)$; adding, the two terms cancel. The commuting-square form is the same identity read through the definition of $\kappa^{\flat}$. $\square$

**Corollary.** The adjoint representation lands in the operators preserving the form: the image of $\operatorname{ad}:\mathrm{G}\to\operatorname{End}_K(\mathrm{G})$ lies in the Lie subalgebra of the operators $T$ with $\kappa(Ty,z)+\kappa(y,Tz)=0$. When $\kappa$ is nondegenerate and written in a basis, the matrices of the $\operatorname{ad}_x$ are antisymmetric with respect to the coefficient matrix of $\kappa$.

**Remark.** The corollary names the orthogonal algebra of the form; the orthogonal Lie algebras, their classification and their representation theory belong to the symmetric bilinear algebras of this Part and are not used here. Only the operator statement above is used, and no metric reading is taken.

## The Semisimplicity Criterion as an Operator Statement

**Theorem.** Let $K$ have characteristic zero. Then $\mathrm{G}$ is semisimple if and only if the Killing form operator $\kappa^{\flat}$ is injective; equivalently, the radical of the form is zero.

**Proof.** Cartan's criterion for semisimplicity, recorded in *Structure of Lie Algebras*, states that $\mathrm{G}$ is semisimple if and only if $\kappa$ is nondegenerate; by the first proposition nondegeneracy is the injectivity of $\kappa^{\flat}$. $\square$

**Corollary.** For semisimple $\mathrm{G}$ the map $\kappa^{\flat}:\mathrm{G}\to\mathrm{G}^*$ is an isomorphism of $\mathrm{G}$-modules with the actions of the previous section, so the adjoint and the coadjoint representations are equivalent; the inverse $(\kappa^{\flat})^{-1}:\mathrm{G}^*\to\mathrm{G}$ transfers the form to the dual and is used to build the Casimir operator.

**Proposition.** The radical of the form is stable under derivations: if $D$ is a derivation of $\mathrm{G}$ then $\kappa(Dx,y)+\kappa(x,Dy)=0$, so $D$ preserves $\kappa$, and $\kappa^{\flat}\circ D=-D^{*}\circ\kappa^{\flat}$; for $\mathrm{G}$ semisimple every derivation is inner, and the statement reduces to the skewness of $\operatorname{ad}_x$.

**Proof.** The identity $\operatorname{tr}([D,\operatorname{ad}_x]\operatorname{ad}_y)+\operatorname{tr}(\operatorname{ad}_x[D,\operatorname{ad}_y])=0$, valid for any derivation because $[D,\operatorname{ad}_x]=\operatorname{ad}_{Dx}$, gives the invariance; the inner case is the previous theorem. $\square$

## The Casimir Operator and the Laplacian

**Definition.** Let $\mathrm{G}$ be semisimple, let $x_1,\dots,x_m$ be a basis and let $x^1,\dots,x^m$ be the basis determined by $\kappa(x_i,x^j)=\delta_i^j$. The **Casimir operator** is

$$
C=\sum_{i=1}^{m}x_ix^i\in U(\mathrm{G}),
$$

and its image in $\operatorname{End}_K(V)$ under a representation $\rho$ is the **Laplacian of the representation**, $\Omega=\sum_i\rho(x_i)\rho(x^i)$.

**Theorem.** The element $C$ is independent of the choice of basis, it lies in the centre of $U(\mathrm{G})$, and the Laplacian commutes with the image of the representation; on an irreducible finite-dimensional representation the Laplacian is a scalar.

**Proof.** A change of basis changes the two bases by inverse matrices, whose contributions cancel in the sum; centrality and the commuting property, with the scalar statement, are established in *The Casimir Operator*. $\square$

**Remark.** The operator $\kappa^{\flat}$ is what makes the sum basis-free: it identifies $\mathrm{G}$ with $\mathrm{G}^*$, so a sum over a basis of $\mathrm{G}$ and the dual basis is an invariant element. The Laplacian is the operator form of the Casimir element and is used in *The Casimir Operator* and in *Representations of Lie Algebras*.

## Worked Case: $\mathrm{sl}(2,K)$

Let $\mathrm{G}=\mathrm{sl}(2,K)$ with basis $e,h,f$ and the bracket $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$. The Killing form is

$$
\kappa=\begin{pmatrix}0&0&4\\0&8&0\\4&0&0\end{pmatrix}
$$

in the basis $(e,h,f)$, nondegenerate; the operator $\kappa^{\flat}$ is therefore invertible, and the dual basis is $(f/4,\ h/8,\ e/4)$. The Casimir operator is

$$
C=\tfrac14 ef+\tfrac18 h^2+\tfrac14 fe=\tfrac14\left(ef+fe+\tfrac12h^2\right),
$$

which acts on the irreducible representation of highest weight $n$ by the scalar $\tfrac18 n(n+2)$, the value recorded in *The Casimir Operator*.

**Verified.** The matrix of $\kappa$ was recomputed from the brackets by hand and by exact elimination over $\mathbb{Q}$; the skewness $\kappa(\operatorname{ad}_x y,z)+\kappa(y,\operatorname{ad}_x z)=0$ was checked on the three basis elements and the pairing of the Casimir eigenvalue with the dimension of the representation was checked against the data of *The Casimir Operator*.

## Summary

The Killing form defines the **Killing form operator** $\kappa^{\flat}:\mathrm{G}\to\mathrm{G}^*$, $x\mapsto\kappa(x,-)$, whose kernel is the radical of the form. It is a morphism of $\mathrm{G}$-modules with a sign, $\kappa^{\flat}(\operatorname{ad}_x y)=-\operatorname{ad}_x^{*}\kappa^{\flat}(y)$, and this is the invariance of $\kappa$; equivalently every $\operatorname{ad}_x$ is skew for $\kappa$, $\kappa(\operatorname{ad}_x y,z)+\kappa(y,\operatorname{ad}_x z)=0$, so the adjoint representation lands in the operators preserving the form, and the derivations preserve $\kappa$ as well. By Cartan's criterion, recorded in *Structure of Lie Algebras*, the algebra is semisimple exactly when $\kappa^{\flat}$ is injective, and then $\kappa^{\flat}$ is an isomorphism of $\mathrm{G}$-modules between the adjoint and the coadjoint representations. The isomorphism makes the Casimir operator $C=\sum x_ix^i$ and the Laplacian $\Omega=\sum\rho(x_i)\rho(x^i)$ basis-free invariant operators, central in $U(\mathrm{G})$ and scalar on irreducibles, as in *The Casimir Operator*. For $\mathrm{sl}(2,K)$ the form is nondegenerate with matrix displayed above, and the Laplacian acts on the representation of highest weight $n$ by $\tfrac12 n(n+2)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic zero |
| $\mathrm{G}$ | a finite-dimensional Lie algebra over $K$ |
| $\kappa(x,y)=\operatorname{tr}(\operatorname{ad}_x\operatorname{ad}_y)$ | the Killing form |
| $\kappa^{\flat}:\mathrm{G}\to\mathrm{G}^*$ | the Killing form operator $x\mapsto\kappa(x,-)$ |
| $\operatorname{ad}_x$, $\operatorname{ad}_x^{*}$ | the adjoint operator and its transpose |
| $\mathrm{G}^{\perp}=\ker\kappa^{\flat}$ | the radical of the form |
| $x_i$, $x^i$ | a basis and the $\kappa$-dual basis |
| $C=\sum_i x_ix^i$ | the Casimir operator (owned by *The Casimir Operator*) |
| $\Omega=\sum_i\rho(x_i)\rho(x^i)$ | the Laplacian of a representation |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Killing form, its invariance and Cartan's criteria.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for the semisimplicity criterion and the Casimir operator.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1–3 (Springer, 1989), for the invariance of the Killing form and the structure theory.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 2001), for the Casimir element and its eigenvalues.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for the invariant forms and the operators they define.
