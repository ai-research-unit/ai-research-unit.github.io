# __The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$
(*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*) collapses every product onto the
central line, so the element theory of the operation is read entirely from the coefficient
$N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ and its diagonal. This article reads that coefficient as a
pairing and develops the two objects the article title names: the **radical**, which is the set of elements
annihilated by the whole algebra on both sides, and the **isotropic elements**, the elements whose square
vanishes. It then records the derived objects the collapse produces — the derived law and the ternary law — and identifies the isotropic elements with the zero divisors of the parent plain algebra.

**Placement.** The article is the first entry of the *Specific Theory* section of the block, the section that carries the block's own structural theory, and it is followed by *The Specificities of the Symmetric Quaternionic Algebra*. It assumes the operation and its formula from *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, the centrality from *The Symmetrised Quaternionic Product and the Hermitian Subspace*, the norm, its polarisation and its isotropic cone from *Norm and Invertibility in the General Quaternionic Algebra* and *Zero Divisors of the General Plain Algebra*; the idempotents, the nilpotents and the zero-divisor set of the block are the Common Theory slots *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*, *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* and *Zero Divisors of the Symmetric Quaternionic Algebra*, cited here and not restated. The remarkable subspaces are treated in the companion article *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*, and the form reader is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*.

**Conventions.** The operation is $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$,
equal to $N(\tilde P,\tilde Q)e_0$; the coefficient $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ is the
quaternion form, and $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$ is its diagonal; the quaternionic
bracket is $[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$. The remarkable subspaces are $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$,
$i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Introduction to the Remarkable Subspaces*.

## The Product as a Pairing with Values in the Centre

Because the operation is $\mathbb{C}$-bilinear, it is the same thing as a family of linear maps, and because
its value is central it is the same thing as a bilinear form.

**Definition.** For $\tilde A\in\mathbb{B}$ the **left multiplication by $\tilde A$** is the
$\mathbb{C}$-linear map

$$
L^{\star}_{\tilde A}: \mathbb{B}\longrightarrow\mathbb{C}e_0,\qquad
L^{\star}_{\tilde A}\tilde R = \tilde A\star\tilde R = N(\tilde A,\tilde R)\,e_0 .
$$

Because the product is commutative the right multiplication coincides with it,
$R^{\star}_{\tilde A}=L^{\star}_{\tilde A}$; the operator is examined in *The Multiplication Operators of the
Symmetric Quaternionic Algebra*.

**Proposition (the operation is a form read on the central line).** The operation is determined by $N$ and
$N$ is recovered from it: for every pair,

$$
N(\tilde P,\tilde Q) = \operatorname{Sc}\bigl(\tilde P\star\tilde Q\bigr),
$$

the coefficient of $e_0$ in the value. In particular $\star$ is the **quaternion form** placed on the central
line, and the only datum of the operation is the symmetric $\mathbb{C}$-bilinear form $N$.

*Proof.* The value is $N(\tilde P,\tilde Q)e_0$ by the theorem of *Introduction to the Symmetric Quaternionic
Algebra of Biquaternions*, and its scalar part is $N(\tilde P,\tilde Q)$. Conversely a bilinear operation given
by a form is the form.

**Remark (an algebraic form).** The coefficient $N$ is a $\mathbb{C}$-bilinear form, symmetric,
with values in $\mathbb{C}$; its values are complex and not real in general, as at $\tilde P=e_0$,
$\tilde Q=ie_0$, where $N=i$. The diagonal $N$ is the algebraic
norm of *Norm and Invertibility in the General Quaternionic Algebra*, and $N$ is multiplicative on the algebra. The reader must keep
the two readings apart: the diagonal $N(\tilde Q)$ is multiplicative and central-valued, while the form $N(\tilde P,\tilde Q)$ is only bilinear.

## The Radical

**Definition.** The **radical** or **two-sided annihilator** of $\star$ is the set of elements annihilated by
every element on both sides,

$$
\operatorname{Rad}(\star) = \{\tilde A\in\mathbb{B}: \tilde A\star\tilde R=0 \text{ and }
\tilde R\star\tilde A=0 \text{ for every } \tilde R\in\mathbb{B}\}
= \{\tilde A\in\mathbb{B}: L^{\star}_{\tilde A}=0\}.
$$

Because the operation is commutative the two-sided and the one-sided definitions agree, and the radical is the
common kernel of the left multiplications, $\bigcap_{\tilde R}\ker L^{\star}_{\tilde R}=\{\tilde A: N(\tilde A,\tilde R)=0 \text{ for all } \tilde R\}$.

**Theorem (the radical is trivial).** $\operatorname{Rad}(\star)=\{0\}$: the only element annihilated by the
whole algebra is $0$.

*Proof.* $N$ is the standard symmetric form of $\mathbb{C}^4$ in the basis $e_0,e_1,e_2,e_3$, whose Gram
matrix is $I_4$; a form with invertible Gram matrix has no nonzero element paired to zero with the whole
space. Concretely $\tilde A\star e_0=A_0e_0$ and $\tilde A\star e_k=A_ke_0$ for $k=1,2,3$, so
$\tilde A\star\tilde R=0$ for all $\tilde R$ forces $A_0=A_1=A_2=A_3=0$.

**Corollary (the operation is not the zero operation, and it is non-degenerate as a form).** The operation is
nonzero — $N(e_0,e_0)=1$ — and the form $N$ is non-degenerate, of rank $4$ over $\mathbb{C}$ and of Gram
matrix $I_4$ in the basis. The image of each nonzero left multiplication is the whole central line
$\mathbb{C}e_0$: for $\tilde A\ne0$ some coordinate $A_\mu\ne0$, so $L^{\star}_{\tilde A}e_\mu=A_\mu e_0\ne0$ and no nonzero element acts by zero.

**Remark (a trivial radical and a poor element theory are not the same fact).** A non-degenerate pairing is
what one expects of a form, and it does not prevent the operation from being element-theoretically poor: the
radical is trivial, yet the operation has no unit, its idempotents reduce to $0$ and $e_0$, and its
square-zero set is a cone of complex dimension $3$. The triviality of the radical is a statement about the
pairing; the poverty is a statement about the product. The two must not be confused.

## The Isotropic Elements

**Definition.** An element $\tilde Q$ is **isotropic** when its square under $\star$ vanishes,
$\tilde Q\star\tilde Q=0$; equivalently when $N(\tilde Q)=0$. The **isotropic cone** of the operation is the
set of isotropic elements.

**Theorem (the isotropic elements are the zero divisors of the parent).** An element is isotropic for $\star$ exactly when
$N(\tilde Q)=\sum_\mu Q_\mu^2=0$, and the nonzero isotropic elements are exactly the zero divisors of the parent plain
product, $\{N=0\}\setminus\{0\}=\mathcal{Z}_{\tilde P\tilde Q}$; the zero-divisor set of the block itself is strictly larger, being the whole punctured space
(*Zero Divisors of the Symmetric Quaternionic Algebra*). The
cone is the affine cone over the quadric $\{[Q_0:Q_1:Q_2:Q_3]:\sum_\mu Q_\mu^2=0\}$ of
$\mathbb{P}^3(\mathbb{C})$, of complex dimension $2$ in the projective space and $3$ in the algebra, and it is
the isotropic cone of the form $N(\tilde P,\tilde Q)$ and of the norm $N(\tilde Q)$ alike (*Zero Divisors of the General Plain Algebra*, *Norm
and Invertibility in the Symmetric Quaternionic Algebra*). It splits into the **pure family**, the elements with $Q_0=0$, a cone of complex
dimension $2$, and the **non-pure family**, the elements with $Q_0\ne0$, of complex dimension $3$; the two are
disjoint and their union is the cone (*Zero Divisors of the General Plain Algebra*).

*Proof.* $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ by the square formula of *Introduction to the Symmetric
Quaternionic Algebra of Biquaternions*, and this vanishes exactly when $N(\tilde Q)=0$. The identification of
the set $N=0$ with the zero divisors and its description as a quadric cone are *Zero Divisors of the General Plain Algebra*.

**Example (the standard isotropic elements).** For $\tilde Q=e_0+ie_1$ the norm is $N=1+i^2=0$, so the
element is isotropic; it lies on the Hermitian subspace $\mathbb{M}_+$ and is a non-pure zero divisor. For
$\tilde Q=e_1+ie_2$ the norm is $N=1+i^2=0$ as well, and the element is a pure zero divisor, lying in the
vector subspace. For $\tilde Q=e_1+e_2+e_3$ the norm is $N=1+1+1=3\ne0$, and the element is not isotropic.

**Remark (isotropy is not the vanishing of the value).** An element with $N(\tilde Q)=0$ still multiplies
nonzero elements to nonzero values: the product $\tilde Q\star\tilde R=N(\tilde Q,\tilde R)e_0$ can be
nonzero even when $N(\tilde Q,\tilde Q)=0$, because the form is indefinite and not positive. The isotropy of
$N$ is the vanishing of the form on one direction, and it is the diagonal that reads it; the radical, by
contrast, is the vanishing on all directions, and it is trivial. Isotropy is a property of each element, and
the radical is a property of the space.

**Remark (the idempotents and the square-zero elements).** The idempotents of the operation are $0$ and $e_0$ alone, and the square-zero elements are exactly the isotropic ones, that is the punctured cone $\{N=0\}\setminus\{0\}$. Both are Common Theory slots of the block — *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* — and they are cited here rather than restated; the point kept here is only that the idempotents and the nilpotents meet only at the origin, that the idempotents meet the square-zero elements nowhere, and that the square-zero *elements* are not the square-zero *operators* of *The Specificities of the Symmetric Quaternionic Algebra*, which are the vector subspace $Q_0=0$.

## The Derived Objects and the Collapse of the Laws

**Proposition (the derived law collapses).** The commutator of the operation vanishes identically,

$$
[\tilde P,\tilde Q]_{\star} = \tilde P\star\tilde Q-\tilde Q\star\tilde P = 0 ,
$$

so the operation has no derived Lie structure: the derived operation of $\mathrm{SQA}$ is the zero operation
on the whole space. The derived object of the operation is therefore the one-dimensional algebra
$\mathbb{C}e_0=\mathbb{C}_{\mathbb{B}}$, with the multiplication of $\mathbb{C}$.

*Proof.* The operation is commutative. The image is the central line, on which the operation is the
multiplication of $\mathbb{C}$ by the proposition of *Introduction to the Symmetric Quaternionic Algebra of
Biquaternions*.

**Proposition (the associative law does not collapse).** The operation is not associative: at
$\tilde P=\tilde Q=e_1$, $\tilde R=e_0$ the two bracketings are

$$
(\tilde P\star\tilde Q)\star\tilde R = e_0, \qquad
\tilde P\star(\tilde Q\star\tilde R) = 0 ,
$$

so the associator is the nonzero element $e_0$. The general associator is

$$
(\tilde P\star\tilde Q)\star\tilde R-\tilde P\star(\tilde Q\star\tilde R)
= \Bigl(N(\tilde P,\tilde Q)R_0 - P_0N(\tilde Q,\tilde R)\Bigr)e_0 .
$$

*Proof.* $(\tilde P\star\tilde Q)\star\tilde R=N(\tilde P,\tilde Q)e_0\star\tilde R=N(\tilde P,\tilde Q)R_0e_0$, and $\tilde P\star(\tilde Q\star\tilde R)=N(\tilde Q,\tilde R)\,L^{\star}_{\tilde P}e_0=N(\tilde Q,\tilde R)P_0e_0$. At the witness the first is
$N(e_1,e_1)\cdot 1\cdot e_0=e_0$ and the second is $N(e_1,e_0)\cdot 0=0$.

**Remark (the ternary law).** The ternary object the operation carries is the one obtained by composing the
quaternionic bracket with the product,

$$
T(\tilde P,\tilde Q,\tilde R) = [\tilde P,\tilde R]_{\natural}\star\tilde Q
= N\bigl([\tilde P,\tilde R]_{\natural},\tilde Q\bigr)e_0 ,
$$

which is linear in each of its three arguments and alternating in the first and the third, the bracket
$[\tilde P,\tilde R]_{\natural}=2\bigl(P_0\mathbf R-R_0\mathbf P-\mathbf P\times\mathbf R\bigr)$ being alternating. It does
**not** vanish in general: at $\tilde P=e_1$, $\tilde R=e_2$, $\tilde Q=e_3$ the bracket is
$[\tilde P,\tilde R]_{\natural}=-2e_3$ and $N(-2e_3,e_3)=-2$, so $T=-2e_0$, and the sum
$[\tilde P,\tilde R]_{\natural}\star\tilde Q+\tilde Q\star[\tilde P,\tilde R]_{\natural}=2N([\tilde P,\tilde R]_{\natural},\tilde Q)e_0$ is twice this value and is not $0$. The operation therefore
does not kill the bracket by symmetrisation; what is zero is the commutator of $\star$ itself, not its
composition with the bracket.

## The Relation to the Zero Divisors

The identification of the isotropic elements with the zero divisors makes the element theory of the operation
a small chapter of the zero-divisor geometry of $\mathbb{B}$, which is algebraic: the cone $N=0$ is a quadric
cone, cut by the remarkable subspaces into the pieces recorded in *Remarkable Subspaces under the
Symmetric Quaternionic Algebra of Biquaternions*. On the two definite rows $\mathbb{H}_{\mathbb{B}}$ and
$i\mathbb{H}_{\mathbb{B}}$ the norm is strictly signed and the cone meets the row only at the origin; on the
vector subspace the cone is the pure zero-divisor cone; on the two Hermitian subspaces the cone is their real
light cone.

**Proposition (the operation kills nothing on the definite rows).** No nonzero element of $\mathbb{H}_{\mathbb{B}}$
or of $i\mathbb{H}_{\mathbb{B}}$ is isotropic for $\star$.

*Proof.* On $\mathbb{H}_{\mathbb{B}}$ the form is positive definite, $N=\sum_\mu q_\mu^2\ge0$, vanishing only
at the origin; on $i\mathbb{H}_{\mathbb{B}}$ it is negative definite, $N=-\sum_\mu(q'_\mu)^2\le0$, vanishing
only at the origin (*Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*).

**Remark (the radical again, from the subspaces).** The triviality of the radical is compatible with a large
isotropic cone, and the two are read on the Gram data: the form has Gram matrix $I_4$, which is invertible and
carries no radical; the cone is the set where the diagonal vanishes, which is the isotropic set of an
indefinite form on a complex space. A well-defined form with an isotropic cone of positive dimension is the
generic situation.

## Summary

The symmetric quaternionic multiplication is a pairing: $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$, the
quaternion form placed on the central line, and the form is recovered from the product as the coefficient of
$e_0$. Its radical — the two-sided annihilator — is trivial, the Gram matrix of $N$ being the unit matrix; the
operation is therefore not the zero operation and its form is non-degenerate. Its isotropic elements are the
zero divisors, $N(\tilde Q)=\sum_\mu Q_\mu^2=0$, forming the affine cone over the quadric
$\sum_\mu Q_\mu^2=0$ of $\mathbb{P}^3(\mathbb{C})$, of complex dimension $3$ in the algebra; the standard
witnesses are $e_0+ie_1$ on the Hermitian subspace and $e_1+ie_2$ on the vector subspace. The square-zero
elements are exactly the isotropic ones; the idempotents are $0$ and $e_0$ alone; the derived law collapses,
the commutator of $\star$ being identically zero; the associative law does not collapse, the associator being
$N(\tilde P,\tilde Q)R_0-P_0N(\tilde Q,\tilde R)$ times $e_0$, nonzero at $e_1,e_1,e_0$; and the ternary
object $N([\tilde P,\tilde R]_{\natural},\tilde Q)e_0$ does not vanish. The two definite rows of the remarkable subspaces
contain no nonzero isotropic element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | the quaternion form, the coefficient of the product |
| $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$ | the norm form, the diagonal of $N$ |
| $L^{\star}_{\tilde A}$ | the left (and right) multiplication, $L^{\star}_{\tilde A}\tilde R=N(\tilde A,\tilde R)e_0$ |
| $\operatorname{Rad}(\star)$ | the two-sided annihilator, $\{0\}$ |
| $[\tilde P,\tilde Q]_{\natural}$ | the quaternionic bracket $\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$ |
| $[\tilde P,\tilde Q]_{\star}$ | the commutator of the operation, identically zero |
| $T(\tilde P,\tilde Q,\tilde R)=N([\tilde P,\tilde R]_{\natural},\tilde Q)e_0$ | the ternary object of the operation |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable subspaces |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the operation and its square.
- *Norm and Invertibility in the Symmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-algebra.md`) and *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), for the diagonal, the non-degenerate form and the maximal zero-divisor set of the block.
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra.md`) and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra.md`), for the two idempotents and for the square-zero elements.
- *The Symmetrised Quaternionic Product and the Hermitian Subspace* (`articles_maths/the-symmetrised-quaternionic-product-and-the-hermitian-subspace.md`), for the centrality and the coefficient in full.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`) and *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the norm, its polarisation and the isotropic cone.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the idempotents of the algebra and their contrast with the idempotents of $\mathrm{SQA}$.
- *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the isotropic elements on each subspace.
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the operators $L^{\star}_{\tilde A}$ in full.
