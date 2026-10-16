# __The Idempotent Decomposition and the Split Fractal__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ of basis $1,i,j,ij$, and its two idempotents $\Pi_{1,2}=\tfrac12(1\pm j)$ satisfy

$$
\Pi_{1}+\Pi_{2}=1,\qquad \Pi_{1}\Pi_{2}=0,\qquad \Pi_{1}^{2}=\Pi_{1},\qquad \Pi_{2}^{2}=\Pi_{2},
$$

so the algebra is the direct sum of rings $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$. The decomposition is **global**: the idempotents are central, every element is a pair of complex numbers, and every multiplication, every involution and every norm of the algebra is computed coordinatewise. The article draws the consequences for the fractals of the algebra, and proves the reduction of the dynamics to the two complex slices.

The result is the strongest possible reduction. A self-map of the algebra written in the coordinates is a pair of complex maps with the same index, a quadratic map of the algebra is a pair of complex quadratic maps, and a quadratic fractal is the product of the two complex fractals while the attractor of a system of contractions is the graph-like set of the pairs matched by the same coding. The coupling term that makes the non-commutative companion hard is identically zero here, and the only place where the two coordinates interact is the index of the generators: a point of the attractor has the same coding in the two coordinates, and that is the whole of the interaction. The singular sets, the zero-divisor cone and its slices, are then computed from the two complex singular sets.

The article owns the global decomposition, the proof of the reduction, the coupling term and its vanishing, the matched structure of the split fractal, and the effect of the zero divisors on the singular sets. The algebra, the idempotents and the coordinates are *Reduced Biquaternion Space* and *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the quadratic map and its fractal are *The Reduced Biquaternion Quadratic Map and Its Julia Sets*; the slices are *The Slices of the Reduced Biquaternion Julia Sets*; the dimension is *The Hausdorff Dimension of the Reduced Biquaternion Julia Sets*; the systems of contractions are *The Reduced Biquaternion Iterated Function Systems*; the connectedness locus is *The Reduced Biquaternion Mandelbrot Set and the Connectedness Locus*. The companion is *The Idempotent Decomposition and the Split Fractal*, where the idempotents are not central and the decomposition is only local.

**Conventions.** The element is $T=q_1\Pi_{1}+q_2\Pi_{2}$ with $q_1,q_2\in\mathbb{C}$; the topological norm is $\langle T\rangle_{\natural*}=\tfrac12(|q_1|^{2}+|q_2|^{2})$; the complex quadratic map of parameter $c$ is $f_{c}(\zeta)=\zeta^{2}+c$ with filled Julia set $K_{c}$ and Julia set $J_{c}$; a **map of the algebra** is a map written in the coordinates, and a **generator** is one of the maps of a finite system.

## The Global Decomposition

**Theorem (the decomposition is a direct sum of rings).** The algebra is the direct sum of its two idempotent lines,

$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2},
$$

and the two projections $T\mapsto q_1$ and $T\mapsto q_2$ are algebra homomorphisms onto $\mathbb{C}$, the two characters of the algebra.

**Proof.** The four relations above give $\Pi_{1}(q_1\Pi_{1}+q_2\Pi_{2})=q_1\Pi_{1}$ and $\Pi_{2}(q_1\Pi_{1}+q_2\Pi_{2})=q_2\Pi_{2}$, so the decomposition is additive and multiplicative; the projections are ring homomorphisms because the multiplication is componentwise, and they are the two nontrivial complex-valued algebra homomorphisms.

**Corollary (everything is coordinatewise).** The multiplication, the four products, the involutions, the four norms and the matrix model are computed on the two coordinates separately and combined; an algebra endomorphism is the pair of a complex automorphism of the first coordinate and a complex automorphism of the second, subject to the reality condition.

**Proof.** The assertion is the definition of the componentwise multiplication together with the tables of *The Four Products, Their Forms and Their Algebraic Norms* and *Reduced Biquaternion Other Algebraic Element Representations*.

## The Reduction of the Dynamics

**Theorem (the reduction).** Let $F:\mathbb{B}_{\mathrm{r}}\to\mathbb{B}_{\mathrm{r}}$ be a map that in the coordinates is continuous and written as $F(q_1,q_2)=(F_{1}(q_1),F_{2}(q_2))$ — that is, a pair of maps of one complex variable, each depending on its own coordinate. Then the orbit of $T=(q_1,q_2)$ is the pair of the orbits of the two coordinates,

$$
F^{n}(T)=\bigl(F_{1}^{n}(q_1),\,F_{2}^{n}(q_2)\bigr),
$$

and the filled set of bounded orbits is

$$
\mathcal{K}=\pi_{1}^{-1}\bigl(K^{(1)}\bigr)\cap\pi_{2}^{-1}\bigl(K^{(2)}\bigr)=K^{(1)}\times K^{(2)},
$$

where $K^{(j)}$ is the filled set of the one-variable map $F_{j}$ in the bounded sense.

**Proof.** By induction the $n$-th iterate is the pair of the $n$-th iterates; the orbit is bounded for $\langle\cdot\rangle_{\natural*}=\tfrac12(|q_1|^{2}+|q_2|^{2})$ exactly when both coordinate orbits are bounded.

**Corollary (the quadratic case).** The quadratic map $F_{C}(T)=T^{2}+C$ is a map of this form, with $F_{j}(\zeta)=\zeta^{2}+c_{j}$; hence $\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}}$ and the dynamics of the algebra is the product of the two complex dynamics.

**Proof.** The square and the translation are coordinatewise, and the corollary restates the product theorem of *The Reduced Biquaternion Quadratic Map and Its Julia Sets*.

## The Coupling Term and Its Vanishing

**Proposition (the coupling vanishes).** Write a general quadratic map of the algebra with a linear and a constant term, $F(T)=T^{2}+AT+B$, in the coordinates $A=a_{1}\Pi_{1}+a_{2}\Pi_{2}$ and $B=b_{1}\Pi_{1}+b_{2}\Pi_{2}$. Then

$$
F(q_1,q_2)=\bigl(q_1^{2}+a_{1}q_1+b_{1},\;q_2^{2}+a_{2}q_2+b_{2}\bigr),
$$

with no term mixing $q_1$ and $q_2$; every polynomial map of the algebra is the pair of its two complex polynomial maps.

**Proof.** The multiplication is componentwise, so $T^{2}=(q_1^{2},q_2^{2})$, $AT=(a_{1}q_1,a_{2}q_2)$ and $B=(b_{1},b_{2})$; there is no monomial of mixed coordinates because the algebra is a direct product of rings, in which the two coordinates are orthogonal.

**Remark (what the vanishing buys).** In the biquaternion algebra the product $AT$ is not coordinatewise, and the idempotent coordinates of a product contain a term mixing the two complex coordinates, proportional to the imaginary part of the quaternion product; that term is the obstruction to the global reduction and the source of the non-product structure of the biquaternion fractal. In the reduced algebra the term is identically zero, and the global reduction is available.

## The Matched Structure of the Split Fractal

**Definition (the split fractal).** Let $f_{1},\dots,f_{m}$ be **generators**, each a contraction of the algebra written in the coordinates as a pair of complex maps, $f_{i}(q_1,q_2)=(f_{i}^{+}(q_1),f_{i}^{-}(q_2))$. The **split fractal** of the system is the attractor of the system, the unique non-empty compact set $\mathcal{K}$ with

$$
\mathcal{K}=\bigcup_{i=1}^{m}f_{i}(\mathcal{K}).
$$

**Theorem (the attractor is the matched set of the coding space).** Let $\Sigma=\{1,\dots,m\}^{\mathbb{N}}$ be the coding space and let $h^{+},h^{-}:\Sigma\to\mathbb{C}$ be the two coding maps, so that $h^{\pm}(\sigma)=\lim_{n}f^{\pm}_{\sigma_{1}}\circ\cdots\circ f^{\pm}_{\sigma_{n}}(0)$; then $K^{\pm}=h^{\pm}(\Sigma)$ and the attractor of the system is

$$
\mathcal{K}=\Bigl\{\bigl(h^{+}(\sigma),\,h^{-}(\sigma)\bigr):\sigma\in\Sigma\Bigr\},
$$

the set of the pairs of points of $K^{+}$ and $K^{-}$ that are **matched**, that is coded by the same sequence of generators. Consequently $\mathcal{K}\subseteq K^{+}\times K^{-}$, the two projections of $\mathcal{K}$ are $K^{+}$ and $K^{-}$, the attractor has the dimension of one coordinate attractor and not the sum when the two systems have the same ratios, and the inclusion is strict as soon as neither coordinate attractor is a single point; for one generator the attractor is the single matched pair, which is the product of the two fixed points.

**Proof.** The coding map satisfies $h^{\pm}(i\sigma)=f^{\pm}_{i}(h^{\pm}(\sigma))$ for every $i$ and every $\sigma$, because the limit of the compositions starting with $i$ is the image under $f^{\pm}_{i}$ of the limit of the remaining compositions; hence

$$
\bigcup_{i}f_{i}\Bigl(\bigl\{\bigl(h^{+}(\sigma),h^{-}(\sigma)\bigr)\}\Bigr)
=\Bigl\{\bigl(h^{+}(i\sigma),h^{-}(i\sigma)\bigr):i,\sigma\Bigr\}
=\Bigl\{\bigl(h^{+}(\tau),h^{-}(\tau)\bigr):\tau\Bigr\},
$$

so the displayed set is a fixed point of the Hutchinson operator; it is compact, being the continuous image of the compact coding space, and non-empty, so it is the attractor by uniqueness. The projections are $h^{\pm}(\Sigma)=K^{\pm}$, which are onto. For one generator the coding space is a point, so the attractor is a single matched pair; and for more than one generator the off-diagonal pairs $\bigl(h^{+}(\sigma),h^{-}(\tau)\bigr)$ with $\sigma\neq\tau$ whose two values have no common code lie in $K^{+}\times K^{-}$ and not in $\mathcal{K}$, so the inclusion is strict whenever both coordinate attractors have more than one point.

**Remark (the meaning of the matching).** The attractor consists of the pairs of points of $K^{+}$ and $K^{-}$ obtained by iterating the same sequence of generators in the two coordinates. The interaction between the coordinates is the identity of the coding and nothing else, and it is the expression of the fact that a map of the algebra carries the honest single index of the algebra, not a pair of independent indices. The attractor is therefore not the product of the two coordinate attractors and not a union of products either, but the graph-like set of the matched pairs; when the two coordinate systems coincide it is the diagonal $\{(x,x):x\in K^{+}\}$.

**Corollary (the quadratic case is a single product).** For the quadratic family the filled Julia set is the product of the two complex filled Julia sets, because the orbit of an element is the pair of the orbits of its two coordinates; the difference from the system above is that the quadratic family has a single map, whose bounded orbit locus is the product, and not a system of contractions, whose attractor is only the matched subset of the product.

**Proof.** The bounded orbit locus of the quadratic map is the product by the direct computation of the orbits, and the attractor of a single contraction is the matched pair of the two fixed points, which is the product of the two one-point attractors.

## The Zero Divisors and the Singular Sets

**Proposition (the singular slices).** The zero-divisor cone of the algebra is $\mathscr{Z}=\{q_1=0\}\cup\{q_2=0\}$, the union of the two coordinate planes, and for the quadratic family

$$
\mathcal{K}_{C}\cap\mathscr{Z}=\bigl(\{0\}\cap K_{c_{1}}\bigr)\times K_{c_{2}}\;\cup\;K_{c_{1}}\times\bigl(\{0\}\cap K_{c_{2}}\bigr),
$$

so each singular slice is either a full complex filled Julia set or empty, and it is a two-real-dimensional set.

**Proof.** The singular set is the set of elements with a vanishing coordinate; intersecting a product with the plane $q_1=0$ gives the product of the intersection of the first factor with $\{0\}$ and the whole second factor; the set $\{0\}\cap K_{c_{1}}$ is the filled Julia set of the parameter $c_{1}$ when the critical point $0$ belongs to it, and empty otherwise.

**Remark (the singular codes).** For a general system the same computation gives the singular slices as unions of products in which one coordinate is a point and the other a piece of the coordinate attractor; the singular part of the split fractal is therefore thin, of the dimension of one complex slice, and the zero divisors do not create a singular manifold of the dimension of the algebra. This is the sharp contrast with the non-commutative companion, where the idempotent manifold is a real four-dimensional subset of the fractal and its singular structure is genuinely higher-dimensional.

**Corollary (the connectedness of the split fractal).** The quadratic filled set $\mathcal{K}_{C}$ is connected exactly when the two complex filled Julia sets are connected, that is exactly when $C$ belongs to the product of the two Mandelbrot sets; and the general split fractal is connected when the union of the products is connected, which is the condition that the pieces $f_{i}^{+}(K^{+})\times f_{i}^{-}(K^{-})$ meet along the union.

**Proof.** A product of two compact sets is connected exactly when both are, and a finite union is connected exactly when its members form a chain of intersections; the connectedness locus of the complex quadratic family is the Mandelbrot set.

## Summary

The idempotent decomposition of the reduced biquaternion algebra is a direct sum of rings, global because the idempotents are central: the algebra is $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$, the two coordinates are the two characters, and every product, norm and polynomial map is computed coordinatewise. Consequently the quadratic map is the pair of two complex quadratic maps, the filled Julia set is exactly the product $K_{c_{1}}\times K_{c_{2}}$, and there is no coupling term mixing the two coordinates, in sharp contrast with the biquaternion algebra, where that term is the obstruction to a global reduction. For a finite system of generators the attractor is the set of the matched pairs, the image of the coding space under the pair of the two coding maps, a graph-like subset of the product of the two coordinate attractors, of the dimension of one coordinate attractor and not of the sum; the interaction between the two coordinates is exactly the identity of the coding. The singular sets are read from the two complex slices: for the quadratic family the slice on a coordinate plane is either a full complex filled Julia set or empty, so the singular part of the fractal is thin, of the dimension of a complex slice, whereas in the non-commutative companion the singular manifold has the dimension of the algebra. The connectedness of the quadratic filled set is exactly the connectedness of the two complex filled sets, that is the membership of the parameter in the product of the two Mandelbrot sets.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_{1,2}=\tfrac12(1\pm j)$ | the two central idempotents |
| $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ | the global decomposition |
| $T=q_1\Pi_{1}+q_2\Pi_{2}$ | the element and its idempotent coordinates |
| $f_{i}(q_1,q_2)=(f_{i}^{+}(q_1),f_{i}^{-}(q_2))$ | a generator of a system, a pair of complex maps |
| $\mathcal{K}=\bigcup_{i}f_{i}(\mathcal{K})$ | the attractor, the split fractal |
| $\mathcal{K}=\{(h^{+}(\sigma),h^{-}(\sigma)):\sigma\in\Sigma\}$ | the matched set of the coding space |
| $\mathscr{Z}=\{q_1=0\}\cup\{q_2=0\}$ | the zero-divisor cone, the singular set |
| $\mathcal{K}_{C}\cap\mathscr{Z}$ | the singular slices, full complex filled sets or empty |

## Further Reading

- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), above this article in this category, for the idempotents and the coordinates.
- *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the decomposition of the algebra into the idempotent lines.
- *The Reduced Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-reduced-biquaternion-quadratic-map-and-its-julia-sets.md`), above this article, for the quadratic family and its product fractal.
- *The Slices of the Reduced Biquaternion Julia Sets* (`articles_maths/the-slices-of-the-reduced-biquaternion-julia-sets.md`), below this article, for the slices computed from the product.
- *The Reduced Biquaternion Iterated Function Systems* (`articles_maths/the-reduced-biquaternion-iterated-function-systems.md`), below this article, for the contractions and the dimension of the attractors.
- *The Idempotent Decomposition and the Split Fractal* (`articles_maths/the-idempotent-decomposition-and-the-split-fractal.md`), for the companion in which the idempotents are not central, the decomposition is only local and the coupling term is nonzero.
