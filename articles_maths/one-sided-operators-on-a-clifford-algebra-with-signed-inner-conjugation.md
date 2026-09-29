# __One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation__

## Introduction

Every two-sided operator of *Two-Sided Operators on a Clifford Algebra* is the product of a left multiplication and a right multiplication, and the signed inner conjugation of *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* is the product of two such factors:

$$
\mathrm{Ad}^{\alpha}_x=\Lambda^{\alpha}_x\circ R_{x^{-1}},\qquad \Lambda^{\alpha}_x(y)=\alpha(x)\,y,\qquad R_{x^{-1}}(y)=y\,x^{-1}.
$$

The **signed left multiplication** $\Lambda^{\alpha}_x$ is the one-sided operator that carries the minus. On an even element it is the ordinary left multiplication $L_x$, on an odd element it is $-L_x$, and it is the left factor of the signed inner conjugation, while the right factor is the inverse. This article treats the pair, with the emphasis on where the sign sits and on what the pairing buys.

Two facts organise the account. The first is that the minus is entirely in the left factor: the right factor $R_{x^{-1}}$ is the inverse right multiplication, which is common to the inner conjugation and to the signed inner conjugation, and it is the substitution $L_x\mapsto\Lambda^{\alpha}_x$ that turns the product $L_xR_{x^{-1}}$ into $\Lambda^{\alpha}_xR_{x^{-1}}$, that is, $\mathrm{Ad}_x$ into $\mathrm{Ad}^{\alpha}_x$. The second is that a one-sided operator does not preserve the space of vectors, so the sign cannot be detected one-sidedly: no left multiplication and no right multiplication carries $V$ into itself except the scalars, and it is the product of two factors that acts on $V$ by an isometry. The signed left multiplication is therefore not a geometric transformation on its own; it is half of one, and the half that decides the sign.

The general theory of the two one-sided families — their definitions, their composition laws, the anti-multiplicativity of the plain right multiplication, their mutual commutants, their kernels and their images — is *One-Sided Operators on a Clifford Algebra*, and nothing of it is re-derived here. The two-sided family and the inverse members are *Two-Sided Operators on a Clifford Algebra*; the signed member is *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*; the groups are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; and the action of the pair on a Clifford module is *Pin Representations and Clifford Modules with Signed Inner Conjugation*. The base is a field $F$ of characteristic not $2$, with $q$ a non-degenerate quadratic form on the finite-dimensional space $V$ and $B$ its polar form.

## The Signed Left Multiplication

**Definition.** For $x\in\mathrm{Cl}(V,q)$ the **signed left multiplication** by $x$ is the $F$-linear map

$$
\Lambda^{\alpha}_x:\mathrm{Cl}(V,q)\longrightarrow\mathrm{Cl}(V,q),\qquad \Lambda^{\alpha}_x(y)=\alpha(x)\,y .
$$

It is the left one-sided operator $\Lambda^{\theta}_x$ of *One-Sided Operators on a Clifford Algebra* with $\theta=\alpha$, and it is defined for every $x$, invertibility not being required.

**Proposition (the sign, and the conjugate form).** Let $x$ be homogeneous of degree $k$ and $\varepsilon_x=(-1)^{k}$, so that $\alpha(x)=\varepsilon_xx$. Then

$$
\Lambda^{\alpha}_x=\varepsilon_x\,L_x=\alpha\circ L_x\circ\alpha .
$$

In particular $\Lambda^{\alpha}_x=L_x$ for even $x$ and $\Lambda^{\alpha}_x=-L_x$ for odd $x$.

*Proof.* The first equality is $\alpha(x)=\varepsilon_xx$ with $\varepsilon_x$ central. For the second, $\alpha\bigl(L_x(\alpha(y))\bigr)=\alpha\bigl(x\,\alpha(y)\bigr)=\alpha(x)\,y$.

**Proposition (value at the unit, parity, composition).** One has $\Lambda^{\alpha}_x(1)=\alpha(x)$, equal to $+x$ on the even part and $-x$ on the odd part; the operator preserves the parity grading when $x$ is even and interchanges its two components when $x$ is odd; and

$$
\Lambda^{\alpha}_{xz}=\Lambda^{\alpha}_x\circ\Lambda^{\alpha}_z .
$$

*Proof.* The value at the unit and the composition law are the general statements for the left family with $\theta=\alpha$. For the parity, $\Lambda^{\alpha}_x(\mathrm{Cl}^i)\subseteq\mathrm{Cl}^{i+|x|}$ by the general parity proposition of *One-Sided Operators on a Clifford Algebra*, the grade involution $\alpha$ preserving the degree modulo two.

**Remark.** The signed left multiplication is the conjugate of the plain one by the grade involution, and the grade involution is the identity on the even part and the negation on the odd part; both statements of the proposition are that one fact, read at the unit and read on the parity.

## The Inverse Right Multiplication and the Pairing

**Definition.** For a unit $x$ the **inverse right multiplication** is

$$
R_{x^{-1}}:\mathrm{Cl}(V,q)\longrightarrow\mathrm{Cl}(V,q),\qquad R_{x^{-1}}(y)=y\,x^{-1}.
$$

It is the right one-sided operator $\mathrm P^{c}_x$ of *One-Sided Operators on a Clifford Algebra* with $c$ the inverse, which is an anti-automorphism of the unit group, $c(xz)=c(z)c(x)$; the operator is therefore available only on the units.

**Proposition (composition, order preserved).** For units $x,z$ one has

$$
R_{x^{-1}}\circ R_{z^{-1}}=R_{(xz)^{-1}},\qquad R_{x^{-1}}(1)=x^{-1}.
$$

*Proof.* $R_{x^{-1}}\bigl(R_{z^{-1}}(y)\bigr)=y\,z^{-1}x^{-1}=y\,(xz)^{-1}$.

**Proposition (the two pairings).** The left and right factors commute, and

$$
L_x\circ R_{x^{-1}}=\mathrm{Ad}_x,\qquad \Lambda^{\alpha}_x\circ R_{x^{-1}}=\mathrm{Ad}^{\alpha}_x .
$$

*Proof.* $L_x\bigl(R_{x^{-1}}(y)\bigr)=x\,y\,x^{-1}$ and $\Lambda^{\alpha}_x\bigl(R_{x^{-1}}(y)\bigr)=\alpha(x)\,y\,x^{-1}$; the commutation of a left and a right multiplication is associativity.

**Corollary (the minus is in the left factor).** The two pairings differ by the parity sign,

$$
\mathrm{Ad}^{\alpha}_x=\varepsilon_x\,\mathrm{Ad}_x,\qquad \Lambda^{\alpha}_x=\varepsilon_x\,L_x,
$$

with the same $\varepsilon_x=(-1)^{k}$. The right factor is the same in both, so the entire sign bookkeeping of the two-sided operator is carried by the left one-sided operator.

**Corollary (the reflection).** For a vector $u$ with $q(u)\neq0$ the pairing with the signed left multiplication gives the reflection on the space of vectors,

$$
\Lambda^{\alpha}_u\bigl(R_{u^{-1}}(v)\bigr)=\mathrm{Ad}^{\alpha}_u(v)=\rho_u(v),\qquad L_u\bigl(R_{u^{-1}}(v)\bigr)=\mathrm{Ad}_u(v)=-\rho_u(v),
$$

for every $v\in V$. So the plain pairing sends an odd element to the negative of the reflection and the signed pairing to the reflection itself; a reflection is produced by the pair, and the sign that selects $\rho_u$ over $-\rho_u$ is the one carried by $\Lambda^{\alpha}_u$.

**Remark (why no one-sided operator can show the sign on $V$).** The corollary is the only place where the sign becomes visible, and it needs both factors. By the theorem of *One-Sided Operators on a Clifford Algebra* the only left multiplications with $L_x(V)\subseteq V$ are the scalars, and the same holds on the right; so no one-sided operator, signed or not, acts on the quadratic space, and the minus has no one-sided manifestation there. On the module, where a one-sided action is the natural one, the sign shows up differently, in the parity of the operator, and that is the subject of *Pin Representations and Clifford Modules with Signed Inner Conjugation*.

## Kernels, Images and the Unsigned Part

**Proposition.** The kernel and the image of the signed left multiplication are those of the ordinary one,

$$
\ker\Lambda^{\alpha}_x=\ell(\alpha(x))=\ell(x),\qquad \Lambda^{\alpha}_x\bigl(\mathrm{Cl}(V,q)\bigr)=x\cdot\mathrm{Cl}(V,q),
$$

the left annihilator and the right ideal. For the inverse right multiplication, $\ker R_{x^{-1}}=r(x^{-1})$ and $R_{x^{-1}}(\mathrm{Cl})=\mathrm{Cl}\cdot x^{-1}$, a left ideal.

*Proof.* $\alpha(x)=\varepsilon_xx$ with $\varepsilon_x$ a nonzero scalar, so $\alpha(x)y=0$ exactly when $xy=0$, and the image of the left multiplication by a scalar multiple of $x$ is the right ideal $x\cdot\mathrm{Cl}$; the statements on the right are the general ones for the right family.

**Remark.** The kernels and the images do not see the sign, because multiplication by $\alpha(x)$ and multiplication by $x$ differ by the invertible central scalar $\varepsilon_x$. The signed left multiplication is the plain one rescaled, and everything intrinsic to it as a one-sided operator — its kernel, its image, its rank, its parity when $x$ is even — is shared with the plain one. Only the pairing with the inverse right multiplication, that is only the two-sided operator, distinguishes them.

## Worked Cases

### An Odd Element

In $\mathrm{Cl}_{0,3}(\mathbb{R})$ with $e_j^{2}=-1$, let $x=e_1$. Then $x$ is odd, $\varepsilon_x=-1$, $x^{-1}=-e_1$ and $\alpha(x)=-e_1$, so $\Lambda^{\alpha}_{e_1}=-L_{e_1}$ and $R_{e_1^{-1}}=R_{-e_1}=-R_{e_1}$. At the unit,

$$
\Lambda^{\alpha}_{e_1}(1)=-e_1,\qquad R_{e_1^{-1}}(1)=-e_1,\qquad \Lambda^{\alpha}_{e_1}\bigl(R_{e_1^{-1}}(1)\bigr)=\mathrm{Ad}^{\alpha}_{e_1}(1)=-1 .
$$

On the vectors the pairings act as

| pairing | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|
| $L_{e_1}R_{e_1^{-1}}=\mathrm{Ad}_{e_1}$ | $e_1$ | $-e_2$ | $-e_3$ |
| $\Lambda^{\alpha}_{e_1}R_{e_1^{-1}}=\mathrm{Ad}^{\alpha}_{e_1}$ | $-e_1$ | $e_2$ | $e_3$ |

The second row is the reflection $\rho_{e_1}$ and the first is its negative; the two left factors differ by $-1$ and the right factor is common.

### An Even Element

For the rotor $R=e_1e_2$, even with $R^{-1}=-e_1e_2$, one has $\Lambda^{\alpha}_R=L_R$ and

$$
\Lambda^{\alpha}_R\bigl(R_{R^{-1}}(e_1)\bigr)=-e_1,\qquad \Lambda^{\alpha}_R\bigl(R_{R^{-1}}(e_2)\bigr)=-e_2,\qquad \Lambda^{\alpha}_R\bigl(R_{R^{-1}}(e_3)\bigr)=e_3 ,
$$

the half-turn of the plane $\mathrm{span}(e_1,e_2)$. Here the plain and the signed left multiplications coincide and the pairings are equal; the sign appears only on the odd part.

### The Sign Cannot Be Seen on the Ideal Alone

In the same algebra let $\pi=\tfrac12(1+e_3)$ be the primitive idempotent of *Spinors as Minimal Left Ideals with Inner Conjugation*, and let $I=\mathrm{Cl}\,\pi$. Left multiplication by $e_1$ maps $I$ onto $e_1I$, and left multiplication by $\alpha(e_1)=-e_1$ maps it onto $-I$; the two images coincide as subspaces, since $I$ is a linear subspace and $e_1I=(-e_1)I$. So on the ideal the two one-sided operators have the same image and the same kernel, and no one-sided computation on $I$ separates them. What separates them is the parity of the representative and the pairing with the inverse right multiplication, which is the content of the two next articles of the category.

## Summary

The **signed left multiplication** $\Lambda^{\alpha}_x(y)=\alpha(x)\,y$ is the left one-sided operator of the pair $(\theta,c)=(\alpha,(\ )^{-1})$, and the **inverse right multiplication** $R_{x^{-1}}(y)=y\,x^{-1}$ is the right factor of both the inner conjugation and the signed inner conjugation. The pairings are

$$
L_xR_{x^{-1}}=\mathrm{Ad}_x,\qquad \Lambda^{\alpha}_xR_{x^{-1}}=\mathrm{Ad}^{\alpha}_x,\qquad \Lambda^{\alpha}_x=\varepsilon_xL_x,\qquad \mathrm{Ad}^{\alpha}_x=\varepsilon_x\mathrm{Ad}_x ,
$$

with $\varepsilon_x=(-1)^{k}$ the parity sign, so the entire difference between the two two-sided operators sits in the left factor. The signed left multiplication is the conjugate of the plain one by the grade involution, $\Lambda^{\alpha}_x=\alpha L_x\alpha$; it agrees with $L_x$ on the even part and is $-L_x$ on the odd part; it is defined for every $x$, unlike the right factor; its value at the unit is $\alpha(x)$; it preserves the parity for even $x$ and interchanges the two parts for odd $x$; and its kernel and image are those of $L_x$, because it differs from $L_x$ by an invertible scalar.

The sign is visible only in the pairing and only on the quadratic space. For a vector $u$, $\Lambda^{\alpha}_uR_{u^{-1}}(v)=\rho_u(v)$ while $L_uR_{u^{-1}}(v)=-\rho_u(v)$, so the signed left multiplication is exactly what turns the negative of the reflection into the reflection; no one-sided operator preserves $V$, so the minus has no one-sided manifestation there, and on a module it appears instead as the parity of the operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | Grade involution, the sign character, $\alpha(x)=(-1)^kx$ |
| $\varepsilon_x=(-1)^{k}$ | Parity sign of a homogeneous element, $\alpha(x)=\varepsilon_xx$ |
| $L_x(y)=xy$ | Plain left multiplication |
| $\Lambda^{\alpha}_x(y)=\alpha(x)y$ | Signed left multiplication, $\Lambda^{\alpha}_x=\varepsilon_xL_x=\alpha L_x\alpha$ |
| $R_{x^{-1}}(y)=yx^{-1}$ | Inverse right multiplication, defined on the units |
| $\Lambda^{\alpha}_{xz}=\Lambda^{\alpha}_x\Lambda^{\alpha}_z$, $R_{x^{-1}}R_{z^{-1}}=R_{(xz)^{-1}}$ | Composition laws |
| $\Lambda^{\alpha}_xR_{x^{-1}}=\mathrm{Ad}^{\alpha}_x$, $L_xR_{x^{-1}}=\mathrm{Ad}_x$ | The two pairings |
| $\Lambda^{\alpha}_uR_{u^{-1}}=\rho_u$, $L_uR_{u^{-1}}=-\rho_u$ | The reflection and its negative on a vector $u$ |
| $\ell(x)$, $r(x^{-1})$ | Left annihilator and right annihilator, the kernels |
| $x\cdot\mathrm{Cl}$, $\mathrm{Cl}\cdot x^{-1}$ | Right and left ideals, the images |
| $\{x:L_x(V)\subseteq V\}=F\cdot1$ | No one-sided operator preserves the space of vectors |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the left and right regular representations and the sandwich as a product of two one-sided multiplications.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the two-sided sandwich, the reflection formula and the sign carried by a vector.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford action on a module, which is one-sided by construction, and its relation to the action on the quadratic space.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the left and right regular representations, their kernels as annihilators and their images as ideals.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (American Mathematical Society, 1956), for the double centraliser theorem on the regular bimodule.
