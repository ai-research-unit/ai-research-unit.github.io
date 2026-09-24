
# __Adeles and Ideles__

## Introduction

Local fields are the completions of a global field at its places, and the arithmetic of a global field is the arithmetic of its completions considered together. To carry the local information in one structure one takes, over the places $v$ of a global field $K$, the product of the completions $K_v$ — but the unrestricted product is far too large to be locally compact. The restriction that makes the product manageable is local integrality: outside a finite set of places an element must lie in the valuation ring $\mathcal{O}_v$. The resulting ring is the **adele ring** $\mathbb{A}_K$, and the corresponding object for the multiplicative groups is the **idele group** $\mathbb{I}_K$. Both are locally compact and totally disconnected away from the Archimedean places; both carry a natural topology which is adapted to the arithmetic.

The construction belongs to this article: the **restricted product** and the ring of adeles with its topology, the idele group with its topology (which is not the subspace topology from $\mathbb{A}_K$), the embedding of $K$ as a discrete co-compact subgroup, and the compactness of the norm-one idele class group. The *analysis* on the adeles — additive and multiplicative Fourier transform, the Poisson summation formula, the Tamagawa measure and Tamagawa numbers, zeta integrals and the adelic theory of automorphic forms — belongs to Part III, where the measure and the limit are available, and is treated in that Part. The Haar measure that the analytic theory uses belongs to *Locally Compact Groups and Haar Measure*, and the integration theory on the locally compact groups constructed here belongs to Part III; this article constructs the topological groups and states no more about measure than the compactness results that the topology itself supplies.

The article assumes *Local Fields* for the local theory at each place, *Topological Rings and Fields* and *Topological Groups* for the general theory of topological rings and locally compact groups, and the algebraic number theory of Part I for the class number, the unit theorem and the product formula, which are cited rather than reproved. Throughout, $K$ is a global field, that is, a finite extension of $\mathbb{Q}$ (a **number field**) or a finite extension of $\mathbb{F}_p(t)$ (a **function field**); $V_K$ is its set of places, $V_K^\infty$ the Archimedean ones and $V_K^{\mathrm{fin}}$ the non-Archimedean ones. For a place $v$, the completion is written $K_v$, its valuation ring $\mathcal{O}_v$, its maximal ideal $\mathfrak{m}_v$, its residue field $k_v$ and its normalised absolute value $\lvert \cdot \rvert_v$, in the notation of *Local Fields*. The symbol $S$ always denotes a finite set of places containing $V_K^\infty$ when $K$ is a number field, and the phrase "almost all $v$" means all but finitely many.

---

## Restricted Products

### Definition

**Definition.** Let $(G_v)_{v \in V}$ be a family of locally compact topological groups indexed by a set $V$, and for each $v$ let $H_v \subseteq G_v$ be a compact open subgroup, with $H_v = G_v$ for almost all $v$. The **restricted product** is the subgroup

$$
\prod_{v \in V}{}' (G_v, H_v) = \Bigl\{(x_v) \in \prod_{v \in V} G_v : x_v \in H_v \text{ for almost all } v\Bigr\},
$$

equipped with the topology for which a basis of neighbourhoods of the identity is given by the sets $\prod_v U_v$, where each $U_v$ is a neighbourhood of the identity in $G_v$ and $U_v = H_v$ for almost all $v$. The groups $H_v$ are the **defining subgroups**, and they are part of the data: a family with different defining subgroups can define the same restricted product only when the subgroups are almost everywhere equal.

The definition is the exact analogue for products of the condition that makes a direct sum finite. The unrestricted product $\prod_v (G_v, G_v)$ and the direct sum $\bigoplus_v (G_v, \{1\})$ are the two extreme cases; the intermediate case is what the adeles require.

**Proposition.** The restricted product $\prod'_v (G_v, H_v)$ is a topological group, and it is Hausdorff when each $G_v$ is Hausdorff.

**Proof.** The sets $\prod_v U_v$ with $U_v = H_v$ for almost all $v$ form a filter base of identity neighbourhoods closed under inversion, because each $H_v$ is a subgroup and each $U_v$ may be replaced by $U_v \cap U_v^{-1}$. Multiplication is continuous: for a basic neighbourhood $\prod_v U_v$ of $1$ choose, for each $v$, a neighbourhood $W_v$ of $1$ in $G_v$ with $W_v \cdot W_v \subseteq U_v$, and take $W_v = H_v$ when $U_v = H_v$; then $\prod_v W_v$ is a basic neighbourhood and its square is contained in $\prod_v U_v$. Hence the group operations are continuous. The Hausdorff property is inherited coordinatewise from the $G_v$. $\square$

**Theorem (the direct limit description).** With the notation above, for a finite subset $S \subseteq V$ let

$$
G_S = \prod_{v \in S} G_v \times \prod_{v \notin S} H_v .
$$

Then each $G_S$ is a locally compact group, the inclusions $G_S \hookrightarrow G_{S'}$ for $S \subseteq S'$ are open embeddings, and the restricted product is the union of the $G_S$ over the directed set of finite subsets $S$, carrying the direct limit topology.

**Proof.** A finite product of locally compact groups is locally compact, and an arbitrary product of compact groups is compact by Tychonoff; hence $G_S$ is locally compact. A basic neighbourhood of $1$ in $G_S$ is $\prod_{v \in S} U_v \times \prod_{v \notin S} H_v$, which is exactly the trace on $G_S$ of the basic neighbourhood $\prod_v U_v$ with $U_v = H_v$ for $v \notin S$; this is the statement that the embedding is open. Every element of the restricted product lies in some $G_S$, with $S$ the finite set of places at which the coordinate is not in $H_v$, and the definition of the neighbourhood base is precisely the direct limit topology on the union. $\square$

**Corollary.** If each $G_v$ is locally compact, then the restricted product is locally compact. If each $G_v$ is moreover totally disconnected, then so is the restricted product, provided the defining subgroups $H_v$ are as above, since the $G_S$ are then totally disconnected and the property is local.

**Proof.** Every point lies in some $G_S$, an open locally compact subset. Total disconnectedness passes to products and to open subsets. $\square$

**Remark.** The restricted product is not the subspace topology of the unrestricted product. In the unrestricted product the set of tuples that are almost everywhere in $H_v$ would be a countable intersection of open sets, hence not necessarily open, and the group would not be locally compact. The extra instruction — that a basic neighbourhood may restrict only finitely many coordinates — is what the topology of the restricted product adds.

---

## The Adele Ring

### Definition

**Definition.** Let $K$ be a global field. The **adele ring** of $K$ is the restricted product of the additive groups of the completions with respect to the valuation rings,

$$
\mathbb{A}_K = \prod_{v \in V_K}{}' (K_v, \mathcal{O}_v).
$$

Thus an adele is a tuple $x = (x_v)_{v}$ with $x_v \in K_v$ for all $v$ and $x_v \in \mathcal{O}_v$ for almost all $v$. Addition and multiplication are coordinatewise, and $K$ embeds diagonally as the **principal adeles**: $K \hookrightarrow \mathbb{A}_K$, $a \mapsto (a)_v$. The **finite adeles** are the restricted product over the non-Archimedean places alone,

$$
\mathbb{A}_K^{\mathrm{fin}} = \prod_{v \in V_K^{\mathrm{fin}}}{}' (K_v, \mathcal{O}_v),
$$

and the **integral adeles** are the compact open subring $\widehat{\mathcal{O}}_K = \prod_{v}\bigl(\mathcal{O}_v \text{ for } v \in V_K^{\mathrm{fin}}\bigr)$, that is, the product of the valuation rings with the identity as defining subgroups; for number fields one defines $\widehat{\mathcal{O}}_K$ for the finite places only, and its product with the Archimedean factor is written $\mathbb{A}_K^\infty = \prod_{v \in V_K^\infty} K_v$ when $V_K^\infty$ is nonempty.

**Theorem.** The adele ring $\mathbb{A}_K$ is a topological ring: the coordinatewise addition and multiplication are continuous for the restricted product topology.

**Proof.** Addition is continuous by the proposition on restricted products applied to the additive groups. For multiplication, let $x$ be an adele and consider the map $y \mapsto xy$. Choose a finite set $S \supseteq V_K^\infty$ with $x_v \in \mathcal{O}_v$ for all $v \notin S$; for $v \notin S$, the set $\{y_v \in K_v : x_v y_v \in \mathcal{O}_v\}$ contains the open subset $y_v \in \mathcal{O}_v$, since $\mathcal{O}_v$ is a ring and $x_v \in \mathcal{O}_v$. Hence the product of these sets, over almost all $v$, contains $\prod_{v \notin S} \mathcal{O}_v$ and is a basic neighbourhood of $0$ in the restricted product; this shows continuity of multiplication at $(x, 0)$ and, by linearity in $y$, at every point. $\square$

### Examples

**Example ($K = \mathbb{Q}$).** The places of $\mathbb{Q}$ are $\infty$ and the primes $p$, so

$$
\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod_p{}' (\mathbb{Q}_p, \mathbb{Z}_p), \qquad
\widehat{\mathcal{O}}_\mathbb{Q} = \prod_p \mathbb{Z}_p ,
$$

and the integral adeles over the finite places are the profinite ring $\widehat{\mathbb{Z}} = \prod_p \mathbb{Z}_p$. The diagonal copy of $\mathbb{Q}$ consists of the tuples with a single rational number in each coordinate. A fundamental observation is that $\mathbb{A}_\mathbb{Q} = \mathbb{Q} + (\mathbb{R} \times \widehat{\mathbb{Z}})$: every adele is the sum of a rational number and a tuple whose Archimedean coordinate lies in $[0,1)$ and whose non-Archimedean coordinates are integral. This identity is what makes the quotient compact, and it is the arithmetic content of the Chinese remainder theorem applied at all primes at once.

**Example ($K$ a number field).** The Archimedean factor is $\prod_{v \mid \infty} K_v = \mathbb{R}^{r_1} \times \mathbb{C}^{r_2}$ for the signature $(r_1, r_2)$ of $K$, and it is a finite-dimensional real vector space. The adele ring is the product of this vector space with the finite adeles $\mathbb{A}_K^{\mathrm{fin}}$.

**Example ($K = \mathbb{F}_p(t)$).** There are no Archimedean places and the adele ring is purely non-Archimedean and totally disconnected. The analogue of the integral adeles is again the infinite product of the local valuation rings.

**Example (the localisation principle).** For a place $v$ the projection $\mathbb{A}_K \to K_v$ is a continuous open surjective ring homomorphism. The topology of $\mathbb{A}_K$ is exactly the weakest topology making all these projections continuous and agreeing with the defining subgroups, which is the precise sense in which the adeles assemble the local fields without losing the local topologies.

### The Principal Adeles

**Theorem (discreteness and co-compactness).** Let $K$ be a number field. Then the diagonal image of $K$ in $\mathbb{A}_K$ is a discrete subgroup, and the quotient $\mathbb{A}_K / K$ is compact.

**Proof.** *Discreteness.* It suffices to find a neighbourhood of $0$ in $\mathbb{A}_K$ meeting the diagonal copy of $K$ only at $0$. By the product formula of *Absolute Values, Valuations and Completions*, a nonzero $a \in K^\times$ satisfies $\prod_v \lvert a \rvert_v = 1$: if $\lvert a \rvert_v \leq 1$ at every place then $\lvert a \rvert_v = 1$ at every place, so that $a$ is a unit of $\mathcal{O}_K$, while if $\lvert a \rvert_v < 1$ at one place then $\lvert a \rvert_{v'} > 1$ at some other place. Take $S = V_K^\infty$ and a small $\varepsilon > 0$. The ring of integers $\mathcal{O}_K$ is a lattice in $\prod_{v \in S} K_v$ under the diagonal embedding — that is, its image is discrete, by the standard lattice theorem for the Minkowski embedding of a number field — so for small $\varepsilon$ the only $a \in \mathcal{O}_K$ with $\lvert a \rvert_v < \varepsilon$ for all $v \in S$ is $a = 0$. The basic neighbourhood $\prod_{v \in S}\{x : \lvert x \rvert_v < \varepsilon\} \times \prod_{v \notin S}\mathcal{O}_v$ of $0$ in $\mathbb{A}_K$ therefore meets the diagonal copy of $K$ only at $0$, so $K$ is discrete. *Co-compactness.* The quotient $\mathbb{A}_K/K$ is the quotient of $\mathbb{A}_K$ by a discrete subgroup; it is compact because $\mathbb{A}_K = K + D$ for a compact set $D$. For $K = \mathbb{Q}$ one may take $D = [0,1) \times \widehat{\mathcal{O}}_\mathbb{Q}$ as in the example above, and the closure of $D$ is compact, the endpoints being accounted for by the equivalence relation modulo $\mathbb{Q}$. For a general number field the set

$$
D = D_\infty \times \widehat{\mathcal{O}}_K , \qquad D_\infty \subseteq \prod_{v \in V_K^\infty} K_v ,
$$

with $D_\infty$ a bounded fundamental domain for the action of the image of $\mathcal{O}_K$ on the Archimedean factor $\prod_{v \in V_K^\infty} K_v$ — an image which is a lattice there by the Minkowski embedding — and $\widehat{\mathcal{O}}_K$ the integral adeles at the finite places, is compact and satisfies $K + D = \mathbb{A}_K$. Given an adele $x$, the density of $K$ in the finite adeles supplies $a \in K$ with $x_v - a \in \mathcal{O}_v$ for every $v \in V_K^{\mathrm{fin}}$, so $x - a$ lies in $\mathbb{A}_K^\infty \times \widehat{\mathcal{O}}_K$; subtracting a further element of $\mathcal{O}_K = K \cap \widehat{\mathcal{O}}_K$ leaves the finite part integral and translates the Archimedean part by the lattice image of $\mathcal{O}_K$, so that the Archimedean coordinate may be brought into $D_\infty$. $\square$

**Remark.** For a function field $K$, the group $K$ is discrete in $\mathbb{A}_K$ but the quotient $\mathbb{A}_K/K$ is not compact; it is the subgroup of **degree zero** adeles $\mathbb{A}_K^0$, the kernel of the degree map on the adeles, that contains $K$ as a discrete co-compact subgroup. The degree of an adele is the sum of the local degrees weighted by the residues; this is the global degree of a divisor, transferred to the adeles.

**Corollary.** Let $K$ be a number field. Then $\mathbb{A}_K/K$ is a compact connected Hausdorff abelian group. For a function field $K$ the quotient $\mathbb{A}_K^0/K$ is a compact totally disconnected Hausdorff abelian group.

**Proof.** Compactness and Hausdorffness are the theorem and the fact that $K$ is discrete, in the number field case for $\mathbb{A}_K$ and in the function field case for $\mathbb{A}_K^0$. Connectedness in the number field case is read off from the Pontryagin dual: $(\mathbb{A}_K/K)^\wedge \cong K$, because $\mathbb{A}_K$ is self-dual and the annihilator of $K$ in $\mathbb{A}_K$ is $K$ again, and a compact abelian group is connected exactly when its dual is torsion-free; $K$ is a field, hence torsion-free. In the function field case every completion $K_v$ is non-Archimedean and hence totally disconnected, so $\mathbb{A}_K^0$, a union of compact open subgroups, is totally disconnected, and so is its quotient by $K$. $\square$

**Theorem (the additive quotient as a lattice quotient).** Let $K$ be a number field. Then the image of $K$ in $\mathbb{A}_K$ is a **lattice** in the locally compact abelian group $\mathbb{A}_K$: it is discrete and co-compact. For a function field the same holds with $\mathbb{A}_K$ replaced by the group $\mathbb{A}_K^0$ of degree zero adeles. Consequently $\mathbb{A}_K$, in the number field case, and $\mathbb{A}_K^0$, in the function field case, are locally compact abelian groups with a discrete co-compact subgroup, and $\mathbb{A}_K$ is self-dual under Pontryagin duality.

**Proof.** The lattice property is discreteness together with co-compactness, which are the two statements already proved, the function field case being the corresponding statement for $\mathbb{A}_K^0$. Self-duality is the standard Pontryagin duality of the adeles: each $K_v$ is self-dual under its local additive character pairing, by the duality theory of *Abelian Topological Groups*, and the restricted product of self-dual groups is self-dual with respect to the restricted product of the duals, the defining compact open subgroups being their own annihilators. It is quoted here for use in the analytic theory of Part III. $\square$

---

## The Idele Group

### Definition and the Two Topologies

**Definition.** Let $K$ be a global field. The **idele group** of $K$ is the restricted product of the multiplicative groups of the completions with respect to the unit groups of the valuation rings,

$$
\mathbb{I}_K = \prod_{v \in V_K}{}' (K_v^\times, \mathcal{O}_v^\times).
$$

Thus an idele is a tuple $x = (x_v)$ with $x_v \in K_v^\times$ for all $v$ and $x_v \in \mathcal{O}_v^\times$ for almost all $v$, and the group operation is coordinatewise multiplication. This topology is the **idele topology**.

**Remark (the idele topology is not the subspace topology).** The set of units of the ring $\mathbb{A}_K$ is exactly $\mathbb{I}_K$ as an abstract group, but the topology just defined is strictly finer than the subspace topology induced from $\mathbb{A}_K$. A basic neighbourhood of the identity in the subspace topology has $U_v = K_v$ for almost all $v$, whereas a basic neighbourhood in the idele topology has $U_v = \mathcal{O}_v^\times$ for almost all $v$. In the subspace topology a basic neighbourhood of the identity therefore constrains only finitely many coordinates, so it contains ideles whose coordinates at all the remaining places are arbitrarily large; its closure is a product of infinitely many non-compact factors, hence is not compact, and no open subset of it lies in a compact set. The subspace topology is thus not locally compact, and the idele topology is the restricted product built on the compact open subgroups $\mathcal{O}_v^\times$: it is the topology in which $\mathbb{I}_K$ is locally compact and in which the compactness and finiteness statements below hold.

**Theorem.** $\mathbb{I}_K$ is a locally compact abelian topological group, and it is totally disconnected when $K$ has no real place, and in general is a product of a finite-dimensional real vector space factor with a totally disconnected group.

**Proof.** Each $K_v^\times$ is locally compact by *Local Fields*, and each $\mathcal{O}_v^\times$ is a compact open subgroup; the restricted product is therefore locally compact by the corollary of the restricted product theorem, and it is a topological group by the proposition. It is abelian because each factor is. Total disconnectedness in the absence of real places follows because each $K_v^\times$ is then totally disconnected; the real places contribute the connected factor $\mathbb{R}_{>0}$. $\square$

**Proposition (the norm and the product formula).** The **idele norm** is the continuous homomorphism

$$
\lvert \cdot \rvert : \mathbb{I}_K \longrightarrow \mathbb{R}_{>0}, \qquad \lvert x \rvert = \prod_{v \in V_K} \lvert x_v \rvert_v ,
$$

which is well defined because almost all factors equal $1$, and which restricts to $K^\times$ as the trivial character: $\lvert a \rvert = 1$ for every $a \in K^\times$, by the product formula.

**Proof.** Continuity is local: each $\lvert \cdot \rvert_v$ is continuous on $K_v^\times$, and $\lvert x_v \rvert_v = 1$ for almost all $v$, so the product is a finite product in a neighbourhood of the identity. The restriction statement is the product formula of *Absolute Values, Valuations and Completions*. $\square$

### The Idele Class Group

**Definition.** The **idele class group** is $C_K = \mathbb{I}_K / K^\times$, where $K^\times$ is embedded diagonally; the norm-one subgroup is

$$
\mathbb{I}_K^1 = \ker(\lvert \cdot \rvert) = \{x \in \mathbb{I}_K : \lvert x \rvert = 1\}, \qquad C_K^1 = \mathbb{I}_K^1 K^\times / K^\times .
$$

The group $C_K^1$ is the **norm-one idele class group**.

**Theorem (compactness of the norm-one class group; finiteness).** Let $K$ be a number field. Then $K^\times$ is a discrete subgroup of $\mathbb{I}_K$, the group $\mathbb{I}_K^1 / K^\times$ is compact, and the class group of $K$ is finite. In the function field case the corresponding statement holds with the degree-zero ideles in place of the norm-one ideles.

**Proof.** The discreteness of $K^\times$ in $\mathbb{I}_K$ follows from the discreteness of $K$ in $\mathbb{A}_K$: a discrete subgroup of a topological ring is discrete in its unit group for the restricted product topology, since the idele topology is finer. For the compactness one uses that $\mathbb{I}_K^1/K^\times$ is the quotient of the compact set of ideles of norm one lying in a fundamental domain by the discrete acting group; equivalently, the compactness is the conjunction of the finiteness of the class number and Dirichlet's unit theorem, both of which belong to the algebraic number theory of Part I and are quoted as standard. The finiteness of the class group is the case of the compactness statement in which the Archimedean component is held fixed. $\square$

**Theorem (structure of the idele class group).** For a number field $K$ there is an isomorphism of topological groups

$$
\mathbb{I}_K \cong \mathbb{I}_K^1 \times \mathbb{R}_{>0},
$$

obtained by choosing a place $v_0$ and sending $x$ to $(x \cdot c(x)^{-1}, \lvert x \rvert)$ for an idele $c(x)$ supported at $v_0$ with $\lvert c(x) \rvert = \lvert x \rvert$; consequently $C_K$ is the product of the compact group $C_K^1$ and $\mathbb{R}_{>0}$. For a function field $K$, the image of the norm is $q^{\mathbb{Z}}$ and $\mathbb{I}_K / \mathbb{I}_K^1 \cong \mathbb{Z}$.

**Proof.** The chosen place $v_0$ has valuation group $\mathbb{Z}$ (or, if Archimedean, an element of norm any prescribed positive real, by the density of $\lvert K_{v_0} \rvert$ in $\mathbb{R}_{>0}$ for a real place and by taking an even power at a complex place), so an idele of any prescribed positive norm supported at $v_0$ may be found; the map is then a topological isomorphism by the open mapping theorem for locally compact groups, or directly from the product decomposition. The function field case is the statement that the norm of an idele is a power of $q$ and that the degree map has image $\mathbb{Z}$. $\square$

**Example (the ideles of $\mathbb{Q}$).** Here $\mathbb{I}_\mathbb{Q} = \mathbb{R}^\times \times \prod'_p (\mathbb{Q}_p^\times, \mathbb{Z}_p^\times)$, the norm is $\lvert x \rvert = \lvert x_\infty \rvert \cdot \prod_p \lvert x_p \rvert_p$, and $\mathbb{Q}^\times$ is the diagonal copy of the nonzero rationals. The norm-one ideles modulo $\mathbb{Q}^\times$ are compact, and their quotient by the connected component of the identity is the profinite group $\widehat{\mathbb{Z}}^\times$, reflecting the fact that $\mathbb{Q}$ has class number one and unit group $\{\pm 1\}$.

**Example (the ray class groups).** For a modulus $\mathfrak{m}$ of $K$, the quotient of $\mathbb{I}_K$ by the product of the ray subgroup $U(\mathfrak{m})$ — the ideles congruent to $1$ modulo $\mathfrak{m}$ — and $K^\times$ is the **ray class group** mod $\mathfrak{m}$. For the trivial modulus this is the ordinary ideal class group. This is the idelic form of the groups that appear in class field theory; the reciprocity isomorphism identifying these quotients with the abelian Galois groups of $K$ belongs to Part I, and the analytic description of these groups through $L$-functions belongs to Part III.

---

## Topological Properties

### The Adeles and Ideles as Locally Compact Groups

**Theorem.** Let $K$ be a global field.

**(a)** $\mathbb{A}_K$ is a locally compact, Hausdorff, $\sigma$-compact topological ring, and it is totally disconnected away from the Archimedean places.

**(b)** $\mathbb{I}_K$ is a locally compact, Hausdorff, $\sigma$-compact abelian topological group, and it is open in $\mathbb{I}_K$ at every point; every compact subset of $\mathbb{I}_K$ is contained in $\prod_{v \in S} C_v \times \prod_{v \notin S} \mathcal{O}_v^\times$ for a finite $S$ and compact sets $C_v \subseteq K_v^\times$.

**(c)** The inclusion $\mathbb{I}_K \hookrightarrow \mathbb{A}_K$ is continuous, and its image is the set of units of the ring; the induced topology is strictly coarser.

**(d)** $\mathbb{I}_K^1$ and its quotient $C_K^1 = \mathbb{I}_K^1/K^\times$ are closed; $C_K^1$ is compact for a number field, and for a function field the analogous degree-zero quotient is compact.

**Proof.** (a) The adele ring is a restricted product of locally compact spaces, hence locally compact by the corollary; it is a topological ring by the theorem on continuity of multiplication; total disconnectedness away from the Archimedean places is inherited coordinatewise. (b) The same restricted-product corollary gives local compactness; every point of $\mathbb{I}_K$ has a neighbourhood of the form $\prod_{v \in S} U_v \times \prod_{v \notin S} \mathcal{O}_v^\times$ with $U_v$ open, and this is a product of open sets, so it is open in $\mathbb{I}_K$; a compact set is contained in such a product with the $C_v$ compact because a compact subset of the union of the open sets $\prod_{v \in S'} \cdots$ is contained in one of them. (c) The inclusion is continuous because the identity map on tuples is continuous when the target topology is coarser; it is not a homeomorphism because inversion is not continuous in the subspace topology. (d) The norm-one subgroup is the kernel of a continuous homomorphism into a Hausdorff group, hence closed; the class group is its image modulo a discrete subgroup, and compactness is the theorem on the norm-one class group. $\square$

**Theorem (nothing but the class group is compact).** $\mathbb{A}_K$ is not compact; $\mathbb{I}_K$ is not compact; $\mathbb{I}_K^1$ is not compact; but $\mathbb{A}_K/K$ and $C_K^1 = \mathbb{I}_K^1/K^\times$ are compact.

**Proof.** The global field $K$ is infinite and is discrete in $\mathbb{A}_K$, and an infinite discrete subset of a compact Hausdorff space is impossible; hence $\mathbb{A}_K$ is not compact. The idele norm maps $\mathbb{I}_K$ continuously onto the non-compact group $\mathbb{R}_{>0}$ in the number field case (and onto $q^{\mathbb{Z}}$ in the function field case), so $\mathbb{I}_K$ is not compact. The units of a topological ring form an open subset, so $\mathbb{I}_K$ is open in $\mathbb{A}_K$ and $K^\times = K \cap \mathbb{I}_K$ is discrete in $\mathbb{I}_K$; the subgroup $K^\times$ lies in $\mathbb{I}_K^1$ by the product formula and is infinite, and a discrete subgroup of a compact group is finite: if $H$ is discrete in a compact group $G$, choose an open $U$ of the identity with $U \cap H = \{1\}$, cover $G$ by finitely many translates $h_i U$ with $h_i \in H$, and note that each $h_i U$ meets $H$ in at most one point. Hence $\mathbb{I}_K^1$ is not compact. The compactness of $\mathbb{A}_K/K$ and of $C_K^1$ is the theorem on the norm-one class group, proved there from the class number and the unit theorem. $\square$

### Functoriality

**Proposition.** Let $L/K$ be a finite extension of global fields. Then there are continuous ring homomorphisms $\mathbb{A}_K \to \mathbb{A}_L$ and group homomorphisms $\mathbb{I}_K \to \mathbb{I}_L$ induced by the embeddings $K \hookrightarrow L$, and the norm and trace maps on the completions assemble into continuous homomorphisms $\mathbb{A}_L \to \mathbb{A}_K$ and $\mathbb{I}_L \to \mathbb{I}_K$; these are compatible with the diagonal embeddings in the sense that the diagrams with $K \hookrightarrow L$ commute.

**Proof.** At each place $w$ of $L$ lying over $v$ of $K$, the local field extension $L_w/K_v$ is finite, and the local trace and norm are continuous; an adele of $L$ has $w$-component in $\mathcal{O}_w$ for almost all $w$, hence its trace and norm lie in $\mathcal{O}_v$ for almost all $v$, so the maps are defined on the restricted products. Continuity is local and the products are finite in a neighbourhood, as in the continuity of the idele norm. $\square$

**Remark.** The map $\mathbb{A}_K \to \mathbb{A}_L$ is not the same as the map induced by the diagonal; it is the base change, and it is open onto its image only after accounting for the Archimedean places. The precise complement, the **different** and its relation to the discriminant, is used in the theory of the Tamagawa measure, which is Part III's.

---

## The Adeles and Global Arithmetic

### The Product Formula Recovered

**Proposition.** The product formula over the places of $K$ is equivalent to the statement that the idele norm restricts trivially to $K^\times$; both are equivalent to the statement that the principal ideles lie in the kernel of a character that separates the places.

**Proof.** The product formula says $\prod_v \lvert a \rvert_v = 1$ for all $a \in K^\times$, which is exactly the restriction statement, since $\lvert a \rvert = \prod_v \lvert a \rvert_v$; conversely the restriction statement for all $a$ is the product formula. $\square$

**Proposition (the two lattices).** The additive group $\mathbb{A}_K$ contains $K$ as a discrete co-compact subgroup. The multiplicative group $\mathbb{I}_K$ contains $K^\times$ discretely, and the quotient of the norm-one subgroup $\mathbb{I}_K^1$ by $K^\times$ is compact, the norm-one condition removing the non-compact $\mathbb{R}_{>0}$-direction of the idele norm. Thus the same field $K$ is a lattice in both constructions, once in the additive group and once in the multiplicative group restricted to norm one.

**Proof.** The additive statement is the discreteness and co-compactness theorem above. For the multiplicative statement, $K^\times$ is discrete in $\mathbb{I}_K$ because $\mathbb{I}_K$ is open in $\mathbb{A}_K$ and $K$ is discrete in $\mathbb{A}_K$, and the compactness of $\mathbb{I}_K^1/K^\times$ is the theorem on the norm-one class group. $\square$

### Adelic Class Field Theory

**Theorem (statement of the idelic reciprocity law).** Let $K$ be a global field. There is a continuous homomorphism

$$
\operatorname{rec}_K : C_K = \mathbb{I}_K/K^\times \longrightarrow \operatorname{Gal}(K^{\mathrm{ab}}/K),
$$

the **global reciprocity map**, whose kernel is the connected component of the identity in the number field case and the closure of the image of the norm subgroups in general, and which induces a bijection between the open subgroups of $C_K$ of finite index and the finite abelian extensions of $K$, sending an extension $L/K$ to the quotient $C_K / N_{L/K}(C_L)$.

**Proof.** This is the main theorem of global class field theory, resting on the local reciprocity laws at all places assembled into an adelic product; the full proof belongs to Part I, and the statement is recorded here only to display the role of the idele class group as the topological group in which the abelian extensions are parameterised. $\square$

**Remark.** The advantage of the idelic formulation over the older ideal-theoretic one is that the reciprocity map is a single continuous homomorphism of locally compact groups, with no exceptional behaviour at the Archimedean places and no separate treatment of the primes at infinity; the topology of $\mathbb{I}_K$ is exactly what is needed to make the statement a statement about local compactness and open subgroups. This is the topological content of the construction and the reason it belongs to this Part.

---

## Summary

For a global field $K$, the **restricted product** $\prod'_v (G_v, H_v)$ is the group of tuples lying in the compact open subgroups $H_v$ almost everywhere, with the topology in which a basic neighbourhood may restrict only finitely many coordinates; it is a topological group and is locally compact when the $G_v$ are, and it is the direct limit of the products $\prod_{v \in S} G_v \times \prod_{v \notin S} H_v$. The **adele ring** $\mathbb{A}_K = \prod'_v (K_v, \mathcal{O}_v)$ is a locally compact, Hausdorff, $\sigma$-compact topological ring, the coordinatewise operations being continuous; it contains $K$ diagonally as a discrete subgroup, and for a number field the quotient $\mathbb{A}_K/K$ is compact, while for a function field the degree-zero adeles $\mathbb{A}_K^0$ play that role.

The **idele group** $\mathbb{I}_K = \prod'_v (K_v^\times, \mathcal{O}_v^\times)$ is the restricted product of the local unit groups. Its topology is strictly finer than the subspace topology induced from $\mathbb{A}_K$, precisely so that it is a locally compact abelian topological group and inversion is continuous. The idele norm $\lvert x \rvert = \prod_v \lvert x_v \rvert_v$ is a continuous homomorphism, trivial on $K^\times$ by the product formula. The **idele class group** $C_K = \mathbb{I}_K/K^\times$ decomposes as $C_K^1 \times \mathbb{R}_{>0}$ for a number field, and the norm-one part $C_K^1 = \mathbb{I}_K^1/K^\times$ is compact, a topological statement equivalent to the finiteness of the class number together with Dirichlet's unit theorem. The construction is functorial in finite extensions, and the global reciprocity law is a continuous homomorphism from $C_K$ to the abelianised absolute Galois group, whose open subgroups of finite index parameterise the finite abelian extensions of $K$.

The ring of adeles, its topology, its locally compactness and the discreteness and co-compactness of $K$ are the subject of this article. The Fourier analysis on $\mathbb{A}_K$, the Tamagawa measure, the Poisson summation formula, the zeta integrals and the analytic theory of automorphic representations belong to Part III, and the Haar measure and its invariance on the locally compact groups constructed here belong to *Locally Compact Groups and Haar Measure*, the integration theory on them to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | A global field |
| $V_K$, $V_K^\infty$, $V_K^{\mathrm{fin}}$ | Places of $K$, Archimedean and finite places |
| $K_v$, $\mathcal{O}_v$, $\mathfrak{m}_v$, $k_v$ | Completion at $v$, its valuation ring, maximal ideal, residue field |
| $\mathcal{O}_K$ | The ring of integers of the number field $K$ |
| $D$, $D_\infty$ | A compact subset with $\mathbb{A}_K = K + D$, and its Archimedean factor |
| $\lvert \cdot \rvert_v$ | Normalised absolute value at $v$ |
| $S$ | A finite set of places, containing $V_K^\infty$ when $K$ is a number field |
| $\prod'_v (G_v, H_v)$ | Restricted product with defining subgroups $H_v$ |
| $G_S = \prod_{v \in S} G_v \times \prod_{v \notin S} H_v$ | The open locally compact pieces of the direct limit |
| $\mathbb{A}_K = \prod'_v (K_v, \mathcal{O}_v)$ | Adele ring |
| $\mathbb{A}_K^{\mathrm{fin}}$ | Finite adeles, over $V_K^{\mathrm{fin}}$ |
| $\widehat{\mathcal{O}}_K = \prod_{v \in V_K^{\mathrm{fin}}} \mathcal{O}_v$ | Integral adeles, a compact open subring |
| $\mathbb{A}_K^0$ | Degree-zero adeles (function field case) |
| $\mathbb{I}_K = \prod'_v (K_v^\times, \mathcal{O}_v^\times)$ | Idele group, with the idele topology |
| $\lvert x \rvert = \prod_v \lvert x_v \rvert_v$ | Idele norm |
| $\mathbb{I}_K^1$ | Norm-one ideles |
| $C_K = \mathbb{I}_K / K^\times$ | Idele class group |
| $C_K^1 = \mathbb{I}_K^1 K^\times / K^\times$ | Norm-one idele class group, compact for a number field |
| $\operatorname{rec}_K$ | Global reciprocity map |
| $N_{L/K}$, $\operatorname{Tr}_{L/K}$ | Norm and trace, assembled adelicwise |



## Further Reading

- André Weil, *Basic Number Theory* (Springer, 3rd ed. 1974), for the adeles, ideles and the topology of the restricted product.
- J. W. S. Cassels and A. Fröhlich (eds.), *Algebraic Number Theory* (Academic Press, 1967), for the idelic formulation of class field theory and the compactness of the idele class group.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for the adele ring, the idele group and the reciprocity map.
- Claude Chevalley, "Sur la théorie du corps de classes", *Journal of the Mathematical Society of Japan* **3** (1951), 36–44, for the idelic formulation of class field theory.
- John Tate, "Fourier analysis in number fields and Hecke's zeta-functions" (in *Algebraic Number Theory*, eds. Cassels and Fröhlich, Academic Press, 1967), for the additive and multiplicative analysis on the adeles.
- Dinakar Ramakrishnan and Robert J. Valenza, *Fourier Analysis on Number Fields* (Springer, 1999), for the restricted product topology, the idele class group and the route from the local to the global analysis.
- Anton Deitmar and Siegfried Echterhoff, *Principles of Harmonic Analysis* (Springer, 2nd ed. 2014), for the restricted product and locally compact group structure used here.
