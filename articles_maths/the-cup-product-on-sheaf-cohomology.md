
# __The Cup Product on Sheaf Cohomology__

## Introduction

The cohomology of a sheaf is a graded abelian group, and when the coefficients carry a multiplication, the cohomology carries one too: the **cup product** pairs a class of degree $p$ with a class of degree $q$ to give a class of degree $p+q$, and when the coefficient sheaf is a sheaf of commutative rings the direct sum $H^*(X,\mathcal{R})=\bigoplus_iH^i(X,\mathcal{R})$ becomes a graded ring. The product is the sheaf-theoretic form of the cup product of singular cohomology: for the constant sheaf it agrees with the singular product of *Cup and Cap Products*, so that the cohomology ring of a space may be computed from the sheaves alone. The product is the operation that makes the cohomology of a space a finer invariant than its graded group, and it is the operation through which the cohomology ring of a variety, of a manifold and of a classifying space is expressed.

This article constructs the cup product for sheaves of modules over a ringed space, proves its formal properties — associativity, graded commutativity with the Koszul sign, unity, naturality and the Leibniz rule for the coboundary — and develops the Čech model of the product, which is the one used for the computations. It then specialises to a sheaf of commutative rings, obtaining the cohomology ring, and computes the basic examples. The general homological algebra of the tensor product of complexes, of the derived tensor product and of the Eilenberg–Zilber comparison is Part I's, in *Ext and Tor*, *Homological Algebra* and *Derived Categories*, and it is cited; the sheaf-theoretic construction is what is developed.

The notation for sheaves, for the tensor product $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$, for the stalks and for the derived functors is that of *Presheaves and Sheaves* and *Sheaf Cohomology*; the Čech complex and the limit over refinements are those of *Čech Cohomology*, and the sign convention is the one fixed in *Cup and Cap Products*. The article precedes *Equivariant Sheaves and Descent* and the rest of the involution layer of the category, and it is used by them for the ring structure on the cohomology of an equivariant sheaf. Nothing analytic and nothing geometric is used: the tensor product of sheaves is an algebraic operation on the coefficient sheaves, and no form, no norm and no derivative occurs. Throughout, $(X,\mathcal{O}_X)$ is a ringed space, $\mathcal{F},\mathcal{G},\mathcal{H}$ are sheaves of $\mathcal{O}_X$-modules, $R$ denotes a coefficient ring when the sheaves are constant, and the Koszul sign $(-1)^{|\alpha||\beta|}$ is written for classes of degrees $|\alpha|=p$ and $|\beta|=q$.

## The Tensor Product of Sheaves

**Definition.** The **tensor product** of the sheaves of $\mathcal{O}_X$-modules $\mathcal{F}$ and $\mathcal{G}$ is the sheaf $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$ obtained by sheafifying the presheaf $U\mapsto\mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$; it is characterised by the bilinear universal property, and it is commutative, associative and unital, with unit $\mathcal{O}_X$.

**Proposition (stalks and exactness).** $(\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G})_x=\mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\mathcal{G}_x$ for every $x$; the tensor product is right exact in each variable, and it is exact in $\mathcal{G}$ when $\mathcal{F}$ is flat, in particular when $\mathcal{F}$ is locally free of finite rank or $\mathcal{F}=\mathcal{O}_X$.

*Proof.* The stalk formula is the commutation of the sheafification with the passage to the stalk and the exactness of the tensor product of modules over a local ring with the localisation; the right exactness is the right exactness of the tensor product of modules, and the left exactness for flat coefficients is the definition of flatness, with locally free sheaves flat over the structure sheaf.

**Definition.** A sheaf $\mathcal{F}$ is **flat** if $\mathcal{F}\otimes_{\mathcal{O}_X}-$ is exact; $\mathcal{O}_X$ and every locally free sheaf are flat, and the constant sheaf $\underline{R}$ is flat for $R$ a field.

## The Cup Product

**Theorem (the cup product).** Let $\mathcal{F}$ and $\mathcal{G}$ be sheaves of $\mathcal{O}_X$-modules, and suppose that $\mathcal{F}$ is flat, or more generally that the higher tensor sheaves $\operatorname{Tor}_i^{\mathcal{O}_X}(\mathcal{F},\mathcal{G})$ vanish for $i>0$. Then there is a natural bilinear product

$$
\smile\ :\ H^p(X,\mathcal{F})\times H^q(X,\mathcal{G})\longrightarrow H^{p+q}(X,\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}),\qquad (\alpha,\beta)\mapsto\alpha\smile\beta,
$$

for all $p,q\geq0$. Without the flatness hypothesis, the product is defined into the hypercohomology of the derived tensor product, $\smile:H^p(X,\mathcal{F})\times H^q(X,\mathcal{G})\to\mathbb{H}^{p+q}(X,\mathcal{F}\otimes_{\mathcal{O}_X}^{\mathbf{L}}\mathcal{G})$; the two agree when the Tor sheaves vanish.

*Proof (construction).* Choose flabby resolutions $\mathcal{F}\to\mathcal{A}^\bullet$ and $\mathcal{G}\to\mathcal{B}^\bullet$, which exist by *Sheaf Cohomology*. The tensor product of the two complexes is a complex of sheaves with the differential $D(a\otimes b)=da\otimes b+(-1)^{|a|}a\otimes db$, and flabby sheaves being a tensor ideal and acyclic for the tensor product, this complex represents the derived tensor product $\mathcal{F}\otimes^{\mathbf{L}}\mathcal{G}$; it is a resolution of $\mathcal{F}\otimes\mathcal{G}$ exactly when the Tor sheaves vanish, in particular when $\mathcal{F}$ is flat. The tensor product of a cocycle in $\mathcal{A}^p$ with a cocycle in $\mathcal{B}^q$ is a cocycle in $(\mathcal{A}^\bullet\otimes\mathcal{B}^\bullet)^{p+q}$ by the Leibniz rule below, and a coboundary in either factor gives a coboundary in the total complex; passing to cohomology gives the product. The construction is the sheaf-theoretic case of the Eilenberg–Zilber comparison of *Cup and Cap Products* and of the derived tensor product of *Derived Categories*.

**Theorem (properties).** For classes $\alpha,\alpha'\in H^p(X,\mathcal{F})$, $\beta,\beta'\in H^q(X,\mathcal{G})$, $\gamma\in H^r(X,\mathcal{H})$:

1. **Bilinearity**: $(\alpha+\alpha')\smile\beta=\alpha\smile\beta+\alpha'\smile\beta$, and similarly in the second variable.
2. **Associativity**: $(\alpha\smile\beta)\smile\gamma=\alpha\smile(\beta\smile\gamma)$ under the associativity isomorphism of the tensor product.
3. **Graded commutativity**: $\alpha\smile\beta=(-1)^{pq}(\beta\smile\alpha)$ under the symmetry isomorphism $\mathcal{F}\otimes\mathcal{G}\cong\mathcal{G}\otimes\mathcal{F}$, with the Koszul sign $(-1)^{pq}$ of *Cup and Cap Products*.
4. **Unity**: if $\mathcal{F}=\mathcal{G}=\mathcal{O}_X$, the class $1\in H^0(X,\mathcal{O}_X)$ of the identity section satisfies $1\smile\beta=\beta$.
5. **Naturality**: for a continuous map $f:Y\to X$, $f^*(\alpha\smile\beta)=f^*\alpha\smile f^*\beta$ in $H^{p+q}(Y,f^{-1}\mathcal{F}\otimes f^{-1}\mathcal{G})$.

*Proof.* Each statement is checked on cocycle representatives in the resolutions and then passed to cohomology. Bilinearity is the bilinearity of the tensor product. Associativity is the associativity of the tensor product of complexes, up to the canonical comparison. Graded commutativity is the symmetry of the tensor product combined with the sign produced by moving a degree-$q$ element past a degree-$p$ element in the total complex; the sign is the Koszul sign. Unity is the fact that the identity section is a cocycle in degree zero and the tensor product with it is the identity of the coefficient. Naturality is the exactness of $f^{-1}$ and its commutation with the tensor product.

**Proposition (the Leibniz rule).** If $(\mathcal{A}^\bullet,d)$ and $(\mathcal{B}^\bullet,e)$ are complexes of sheaves, the differential of the total complex of $\mathcal{A}^\bullet\otimes\mathcal{B}^\bullet$ is

$$
D(a\otimes b)=da\otimes b+(-1)^{|a|}a\otimes eb,
$$

so that $D^2=0$ and $D$ is a graded derivation; on the global sections it is the coboundary of *The Coboundary Operator*. The sign $(-1)^{|a|}$ is the same sign that appears in the shift of a complex and in the Koszul sign of graded commutativity.

*Proof.* $D^2(a\otimes b)=d^2a\otimes b+(-1)^{|a|}da\otimes eb+(-1)^{|a|+1}da\otimes eb+(-1)^{2|a|}a\otimes e^2b=0$, the two middle terms cancelling; the derivation property is the definition of $D$ and the bilinearity of the tensor product.

## The Čech Cup Product

**Definition.** For an open cover $\mathcal{U}$ of $X$ the **Čech cup product** pairs cochains by

$$
(\alpha\smile\beta)_{i_0\ldots i_{p+q}}=\alpha_{i_0\ldots i_p}\otimes\beta_{i_p\ldots i_{p+q}},
$$

the two factors sharing the index $i_p$; with the alternating convention of *Čech Cohomology* this is a cochain map and induces

$$
\check H^p(\mathcal{U},\mathcal{F})\times\check H^q(\mathcal{U},\mathcal{G})\longrightarrow\check H^{p+q}(\mathcal{U},\mathcal{F}\otimes\mathcal{G}),
$$

and passing to the limit over the refinements gives the product $\check H^p(X,\mathcal{F})\times\check H^q(X,\mathcal{G})\to\check H^{p+q}(X,\mathcal{F}\otimes\mathcal{G})$. The formula is the sheaf-theoretic case of the front-face/back-face formula of *Cup and Cap Products*, with the shared index playing the role of the shared vertex.

**Theorem (the Čech product and sheaf cohomology).** For $X$ paracompact, Godement's theorem identifies the limit Čech cohomology with the sheaf cohomology in all degrees, and under this identification the Čech cup product agrees with the cup product of the previous section. Hence for a paracompact space the cup product is computed on the Čech complex of any cover, and on a good cover — one whose nonempty finite intersections are contractible, as in *Čech Cohomology* — the Čech complex computes the product exactly.

*Proof.* The agreement of the products is the compatibility of the two constructions of the product from the two resolutions; the Godement identification is quoted in *Čech Cohomology* as a standing weakness, and the remaining statements are the definitions. For a good cover the nerve theorem of *Čech Cohomology* identifies the Čech complex with the simplicial cochain complex of the nerve, and the product becomes the simplicial cup product.

**Proposition (comparison with the singular product).** Let $X$ be paracompact and locally contractible and let $R$ be a commutative ring. Under the comparison isomorphism $H^*(X,\underline{R})\cong H^*(X;R)$ of *Sheaf Cohomology*, the cup product on the sheaf cohomology of the constant sheaf corresponds to the singular cup product of *Cup and Cap Products*;

$$
H^*(X,\underline{R})\cong H^*(X;R)\quad\text{as graded rings.}
$$

*Proof.* The comparison theorem identifies the sheafified singular cochain complex with a flabby resolution of $\underline{R}$ and compares the multiplication on the cochains, which is the front-face/back-face product on both sides; the signs and the unit agree.

## The Cohomology Ring

**Theorem (the cohomology ring).** Let $\mathcal{R}$ be a sheaf of commutative $\mathcal{O}_X$-algebras that is flat over $\mathcal{O}_X$, with multiplication $\mu:\mathcal{R}\otimes_{\mathcal{O}_X}\mathcal{R}\to\mathcal{R}$. Composing the cup product with $\mu$ gives a product

$$
H^p(X,\mathcal{R})\times H^q(X,\mathcal{R})\longrightarrow H^{p+q}(X,\mathcal{R}),\qquad (\alpha,\beta)\mapsto\alpha\smile\beta,
$$

under which $H^*(X,\mathcal{R})=\bigoplus_iH^i(X,\mathcal{R})$ is a graded commutative unital ring, with unit the class $1\in H^0(X,\mathcal{R})$ of the identity section. For $\mathcal{R}=\mathcal{O}_X$ this is the **cohomology ring of the structure sheaf**, and for $\mathcal{R}=\underline{R}$ the constant sheaf it is the **cohomology ring of the space** with coefficients in $R$.

*Proof.* The product of the theorem on the cup product is followed by the map induced by $\mu$ on cohomology, which exists because $\mathcal{R}$ is flat; the ring axioms are those of the cup product transported by $\mu$, and the graded commutativity is the Koszul sign together with the commutativity of $\mu$ and the symmetry of the tensor product.

**Proposition (functoriality of the ring).** For a continuous map $f:Y\to X$ the pullback restricts to a morphism of graded rings $f^*:H^*(X,\mathcal{R})\to H^*(Y,f^{-1}\mathcal{R})$, and for an open immersion $j:U\hookrightarrow X$ the restriction $j^*$ is a morphism of graded rings; the extension by zero is a functor of coefficient sheaves and does not preserve the ring structure unless it is a morphism of sheaves of rings.

*Proof.* The pullback is multiplicative by the naturality of the cup product, and it preserves the unit; the restriction is the case $f=j$. The last statement is the definition of a morphism of sheaves of rings.

**Remark (the non-flat case).** For a sheaf of rings $\mathcal{R}$ not flat over $\mathcal{O}_X$ the product with itself involves the derived tensor product; the ring structure is then defined on the hypercohomology of a dg-resolution of $\mathcal{R}$, or on $H^*(X,\mathcal{R})$ only after the Tor sheaves have been shown to vanish. The classical cases $\mathcal{R}=\mathcal{O}_X$, $\mathcal{R}=\underline{R}$ for $R$ a field, and $\mathcal{R}$ locally free as an $\mathcal{O}_X$-module are all flat.

## Computations

### The Sphere

For $X=S^n$ with $n\geq1$ and coefficients $\mathbb{Z}$, the cohomology is $\mathbb{Z}$ in degrees $0$ and $n$ and zero otherwise, so that the ring is

$$
H^*(S^n,\underline{\mathbb{Z}})\cong\mathbb{Z}[x]/(x^2),\qquad |x|=n,
$$

the generator $x$ of degree $n$; the square vanishes because there is no cohomology in degree $2n$. For $n$ even the square could only be a multiple of $x$, and the constraint of degree forces the choice $x^2=0$ anyway; the computation agrees with the singular ring of *Cup and Cap Products*.

### The Torus

For the torus $T^n=(S^1)^n$ the cohomology ring with coefficients $\mathbb{Z}$ is the exterior algebra on $n$ generators of degree one,

$$
H^*(T^n,\underline{\mathbb{Z}})\cong\Lambda(x_1,\ldots,x_n),\qquad |x_i|=1,\qquad x_ix_j=-x_jx_i,
$$

a graded-commutative ring with Hilbert series $(1+t)^n$; the Koszul sign makes the square of every generator vanish, consistent with the structure theorem for exterior algebras of odd generators.

### The Projective Space

For the complex projective space $\mathbb{CP}^n$ the cohomology ring with coefficients $\mathbb{Z}$ is the truncated polynomial ring

$$
H^*(\mathbb{CP}^n,\underline{\mathbb{Z}})\cong\mathbb{Z}[x]/(x^{n+1}),\qquad |x|=2,
$$

so that the ring detects the dimension and distinguishes the projective spaces from the odd spheres. The cohomology of the structure sheaf is concentrated in degree zero, $H^0(\mathbb{CP}^n,\mathcal{O})=\mathbb{C}$ and $H^i(\mathbb{CP}^n,\mathcal{O})=0$ for $i>0$, by the vanishing theorem of *Sheaves in Algebraic Geometry*; the ring $H^*(\mathbb{CP}^n,\mathcal{O})$ is therefore the field $\mathbb{C}$ concentrated in degree zero, in agreement with the general fact that the higher cohomology of the structure sheaf of a projective space vanishes, and the interesting ring is the one with the constant coefficients.

## Summary

The tensor product of sheaves is the sheafification of the sectionwise tensor product, with stalks the tensor products of the stalks and with the exactness properties of the tensor product of modules; the sheaves that are flat include the structure sheaf, the locally free sheaves and the constant sheaves over a field. The cup product pairs a class in $H^p(X,\mathcal{F})$ with one in $H^q(X,\mathcal{G})$ to give a class in $H^{p+q}(X,\mathcal{F}\otimes\mathcal{G})$ whenever the Tor sheaves vanish, and in general it takes values in the hypercohomology of the derived tensor product; it is constructed from flabby resolutions of the coefficients by multiplying cocycles in the total complex, and on the Čech complex it is the front-face/back-face product with the shared index, which Godement's theorem identifies with the sheaf product for paracompact spaces and which agrees with the singular cup product under the comparison theorem.

The product is bilinear, associative, unital and graded-commutative, with the Koszul sign of *Cup and Cap Products*, and natural for pullbacks; its differential is the graded Leibniz rule $D(a\otimes b)=da\otimes b+(-1)^{|a|}a\otimes db$ on the total complex of two complexes of sheaves, the sign being that of *The Coboundary Operator*. For a flat sheaf of commutative rings the product followed by the multiplication makes the cohomology a graded commutative ring, the cohomology ring of the structure sheaf or of the space; it is computed by the Čech complex of a good cover, and its basic values are the truncated polynomial rings of the spheres and the projective spaces and the exterior algebras of the tori.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$ | tensor product of sheaves; stalks $(\mathcal{F}\otimes\mathcal{G})_x=\mathcal{F}_x\otimes\mathcal{G}_x$ |
| flat sheaf | $\mathcal{F}\otimes_{\mathcal{O}_X}-$ exact; includes $\mathcal{O}_X$, locally free, constants over a field |
| $\alpha\smile\beta$ | cup product; $H^p(X,\mathcal{F})\times H^q(X,\mathcal{G})\to H^{p+q}(X,\mathcal{F}\otimes\mathcal{G})$ |
| $(-1)^{pq}$ | Koszul sign of graded commutativity, $p=|\alpha|$, $q=|\beta|$ |
| $\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$ | graded commutativity under the symmetry of the tensor product |
| $(\alpha\smile\beta)_{i_0\ldots i_{p+q}}=\alpha_{i_0\ldots i_p}\otimes\beta_{i_p\ldots i_{p+q}}$ | Čech cup product, shared index $i_p$ |
| $D(a\otimes b)=da\otimes b+(-1)^{\lvert a\rvert}a\otimes eb$ | differential of the total complex of two complexes; Leibniz rule |
| $H^*(X,\mathcal{R})=\bigoplus_iH^i(X,\mathcal{R})$ | cohomology ring of a flat sheaf of commutative rings |
| $\mathcal{F}\otimes^{\mathbf{L}}_{\mathcal{O}_X}\mathcal{G}$ | derived tensor product; values of the general cup product |
| $H^*(X,\underline{R})\cong H^*(X;R)$ | ring isomorphism with singular cohomology for a nice space |

## Further Reading

- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the derived tensor product and the spectral sequences of a composite of functors.
- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for the construction of the cup product from flabby resolutions and the identification with the Čech product.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the cup product on sheaf cohomology, its properties and the comparison with the singular product.
- Birger Iversen, *Cohomology of Sheaves* (Springer, 1986), for the cup product in the derived category and the projection formula.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the singular cup product and the ring computations of the spheres, the tori and the projective spaces, transported to the sheaf setting here.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the Eilenberg–Zilber comparison and the tensor product of complexes.
- Masaki Kashiwara and Pierre Schapira, *Sheaves on Manifolds* (Springer, 1990), for the monoidal structure of the derived category of sheaves and the induced products.
