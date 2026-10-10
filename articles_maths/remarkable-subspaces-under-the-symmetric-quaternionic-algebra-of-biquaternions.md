# __Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions__

## Introduction

The symmetric quaternionic multiplication $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$
(*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*) is read here on the remarkable
real subspaces of *Introduction to the Remarkable Subspaces*: the centre $\mathbb{C}_{\mathbb{B}}$, the vector
subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion
subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace
$\mathbb{M}_-$. On each the product of two general elements is computed, and the article records the rule, the
**closure** of the subspace — whether the product of two of its elements is again in the subspace — the
elements off the subspace that the product produces, the isotropic elements and the idempotents.

The article follows the pattern of the companion readings of the same remarkable subspaces under the other
$\mathbb{C}$-bilinear operations, *Remarkable Subspaces under the General Plain Algebra of Biquaternions* and
*Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*; the subspaces themselves, their
real bases and their elements are *Introduction to the Remarkable Subspaces*, and the restrictions of the form that
the product carries are *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* and
*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*, whose table is quoted here and not
recomputed. The isotropic elements are *Zero Divisors of the General Plain Algebra* and *The Radical and the Isotropic
Elements of the Symmetric Quaternionic Algebra*; the closure statement for the symmetrised quaternionic
product is *Remarkable Subspaces and the Four General Products*.

**Conventions.** A general element is $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$ and
$Q_\mu\in\mathbb{C}$; $A,B$ are complex numbers; $h,g$ are real quaternions, $h=h_0e_0+\cdots+h_3e_3$ with
$h_\mu\in\mathbb{R}$; and $\mathbf p,\mathbf q,\mathbf r$ are real vectors of $\mathbb{R}^3$. The remarkable subspaces have the real bases $\{e_0,ie_0\}$ for the centre, $\{e_k,ie_k\}$ for the vector subspace,
$\{e_0,e_1,e_2,e_3\}$ for $\mathbb{H}_{\mathbb{B}}$, $\{ie_0,ie_1,ie_2,ie_3\}$ for
$i\mathbb{H}_{\mathbb{B}}$, $\{e_0,ie_1,ie_2,ie_3\}$ for $\mathbb{M}_+$ and $\{ie_0,e_1,e_2,e_3\}$ for
$\mathbb{M}_-$.

**Definition.** A subspace $U$ **stays inside itself** under $\star$, or is **kept inside itself** by $\star$,
when $\tilde P,\tilde Q\in U$ implies $\tilde P\star\tilde Q\in U$.

## The Product on the Remarkable Subspaces

### The Centre

On $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ the general elements are $Ae_0$ and $Be_0$, and

$$
(Ae_0)\star(Be_0) = \bigl(AB\bigr)e_0 .
$$

The product stays in the centre, and the restriction of the operation to the centre is the multiplication of
$\mathbb{C}$: the centre is kept inside itself by $\star$ and is the only subspace on which the operation is a
multiplication with a unit, the unit being $e_0$ for the centre. The idempotents are $0$ and $e_0$; the
isotropic elements are none for the complex form, since the norm of a central element is $N(Ae_0)=A^2$, which
vanishes only at $A=0$; the two real
lines $\mathbb{R}(e_0\pm ie_0)$ are isotropic for the **realification** of the form and not for the complex
form.

### The Vector Subspace

On $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$ the general elements are $\mathbf P$ and
$\mathbf Q$, and

$$
\mathbf P\star\mathbf Q = \bigl(\mathbf P,\mathbf Q\bigr)e_0 .
$$

The product does not stay in the vector subspace: it is central, and it is in the subspace only when the
coefficient vanishes. The **smallest nonzero value off the subspace** is $e_0$, produced by the pair
$e_1,e_1$; more generally $\mathbf P\star\mathbf Q=0$ exactly when the two complex vectors are
$B$-isotropic partners, $(\mathbf P,\mathbf Q)=0$. The idempotents are $0$ alone, since $e_0$ is not in the
subspace; the isotropic elements are the pure zero divisors, the complex cone
$\sum_kQ_k^2=0$ of *Zero Divisors of the General Plain Algebra*.

### The Quaternion Subspace

On $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$ the general elements are real quaternions $h$ and
$g$, and

$$
h\star g = \bigl(h_0g_0+h_1g_1+h_2g_2+h_3g_3\bigr)e_0 .
$$

The coefficient is real, so the product is a real multiple of $e_0$, an element of the real line
$\mathbb{R}e_0\subset\mathbb{H}_{\mathbb{B}}$: the quaternion subspace is kept inside itself by $\star$. It is a **definite**
row, the coefficient being the positive definite form $\sum_\mu h_\mu g_\mu$; hence there is **no isotropic
element**, and no nonzero element is a zero divisor. The idempotents are $0$ and $e_0$.

### The Anti-Quaternion Subspace

On $i\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{ie_0,ie_1,ie_2,ie_3\}$ the general elements are $ih$ and $ig$ with
$h,g$ real, and

$$
(ih)\star(ig) = -\bigl(h_0g_0+h_1g_1+h_2g_2+h_3g_3\bigr)e_0 .
$$

The coefficient is real and the product is a real multiple of $e_0$, which lies in $\mathbb{H}_{\mathbb{B}}$
and not in $i\mathbb{H}_{\mathbb{B}}$: the subspace is **not** kept inside itself by $\star$, and the **smallest nonzero
value off the subspace** is $-e_0$, produced by the pair $ie_1,ie_1$. The subspace is a definite row of
negative sign, so there is no isotropic element; the idempotent is $0$ alone, $e_0$ not lying in the subspace.

### The Hermitian Subspace

On $\mathbb{M}_+=\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ the general elements are $a_0e_0+i\mathbf p$ and
$b_0e_0+i\mathbf q$ with $a_0,b_0$ real and $\mathbf p,\mathbf q$ real vectors, and

$$
(a_0e_0+i\mathbf p)\star(b_0e_0+i\mathbf q) = \bigl(a_0b_0-(\mathbf p,\mathbf q)\bigr)e_0 .
$$

The coefficient is real, so the product is a real multiple of $e_0$, an element of the real line
$\mathbb{R}e_0\subset\mathbb{M}_+$: the Hermitian subspace is kept inside itself by $\star$. The idempotents of the
operation are $0$ and $e_0$: the nontrivial idempotents of the algebra, the elements $\tfrac12(e_0+i\mathbf u)$
over real unit vectors $\mathbf u$, have norm $N=\tfrac14(1-(\mathbf u,\mathbf u))=0$ and are isotropic for
$\star$ instead of idempotent. The isotropic elements are the real light cone, the elements with
$a_0^2=(\mathbf p,\mathbf p)$, which
are the non-pure zero divisors of the Hermitian subspace (*Remarkable Subspaces under the General Quaternionic
Algebra of Biquaternions*).

### The Anti-Hermitian Subspace

On $\mathbb{M}_-=\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ the general elements are $ia_0e_0+\mathbf p$ and
$ib_0e_0+\mathbf q$, and

$$
(ia_0e_0+\mathbf p)\star(ib_0e_0+\mathbf q) = \bigl((\mathbf p,\mathbf q)-a_0b_0\bigr)e_0 .
$$

The coefficient is real but the product is a real multiple of $e_0$, which lies in $\mathbb{H}_{\mathbb{B}}$
and not in $\mathbb{M}_-$: the subspace is **not** kept inside itself by $\star$, and the **smallest nonzero value off the
subspace** is $e_0$, produced by the pair $e_3,e_3$. The idempotent is $0$ alone, $e_0$ not lying in the
subspace; the isotropic elements are the real light cone of the subspace, the elements with
$(\mathbf p,\mathbf p)=a_0^2$.

## The Table of the Remarkable Subspaces

| subspace | real basis | the product of two general elements | stays inside itself | smallest nonzero value off | isotropic elements | idempotents |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $e_0,\,ie_0$ | $(AB)e_0$ | yes | — | none (complex form) | $0,\,e_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | $e_k,\,ie_k$ | $(\mathbf P,\mathbf Q)e_0$ | no | $e_0$ at $e_1,e_1$ | the pure zero divisors | $0$ |
| $\mathbb{H}_{\mathbb{B}}$ | $e_0,\dots,e_3$ | $\bigl(\sum_\mu h_\mu g_\mu\bigr)e_0$ | yes | — | none | $0,\,e_0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $ie_0,\dots,ie_3$ | $-\bigl(\sum_\mu h_\mu g_\mu\bigr)e_0$ | no | $-e_0$ at $ie_1,ie_1$ | none | $0$ |
| $\mathbb{M}_+$ | $e_0,ie_1,ie_2,ie_3$ | $\bigl(a_0b_0-(\mathbf p,\mathbf q)\bigr)e_0$ | yes | — | the real light cone | $0,\,e_0$ |
| $\mathbb{M}_-$ | $ie_0,e_1,e_2,e_3$ | $\bigl((\mathbf p,\mathbf q)-a_0b_0\bigr)e_0$ | no | $e_0$ at $e_3,e_3$ | the real light cone | $0$ |

**Remark (the three that stay inside and the three that leave).** The operation is kept inside itself by
exactly three of the remarkable subspaces — the centre, the quaternion subspace and the Hermitian subspace — and it
leaves the other three, in agreement with the closure statement of *Remarkable Subspaces and the Four General Products* for the symmetrisation of the general quaternionic product, which this article follows. The centre
stays inside because it is the image of the operation; the quaternion subspace and the Hermitian subspace stay
inside because the coefficient is real on each of them and the real line $\mathbb{R}e_0$ lies in both. The
vector subspace returns a complex multiple of $e_0$ that leaves it, while the anti-quaternion and
anti-Hermitian subspaces return a real multiple of $e_0$, which lies in $\mathbb{H}_{\mathbb{B}}$ and not in
them: each of the three leaves the subspace and enters the centre.

**Remark (no unit on any subspace).** The operation has no unit on the whole algebra
(*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*), so it has no unit on any of the remarkable subspaces;
and even on the centre, where the restriction is the multiplication of $\mathbb{C}$, the unit $e_0$ is a unit
of the restricted centre and not of the algebra. The element $e_0$ acts on every subspace by the projection of
the scalar part, $\tilde A\star e_0=A_0e_0$, which is the identity only on the centre. For every nonzero
$\tilde A$ the equation $\tilde A\star\tilde X=e_0$ has the affine hyperplane $B(\tilde A,\tilde X)=1$ of
solutions, since the form is non-degenerate; but there is no unit, so no element is invertible in the sense of
the operation.

**Remark (the two definite rows and the two light cones).** The quaternion and anti-quaternion subspaces are
the two definite rows: on each the coefficient is a real form of a single sign, so no nonzero element is
isotropic and no nonzero element is a zero divisor. The centre is indefinite over the reals but anisotropic
over $\mathbb{C}$; the vector subspace carries the complex isotropic cone of the pure zero divisors; and the
two Hermitian subspaces carry the two real light cones of the non-pure zero divisors. The three isotropic
readings — none, the complex cone, the real light cone — are the ones recorded in the table and developed in
*Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*.

## Worked Examples

**A central pair.** For $\tilde P=e_0$ and $\tilde Q=ie_0$ the product is $(1\cdot i)e_0=ie_0$, a central
element: the centre is kept inside itself and the value is the product $i$ of the two coefficients.

**A vector pair off the subspace.** For $\tilde P=\tilde Q=e_1$ in the vector subspace the product is
$(\mathbf P,\mathbf Q)e_0=1\cdot e_0=e_0$, so the smallest nonzero value off the subspace is $e_0$; the
product of $e_1$ with $ie_2$ is $(1\cdot i)e_0=ie_0$, again off the subspace.

**A quaternion pair.** For $h=e_0+e_1$ and $g=e_0-e_1$ the coefficient is $1-1=0$, so $h\star g=0$: two
nonzero elements of the quaternion subspace multiply to $0$. Definiteness is a statement about the diagonal,
$B(h,h)>0$, and does not prevent two distinct elements from pairing to zero.

**An anti-quaternion pair.** For $\tilde P=\tilde Q=ie_1$ the product is $-e_0$, which lies in
$\mathbb{H}_{\mathbb{B}}$: the anti-quaternion subspace is not kept inside itself, and the value is the
negative of the unit.

**A Hermitian pair.** For $\tilde P=e_0+ie_1$ and $\tilde Q=e_0+ie_1$ the coefficient is $1-1=0$, so the
element is isotropic; it is the standard non-pure zero divisor of the Hermitian subspace. For
$\tilde P=e_0+ie_1$ and $\tilde Q=e_0-ie_1$ the coefficient is $1+1=2$, so the product is $2e_0$.

**An anti-Hermitian pair.** For $\tilde P=ie_0+e_1$ the square is $(1-1)e_0=0$: the element is isotropic and
non-pure, and its product is $0$ with itself.

**A cross pair.** For $\tilde P=e_0$ in the quaternion subspace and $\tilde Q=ie_1$ in the vector subspace the
product is $B(e_0,ie_1)e_0=0$, the two directions being paired to zero by the form.

## Summary

On the remarkable real subspaces the symmetric quaternionic multiplication has the rules
$(AB)e_0$ on the centre, $(\mathbf P,\mathbf Q)e_0$ on the vector subspace, $(\sum_\mu h_\mu g_\mu)e_0$ on the
quaternion subspace, $-(\sum_\mu h_\mu g_\mu)e_0$ on the anti-quaternion subspace,
$(a_0b_0-(\mathbf p,\mathbf q))e_0$ on the Hermitian subspace and $((\mathbf p,\mathbf q)-a_0b_0)e_0$ on the
anti-Hermitian subspace. Exactly three of the remarkable subspaces are kept inside themselves — the centre, the quaternion
subspace and the Hermitian subspace, the three that contain the real line — and the other three leave the
subspace, the vector subspace producing a complex multiple of $e_0$ and the anti-quaternion and anti-Hermitian
subspaces a real one; the smallest nonzero values off are $e_0$ at $e_1,e_1$, $-e_0$ at $ie_1,ie_1$ and $e_0$ at
$e_3,e_3$. The idempotents are $0$ and $e_0$ on the three subspaces that contain $e_0$ and $0$ alone on the
other three; there is no unit on any subspace. The isotropic elements are none on the two definite rows, the
pure zero divisors on the vector subspace, none for the complex form on the centre, and the real light cones of
the non-pure zero divisors on the two Hermitian subspaces. The form whose coefficient the product reads has
the signatures $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$ on the remarkable subspaces, and the product carries the
isotropic set appropriate to each.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable real subspaces |
| $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $A,B$; $h,g$; $a_0,b_0$; $\mathbf p,\mathbf q$ | complex coefficients, real quaternions, real scalars, real vectors |
| $(AB)e_0$, $(\mathbf P,\mathbf Q)e_0$, $\bigl(\sum_\mu h_\mu g_\mu\bigr)e_0$ | the products on the centre, the vector and the quaternion subspaces |
| $-\bigl(\sum_\mu h_\mu g_\mu\bigr)e_0$, $\bigl(a_0b_0-(\mathbf p,\mathbf q)\bigr)e_0$, $\bigl((\mathbf p,\mathbf q)-a_0b_0\bigr)e_0$ | the products on the anti-quaternion, Hermitian and anti-Hermitian subspaces |
| kept inside itself by $\star$ | the product of two elements stays in the subspace |
| $0$, $e_0$ | the idempotents of the operation |
| $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ | the signatures of the form on the remarkable subspaces |

## Further Reading

- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces, their bases and their elements
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-algebra-of-biquaternions.md`) and *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the same remarkable subspaces under the other $\mathbb{C}$-bilinear operations
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the closure statement of the symmetrisation
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the restrictions of the form and their signatures
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the radical and the isotropic cone
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the pure and the non-pure zero divisors
