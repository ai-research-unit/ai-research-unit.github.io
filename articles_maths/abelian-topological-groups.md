
# __Abelian Topological Groups__

## Introduction

An **abelian topological group** is an abelian group carrying a topology for which addition and negation are continuous. The combination of commutativity with a topology is much more restrictive than either hypothesis alone: an abelian topological group carries a *compact-open* dual that is again an abelian topological group, its structure as a locally compact group is completely described by a real vector part and a compact part, and the assignment $G \mapsto G^\vee$ to the group of continuous characters turns out to be an equivalence of that category with its opposite. This article develops the structure theory and the character theory up to the point where duality is stated, and it isolates the two objects — the character group and the structure theorem — that takes as its subject.

The article is written additively throughout, since the groups here are abelian: the group law is $+$, the identity is $0$, and the inverse is $-x$. The topological frame is that of the companion articles *Topological Spaces* and *Metric, Uniform and Complete Spaces*, the group-theoretic frame is *Topological Groups*, and the abstract structure theory of discrete abelian groups — torsion, divisibility, rank — is that of *Infinite Abelian Groups* in the algebra of Part I. A topology on an abelian group may come from a distance, from a norm, from a filtration by subgroups, or from no metric at all; the examples below include the first three and the profinite groups of the third kind.

Two boundaries are stated once and used throughout. The **measure** enters only as the Haar measure constructed in: this article uses it only as an invariant measure on a locally compact group, and integrates against it nowhere beyond the finite sums of the finite case. The Fourier transform, the convolution algebra $L^1(G)$, the $L^p$ spaces and the Plancherel theorem are the subject in Part III, where the measure and the limit are available; where the harmonic analysis of an example is classical, the example is named and the analysis is deferred. The base ring $R$ is a commutative ring with identity $1 \neq 0$ and $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; no physics is invoked.

## The Additive Setting

### Definition and First Consequences

**Definition.** An **abelian topological group** is an abelian group $G$ with a topology for which the maps

$$
G \times G \to G, \quad (x, y) \mapsto x + y, \qquad G \to G, \quad x \mapsto -x,
$$

are continuous, the product carrying the product topology. Equivalently, the single map $(x, y) \mapsto x - y$ is continuous.

The definition is the additive case of *Topological Groups*, §The Axioms and Their Consequences, and the general theory transfers without change: translations $x \mapsto x + a$ are homeomorphisms, so $G$ is homogeneous and its topology is determined by a neighbourhood base at $0$; a subgroup is open if and only if it is a neighbourhood of $0$, and an open subgroup is closed; the quotient $G/H$ by a subgroup carries the quotient topology and is Hausdorff exactly when $H$ is closed; and the body of examples is shared with the non-abelian theory. What is new is the following, and it is used constantly.

**Proposition.** In an abelian topological group the left and right uniformities coincide, and the map $(x, y) \mapsto x + y$ is uniformly continuous for the common uniformity. Consequently every abelian topological group is unimodular: its left Haar measure, when it exists, is right-invariant.

**Pro.** The left uniformity has a base of sets $\{(x,y): x^{-1}y \in U\}$ and the right uniformity a base of sets $\{(x,y): yx^{-1} \in U\}$; in additive notation $x^{-1}y = y - x = yx^{-1}$, so the two families are identical. For uniform continuity of addition, if $y - x \in U$ and $y' - x' \in U$ then $(y + y') - (x + x') = (y - x) + (y' - x') \in U + U$, so the preimage of the entourage of $U + U$ contains the product of the entourages of $U$. Unimodularity: the modular function is a continuous homomorphism to the abelian group $\mathbb{R}_{>0}$, and the modular function is invariant under conjugation, and conjugation is trivial in an abelian group, so the modular function is identically $1$ and left and right invariance agree. $\square$

**Example (the classical additive groups).** $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$, $\mathbb{Z}$, $\mathbb{R}^n$ and $\mathbb{K}^n$ with the usual topology are abelian topological groups; $\mathbb{Z}$ and every group with the discrete topology are discrete abelian topological groups; a finite group is a compact discrete abelian topological group. The circle group $S^1 = \{z \in \mathbb{C} : |z| = 1\}$ is a compact abelian topological group, and the map $t \mapsto e^{2\pi i t}$ presents it as $\mathbb{R}/\mathbb{Z}$.

**Example (locally compact and p-adic cases).** $\mathbb{Q}_p$ with the $p$-adic absolute value and $\mathbb{Z}_p$ with the subspace topology are locally compact abelian topological groups, the second compact and totally disconnected; both are treated, and the profinite topology of $\mathbb{Z}_p$ is developed . The direct product of locally compact abelian groups with the product topology is locally compact abelian.

**Example (topological vector spaces).** A topological vector space is in particular an abelian topological group under addition, and the additive group of a topological ring is an abelian topological group; the additive groups $\mathbb{Q}_p^n$ and the function groups $C(X, \mathbb{R})$ with the compact-open topology are instances. The additive structure alone forgets the scalars, which is why the theory below is the *group* theory of these objects and not their linear theory.

### Subgroups, Quotients and Products

The following dictionary is the algebraic content of the additive theory, and duality later inverts it.

**Proposition.** Let $G$ be an abelian topological group and let $H \subseteq G$ be a subgroup.

**(a)** The closure $\overline H$ is a subgroup, and $\overline H$ is the smallest closed subgroup containing $H$; a subgroup is open if and only if it is a neighbourhood of $0$.

**(b)** If $H$ is closed, $G/H$ is a Hausdorff abelian topological group and the quotient map $\pi : G \to G/H$ is open, continuous and a homomorphism.

**(c)** If $H$ is open and $G$ is compact, $H$ has finite index; if $H$ is open and $G$ is connected, then $H = G$.

**(d)** For a family $(G_i)$ of abelian topological groups the product $\prod_i G_i$ with the product topology is an abelian topological group, and the coordinate maps are continuous open homomorphisms.

**Proof.** (a) The closure of a subgroup is a subgroup because the group operations are continuous and $H + H \subseteq H$, $-H \subseteq H$ imply the same for the closure by continuity. A subgroup $H$ that is a neighbourhood of $0$ is open because $H = \bigcup_{h \in H} (h + H)$ is a union of translates of a neighbourhood of $0$, hence open; conversely an open subgroup is a neighbourhood of $0$ by definition. (b) The quotient map is open by the definition of the quotient topology, and $G/H$ is Hausdorff because $H$ is closed, as in *Topological Groups*, §Subgroups and Quotients. (c) The cosets of an open subgroup cover the compact group $G$ and form an open cover, so finitely many suffice, giving finite index; if $G$ is connected the cosets separate $G$ into disjoint open sets, so there is only one. (d) Standard properties of the product topology. $\square$

**Remark.** The additive groups of this article are exactly the objects whose dual is again a group: the set of continuous homomorphisms to the circle is a group under pointwise addition only because the target is abelian, and it inherits a topology from the compact-open structure. The next section makes this precise.

## Characters and the Dual

### Definition

**Definition.** Let $G$ be an abelian topological group. A **character** of $G$ is a continuous homomorphism $\chi : G \to S^1$, the circle being written multiplicatively. The set of characters, written $G^\vee$, is the **character group** or **Pontryagin dual** of $G$. It is a group under pointwise multiplication,

$$
(\chi_1 \chi_2)(x) = \chi_1(x)\, \chi_2(x),
$$

and it is given the **compact-open topology**: a subbase consists of the sets

$$
\{\chi : \chi(K) \subseteq U\}, \qquad K \subseteq G \text{ compact},\ U \subseteq S^1 \text{ open}.
$$

The symbol $G^\vee$ is used throughout in preference to a hat, which the corpus reserves for completions. The neutral element of $G^\vee$ is the trivial character $\chi \equiv 1$.

**Theorem.** For an abelian topological group $G$, the dual $G^\vee$ with the compact-open topology is an abelian topological group; it is Hausdorff, and it is compact, discrete or locally compact exactly when $G$ is discrete, compact or locally compact, respectively.

**Proof.** The pointwise product of two characters is a continuous homomorphism because both properties are preserved by pointwise multiplication, and inversion $\chi \mapsto \chi^{-1} = \bar\chi$ preserves them; the group laws are continuous for the compact-open topology because evaluation at a point and multiplication in $S^1$ are continuous, and the compact-open topology is the topology of uniform convergence on compacta. If $G$ is discrete the compact subsets are finite, so the compact-open topology is the topology of pointwise convergence, which is the product topology on $(S^1)^G$; the dual is then a closed subgroup of the compact group $(S^1)^G$, hence compact. The topology is Hausdorff because two distinct characters differ at a point $x$, and the compact-open subbase with the compact set $K = \{x\}$ separates them. If $G$ is compact, the neighbourhood $\{\chi : \chi(G) \subseteq U\}$ for a proper open arc $U$ containing $1$ contains only the trivial character, since $\chi(G)$ is a subgroup of $S^1$ contained in $U$, and the only subgroup of the circle lying in a proper arc is the trivial one; hence the trivial character is an isolated point and the dual is discrete. The locally compact statement is the substance of the duality theorem and is stated below. $\square$

**Example (duals of the standard groups).** The following table collects the characters used repeatedly; each entry is standard and each is verified by exhibiting the pairing.

| Group $G$ | Dual $G^\vee$ | Pairing $\chi(x)$ |
|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | $x \mapsto e^{2\pi i \xi x}$, $\xi \in \mathbb{R}$ |
| $\mathbb{R}^n$ | $\mathbb{R}^n$ | $x \mapsto e^{2\pi i \langle \xi, x\rangle}$ |
| $S^1 = \mathbb{R}/\mathbb{Z}$ | $\mathbb{Z}$ | $z \mapsto z^n$, $n \in \mathbb{Z}$ |
| $\mathbb{Z}$ | $S^1$ | $n \mapsto z^n$, $z \in S^1$ |
| $\mathbb{Z}/n\mathbb{Z}$ | $\mathbb{Z}/n\mathbb{Z}$ | $m \mapsto e^{2\pi i k m/n}$, $k \in \mathbb{Z}/n\mathbb{Z}$ |
| $\mathbb{Z}_p$ | $\mu_{p^\infty}$ | compatible system of $p^k$-th roots of unity |
| $\mathbb{Q}_p$ | $\mathbb{Q}_p$ | additive character $x \mapsto e^{2\pi i \{x\}}$ composed with a duality |
| $\mathbb{Q}$ (discrete) | compact, the Bohr compactification | $\chi$ continuous for the discrete topology |

The **Prüfer group** $\mu_{p^\infty} = \bigcup_k \mu_{p^k}$ is the group of all $p$-power roots of unity, with the discrete topology; it is the dual of the compact group $\mathbb{Z}_p$, and its own dual is $\mathbb{Z}_p$. The passage $\mathbb{Z}_p \leftrightarrow \mu_{p^\infty}$ is the basic example of the interchange of compactness and discreteness under duality, and it is why the structure theory of the dual of a compact group is a statement about a discrete torsion group.

**Proposition (separation).** For a locally compact abelian group $G$ and $x \neq 0$ in $G$, there is a character $\chi$ with $\chi(x) \neq 1$. Hence the characters separate the points of $G$, and the evaluation map $G \to G^{\vee\vee}$ is injective.

**Pro.** By the structure theorem below, $G$ contains an open subgroup of the form $\mathbb{R}^n \times K$ with $K$ compact, so it suffices first to separate points of $\mathbb{R}^n$ and of a compact group, and then to observe that a character of an open subgroup extends to $G$ because $G/H$ is discrete. For $\mathbb{R}^n$ the characters $x \mapsto e^{2\pi i\langle \xi, x\rangle}$ separate points by the non-degeneracy of the inner product. For a compact group $K$ the characters separate points by the Peter–Weyl theory in Part III, or equivalently by the theorem of Gelfand–Raĭkov that a compact abelian group embeds in a product of circles; the construction uses the Haar measure and the integration of Part III, and is quoted as standard here. Extension from an open subgroup to $G$ uses that $G/H$ is discrete, so a homomorphism on $H$ extends by choosing values on a set of coset representatives and using compactness. $\square$

### Annihilators and the Algebraic Duality

**Definition.** For a subgroup $H \subseteq G$ the **annihilator** is

$$
H^\perp = \{\chi \in G^\vee : \chi(x) = 1 \text{ for all } x \in H\}.
$$

It is a subgroup of $G^\vee$, closed in the compact-open topology, and the assignment $H \mapsto H^\perp$ reverses inclusions.

**Theorem (annihilator duality).** Let $G$ be a locally compact abelian group and $H \subseteq G$ a closed subgroup. Then

$$
(G/H)^\vee \cong H^\perp, \qquad H^\vee \cong G^\vee / H^\perp,
$$

as topological groups, the first isomorphism carrying a character of $G/H$ to its composite with the quotient map and the second carrying a character of $H$ to its class modulo the characters vanishing on $H$.

**Proof.** The first map is certainly an injective homomorphism of $H^\perp$ onto $(G/H)^\vee$: a character of $G$ vanishing on $H$ factors through $G/H$, and conversely a character of $G/H$ pulls back to one of $G$ vanishing on $H$; continuity is preserved because the quotient map is continuous and open. The second map is the composite $G^\vee \to H^\vee$ of restriction with the quotient by its kernel $H^\perp$, which is a continuous open homomorphism because restriction to a closed subgroup is continuous for the compact-open topology; injectivity and surjectivity are the statement that every character of a closed subgroup extends to $G$, the extension theorem for locally compact abelian groups, which is deduced from the structure theorem in the standard theory and is quoted here as standard. $\square$

**Corollary (exact sequences).** A short exact sequence $0 \to H \to G \to G/H \to 0$ of locally compact abelian groups dualises to the short exact sequence

$$
0 \to H^\perp \to G^\vee \to H^\vee \to 0,
$$

so that duality is an exact contravariant functor on locally compact abelian groups; it carries arbitrary products to direct sums and arbitrary direct sums to products.

**Remark.** The annihilator formalism is the algebraic skeleton of duality and is used in to organise the proof of the main theorem; here it records that the *algebraic* part of duality needs no compactness or local compactness beyond the extension of characters, and that the topological part is the statement that the canonical map $G \to G^{\vee\vee}$ is a homeomorphism.

## The Structure of Locally Compact Abelian Groups

### The Structure Theorem

The structure of a locally compact abelian group is completely described by a real vector part and a compact part, with no further invariants.

**Theorem (structure of locally compact abelian groups).** Let $G$ be a locally compact abelian group. Then $G$ has an open subgroup of the form

$$
\mathbb{R}^n \times K,
$$

where $n \geq 0$ and $K$ is a compact abelian group; equivalently, $G \cong \mathbb{R}^n \times G_1$ with $G_1$ a locally compact abelian group containing a compact open subgroup, and the global product $G \cong \mathbb{R}^n \times K$ with $K$ compact is not available in general. And $G$ is compactly generated if and only if

$$
G \cong \mathbb{R}^n \times \mathbb{Z}^m \times K
$$

with $K$ compact; the compact factor is finite, $G \cong \mathbb{R}^n \times \mathbb{Z}^m \times F$, exactly when $G$ contains no infinite compact subgroup.

**Proof sketch.** The identity component $G_0$ of $G$ is a connected locally compact abelian group. By the solution of Hilbert's fifth problem in the abelian case — the theorem of Gleason and Montgomery–Zipp, as stated — a connected locally compact group is a projective limit of Lie groups; for an abelian group the limit is a Lie group, and a connected abelian Lie group is of the form $\mathbb{R}^n \times T^k$ with $T^k$ a torus. Passing to the quotient $G/G_0$, which is totally disconnected and locally compact, one uses van Dantzig's theorem that a totally disconnected locally compact group has a compact open subgroup, and hence contains an open compact subgroup; combining the two gives an open subgroup $\mathbb{R}^n \times K$ with $K$ compact. For the compactly generated refinement, the quotient of $G$ by the open subgroup $\mathbb{R}^n \times K$ is a compactly generated discrete abelian group, hence finitely generated; since $G$ is abelian the extension is central, and the compact factor may be enlarged to absorb the finite part, so that $G \cong \mathbb{R}^n \times \mathbb{Z}^m \times K$ with $K$ compact, namely the maximal compact subgroup of $G$. The compact factor is finite exactly when $G$ has no infinite compact subgroup, the case of the classical form $\mathbb{R}^n \times \mathbb{Z}^m \times F$; the compactly generated group $\mathbb{Z}_p$ shows that it can be infinite. $\square$

**Corollary.** Every locally compact abelian group has an open subgroup $\mathbb{R}^n \times K$ with $K$ compact, and is an extension of a discrete abelian group by it; its identity component is $\mathbb{R}^n \times K_0$, where $K_0$ is compact connected. The global splitting $G \cong \mathbb{R}^n \times K$ with $K$ compact fails for $\mathbb{Q}_p$ and for $\mathbb{Z}[1/p]$. The discrete locally compact abelian groups are exactly the abstract abelian groups with the discrete topology, and a compact locally compact abelian group is compact abelian by definition, so the abstract theory of discrete abelian groups sits inside the topological one.

**Example.** $\mathbb{R}^n$, $T^n = \mathbb{R}^n/\mathbb{Z}^n$, $\mathbb{Z}^n$, a finite abelian group, $\mathbb{Z}_p$, $\mathbb{Q}_p$ and $\mathbb{R}^n \times \mathbb{Z}^m \times F$ all conform to the theorem. A solenoid $\Sigma_p = \varprojlim_k (S^1 \xrightarrow{\,p\,} S^1)$ is a compact connected abelian group of dimension one in the sense of covering dimension, and it is not a Lie group; it is the standard compact group that is not a torus, and its dual is the discrete group $\mathbb{Z}[1/p]$.

### The Discrete and Compact Constituents

The two extreme cases govern the general one, and they are dual to each other.

**Theorem.** For a locally compact abelian group $G$ the following hold.

**(a)** $G$ is discrete if and only if $G^\vee$ is compact.

**(b)** $G$ is compact if and only if $G^\vee$ is discrete.

**(c)** $G$ is compactly generated if and only if $G \cong \mathbb{R}^n \times \mathbb{Z}^m \times K$ with $K$ compact, the compact factor being finite exactly when $G$ has no infinite compact subgroup.

**Proof.** (a) and (b) are proved in the theorem on the dual above: for discrete $G$ the compact-open topology on $G^\vee$ is the product topology on a closed subgroup of $(S^1)^G$, hence compact, and a compact $G$ has discrete dual; the converse directions follow on applying the two forward statements to $G^\vee$ and using the reflexivity $G \cong G^{\vee\vee}$ of the duality theorem. (c) is the compactly generated half of the structure theorem, restated; dually the structure theorem gives $G^\vee \cong \mathbb{R}^n \times T^m \times K^\vee$ with $K^\vee$ discrete, and $K^\vee$ is finitely generated precisely when the compact factor $K$ is a compact Lie group, $K \cong T^k \times F$ with $F$ finite. $\square$

**Example (finite abelian groups).** For a finite abelian group $G$ the dual $G^\vee = \operatorname{Hom}(G, S^1)$ has the same order as $G$, and $G \cong G^\vee$ non-canonically, the isomorphism requiring a choice of roots of unity. For $G = \mathbb{Z}/n\mathbb{Z}$ every character is $\chi_k(m) = e^{2\pi i k m/n}$ for a unique $k$, and the orthogonality relation

$$
\frac{1}{n}\sum_{m=0}^{n-1} \chi_k(m)\overline{\chi_l(m)} = \delta_{kl}
$$

holds, the left-hand side being the average $\frac{1}{n}\sum_{m=0}^{n-1} (e^{2\pi i (k-l)/n})^m$ of the $n$-th roots of unity, which is $1$ for $k = l$ and $0$ otherwise. The dual of a direct sum of cyclic groups is the direct sum of the duals, so the duality of finite abelian groups is decided on the cyclic factors; for $G = \bigoplus_i \mathbb{Z}/n_i\mathbb{Z}$ one has $G^\vee \cong \bigoplus_i \mathbb{Z}/n_i\mathbb{Z}$.

**Example (compact abelian groups).** The dual of $S^1$ is $\mathbb{Z}$, the dual of $T^n$ is $\mathbb{Z}^n$, the dual of $\mathbb{Z}_p$ is the discrete Prüfer group $\mu_{p^\infty}$, and the dual of a finite abelian group is finite. A compact abelian group embeds in a product of circles, and its dual is a discrete torsion-free group for the connected case: the dual of a torus is free abelian, and a connected compact abelian group is the dual of a discrete torsion-free group (such groups are called solenoids).

## Duality

### Statement of Pontryagin Duality

The main theorem of the theory is stated here and developed in the companion article.

**Theorem (Pontryagin duality).** For every locally compact abelian group $G$, the evaluation map

$$
\iota_G : G \longrightarrow G^{\vee\vee}, \qquad \iota_G(x)(\chi) = \chi(x),
$$

is an isomorphism of topological groups. The assignment $G \mapsto G^\vee$ is a contravariant functor that is an equivalence of categories between the category of locally compact abelian groups and its opposite, and it carries compact groups to discrete groups and conversely.

**Proof sketch.** The evaluation map is a continuous homomorphism by the definition of the compact-open topology, and it is injective by the separation theorem above. Surjectivity and the topological statement reduce, by the structure theorem, to the cases $G = \mathbb{R}^n$, $G = S^1$, $G = \mathbb{Z}$, $G$ finite and $G$ compact; in each the computation is explicit — $\mathbb{R}^n$ is self-dual, $\mathbb{Z}^\vee = S^1$ and $(S^1)^\vee = \mathbb{Z}$ are exchanged, and a finite abelian group is (non-canonically) isomorphic to its dual, with the canonical evaluation being an isomorphism in each case. The general case follows by the exactness of duality on the open subgroup $\mathbb{R}^n \times K$ and the discreteness of the quotient. The complete argument, together with the verification that evaluation is a homeomorphism and not merely a bijection, is not covered here. $\square$

**Remark.** The content of the theorem is the *reflexivity* of every locally compact abelian group. A character group is a group of homomorphisms into a compact group, and the theorem says that every such group arises from a locally compact group and that the correspondence loses no information; it is the cleanest example in the corpus of a contravariant duality that is nevertheless an equivalence, of the category of locally compact abelian groups with its opposite.

### Duality of Substructure

The annihilator formalism of §Characters and the Dual becomes a dictionary of substructures under duality.

**Corollary (the duality dictionary).** Let $G$ be a locally compact abelian group. Under the evaluation isomorphism the following correspond.

| In $G$ | In $G^\vee$ |
|---|---|
| closed subgroup $H$ | closed subgroup $H^\perp$, with $(G/H)^\vee \cong H^\perp$ |
| quotient $G/H$ | closed subgroup $H^\perp$ |
| open subgroup $H$ | compact subgroup $H^\perp$ |
| compact subgroup $H$ | open subgroup $H^\perp$ |
| discrete subgroup $H$ | subgroup $H^\perp$ whose quotient $G^\vee/H^\perp$ is compact |
| finite subgroup $H$ | subgroup $H^\perp$ that is open and of finite index |

**Proof.** The first two rows are the annihilator theorem: $H$ closed corresponds to the quotient $G^\vee/H^\perp$, and the quotient $G/H$ to its annihilator $H^\perp$. The remaining rows are read off from the extreme cases: $H$ is open exactly when $G/H$ is discrete, and the dual of a discrete group is compact, so $H^\perp \cong (G/H)^\vee$ is compact; $H$ is compact exactly when $H^\vee$ is discrete, and $H^\vee \cong G^\vee/H^\perp$, so $H^\perp$ is open; $H$ is discrete exactly when $H^\vee$ is compact, that is, exactly when $G^\vee/H^\perp$ is compact; and a finite subgroup, being compact and discrete, has an annihilator that is both open and compact, hence open of finite index. $\square$

**Corollary (duality of the structure theorem).** A locally compact abelian group $G$ is compactly generated if and only if $G \cong \mathbb{R}^n \times \mathbb{Z}^m \times K$ with $K$ compact, and then $G^\vee \cong \mathbb{R}^n \times T^m \times K^\vee$ with $K^\vee$ discrete. Moreover $G$ is a Lie group if and only if $G \cong \mathbb{R}^n \times T^k \times D$ with $D$ a countable discrete abelian group, equivalently if and only if the identity component $G_0$ is open and the quotient $G/G_0$ is countable.

**Proof.** The first statement is the compactly generated half of the structure theorem, together with the computation of the dual of a product of the three factors. For the second, in a Lie group the identity component is open and there are countably many components; conversely a locally compact group with $G_0$ open is a Lie group exactly when its discrete quotient $G/G_0$ is countable. $\square$

### Reflexive Subcategories and Examples

**Example (the circle and its powers).** $S^1$ is self-dual in the sense that $S^1 \cong (S^1)^\vee$ by the evaluation at a generator of the dual; the pairing $(z, n) \mapsto z^n$ exhibits $S^1$ and $\mathbb{Z}$ as mutual duals, and $T^n$ and $\mathbb{Z}^n$ similarly. This exchange of a compact group and a discrete group of the same rank is the paradigm of the theorem.

**Example (the p-adic line and its dual).** The additive group $\mathbb{Q}_p$ is self-dual, and $\mathbb{Z}_p$ is dual to the discrete Prüfer group $\mu_{p^\infty}$. The exact sequence $0 \to \mathbb{Z}_p \to \mathbb{Q}_p \to \mathbb{Q}_p/\mathbb{Z}_p \to 0$, in which the quotient is the discrete Prüfer group, dualises to $0 \to \mathbb{Z}_p \to \mathbb{Q}_p \to \mu_{p^\infty} \to 0$: the self-duality of $\mathbb{Q}_p$ exchanges the compact open subgroup $\mathbb{Z}_p$ and the discrete quotient $\mathbb{Q}_p/\mathbb{Z}_p$, whose dual is $\mathbb{Z}_p$, and is the model for the adelic self-duality.

**Example (the rationals and the Bohr compactification).** The discrete group $\mathbb{Q}$ has compact dual, the **Bohr compactification** $b\mathbb{Q}$ of $\mathbb{Q}$; it is a compact connected abelian group of infinite dimension, and it is the largest compact group containing $\mathbb{Q}$ as a dense subgroup. Its dual is $\mathbb{Q}$ with the discrete topology, and the inclusion $\mathbb{Q} \to b\mathbb{Q}$ dualises to the identity of the discrete dual; hence $b\mathbb{Q}$ is not a Lie group, being the dual of a discrete torsion-free group of infinite rank.

## Abelian Groups as Quotients, Limits and Dense Subgroups

### Inverse Limits

**Definition.** An **inverse system** of abelian topological groups is a directed set $I$ with groups $G_i$ and continuous homomorphisms $\varphi_{ij} : G_j \to G_i$ for $i \leq j$, compatible in the evident sense; its **inverse limit** is

$$
\varprojlim_i G_i = \Bigl\{(x_i) \in \prod_i G_i : \varphi_{ij}(x_j) = x_i \text{ for all } i \leq j\Bigr\},
$$

with the subspace topology.

**Theorem.** The inverse limit of compact abelian groups is a closed subgroup of the product, hence compact abelian; the inverse limit of discrete abelian groups is a closed subgroup of the product of discrete groups, hence totally disconnected and, when the system is countable and the groups finite, compact and profinite. Duality sends inverse limits to direct limits:

$$
\Bigl(\varprojlim_i G_i\Bigr)^\vee \cong \varinjlim_i G_i^\vee.
$$

**Proof.** The limit is the intersection of the closed sets on which the two coordinate projections agree, hence closed in the product; compactness and total disconnectedness pass to closed subgroups. The duality statement is the exactness of duality on the projections defining the limit; it is the statement that a character of the limit is a compatible family of characters, which is the direct limit of the duals. $\square$

**Example.** $\mathbb{Z}_p = \varprojlim_k \mathbb{Z}/p^k\mathbb{Z}$ is the inverse limit of finite groups, and its dual is the direct limit $\varinjlim_k \mu_{p^k} = \mu_{p^\infty}$. The profinite completion $\hat{\mathbb{Z}} = \varprojlim_n \mathbb{Z}/n\mathbb{Z} \cong \prod_p \mathbb{Z}_p$ has dual the discrete torsion group $\bigoplus_p \mu_{p^\infty} = \mathbb{Q}/\mathbb{Z}$; this is the statement that the character group of the profinite completion of $\mathbb{Z}$ is the torsion subgroup of the circle, the Q/Z of *Finitely Generated Abelian Groups*.

### Dense Subgroups and Completions

**Theorem.** Let $G$ be a locally compact abelian group and let $D \subseteq G$ be a dense subgroup. Then every character of $D$ is the restriction of at most one character of $G$, and the restriction map $G^\vee \to D^\vee$ is injective with image the characters of $D$ that are uniformly continuous for the uniformity inherited from $G$. In particular, when $G$ is compact, every character of $G$ restricts to a character of $D$, so that $G^\vee$ is isomorphic to a subgroup of $D^\vee$.

**Proof.** Two continuous characters of $G$ agreeing on a dense subset agree everywhere, since $S^1$ is Hausdorff; so restriction is injective. A restriction of a continuous character is uniformly continuous, and conversely a uniformly continuous character on $D$ extends uniquely to the completion by the universal property of the uniform completion, which is $G$ when $D$ is dense in $G$. $\square$

**Example.** The inclusion $\mathbb{Z} \to \mathbb{Z}_p$ dualises to the map $\mu_{p^\infty} \to S^1$ sending $\zeta$ to the character $n \mapsto \zeta^n$, which is the inclusion of the torsion subgroup of the circle; the inclusion $\mathbb{Q} \to \mathbb{R}$ has dense image, and its dual restriction maps $\mathbb{R}$ into the dual of the discrete group $\mathbb{Q}$. The **solenoid** $\Sigma_p$ is the dual of $\mathbb{Z}[1/p]$, the group of rationals whose denominator is a power of $p$; the inclusion $\mathbb{Z} \to \mathbb{Z}[1/p]$ dualises to a surjection $\Sigma_p \to S^1$ whose kernel is a copy of $\mathbb{Z}_p$, exhibiting the solenoid as a compact one-dimensional group that is not a Lie group.

## The Boundary with Harmonic Analysis

The theory above is the *structure* theory of abelian topological groups: it describes the objects, their duals and the correspondence between them, and it is complete without any integration. The next steps in the classical development use the Haar measure and the integration of Part III, and they are deliberately not taken here.

- The **Fourier transform** $\hat f(\chi) = \int_G f(x)\overline{\chi(x)}\,dx$ requires the integral and the $L^p$ spaces; it is treated in Part III, together with the inversion theorem and the Plancherel theorem for a locally compact abelian group.
- The **convolution algebra** $L^1(G)$ and its relation to the dual is likewise Part III; the finite case, in which convolution is a finite sum and the transform is the discrete Fourier transform, is the content of *Representations of Groups* and is used here only as the motivating example.
- **Positive definite functions**, the Gelfand–Raĭkov theorem and the construction of Haar measure itself are stated where they are needed from the standard literature; the measure and its invariance are the subject, and the analytic consequences are Part III.

## Summary

An abelian topological group is an abelian group with continuous addition and negation; it is homogeneous, its left and right uniformities coincide, and it is always unimodular. Its continuous homomorphisms to the circle form the character group $G^\vee$, a group under pointwise multiplication with the compact-open topology; the dual is compact, discrete or locally compact exactly as $G$ is discrete, compact or locally compact, and the characters separate points. Annihilators turn closed subgroups into quotients and quotients into closed subgroups, so that duality is exact and inverts the lattice of closed subgroups.

The structure theorem gives every locally compact abelian group an open subgroup $\mathbb{R}^n \times K$ with $K$ compact — equivalently $G \cong \mathbb{R}^n \times G_1$ with $G_1$ containing a compact open subgroup — and describes every compactly generated one as $\mathbb{R}^n \times \mathbb{Z}^m \times K$ with $K$ compact, the compact factor being finite exactly when there is no infinite compact subgroup; the proof uses the solution of Hilbert's fifth problem in the abelian case and van Dantzig's theorem for the totally disconnected part. The extreme cases are dual to each other: a discrete group has compact dual and a compact group has discrete dual, the paradigm being the exchange of $S^1$ with $\mathbb{Z}$ and of $\mathbb{Z}_p$ with the Prüfer group $\mu_{p^\infty}$. Inverse limits of compact groups are compact, and duality sends inverse limits to direct limits, so the profinite completion $\hat{\mathbb{Z}}$ is dual to the torsion group $\mathbb{Q}/\mathbb{Z}$.

Pontryagin duality, stated here, asserts that evaluation $G \to G^{\vee\vee}$ is an isomorphism of topological groups for every locally compact abelian group, so that the category of such groups is equivalent to its own opposite with compactness and discreteness exchanged. Everything requiring the integral, the Fourier transform, the convolution algebra or the Plancherel theorem belongs in Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $x$, $y$ | An abelian topological group, written additively, and its elements |
| $0$, $-x$, $x + y$ | Identity, inverse and sum in the additive notation |
| $G_0$ | Identity component of $G$, a closed subgroup |
| $G/H$ | Quotient by a subgroup, with the quotient topology |
| $S^1 = \mathbb{R}/\mathbb{Z}$ | The circle group, written multiplicatively |
| $G^\vee$, $\chi$ | Character group (Pontryagin dual) and a character $G \to S^1$ |
| $H^\perp$ | Annihilator of a subgroup $H \subseteq G$ in $G^\vee$ |
| $\iota_G : G \to G^{\vee\vee}$ | Evaluation map, an isomorphism by Pontryagin duality |
| $\mathbb{R}^n \times K$ | Open subgroup of a locally compact abelian group, $K$ compact |
| $\mathbb{R}^n \times G_1$ | Structure of a locally compact abelian group, $G_1$ with a compact open subgroup |
| $\mathbb{R}^n \times \mathbb{Z}^m \times K$ | Structure of a compactly generated locally compact abelian group, $K$ compact (finite iff no infinite compact subgroup) |
| $T^n = \mathbb{R}^n/\mathbb{Z}^n$ | The $n$-torus, compact and connected |
| $\mathbb{Z}_p$, $\mathbb{Q}_p$, $\mu_{p^\infty}$ | $p$-adic integers, $p$-adic numbers, Prüfer group |
| $\hat{\mathbb{Z}} = \varprojlim_n \mathbb{Z}/n\mathbb{Z}$ | Profinite completion of $\mathbb{Z}$; $\hat{\mathbb{Z}} \cong \prod_p \mathbb{Z}_p$ |
| $\Sigma_p$ | Solenoid $\varprojlim_k(S^1 \xrightarrow{p} S^1)$, dual to $\mathbb{Z}[1/p]$ |
| $b\mathbb{Q}$ | Bohr compactification of the discrete group $\mathbb{Q}$ |
| $\varprojlim$, $\varinjlim$ | Inverse and direct limits of groups |
| $\mathbb{R}_{>0}$, $\Delta$ | Positive reals; the modular function, trivial for abelian groups |
| $\mu$, $dx$ | Haar measure and its notation; the measure is constructed in the companion article |





## Further Reading

- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, 2nd ed. 1966), for the classical development of characters and the structure of locally compact abelian groups.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, 2nd ed. 1979), for the structure theorem, duality and the standard examples in full detail.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for a concise account of duality and invariant integration.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962; reprinted Wiley, 1990), for the harmonic analysis of locally compact abelian groups.
- Sidney A. Morris, *Pontryagin Duality and the Structure of Locally Compact Abelian Groups* (Cambridge University Press, 1977), for the structure theorem, solenoids and the Bohr compactification.
- Karl H. Hofmann and Sidney A. Morris, *The Structure of Compact Groups* (De Gruyter, 3rd ed. 2013), for the structure of compact and locally compact groups and their duals.
- David L. Armacost, *The Structure of Locally Compact Abelian Groups* (Marcel Dekker, 1981), for the classification of the locally compact abelian groups by their duals.
- J. Frank Adams, *Lectures on Lie Groups* (University of Chicago Press, 1969), for the structure of abelian Lie groups and the tori among them.
