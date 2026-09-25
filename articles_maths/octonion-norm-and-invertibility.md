
# __Octonion Norm and Invertibility__

## Introduction

This article is the second half of the algebra slot of the octonion system: the norm form, its multiplicative property, the invariance of the associated inner product, and the invertibility theory that the norm governs. The article takes the multiplication, the conjugation and the identities of *Octonion Algebra* as established and does not repeat them; it develops the single quadratic form that the algebra carries and the consequences of its behaviour under multiplication.

The article is the octonion member of the pair of algebra slots that Part V traverses one number system at a time, and it follows the model of the norm and invertibility theory of the quaternions in *Quaternion Algebra* and of the general theory of *Division Algebras*. The composition algebras over a field, the notion of the norm form of an algebra and the invariance of a quadratic form under multiplication are treated in the Part I companion *Quadratic Forms over Algebras and Norm Forms*; the present article is the octonion case and is not the general theory. The unit sphere constructed here is used, the multiplication operators, and the eight-square identity is used.

**Conventions.** The octonions are $\mathbb{O} = \mathbb{H}\oplus\mathbb{H}$ with basis $e_0,\dots,e_7$, the Fano multiplication rule, and the conjugation $\bar x$ of *Octonion Algebra*; the vector part is written $\operatorname{Vect}(x)$ and the imaginary subspace $\operatorname{Im}\mathbb{O}$. The **norm** of $x = \sum_{k=0}^{7}x_ke_k$ is the real number

$$
\lvert x\rvert^2 = x\bar x = \bar xx = \sum_{k=0}^{7}x_k^2 ,
$$

and the symbol $N(x)$ is reserved in this Part for the split complex valued norm form of *Split-Biquaternion Norm and Invertibility*; the octonion norm is written $\lvert x\rvert^2$ throughout the octonion articles, and the associated bilinear form is written $\langle x,y\rangle$.

## The Norm Form and the Inner Product

**Definition.** The **norm form** of $\mathbb{O}$ is the map $\lvert\cdot\rvert^2 : \mathbb{O}\to\mathbb{R}$ above; its **polar form** is

$$
\langle x,y\rangle = \tfrac{1}{2}\left(\lvert x+y\rvert^2 - \lvert x\rvert^2 - \lvert y\rvert^2\right), \qquad x,y\in\mathbb{O}.
$$

**Theorem.** The polar form is a symmetric bilinear form on $\mathbb{O}$, and for $x = \sum_kx_ke_k$, $y = \sum_ky_ke_k$,

$$
\langle x,y\rangle = \sum_{k=0}^{7}x_ky_k = \operatorname{Sc}(x\bar y) = \operatorname{Sc}(\bar xy) .
$$

It is positive definite, so that $\mathbb{O}$ with $\langle\cdot,\cdot\rangle$ is a Euclidean space of dimension eight, and the basis $e_0,\dots,e_7$ is orthonormal. The norm form is the quadratic form of the bilinear form, $\lvert x\rvert^2 = \langle x,x\rangle$.

*Proof.* By the second and third statements of the proposition on conjugation in *Octonion Algebra*, $x\bar x = \sum x_k^2$ and $\bar xx = x\bar x$; the displayed identity for the polar form follows by expanding $\lvert x+y\rvert^2$. Bilinearity follows from the coordinate expression. Positive definiteness is the positivity of a sum of squares. $\square$

The inner product is the standard Euclidean product of $\mathbb{R}^8$ under the coordinate identification; the octonion structure on $\mathbb{R}^8$ is thus a multiplication whose norm form is the standard one. The automorphism group of the algebra is therefore a subgroup of the orthogonal group,

$$
G_2 = \operatorname{Aut}(\mathbb{O})\subset O(8),
$$

and a single octonion automorphism is an orthogonal transformation; the proof is in the second proposition below. The verification that $\operatorname{Aut}(\mathbb{O})$ preserves $\lvert\cdot\rvert^2$ is immediate: an automorphism fixes $e_0$, hence commutes with conjugation, hence preserves $x\bar x$.

**Proposition.** For all $x,y,z\in\mathbb{O}$,

$$
\langle x,y\rangle = \tfrac{1}{2}\left(x\bar y + y\bar x\right) = \tfrac{1}{2}\left(\bar xy + \bar yx\right),
$$

and $\langle x,y\rangle e_0 = \tfrac{1}{2}(x\bar y + y\bar x)$. In particular $x\bar y + y\bar x\in\mathbb{R}e_0$ for all octonions $x,y$.

*Proof.* Expand the right-hand side in coordinates, or use the identity $\operatorname{Sc}(u) = \tfrac{1}{2}(u + \bar u)$ applied to $u = x\bar y$. $\square$

The identity in the display is the form in which the inner product enters computations with two octonions; it holds because $\bar u + u$ is always a real scalar even though the algebra is neither commutative nor associative.

## Multiplicativity of the Norm

### The Composition Property

**Theorem.** For all $x,y\in\mathbb{O}$,

$$
\lvert xy\rvert^2 = \lvert x\rvert^2\lvert y\rvert^2 .
$$

Equivalently, the norm form of $\mathbb{O}$ is **multiplicative**, or the octonion algebra is a **composition algebra** for the form $\lvert\cdot\rvert^2$.

*Proof.* By the Cayley–Dickson construction, $\mathbb{O}$ is obtained from $\mathbb{H}$ by the doubling with product $(a,b)(c,d) = (ac-\bar db, da+b\bar c)$ and norm $\lvert(a,b)\rvert^2 = \lvert a\rvert^2 + \lvert b\rvert^2$; a direct expansion using the multiplicativity of the quaternion norm, which is established in *Quaternion Algebra*, gives $\lvert(a,b)(c,d)\rvert^2 = \lvert(a,b)\rvert^2\lvert(c,d)\rvert^2$. Equivalently, the identity is checked on the basis with the aid of the Fano rule, since both sides are quartic and the basis is orthonormal. $\square$

**Corollary (Degen's eight-square identity).** For all real $x_0,\dots,x_7$ and $y_0,\dots,y_7$,

$$
\left(\sum_{k=0}^{7}x_k^2\right)\left(\sum_{k=0}^{7}y_k^2\right) = \sum_{k=0}^{7}z_k^2 ,
$$

where the $z_k$ are the coefficients of the octonion product $z = xy$, each $z_k$ a bilinear form in the $x$'s and $y$'s with coefficients in $\{0,\pm1\}$. In particular the product of two sums of eight squares is again a sum of eight squares, and the identity is integral: it holds over $\mathbb{Z}$.

*Proof.* The displayed identity is the coordinate form of the multiplicativity theorem, and the assertion about the coefficients is the assertion that the structure constants of the multiplication table are in $\{0,\pm1\}$, which the table of *Octonion Algebra* exhibits. $\square$

**Remark.** The eight-square identity and the multiplicative norm are the same fact. The identity exists for $1$, $2$, $4$ and $8$ squares, corresponding to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$, and for no other number of squares: this is Hurwitz's theorem, stated below. The identity for sixteen squares fails, and the Cayley–Dickson double $\mathrm{CD}(\mathbb{O})$ of dimension sixteen, the **sedenions**, is not a division algebra.

### Invariance of the Inner Product

**Theorem.** For all $x,y,z\in\mathbb{O}$,

$$
\langle xy,xz\rangle = \lvert x\rvert^2\langle y,z\rangle, \qquad \langle xy,zy\rangle = \langle x,z\rangle\lvert y\rvert^2 .
$$

Equivalently, for every $x\neq0$ the left multiplication $L_x$ and the right multiplication $R_x$ are **conformal** with factor $\lvert x\rvert^2$; for $\lvert x\rvert = 1$ they are orthogonal.

*Proof.* The first identity follows from the second and the multiplicativity of the norm by polarisation: $\langle xy,xz\rangle = \tfrac{1}{2}(\lvert x(y+z)\rvert^2 - \lvert xy\rvert^2 - \lvert xz\rvert^2) = \tfrac{1}{2}\lvert x\rvert^2(\lvert y+z\rvert^2 - \lvert y\rvert^2 - \lvert z\rvert^2) = \lvert x\rvert^2\langle y,z\rangle$; the computation uses only multiplicativity, and no associativity is required. The second is proved in the same way from the right-hand multiplicativity of the norm, or directly from the identity $\langle xy,zy\rangle = \operatorname{Sc}((xy)(\overline{zy})) = \operatorname{Sc}((xy)(\bar y\bar z))$ together with the identities of *Octonion Algebra*. The conformality statement is the same two identities read as assertions about the operators. $\square$

**Corollary.** For every unit octonion $u$ the maps $L_u$ and $R_u$ belong to the orthogonal group $O(8)$, and in fact to $SO(8)$; the map $u\mapsto L_u$ is injective, with $L_ue_0 = u$, so that the unit sphere embeds in $SO(8)$ and acts simply transitively on itself by left multiplication. The group generated by all left and right multiplications by unit octonions is $SO(8)$.

*Proof.* Orthogonality is the previous theorem at $\lvert u\rvert = 1$; the determinant is one because $u\mapsto L_u$ is continuous and $L_1 = \mathrm{id}$ on the connected sphere $S^7$. Injectivity is the computation $L_ue_0 = ue_0 = u$. The transitivity of the left action on $S^7$ is the statement that for unit $u,v$ the unit $vu^{-1}$ has $L_{vu^{-1}}u = v$, using the two-sided inverse; the action is free because $L_uw = L_uv$ implies $w = v$ by left cancellation, which holds in a division algebra. The last statement is standard and is quoted with the standard references. $\square$

The corollary is the reason why the failure of associativity does not destroy the rotational geometry of the octonions: left multiplication by a unit is an isometry of the Euclidean space, and the failure appears not in the isometry but in the composition law $L_xL_y\neq L_{xy}$ in general. Indeed

$$
L_xL_y = L_{xy}\quad\text{for all }x,y \iff \mathbb{O}\text{ is associative},
$$

so the map $L$ is a loop homomorphism and not a group homomorphism; this is the representation-theoretic face of non-associativity and is treated.

## Invertibility

**Definition.** An element $x\in\mathbb{O}$ is **invertible** if there is $x^{-1}\in\mathbb{O}$ with $xx^{-1} = x^{-1}x = e_0$; a **zero divisor** is a non-zero $x$ for which $xy = 0$ or $yx = 0$ for some $y\neq0$.

**Theorem.** Every non-zero octonion is invertible; equivalently, $\mathbb{O}$ is a division algebra and has no zero divisors. The inverse is

$$
x^{-1} = \frac{\bar x}{\lvert x\rvert^2},
$$

and it is unique and two-sided. Consequently the multiplication is cancellative: $xy = xz$ with $x\neq0$ implies $y = z$, and $yx = zx$ with $x\neq0$ implies $y = z$.

*Proof.* The identities $x(\bar xy) = \lvert x\rvert^2y$ and $(\bar xy)\bar x = \lvert x\rvert^2y$ of *Octonion Algebra*, together with $x\bar x = \bar xx = \lvert x\rvert^2$, give $x\bigl(\bar x/\lvert x\rvert^2\bigr) = e_0$ and $\bigl(\bar x/\lvert x\rvert^2\bigr)x = e_0$ for $x\neq0$. Uniqueness: if $xx' = e_0$ then $x' = \bar x/\lvert x\rvert^2$ by multiplying on the left by $\bar x/\lvert x\rvert^2$ and using the displayed identity; the two-sidedness follows. For cancellativity, multiply the equation by $x^{-1}$ on the left, using the alternative law $(x^{-1}x)y = x^{-1}(xy)$, which holds because $x^{-1}$ and $x$ lie in an associative subalgebra by Artin's theorem. $\square$

**Proposition.** The inversion map is an anti-automorphism of the multiplicative structure: for all non-zero $x,y$,

$$
(xy)^{-1} = y^{-1}x^{-1}, \qquad \overline{x^{-1}} = \overline{x}^{-1}, \qquad \lvert x^{-1}\rvert = \lvert x\rvert^{-1} .
$$

Moreover $x^{-1} = \bar x/\lvert x\rvert^2$ commutes with $x$; the pair $\{x,\bar x\}$ generates an associative subalgebra, and the inverse lies in it.

*Proof.* The first identity follows from $\overline{xy} = \bar y\bar x$ and $\lvert xy\rvert^2 = \lvert x\rvert^2\lvert y\rvert^2$; the second and third are immediate from the formula; the last statements are Artin's theorem applied to the two generators $x$ and $\bar x$. $\square$

**Corollary.** For every $x$, the left and right multiplications by $x$ are invertible maps of $\mathbb{O}$ onto itself when $x\neq0$, with inverses $L_{x^{-1}}$ and $R_{x^{-1}}$; the algebra is a **division algebra**, and it is the largest such obtainable from the Cayley–Dickson process.

The invertibility theory of the octonions is thus as simple as that of a field, and it is a consequence of the norm being multiplicative and positive definite; what the octonions lose is not invertibility but the associativity of products of three or more factors. This is the sense in which $\mathbb{O}$ is a division algebra but not a field-like object.

## The Unit Sphere

### The Sphere as a Moufang Loop

**Definition.** The **unit sphere** of the octonions is

$$
S(\mathbb{O}) = \left\{x\in\mathbb{O} : \lvert x\rvert^2 = 1\right\}\cong S^7 .
$$

**Theorem.** The unit sphere is closed under multiplication and under inversion, and with these operations it is a **Moufang loop**: it is a loop with identity $e_0$, in which every element has a two-sided inverse, and it satisfies the Moufang identity $(xyx)z = x(y(xz))$. It is **not** a group, because the multiplication is not associative: for the unit octonions $e_1,e_2,e_4$ one has

$$
(e_1e_2)e_4 = e_3e_4 = e_7, \qquad e_1(e_2e_4) = e_1e_6 = -e_7 ,
$$

which differ, and the defect $[e_1,e_2,e_4] = 2e_7$ has norm $2$; likewise $(e_1e_4)e_2 = e_5e_2 = -e_7$ while $e_1(e_4e_2) = e_1(-e_6) = e_7$.

*Proof.* Closure under multiplication is multiplicativity of the norm; closure under inversion is $\lvert x^{-1}\rvert = \lvert x\rvert^{-1} = 1$. The one-sided inverse statements of the previous section give the loop property; the Moufang identity is that of *Octonion Algebra*. The computations use the multiplication table, in which $e_1e_2 = e_3$, $e_3e_4 = e_7$, $e_2e_4 = e_6$, $e_1e_6 = -e_7$, $e_1e_4 = e_5$, $e_5e_2 = -e_7$, $e_4e_2 = -e_6$ and $e_1(-e_6) = e_7$. $\square$

The unit sphere is therefore a compact seven-dimensional manifold with a continuous, non-associative multiplication, and it is the standard example of a Moufang loop that is not a group. The associativity defect computed above is twice the associator $[e_1,e_2,e_4]$, and it shows that the failure is not marginal but of order the size of the units themselves.

### Parallelizability and the Volume

**Proposition.** Every point $x$ of the unit sphere is a unit octonion, and left multiplication by $x$ identifies the tangent space at $e_0$ with the tangent space at $x$; since the tangent space at $e_0$ is $\operatorname{Im}\mathbb{O}\cong\mathbb{R}^7$, the sphere $S^7$ admits a global basis of seven vector fields and is **parallelizable**. By the theorem of Adams, the spheres $S^1$, $S^3$ and $S^7$ are the only parallelizable spheres, and they correspond to the complex numbers, the quaternions and the octonions.

*Proof.* The differential of $L_x$ at the identity is an isomorphism $T_{e_0}S\cong\mathbb{R}^7\to T_xS$, and the eight vector fields $x\mapsto x e_k$ for $k = 1,\dots,7$ are everywhere independent and tangent, since $\langle x,xe_k\rangle = \lvert x\rvert^2\langle e_0,e_k\rangle = 0$. The theorem of Adams is quoted as standard. $\square$

**Proposition.** The volume of the unit sphere $S^7\subset\mathbb{R}^8$ in the Euclidean metric is

$$
\operatorname{vol}(S^7) = \frac{\pi^4}{3},
$$

and the volume of the unit ball of $\mathbb{O}$ is $\pi^4/24$.

*Proof.* The standard formula $\operatorname{vol}(S^{n}) = 2\pi^{(n+1)/2}/\Gamma((n+1)/2)$ at $n = 7$ gives $2\pi^4/\Gamma(4) = 2\pi^4/6 = \pi^4/3$; the ball's volume is that of $S^7$ divided by $8$, by the formula $\operatorname{vol}(B^n) = \operatorname{vol}(S^{n-1})/n$. $\square$

### The Exponential

**Definition.** For $x\in\mathbb{O}$ the **exponential** is the sum of the convergent series

$$
e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!},
$$

where $x^n$ is the left-associated power $x^n = x(\cdots(xx))$; the power is unambiguous because all powers of a single element lie in the associative subalgebra generated by $x$ (Artin's theorem).

**Theorem.** The exponential converges for every $x$ and satisfies $\lvert e^x\rvert = e^{\operatorname{Sc}(x)}$. For an imaginary octonion $u$ the formula

$$
e^{u} = \cos\lvert u\rvert + \frac{u}{\lvert u\rvert}\sin\lvert u\rvert
$$

holds, and the exponential maps $\operatorname{Im}\mathbb{O}$ onto $S^7$; the map is surjective and not injective, the fibres being the spheres $\{u : \lvert u\rvert = \theta,\ u/\lvert u\rvert = v\}$ for $v\in S^6$ and $e^{2\pi nv} = e_0$.

*Proof.* Convergence is absolute in the finite-dimensional normed space $\mathbb{O}$, and $e^x$ lies in the associative subalgebra generated by $x$, where the ordinary power-series laws hold; $\lvert e^x\rvert = e^{\operatorname{Sc}(x)}$ follows by comparing the series with the scalar exponential. For imaginary $u$, the subalgebra generated by $u$ is $\mathbb{R}\oplus\mathbb{R}u\cong\mathbb{C}$, so the complex exponential formula applies with $u$ in place of $i\theta$; this gives the displayed formula and shows $\lvert e^u\rvert = 1$. Surjectivity: a unit octonion is $x = \alpha + v$ with $\alpha\in\mathbb{R}$, $v\in\operatorname{Im}\mathbb{O}$ and $\alpha^2 + \lvert v\rvert^2 = 1$, so $x = \cos\theta + (v/\lvert v\rvert)\sin\theta$ with $\theta = \arccos\alpha\in[0,\pi]$, and $v\neq0$ or $\alpha = \pm1$; in the first case $x = e^{\theta v/\lvert v\rvert}$, in the second $x = \pm e_0$. $\square$

The exponential exhibits the unit sphere as the image of a single function of the imaginary space, and gives a clean parametrisation of the units other than $-e_0$; the failure of injectivity is the periodicity of the exponential along each radial line, exactly as for the complex numbers.

## The Norm Form and the Classification of the Real Division Algebras

**Theorem (Hurwitz, 1898).** Let $A$ be a finite-dimensional real algebra with identity and with a positive definite quadratic form $q$ satisfying $q(xy) = q(x)q(y)$ for all $x,y$ and whose polar form satisfies $\langle xy,xz\rangle = q(x)\langle y,z\rangle$. Then $A$ is isomorphic to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ or $\mathbb{O}$.

*Proof.* The theorem is standard; it is proved by the Cayley–Dickson induction, at each step either doubling a composition algebra or producing a zero divisor, and the induction terminates at dimension eight. The standard references are listed in the Further Reading; the corpus states the general theory of composition algebras in *Quadratic Forms over Algebras and Norm Forms* and the classification over $\mathbb{R}$ in *Normed Division Algebras and the Hurwitz Theorem*, written in parallel. $\square$

**Corollary.** The octonions are the largest normed division algebra over $\mathbb{R}$. Every composition algebra over $\mathbb{R}$ of dimension greater than eight has zero divisors; in particular the sedenions $\mathrm{CD}(\mathbb{O})$ of dimension sixteen contain non-zero $x,y$ with $xy = 0$, and their norm form is not multiplicative.

*Proof.* Hurwitz's theorem plus the failure of multiplicativity in the next Cayley–Dickson double. $\square$

| Algebra | Dimension | Norm form | Multiplicative | Division | Zero divisors |
|---|---|---|---|---|---|
| $\mathbb{R}$ | $1$ | $x^2$ | yes | yes | none |
| $\mathbb{C}$ | $2$ | $x_0^2 + x_1^2$ | yes | yes | none |
| $\mathbb{H}$ | $4$ | $x_0^2 + x_1^2 + x_2^2 + x_3^2$ | yes | yes | none |
| $\mathbb{O}$ | $8$ | $\sum_{k=0}^{7}x_k^2$ | yes | yes | none |
| $\mathrm{CD}(\mathbb{O})$ | $16$ | $\sum_{k=0}^{15}x_k^2$ | no | no | many |

The table is the octonion entry of the register of number systems that this Part traverses one system at a time: the norm form is positive definite for the four composition algebras, becomes the split complex valued form $N$ for the split biquaternions, and loses multiplicativity at the sedenions.

## Summary

The octonion algebra carries a positive definite quadratic form $\lvert x\rvert^2 = x\bar x = \bar xx = \sum_{k=0}^{7}x_k^2$, whose polar form is the Euclidean inner product $\langle x,y\rangle = \operatorname{Sc}(x\bar y) = \sum_kx_ky_k$ and whose associated bilinear form is invariant under multiplication: $\langle xy,xz\rangle = \lvert x\rvert^2\langle y,z\rangle$ and $\langle xy,zy\rangle = \langle x,z\rangle\lvert y\rvert^2$. The norm is multiplicative, $\lvert xy\rvert^2 = \lvert x\rvert^2\lvert y\rvert^2$, and this is the eight-square identity of Degen: the product of two sums of eight squares is again a sum of eight squares, with integral coefficients.

Every non-zero octonion is invertible, with $x^{-1} = \bar x/\lvert x\rvert^2$, and inversion is an anti-automorphism, $(xy)^{-1} = y^{-1}x^{-1}$; the algebra is a division algebra. The unit sphere $S^7 = \{\lvert x\rvert = 1\}$ is closed under multiplication and inversion and is a Moufang loop which is not a group, the defect of associativity on units being $2$ for the triple $e_1,e_4,e_2$; it is parallelizable, of volume $\pi^4/3$, and left multiplication embeds it in $SO(8)$ as a simply transitive family of isometries. For an imaginary octonion $u$ one has $e^u = \cos\lvert u\rvert + (u/\lvert u\rvert)\sin\lvert u\rvert$, and the exponential maps $\operatorname{Im}\mathbb{O}$ onto $S^7$. By Hurwitz's theorem the octonions are the largest real composition algebra and the largest normed division algebra; the two-square, four-square and eight-square identities exist and the sixteen-square identity does not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{O}$ | The octonion algebra, $\dim_{\mathbb{R}} = 8$ |
| $e_0 = 1, e_1,\dots,e_7$ | Orthonormal basis, $e_k^2 = -e_0$ for $k\geq1$ |
| $\bar{x}$ | Conjugation, $\overline{xy} = \bar y\bar x$ |
| $\lvert x\rvert^2 = x\bar x = \bar xx = \sum_kx_k^2$ | The octonion norm form, positive definite |
| $\langle x,y\rangle = \sum_kx_ky_k = \operatorname{Sc}(x\bar y)$ | Polar (Euclidean) form on $\mathbb{O}$ |
| $L_x$, $R_x$ | Left and right multiplication by $x$ |
| $x^{-1} = \bar x/\lvert x\rvert^2$ | Two-sided inverse |
| $S^7 = \{\lvert x\rvert = 1\}$ | Unit sphere, a Moufang loop |
| $e^x = \sum_nx^n/n!$ | Octonion exponential |
| $\mathrm{CD}(A) = A\oplus A$ | Cayley–Dickson double; $\mathrm{CD}(\mathbb{O})$ the sedenions |
| $SO(8)$ | Contains $L_u$ and $R_u$ for unit $u$ |



## Further Reading

- Adolf Hurwitz, "Über die Composition der quadratischen Formen von beliebig vielen Variabeln", *Nachrichten von der Königlichen Gesellschaft der Wissenschaften zu Göttingen* (1898), 309–316, for the classification of composition algebras and the octonion case.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for composition algebras, the Cayley–Dickson process and the proof that the sixteen-square identity fails.
- John C. Baez, "The octonions", *Bulletin of the American Mathematical Society* **39** (2002), 145–205, for the eight-square identity, the unit sphere as a Moufang loop and the parallelizability of $S^7$.
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000), for the norm form and its invariance properties.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the inner product invariance, the embedding of $S^7$ in $SO(8)$ and the exceptional structure.
- John Frank Adams, "On the non-existence of elements of Hopf invariant one", *Annals of Mathematics* **72** (1960), 20–104, for the theorem that only $S^1$, $S^3$ and $S^7$ are parallelizable.
