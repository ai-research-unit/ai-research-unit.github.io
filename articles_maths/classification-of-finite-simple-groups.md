
# __The Classification of Finite Simple Groups__

## Introduction

A finite group is built from its simple composition factors, in the sense of the Jordan–Hölder theorem, and the factors are simple groups; the classification of the finite simple groups is therefore the classification of the atomic objects of finite group theory. The theorem states that every finite simple group belongs to one of four families: the cyclic groups of prime order, the alternating groups of degree at least five, the groups of Lie type, and the twenty-six sporadic groups. Its proof is the longest in mathematics, spread over some hundreds of research papers and ten to fifteen thousand pages, and its consequences pervade finite group theory, representation theory and combinatorics.

This article is the seventeenth of the corpus and the eighth of the group articles, below the foundational layer and *Infinite Abelian Groups*, *Solvable and Nilpotent Groups*, *Combinatorial Group Theory*, *Infinite Groups*, *Coxeter Groups*, *Braid Groups* and *Group Cohomology*. It uses the solvable and nilpotent theory, the group actions of *Group Actions and Structure*, the symmetric groups, and the cohomological machinery of *Group Cohomology* for the statements about automorphisms, Schur multipliers and extensions. The classification is stated here and its families described; the detailed construction of the groups of Lie type as abstract finite groups is not treated here, and the algebraic-group and building-theoretic background belongs to Part II. This article is otherwise self-contained in the language of finite groups.

## Simple Groups and the Statement

### Simplicity and Composition Factors

**Definition.** A group $G \neq 1$ is **simple** if its only normal subgroups are $1$ and $G$; a **composition series** of a finite group $G$ is a chain $1 = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_r = G$ with each quotient $G_i/G_{i-1}$ simple, and the quotients are the **composition factors**.

**Theorem (Jordan–Hölder).** Any two composition series of a finite group have the same length and the same multiset of composition factors up to isomorphism and order.

**Proof sketch.** Induction on $|G|$: given two series, refine both to series with isomorphic factors using the second isomorphism theorem, and apply induction to the proper normal subgroups appearing in a common refinement. $\square$

Consequently a finite group is determined, in the coarse sense of its factor multiset, by simple groups and extensions, and the classification of the simple groups is the first and indispensable step of the classification of all finite groups.

**Proposition.** A finite abelian simple group is cyclic of prime order; a finite simple group is either cyclic of prime order or nonabelian, and a nonabelian finite simple group is perfect: $G = [G,G]$, and its centre is trivial.

**Proof.** In an abelian group every subgroup is normal, so simplicity forces the group to have no proper nontrivial subgroup, which for a finite group means prime order. If $G$ is nonabelian and simple then $[G,G]$ is a proper normal subgroup unless $G = [G,G]$; the centre is a normal subgroup, so it is trivial. $\square$

### The Classification Theorem

**Theorem (classification of finite simple groups).** Every finite simple group is isomorphic to one of the following:

1. a **cyclic group** $\mathbb{Z}/p\mathbb{Z}$ of prime order $p$;
2. an **alternating group** $A_n$ of degree $n \geq 5$;
3. a **group of Lie type**, that is, a Chevalley group, a Steinberg group, a Suzuki group, a Ree group or a twisted group of type $^3D_4$, over a finite field;
4. one of the **twenty-six sporadic groups**.

**Remark.** The list is not a classification up to isomorphism in the naive sense: the groups of Lie type over finite fields form sixteen infinite families, with small members that coincide with one another and with alternating groups of low degree. The isomorphisms among the small members — $A_5 \cong \mathrm{PSL}_2(4) \cong \mathrm{PSL}_2(5)$, $A_6 \cong \mathrm{PSL}_2(9)$, $A_8 \cong \mathrm{PSL}_4(2)$ and a finite list of others — are part of the classification. The cyclic groups of prime order are simple and abelian; every other finite simple group is nonabelian.

**Theorem (Feit–Thompson; the odd order theorem).** Every finite group of odd order is solvable.

**Corollary.** Every nonabelian finite simple group has even order, and hence contains an involution. Every finite simple group is therefore one of the cyclic groups of prime order, which are of odd order for odd $p$, or a group of even order containing an involution.

**Corollary (Burnside).** A group of order $p^a q^b$ for primes $p, q$ is solvable; hence no nonabelian finite simple group has an order divisible by only two distinct primes.

**Proof sketch of the corollary.** Burnside's theorem is proved by character theory, a tool of the representation theory of finite groups developed in *Representations of Groups*, in the category *Linear Spaces over Linear Algebras* of this Part; the character-theoretic argument is deferred to that article. The full proof is the $p^aq^b$ theorem of Burnside, and the odd order theorem is much deeper; both are character-theoretic and are cited as standard. $\square$

**Corollary.** The smallest nonabelian finite simple group is $A_5$, of order $60$; there is a unique simple group of order $60$ up to isomorphism. There is no nonabelian simple group of order less than $60$.

**Proof.** $A_5$ has order $60$ and is simple, as verified below. A nonabelian simple group $G$ of order less than $60$ would have order with at least three distinct prime factors by Burnside's theorem; for every such order less than $60$ one of the Sylow theorems forces a nontrivial normal Sylow subgroup, or an element count forbids simplicity. The verification accompanying this article checks the counting for all orders less than $60$. $\square$

## The Families

### Cyclic and Alternating Groups

**Proposition.** $\mathbb{Z}/p\mathbb{Z}$ is simple for every prime $p$, and these are the only abelian finite simple groups. The alternating group $A_n$ is simple for $n \geq 5$, with $|A_n| = n!/2$.

**Proof sketch.** For $A_n$, the simplicity is proved by showing that any nontrivial normal subgroup contains a $3$-cycle: a nontrivial element of $A_n$ can be moved by conjugating with a $3$-cycle to produce a commutator, and the $3$-cycles generate $A_n$; the case $n \geq 5$ is uniform because a $3$-cycle has a fixed point. $\square$

**Example.** $A_5$ has order $60$, and its conjugacy classes have sizes $1, 15, 20, 12, 12$; it is simple, and it is the smallest nonabelian simple group. The group $A_5$ acts on five points and, through its action on the six Sylow $5$-subgroups, on six points, where the image is $\mathrm{PSL}_2(5) \cong A_5$.

### Groups of Lie Type

**Definition.** The **groups of Lie type** are the finite groups obtained from a simple linear algebraic group over a finite field — the Chevalley groups, their twisted forms (Steinberg, Suzuki, Ree, $^3D_4$) — as the groups of $\mathbb{F}_q$-points modulo their centres. The families include

$$
\mathrm{PSL}_{n}(q),\quad \mathrm{PSp}_{2n}(q),\quad \mathrm{PSU}_{n}(q),\quad \mathrm{P}\Omega_{n}(q),
$$

together with the exceptional families $G_2(q)$, $F_4(q)$, $E_6(q)$, $E_7(q)$, $E_8(q)$, the Suzuki groups $^2B_2(2^{2n+1})$, the Ree groups $^2G_2(3^{2n+1})$ and $^2F_4(2^{2n+1})$, and the Tits group $^3D_4(q)$; there are sixteen infinite families, with the small parameter values producing coincidences among them.

**Theorem.** The groups of Lie type are simple except for a finite list of small cases: $\mathrm{PSL}_2(2) \cong S_3$ and $\mathrm{PSL}_2(3) \cong A_4$ are not simple, $\mathrm{Sp}_4(2) \cong S_6$ is not simple while its derived subgroup $\mathrm{Sp}_4(2)' \cong A_6$ is, $\mathrm{PSU}_3(2)$ is solvable, and $G_2(2)$ and ${}^2G_2(3)$ are not simple while $G_2(2)' \cong \mathrm{PSU}_3(3)$ and ${}^2G_2(3)' \cong \mathrm{PSL}_2(8)$ are. The group ${}^2F_4(2)'$, the **Tits group**, is simple but is not itself a group of Lie type in the strict sense.

The definitions of these groups as matrix groups require the theory of linear groups, which belongs to the Linear Spaces slot of this Part, and the theory of forms, which belongs to Part II; both are deferred here. The companion articlewritten in this same batch, treats them as abstract finite groups with their orders and their simplicity, and the facts about those orders and that simplicity quoted in this article are the standard ones.

### Small Coincidences and the Exceptional Isomorphisms

The four families intersect in a finite and completely known list of small cases. Among the simple groups the coincidences include

$$
A_5 \cong \mathrm{PSL}_2(4) \cong \mathrm{PSL}_2(5), \qquad A_6 \cong \mathrm{PSL}_2(9), \qquad A_8 \cong \mathrm{PSL}_4(2),
$$

$$
\mathrm{PSL}_2(7) \cong \mathrm{PSL}_3(2), \qquad \mathrm{PSU}_4(2) \cong \mathrm{PSp}_4(3), \qquad G_2(2)' \cong \mathrm{PSU}_3(3), \qquad {}^2G_2(3)' \cong \mathrm{PSL}_2(8),
$$

and among the small non-simple members $A_4 \cong \mathrm{PSL}_2(3)$, $S_4 \cong \mathrm{PGL}_2(3)$ and $S_6 \cong \mathrm{Sp}_4(2)$. The list of coincidences is part of the classification: an isomorphism of abstract groups between members of different families must be registered, or the "list" of simple groups would count $A_5$ twice. The identification of $\mathrm{PSL}$, $\mathrm{PSp}$, $\mathrm{PSU}$ and $\mathrm{P}\Omega$ with the Chevalley and twisted families of the corresponding Dynkin diagrams is standard, so that each abstract simple group has exactly one name in the final list.

**Proposition.** The number of isomorphism classes of finite simple groups of order at most $N$ is finite for every $N$, and the classification determines it; the number of finite simple groups of order at most $100$ is $26$: the $25$ cyclic groups of prime order at most $100$ and $A_5$.

**Proof sketch.** A finite group of order at most $N$ has at most $N$ elements and hence only finitely many multiplication tables, so finitely many isomorphism classes; the classification identifies which of these orders are realised by simple groups. The count for $N = 100$ is the list of primes at most $100$ together with the single order $60$ realised by $A_5$. $\square$

### The Sporadic Groups

**Definition.** The **sporadic groups** are the twenty-six finite simple groups that belong to none of the three infinite families. They are:

| Family | Groups |
|---|---|
| Mathieu groups (5) | $M_{11}, M_{12}, M_{22}, M_{23}, M_{24}$ |
| Leech and Conway groups (7) | $\mathrm{Co}_1, \mathrm{Co}_2, \mathrm{Co}_3, \mathrm{McL}, \mathrm{HS}, \mathrm{Suz}, J_2$ |
| Fischer and related (3) | $\mathrm{Fi}_{22}, \mathrm{Fi}_{23}, \mathrm{Fi}_{24}$ |
| Held, Thompson, Harada–Norton (3) | $\mathrm{He}, \mathrm{Th}, \mathrm{HN}$ |
| The pariahs (6) | $J_1, J_3, J_4, \mathrm{O'N}, \mathrm{Ru}, \mathrm{Ly}$ |
| The large sporadics (2) | $\mathbb{B}$ (Baby Monster), $\mathbb{M}$ (Monster) |

The **Monster** $\mathbb{M}$ has order

$$
|\mathbb{M}| = 2^{46}\cdot 3^{20}\cdot 5^{9}\cdot 7^{6}\cdot 11^{2}\cdot 13^{3}\cdot 17\cdot 19\cdot 23\cdot 29\cdot 31\cdot 41\cdot 47\cdot 59\cdot 71,
$$

and it contains twenty of the sporadic groups as subquotients; the six **pariahs** $J_1, J_3, J_4, \mathrm{O'N}, \mathrm{Ru}, \mathrm{Ly}$ are not among them. The Baby Monster $\mathbb{B}$ is the second largest sporadic group, of order $2^{41}3^{13}5^6 7^2 11\cdot 13\cdot 17\cdot 19\cdot 23\cdot 31\cdot 47$, and it arises as the centraliser in the Monster of an involution, modulo that involution.

**Example.** The Mathieu groups are the sporadic groups with the smallest orders: $|M_{11}| = 7920$, $|M_{12}| = 95040$, $|M_{22}| = 443520$, $|M_{23}| = 10200960$, $|M_{24}| = 244823040$. The group $M_{11}$ was discovered by Mathieu in 1861 and was the first sporadic group; the verification accompanying this article recomputes the five orders from their prime factorisations.

## The Feit–Thompson Theorem and the Methods

### The Odd Order Theorem

**Theorem (Feit–Thompson, 1963).** Every finite group of odd order is solvable.

The theorem occupies an entire volume, and its immediate consequence for the classification is that every nonabelian finite simple group has even order and therefore an involution:

**Corollary.** Every nonabelian finite simple group contains an involution. Hence the classification can proceed by the **local analysis** of the centralisers of involutions: if $G$ is a nonabelian finite simple group and $t \in G$ is an involution, then $C_G(t)$ is a proper subgroup of even order, and the fusion in $G$ of the $2$-subgroups of $C_G(t)$ carries the information needed to reconstruct $G$.

**Proof sketch of the corollary.** If $G$ has odd order it is solvable, so if $G$ is simple of odd order it is cyclic of prime order; a nonabelian simple group therefore has even order and contains an involution. The local analysis then begins from $C_G(t)$. $\square$

### The Shape of the Proof

The classification is proved by a case division that begins with the centraliser $C_G(t)$ of an involution and proceeds according to the structure of the Sylow $2$-subgroup of $G$ and the "local" subgroups generated by $2$-subgroups:

- **Small $2$-rank and low rank.** The groups of $2$-rank at most $2$ (with a dihedral, semidihedral, wreathed or cyclic Sylow $2$-subgroup) are analysed by the work of Gorenstein, Walter, Alperin, Brauer, Suzuki and others, with the quasithin case completed by Aschbacher and Smith in 2004.
- **Component type and the general case.** For groups of $2$-rank at least $3$, the general theory of the "standard component" and the "signalizer functor" reduces the problem to the known simple groups; this is the bulk of the classification, due to Gorenstein, Aschbacher, Thompson, Bender, Glauberman and many others.
- **Character theory.** The Feit–Thompson theorem and many auxiliary results, including Burnside's $p^aq^b$ theorem and the theory of blocks, use the ordinary and modular character theory of finite groups.

**Theorem (second generation proof).** The classification has been reorganised into a structured proof in the series *The Classification of the Finite Simple Groups* by Gorenstein, Lyons and Solomon, whose several volumes give a complete and self-contained proof; the last missing case was the quasithin case, settled by Aschbacher and Smith.

The importance of the reorganisation is that the original proof was scattered over many papers, some of which were never fully published, and the second-generation proof is the reference for a rigorous statement of the theorem.

### The Status of the Proof

The chronology of the classification is itself part of its content. The Feit–Thompson theorem of 1963 removed the odd-order case; the classification of the groups of small $2$-rank was completed in the 1960s and 1970s by Gorenstein, Walter, Alperin, Brauer, Suzuki, Bender, Glauberman and others; the sporadic groups were discovered between 1861 and 1980, the Monster last; and Gorenstein announced the completion of the classification in 1981. The announcement rested on a case division whose "quasithin" case had a proof that was not published in full, and the gap was closed by Aschbacher and Smith in 2004, in two volumes. The second-generation proof of Gorenstein, Lyons and Solomon reorganises the argument into a structured sequence of theorems with explicit hypotheses, so that the classification no longer depends on an unpublished manuscript.

**Remark.** The theorem is the only large-scale classification in algebra in which the object list was known before the proof and the proof consists in showing that the list is complete. The proof is not merely long but *local*: each case is settled by the analysis of a single involution and its centraliser, and the global conclusion follows from the reconstruction of the group from that local data. This method — local analysis — has since been applied to the classification of other classes of groups, and it is the reason the theory of finite groups is organised around $2$-subgroups and their normalisers.

## Consequences and Groups of Small Order

### Consequences

**Theorem (automorphisms and multipliers).** For a finite simple group $S$ the outer automorphism group $\mathrm{Out}(S) = \mathrm{Aut}(S)/\mathrm{Inn}(S)$ is solvable, of derived length at most $3$ (the **Schreier conjecture**, proved by the classification); for groups of Lie type, $\mathrm{Out}(S)$ is generated by the diagonal, field and graph automorphisms, and for alternating groups it has order $2$ except for $n = 6$, where it has order $4$; for sporadic groups it has order at most $2$. The Schur multiplier $M(S) = H_2(S,\mathbb{Z})$ is known for every finite simple group.

**Proof sketch.** The automorphism group is computed group by group from the classification; the Lie-type case uses the structure of the algebraic group, and the alternating case uses the normaliser of the standard subgroup, with $A_6$ as the exceptional case. $\square$

**Theorem (applications).** The classification implies:

1. the classification of all finite groups of order less than a given bound, and the determination of which orders admit simple groups;
2. the O'Nan–Scott theorem and the classification of finite primitive and multiply transitive permutation groups;
3. the solution of the Schreier conjecture and the determination of the automorphism groups of the finite simple groups;
4. the classification of the finite groups with a given involution centraliser, which reconstructs a simple group from the local data of one of its involutions;
5. the classification of the finite subgroups of large classes of groups, reducing to the classification of the simple subgroups of the same class.

### Groups of Small Order

**Theorem.** The finite simple groups of order less than $100$ are the cyclic groups of prime order and $A_5$ of order $60$; there is a unique simple group of order $60$.

**Proposition.** The finite groups of order $p$, $p^2$, $pq$ (with $p < q$ and $p \nmid q-1$) and $p^3$ are abelian except in the last case, where the nonabelian group of order $p^3$ and exponent $p$ appears for odd $p$; the groups of order $pq$ with $p \mid q-1$ include a nonabelian group, and none of these groups is simple.

**Example.** The smallest orders of nonabelian simple groups are $60$ ($A_5$), $168$ ($\mathrm{PSL}_2(7)$), $360$ ($A_6$), $504$ ($\mathrm{PSL}_2(8)$), $660$ ($\mathrm{PSL}_2(11)$) and $1092$ ($\mathrm{PSL}_2(13)$); the sequence is irregular, and the classification of simple groups by order is one of the standard applications of the theorem.

**Theorem.** Orders $n$ for which every group of order $n$ is cyclic or for which every group of order $n$ is abelian are described by the prime factorisation of $n$; the smallest $n$ admitting a nonabelian simple group is $60$, and the smallest $n$ admitting a nonabelian group is $6$.

## Summary

A finite simple group is one with no nontrivial proper normal subgroup, and by Jordan–Hölder the finite groups are built from simple ones and extensions. The classification states that every finite simple group is cyclic of prime order, alternating of degree at least five, of Lie type, or one of the twenty-six sporadic groups; the groups of Lie type form sixteen infinite families, with a finite list of isomorphisms and solvable exceptions among the small members, and the sporadic groups include the five Mathieu groups, the Conway and Leech-related groups, the Fischer groups, the pariahs and the Monster.

The Feit–Thompson odd order theorem — every finite group of odd order is solvable — implies that every nonabelian finite simple group has even order and hence contains an involution, which makes the local analysis of involution centralisers the engine of the pro; Burnside's $p^aq^b$ theorem rules out orders with two prime factors. The original proof is scattered over many papers; the Gorenstein–Lyons–Solomon series reorganises it into a structured second-generation pro, completed with the quasithin case of Aschbacher and Smith. The smallest nonabelian simple group is $A_5$ of order $60$, and there is no nonabelian simple group of order less than $60$. The classification determines the automorphism groups (the Schreier conjecture) and the Schur multipliers of all finite simple groups, and it underlies the classification of finite permutation groups. The detailed construction of the groups of Lie type is not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_n$ | Alternating group of degree $n$, simple for $n \geq 5$ |
| $\mathbb{Z}/p\mathbb{Z}$ | Cyclic group of prime order |
| $\mathrm{PSL}_n(q)$, $\mathrm{PSp}_{2n}(q)$, $\mathrm{PSU}_n(q)$, $\mathrm{P}\Omega_n(q)$ | Classical groups of Lie type |
| $G_2(q), F_4(q), E_6(q), E_7(q), E_8(q)$ | Exceptional groups of Lie type |
| $^2B_2, ^2G_2, ^2F_4, ^3D_4$ | Twisted (Suzuki, Ree, Tits) families |
| $M_{11},M_{12},M_{22},M_{23},M_{24}$ | Mathieu groups |
| $\mathrm{Co}_1,\mathrm{Co}_2,\mathrm{Co}_3,\mathrm{McL},\mathrm{HS},\mathrm{Suz},J_2$ | Conway, McLaughlin, Higman–Sims, Suzuki, Hall–Janko groups |
| $\mathrm{Fi}_{22},\mathrm{Fi}_{23},\mathrm{Fi}_{24}$ | Fischer groups |
| $\mathrm{He},\mathrm{Th},\mathrm{HN}$ | Held, Thompson, Harada–Norton groups |
| $J_1,J_3,J_4,\mathrm{O'N},\mathrm{Ru},\mathrm{Ly}$ | Pariahs |
| $\mathbb{B}, \mathbb{M}$ | Baby Monster and Monster |
| $\mathrm{Out}(S) = \mathrm{Aut}(S)/\mathrm{Inn}(S)$ | Outer automorphism group |
| $M(S) = H_2(S,\mathbb{Z})$ | Schur multiplier |







## Further Reading

- Daniel Gorenstein, *Finite Simple Groups: An Introduction to Their Classification* (Plenum, 1982), for the statement of the classification and the structure of the proof.
- Daniel Gorenstein, Richard Lyons and Ronald Solomon, *The Classification of the Finite Simple Groups*, Mathematical Surveys and Monographs (American Mathematical Society, 1994–), for the second-generation proof.
- Walter Feit and John G. Thompson, "Solvability of groups of odd order", *Pacific Journal of Mathematics* **13** (1963), 775–1029, for the odd order theorem.
- Michael Aschbacher and Stephen D. Smith, *The Classification of Quasithin Groups*, Mathematical Surveys and Monographs **111–112** (American Mathematical Society, 2004), for the completion of the second-generation proof.
- John H. Conway, Robert T. Curtis, Simon P. Norton, Richard A. Parker and Robert A. Wilson, *Atlas of Finite Groups* (Oxford University Press, 1985), for the character tables, orders and local structure of the finite simple groups.
- Robert A. Wilson, *The Finite Simple Groups* (Springer, 2009), for a modern account of the families and their construction.
- Jean-Pierre Serre, "A course on the classification of finite simple groups", unfinished manuscript, for a structural account of the strategy of the proof.
