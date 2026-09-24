
# __Property (T)__

## Introduction

**Kazhdan's property (T)** is a rigidity property of a locally compact group: the trivial one-dimensional representation is isolated in the unitary dual. Equivalently, if a unitary representation is close to the trivial representation on a compact generating set — if it has **almost invariant vectors** — then it has a nonzero invariant vector. The property was isolated by Kazhdan in order to prove that a lattice in a simple Lie group of real rank at least two is finitely generated, and it has since become the basic tool in the rigidity theory of lattices, arithmetic groups and their profinite quotients, in the construction of expanding families of finite graphs, and in the theory of group von Neumann algebras.

The article develops the definition and its formulations, the fixed-point characterisation for affine isometric actions due to Delorme and Guichardet, the principal examples and non-examples, the heredity properties and the rigidity consequences — finite generation, finiteness of the abelianisation, and the spectral gap — and the contrast with amenability and with the Haagerup property. The group is a locally compact group $G$ with Haar measure $dg$ as in *Locally Compact Groups and Haar Measure*; the unitary representations, the unitary dual $\operatorname{Irr}(G)$ and Schur's lemma are those of *Representation Theory of Locally Compact Groups*; the group cohomology used in the cohomological characterisation is that of *Group Cohomology* in Part I and the induced representations and Mackey theory are those of the companion articles of this category. A **lattice** in $G$ is, as standard, a discrete subgroup $\Gamma \leq G$ for which the homogeneous space $G/\Gamma$ carries a finite invariant measure; the theory of lattices in Lie groups is developed in with this one, and is not used here beyond the definition.

The boundary with Part III is the one fixed in the representation-theoretic block. What is developed here is the representation-theoretic property: the Kazhdan pair, the equivalent formulations, the cohomological vanishing, the heredity and the consequences. What is deferred is the **analytic and ergodic** content: the strong ergodicity of the action of a (T) group on a measure space, the spectral gap of the Laplacian on a quotient, the mixing and equidistribution theorems, the measured-group-theoretic applications and the explicit construction of expander families from the spectral gap, all of which belong to *Analysis on Groups* and in Part III, where the measure and the limit are available. The Cayley graph is introduced in line as the standard graph of a finitely generated group, since the group-theoretic formulation of the spectral gap is clearest there. No physics is invoked.

## Kazhdan's Definition

### Almost Invariant Vectors

**Definition.** Let $\pi$ be a unitary representation of a locally compact group $G$ on a Hilbert space $\mathcal{H}$. A vector $\xi \in \mathcal{H}$ is **invariant** if $\pi(g)\xi = \xi$ for all $g \in G$. For a compact subset $Q \subseteq G$ and $\varepsilon > 0$, a vector $\xi$ with $\|\xi\| = 1$ is **$(Q, \varepsilon)$-invariant** if

$$
\sup_{g \in Q} \|\pi(g)\xi - \xi\| < \varepsilon .
$$

The representation $\pi$ **almost has invariant vectors** if for every compact $Q$ and every $\varepsilon > 0$ there is a unit $(Q,\varepsilon)$-invariant vector. The trivial representation $1_G$ is **weakly contained** in $\pi$, written $1_G \prec \pi$, if the matrix coefficients of $1_G$ are limits of matrix coefficients of $\pi$ uniformly on compacta; equivalently, if $\pi$ almost has invariant vectors.

**Definition (Kazhdan).** A locally compact group $G$ has **property (T)** if there is a compact subset $Q \subseteq G$ and a number $\varepsilon > 0$ such that every unitary representation of $G$ with a $(Q,\varepsilon)$-invariant vector has a nonzero invariant vector. The pair $(Q, \varepsilon)$ is then a **Kazhdan pair**.

**Theorem (equivalent formulations).** For a locally compact group $G$ the following are equivalent:

**(a)** $G$ has property (T);

**(b)** every unitary representation of $G$ that almost has invariant vectors has a nonzero invariant vector;

**(c)** the trivial representation $1_G$ is an isolated point of the unitary dual $\operatorname{Irr}(G)$ in the Fell topology;

**(d)** whenever $1_G \prec \pi$, the trivial representation is a subrepresentation of $\pi$;

**(e)** $G$ is compactly generated and there is a compact generating set $Q$ and $\varepsilon > 0$ with the Kazhdan property.

**Proof.** (a) $\Rightarrow$ (b) is the definition: a representation with almost invariant vectors has a $(Q,\varepsilon)$-invariant vector for the Kazhdan pair, hence an invariant vector. (b) $\Rightarrow$ (d): if $1_G \prec \pi$ then $\pi$ almost has invariant vectors, so it contains an invariant vector, and the one-dimensional subspace spanned by it is a copy of $1_G$. (d) $\Rightarrow$ (c): a net of irreducibles converging to $1_G$ in the Fell topology satisfies $1_G \prec \bigoplus_i\pi_i$ for the sum of the net, so by (d) the sum contains $1_G$ as a subrepresentation, whence one $\pi_i$ is $1_G$ for a cofinal part of the net; this is exactly isolation. (c) $\Rightarrow$ (a): isolation in the Fell topology means there is a compact $Q$ and $\varepsilon>0$ such that no irreducible except $1_G$ has a $(Q,\varepsilon)$-invariant vector; passing to a general representation by decomposing it into irreducibles and using that a $(Q,\varepsilon)$-invariant vector of a direct sum is approximated by finitely many components gives (a). (e) is a restatement of (a) with the observation, proved below, that (T) implies compact generation. The equivalences are the standard ones of the theory. $\square$

**Remark.** The compactness of the generating set in the definition is essential: without it the condition would be vacuous for a discrete group generated by an infinite set. The equivalence of (c) explains the name: property (T) is the isolation of the *trivial* representation, and the corresponding isolation of an arbitrary point of the dual is the property often called rigidity of that point.

### Invariant Vectors and the Orthogonal Complement

**Proposition.** If $\pi$ has a nonzero invariant vector then the subspace of invariant vectors, $\mathcal{H}^G = \{\xi : \pi(g)\xi = \xi\ \forall g\}$, is a closed invariant subspace, and $\pi$ splits as $\pi^G \oplus \pi_0$ with $\pi_0$ having no nonzero invariant vector. Property (T) is the statement that for the Kazhdan pair the two alternatives "$\pi$ has a nonzero invariant vector" and "$\pi$ has no $(Q,\varepsilon)$-invariant vector" are exhaustive for every unitary representation.

**Proof.** The set of invariant vectors is closed, being the intersection over $g \in G$ of the closed sets $\{\xi : \pi(g)\xi = \xi\}$, and it is invariant. The orthogonal complement is invariant, because for $g \in G$ and $\eta \perp \mathcal{H}^G$, $\langle \pi(g)\eta, \xi\rangle = \langle \eta, \pi(g)^{-1}\xi\rangle = \langle\eta,\xi\rangle = 0$ for $\xi \in \mathcal{H}^G$. The decomposition is the orthogonal decomposition. The last statement is a restatement of the definition. $\square$

**Example (compact groups).** A compact group has property (T): the trivial representation is isolated because every unitary representation has a nonzero invariant vector, obtained by averaging a vector over the group using the normalised Haar measure of *Locally Compact Groups and Haar Measure*. The Kazhdan pair can be taken to be $(G, \sqrt{1/2})$ for the normalised Haar measure, since a vector whose translates move by less than $\sqrt{1/2}$ on average has a nonzero average.

**Example (the additive line).** $G = \mathbb{R}$ does not have (T). The characters $\chi_\xi(x) = e^{2\pi i\xi x}$ converge to the trivial character as $\xi \to 0$ in the Fell topology, and each is irreducible and nontrivial; by the equivalence (c) the trivial representation is not isolated. Equivalently, for $Q = [-1,1]$ and any $\varepsilon > 0$ a unit vector in the one-dimensional space of $\chi_\xi$ is $(Q,\varepsilon)$-invariant as soon as $|\xi|$ is small, and the representation has no nonzero invariant vector unless $\xi = 0$.

## The Fixed-Point and Cohomological Characterisations

### Affine Isometric Actions

**Definition.** An **affine isometric action** of $G$ on a Hilbert space $\mathcal{H}$ is a map $\alpha : G \times \mathcal{H} \to \mathcal{H}$ such that for each $g$ the map $\alpha_g$ is an isometry of the affine structure and $\alpha_{gh} = \alpha_g\alpha_h$. Every such action is of the form

$$
\alpha_g(v) = \pi(g)v + b(g)
$$

for a unitary representation $\pi$ (the **linear part**) and a **cocycle** $b : G \to \mathcal{H}$:

$$
b(gh) = b(g) + \pi(g)b(h) \qquad \text{for all } g, h \in G ,
$$

with $\pi$ and $b$ continuous in the appropriate sense. A **fixed point** of the action is a vector $v_0$ with $\alpha_g(v_0) = v_0$ for all $g$, equivalently a vector $v_0$ with $b(g) = v_0 - \pi(g)v_0$ for all $g$, that is, a **coboundary** $b = \delta v_0$.

**Lemma (bounded cocycles are coboundaries).** Let $\alpha_g(v) = \pi(g)v + b(g)$ be a continuous affine isometric action of $G$ on a Hilbert space $\mathcal{H}$. If the orbit of some (equivalently, every) vector is bounded, then $b$ is a coboundary and the action has a fixed point.

**Proof.** Let $C$ be the closed convex hull of the orbit of a vector $v$; by hypothesis $C$ is bounded, closed and convex, and it is invariant. A bounded closed convex subset of a Hilbert space has a unique point $v_0$ of least norm. For each $g \in G$ the point $\alpha_g(v_0)$ lies in $C$, and so does the midpoint $(\alpha_g(v_0)+v_0)/2$, whose norm is at least $\|v_0\|$. The parallelogram identity gives

$$
\Bigl\|\tfrac{1}{2}\bigl(\alpha_g(v_0)+v_0\bigr)\Bigr\|^2 = \|v_0\|^2 - \tfrac{1}{4}\|\alpha_g(v_0)-v_0\|^2 ,
$$

so the left side is $\geq \|v_0\|^2$ only if $\alpha_g(v_0) = v_0$. Hence $v_0$ is a fixed point, and $b(g) = v_0 - \pi(g)v_0$. $\square$

**Theorem (fixed-point characterisation).** A locally compact group $G$ has property (T) if and only if every continuous affine isometric action of $G$ on a Hilbert space has a fixed point.

**Proof sketch.** By the lemma, an affine action fails to have a fixed point exactly when its orbits are unbounded, so the theorem is the statement that $G$ has (T) if and only if every continuous $1$-cocycle of $G$ is **bounded**, that is, $\sup_{g\in Q}\|b(g)\| < \infty$ for every compact $Q$. That (T) forces boundedness is the averaging argument: if $b$ were unbounded, the standard computation along the vectors $b(g_n)$ for a sequence $g_n$ with $\|b(g_n)\| \to \infty$ produces unit vectors almost fixed by the Kazhdan pair, hence a nonzero invariant vector, which the cocycle identity forbids — the construction is carried out uniformly on $Q$ and contradicts the Kazhdan pair. That boundedness of all cocycles forces (T) is the converse construction: a representation with almost invariant vectors but no invariant vector yields the cocycle $b(g) = \lim_n (\pi(g)\xi_n - \xi_n)$ along a suitable diagonal subsequence, and this cocycle is unbounded precisely because $\pi$ has no invariant vector, so the action obtained from it has no fixed point. The two estimates are the content of the theorem of Delorme and Guichardet and are quoted from the literature. $\square$

### Delorme–Guichardet

**Theorem (Delorme–Guichardet).** For a locally compact $\sigma$-compact group $G$, property (T) is equivalent to either of the following:

**(a)** every continuous affine isometric action of $G$ on a Hilbert space has a fixed point;

**(b)** for every unitary representation $\pi$ of $G$, the first cohomology with coefficients in $\pi$ vanishes: $H^1(G,\pi) = 0$, that is, every continuous $1$-cocycle $b : G \to \mathcal{H}_\pi$ is a coboundary $b(g) = \pi(g)v - v$ for some $v \in \mathcal{H}_\pi$.

**Proof.** The equivalence of (a) with (b) is the translation of the previous paragraph: a continuous $1$-cocycle with coefficients in $\pi$ is exactly the translational part of an affine isometric action with linear part $\pi$, and a fixed point is exactly a vector $v$ with $b = \delta v$. The equivalence with (T) is the theorem of Delorme and Guichardet, proved by the argument of the previous theorem in both directions; the cohomological formulation makes the property a vanishing statement in group cohomology with coefficients in a representation, in the sense of *Group Cohomology* in Part I, and the vanishing of $H^1$ is often the cleanest way to verify (T) for a specific group. The theorem is quoted as standard. $\square$

**Corollary.** If $G$ has property (T) then $G$ admits no continuous homomorphism onto an additive group $\mathcal{H}$ of a Hilbert space, viewed as a group of translations of $\mathcal{H}$: such a homomorphism would define an affine isometric action of $G$ with no fixed point. In particular $G$ has no quotient isomorphic to $\mathbb{R}^n$ or to $\mathbb{Z}^n$ with $n \geq 1$.

## Examples and Non-Examples

### Groups with Property (T)

**Theorem (Kazhdan).** Let $G$ be a connected semisimple Lie group with finite centre, all of whose simple factors have real rank at least two. Then $G$ has property (T). In particular:

**(a)** $SL_n(\mathbb{R})$ and $SL_n(\mathbb{C})$ have (T) for $n \geq 3$, since their real rank is $n-1 \geq 2$;

**(b)** $Sp_{2n}(\mathbb{R})$ has (T) for $n \geq 2$, since its real rank is $n \geq 2$;

**(c)** the compactly generated groups with (T) include the compact groups, the finite groups and the lattices in the above groups.

**Proof sketch.** The proof of Kazhdan's theorem for a semisimple Lie group uses the structure theory of Part I: the Lie algebra decomposes into simple factors, the Cartan decomposition $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$ exhibits $G$ as compactly generated, and the *Mautner phenomenon* — an invariant vector under a one-parameter subgroup of a representation is invariant under the whole group whenever the subgroup is not contained in a compact subgroup — reduces the isolation of the trivial representation to a computation with the root spaces. If every simple factor has real rank at least two, then in each factor the commutator of two opposed root subgroups generates the factor, and a vector that is almost fixed on a compact generating set is shown to be almost fixed on a larger and larger set until the Mautner phenomenon applies. The details are Kazhdan's original argument and are quoted from the literature. (a) and (b) are the cases $SL_n$ and $Sp_{2n}$; (c) is the heredity proved below. $\square$

**Remark.** The rank hypothesis is sharp: if a simple factor of $G$ has real rank one, then (T) passes to the quotient $G \to$ that factor by the heredity theorem below, and the factor does not have (T), so neither does $G$. The rank-one simple groups $SL_2(\mathbb{R}) \cong SO(2,1)$, $SO(n,1)$ for $n \geq 2$, $SU(n,1)$ for $n \geq 2$, $Sp(n,1)$ and the exceptional $F_4^{-20}$ all have the Haagerup property and no (T). The exceptional behaviour of the rank-one groups is the reason the theory of lattices in semisimple groups splits into the higher-rank case, where (T) and rigidity hold, and the rank-one case, where the geometry of the associated symmetric space is used instead.

**Example ($SL_3(\mathbb{Z})$ and $SL_n(\mathbb{Z})$).** The discrete group $SL_n(\mathbb{Z})$ has property (T) for $n \geq 3$. This follows from Kazhdan's theorem for $SL_n(\mathbb{R})$ together with the heredity of (T) from a group to its lattices, proved below, because $SL_n(\mathbb{Z})$ is a lattice in $SL_n(\mathbb{R})$; the discreteness is elementary and the finite covolume is the reduction theory. The group $SL_2(\mathbb{Z})$ does not have (T), being virtually free.

### Groups without Property (T)

**Theorem (folklore).** The following groups do not have property (T):

**(a)** $\mathbb{R}^n$, $\mathbb{Z}^n$ and every non-compact abelian group;

**(b)** every infinite amenable group, and more generally every non-compact group that is amenable;

**(c)** the free group $F_2$ and the free products of finite groups other than the infinite dihedral group; note that a group with (T) may nevertheless contain free subgroups — $SL_3(\mathbb{Z})$ has (T) and does — since (T) is not inherited by closed subgroups of infinite covolume;

**(d)** $SL_2(\mathbb{Z})$, $SL_2(\mathbb{R})$, and every simple Lie group of real rank one;

**(e)** every group with the Haagerup property.

**Proof.** (a) The characters of $\mathbb{R}^n$ converge to the trivial representation, so it is not isolated; the same computation applies to a closed subgroup, and a non-compact abelian group has $\mathbb{R}$ or $\mathbb{Z}$ as a quotient, so the quotient dual converges and the group has no (T) since (T) passes to quotients. (b) An amenable group has the Følner property, which gives almost invariant vectors for the left regular representation; if the group is not compact the representation has no nonzero invariant vector, so (T) fails. (c) A free group acts properly on its Cayley tree, and the associated cocycle gives a proper affine isometric action on a Hilbert space with no fixed point — the Haagerup property of the free groups, stated below; by Delorme–Guichardet (T) fails, and (T) passes to finite-covolume subgroups, so the failure is inherited by any group in which $F_2$ has finite covolume. (d) $SL_2(\mathbb{R})$ has real rank one and acts on the hyperbolic plane; the same cocycle argument with the Busemann cocycle on the boundary circle shows the failure of (T), and $SL_2(\mathbb{Z})$ is virtually free. (e) The Haagerup property is the existence of a proper affine isometric action on a Hilbert space, which is incompatible with (T) by the fixed-point characterisation; the two properties are in fact opposite in the sense made precise below. $\square$

**Example (the failure of isolation).** For $G = \mathbb{R}$ the dual is $\mathbb{R}$ with the topology of $\mathbb{R}$, and the trivial character is not isolated: the neighbourhoods of $1_G$ in $\operatorname{Irr}(\mathbb{R})$ are the sets $\{\chi_\xi : |\xi| < \delta\}$, none of which is a single point. For $G = F_2$ the dual is a wild Borel space — the group is not of type I, a standard fact recorded in the literature (Bekka–de la Harpe–Valette, *Kazhdan's Property (T)*) — and the trivial representation is not isolated; equivalently the Cayley tree of $F_2$ carries a proper action with a proper cocycle.

## Heredity and Consequences

### Lattices, Quotients and Subgroups

**Theorem (heredity).** Let $G$ be a locally compact group with property (T).

**(a)** Every quotient $G/N$ of $G$ by a closed normal subgroup has (T).

**(b)** Every closed subgroup $H \leq G$ with finite covolume, in particular every lattice in $G$, has (T). For a discrete group, (T) passes from a finite-index subgroup to the whole group, and from the group to every finite-index subgroup.

**(c)** A finite direct product of groups with (T) has (T), and a group is (T) if and only if both factors are, for a product of two locally compact groups.

**Proof.** (a) A unitary representation of $G/N$ is a representation of $G$ trivial on $N$; invariance and almost-invariance are computed in the quotient, and an invariant vector for $G$ is one for $G/N$. (b) Let $H \leq G$ have finite covolume and let $\pi$ be a unitary representation of $H$ with a $(Q,\varepsilon)$-invariant vector $v$. Because $G/H$ carries a finite $G$-invariant measure, the constant section with value $v$ has finite norm in the induced space, and a standard partition-of-unity construction on $G/H$ produces a unit vector of $\operatorname{Ind}_H^G\pi$ almost fixed on a Kazhdan set of $G$; by (T) of $G$ the induced representation contains a nonzero $G$-invariant vector $f$. In the function-space realisation a $G$-invariant function is constant, $f(g) = f(e)$ for all $g$, and the equivariance condition $f(gh) = \pi(h)^{-1}f(g)$ then forces $f(e)$ to be $H$-invariant; since $f \neq 0$, the representation $\pi$ has a nonzero invariant vector. This is the argument in the cocompact case; for the general finite-covolume case the same construction is carried out with the measurable fundamental domain and uses the finite invariant measure on $G/H$ whose existence is the definition of finite covolume, and the bookkeeping is the measured-group theory of Part III. For a discrete group the finite-index cases are immediate from this. (c) A representation of $G_1\times G_2$ with almost invariant vectors restricts to each factor with almost invariant vectors, and the double average of an almost invariant vector over $G_1$ and $G_2$ produces an invariant vector; the converse is (a). $\square$

**Corollary (Kazhdan's application).** If $\Gamma$ is a lattice in a group $G$ with (T) then $\Gamma$ is finitely generated; more precisely $\Gamma$ has (T) and a group with (T) is compactly generated. In particular a lattice in $SL_n(\mathbb{R})$ for $n \geq 3$ is finitely generated, and the same holds for the higher-rank semisimple groups.

### Finite Generation and the Abelianisation

**Theorem.** Let $G$ be a locally compact group with property (T). Then $G$ is compactly generated, and if $G$ is discrete it is finitely generated; moreover the abelianisation $G^{\mathrm{ab}} = G/[G,G]$ is compact (finite in the discrete case).

**Proof.** Compact generation: if $G$ is not compactly generated, the family of subgroups generated by increasing compact sets gives a net of proper open subgroups and a unitary representation of $G$ weakly containing the trivial representation without containing it — for instance, the quasiregular representation on the coset space of an exhausting sequence of open subgroups — contradicting (T); the standard proof uses the left regular representation of the quotient. Abelianisation: the quotient $G^{\mathrm{ab}}$ has (T) by heredity (a), and a locally compact abelian group with (T) is compact, because for a non-compact abelian group the dual contains a net converging to the trivial character; a compact abelian group has (T). Hence $G^{\mathrm{ab}}$ is compact, and for discrete $G$ it is a compact discrete group, that is finite. $\square$

**Corollary (rigidity of homomorphisms).** Let $G$ be a discrete group with property (T). Then every homomorphism $G \to A$ into a virtually abelian group has image contained in a finite subgroup when $A$ is discrete. In particular $G$ has no surjection onto $\mathbb{Z}$, no surjection onto a free group, and its first Betti number vanishes.

**Proof.** The image is a quotient of $G$, hence has (T), and it lies in a virtually abelian group; a virtually abelian group with (T) is finite, as in the previous proof, since it is a finite extension of an abelian group with (T). For a free image the argument is the same in spirit: a finitely generated free group has the Haagerup property, hence cannot have (T) unless it is compact, so no nontrivial free group is a quotient of a (T) group. The vanishing of the first Betti number is the case $A = \mathbb{Z}$. $\square$

### Spectral Gap

**Definition.** Let $G$ be a compactly generated locally compact group with a compact generating set $S$ that is symmetric and contains the identity, and let $\mu$ be a probability measure supported on $S$, for instance the normalised restriction of the Haar measure. For a unitary representation $\pi$ of $G$ write $\pi(\mu) = \int \pi(g)\,d\mu(g)$ for the averaging operator, a contraction of $\mathcal{H}_\pi$. The representation has a **spectral gap** if the spectrum of $\pi(\mu)$ on the orthogonal complement of the invariant vectors is bounded away from $1$; the gap is the distance from $1$ to that spectrum.

**Theorem (spectral gap characterisation).** A locally compact group $G$ has property (T) if and only if for some (equivalently, every) compact symmetric generating set the corresponding averaging operator has a spectral gap uniformly over all unitary representations without nonzero invariant vectors.

**Proof.** If $G$ has (T) with Kazhdan pair $(Q,\varepsilon)$, take a generating set $S$ and a measure $\mu$ such that every $(S,\delta)$-invariant vector is $(Q,\varepsilon)$-invariant; a vector almost fixed by $\pi(\mu)$ is almost invariant on $S$, hence has an invariant vector. Conversely, a uniform spectral gap for the averaging operator gives a Kazhdan pair: a $(Q,\varepsilon)$-invariant vector produces a vector nearly fixed by $\pi(\mu^n)$ for suitable $n$, and the gap bounds $\|\pi(\mu^n)\xi\|$ away from $\|\xi\|$ in the absence of invariant vectors. $\square$

**Example (expanders from a (T) group).** Let $G$ be a finitely generated discrete group with (T), for instance $SL_3(\mathbb{Z})$, and let $S$ be a finite symmetric generating set. For a family of finite quotients $G \to G_i$ with $|G_i| \to \infty$, the Cayley graphs of the $G_i$ with respect to the images of $S$ form an **expander family**: the spectral gap of the regular representation of $G_i$ is bounded below by the Kazhdan constant. The classical instance is the family $SL_3(\mathbb{Z}/m\mathbb{Z})$ with $m$ running over the integers, whose expansion follows from (T) of $SL_3(\mathbb{Z})$ together with the congruence subgroup property. The graph-theoretic and analytic consequences — Cheeger constants, mixing rates, the counting of rational points — are the ergodic and analytic theory of Part III.

## Property (T) and its Complements

### The Haagerup Property and Amenability

**Definition.** A locally compact group $G$ has the **Haagerup property** if there is a proper continuous affine isometric action of $G$ on a Hilbert space; equivalently, if there is a net of continuous positive definite functions vanishing at infinity and converging pointwise to $1$.

**Theorem.** A group with property (T) and the Haagerup property is compact. The two properties are therefore mutually exclusive for non-compact groups, and a non-compact group with (T) has no proper affine isometric action on a Hilbert space.

**Proof.** By the fixed-point characterisation, a group with (T) has a fixed point for every affine isometric action; by the Haagerup property it has a proper one. A fixed point of a proper action exists only if the group is compact: the orbit of the fixed point is a single point, and properness forces the group to be compact. $\square$

**Corollary (the contrast).** The infinite amenable groups and the free groups have the Haagerup property and hence no (T); the higher-rank semisimple groups have (T) and hence no proper affine action on a Hilbert space. The two classes are the extremes of a spectrum of approximation properties: at one end the groups approximable by actions with fixed points (amenable, Haagerup), at the other the groups for which every such action has a fixed point (Kazhdan).

**Remark.** Property (T) is not the negation of amenability: there are groups that are neither amenable nor (T), for instance the rank-one simple groups $SO(n,1)$ and $SU(n,1)$ with $n \geq 2$, which have the Haagerup property but are non-amenable. The class of (T) groups is also separated from the class of non-amenable groups by the approximation properties: the Haagerup groups approximate the trivial representation by actions with fixed points, the (T) groups admit no such approximation.

## The Boundary with Analysis

- The **strong ergodicity** of an action of a (T) group on a probability space, the **spectral gap** of the Laplacian on a homogeneous space, and the mixing, equidistribution and counting theorems that follow areand *Analysis on Groups* in Part III, where the measure, the limit and the $L^2$ spaces are available.
- The **construction of expander families**, the Cheeger inequalities and the combinatorial applications belong to the analytic and ergodic theory of Part III.
- The **operator-algebraic consequences** — the type of the group von Neumann algebra, the structure of the group $C^*$-algebra and the property of the reduced group $C^*$-algebra — are developed in *Topology on Linear Algebras* , and are quoted from the literature where used.
- What is *not* deferred: the Kazhdan pair, the equivalent formulations of (T), the fixed-point and cohomological characterisations, the classification of the examples and non-examples at the level of the groups, the heredity, the finite-generation and abelianisation consequences, and the spectral-gap formulation.

## Summary

A locally compact group $G$ has property (T) if there is a compact set $Q$ and an $\varepsilon > 0$ such that every unitary representation with a $(Q,\varepsilon)$-invariant unit vector has a nonzero invariant vector. Equivalently, every representation almost having invariant vectors has an invariant vector; equivalently the trivial representation is an isolated point of the unitary dual. By Delorme–Guichardet, (T) is equivalent to the existence of a fixed point for every continuous affine isometric action on a Hilbert space, and to the vanishing of the first cohomology $H^1(G,\pi) = 0$ for every unitary representation $\pi$.

The principal examples are the compact groups, the connected semisimple Lie groups of real rank at least two and with no rank-one factor — in particular $SL_n(\mathbb{R})$ and $Sp_{2n}(\mathbb{R})$ for the stated ranges — and the lattices in them, such as $SL_n(\mathbb{Z})$ for $n \geq 3$; compact groups are (T) because every representation has an invariant vector. The non-examples include the non-compact abelian groups, the infinite amenable groups, the free groups, and the real-rank-one simple groups $SL_2(\mathbb{R})$ and $SO(n,1)$; the free groups and the real-rank-one groups have the Haagerup property, which is incompatible with (T) for a non-compact group.

Property (T) passes to quotients, to lattices and finite-covolume subgroups, and to finite-index subgroups of a discrete group, and it is preserved by finite direct products; it is not inherited by closed subgroups of infinite covolume, so a (T) group may contain a free subgroup. It implies compact generation — finite generation for discrete groups — and finiteness of the abelianisation, so a (T) group has no homomorphism onto $\mathbb{Z}$ and vanishing first Betti number. For a compactly generated group the property is equivalent to a uniform spectral gap of the averaging operator over a generating measure, which is the mechanism by which (T) groups produce expander families of finite quotients. The ergodic, analytic and operator-algebraic consequences belong to Part III .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $Q$ | Locally compact group; compact subset used for the Kazhdan pair |
| $\pi$, $\mathcal{H}_\pi$ | Unitary representation and its Hilbert space |
| $(Q,\varepsilon)$-invariant | $\sup_{g\in Q}\|\pi(g)\xi - \xi\| < \varepsilon$ for a unit vector $\xi$ |
| Kazhdan pair $(Q,\varepsilon)$ | Compact $Q$, $\varepsilon>0$ defining property (T) |
| property (T) | Every representation with a $(Q,\varepsilon)$-invariant vector has an invariant vector |
| $1_G \prec \pi$ | The trivial representation is weakly contained in $\pi$ |
| $\mathcal{H}^G$ | Closed subspace of invariant vectors |
| $\alpha_g(v) = \pi(g)v + b(g)$ | Affine isometric action with linear part $\pi$ and cocycle $b$ |
| $b(gh) = b(g) + \pi(g)b(h)$ | Cocycle identity |
| $H^1(G,\pi) = 0$ | Delorme–Guichardet cohomological form of (T) |
| Haagerup property | Existence of a proper affine isometric action on a Hilbert space |
| $\pi(\mu) = \int\pi(g)d\mu(g)$ | Averaging operator over a generating probability measure |
| spectral gap | Spectrum of $\pi(\mu)$ bounded away from $1$ off the invariant vectors |
| lattice | Discrete subgroup $\Gamma$ with $G/\Gamma$ of finite invariant measure |
| $G^{\mathrm{ab}} = G/[G,G]$ | Abelianisation; compact (finite for discrete) if $G$ has (T) |
| $F_2$ | Free group on two generators; no (T) |
| $SL_n(\mathbb{Z})$ | Lattice in $SL_n(\mathbb{R})$; has (T) for $n \geq 3$ |
| $SO(n,1)$, $SU(n,1)$, $SL_2(\mathbb{R})$ | Real-rank-one groups; Haagerup, no (T) |
| Cayley graph | Graph of a finitely generated group with respect to a finite generating set, defined in *Graph Theory*, above this article in the menu |



## Further Reading

- David A. Kazhdan, *On the connection between the dual space of a group and the structure of its closed subgroups*, Functional Analysis and its Applications 1 (1967), 63–65, for the original definition and the higher-rank theorem.
- Pierre Delorme, *1-cohomologie des représentations unitaires des groupes de Lie semi-simples et résolubles*, Bulletin de la Société Mathématique de France 105 (1977), 281–336, for the fixed-point and cohomological characterisation.
- Alain Guichardet, *Sur la cohomologie des groupes topologiques II*, Bulletin des Sciences Mathématiques 96 (1972), 305–332, for the cohomological characterisation.
- Bachir Bekka, Pierre de la Harpe and Alain Valette, *Kazhdan's Property (T)* (Cambridge University Press, 2008), for the systematic modern account, the examples and the applications.
- Pierre de la Harpe and Alain Valette, *La propriété (T) de Kazhdan pour les groupes localement compacts* (Astérisque 175, 1989), for the locally compact theory and the expander applications.
- Uffe Haagerup, *An example of a non nuclear $C^*$-algebra, which has the metric approximation property*, Inventiones Mathematicae 50 (1979), 279–293, for the Haagerup property and its incompatibility with (T).
- Gregory Margulis, *Discrete Subgroups of Semisimple Lie Groups* (Springer, 1991), for the rigidity applications and the expander construction.
- Robert J. Zimmer, *Ergodic Theory and Semisimple Groups* (Birkhäuser, 1984), for the ergodic-theoretic consequences of (T).
- Yves Cornulier and Pierre de la Harpe, *Metric Geometry of Locally Compact Groups* (European Mathematical Society, 2016), for property (T) in the locally compact and geometric setting.
