# __The Reduced Biquaternion Quadratic Map and Its Julia Sets__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ of basis $1,i,j,ij$, with element $T=A+Bj$, idempotent coordinates $(q_1,q_2)=(A+B,A-B)$ and the two central idempotents $\Pi_{1,2}=\tfrac12(1\pm j)$. The quadratic family of the algebra is

$$
F_{C}(T)=T^{2}+C,\qquad C\in\mathbb{B}_{\mathrm{r}},
$$

and it is the subject of the article. The single structural fact that decides everything is that the multiplication is componentwise in the idempotent coordinates, so the map is the pair of two complex quadratic maps,

$$
F_{C}(q_1,q_2)=\bigl(q_1^{2}+c_{1},\;q_2^{2}+c_{2}\bigr),\qquad C=c_{1}\Pi_{1}+c_{2}\Pi_{2},
$$

and the dynamics of the reduced biquaternion quadratic map is therefore the dynamics of a pair of independent complex quadratic maps. The square is unambiguous here, the algebra being commutative; the filled Julia set is the product of the two complex filled Julia sets; the Julia set is the boundary of that product; the critical set is the zero-divisor cone; and the escape is read from the topological norm.

The article owns the map, the unique reading of the square, the family, the filled Julia set and the Julia set with their product description, the equivariance under the involutions, the critical set and the central parameter. The algebra and the idempotents are *Reduced Biquaternion Space*; the zero divisors that form the critical set are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*; the topological norm that measures the escape is *Topology and Metric for Each of the Operations*; the idempotent decomposition and its consequences for the dynamics are *The Idempotent Decomposition and the Split Fractal*; the slices are *The Slices of the Reduced Biquaternion Julia Sets*; the dimension is *The Hausdorff Dimension of the Reduced Biquaternion Julia Sets*; the iterated function systems are *The Reduced Biquaternion Iterated Function Systems*; the connectedness locus is *The Reduced Biquaternion Mandelbrot Set and the Connectedness Locus*. The companion is *The Biquaternion Quadratic Map and Its Julia Sets*, where the non-commutativity makes the square ambiguous and the fractal is not a product.

**Conventions.** The topological norm is $K(T)=|A|^{2}+|B|^{2}=\tfrac12(|q_1|^{2}+|q_2|^{2})$, the Euclidean norm of the four-space; the algebraic norm is $\langle T\rangle_{\natural}=A^{2}-B^{2}=q_1q_2$, an element of the algebra; a set is **bounded** when it is bounded for $K$. The complex quadratic map of a parameter $c$ is $f_{c}(\zeta)=\zeta^{2}+c$, with filled Julia set $K_{c}$ and Julia set $J_{c}$.

## The Square and Its Unique Reading

**Proposition (the square is coordinatewise).** For $T=q_1\Pi_{1}+q_2\Pi_{2}$ the square is

$$
T^{2}=q_1^{2}\Pi_{1}+q_2^{2}\Pi_{2},
$$

and the reading is unique: the algebra being commutative, there is only one product of $T$ with itself, and the left, the right, the plain and the natural-sign products all give the same square.

**Proof.** The multiplication is $\Pi_{1}^{2}=\Pi_{1}$, $\Pi_{2}^{2}=\Pi_{2}$, $\Pi_{1}\Pi_{2}=0$, so $T^{2}=q_1^{2}\Pi_{1}+q_2^{2}\Pi_{2}$; in a commutative algebra the products $TT$, $T T^{\natural}$ and $T^{*}T$ are related by the involutions and the coefficient conjugation, and $TT$ is the square of the algebra. The biquaternion square, by contrast, has several readings because the multiplication is not commutative.

**Corollary (the derivative and the critical set).** The derivative of the square is the multiplication by $2T$, an operator that is singular exactly when $T$ is a zero divisor; the derivative vanishes identically only at $T=0$. Hence the critical set of the map in the sense of the points where the derivative is not invertible is the zero-divisor cone

$$
\mathscr{Z}=\{q_1=0\}\cup\{q_2=0\},
$$

and the unique classical critical point is the origin.

**Proof.** The derivative of $T\mapsto T^{2}$ at $T$ in the direction $H$ is $TH+HT=2TH$, the multiplication by $2T$; that operator is invertible exactly when $2T$ is a unit, that is when $q_1\neq0$ and $q_2\neq0$; and the operator is zero exactly when $T=0$.

## The Quadratic Family

**Definition (the family).** The **quadratic family** of the reduced biquaternion algebra is the family $F_{C}(T)=T^{2}+C$, parametrised by the algebra, and in the idempotent coordinates it is the pair of complex quadratic maps

$$
F_{c_{1},c_{2}}(q_1,q_2)=\bigl(q_1^{2}+c_{1},\;q_2^{2}+c_{2}\bigr).
$$

**Proposition (the family is a product family).** The family is the product of the complex quadratic families of the two coordinates, and every dynamical statement about $F_{C}$ is the corresponding statement about the two complex maps $f_{c_{1}}$ and $f_{c_{2}}$.

**Proof.** The two coordinates evolve independently, since the map changes each by its own complex quadratic map and the norm reads the two coordinates separately.

**Remark (the central and the non-central parameters).** A parameter $C=c\cdot1$ is **central**, with $c_{1}=c_{2}=c$, so the two complex maps coincide and the fractal is the product of a complex fractal with itself, invariant under the exchange of the two coordinates; a general parameter is the pair of two possibly different complex parameters, and the exchange symmetry is then broken. Every parameter of the algebra is realised, so the family is the full product of two complex quadratic families.

## The Filled Julia Set and the Julia Set

**Definition (the two sets).** The **filled Julia set** of $F_{C}$ is

$$
\mathcal{K}_{C}=\{T\in\mathbb{B}_{\mathrm{r}}:\text{the orbit }F_{C}^{n}(T)\text{ is bounded}\},
$$

and the **Julia set** $\mathcal{J}_{C}$ is its boundary.

**Theorem (the product description).** With $C=c_{1}\Pi_{1}+c_{2}\Pi_{2}$,

$$
\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}},\qquad
\mathcal{J}_{C}=\partial\bigl(K_{c_{1}}\times K_{c_{2}}\bigr)
=\bigl(J_{c_{1}}\times K_{c_{2}}\bigr)\cup\bigl(K_{c_{1}}\times J_{c_{2}}\bigr),
$$

the product of the two complex filled Julia sets being read in the idempotent coordinates.

**Proof.** The orbit of $T=(q_1,q_2)$ is the pair of the orbits of $q_1$ under $f_{c_{1}}$ and of $q_2$ under $f_{c_{2}}$, and the orbit is bounded for the topological norm exactly when both coordinate orbits are bounded; hence the filled set is the product. For a product of two compact sets the boundary is the union of the two products obtained by replacing one factor by its boundary, which gives the second identity since $K_{c}=J_{c}\cup\operatorname{int}K_{c}$ and the interior of the product is the product of the interiors.

**Corollary (the escape criterion).** An element escapes to infinity, that is its orbit is unbounded, exactly when one of its two coordinates escapes for the corresponding complex map; the numerical criterion is the classical one, applied to each coordinate.

**Proof.** The norm $\langle\cdot\rangle_{\natural*}$ is the half-sum of the squared moduli of the coordinates, so it is unbounded exactly when one of the two moduli is unbounded; the complex criterion $|\zeta|>R$ with $R$ the standard escape radius of the quadratic family is applied to each coordinate.

**Remark (the direct product survives the dynamics).** The filled Julia set is exactly a product, and not merely contained in one, because the single generator $F_{C}$ acts coordinatewise with the same index on the two coordinates; the product structure of the algebra and the product structure of the fractal are the same product. This is the essential difference from the non-commutative companion, where the filled set is not a product and the coupling terms appear.

## The Conjugations and the Equivariance

**Proposition (the equivariance).** Let $g$ be one of the involutions $\bar{\cdot}$, ${}^{\natural}$, ${}^{*}$. Then

$$
F_{C}\bigl(g(T)\bigr)=g\bigl(F_{g(C)}(T)\bigr),
$$

so $g$ maps the dynamics of $C$ to the dynamics of $g(C)$; in particular $g$ maps $\mathcal{K}_{C}$ onto $\mathcal{K}_{g(C)}$ and $\mathcal{J}_{C}$ onto $\mathcal{J}_{g(C)}$, and if $g(C)=C$ then $g$ preserves both sets.

**Proof.** Each involution is a real-algebra isomorphism onto its image and an isometry of the topological norm, so it commutes with the squaring and carries the translation by $C$ to the translation by $g(C)$; the statement about the sets follows from the uniqueness of the filled Julia set as the bounded orbit locus.

**Corollary (the symmetry group of a real parameter).** A parameter fixed by all three involutions is central and real, $C=c\cdot1$ with $c\in\mathbb{R}$, and then the dynamics is equivariant under the whole group of involutions; a central complex parameter, $C=c\cdot1$ with $c$ non-real, is fixed by the natural sign and by no other nontrivial involution.

**Proof.** The fixed set of the coefficient conjugation is the real-coefficient subspace, the fixed set of the natural sign is the set of elements with $B=0$, and the fixed set of the star is their intersection; the central elements are the ones with $B=0$, and their bar-fixed part is the real central line.

## The Critical Set and the Central Parameter

**Proposition (the critical orbits).** The critical set is the zero-divisor cone $\mathscr{Z}=\{q_1=0\}\cup\{q_2=0\}$, and the critical orbits are the orbits of its elements; the orbit of the origin is the orbit of the pair $(0,0)$, that is of the pair of the critical points of the two complex maps.

**Proof.** The critical set is the set where the derivative is not invertible, which is the zero-divisor cone by the corollary above, and the origin is the unique point where the derivative vanishes.

**Theorem (the central parameter).** For a central parameter $C=c\cdot1$ the two complex maps coincide, the filled Julia set is $K_{c}\times K_{c}$, and the Julia set is $\partial(K_{c}\times K_{c})=(J_{c}\times K_{c})\cup(K_{c}\times J_{c})$. At the parameter zero, $K_{0}$ is the product of two unit discs and $\mathcal{K}_{0}$ is a solid bidisc of real dimension four, while $\mathcal{J}_{0}$ is its boundary, of real dimension three.

**Proof.** The central parameter has $c_{1}=c_{2}=c$ by definition, and the product formulae apply; at $c=0$ the complex filled Julia set is the closed unit disc, so the product is the bidisc and its boundary is the union of the two products of a circle and a disc, of real dimension three.

**Corollary (the singular part at the parameter zero).** The intersection of the Julia set at the parameter zero with the zero-divisor cone is the union of the two circles

$$
\mathcal{J}_{0}\cap\mathscr{Z}=\bigl(\{0\}\times S^{1}\bigr)\cup\bigl(S^{1}\times\{0\}\bigr),
$$

of real dimension one.

**Proof.** On the plane $q_1=0$ the pair is $(0,q_2)$ and the boundary of the bidisc meets that plane in the circle $|q_2|=1$; likewise for $q_2=0$.

**Remark (thin singular part).** In the reduced biquaternion dynamics the singular part of the fractal at the parameter zero is a pair of circles, of real dimension one; in the biquaternion dynamics the corresponding singular part contains a real four-dimensional manifold. The difference is the difference between a product of two one-complex-dimensional dynamics, where the singularities are the coordinate planes of the product, and a higher-dimensional dynamics with a genuine critical hypersurface.

## Summary

The quadratic map of the reduced biquaternion algebra is $F_{C}(T)=T^{2}+C$, and because the algebra is commutative the square has a single reading: in the idempotent coordinates the map is the pair $F_{C}(q_1,q_2)=(q_1^{2}+c_{1},q_2^{2}+c_{2})$ of two complex quadratic maps. The filled Julia set is exactly the product $\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}}$ of the two complex filled Julia sets, the Julia set is the boundary of that product, the union of the two mixed products of a boundary and a filled set, and the escape of an orbit is the escape of one of its coordinates. The derivative is the multiplication by $2T$, which is singular exactly on the zero-divisor cone $\{q_1=0\}\cup\{q_2=0\}$ and vanishes only at the origin, so the critical set is the cone and the unique classical critical point is the origin. The involutions are equivariances, carrying the dynamics of a parameter to the dynamics of its image, and a real central parameter is fixed by the whole group. For a central parameter the two complex maps coincide and the fractal is the product of a complex fractal with itself; at the parameter zero the filled set is a solid bidisc of real dimension four, the Julia set is its boundary of real dimension three, and the singular part of the Julia set is a pair of circles of real dimension one, thin where the non-commutative companion has a four-dimensional singular manifold.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F_{C}(T)=T^{2}+C$ | the quadratic map of the algebra |
| $(q_1,q_2)=(A+B,A-B)$ | the idempotent coordinates, $T=q_1\Pi_{1}+q_2\Pi_{2}$ |
| $C=c_{1}\Pi_{1}+c_{2}\Pi_{2}$ | the parameter in idempotent coordinates |
| $f_{c}(\zeta)=\zeta^{2}+c$ | the complex quadratic map |
| $\mathcal{K}_{C}=K_{c_{1}}\times K_{c_{2}}$ | the filled Julia set, the product of the two complex filled Julia sets |
| $\mathcal{J}_{C}=\partial(K_{c_{1}}\times K_{c_{2}})$ | the Julia set |
| $\mathscr{Z}=\{q_1=0\}\cup\{q_2=0\}$ | the critical set, the zero-divisor cone |
| \langle T\rangle_{\natural*}=\tfrac12(\lvert q_1\rvert^{2}+\lvert q_2\rvert^{2})$ | the topological norm that measures the escape |
| $F_{C}\circ g=g\circ F_{g(C)}$ | the equivariance under an involution $g$ |

## Further Reading

- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), above this article in this category, for the multiplication, the idempotents and the coordinates.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the critical cone.
- *The Idempotent Decomposition and the Split Fractal* (`articles_maths/the-idempotent-decomposition-and-the-reduced-biquaternion-split-fractal.md`), below this article, for the proof that the decomposition is global.
- *The Slices of the Reduced Biquaternion Julia Sets* (`articles_maths/the-slices-of-the-reduced-biquaternion-julia-sets.md`), below this article, for the slices of the fractal.
- *The Hausdorff Dimension of the Reduced Biquaternion Julia Sets* (`articles_maths/the-hausdorff-dimension-of-the-reduced-biquaternion-julia-sets.md`), below this article, for the dimension.
- *The Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-biquaternion-quadratic-map-and-its-julia-sets.md`), for the companion in which the square is ambiguous and the fractal is not a product.
