# __The Reduced Biquaternion Mandelbrot Set and the Connectedness Locus__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ of basis $1,i,j,ij$, with element $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ in the two central idempotents, and with the quadratic family $F_{C}(\breve Q)=\breve Q^{2}+C$ whose filled Julia set, in the idempotent coordinates $C=c_{1}\Pi_++c_{2}\Pi_-$, is the product

$$
\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}}.
$$

The **connectedness locus** of the family is the set of parameters whose filled Julia set is connected; in the complex quadratic family this locus is the Mandelbrot set. The article identifies the connectedness locus of the reduced biquaternion family, reads the escape-time algorithm and its exactness, describes the role of the zero divisors in the singular parameters and the singular slices, and compares the situation with the non-commutative companion.

The result is that the connectedness locus is the product of the Mandelbrot set with itself, that the escape-time algorithm is exact and decomposes into the two complex algorithms, and that there is no obstruction to the theory. The reduced biquaternion Mandelbrot set is therefore the square of the complex Mandelbrot set, a set in the two-dimensional complex parameter space; its complex line slices are degenerate, its real slices are intersections of the Mandelbrot set with translates of itself, and the bifurcation locus is the union of the two products of a boundary with the whole. The zero divisors enter through the critical set, which is the zero-divisor cone, and through the parameters whose critical orbit meets it.

The article owns the connectedness locus, the bifurcation locus, the escape-time algorithm and its exactness, the singular parameters and the singular slices. The fractal and its product structure are *The Reduced Biquaternion Quadratic Map and Its Julia Sets*; the global decomposition is *The Idempotent Decomposition and the Split Fractal*; the slices are *The Slices of the Reduced Biquaternion Julia Sets*; the dimension is *The Hausdorff Dimension of the Reduced Biquaternion Julia Sets*; the zero divisors are *Zero Divisors of the Algebra of the Reduced Biquaternions*; the topological norm that measures the escape is *Topology and Metric for Each of the Operations*. The companion is *The Biquaternion Mandelbrot Set and the Connectedness Locus*, where the escape criterion meets an obstruction.

**Conventions.** The complex quadratic map of parameter $c$ is $f_{c}(\zeta)=\zeta^{2}+c$, with filled Julia set $K_{c}$, Julia set $J_{c}$ and Mandelbrot set $\mathcal{M}=\{c:K_{c}\text{ connected}\}$; the reduced biquaternion family is parametrised by $C=c_{1}\Pi_++c_{2}\Pi_-$; the topological norm is $K(\breve Q)=\tfrac12(|Q_{+}|^{2}+|Q_{-}|^{2})$.

## The Mandelbrot Set of the Complex Family

**Proposition (the complex locus).** For the complex quadratic family the connectedness locus is the Mandelbrot set

$$
\mathcal{M}=\{c\in\mathbb{C}:K_{c}\text{ is connected}\}=\bigl\{c:\text{the orbit of }0\text{ under }f_{c}\text{ is bounded}\bigr\},
$$

which is compact, connected and full, of interior the union of the hyperbolic components and of boundary the bifurcation locus of the family.

**Proof.** This is the standard theory of the complex quadratic family, cited and not restated; the two descriptions agree because the filled Julia set is connected exactly when the critical orbit does not escape.

## The Connectedness Locus of the Reduced Biquaternion Family

**Theorem (the locus is the product).** The connectedness locus of the reduced biquaternion quadratic family is

$$
\mathfrak{M}=\{C:\mathcal{K}_{C}\text{ is connected}\}=\{C:c_{1}\in\mathcal{M}\text{ and }c_{2}\in\mathcal{M}\}=\mathcal{M}\times\mathcal{M},
$$

the product of the Mandelbrot set with itself, read in the idempotent coordinates.

**Proof.** The filled Julia set is the product $K_{c_{1}}\times K_{c_{2}}$, and a product of two non-empty compact sets is connected exactly when both factors are connected and non-empty; the factors are non-empty always, so connectivity of $\mathcal{K}_{C}$ is the conjunction of the two complex connectivities, which is the product statement.

**Corollary (the elementary properties).** The locus $\mathfrak{M}$ is compact, connected and full in the complex two-space; its boundary is the union of the two products of a boundary with the whole,

$$
\partial\mathfrak{M}=\bigl(\partial\mathcal{M}\times\mathcal{M}\bigr)\cup\bigl(\mathcal{M}\times\partial\mathcal{M}\bigr),
$$

and the same formula holds for the boundary of the locus inside the product.

**Proof.** The product of two compact connected full sets is compact, connected and full; the boundary of a product is the union of the two mixed products of a boundary and a set, by the same computation as for the Julia sets of *The Reduced Biquaternion Quadratic Map and Its Julia Sets*.

**Remark (the shape).** The locus is the square of a famous plane set, so its real dimension is four and its shape is the product shape; its complex line slices are degenerate, being empty or a translate of the Mandelbrot set, and its informative slices are the real two-dimensional ones, of which the diagonal $\{c_{1}=c_{2}\}$ is a copy of $\mathcal{M}$ itself and the translated lines $\{c_{2}=c_{1}+\mu\}$ are the intersections $\mathcal{M}\cap(\mathcal{M}-\mu)$ of the Mandelbrot set with its translates.

## The Bifurcation Locus

**Theorem (the bifurcation locus).** The parameter $C$ is a bifurcation parameter, that is the dynamics of $F_{C}$ is unstable in the sense that the critical orbit changes its qualitative behaviour under every neighbourhood, exactly when at least one of the two complex parameters is a bifurcation parameter of the complex family, that is exactly when

$$
C\in\bigl(\partial\mathcal{M}\times\mathbb{C}\bigr)\cup\bigl(\mathbb{C}\times\partial\mathcal{M}\bigr).
$$

**Proof.** The dynamics of $F_{C}$ is the product of the two complex dynamics, and a property of the product is stable exactly when it is stable in both factors, because the norm separates the two coordinates; so the instability occurs exactly when one factor is unstable, which is the displayed union.

**Corollary (the stratified picture).** The parameter space splits into the four regions according to the membership of the two coordinates in the interior, the boundary and the exterior of $\mathcal{M}$; the dynamics is hyperbolic in the region where both coordinates lie in the union of the complements of the boundary, and the bifurcation locus is the union of the two products of a boundary with the whole.

**Proof.** The classification of the complex parameter as attracting, indifferent or escaping is the classical one, and the product classification is the pair of the two.

## The Escape-Time Algorithm

**Theorem (the algorithm is exact and decomposes).** The orbit of $\breve Q=(Q_{+},Q_{-})$ under $F_{C}$ is bounded exactly when both coordinate orbits are bounded, and the numerical criterion is applied to each coordinate separately: with the standard escape radius $R$ of the complex family, if $|Q_{+}|>R$ or $|Q_{-}|>R$ after an iterate then the orbit escapes, and the membership of $C$ in the connectedness locus is decided coordinatewise.

**Proof.** The orbit is the pair of the coordinate orbits, and the norm $\langle\cdot\rangle_{\mathrm{ts}*}$ is unbounded exactly when one coordinate modulus is unbounded; the complex escape criterion $|\zeta|>R$ with $R$ the standard radius of the quadratic family is applied to each coordinate.

**Corollary (the computational picture).** The two-dimensional complex pictures of the reduced biquaternion locus are drawn from the two complex pictures of the Mandelbrot set; the algorithm does not need the algebra at all, only the two complex memberships, and the escape time of an element is the smaller of the escape times of its two coordinates.

**Proof.** The membership in the locus is the conjunction of the two memberships, and the escape time of an element is by definition the first iterate at which one coordinate exceeds the radius, which is the smaller of the two coordinate escape times.

## The Zero Divisors and the Singular Parameters

**Proposition (the critical set and the singular slices).** The derivative of $F_{C}$ is the multiplication by $2\breve Q$, singular exactly on the zero-divisor cone $\mathscr{Z}=\{Q_{+}=0\}\cup\{Q_{-}=0\}$ and vanishing only at the origin; the singular slices of the fractal are

$$
\mathcal{K}_{C}\cap\mathscr{Z}=\bigl(\{0\}\cap K_{c_{1}}\bigr)\times K_{c_{2}}\;\cup\;K_{c_{1}}\times\bigl(\{0\}\cap K_{c_{2}}\bigr),
$$

of the Hausdorff dimension of the surviving complex factor, at most two, and non-empty exactly when the corresponding coordinate parameter lies in $\mathcal{M}$.

**Proof.** This is the computation of *The Reduced Biquaternion Quadratic Map and Its Julia Sets*.

**Definition (the singular parameters).** A parameter is **singular** when the critical orbit of the origin meets the zero-divisor cone, that is when the origin belongs to one of the two coordinate critical orbits; the set of singular parameters is

$$
\mathfrak{S}=\bigl(C_{0}\times\mathbb{C}\bigr)\cup\bigl(\mathbb{C}\times C_{0}\bigr),\qquad C_{0}=\{c:f_{c}^{n}(0)=0\text{ for some }n\geq1\},
$$

$C_{0}$ being the set of centres of the hyperbolic components of the Mandelbrot set.

**Proof.** The critical orbit is $0\mapsto C\mapsto F_{C}(C)\mapsto\cdots$, and in the coordinates it is the pair of the two complex critical orbits; it meets the zero-divisor cone exactly when one of the two coordinate orbits returns to the origin, which is the definition of $C_{0}$ in the complex family.

**Remark (the effect of the zero divisors).** The zero divisors enter the fractal theory in three places: as the branching set of the square, where the inverse branches collapse; as the critical set, where the derivative loses invertibility; and as the singular parameters, where the critical orbit meets the critical set. In the reduced biquaternion algebra all three are the same cone of two complex planes, and its structure is the product structure of the algebra; the singular part of the fractal is of the dimension of a complex slice, whereas in the non-commutative companion the singular set is a genuine critical hypersurface.

## The Slices of the Locus

**Remark (the slices).** The slices of the locus are those of *The Slices of the Reduced Biquaternion Julia Sets*: the complex line slices are empty or copies of the Mandelbrot set, the central line $\{c_{1}=c_{2}\}$ is a copy of the Mandelbrot set, the conjugate line $\{c_{2}=\bar c_{1}\}$ is again a copy, and the translated lines give the intersections of the Mandelbrot set with its translates. The two-dimensional real slices are the informative ones, and they are the intersections of two copies of the Mandelbrot set, one for each coordinate.

## Comparison with the Biquaternion Case

**Remark (the obstruction).** The reduced biquaternion family has a connectedness locus, an escape-time algorithm and a slice theory, all exact, because the fractal is a product of two complex fractals and the complex theory is available for each factor. In the biquaternion algebra the corresponding family is not a product, the coupling term of the idempotent coordinates is nonzero, and the escape criterion and the connectedness locus are not known in the same generality; the reduced algebra is the case in which the obstruction disappears, and it disappears for the structural reason that the algebra is a direct product of two fields.

## Summary

The connectedness locus of the reduced biquaternion quadratic family is the product $\mathcal{M}\times\mathcal{M}$ of the Mandelbrot set with itself, its boundary is the union of the two mixed products of a boundary and the whole, and the bifurcation locus is the union of the two products of a boundary with the entire complex plane. The escape-time algorithm is exact and decomposes: the orbit of an element is bounded exactly when both coordinate orbits are, the criterion is applied coordinatewise, and the escape time of an element is the smaller of the two coordinate escape times. The critical set is the zero-divisor cone, where the derivative is singular, the singular slices of the fractal are products with one coordinate at the origin, of the dimension of the surviving complex factor and at most two, and the singular parameters are those whose critical orbit meets the cone, that is the products of the set of centres of the hyperbolic components with the whole plane. The slices of the locus reduce to the complex theory: complex line slices are degenerate, the central and the conjugate lines are copies of the Mandelbrot set, and the translated lines are intersections of the Mandelbrot set with its translates. In contrast with the non-commutative companion, there is no obstruction to the theory, the reason being that the algebra is a direct product of two fields and its dynamics is the product of two complex dynamics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F_{C}(\breve Q)=\breve Q^{2}+C$ | the quadratic map of the algebra |
| $\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}}$ | the filled Julia set as a product |
| $\mathcal{M}$ | the complex Mandelbrot set |
| $\mathfrak{M}=\mathcal{M}\times\mathcal{M}$ | the connectedness locus of the reduced biquaternion family |
| $\partial\mathfrak{M}=(\partial\mathcal{M}\times\mathcal{M})\cup(\mathcal{M}\times\partial\mathcal{M})$ | the boundary of the locus |
| $\mathscr{Z}=\{Q_{+}=0\}\cup\{Q_{-}=0\}$ | the critical set, the zero-divisor cone |
| $C_{0}$ | the complex parameters whose critical orbit returns to the origin, the centres |
| $\mathfrak{S}=(C_{0}\times\mathbb{C})\cup(\mathbb{C}\times C_{0})$ | the singular parameters |
| escape time | the smaller of the two coordinate escape times |

## Further Reading

- [The Reduced Biquaternion Quadratic Map and Its Julia Sets](the-reduced-biquaternion-quadratic-map-and-its-julia-sets.html), above this article, for the product fractal and the critical set.
- [The Idempotent Decomposition and the Split Fractal](the-idempotent-decomposition-and-the-reduced-biquaternion-split-fractal.html), above this article, for the global product structure behind the locus.
- [The Slices of the Reduced Biquaternion Julia Sets](the-slices-of-the-reduced-biquaternion-julia-sets.html), above this article, for the slices of the locus.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), above this article, for the critical cone.
- [The Hausdorff Dimension of the Reduced Biquaternion Julia Sets](the-hausdorff-dimension-of-the-reduced-biquaternion-julia-sets.html), below this article, for the dimension as a function of the parameter.
- [The Biquaternion Mandelbrot Set and the Connectedness Locus](the-biquaternion-mandelbrot-set-and-the-connectedness-locus.html), for the companion in which the escape criterion meets an obstruction.
