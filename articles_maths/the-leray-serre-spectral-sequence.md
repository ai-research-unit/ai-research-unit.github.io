
# __The Leray–Serre Spectral Sequence__

## Introduction

A fibration $p : E \to B$ with fibre $F$ relates the three spaces by the long exact sequence on homotopy groups of *Homotopy Groups and Fibrations*, but homotopy groups are not computable and the sequence does not determine the homology of $E$. The **Leray–Serre spectral sequence** supplies the homology: it is a spectral sequence whose second page is the homology of the base with coefficients in the homology of the fibre,

$$
E^2_{p,q} = H_p\bigl(B; H_q(F;R)\bigr) \ \Longrightarrow \ H_{p+q}(E;R),
$$

converging to the homology of the total space. It is the machine that computes the homology of a loop space from that of a sphere, the homology of a classifying space from that of a group, and the transgression and edge homomorphisms that generalise the exact sequence of a fibration to all degrees.

The general theory of spectral sequences — filtered complexes, exact couples, convergence, the comparison theorem — is the subject of the companion article *Spectral Sequences* of Part I, which is being written in parallel, and none of it is re-derived here. What this article does is the *topological* instance: it constructs the filtration of the singular chains of the total space by the skeleta of the base, identifies the $E^2$ page, states the convergence and the multiplicative structure, and computes. This division is deliberate and is the corpus's general organisation: the algebra of derived functors and spectral sequences belongs to Part I, the topological and geometric instances belong here.

Two further articles of this batch depend on the present one:which runs the spectral sequence for the fibrations $G/H \to BH \to BG$, , which uses the Atiyah–Hirzebruch spectral sequence. The article closes by recording the **Leray–Serre spectral sequence with local coefficients**, in which the fundamental group of the base acts on the homology of the fibre, and the **Wang sequence** of a fibration over a sphere.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$; coefficients are in $R$ unless a coefficient system is named; a fibration means a Serre fibration, as in *Homotopy Groups and Fibrations*. The spectral sequence is indexed homologically unless stated, with total degree $n = p+q$.

## The Algebraic Input

### Filtered Complexes and Spectral Sequences

**Definition (quoted from Part I).** A **spectral sequence** is a sequence of bigraded $R$-modules $(E^r_{p,q}, d^r)$ for $r \geq r_0$, with differentials

$$
d^r : E^r_{p,q} \longrightarrow E^r_{p-r,\,q+r-1}, \qquad d^r \circ d^r = 0,
$$

and isomorphisms $E^{r+1}_{p,q} \cong \ker d^r\big|_{E^r_{p,q}} \big/ \operatorname{im} d^r\big|_{E^r_{p+r,\,q-r+1}}$. A spectral sequence **converges** to a graded module $H_*$ with a filtration $0 \subseteq F_0H_n \subseteq F_1H_n \subseteq \cdots \subseteq H_n$ if there are isomorphisms

$$
E^\infty_{p,q} \cong F_p H_{p+q} / F_{p-1}H_{p+q}.
$$

**Theorem (the spectral sequence of a filtration; Part I).** Let $C_*$ be a chain complex of $R$-modules with a decreasing filtration $F_p C_*$ such that for each $n$ the induced filtration on $C_n$ is finite. Then there is a spectral sequence with

$$
E^1_{p,q} = H_{p+q}\bigl(F_p C_* / F_{p+1}C_*\bigr) \ \Longrightarrow \ H_{p+q}(C_*),
$$

whose differential $d^1$ is induced by the boundary of $C_*$.

This theorem, its proof, and the convergence and comparison theorems for spectral sequences are those of the companion article *Spectral Sequences* of Part I, written in parallel; they are used here as stated.

### The Filtration of the Total Space

**Definition.** Let $p : E \to B$ be a fibration with $B$ a CW complex and let $C_*(E;R)$ be the singular chain complex. The **Serre filtration** is

$$
F_p C_n(E;R) = \text{the subgroup spanned by singular simplices } \sigma : \Delta_n \to E
\text{ with } p\sigma(\Delta_n) \subseteq B^{(p)},
$$

where $B^{(p)}$ is the $p$-skeleton of *CW Complexes and Cellular Approximation*, the filtration of $B$ being by skeleta and hence finite on each chain.

For each $n$ the filtration is finite because a singular simplex has compact image, which meets only finitely many open cells of a CW complex. The filtration is compatible with $\partial$ because the boundary of a simplex is contained in the simplex.

**Theorem (the Serre spectral sequence).** Let $p : E \to B$ be a Serre fibration with $B$ a CW complex, and suppose that $B$ is path-connected and that $\pi_1(B, b_0)$ acts trivially on $H_*(F;R)$ for the fibre $F$ over $b_0$. Then the spectral sequence of the Serre filtration has

$$
E^2_{p,q} = H_p\bigl(B; H_q(F;R)\bigr) \ \Longrightarrow \ H_{p+q}(E;R),
$$

with the coefficient module $H_q(F;R)$ constant, and the differential on the second page is

$$
d^2 : E^2_{p,q} \to E^2_{p-2,\,q+1}.
$$

Dually, in cohomology, $E_2^{p,q} = H^p(B;H^q(F;R)) \Rightarrow H^{p+q}(E;R)$, with $d_2 : E_2^{p,q}\to E_2^{p+2,q-1}$.

*Proof sketch.* The $E^1$ page of the filtered complex computes the homology of the graded pieces $F_pC_*/F_{p+1}C_*$. A simplex in $F_p$ but not in $F_{p+1}$ projects to a simplex in a single $p$-cell of $B$; the quotient complex is therefore the relative chain complex of the fibration over the pair $(B^{(p)}, B^{(p-1)})$, and excision identifies it with the chains of a disjoint union of copies of the fibre, one for each $p$-cell. Hence

$$
E^1_{p,q} \cong C_p^{\mathrm{CW}}\bigl(B; H_q(F;R)\bigr),
$$

the cellular chains of $B$ with coefficients in $H_q(F)$, and the differential $d^1$ is the cellular boundary twisted by the action of $\pi_1(B)$; when the action is trivial, $E^2_{p,q} = H_p(B;H_q(F;R))$ as stated. Convergence is the theorem of Part I applied to the Serre filtration. $\square$

**Remark.** The triviality of the action of $\pi_1(B)$ on $H_q(F;R)$ holds automatically when $B$ is simply connected, and when $R = \mathbb{Q}$ and the action is finite it may be replaced by the invariant and coinvariant parts. The general statement with local coefficients is recorded at the end of the article.

## The Exact Sequence of a Fibration, Revisited

### Edge Homomorphisms

**Definition.** In a first quadrant spectral sequence converging to $H_*(E)$, the **edge homomorphisms** are the maps

$$
H_p(E) \longrightarrow E^\infty_{p,0} \subseteq E^2_{p,0} = H_p(B; H_0(F)), \qquad E^2_{0,q} = H_q(F) = H_0(B;H_q(F)) \longrightarrow E^\infty_{0,q} \subseteq H_q(E),
$$

obtained by projecting the filtration quotients. When $B$ is path-connected and $F$ connected, $H_0(F;R) \cong R$ and $H_0(B;H_q(F)) \cong H_q(F)$, so the second is a map $H_q(F) \to H_q(E)$, the map induced by the inclusion of the fibre; the first is a map $H_p(E) \to H_p(B)$, the map induced by $p$.

**Theorem.** The edge homomorphisms coincide with the maps induced by the inclusion $F \hookrightarrow E$ and the projection $p : E \to B$.

*Proof.* A cycle whose simplices all project to the basepoint is a cycle in the fibre, and a cycle whose simplices project into the $0$-skeleton... more precisely, the projection of the filtration identifies the $(0,q)$-entry with the chains in $F$, and the identification of the $(p,0)$-entry passes to the base's cellular chains through $p_\#$. Naturality of the filtration under the inclusion and the projection gives the identification on homology. $\square$

### The Five-Term and Low-Degree Exact Sequences

**Theorem (the five-term exact sequence).** For a fibration $F \to E \to B$ as in the theorem above, the low-degree terms of the spectral sequence give the exact sequence

$$
H_2(E;R) \to H_2(B;R) \xrightarrow{\ \tau\ } H_1(F;R)_B \to H_1(E;R) \to H_1(B;R) \to 0,
$$

where the subscript denotes the coinvariants under the action of $\pi_1(B)$ (no subscript when the action is trivial), and $\tau$ is the **transgression**, which in these degrees is the differential $d^2$. In cohomology the corresponding sequence is

$$
0 \to H^1(B;R) \to H^1(E;R) \to H^1(F;R)^{B} \xrightarrow{\ \tau\ } H^2(B;R) \to H^2(E;R).
$$

*Proof.* These are the statements that in the spectral sequence of a first quadrant double complex all differentials into and out of the entries of total degree $\leq 2$ vanish or are the only ones present; reading off $E^\infty$ from $E^2$ and using the filtration gives the sequences. $\square$

**Definition.** The **transgression** of the spectral sequence of a fibration is the map that a class of the fibre acquires when it survives long enough to receive a differential. In the cohomological indexing $E_r^{p,q} = H^p(B;H^q(F))$, a class of $E_2^{0,q}$ that is killed by $d_2, d_3, \ldots, d_q$ survives to the entry $E_{q+1}^{0,q}$, and $d_{q+1}$ then carries it to $E_{q+1}^{q+1,0}$; this assignment is the transgression

$$
\tau : \operatorname{dom}\tau \subseteq E_2^{0,q} \xrightarrow{\ d_{q+1}\ } E_{q+1}^{q+1,0}.
$$

No differential can leave the entry $(q+1,0)$ in a first quadrant spectral sequence — the target of $d_r$ from that bidegree is $(q+1+r, 1-r)$, with negative second index for $r \geq 2$ — so after the incoming differentials have been factored out the target may be identified with $E_2^{q+1,0}$, and the transgression is written $\tau : E_2^{0,q} \to E_2^{q+1,0}$. Homologically, with the indexing of the five-term sequence above, the transgression is the differential $d^q : E^2_{q,0} \to E^2_{0,q-1}$.

Geometrically, the transgression is the obstruction to extending a class of the fibre to a class of the total space: a class of $H^q(F)$ that is the restriction of a class of $H^q(E)$ transgresses to zero, the classes on which $\tau$ is defined form the subgroup that survives the earlier differentials, and the values of $\tau$ lie in the cohomology of the base one degree higher.

**Remark.** The transgression is the spectral-sequence generalisation of the connecting homomorphism of the long exact sequence of a fibration; for a fibration with fibre an Eilenberg–MacLane space it computes the $k$-invariants, and for the path–loop fibration it produces the suspension isomorphism. It is natural in maps of fibrations.

**Corollary (the exact sequence of a fibration on homology, low degrees).** Comparing the five-term sequence above with the Hurewicz isomorphism $\pi_1^{\mathrm{ab}} \cong H_1$ of *Homotopy Groups and Fibrations* recovers the exactness of the homotopy sequence in degrees one and two; the spectral sequence is thus strictly stronger than the homotopy sequence, since it computes all degrees at once.

## Computations

### Fibrations over Spheres and the Wang Sequence

**Theorem (Wang sequence).** Let $F \to E \to S^n$ be a fibration over the sphere with $n \geq 2$, so that the base is simply connected and the action of $\pi_1(B)$ is trivial. Then the Serre spectral sequence has only two nonzero columns, $p = 0$ and $p = n$, so the only possibly nonzero differential is

$$
d^n : E^n_{n,q} \to E^n_{0,\,q+n-1},
$$

and the spectral sequence collapses at $E^{n+1} = E^\infty$. It need not collapse at $E^2$: for the Hopf fibration below the differential $d^2$ is an isomorphism. Reading the convergence off the two-column filtration gives the long exact sequence

$$
\cdots \to H_p(F) \xrightarrow{\ i_*\ } H_p(E) \xrightarrow{\ p_*\ } H_{p-n}(F) \xrightarrow{\ \partial\ } H_{p-1}(F) \to H_{p-1}(E) \to \cdots,
$$

the **Wang sequence** of the fibration; the map $\partial$ is the differential $d^n$ in the indexing of the sequence. The sequence does not split in general: for the Hopf fibration the term $H_1(E) = H_1(S^3)$ vanishes while $H_1(F) \oplus H_{1-n}(F) = H_1(S^1) \cong R$, so $H_*(E)$ is not the direct sum of the two columns.

*Proof.* The $E^2$ page has $E^2_{p,q} = H_p(S^n;H_q(F))$, which is nonzero only for $p = 0$ and $p = n$; hence the only possibly nonzero differential is $d^n : E^n_{n,q} \to E^n_{0,q+n-1}$, and the spectral sequence collapses at $E^{n+1} = E^\infty$. Reading the convergence off the filtration gives the exact sequence. $\square$

**Example (the Hopf fibration).** For $F = S^1$, $E = S^3$, $B = S^2$ and $n = 2$, the Wang sequence is

$$
\cdots \to H_p(S^1) \to H_p(S^3) \to H_{p-2}(S^1) \xrightarrow{\ \partial\ } H_{p-1}(S^1) \to H_{p-1}(S^3) \to \cdots,
$$

and in degree $p = 2$ it reads $H_2(S^1) \to H_2(S^3) \to H_0(S^1) \to H_1(S^1) \to H_1(S^3)$, that is, $0 \to 0 \to R \xrightarrow{\ \cong\ } R \to 0$. The spectral sequence therefore has its only nonzero differential $d^2$ mapping $E^2_{2,0} = H_2(S^2;H_0(S^1)) \cong R$ isomorphically onto $E^2_{0,1} = H_1(S^1) \cong R$, and it reads off the known homology $H_0(S^3) = H_3(S^3) = R$ with all other reduced groups zero. The geometric content is that the fundamental class of the fibre transgresses to the fundamental class of the base.

**Example (the loop space of a sphere, in the small dimensions).** For the path–loop fibration $\Omega S^n \to PS^n \to S^n$ with $PS^n$ contractible, the Wang sequence computes the homology of $\Omega S^n$ from that of the point, and since it reads $H_i(\Omega S^n) \cong H_{i-n+1}(\Omega S^n)$ it gives a periodicity of $n-1$. For $S^2$ the period is one, so

$$
H_k(\Omega S^2;R) \cong R \text{ for every } k \geq 0,
$$

while for $S^3$ the period is two and, since there is nothing in negative degrees, the groups vanish in odd degree:

$$
H_k(\Omega S^3;R) \cong \begin{cases} R, & k \text{ even}, \\ 0, & k \text{ odd.}\end{cases}
$$

The general statement, that $\Omega S^n$ has the homology of a free monoid on a single generator of degree $n-1$, is the content of the James construction and of the Bott–Samelson theorem; the rational statement is used through the Chern character.

### Eilenberg–MacLane Spaces and the Path–Loop Fibration

**Definition.** For an abelian group $\pi$ and $n \geq 1$, an **Eilenberg–MacLane space** $K(\pi,n)$ is a CW complex with $\pi_n \cong \pi$ and all other homotopy groups zero; the construction, the functoriality and the standard cases are those of *Classifying Spaces and Cohomology Operations*, above this article, and are used here as they stand there.

**Theorem (the path–loop spectral sequence).** For $n \geq 2$ and $X = K(\pi,n)$ with $\pi$ finitely generated, the path–loop fibration $\Omega X \to PX \to X$ gives a spectral sequence

$$
E^2_{p,q} = H_p\bigl(K(\pi,n); H_q(\Omega X;R)\bigr) \Longrightarrow H_{p+q}(PX;R) = \begin{cases} R, & p+q = 0, \\ 0, & \text{otherwise},\end{cases}
$$

and the collapse of the target computes $H_*(K(\pi,n);R)$ from $H_*(\Omega K(\pi,n);R)$ by an induction in the total degree.

**Example.** For $n = 2$ and $\pi = \mathbb{Z}$, the first computations give $H_0(K(\mathbb{Z},2)) = R$, $H_1 = 0$, $H_2 = R$ generated by the fundamental class $\iota_2$, $H_3 = 0$, and $H_4 \cong R$ generated by $\iota_2^2$; this is the pattern of a polynomial algebra. Indeed $K(\mathbb{Z},2) = \mathbb{CP}^\infty$, whose cohomology is the polynomial ring $R[x]$ with $|x| = 2$, consistent with the ring structure of *Cup and Cap Products*. For $n$ odd and $\pi = \mathbb{Z}$ the answer is an exterior algebra on a generator of degree $n$, and for $n$ even, a divided polynomial algebra; these are the standard computations of the cohomology of Eilenberg–MacLane spaces.

**Remark.** The path–loop method is the standard route to the cohomology of Eilenberg–MacLane spaces, and it is the input to obstruction theory and to the Postnikov tower, which assembles a space from its homotopy groups by a sequence of fibrations with Eilenberg–MacLane fibres. The $k$-invariants appearing at each stage are the transgressions of the corresponding path–loop spectral sequence, and they are the cohomology operations of the stable theory.

## Multiplicativity and Local Coefficients

### The Product Structure

**Theorem.** Let $p : E \to B$ be a fibration with fibre $F$ and $B$ simply connected. Then the Leray–Serre spectral sequence in cohomology is a spectral sequence of rings: there is a product

$$
\smile : E_r^{p,q} \otimes_R E_r^{p',q'} \longrightarrow E_r^{p+p',q+q'}
$$

satisfying the Leibniz rule $d_r(x \smile y) = d_r x \smile y + (-1)^{p+q}x \smile d_r y$, and on the $E_2$ page it is the cup product

$$
H^p(B;H^q(F;R)) \otimes H^{p'}(B;H^{q'}(F;R)) \to H^{p+p'}(B;H^{q+q'}(F;R))
$$

induced by the cross product and the multiplication of $H^*(F;R)$. The product on $E_\infty$ induces the cup product on $H^*(E;R)$.

*Proof sketch.* The product is induced by the Eilenberg–Zilber map of *Cup and Cap Products* applied to the filtered complexes: $\Xi$ is compatible with the filtrations because the product of a simplex projecting to $B^{(p)}$ with one projecting to $B^{(p')}$ projects to $B^{(p+p')}$. The Leibniz rule is the derivation property of the differential, and the identification on $E_2$ uses the Künneth theorem of *Cup and Cap Products* for the tensor product of the base's cochains with $H^*(F)$. $\square$

**Corollary.** If the coefficient module $H^*(F;R)$ is free over $R$ and the spectral sequence degenerates, then $E_2 = E_\infty = H^*(B;R)\otimes_R H^*(F;R)$ by the universal coefficient theorem, so $H^*(E;R)$ is the associated graded of a filtration of that tensor product, and the edge homomorphisms assemble into the successive quotients of the filtration. For a fibration $F \to E \to B$ with $B$ simply connected and $R$ a field, the multiplicativity of the spectral sequence makes the computation of $H^*(E;R)$ from the $E_2$ page a computation of rings and not merely of groups.

**Example (the transgression of the Euler class).** For an oriented sphere bundle $S^{n-1} \to E \to B$ with $B$ simply connected, the only possible differential is $d^n : E_n^{0,n-1} \to E_n^{n,0}$, from the fundamental class of the fibre to the top cohomology of the base; the transgression of that class is the **Euler class** $e \in H^n(B;R)$ of the bundle. The Euler class is thus a cohomology class of the base measuring the failure of the sphere bundle to admit a section, and it is the basic example of a characteristic class; the characteristic-class theory itself is the subject of *Fibre Bundles, Connections and Curvature* and of *Characteristic Classes*, both earlier in this Part.

### Local Coefficients

**Definition.** Let $p : E \to B$ be a fibration with $B$ path-connected and fibre $F$ over $b_0$. The **monodromy** of the fibration is the action of $\pi_1(B,b_0)$ on $H_*(F;R)$ obtained by lifting loops in $B$ to homotopy equivalences of $F$ over the loop, as in *Homotopy Groups and Fibrations*. The corresponding local coefficient system on $B$ is written $\mathcal{H}_q(F;R)$.

**Theorem (Leray–Serre with local coefficients).** For a Serre fibration $p : E \to B$ with $B$ path-connected, there is a first quadrant spectral sequence

$$
E^2_{p,q} = H_p\bigl(B; \mathcal{H}_q(F;R)\bigr) \Longrightarrow H_{p+q}(E;R),
$$

the homology of $B$ with coefficients in the local system $\mathcal{H}_q(F;R)$; when the monodromy is trivial this is the constant-coefficient statement above. The theory of local coefficients is the sheaf theory of andwritten later in this batch, and the identification of $H_*(B;\mathcal{H})$ with the cohomology of the corresponding sheaf is made there.

**Remark.** The monodromy is the reason the orientation hypothesis appears with a coefficient twist in the Gysin and Thom sequences of *Fibre Bundles, Connections and Curvature*: an oriented bundle is one whose top local system is constant.

## Summary

The Leray–Serre spectral sequence is the spectral sequence of the filtration of the singular chains of the total space of a fibration by the skeleta of the base. Its second page is the homology of the base with coefficients in the homology of the fibre, $E^2_{p,q} = H_p(B;H_q(F;R))$, and it converges to the homology of the total space; dually in cohomology, $E_2^{p,q} = H^p(B;H^q(F;R)) \Rightarrow H^{p+q}(E;R)$. The construction uses the filtration theorem for a filtered chain complex, which is the algebraic input of Part I's *Spectral Sequences* and is not re-derived here.

The edge homomorphisms of the spectral sequence are the maps induced by the inclusion of the fibre and the projection to the base, and the transgression is the differential carrying a class of the fibre to one of the base. In low degrees the spectral sequence reduces to the five-term exact sequence relating $H_1$ and $H_2$ of the three spaces, which recovers and extends the long exact sequence of a fibration on homotopy groups. The spectral sequence is multiplicative, with the cup product on the $E_2$ page induced by the cross product and the product of $H^*(F)$; this makes the computation of the cohomology ring of the total space a ring computation, and it produces the transgression whose value on the fundamental class of the fibre is the Euler class of a sphere bundle. For a fibration over a sphere the Wang sequence isolates the single differential, and it computes the homology of loop spaces and of Eilenberg–MacLane spaces; and with the triviality of the monodromy removed, the coefficients become a local system, which is the sheaf-theoretic form of the theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p : E \to B$, $F$ | Fibration, total space, base, fibre (Serre fibration) |
| $E^r_{p,q}$, $d^r$ | Spectral sequence pages and differentials, $d^r : E^r_{p,q} \to E^r_{p-r,q+r-1}$ |
| $E^2_{p,q} = H_p(B;H_q(F;R))$ | Leray–Serre $E^2$ page, homology form |
| $E_2^{p,q} = H^p(B;H^q(F;R))$ | Leray–Serre $E_2$ page, cohomology form |
| $\Longrightarrow$ | Convergence: $E^\infty_{p,q} \cong F_pH_{p+q}/F_{p-1}H_{p+q}$ |
| $F_pC_*(E;R)$ | Serre filtration by preimages of the skeleta of $B$ |
| $B^{(p)}$ | $p$-skeleton of the base |
| $\tau$ | Transgression; in cohomology $\tau : E_2^{0,q}\to E_2^{q+1,0}$ |
| Edge homomorphism | $H_q(F) \to H_q(E)$ and $H_p(E) \to H_p(B)$ |
| Five-term sequence | $H_2(E) \to H_2(B) \to H_1(F)_B \to H_1(E) \to H_1(B) \to 0$ |
| Wang sequence | Long exact sequence for a fibration over $S^n$, $n \geq 2$ |
| $K(\pi,n)$ | Eilenberg–MacLane space; $\pi_n \cong \pi$, others zero |
| $e \in H^n(B;R)$ | Euler class; transgression of the fibre's fundamental class |
| $\mathcal{H}_q(F;R)$ | Local coefficient system from the monodromy action of $\pi_1(B)$ |
| $H_p(B;\mathcal{H})$ | Homology with local coefficients |
| $\smile$ | Product on the spectral sequence; Leibniz rule with $d_r$ |
| $R$ | Commutative ring with identity $1 \neq 0$ |



## Further Reading

- Jean-Pierre Serre, *Homologie singulière des espaces fibrés* (Annals of Mathematics 54, 1951), for the original construction of the spectral sequence of a fibration.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the Serre spectral sequence and its edge homomorphisms and transgression.
- John McCleary, *A User's Guide to Spectral Sequences* (Cambridge University Press, 2nd ed. 2001), for the spectral sequence of a fibration with full proofs and many computations.
- Jean Leray, *Sur les anneaux spectraux* (Journal de Mathématiques Pures et Appliquées, 1946), for the original filtered-complex construction.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the de Rham form of the spectral sequence and the transgression of the Euler class.
- Allen Hatcher, *Spectral Sequences* (unpublished notes, 2004), for a concise treatment aimed at the computations of this article.
- Mimura Mamoru and Hirosi Toda, *Topology of Lie Groups* (American Mathematical Society, 1991), for the spectral-sequence computations of the homology of Lie groups and their homogeneous spaces.
