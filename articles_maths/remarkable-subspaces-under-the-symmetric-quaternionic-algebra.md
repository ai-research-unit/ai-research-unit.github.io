# __Remarkable Subspaces under the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$
(*Introduction to the Symmetric Quaternionic Algebra*) is read here on the remarkable
real subspaces of *The Six Subspaces*: the centre $\mathbb{C}_{\mathbb{B}}$, the vector
subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion
subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace
$\mathbb{M}_-$. On each the product of two general elements is computed, and the article records the rule,
whether the subspace **stays inside itself**, the
elements off the subspace that the product produces, the isotropic elements and the idempotents.

The article follows the pattern of the companion readings of the same remarkable subspaces under the other
$\mathbb{C}$-bilinear operations, *Remarkable Subspaces and the Four General Products, Forms and Norms* and
*Remarkable Subspaces under the General Quaternionic Algebra*; the subspaces themselves, their
real bases and their elements are *The Six Subspaces*, and the restrictions of the form that
the product carries are *Remarkable Subspaces under the General Quaternionic Algebra* and
*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*, whose table is quoted here and not
recomputed. The isotropic elements are *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors* and *The Radical and the Isotropic
Elements of the Symmetric Quaternionic Algebra*; the staying-inside statement for the symmetrised quaternionic
product is *Remarkable Subspaces and the Four General Products, Forms and Norms*.

**Definition.** A subspace $U$ **stays inside itself** under $\star$, or is **kept inside itself** by $\star$,
when $\tilde Q_1,\tilde Q_2\in U$ implies $\tilde Q_1\star\tilde Q_2\in U$.

## The Product on the Remarkable Subspaces

### The Centre

On $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ the general elements are $Ae_t$ and $Be_t$, and

$$
(Ae_t)\star(Be_t) = \bigl(AB\bigr)e_t .
$$

The product stays in the centre, and the restriction of the operation to the centre is the multiplication of
$\mathbb{C}$: the centre is kept inside itself by $\star$ and is the only subspace on which the operation is a
multiplication with a unit, the unit being $e_t$ for the centre. The idempotents are $0$ and $e_t$; the
isotropic elements are none for the complex form, since the norm of a central element is $\langle Ae_t\rangle_{\natural}=A^2$, which
vanishes only at $A=0$; the two real
lines $\mathbb{R}(e_t\pm ie_t)$ are isotropic for the **realification** of the form and not for the complex
form.

### The Vector Subspace

On $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{\vec e_x,\vec e_y,\vec e_z\}$ the general elements are $\vec Q_1$ and
$\vec Q_2$, and

$$ \boxed{\; \vec Q_1\star\vec Q_2 = \bigl(\vec Q_1,\vec Q_2\bigr)e_t \;}. $$

The product does not stay in the vector subspace: it is central, and it is in the subspace only when the
coefficient vanishes. The **smallest nonzero value off the subspace** is $e_t$, produced by the pair
$\vec e_x,\vec e_x$; more generally $\vec Q_1\star\vec Q_2=0$ exactly when the two complex vectors are
$\langle\cdot\rangle_{\natural}$-isotropic partners, $(\vec Q_1,\vec Q_2)=0$. The idempotents are $0$ alone, since $e_t$ is not in the
subspace; the isotropic elements are the pure zero divisors, the complex cone
$\sum_kQ_{2,k}^2=0$ of *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*.

### The Quaternion Subspace

On $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$ the general elements are real quaternions $h$ and
$g$, and

$$ \boxed{\; h\star g = \bigl(h_tg_t+h_xg_x+h_yg_y+h_zg_z\bigr)e_t \;}. $$

The coefficient is real, so the product is a real multiple of $e_t$, an element of the real line
$\mathbb{R}e_t\subset\mathbb{H}_{\mathbb{B}}$: the quaternion subspace is kept inside itself by $\star$. It is a **definite**
row, the coefficient being the positive definite form $\sum_\mu h_\mu g_\mu$; hence there is **no nonzero isotropic
element** of the form, and no nonzero element of the subspace is a zero divisor of the parent plain product. (Every nonzero
element of the block is a zero divisor of the block itself, as *Zero Divisors of the Symmetric Quaternionic
Algebra* shows; the definiteness is a statement about the form and about the parent product, not about the block's
zero-divisor set.) The idempotents are $0$ and $e_t$.

### The Anti-Quaternion Subspace

On $i\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{ie_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ the general elements are $ih$ and $ig$ with
$h,g$ real, and

$$
(ih)\star(ig) = -\bigl(h_tg_t+h_xg_x+h_yg_y+h_zg_z\bigr)e_t .
$$

The coefficient is real and the product is a real multiple of $e_t$, which lies in $\mathbb{H}_{\mathbb{B}}$
and not in $i\mathbb{H}_{\mathbb{B}}$: the subspace is **not** kept inside itself by $\star$, and the **smallest nonzero
value off the subspace** is $-e_t$, produced by the pair $i\vec e_x,i\vec e_x$. The subspace is a definite row of
negative sign, so there is no isotropic element; the idempotent is $0$ alone, $e_t$ not lying in the subspace.

### The Hermitian Subspace

On $\mathbb{M}_+=\mathbb{R}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ the general elements are $a_te_t+i\vec p$ and
$b_te_t+i\vec q$ with $a_t,b_t$ real and $\vec p,\vec q$ real vectors, and

$$ \boxed{\; (a_te_t+i\vec p)\star(b_te_t+i\vec q) = \bigl(a_tb_t-(\vec p,\vec q)\bigr)e_t \;}. $$

The coefficient is real, so the product is a real multiple of $e_t$, an element of the real line
$\mathbb{R}e_t\subset\mathbb{M}_+$: the Hermitian subspace is kept inside itself by $\star$. The idempotents of the
operation are $0$ and $e_t$: the nontrivial idempotents of the algebra, the elements $\tfrac12(e_t+i\vec q_a)$
over real unit vectors $\vec q_a$, have norm $N=\tfrac14(1-(\vec q_a,\vec q_a))=0$ and are isotropic for
$\star$ instead of idempotent. The isotropic elements are the real null cone, the elements with
$a_t^2=(\vec p,\vec p)$, which
are the non-pure zero divisors of the Hermitian subspace (*Remarkable Subspaces under the General Quaternionic
Algebra of Biquaternions*).

### The Anti-Hermitian Subspace

On $\mathbb{M}_-=\mathbb{R}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ the general elements are $ia_te_t+\vec p$ and
$ib_te_t+\vec q$, and

$$
(ia_te_t+\vec p)\star(ib_te_t+\vec q) = \bigl((\vec p,\vec q)-a_tb_t\bigr)e_t .
$$

The coefficient is real but the product is a real multiple of $e_t$, which lies in $\mathbb{H}_{\mathbb{B}}$
and not in $\mathbb{M}_-$: the subspace is **not** kept inside itself by $\star$, and the **smallest nonzero value off the
subspace** is $e_t$, produced by the pair $\vec e_z,\vec e_z$. The idempotent is $0$ alone, $e_t$ not lying in the
subspace; the isotropic elements are the real null cone of the subspace, the elements with
$(\vec p,\vec p)=a_t^2$.

## The Table of the Remarkable Subspaces

| subspace | real basis | the product of two general elements | stays inside itself | smallest nonzero value off | isotropic elements | idempotents |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $e_t,\,ie_t$ | $(AB)e_t$ | yes | — | none (complex form) | $0,\,e_t$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\vec e_k,\,i\vec e_k$ | $(\vec Q_1,\vec Q_2)e_t$ | no | $e_t$ at $\vec e_x,\vec e_x$ | the pure zero divisors | $0$ |
| $\mathbb{H}_{\mathbb{B}}$ | $e_t,\dots,\vec e_z$ | $\bigl(\sum_\mu h_\mu g_\mu\bigr)e_t$ | yes | — | none | $0,\,e_t$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $ie_t,\dots,i\vec e_z$ | $-\bigl(\sum_\mu h_\mu g_\mu\bigr)e_t$ | no | $-e_t$ at $i\vec e_x,i\vec e_x$ | none | $0$ |
| $\mathbb{M}_+$ | $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ | $\bigl(a_tb_t-(\vec p,\vec q)\bigr)e_t$ | yes | — | the real null cone | $0,\,e_t$ |
| $\mathbb{M}_-$ | $ie_t,\vec e_x,\vec e_y,\vec e_z$ | $\bigl((\vec p,\vec q)-a_tb_t\bigr)e_t$ | no | $e_t$ at $\vec e_z,\vec e_z$ | the real null cone | $0$ |

**Remark (the three that stay inside and the three that leave).** The operation is kept inside itself by
exactly three of the remarkable subspaces — the centre, the quaternion subspace and the Hermitian subspace — and it
leaves the other three, in agreement with the staying-inside statement of *Remarkable Subspaces and the Four General Products, Forms and Norms* for the symmetrisation of the general quaternionic product, which this article follows. The centre
stays inside because it is the image of the operation; the quaternion subspace and the Hermitian subspace stay
inside because the coefficient is real on each of them and the real line $\mathbb{R}e_t$ lies in both. The
vector subspace returns a complex multiple of $e_t$ that leaves it, while the anti-quaternion and
anti-Hermitian subspaces return a real multiple of $e_t$, which lies in $\mathbb{H}_{\mathbb{B}}$ and not in
them: each of the three leaves the subspace and enters the centre.

**Remark (no unit on any subspace).** The operation has no unit on the whole algebra
(*Introduction to the Symmetric Quaternionic Algebra*), so it has no unit on any of the remarkable subspaces;
and even on the centre, where the restriction is the multiplication of $\mathbb{C}$, the unit $e_t$ is a unit
of the restricted centre and not of the algebra. The element $e_t$ acts on every subspace by the projection of
the scalar part, $\tilde Q_3\star e_t=Q_{3t}e_t$, which is the identity only on the centre. For every nonzero
$\tilde Q_3$ the equation $\tilde Q_3\star\tilde Q_1=e_t$ has the affine hyperplane $\langle\tilde Q_3,\tilde Q_1\rangle_{\natural}=1$ of
solutions, since the form is non-degenerate; but there is no unit, so no element is invertible in the sense of
the operation.

**Remark (the two definite rows and the two null cones).** The quaternion and anti-quaternion subspaces are
the two definite rows: on each the coefficient is a real form of a single sign, so no nonzero element is
isotropic and no nonzero element is a zero divisor of the parent plain product (the block itself has no
regular element, its zero-divisor set being everything but the origin). The centre is indefinite over the reals but anisotropic
over $\mathbb{C}$; the vector subspace carries the complex isotropic cone of the pure zero divisors; and the
two Hermitian subspaces carry the two real null cones of the non-pure zero divisors. The three isotropic
readings — none, the complex cone, the real null cone — are the ones recorded in the table and developed in
*Remarkable Subspaces under the General Quaternionic Algebra*.

## Worked Examples

**A central pair.** For $\tilde Q_1=e_t$ and $\tilde Q_2=ie_t$ the product is $(1\cdot i)e_t=ie_t$, a central
element: the centre is kept inside itself and the value is the product $i$ of the two coefficients.

**A vector pair off the subspace.** For $\tilde Q_1=\tilde Q_2=\vec e_x$ in the vector subspace the product is
$(\vec Q_1,\vec Q_2)e_t=1\cdot e_t=e_t$, so the smallest nonzero value off the subspace is $e_t$; the
product of $\vec e_x$ with $i\vec e_y$ is $(1\cdot i)e_t=ie_t$, again off the subspace.

**A quaternion pair.** For $h=e_t+\vec e_x$ and $g=e_t-\vec e_x$ the coefficient is $1-1=0$, so $h\star g=0$: two
nonzero elements of the quaternion subspace multiply to $0$. Definiteness is a statement about the diagonal,
$\langle h,h\rangle_{\natural}>0$, and does not prevent two distinct elements from pairing to zero.

**An anti-quaternion pair.** For $\tilde Q_1=\tilde Q_2=i\vec e_x$ the product is $-e_t$, which lies in
$\mathbb{H}_{\mathbb{B}}$: the anti-quaternion subspace is not kept inside itself, and the value is the
negative of the unit.

**A Hermitian pair.** For $\tilde Q_1=e_t+i\vec e_x$ and $\tilde Q_2=e_t+i\vec e_x$ the coefficient is $1-1=0$, so the
element is isotropic; it is the standard non-pure zero divisor of the Hermitian subspace. For
$\tilde Q_1=e_t+i\vec e_x$ and $\tilde Q_2=e_t-i\vec e_x$ the coefficient is $1+1=2$, so the product is $2e_t$.

**An anti-Hermitian pair.** For $\tilde Q_1=ie_t+\vec e_x$ the square is $(1-1)e_t=0$: the element is isotropic and
non-pure, and its product is $0$ with itself.

**A cross pair.** For $\tilde Q_1=e_t$ in the quaternion subspace and $\tilde Q_2=i\vec e_x$ in the vector subspace the
product is $\langle e_t,i\vec e_x\rangle_{\natural}e_t=0$, the two directions being paired to zero by the form.

## Summary

On the remarkable real subspaces the symmetric quaternionic multiplication has the rules
$(AB)e_t$ on the centre, $(\vec Q_1,\vec Q_2)e_t$ on the vector subspace, $(\sum_\mu h_\mu g_\mu)e_t$ on the
quaternion subspace, $-(\sum_\mu h_\mu g_\mu)e_t$ on the anti-quaternion subspace,
$(a_tb_t-(\vec p,\vec q))e_t$ on the Hermitian subspace and $((\vec p,\vec q)-a_tb_t)e_t$ on the
anti-Hermitian subspace. Exactly three of the remarkable subspaces are kept inside themselves — the centre, the quaternion
subspace and the Hermitian subspace, the three that contain the real line — and the other three leave the
subspace, the vector subspace producing a complex multiple of $e_t$ and the anti-quaternion and anti-Hermitian
subspaces a real one; the smallest nonzero values off are $e_t$ at $\vec e_x,\vec e_x$, $-e_t$ at $i\vec e_x,i\vec e_x$ and $e_t$ at
$\vec e_z,\vec e_z$. The idempotents are $0$ and $e_t$ on the three subspaces that contain $e_t$ and $0$ alone on the
other three; there is no unit on any subspace. The isotropic elements are none on the two definite rows, the
pure zero divisors on the vector subspace, none for the complex form on the centre, and the real null cones of
the non-pure zero divisors on the two Hermitian subspaces. The form whose coefficient the product reads has
the signatures $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$ on the remarkable subspaces, and the product carries the
isotropic set appropriate to each.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable real subspaces |
| $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ | the symmetric quaternionic multiplication |
| $A,B$; $h,g$; $a_t,b_t$; $\vec p,\vec q$ | complex coefficients, real quaternions, real scalars, real vectors |
| $(AB)e_t$, $(\vec Q_1,\vec Q_2)e_t$, $\bigl(\sum_\mu h_\mu g_\mu\bigr)e_t$ | the products on the centre, the vector and the quaternion subspaces |
| $-\bigl(\sum_\mu h_\mu g_\mu\bigr)e_t$, $\bigl(a_tb_t-(\vec p,\vec q)\bigr)e_t$, $\bigl((\vec p,\vec q)-a_tb_t\bigr)e_t$ | the products on the anti-quaternion, Hermitian and anti-Hermitian subspaces |
| kept inside itself by $\star$ | the product of two elements stays in the subspace |
| $0$, $e_t$ | the idempotents of the operation |
| $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ | the signatures of the form on the remarkable subspaces |

## Further Reading

- [The Six Subspaces](the-six-subspaces.html), for the remarkable subspaces, their bases and their elements
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) and [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), for the staying-inside statement of the symmetrisation and for the same remarkable subspaces under the other $\mathbb{C}$-bilinear operations
- [The Quaternion Form as a Product on the Symmetric Quaternionic Algebra](the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.html), for the restrictions of the form and their signatures
- [The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra](the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.html), for the radical and the isotropic cone
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the pure and the non-pure zero divisors
