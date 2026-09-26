
# __Paracompactness and Partitions of Unity__

## Introduction

A metric space carries a base that is a countable union of locally finite families, and the previous article used this to characterise metrisability. The present article studies the covering property that underlies that base condition, and the device that turns a locally finite cover into a tool for gluing: the partition of unity.

A cover of a space is **locally finite** if every point has a neighbourhood meeting only finitely many of its members. A space is **paracompact** if every open cover has a locally finite open refinement. The definition is due to Dieudonné, who introduced it precisely to isolate the covering condition that metric spaces satisfy and that makes the classical constructions work. The first consequences are that a paracompact Hausdorff space is normal, that every metrisable space is paracompact, and that paracompactness is exactly the hypothesis under which every open cover admits a **partition of unity** subordinate to it — a family of continuous functions with locally finite supports, summing to $1$, each supported in a member of the cover. A partition of unity converts a family of locally defined functions into a globally defined one, and it is the device by which the local data of differential geometry, of fibre bundles and of sheaf theory are assembled.

The article develops paracompactness, its equivalent formulations, the shrinking lemma, the construction of partitions of unity, and the metrisation theorems that connect the notion to distance. The separation axioms used throughout are those of the preceding article, *Metrisation and Separation Axioms*, where Urysohn's lemma, the Tietze theorem and the bump function are proved; the distance and its completeness are those of *Metric, Uniform and Complete Spaces*; and the manifolds, bundles and connections that consume partitions of unity are not covered here. No measure, integral or analytic limit is used, and no physics is invoked.

## Paracompact Spaces

### Covers and Refinements

**Definition.** Let $X$ be a topological space. A family $\mathcal{U} = (U_s)_{s \in S}$ of subsets of $X$ is a **cover** of $X$ if $\bigcup_s U_s = X$, an **open cover** if every $U_s$ is open, and a **closed cover** if every $U_s$ is closed. A family $\mathcal{V} = (V_t)_{t \in T}$ is a **refinement** of $\mathcal{U}$ if for every $t$ there is $s$ with $V_t \subseteq U_s$; it is an **open refinement** if its members are open. The refinement is **point finite** if every point lies in finitely many members, **locally finite** if every point has a neighbourhood meeting finitely many members, and **σ-locally finite** if it is a countable union of locally finite families.

The definitions of local finiteness and discrete families were given in *Metrisation and Separation Axioms*, where their use in the Nagata–Smirnov theorem was recorded. Three elementary facts about locally finite families are used repeatedly and are stated together.

**Proposition.** Let $(A_s)_{s \in S}$ be a locally finite family of subsets of $X$. Then

**(i)** the family $(\overline{A_s})$ is locally finite, and $\overline{\bigcup_s A_s} = \bigcup_s \overline{A_s}$;

**(ii)** if every $A_s$ is closed, then $\bigcup_s A_s$ is closed;

**(iii)** if $f$ is a function whose restriction to $A_s$ is continuous for every $s$, and the family is locally finite with closed members, then $f$ is continuous.

**Proof.** For (i), a neighbourhood of $x$ meeting only $A_{s_1}, \ldots, A_{s_n}$ meets only the corresponding closures, since a neighbourhood of a point of $\overline{A_s}$ must meet $A_s$; hence $(\overline{A_s})$ is locally finite. A point lies in $\overline{\bigcup_s A_s}$ exactly when every neighbourhood meets some $A_s$, which by local finiteness can only happen for one of the finitely many relevant indices, so the point lies in some $\overline{A_s}$; the reverse inclusion is trivial. Part (ii) is the case $f$ equal to the characteristic function of the union, and part (iii) follows because continuity at $x$ involves only the finitely many $A_s$ meeting a neighbourhood of $x$. $\square$

### The Definition and its Equivalent Forms

**Definition.** A topological space $X$ is **paracompact** if every open cover of $X$ has a locally finite open refinement.

The definition is stated for the open cover itself and not merely for an arbitrary cover, and this matters; refining only closed covers would give a weaker notion. Four equivalent formulations are used in practice.

**Theorem.** For a regular space $X$ the following are equivalent:

**(i)** every open cover has a locally finite open refinement;

**(ii)** every open cover has a locally finite refinement by arbitrary sets;

**(iii)** every open cover has a locally finite closed refinement;

**(iv)** every open cover has a σ-locally finite open refinement.

**Proof sketch.** The implications (i) $\Rightarrow$ (ii), (i) $\Rightarrow$ (iv) and (ii) $\Rightarrow$ (iv) are immediate. For (iv) $\Rightarrow$ (i), a σ-locally finite open refinement is made locally finite by shrinking, using regularity: each member is contained in an open set whose closure meets only finitely many members of each locally finite layer, a standard construction (Michael). For (ii) $\Rightarrow$ (i), a locally finite refinement by arbitrary sets is first closed up and then shrunk using regularity and the normality that the locally finite refinement confers. For (iii) $\Rightarrow$ (i), a locally finite closed refinement is expanded to an open one by regularity applied to each closed member inside the member of the original cover that contains it. The full argument is standard and is given in Engelking, §5.1. $\square$

**Remark.** The regularity hypothesis is not a convenience. Without it the four conditions differ, and the definition of paracompactness is conventionally given by (i), the form that behaves well under the constructions of the next sections.

**Theorem (Dieudonné).** A paracompact Hausdorff space is normal, hence $T_4$, and every paracompact Hausdorff space is collectionwise normal: for every discrete family $(F_s)$ of closed sets there is a discrete family $(U_s)$ of open sets with $F_s \subseteq U_s$.

**Proof sketch.** Let $F$ and $G$ be disjoint closed sets and let $\mathcal{U}$ be a locally finite open refinement of the open cover $\{X \setminus F, X \setminus G\}$. Write $\mathcal{U} = \mathcal{U}_F \cup \mathcal{U}_G$ according to which member of the cover each set refines, and put $U = \bigcup \{V : V \in \mathcal{U}_F\}$ and $W = \bigcup\{V : V \in \mathcal{U}_G\}$. Local finiteness makes the closures of the sets in $\mathcal{U}_F$ locally finite, so $\overline{U} \subseteq X \setminus G$; symmetrically $\overline{W} \subseteq X \setminus F$. Hence $U \supseteq F$, $W \supseteq G$, and $U \cap W = \emptyset$. Collectionwise normality is the same argument with the discrete family decomposed by a well-ordering and the locally finite cover refined one closed set at a time; it is a theorem of Bing that every metrisable space is collectionwise normal. $\square$

**Corollary.** Every paracompact Hausdorff space is normal, and every regular paracompact space is normal. Every compact Hausdorff space is paracompact, and every Lindelöf regular space is paracompact: a countable subcover is trivially σ-locally finite, and the shrinking of the previous theorem makes it locally finite.

### The Shrinking Lemma

The tool that turns a locally finite cover into a partition of unity is the possibility of shrinking each member of a cover while retaining the covering property.

**Lemma (shrinking lemma).** Let $X$ be normal and let $(U_s)_{s \in S}$ be a point-finite open cover of $X$. Then there is an open cover $(V_s)_{s \in S}$ indexed by the same set with $\overline{V_s} \subseteq U_s$ for every $s$.

**Proof.** Well-order $S$. For each $s$ put $B_s = X \setminus \bigcup_{t > s} U_t$, a closed set. One constructs, by transfinite induction on $s$, open sets $V_s$ with
$$
\overline{V_s} \subseteq U_s, \qquad B_s \subseteq \bigcup_{t \leq s} V_t .
$$
At the successor step $s$, suppose the second condition holds at every $t < s$ and put
$$
C = B_s \setminus \bigcup_{t < s} V_t .
$$
Then $C$ is closed, and $C \subseteq U_s$: if $x \in C$ and $x \notin U_s$, then by point finiteness the set of indices $r$ with $x \in U_r$ is finite, and since $x \in B_s$ no such index exceeds $s$ and $s$ is not among them, so there is a largest index $t < s$ with $x \in U_t$; the induction hypothesis at $t$ gives $B_t \subseteq \bigcup_{r \leq t} V_r$, and $x \in B_t$ because $x \notin U_r$ for every $r > t$, so $x \in \bigcup_{r \leq t} V_r \subseteq \bigcup_{r<s} V_r$, contradicting $x \in C$. As $C$ and $X \setminus U_s$ are disjoint closed sets, normality supplies an open $V_s$ with $C \subseteq V_s \subseteq \overline{V_s} \subseteq U_s$, which restores the two conditions at $s$. To see that the $V_s$ cover $X$, let $x \in X$; by point finiteness the set of indices $r$ with $x \in U_r$ is finite and nonempty, so it has a largest element $s$, and $x \in B_s$ because no index beyond $s$ carries $x$; the second condition at $s$ then gives $x \in \bigcup_{t \leq s} V_t$. The well-ordering serves only to run the induction, and a Zorn's lemma formulation avoids it. $\square$

**Corollary.** A point-finite open cover of a normal space can be shrunk to a closed cover $(F_s)$ with $F_s \subseteq U_s$; and if the original cover is locally finite, so is the shrunk cover, and the same conclusion holds in every paracompact space.

**Remark.** Point finiteness is what the transfinite induction consumes: it guarantees that at each point the set of indices carrying that point is finite and nonempty, so that it has a largest element, which is what recovers the covering at the end of the argument. For a locally finite cover it is automatic, and the locally finite case is the one the partition of unity needs.

### Paracompactness and Normality: the Characterisations

**Theorem.** For a $T_1$ space $X$ the following are equivalent:

**(i)** $X$ is paracompact;

**(ii)** $X$ is regular and every open cover has a locally finite open refinement;

**(iii)** every open cover of $X$ has an open **star refinement** $\mathcal{V}$: for every $V \in \mathcal{V}$ the star
$$
\operatorname{st}(V, \mathcal{V}) = \bigcup \{\, V' \in \mathcal{V} : V' \cap V \neq \emptyset \,\}
$$
is contained in some member of the cover;

**(iv)** $X$ is normal and every open cover has a locally finite refinement.

**Proof sketch.** (i) $\Rightarrow$ (iv) is Dieudonné's theorem together with the definition. (iv) $\Rightarrow$ (iii): given an open cover $\mathcal{U}$, refine it by a locally finite open cover, shrink it by the shrinking lemma to a closed cover $(F_s)$, and let $\mathcal{V}$ be a locally finite open cover with $V_s \supseteq F_s$ and $\overline{V_s} \subseteq U_s$; then the star of $V_s$ with respect to $\mathcal{V}$ lies in $U_s$, by local finiteness. (iii) $\Rightarrow$ (ii): a star refinement of an open cover is in particular a refinement, and regularity follows from the star condition applied to a cover by a point and its complement. Spaces satisfying (iii) are called **fully normal**, and the equivalence with paracompactness for $T_1$ spaces is Stone's theorem. $\square$

## Paracompactness and Metrisability

### Metrisable Spaces are Paracompact

**Theorem (Stone).** Every metrisable space is paracompact. Indeed, every open cover of a metrisable space has a σ-discrete open refinement.

**Proof sketch.** Let $d$ be a metric and $\mathcal{U}$ an open cover. For a nonempty subset $A \subseteq X$ and $\epsilon > 0$ write $U_\epsilon(A) = \{x : d(x, A) < \epsilon\}$. Choose, for each $n \in \mathbb{N}$, a maximal $2^{-n}$-separated subset $S_n$ of $X$, so that the balls $B(x, 2^{-n})$ with $x \in S_n$ cover $X$ and the balls $B(x, 2^{-n-1})$ are pairwise disjoint. For fixed $n$ and $U \in \mathcal{U}$, let
$$
\mathcal{A}_{n,U} = \{\, B(x, 2^{-n}) : x \in S_n,\ x \notin U \,\},
$$
and use the separability of the covers by $S_n$ to assign each such ball to a cover member containing it in a locally finite fashion; the resulting family, taken over all $n$ and all $U$, is a σ-discrete refinement of $\mathcal{U}$. The key point is that the balls of a fixed scale are disjoint, so a point meets at most one member from each $S_n$, which gives σ-discreteness and hence local finiteness. $\square$

### The Smirnov Metrisation Theorem

**Theorem (Smirnov).** A $T_1$ space $X$ is metrisable if and only if it is paracompact and locally metrisable.

Here **locally metrisable** means that every point has a metrisable neighbourhood.

**Proof sketch.** If $X$ is metrisable, then every subspace is metrisable, so $X$ is locally metrisable, and paracompactness is Stone's theorem. Conversely, by local metrisability and paracompactness choose a locally finite open cover $(U_s)_{s \in S}$ with every $U_s$ metrisable — refine a cover of $X$ by metrisable neighbourhoods, then refine the result to a locally finite open cover. Each $U_s$ is metrisable, so by the necessary direction of the Nagata–Smirnov theorem it has a σ-locally finite base $\mathcal{B}_s$; write $\mathcal{B}_s = \bigcup_n \mathcal{B}_{s,n}$ with each $\mathcal{B}_{s,n}$ locally finite in $U_s$. The union $\mathcal{B} = \bigcup_n \bigcup_s \mathcal{B}_{s,n}$ is a base of $X$: for $x$ and an open neighbourhood $W$ of $x$, one of the $U_s$ contains $x$, and a member of $\mathcal{B}_s$ lies between $x$ and $W \cap U_s$. It is σ-locally finite: for fixed $n$, the family $\bigcup_s \mathcal{B}_{s,n}$ is locally finite at $x$, because $x$ lies in finitely many $U_s$ and in each of those a neighbourhood meets finitely many members of $\mathcal{B}_{s,n}$. Thus $X$ is regular with a σ-locally finite base, and the Nagata–Smirnov theorem of the previous article makes it metrisable. This is the argument of Smirnov, in the form in which it reduces to Nagata–Smirnov. $\square$

**Corollary.** A paracompact space with a σ-locally finite base is metrisable, since σ-local finiteness of the base supplies local metrisability. This is the Nagata–Smirnov theorem of the previous article, recovered here as a corollary of Smirnov's theorem.

**Example (the long line).** Let $L$ be the ordered set $\omega_1 \times [0,1)$ with the lexicographic order and the order topology, the **long line**. Every point has a neighbourhood homeomorphic to an open interval of $\mathbb{R}$, so $L$ is locally metrisable; it is not metrisable, because every countable subset of $L$ is bounded above, so $L$ is countably compact, a countably compact metric space is compact, and $L$ is not compact since the initial segments cover it with no finite subcover. By Smirnov's theorem $L$ is not paracompact, which can be checked directly: the cover by the initial segments $\{x : x < \alpha\}$ for $\alpha$ a countable ordinal has no locally finite refinement. The long line therefore shows that local metrisability alone is strictly weaker than metrisability.

**Example (the Sorgenfrey line).** The Sorgenfrey line $\mathbb{R}_S$ of the preceding article is Lindelöf, hence paracompact by the Corollary to Dieudonné's theorem, and it is not metrisable. By Smirnov's theorem it is therefore not locally metrisable, and this is the classical example of a paracompact space failing local metrisability. Together the two examples show that the two hypotheses of Smirnov's theorem are independent.

**Example (ordinal spaces).** The space $[0, \omega_1)$ of countable ordinals with the order topology is first countable, locally compact, locally metrisable and countably compact, and it is not compact; a countably compact paracompact space is compact, so $[0,\omega_1)$ is not paracompact. It is the second standard example of a locally metrisable non-paracompact space, and its one-point compactification $[0,\omega_1]$ is compact and therefore paracompact.

**Example (the Sorgenfrey plane).** The square $\mathbb{R}_S \times \mathbb{R}_S$ is not normal, by the preceding article, so it is not paracompact, since a paracompact Hausdorff space is normal. It is therefore an example of a product of two paracompact spaces that is not paracompact, and it shows that paracompactness is not finitely productive.

**Example (products with compact spaces).** If $X$ is paracompact and $K$ is compact, then $X \times K$ is paracompact. The proof is the tube lemma: given an open cover of $X \times K$, compactness of $K$ supplies for each $x \in X$ a neighbourhood $W_x$ such that $W_x \times K$ is covered by finitely many members of the cover, and a locally finite refinement of the cover $(W_x)$ of $X$ produces a locally finite refinement of the product cover. Paracompactness is thus preserved by compact factors but not by arbitrary factors, as the Sorgenfrey plane shows.

## Partitions of Unity

### Definitions

**Definition.** Let $X$ be a topological space and let $\mathcal{U} = (U_s)_{s \in S}$ be an open cover. A family $(\varphi_s)_{s \in S}$ of continuous functions $\varphi_s : X \to [0,1]$ is a **partition of unity subordinate to** $\mathcal{U}$ if

**(P1)** the family of supports $\operatorname{supp} \varphi_s = \overline{\{x : \varphi_s(x) \neq 0\}}$ is locally finite;

**(P2)** $\operatorname{supp} \varphi_s \subseteq U_s$ for every $s$;

**(P3)** $\sum_s \varphi_s(x) = 1$ for every $x \in X$.

The sum in (P3) is a finite sum at each point by (P1), and it is a continuous function of $x$ by the proposition on locally finite families above. A **locally finite partition of unity** is one in which the supports form a locally finite family, and a **σ-locally finite partition** is a countable union of locally finite ones; a σ-locally finite partition subordinate to a cover $\mathcal{U}$ can be refined to a locally finite one by passing to a locally finite refinement of $\mathcal{U}$ first.

**Lemma.** Let $(\varphi_s)_{s \in S}$ be a partition of unity on $X$ subordinate to the open cover $\mathcal{U}$. Then the family of open sets $W_s = \varphi_s^{-1}(0,1]$ is a locally finite open refinement of $\mathcal{U}$.

**Proof.** Each $W_s$ is open as the preimage of an open set under a continuous map, and $W_s \subseteq \operatorname{supp}\varphi_s \subseteq U_s$. The family is locally finite because $\operatorname{supp} \varphi_s$ is and $W_s \subseteq \operatorname{supp} \varphi_s$. It covers $X$, since at each point the sum of the $\varphi_s$ is $1$, so some $\varphi_s$ is positive. $\square$

### Existence

**Theorem.** A Hausdorff space $X$ is paracompact if and only if every open cover of $X$ admits a partition of unity subordinate to it.

**Proof.** Suppose $\mathcal{U}$ is an open cover of the paracompact Hausdorff space $X$. Refine it to a locally finite open cover $\mathcal{W} = (W_t)_{t \in T}$, and choose $s(t)$ with $W_t \subseteq U_{s(t)}$. By the shrinking lemma applied to the normal space $X$ — paracompact Hausdorff is normal by Dieudonné's theorem — the cover $\mathcal{W}$ can be shrunk to a locally finite open cover $\mathcal{V} = (V_t)$ with $\overline{V_t} \subseteq W_t$, and then to a closed cover $(F_t)$ with $F_t \subseteq V_t$. For each $t$, Urysohn's lemma applied to the disjoint closed sets $F_t$ and $X \setminus V_t$ in the normal space $X$ produces a continuous $\psi_t : X \to [0,1]$ with $\psi_t = 1$ on $F_t$ and $\psi_t = 0$ outside $V_t$, so that $\operatorname{supp}\psi_t \subseteq \overline{V_t} \subseteq W_t \subseteq U_{s(t)}$. The family $(\psi_t)$ is locally finite, since each support lies in the corresponding member of the locally finite cover $\mathcal{W}$; and at every point some $\psi_t$ is positive, because the $F_t$ cover $X$. Hence
$$
\psi = \sum_t \psi_t
$$
is a continuous strictly positive function. Define $\varphi_t = \psi_t / \psi$; the family $(\varphi_t)$ is a locally finite partition of unity with $\operatorname{supp}\varphi_t \subseteq U_{s(t)}$. To obtain a partition indexed by $S$ and subordinate to $\mathcal{U}$, put $\varphi_s = \sum_{t : s(t) = s} \varphi_t$, a locally finite sum. Conversely, if every open cover admits a subordinate partition of unity, the lemma produces a locally finite open refinement of the cover, so $X$ is paracompact. $\square$

**Corollary.** In a paracompact Hausdorff space every open cover has a locally finite partition of unity subordinate to it, and the family of supports of such a partition is a locally finite closed refinement of the cover.

**Example.** On $\mathbb{R}$ the cover by the intervals $(n-1, n+1)$ for $n \in \mathbb{Z}$ has the subordinate partition of unity with hat functions: let $\varphi_n$ be the continuous piecewise linear function equal to $1$ at $n$, to $0$ outside $(n-1, n+1)$, and linear on the two intervening intervals; the supports are the closed intervals $[n-1, n+1]$, a locally finite family, and the sum is identically $1$ — the double overlap makes the sum at $x \in (n, n+1)$ equal to $\varphi_n(x) + \varphi_{n+1}(x) = (n+1-x) + (x-n) = 1$. The example is the standard picture of a partition of unity, and the same construction with a countable family of bumps gives a partition of unity on $\mathbb{R}^m$ subordinate to any locally finite cover by balls.

### Gluing with Partitions of Unity

**Theorem (gluing lemma).** Let $\mathcal{U} = (U_s)$ be an open cover of a paracompact Hausdorff space $X$ and let $f_s : U_s \to \mathbb{R}$ be continuous. If the functions agree on the overlaps, that is $f_s = f_t$ on $U_s \cap U_t$ for all $s, t$, then there is a unique continuous $f : X \to \mathbb{R}$ with $f|_{U_s} = f_s$.

**Proof.** Uniqueness is clear, since the $U_s$ cover. For existence, let $(\varphi_s)$ be a partition of unity subordinate to the cover and define the $s$-th term $g_s$ on $X$ by $g_s(x) = \varphi_s(x) f_s(x)$ for $x \in U_s$ and $g_s(x) = 0$ otherwise. Each $g_s$ is continuous: at a point outside $\operatorname{supp}\varphi_s$ the function $\varphi_s$ vanishes identically on a neighbourhood, and at a point of $U_s$ the function $g_s$ is a product of continuous functions, the factor $f_s$ being bounded near the point and the factor $\varphi_s$ tending to $0$ where $\varphi_s$ does. Since $\operatorname{supp}\varphi_s \subseteq U_s$, the value $f_s(x)$ is defined wherever $g_s(x) \neq 0$, so the definition is consistent. Put
$$
f(x) = \sum_s g_s(x) = \sum_s \varphi_s(x) \, f_s(x).
$$
The sum is finite at each point and locally finite as a family, so $f$ is continuous, and on $U_s$ the value is $\sum_t \varphi_t(x) f_t(x) = f_s(x)$, because the terms with $\varphi_t(x) \neq 0$ have $f_t(x) = f_s(x)$ by the agreement on overlaps and the weights sum to $1$. $\square$

**Corollary (local-to-global for functions).** A continuous real-valued function defined on a neighbourhood of each point of a paracompact Hausdorff space, with agreement on overlaps, extends to the whole space. The statement is the reason partitions of unity are the standard gluing device: the data are local, the assembled function is global, and no compatibility beyond agreement on overlaps is needed.

**Remark.** The construction of the gluing lemma uses the *values* $f_s(x)$ and the weights $\varphi_s(x)$, and therefore needs the target to carry an algebraic structure in which the convex combination $\sum_s \varphi_s(x) f_s(x)$ makes sense; for $\mathbb{R}$ this is the field structure, and the vector-valued case needs the topological vector spaces of this Part, which are constructed later, where the finite convex combinations are available. For targets that are not linear — a symmetric power of a bundle, a homogeneous space, a manifold — the partition of unity does not glue maps but glues the *local data* that define them, such as a metric, a connection or a trivialisation, and each of those constructions has its own compatibility condition. This is the mechanism by which the existence of Riemannian metrics, of connections on a principal bundle and of splittings of short exact sequences of vector bundles is proved; the constructions belong there, and they use the theorem above as their covering input.

**Theorem (Urysohn's lemma via partitions of unity).** Let $X$ be paracompact Hausdorff and let $A, B$ be disjoint closed sets. Then there is a continuous $f : X \to [0,1]$ with $f = 0$ on $A$ and $f = 1$ on $B$.

**Proof.** The cover $\{X \setminus A, X \setminus B\}$ has a subordinate partition of unity $(\varphi_1, \varphi_2)$ with $\operatorname{supp}\varphi_1 \subseteq X \setminus A$ and $\operatorname{supp}\varphi_2 \subseteq X \setminus B$. Put $f = \varphi_1$. Then $\varphi_1 = 0$ on $A$, since it vanishes off its support, and $\varphi_2 = 0$ on $B$, so $f = 1 - \varphi_2 = 1$ on $B$. $\square$

## Refinements, Star Refinements and the Nerve

### Star Refinements and the Michael Characterisation

The star refinement of the previous section is a combinatorial condition on covers, and it can be used to characterise paracompactness without ever mentioning a locally finite family. This is the form in which the property passes to function spaces and to the theory of uniform spaces.

**Definition.** A cover $\mathcal{V}$ **star refines** a cover $\mathcal{U}$, written $\mathcal{V} \prec^* \mathcal{U}$, if for every $V \in \mathcal{V}$ the star $\operatorname{st}(V, \mathcal{V})$ is contained in some member of $\mathcal{U}$; it **barycentrically refines** $\mathcal{U}$ if the family of stars $\operatorname{st}(V, \mathcal{V})$ refines $\mathcal{U}$; and $\mathcal{V}$ refines $\mathcal{U}$ if every member of $\mathcal{V}$ lies in a member of $\mathcal{U}$.

**Theorem.** For a $T_1$ space $X$, the following are equivalent: $X$ is paracompact Hausdorff; every open cover of $X$ has an open star refinement; every open cover of $X$ has an open barycentric refinement.

**Proof sketch.** A star refinement is a barycentric refinement, and a barycentric refinement $\mathcal{V}$ of $\mathcal{U}$ can be improved to a star refinement by passing to the cover by the sets $\operatorname{st}(V, \mathcal{V})$, so the last two conditions are equivalent. A paracompact Hausdorff space has open star refinements by the shrinking argument of the characterisation theorem above. Conversely, an open star refinement of a cover is a refinement of it, and the star condition applied to the cover $\{X \setminus F, U\}$ for a closed set $F$ and an open set $U \supseteq F$ gives regularity; a barycentric refinement argument then produces a locally finite refinement, hence paracompactness. $\square$

**Remark.** The notion of a star refinement is the point at which the theory of paracompactness meets the theory of uniform spaces. In the covering formulation, a uniformity on $X$ is a family of covers closed under refinement and under star refinement, and the decisive theorem of Stone is that a Hausdorff space $X$ is paracompact if and only if its open covers form a base for a compatible uniformity — equivalently, if and only if every open cover has an open star refinement. The metric and uniform notions themselves, and the completion of a uniform space, belong to *Metric, Uniform and Complete Spaces*; the present article uses only the covering form, and the nerve construction below is what makes the covering form computable.

### The Nerve of a Cover

**Definition.** Let $\mathcal{U} = (U_s)_{s \in S}$ be a locally finite open cover of a normal space. The **nerve** of $\mathcal{U}$ is the abstract simplicial complex $N(\mathcal{U})$ whose vertices are the indices $s$ and whose simplices are the finite sets of indices with nonempty intersection. The **barycentric cover** of $\mathcal{U}$ is the cover, indexed by the simplices of the nerve, whose member over a simplex $\sigma$ is $\bigcap_{s \in \sigma} U_s$.

**Proposition.** The barycentric cover of a locally finite open cover of a normal space is an open cover refining it; and the nerve of a cover is a locally finite simplicial complex exactly when every member of the cover meets only finitely many of the other members, a condition on the cover that is stronger than local finiteness.

**Proof.** A point $x$ belongs to $\bigcap_{s \in \sigma} U_s$ for the finite set $\sigma$ of indices with $x \in U_s$, so the barycentric sets cover; each is contained in every $U_s$ with $s \in \sigma$, so the cover refines. The nerve is locally finite exactly when every vertex lies in finitely many simplices, and a vertex $s$ lies in a simplex $\sigma$ exactly when $U_s$ meets $\bigcap_{t \in \sigma \setminus \{s\}} U_t$, so local finiteness of the nerve says that $U_s$ meets only finitely many of the other members. This is stronger than the local finiteness of the cover: the cover consisting of the whole space $X$ together with a locally finite family of proper subsets is locally finite, and its nerve has a vertex lying in every simplex the family determines. $\square$

**Remark.** The nerve is the combinatorial skeleton of the cover, and the assignment of a point of $X$ to the simplex of the indices whose sets contain it is the **nerve map**. For a locally finite cover of a paracompact Hausdorff space, the nerve map is continuous when the nerve is given the weak topology and the point is sent to the barycentric coordinate vector; this is the construction behind the homotopy-theoretic classification of covers, and it belongs, where the simplicial and singular theories make it precise. The present article records only the covering statement, since the topological realization of the nerve is a construction of that category.

## Examples and Non-examples

The examples below separate the hypotheses of the theorems, and they are the standard counterexamples of the subject.

### A Table of Standard Spaces

The following table records which of the standard spaces are metrisable, paracompact, normal and locally metrisable.

| Space | Metrisable | Paracompact | Normal | Locally metrisable |
|---|---|---|---|---|
| Metric space | yes | yes | yes | yes |
| Compact Hausdorff space | not always | yes | yes | not always |
| $\beta\mathbb{N}$ | no | yes | yes | no |
| Sorgenfrey line $\mathbb{R}_S$ | no | yes | yes | no |
| Sorgenfrey plane $\mathbb{R}_S^2$ | no | no | no | no |
| Niemytzki plane | no | no | no | yes |
| Long line $L$ | no | no | yes | yes |
| $[0,\omega_1)$ | no | no | yes | yes |
| $[0,\omega_1]$ | no | yes | yes | no |

**Proposition.** The entries of the table hold as recorded.

**Proof.** Metric spaces are metrisable, paracompact by Stone's theorem and normal by the preceding article. A compact Hausdorff space is paracompact because a finite subcover is locally finite, and it is normal; it need not be metrisable, by the one-point compactification of an uncountable discrete space, and then it is not locally metrisable either. The space $\beta\mathbb{N}$ is compact Hausdorff, not metrisable and not locally metrisable, since it is not first countable at a free ultrafilter. The Sorgenfrey line is Lindelöf and regular, hence paracompact, and not metrisable; it is not locally metrisable by Smirnov's theorem. The Sorgenfrey plane is the product of two paracompact spaces and is not normal, hence not paracompact; it is not locally metrisable either, since it contains the Sorgenfrey line as a subspace and local metrisability is hereditary. The Niemytzki plane is separable, first countable and locally metrisable, and it is not normal, hence not paracompact. The long line and $[0,\omega_1)$ are locally metrisable and not paracompact, as shown above, and both are normal ordered spaces; their one-point compactifications are compact and hence paracompact. $\square$

**Example (a partition of unity on a compact space).** Every open cover of a compact Hausdorff space has a finite subcover, hence a subordinate partition of unity with finitely many members: take a finite subcover, shrink it to a closed cover $(F_i)$ inside it, choose bump functions $\psi_i$ equal to $1$ on $F_i$ and supported in the corresponding member, and normalise. This is the compact case of the existence theorem, and it is the form in which partitions of unity appear in the theory of vector bundles over compact base spaces.

**Example (a cover with no locally finite refinement).** On the long line, the cover by the initial segments $\{x : x < \alpha\}$ over the countable ordinals $\alpha$ has no locally finite refinement. The long line is countably compact, and in a countably compact space every locally finite family of nonempty sets is finite: given an infinite subfamily, choose a point in each of countably many distinct members, and a cluster point of the resulting sequence has every neighbourhood meeting infinitely many of the members, which local finiteness forbids. A locally finite refinement of the cover is therefore finite, and finitely many initial segments $\{x : x < \alpha_1\}, \ldots, \{x : x < \alpha_k\}$ do not cover the long line, their union being $\{x : x < \max_i \alpha_i\}$. This is the direct verification that the long line is not paracompact.

## Summary

A locally finite family is one whose members meet each neighbourhood finitely often, and a space is **paracompact** when every open cover has a locally finite open refinement. For a regular space this is equivalent to the existence of a locally finite refinement by arbitrary sets, of a locally finite closed refinement, or of a σ-locally finite open refinement. A paracompact Hausdorff space is normal and collectionwise normal, every metrisable space is paracompact, and every Lindelöf regular space is paracompact. The **shrinking lemma** replaces a point-finite open cover of a normal space by an open cover with the closures of the members inside the original ones, and it is the step that converts a cover into a partition of unity.

A **partition of unity** subordinate to an open cover is a locally finite family of continuous functions to $[0,1]$, each supported in a member of the cover, with sum identically $1$. A Hausdorff space is paracompact exactly when every open cover admits such a partition, and the construction uses the shrinking lemma and Urysohn's lemma of the preceding article. Partitions of unity glue local data: a family of continuous functions on the members of a cover agreeing on overlaps assembles into a global function, and the local constructions of metrics, connections and trivialisations on manifolds and bundles use the same input. The **Smirnov metrisation theorem** characterises metrisability as paracompactness together with local metrisability; the Sorgenfrey line is paracompact and not locally metrisable, the long line and $[0,\omega_1)$ are locally metrisable and not paracompact, and the two examples show the hypotheses to be independent. The Sorgenfrey plane is the standard product of paracompact spaces that is not paracompact, and the star refinement characterisation of paracompactness is the form in which the property passes to uniform spaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{U} = (U_s)_{s \in S}$ | An open cover of a space $X$ |
| Refinement | A family each of whose members lies in a member of $\mathcal{U}$ |
| point finite, locally finite, σ-locally finite, discrete | Finiteness conditions on a family of sets |
| paracompact | Every open cover has a locally finite open refinement |
| fully normal | Every open cover has an open star refinement |
| $\operatorname{st}(V, \mathcal{V})$ | Star of $V$ with respect to the cover $\mathcal{V}$ |
| $\overline{A}$, $A^\circ$ | Closure and interior |
| $(V_s)$, $(F_s)$ | Shrunk open cover and closed cover of the shrinking lemma |
| $\operatorname{supp}\varphi$ | Support $\overline{\{x : \varphi(x) \neq 0\}}$ of a function |
| $(\varphi_s)$ | Partition of unity subordinate to $\mathcal{U}$ |
| $\psi_s$, $\psi = \sum_s \psi_s$ | Bump functions and their normalising sum |
| $N(\mathcal{U})$ | Nerve of a locally finite cover; barycentric refinement |
| $\mathbb{R}_S$ | Sorgenfrey line; its square is the Sorgenfrey plane |
| $L$, $[0,\omega_1)$, $[0,\omega_1]$ | Long line and ordinal spaces |
| $\beta\mathbb{N}$ | Stone space of ultrafilters on $\mathbb{N}$ |
| $\mathcal{W}, \mathcal{V}, (F_t)$ | Locally finite open refinement, its shrinking, and the closed cover inside it |
| $d_s$, $U_s$ | Local metrics and metrisable open sets in Smirnov's theorem |





## Further Reading

- Jean Dieudonné, "Une généralisation des espaces compacts", *Journal de Mathématiques Pures et Appliquées* 23 (1944), 65–76, for the introduction of paracompactness and its relation to normality.
- A. H. Stone, "Paracompactness and Product Spaces", *Bulletin of the American Mathematical Society* 54 (1948), 977–982, for the paracompactness of metric spaces and full normality.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for the shrinking lemma, star refinements, partitions of unity and the Smirnov metrisation theorem.
- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for a first treatment of paracompactness and partitions of unity.
- Yu. M. Smirnov, "On metrization of topological spaces", *Uspekhi Matematicheskikh Nauk* 6 (1951), 366–372, for the metrisation theorem by paracompactness and local metrisability.
- Lynn A. Steen and J. Arthur Seebach, *Counterexamples in Topology* (Springer, 2nd ed. 1978), for the Sorgenfrey, Niemytzki, long line and ordinal examples.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for the uniform-space form of the star refinement condition.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry*, Volume I (Publish or Perish, 3rd ed. 1999), for the use of partitions of unity in the local-to-global constructions of differential geometry.
