
# __The Involution on the Coboundary__

## Introduction

The coboundary operator $\delta$ of a complex of sheaves satisfies $\delta^2=0$, and an **involution on the coboundary** is an endomorphism $\theta$ of the complex of order two that intertwines $\delta$ with itself up to a sign,

$$
\theta\,\delta=\varepsilon\,\delta\,\theta,\qquad \varepsilon=\pm1,
$$

with $\theta^2=\mathrm{id}$. The two cases are the **commuting** one, $\varepsilon=+1$, in which $\theta$ is an involution of the complex as a cochain complex and acts on the cohomology by an involution of *Cohomology with an Involution*, and the **anticommuting** one, $\varepsilon=-1$, in which $\theta$ still carries cocycles to cocycles and induces an involution of the cohomology, but with the sign entering the products. The involution on the coboundary is the operator that produces the involution on the cohomology: the element-level involution of *Cohomology with an Involution* is the shadow of the operator-level involution of the complex, and the two are related by the rule that a cochain involution induces the involution it does, never by assumption. The typical example is the involution induced by an involution of a cover or of a group acting on the complex, where the sign comes from the permutation of the indices in the alternating convention of the Čech coboundary.

This article develops the involutions of a complex of sheaves, the commuting and the anticommuting cases, the fixed and anti-invariant subcomplexes, the induced involution on the cohomology and on the pages of a spectral sequence, and the sign that the Čech coboundary and the cup product impose. It is the first article of the `- * Operator Theory` group of the category, in which the operators built from the involution are studied; the elements and the involution on them are the previous group, the coboundary operator itself is *The Coboundary Operator*, the cup product is *The Cup Product on Sheaf Cohomology*, the spectral sequences are *Spectral Sequences*, and the adjoints are *Hermitian Pairings of Sheaves* and *Self-Adjoint Operators on Sheaves*.

The article uses no analysis and no geometry: the complexes are complexes of sheaves of modules, the coboundary is the Čech or the resolution coboundary, and no form, no norm and no derivative occurs. Throughout, $(\mathcal{C}^{\bullet},d)$ is a complex of sheaves on $X$ (the Čech complex of a cover or the complex of a resolution), $\theta$ is an involution of the complex, $\varepsilon=\pm1$ is the sign of the intertwining, $H^{\bullet}(\mathcal{C}^{\bullet})$ is the cohomology, and the alternating convention for the Čech cochains and the cup product is the one fixed in *Čech Cohomology* and *The Cup Product on Sheaf Cohomology*.

## The Coboundary Operator

**Definition.** A **complex of sheaves** is a sequence of sheaves and morphisms

$$
\cdots\longrightarrow\mathcal{C}^{p-1}\xrightarrow{\ d\ }\mathcal{C}^{p}\xrightarrow{\ d\ }\mathcal{C}^{p+1}\longrightarrow\cdots,\qquad d^2=0,
$$

and its **coboundary operator** is $d$; for the Čech complex of a cover it is the alternating sum of the restriction maps, as in *The Coboundary Operator* and *Čech Cohomology*, and for a resolution of a sheaf it is the differential of the resolution.

**Definition.** A **morphism of complexes** $\psi:(\mathcal{C}^{\bullet},d)\to(\mathcal{D}^{\bullet},e)$ is a family of morphisms $\psi^p:\mathcal{C}^p\to\mathcal{D}^p$ with $\psi\circ d=e\circ\psi$; two morphisms are **homotopic** if they differ by $h d+d h$ for a family $h$ of degree $-1$, and homotopic morphisms induce the same map on cohomology.

**Proposition (the cohomology).** The cohomology $H^p(\mathcal{C}^{\bullet})=\ker(d:\mathcal{C}^p\to\mathcal{C}^{p+1})/\operatorname{im}(d:\mathcal{C}^{p-1}\to\mathcal{C}^p)$ is well defined, and a morphism of complexes induces a morphism on the cohomology that depends only on its homotopy class.

## Involutions of a Complex

**Definition.** An **involution of a complex** $(\mathcal{C}^{\bullet},d)$ is an endomorphism $\theta$ of degree zero with $\theta^2=\mathrm{id}$ and $\theta\,d=\varepsilon\,d\,\theta$ for a sign $\varepsilon=\pm1$; for $\varepsilon=+1$ the involution is **commuting** and is an involution of the complex as a cochain complex, and for $\varepsilon=-1$ it is **anticommuting**. The **fixed subcomplex** is the image of the idempotent $\frac12(\mathrm{id}+\theta)$ when $2$ is invertible, and the **anti-invariant subcomplex** the image of $\frac12(\mathrm{id}-\theta)$.

**Proposition (the subcomplexes).** If $2$ is invertible and $\theta$ is a commuting involution, then $\mathcal{C}^{\bullet}=\mathcal{C}^{\bullet}_+\oplus\mathcal{C}^{\bullet}_-$ is a decomposition into subcomplexes, the fixed and the anti-invariant ones; in the anticommuting case the two idempotents are not morphisms of complexes, and the decomposition is only a decomposition of the underlying graded sheaves.

*Proof.* The kernels of $\theta-\mathrm{id}$ and $\theta+\mathrm{id}$ are the images of the two idempotents when $2^{-1}$ exists; in the commuting case each is stable under $d$ because $d$ commutes with $\theta$, while in the anticommuting case $d$ exchanges the two because $d\theta=-\theta d$, so neither is a subcomplex.

**Theorem (the induced involution).** Let $\theta$ be an involution of the complex $(\mathcal{C}^{\bullet},d)$, commuting or anticommuting. Then $\theta$ carries cocycles to cocycles and coboundaries to coboundaries, so it induces an endomorphism

$$
\theta^*:H^p(\mathcal{C}^{\bullet})\longrightarrow H^p(\mathcal{C}^{\bullet}),\qquad (\theta^*)^2=\mathrm{id},
$$

an involution of the cohomology in the sense of *Cohomology with an Involution*; in the commuting case $\theta^*$ is induced by an involution of the complex as a cochain complex, and in the anticommuting case it is induced by $\theta$ after the sign is absorbed.

*Proof.* If $dx=0$ then $d(\theta x)=\varepsilon\theta(dx)=0$, and if $y=dz$ then $\theta y=\varepsilon\,d(\theta z)$; hence $\theta$ preserves both the cocycles and the coboundaries and descends to the cohomology. The square is the identity because $\theta^2=\mathrm{id}$, and the induced map is independent of the choices because a homotopy between two representatives is carried to a homotopy.

**Proposition (the sign and the products).** If the complex carries a product for which $d$ is a graded derivation, $d(x\cdot y)=dx\cdot y+(-1)^{|x|}x\cdot dy$, and if $\theta$ is a commuting ring involution, then $\theta^*$ is a ring involution of the cohomology; if $\theta$ is anticommuting and the product is the cup product, then $\theta^*$ is a ring involution twisted by the sign $(-1)^{|x|}$ in the sense that $\theta^*(x\cdot y)=(-1)^{|x||y|}\theta^*x\cdot\theta^*y$ only when $\varepsilon=+1$, and the anticommuting case requires the Koszul sign.

*Proof.* The Leibniz rule and the multiplicativity of $\theta$ give the multiplicativity of $\theta^*$ in the commuting case; in the anticommuting case the sign produced by moving $\theta$ past $d$ is the Koszul sign of *The Cup Product on Sheaf Cohomology*, and the two signs must be combined consistently, which is why the commuting case is the natural one for a ring involution.

## The Involution of the Čech Coboundary

**Theorem (an involution of a cover).** Let $\theta$ be an involution of the index set of a cover $\mathcal{U}=\{U_i\}$, permuting the opens with $\theta(U_i)=U_{\theta(i)}$ and $\theta^2=\mathrm{id}$, compatible with the inclusion of the overlaps. Then $\theta$ induces an endomorphism of the Čech complex by

$$
(\theta\alpha)_{i_0\ldots i_p}=(-1)^{\operatorname{sgn}(\theta,i_0,\ldots,i_p)}\,\theta\bigl(\alpha_{\theta(i_0)\ldots\theta(i_p)}\bigr),
$$

and it satisfies $\theta\,\delta=\operatorname{sgn}(\theta)\,\delta\,\theta$, where the sign is the product of the sign of the permutation of the indices and the sign of the involution on the coefficients; in particular the induced map on the Čech cohomology is an involution, and its fixed part is computed on the $\theta$-invariant cochains.

*Proof.* The Čech coboundary is a sum over the omission of one index; applying $\theta$ permutes the terms and produces the sign of the permutation that reorders the indices, and the alternating convention of *Čech Cohomology* accounts for the sign displayed. The square of $\theta$ on the cochains is the identity because $\theta^2=\mathrm{id}$ on the indices and on the coefficients; the induced map on the cohomology is an involution by the theorem on the induced involution.

**Example (the group action on the cover).** If a group $G$ acts on $X$ and $\mathcal{U}$ is a $G$-invariant cover, every $g\in G$ induces an endomorphism of the Čech complex as above, the cocycle condition of the action giving the compatibility; the equivariant cohomology of *Cohomology with an Involution* is computed on the invariant cochains, and the involution is the case of an element of order two.

## The Involution and the Spectral Sequence

**Theorem (the involution on a spectral sequence).** Let $(\mathcal{C}^{p,q},d',d'')$ be a double complex with an involution $\theta$ commuting (or anticommuting) with both differentials, of order two and bidegree zero. Then the spectral sequences of the double complex carry an involution on each page,

$$
\theta_r:E_r^{p,q}\longrightarrow E_r^{p,q},\qquad (\theta_r)^2=\mathrm{id},
$$

compatible with the differentials, $\theta_{r+1}\circ d_r=d_r\circ\theta_{r+1}$ on the derived page, and converging to the involution $\theta^*$ on the cohomology of the total complex; hence the fixed part of the abutment is computed from the fixed parts of the pages.

*Proof.* The involution of the double complex induces an involution of the associated single complex and of its filtration; the filtration is preserved, so the involution acts on the pages of the spectral sequence and commutes with the differentials by the functoriality of the construction of *Spectral Sequences*. The convergence is that of the double complex, and the identification of the limit involution with $\theta^*$ is the naturality of the edge maps.

**Corollary (the invariant cohomology from the pages).** If the spectral sequence degenerates and the pages are finite dimensional over a field of characteristic different from two, the fixed part of the abutment is the direct sum of the fixed parts of the pages, and the anti-invariant part is the direct sum of the anti-invariant parts; the Euler characteristics add.

*Proof.* The decomposition into fixed and anti-invariant parts is natural for the involution on each finite-dimensional vector space when $2$ is invertible, and the differentials preserve the decomposition, so the decomposition passes to the derived pages and to the limit.

## Worked Cases

### The Antipodal Involution of the Čech Complex

For the antipodal involution of the sphere and the cover by two open hemispheres exchanged by the involution, the Čech complex carries the index permutation of the previous theorem, and the induced involution on the Čech cohomology is the antipodal involution of *Cohomology with an Involution*; the fixed part is the cohomology of the projective space under the transfer hypotheses, recovered directly from the invariant cochains.

### The Trivial Involution of a Complex

For $\theta=\mathrm{id}$ the sign is $+1$, the fixed subcomplex is the whole complex, the anti-invariant subcomplex vanishes, and the induced involution on the cohomology is the identity. The case is the degenerate check and shows that the anticommuting case cannot be reduced to it by a change of the complex without changing the products.

### The Sign of the Koszul Convention

For a complex of graded sheaves with the Koszul sign in the differential of the total complex of a tensor product, the involution that exchanges the two factors of a tensor product is an anticommuting involution with $\varepsilon=-1$ when the factors are odd; the induced map on the cohomology is the symmetry of the cup product, $\alpha\smile\beta\mapsto(-1)^{pq}\beta\smile\alpha$, which is the graded commutativity of *The Cup Product on Sheaf Cohomology*. The example shows that the sign $\varepsilon$ is not a defect but the source of the Koszul sign.

## Summary

An involution of a complex of sheaves is an endomorphism $\theta$ of degree zero and order two with $\theta d=\varepsilon d\theta$ for a sign $\varepsilon=\pm1$; it is commuting for $\varepsilon=+1$ and anticommuting for $\varepsilon=-1$. A commuting involution splits the complex into the fixed and the anti-invariant subcomplexes when $2$ is invertible, and any involution of either kind preserves the cocycles and the coboundaries, so it induces an involution $\theta^*$ of the cohomology, of order two, which is the element-level involution of *Cohomology with an Involution*. In the commuting case the induced map is a ring involution for a product for which $d$ is a graded derivation; in the anticommuting case the Koszul sign enters, and the sign is exactly the graded commutativity of the cup product.

The Čech coboundary of a cover with an involution of its index set carries the induced involution with the sign of the permutation of the indices, the group actions on a cover being the typical case; a double complex with an involution carries an involution on each page of its spectral sequence, compatible with the differentials and converging to the involution on the cohomology, so that the fixed part of the abutment is computed from the fixed parts of the pages.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\mathcal{C}^{\bullet},d)$, $\delta$ | complex of sheaves and its coboundary; $d^2=0$ |
| $\theta$ | involution of the complex; $\theta^2=\mathrm{id}$, degree zero |
| $\theta\,d=\varepsilon\,d\,\theta$, $\varepsilon=\pm1$ | commuting ($+$) and anticommuting ($-$) involution |
| $\mathcal{C}^{\bullet}_+\oplus\mathcal{C}^{\bullet}_-$ | fixed and anti-invariant subcomplexes, for $\varepsilon=+1$ and $2$ invertible |
| $\theta^*:H^p(\mathcal{C}^{\bullet})\to H^p(\mathcal{C}^{\bullet})$ | induced involution on the cohomology; $(\theta^*)^2=\mathrm{id}$ |
| $(\theta\alpha)_{i_0\ldots i_p}=(-1)^{\operatorname{sgn}}\theta(\alpha_{\theta(i_0)\ldots\theta(i_p)})$ | induced involution on the Čech cochains |
| $\theta_r:E_r^{p,q}\to E_r^{p,q}$ | involution on the pages of a spectral sequence |
| $(-1)^{pq}$ | Koszul sign; the sign of the anticommuting case in the cup product |

## Further Reading

- John McCleary, *A User's Guide to Spectral Sequences* (Cambridge University Press, second edition, 2001), for the spectral sequences of a double complex and their functoriality.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the Čech complex, its coboundary and the actions of a group on it.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the sign conventions in the double complexes and the spectral sequences, cited for the algebraic conventions.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the spectral sequences and the functoriality.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the complexes, the homotopies and the induced maps on cohomology.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the sign conventions of the tensor product of complexes and the Koszul sign.
