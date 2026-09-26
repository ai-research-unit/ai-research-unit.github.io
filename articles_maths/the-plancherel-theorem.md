
# __The Plancherel Theorem__

## Introduction

The Plancherel theorem is the statement that the Fourier transform on a unimodular group of type I is an isometry of the group as a measure space onto its dual as a measure space. For the line it is the classical identity $\int_{\mathbb{R}}|f(x)|^2dx = \int_{\mathbb{R}}|\hat f(\xi)|^2d\xi$; for the circle it is Parseval's identity; for a compact group it is the statement that the square of the $L^2$ norm is the sum of the squared Hilbert–Schmidt norms of the Fourier transforms weighted by the dimensions; and for a general unimodular group of type I it is the assertion that there is a measure $\mu_P$ on the unitary dual with respect to which the regular representation is a direct integral of the irreducible representations and the operator-valued transform is unitary. That measure is the **Plancherel measure**, and its existence, uniqueness and explicit computation are the content of the theory.

The article states the theorem in its definite and isometric forms, gives the construction of the measure from the trace of the regular representation and Dixmier's abstract theorem, verifies the normalisation in the abelian, compact and finite cases where it reduces to facts already established in this category, and computes the measure in the standard non-compact examples: the Heisenberg group, where the density is $|\lambda|$; the semisimple groups, where the Harish-Chandra formula governs the continuous part and the discrete series contributes point masses; and the nilpotent groups, where the orbit method produces the measure as the pushforward of Lebesgue measure on the coadjoint orbits. It closes with the two ways in which the theorem can fail: the modification required for non-unimodular groups and the total failure for groups that are not of type I.

The boundaries. The **operator-valued transform**, the coefficient algebra and the general decomposition theory are *Noncommutative Harmonic Analysis*; the **convolution algebra** and its completions are *The Convolution Algebra $L^1(G)$*; the **abelian** transform and its inversion and Plancherel theorems are *Harmonic Analysis on Groups*; the **compact** transform and its orthogonality relations are *Analysis on Compact Groups*, and the decomposition theorem behind it is *The Peter–Weyl Theorem*. The **unitary dual, the type I property, the Borel structure of the dual and the uniqueness of the direct-integral decomposition** are Part II's *Type I Groups*, and the **Haar measure and the modular function** are *Locally Compact Groups and Haar Measure*. The functional analysis — the trace-class and Hilbert–Schmidt ideals, the spectral theorem, the polar decomposition — is standard and is quoted as it is used, with the operator-algebraic part belonging to *Operator Algebras* and the space theory to the later; the integration is *Measure Theory and Integration*. No physics is invoked.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$, modular function $\Delta$, identity $e$; the operator-valued transform is $\hat f(\pi) = \int_G f(g)\pi(g)\,dg$; the unitary dual is $\operatorname{Irr}(G)$; the Plancherel measure is $\mu_P$; and the group von Neumann algebra is $L(G) = \lambda(G)''$. The convolution and involution are those of *The Convolution Algebra $L^1(G)$*, and the direct-integral notation is that of *Noncommutative Harmonic Analysis*. The abelian dual is $G^\vee$; the hat is not used for a dual.

## The Plancherel Formula

### The Definite Form and the Isometry

**Definition.** A locally compact group $G$ is **Plancherel** (or satisfies the Plancherel theorem) if it is unimodular and of type I.

**Theorem (Plancherel).** Let $G$ be a second countable unimodular group of type I. There is a unique Radon measure $\mu_P$ on the unitary dual $\operatorname{Irr}(G)$, the **Plancherel measure**, such that for all $f, h \in L^1(G)\cap L^2(G)$

$$
\int_{\operatorname{Irr}(G)} \operatorname{Tr}\bigl(\hat f(\pi)\,\hat h(\pi)^*\bigr)\,d\mu_P(\pi) \;=\; \int_G f(g)\,\overline{h(g)}\,dg ,
$$

where the trace is the ordinary trace on the finite-rank operators and $\hat f(\pi)\hat h(\pi)^*$ is trace class. Taking $h = f$ gives the **isometric form**

$$
\int_{\operatorname{Irr}(G)} \bigl\|\hat f(\pi)\bigr\|_{\mathrm{HS}}^2\,d\mu_P(\pi) \;=\; \int_G |f(g)|^2\,dg ,
$$

and taking $h$ to be an approximate identity concentrated at $e$ and passing to the limit gives the **definite form**

$$
f(e) = \int_{\operatorname{Irr}(G)} \operatorname{Tr}\bigl(\hat f(\pi)\bigr)\,d\mu_P(\pi) ,
$$

valid for $f$ in the coefficient algebra for which the integral converges absolutely.

**Proof sketch.** The theorem is proved by first establishing the definite form for a suitable dense algebra of functions and then polarising. Let $\mathcal{A} \subseteq L^1(G)\cap L^2(G)$ be the coefficient algebra, the span of the matrix coefficients of the finite-dimensional representations together with the functions $f*h^*$. For $f, h \in \mathcal{A}$, the operators $\hat f(\pi), \hat h(\pi)$ are Hilbert–Schmidt for $\mu_P$-almost every $\pi$ and their product $\hat f(\pi)\hat h(\pi)^*$ is trace class; the function $\pi \mapsto \operatorname{Tr}(\hat f(\pi)\hat h(\pi)^*)$ is Borel and integrable with respect to the measure constructed below, and its integral is a positive-definite bilinear form on $\mathcal{A}$ dominated by the $L^2$ inner product. The isometry then follows from the identification of the two inner products, and the extension to $L^2(G)$ is by density and completeness. The construction of $\mu_P$ is the subject of the next section and is Dixmier's theorem. $\square$

**Remark (the definite form determines everything).** The definite form is the primitive statement: it says that the delta mass at the identity, regarded as a distribution on the coefficient algebra, is the integral of the character distributions $\operatorname{Tr}\pi$ against $\mu_P$. Equivalently, in the distributional sense on the group,

$$
\int_{\operatorname{Irr}(G)} \chi_\pi(g)\,d\mu_P(\pi) = \delta_e(g),
$$

where $\chi_\pi(g) = \operatorname{Tr}\pi(g)$ is the (possibly distributional, for infinite-dimensional $\pi$) character. For a compact group this is the completeness of the characters at the identity, $\sum_\pi d_\pi\chi_\pi(g) = \delta_e(g)$; for an abelian group it is the Fourier inversion theorem for the delta mass; for the line it is $\int_{\mathbb{R}}e^{2\pi i\xi x}d\xi = \delta_0(x)$. The three are one identity, and the two below are its explicitly computable cases.

### Inversion

**Theorem (inversion).** Let $G$ be unimodular of type I and let $f \in L^1(G)\cap L^2(G)$ be such that $\pi \mapsto \operatorname{Tr}(\hat f(\pi)\pi(g)^{-1})$ is integrable against $\mu_P$ for almost every $g$. Then

$$
f(g) = \int_{\operatorname{Irr}(G)} \operatorname{Tr}\bigl(\hat f(\pi)\,\pi(g)^{-1}\bigr)\,d\mu_P(\pi)
$$

for almost every $g$; the integral converges in $L^2(G)$ for every $f \in L^2(G)$ and defines the inverse transform. In the abelian case $\operatorname{Irr}(G) = G^\vee$, $d_\pi = 1$, and the formula is the inversion theorem of *Harmonic Analysis on Groups*; in the compact case it is the Fourier inversion of *Analysis on Compact Groups*.

**Proof sketch.** Apply the definite form of the Plancherel theorem to the left translate $L_{g^{-1}}f$, whose transform is $\pi(g)^{-1}\hat f(\pi)$; the definite form at the identity of the translate is the value of $f$ at $g$, and the trace of the product gives the displayed integrand. The $L^2$ statement is the inverse of the unitary equivalence below. $\square$

### The Transform as a Unitary Equivalence

**Theorem.** For a unimodular group $G$ of type I, the operator-valued transform extends uniquely to a unitary equivalence of Hilbert spaces

$$
\mathcal{F} : L^2(G) \;\longrightarrow\; \int_{\operatorname{Irr}(G)}^{\oplus} \bigl(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*\bigr)\,d\mu_P(\pi),
$$

where the fibre $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$ carries the Hilbert–Schmidt inner product $\langle A,B\rangle = \operatorname{Tr}(AB^*)$. Under $\mathcal{F}$, left convolution by $f \in L^1(G)$ corresponds to the field of operators $\hat f(\pi)$, and the left regular representation corresponds to the field $\pi\otimes\pi^*$; equivalently $\mathcal{F}\,\lambda(f)\,\mathcal{F}^{-1}$ is multiplication by $\hat f(\pi)$ on the fibres.

**Proof.** The transform is isometric on the dense subspace $L^1\cap L^2$ by the Plancherel identity, and its image is dense in the direct integral because it contains the fields of finite rank supported on compact subsets of the dual; density of the image follows from the definite form applied to $f*h^*$ for $f,h$ in the coefficient algebra, which produces the rank-one fields $\hat f(\pi)\hat h(\pi)^* = |\hat f(\pi)\rangle\langle\hat h(\pi)|$. Hence the extension is unitary and onto. The intertwining statement is the convolution theorem, $\widehat{f*h}(\pi) = \hat f(\pi)\hat h(\pi)$, applied to the definition of $\lambda(f)$. $\square$

## Construction and Normalisation

### The Trace of the Regular Representation

The Plancherel measure is not an extra datum: it is determined by the trace on the group von Neumann algebra. Recall from *Noncommutative Harmonic Analysis*, §Central Decomposition and Multiplicities, that for a unimodular type I group

$$
L(G) = \lambda(G)'' \cong \int_{\operatorname{Irr}(G)}^{\oplus} B(\mathcal{H}_\pi)\,d\mu_P(\pi) ,
$$

with centre $Z(L(G))\cong L^\infty(\operatorname{Irr}(G),\mu_P)$ and faithful normal semifinite trace

$$
\tau(a) = \int_{\operatorname{Irr}(G)} \operatorname{Tr}\bigl(a(\pi)\bigr)\,d\mu_P(\pi).
$$

**Theorem (the measure is the trace).** The Plancherel measure is the measure on $\operatorname{Irr}(G)$ for which the trace of the group von Neumann algebra is integration, normalised by

$$
\tau\bigl(\lambda(f)\lambda(h)^*\bigr) = \int_{\operatorname{Irr}(G)}\operatorname{Tr}\bigl(\hat f(\pi)\hat h(\pi)^*\bigr)\,d\mu_P(\pi) = \langle f,h\rangle_{L^2(G)} .
$$

Consequently $\mu_P$ is unique once the normalisation of the Haar measure is fixed, and it is the measure of the central decomposition of $L(G)$: the dual is the spectrum of the centre, and $\mu_P$ is the spectral measure of the trace.

**Proof.** The trace on the direct integral of type I factors is integration of the ordinary trace against the measure of the decomposition, by the uniqueness of the central decomposition and of the trace on a type I factor; and the value on $\lambda(f)\lambda(h)^*$ is the definite Plancherel form. The identification with the $L^2$ inner product is the theorem of the previous section. $\square$

**Corollary (change of normalisation).** If $dx$ is replaced by $c\,dx$, $c > 0$, then $\mu_P$ is replaced by $c^{-1}\mu_P$; the two normalisations are exchanged, exactly as the Haar measure and the dual Haar measure are exchanged in the abelian case of *Harmonic Analysis on Groups*, §The Dual Haar Measure. When $G$ is compact, $dx$ is normalised to total mass $1$ and $\mu_P$ is the weighted counting measure; when $G$ is discrete with counting measure, $\lambda(e) = 1$ and $\tau(1) = \mu_P(\operatorname{Irr}(G))$ is the "total mass" of the dual, which is $1$ for an amenable discrete group and is not a number (the trace is not finite) in general.

### Dixmier's Abstract Plancherel Theorem

**Theorem (Dixmier).** Let $G$ be a second countable unimodular group of type I. Then the operator-valued Fourier transform $f \mapsto \hat f$, defined on $L^1(G)\cap L^2(G)$ and taking values in the measurable fields of Hilbert–Schmidt operators on the dual, extends to a unitary equivalence of $L^2(G)$ with the direct integral of the $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$, and the measure is the Plancherel measure of the previous theorem. Equivalently, every such $G$ is Plancherel.

**Proof sketch.** The general direct-integral decomposition of a representation of a separable type I $\mathrm{C}^*$-algebra (Part II's *Type I Groups*, §Uniqueness of Decomposition) applies to the regular representation of $C^*(G)$; the fibres of the decomposition of $\lambda$ are the irreducible representations $\pi$ with multiplicity $d_\pi$, the multiplicity being constant because $\lambda$ is the regular representation and its commutant is generated by the right regular representation; the measure is the standard measure of the central decomposition. The identification of the abstract measure with the trace normalisation of the previous theorem is the computation of $\tau$ on the coefficient algebra. The details are Dixmier's. $\square$

**Remark (type I is essential, and unimodularity too).** Without countable separation of the dual there is no Borel measure for which the decomposition is indexed by the irreducible classes: the decomposition of the regular representation of $F_2$ is into type $\mathrm{II}_1$ factors over a non-atomic space, and no Plancherel measure exists. Without unimodularity the transform is not isometric in the naive way and the theorem must be modified; the modification is described in the last section.

## The Abelian Case

Let $G$ be locally compact abelian. Every irreducible unitary representation is one-dimensional, so $\mathcal{H}_\pi = \mathbb{C}$, $d_\pi = 1$, $\operatorname{Irr}(G) = G^\vee$, and the Hilbert–Schmidt norm is the modulus. The Plancherel identity becomes

$$
\int_G |f(x)|^2\,dx = \int_{G^\vee}|\hat f(\chi)|^2\,d\mu_P(\chi) ,
$$

and the definite form becomes $f(e) = \int_{G^\vee}\hat f(\chi)\,d\mu_P(\chi)$. Comparing with the inversion theorem of *Harmonic Analysis on Groups*, §The Inversion and Plancherel Theorems, the measure is exactly the **dual Haar measure** normalised by inversion, and the inverse transform is $f(x) = \int_{G^\vee}\hat f(\chi)\chi(x)\,d\mu_P(\chi)$. In particular:

- $G = \mathbb{R}^n$: $\mu_P$ is Lebesgue measure on $\mathbb{R}^n$, and the theorem is the classical Plancherel theorem of *Fourier Analysis on Euclidean Spaces*.
- $G = S^1$: $\mu_P$ is counting measure on $\mathbb{Z}$, and the theorem is Parseval's identity for Fourier series.
- $G = \mathbb{Z}$: $\mu_P$ is normalised Lebesgue measure on $S^1$, and the theorem is Parseval for the discrete transform.
- $G = \mathbb{Q}_p$: $\mu_P$ is the self-dual Haar measure, and the theorem is the $p$-adic Plancherel identity.

The abelian Plancherel theorem is thus the statement that the scalar transform is unitary, and the general theorem is its operator-valued analogue with the trace replacing the modulus square.

## The Compact and Finite Cases

Let $K$ be compact with normalised Haar measure. The dual is discrete, the direct integral is a direct sum, and the Plancherel measure is the weighted counting measure

$$
\mu_P = \sum_{\pi\in\operatorname{Irr}(K)} d_\pi\,\delta_\pi ,
$$

so that the Plancherel identity is

$$
\int_K |f(k)|^2\,dk = \sum_{\pi\in\operatorname{Irr}(K)} d_\pi\,\|\hat f(\pi)\|_{\mathrm{HS}}^2 ,
$$

and inversion is $f(k) = \sum_\pi d_\pi\operatorname{Tr}(\hat f(\pi)\pi(k)^{-1})$, both of *Analysis on Compact Groups*, §The Inversion and Plancherel Formulas. The definite form $f(e) = \sum_\pi d_\pi\operatorname{Tr}\hat f(\pi)$ is the expansion of the delta mass at $e$. The weights $d_\pi$ are the multiplicities of the Peter–Weyl decomposition of *The Peter–Weyl Theorem*: the general abstract multiplicity $d_\pi = \dim\mathcal{H}_\pi$ becomes, in the compact case, the multiplicity of $\pi$ in the regular representation. Checking the normalisation, the Plancherel measure of $S^1$ is counting measure on $\mathbb{Z}$ with weights $d_n = 1$, and that of $SU(2)$ is $\sum_j(2j+1)\delta_j$ on the half-integer spins.

**Finite groups.** For a finite group $K$ with the normalised counting measure, $\hat f(\pi) = \frac{1}{|K|}\sum_{k}f(k)\pi(k)$, and the Plancherel identity reads

$$
\frac{1}{|K|}\sum_{k\in K}|f(k)|^2 = \sum_{\pi\in\operatorname{Irr}(K)} d_\pi\,\|\hat f(\pi)\|_{\mathrm{HS}}^2 .
$$

For $f = \delta_e$ both sides are $1/|K|$: the left side is $1/|K|$, and the right is $\sum_\pi d_\pi\cdot d_\pi/|K|^2 = \sum_\pi d_\pi^2/|K|^2 = |K|/|K|^2$. This is the Parseval identity of the discrete Fourier analysis on a finite group, and it is the Plancherel theorem in the case where all integrals are finite sums.

## The Heisenberg Group

Let $H$ be the Heisenberg group with the multiplication $(x,y,z)(x',y',z') = (x+x',y+y',z+z'+xy')$ and the Schrödinger representations $\pi_\lambda$ of *Noncommutative Harmonic Analysis*, §The Heisenberg Group. The group is connected nilpotent, hence unimodular and of type I; its dual is $\mathbb{R}^2 \cup \{\pi_\lambda : \lambda \in \mathbb{R}\smallsetminus\{0\}\}$, the first part consisting of the characters of the abelianisation. The Plancherel measure is supported on the infinite-dimensional part and has density

$$
d\mu_P(\pi_\lambda) = c\,|\lambda|\,d\lambda ,
$$

where the constant $c > 0$ depends on the normalisation of the Haar measure $dx\,dy\,dz$ and of the Schrödinger representation, both fixed above, for which $c = 1$. The computation is a direct application of the definite form: for $f$ in the coefficient algebra, $\operatorname{Tr}\hat f(\pi_\lambda)$ is the trace of an integral operator on $L^2(\mathbb{R})$ whose kernel is the Fourier transform of $f$ in the $z$-variable, and the integral over $\lambda$ against $|\lambda|d\lambda$ reproduces $f(0,0,0)$ by Fourier inversion; the factor $|\lambda|$ is the Jacobian of the orbit parametrisation of the coadjoint representation. The result is the Plancherel theorem for the Heisenberg group, and it is the simplest non-compact, non-abelian instance of the theorem.

**Remark (the characters of the abelianisation carry no measure).** The characters of $H/[H,H]$ are the one-dimensional representations, $d_\pi = 1$, and they form a set of measure zero for $\mu_P$; they contribute nothing to the Plancherel formula, and the whole of the $L^2$ analysis is carried by the infinite-dimensional series. This is the exact opposite of the compact case, where the measure is supported on finitely many points per compact set and every irreducible contributes.

## Semisimple Groups and the Harish-Chandra Formula

For a connected semisimple Lie group $G$ with finite centre, the unitary dual, the characters and the Plancherel measure were determined by Harish-Chandra. The measure is described by two pieces.

- **The continuous (tempered) part.** The principal series representations $\pi_{\lambda}$ induced from a parabolic subgroup contribute an absolutely continuous measure with a density that is an explicit product over the positive roots, the **Harish-Chandra $c$-function**: locally $\mu_P$ has density proportional to $|c(\lambda)|^{-2}$ times Lebesgue measure on the appropriate Cartan subspace. For $G = SL_2(\mathbb{R})$ this gives the densities $t\tanh(\pi t)$ and $t\coth(\pi t)$ on the two parts of the principal series, as recorded in *Noncommutative Harmonic Analysis*, §The Standard Examples.
- **The discrete part.** The discrete series representations contribute point masses, each with a **formal degree** $\deg(\pi) > 0$; for $SL_2(\mathbb{R})$ the discrete series $D_n$ contribute a point mass proportional to the formal degree. The discrete series exists exactly when $G$ has a compact Cartan subgroup, by Harish-Chandra's criterion.

**Theorem (Harish-Chandra's Plancherel formula).** For a connected semisimple Lie group with finite centre, the Plancherel measure is the sum of an absolutely continuous measure on the tempered part of the dual, with density given by the $c$-function, and an atomic measure on the discrete series with masses the formal degrees; the definite form holds for every $f \in C_c^\infty(G)$.

**Proof.** This is Harish-Chandra's theorem; the wave-packet construction of the discrete series and the explicit Fourier inversion of the spherical functions are its two ingredients, and the proof is quoted from the literature. $\square$

**The spherical transform.** For $K$ a maximal compact subgroup and $G/K$ the symmetric space, the $K$-invariant functions on $G$ transform by the **spherical transform** against the spherical functions $\varphi_\lambda$, and the spherical Plancherel measure is the part of $\mu_P$ supported on the spherical (class-one) representations. The spherical transform on $G/K$ is the exact analogue of the Fourier transform on $\mathbb{R}^n$ regarded as the symmetric space of the Euclidean motion group, and the Harish-Chandra $c$-function is the analogue of the normalising factor in the Euclidean inversion formula. This is the analytic core of the harmonic analysis of *Symmetric Spaces*.

**Remark (the automorphic case).** The decomposition of $L^2(G/\Gamma)$ for a lattice $\Gamma$ into a discrete spectrum (cuspidal automorphic forms) and a continuous spectrum (Eisenstein series) is the Plancherel theorem for the homogeneous space rather than for the group; it is the spectral theory, and the trace formula is its quantitative form.

## Nilpotent and Solvable Groups

For a connected simply connected nilpotent Lie group $G$, the **orbit method** of Kirillov identifies the unitary dual with the space $\mathfrak{g}^*/\operatorname{Ad}^*(G)$ of coadjoint orbits, and the representations are parametrised by the orbits. The Plancherel measure is then the pushforward of Lebesgue measure on the dual vector space under the orbit map,

$$
\mu_P = \bigl(\mathfrak{g}^* \to \mathfrak{g}^*/\operatorname{Ad}^*(G)\bigr)_*\bigl(\text{Lebesgue measure}\bigr) ,
$$

normalised so that the definite form holds; equivalently the density of a representation is the square root of the Pfaffian of the Kirillov form on its orbit. For the Heisenberg group the orbits in the non-degenerate part are parametrised by $\lambda \in \mathbb{R}\smallsetminus\{0\}$ with Lebesgue measure $d\lambda$, and the passage to the representation $\pi_\lambda$ multiplies by the factor $|\lambda|$ from the Fourier transform in the $z$-variable; this is the computation of the previous section. Every connected simply connected nilpotent Lie group is type I and unimodular, so the Plancherel theorem applies without exception to this class.

**Theorem (Kirillov's Plancherel formula).** For a connected simply connected nilpotent Lie group, the operator-valued transform is unitary with respect to the pushforward of Lebesgue measure on $\mathfrak{g}^*$, and the inversion and definite forms hold for $f \in C_c^\infty(G)$.

**Proof.** The orbit method and the Plancherel formula are Kirillov's; the proof uses the Kirillov character formula and the stationary-phase computation of the characters on the orbits. It is quoted. $\square$

**Remark (solvable groups).** Connected solvable Lie groups are type I by the Auslander–Kostant theorem, but the orbit picture is more delicate, the dual need not be smooth in a uniform way, and the Plancherel measure need not be a pushforward of Lebesgue measure; groups of exponential type behave as in the nilpotent case, and the general solvable case is treated by the orbit method with the complications of the non-exponential fibres.

## Non-Unimodular and Non-Type-I Cases

### The Non-Unimodular Modification

If $G$ is not unimodular the operator-valued transform is not an isometry with respect to the left Haar measure alone, because the left regular representation is not unitary on $L^2(G,dx)$; the correct picture is obtained by using the right regular representation on the same space or by weighting by $\Delta^{1/2}$, and the resulting formula for the transform involves the square root of the modular function. Explicitly, with

$$
\hat f(\pi) = \int_G f(g)\pi(g)\,dg
$$

one has the modified inversion in which $f(g)\Delta(g)^{-1/2}$ is the inverse transform of the field, and the Plancherel density is not the multiplicity $d_\pi$ alone but is corrected by the modular character of the inducing data. The affine group is the standard illustration of the necessity of the correction; the theory for this class was developed by Duflo and is quoted.

**Remark (amenable and unimodular).** Every amenable group is unimodular, so a non-unimodular group is never amenable; the Plancherel theory and the amenable theory of *Noncommutative Harmonic Analysis*, §Weak Containment and Amenability therefore occupy different classes of groups, and a group may be Plancherel without being amenable ($SL_2(\mathbb{R})$) and amenable without being non-unimodular.

### The Failure for $F_2$

If $G$ is not of type I, no Plancherel measure exists. For the free group $F_2$, the regular representation decomposes into factor representations of type $\mathrm{II}_1$ over a non-atomic space, the group von Neumann algebra $L(F_2)$ is a $\mathrm{II}_1$ factor with no minimal projections, and there is no Borel measure on $\operatorname{Irr}(F_2)$ indexing the decomposition. The trace $\tau(a) = \langle a\delta_e,\delta_e\rangle$ is still the correct object replacing the measure, but it is not integration against a measure on the dual. In this sense the Plancherel theorem is exactly the statement that the trace is $L^\infty$ of a measure, and the type I hypothesis is what makes that true.

**Theorem (dichotomy).** For a unimodular group $G$ the following are equivalent: $G$ is of type I; the regular representation is a direct integral of irreducible representations; there is a Plancherel measure on $\operatorname{Irr}(G)$ for which the definite form holds. Each fails for $F_2$, whose regular representation is a direct integral of $\mathrm{II}_1$ factors and whose trace is not a measure on the dual.

**Proof.** The equivalence of the first two is the general multiplicity theory of *Type I Groups*, §Uniqueness of Decomposition; the equivalence with the third is the constructive part of Dixmier's theorem together with the observation that a decomposition indexed by the irreducible classes with a measurable multiplicity function is exactly a Plancherel measure. $\square$

## Summary

For a second countable unimodular group $G$ of type I the Plancherel theorem states that there is a unique Radon measure $\mu_P$ on the unitary dual $\operatorname{Irr}(G)$ — the Plancherel measure — such that the operator-valued Fourier transform $\hat f(\pi) = \int_G f(g)\pi(g)dg$ is isometric, $\int_{\operatorname{Irr}(G)}\|\hat f(\pi)\|_{\mathrm{HS}}^2d\mu_P(\pi) = \int_G|f(g)|^2dg$, definite, $f(e) = \int_{\operatorname{Irr}(G)}\operatorname{Tr}(\hat f(\pi))d\mu_P(\pi)$, and invertible, $f(g) = \int_{\operatorname{Irr}(G)}\operatorname{Tr}(\hat f(\pi)\pi(g)^{-1})d\mu_P(\pi)$; equivalently, the transform extends to a unitary equivalence $L^2(G)\cong\int^\oplus(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*)d\mu_P$. The measure is uniquely determined by the trace of the group von Neumann algebra, $\tau(a) = \int\operatorname{Tr}(a(\pi))d\mu_P(\pi)$, and its existence is Dixmier's abstract theorem, the fibres of the central decomposition $L(G)\cong\int^\oplus B(\mathcal{H}_\pi)d\mu_P$ being the irreducibles with multiplicity $d_\pi = \dim\mathcal{H}_\pi$. The abelian case recovers the dual Haar measure and the classical Plancherel identity, the compact case is the weighted counting measure $\sum_\pi d_\pi\delta_\pi$ and the Peter–Weyl Plancherel identity, and the finite case is Parseval for the discrete transform; the Heisenberg group has density $|\lambda|d\lambda$ on its infinite-dimensional series, the semisimple groups have Harish-Chandra's measure with the $c$-function density on the tempered part and formal-degree atoms on the discrete series, the spherical transform on a symmetric space is the class-one part, and the nilpotent groups are governed by Kirillov's orbit method with the pushforward of Lebesgue measure on $\mathfrak{g}^*/\operatorname{Ad}^*(G)$. Outside the hypotheses the theorem changes form for non-unimodular groups, where the transform acquires a $\Delta^{1/2}$ correction, and fails altogether for non-type-I groups, where $F_2$ exhibits a $\mathrm{II}_1$ factor and no Plancherel measure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $dx$, $\Delta$, $e$ | Locally compact group, left Haar measure, modular function, identity |
| unimodular, Plancherel | $\Delta\equiv1$; unimodular and type I |
| $\operatorname{Irr}(G)$, $\mathcal{H}_\pi$, $d_\pi$ | Unitary dual, representation space, dimension/multiplicity |
| $\hat f(\pi) = \int_G f(g)\pi(g)\,dg$ | Operator-valued Fourier transform |
| $\mu_P$ | Plancherel measure |
| $\int^\oplus$ | Direct integral |
| $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$ | Fibre of the Plancherel decomposition, with Hilbert–Schmidt inner product |
| $\tau(a) = \int\operatorname{Tr}(a(\pi))\,d\mu_P(\pi)$ | Trace on $L(G)$ |
| $\delta_e$ | Delta mass at the identity; definite form |
| $c(\lambda)$ | Harish-Chandra $c$-function |
| $\varphi_\lambda$ | Spherical function; spherical transform |
| $\deg(\pi)$ | Formal degree of a discrete series representation |
| $\mathfrak{g}^*/\operatorname{Ad}^*(G)$ | Coadjoint orbit space (nilpotent groups) |
| $\mathbb{R}^2\cup\{\pi_\lambda\}$ | Dual of the Heisenberg group |
| $\lvert\lambda\rvert\,d\lambda$ | Heisenberg Plancherel density |
| $F_2$ | Free group on two generators; non-type-I failure |





## Further Reading

- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the abstract Plancherel theorem and the decomposition of a representation of a type I algebra.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for the Plancherel theorem on unimodular groups and the standard examples.
- Harish-Chandra, *Collected Papers* (Springer, 1984), for the Plancherel formula, the $c$-function and the discrete series.
- A. A. Kirillov, *Elements of the Theory of Representations* (Springer, 1976), for the orbit method and the Plancherel formula for nilpotent groups.
- Michel Duflo, *Théorie de Mackey et représentations des groupes de Lie résolubles* (North-Holland, 1980), for the Plancherel theory beyond the nilpotent case and the non-unimodular modification.
- Sigurdur Helgason, *Groups and Geometric Analysis* (AMS, 1984), for the spherical transform and the harmonic analysis on symmetric spaces.
- George W. Mackey, *The Theory of Unitary Group Representations* (Chicago, 1976), for the Borel structure of the dual and the multiplicity theory used in the decomposition.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, 2nd ed. 1991), for the Hilbert-space spectral theory, the compact and Hilbert–Schmidt operators and the Banach-algebra foundations quoted as standard.
