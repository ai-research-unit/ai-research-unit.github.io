
# __Split-Quaternion Analysis on Subspaces__

## Introduction

This article develops the analysis of the distinguished subspaces of the split-quaternion algebra. It lists the subspaces cut out by the involutions of the algebra, writes the differential operator carried by each, compares the operators and their types, relates the idempotent decomposition to the subspaces, and describes the role of the zero divisors on each.

The split-quaternion algebra, its involutions, its idempotents and its subspaces are assumed from *Split-Quaternion Algebra*; the forms on the subspaces from the same article and from *Split-Quaternion Norm and Invertibility*; the zero divisors and the isotropic lines from *Split-Quaternion Zero Divisors*; the metric, the operators and the failure of the naive derivative from *Split-Quaternion Analysis*. The two-dimensional hyperbolic analysis is that of *Split-Complex Integration*, the definite analysis of the plane that of *Several Complex Variables*, and the elliptic operator theory of the definite case that of *Clifford Analysis* and *Dirac Operators*. The skeleton follows the sibling article *Split-Biquaternion Analysis on Subspaces*, named only, which performs the same task for the eight-dimensional algebra; no result of it is used. Nothing physical is invoked.

## The Subspaces and the Involutions

**Definition.** The subspaces considered here are the following.

| Subspace | Description | Form $N$ restricted | Character |
|---|---|---|---|
| $S$ | the scalars, $\operatorname{span}\{1\}$ | $a^2$ | definite |
| $\mathbb{R}[e_1]$ | $\operatorname{span}\{1, e_1\} \cong \mathbb{C}$ | $a^2 + b^2$ | definite |
| $\mathbb{D}_2$ | $\operatorname{span}\{1, e_2\} \cong \mathbb{D}$ | $a^2 - c^2$ | indefinite of signature $(1,1)$ |
| $\mathbb{D}_3$ | $\operatorname{span}\{1, e_3\} \cong \mathbb{D}$ | $a^2 - d^2$ | indefinite of signature $(1,1)$ |
| $V$ | the vectors, $\operatorname{span}\{e_1,e_2,e_3\}$ | $b^2 - c^2 - d^2$ | indefinite of signature $(2,1)$ |

**Theorem (The Subspaces Cut Out by the Three Involutions).** The conjugation $\bar{\cdot}$, the principal involution $\alpha$ and the reversal $\rho$ of (*Split-Quaternion Algebra*, §*The Conjugation* and §*The Other Two Involutions*) cut the algebra into the following Hermitian and anti-Hermitian parts.

| Involution | Type | Fixed subspace | Anti-fixed subspace |
|---|---|---|---|
| conjugation $\bar{\cdot}\, = \alpha\rho$ | anti-automorphism | $S = \mathbb{R}\cdot 1$ | $V$ |
| principal involution $\alpha$ | automorphism | $\operatorname{span}\{1, e_3\}$ | $\operatorname{span}\{e_1, e_2\}$ |
| reversal $\rho$ | anti-automorphism | $\operatorname{span}\{1, e_1, e_2\}$ | $\operatorname{span}\{e_3\}$ |

The three involutions commute, and their common eigenspaces are $\mathbb{R}\cdot 1$, $\operatorname{span}\{e_1,e_2\}$ and $\mathbb{R} e_3$; they do not separate $e_1$ from $e_2$, because on $\operatorname{span}\{e_1,e_2\}$ all three act as $-1$.

**Proof.** The sign patterns and the commutativity are computed in (*Split-Quaternion Algebra*, §*The Other Two Involutions*), where it is also recorded that $\alpha$ and $\rho$ agree on $\operatorname{span}\{e_1,e_2\}$ and that this plane is therefore a common eigenspace rather than two. The Hermitian and anti-Hermitian parts are the $+1$ and $-1$ eigenspaces, and the type of each involution, automorphism or anti-automorphism, is recorded there. $\square$

**Corollary (Two Meanings of Hermitian).** With respect to the conjugation, the Hermitian part of the algebra is the scalar line and the anti-Hermitian part is the vector subspace; with respect to the reversal, the Hermitian part is the three-dimensional subspace $\operatorname{span}\{1,e_1,e_2\}$ and the anti-Hermitian part is the line $\mathbb{R} e_3$. The two readings give different decompositions and both are used below, with the involution named each time.

**Proof.** Immediate from the table. $\square$

## The Operators on the Split-Complex Subspaces

**Definition.** On a two-dimensional subspace with coordinates $(s,t)$ and generators of the form $g$ with $g^2 = \pm 1$, the **conjugate pair of first-order operators** is

$$
\partial_s + g\,\partial_t, \qquad \partial_s - g\,\partial_t .
$$

**Theorem (The Definite Plane).** On the plane $\mathbb{R}[e_1] = \operatorname{span}\{1,e_1\} \cong \mathbb{C}$ with the definite form $a^2+b^2$, the conjugate pair is $\partial_a \pm e_1\partial_b$ and

$$
(\partial_a + e_1\partial_b)(\partial_a - e_1\partial_b) = \partial_a^2 + \partial_b^2 = \Delta ,
$$

the Laplacian of the plane. The operator is elliptic, there are no zero divisors on the plane, and the kernel of $\partial_a + e_1\partial_b$ is the space of holomorphic functions of $z = a + b e_1$, in the sense of *Several Complex Variables*.

**Proof.** The product is computed with $e_1^2 = -1$ and the commutation of the partial derivatives: the cross terms cancel and the diagonal terms add. Ellipticity is the definiteness of the form, and the absence of zero divisors on the plane is (*Split-Quaternion Norm and Invertibility*, §*The Three-Way Classification*). $\square$

**Theorem (The Split-Complex Planes).** On the plane $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ with the indefinite form $a^2-c^2$, the conjugate pair is $\partial_a \pm e_2\partial_c$ and

$$
(\partial_a + e_2\partial_c)(\partial_a - e_2\partial_c) = \partial_a^2 - \partial_c^2 = \Box_{(1,1)},
$$

the one-dimensional wave operator of signature $(1,1)$. The operator is hyperbolic; its characteristic variety is the pair of isotropic lines $\mathbb{R}(1 \pm e_2)$, which is exactly the zero divisor set of the plane. The same statements hold on $\mathbb{D}_3$ with $c$ replaced by $d$.

**Proof.** The product is computed with $e_2^2 = +1$; the characteristic variety of the symbol $\xi_a \pm e_2\xi_c$ is $\xi_a^2 - \xi_c^2 = 0$, the two isotropic lines, which are the zero divisors of the plane by *Split-Quaternion Zero Divisors*, §*The Two Families in the Algebra*. $\square$

## The Operators on the Vector Subspace

**Theorem (The Vector Operator).** On the vector subspace with coordinates $(b,c,d)$ and basis $e_1,e_2,e_3$, the operator

$$
D = e_1\,\frac{\partial}{\partial b} + e_2\,\frac{\partial}{\partial c} + e_3\,\frac{\partial}{\partial d}
$$

satisfies

$$
D^2 = -\frac{\partial^2}{\partial b^2} + \frac{\partial^2}{\partial c^2} + \frac{\partial^2}{\partial d^2} = \Box_{(2,1)},
$$

the wave operator of signature $(2,1)$, which is hyperbolic. The first-order operator $D$ is not elliptic: its symbol is left multiplication by the frequency vector $\xi = \xi_b e_1 + \xi_c e_2 + \xi_d e_3$, invertible exactly when $N(\xi) \neq 0$, so the set where the symbol degenerates — its characteristic variety — is the null cone $b^2-c^2-d^2=0$, which is the zero divisor set of the vector subspace. There is no elliptic theory on the subspace, and the first-order system $Df = 0$ is not the scalar wave equation: its kernel is large, as *Split-Quaternion Integration*, §*The Kernel of the Vector Operator*, records.

**Proof.** This is (*Split-Quaternion Analysis*, §*The Differential Operators*), where the cancellation of the cross terms and the identification of the characteristic variety are proved. $\square$

**Corollary (The Operators Are of the Forms of the Subspaces).** The type of the operator on a subspace is determined by the signature of the form on that subspace: elliptic when the form is definite, hyperbolic when it is indefinite, and the characteristic variety is the null cone of the form, which is the zero divisor set of the subspace.

**Proof.** The symbol of the operator is the linear form on the subspace with values in the Clifford algebra of the form; its square is the quadratic form, so the characteristic variety is the null cone; definiteness makes the operator elliptic by definition, and indefiniteness makes the variety a cone and the operator hyperbolic. $\square$

## The Operators on the Hermitian and Anti-Hermitian Subspaces

**Theorem (The Two Decompositions and Their Operators).** For the conjugation the algebra splits as $S \oplus V$; the operator carried by the Hermitian part $S$ is the single derivative $\partial_a$ and the operator carried by the anti-Hermitian part $V$ is the vector operator $D$. For the reversal the Hermitian part is $\operatorname{span}\{1,e_1,e_2\}$ with the inherited form $a^2+b^2-c^2$ of signature $(2,1)$, and the anti-Hermitian part is the line $\mathbb{R}e_3$ with the negative-definite form $-d^2$; the operators are

$$
D^{\rho}_{+} = e_2\partial_a + e_3\partial_b + e_1\partial_c, \qquad D^{\rho}_{-} = e_1\partial_d,
$$

with $(D^{\rho}_+)^2 = \partial_a^2 + \partial_b^2 - \partial_c^2$, the Laplacian of the inherited form, and $(D^{\rho}_-)^2 = -\partial_d^2$, the Laplacian of the negative-definite line.

**Proof.** The decomposition for the conjugation is (*Split-Quaternion Algebra*, §*The Two Eigenspaces*), and the operator on $V$ is the theorem above; for the reversal the eigen-subspaces are those of the table in the first section, and the operators are formed from a Clifford system adapted to the sign pattern of each inherited form, as in the construction of the conjugate pair. $\square$

**Corollary (The Idempotents Lie in a Split-Complex Plane).** The idempotents are

$$
u_{\pm} = \tfrac12(1 \pm e_2) \in \mathbb{D}_2,
$$

and they lie in the split-complex plane, not in the Hermitian part of the conjugation and not in a definite subspace. Their products vanish, $u_+u_- = 0$, and each generates a minimal left ideal.

**Proof.** The formula is (*Split-Quaternion Algebra*, §*The Idempotents*), and the vanishing of the product follows from $e_2^2 = 1$. $\square$

## The Idempotent Decomposition and the Subspaces

**Theorem (The Peirce Decomposition).** With $u_{\pm} = \tfrac12(1\pm e_2)$, every element decomposes as

$$
x = u_+ x u_+ + u_+ x u_- + u_- x u_+ + u_- x u_- ,
$$

the four **Peirce components** being one-dimensional real subspaces; the decomposition is the matrix-entry decomposition of *Split-Quaternion Analysis*, §*The Calculus in the Peirce Coordinates*, and the algebra is not the product of the two ideals, because the off-diagonal Peirce components do not vanish.

**Proof.** The decomposition of the identity and the vanishing of $u_+u_-$ give the direct sum; the non-vanishing of the mixed terms $u_+xu_-$ is the statement that $M_2(\mathbb{R})$ is not a product ring, and the identification with the entries is (*Split-Quaternion Matrix Representations*, §*The Image as a Linear Subspace*). $\square$

**Corollary (The Subspaces Against the Idempotents).** The individual Peirce projections do not preserve $V$; they map it onto the four lines

$$
u_+Vu_+ = \mathbb{R} u_+, \qquad u_-Vu_- = \mathbb{R} u_-, \qquad u_+Vu_- = \mathbb{R}(e_1-e_3), \qquad u_-Vu_+ = \mathbb{R}(e_1+e_3),
$$

and the first two of these are not contained in $V$, because $u_\pm = \tfrac12(1\pm e_2)$ has scalar part $\tfrac12$. The two *sums* $u_+\cdot u_+ + u_-\cdot u_-$ and $u_+\cdot u_- + u_-\cdot u_+$ do preserve $V$, and they give the orthogonal splitting of the vector subspace

$$
V = \mathbb{R} e_2 \;\perp\; \operatorname{span}\{e_1,e_3\},
$$

whose first summand is the $e_2$-axis of the split-complex plane $\mathbb{D}_2$, on which the form takes the value $-1$, and whose second summand is the hyperbolic plane of the form $b^2-d^2$, of signature $(1,1)$, carrying the two isotropic lines $\mathbb{R}(e_1\pm e_3)$; these two null lines are exactly the off-diagonal Peirce lines, and they are the traces in $V$ of the isotropic planes of *Split-Quaternion Zero Divisors*, §*The Two Families in the Algebra*.

**Proof.** The Peirce components of a vector $v = be_1 + ce_2 + de_3$ are computed from the multiplication table. For $e_1$: $u_+e_1u_+ = 0$, $u_+e_1u_- = \tfrac12(e_1-e_3)$, $u_-e_1u_+ = \tfrac12(e_1+e_3)$, $u_-e_1u_- = 0$. For $e_3$: $u_+e_3u_+ = 0$, $u_+e_3u_- = \tfrac12(e_3-e_1) = -\tfrac12(e_1-e_3)$, $u_-e_3u_+ = \tfrac12(e_1+e_3)$, $u_-e_3u_- = 0$. For $e_2$: $u_+e_2u_+ = u_+$, $u_+e_2u_- = 0$, $u_-e_2u_+ = 0$, $u_-e_2u_- = -u_-$. Hence

$$
u_+vu_+ + u_-vu_- = c\,(u_+ - u_-) = c\,e_2, \qquad u_+vu_- + u_-vu_+ = \tfrac{b-d}{2}(e_1-e_3) + \tfrac{b+d}{2}(e_1+e_3) = be_1 + de_3,
$$

so the two sums return $v$ and the individual projections do not; the lines displayed are read off the same products, and the splitting is orthogonal because $B(e_2,e_1) = B(e_2,e_3) = 0$. The traces are the left ideal $\mathbb{H}_{\mathrm{s}}u_+ = \operatorname{span}\{u_+, \tfrac12(e_1+e_3)\}$ and the right ideal $u_+\mathbb{H}_{\mathrm{s}}$, intersected with $V$: the vector $\tfrac12(e_1+e_3)$ is null, which gives the line $\mathbb{R}(e_1+e_3)$. $\square$

## The Role of the Zero Divisors on Each Subspace

**Theorem (The Zero Divisors Subspace by Subspace).** The zero divisors and the nilpotents of each subspace are as follows.

| Subspace | Zero divisors | Nilpotents |
|---|---|---|
| $S$ | none | none |
| $\mathbb{R}[e_1] \cong \mathbb{C}$ | none | none |
| $\mathbb{D}_2$ | the two isotropic lines $\mathbb{R}(1 \pm e_2)$ | yes, of the form $p(1 \mp e_2)$ with suitable $p$ |
| $\mathbb{D}_3$ | the two isotropic lines $\mathbb{R}(1 \pm e_3)$ | yes |
| $V$ | the light cone $b^2 = c^2+d^2$ | yes, the lightlike vectors |

The characteristic variety of the operator of a subspace is exactly the zero divisor set of that subspace, so the operator degenerates precisely where the algebra degenerates.

**Proof.** The definite subspaces have no zero divisors by (*Split-Quaternion Norm and Invertibility*, §*The Three-Way Classification*); the split-complex planes and the vector subspace have the null lines and the light cone as their zero divisors by *Split-Quaternion Zero Divisors*, §*The Two Families in the Algebra* and §*Nonzero Nilpotents*; the identification with the characteristic varieties is the corollary on the types of the operators. $\square$

**Corollary (The Definite Subspaces Are the Elliptic Islands).** The only subspaces on which the analysis is elliptic, with a Cauchy–Riemann operator and holomorphic functions, are the definite ones, the scalar line and the complex plane $\mathbb{R}[e_1]$; on every indefinite subspace the analysis is hyperbolic and the operator has the zero divisors as its characteristic directions.

**Proof.** The operators are elliptic exactly on the definite subspaces by the corollary on the types, and the elliptic theory on the complex plane is the classical one of *Several Complex Variables*. $\square$

## The Domains of the Operators

**Definition.** A hypersurface of the vector subspace or of a coordinate plane is **characteristic** for the operator of that subspace when its normal is null for the inherited form, and **non-characteristic** otherwise.

**Theorem (Non-Characteristic Restrictions).** On a non-characteristic hypersurface the vector operator restricts to an operator of the induced metric: on a sheet of the hyperboloid $N=1$ in $V$ the operator restricts to the Dirac operator of the Riemannian metric $-B$ on the sheet, and on a piece of a non-null plane the operator restricts to the operator of the induced form. On a characteristic hypersurface the induced form is degenerate, there is no induced metric, and the restricted operator loses its principal part.

**Proof.** The decomposition of the operator along a hypersurface separates the normal derivative, whose symbol is the normal vector, from the tangential part; when the normal is non-null the normal derivative can be eliminated and the tangential part is the operator of the induced form, exactly as in the restriction of the metric in (*Split-Quaternion Geometry*, §*The Unit Hyperboloids and Their Metrics*). When the normal is null the induced form is degenerate by *Split-Quaternion Norm and Invertibility*, §*Isotropy*. $\square$

**Corollary (The Cauchy Problem and Its Domains).** The operator whose initial-value problem is well posed on non-characteristic hypersurfaces is the second-order wave operator $\Box_{(2,1)} = D^2$: for the split-complex plane it is the Cauchy problem for the one-dimensional wave equation, with the two characteristic lines as the boundaries of the domains of determination, and for the vector subspace it is the Cauchy problem for the wave equation of signature $(2,1)$, with the light cone as the characteristic cone. The hyperboloids are non-characteristic and carry initial data; the cone itself is characteristic and carries none. The first-order system $Df = 0$ is a different and much more restrictive problem, and does not inherit that well-posedness: every solution of $Df = 0$ solves the wave equation, but the class is proper — the scalar function $bc$ solves $\Box_{(2,1)}f = 0$ with $Df = ce_1+be_2 \neq 0$ — and the kernel of $D$ contains the two transported families $u_+h(b-d)$ and $h(b+d)u_-$, for every smooth $h$, together with nonzero compactly supported solutions.

**Proof.** The characteristic hypersurfaces are those with null normal, by the preceding theorem; the implication $Df = 0 \Rightarrow \Box_{(2,1)}f = 0$ is $D^2 = \Box_{(2,1)}$, the properness is the displayed counterexample, and the domains of dependence for the wave equation are the usual ones. The kernel statement is the computation of *Split-Quaternion Integration*, §*The Kernel of the Vector Operator*, and it shows that the first-order constraint is not implied by the wave equation, so the two problems are distinct. $\square$

## Comparison of the Subspaces and Relation Between Them

### The Summary of the Operators

| Subspace | Dimension | Form | Operator | Square or product | Type |
|---|---|---|---|---|---|
| $S$ | $1$ | $a^2$ | $\partial_a$ | $\partial_a^2$ | elliptic |
| $\mathbb{R}[e_1]$ | $2$ | $a^2+b^2$ | $\partial_a \pm e_1\partial_b$ | $\Delta$ | elliptic |
| $\mathbb{D}_2$ | $2$ | $a^2-c^2$ | $\partial_a \pm e_2\partial_c$ | $\Box_{(1,1)}$ | hyperbolic |
| $\mathbb{D}_3$ | $2$ | $a^2-d^2$ | $\partial_a \pm e_3\partial_d$ | $\Box_{(1,1)}$ | hyperbolic |
| $V$ | $3$ | $b^2-c^2-d^2$ | $D$ | $\Box_{(2,1)}$ | hyperbolic |
| $\operatorname{span}\{1,e_1,e_2\}$ | $3$ | $a^2+b^2-c^2$ | $D^{\rho}_+$ | $\partial_a^2+\partial_b^2-\partial_c^2$ | hyperbolic |
| $\mathbb{R} e_3$ | $1$ | $-d^2$ | $D^{\rho}_-$ | $-\partial_d^2$ | elliptic |

The relations between the operators are the relations between the forms: each operator on a subspace is the restriction of the ambient operator to the coordinates of the subspace, and the square of the vector operator is the sum of the squares of the operators on the coordinate lines with the signs of the generators, which is the statement that the form of the whole is the orthogonal sum of the forms of the pieces. The idempotent decomposition cuts the algebra in the split-complex direction and is not the same as any of the involutive decompositions; it is the decomposition that makes the algebra a matrix algebra and its analysis an entrywise analysis.

## Summary

The subspaces of the split-quaternion algebra are cut out in two ways: by the coordinate subalgebras, the scalar line, the definite complex plane $\mathbb{R}[e_1]$ and the split-complex planes $\mathbb{D}_2$, $\mathbb{D}_3$, together with the vector subspace $V$; and by the three mutually commuting involutions, whose Hermitian and anti-Hermitian parts give the scalar–vector splitting for the conjugation, the $\operatorname{span}\{1,e_3\}$–$\operatorname{span}\{e_1,e_2\}$ splitting for the principal involution, and the $\operatorname{span}\{1,e_1,e_2\}$–$\mathbb{R}e_3$ splitting for the reversal.

On each subspace the analysis is governed by the Clifford operator of the inherited form. On the definite subspaces, the scalar line and the complex plane, the operator pair $\partial_a \pm e_1\partial_b$ multiplies to the Laplacian and the analysis is elliptic, with holomorphic functions. On the indefinite subspaces, the split-complex planes and the vector subspace, the operator pair multiplies to the one-dimensional wave operator and the vector operator squares to the wave operator of signature $(2,1)$, and the analysis is hyperbolic, with the zero divisors as the characteristic directions. The type of the operator is determined by the signature of the form and by nothing else.

The idempotents $u_\pm = \tfrac12(1\pm e_2)$ lie in the split-complex plane $\mathbb{D}_2$ and give the Peirce decomposition, which is the matrix-entry decomposition and not a product decomposition. The subspace of a given signature contains zero divisors exactly when its form is indefinite, and the characteristic variety of its operator is then exactly that zero divisor set. The operators of the definite case are those of *Clifford Analysis*, and the two-dimensional hyperbolic case is that of *Split-Complex Integration*.

Finally, the domain on which each operator is analysed is constrained by its type. The Cauchy problem is posed on non-characteristic hypersurfaces, and for the indefinite subspaces the characteristic hypersurfaces are exactly the level sets of the null cone; the hyperboloids are non-characteristic and carry initial data, and on them the vector operator restricts to the Dirac operator of the induced Riemannian metric. On the characteristic hypersurfaces the induced form degenerates and the restricted operator loses its principal part, which is the analytic face of the presence of the zero divisors. For the first-order system $Df = 0$ the analysis is a transport theory along the null directions rather than an initial-value theory: the solutions include the functions transported along the null directions, and the system has neither the well-posedness of the wave equation nor the rigidity of the elliptic case.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $S$, $V$ | the Hermitian and anti-Hermitian parts for the conjugation | *Split-Quaternion Algebra* |
| $\alpha$, $\rho$ | the principal involution and the reversal | *Split-Quaternion Algebra* |
| $\mathbb{R}[e_1] \cong \mathbb{C}$ | the definite plane, with the Laplacian pair | this article |
| $\mathbb{D}_2$, $\mathbb{D}_3$ | the split-complex planes, with the wave pairs | this article |
| $\partial_a \pm g\partial_t$ | the conjugate pair on a coordinate plane | this article |
| $D = e_1\partial_b + e_2\partial_c + e_3\partial_d$ | the vector operator | *Split-Quaternion Analysis* |
| $\Box_{(1,1)}$, $\Box_{(2,1)}$, $\Delta$ | the wave operators and the Laplacian | this article |
| $u_\pm$, Peirce components | the idempotents and the matrix-entry decomposition | *Split-Quaternion Analysis* |
| zero divisors of a subspace | the null cone of the inherited form | *Split-Quaternion Zero Divisors* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the Clifford operators of forms of each signature and the elliptic–hyperbolic dichotomy.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the elliptic case and the functions in its kernel.
- Gerald B. Folland, *Introduction to Partial Differential Equations*, 2nd ed. (Princeton University Press, 1995), for the wave operator, its factorisation and its characteristic variety.
- Steven G. Krantz, *Function Theory of Several Complex Variables*, 2nd ed. (American Mathematical Society, 2001), for the holomorphic functions of the definite plane and the Cauchy–Riemann operator in one and several variables.
