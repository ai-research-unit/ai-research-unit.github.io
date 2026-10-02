
# __Descent and the Involution on the Cohomology__

## Introduction

A descent datum on a sheaf — an action of a group, an involution, a Galois action — acts on the cohomology of the sheaf, and the **fixed part** of that action is the cohomology of the **descended** sheaf: the classes that are invariant under the descent are exactly the classes that come from the quotient or from the base. This article is the operator-level synthesis of the two previous themes: it takes the involution of *Cohomology with an Involution* and the descent of *Galois Descent for Sheaves*, and it studies the cohomological consequence of the descent — the action of the descent group on the cohomology, the identification of its fixed part with the cohomology of the descended object, the spectral sequence that computes the passage from the one to the other, and the **descent of an involution on the cohomology**: an involution of the cohomology of the descended datum that is compatible with the descent descends to an involution of the cohomology of the descended sheaf. The involution is the order-two case throughout, and the Galois action is the semilinear case over a field extension.

The group acts on the cohomology through its action on the sheaf, the action commutes with the cup product, and the fixed part is computed by the transfer in the finite case and by the descent spectral sequence in general; the Galois case adds the semilinearity of the action on the coefficients and the identification $H^*(X,\mathcal{F}^{\Gamma})\cong H^*(X_K,\mathcal{F})^{\Gamma}$ of the invariants with the cohomology of the descended sheaf. This article is the third and last of the `- * Operator Theory` group and closes the category; the involution on the cohomology is *Cohomology with an Involution*, the descent of the sheaves is *Galois Descent for Sheaves* and *Equivariant Sheaves and Descent*, the spectral sequences are *Spectral Sequences*, the group cohomology is *Group Cohomology* of Part I, and the fixed-point formula for a general action is Part III.

The article uses no analysis and no geometry: the actions are algebraic actions on sheaves of modules, the cohomology is the sheaf cohomology of Part II, the Galois theory is that of Part I, and no measure, no norm and no derivative occurs. Throughout, $G$ or $\Gamma$ is a group acting on $X$ with an equivariant structure on the sheaf $\mathcal{F}$, the action on the cohomology is written $\theta$ when it is an involution and $\gamma\mapsto\gamma^*$ in general, the fixed part is written $H^*(X,\mathcal{F})^{G}$, and the descended sheaf is $\mathcal{F}^{G}$ over the quotient $X/G$ or the fixed sheaf $\mathcal{F}^{\Gamma}$ over $X$.

## The Action of the Descent Group on the Cohomology

**Proposition (the action).** Let $G$ act on $X$ and let $\mathcal{F}$ carry a $G$-equivariant structure, as in *Equivariant Sheaves and Descent*. Then $G$ acts on the cohomology $H^*(X,\mathcal{F})$ by $\gamma^*=H^*(\gamma,\varphi_{\gamma})$, the action is functorial in the equivariant sheaf, and it commutes with the cup product of *The Cup Product on Sheaf Cohomology*: $\gamma^*(\alpha\smile\beta)=\gamma^*\alpha\smile\gamma^*\beta$. When $G=\mathbb{Z}/2$ with generator $\theta$, the action is an involution of the graded ring, $\theta^2=\mathrm{id}$, and its fixed part $H^*(X,\mathcal{F})^{\theta}$ is the invariant cohomology.

*Proof.* The equivariant structure gives an isomorphism $\varphi_{\gamma}:\gamma_*\mathcal{F}\to\mathcal{F}$, and the functor $H^*(X,-)$ carries it to an isomorphism $H^*(X,\mathcal{F})\to H^*(X,\mathcal{F})$ that is the action; the composability of the equivariant structures makes the assignment a group homomorphism, and the naturality of the cup product makes it multiplicative. For an involution the square is the identity because the equivariant structure is of order two.

**Proposition (the fixed part is a module of the invariant ring).** The fixed part $H^*(X,\mathcal{F})^{G}$ is a module over the invariant ring $H^*(X,\mathcal{O}_X)^{G}$, and the cup product of two invariant classes is invariant; the graded ring $H^*(X,\mathcal{O}_X)^{G}$ is the **invariant cohomology ring**.

*Proof.* The action is a ring action on the cohomology by the multiplicativity, so the fixed elements form a subring and the fixed part of the coefficients is a module over it.

**Proposition (the sign convention of the graded case).** If the action is by a graded involution $\theta$ with a sign on the cohomological degree, that is $\theta\alpha=(-1)^{|\alpha|}\theta^*\alpha$ on a class of degree $|\alpha|$, the fixed part is the **even part** of the action and the anti-invariant part the odd part; the two conventions agree when the involution is not twisted by the degree, which is the case of an action on the space.

*Proof.* The twisted action is the composition of the untwisted one with the degree sign; its fixed part is the set of classes with $\theta^*\alpha=(-1)^{|\alpha|}\alpha$, which is the even eigenspace of $\theta^*$ in degrees where $(-1)^{|\alpha|}=+1$. The two conventions are distinguished in practice and one must say which is meant, as in *Cohomology with an Involution*.

## The Fixed Part and the Descent Isomorphism

**Theorem (the fixed part is the cohomology of the descended sheaf).** Let $G$ act on $X$ with the equivariant sheaf $\mathcal{F}$, and let the descent hold: the quotient $X/G$ exists and $\mathcal{F}^{G}$ is the fixed sheaf. Then the descent isomorphism on the cohomology is

$$
H^*(X/G,\mathcal{F}^{G})\;\xrightarrow{\ \cong\ }\;H^*(X,\mathcal{F})^{G},
$$

the fixed part of the cohomology of the sheaf is the cohomology of its descended sheaf; for $G$ finite the identification follows from the transfer, $q^*:H^*(X/G,\mathcal{F}^{G})\to H^*(X,\mathcal{F})^{G}$ being an isomorphism.

*Proof.* The transfer of *Cohomology with an Involution* gives the statements for a finite group: the composite $q^*\rho$ is multiplication by the order of the group on the invariant part, invertible when the order is invertible in the coefficients, and it is the identity in the standard cases over a field of characteristic zero; the map $q^*$ from the quotient to the invariants is the isomorphism in those cases. The general descent is that of *Equivariant Sheaves and Descent*.

**Theorem (the Galois form).** Let $\Gamma=\operatorname{Gal}(K/k)$ act semilinearly on the sheaf $\mathcal{F}$ over $X_K$, as in *Galois Descent for Sheaves*, and let $\mathcal{F}^{\Gamma}$ be the fixed sheaf over $X$. Then

$$
H^*(X,\mathcal{F}^{\Gamma})\;\xrightarrow{\ \cong\ }\;H^*(X_K,\mathcal{F})^{\Gamma},
$$

with the action of $\Gamma$ on the cohomology semilinear over $K$; the invariants of the cohomology are the cohomology of the descended sheaf.

*Proof.* The base change and the descent of the sheaf give the statement by the functoriality of the cohomology along the descent; the fixed sheaf is defined as in *Galois Descent for Sheaves*, and the same argument identifies the invariants of the cohomology, the two functors $\Gamma$-fixed sheaf and cohomology commuting with the descent because the descent is an equivalence of categories of equivariant sheaves.

## The Descent Spectral Sequence

**Theorem (the descent spectral sequence).** Let $G$ act on $X$ with $\mathcal{F}$ equivariant and let the action be **free** on a $G$-invariant open cover, so that the quotient exists and the cover descends. Then there is a spectral sequence

$$
E_2^{p,q}=H^p(G,H^q(X,\mathcal{F}))\;\Longrightarrow\;H^{p+q}(X/G,\mathcal{F}^{G}),
$$

the **descent spectral sequence**; its edge maps in low degree give the exact sequence

$$
0\to H^1(G,H^0(X,\mathcal{F}))\to H^1(X/G,\mathcal{F}^{G})\to H^0(G,H^1(X,\mathcal{F}))\to H^2(G,H^0(X,\mathcal{F}))\to\cdots,
$$

which describes the cohomology of the descended sheaf in terms of the invariants of the cohomology and the group cohomology.

*Proof.* The spectral sequence is the Cartan–Leray spectral sequence of the quotient map, whose construction is *Spectral Sequences* and *Group Cohomology*: the double complex is the one of the equivariant Čech complex of a $G$-invariant cover, one differential being the Čech coboundary of *The Coboundary Operator* and the other the group differential, and the two spectral sequences of the double complex carry the two filtrations. The low-degree exact sequence is the standard exact sequence of the edge maps of a first-quadrant spectral sequence.

**Proposition (the involution on the pages).** For $G=\mathbb{Z}/2$ the descent spectral sequence carries the involution $\theta$ of the cohomology on the $E_2$ page, $E_2^{p,q}=H^p(\mathbb{Z}/2,H^q(X,\mathcal{F}))$ with the involution induced by the action on the coefficients and on the group, and the involution commutes with the differentials and converges to the involution induced by $\theta$ on $H^*(X/G,\mathcal{F}^{G})$; the fixed part of the abutment is computed from the fixed parts of the pages. A class of the abutment is invariant under the descended involution exactly when its representatives are invariant on the pages, the degeneration hypothesis of *The Involution on the Coboundary* being understood.

*Proof.* The involution of the sheaf acts on the equivariant Čech complex and commutes with both differentials, so it induces an involution on the pages of the spectral sequence by *The Involution on the Coboundary*; the identification of the limit involution is the naturality of the edge maps, and the fixed part of the abutment is the limit of the fixed parts when the sequence degenerates.

**Remark (the obstruction).** The spectral sequence measures the failure of a class of the cohomology to come from the quotient: the invariants $H^0(G,H^q)$ contribute the descended classes, and the higher group cohomology registers the obstructions. For a class of degree zero fixed by the action, the obstruction to its being descended is a class in $H^1(G,H^0)$, which is the first cohomology of the group in the coefficient sheaf.

## The Galois Action on the Cohomology

**Proposition (the semilinear action).** Under a Galois descent, the group $\Gamma$ acts on $H^*(X_K,\mathcal{F})$ semilinearly over $K$: $\gamma^*(\lambda\alpha)=\gamma(\lambda)\gamma^*\alpha$ for $\lambda\in K$ and $\alpha$ a class, and the invariants form a $k$-vector space. The cohomology of the descended sheaf is $k$-linear and the descent isomorphism $H^*(X,\mathcal{F}^{\Gamma})\otimes_kK\cong H^*(X_K,\mathcal{F})$ holds when the invariants span, in particular in the finite Galois case with a normal basis.

*Proof.* The action of $\Gamma$ is through the equivariant structure and hence is semilinear over the action of $\Gamma$ on the coefficients $K$; the invariants are a $k$-subspace because $\gamma(c)=c$ for $c\in k$. The identification with the cohomology of the descended sheaf is the Galois form of the fixed-part theorem, and the spanning is the normal-basis descent used in *Galois Descent for Sheaves*.

**Corollary (the real case).** For the conjugation of $K=\mathbb{C}$ over $k=\mathbb{R}$ acting on a sheaf over $X_{\mathbb{C}}$, the invariants of the cohomology are the cohomology of the real form: $H^*(X,\mathcal{F}^{\Gamma})\cong H^*(X_{\mathbb{C}},\mathcal{F})^{\Gamma}$, and for the constant sheaf $\mathbb{C}$ this reads $H^*(X,\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}=H^*(X_{\mathbb{C}},\mathbb{C})^{\Gamma}$, the cohomology of the real locus being the fixed part of the cohomology of the complexification.

*Proof.* The statement is the Galois form with $K/k=\mathbb{C}/\mathbb{R}$ and $\Gamma=\mathbb{Z}/2$; the computation for the constant sheaf uses the identification of the complexified cohomology with the cohomology of the constant sheaf $\mathbb{C}$ and the semilinear involution of the coefficients, whose fixed part is the real cohomology.

**Proposition (the descent of an involution on the cohomology).** Let $\theta$ be an involution of $H^*(X_K,\mathcal{F})$ commuting with the Galois action and semilinear over the involution $\sigma$ of $K$, $\theta(\lambda\alpha)=\sigma(\lambda)\theta(\alpha)$. Then $\theta$ descends to an involution $\theta^{\Gamma}$ of the fixed part $H^*(X_K,\mathcal{F})^{\Gamma}\cong H^*(X,\mathcal{F}^{\Gamma})$, and the descended involution is the involution of the cohomology of the descended sheaf; the fixed part of the descended involution is the fixed part of the original one, computed on the invariants.

*Proof.* The involution preserves the invariants because it commutes with the Galois action, so it restricts to the fixed part; the restriction is an involution of the fixed part, and the identification of the fixed part with the cohomology of the descended sheaf transports it to the descended involution. The invariance of the construction is the functoriality of the fixed part, and the fixed part of the restriction is the fixed part of $\theta$ intersected with the invariants.

## Worked Cases

### The Involution of the Čech Complex and the Quotient

For a free involution of the space and an invariant cover, the involution of the Čech complex of *The Involution on the Coboundary* computes the action on the cohomology at the level of cochains, and its invariant cochains compute the fixed part $H^*(X,\mathcal{F})^{\theta}=H^*(X/\theta,\mathcal{F}^{\theta})$ of the transfer; the descent spectral sequence degenerates and the descent isomorphism is read directly from the invariant cochains.

### The Galois Action on the Constant Sheaf

For $\Gamma$ acting on the constant sheaf $K$ over $X_K$, the action on the cohomology is semilinear, and the invariants are $H^*(X_K,K)^{\Gamma}=H^*(X,k)\otimes_kK$; for $K/k=\mathbb{C}/\mathbb{R}$ this is the comparison of the real and the complex cohomology, and the conjugation acts on $H^*(X_{\mathbb{C}},\mathbb{C})$ with the fixed part the complexification of the real cohomology.

### The Order-Two Case of the Spectral Sequence

For $G=\mathbb{Z}/2$, the $E_2$ page of the descent spectral sequence is $H^p(\mathbb{Z}/2,H^q(X,\mathcal{F}))$, and the low-degree exact sequence gives $0\to H^1(\mathbb{Z}/2,H^0)\to H^1(X/G,\mathcal{F}^{G})\to (H^1)^{\theta}\to H^2(\mathbb{Z}/2,H^0)$; the example shows how the invariants of the cohomology and the group cohomology combine, the group cohomology of $\mathbb{Z}/2$ being periodic of period one.

## Summary

A descent datum on a sheaf — an action of a group $G$, an involution, a Galois action — acts on the sheaf cohomology, functorially and compatibly with the cup product, so that the fixed part is a module over the invariant cohomology ring. The fixed part of the cohomology is the cohomology of the descended sheaf, $H^*(X/G,\mathcal{F}^{G})\cong H^*(X,\mathcal{F})^{G}$, by the transfer in the finite case and by the descent of the equivariant sheaves in general; in the Galois case the action is semilinear over $K$ and $H^*(X,\mathcal{F}^{\Gamma})\cong H^*(X_K,\mathcal{F})^{\Gamma}$, with the real case $H^*(X_{\mathbb{C}},\mathbb{C})^{\Gamma}=H^*(X,\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}$ as the model.

The passage from the invariants of the cohomology to the cohomology of the descended object is computed by the descent spectral sequence $E_2^{p,q}=H^p(G,H^q(X,\mathcal{F}))\Longrightarrow H^{p+q}(X/G,\mathcal{F}^{G})$, whose edge maps give the cohomological obstructions to descending a class; for an involution the sequence carries on each page the involution induced by the action, and the fixed part of the abutment is the limit of the fixed parts. An involution of the cohomology that commutes with the descent and is semilinear over the involution of the coefficients descends to an involution of the cohomology of the descended sheaf, and this descent of the involution is the last statement of the category: the element involution, the operator adjoint and the cohomological action meet in the invariants, and all three are computed by the same descent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $\Gamma$ | descent group; Galois group $\operatorname{Gal}(K/k)$ in the semilinear case |
| $\gamma^*=H^*(\gamma,\varphi_{\gamma})$ | action on the cohomology; commutes with the cup product |
| $H^*(X,\mathcal{F})^{G}$, $H^*(X,\mathcal{F})^{\theta}$ | fixed part of the cohomology; invariant cohomology |
| $H^*(X/G,\mathcal{F}^{G})\cong H^*(X,\mathcal{F})^{G}$ | descent isomorphism; fixed part $=$ cohomology of the descended sheaf |
| $H^*(X,\mathcal{F}^{\Gamma})\cong H^*(X_K,\mathcal{F})^{\Gamma}$ | Galois form; semilinear action over $K$ |
| $E_2^{p,q}=H^p(G,H^q(X,\mathcal{F}))\Longrightarrow H^{p+q}(X/G,\mathcal{F}^{G})$ | descent spectral sequence |
| $H^1(G,H^0)\to H^1(X/G,\mathcal{F}^{G})\to H^0(G,H^1)$ | low-degree edge sequence; the obstruction to descending a class |
| $H^*(X_{\mathbb{C}},\mathbb{C})^{\Gamma}=H^*(X,\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}$ | the real case of the Galois invariants |
| $\theta(\lambda\alpha)=\sigma(\lambda)\theta(\alpha)$ | semilinear involution; descends to $\theta^{\Gamma}$ on the invariants |

## Further Reading

- Jean-Pierre Serre, *Galois Cohomology* (Springer, corrected second printing, 2002), for the Galois descent and the group cohomology of the descent.
- Kenneth S. Brown, *Cohomology of Groups* (Springer, 1982), for the group cohomology and the spectral sequence of a group extension.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the spectral sequences of a double complex and the edge maps.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the actions on the Čech complexes and the invariant cohomology.
- Joseph Bernstein and Valery Lunts, *Equivariant Sheaves and Functors* (Springer Lecture Notes in Mathematics 1578, 1994), for the equivariant cohomology and the descent of the functors.
- Amnon Neeman, *Triangulated Categories* (Annals of Mathematics Studies 148, Princeton University Press, 2001), for the descent in the derived setting and the identification of the invariants, cited for the derived form.
