
# __Induced Representations of Locally Compact Groups__

## Introduction

**Induction** builds a representation of a group $G$ from a representation of a subgroup $H$, and it is the principal construction of the representation theory of a non-compact locally compact group: the principal series of a semisimple group, the Stone–von Neumann representations of the Heisenberg group, the representations of a group acting on a homogeneous space, and the spherical representations of a Gelfand pair are all induced. This article develops the construction in its two equivalent forms — the **induced representation** on a space of functions on $G$ and the **balanced-product** form, in which the representation space is the completion of $C_c(G) \otimes_{\mathbb{C}[H]} V$ — and proves the properties that make it useful: transitivity in stages, the universal property that identifies intertwiners out of an induced representation, the relation to restriction, and the realisation in the quasiregular case on $L^2(G/H)$.

The **boundary with Part III** is the same seam fixed in the companion article *Representation Theory of Locally Compact Groups*, and it is stated in the same words. The *induced representations* — their definition, their equivalence, their intertwiners, their tensor products, restriction, the imprimitivity theorem and the algebraic realisation as a balanced product — are the subject of this article . The **harmonic analysis** — the completion $L^2(G)$, the convolution algebra $L^1(G)$ and its $C^*$-completion, the Peter–Weyl theorem, the Plancherel theorem, the direct-integral decomposition of an induced representation and the explicit analysis of the standard examples — belongs to *Analysis on Groups* in Part III, where the measure and the limit are available. In particular the *completions* of the function spaces below, and the identification of the induced representation with a representation on an $L^2$ space, require the $L^2$ theory of Part III; the article works with the dense algebraic subspace of continuous compactly supported functions and states the completion as part of the deferred analysis.

The conventions are those of the companion articles: $G$ is a locally compact group written multiplicatively, $H$ a closed subgroup, $dg$ and $dh$ the Haar measures of *Locally Compact Groups and Haar Measure* with the modular functions $\Delta_G, \Delta_H$, $\operatorname{Irr}(G)$ the unitary dual of *Representation Theory of Locally Compact Groups*, and $\pi, V$ a unitary representation. The balanced product $\otimes_{\mathbb{C}[H]}$ is the algebraic tensor product over the group algebra, as in *The Balanced Product over an Algebra* and *Morita Equivalence*, and the induced representation is its unitary completion. The measure on a homogeneous space and the cocycle of a quasi-invariant measure are those of *Locally Compact Groups and Haar Measure*, §Quotients and Homogeneous Spaces. No physics is invoked.

## Motivating Cases

Before the definitions, three cases show what the construction must produce.

**Example (a character of a subgroup of a finite group).** Let $G$ be finite, $H \leq G$, and let $\chi$ be a one-dimensional representation of $H$. The representation of $G$ **induced** from $\chi$ acts on the space of functions $f : G \to \mathbb{C}$ with $f(gh) = \chi(h)^{-1}f(g)$ for all $h \in H$, by $(g \cdot f)(x) = f(g^{-1}x)$. Its dimension is $[G : H]$, its character at $g \in G$ is

$$
\chi^G(g) = \frac{1}{|H|}\sum_{x \in G,\ x^{-1}gx \in H} \chi(x^{-1}gx) ,
$$

and the construction is the one of *Representations of Groups*, §Induction, Restriction and Frobenius Reciprocity, where Frobenius reciprocity is proved for finite groups. The present article generalises that construction to a locally compact group, the sum over the finite index set being replaced by an integral over the homogeneous space.

**Example (the principal series of $SL_2(\mathbb{R})$).** Let $G = SL_2(\mathbb{R})$ and let $H = B$ be the Borel subgroup of upper triangular matrices, a closed subgroup whose quotient $G/B$ is the projective line $\mathbb{RP}^1$, a compact homogeneous space. A unitary character $\chi$ of $B$ induces a representation of $G$ on a space of functions on $\mathbb{RP}^1$; these are the **principal series** representations, and they are exactly the unitary representations of $SL_2(\mathbb{R})$ that are not discrete series or complementary series. The induction is the source of the continuous part of the unitary dual, and the identification of all irreducibles as constituents of induced representations is the content of the classification of *Representation Theory of Locally Compact Groups*, §The General Case and the Unitary Dual.

**Example (the Heisenberg group).** For the Heisenberg group $N$ with centre $Z$, the Stone–von Neumann representations $\pi_\lambda$ are the representations induced from a nontrivial unitary character of an abelian subgroup $M = Z\times A$, where $A$ is a one-parameter subgroup and $M$ is maximal abelian in $N$; their realisation on the square-integrable functions of the line — an object of Part III, quoted here as the classical Schrödinger model — is the standard presentation of a **monomial** representation, one induced from a character. Kirillov's orbit method describes every irreducible unitary representation of a nilpotent Lie group as monomial, and Mackey's theory extends the statement to a large class of groups.

## The Definition of an Induced Representation

### The Function-Space Realisation

**Definition.** Let $G$ be a locally compact group, $H$ a closed subgroup, and $(\sigma, V)$ a unitary representation of $H$ on a Hilbert space $V$. A function $f : G \to V$ is **$H$-equivariant of type $\sigma$** if

$$
f(gh) = \sigma(h)^{-1}f(g) \qquad \text{for all } g \in G,\ h \in H .
$$

The induced representation, in its **function-space realisation**, is the action of $G$ on a space of such functions by left translation:

$$
\bigl(\operatorname{Ind}_H^G \sigma\bigr)(g)\, f(x) = f(g^{-1}x) .
$$

The action preserves the equivariance condition: $f(g^{-1}xh) = \sigma(h)^{-1}f(g^{-1}x)$. The space on which the unitary operator acts is the completion, in the norm below, of the continuous compactly supported $H$-equivariant functions; the completion is deferred to the analysis of Part III, and the dense algebraic subspace is used throughout.

**Theorem (the induced inner product).** Let $H$ be a closed subgroup of $G$ and $\sigma$ a unitary representation of $H$ on $V$. If $\Delta_G|_H = \Delta_H$ there is a $G$-invariant Radon measure $\nu$ on $G/H$, and

$$
\langle f_1, f_2\rangle = \int_{G/H} \langle f_1(g), f_2(g)\rangle_V\; d\nu(gH)
$$

is a $G$-invariant inner product on the continuous $H$-equivariant functions of type $\sigma^{-1}$ with compact support modulo $H$. In general one replaces $\sigma$ by the **normalised** representation $\tilde\sigma(h) = \bigl(\Delta_G(h)/\Delta_H(h)\bigr)^{1/2}\sigma(h)$ and takes for $\nu$ the quasi-invariant measure on $G/H$ of *Locally Compact Groups and Haar Measure*, §Quotients and Homogeneous Spaces, normalised once and for all; with the type $\tilde\sigma^{-1}$ the same formula is again a $G$-invariant inner product. In either case the integrand is well defined, because for $h \in H$

$$
\langle f_1(gh), f_2(gh)\rangle_V = \langle \sigma(h)^{-1}f_1(g), \sigma(h)^{-1}f_2(g)\rangle_V = \langle f_1(g), f_2(g)\rangle_V ,
$$

$\sigma(h)$ being unitary; and $\operatorname{Ind}_H^G\sigma$ is unitary for this inner product once the completion is taken.

**Proof.** The computation just made shows that the integrand is constant along the right cosets of $H$, so it descends to $G/H$ and the integral is defined. For $g_0 \in G$,

$$
\langle g_0\cdot f_1, g_0\cdot f_2\rangle = \int_{G/H}\langle f_1(g_0^{-1}g), f_2(g_0^{-1}g)\rangle_V\, d\nu(gH) = \int_{G/H}\langle f_1(g), f_2(g)\rangle_V\, d(g_0\cdot\nu)(gH) ,
$$

so invariance of the inner product is exactly invariance of $\nu$; this is the case $\Delta_G|_H = \Delta_H$ by the criterion of *Locally Compact Groups and Haar Measure*, §Quotients and Homogeneous Spaces. In the general case the Radon–Nikodym factor contributed by the quasi-invariant $\nu$ is compensated by the half-density factor in $\tilde\sigma$, which is the standard computation of the space of half-densities; the two normalisations agree when the criterion holds, since then $\Delta_G|_H = \Delta_H$ and $\tilde\sigma = \sigma$. Changing $\nu$ to an equivalent quasi-invariant measure multiplies the inner product by a positive continuous density and does not change the unitary equivalence class of the induced representation. $\square$

**Remark.** The previous proof is the one place where the modular functions enter the construction. The standard convention, followed here, is to induce from the normalised representation $\tilde\sigma$, so that the induced inner product is genuinely invariant; the article states the results for $\sigma$ and notes where the normalisation is required. When $\Delta_G|_H = \Delta_H$ — in particular when $G$ is unimodular, and in particular for a compact $H$ — no normalisation is needed and $\sigma$ may be induced as it stands.

### The Balanced-Product Realisation

**Definition.** Let $C_c(G)$ denote the continuous compactly supported functions on $G$. It is a right $\mathbb{C}[H]$-module under $(f \cdot h)(g) = f(gh)$, and a left $\mathbb{C}[G]$-module under left translation; the two structures make it a $(\mathbb{C}[G], \mathbb{C}[H])$-bimodule, and $V$ is a left $\mathbb{C}[H]$-module through $\sigma$. The **balanced product**

$$
C_c(G) \otimes_{\mathbb{C}[H]} V
$$

is the quotient of the tensor product $C_c(G)\otimes_{\mathbb{C}} V$ by the relations $f \otimes \sigma(h)v = (f \cdot h) \otimes v$ for $h \in H$. Left translation of the first factor makes it a left $\mathbb{C}[G]$-module, hence a representation of $G$; when a half-density normalisation is in force it is applied to the second factor, replacing $\sigma$ by $\tilde\sigma$. The result is a representation of $G$, and the module structure $(f\cdot h)(g) = f(gh)$ is the one for which the relations are those of the equivariance condition below.

**Theorem (the two realisations agree).** There is a canonical isomorphism of $\mathbb{C}[G]$-modules between the balanced product and the space

$$
\bigl\{f : G \to V \text{ continuous, compactly supported mod } H,\ f(gh) = \sigma(h)^{-1}f(g)\bigr\}
$$

of $H$-equivariant functions of the function-space model, so that the two models define the same representation of $G$.

**Proof.** In the discrete model — $G$ discrete, so that $C_c(G) = \mathbb{C}[G]$ — the inverse isomorphism is $f \mapsto \sum_{x} \delta_x \otimes f(x)$, the sum over a set of coset representatives of $H$ in $G$: replacing $x$ by $xh$ with $h \in H$ replaces $\delta_x\otimes f(x)$ by $\delta_{xh}\otimes f(xh) = \delta_{xh}\otimes\sigma(h)^{-1}f(x) = (\delta_x\cdot h)\otimes\sigma(h)^{-1}f(x) = \delta_x\otimes f(x)$ by the balanced relation, so the sum is well defined, and the two constructions are plainly inverse and $\mathbb{C}[G]$-linear. For a general locally compact $G$ one replaces the sum by a partition of unity subordinate to a finite cover of the support modulo $H$, using local sections of $G \to G/H$ and the Haar functional on the compactly supported functions; the same computation of the balanced relations shows that the resulting element of the balanced product is independent of the choices. The universal property of the balanced product — an $H$-balanced bilinear map out of $C_c(G)\times V$ is a $\mathbb{C}[G]$-linear map out of the balanced product — then says that the balanced-product induction is left adjoint to restriction, $\operatorname{Hom}_H(V, W|_H)\cong\operatorname{Hom}_G\bigl(C_c(G)\otimes_{\mathbb{C}[H]}V, W\bigr)$, while the function-space induction is right adjoint to restriction in the form of the Frobenius reciprocity proved below. $\square$

**Remark.** The balanced-product form is the one that generalises beyond the unitary case: for a representation of $H$ on a module over a ring and a $G$-set $G/H$, the induction is the balanced product $R[G/H]\otimes_{R[H]}V$, which is the construction of *The Balanced Product over an Algebra*. The unitary theory adds the inner product and the completion.

## Basic Properties of Induction

### Transitivity in Stages

**Theorem (induction in stages).** Let $K \leq H \leq G$ be closed subgroups and let $\sigma$ be a unitary representation of $K$. Then there is a natural unitary equivalence

$$
\operatorname{Ind}_K^G \sigma \;\cong\; \operatorname{Ind}_H^G\bigl(\operatorname{Ind}_K^H \sigma\bigr) ,
$$

and the identification is given by composing the two function-space descriptions.

**Proof.** An element of the right side is a function $F : G \to \mathcal{H}_{\operatorname{Ind}_K^H\sigma}$ with $F(gh) = \bigl(\operatorname{Ind}_K^H\sigma\bigr)(h)^{-1}F(g)$ for $h \in H$; evaluating the inner function at the identity of $H$ gives the function $f(g) = F(g)(e)$ on $G$, and the two equivariance conditions together give $f(gk) = \sigma(k)^{-1}f(g)$ for $k \in K$, so $f$ represents an element of $\operatorname{Ind}_K^G\sigma$. Conversely an element $f$ of $\operatorname{Ind}_K^G\sigma$ defines $F(g)(\cdot)$ by $h \mapsto f(gh)$, and the $H$-equivariance computed above holds. The two constructions are inverse and commute with the left translations of $G$, hence give a unitary equivalence. $\square$

**Corollary.** If $H = G$ then $\operatorname{Ind}_G^G\sigma \cong \sigma$; if $H = \{e\}$ and $\sigma$ is the trivial representation of the trivial group then $\operatorname{Ind}_{\{e\}}^G 1 = \lambda_G$, the left regular representation of $G$ on functions on $G$, whose completion is the object studied in Part III.

### Frobenius Reciprocity

The fundamental relation between induction and restriction is the adjunction between the two functors.

**Theorem (Frobenius reciprocity).** Let $H \leq G$ be closed subgroups, $\sigma$ a unitary representation of $H$ and $\pi$ a unitary representation of $G$. There is a natural isomorphism of vector spaces

$$
\operatorname{Hom}_G\bigl(\pi, \operatorname{Ind}_H^G\sigma\bigr) \;\cong\; \operatorname{Hom}_H\bigl(\pi|_H, \sigma\bigr) ,
$$

where $\operatorname{Hom}_G$ and $\operatorname{Hom}_H$ denote spaces of intertwining operators. In the finite case with $\sigma$ one-dimensional this is the classical Frobenius reciprocity of *Representations of Groups*, and its character form is

$$
\langle \chi_\pi,\ \operatorname{Ind}_H^G\chi_\sigma\rangle_G = \langle \chi_\pi|_H,\ \chi_\sigma\rangle_H .
$$

**Proof.** Let $T \in \operatorname{Hom}_G(\pi, \operatorname{Ind}_H^G\sigma)$. For $v \in \mathcal{H}_\pi$ the function $Tv : G \to \mathcal{H}_\sigma$ is continuous and $H$-equivariant; evaluation at the identity of $G$ defines $S : \mathcal{H}_\pi \to \mathcal{H}_\sigma$ by $Sv = (Tv)(e)$. For $h \in H$, using $G$-equivariance of $T$ and $H$-equivariance of the values,

$$
S(hv) = (T(hv))(e) = (h \cdot Tv)(e) = (Tv)(h^{-1}) = \sigma(h)(Tv)(e) = \sigma(h)Sv ,
$$

so $S \in \operatorname{Hom}_H(\pi|_H,\sigma)$; the map $T \mapsto S$ is linear. Conversely, given $S \in \operatorname{Hom}_H(\pi|_H,\sigma)$, define $(Tv)(g) = S(\pi(g)^{-1}v)$; then $Tv$ is continuous and compactly supported modulo $H$ when $v$ is in the dense subspace of $G$-finite vectors, and

$$
(Tv)(gh) = S(\pi(h)^{-1}\pi(g)^{-1}v) = \sigma(h)^{-1}S(\pi(g)^{-1}v) = \sigma(h)^{-1}(Tv)(g) ,
$$

so $Tv \in \operatorname{Ind}_H^G\sigma$; and $T$ interwines: $(T\pi(g_0)v)(g) = S(\pi(g)^{-1}\pi(g_0)v) = (Tv)(g_0^{-1}g) = (g_0\cdot Tv)(g)$. The two constructions are inverse, and the character form follows by taking traces in the finite case. $\square$

**Remark.** With the covariant (function-space) induction the adjunction $\operatorname{Hom}_G(\pi, \operatorname{Ind}_H^G\sigma)\cong\operatorname{Hom}_H(\pi|_H,\sigma)$ says that induction is *right* adjoint to restriction; the balanced-product form of induction, which realises the same representation, is *left* adjoint to restriction, $\operatorname{Hom}_H(V, W|_H)\cong\operatorname{Hom}_G(C_c(G)\otimes_{\mathbb{C}[H]}V, W)$. The two are dual statements and coincide for finite groups, where the induced module is both. For a fixed quasi-invariant measure the identification is independent of the measure, which is why the theory is stated with intertwiner spaces rather than with the representation spaces themselves.

### Restriction and Tensor Products

**Theorem (Mackey's restriction and tensor product formulas, statement).** Let $H_1, H_2 \leq G$ be closed subgroups and let $\sigma_i$ be representations of $H_i$.

**(a)** The restriction of $\operatorname{Ind}_{H_1}^G\sigma_1$ to $H_2$ is a direct sum, over the double cosets $H_2 \backslash G / H_1$, of representations induced from the stabilisers; for a double coset $s$, the corresponding constituent is induced from the representation of the subgroup $H_2 \cap sH_1s^{-1}$ obtained by conjugating and restricting $\sigma_1$.

**(b)** The tensor product of two induced representations is a direct sum of induced representations over the double cosets of $H_1 \backslash G/H_2$, with the constituents constructed from $\sigma_1 \otimes \sigma_2$ restricted and conjugated.

**(c)** If $H_1 = H_2 = H$ and $\sigma_1, \sigma_2$ are representations of $H$, then $\operatorname{Ind}_H^G\sigma_1 \otimes \operatorname{Ind}_H^G\sigma_2$ is a direct sum over the double cosets, and $\operatorname{Ind}_H^G\sigma_1$ is irreducible if and only if $\sigma_1$ is irreducible and the double coset space has the appropriate structure.

**Pro.** For (a) the space of $\operatorname{Ind}_{H_1}^G\sigma_1$ decomposes according to the orbits of $H_2$ on $G/H_1$, which are the double cosets; an element of an orbit is written $s$ for a representative, and the stabiliser of the coset $sH_1$ in $H_2$ is $H_2 \cap sH_1s^{-1}$, whose representation is $\sigma_1^s$; the orbit contribution is the induction of that representation to $H_2$ by transitivity of induction. For (b) and (c) one uses the identity $\operatorname{Ind}_{H_1}^G\sigma_1\otimes\operatorname{Ind}_{H_2}^G\sigma_2 \cong \operatorname{Ind}_{H_1\times H_2}^{G\times G}(\sigma_1\boxtimes\sigma_2)$ restricted to the diagonal, together with (a); the details are the **Mackey machine**, and they are not covered here. The statements are recorded here for the induced representations of a locally compact group; the finite versions are those of *Representations of Groups*, §Induction, Restriction and Frobenius Reciprocity, and the proofs there specialise from the present ones. $\square$

### Induction and the Quasiregular Representation

**Definition.** Let $H \leq G$ be a closed subgroup and let $1_H$ be the trivial one-dimensional representation of $H$. The **quasiregular representation** of $G$ on $G/H$ is

$$
\lambda_{G/H} = \operatorname{Ind}_H^G 1_H ,
$$

the action of $G$ by left translation on functions on $G/H$.

**Theorem.** $G/H$ carries a $G$-invariant Radon measure precisely when $\Delta_G|_H = \Delta_H$, by *Locally Compact Groups and Haar Measure*, §Quotients and Homogeneous Spaces. When it does, the quasiregular representation is the natural action of $G$ on the completion of $C_c(G/H)$ in the invariant norm, and the constant function $1$ is an invariant vector; the quasiregular representation therefore contains the trivial representation as a subrepresentation, and the invariant vector is unique up to scale. When $G/H$ has finite invariant volume, $1$ is in the Hilbert space and the trivial representation is a direct summand.

**Proof.** The invariant measure exists by the criterion of *Locally Compact Groups and Haar Measure*; in the function-space model of induction the space consists of functions on $G$ constant on the right cosets of $H$, which is $C_c(G/H)$. The constant function satisfies $f(gh) = f(g)$, is fixed by left translation and has $\|1\|^2 = \operatorname{vol}(G/H)$; it lies in the Hilbert space exactly when the volume is finite. Uniqueness of the invariant vector is the constancy of a function fixed by a transitive action. $\square$

**Example (the sphere and the orthogonal group).** For $G = SO(n+1)$ and $H = SO(n)$ the space $G/H$ is the unit sphere $S^n$, and the quasiregular representation on $L^2(S^n)$ is the classical decomposition of *Symmetric Tensors and Spherical Harmonics*: the irreducible constituents of $\operatorname{Ind}_{SO(n)}^{SO(n+1)}1$ are the spaces of spherical harmonics of degree $k$, each of which is an irreducible representation of $SO(n+1)$ occurring once. The irreducibility of each copy and the multiplicity-free decomposition are the content of the theory of Gelfand pairs, stated below; the analytic decomposition into spherical harmonics is that of *Symmetric Tensors and Spherical Harmonics* and in Part III.

### Multiplicity-Free Induction and Gelfand Pairs

**Definition.** A pair $(G, K)$ with $K \leq G$ compact is a **Gelfand pair** if the algebra of $K$-bi-invariant continuous compactly supported functions on $G$ is commutative under convolution. Equivalently, the quasiregular representation $\operatorname{Ind}_K^G 1_K$ is multiplicity-free: every irreducible unitary representation of $G$ occurs in it with multiplicity at most one.

**Theorem.** For a Gelfand pair $(G, K)$:

**(a)** the induced representation $\operatorname{Ind}_K^G 1_K$ is multiplicity-free — no irreducible occurs in it more than once; when $G$ is compact the decomposition is a direct sum of pairwise inequivalent irreducibles, each occurring once, and in general the decomposition is the direct integral over the spherical dual that belongs to the harmonic analysis of Part III;

**(b)** an irreducible unitary representation $\pi$ of $G$ occurs in $\operatorname{Ind}_K^G1_K$ if and only if $\pi$ has a nonzero $K$-fixed vector, which is then unique up to scale;

**(c)** the spherical functions — the $K$-bi-invariant matrix coefficients $g \mapsto \langle \pi(g)v, v\rangle$ with $v$ a $K$-fixed unit vector — are simultaneous eigenfunctions of the convolution algebra, and they are indexed by the irreducibles occurring;

**(d)** the pair $(G, K)$ is a Gelfand pair if and only if the algebra of $K$-bi-invariant functions is commutative, and for a symmetric pair $(G, K)$ this holds because every $K$-bi-invariant function is invariant under the involution $g \mapsto g^{-1}$.

**Proof.** (a) and (b) are read off from Frobenius reciprocity: the multiplicity of an irreducible $\pi$ in $\operatorname{Ind}_K^G1_K$ is $\dim\operatorname{Hom}_G(\pi, \operatorname{Ind}_K^G1_K) = \dim\operatorname{Hom}_K(\pi|_K, 1_K) = \dim\mathcal{H}_\pi^K$, the dimension of the space of $K$-fixed vectors, and the quasiregular representation is multiplicity-free exactly when this dimension is at most one for every irreducible, which is the standard criterion for $(G,K)$ to be a Gelfand pair. In particular (b) holds, the $K$-fixed vector being unique up to scale. (c) The bi-invariance and the eigenfunction property are checked by a change of variables in the convolution. (d) The commutativity is the defining condition; for a symmetric pair the involution inverts $g$ and acts on the bi-invariant algebra as the identity, forcing commutativity. The harmonic-analytic consequences — the explicit decomposition and the convergence of the spherical expansion — are Part III. $\square$

**Example.** $(SO(n+1), SO(n))$ with $G/K = S^n$; $(SL_2(\mathbb{R}), SO(2))$ with $G/K$ the hyperbolic plane, where the spherical functions are the Legendre functions; $(G, K)$ with $G$ a compact group and $K$ a maximal torus, where the spherical functions are the characters of the highest-weight theory.

## Induction in the Abelian and Compact Cases

**Example (abelian groups and the Fourier transform).** Let $G$ be locally compact abelian and $H \leq G$ a closed subgroup. Every irreducible unitary representation of $G$ is a character, and the irreducibles occurring in $\operatorname{Ind}_H^G\chi$ are those characters of $G$ whose restriction to $H$ is $\chi$. In the Pontryagin-dual picture of *Pontryagin Duality*, the dual $H^\vee = G^\vee/H^\perp$ sits inside $G^\vee$, and

$$
\operatorname{Ind}_H^G\chi \;\longleftrightarrow\; \text{the characters of } G \text{ lying over } \chi ,
$$

a coset of $H^\perp$ in $G^\vee$. In particular $\operatorname{Ind}_{\{e\}}^G1_{\{e\}}$ corresponds to the whole dual $G^\vee$, and the decomposition of the regular representation into characters is the Fourier inversion theorem of Part III. The general theory of this article is therefore the non-abelian replacement for the trivial statement that a character of $G$ restricts to a character of $H$.

**Example (compact groups and the Weyl character formula).** Let $K$ be a compact connected Lie group, $T$ a maximal torus and $B$ a Borel subgroup containing $T$; the irreducibles of $K$ are the constituents of $\operatorname{Ind}_T^K\chi$ and of $\operatorname{Ind}_B^{K_{\mathbb{C}}}\chi$ for dominant characters $\chi$ of $T$. The Weyl character formula computes the character of the induced representation and shows that the induced representation has a unique highest-weight constituent when $\chi$ is dominant regular, namely the irreducible of that highest weight; the remaining constituents are lower. This gives the Borel–Weil–Bott realisation of the irreducible representations as cohomology of line bundles on the flag variety $K/T$, an instance of the correspondence between induced representations and vector bundles on homogeneous spaces.

**Example (finite groups and the Littlewood–Richardson theory).** For finite $G$ and $H$, induction is the finite construction, and the symmetric group case $G = S_n$, $H = S_{n-1}$ or the Young subgroup gives the branching and Pieri rules of *Symmetric Functions and Schur Functions* and *Symmetric Tensors and Spherical Harmonics*; the multiplicity-free cases are the Gelfand pairs, of which $(S_n, S_{n-1})$ is the basic example with the decomposition by the branching rule for Young diagrams.

## The Boundary with Analysis

- The **completion** of the induced space in the invariant norm, the identification with a space of $L^2$ sections of a Hilbert bundle over $G/H$, and the measurability of the equivariant functions are part of the $L^2$ theory of Part III, beginning.
- The **direct-integral decomposition** of an induced representation, the **Plancherel formula** for a semisimple group and the explicit decomposition of the quasiregular representation are *Analysis on Groups* in Part III.
- The **Mackey machine**, the imprimitivity theorem and the classification of the irreducibles of a group with a normal subgroup are not covered here; the present article supplies the induction construction on which that theorem is built.
- What is *not* deferred: the induction construction, its two realisations, transitivity in stages, Frobenius reciprocity, the quasiregular representation and the Gelfand-pair statements are developed here, and are used in the representation theory of the group-theoretic articles throughout.

## Summary

Induction builds a unitary representation $\operatorname{Ind}_H^G\sigma$ of $G$ from a unitary representation $\sigma$ of a closed subgroup $H$. In the function-space realisation the space consists of the continuous compactly supported functions $G \to V$ with $f(gh) = \sigma(h)^{-1}f(g)$, acted on by left translation; in the balanced-product realisation it is $C_c(G)\otimes_{\mathbb{C}[H]}V$, and the two agree. The inner product is the invariant integral over $G/H$ with respect to a quasi-invariant measure, with the half-density normalisation by the modular functions when $G$ and $H$ are not unimodular.

The principal properties are: induction in stages, $\operatorname{Ind}_K^G\sigma \cong \operatorname{Ind}_H^G(\operatorname{Ind}_K^H\sigma)$; Frobenius reciprocity, $\operatorname{Hom}_G(\pi, \operatorname{Ind}_H^G\sigma) \cong \operatorname{Hom}_H(\pi|_H, \sigma)$, the adjunction of induction and restriction; the restriction and tensor-product formulas over double cosets, which are the Mackey machine; and the quasiregular representation $\operatorname{Ind}_H^G1_H$ on $G/H$, whose invariant measure exists exactly when the modular functions agree. For a Gelfand pair $(G,K)$ the quasiregular representation is multiplicity-free, an irreducible occurs exactly when it has a nonzero $K$-fixed vector, and the spherical functions are the joint eigenfunctions of the commutative convolution algebra.

In the abelian case induction corresponds to passing to a coset of $H^\perp$ in the Pontryagin dual, and the decomposition of $\operatorname{Ind}_{\{e\}}^G1$ is Fourier inversion; in the compact case the irreducibles are the constituents of inductions from a maximal torus, computed by the Weyl character formula. The completion in the invariant norm, the direct-integral decomposition and the Plancherel theory are *Analysis on Groups* in Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $H$, $K$ | Locally compact groups, $H, K \leq G$ closed subgroups |
| $\sigma, V$ | Unitary representation of $H$ and its Hilbert space |
| $\operatorname{Ind}_H^G\sigma$ | Representation of $G$ induced from $\sigma$ |
| $f(gh) = \sigma(h)^{-1}f(g)$ | Equivariance condition of the function-space model |
| $C_c(G)\otimes_{\mathbb{C}[H]}V$ | Balanced-product model of the induced representation |
| $dg$, $dh$, $d\nu$ | Haar measures on $G$, $H$ and the quasi-invariant measure on $G/H$ |
| $\Delta_G, \Delta_H$ | Modular functions; $(\Delta_G/\Delta_H)^{1/2}$ is the half-density normalisation |
| $\operatorname{Hom}_G$, $\operatorname{Hom}_H$ | Intertwining operators over $G$ and over $H$ |
| Frobenius reciprocity | $\operatorname{Hom}_G(\pi, \operatorname{Ind}_H^G\sigma)\cong \operatorname{Hom}_H(\pi|_H,\sigma)$ |
| $\pi|_H$ | Restriction of a representation of $G$ to $H$ |
| $\lambda_{G/H} = \operatorname{Ind}_H^G1_H$ | Quasiregular representation on $G/H$ |
| Gelfand pair $(G,K)$ | $\operatorname{Ind}_K^G1_K$ is multiplicity-free |
| spherical function | $K$-bi-invariant matrix coefficient $\langle\pi(g)v,v\rangle$, $v$ a $K$-fixed unit vector |
| $H_2\backslash G/H_1$ | Double cosets indexing Mackey's restriction and tensor-product formulas |
| $L^2(G/H)$, $L^1(G)$ | Part III objects: completions and convolution |









## Further Reading

- George W. Mackey, *The Theory of Unitary Group Representations* (University of Chicago Press, 1976), for induced representations and the imprimitivity theorem.
- George W. Mackey, *Unitary Group Representations in Physics, Probability, and Number Theory* (Benjamin, 1978), for the classical account of the construction and its applications.
- David A. Vogan, *Unitary Representations of Reductive Lie Groups* (Princeton University Press, 1987), for the classification of the unitary dual via induction.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for induction in the locally compact setting and Frobenius reciprocity.
- Robert J. Blattner, *Induced Representations* (Benjamin, 1972), for the function-space and bundle models.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the principal series and the Borel–Weil theorem.
- Serge Lang, *$SL_2(\mathbb{R})$* (Springer, 1975; reprinted 1998), for the principal, discrete and complementary series in detail.
- V. S. Varadarajan, *An Introduction to Harmonic Analysis on Semisimple Lie Groups* (Cambridge University Press, 1999), for the spherical function theory of Gelfand pairs.
- François Digne and Jean Michel, *Representations of Finite Groups of Lie Type* (Cambridge University Press, 2nd ed. 2020), for Harish-Chandra induction and the algebraic theory of induced representations.
- Nolan R. Wallach, *Real Reductive Groups I* (Academic Press, 1988), for induced representations of reductive Lie groups and their classification.
- Joseph A. Wolf, *Harmonic Analysis on Commutative Spaces* (American Mathematical Society, 2007), for Gelfand pairs and multiplicity-free induction.
