# __The Split-Biquaternion Julia Sets__

## Introduction

The split-biquaternion Julia set is the boundary of the product of two quaternion filled Julia sets, and its geometry is the geometry of a product: it is connected exactly when both factors are connected, it is a dust exactly when one factor is a dust, its local structure is the product of the local structures of the factors, and its symmetries are the symmetries of the two factors together with the swap. The article describes the fractal in these terms, computes the parameter slice carried by the split-complex scalar line, where the connectedness locus is a square and the quaternion factors are solids of revolution, and compares the product with the biquaternion fractal, which is not a product.

The family and its reduction are *The Split-Biquaternion Quadratic Family*; the quaternion fractal and its structure are *The Quaternion Quadratic Map and Its Julia Sets* and *The Slices of the Quaternion Julia Sets*; the quaternion connectedness locus is *The Quaternion Mandelbrot Set*; the product formula for the dimension and the product topology are *Fractal Geometry*; the central idempotents are *Split-Biquaternion Idempotents and Projections*. The biquaternion comparison is *The Idempotent Decomposition and the Split Fractal* and *The Biquaternion Quadratic Map and Its Julia Sets*. No physics is invoked.

The article owns the topology of the split-biquaternion Julia set as a product, the description of its components and dust, the split-complex scalar slice and its square connectedness locus, the solid-of-revolution description of the factors, the symmetry of the fractal, and the comparison with the biquaternion case.

**Standing convention.** $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ via $\tilde Q=\tilde Q_+\tilde\Pi_++\tilde Q_-\tilde\Pi_-$, $\tilde\Pi_\pm=\tfrac12(e_0\pm j)$; $K_{\tilde C}=K_{\tilde C_+}\times K_{\tilde C_-}$ and $J_{\tilde C}=\partial K_{\tilde C}$; for a quaternion parameter $\tilde c\in\mathbb{H}$ the filled Julia set and the Julia set of $f_{\tilde c}(\tilde q)=\tilde q^2+\tilde c$ are written $K_{\tilde c}$ and $J_{\tilde c}$.

## The Product Structure of the Fractal

**Theorem (topology of the product).** The split-biquaternion Julia set is

$$
J_{\tilde C}=\bigl(J_{\tilde C_+}\times K_{\tilde C_-}\bigr)\cup\bigl(K_{\tilde C_+}\times J_{\tilde C_-}\bigr),
$$

and the following hold.

1. $K_{\tilde C}$ is connected if and only if both $K_{\tilde C_\pm}$ are connected.
2. $K_{\tilde C}$ is locally connected if and only if both $K_{\tilde C_\pm}$ are locally connected.
3. $\dim_HK_{\tilde C}=\dim_HK_{\tilde C_+}+\dim_HK_{\tilde C_-}$, and $\dim_HJ_{\tilde C}=\max\bigl(\dim_HJ_{\tilde C_+}+\dim_HK_{\tilde C_-},\ \dim_HK_{\tilde C_+}+\dim_HJ_{\tilde C_-}\bigr)$; when a factor has empty interior, $J_{\tilde C_\pm}=K_{\tilde C_\pm}$ there and the second formula reduces to $\dim_HJ_{\tilde C}=\dim_HK_{\tilde C}$.
4. $K_{\tilde C}$ has empty interior if and only if one of $K_{\tilde C_\pm}$ does.

**Proof.** Every statement is the corresponding statement for the product of two compact subsets of $\mathbb{R}^4$: products of connected spaces are connected and conversely for non-empty factors; local connectedness is preserved by finite products and is a property of each factor when the other is non-degenerate; the product formula for the Hausdorff dimension holds for the filled Julia sets of the quadratic family (*Fractal Geometry*, §*Products and the Dimension Formula*); the boundary of the product is $(J_{\tilde C_+}\times K_{\tilde C_-})\cup(K_{\tilde C_+}\times J_{\tilde C_-})$, whose dimension is the maximum of the two product terms by the same formula; and a product has empty interior exactly when a factor does (Fubini).

**Remark (the dust and the body).** If both quaternion factors are connected bodies of dimension four, the split-biquaternion Julia set is a seven-dimensional boundary of an eight-dimensional body. If one quaternion factor is a Cantor set, the product is a Cantor-like dust of smaller dimension and the fractal is disconnected. **The whole phase space of the split-biquaternion dynamics is a product of two four-dimensional phase spaces, and a picture of the fractal in any subspaces is a picture of a product.**

## The Fatou Set and the Two Julia Sets

**Proposition (the Fatou set is a product).** The Fatou set of the split-biquaternion family is the product of the two quaternion Fatou sets,

$$
\mathcal{F}_{\tilde C}=\mathcal{F}_{\tilde C_+}\times\mathcal{F}_{\tilde C_-},
$$

and the dynamical Julia set of the family, the complement of the Fatou set, is the union of the two cylinders

$$
\mathcal{J}_{\tilde C}=\bigl(\mathcal{J}_{\tilde C_+}\times\mathbb{H}\bigr)\cup\bigl(\mathbb{H}\times\mathcal{J}_{\tilde C_-}\bigr).
$$

**Proof.** A family of maps of a product is normal if and only if both factor families are normal, since equicontinuity is checked in each coordinate; hence the Fatou set is the product and the complement is the union of the two cylinders.

**Remark (the two Julia sets differ for a product).** In one variable the dynamical Julia set and the boundary of the filled Julia set coincide. For the product they need not: the set-theoretic Julia set of the article is $\partial K_{\tilde C}=(J_{\tilde C_+}\times K_{\tilde C_-})\cup(K_{\tilde C_+}\times J_{\tilde C_-})$, and it is strictly contained in the dynamical Julia set: the cylinder $J_{\tilde C_+}\times\mathbb{C}$ lies in the dynamical Julia set, because the $z$-factor is non-normal there, while it meets $\partial K_{\tilde C}$ only in $J_{\tilde C_+}\times K_{\tilde C_-}$, a proper subset of the cylinder since $K_{\tilde C_-}\neq\mathbb{C}$ (the basin of infinity is non-empty). **The split-biquaternion fractal is the product fractal of the set-theoretic definition, and the dynamical Julia set of the normality definition is the larger union of cylinders; the two are distinguished exactly as in the biquaternion case (*The Biquaternion Holomorphic Dynamics and the Jacobian*).**

**Remark (the domain of the local theory).** The family is a local diffeomorphism exactly where both quaternion factors are, that is, off the union of the two hyperplanes $\{\operatorname{Re}\tilde Q_+=0\}$ and $\{\operatorname{Re}\tilde Q_-=0\}$; the zero-divisor set $\{\tilde Q_+=0\}\cup\{\tilde Q_-=0\}$, on which a whole factor vanishes, is the smaller part of the critical set that is special to the split algebra. **The critical set of the biquaternion algebra is the union of the cone and the vector subspace, a quadric with a hyperplane; the critical set of the split-biquaternion algebra is the union of the two quaternion critical hyperplanes, so the local theory off it is the product of the quaternion local theories.**

## The Split-Complex Scalar Slice

**Theorem (the $\mathbb{D}$-line).** Let $\tilde C=\lambda e_0$ with $\lambda\in\mathbb{D}$, and write $\lambda=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ with $\lambda_\pm\in\mathbb{R}$. Then $\tilde C_\pm=\lambda_\pm e_0$ are real, and the connectedness locus of the family restricted to the $\mathbb{D}$-line is the square

$$
\bigl\{\lambda\in\mathbb{D} : K_{\lambda e_0} \text{ connected}\bigr\}\;=\;\{\lambda : \lambda_+\in[-2,\tfrac14],\ \lambda_-\in[-2,\tfrac14]\} ,
$$

the square of the real Mandelbrot interval.

**Proof.** For a real parameter $c\in\mathbb{R}$ the quaternion connectedness locus is the real interval $[-2,\tfrac14]$ (*The Quaternion Mandelbrot Set*); the connectedness locus of the product is the product of the two quaternion loci, and the $\mathbb{D}$-line is the set of pairs $(\lambda_+,\lambda_-)$, giving the square.

**Theorem (the solids of revolution).** For a real quaternion parameter $c\in[-2,\tfrac14]$ the quaternion filled Julia set is the solid of revolution about the real axis,

$$
K_c=\{\tilde q\in\mathbb{H} : (\operatorname{Sc}\tilde q,\ |\operatorname{Vect}\tilde q|)\in K_c^{\mathbb{C}}\} ,
$$

where $K_c^{\mathbb{C}}$ is the complex filled Julia set of $z\mapsto z^2+c$. Hence on the $\mathbb{D}$-line the split-biquaternion filled Julia set is the product of two such solids of revolution, one for each component.

**Proof.** For a real parameter the orbit of $\tilde q$ stays in the plane spanned by $1$ and $\tilde q$, which is a copy of $\mathbb{C}$, and the point $\tilde q$ corresponds to the complex number $\operatorname{Sc}\tilde q+i|\operatorname{Vect}\tilde q|$; the orbit is that of the complex quadratic map of the real parameter, whence the description (*The Slices of the Quaternion Julia Sets*).

**Remark (the $\mathbb{D}$-line is the fully symmetric line).** The $\mathbb{D}$-scalar parameters are fixed by every automorphism of the algebra that preserves the idempotents, so the fractal on the $\mathbb{D}$-line has the full symmetry of the algebra; **the square of the real Mandelbrot interval is the base of the family, and it is the only slice whose connectedness locus is a square.** The other slices have products of the corresponding quaternion loci.

## Components, Dust and the Parameter Square

**Proposition (the components).** The connected components of $J_{\tilde C}$ are the products of the components of the two factors: if $J_{\tilde C_+}$ has components $(E_j)$ and $K_{\tilde C_-}$ has components $(F_k)$, then the components of $J_{\tilde C}$ are the sets $E_j\times F_k$ together with $K_{\tilde C_+}\times G_l$ for the components $G_l$ of $J_{\tilde C_-}$.

**Proof.** The components of a product of compact spaces are the products of the components, and $J_{\tilde C}$ is the union of the two products of the statement.

**Remark (the parameter diagram).** The connectedness locus is the square of the quaternion connectedness locus, so the parameter diagram of the split-biquaternion family is the two-dimensional fibre product of the quaternion diagram with itself; its boundary is the union of the two cylinders over the quaternion Mandelbrot boundary. **The Mandelbrot picture of the split-biquaternion family is a square made of two copies of the quaternion picture, and no new bifurcation appears**: the bifurcations of the family are the pairs of the bifurcations of the two quaternion factors.

## Symmetry

**Proposition (the symmetry group).** The fractal $J_{\tilde C}$ is invariant under the product of the symmetry groups of the two quaternion factors and under the swap,

$$
\mathrm{Sym}(J_{\tilde C})\supset \mathrm{Sym}(J_{\tilde C_+})\times\mathrm{Sym}(J_{\tilde C_-})\rtimes\mathbb{Z}/2 ,
$$

and for a $\mathbb{D}$-scalar parameter the symmetry is the full product of the quaternion symmetries of the two factors together with the swap.

**Proof.** The group $\mathrm{Sym}(J_+)\times\mathrm{Sym}(J_-)$ acts componentwise and preserves the product; the swap exchanges the factors and maps $K_+\times K_-$ to $K_-\times K_+$, which is the filled Julia set of the swapped parameter, so it preserves $J_{\tilde C}$ when the parameter is exchanged accordingly, and for a $\mathbb{D}$-scalar parameter it preserves the set outright.

**Remark (contrast with the biquaternion symmetry).** The biquaternion fractal has only the diagonal symmetry of the conjugations, because the idempotents are not central and the two halves cannot be rotated independently (*The Three Conjugations and the Symmetric Biquaternion Fractals*). The split-biquaternion fractal has the full product symmetry. **The centrality of the idempotents enlarges the symmetry from the diagonal to the product, and the fractal reflects it.**

## Comparison with the Biquaternion Case

**Remark (product against coupling).** The biquaternion fractal restricted to the idempotent plane is a product, and off the plane it is coupled; the split-biquaternion fractal is a product everywhere. The comparison is exact: the central idempotents of the split-biquaternion algebra give $\mathbb{H}_{\mathbb{D}}=\mathbb{H}\tilde\Pi_+\oplus\mathbb{H}\tilde\Pi_-$ as a direct sum of two ideals, whereas the idempotents of the biquaternion algebra give only the Peirce decomposition of the space with a non-zero off-diagonal block. **One algebra is a product, the other is a simple algebra, and the fractal theory is a product theory in the first case and an irreducible one in the second.**

**Remark (what the split side cannot have).** The split-biquaternion algebra is not a division algebra and its $\mathbb{D}$-valued norm is indefinite, so its fractal theory has zero divisors and no natural pluripotential theory; the fractal is a product and the analysis is the quaternion analysis on two factors. The biquaternion algebra has a complex structure and a pluripotential theory, and pays for it with the coupling and the cone. **Neither algebra contains the other, and the two threads are the two resolutions of the quadratic family over the quaternions.**

## Summary

The split-biquaternion Julia set is the boundary of the product of two quaternion filled Julia sets, and its topology, its connectedness, its local connectedness, its dimension and its components are the product statements of the two factors; it is a seven-dimensional boundary of an eight-dimensional body when both factors are bodies and a dust when a factor is a dust. On the split-complex scalar line the parameters are pairs of real numbers, the connectedness locus is the square of the real Mandelbrot interval, and each quaternion factor is a solid of revolution of a complex filled Julia set. The parameter diagram is the fibre product of the quaternion diagram with itself, so no new bifurcation appears. The symmetry of the fractal is the product of the symmetries of the two factors extended by the swap, larger than the diagonal symmetry of the biquaternion fractal; the difference is exactly the centrality of the idempotents, which makes the split-biquaternion algebra a product and leaves the biquaternion algebra simple. The Fatou set is the product of the two quaternion Fatou sets and the dynamical Julia set is the union of the two cylinders, strictly larger than the set-theoretic Julia set $\partial K_{\tilde C}$ whenever a factor has interior; the local theory is defined off the union of the two quaternion critical hyperplanes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $K_{\tilde C}=K_{\tilde C_+}\times K_{\tilde C_-}$ | the filled Julia set |
| $J_{\tilde C}=\partial K_{\tilde C}$ | the Julia set |
| $K_{\tilde c}$, $J_{\tilde c}$ | the quaternion filled Julia set and Julia set |
| $K_c^{\mathbb{C}}$ | the complex filled Julia set of $z\mapsto z^2+c$ |
| $[-2,\tfrac14]$ | the real (and quaternion, on the real line) connectedness interval |
| $\lambda=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ | the split-complex scalar parameter |
| $\mathrm{Sym}(J_{\tilde C})$ | the symmetry group of the fractal |

## Further Reading

- *The Split-Biquaternion Quadratic Family* (`articles_maths/the-split-biquaternion-quadratic-family.md`), for the reduction, the escape lemma and the connectedness criterion.
- *The Quaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-quaternion-quadratic-map-and-its-julia-sets.md`) and *The Slices of the Quaternion Julia Sets* (`articles_maths/the-slices-of-the-quaternion-julia-sets.md`), for the two factors.
- *The Quaternion Mandelbrot Set* (`articles_maths/the-quaternion-mandelbrot-set.md`), for the connectedness interval and the parameter picture of a factor.
- *The Idempotent Decomposition and the Split Fractal* (`articles_maths/the-idempotent-decomposition-and-the-split-fractal.md`), for the biquaternion coupling that the split side lacks.
- *Fractal Geometry* (`articles_maths/fractal-geometry.md`), for the product formula and the product topology used here.
