
# __Representation Theory of Locally Compact Groups__

## Introduction

A **unitary representation** of a locally compact group $G$ is a continuous action of $G$ by unitary operators on a Hilbert space, the continuity being that of the strong operator topology. The theory of these representations is the frame in which a non-abelian group is studied through linear algebra: the group is resolved into operators, irreducibility is the analogue of simplicity, and the classification of the irreducible representations is the analogue of the Pontryagin dual of an abelian group. For a compact group the theory is especially clean — the irreducible unitary representations are finite-dimensional and every unitary representation is a direct sum of them — and for a general locally compact group the decomposition into irreducibles is a decomposition into a direct integral, whose existence and uniqueness is the harmonic analysis of the group.

The article develops the definitions, the equivalence relation of unitary representations, the invariant-subspace and commutant theory, Schur's lemma and the complete reducibility that orthogonal complements give, the standard constructions (direct sums, tensor products, contragredient, restriction, matrix coefficients), the abelian case in which the irreducible representations are exactly the characters of the previous articles, the compact case as a theorem stated and proved in Part III, and the relation to the Lie-theoretic representation theory of Part I.

The **boundary with Part III** is exact and is stated once for the whole representation-theoretic block of this category. The *representations* — their definition, their equivalences, their intertwiners, their irreducibility, their tensor products, their direct sums, the unitary dual as a set, and the algebraic theory of the group algebra and of the $( \mathfrak{g}, K )$-module — are the subject of this article . The **harmonic analysis** — the construction of $L^2(G)$ and of the regular representation on it, the convolution algebra $L^1(G)$ and its $C^*$-completion, the Peter–Weyl theorem, the Plancherel theorem and the decomposition of a unitary representation into a direct integral — belongs to *Analysis on Groups* in Part III, where the measure and the limit are available. The Haar measure used here is the invariant object constructed in *Locally Compact Groups and Haar Measure*; the Hilbert space $\mathcal{H}$ and its bounded operators are defined in line below, with the systematic theory in Part III; the finite-dimensional representation theory over $\mathbb{C}$ is that of *Representations of Groups* and *Representations of Lie Algebras* in Part I; and no physics is invoked.

## Unitary Representations

### Hilbert Spaces and Bounded Operators

**Definition.** A **Hilbert space** over $\mathbb{C}$ is a complex vector space $\mathcal{H}$ with a positive definite inner product $\langle \cdot, \cdot \rangle$, linear in the second variable and conjugate-linear in the first, that is complete for the norm $\|v\| = \langle v, v\rangle^{1/2}$. A **bounded operator** on $\mathcal{H}$ is a linear map $T : \mathcal{H} \to \mathcal{H}$ with finite operator norm

$$
\|T\| = \sup\{\|Tv\| : \|v\| \leq 1\} ,
$$

and $B(\mathcal{H})$ denotes the algebra of all bounded operators. The **adjoint** $T^*$ of $T \in B(\mathcal{H})$ is the unique bounded operator with $\langle Tv, w\rangle = \langle v, T^*w\rangle$ for all $v, w$; $T$ is **self-adjoint** if $T = T^*$, **unitary** if $T^*T = TT^* = 1$, and **positive** if $\langle Tv, v\rangle \geq 0$ for all $v$. The **unitary group**

$$
U(\mathcal{H}) = \{T \in B(\mathcal{H}) : T \text{ unitary}\}
$$

is a group under composition. The systematic theory of Hilbert spaces, their completions, their orthonormal bases and the spectral theorem for self-adjoint operators is that ; the elementary facts quoted here — the Cauchy–Schwarz inequality, the parallelogram law, the existence of orthogonal projections onto closed subspaces, and the orthogonal decomposition $\mathcal{H} = M \oplus M^\perp$ for a closed subspace $M$ — are standard and are used with that attribution.

**Definition.** The **strong operator topology** on $B(\mathcal{H})$ is the initial topology for the family of maps $\{T \mapsto Tv\}_{v \in \mathcal{H}}$, where $\mathcal{H}$ carries its norm topology; a net $T_\alpha \to T$ strongly if and only if $T_\alpha v \to Tv$ for every $v$. The **weak operator topology** is the initial topology for the family $\{T \mapsto \langle Tv, w\rangle\}_{v,w \in \mathcal{H}}$. The unitary group $U(\mathcal{H})$ carries the subspace topology from the strong operator topology; with it, $U(\mathcal{H})$ is a topological group.

**Proposition.** On $U(\mathcal{H})$ the strong and weak operator topologies coincide. Multiplication is strongly continuous, and inversion is strongly continuous on $U(\mathcal{H})$; hence $U(\mathcal{H})$ is a topological group for the strong operator topology. Equivalently, $U(\mathcal{H})$ is a closed subgroup of the product $\mathcal{H}^{\mathcal{H}}$ with the product topology.

**Proof.** For unitary $T$ and any $v$, $\|Tv - v\|^2 = 2\|v\|^2 - 2\operatorname{Re}\langle Tv, v\rangle$, so convergence of the matrix coefficients $\langle T_\alpha v, v\rangle$ at every $v$ implies strong convergence; replacing $\langle T_\alpha v, v\rangle$ by $\langle T_\alpha v, Tv\rangle$ in the same identity, and using unitarity of $T$, shows that weak convergence of $T_\alpha$ to $T$ implies strong convergence. Multiplication: $\|T_\alpha S_\alpha v - TSv\| \leq \|T_\alpha(S_\alpha v - Sv)\| + \|(T_\alpha - T)Sv\| = \|S_\alpha v - Sv\| + \|(T_\alpha - T)Sv\|$ by unitarity. Inversion: $\|T_\alpha^{-1}v - T^{-1}v\| = \|T_\alpha^{-1}(v - T_\alpha T^{-1}v)\| = \|v - T_\alpha T^{-1}v\| \to 0$. The last statement follows from the description of the initial topology as a subspace of the product. $\square$

### Definition and Continuity

**Definition.** A **unitary representation** of a locally compact group $G$ on a Hilbert space $\mathcal{H}$ is a group homomorphism

$$
\pi : G \longrightarrow U(\mathcal{H})
$$

that is continuous for the strong operator topology on $U(\mathcal{H})$; equivalently, the map $G \times \mathcal{H} \to \mathcal{H}$, $(g, v) \mapsto \pi(g)v$, is continuous. The space $\mathcal{H}$ is the **representation space** of $\pi$, written $\mathcal{H}_\pi$ when several representations occur; the **degree** of $\pi$ is $\dim \mathcal{H}_\pi$.

**Theorem (continuity criteria).** For a homomorphism $\pi : G \to U(\mathcal{H})$ the following are equivalent:

**(a)** $\pi$ is strongly continuous;

**(b)** $\pi$ is weakly continuous, that is, $g \mapsto \langle \pi(g)v, w\rangle$ is continuous for all $v, w \in \mathcal{H}$;

**(c)** for every $v \in \mathcal{H}$, the **matrix coefficient** $c_{v,w}(g) = \langle \pi(g)v, w\rangle$ is continuous for every $w$, equivalently $g \mapsto \pi(g)v$ is continuous;

**(d)** for every $v, w$ the function $g \mapsto \langle \pi(g)v, w\rangle$ is continuous at the identity.

**Proof.** (a) $\Rightarrow$ (b) is immediate from the continuity of the inner product and the initial topology. (b) $\Rightarrow$ (a): the identity $\|\pi(g)v - v\|^2 = 2\|v\|^2 - 2\operatorname{Re}\langle \pi(g)v, v\rangle$ of the proposition shows that continuity of $g \mapsto \langle \pi(g)v, v\rangle$ at $e$ gives continuity of $g \mapsto \pi(g)v$ at $e$ for each $v$; continuity at an arbitrary point follows by translation, $\|\pi(g)v - \pi(g_0)v\| = \|\pi(g_0^{-1}g)v - v\|$, using unitarity. (c) and (d) are restatements of (b) and of the same identity. $\square$

**Example (the trivial representation).** For every $G$ the **trivial representation** $1_G$ is the action of $G$ on $\mathbb{C}$ by the identity; it is the one-dimensional representation with constant matrix coefficient $1$, and its equivalence class is the distinguished point of the unitary dual below.

**Example (characters of an abelian group).** Let $G$ be locally compact abelian. Every character $\chi : G \to S^1$ of *Abelian Topological Groups* is a one-dimensional unitary representation on $\mathbb{C}$ with $\pi_\chi(g)z = \chi(g)z$. Conversely every irreducible unitary representation of $G$ is one-dimensional and of this form: the operators $\pi(g)$ commute with one another, so they lie in the commutant of an irreducible representation, which is $\mathbb{C}\cdot 1$ by Schur's lemma below, and each $\pi(g)$ is therefore a scalar. Hence the unitary dual of a locally compact abelian group, in the sense of the classification of irreducible unitary representations, is *exactly* the Pontryagin dual $G^\vee$ of *Pontryagin Duality*; the two theories coincide in the abelian case, and this is the sense in which the present article generalises Pontryagin duality to the non-abelian case.

**Example (finite-dimensional representations of a compact Lie group).** If $K$ is a compact Lie group and $\rho : K \to GL_n(\mathbb{C})$ is a continuous representation, then averaging any inner product on $\mathbb{C}^n$ over $K$ against its normalised Haar measure — the invariant integration of Part III on the compact group — produces an invariant inner product for which $\rho$ is unitary, with the same underlying homomorphism; this is the **Weyl unitary trick**. In its Lie-algebraic form, a finite-dimensional representation of a complex semisimple Lie algebra is completely reducible because it integrates to a representation of a compact real form, to which the averaging argument applies. The finite-dimensional representation theory of compact Lie groups, including the classification by highest weights of *Representations of Lie Algebras* and *Root Systems and Classification*, therefore embeds in the unitary theory, and every finite-dimensional unitary representation is completely reducible by the orthogonal-complement argument above.

### Equivalence, Intertwiners and Direct Sums

**Definition.** Let $\pi : G \to U(\mathcal{H})$ and $\pi' : G \to U(\mathcal{H}')$ be unitary representations.

**(a)** An **intertwining operator** or **intertwiner** is a bounded linear map $T : \mathcal{H} \to \mathcal{H}'$ with $T\pi(g) = \pi'(g)T$ for all $g \in G$. The set of intertwiners is a vector space $\operatorname{Hom}_G(\pi, \pi')$, and $\operatorname{End}_G(\pi)$ is the **commutant** of $\pi$.

**(b)** $\pi$ and $\pi'$ are **unitarily equivalent**, written $\pi \cong \pi'$, if there is a unitary intertwiner $T : \mathcal{H} \to \mathcal{H}'$; they are **isomorphic** if there is an invertible intertwiner, and this is the same relation.

**(c)** $\pi$ is **irreducible** if $\mathcal{H} \neq 0$ and the only closed subspaces invariant under all $\pi(g)$, $g \in G$, are $0$ and $\mathcal{H}$; otherwise $\pi$ is **reducible**. A representation is **completely reducible** if it is a direct sum of irreducible representations.

**Proposition.** Let $T \in \operatorname{Hom}_G(\pi, \pi')$. Then $\ker T$ is a closed invariant subspace and the closure of $\operatorname{im} T$ is a closed invariant subspace, so $T$ is injective when $\pi$ is irreducible and of dense image when $\pi'$ is irreducible; the adjoint $T^*$ is an intertwiner $\pi' \to \pi$, $\operatorname{End}_G(\pi)$ is a subalgebra of $B(\mathcal{H}_\pi)$ closed under the adjoint and under strong limits, and the partial isometry $U$ and the positive operator $|T| = (T^*T)^{1/2}$ of the polar decomposition $T = U|T|$ are intertwiners as well. The image of an intertwiner need not be closed: an operator of multiplication by a bounded function that does not vanish on a set of positive measure but is not bounded away from zero on its support commutes with the representation of $\mathbb{Z}$ on the square-summable functions of the circle given by $f \mapsto z^n f$ and has dense, non-closed image; the analytic background for such examples is Part III, and on irreducible representations the question does not arise.

**Proof.** The kernel of $T$ is closed because $T$ is bounded, and it is invariant: $T\pi(g)v = \pi'(g)Tv = 0$ for $v \in \ker T$. The image is invariant, and so is its closure, since each $\pi'(g)$ is a homeomorphism; hence the image is dense whenever $\pi'$ is irreducible. For the adjoint, $\langle T\pi(g)v, w\rangle = \langle \pi(g)v, T^*w\rangle$ while $\langle \pi'(g)Tv, w\rangle = \langle Tv, \pi'(g)^{-1}w\rangle$; the intertwining identity with $g^{-1}$ in place of $g$ gives $T\pi(g)^{-1} = \pi'(g)^{-1}T$, and hence $T^*\pi'(g) = \pi(g)T^*$, so $T^*$ intertwines $\pi'$ and $\pi$. The strong closedness is that of the commutant proposition below, and the statements about $|T|$ and $U$ follow by applying the adjoint computation to $T^*T$, whose square root is an intertwiner, and by the uniqueness of the polar decomposition. $\square$

**Proposition (complete reducibility of invariant subspaces).** Let $\pi$ be a unitary representation on $\mathcal{H}$ and let $M \subseteq \mathcal{H}$ be a closed invariant subspace. Then $M^\perp$ is closed and invariant, and

$$
\mathcal{H} = M \oplus M^\perp
$$

as unitary representations. Consequently every finite-dimensional unitary representation is completely reducible, and every unitary representation of a compact group is completely reducible once it is known that the irreducible representations of a compact group are finite-dimensional.

**Proof.** For $w \in M^\perp$ and $v \in M$, $\langle \pi(g)w, v\rangle = \langle w, \pi(g)^{-1}v\rangle = 0$ because $\pi(g)^{-1}v \in M$; so $M^\perp$ is invariant. The orthogonal decomposition is standard Hilbert-space geometry, and $\pi$ is the direct sum of its restrictions. The finite-dimensional statement is the classical complete reducibility of finite-dimensional unitary representations, proved by averaging or by taking orthogonal complements iteratively: choose a nonzero invariant subspace, split it off, and induct on the dimension. The compact statement is proved by induction over a maximal orthogonal decomposition, using the finite-dimensionality of the irreducibles as stated in §The Compact Case. $\square$

**Remark.** For a general unitary representation the reduction can fail: there are unitary representations of abelian groups with no irreducible subrepresentation, the standard example being the translation representation of $\mathbb{R}$ on $L^2(\mathbb{R})$, whose spectral resolution is a direct integral rather than a direct sum. The decomposition of an arbitrary unitary representation is therefore a decomposition into a direct *integral* over the unitary dual, and it is exactly the Plancherel theory of Part III; the algebraic skeleton developed here is the input to that theory, and the class of groups for which the decomposition is discrete and well behaved is not covered here.

## Schur's Lemma and Irreducibility

### Schur's Lemma

**Theorem (Schur).** Let $\pi$ and $\pi'$ be irreducible unitary representations of $G$.

**(a)** Every intertwiner $T \in \operatorname{Hom}_G(\pi, \pi')$ is either zero or an isomorphism; if $\pi \not\cong \pi'$ then $\operatorname{Hom}_G(\pi, \pi') = 0$.

**(b)** Every intertwiner $T \in \operatorname{End}_G(\pi)$ is a scalar: $\operatorname{End}_G(\pi) = \mathbb{C}\cdot 1$ for a complex irreducible unitary representation.

**Proof.** (b) first, in the form needed for (a). Let $A \in \operatorname{End}_G(\pi)$ be self-adjoint. The operator $A^2$ is a positive self-adjoint intertwiner. If $A^2$ were not a scalar, then by the spectral theorem for self-adjoint operators (Part III) it would have a spectral projection $P$ onto a nontrivial part of its spectrum; $P$ is a strong limit of polynomials in $A^2$, hence an intertwiner, and its image is a proper nonzero closed invariant subspace, contradicting irreducibility. So $A^2 = \mu 1$ with $\mu \geq 0$, and again by the spectral theorem $A = \sqrt{\mu}\,P - \sqrt{\mu}\,(1 - P)$ for the spectral projection $P$ of the positive part of the spectrum, which is an intertwiner; irreducibility forces $P = 0$ or $P = 1$, so $A$ is scalar. Every $T \in \operatorname{End}_G(\pi)$ is a complex combination $T = \tfrac12 (T + T^*) - \tfrac{i}{2}\, i(T - T^*)$ of the two self-adjoint intertwiners $T + T^*$ and $i(T - T^*)$, so $T$ is scalar as well: $\operatorname{End}_G(\pi) = \mathbb{C}\cdot 1$. In finite dimensions the same conclusion follows directly from the existence of an eigenvalue and the invariance of its eigenspace, by the fundamental theorem of algebra.

(a) Let $T \in \operatorname{Hom}_G(\pi, \pi')$ be nonzero. Then $T^*T$ is a nonzero positive self-adjoint intertwiner of $\pi$, so by (b) $T^*T = \lambda 1$ with $\lambda = \|T\|^2 > 0$, and $U = T/\sqrt{\lambda}$ satisfies $U^*U = 1$. The operator $UU^*$ is a positive self-adjoint intertwiner of $\pi'$ and a projection; by (b) $UU^* = \mu 1$ with $\mu \in \{0, 1\}$, and $U \neq 0$ gives $\mu = 1$, so $U$ is unitary and $T$ is an isomorphism. Hence $\operatorname{Hom}_G(\pi, \pi') = 0$ for inequivalent irreducible $\pi, \pi'$. The spectral-theoretic input — the existence of a nontrivial spectral projection, and the functional calculus giving it as a strong limit of polynomials — is the spectral theorem of Part III; the finite-dimensional argument is self-contained and covers the cases used in this article and in the compact theory, and the general statement is quoted as standard. $\square$

**Corollary.** A unitary representation $\pi$ is irreducible if and only if $\operatorname{End}_G(\pi) = \mathbb{C}\cdot 1$; and if $G$ is abelian then every irreducible unitary representation is one-dimensional. More generally, if $A$ is a closed abelian normal subgroup of $G$, the operators $\pi(a)$, $a \in A$, span a representation of the abelian group $A$ that is normalised by $\pi(G)$; the analysis of the commutant of $\pi$, and with it the classification of the irreducibles of $G$, is then governed by the action of $G$ on the dual $A^\vee$, which is the Mackey machine.

**Proof.** The first statement is Schur's lemma in one direction, and the converse is the observation that the orthogonal projection onto a closed invariant subspace is an intertwiner, so a nontrivial invariant subspace gives a non-scalar self-adjoint intertwiner. For abelian $G$, the operators $\pi(g)$ commute with all $\pi(h)$, so lie in the commutant, which is scalar; hence each $\pi(g)$ is scalar and the representation is one-dimensional. $\square$

### The Commutant and Multiplication Operators

**Proposition.** Let $\pi$ be a unitary representation. The commutant $\pi(G)' = \operatorname{End}_G(\pi)$ is a strongly closed self-adjoint subalgebra of $B(\mathcal{H}_\pi)$ containing $1$: a **von Neumann algebra**. If $\pi = \bigoplus_{i \in I}\pi_i$ is a direct sum of irreducible representations, then

$$
\operatorname{End}_G(\pi) \cong \prod_i \mathbb{C}\cdot 1_{\mathcal{H}_{\pi_i}} \qquad \text{when the } \pi_i \text{ are pairwise inequivalent,}
$$

and the commutant is larger, by matrix algebras over the multiplicities, when equivalences occur. The general structure theory of such commutants is that in Part II, and the classification of the group representations by the type of the commutant is not covered here.

**Proof.** The commutant is the intersection over $g$ of the kernels of the strongly continuous maps $T \mapsto T\pi(g) - \pi(g)T$, hence strongly closed; it is a subalgebra, contains $1$, and is self-adjoint by the proposition on intertwiners. For a direct sum of pairwise inequivalent irreducibles, an intertwiner restricts to an intertwiner on each summand, $\operatorname{Hom}_G(\pi_i, \pi_j) = 0$ for $i \neq j$, and $\operatorname{End}_G(\pi_i) = \mathbb{C}$, giving the product description; when $\pi_i \cong \pi_j$, the summands may be grouped and the multiplicities contribute a full matrix algebra by Schur's lemma. $\square$

## The Compact Case

For a compact group the representation theory is the model case; the analytic proofs of its main theorem belong to Part III, and the statement is recorded here because every other article of the category uses it.

**Theorem (compact representation theory).** Let $K$ be a compact group and let $\pi$ be an irreducible unitary representation of $K$ on $\mathcal{H}_\pi$. Then:

**(a)** $\mathcal{H}_\pi$ is finite-dimensional;

**(b)** every unitary representation of $K$ is a direct sum of irreducible unitary representations, and each irreducible occurs with finite multiplicity in any representation of finite degree;

**(c)** the matrix coefficients $c_{v,w}(g) = \langle \pi(g)v, w\rangle$ of the irreducible representations form an orthogonal family in $L^2(K)$ with respect to the normalised Haar measure, with

$$
\int_K c_{v,w}(g)\,\overline{c_{v',w'}(g)}\,dg = \frac{\langle v, v'\rangle\,\langle w, w'\rangle}{\dim \mathcal{H}_\pi} ,
$$

and the finite linear combinations of matrix coefficients are dense in $L^2(K)$ (Peter–Weyl);

**(d)** when $K$ is a connected compact Lie group, the irreducible unitary representations of $K$ are in bijection with the dominant integral weights of a maximal torus, in the classification of *Root Systems and Classification* and *Representations of Lie Algebras*, and the character of an irreducible representation is a Schur function on the torus (Weyl character formula).

**Pro.** The proof of (a) averages an inner product over $K$ using the Haar integral of *Locally Compact Groups and Haar Measure* and then shows by a compact-operator argument that an irreducible space is finite-dimensional; (b) is the decomposition of the regular or a given representation by the spectral theorem for compact self-adjoint operators; (c) is the orthogonality of the matrix coefficients under the invariant integral, together with the density statement of Peter–Weyl; (d) is the highest-weight theory of compact Lie groups. All four use the invariant integral and the spectral theory of compact operators and are therefore established,; the statements are quoted here as standard, and the finite-dimensional classification is that of Part I. $\square$

**Example ($SU(2)$ and $SO(3)$).** For $K = SU(2)$ the irreducible unitary representations are parametrised by the half-integers $j = 0, \tfrac12, 1, \tfrac32, \dots$, with $\dim V_j = 2j+1$; the representation $V_j$ is the $2j$-th symmetric power of the defining two-dimensional representation, and its character is the Weyl character $[2j+1]_{\text{sym}}$. The centre $\{\pm 1\}$ acts by $(-1)^{2j}$, so the representations with half-integral $j$ descend to projective representations of $SO(3)$ and the integral ones to genuine representations, the spin representations being the half-integral cases; the tensor product decomposes by the Clebsch–Gordan rule $V_j \otimes V_k \cong \bigoplus_{r} V_r$ with $r$ running over $|j-k| \leq r \leq j+k$ in steps of $1$. These are the finite-dimensional irreducible representations of Part I, made unitary by the Weyl unitary trick. The general compact semisimple case is Weyl's theorem: the finite-dimensional representation theory of a compact connected Lie group is that of its complexified Lie algebra, classified by highest weights.

**Example (compact abelian groups).** If $K$ is compact abelian, the irreducibles are the characters $K \to S^1$ and the Peter–Weyl theorem becomes the statement that the characters form an orthonormal basis of $L^2(K)$; the decomposition of $L^2(K)$ into the one-dimensional characters is the Fourier expansion of a function on $K$, and it is the harmonic analysis in Part III. The dual $K^\vee$ here is the Pontryagin dual of *Pontryagin Duality*, discrete because $K$ is compact.

**Example (finite groups).** A finite group is compact and discrete, and every unitary representation is finite-dimensional and completely reducible; this is the classical theory of *Representations of Groups*, where the group algebra $\mathbb{C}[G]$ decomposes as $\bigoplus_i \operatorname{End}(V_i)$ and the irreducible characters satisfy the orthogonality relations. The Haar measure is the normalised counting measure, and the orthogonality relations of that article are the compact orthogonality relations with the integral replaced by the average over $G$.

## The General Case and the Unitary Dual

### The Unitary Dual

**Definition.** The **unitary dual** of a locally compact group $G$, written $\operatorname{Irr}(G)$, is the set of unitary equivalence classes of irreducible unitary representations of $G$. The notation $\operatorname{Irr}(G)$ is used in preference to a hat, which the corpus reserves for completions. The dual carries the trivial class $1_G$; a class is a **character** when the representation is one-dimensional, which is the abelian case.

**Example.** For a locally compact abelian group $\operatorname{Irr}(G) = G^\vee$; for a compact group $\operatorname{Irr}(K)$ is the discrete set of dominant weights of the theorem above; for the additive group $\mathbb{R}^n$ the irreducible unitary representations are the characters $x \mapsto e^{2\pi i\langle \xi, x\rangle}$ and $\operatorname{Irr}(\mathbb{R}^n) = \mathbb{R}^n$; for a finite group $\operatorname{Irr}(G)$ is the finite set of irreducible complex characters of *Representations of Groups*.

**Example (the Heisenberg group and the orbit method).** For the Heisenberg group $H$ of upper triangular unipotent $3 \times 3$ real matrices the irreducible unitary representations are the one-parameter family of infinite-dimensional representations $\pi_\lambda$ with central character $e^{i\lambda t}$, $\lambda \in \mathbb{R} \smallsetminus \{0\}$ — the classical model is realised on the square-integrable functions of the line, an object of Part III quoted here as the standard realisation — together with the one-dimensional characters of $H$, which are the representations trivial on the centre. The theorem of Stone–von Neumann identifies each $\pi_\lambda$ up to unitary equivalence, and the coadjoint action on the dual of the Lie algebra has for its orbits the planes $\lambda \neq 0$, one for each $\lambda$ and each carrying the class of $\pi_\lambda$, together with the points of the plane $\lambda = 0$, which carry the characters. This is the model of the **orbit method** of Kirillov, in which the unitary dual of a nilpotent (, conjecturally and in many cases provably, a solvable) Lie group is parametrised by the coadjoint orbits; it is developed and quoted from the literature where the method is used.

**Example (semisimple groups).** For $G = SL_2(\mathbb{R})$ the irreducible unitary representations fall into the **principal series**, induced from characters of the Borel subgroup and parametrised by a unitary character and a real parameter, the **discrete series**, which are the square-integrable representations and are isolated in the dual, and the **complementary series**; the classification is due to Bargmann and Gelfand–Naimark and is the historical origin of the subject. The decomposition of $L^2(G)$ into irreducible pieces is the Plancherel formula of Part III, and the induced representations supply the principal series.

### Representations of Lie Groups and the Algebraic Frame

**Theorem (differentiable vectors and $(\mathfrak{g}, K)$-modules).** Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$ and let $\pi$ be a unitary representation of $G$ on $\mathcal{H}$. The space $\mathcal{H}^\infty$ of **smooth vectors** — those $v$ for which $g \mapsto \pi(g)v$ is $C^\infty$ — is a dense $G$-invariant subspace of $\mathcal{H}$, and the derived action

$$
d\pi(X)v = \frac{d}{dt}\Big|_{t=0} \pi(\exp tX)v , \qquad X \in \mathfrak{g},\ v \in \mathcal{H}^\infty ,
$$

makes $\mathcal{H}^\infty$ a module over the universal enveloping algebra of $\mathfrak{g}$; the derived action is a representation of the Lie algebra $\mathfrak{g}$ by skew-adjoint operators, $d\pi(X)^* = -d\pi(X)$. When $G$ is a reductive Lie group with maximal compact subgroup $K$, the space $\mathcal{H}^\infty$ with its $K$-finite part is a $(\mathfrak{g}, K)$-module, and the irreducible unitary representations of $G$ correspond to irreducible $(\mathfrak{g}, K)$-modules with an invariant Hermitian form; this is the algebraic frame of the representation theory.

**Proof sketch.** The smoothness of $g \mapsto \pi(g)v$ is a local condition, and the density of the smooth vectors follows from the smoothing of $v$ against a compactly supported smooth function on $G$ with the Haar integral; the derived action is defined by the Lie derivative and satisfies the Lie algebra relations because $g \mapsto \pi(g)$ is a homomorphism. The correspondence with $(\mathfrak{g}, K)$-modules is the theorem of Harish-Chandra and is quoted as standard. The differential-geometric objects — vector fields, the exponential map, the universal enveloping algebra on the Lie-algebraic side — are those of *The Lie Algebra and the Exponential Map*, *The Lie Correspondence and the Adjoint Representation* and *Representations of Lie Algebras*; no derivative is taken in the analytic sense beyond the $C^\infty$ differentiability of a curve of vectors, which is the Lie-theoretic frame of Part I. $\square$

## The Boundary with Harmonic Analysis

The representation-theoretic objects above are the input to the analytic theory, and the analytic conclusions are Part III.

- The **regular representation** $\lambda$ of $G$ on $L^2(G)$, defined by $\lambda(g)f(x) = f(g^{-1}x)$, requires the construction of $L^2(G)$, the completeness of which is Part III; the **left and right regular representations** and their relation to the group algebra are treated in *Analysis on Groups*.
- The **convolution algebra** $L^1(G)$ and the **group $C^*$-algebra** $C^*(G)$, with the correspondence between nondegenerate representations of $C^*(G)$ and unitary representations of $G$, are Part III and the operator-algebra articles of *Topology on Linear Algebras*; the group von Neumann algebra is treated.
- The **Peter–Weyl theorem** and the **Plancherel theorem**, the decomposition of a unitary representation into a direct integral of irreducibles over $\operatorname{Irr}(G)$, and the notion of a **tempered** representation are Part III.
- What is *not* deferred: the representation theory as such — equivalence, irreducibility, intertwiners, Schur's lemma, tensor products, contragredients, restrictions, and the classification statements in the compact and abelian cases — is developed here and in the next three articles, and is used throughout the corpus.

## Summary

A unitary representation of a locally compact group $G$ is a strongly continuous homomorphism $\pi : G \to U(\mathcal{H})$ into the unitary group of a Hilbert space; strong, weak and matrix-coefficient continuity coincide, and the identity $\|\pi(g)v - v\|^2 = 2\|v\|^2 - 2\operatorname{Re}\langle\pi(g)v, v\rangle$ is the basic tool. Intertwiners, unitary equivalence, subrepresentations, direct sums, tensor products and contragredients form the algebraic frame; every closed invariant subspace has a closed invariant orthogonal complement, so unitary representations are reduced by their invariant subspaces, and finite-dimensional ones are completely reducible.

Schur's lemma states that the commutant of an irreducible unitary representation is $\mathbb{C}\cdot 1$ (the finite-dimensional case proved by eigenvalues, the general case by the spectral theorem of Part III), that intertwiners between inequivalent irreducibles vanish, and that the irreducible unitary representations of an abelian group are exactly its characters, so that the unitary dual of an abelian group is its Pontryagin dual. For a compact group the irreducibles are finite-dimensional, every unitary representation is a direct sum of them with finite multiplicities, the matrix coefficients satisfy the orthogonality relations and are dense in $L^2(K)$ (Peter–Weyl), and the irreducibles are classified by dominant weights; the proofs of these facts use the invariant integral and the spectral theory of compact operators and belong to Part III.

The unitary dual $\operatorname{Irr}(G)$ is the set of equivalence classes of irreducible unitary representations; it is $G^\vee$ for abelian $G$, the dominant weights for compact $G$, the coadjoint orbits for a nilpotent Lie group by the orbit method, and a union of principal, discrete and complementary series for $SL_2(\mathbb{R})$. The decomposition of an arbitrary unitary representation into a direct integral over $\operatorname{Irr}(G)$, the convolution algebra $L^1(G)$, the group $C^*$-algebra, the regular representation and the Plancherel theorem are *Analysis on Groups* in Part III; the algebraic representation theory is completed by the induced representations, Mackey theory and type classification.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{H}$, $\mathcal{H}_\pi$ | Hilbert space; representation space of $\pi$ |
| $\langle \cdot, \cdot\rangle$, $\|\cdot\|$ | Inner product and norm |
| $B(\mathcal{H})$, $U(\mathcal{H})$ | Bounded operators; unitary group, a topological group |
| $T^*$, $T = T^*$, $T \geq 0$ | Adjoint; self-adjoint; positive operator |
| strong, weak operator topology | Topologies of pointwise convergence of $Tv$ and of $\langle Tv, w\rangle$ |
| $\pi : G \to U(\mathcal{H})$ | A unitary representation; $\deg \pi = \dim \mathcal{H}_\pi$ |
| $c_{v,w}(g) = \langle\pi(g)v, w\rangle$ | Matrix coefficient of $\pi$ |
| $\operatorname{Hom}_G(\pi, \pi')$ | Space of intertwiners |
| $\operatorname{End}_G(\pi) = \pi(G)'$ | Commutant of $\pi$; a von Neumann algebra |
| $\pi \cong \pi'$ | Unitary equivalence |
| irreducible | Only invariant closed subspaces are $0$ and $\mathcal{H}$ |
| completely reducible | Direct sum of irreducibles |
| $1_G$ | Trivial one-dimensional representation |
| $\operatorname{Irr}(G)$ | Unitary dual: irreducible unitary representations up to equivalence |
| $G^\vee$ | Pontryagin dual; equals $\operatorname{Irr}(G)$ for abelian $G$ |
| $V_j$, $j \in \tfrac12\mathbb{Z}_{\geq 0}$ | Irreducible representations of $SU(2)$, $\dim V_j = 2j+1$ |
| $\pi_\lambda$, $\lambda \in \mathbb{R}^\times$ | Stone–von Neumann representations of the Heisenberg group |
| $\mathcal{H}^\infty$, $d\pi(X)$ | Smooth vectors and derived Lie-algebra action |
| $(\mathfrak{g}, K)$-module | Algebraic frame for reductive $G$ |
| $L^2(G)$, $L^1(G)$, $C^*(G)$ | Part III objects: regular representation, convolution algebra, group $C^*$-algebra |
| $dg$ | Haar measure of $G$, from *Locally Compact Groups and Haar Measure* |





## Further Reading

- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for unitary representations, Schur's lemma and the compact theory.
- Jacques Dixmier, *Les $C^*$-algèbres et leurs représentations* (Gauthier-Villars, 1964; English translation North-Holland, 1977), for the algebraic frame and the unitary dual.
- George W. Mackey, *The Theory of Unitary Group Representations* (University of Chicago Press, 1976), for the general theory and its applications.
- Israel M. Gelfand, Mark A. Naimark, *Unitäre Darstellungen der klassischen Gruppen* (Akademie-Verlag, 1957), for the classical representation theory of the classical groups.
- Serge Lang, *$SL_2(\mathbb{R})$* (Springer, 1975; reprinted 1998), for the principal, discrete and complementary series.
- V. S. Varadarajan, *An Introduction to Harmonic Analysis on Semisimple Lie Groups* (Cambridge University Press, 1999), for the representation theory of semisimple groups and the Plancherel theory.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the $(\mathfrak{g}, K)$-module framework and the classification.
- Daniel Bump, *Lie Groups* (Springer, 2nd ed. 2013), for the analytic input and the classical examples.
- Theodore W. Palmer, *Banach Algebras and the General Theory of $*$-Algebras* (Cambridge University Press, 1994), for the operator-algebraic background.
