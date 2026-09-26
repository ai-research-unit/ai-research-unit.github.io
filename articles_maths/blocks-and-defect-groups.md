
# __Blocks and Defect Groups__

## Introduction

Let $G$ be a finite group, $p$ a prime dividing $\lvert G\rvert$, $k$ an algebraically closed field of characteristic $p$, and let $k[G] = \bigoplus_BB$ be the decomposition of the group algebra into its indecomposable two-sided ideals: the **blocks** of $G$. The blocks partition the ordinary irreducible characters and the simple modular modules of *Modular Representation Theory* into classes that cannot be mixed by the representations, and to each block is attached a conjugacy class of $p$-subgroups of $G$, its **defect group**, which measures how far the block is from the semisimple case: the principal block, containing the trivial module, has a Sylow $p$-subgroup as its defect group, the blocks of defect zero consist of a single ordinary character and behave as if the characteristic did not divide the order, and in general the defect group controls the decomposition numbers, the Cartan invariants and the way the block restricts to the subgroups of $G$.

The article is the twenty-fifth of the corpus, in the category *Linear Spaces over Linear Algebras*, and it follows *Modular Representation Theory*; it uses the centre of the group algebra and the idempotents as in *Frobenius Algebras* and *Simple and Semisimple Modules*, the decomposition and Cartan matrices of the previous article, the induction and restriction of *Induced Representations*, and the characters of *Character Theory*. It develops the centre and its primitive idempotents, the definition of a block and the partition of the ordinary and modular characters, the central characters and the connectedness criterion, the defect of a character and of a block with the **defect group** and its properties, the first and second main theorems of **Brauer** with the correspondence between the blocks of $G$ and of the normaliser of the defect group, the theory of **Green** of vertices and sources for indecomposable modules, and the classification of the blocks of the symmetric groups by the $p$-cores; the examples are worked out and verified.

The article is algebraic throughout. The blocks are defined by the idempotents of the centre of the group algebra over the field $k$ and over a discrete valuation ring of characteristic zero with residue field $k$, the defect groups are $p$-subgroups, and the correspondence theorems relate the blocks of two finite groups; no completion, no measure and no manifold occurs, and the analytic theory of the modular forms attached to the blocks, and the $p$-adic and Galois-theoretic refinements of the central characters, belong to Part III. The integral lattices over the valuation ring, which underlie the reduction of a block, are the subject, the final article of this category.

Throughout, $G$ is a finite group, $p$ a prime, $k$ an algebraically closed field of characteristic $p$, $\mathcal{O}$ a discrete valuation ring of characteristic zero with residue field $k$ and maximal ideal $(\pi)$, $k[G]$ and $\mathcal{O}[G]$ the group algebras, $Z(k[G])$ the centre, $B$ a block, $e_B$ its central idempotent, $D$ a defect group, $N_G(D)$ the normaliser of $D$, $C_G(D)$ the centraliser, $a = v_p(\lvert G\rvert)$ the $p$-adic valuation of the order of the group, $d(\chi) = a-v_p(\chi(1))$ the **defect** of an ordinary irreducible character, $d(B)$ the defect of a block, $C = D^{\mathsf{T}}D$ the Cartan matrix, and $S_j$, $P_j$ the simple and the projective indecomposable modules.

## The Centre and the Blocks

**Definition.** The **blocks** of $G$ (at the prime $p$) are the indecomposable two-sided ideals of the group algebra $k[G]$: one has

$$
k[G] = \bigoplus_{B}B_1\oplus\cdots\oplus B_s,
$$

the summands being the blocks, each $B$ is an indecomposable algebra with unit $e_B$, the $e_B$ are the primitive idempotents of the centre $Z(k[G])$, they are pairwise orthogonal, $e_Be_{B'} = \delta_{BB'}e_B$, and their sum is the identity. Equivalently the blocks are the maximal sets of the simple and the indecomposable projective modules that cannot be separated: the simple module $S_j$ belongs to $B$ if $e_BS_j\neq0$, the projective indecomposable $P_j$ belongs to the block of $S_j$, and $B$ as an algebra is the direct sum of the projective indecomposables in it.

**Proposition.** The primitive idempotents of $Z(k[G])$ lift to primitive idempotents of $Z(\mathcal{O}[G])$, and the blocks of $\mathcal{O}[G]$ and of $k[G]$ are in a natural bijection, the reduction of an idempotent being the idempotent of the corresponding block; the ordinary irreducible characters are distributed among the blocks of $\mathcal{O}[G]$ by the rule that $\chi$ belongs to $B$ if the central character $\omega_\chi$ of $\chi$ is the restriction to $Z(\mathcal{O}[G])$ of the central character of $B$, and the two partitions — of the ordinary characters and of the modular simple modules — are compatible in the sense that an ordinary irreducible character $\chi$ and a simple modular module $S_j$ are in the same block whenever $d_{\chi j}\neq0$.

*Proof.* The centre of $\mathcal{O}[G]$ is a finite $\mathcal{O}$-algebra which is free of finite rank as an $\mathcal{O}$-module, and the idempotents of its reduction lift because the radical of the centre lies in the maximal ideal of $\mathcal{O}$ and the idempotents are detected by the separable algebra $Z(k[G])$; the central characters of the blocks and of the ordinary characters agree on the common centre, and the compatibility of the partitions with the decomposition numbers is the standard statement that the decomposition matrix is a block diagonal matrix with respect to the two partitions. $\square$

**Definition.** The **central character** of an ordinary irreducible character $\chi$ is the algebra homomorphism

$$
\omega_\chi:Z(k[G])\longrightarrow k, \qquad \omega_\chi(C) = \frac{\lvert C\rvert\,\chi(g_C)}{\chi(1)},
$$

on the class sums $C$ of the conjugacy classes with representative $g_C$; it is a $k$-algebra homomorphism because the class sums multiply by the character-theoretic convolution, and it determines $\chi$ up to the Galois conjugacy of the values. Two ordinary irreducible characters lie in the same block if and only if they are linked by a chain of ordinary characters and simple modular modules with non-zero decomposition numbers; equivalently, the blocks correspond to the connected components of the bipartite graph whose vertices are the ordinary characters and the simple modular modules, with an edge between $\chi$ and $S_j$ whenever $d_{\chi j}\neq0$.

**Theorem (the connectedness criterion, standard).** Two ordinary irreducible characters $\chi,\chi'$ lie in the same block if and only if their central characters agree on the elements of the centre which are linear combinations of the class sums of $p$-regular elements, and the blocks are the connected components of the decomposition matrix as displayed; consequently the number of blocks is the number of the equivalence classes of the relation generated by the non-vanishing of the decomposition numbers.

*Proof (outline).* The idempotent $e_B$ belongs to the centre and acts on the ordinary module of $\chi$ by a scalar; the scalar is $\omega_\chi(e_B)$, and it is non-zero exactly when $\chi$ is in $B$. Working over $\mathcal{O}$ and using the reduction, the scalar is determined by the behaviour of $\omega_\chi$ on the $p$-regular part of the centre, which gives the criterion; the identity of the connected components with the blocks is the standard form of the same computation. The proof is recorded in the references. $\square$

## Defect Groups

**Definition.** Let $\chi$ be an ordinary irreducible character of $G$ and let $p^a$ be the exact power of $p$ dividing $\lvert G\rvert$. The **defect** of $\chi$ is

$$
d(\chi) = a-v_p\bigl(\chi(1)\bigr),
$$

an integer between $0$ and $a$; the integer $p^{d(\chi)}$ is the **defect** of the character, and a character of defect zero is one whose degree is divisible by the full power $p^a$.

**Theorem (Brauer, standard).** Let $B$ be a block of $G$ at the prime $p$. Then:

1. the set $\{d(\chi) : \chi\in B\}$ has a maximum, denoted $d(B)$ and called the **defect** of the block, and $d(\chi)\leq d(B)$ for every $\chi\in B$;
2. there is a $p$-subgroup $D\leq G$, unique up to conjugacy, with $\lvert D\rvert = p^{d(B)}$, the **defect group** of $B$; the defect group of the principal block is a Sylow $p$-subgroup of $G$, and $B$ has defect zero if and only if $D = 1$;
3. a block of defect zero contains exactly one ordinary irreducible character, and its degree is divisible by $p^a$; conversely every ordinary irreducible character of degree divisible by $p^a$ lies alone in a block of defect zero, and that block is isomorphic to the full matrix algebra $M_{\chi(1)}(k)$ over $k$ (respectively to $M_{\chi(1)}(\mathcal{O})$ over $\mathcal{O}$);
4. the decomposition matrix is block diagonal with respect to the partition into blocks, the Cartan matrix of $B$ is a symmetric positive definite matrix with integer entries and positive diagonal, and the inequality $p^{a-d(B)}\mid\chi(1)$ holds for every $\chi\in B$, so that the defect controls the $p$-parts of the degrees in the block.

*Proof (outline).* The defect is defined by the idempotent: the block idempotent $e_B = \sum a_gg$ has the property that $a_g = 0$ unless $g$ is $p$-regular, and the largest $p$-subgroup with respect to which $e_B$ is "stable" has order $p^{d(B)}$; the character-theoretic description of this group is the inequality $p^{a-d}\mid\chi(1)$ for the characters in a block of defect $d$, proved by Brauer by an induction on the group order. The uniqueness up to conjugacy and the case of the principal block are the standard theorems of the theory, and the defect-zero case is the theorem of Brauer on the blocks of defect zero. The proofs are recorded in the references. $\square$

**Definition.** A $k[G]$-module $M$ is **relatively $Q$-projective** for a $p$-subgroup $Q\leq G$ if $M$ is a direct summand of $\operatorname{Ind}_Q^G\operatorname{Res}_Q^GM$; the **vertices** of an indecomposable module $M$ are the minimal such $Q$, which are the conjugates of a single subgroup, and the **source** of $M$ is the indecomposable module of a vertex of which $M$ is a summand of the induced module, defined up to conjugacy.

**Theorem (Green, standard).** Let $M$ be an indecomposable $k[G]$-module. Then:

1. $M$ has a vertex, which is a $p$-subgroup of $G$ defined up to conjugacy, and $M$ is relatively $Q$-projective exactly for the $Q$ containing a conjugate of a vertex; the vertex of an indecomposable projective module is the same for all the projectives of a block and equals the defect group of the block;
2. the vertex of the trivial module is $1$, and a module with vertex $1$ is projective: the modules with trivial vertex are exactly the projective ones;
3. the **Green correspondence** gives a bijection between the indecomposable modules with vertex $Q$ of $G$ and the indecomposable modules with vertex $Q$ of the normaliser $N_G(Q)$, compatible with the induction, the restriction and the Brauer construction;

consequently the defect group of a block is the common vertex of its projective indecomposable modules, and the theory of the vertices and the sources organises the indecomposable modules of $G$ by their defect.

*Proof (outline).* The relative projectivity is characterised by the splitting of the induction and the restriction, and the existence of the minimal subgroup, the uniqueness up to conjugacy and the correspondence are the theorems of Green, proved by the standard trace and induction arguments recorded in the references. $\square$

## The Brauer Correspondence

**Theorem (Brauer's first main theorem, standard).** Let $D$ be a $p$-subgroup of $G$. Then the blocks of $G$ with defect group $D$ are in bijection with the blocks of $N_G(D)$ with defect group $D$; the bijection, called the **Brauer correspondence**, is given by $B\mapsto B^{N_G(D)}$, where $B^{N_G(D)}$ is the unique block of the normaliser receiving the block idempotent of $B$ under the summation map that adds up the coefficients of the conjugates, and the correspondence is compatible with the inclusion of the normaliser in the group.

*Proof (outline).* A block of $G$ with defect group $D$ has its idempotent supported on the $p$-regular elements and stable under the conjugation; the summation map from the centre of $G$ to the centre of the subgroup, defined by the traces with respect to the conjugacy classes of the two groups, carries the primitive idempotent of $B$ to a primitive idempotent of a block of the normaliser with the same defect group, and the map so obtained is a bijection between the two sets of blocks. The proof is the standard one and is recorded in the references. $\square$

**Theorem (Brauer's second main theorem, standard).** Let $B$ be a block of $G$ with defect group $D$ and let $Q$ be a $p$-subgroup of $G$. Then $B$ has a defect group contained in a conjugate of $Q$ if and only if there is a block $b$ of $C_G(Q)$ which is related to $B$ by the Brauer correspondence, that is a block whose block idempotent is the image of the idempotent of $B$ under the **Brauer map**, the trace map from the centre of $k[G]$ to the centre of $k[C_G(Q)]$; equivalently, the defect group of $B$ is the largest $p$-subgroup $D$ for which the corresponding block of the centraliser $C_G(D)$ exists and is not annihilated. The precise form of the theorem, including the description by the $p$-sections of $G$, is recorded in the references.

*Proof (outline).* The theorem is proved by the analysis of the $p$-sections of $G$ — the sets of elements with a fixed $p$-regular part — and the interaction of the block idempotents with the centralisers of the $p$-subgroups; the precise statement is the one recorded in the references, and the version displayed is its standard form. $\square$

**Remark (the block theory as a partition of the representation theory).** The blocks organise the ordinary and the modular representation theory of $G$ into the pieces that cannot be mixed, and the defect group of a block controls the pieces: the Cartan matrix of a block is a block of the global Cartan matrix, the decomposition matrix is block diagonal, the projective indecomposables in a block all have the defect group as vertex by Green's theorem, and the cohomological invariants of the block — its centre, its cohomology and its derived category — are attached to the defect group through the correspondence theorems, the deepest facts of the theory being the "block-theoretic" form of the classification of the modular representations, as in the theory of the Broué conjecture relating a block with abelian defect group to the derived category of its defect group and the associated Hecke algebra.

## Examples and the Blocks of the Symmetric Groups

**Example (the symmetric group $S_3$ at the prime $3$).** Let $G = S_3$ and $p = 3$, so that $a = v_3(6) = 1$. The ordinary irreducible characters are $\mathbf{1}$, $\varepsilon$ and $\sigma$ of degrees $1,1,2$ and the simple modular modules are $S_1$ and $S_2$, both of dimension one; the decomposition matrix is $D = \begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}$, whose bipartite graph is connected — the row of $\sigma$ is adjacent to both simple modules — so that $k[S_3]$ has exactly one block, the principal block, containing all three ordinary characters and both simple modules. The defects of the characters are $d(\mathbf{1}) = d(\varepsilon) = d(\sigma) = 1-0 = 1$, so the block has defect $d(B) = 1$ and defect group a Sylow $3$-subgroup of order $3$, namely the cyclic group generated by a 3-cycle; the Cartan matrix of the block is the verified matrix $C = \begin{pmatrix}2&1\\1&2\end{pmatrix}$ of *Modular Representation Theory*, of determinant $3$, and the projective indecomposables $P_1,P_2$ both have the defect group as vertex by Green's theorem. The case $p = 3$ therefore has no block of defect zero, in accordance with the general fact that the existence of such a block requires a degree divisible by $p^a = 3$, which no degree of $S_3$ satisfies.

**Example (the same group at the prime $2$).** For $p = 2$ and $a = v_2(6) = 1$, the defect of the characters is $d(\mathbf{1}) = d(\varepsilon) = 1$ and $d(\sigma) = 1-v_2(2) = 0$; the block of $\sigma$ has defect $0$, defect group $1$, and consists of the single character $\sigma$, its block algebra being the matrix algebra $M_2(k)$ (respectively $M_2(\mathcal{O})$); the remaining two characters lie in the principal block of defect $1$ with defect group a Sylow $2$-subgroup of order $2$, that is the subgroup generated by a transposition. This is the smallest example in which both cases occur, and the defect groups of the two blocks are found from the degrees alone.

**Theorem (Nakayama's conjecture; Brauer–Robinson, standard).** Let $p$ be a prime and let $\lambda$, $\mu$ be partitions of $n$ indexing the ordinary irreducible characters of $S_n$ as in the theory of the symmetric groups. Then the irreducible characters $\chi^\lambda$ and $\chi^\mu$ lie in the same $p$-block of $S_n$ if and only if the partitions $\lambda$ and $\mu$ have the same $p$-core; consequently the $p$-blocks of $S_n$ are indexed by the $p$-cores, and the defect group of the block of the core $\gamma$ is a Sylow $p$-subgroup of $S_{n-\lvert\gamma\rvert}$, of order $p^{v_p((n-\lvert\gamma\rvert)!)}$.

**Example (the verification for $S_3$).** For $p = 3$ every partition of $3$ — namely $(3)$, $(2,1)$ and $(1,1,1)$ — has a hook of length $3$, so its rim may be removed entirely and the $3$-core of each is the empty partition; all three characters therefore lie in one block, in agreement with the connectedness of the decomposition matrix computed above. For $p = 2$ the partition $(3)$ has a hook of length $2$ and the removal leaves the partition $(1)$, the partition $(1,1,1)$ likewise has $2$-core $(1)$, while the partition $(2,1)$ has the hook lengths $3,1,1$ and no hook of length $2$, so that it is its own $2$-core; hence $(3)$ and $(1,1,1)$ lie in one block and $(2,1)$ in a block of its own with core of size $3 = n$ and weight zero, that is a block of defect zero. The hook lengths of the three partitions of $3$ were recomputed and the presence or absence of the hooks of length $p$ for $p = 3$ and $p = 2$ was confirmed, giving exactly the two block distributions displayed; the correspondence with the defect computation is that the block containing the characters of degree $1,1$ has defect group of order $2$ while the character of degree $2$, whose partition is its own $2$-core, forms the block of defect zero.

## Summary

Let $G$ be a finite group, $p$ a prime dividing $\lvert G\rvert$ and $k$ an algebraically closed field of characteristic $p$. The group algebra decomposes as $k[G] = \bigoplus_BB$ into the **blocks**, the indecomposable two-sided ideals, which are the same as the primitive idempotents of the centre $Z(k[G])$; the idempotents lift to a discrete valuation ring of characteristic zero with residue field $k$, so that the blocks of $k[G]$ and of $\mathcal{O}[G]$ correspond, and the ordinary irreducible characters and the simple modular modules are partitioned into blocks, an ordinary character $\chi$ and a simple module $S_j$ lying together whenever the decomposition number $d_{\chi j}$ is non-zero, the blocks being the connected components of the bipartite graph of the decomposition matrix. To each ordinary irreducible character is attached its **defect** $d(\chi) = a-v_p(\chi(1))$, with $p^a$ the exact power of $p$ dividing $\lvert G\rvert$, and to each block its defect $d(B) = \max_{\chi\in B}d(\chi)$ and its **defect group** $D$, a $p$-subgroup of order $p^{d(B)}$ defined up to conjugacy; the principal block has a Sylow $p$-subgroup as its defect group, a block of defect zero contains exactly one ordinary irreducible character of degree divisible by $p^a$ and is isomorphic to a full matrix algebra, and $p^{a-d(B)}\mid\chi(1)$ for every $\chi$ in $B$. **Green's theory** attaches to every indecomposable module a **vertex**, a $p$-subgroup defined up to conjugacy, and a source, the module being relatively $Q$-projective exactly for the $Q$ containing a vertex; the modules with trivial vertex are the projective ones, and the defect group of a block is the common vertex of its projective indecomposables. **Brauer's first main theorem** puts the blocks of $G$ with defect group $D$ in bijection with the blocks of $N_G(D)$ with defect group $D$, and the second main theorem describes the defect group through the centralisers of the $p$-subgroups and the Brauer construction. For the symmetric groups **Nakayama's conjecture**, proved by Brauer and Robinson, classifies the $p$-blocks by the $p$-cores of the partitions, the defect group of the block of the core $\gamma$ being a Sylow $p$-subgroup of $S_{n-\lvert\gamma\rvert}$. The examples are verified: for $S_3$ at the prime $3$ there is one block of defect $1$ with defect group of order $3$ and the Cartan matrix $\begin{pmatrix}2&1\\1&2\end{pmatrix}$, all three partitions having empty $3$-core, while at the prime $2$ the character $\sigma$, whose partition $(2,1)$ is its own $2$-core, forms a block of defect zero and the other two characters form the principal block of defect $1$. The integral lattices underlying the reduction and the block decomposition over a valuation ring are the subject, the final article of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k[G] = \bigoplus_BB$ | decomposition into blocks, the indecomposable two-sided ideals |
| $e_B$, $Z(k[G])$ | block idempotent, primitive idempotent of the centre |
| $\omega_\chi(C) = \lvert C\rvert\chi(g_C)/\chi(1)$ | central character of an ordinary irreducible character |
| $d_{\chi j}$, $d_{\chi j}\neq0 \iff$ linked | decomposition numbers and connectedness of the blocks |
| $a = v_p(\lvert G\rvert)$, $d(\chi) = a-v_p(\chi(1))$ | $p$-adic valuation of the order, defect of a character |
| $d(B) = \max_{\chi\in B}d(\chi)$ | defect of a block |
| $D$, $\lvert D\rvert = p^{d(B)}$ | defect group, defined up to conjugacy |
| $N_G(D)$, $C_G(D)$, Brauer correspondence | normaliser, centraliser, first main theorem |
| vertex, source, relatively $Q$-projective | Green's theory of indecomposable modules |
| $p$-core of a partition | Nakayama's classification of the blocks of $S_n$ |
| $M_{\chi(1)}(k)$, defect zero | structure of a block of defect zero |



## Further Reading

- Richard Brauer, "On the structure of groups of finite order", *Proceedings of the International Congress of Mathematicians, Amsterdam* **1** (1954), 209–217, and "Zur Darstellungstheorie der Gruppen endlicher Ordnung", *Mathematische Zeitschrift* **63** (1956), 406–444, for the blocks, the defect groups and the main theorems.
- Richard Brauer and Colin J. Nesbitt, "On the modular characters of groups", *Annals of Mathematics* **42** (1941), 556–590, for the decomposition numbers and the first form of the block theory.
- Richard Brauer and Hsio-Fu Tuan, "On simple groups of finite order I", *Bulletin of the American Mathematical Society* **51** (1945), 756–766, for the block theory and the second main theorem.
- Walter Feit, *The Representation Theory of Finite Groups* (North-Holland, 1982), for the systematic treatment of the blocks, the defect groups and the Brauer correspondence.
- J. Alexander Green, "On the indecomposable representations of a finite group", *Mathematische Zeitschrift* **70** (1959), 430–445, for the vertices, the sources and the Green correspondence.
- Tadasi Nakayama, "On some modular properties of irreducible representations of a symmetric group I, II", *Japanese Journal of Mathematics* **17** (1940), 89–108 and 411–423, for the $p$-core classification of the blocks of the symmetric groups; and Richard Brauer and Geoffrey de B. Robinson, "On a conjecture by Nakayama", *Transactions of the Royal Society of Canada* **41** (1947), 11–25, for the proof.
- Michel Broué, "Isométries de caractères et équivalences de Morita ou dérivées", *Publications Mathématiques de l'IHÉS* **71** (1990), 45–63, and Michel Broué and Jørn Olsson, "Subpair multiplicities in finite groups", for the conjecture relating a block with abelian defect group to the derived category of its defect group.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), and *Methods of Representation Theory II* (Wiley, 1987), for the systematic block theory, the defect groups and the Green correspondence.
- Gordon James and Adalbert Kerber, *The Representation Theory of the Symmetric Group* (Addison-Wesley, 1981), for the blocks of $S_n$, the $p$-cores and the modular theory of the symmetric groups.
