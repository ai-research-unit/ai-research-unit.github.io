# __The Mod 2 Cohomology of an Involution__

## Introduction

An involution is the action of the group of order two, and with coefficients in the field $\mathbb{F}_2$ its cohomology is a single computable package: the equivariant cohomology is the cohomology of the homotopy quotient $X_{\mathbb{Z}/2} = X\times_{\mathbb{Z}/2}E\mathbb{Z}/2$, it is a module over the polynomial ring $\mathbb{F}_2[x] = H^*(B\mathbb{Z}/2;\mathbb{F}_2)$ with $|x|=1$, and the Borel fibration $X\to X_{\mathbb{Z}/2}\to\mathbb{RP}^{\infty}$ carries a Serre spectral sequence whose differential is the transgression of the involution. Because the coefficients are $\mathbb{F}_2$, no sign enters, the spectral sequence is especially simple, and the whole theory is the interaction of two facts: the **fixed set** $F = X^{\sigma}$ controls the module up to the localization that inverts $x$, and the mod 2 homology of $F$ is bounded by that of $X$ — the **Smith inequality**. This is the mod 2 chapter of the equivariant cohomology of an involution, and it is the case of the Borel model of *Equivariant Cohomology* in which the action of the group is the order two.

The article develops the package. It defines the homotopy quotient of an involution, records its cohomology ring and its structure as a module over $\mathbb{F}_2[x]$, writes down the Serre spectral sequence of the Borel fibration and identifies the transgression with the fixed-set restriction, proves the localization theorem that the fixed set computes the equivariant cohomology after inverting $x$, states the Smith inequality and the Smith theorem on homology spheres for the involution, and closes with the computations for the spheres, the projective spaces and the tori. The Borel construction for $\mathbb{Z}/2$ is that of *Two-Fold Coverings and the Borel Construction*; the equivariant cohomology and the Borel fibration are those of *Equivariant Cohomology*; the spectral sequence is that of *The Leray–Serre Spectral Sequence*; the coefficient rings $H^*(\mathbb{RP}^{\infty};\mathbb{F}_2)$ and $H^*(\mathbb{RP}^n;\mathbb{F}_2)$ are those of *Cup and Cap Products*; and the general Smith theory of a periodic map of period $p$ is the subject of the following article *Smith Theory and the Fixed Sets of Periodic Maps*, of which the present article is the mod-2 case. The transfer and its action on the fixed set are those of *The Transfer and the Involution*, later in this category.

Nothing analytic and nothing geometric is used. The article is the cohomology of a space with a self-map of order two and its fixed set; the spaces are finite-dimensional complexes when the Smith theorem is stated, so that the homological algebra is finite, and no distance, no norm, no measure and no smooth structure is chosen. Throughout, $(X,\sigma)$ is a space with an involution $\sigma$, $X^{\sigma} = F$ is its **fixed set**, the coefficient field is $\mathbb{F}_2 = \mathbb{Z}/2$, and all cohomology is singular cohomology with $\mathbb{F}_2$ coefficients unless stated. The **homotopy quotient** is $X_{\mathbb{Z}/2} = X\times_{\mathbb{Z}/2}E\mathbb{Z}/2$ and the **equivariant cohomology** is $H_{\mathbb{Z}/2}^*(X) = H^*(X_{\mathbb{Z}/2})$; the generator of $H^1(B\mathbb{Z}/2;\mathbb{F}_2) = H^1(\mathbb{RP}^{\infty};\mathbb{F}_2)$ is written $x$, so that $H^*(B\mathbb{Z}/2;\mathbb{F}_2) = \mathbb{F}_2[x]$. All modules are graded $\mathbb{F}_2[x]$-modules.

## The Equivariant Cohomology of an Involution

### The Homotopy Quotient

**Definition.** For a space with an involution $(X,\sigma)$ the **homotopy quotient** is

$$
X_{\mathbb{Z}/2} = X\times_{\mathbb{Z}/2}E\mathbb{Z}/2 = \frac{X\times S^{\infty}}{(x,e)\sim(\sigma x, -e)},
$$

the quotient of the product by the diagonal involution, where $E\mathbb{Z}/2 = S^{\infty}$ with the antipodal involution; the **equivariant cohomology** is $H_{\mathbb{Z}/2}^*(X) = H^*(X_{\mathbb{Z}/2};\mathbb{F}_2)$.

**Theorem.** The diagonal involution on $X\times S^{\infty}$ is free, so the projection

$$
p : X_{\mathbb{Z}/2} \longrightarrow B\mathbb{Z}/2 = \mathbb{RP}^{\infty}
$$

is a fibre bundle with fibre $X$, the **Borel fibration** of the involution; the construction is natural for equivariant maps and homotopy invariant for equivariant homotopies. For the free involution the projection $X\times S^{\infty}\to X$ descends to a homotopy equivalence $X_{\mathbb{Z}/2}\simeq X/\sigma$, so that $H_{\mathbb{Z}/2}^*(X)\cong H^*(X/\sigma)$.

*Proof.* The construction of *Two-Fold Coverings and the Borel Construction* with the group of order two; freeness is that $S^{\infty}$ has no antipodal fixed point, the fibre bundle is the quotient of the product projection, and the homotopy equivalence in the free case is that theorem. $\square$

### The Module Structure

**Theorem.** The projection $p$ makes $H_{\mathbb{Z}/2}^*(X)$ a graded module over

$$
H^*(B\mathbb{Z}/2;\mathbb{F}_2) = \mathbb{F}_2[x], \qquad |x| = 1,
$$

the action being the pullback $p^*$ followed by the cup product; the module is finitely generated in each degree when $X$ has finitely generated cohomology, and the action is compatible with the cup product on $H_{\mathbb{Z}/2}^*(X)$, so that $H_{\mathbb{Z}/2}^*(X)$ is a graded $\mathbb{F}_2[x]$-algebra. The restriction to the fibre is a ring homomorphism $H_{\mathbb{Z}/2}^*(X)\to H^*(X)$ that makes $H^*(X)$ a module over the equivariant ring, and on the unit component it is the map $H^*(B\mathbb{Z}/2)\to H^*(\mathrm{pt}) = \mathbb{F}_2$ sending $x$ to $0$.

*Proof.* The pullback of the cohomology of the base along the projection is a ring homomorphism, and the cup product makes the target an algebra over the source by the module structure of *The Cup Product as an Operator*; the statement about the fibre is the naturality of the restriction to a fibre. $\square$

The module structure is the algebraic content of the involution: the class $x$ acts by a degree-one operator on $H_{\mathbb{Z}/2}^*(X)$, and the whole equivariant cohomology is the module generated by the fibre cohomology under this operator and the cup product.

### The Serre Spectral Sequence

**Theorem.** The Borel fibration has the Serre spectral sequence of *The Leray–Serre Spectral Sequence* with

$$
E_2^{p,q} = H^p(B\mathbb{Z}/2;\mathbb{F}_2)\otimes_{\mathbb{F}_2} H^q(X;\mathbb{F}_2) = \mathbb{F}_2[x]\otimes_{\mathbb{F}_2} H^q(X;\mathbb{F}_2) \ \Longrightarrow \ H_{\mathbb{Z}/2}^{p+q}(X),
$$

the monodromy being trivial because the local system of the fibre cohomology over $\mathbb{RP}^{\infty}$ is trivial in $\mathbb{F}_2$ coefficients; the differentials are derivations with respect to the $\mathbb{F}_2[x]$-module structure, $d_r(x\cdot a) = x\cdot d_r(a)$ for $r \geq 2$, and the sequence converges to the equivariant cohomology with the filtration by the degree of $x$. The edge homomorphism of the base is $H^*(B\mathbb{Z}/2)\to H_{\mathbb{Z}/2}^*(X)$ and the edge homomorphism of the fibre is $H_{\mathbb{Z}/2}^*(X)\to H^*(X)$.

*Proof.* The Serre spectral sequence of the fibration $p$ with the trivial monodromy in $\mathbb{F}_2$ coefficients; the differentials are $\mathbb{F}_2[x]$-linear because they commute with the cup product by the base, and the edge maps are the standard ones of *The Leray–Serre Spectral Sequence*. $\square$

**Corollary.** If the spectral sequence collapses, that is if all the differentials vanish, then

$$
H_{\mathbb{Z}/2}^*(X) \cong \mathbb{F}_2[x]\otimes_{\mathbb{F}_2} H^*(X;\mathbb{F}_2)
$$

as a module over $\mathbb{F}_2[x]$, and it is free; the collapse holds for a free involution, for which the equivariant cohomology is $H^*(X/\sigma)$ and the module structure is the one induced by the projection $X/\sigma\to\mathbb{RP}^{\infty}$.

*Proof.* A spectral sequence with trivial differentials has $E_2 = E_\infty$, and the extension problem is trivial for a free module over $\mathbb{F}_2[x]$; the free case is the free-action computation above. $\square$

## The Fixed Set and the Localization

### The Localization Theorem

**Theorem (localization).** Let $(X,\sigma)$ be an involution of a finite-dimensional complex and let $F = X^{\sigma}$ be the fixed set. Then the inclusion $F\hookrightarrow X$ induces an isomorphism after inverting the class $x$,

$$
x^{-1} H_{\mathbb{Z}/2}^*(X) \;\cong\; x^{-1}H_{\mathbb{Z}/2}^*(F) \;\cong\; H^*(F;\mathbb{F}_2)\otimes_{\mathbb{F}_2}\mathbb{F}_2[x^{\pm1}],
$$

where $x^{-1}$ denotes the localization of the $\mathbb{F}_2[x]$-module at the multiplicative set generated by $x$. Equivalently, the equivariant cohomology away from the fixed set is $x$-torsion: every class in the kernel of the restriction to the fixed set is annihilated by a power of $x$.

*Proof.* The action of $\sigma$ on a small neighbourhood of a point outside the fixed set is free, and on such a neighbourhood the local system is the free module with the action of $x$ invertible; the localization computes the cohomology of the free part by the local computation and the fixed set contributes the non-free part, which is where the restriction is an isomorphism after inverting $x$. The theorem is the $\mathbb{Z}/2$ case of the localization theorem of *Equivariant Cohomology*, and the proof is by the equivariant cell decomposition of $X$ relative to $F$. $\square$

### The Fixed Set as the Free Part

**Corollary.** The rank of $H_{\mathbb{Z}/2}^*(X)$ as a module over $\mathbb{F}_2[x]$ is the dimension of $H^*(F;\mathbb{F}_2)$; more precisely, the module $H_{\mathbb{Z}/2}^*(X)$ is the direct sum of a free $\mathbb{F}_2[x]$-module of rank the total dimension of $H^*(F)$ and a torsion module supported away from the fixed set. Hence the fixed set is detected by the module structure at the generic point, and a free involution has no torsion of this kind and the module is free.

*Proof.* The localization theorem identifies the generic fibre of the module with $H^*(F)\otimes\mathbb{F}_2[x^{\pm1}]$, whose rank is $\dim_{\mathbb{F}_2}H^*(F)$; the complement is the torsion, and the torsion vanishes when the action is free. $\square$

So for an involution the equivariant mod 2 cohomology is a finitely generated module over a principal ideal domain in one variable, and it is classified by its rank, which is the fixed-set total dimension, and by its torsion, which is the part of the action that is not free.

## The Smith Theory

### The Inequality

**Theorem (Smith inequality; mod 2).** Let $\sigma$ be an involution of a finite-dimensional complex $X$ and let $F = X^{\sigma}$. Then

$$
\sum_i \dim_{\mathbb{F}_2} H_i(F;\mathbb{F}_2) \;\leq\; \sum_i \dim_{\mathbb{F}_2} H_i(X;\mathbb{F}_2),
$$

the total mod 2 Betti number of the fixed set is at most that of the space; more precisely, for each $i$,

$$
\dim_{\mathbb{F}_2} H_i(F;\mathbb{F}_2) \;\leq\; \dim_{\mathbb{F}_2} H_i(X;\mathbb{F}_2) + \dim_{\mathbb{F}_2} H_{i-1}(X;\mathbb{F}_2) + \cdots \leq \sum_j \dim_{\mathbb{F}_2} H_j(X;\mathbb{F}_2).
$$

*Proof.* The equivariant cohomology $H_{\mathbb{Z}/2}^*(X)$ is a finitely generated module over the principal ideal domain $\mathbb{F}_2[x]$, and the localization theorem identifies the rank with the total dimension of $H^*(F)$; the Euler-characteristic and rank arguments applied to the module, together with the fact that the equivariant cohomology surjects onto $H^*(X)$ and has the fibre cohomology as its quotient by $x$, give the stated bounds. The argument is the mod 2 case of the Smith theory of *Smith Theory and the Fixed Sets of Periodic Maps*. $\square$

### The Homology Spheres

**Theorem (Smith; mod 2).** Let $\sigma$ be an involution of a finite-dimensional complex $X$ whose mod 2 homology is that of an $n$-sphere, $H_i(X;\mathbb{F}_2) = \mathbb{F}_2$ for $i \in \{0,n\}$ and zero otherwise. Then either the fixed set is empty and the action preserves the sphere degree, or $F$ is a mod 2 homology $r$-sphere for some $r \le n$, and if $F \neq X$ then $r \le n - 1$; when $F\neq\emptyset$ the dimension drop is unconstrained in parity in this mod 2 case, the reflection of $S^n$ in an equatorial $S^{n-1}$ being the model.

*Proof.* The Smith inequality bounds the total dimension of $H^*(F)$ by two, so $F$ has the mod 2 homology of a point or of a sphere; the localization and the action of the group on the top class, which is either fixed or negated, rule out the intermediate cases, and the reflection realises the drop of one. The parity statement for an odd prime requires the transfer of *Smith Theory and the Fixed Sets of Periodic Maps*, and is not claimed here. $\square$

**Corollary.** An involution of a sphere without fixed points is free; the antipodal map of $S^n$ is free and has no fixed set and no fixed classes, while a reflection has the equatorial sphere as the fixed set. In both cases the fixed set is a mod 2 homology sphere of dimension at most $n$, and the mod 2 homology of the orbifold $X/\sigma$ is the equivariant cohomology of the free part.

*Proof.* A non-empty fixed set is a mod 2 homology sphere; a point is a homology sphere of dimension $0$; the empty fixed set is the free case, which is the first alternative. $\square$

### The Period and the Coefficients

**Remark.** The mod 2 theory is the case $p=2$ of the Smith theory, and for an odd period the sign appears: the transfer averages over the group with a coefficient $1/p$ and the parity of the dimension drop is even, and the correct coefficients are $\mathbb{F}_p$. The general statements for a periodic map of any period, for a $p$-group and for a finite group, with the transfer-theoretic proofs and the localization, are those of *Smith Theory and the Fixed Sets of Periodic Maps*; the present article is the case in which the coefficients are $\mathbb{F}_2$ and the group is $\mathbb{Z}/2$, where the theory is the module theory of $\mathbb{F}_2[x]$ developed above.

## The Edge Maps and the Transgression

### The Edge Homomorphisms

**Theorem.** In the Serre spectral sequence of the Borel fibration the edge homomorphisms of the base and of the fibre are the natural maps

$$
b : H^*(B\mathbb{Z}/2;\mathbb{F}_2) \to H_{\mathbb{Z}/2}^*(X) , \qquad f : H_{\mathbb{Z}/2}^*(X) \to H^*(X;\mathbb{F}_2) ,
$$

with $b$ the pullback along the projection and $f$ the restriction to the fibre. The base edge homomorphism is injective, because the differentials out of the base axis vanish (there is no column of negative fibre degree), so $\mathbb{F}_2[x] \to H_{\mathbb{Z}/2}^*(X)$ is injective and the equivariant cohomology is generated as an $\mathbb{F}_2[x]$-module by the image of the fibre; the fibre edge homomorphism is surjective, with kernel the ideal generated by $x$, and the fibre cohomology is the quotient of the equivariant cohomology by $x$.

*Proof.* The spectral sequence has $E_2^{p,q}=0$ for $q<0$, so $d_r^{p,0}=0$ for $r \geq 2$ and the base axis survives to $E_\infty$, giving the injectivity of the base edge; the fibre edge is the composite $H_{\mathbb{Z}/2}^*(X)\to E_\infty^{0,*}\hookrightarrow E_2^{0,*}=H^*(X)$, and its kernel is the image of the multiplication by $x$ by the module structure. $\square$

### The Transgression and the Collapse

**Theorem.** The only differential of the spectral sequence relevant to the collapse is the transgression, and the sequence collapses at $E_2$ when the involution acts trivially on the mod 2 cohomology of $X$, in which case

$$
H_{\mathbb{Z}/2}^*(X;\mathbb{F}_2) \cong \mathbb{F}_2[x]\otimes_{\mathbb{F}_2}H^*(X;\mathbb{F}_2)
$$

and the module is free; in general the differentials are $\mathbb{F}_2[x]$-linear and their non-vanishing measures the failure of the module to be free.

*Proof.* The collapse criterion is the triviality of the action on the fibre cohomology, $\sigma^*=\mathrm{id}$ on $H^*(X;\mathbb{F}_2)$, together with the vanishing of the transgression; the $E_2$ page has the tensor product form, and when the action is cohomologically trivial all the differentials vanish, giving the stated isomorphism. $\square$

## The Comparison with the Orbit Space

**Theorem.** The homotopy quotient and the orbit space are related by the comparison map $\pi_G : X_{\mathbb{Z}/2}\to X/\sigma$ induced by the projection $EG\to\mathrm{pt}$; it is a homotopy equivalence for the free involution, so that the equivariant cohomology is the cohomology of the orbit space, and away from freeness the comparison fails to be an equivalence by an amount measured by the fixed set through the localisation theorem. The cohomology of the orbit space is computed from the invariants of the mod 2 cohomology by the theory of *The Cohomology of an Orbit Space*, and the whole mod 2 package of this article is the specialisation of the equivariant theory to the group of order two.

*Proof.* The comparison map and the identification in the free case are those of *The Cohomology of an Orbit Space*; the fixed-set contribution is the localisation theorem of the previous section. $\square$

## Examples

**Example (the point and the classifying space).** For $X=\mathrm{pt}$ with the trivial involution the homotopy quotient is $B\mathbb{Z}/2=\mathbb{RP}^{\infty}$, so $H_{\mathbb{Z}/2}^*(\mathrm{pt};\mathbb{F}_2)=\mathbb{F}_2[x]$, the free module of rank one, consistent with the fixed set being the point and the localisation giving $\mathbb{F}_2[x^{\pm1}]$; the Borel fibration degenerates, and the example is the universal case in which the equivariant cohomology is the cohomology of the group alone.

**Example (the spheres).** For the antipodal involution of $S^n$ the fixed set is empty, the Borel fibration is the sphere bundle $S^n\to\mathbb{RP}^n\to\mathbb{RP}^{\infty}$, and $H_{\mathbb{Z}/2}^*(S^n)\cong H^*(\mathbb{RP}^n;\mathbb{F}_2) = \mathbb{F}_2[x]/(x^{n+1})$, a cyclic torsion module over $\mathbb{F}_2[x]$; the module has rank zero, consistent with the empty fixed set, and the torsion is the whole module.

**Example (the reflection).** For the reflection of $S^n$ fixing $S^{n-1}$ the fixed set has total mod 2 dimension two, the module $H_{\mathbb{Z}/2}^*(S^n)$ has rank two, and the localization identifies the generic part with $\mathbb{F}_2[x^{\pm1}]\oplus x^{n-1}\mathbb{F}_2[x^{\pm1}]$, the two generators being the classes of the fixed sphere and of the free complement; the Smith inequality is an equality.

**Remark (the rank with several components).** When the fixed set has several connected components the rank of the equivariant cohomology over $\mathbb{F}_2[x]$ is the sum of the total mod 2 Betti numbers of the components, so the rank detects each component separately; the localisation is componentwise, and each component contributes its own free summand to the localised module, consistent with the rank formula of the localisation theorem.

**Example (the tori and the projective spaces).** The involution of the $n$-torus inverting one circle has fixed set the remaining $(n-1)$-torus, and the mod 2 Smith inequality is an equality on the total dimensions; the involution of $\mathbb{CP}^n$ given by conjugation has fixed set $\mathbb{RP}^n$, and again the total mod 2 dimensions agree, so the fixed set is as large as the inequality allows. In both cases the localization theorem computes the generic part of the equivariant cohomology from the fixed set, and the torsion is the contribution of the non-free cells.

**Remark (the finite generation).** For a finite complex the module $H_{\mathbb{Z}/2}^*(X)$ is finitely generated over the Noetherian ring $\mathbb{F}_2[x]$, so it splits into a free part of the rank of the fixed set and a torsion part; the torsion is annihilated by a power of $x$, and for a free action the exponent is bounded by the dimension.

**Remark (the odd primes and the difference).** For an odd prime $p$ the theory differs in two ways: the coefficients are $\mathbb{F}_p$ and the module is over $H^*(B\mathbb{Z}/p;\mathbb{F}_p)=\mathbb{F}_p[x]\otimes\Lambda(y)$ with an exterior generator $y$ in odd degree, and the norm is the sum over the group of order $p$ with the alternating signs of the roots of unity. The rank formula and the localisation hold with the Euler class $x$ and the parity condition, and the dimension drop has even parity; the odd-primary statements belong to *Smith Theory and the Fixed Sets of Periodic Maps*, and the present article is the case $p=2$, in which the exterior generator is absent and the algebra is the polynomial algebra in one variable.

**Remark (the comparison with the equivariant K-theory).** The module structure and the localisation have exact analogues in the equivariant K-theory of *Equivariant K-Theory*: the equivariant K-theory is a module over the representation ring, the restriction to the fixed set localises, and the rank is the rank of the fixed-point data. The mod 2 statement of this article is the cohomological form of that localisation, with the polynomial ring $\mathbb{F}_2[x]$ in place of the representation ring and the $x$-torsion in place of the representation-theoretic torsion. The two theories are the extremes of a single family: the equivariant cohomology is the graded-algebraic member, with the module structure over $\mathbb{F}_2[x]$, and the equivariant K-theory is the representation-theoretic member, with the module structure over $R(G)$, and in both the fixed set controls the generic part by the same localisation.

## Summary

For a space with an involution and coefficients in $\mathbb{F}_2$, the equivariant cohomology is the cohomology of the homotopy quotient $X_{\mathbb{Z}/2} = X\times_{\mathbb{Z}/2}E\mathbb{Z}/2$, it is an $\mathbb{F}_2[x]$-algebra with $|x|=1$ through the projection to $B\mathbb{Z}/2 = \mathbb{RP}^{\infty}$, and it is computed by the Serre spectral sequence $E_2 = \mathbb{F}_2[x]\otimes H^*(X;\mathbb{F}_2)$ with $\mathbb{F}_2[x]$-linear differentials; a free involution collapses the sequence and gives $H_{\mathbb{Z}/2}^*(X)\cong H^*(X/\sigma)$. The fixed set $F = X^{\sigma}$ controls the module: after inverting $x$ the restriction to $F$ is an isomorphism, so the rank of the equivariant cohomology over $\mathbb{F}_2[x]$ is the total mod 2 dimension of the fixed set, and the rest is $x$-torsion carried by the free part of the action. The Smith inequality bounds the total mod 2 Betti number of the fixed set by that of the space, and the Smith theorem makes the fixed set of an involution of a mod 2 homology $n$-sphere a mod 2 homology sphere of dimension at most $n$; the parity restriction on the dimension drop is a phenomenon of the odd primes and belongs to the general theory of *Smith Theory and the Fixed Sets of Periodic Maps*. The transfer, its compatibility and the induced map on the fixed set are the subject of *The Transfer and the Involution*. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X,\sigma)$ | Space with an involution $\sigma$ |
| $F = X^{\sigma}$ | Fixed set of the involution |
| $\mathbb{F}_2$ | Coefficient field $\mathbb{Z}/2$ |
| $X_{\mathbb{Z}/2} = X\times_{\mathbb{Z}/2}E\mathbb{Z}/2$ | Homotopy quotient of the involution |
| $H_{\mathbb{Z}/2}^*(X) = H^*(X_{\mathbb{Z}/2})$ | Equivariant cohomology |
| $p : X_{\mathbb{Z}/2}\to\mathbb{RP}^{\infty}$ | Borel fibration; fibre $X$ |
| $x \in H^1(B\mathbb{Z}/2;\mathbb{F}_2)$ | Generator; $\mathbb{F}_2[x] = H^*(B\mathbb{Z}/2;\mathbb{F}_2)$ |
| $E_2^{p,q} = \mathbb{F}_2[x]\otimes H^q(X;\mathbb{F}_2)$ | Serre spectral sequence of the Borel fibration |
| $x^{-1}H_{\mathbb{Z}/2}^*(X)\cong H^*(F)\otimes\mathbb{F}_2[x^{\pm1}]$ | Localization theorem |
| rank of the module $= \dim H^*(F)$ | The fixed set is the generic rank |
| $\sum\dim H_i(F)\le\sum\dim H_i(X)$ | Smith inequality, mod 2 |
| $F$ a mod 2 homology sphere, $\dim F\le n$ | Smith theorem for an involution of a homology sphere |

## Further Reading

- Paul A. Smith, "Transformations of finite period", *Annals of Mathematics* 39 (1938), 127–164, and the continuation papers, for the mod 2 Smith theory and the fixed-set theorems.
- Armand Borel, *Seminar on Transformation Groups* (Annals of Mathematics Studies 46, 1960), for the homotopy quotient, the localization theorem and the module structure.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the equivariant cohomology of an involution and the Smith theory.
- Wu-yi Hsiang, *Cohomology Theory of Topological Transformation Groups* (Springer, 1975), for the localization and the computations of the fixed-set cohomology.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the cohomology of $\mathbb{RP}^n$ and $\mathbb{RP}^{\infty}$ with $\mathbb{F}_2$ coefficients.
- John McCleary, *A User's Guide to Spectral Sequences* (Cambridge University Press, 2nd ed. 2001), for the Serre spectral sequence of a fibration and its $\mathbb{F}_2[x]$-linear differentials.
