
# __Fueter Theory for Split-Quaternions__

## Introduction

This article develops Fueter theory in the split-quaternion setting: the **Fueter operator**, the **Fueter-regular** functions it defines, the **axial and slice** approach, and the power-series description. In the quaternion and biquaternion theories the Fueter operator is a square root of the definite Laplacian on the quaternion subspace, and the Fueter construction converts holomorphic functions of one complex variable into regular functions by applying a power of the Laplacian to their axial extension. In the split signature the second-order operator is not a Laplacian but the **ultrahyperbolic** operator $\Box = \partial^2/\partial q_t^2+\partial^2/\partial q_x^2-\partial^2/\partial q_y^2-\partial^2/\partial q_z^2$ of signature $(2,2)$, and the spherical symmetry on which the classical scalar case rests is replaced by hyperbolic symmetry. The slice results survive verbatim; the axial construction does not, and the reason is the indefinite form together with the zero divisors.

The article owns the Fueter theory of the category. It relies on *Split-Quaternion Regular Functions* for the Cauchy–Riemann operator and its factorization, on *Split-Quaternion Roots of Minus One* for the imaginary units, and on the power-series material developed in *Split-Quaternion Analysis* and *Split-Quaternion Elementary Functions*. It is compared throughout with the biquaternion counterpart *Fueter Theory for Biquaternions* and with the quaternion theory. No physics is invoked, and the first-order operator is called the **Cauchy–Riemann operator**, not the Dirac operator.

**Conventions.** Coordinates are $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ with $\langle\tilde q\rangle_{\natural} = q_t^2+q_x^2-q_y^2-q_z^2$; the vector part is $\vec v = q_x \vec e_x+q_y \vec e_y+q_z \vec e_z \in V$ with $\langle \vec v\rangle_{\natural} = q_x^2-q_y^2-q_z^2$. Partial derivatives are $\partial/\partial q_t,\partial/\partial q_x,\partial/\partial q_y,\partial/\partial q_z$.

## The Fueter Operator in the Split Signature

### Definition and Conjugate

**Definition.** The **Fueter operator** (the **Cauchy–Riemann–Fueter operator**) and its **conjugate** are

$$
\nabla = e_t\,\partial/\partial q_t + \vec e_x\,\partial/\partial q_x + \vec e_y\,\partial/\partial q_y + \vec e_z\,\partial/\partial q_z = \partial/\partial q_t + \vec D, \qquad
\bar{\nabla} = \partial/\partial q_t - \vec D, \qquad
\vec D = \vec e_x\,\partial/\partial q_x + \vec e_y\,\partial/\partial q_y + \vec e_z\,\partial/\partial q_z,
$$

acting on the left. The operators are the same expressions as in the quaternion and biquaternion theories; only the squares of the generators differ, $\vec e_x^2 = -1$, $\vec e_y^2 = \vec e_z^2 = +1$.

### Factorization of the Ultrahyperbolic Operator

**Proposition.** $\nabla\bar{\nabla} = \bar{\nabla}\nabla = \Box e_t$, where

$$
\Box = \partial^2/\partial q_t^2 + \partial^2/\partial q_x^2 - \partial^2/\partial q_y^2 - \partial^2/\partial q_z^2
$$

is the **ultrahyperbolic operator** of signature $(2,2)$.

**Proof.** Expand $\nabla\bar{\nabla} = \sum_{\mu,\nu}e_\mu e_\nu^{\natural}\,\partial^2/\partial q_\mu\partial q_\nu$. The diagonal coefficients are $e_te_t^{\natural} = e_t$, $\vec e_x\vec e_x^{\natural} = -\vec e_x^2 = e_t$, $\vec e_y\vec e_y^{\natural} = -\vec e_y^2 = -e_t$, $\vec e_z\vec e_z^{\natural} = -e_t$; the off-diagonal coefficients vanish by the Clifford relations $e_\mu e_\nu^{\natural} + e_\nu e_\mu^{\natural} = 0$ for $\mu\neq\nu$.

Thus the Fueter operator is a square root not of the Laplacian but of a wave operator: it is the Cauchy–Riemann operator of the Clifford algebra $\mathrm{Cl}_{2,2}$, of signature $(2,2)$. This is the single structural sign that separates the theory from the quaternion ($\mathrm{Cl}_{0,3}$) and biquaternion ($\mathrm{Cl}_{1,3}$) cases.

### Relation to the Cauchy–Riemann Operator

On the full algebra the Fueter operator is exactly the Cauchy–Riemann operator of *Split-Quaternion Regular Functions*: its symbol $s(\xi) = \xi_t + \xi_x\vec e_x+\xi_y\vec e_y+\xi_z\vec e_z$ satisfies $s(\xi)s^{\natural}(\xi) = \langle \xi\rangle_{\natural}e_t$, so it is **not** elliptic and its characteristic set is the null cone $\mathcal{N}$. In Clifford language, $\mathbb{H}_{\mathrm{s}}$ is the even subalgebra of $\mathrm{Cl}_{2,2}$ up to the standard identification, and the Fueter-regular functions are its **monogenic** functions.

## Fueter-Regular Functions

### Left and Right Regularity

**Definition.** Let $\Omega$ be open in $\mathbb{R}^4$, and let $F : \Omega \to \mathbb{H}_{\mathrm{s}}$ be continuously differentiable. Then $F$ is **left-Fueter-regular** if $\nabla F = 0$; **right-Fueter-regular** if $F\nabla := \sum_\mu\partial/\partial q_\mu\,F\,e_\mu = 0$; and **anti-regular** if $\bar\nabla F = 0$. As in the rest of the category, **regular** means left-regular, and the first-order operator $\nabla$ is the one inverted.

### The Componentwise System

Writing $F = F_0 + \vec F$ with $\vec F = F_1\vec e_x+F_2\vec e_y+F_3\vec e_z$, the regularity condition is the split Cauchy–Riemann–Fueter system of *Split-Quaternion Regular Functions*,

$$
\partial/\partial q_t\,F_0 = \mathrm{div}_{\mathrm{s}}\,\vec F, \qquad \partial/\partial q_t\,\vec F + \operatorname{grad}_{\mathrm{s}}F_0 + \operatorname{rot}_{\mathrm{s}}\vec F = 0,
$$

with the divergence, gradient and curl taken for the indefinite form $N|_V$. Left- and right-regularity differ only in the sign of the curl term, exactly as in the quaternion case.

**Proposition (harmonicity).** Every Fueter-regular function is $\Box$-harmonic: $\nabla F = 0$ implies $\Box F = \bar\nabla\nabla F = 0$. The converse is false.

**Proof.** Immediate from the factorization; the function $F_0 = q_t$ is $\Box$-harmonic but $\nabla q_t = e_t \neq 0$.

## The Axial and Slice Approach

### Imaginary Units and Slices

**Definition.** An **imaginary unit** is an element $I$ with $I^2 = -1$, and a **slice** is a real plane $\mathbb{C}_I = \mathbb{R} + I\mathbb{R}$ spanned by $1$ and an imaginary unit.

**Theorem.** The imaginary units of $\mathbb{H}_{\mathrm{s}}$ are the elements of the vector subspace

$$
\{ I \in V : I^2 = -1 \} = \{ I \in V : \langle I\rangle_{\natural} = 1 \} = \{ q_x \vec e_x + q_y \vec e_y + q_z \vec e_z : q_x^2 - q_y^2 - q_z^2 = 1 \},
$$

a **two-sheeted hyperboloid** of dimension $2$ in $V$, with the two sheets distinguished by the sign of the coefficient $q_x$. Each imaginary unit spans a slice $\mathbb{C}_I \cong \mathbb{C}$, and two slices $\mathbb{C}_I$, $\mathbb{C}_J$ coincide when $I = \pm J$ and otherwise meet only in $\mathbb{R}$.

**Proof.** $I \in V$ satisfies $I^2 = -\langle I\rangle_{\natural}$ (the vector part squares to minus its split-quaternion norm), so $I^2 = -1$ iff $\langle I\rangle_{\natural} = 1$, which is the displayed hyperboloid, two-sheeted because $q_x^2 = 1+q_y^2+q_z^2\geq1$; the slice intersection statement is linear algebra.

This is the first departure from the quaternion theory, where the imaginary units form the two-sphere $S^2$. Here there is no compact imaginary sphere: the imaginary units are unbounded and split into two sheets, so an "imaginary direction" must be selected one root at a time, as in the biquaternion case but for a different reason.

### Holomorphic Functions on a Slice Are Regular

**Theorem.** Fix an imaginary unit $I$, with slice coordinate $A = q_t + I\rho$ on $\mathbb{C}_I$, and let $F$ depend only on $q_t$ and $\rho$ (not on the two directions of $V$ orthogonal to $I$). Then

$$
\nabla F = (\partial/\partial q_t + I\,\partial/\partial\rho)F = 2\,\partial/\partial\bar A\,F,
$$

so $F$ is regular if and only if $F$ is holomorphic in $A$ in the classical sense. Hence every classical holomorphic function of $A = q_t+I\rho$, extended by constancy in the orthogonal directions, is Fueter-regular.

**Proof.** Restricted to functions of $q_t,\rho$, the operator is $\nabla = e_t\,\partial/\partial q_t + I\,\partial/\partial\rho$, and $I^2 = -1$ makes $\mathbb{R}[I]$ a copy of $\mathbb{C}$ with $\bar A = q_t - I\rho$; the classical Cauchy–Riemann operator of that copy is $\partial/\partial\bar A = \tfrac12(\partial/\partial q_t + I\,\partial/\partial\rho)$.

This slice statement is exact and requires no modification for the split signature, because on a slice the form is definite (the slice is a copy of $\mathbb{C}$). It is the part of the theory that survives intact.

### Axial Coordinates and the Obstruction by the Zero Divisors

For an element $\tilde q = q_t+\vec v$ with $\langle \vec v\rangle_{\natural} > 0$, the **axial coordinates** are

$$
\rho = \sqrt{\langle \vec v\rangle_{\natural}} > 0, \qquad \vec u = \vec v/\rho, \qquad \vec u^2 = -1,
$$

so that $\vec u$ is an imaginary unit and $\tilde q$ lies on the slice $\mathbb{C}_{\vec u}$. On this region an **axially symmetric** function has the representation

$$
F(\tilde q) = A(q_t,\rho) + \vec u\,B(q_t,\rho),
$$

with **axial coefficients** $A, B$ that depend on the direction only through $\vec u$. This is the exact analogue of the quaternion axial representation, and it is available precisely where $\langle \vec v\rangle_{\natural} > 0$.

**Theorem (the obstruction).** The axial representation is defined only on the timelike region $\langle \vec v\rangle_{\natural} > 0$. On the null cone $\langle \vec v\rangle_{\natural} = 0$ the axial direction is a zero divisor and no imaginary unit is defined; on the spacelike region $\langle \vec v\rangle_{\natural} < 0$ the normalised direction satisfies $\vec u^2 = +1$, a root of $+1$, so the axial coefficient system is hyperbolic rather than complex. The region is the disjoint union of the timelike region $\langle \vec v\rangle_{\natural}>0$, on which the axial complex structure exists, the null cone $\mathcal{N}$, on which it degenerates, and the spacelike region $\langle \vec v\rangle_{\natural}<0$, on which it is replaced by a split-complex structure.

**Proof.** $\vec u^2 = -\langle \vec v\rangle_{\natural}/\rho^2 = -\operatorname{sgn}\langle \vec v\rangle_{\natural}$, so $\vec u^2 = -1$ on the timelike region, $\vec u^2 = +1$ on the spacelike region, and $\vec u$ is undefined on the null cone.

Thus the axial and slice approach is available on the whole timelike region and on a slice-by-slice basis, but it cannot be extended across the null cone, exactly as in the indefinite biquaternion case; and here, unlike the biquaternion case, there is no definite half to fall back on.

### Why the Definite Fueter Construction Does Not Transfer

The classical Fueter construction sends a holomorphic $f_0$ to $F = \Delta_4f^{\mathrm{ax}}_0$, the Laplacian applied to the axial extension, and its proof uses the radial identity $\sum_{\mu,\nu}(\partial/\partial v_\nu\,\vec u_\mu)\vec e_\nu \vec e_\mu = -2/\rho$ on the sphere of imaginary units. In the split signature the level sets of $\langle \vec v\rangle_{\natural}$ in the timelike region are **two-sheeted hyperboloids**, not spheres, and the corresponding identity acquires a vector part:

$$
\sum_{\mu,\nu}(\partial/\partial v_\nu\,\vec u_\mu)\,\vec e_\nu \vec e_\mu = \frac{1}{\rho}\sum_\nu \vec e_\nu^2 - \frac{1}{\rho^3}\sum_{\mu,\nu} g_{\nu\nu} v_\mu v_\nu\, \vec e_\nu \vec e_\mu, \qquad \sum_\nu \vec e_\nu^2 = 1,
$$

and the second sum is not a scalar multiple of $\vec u$ but has the nonzero vector part $2v_x(-v_z\vec e_y+v_y\vec e_z)$ together with the Euclidean scalar part $-|\vec v|_E^2$. Hence the definite Fueter construction, with $\Box$ in place of $\Delta_4$, does **not** in general produce regular functions, and there is no direct radial/spherical version of Fueter's theorem in the split signature.

**Remark.** What remains is the slice construction of the previous subsection, which is exact and local to each slice, and the general Clifford-algebraic theory of monogenic functions on $\mathrm{Cl}_{2,2}$, which is signature-independent for the Fischer decomposition below. The axial radial construction is the part that fails, and its failure is measured by the vector part displayed above.

## Power Series Representations

**Theorem (right-coefficient series).** A series $F(\tilde q) = \sum_{n\geq0} \tilde q^n a_n$ with coefficients $a_n \in \mathbb{H}_{\mathrm{s}}$ on the right converges absolutely and normally on $\|\tilde q\|_E < R$, where $R^{-1} = \limsup_n\|a_n\|_E^{1/n}$, and its sum is **slice-regular** (Cullen-regular): holomorphic on each slice.

**Proof.** The Euclidean operator norm is submultiplicative, so $\|\tilde q^n\|_E \le \|\tilde q\|_E^n$ and the series is dominated by the scalar series $\sum\|a_n\|_E\|\tilde q\|_E^n$; on a slice, $\tilde q = A$ and the sum is a power series in the slice variable.

**Proposition.** The coordinate function $\tilde q$ is slice-regular but not Fueter-regular: $\nabla \tilde q = \sum_\mu e_\mu e_\mu = e_t^2+\vec e_x^2+\vec e_y^2+\vec e_z^2 = 1-1+1+1 = 2e_t \neq 0$. In general the slice-regular class is strictly larger than the Fueter-regular class, and the Fueter construction is the operation that converts the first into the second.

**Theorem (Fischer decomposition).** Let $\mathcal{P}_k$ be the $\mathbb{H}_{\mathrm{s}}$-valued homogeneous polynomials of degree $k$ and $\mathcal{M}_k = \{P \in \mathcal{P}_k : \nabla P = 0\}$ the **monogenic homogeneous polynomials**. Then

$$
\mathcal{P}_k = \bigoplus_{j=0}^{k} \tilde q^j \mathcal{M}_{k-j},
$$

so every Fueter-regular function on a ball has a normally convergent expansion in monogenic homogeneous polynomials, the analogue of the Taylor series of complex analysis.

**Proof.** This is the standard Fischer decomposition for a real Clifford algebra with a non-degenerate quadratic form; it depends only on the non-degeneracy of $\langle\cdot\rangle_{\natural}$ and the factorization $\Box = \nabla\bar\nabla$, both of which hold with the split signature.

## Relation to the Quaternion and Biquaternion Fueter Theories

The biquaternion article *Fueter Theory for Biquaternions* develops the operator on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where $\tilde\nabla\tilde{\nabla}^{\natural} = \Delta_4 e_t$ is the definite Laplacian; there the imaginary units form the sphere $S^2$, the axial representation and the Fueter construction are classical, the Fueter–Sce theorem holds for odd $n$ with the power $(n-1)/2$, and the Cauchy kernel is singular only at the origin. On the indefinite biquaternion subspaces $\mathbb{M}_\pm$ the second-order operator becomes a wave operator and the elliptic tools disappear, while the full algebra $\mathbb{B}$ has the six-dimensional null quadric as an obstruction.

The split-quaternion theory is the case in which **every** direction is of that indefinite kind: the second-order operator is ultrahyperbolic on the whole algebra, the imaginary units form a two-sheeted hyperboloid rather than a sphere, and the axial construction is obstructed on the null cone and replaced by a hyperbolic structure outside the timelike region. The slice statements survive because each slice restores a definite (complex) structure, and the Fischer decomposition survives because it needs only non-degeneracy; the radial Fueter construction and the Fueter–Sce parity theorem do not transfer, because they rest on spherical symmetry of a definite form. In Clifford terms the split-quaternion Fueter theory is the monogenic function theory of $\mathrm{Cl}_{2,2}$, to be compared with the $\mathrm{Cl}_{0,3}$ theory of the quaternions and the $\mathrm{Cl}_{1,3}$ theory of the biquaternions. Nothing quaternion- or biquaternion-specific — no imaginary sphere $S^2$, no definite half, no Euclidean Cauchy kernel — is imported.

## Summary

The Fueter operator $\nabla = \sum_\mu e_\mu\,\partial/\partial q_\mu$ and its conjugate satisfy $\nabla\bar\nabla = \bar\nabla\nabla = \Box e_t$, the ultrahyperbolic operator $\partial^2/\partial q_t^2+\partial^2/\partial q_x^2-\partial^2/\partial q_y^2-\partial^2/\partial q_z^2$ of signature $(2,2)$; the Fueter operator is the Cauchy–Riemann operator of $\mathrm{Cl}_{2,2}$, non-elliptic, with the null cone as its characteristic set. Fueter-regular functions are the solutions of $\nabla F = 0$, equivalently of the split Cauchy–Riemann–Fueter system, and every such function is $\Box$-harmonic. The imaginary units are the two-sheeted hyperboloid $\{\langle I\rangle_{\natural}=1\}$ in $V$, not a sphere; on any slice $\mathbb{C}_I$ the operator reduces to the classical Cauchy–Riemann operator $\partial/\partial q_t + I\,\partial/\partial\rho$, so holomorphic functions of the slice variable are regular. The axial representation $F = A + \vec uB$ is available exactly on the timelike region $\langle \vec v\rangle_{\natural}>0$, degenerates on the null cone, and is replaced by a hyperbolic structure on the spacelike region; and the radial Fueter construction does not transfer, because the level sets of $\langle \vec v\rangle_{\natural}$ are hyperboloids rather than spheres and the radial identity acquires the vector part $2q_x(-q_z\vec e_y+q_y\vec e_z)$. Right-coefficient series are slice-regular on $\|\tilde q\|_E < R$, the coordinate $\tilde q$ is slice-regular but not regular, and the Fischer decomposition $\mathcal{P}_k = \bigoplus_j \tilde q^j\mathcal{M}_{k-j}$ gives the monogenic Taylor expansion. The split-quaternion theory is the fully indefinite member of the family: the slice and Fischer parts survive, and the radial, spherical and Fueter–Sce parts do not.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\nabla = \partial/\partial q_t + \vec D$, $\bar\nabla = \partial/\partial q_t - \vec D$ | the Fueter (Cauchy–Riemann–Fueter) operator and its conjugate | *Split-Quaternion Regular Functions* |
| $\vec D = \sum_\mu \vec e_\mu\,\partial/\partial q_\mu$ | the vector-derivative part | this article |
| $\Box = \partial^2/\partial q_t^2+\partial^2/\partial q_x^2-\partial^2/\partial q_y^2-\partial^2/\partial q_z^2$ | the ultrahyperbolic operator, signature $(2,2)$ | this article |
| $\nabla F = 0$ | left-Fueter-regular (monogenic); $F\nabla=0$ right-regular | this article |
| $I$, $\{\langle I\rangle_{\natural}=1\}$ | an imaginary unit, and the two-sheeted hyperboloid of imaginary units | *Split-Quaternion Roots of Minus One* |
| $\mathbb{C}_I = \mathbb{R}+I\mathbb{R}$ | a slice, a copy of the complex plane | this article |
| $\rho = \sqrt{\langle \vec v\rangle_{\natural}}$, $\vec u = \vec v/\rho$ | axial radius and direction, on the timelike region $\langle \vec v\rangle_{\natural}>0$ | this article |
| $A, B$ | axial coefficients, $F = A(q_t,\rho) + \vec uB(q_t,\rho)$ | this article |
| $\mathcal{P}_k, \mathcal{M}_k$ | homogeneous and monogenic homogeneous polynomials | this article |
| $\langle\tilde q\rangle_{\natural}=q_t^2+q_x^2-q_y^2-q_z^2$ | the split-quaternion norm, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |
| $\mathcal{N} = \{N=0\}$ | the null cone / zero-divisor set | *Split-Quaternion Zero Divisors* |

## Further Reading

- R. Fueter, "Über die analytische Darstellung der regulären Funktionen einer Quaternionenvariablen", *Commentarii Mathematici Helvetici* 8 (1935–1936), 371–378, for the original axial construction.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis*, Research Notes in Mathematics 76 (Pitman, 1982), for monogenic functions, the Cauchy–Riemann–Fueter operator and the Fischer decomposition.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for monogenic function theory over Clifford algebras of general signature.
- Graziano Gentili, Caterina Stoppato and Daniele C. Struppa, *Regular Functions of a Quaternionic Variable* (Springer, 2013), for the slice-regular (Cullen-regular) class and its relation to the Fueter construction.
- R. S. Ward and Raymond O. Wells, *Twistor Geometry and Field Theory* (Cambridge University Press, 1990), for the Cauchy–Riemann operators of signature $(2,2)$ and the ultrahyperbolic equation.
