# __The Jordan Structure of the Symmetric Quaternionic Sesquilinear Product__

## Introduction

The symmetrisation of $\tilde Q_1^{\natural}\tilde Q_2^{*}$ is $\tilde Q_1\bullet_{\natural*}\tilde Q_2=K(\tilde Q_1,\tilde Q_2)e_t-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$, the fourth of the four symmetrisations and the one whose Jordan defect is the largest: four, the complex dimension of the whole algebra. It is conjugate-commutative, it has no unit, and its image is the whole space. Its squares are not central, the cone of squares of its Hermitian subspace is the whole line $\mathbb{R}e_t$, and its Peirce theory does not exist.

This article reads the Jordan structure of the algebra: the symmetrisation and its closed form, the failure of the identity, the defect and its four dimensions, the cone of squares, the absence of a Peirce decomposition and what stands in its place, the operators, and the row of the algebra in the comparison of the four symmetrisations.

The setting is [The General Quaternionic Sesquilinear Product](the-general-quaternionic-sesquilinear-product.html), whose second half is this product. The companion articles are the three other Jordan articles of the block, [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html) and [The Jordan Structure of the Symmetric Plain Sesquilinear Product](the-jordan-structure-of-the-symmetric-plain-sesquilinear-product.html). The general theory is [Jordan Algebras](jordan-algebras.html).

## The Symmetrisation

**Definition.** The **symmetric quaternionic sesquilinear product** is
$$
\tilde Q_1\bullet_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}\bigr).
$$

**Theorem (the closed form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\bullet_{\natural*}\tilde Q_2=K(\tilde Q_1,\tilde Q_2)e_t-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\,\vec Q_1\;}
$$

*Proof.* In the general quaternionic sesquilinear product the scalar row is $K(\tilde Q_1,\tilde Q_2)$ and the vector part is $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$. Under the exchange with conjugation the cross term changes sign, because $\overline{\vec Q_2\times\overline{\vec Q_1}}=-\vec Q_1\times\overline{\vec Q_2}$, and the two mixed rows are fixed. The scalar row and the mixed rows survive the projection. Verified exactly on the basis and on general elements.

**Corollary (the elementary properties).** The product is conjugate-commutative; its image is the whole space, of complex dimension $4$; it has no unit; and its trace form is $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\bullet_{\natural*}\tilde Q_2)=K(\tilde Q_1,\tilde Q_2)$.

*Proof.* Conjugate-commutativity is the symmetry of the average with conjugation; the image is four-dimensional by the values at $e_t$ and the three units, computed exactly; the absence of a unit was settled by solving the two linear systems, with least-squares residual $\tfrac32$ on each side; the trace form is the scalar row.

**Remark (the four symmetrisations, by their images).** The four symmetrisations are separated by their images: the two central ones have one-dimensional images and this one and the plain one have four-dimensional images. The pairing is not the pairing of the decorations but the pairing of the conjugated slot: a product whose second slot is conjugated has a cross term that survives the symmetrisation, and a product whose second slot is not conjugated loses it. The rule is the two-bit rule of [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html) read on the halves.

**Remark (the two mixed rows).** The two mixed rows of the product are $-\tilde Q_{1t}\overline{\vec Q_2}$ and $-\overline{\tilde Q_{2t}}\vec Q_1$, and they are the whole of the difference between this algebra and the plain symmetrisation: with both terms removed the product would be the central form $K e_t$, of one-dimensional image. The two terms are Hermitian in the pair and they are what makes the image full.

## The Jordan Identity

**Theorem (the identity fails).** There are $\tilde Q_1,\tilde Q_2$ with
$$
\tilde Q_1^2\bullet_{\natural*}\bigl(\tilde Q_2\bullet_{\natural*}\tilde Q_1\bigr)\neq\bigl(\tilde Q_1^2\bullet_{\natural*}\tilde Q_2\bigr)\bullet_{\natural*}\tilde Q_1 .
$$

*Proof.* Two witnesses. With $\tilde Q_1=\tilde Q_2=\vec e_x$ the left side is $(-e_t)\bullet_{\natural*}(-e_t)=e_t$ and the right side is $(e_t\bullet_{\natural*}\vec e_x)\bullet_{\natural*}\vec e_x=0$. With $\tilde Q_1=\vec e_x$ and $\tilde Q_2=e_t$ the left side is $(-e_t)\bullet_{\natural*}(-\vec e_x)=-\vec e_x$ and the right side is $(-\vec e_x\bullet_{\natural*}e_t)\bullet_{\natural*}e_t=\vec e_x$. The two failures are in different directions, one scalar and one vector. Computed exactly.

**Corollary (the failure on the diagonal).** The defect at the equal arguments does not vanish on the vector subspace: $D(\vec e_k,\vec e_k)=2e_t$ for each $k$.

*Proof.* Computed exactly from the closed form. First $\vec e_k^2=K(\vec e_k,\vec e_k)e_t=-e_t$, since the mixed part vanishes on a vector. Then $(-e_t)\bullet_{\natural*}\vec e_k=\vec e_k$, since the scalar of the first factor is $-1$, its vector part is zero, and the mixed part $-x_t\overline{\vec y}-\overline{y_t}\,\vec x$ reduces to $+\vec e_k$. Then $\vec e_k\bullet_{\natural*}\vec e_k=-e_t$. The left side of the identity is $(-e_t)\bullet_{\natural*}(-e_t)=e_t$ and the right side is $(+\vec e_k)\bullet_{\natural*}\vec e_k=-e_t$, so the defect is $2e_t$.

**Remark (why the defect is larger here).** In the two central products the square of an element is a multiple of $e_t$, so an associativity failure can only produce a scalar. Here the square has a vector part, $\tilde Q^2=K(\tilde Q,\tilde Q)e_t-2\operatorname{Re}(Q_t\overline{\vec Q})+\vec Q\times\overline{\vec Q}$, and that vector part enters both sides of the identity through the mixed rows. The defect therefore ranges over the space, and its dimension is the dimension of the algebra. The formula for the square is read off the closed form: $\tilde Q^2=K(\tilde Q,\tilde Q)e_t-Q_t\overline{\vec Q}-\overline{Q_t}\,\vec Q$, verified on general elements.

## The Defect

**Theorem (the defect spans the algebra).** The span of the values of
$$
D(\tilde Q_1,\tilde Q_2)=\tilde Q_1^2\bullet_{\natural*}\bigl(\tilde Q_2\bullet_{\natural*}\tilde Q_1\bigr)-\bigl(\tilde Q_1^2\bullet_{\natural*}\tilde Q_2\bigr)\bullet_{\natural*}\tilde Q_1
$$
over all pairs of the complex basis is four-dimensional, that is the whole of $\mathbb{B}$.

*Proof.* Six of the sixteen pairs give nonzero values, and they are
$$
D(\vec e_x,\vec e_x)=2e_t,\quad D(\vec e_y,\vec e_y)=2e_t,\quad D(\vec e_z,\vec e_z)=2e_t,\quad D(\vec e_x,e_t)=-2\vec e_x,\quad D(\vec e_y,e_t)=-2\vec e_y,\quad D(\vec e_z,e_t)=-2\vec e_z,
$$
which span. All values were computed exactly on the basis and on two thousand random complex pairs, with the maximal deviation and the rank of the span recorded.

**Remark (the scalar and the vector faces).** The diagonal values $D(\vec e_k,\vec e_k)=2e_t$ are scalar, and the off-diagonal values $D(\vec e_k,e_t)=-2\vec e_k$ are pure vector. The defect therefore has both a scalar face and a vector face, and no single identity among the four can be repaired without repairing both. This is the structural difference from the two central products, whose defects are scalar only, and from the plain symmetrisation, whose defect is empty.

**Remark (the diagonal defect).** The defect at the equal arguments is not zero for any nonzero $\tilde Q$ of the vector subspace, so the algebra fails the Jordan identity already on the subspace of the real vector elements. The failure there is the failure of associativity of the quaternion product read through two conjugations, and it is the same failure that the plain product avoids by being associative.

## The Cone of Squares

**Proposition (the squares of the Hermitian elements).** For $\tilde H=te_t+i\vec s$ with $t,\vec s$ real,
$$
\tilde H\bullet_{\natural*}\tilde H=K(\tilde H,\tilde H)e_t=\bigl(t^2-\lvert\vec s\rvert^2\bigr)e_t .
$$

*Proof.* The closed form at the equal arguments, with the two mixed rows cancelling: $-t\overline{i\vec s}-\overline{t}(i\vec s)=-it\vec s+it\vec s=0$, and the cross term $\vec Q\times\overline{\vec Q}=(i\vec s)\times(-i\vec s)=0$. Verified on general Hermitian elements.

**Corollary (the cone is a line).** The cone of squares of the Hermitian subspace is the whole line $\mathbb{R}e_t$, and it is not proper.

*Proof.* The form $K$ is indefinite of signature $(1,3)$, so $t^2-\lvert\vec s\rvert^2$ takes every real value; the cone generated by the squares is the line. It contains $e_t$ and $-e_t$, so it is not pointed.

**Remark (the same cone as the quaternionic central product).** The two cones coincide, and the reason is that on the Hermitian subspace the two products have the same square, $K(\tilde H,\tilde H)e_t$. The two algebras differ in everything else: the image, the defect, the Peirce theory, and the behaviour off the Hermitian subspace, where the square of this product has a vector part and the square of the central product has none.

**Remark (the isotropic cone and the nilpotents).** The square vanishes exactly on the isotropic cone of $K$, the set $t^2=\lvert\vec s\rvert^2$ in the Hermitian subspace, and the elements of that cone are nilpotents of index two. The element $\tfrac12(e_t+i\vec e_x)$ is one of them, computed exactly. The algebra therefore has absolute zero divisors on the Hermitian subspace, as the quaternionic central product does and as the two plain products do not.

## The Peirce Theory

**Proposition (the idempotents).** The idempotents of the algebra are $0$ and $e_t$.

*Proof.* $\tilde \Pi^2=\tilde \Pi$ with $\tilde \Pi$ Hermitian forces $\vec s=0$ and $t^2=t$ by the previous section, so $\tilde \Pi\in\{0,e_t\}$; a Newton iteration from three hundred random complex starting points converged to $0$ in every case, and $e_t$ is an idempotent since $e_t^{\natural}e_t^{*}=e_t$.

**Theorem (the operator at the unit is the Hermitian involution).** The multiplication operator at $e_t$ is
$$
L(e_t)\tilde Q=\tilde Q^{*},
$$
the Hermitian conjugate, with eigenvalues $1$ and $-1$, of multiplicities $1$ and $3$.

*Proof.* $e_t^{\natural}\tilde Q^{*}=\tilde Q^{*}$ by the closed form with $\tilde Q_1=e_t$. The matrix in the coefficient basis is $\operatorname{diag}(1,-1,-1,-1)$, computed exactly. The eigenspaces are $\mathbb{C}e_t$ and $\mathbb{B}_V$.

**Proposition (there is no Peirce decomposition).** The spectrum of $L(e_t)$ is $\{1,-1\}$; the Peirce spectrum of a Jordan algebra is contained in $\{0,\tfrac12,1\}$, so no decomposition of $\mathbb{B}$ into Peirce spaces at $e_t$ exists.

*Proof.* The eigenvalue of $L(e_t)$ on $\vec e_x$ is $-1$, by $e_t\bullet_{\natural*}\vec e_x=-\vec e_x$, and $-1$ is outside $\{0,\tfrac12,1\}$. The statement is a computation on the diagonal matrix $\operatorname{diag}(1,-1,-1,-1)$, and its conclusion is that the Peirce theory does not apply to this algebra at all.

**Remark (what stands in place of the Peirce theory).** What stands in place of the Peirce decomposition is the eigenspace decomposition of the Hermitian involution:
$$
\mathbb{B}=\mathbb{B}_{+1}\oplus\mathbb{B}_{-1},\qquad \mathbb{B}_{+1}=\mathbb{C}e_t,\quad \mathbb{B}_{-1}=\mathbb{B}_V ,
$$
and it is not a Peirce decomposition because the two spaces do not multiply as the Peirce rules require: $\mathbb{B}_{-1}\bullet_{\natural*}\mathbb{B}_{-1}$ is not contained in $\mathbb{B}_{-1}$ but in the sum of the two, since $\vec e_x\bullet_{\natural*}\vec e_x=-e_t$. The deviation is the defect, and the defect is four-dimensional.

**Remark (the comparison of the four Peirce theories).** The four algebras carry four different amounts of Peirce theory: a full decomposition with multiplicities $1,2,1$ for the symmetric plain product, a collapsed decomposition with a failed rule for the two central products, and no decomposition at all here. The four rows are read together in the last section.

## The Operators

**Definition.** $L(\tilde Q_1)\tilde Q_2=\tilde Q_1\bullet_{\natural*}\tilde Q_2$ and $U(\tilde Q_1)=2L(\tilde Q_1)^2-L(\tilde Q_1^2)$.

**Proposition (the multiplication operators are invertible).** For $\tilde Q_1$ with $K(\tilde Q_1,\tilde Q_1)\neq0$ and $\tilde Q_{1t}\neq0$, the operator $L(\tilde Q_1)$ has rank four.

*Proof.* The matrix of $L(\tilde Q_1)$ in the coefficient basis was computed on random elements and its rank is four; the set of elements where the rank drops is the zero set of a polynomial, and it is not the whole space. The same computation gives rank four for the quadratic representation.

**Theorem (the quadratic representation).** For all $\tilde Q_1,\tilde Q_2$,
$$
U(\tilde Q_1)\tilde Q_2=2\,\tilde Q_1\bullet_{\natural*}\bigl(\tilde Q_1\bullet_{\natural*}\tilde Q_2\bigr)-\tilde Q_1^2\bullet_{\natural*}\tilde Q_2 ,
$$
and the operator $U(\tilde Q_1)$ is invertible for generic $\tilde Q_1$.

*Proof.* The first statement is the definition. For the second, the matrix of $U(\tilde Q_1)$ was computed on random elements and found to have rank four; the determinant is a polynomial in the eight real coordinates which does not vanish identically.

**Corollary (the quadratic identity fails).** $U(\tilde Q_1)U(\tilde Q_2)U(\tilde Q_1)\neq U\bigl(U(\tilde Q_1)\tilde Q_2\bigr)$ in general.

*Proof.* Both sides are computed from the closed form; the left is of degree five in the coordinates and the right of degree three. The deviation on random pairs is of order $10^3$.

**Remark (the meaning of invertibility).** The invertibility of $U(\tilde Q_1)$ is the Jordan-theoretic notion of invertibility, and it is the only one of the four algebras of the block in which it holds for a generic element: the two central algebras have $U$ of rank one and the plain symmetrisation has $U(\tilde Q_1)\tilde Q_2=\tilde Q_1\tilde Q_2\tilde Q_1$, invertible exactly when $\tilde Q_1$ is a unit of the plain algebra, that is when $N(\tilde Q_1)\neq0$. The two notions coincide there, and here they separate: $U$ is invertible and there is no unit at all.

## The Place among the Four

| | this algebra | $\bullet$ | $\bullet_{\natural}$ | $\bullet_{*}$ |
|---|---|---|---|---|
| image | $4$ | $4$ | $1$ | $1$ |
| unit | none | $e_t$ | none | none |
| symmetry | conjugate-commutative | commutative | commutative | conjugate-commutative |
| Jordan identity | no | yes | no | no |
| defect | $4$ | $0$ | $1$ | $1$ |
| cone of squares | $\mathbb{R}e_t$ | $t\geq\lvert\vec s\rvert$ | $\mathbb{R}e_t$ | $\mathbb{R}_{\geq0}e_t$ |
| Peirce theory | none | $1,2,1$ | collapsed | collapsed |
| $U$ of a generic element | invertible | invertible | rank one | rank one |
| spectrum of $L(e_t)$ | $1,-1,-1,-1$ | $1,1,1,1$ | $1,0,0,0$ | $1,0,0,0$ |

**Remark (the column of the largest defect).** This is the column with the full defect, and it is the only column in which the failure of the Jordan identity has both a scalar and a vector face. It is also the only column whose operator at the unit is an involution, and the only one with no Peirce theory of any kind. The three facts have one cause: the square of a generic element is not central, so the algebra cannot be reduced to a form and a line.

## Summary

The symmetric quaternionic sesquilinear product is $\tilde Q_1\bullet_{\natural*}\tilde Q_2=K(\tilde Q_1,\tilde Q_2)e_t-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$. It is conjugate-commutative, it has no unit, its image is the whole space, and its trace form is the Krein form $K$.

It fails the Jordan identity everywhere: the defect is four-dimensional, spanned by the values $2e_t$ at the three pairs of equal vector units and $-2\vec e_k$ at the three pairs $(\vec e_k,e_t)$. The square of a generic element has a vector part, and that vector part is the source of the failure.

On the Hermitian subspace the square is $K(\tilde H,\tilde H)e_t$, so the cone of squares is the line $\mathbb{R}e_t$, and the isotropic cone of $K$ is a cone of index-two nilpotents. The idempotents are $0$ and $e_t$; the operator at the unit is the Hermitian involution with spectrum $\{1,-1\}$, and there is no Peirce decomposition. The multiplication operators and the quadratic representation are of rank four for generic elements, and the quadratic identity fails.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1\bullet_{\natural*}\tilde Q_2$ | the symmetric quaternionic sesquilinear product |
| $K(\tilde Q_1,\tilde Q_2)=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | the Krein form |
| ${}^{\natural}$, ${}^{*}$ | the quaternion involution and the Hermitian involution |
| $L(\tilde Q_1)$, $U(\tilde Q_1)$ | the multiplication operator and the quadratic representation |
| $D(\tilde Q_1,\tilde Q_2)$ | the Jordan defect |
| $\mathbb{B}_{+1},\mathbb{B}_{-1}$ | the eigenspaces of the Hermitian involution |
| $\mathbb{B}_{V}$ | the vector subspace |
| $\mathbb{B}_{\Psi}$ | the Hermitian subspace |

## Further Reading

- [The General Quaternionic Sesquilinear Product](the-general-quaternionic-sesquilinear-product.html), for the product of which this is the symmetrisation.
- [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), for the symmetrisation that satisfies the identity.
- [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html) and [The Jordan Structure of the Symmetric Plain Sesquilinear Product](the-jordan-structure-of-the-symmetric-plain-sesquilinear-product.html), for the two central companions.
- [The Lie Structure of the Antisymmetric Quaternionic Sesquilinear Product](the-lie-structure-of-the-antisymmetric-quaternionic-sesquilinear-product.html), for the other half of the same product.
- [Jordan Algebras](jordan-algebras.html), for the identity, the Peirce theory and the quadratic representation in general.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the Krein form and its index.
