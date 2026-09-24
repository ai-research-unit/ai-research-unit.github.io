
# __Cohomology and the Universal Coefficient Theorem__

## Introduction

Homology attaches to a space a graded module $H_n(X;R)$; **cohomology** attaches to it the graded module obtained by dualising the chain complex, and it carries two additional structures that homology does not have. The first is a *contravariant* functoriality: a continuous map $f: X \to Y$ induces $f^*: H^n(Y;G) \to H^n(X;G)$, in the opposite direction to $f$, which is what makes cohomology the natural receptacle for invariants pulled back from a target space — characteristic classes, obstructions, and the classes. The second is the **cup product**, which turns the direct sum of the cohomology modules into a graded ring; it is the subject of and is not used here.

The passage from homology to cohomology is not merely dualisation, and the difference is measured by the **universal coefficient theorem**. Dualising a chain complex with $\operatorname{Hom}_R(-,G)$ is a left exact functor, so it loses the information of the quotients, and that loss is precisely an $\operatorname{Ext}^1_R$ term; the theorem states a split short exact sequence exhibiting cohomology as an extension of a $\operatorname{Hom}$ by an $\operatorname{Ext}^1$, with the splitting unnatural. The homological algebra is that of Part I: $\operatorname{Ext}^1_R$ and its long exact sequence are the subject of the planned *Ext and Tor* and *Derived Functors*, written in parallel, and the exactness and diagram lemmas are proved in the written *Exact Sequences*. The present article takes the algebraic input as given and concentrates on the topological content: the cochain complex of a space, the cochain complex of a CW complex, the universal coefficient theorem for spaces, and the **Bockstein homomorphism** that measures how an integral class is transported through a short exact sequence of coefficient modules.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, $G$ is an $R$-module, chains are as in *Simplicial and Singular Homology*, and the coefficient module is separated from the space by a semicolon, so $H_n(X;R)$ is homology and $H^n(X;G)$ is cohomology, both functors to $R$-modules. Where a statement needs a field or the vanishing of torsion it is flagged at that point.

## Cohomology Groups

### The Dual Complex

**Definition.** Let $X$ be a topological space, $R$ a commutative ring with $1 \neq 0$ and $G$ an $R$-module. The **singular cochain module** in degree $n$ is the module of $R$-linear maps on the singular chains,

$$
C^n(X;G) = \operatorname{Hom}_R\bigl(C_n(X;R), G\bigr),
$$

whose elements are the **singular $n$-cochains**. A cochain $\varphi$ is determined by its values on singular simplices, and $C^n(X;G)$ is the direct product over singular $n$-simplices of copies of $G$, illustrating that cochain groups can be larger than chain groups.

**Definition.** The **coboundary** is the dual of the boundary,

$$
\delta^n = \partial_{n+1}^* : C^n(X;G) \to C^{n+1}(X;G), \qquad (\delta^n\varphi)(c) = \varphi(\partial_{n+1}c),
$$

for a cochain $\varphi$ and a chain $c$. Since $\partial\partial = 0$, also $\delta\delta = 0$, and $(C^*(X;G),\delta^*)$ is a **cochain complex**.

**Definition.** The **singular cohomology** of $X$ with coefficients in $G$ is

$$
H^n(X;G) = \ker\delta^n / \operatorname{im}\delta^{n-1},
$$

the **cocycles** modulo the **coboundaries**. In degree zero, $H^0(X;G)$ is the module of locally constant functions $X \to G$, so $H^0(X;G) \cong G$ for connected $X$ and $H^0(X;G) \cong G^{\pi_0(X)}$ in general.

**Definition (reduced cohomology).** Dualising the augmented chain complex of *Simplicial and Singular Homology* gives the **reduced cohomology** $\tilde H^n(X;G)$, with $\tilde H^n = H^n$ for $n \geq 1$ and $\tilde H^0(X;G) \cong \operatorname{coker}\bigl(\varepsilon^* : G \to \operatorname{Hom}_R(C_0(X;R),G)\bigr)$; for path-connected $X$, $\tilde H^0(X;G) = 0$.

### Functoriality and Covariance

**Theorem.** A continuous map $f : X \to Y$ induces a chain map $f_\# : C_*(X;R) \to C_*(Y;R)$, hence a cochain map $f^\# = \operatorname{Hom}_R(f_\#,G)$ in the opposite direction, and therefore homomorphisms

$$
f^* : H^n(Y;G) \longrightarrow H^n(X;G),
$$

with $(g \circ f)^* = f^* \circ g^*$ and $(\mathrm{id}_X)^* = \mathrm{id}$. Thus $H^n(-;G)$ is a **contravariant** functor. Homotopic maps induce the same homomorphism, and a homotopy equivalence induces an isomorphism.

*Proof.* For a cochain $\varphi$ on $Y$ the composite $\varphi \circ f_\#$ is a cochain on $X$; the identity $f^\# \delta = \delta f^\#$ is the chain-map identity $f_\#\partial = \partial f_\#$ dualised. Contravariance is immediate from $(g f)_\# = g_\# f_\#$. If $f \simeq g$ then $f_\# - g_\# = \partial P + P\partial$ for a chain homotopy $P$, and dualising gives $f^\# - g^\# = \delta P^* + P^*\delta$, so the induced maps on cohomology agree. $\square$

**Remark.** The contrast with homology is the point of the definition: the contravariant functor represented by a space is the object that admits pullbacks, and the whole of obstruction theory, characteristic-class theory and sheaf theory is built on it.

### Relative Cohomology and the Long Exact Sequence

**Definition.** For a subspace $A \subseteq X$ the **relative cochain complex** is $C^*(X,A;G) = \operatorname{Hom}_R(C_*(X,A;R),G)$, and its cohomology is the **relative cohomology** $H^n(X,A;G)$. Dualising the short exact sequence of *Simplicial and Singular Homology*,

$$
0 \to C_*(A;R) \to C_*(X;R) \to C_*(X,A;R) \to 0,
$$

by $\operatorname{Hom}_R(-,G)$ is left exact, and yields a short exact sequence of cochain complexes with the reversed arrow pattern; the snake lemma then gives the **long exact sequence of the pair**

$$
\cdots \to H^n(X,A;G) \to H^n(X;G) \to H^n(A;G) \xrightarrow{\ \delta\ } H^{n+1}(X,A;G) \to \cdots,
$$

with the connecting map **raising** degree by one, the dual of the homological case.

**Theorem (excision).** If $\overline Z \subseteq \operatorname{int}A$ then the inclusion induces $H^n(X,A;G) \cong H^n(X \setminus Z, A \setminus Z; G)$, by dualising the excision isomorphism of chain complexes.

## The Universal Coefficient Theorem

### Statement

**Theorem (universal coefficient theorem, cohomology).** Let $X$ be a topological space, $R$ a commutative ring with $1 \neq 0$ and $G$ an $R$-module. For each $n \geq 0$ there is a short exact sequence of $R$-modules

$$
0 \longrightarrow \operatorname{Ext}^1_R\bigl(H_{n-1}(X;R),\, G\bigr) \xrightarrow{\ \beta\ } H^n(X;G) \xrightarrow{\ \alpha\ } \operatorname{Hom}_R\bigl(H_n(X;R),\, G\bigr) \longrightarrow 0,
$$

which **splits**, though not naturally. The map $\alpha$ sends the class of a cocycle $\varphi$ to the homomorphism induced by $\varphi$ on homology classes, and is called the **Kronecker** or evaluation map. Consequently there is a (non-natural) isomorphism

$$
H^n(X;G) \cong \operatorname{Hom}_R\bigl(H_n(X;R),G\bigr) \oplus \operatorname{Ext}^1_R\bigl(H_{n-1}(X;R),G\bigr).
$$

The functors $\operatorname{Ext}^1_R$ and the long exact sequence it carries are the subject of the planned *Ext and Tor* and *Derived Functors* of Part I, which are being written in parallel; only their defining property is used here.

*Proof sketch.* Let $C_* = C_*(X;R)$, let $Z_n \subseteq C_n$ be the cycles and $B_n \subseteq C_n$ the boundaries, so that $0 \to B_n \to Z_n \to H_n \to 0$ and $0 \to Z_n \to C_n \to B_{n-1} \to 0$ are short exact. Applying $\operatorname{Hom}_R(-,G)$ to the second sequence and using that $C_n$ is free, hence that $\operatorname{Ext}^1_R(C_n,G) = 0$, gives $\operatorname{coker}\bigl(\operatorname{Hom}(C_n,G)\to\operatorname{Hom}(Z_n,G)\bigr) \cong \operatorname{Ext}^1_R(B_{n-1},G)$; applying it to the first gives the identity $H^n = \operatorname{coker}\bigl(\operatorname{Hom}(C_n,G) \to \operatorname{Hom}(Z_n,G)\bigr)$. Combining, $H^n \cong \operatorname{Ext}^1_R(B_{n-1},G)$, and the sequence $0 \to B_{n-1}\to Z_{n-1} \to H_{n-1}\to 0$ with $\operatorname{Hom}(Z_{n-1},G)$ analysed in the same way produces the four-term exact sequence displayed. Splitting holds because $\operatorname{Hom}_R(H_n,G)$ is free when $R$ is a principal ideal domain and $H_n$ is finitely generated, and in general the sequence splits because the Ext term is a direct summand in the relevant cases; the splitting depends on choices, which is why it is not natural. $\square$

**Corollary (field coefficients).** If $R = F$ is a field and $G$ an $F$-vector space, then $\operatorname{Ext}^1_F(-,G) = 0$, so

$$
H^n(X;G) \cong \operatorname{Hom}_F\bigl(H_n(X;F),G\bigr),
$$

naturally; with $G = F$ this is the duality $H^n(X;F) \cong H_n(X;F)^*$ between cohomology and the linear dual of homology. In particular $\dim_F H^n(X;F) = \dim_F H_n(X;F)$ for each $n$.

**Corollary (integral coefficients).** For $G = \mathbb{Z}$ and $R = \mathbb{Z}$, the structure theorem for finitely generated abelian groups gives

$$
H^n(X;\mathbb{Z}) \cong \bigl(H_n(X;\mathbb{Z})/\text{torsion}\bigr) \oplus \operatorname{Torsion}\bigl(H_{n-1}(X;\mathbb{Z})\bigr),
$$

so the free parts of $H^n$ and $H_n$ agree and the torsion of $H^n$ in degree $n$ is the torsion of $H_{n-1}$: **cohomological torsion is shifted down by one degree relative to homology**. Thus $\mathbb{RP}^2$ has $H_0 \cong \mathbb{Z}$, $H_1 \cong \mathbb{Z}/2$, $H_2 = 0$ and dually $H^0 \cong \mathbb{Z}$, $H^1 = 0$, $H^2 \cong \mathbb{Z}/2$.

**Corollary (universal coefficient theorem, homology).** The same argument applied to the tensor product gives the homology version,

$$
0 \to H_n(X;R) \otimes_R G \to H_n(X;G) \to \operatorname{Tor}_1^R\bigl(H_{n-1}(X;R),G\bigr) \to 0,
$$

splitting unnaturally, with $\operatorname{Tor}_1^R$ the torsion functor of Part I's *Ext and Tor*, written in parallel.

**Remark.** The failure of naturality is not a technicality: the splitting requires a choice of splitting of the surjections $C_n \to B_{n-1}$, and different choices produce different isomorphisms, related by the action of $\operatorname{Hom}(H_n,G)$ shifted by natural transformations. The non-naturality is the reason the Bockstein homomorphism below is not induced by a map of spaces.

### The Cohomology of a CW Complex

**Definition.** Let $X$ be a CW complex with cellular chain complex $C_*^{\mathrm{CW}}(X;R)$ as in *CW Complexes and Cellular Approximation*. The **cellular cochain complex** is

$$
C^n_{\mathrm{CW}}(X;G) = \operatorname{Hom}_R\bigl(C_n^{\mathrm{CW}}(X;R), G\bigr),
$$

with coboundary the dual of the cellular boundary. Since the cellular chain complex computes $H_*(X;R)$, and dualising a chain complex of free modules computes the cohomology of the dual, the cohomology of the cellular complex is $H^*(X;G)$, and the universal coefficient theorem applies with $H_*(X;R)$ computed cellularly.

**Example.** For the sphere $S^n$ with one $0$-cell and one $n$-cell, $C^k_{\mathrm{CW}} \cong G$ for $k = 0, n$ and $0$ otherwise, and all coboundaries vanish; hence $H^k(S^n;G) \cong G$ for $k = 0,n$ and $0$ otherwise, for every coefficient module $G$. This is the case in which cohomology and homology are indistinguishable.

**Example.** For $\mathbb{RP}^2$ the cellular chain complex over $\mathbb{Z}$ is $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \xrightarrow{0} \mathbb{Z} \to 0$, dualising gives $0 \to \mathbb{Z} \xrightarrow{0} \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to 0$, so $H^0 \cong \mathbb{Z}$, $H^1 = 0$, $H^2 \cong \mathbb{Z}/2$, in agreement with the universal coefficient theorem; note that $H^1(\mathbb{RP}^2;\mathbb{Z}) = 0$ while $H_1(\mathbb{RP}^2;\mathbb{Z}) \cong \mathbb{Z}/2$, the shift of torsion.

## The Bockstein Homomorphism

### Coefficients in a Short Exact Sequence

**Theorem (Bockstein).** Let

$$
0 \longrightarrow G' \xrightarrow{\ i\ } G \xrightarrow{\ j\ } G'' \longrightarrow 0
$$

be a short exact sequence of $R$-modules. Then there is a long exact sequence in cohomology,

$$
\cdots \to H^n(X;G') \xrightarrow{\ i_* \ } H^n(X;G) \xrightarrow{\ j_* \ } H^n(X;G'') \xrightarrow{\ \beta\ } H^{n+1}(X;G') \to \cdots,
$$

natural in $X$, in which $\beta$ is the **Bockstein homomorphism** associated to the coefficient sequence.

*Proof.* The functor $\operatorname{Hom}_R(C_n(X;R),-)$ is left exact, so applying it to the coefficient sequence gives a short exact sequence of cochain complexes $0 \to C^*(X;G') \to C^*(X;G) \to C^*(X;G'') \to 0$; the connecting map of the snake lemma is $\beta$, and exactness is the snake lemma. Naturality in $X$ is the naturality of the snake lemma under chain maps. $\square$

**Example (the mod-2 Bockstein).** For $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$ there is an exact sequence

$$
\cdots \to H^n(X;\mathbb{Z}) \xrightarrow{2} H^n(X;\mathbb{Z}) \to H^n(X;\mathbb{Z}/2) \xrightarrow{\ \beta\ } H^{n+1}(X;\mathbb{Z}) \xrightarrow{2} \cdots,
$$

the map $\beta$ being that of **coefficient reduction**; it detects whether an integral class lifts a mod-2 class. For $\mathbb{RP}^2$, $\beta$ is an isomorphism $H^1(X;\mathbb{Z}/2) \cong \mathbb{Z}/2 \to H^2(X;\mathbb{Z}) \cong \mathbb{Z}/2$.

**Example (the integral Bockstein).** For $0 \to \mathbb{Z} \xrightarrow{m} \mathbb{Z} \to \mathbb{Z}/m \to 0$ the same construction gives the **Bockstein** $\beta_m : H^n(X;\mathbb{Z}/m) \to H^{n+1}(X;\mathbb{Z})$ with $m\beta_m = 0$; the composite $\beta \beta$ need not vanish for a general coefficient sequence, and when the sequence is the one above the relation $\beta^2 = 0$ holds on the image of reduction.

**Remark.** The Bockstein is not induced by a map of spaces: it does not commute with arbitrary coefficient maps, only with maps of short exact sequences, and this is the same non-naturality met in the universal coefficient theorem. It is the standard tool for extracting integral information from mod-$p$ information, and it reappears in the cohomology operations of the stable theory.

## Computations and the Degenerate Spectral Sequence

### The Universal Coefficient Theorem as a Spectral Sequence

**Theorem (universal coefficient spectral sequence).** Let $X$ be a topological space, $R$ a commutative ring with $1\neq0$ and $G$ an $R$-module. There is a convergent first-quadrant spectral sequence

$$
E_2^{p,q} = \operatorname{Ext}^p_R\bigl(H_q(X;R),G\bigr)\ \Longrightarrow\ H^{p+q}(X;G),
$$

natural in $X$ and in $G$ as an $R$-module, with $E_2^{p,q} = 0$ for $p\geq2$. Consequently $E_2 = E_\infty$, and the filtration of $H^n(X;G)$ has exactly two pieces, $E_\infty^{0,n} = \operatorname{Hom}_R(H_n(X;R),G)$ and $E_\infty^{1,n-1} = \operatorname{Ext}^1_R(H_{n-1}(X;R),G)$, whose extension is $H^n(X;G)$.

*Proof.* The spectral sequence is the one of the double complex obtained from a projective resolution of $G$ and a projective resolution of the chain complex $C_*(X;R)$, and it is the standard spectral sequence of these two resolutions, as in Part I's *Spectral Sequences* and *Derived Functors*; its $E_2$ page is as stated and it converges to the cohomology of the total complex, which is $H^*(X;G)$. The vanishing of the columns $p\geq2$ forces all differentials out of $E_2$ to land in zero, so $E_2 = E_\infty$, and only the two columns with $p = 0,1$ can contribute to total degree $n$. $\square$

**Remark (what the spectral sequence adds to the short exact sequence).** The short exact sequence of the universal coefficient theorem is the assertion that the two-piece filtration of $H^n(X;G)$ has subquotients as above; the extension is nontrivial in general and is split only after a noncanonical choice, which is one way to see the non-naturality. The spectral-sequence form has the further content that it survives when the coefficient module has higher derived functors: if the ground ring is replaced by a ring of higher global dimension, or if the complex is replaced by one unbounded below, the higher columns are the ones that measure the new phenomena, and the collapsed statement above is exactly the degenerate case. This is the pattern shared by the Künneth theorem, whose spectral sequence is described.

### Lens Spaces, Moore Spaces and Real Projective Spaces

**Example (the lens space $L(n;1)$).** The lens space $L(n;1) = S^3/(\mathbb{Z}/n)$ has a CW structure with one cell in each of the dimensions $0,1,2,3$, and the cellular chain complex over $\mathbb{Z}$ is

$$
0\to\mathbb{Z}\xrightarrow{\ 0\ }\mathbb{Z}\xrightarrow{\ n\ }\mathbb{Z}\xrightarrow{\ 0\ }\mathbb{Z}\to 0,
$$

the differentials alternating between $0$ and multiplication by $n$, beginning with $d_1 = 0$, by the cellular boundary formula of *CW Complexes and Cellular Approximation*. Hence

$$
H_0 = \mathbb{Z},\quad H_1 = \mathbb{Z}/n,\quad H_2 = 0,\quad H_3 = \mathbb{Z},
$$

and dualising the complex gives $H^0 = \mathbb{Z}$, $H^1 = 0$, $H^2 = \mathbb{Z}/n$, $H^3 = \mathbb{Z}$. The universal coefficient theorem confirms each entry: $H^1 = \operatorname{Ext}^1(H_0,\mathbb{Z})\oplus\operatorname{Hom}(H_1,\mathbb{Z}) = 0$, since $\operatorname{Hom}(\mathbb{Z}/n,\mathbb{Z}) = 0$; and $H^2 = \operatorname{Ext}^1(H_1,\mathbb{Z})\oplus\operatorname{Hom}(H_2,\mathbb{Z}) = \mathbb{Z}/n$, since $\operatorname{Ext}^1(\mathbb{Z}/n,\mathbb{Z}) \cong \mathbb{Z}/n$ from the resolution $0\to\mathbb{Z}\xrightarrow{n}\mathbb{Z}\to\mathbb{Z}/n\to0$. The example is the standard witness of the degree shift: the torsion of $H_1$ appears in $H^2$.

**Example (the Moore space $M(\mathbb{Z}/n,1)$).** Let $M(\mathbb{Z}/n,1) = S^1\cup_n e^2$ be the two-dimensional cell complex obtained by attaching a $2$-cell to a circle by a map of degree $n$. Its homology is $H_0 = \mathbb{Z}$, $H_1 = \mathbb{Z}/n$ and $H_i = 0$ otherwise, and the universal coefficient theorem gives

$$
H^0 = \mathbb{Z},\qquad H^1 = \operatorname{Hom}(\mathbb{Z}/n,\mathbb{Z}) = 0,\qquad H^2 = \operatorname{Ext}^1(\mathbb{Z}/n,\mathbb{Z}) \cong \mathbb{Z}/n,
$$

so that cohomology with integral coefficients does not see the mod-$n$ class in degree one at all but sees it in degree two. With coefficients in $\mathbb{Z}/m$ the same theorem gives

$$
H^1(M;\mathbb{Z}/m) \cong \operatorname{Hom}(\mathbb{Z}/n,\mathbb{Z}/m)\cong\mathbb{Z}/\gcd(m,n), \qquad H^2(M;\mathbb{Z}/m)\cong\operatorname{Ext}^1(\mathbb{Z}/n,\mathbb{Z}/m)\cong\mathbb{Z}/\gcd(m,n),
$$

the last isomorphism because $\operatorname{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/n,\mathbb{Z}/m)\cong\ker(m : \mathbb{Z}/n\to\mathbb{Z}/n)$ has order $\gcd(m,n)$. The two groups agree, which is a general feature of coefficients in a finite cyclic group on a space whose homology is concentrated in two adjacent degrees. The Bockstein $\beta_m : H^1(M;\mathbb{Z}/m)\to H^2(M;\mathbb{Z})$ of the coefficient sequence $0\to\mathbb{Z}\xrightarrow{m}\mathbb{Z}\to\mathbb{Z}/m\to0$ is injective with image the subgroup of $\mathbb{Z}/n$ of order $\gcd(m,n)$, since $H^1(M;\mathbb{Z}) = 0$ and the image is the kernel of multiplication by $m$ on $H^2(M;\mathbb{Z}) \cong \mathbb{Z}/n$.

**Example (real projective space).** For $\mathbb{RP}^n$ with its standard cell structure the differentials of the cellular chain complex over $\mathbb{Z}$ alternate between $0$ and multiplication by $2$, so

$$
H_0 = \mathbb{Z},\qquad H_k = \mathbb{Z}/2\ \ (k \text{ odd},\ 0<k<n),\qquad H_k = 0\ \ (k \text{ even},\ 0<k<n),
$$

with $H_n = \mathbb{Z}$ for $n$ odd and $H_n = 0$ for $n$ even. The universal coefficient theorem then gives $H^k(\mathbb{RP}^n;\mathbb{Z}) \cong \mathbb{Z}/2$ for $k$ even with $0<k<n$, $H^k = 0$ for $k$ odd with $0<k<n$, and at the top degree $H^n \cong \mathbb{Z}$ for $n$ odd, $H^n\cong\mathbb{Z}/2$ for $n$ even. In particular $H^n(\mathbb{RP}^n;\mathbb{Z})$ is not the dual of $H_n(\mathbb{RP}^n;\mathbb{Z})$ in the naive sense, and the discrepancy at the top degree is the first appearance of the orientability class, whose cohomological form is not covered here.

**Remark (the general rule for the computation).** The examples display the two-part structure of the theorem: the free part of $H^n(X;\mathbb{Z})$ is the free part of $H_n(X;\mathbb{Z})$, and the torsion of $H^n(X;\mathbb{Z})$ is the torsion of $H_{n-1}(X;\mathbb{Z})$. Computationally one may therefore read the integral cohomology of a finite CW complex from its integral homology by shifting the torsion up one degree and leaving the free parts in place; with coefficients in a ring $R$ and a module $G$, the same computation uses the structure of the modules $H_n(X;R)$ over $R$, and the naturality of the sequence ensures that the computation is compatible with maps of spaces.

## Summary

Cohomology is the homology of the complex obtained by applying $\operatorname{Hom}_R(-,G)$ to the singular chain complex. It is a contravariant functor: a map $f$ induces $f^*$ in the opposite direction, homotopic maps induce the same map, and homotopy equivalences induce isomorphisms. The relative groups fit in a long exact sequence of a pair with the connecting map raising degree, and excision holds exactly as in homology.

The universal coefficient theorem expresses cohomology in terms of homology: there is a split short exact sequence with $\operatorname{Ext}^1_R(H_{n-1}(X;R),G)$ as submodule and $\operatorname{Hom}_R(H_n(X;R),G)$ as quotient, the splitting being unnatural. Over a field the Ext term vanishes and cohomology is the linear dual of homology in each degree; over $\mathbb{Z}$ the free parts agree and the torsion of $H^n$ is the torsion of $H_{n-1}$, shifted down by one. A CW complex computes its cohomology by dualising its cellular chain complex, so all the computations of the cellular theory carry over. The Bockstein homomorphism, associated to a short exact sequence of coefficient modules, is the connecting map of the resulting long exact sequence in cohomology; it is natural in the space but not induced by a map of spaces, and it detects the failure of an integral class to lift a class with smaller coefficients.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$ |
| $G$ | coefficient $R$-module |
| $C^n(X;G) = \operatorname{Hom}_R(C_n(X;R),G)$ | Singular $n$-cochains |
| $\delta^n = \partial_{n+1}^*$ | Coboundary; $\delta\delta = 0$ |
| $H^n(X;G) = \ker\delta/\operatorname{im}\delta$ | Singular cohomology; cocycles modulo coboundaries |
| $\tilde H^n(X;G)$ | Reduced cohomology |
| $H^n(X,A;G)$ | Relative cohomology |
| $f^* : H^n(Y;G) \to H^n(X;G)$ | Contravariant pullback along $f : X \to Y$ |
| $\alpha : H^n(X;G) \to \operatorname{Hom}_R(H_n(X;R),G)$ | Evaluation (Kronecker) map |
| $\operatorname{Ext}^1_R(-,-)$, $\operatorname{Tor}_1^R(-,-)$ | Derived functors of Part I, written in parallel; the UCT terms |
| $0 \to \operatorname{Ext}^1(H_{n-1},G) \to H^n(X;G) \to \operatorname{Hom}(H_n,G) \to 0$ | Universal coefficient theorem (splits unnaturally) |
| $C^n_{\mathrm{CW}}(X;G)$ | Cellular cochains; dual of the cellular chain complex |
| $\beta$ | Bockstein homomorphism, raising degree by one |
| $\beta_m : H^n(X;\mathbb{Z}/m) \to H^{n+1}(X;\mathbb{Z})$ | Bockstein of the sequence $0 \to \mathbb{Z} \xrightarrow{m} \mathbb{Z} \to \mathbb{Z}/m \to 0$ |
| $S^n$, $\mathbb{RP}^n$ | Sphere and real projective space, as computational examples |





## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for singular cohomology, the universal coefficient theorem and the Bockstein homomorphism.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for $\operatorname{Ext}$ and $\operatorname{Tor}$, their long exact sequences, and the universal coefficient theorems in full.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the derived-functor approach to the universal coefficient theorem and the role of naturality.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for the split exact sequence and its non-naturality.
- Samuel Eilenberg and Norman Steenrod, *Foundations of Algebraic Topology* (Princeton University Press, 1952), for the axiomatic treatment of cohomology and the coefficient sequences.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for cohomology with local coefficients and the Bockstein operations.
- Edwin H. Spanier, *Algebraic Topology* (McGraw–Hill, 1966), for the universal coefficient spectral sequence and its degenerate cases.
