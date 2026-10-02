
# __The Galois Action on the Cohomology__

## Introduction

The Galois action on a variety over a field acts on the cohomology of its sheaves, and at the level of the elements of the cohomology it is an **involution**, or a group action, that is fixed by nothing linear and yet has a rich theory: the cohomology is a **semilinear module**, its invariants are the cohomology of the descended variety, and the comparison between the two is the **Hochschild–Serre spectral sequence**. When the coefficients are chosen so that the twist is absorbed, the semilinear module becomes a **Galois representation**, a continuous linear action of the Galois group on a finite-dimensional space over the coefficient field, and the invariants of the representation are the cohomology of the variety over the base field. This article fixes the semilinear module of the cohomology, its invariants and the spectral sequence, the Galois representations it defines, and the behaviour of the cup product and the intersection pairing under the involution, and it is the fourth article of the `- * Theory` group.

The article reads the operator of *The Galois Action as an Operator* on the cohomology, and it is the cohomological companion of *Real Structures on Varieties and Galois Descent*: descent gives the variety, and the present article gives the cohomology of the descended variety as the invariants. The cohomology is that of *Coherent Sheaves* and *Sheaf Cohomology*, the group cohomology and the spectral sequences are Part I's *Group Cohomology*, *Galois Cohomology* and *Spectral Sequences*, and the cup product and the duality pairing are *Sheaf Cohomology* and the Serre duality of *Sheaves in Algebraic Geometry*. The **étale** cohomology, in which the Galois representations of arithmetic are constructed and in which the Frobenius eigenvalues of the Weil conjectures live, is not part of this Part and is named with an explicit deferral; the reader meets it in the literature of *The Frobenius Operator*.

Throughout $k$ is a field, $L/k$ is a Galois extension with group $G$, $X$ is a variety over $k$, and $\mathcal{F}$ is a quasi-coherent sheaf on $X_L$ that is $G$-equivariant, with the descent datum $\alpha_\sigma : \sigma^*\mathcal{F}\to\mathcal{F}$ of *The Galois Action as an Operator*. The cohomology is written $H^i(X_L,\mathcal{F})$ and the invariants $H^i(X_L,\mathcal{F})^G$.

## The Galois Module of the Cohomology

### The Semilinear Action

**Definition.** A **semilinear $G$-module** over $L$ is an $L$-vector space $M$ with an action of $G$ by additive maps such that
$$
\sigma(\ell m) = \sigma(\ell)\,\sigma(m) \qquad (\sigma\in G,\ \ell\in L,\ m\in M);
$$
the action is $\sigma$-semilinear in each element. The **invariants** are the subspace
$$
M^G = \{m\in M : \sigma(m) = m \text{ for all } \sigma\in G\},
$$
which is a $k$-vector space.

**Theorem (the cohomology is a semilinear module).** For each $i\geq0$ the action of *The Galois Action as an Operator* endows the cohomology with the structure of a semilinear $G$-module over $L$,
$$
\sigma^* : H^i(X_L,\mathcal{F})\longrightarrow H^i(X_L,\mathcal{F}), \qquad \sigma^*(\ell v) = \sigma(\ell)\,\sigma^*(v),
$$
and the assignment $\sigma\mapsto\sigma^*$ is multiplicative, $(\sigma\tau)^* = \sigma^*\tau^*$.

*Proof.* This is the semilinear action of *The Galois Action as an Operator*, applied to the cohomology of a $G$-equivariant sheaf; the semilinearity is the semilinearity of the action on the structure sheaf, which the functoriality of the cohomology inherits, and the multiplicativity is the functoriality of the pullback.

**Remark (the module structure is not linear).** The action is not $L$-linear unless $G$ acts trivially on the coefficients, so the cohomology is not a representation of $G$ in the strict sense over $L$; it is a representation of $G$ in the semilinear sense. This is the same phenomenon as the operator-level semilinearity, now read on the elements, and it is the reason the invariant subspace is taken with respect to the twisted action and is only a $k$-space.

### The Twisted Representation

**Definition.** A **twisted representation** of $G$ over $L$ is a semilinear $G$-module; when a coefficient field $E$ with a linear $G$-action is available and the twist is absorbed, the module $M$ is an $E$-linear representation of $G$, called a **Galois representation**. Concretely, if $\mathcal{F}$ is a sheaf of $E$-modules over $E$ where $G$ acts $E$-linearly and $\mathcal{F}$ is $G$-equivariant, then $H^i(X_L,\mathcal{F})$ is an $E$-linear $G$-module.

**Proposition (the coefficients that linearise the action).** The structure sheaf has the semilinear action with the twist by $G$ on $L$; a constant sheaf with a linear $G$-action over a field on which $G$ acts trivially has a linear one. The passage from the semilinear to the linear is the choice of coefficients, and the two agree when the extension is trivial.

*Proof.* The action on $H^i(X_L,\mathcal{O}_{X_L})$ is semilinear by the theorem above. For a constant sheaf of $E$-modules with $L\hookrightarrow E$ and $G$ acting $E$-linearly, the twist is absorbed by the moduli of the action on the coefficients, and the resulting action is $E$-linear; when $L=k$ the twist is trivial and the two notions coincide.

**Example (the Galois representation of the arithmetic).** For $k$ a number field and $E=\mathbb{Q}_\ell$ the $\ell$-adic cohomology $H^i_{\mathrm{ét}}(X_{\bar k},\mathbb{Q}_\ell)$ carries a continuous $\mathbb{Q}_\ell$-linear action of the absolute Galois group, a Galois representation unramified outside a finite set when $X$ is smooth and proper and of the expected weight when $X$ has good reduction; this is the representation of the arithmetic, and its construction is the deferred étale theory.

## The Invariants

### The Invariant Cohomology

**Theorem (the invariants are the cohomology of the descended variety).** Let $X$ be a variety over $k$, let $L/k$ be a finite Galois extension with group $G$, and let $\mathcal{F}$ be a $G$-equivariant quasi-coherent sheaf on $X_L$ descended from a sheaf $\mathcal{F}_0$ on $X$. Then for every $i$
$$
H^i(X_L,\mathcal{F})^G\ \cong\ H^i(X,\mathcal{F}_0),
$$
the invariants of the semilinear action are the cohomology of the descended sheaf.

*Proof.* For the structure sheaf this is the invariant-cohomology theorem of *The Galois Action as an Operator*, proved by the Čech complex of a $G$-stable affine cover with the action on the coefficients; the general sheaf is handled by the same complex with coefficients in $\mathcal{F}_0$, whose invariants are the Čech complex of $\mathcal{F}_0$ by the descent of the module category in Part I's *Descent Theory*.

**Corollary (the trivial part and the higher parts).** The invariant subspace is the "trivial part" of the cohomology,
$$
H^i(X_L,\mathcal{F})^G = H^i(X_L,\mathcal{F})^{\mathrm{triv}} ,
$$
and it is exactly the image of the pullback $H^i(X,\mathcal{F}_0)\to H^i(X_L,\mathcal{F})$ when the pullback is injective. The cohomology of the descended variety thus sits inside the cohomology of the extension as the fixed elements, and the remaining elements are the higher cohomology of the group.

*Proof.* The identification of the invariants with $H^i(X,\mathcal{F}_0)$ is the theorem; the pullback lands in the invariants because it is the composite of the unit with an isomorphism, and it is injective when the Leray description is available, by the low-degree sequence of the next theorem.

### The Hochschild–Serre Spectral Sequence

**Theorem (the Hochschild–Serre spectral sequence).** Let $L/k$ be a Galois extension with group $G$ and let $\mathcal{F}$ be a $G$-equivariant quasi-coherent sheaf on $X_L$ descended from $\mathcal{F}_0$ on $X$. There is a spectral sequence of cohomological type
$$
E_2^{pq} = H^p\bigl(G,\ H^q(X_L,\mathcal{F})\bigr)\ \Longrightarrow\ H^{p+q}(X,\mathcal{F}_0),
$$
starting from the group cohomology of Part I's *Group Cohomology* with coefficients in the cohomology of the extension and converging to the cohomology of the descended variety.

*Proof.* The two functors are the global sections and the invariants under the action, and the composite of "take the $G$-invariants" with "take the global sections of $X_L$" is the global sections of $X$; the spectral sequence of the composite of two derived functors is the Grothendieck spectral sequence of Part I's *Spectral Sequences*, applied to the invariants functor and the global-sections functor of *Sheaf Cohomology*. The $E_2$ term is the group cohomology of $G$ with coefficients in the sheaf cohomology, computed on the same cover.

**Corollary (the low-degree exact sequence).** The five-term exact sequence of the spectral sequence is
$$
0\longrightarrow H^1\bigl(G,H^0(X_L,\mathcal{F})\bigr)\longrightarrow H^1(X,\mathcal{F}_0)\longrightarrow H^1(X_L,\mathcal{F})^G\longrightarrow H^2\bigl(G,H^0(X_L,\mathcal{F})\bigr)\longrightarrow H^2(X,\mathcal{F}_0),
$$
so that the failure of the invariants to compute the cohomology of the descended variety in degree one is detected by the group cohomology of the global sections in degree two.

*Proof.* The edge maps of the spectral sequence give the five-term sequence of Part I's *Spectral Sequences*, with the $E_2^{0,q}$ page the invariants by the previous theorem and the $E_2^{p,0}$ page the group cohomology.

**Example (the descent of the structure sheaf).** For $\mathcal{F}=\mathcal{O}_{X_L}$ the global sections are the coordinate ring $A\otimes_kL$ and the invariants are $A$, the group cohomology $H^1(G,A\otimes_kL)$ vanishes by Shapiro's lemma when $L/k$ is finite Galois, and the five-term sequence collapses: $H^1(X_L,\mathcal{O})^G\cong H^1(X,\mathcal{O})$. The higher terms survive when $G$ is infinite, which is the arithmetic case.

## Galois Representations

### Linear Coefficients and the Representation

**Definition.** A **Galois representation** of $G$ over a field $E$ is a finite-dimensional $E$-vector space $V$ with a continuous action of $G$ that is $E$-linear, $G$ carrying its profinite topology and $V$ its discrete topology when $E$ is discrete, or the natural topology of $E$ when $E$ is a local field.

**Theorem (the representation of the cohomology).** When the coefficients are $E$-modules with the linear action as in the proposition, the semilinear module $H^i(X_L,\mathcal{F})$ is a Galois representation, its invariants are the cohomology of the descended variety, and the representation is finite-dimensional when the cohomology is. The assignment is functorial in $\mathcal{F}$ and compatible with the long exact sequences and with the cup product.

*Proof.* The linearity is the proposition; the finite-dimensionality is the finiteness of the cohomology of a coherent sheaf on a projective variety by *Coherent Sheaves*, and the functoriality and the exactness are the functoriality of the cohomology and the naturality of the semilinear action.

### Weights and the Frobenius

**Remark (the arithmetic beyond the Part).** For a variety over a finite field and the $\ell$-adic coefficients, the Galois representation is unramified outside a finite set of places, the eigenvalues of the geometric Frobenius are the Weil numbers whose absolute values are the powers $q^{i/2}$ of *The Frobenius Operator*, and the representation is the object in which the Weil conjectures are stated. The construction of the representation, the weight filtration and the monodromy are the arithmetic of that article and of Part III, and this article records only the abstract representation and its invariants.

**Example (the cyclotomic representation).** For $X=\operatorname{Spec}k$ with $k$ a field containing the roots of unity, the cohomology of the structure sheaf is $k$ in degree zero, and the Galois action on the roots of unity $\mu_n$ of the example of *Real Structures on Varieties and Galois Descent* is the cyclotomic character $\chi : G\to(\mathbb{Z}/n)^\times$, $\sigma(\zeta)=\zeta^{\chi(\sigma)}$. This is the fundamental Galois representation from which the others are built, and its invariants recover the descended group $\mu_n^G$.

## The Involution and the Pairing

### The Action on the Cup Product

**Theorem (the action on the cup product).** The cup product of *Sheaf Cohomology*
$$
H^i(X_L,\mathcal{F})\times H^j(X_L,\mathcal{G})\longrightarrow H^{i+j}(X_L,\mathcal{F}\otimes\mathcal{G})
$$
is equivariant for the Galois action: for all $\sigma\in G$ and all classes $u,v$,
$$
\sigma^*(u\smile v) = \sigma^*(u)\smile\sigma^*(v).
$$
Consequently the action is by ring automorphisms of the graded ring $\bigoplus_iH^i(X_L,\mathcal{O}_{X_L})$ when it is defined, and the invariants form a subring, the cohomology ring of the descended variety.

*Proof.* The cup product is natural in the sheaves and in the morphisms, so the pullback of the composite sheaf map is the composite of the pullbacks; this is the compatibility of the semilinear action with the tensor product and the cup product, and it makes each $\sigma^*$ a ring homomorphism. The invariants are closed under the product by the equivariance, and they are the cohomology ring of $X$ by the invariant theorem.

### The Real Case

**Theorem (the eigenspaces of the conjugation).** Let $X$ be a variety over $\mathbb{R}$ and let $\sigma$ be the conjugation of $X_{\mathbb{C}}$. On each cohomology group of the structure sheaf the conjugation $\sigma^*$ is a **semilinear** involution of the $\mathbb{C}$-vector space,
$$
(\sigma^*)^2 = \mathrm{id}, \qquad \sigma^*(\lambda v) = \bar\lambda\,\sigma^*(v),
$$
and it decomposes the cohomology into the $(+1)$-eigenspace $H^i_+ = H^i(X_{\mathbb{C}},\mathcal{O})^\sigma$ and the $(-1)$-eigenspace $H^i_-$, both $\mathbb{R}$-subspaces with
$$
H^i(X_{\mathbb{C}},\mathcal{O}) = H^i_+\oplus H^i_-, \qquad H^i_- = i\,H^i_+, \qquad
H^i_+\cong H^i(X_{\mathbb{R}},\mathcal{O}), \qquad \dim_{\mathbb{C}}H^i(X_{\mathbb{C}},\mathcal{O}) = \dim_{\mathbb{R}}H^i_+ = \dim_{\mathbb{R}}H^i_- .
$$

*Proof.* The conjugation is an antilinear involution of $\mathcal{O}_{X_{\mathbb{C}}}$, so $\sigma^*$ is antilinear with $(\sigma^*)^2=\mathrm{id}$. Every $v$ is the sum of the fixed vector $\tfrac12(v+\sigma^*v)$ and the antifixed vector $\tfrac12(v-\sigma^*v)$, so the two eigenspaces span; they intersect in $0$ because a vector fixed and antifixed at once is $0$; and for a fixed $v$ the vector $iv$ satisfies $\sigma^*(iv) = -i\,\sigma^*(v) = -iv$, so $H^i_- = iH^i_+$ and the two $\mathbb{R}$-subspaces have the same real dimension, namely $\dim_{\mathbb{C}}H^i(X_{\mathbb{C}},\mathcal{O})$. The $(+1)$-eigenspace is the invariant subspace, identified with $H^i(X_{\mathbb{R}},\mathcal{O})$ by the invariant theorem.

**Theorem (the invariance of the duality pairing).** Let $X$ be smooth and proper of dimension $d$ over $k$, and let
$$
\langle-,-\rangle : H^i(X_L,\mathcal{O})\times H^{d-i}(X_L,\mathcal{O})\longrightarrow k
$$
be the Serre duality pairing of *Sheaves in Algebraic Geometry*. Then the pairing is semilinear for the Galois action,
$$
\langle\sigma u,\sigma v\rangle = \sigma\langle u,v\rangle ,
$$
so in the real case $\langle\sigma u,\sigma v\rangle = \overline{\langle u,v\rangle}$ and the pairing is invariant on the fixed classes. Consequently the $(+1)$ and $(-1)$ eigenspaces are orthogonal for the pairing, $H^i_+\perp H^{d-i}_-$, and the pairing restricts to a nondegenerate $\mathbb{R}$-bilinear form on $H^i_+\times H^{d-i}_+$ and on $H^i_-\times H^{d-i}_-$.

*Proof.* The duality pairing is natural in the structure sheaf, and the pullback of the pairing is the pairing of the pullbacks, with the action on the coefficient field: this is the semilinearity. For $u$ fixed and $v$ antifixed, $\langle u,v\rangle = \langle\sigma u,\sigma v\rangle = \langle u,-v\rangle = -\langle u,v\rangle$, so the pairing vanishes; for $u,v$ both fixed the value satisfies $\langle u,v\rangle = \overline{\langle u,v\rangle}$ and is real, and the nondegeneracy restricts because the pairing is nondegenerate on the whole and the eigenspaces are complementary.

*Proof.* The duality pairing is natural in the structure sheaf, and the pullback of the pairing is the pairing of the pullbacks; since the action on the base field $k$ is trivial in the real case, the pairing is invariant. The orthogonality of the eigenspaces is the elementary statement that an invariant pairing pairs opposite eigenspaces of an involution: $\langle u,v\rangle = \langle\sigma u,\sigma v\rangle = \pm\langle u,v\rangle$ for $u,v$ of the two eigenclasses forces the pairing to vanish unless the signs multiply to $1$.

## Summary

For a Galois extension $L/k$ with group $G$ and a $G$-equivariant sheaf $\mathcal{F}$ on $X_L$, the cohomology $H^i(X_L,\mathcal{F})$ is a **semilinear $G$-module** over $L$: the action satisfies $\sigma^*(\ell v) = \sigma(\ell)\sigma^*(v)$, and the invariants $H^i(X_L,\mathcal{F})^G$ are the cohomology $H^i(X,\mathcal{F}_0)$ of the descended variety. The comparison between the invariants and the cohomology is the **Hochschild–Serre spectral sequence**
$$
E_2^{pq} = H^p(G,H^q(X_L,\mathcal{F}))\ \Longrightarrow\ H^{p+q}(X,\mathcal{F}_0),
$$
whose five-term exact sequence begins with $0\to H^1(G,H^0)\to H^1(X,\mathcal{F}_0)\to H^1(X_L,\mathcal{F})^G\to H^2(G,H^0)\to H^2(X,\mathcal{F}_0)$. With coefficients that absorb the twist the semilinear module is a **Galois representation**, an $E$-linear continuous action, and the invariants are again the cohomology of the descended variety; in the arithmetic case the representation is unramified almost everywhere, its Frobenius eigenvalues are the Weil numbers of *The Frobenius Operator*, and the étale cohomology in which it is constructed is deferred. The cup product is equivariant, so the action is by ring automorphisms and the invariants form the cohomology ring of the descended variety; in the real case the involution splits each cohomology group into its $(+1)$ and $(-1)$ eigenspaces, with the $(+1)$-eigenspace the cohomology of the real variety and the $(-1)$-eigenspace its conjugate $iH^i_+$, and the duality pairing is semilinear, with the eigenspaces orthogonal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H^i(X_L,\mathcal{F})$ | cohomology of the base change; a semilinear $G$-module |
| $\sigma^*(\ell v)=\sigma(\ell)\sigma^*(v)$ | semilinearity of the Galois action on cohomology |
| $H^i(X_L,\mathcal{F})^G\cong H^i(X,\mathcal{F}_0)$ | the invariants are the cohomology of the descended variety |
| $H^p(G,H^q(X_L,\mathcal{F}))\Rightarrow H^{p+q}(X,\mathcal{F}_0)$ | the Hochschild–Serre spectral sequence |
| $0\to H^1(G,H^0)\to H^1(X)\to H^1(X_L)^G\to H^2(G,H^0)\to H^2(X)$ | the five-term exact sequence |
| Galois representation | a finite-dimensional $E$-linear continuous $G$-module |
| $\chi:G\to(\mathbb{Z}/n)^\times$, $\sigma(\zeta)=\zeta^{\chi(\sigma)}$ | the cyclotomic representation on $\mu_n$ |
| $\sigma^*(u\smile v)=\sigma^*u\smile\sigma^*v$ | equivariance of the cup product |
| $H^i(X_{\mathbb{C}})=H^i_+\oplus H^i_-$, $H^i_-=iH^i_+$ | the eigenspaces of the conjugation (semilinear) |
| $H^i_+\cong H^i(X_{\mathbb{R}},\mathcal{O})$ | the $(+1)$-eigenspace is the real cohomology |
| $\langle\sigma u,\sigma v\rangle=\overline{\langle u,v\rangle}$ | semilinearity of the Serre duality pairing |
| $H^i_+\perp H^i_-$ | the eigenspaces are orthogonal |
| $H^i_{\mathrm{ét}}(X_{\bar k},\mathbb{Q}_\ell)$ | étale cohomology, deferred; the arithmetic representation |

## Further Reading

- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the Galois action, the cohomology of a group and the descent of the invariants.
- James S. Milne, *Lectures on Étale Cohomology* (v4.02, 2013), for the Hochschild–Serre spectral sequence of a Galois cover and the Galois representations of the arithmetic.
- Alexander Grothendieck, *Sur quelques points d'algèbre homologique* (Tohoku Mathematical Journal 9, 1957), for the Grothendieck spectral sequence of a composite of derived functors.
- Michael Artin, *Grothendieck topologies* (Harvard University Lecture Notes, 1962), for the descent-theoretic form of the comparison of the cohomology of a cover.
- Jean-Louis Verdier, *Des catégories dérivées des catégories abéliennes* (Astérisque 239, 1996), for the derived-category form of the invariants and the spectral sequence.
- Jean-Pierre Serre and John Tate, *Good reduction of abelian varieties* (Annals of Mathematics 88, 1968), for the Galois representation on the cohomology of an abelian variety and its ramification.
