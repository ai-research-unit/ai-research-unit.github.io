# __The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$
(*Introduction to the Symmetric Quaternionic Algebra*) collapses every product onto the
central line, so the element theory of the operation is read entirely from the coefficient
$\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ and its diagonal. This article reads that coefficient as a
pairing and develops the two objects the article title names: the **radical**, which is the set of elements
annihilated by the whole algebra on both sides, and the **isotropic elements**, the elements whose square
vanishes. It then records the derived objects the collapse produces — the derived law and the ternary law — and identifies the isotropic elements with the zero divisors of the parent plain algebra.

## The Product as a Pairing with Values in the Centre

Because the operation is $\mathbb{C}$-bilinear, it is the same thing as a family of linear maps, and because
its value is central it is the same thing as a bilinear form.

**Definition.** For $\tilde Q_4\in\mathbb{B}$ the **left multiplication by $\tilde Q_4$** is the
$\mathbb{C}$-linear map

$$
L^{\star}_{\tilde Q_4}: \mathbb{B}\longrightarrow\mathbb{C}e_t,\qquad
L^{\star}_{\tilde Q_4}\tilde Q_1 = \tilde Q_4\star\tilde Q_1 = \langle\tilde Q_4,\tilde Q_1\rangle_{\natural}\,e_t .
$$

Because the product is commutative the right multiplication coincides with it,
$R^{\star}_{\tilde Q_4}=L^{\star}_{\tilde Q_4}$; the operator is examined in *The Multiplication Operators of the
Symmetric Quaternionic Algebra*.

**Proposition (the operation is a form read on the central line).** The operation is determined by $\langle\cdot\rangle_{\natural}$ and
$\langle\cdot\rangle_{\natural}$ is recovered from it: for every pair,

$$ \boxed{\; \langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = \operatorname{Sc}\bigl(\tilde Q_1\star\tilde Q_2\bigr) \;}, $$

the coefficient of $e_t$ in the value. In particular $\star$ is the **quaternion form** placed on the central
line, and the only datum of the operation is the symmetric $\mathbb{C}$-bilinear form $\langle\cdot\rangle_{\natural}$.

*Proof.* The value is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ by the theorem of *Introduction to the Symmetric Quaternionic
Algebra of Biquaternions*, and its scalar part is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. Conversely a bilinear operation given
by a form is the form.

**Remark (an algebraic form).** The coefficient $\langle\cdot\rangle_{\natural}$ is a $\mathbb{C}$-bilinear form, symmetric,
with values in $\mathbb{C}$; its values are complex and not real in general, as at $\tilde Q_1=e_t$,
$\tilde Q_2=ie_t$, where $N=i$. The diagonal $\langle\cdot\rangle_{\natural}$ is the algebraic
norm of *Norm Regularity and Degeneracy in the Biquaternion Algebra*, and $\langle\cdot\rangle_{\natural}$ is multiplicative on the algebra. The reader must keep
the two readings apart: the diagonal $\langle\tilde Q_1\rangle_{\natural}$ is multiplicative and central-valued, while the form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ is only bilinear.

## The Radical

**Definition.** The **radical** or **two-sided annihilator** of $\star$ is the set of elements annihilated by
every element on both sides,

$$
\operatorname{Rad}(\star) = \{\tilde Q_4\in\mathbb{B}: \tilde Q_4\star\tilde Q_1=0 \text{ and }
\tilde Q_1\star\tilde Q_4=0 \text{ for every } \tilde Q_1\in\mathbb{B}\}
= \{\tilde Q_4\in\mathbb{B}: L^{\star}_{\tilde Q_4}=0\}.
$$

Because the operation is commutative the two-sided and the one-sided definitions agree, and the radical is the
common kernel of the left multiplications, $\bigcap_{\tilde Q_1}\ker L^{\star}_{\tilde Q_1}=\{\tilde Q_4: \langle\tilde Q_4,\tilde Q_1\rangle_{\natural}=0 \text{ for all } \tilde Q_1\}$.

**Theorem (the radical is trivial).** $\operatorname{Rad}(\star)=\{0\}$: the only element annihilated by the
whole algebra is $0$.

*Proof.* $\langle\cdot\rangle_{\natural}$ is the standard symmetric form of $\mathbb{C}^4$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, whose Gram
matrix is $I_4$; a form with invertible Gram matrix has no nonzero element paired to zero with the whole
space. Concretely $\tilde Q_4\star e_t=Q_{4t}e_t$ and $\tilde Q_4\star \vec e_\mu=Q_{4\mu} e_t$ for $\mu\in\{x,y,z\}$, so
$\tilde Q_4\star\tilde Q_1=0$ for all $\tilde Q_1$ forces $Q_{4t}=Q_{4x}=Q_{4y}=Q_{4z}=0$.

**Corollary (the operation is not the zero operation, and it is non-degenerate as a form).** The operation is
nonzero — $\langle e_t,e_t\rangle_{\natural}=1$ — and the form $\langle\cdot\rangle_{\natural}$ is non-degenerate, of rank $4$ over $\mathbb{C}$ and of Gram
matrix $I_4$ in the basis. The image of each nonzero left multiplication is the whole central line
$\mathbb{C}e_t$: for $\tilde Q_4\ne0$ some coordinate $Q_{4\mu}\ne0$, so $L^{\star}_{\tilde Q_4}e_\mu=Q_{4\mu} e_t\ne0$ and no nonzero element acts by zero.

**Remark (a trivial radical and a poor element theory are not the same fact).** A non-degenerate pairing is
what one expects of a form, and it does not prevent the operation from being element-theoretically poor: the
radical is trivial, yet the operation has no unit, its idempotents reduce to $0$ and $e_t$, and its
square-zero set is a cone of complex dimension $3$. The triviality of the radical is a statement about the
pairing; the poverty is a statement about the product. The two must not be confused.

## The Isotropic Elements

**Definition.** An element $\tilde Q$ is **isotropic** when its square under $\star$ vanishes,
$\tilde Q\star\tilde Q=0$; equivalently when $\langle\tilde Q\rangle_{\natural}=0$. The **isotropic cone** of the operation is the
set of isotropic elements.

**Theorem (the isotropic elements are the zero divisors of the parent).** An element is isotropic for $\star$ exactly when
$\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=0$, and the nonzero isotropic elements are exactly the zero divisors of the parent plain
product, $\{N=0\}\setminus\{0\}=\mathcal{Z}_{\tilde Q_1\tilde Q_2}$; the zero-divisor set of the block itself is strictly larger, being the whole punctured space
(*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The
cone is the affine cone over the quadric $\{[Q_t:Q_x:Q_y:Q_z]:\sum_\mu Q_\mu^2=0\}$ of
$\mathbb{P}^3(\mathbb{C})$, of complex dimension $2$ in the projective space and $3$ in the algebra, and it is
the isotropic cone of the form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ and of the norm $\langle\tilde Q_1\rangle_{\natural}$ alike (*Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*, *Norm
and Invertibility in the Symmetric Quaternionic Algebra*). It splits into the **pure family**, the elements with $Q_t=0$, a cone of complex
dimension $2$, and the **non-pure family**, the elements with $Q_t\ne0$, of complex dimension $3$; the two are
disjoint and their union is the cone (*Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*).

*Proof.* $\tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$ by the square formula of *Introduction to the Symmetric
Quaternionic Algebra of Biquaternions*, and this vanishes exactly when $\langle\tilde Q\rangle_{\natural}=0$. The identification of
the set $N=0$ with the zero divisors and its description as a quadric cone are *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*.

**Example (the standard isotropic elements).** For $\tilde Q=e_t+i\vec e_x$ the norm is $N=1+i^2=0$, so the
element is isotropic; it lies on the Hermitian subspace $\mathbb{M}_+$ and is a non-pure zero divisor. For
$\tilde Q=\vec e_x+i\vec e_y$ the norm is $N=1+i^2=0$ as well, and the element is a pure zero divisor, lying in the
vector subspace. For $\tilde Q=\vec e_x+\vec e_y+\vec e_z$ the norm is $N=1+1+1=3\ne0$, and the element is not isotropic.

**Remark (isotropy is not the vanishing of the value).** An element with $\langle\tilde Q_1\rangle_{\natural}=0$ still multiplies
nonzero elements to nonzero values: the product $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ can be
nonzero even when $\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=0$, because the form is indefinite and not positive. The isotropy of
$\langle\cdot\rangle_{\natural}$ is the vanishing of the form on one direction, and it is the diagonal that reads it; the radical, by
contrast, is the vanishing on all directions, and it is trivial. Isotropy is a property of each element, and
the radical is a property of the space.

**Remark (the idempotents and the square-zero elements).** The idempotents of the operation are $0$ and $e_t$ alone, and the square-zero elements are exactly the isotropic ones, that is the punctured cone $\{N=0\}\setminus\{0\}$. Both are Common Theory slots of the block — *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* — and they are cited here rather than restated; the point kept here is only that the idempotents and the nilpotents meet only at the origin, that the idempotents meet the square-zero elements nowhere, and that the square-zero *elements* are not the square-zero *operators* of *The Specificities of the Symmetric Quaternionic Algebra*, which are the vector subspace $Q_t=0$.

## The Derived Objects and the Collapse of the Laws

**Proposition (the derived law collapses).** The commutator of the operation vanishes identically,

$$ \boxed{\; [\tilde Q_1,\tilde Q_2]_{\star} = \tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1 = 0 \;}, $$

so the operation has no derived Lie structure: the derived operation of $\mathrm{SQA}$ is the zero operation
on the whole space. The derived object of the operation is therefore the one-dimensional algebra
$\mathbb{C}e_t=\mathbb{C}_{\mathbb{B}}$, with the multiplication of $\mathbb{C}$.

*Proof.* The operation is commutative. The image is the central line, on which the operation is the
multiplication of $\mathbb{C}$ by the proposition of *Introduction to the Symmetric Quaternionic Algebra of
Biquaternions*.

**Proposition (the associative law does not collapse).** The operation is not associative: at
$\tilde Q_1=\tilde Q_2=\vec e_x$, $\tilde Q_3=e_t$ the two bracketings are

$$
(\tilde Q_1\star\tilde Q_2)\star\tilde Q_3 = e_t, \qquad
\tilde Q_1\star(\tilde Q_2\star\tilde Q_3) = 0 ,
$$

so the associator is the nonzero element $e_t$. The general associator is

$$
(\tilde Q_1\star\tilde Q_2)\star\tilde Q_3-\tilde Q_1\star(\tilde Q_2\star\tilde Q_3)
= \Bigl(\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}Q_{3t} - Q_{1t}\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}\Bigr)e_t .
$$

*Proof.* $(\tilde Q_1\star\tilde Q_2)\star\tilde Q_3=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t\star\tilde Q_3=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}Q_{3t}e_t$, and $\tilde Q_1\star(\tilde Q_2\star\tilde Q_3)=\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}\,L^{\star}_{\tilde Q_1}e_t=\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}Q_te_t$. At the witness the first is
$\langle \vec e_x,\vec e_x\rangle_{\natural}\cdot 1\cdot e_t=e_t$ and the second is $\langle \vec e_x,e_t\rangle_{\natural}\cdot 0=0$.

**Remark (the ternary law).** The ternary object the operation carries is the one obtained by composing the
quaternionic bracket with the product,

$$
\boxed{\;
T(\tilde Q_1,\tilde Q_2,\tilde Q_3) = [\tilde Q_1,\tilde Q_3]_{\natural}\star\tilde Q_2
= \langle[\tilde Q_1,\tilde Q_3]_{\natural},\tilde Q_2\rangle_{\natural}e_t
\;},
$$

which is linear in each of its three arguments and alternating in the first and the third, the bracket
$[\tilde Q_1,\tilde Q_3]_{\natural}=2\bigl(Q_{1t}\vec Q_3-Q_{3t}\vec Q_1-\vec Q_1\times\vec Q_3\bigr)$ being alternating. It does
**not** vanish in general: at $\tilde Q_1=\vec e_x$, $\tilde Q_2=\vec e_z$, $\tilde Q_3=\vec e_y$ the bracket is
$[\tilde Q_1,\tilde Q_3]_{\natural}=-2\vec e_z$ and $\langle -2\vec e_z,\vec e_z\rangle_{\natural}=-2$, so $T=-2e_t$, and the sum
$[\tilde Q_1,\tilde Q_3]_{\natural}\star\tilde Q_2+\tilde Q_2\star[\tilde Q_1,\tilde Q_3]_{\natural}=2\langle[\tilde Q_1,\tilde Q_3]_{\natural},\tilde Q_2\rangle_{\natural}e_t$ is twice this value and is not $0$. The operation therefore
does not kill the bracket by symmetrisation; what is zero is the commutator of $\star$ itself, not its
composition with the bracket.

## The Relation to the Zero Divisors

The identification of the isotropic elements with the zero divisors makes the element theory of the operation
a small chapter of the zero-divisor geometry of $\mathbb{B}$, which is algebraic: the cone $N=0$ is a quadric
cone, cut by the remarkable subspaces into the pieces recorded in *Remarkable Subspaces under the
Symmetric Quaternionic Algebra of Biquaternions*. On the two definite rows $\mathbb{H}_{\mathbb{B}}$ and
$i\mathbb{H}_{\mathbb{B}}$ the norm is strictly signed and the cone meets the row only at the origin; on the
vector subspace the cone is the pure zero-divisor cone; on the two Hermitian subspaces the cone is their real
null cone.

**Proposition (the operation kills nothing on the definite rows).** No nonzero element of $\mathbb{H}_{\mathbb{B}}$
or of $i\mathbb{H}_{\mathbb{B}}$ is isotropic for $\star$.

*Proof.* On $\mathbb{H}_{\mathbb{B}}$ the form is positive definite, $N=\sum_\mu q_\mu^2\ge0$, vanishing only
at the origin; on $i\mathbb{H}_{\mathbb{B}}$ it is negative definite, $N=-\sum_\mu(q'_\mu)^2\le0$, vanishing
only at the origin (*Remarkable Subspaces under the General Quaternionic Algebra*).

**Remark (the radical again, from the subspaces).** The triviality of the radical is compatible with a large
isotropic cone, and the two are read on the Gram data: the form has Gram matrix $I_4$, which is invertible and
carries no radical; the cone is the set where the diagonal vanishes, which is the isotropic set of an
indefinite form on a complex space. A well-defined form with an isotropic cone of positive dimension is the
generic situation.

## Summary

The symmetric quaternionic multiplication is a pairing: $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, the
quaternion form placed on the central line, and the form is recovered from the product as the coefficient of
$e_t$. Its radical — the two-sided annihilator — is trivial, the Gram matrix of $N$ being the unit matrix; the
operation is therefore not the zero operation and its form is non-degenerate. Its isotropic elements are the
zero divisors, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=0$, forming the affine cone over the quadric
$\sum_\mu Q_\mu^2=0$ of $\mathbb{P}^3(\mathbb{C})$, of complex dimension $3$ in the algebra; the standard
witnesses are $e_t+i\vec e_x$ on the Hermitian subspace and $\vec e_x+i\vec e_y$ on the vector subspace. The square-zero
elements are exactly the isotropic ones; the idempotents are $0$ and $e_t$ alone; the derived law collapses,
the commutator of $\star$ being identically zero; the associative law does not collapse, the associator being
$\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}Q_{3t}-Q_{1t}\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}$ times $e_t$, nonzero at $\vec e_x,\vec e_x,e_t$; and the ternary
object $\langle[\tilde Q_1,\tilde Q_3]_{\natural},\tilde Q_2\rangle_{\natural}e_t$ does not vanish. The two definite rows of the remarkable subspaces
contain no nonzero isotropic element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ | the symmetric quaternionic multiplication |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | the quaternion form, the coefficient of the product |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the norm form, the diagonal of $\langle\cdot\rangle_{\natural}$ |
| $L^{\star}_{\tilde Q_4}$ | the left (and right) multiplication, $L^{\star}_{\tilde Q_4}\tilde Q_1=\langle\tilde Q_4,\tilde Q_1\rangle_{\natural}e_t$ |
| $\operatorname{Rad}(\star)$ | the two-sided annihilator, $\{0\}$ |
| $[\tilde Q_1,\tilde Q_2]_{\natural}$ | the quaternionic bracket $\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1$ |
| $[\tilde Q_1,\tilde Q_2]_{\star}$ | the commutator of the operation, identically zero |
| $T(\tilde Q_1,\tilde Q_2,\tilde Q_3)=\langle[\tilde Q_1,\tilde Q_3]_{\natural},\tilde Q_2\rangle_{\natural}e_t$ | the ternary object of the operation |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable subspaces |

## Further Reading

- [Introduction to the Symmetric Quaternionic Algebra](introduction-to-the-symmetric-quaternionic-algebra.html), for the operation and its square.
- [Norm and Invertibility in the Symmetric Quaternionic Algebra](norm-and-invertibility-in-the-symmetric-quaternionic-algebra.html) and [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the diagonal, the non-degenerate form and the maximal zero-divisor set of the block.
- [Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html) and [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the two idempotents and for the square-zero elements.
- [The Symmetrised Quaternionic Product and the Hermitian Subspace](the-symmetrised-quaternionic-product-and-the-hermitian-subspace.html), for the centrality and the coefficient in full.
- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html) and [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the norm, its polarisation and the isotropic cone.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the idempotents of the algebra and their contrast with the idempotents of $\mathrm{SQA}$.
- [Remarkable Subspaces under the Symmetric Quaternionic Algebra](remarkable-subspaces-under-the-symmetric-quaternionic-algebra.html), for the isotropic elements on each subspace.
- [The Multiplication Operators of the Symmetric Quaternionic Algebra](the-multiplication-operators-of-the-symmetric-quaternionic-algebra.html), for the operators $L^{\star}_{\tilde Q_4}$ in full.
