# __The Slices of the Reduced Biquaternion Julia Sets__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ of basis $1,i,j,ij$, with element $Q_\pm=Q_{++}\Pi_++Q_{--}\Pi_-$ in the two central idempotents $\Pi_{\pm}=\tfrac12(1\pm j)$, and with the quadratic family $F_{C}(Q_\pm)=Q_\pm^{2}+C$ whose filled Julia set is the product

$$
\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}},\qquad \mathcal{J}_{C}=\partial\bigl(K_{c_{1}}\times K_{c_{2}}\bigr),
$$

read in the idempotent coordinates, with $C=c_{1}\Pi_++c_{2}\Pi_-$ and with the complex filled Julia sets of the two parameters. The article computes the slices of the reduced biquaternion fractal.

The result is that every slice is exact, because the fractal is a product and the slices of a product are the products of the slices of the factors with the constraint read on each coordinate separately. There is no new phenomenon: a complex line slice of the fractal is either the whole of a complex filled Julia set or empty, the diagonal slice is the intersection of the two complex filled Julia sets, the real slice is the intersection of the first complex filled Julia set with the conjugate of the second, a one-real-dimensional affine slice is the intersection of two affine line slices of the two complex sets, and everything is computed from the two complex pictures without any twistor-like ambiguity. This is the sharp gain over the non-commutative companion, where only the idempotent plane gives an exact slice and the general slice is not computable from complex data.

The article owns the notion of a slice for the algebra, the product rule, the complex slices and their degeneracy, the diagonal and the real slices, the affine one-real-dimensional slices, the slices at the parameter zero and the slices of the connectedness locus. The fractal and its product structure are *The Reduced Biquaternion Quadratic Map and Its Julia Sets*; the global decomposition is *The Idempotent Decomposition and the Split Fractal*; the dimension is *The Hausdorff Dimension of the Reduced Biquaternion Julia Sets*; the connectedness locus is *The Reduced Biquaternion Mandelbrot Set and the Connectedness Locus*; the real subspace and the involution that defines it are *Reduced Biquaternion Space* and *The Two Involutions and the Group of Involutions*. The companion, where only the idempotent slice is exact, is *The Slices of the Biquaternion Julia Sets*.

**Conventions.** The coordinates are $(Q_{++},Q_{--})\in\mathbb{C}^{2}$, identified with the algebra by $Q_\pm=Q_{++}\Pi_++Q_{--}\Pi_-$; the complex quadratic map of parameter $c$ is $f_{c}(\zeta)=\zeta^{2}+c$, with filled Julia set $K_{c}$ and Julia set $J_{c}$; a **slice** is the intersection of a set of the algebra with a subset defined by affine or linear conditions on the two coordinates; the conjugate of a set is the set of conjugates of its points.

## The Notion of a Slice and the Product Rule

**Definition (the slices used).** The slices of this article are the following subsets of the algebra, each written in the idempotent coordinates:

| slice | condition |
|---|---|
| complex line | $Q_{--}={Q_{--}}_{0}$ or $Q_{++}={Q_{++}}_{0}$ with the other coordinate free |
| affine real line | $(Q_{++},Q_{--})=({Q_{++}}_{0},{Q_{--}}_{0})+t(a,b)$ with $t\in\mathbb{R}$ and $a,b\in\mathbb{C}$ |
| diagonal | $Q_{++}=Q_{--}$ |
| real | $Q_{--}=\bar Q_{++}$ |
| central-parameter line | $c_{1}=c_{2}$ in the parameter algebra |

**Theorem (the product rule).** If a set of the algebra is the product $S=K_{1}\times K_{2}$ of a subset of the first coordinate and a subset of the second, and if $\Sigma$ is a slice, then

$$
\Sigma\cap S=\bigl\{\sigma\in\Sigma:\pi_{1}(\sigma)\in K_{1}\text{ and }\pi_{2}(\sigma)\in K_{2}\bigr\},
$$

so that the slice is obtained by intersecting the slice with the two coordinate conditions separately.

**Proof.** The membership $Q_\pm\in K_{1}\times K_{2}$ is the conjunction of the two coordinate memberships, and the slice is a set of constraints on the same two coordinates; intersecting with a product is intersecting with each factor.

**Corollary (slices of the filled Julia set).** For the quadratic family every slice of $\mathcal{K}_{C}$ is computed from the two complex filled Julia sets $K_{c_{1}}$ and $K_{c_{2}}$ by the rule above; for the Julia set one uses the two descriptions $\mathcal{J}_{C}=(J_{c_{1}}\times K_{c_{2}})\cup(K_{c_{1}}\times J_{c_{2}})$ and takes the union of the two slice computations.

**Proof.** The product description of the filled set and the union description of the Julia set are those of *The Reduced Biquaternion Quadratic Map and Its Julia Sets*, and the product rule applies to each product.

## The Complex Slices and Their Degeneracy

**Proposition (complex line slices are all or nothing).** For a complex line slice at a fixed coordinate,

$$
\{Q_{--}={Q_{--}}_{0}\}\cap\mathcal{K}_{C}=
\begin{cases}
K_{c_{1}}, & {Q_{--}}_{0}\in K_{c_{2}},\\[2pt]
\varnothing, & {Q_{--}}_{0}\notin K_{c_{2}},
\end{cases}
\qquad
\{Q_{++}={Q_{++}}_{0}\}\cap\mathcal{K}_{C}=
\begin{cases}
K_{c_{2}}, & {Q_{++}}_{0}\in K_{c_{1}},\\[2pt]
\varnothing, & {Q_{++}}_{0}\notin K_{c_{1}}.
\end{cases}
$$

**Proof.** The complex line is the product of the free coordinate and the single point, and the product rule gives the product of the free complex filled Julia set with the set that is the fixed point when it belongs to the corresponding filled Julia set and empty otherwise.

**Remark (why the complex slices are degenerate).** The slice is degenerate because it is complex and the fractal is a product of complex sets: intersecting a product with a complex line does not cut a real curve out of the fractal, it selects one full complex factor or none. Real one-dimensional slices are the informative ones, and they are the affine real line slices, the diagonal and the real slice below.

## The Diagonal Slice

**Theorem (the diagonal slice).** The diagonal slice of the filled Julia set is the intersection of the two complex filled Julia sets,

$$
\{Q_{++}=Q_{--}\}\cap\mathcal{K}_{C}=\{(\zeta,\zeta):\zeta\in K_{c_{1}}\cap K_{c_{2}}\}\cong K_{c_{1}}\cap K_{c_{2}},
$$

and the diagonal slice of the Julia set is the corresponding part of the boundary. In particular, for a central parameter $C=c\cdot1$ the diagonal slice of $\mathcal{K}_{C}$ is the complex filled Julia set $K_{c}$.

**Proof.** Along the diagonal $Q_{++}=Q_{--}=\zeta$ and the membership in the product is the conjunction of $\zeta\in K_{c_{1}}$ and $\zeta\in K_{c_{2}}$; for a central parameter the two sets coincide.

**Remark (the diagonal and the exchange symmetry).** The diagonal slice is the fixed set of the exchange of the two idempotent coordinates, which is the natural sign restricted to the coordinate level; it is the slice the algebra reads most directly, and for a central parameter it reproduces the complex fractal itself, so the central reduced biquaternion fractal contains the complex fractal as its diagonal slice.

## The Real Slice

**Theorem (the real slice).** The slice on the plane $\mathbb{R}\{1,ij\}$ of the elements fixed by the star, which in the idempotent coordinates is $Q_{--}=\bar Q_{++}$, is

$$
\{Q_{--}=\bar Q_{++}\}\cap\mathcal{K}_{C}=\{(\zeta,\bar\zeta):\zeta\in K_{c_{1}}\cap\overline{K_{c_{2}}}\}\cong K_{c_{1}}\cap\overline{K_{c_{2}}}.
$$

In particular, if the two parameters are conjugate, $c_{2}=\bar c_{1}$, then $K_{c_{2}}=\overline{K_{c_{1}}}$ and the real slice is the complex filled Julia set $K_{c_{1}}$ itself.

**Proof.** The plane $\mathbb{R}\{1,ij\}$ consists of the elements with $Q_+$ real and $Q_-$ purely imaginary, and $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$ give $Q_{--}=\bar Q_{++}$ there (while the coefficient-real plane $\{Q_+,Q_-\in\mathbb{R}\}$ is $\mathbb{R}\{1,j\}$, where $Q_{++}$ and $Q_{--}$ are real and equal only when $Q_-=0$); the product rule then requires $\zeta\in K_{c_{1}}$ and $\bar\zeta\in K_{c_{2}}$, which is the displayed set; the conjugate of $K_{c}$ is $K_{\bar c}$ because the complex quadratic map commutes with the conjugation.

**Corollary (the real slice of the Julia set).** On the real subspace the Julia set slice is the boundary of $K_{c_{1}}\cap\overline{K_{c_{2}}}$, of real dimension at most one, and for the conjugate parameters it is the complex Julia set $J_{c_{1}}$, of real dimension one.

**Proof.** The real slice is identified with a subset of the complex plane by $\zeta\mapsto(\zeta,\bar\zeta)$, and a subset of the plane has boundary of real dimension at most one; for conjugate parameters the slice is the full complex filled Julia set.

## The Affine One-Real-Dimensional Slices

**Theorem (the affine slice is the intersection of two complex line slices).** Let the slice be the affine real line

$$
\Sigma=\{(Q_{++},Q_{--})=({Q_{++}}_{0},{Q_{--}}_{0})+t(a,b):t\in\mathbb{R}\},\qquad a,b\in\mathbb{C}.
$$

Then its intersection with the filled Julia set is

$$
\Sigma\cap\mathcal{K}_{C}=\bigl\{t\in\mathbb{R}:{Q_{++}}_{0}+ta\in K_{c_{1}}\ \text{and}\ {Q_{--}}_{0}+tb\in K_{c_{2}}\bigr\},
$$

the intersection of the affine line slice of $K_{c_{1}}$ with the affine line slice of $K_{c_{2}}$, the second reparametrised by the same real parameter.

**Proof.** The product rule applied to the parametrised line gives the two coordinate conditions for the same $t$.

**Corollary (the visible pictures).** Every real two-dimensional picture of the fractal obtained by drawing a real plane through the origin is the intersection of two complex pictures, one for each coordinate, reparametrised by the same parameter; the picture is the more informative the less the two parametrisations are aligned.

**Proof.** The statement is the theorem specialised to a real two-dimensional parametrisation, which is a family of affine real lines; each line gives the intersection of two complex line slices.

## The Slices at the Parameter Zero

**Proposition (the parameter zero).** At $C=0$ the two complex filled Julia sets are the closed unit discs, $\mathcal{K}_{0}$ is the closed unit bidisc, and

$$
\{Q_{++}=Q_{--}\}\cap\mathcal{K}_{0}=\{|\zeta|\leq1\},\qquad
\{Q_{--}=\bar Q_{++}\}\cap\mathcal{K}_{0}=\{|\zeta|\leq1\},
$$

both slices being unit discs; every affine real line slice is an interval, the intersection of the two intervals cut out by the two discs; and the Julia set slices are the corresponding circles.

**Proof.** The complex filled Julia set of the parameter zero is the closed unit disc, so the products give the bidisc and the slices give the discs and the intersections of discs with lines, which are intervals.

**Remark (the singular slices).** The slice of the Julia set with the zero-divisor cone $\mathscr{Z}=\{Q_{++}=0\}\cup\{Q_{--}=0\}$ is the singular slice, of dimension one at the parameter zero and at most two in general; at the parameter zero it is the union of the two circles $\{0\}\times S^{1}$ and $S^{1}\times\{0\}$ cut out by the two coordinate discs, in agreement with *The Reduced Biquaternion Quadratic Map and Its Julia Sets*. The zero divisors therefore enter the slice theory only through this thin singular slice, the algebra being commutative and having no division but being the product of two fields.

## The Slices of the Connectedness Locus

**Theorem (the slices of the locus).** The connectedness locus of the reduced biquaternion quadratic family is the product $\mathcal{M}\times\mathcal{M}$ of the complex Mandelbrot set with itself, and its slices are:

$$
\{c_{1}=c_{2}\}\cap(\mathcal{M}\times\mathcal{M})\cong\mathcal{M},
$$

the central-parameter line, which is the Mandelbrot set; the conjugate line $\{c_{2}=\bar c_{1}\}$, which is again $\mathcal{M}$; and a translated line $\{c_{2}=c_{1}+\mu\}$, which is the intersection $\mathcal{M}\cap(\mathcal{M}-\mu)$ of the Mandelbrot set with its translate.

**Proof.** The filled Julia set $\mathcal{K}_{C}$ is connected exactly when both complex filled Julia sets are connected, which is the product statement; intersecting a product with a complex affine line gives the two conditions on the same parameter, which for the three displayed lines give the three displayed sets, the last because $c_{1}\in\mathcal{M}$ and $c_{1}+\mu\in\mathcal{M}$ means $c_{1}\in\mathcal{M}\cap(\mathcal{M}-\mu)$.

**Remark (the informative slices).** As for the fractal, the complex line slices of the connectedness locus are degenerate, being empty or a translate of the Mandelbrot set, and the informative slices are the real two-dimensional ones, of which the translated line $\{c_{2}=c_{1}+\mu\}$ is the model: its slices are the intersections of the Mandelbrot set with its translates, exactly as in the complex theory.

## Comparison with the Biquaternion Case

**Remark (the exact slices).** In the reduced biquaternion algebra every slice of the fractal is computed from the two complex filled Julia sets, because the fractal is exactly a product and the imaginary part of the quaternion product, which couples the coordinates in the non-commutative case, is absent. In the biquaternion algebra only the idempotent plane gives an exact slice, the general slice is governed by the coupling term and its complex structure is not reducible to one complex variable per coordinate, and the computation of the slices is the harder problem of *The Slices of the Biquaternion Julia Sets*. The reduced case is the case in which the slice problem has no obstruction.

## Summary

The filled Julia set of the reduced biquaternion quadratic map is the product $K_{c_{1}}\times K_{c_{2}}$ of the two complex filled Julia sets in the idempotent coordinates, so the product rule makes every slice exact: a complex line slice is either the whole of the free complex filled Julia set or empty, the diagonal slice is the intersection $K_{c_{1}}\cap K_{c_{2}}$ and for a central parameter reproduces the complex fractal, the real slice is the intersection $K_{c_{1}}\cap\overline{K_{c_{2}}}$ and for conjugate parameters is the complex filled Julia set itself, an affine real line slice is the intersection of the two affine line slices of the two complex sets with the same real parameter, and the slices at the parameter zero are discs, intervals and circles computed from the unit disc. The connectedness locus is the product of the Mandelbrot set with itself, its central and conjugate lines are copies of the Mandelbrot set, and its translated lines are the intersections of the Mandelbrot set with its translates. Every slice is computed from complex data, with no coupling between the coordinates beyond the identity of the parameter, which is the sharp contrast with the non-commutative companion where only the idempotent slice is exact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(Q_{++},Q_{--})$ | the idempotent coordinates, $Q_\pm=Q_{++}\Pi_++Q_{--}\Pi_-$ |
| $\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}}$ | the filled Julia set as a product |
| product rule | $\Sigma\cap(K_{1}\times K_{2})$ read coordinatewise |
| $\{Q_{--}={Q_{--}}_{0}\}$ | a complex line slice, empty or a full complex filled set |
| $\{Q_{++}=Q_{--}\}$ | the diagonal slice, $\cong K_{c_{1}}\cap K_{c_{2}}$ |
| $\{Q_{--}=\bar Q_{++}\}$ | the real slice, $\cong K_{c_{1}}\cap\overline{K_{c_{2}}}$ |
| $({Q_{++}}_{0},{Q_{--}}_{0})+t(a,b)$ | an affine real line slice, two complex line slices for the same $t$ |
| $\mathcal{M}\times\mathcal{M}$ | the connectedness locus, the product of two Mandelbrot sets |
| $\{c_{2}=c_{1}+\mu\}$ | a translated parameter line, $\mathcal{M}\cap(\mathcal{M}-\mu)$ |

## Further Reading

- *The Reduced Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-reduced-biquaternion-quadratic-map-and-its-julia-sets.md`), above this article, for the map and the product fractal.
- *The Idempotent Decomposition and the Split Fractal* (`articles_maths/the-idempotent-decomposition-and-the-reduced-biquaternion-split-fractal.md`), above this article, for the global decomposition behind the product rule.
- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), above this article, for the coordinates and the real subspace.
- *The Two Involutions and the Group of Involutions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), above this article, for the exchange of the two idempotent coordinates.
- *The Hausdorff Dimension of the Reduced Biquaternion Julia Sets* (`articles_maths/the-hausdorff-dimension-of-the-reduced-biquaternion-julia-sets.md`), below this article, for the dimension of the slices and of the fractal.
- *The Slices of the Biquaternion Julia Sets* (`articles_maths/the-slices-of-the-biquaternion-julia-sets.md`), for the companion in which only the idempotent slice is exact.
