# __The Hausdorff Dimension of the Reduced Biquaternion Julia Sets__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ of basis $1,i,j,ij$, with element $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ in the two central idempotents, and with the quadratic family $F_{C}(\breve Q)=\breve Q^{2}+C$ whose filled Julia set is the product

$$
\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}},\qquad \mathcal{J}_{C}=\partial\bigl(K_{c_{1}}\times K_{c_{2}}\bigr)
=\bigl(J_{c_{1}}\times K_{c_{2}}\bigr)\cup\bigl(K_{c_{1}}\times J_{c_{2}}\bigr),
$$

read in the idempotent coordinates $C=c_{1}\Pi_++c_{2}\Pi_-$. The article computes the Hausdorff dimension of these sets.

The result is that the dimension is exact for every hyperbolic parameter of the family, that is every parameter whose two coordinates lie outside the boundary of the Mandelbrot set: it is the sum of the two complex dimensions for the filled Julia set, and the maximum of the two mixed sums for the Julia set, so that the whole dimension theory of the reduced biquaternion fractal is the sum of the two complex dimension theories. The boundary parameters are the single delicate case, deferred to the complex theory. At the parameter zero the filled Julia set is a solid bidisc of dimension four, the Julia set is its boundary of dimension three, and the singular part of the Julia set, its intersection with the zero-divisor cone, has dimension one. When both complex parameters lie in the interior of the Mandelbrot set the filled Julia set is of dimension four and the Julia set of dimension $2$ plus the larger of the two hyperbolic dimensions; when a parameter leaves the Mandelbrot set the filler becomes a Cantor set and the Julia set and the filled set have the same dimension. The dimension problem is thereby reduced to the complex dimension theory, with the boundary parameters as the only delicate case, in contrast with the non-commutative companion where the exact dimension is known only in part.

The article owns the product formula for the dimension, the dimension of the filled set and of the Julia set for the hyperbolic parameters, the parameter zero, the hyperbolic, the mixed and the disconnected cases, and the dimension of the singular part. The fractal and its product structure are *The Reduced Biquaternion Quadratic Map and Its Julia Sets*; the global decomposition is *The Idempotent Decomposition and the Split Fractal*; the slices are *The Slices of the Reduced Biquaternion Julia Sets*; the connectedness locus is *The Reduced Biquaternion Mandelbrot Set and the Connectedness Locus*; the systems of contractions and their similarity dimension are *The Reduced Biquaternion Iterated Function Systems*; the complex dimension theory is cited from *Hausdorff Dimension of Complex Quadratic Julia Sets*. The companion is *The Hausdorff Dimension of the Biquaternion Julia Sets*.

**Conventions.** The complex quadratic map of parameter $c$ is $f_{c}(\zeta)=\zeta^{2}+c$, with filled Julia set $K_{c}$, Julia set $J_{c}$ and Mandelbrot set $\mathcal{M}$. A parameter is **hyperbolic** when it lies outside the boundary $\partial\mathcal{M}$, that is in the interior of $\mathcal{M}$ — where the map has an attracting cycle and the Julia set is a quasicircle or a Cantor set of circles — or in the exterior of $\mathcal{M}$ — where the Julia set is a Cantor set and the map is expanding. For a hyperbolic parameter the Hausdorff dimension and the upper box dimension of $K_{c}$ and of $J_{c}$ coincide, and the **hyperbolic dimension** of $J_{c}$, for $c$ in the interior of $\mathcal{M}$, is that common value, which lies in the open interval $(1,2)$; a parameter in the exterior of $\mathcal{M}$ has $K_{c}=J_{c}$, a Cantor set of dimension in $(0,2)$.

## The Product Formula

**Theorem (the product formula).** For a parameter $C$ whose two coordinates are hyperbolic, that is whose two coordinates lie outside the boundary of $\mathcal{M}$,

$$
\dim_{H}\mathcal{K}_{C}=\dim_{H}K_{c_{1}}+\dim_{H}K_{c_{2}},
$$

and the identity holds because for a hyperbolic parameter the Hausdorff and the upper box dimensions of the complex filled set coincide, so that the product theorem for Hausdorff dimension applies with equality.

**Proof.** The filled set is the product of the two complex sets, and for a product $A\times B$ the general inequality is $\dim_{H}A+\dim_{H}B\leq\dim_{H}(A\times B)\leq\dim_{H}A+\overline{\dim}_{B}B$; when the two dimensions of one factor coincide, the upper bound equals the lower and the product is additive. For a hyperbolic parameter the coincidence of the Hausdorff and the upper box dimensions of $K_{c}$ and of $J_{c}$ is the standard dimension theory of a conformal expanding repeller, cited and not restated.

**Remark (the boundary parameters).** At a parameter whose one coordinate lies on the boundary of $\mathcal{M}$ the complex map may be parabolic rather than hyperbolic, and the coincidence of the Hausdorff and the box dimension of its Julia set is the delicate point of the complex dimension theory; the quantitative statements of this article are therefore made for the hyperbolic parameters, and the boundary case is deferred to the complex literature, cited rather than reproved. The parameter $C=0$ and the hyperbolic, the mixed and the disconnected cases of the following sections all have their coordinates outside the boundary.

**Corollary (the dimension of the Julia set).** With $e_{j}=\dim_{H}K_{c_{j}}$ and $f_{j}=\dim_{H}J_{c_{j}}$,

$$
\dim_{H}\mathcal{J}_{C}=\max\bigl(f_{1}+e_{2},\;e_{1}+f_{2}\bigr),
$$

because the Julia set is the union of the two products and the dimension of a finite union is the maximum of the dimensions.

**Proof.** The product formula is applied to each of the two products whose union is the Julia set, and the dimension of a finite union is the maximum of the dimensions of its members.

## The Parameter Zero

**Theorem (the dimension at the origin).** At $C=0$ the two complex filled Julia sets are the closed unit discs, so

$$
\dim_{H}\mathcal{K}_{0}=4,\qquad \dim_{H}\mathcal{J}_{0}=3,
$$

and the singular part of the Julia set, its intersection with the zero-divisor cone, has dimension one.

**Proof.** The filled Julia set is the product of two closed discs, of topological and Hausdorff dimension four, and its boundary is the union of the two products of a circle and a disc, of dimension $1+2=3$; the singular slice is the union of two circles by the computation of *The Reduced Biquaternion Quadratic Map and Its Julia Sets*, of dimension one.

**Remark (the dimension against the algebra).** The fractal at the origin has the full dimension of the ambient four-space and its singular part has the dimension of a circle; the algebra enters only through the singular part, which is the intersection of the fractal with the two complex planes of the zero divisors. In the non-commutative companion the corresponding singular part is a real four-dimensional manifold, and the difference of dimensions is the difference between the product geometry and the genuinely higher-dimensional one.

## The Hyperbolic Case

**Theorem (both parameters hyperbolic).** If both parameters lie in the interior of the Mandelbrot set, then

$$
\dim_{H}\mathcal{K}_{C}=4,\qquad \dim_{H}\mathcal{J}_{C}=2+\max\bigl(\dim_{H}J_{c_{1}},\dim_{H}J_{c_{2}}\bigr),
$$

a number in the open interval $(3,4)$.

**Proof.** A parameter in the interior of $\mathcal{M}$ has a filled Julia set with non-empty interior, of Hausdorff dimension two, and a Julia set of dimension in $(1,2)$; the formulae of the product theorem and of the corollary give the displayed values.

**Corollary (the central hyperbolic parameters).** For the central parameter $C=c\cdot1$ with $c$ in the interior of $\mathcal{M}$ the two complex dimensions coincide and

$$
\dim_{H}\mathcal{K}_{C}=4,\qquad \dim_{H}\mathcal{J}_{C}=2+\dim_{H}J_{c}.
$$

**Proof.** The central parameter has $c_{1}=c_{2}=c$, so the two complex Julia sets and dimensions coincide.

## The Mixed Case

**Theorem (one parameter inside, one outside).** If $c_{1}$ lies in the interior of $\mathcal{M}$ and $c_{2}$ lies outside $\mathcal{M}$, then

$$
\dim_{H}\mathcal{J}_{C}=\dim_{H}\mathcal{K}_{C}=2+\dim_{H}K_{c_{2}},
$$

a number in the open interval $(2,4)$, since the Cantor dimension $\dim_{H}K_{c_{2}}$ lies in $(0,2)$.

**Proof.** The filled set is the product of a set with interior and a Cantor set, so its dimension is $2+\dim_{H}K_{c_{2}}$; the Julia set is the union of the two products, of dimensions $\dim_{H}J_{c_{1}}+\dim_{H}K_{c_{2}}<2+\dim_{H}K_{c_{2}}$ and $2+\dim_{H}K_{c_{2}}$, so the maximum is the second, which equals the dimension of the filled set.

**Remark (the geometry of the mixed case).** The fractal is the product of a solid planar set with a Cantor set, so its dimension is the plane dimension plus the Cantor dimension; because the Cantor factor has empty interior the product has empty interior too, and a closed set with empty interior equals its own boundary, so the Julia set and the filled Julia set coincide in the mixed case. The piece $J_{c_{1}}\times K_{c_{2}}$ of the boundary is of dimension $f_{1}+e_{2}$, smaller than the dimension $2+e_{2}$ of the fractal by the hyperbolic defect $2-\dim_{H}J_{c_{1}}$, but the piece $K_{c_{1}}\times K_{c_{2}}$ of the boundary is the fractal itself, so the reduction of the solid factor does not lower the dimension.

## The Disconnected Case

**Theorem (both parameters outside).** If both parameters lie outside the Mandelbrot set, then both complex filled Julia sets are Cantor sets with empty interior, and

$$
\mathcal{J}_{C}=\mathcal{K}_{C},\qquad \dim_{H}\mathcal{J}_{C}=\dim_{H}K_{c_{1}}+\dim_{H}K_{c_{2}},
$$

a number in the open interval $(0,4)$, since each Cantor dimension lies in $(0,2)$.

**Proof.** A parameter outside $\mathcal{M}$ has a Cantor set $K_{c}$ with $K_{c}=J_{c}$ and empty interior; the product of two sets with empty interior has empty interior, so the boundary of the product is the product, and the dimension formula of the product theorem applies.

**Remark (the boundary parameters).** If a coordinate lies on the boundary of $\mathcal{M}$, the corresponding complex map is the delicate case of the complex dimension theory and need not be hyperbolic: a parabolic parameter has a filled Julia set with non-empty interior, while a Misiurewicz parameter has $\mathcal{K}_{c}=\mathcal{J}_{c}$, so neither the factor's dimension nor the box-dimension coincidence is automatic. The dimension of the product is therefore not decided by the simple formulae above and is deferred to the complex theory, the boundary parameters being the single delicate case of the article.

## The Singular Part

**Proposition (the dimension of the singular part).** The singular part of the filled Julia set is

$$
\mathcal{K}_{C}\cap\mathscr{Z}=\bigl(\{0\}\cap K_{c_{1}}\bigr)\times K_{c_{2}}\;\cup\;K_{c_{1}}\times\bigl(\{0\}\cap K_{c_{2}}\bigr),
$$

and its dimension is the maximum of the dimensions of the non-empty members; each non-empty member is a full complex filled Julia set, of dimension $e_{2}$ or $e_{1}$.

**Proof.** The computation of the singular slices gives the displayed union, and a member is the product of a point with a complex filled Julia set, of the dimension of that complex set.

**Corollary (the thinness of the singular part).** The singular part of the fractal has the dimension of one complex factor, not the dimension of the algebra; for the quadratic family at the origin it has dimension one, and in the generic case it is at most $\max(e_{1},e_{2})\leq2$.

**Proof.** Each member is a complex filled Julia set, of dimension at most two, and the maximum of the members is the dimension of the part.

## Comparison with the Biquaternion Case

**Remark (the two dimension theories).** The dimension of the reduced biquaternion fractal is known exactly for every hyperbolic parameter, because the fractal is a product of two complex fractals and the complex dimension theory is available: the dimension is the sum of the two complex dimensions, and every case is decided by the two memberships in the Mandelbrot set, the boundary parameters being the single delicate case. In the biquaternion algebra the exact dimension is known only in part, the fractal is not a product, and the computation of the dimension is one of the open problems of the theory. The reduced algebra is the case in which the dimension problem has a complete answer, and the answer is the sum of the two complex answers, with the singular part contributing only the dimension of a single complex slice.

## Summary

The dimension theory of the reduced biquaternion quadratic fractal is the sum of two complex dimension theories. The filled Julia set satisfies $\dim_{H}\mathcal{K}_{C}=\dim_{H}K_{c_{1}}+\dim_{H}K_{c_{2}}$, for the hyperbolic parameters, because the fractal is a product and the Hausdorff and upper box dimensions coincide for a hyperbolic complex parameter; the Julia set satisfies $\dim_{H}\mathcal{J}_{C}=\max(f_{1}+e_{2},e_{1}+f_{2})$ with the complex dimensions of the filled and the Julia sets, because the Julia set is the union of the two mixed products. At the parameter zero the filled set is a solid bidisc of dimension four, the Julia set has dimension three and the singular part, its intersection with the zero-divisor cone, has dimension one. When both parameters are hyperbolic the filled set has dimension four and the Julia set the dimension two plus the larger hyperbolic dimension; in the mixed case the Julia set and the filled set have the same dimension, the plane dimension plus the Cantor dimension; when both parameters are outside the Mandelbrot set both complex sets are Cantor sets and the Julia set equals the filled set. The singular part always has the dimension of one complex factor, at most two, which is the thin counterpart of the four-dimensional singular manifold of the non-commutative companion, and the answer is exact for every hyperbolic parameter of the reduced family, the boundary parameters aside.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}}$ | the filled Julia set as a product |
| $\dim_{H}\mathcal{K}_{C}=e_{1}+e_{2}$ | the dimension of the filled set, $e_{j}=\dim_{H}K_{c_{j}}$ |
| $\dim_{H}\mathcal{J}_{C}=\max(f_{1}+e_{2},e_{1}+f_{2})$ | the dimension of the Julia set, $f_{j}=\dim_{H}J_{c_{j}}$ |
| $\dim_{H}\mathcal{K}_{0}=4$, $\dim_{H}\mathcal{J}_{0}=3$ | the parameter zero |
| $\dim_{H}\mathcal{J}_{C}=2+\max(\dim_{H}J_{c_{1}},\dim_{H}J_{c_{2}})$ | both parameters in the interior of $\mathcal{M}$ |
| $\dim_{H}\mathcal{J}_{C}=2+\dim_{H}K_{c_{2}}$ | one parameter inside, one outside |
| $\mathcal{J}_{C}=\mathcal{K}_{C}$ | both parameters outside |
| $\dim_{H}(\mathcal{K}_{C}\cap\mathscr{Z})\leq2$ | the singular part, of the dimension of one complex factor |

## Further Reading

- *The Reduced Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-reduced-biquaternion-quadratic-map-and-its-julia-sets.md`), above this article, for the product fractal, the critical cone and the singular slices.
- *The Idempotent Decomposition and the Split Fractal* (`articles_maths/the-idempotent-decomposition-and-the-reduced-biquaternion-split-fractal.md`), above this article, for the global decomposition behind the product formula.
- *The Slices of the Reduced Biquaternion Julia Sets* (`articles_maths/the-slices-of-the-reduced-biquaternion-julia-sets.md`), above this article, for the slices whose dimension is computed here.
- *The Reduced Biquaternion Mandelbrot Set and the Connectedness Locus* (`articles_maths/the-reduced-biquaternion-mandelbrot-set-and-the-connectedness-locus.md`), above this article, for the parameter regions of the cases.
- *The Reduced Biquaternion Iterated Function Systems* (`articles_maths/the-reduced-biquaternion-iterated-function-systems.md`), above this article, for the similarity dimension of self-similar systems.
- *The Hausdorff Dimension of the Biquaternion Julia Sets* (`articles_maths/the-hausdorff-dimension-of-the-biquaternion-julia-sets.md`), for the companion in which the exact dimension is known only in part.
