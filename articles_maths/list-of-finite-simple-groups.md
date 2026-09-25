# __List of Finite Simple Groups__

## Introduction

This article lists the finite simple groups, the atomic objects of finite group theory, following the four families of the classification: the cyclic groups of prime order, the alternating groups of degree at least five, the groups of Lie type in their sixteen infinite families, and the twenty-six sporadic groups. For each family the list records the order, and for the sporadic groups it records the six subfamilies into which they fall.

Every entry points to the article that introduces the group and states the order recorded there. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being a small member of a family that fails simplicity, with the failure named and the article that records it.

## The Statement of the Classification

A finite group is built from its simple composition factors by Jordan–Hölder, so the classification of the simple groups classifies the building blocks. The theorem states that every finite simple group is a cyclic group of prime order, an alternating group $A_n$ with $n \geq 5$, a group of Lie type, or one of the twenty-six sporadic groups. The smallest nonabelian finite simple group is $A_5$, of order $60$, and there is no nonabelian simple group of order less than $60$.

| Object | The property it has | Introduced in |
|---|---|---|
| Finite simple group | a group with no nontrivial proper normal subgroup | *The Classification of Finite Simple Groups* |
| The classification theorem | the four-family statement, with the sixteen Lie families and the twenty-six sporadics | *The Classification of Finite Simple Groups* |
| Feit–Thompson theorem | every finite group of odd order is solvable, so every nonabelian finite simple group has even order | *The Classification of Finite Simple Groups* |
| Burnside $p^aq^b$ theorem | a group of order $p^a q^b$ is solvable, so no nonabelian simple group has an order with only two prime factors | *The Classification of Finite Simple Groups* |
| Jordan–Hölder theorem | the composition factors of a finite group are unique up to isomorphism and order | *The Classification of Finite Simple Groups* |
| Non-example: $A_4$ | a group of order $12$ that fails simplicity: its Klein four-subgroup is normal | *Finite Groups and Symmetry* |
| Non-example: a group of order $pq$, $p<q$, $p\nmid q-1$ | a group of two-prime order that fails simplicity: it is cyclic | *Groups*, §13 |

## The Cyclic Groups of Prime Order

The cyclic groups $\mathbb{Z}/p\mathbb{Z}$ of prime order form the abelian family of the classification, and they are the only abelian finite simple groups. For odd $p$ the order is odd, so these are exactly the odd-order members of the list.

| Group | The property it has | Introduced in |
|---|---|---|
| $\mathbb{Z}/p\mathbb{Z}$, $p$ prime | the cyclic group of prime order $p$; simple and abelian | *The Classification of Finite Simple Groups* |
| $C_p$ | the same group in the multiplicative notation of the finite-groups article | *Finite Groups and Symmetry* |
| Non-example: $\mathbb{Z}/n\mathbb{Z}$, $n$ composite | a cyclic group that fails simplicity: it has a proper nontrivial subgroup | *Groups*, §1 |

## The Alternating Groups

The alternating group $A_n$ is the subgroup of even permutations of $S_n$, of order $n!/2$, and it is simple for every $n \geq 5$. The low-degree cases are the exceptions: $A_4$ of order $12$ has a normal Klein four-subgroup, and $A_3 \cong C_3$ and $A_2 = 1$ fall outside the defining range.

| Group | The property it has | Introduced in |
|---|---|---|
| $A_n$, $n \geq 5$ | order $n!/2$; simple, nonabelian, perfect and with trivial centre | *The Classification of Finite Simple Groups* |
| $A_5$ | order $60$; the smallest nonabelian simple group, with conjugacy classes of sizes $1, 15, 20, 12, 12$ | *The Classification of Finite Simple Groups* |
| $A_6$ | order $360$; simple, and exceptional in having an outer automorphism group of order $4$ | *The Classification of Finite Simple Groups* |
| $A_8$ | order $20160$; simple, and isomorphic to $\mathrm{PSL}_4(2)$ | *The Classification of Finite Simple Groups* |
| $A_n$ | the alternating group inside the symmetric group $S_n$, normal of index $2$ | *Groups* |
| Non-example: $A_4$ | order $12$; fails simplicity | *Finite Groups and Symmetry* |

## The Groups of Lie Type

The groups of Lie type are the finite groups obtained from a simple linear algebraic group over a finite field, as its $\mathbb{F}_q$-points modulo the centre. There are sixteen infinite families: the classical families $\mathrm{PSL}_n(q)$, $\mathrm{PSp}_{2n}(q)$, $\mathrm{PSU}_n(q)$ and $\mathrm{P}\Omega_n(q)$, the exceptional families $G_2(q)$, $F_4(q)$, $E_6(q)$, $E_7(q)$ and $E_8(q)$, the twisted families ${}^2B_2$, ${}^2G_2$, ${}^2F_4$ and ${}^3D_4$, with the Tits group ${}^2F_4(2)'$ simple but not itself of Lie type in the strict sense.

| Family | The property it has | Introduced in |
|---|---|---|
| $\mathrm{PSL}_n(q)$ | order $q^{n(n-1)/2}\prod_{i=2}^{n}(q^i-1)/\gcd(n,q-1)$; the projective special linear family | *Finite Simple Groups of Lie Type* |
| $\mathrm{PSp}_{2n}(q)$ | order $q^{n^2}\prod_{i=1}^{n}(q^{2i}-1)/\gcd(2,q-1)$; the projective symplectic family | *Finite Simple Groups of Lie Type* |
| $\mathrm{PSU}_n(q)$ | the projective special unitary family, of twisted type ${}^2A_{n-1}$ | *Finite Simple Groups of Lie Type* |
| $\mathrm{P}\Omega_n(q)$ | the simple orthogonal families $B_n$, $D_n$ and ${}^2D_n$ | *Finite Simple Groups of Lie Type* |
| $G_2(q)$ | order $q^6(q^6-1)(q^2-1)$; the exceptional family of rank $2$ | *Finite Simple Groups of Lie Type* |
| $F_4(q)$ | order $q^{24}(q^{12}-1)(q^8-1)(q^6-1)(q^2-1)$ | *Finite Simple Groups of Lie Type* |
| $E_6(q)$, $E_7(q)$, $E_8(q)$ | the exceptional families of ranks $6$, $7$ and $8$, with orders $q^{36}$, $q^{63}$ and $q^{120}$ times the standard factors | *Finite Simple Groups of Lie Type* |
| ${}^2B_2(2^{2n+1})$ | the Suzuki family, of order $q^2(q^2+1)(q-1)$ | *Finite Simple Groups of Lie Type* |
| ${}^2G_2(3^{2n+1})$ | the Ree family of type $G_2$, of order $q^3(q^3+1)(q-1)$ | *Finite Simple Groups of Lie Type* |
| ${}^2F_4(2^{2n+1})$ | the Ree family of type $F_4$, of order $q^{12}(q^6+1)(q^4-1)(q^3+1)(q-1)$ | *Finite Simple Groups of Lie Type* |
| ${}^3D_4(q)$ | the Tits twisted family, of order $q^{12}(q^8+q^4+1)(q^6-1)(q^2-1)$ | *Finite Simple Groups of Lie Type* |
| Tits group ${}^2F_4(2)'$ | simple of order $17971200$; not a group of Lie type in the strict sense | *The Classification of Finite Simple Groups* |
| Non-example: $\mathrm{PSL}_2(2) \cong S_3$ | a small member of the family that fails simplicity | *The Classification of Finite Simple Groups* |
| Non-example: $\mathrm{PSL}_2(3) \cong A_4$ | a small member that fails simplicity | *The Classification of Finite Simple Groups* |
| Non-example: $\mathrm{PSU}_3(2)$ | a small member that is solvable | *The Classification of Finite Simple Groups* |
| Non-example: $G_2(2)$, ${}^2G_2(3)$, ${}^2F_4(2)$ | small members that fail simplicity, their derived subgroups being simple | *The Classification of Finite Simple Groups* |
| Non-example: $\mathrm{Sp}_4(2) \cong S_6$ | a small member that fails simplicity, with $\mathrm{Sp}_4(2)' \cong A_6$ | *The Classification of Finite Simple Groups* |

## The Twenty-Six Sporadic Groups

The sporadic groups are the twenty-six finite simple groups outside the three infinite families. They fall into six subfamilies: the five Mathieu groups, the seven Conway and Leech-related groups, the three Fischer groups, the three Held, Thompson and Harada–Norton groups, the six pariahs, and the two large sporadics, the Baby Monster and the Monster.

| Group | The property it has | Introduced in |
|---|---|---|
| $M_{11}$ | Mathieu group, order $7920$; the first sporadic group, discovered in 1861 | *The Classification of Finite Simple Groups* |
| $M_{12}$ | Mathieu group, order $95040$ | *The Classification of Finite Simple Groups* |
| $M_{22}$ | Mathieu group, order $443520$ | *The Classification of Finite Simple Groups* |
| $M_{23}$ | Mathieu group, order $10200960$ | *The Classification of Finite Simple Groups* |
| $M_{24}$ | Mathieu group, order $244823040$ | *The Classification of Finite Simple Groups* |
| $\mathrm{Co}_1$, $\mathrm{Co}_2$, $\mathrm{Co}_3$ | Conway groups, of orders $2^{21}3^95^47^2\cdot11\cdot13\cdot23$, $2^{18}3^65^3\cdot7\cdot11\cdot23$ and $2^{10}3^75^3\cdot7\cdot11\cdot23$ | *The Classification of Finite Simple Groups* |
| $\mathrm{McL}$ | McLaughlin group, order $2^73^65^3\cdot7\cdot11$ | *The Classification of Finite Simple Groups* |
| $\mathrm{HS}$ | Higman–Sims group, order $2^93^25^3\cdot7\cdot11$ | *The Classification of Finite Simple Groups* |
| $\mathrm{Suz}$ | Suzuki group, order $2^{13}3^75^2\cdot7\cdot11\cdot13$ | *The Classification of Finite Simple Groups* |
| $J_2$ | the Hall–Janko group, order $2^73^35^2\cdot7$ | *The Classification of Finite Simple Groups* |
| $\mathrm{Fi}_{22}$, $\mathrm{Fi}_{23}$, $\mathrm{Fi}_{24}'$ | Fischer groups, of orders $2^{17}3^95^2\cdot7\cdot11\cdot13$, $2^{18}3^{13}5^2\cdot7\cdot11\cdot13\cdot17\cdot23$ and $2^{21}3^{16}5^2 7^3\cdot11\cdot13\cdot17\cdot23\cdot29$ | *The Classification of Finite Simple Groups* |
| $\mathrm{He}$ | Held group, order $2^{10}3^35^27^3\cdot17$ | *The Classification of Finite Simple Groups* |
| $\mathrm{Th}$ | Thompson group, order $2^{15}3^{10}5^3 7^2\cdot13\cdot19\cdot31$ | *The Classification of Finite Simple Groups* |
| $\mathrm{HN}$ | Harada–Norton group, order $2^{14}3^65^6\cdot7\cdot11\cdot19$ | *The Classification of Finite Simple Groups* |
| $J_1$ | Janko group, order $175560$; the first pariah | *The Classification of Finite Simple Groups* |
| $J_3$ | Janko group, order $2^73^5\cdot5\cdot17\cdot19$ | *The Classification of Finite Simple Groups* |
| $J_4$ | Janko group, order $2^{21}3^3\cdot5\cdot7\cdot11^3\cdot23\cdot29\cdot31\cdot37\cdot43$ | *The Classification of Finite Simple Groups* |
| $\mathrm{O'N}$ | O'Nan group, order $2^93^4\cdot5\cdot7^3\cdot11\cdot19\cdot31$ | *The Classification of Finite Simple Groups* |
| $\mathrm{Ru}$ | Rudvalis group, order $2^{14}3^3 5^3\cdot7\cdot13\cdot29$ | *The Classification of Finite Simple Groups* |
| $\mathrm{Ly}$ | Lyons group, order $2^83^75^6\cdot7\cdot11\cdot31\cdot37\cdot67$ | *The Classification of Finite Simple Groups* |
| $\mathbb{B}$ | the Baby Monster, order $2^{41}3^{13}5^6 7^2\cdot11\cdot13\cdot17\cdot19\cdot23\cdot31\cdot47$; the centraliser of an involution in the Monster, modulo that involution | *The Classification of Finite Simple Groups* |
| $\mathbb{M}$ | the Monster, order $2^{46}3^{20}5^97^6 11^2 13^3\cdot17\cdot19\cdot23\cdot29\cdot31\cdot41\cdot47\cdot59\cdot71$; the largest sporadic group, containing twenty of the sporadics as subquotients | *The Classification of Finite Simple Groups* |
| The six pariahs | $J_1, J_3, J_4, \mathrm{O'N}, \mathrm{Ru}, \mathrm{Ly}$, the sporadic groups that are not subquotients of the Monster | *The Classification of Finite Simple Groups* |

## Small Orders and Exceptional Isomorphisms

The four families intersect in a finite list of small cases, which the classification registers so that no simple group is counted twice. The coincidences among the simple groups include $A_5 \cong \mathrm{PSL}_2(4) \cong \mathrm{PSL}_2(5)$, $A_6 \cong \mathrm{PSL}_2(9)$, $A_8 \cong \mathrm{PSL}_4(2)$, $\mathrm{PSL}_2(7) \cong \mathrm{PSL}_3(2)$, $\mathrm{PSU}_4(2) \cong \mathrm{PSp}_4(3)$, $G_2(2)' \cong \mathrm{PSU}_3(3)$ and ${}^2G_2(3)' \cong \mathrm{PSL}_2(8)$. The smallest orders of nonabelian simple groups are $60$, $168$, $360$, $504$, $660$ and $1092$.

| Object | The property it has | Introduced in |
|---|---|---|
| $A_5 \cong \mathrm{PSL}_2(4) \cong \mathrm{PSL}_2(5)$ | the exceptional isomorphism of the smallest simple group | *The Classification of Finite Simple Groups* |
| $A_6 \cong \mathrm{PSL}_2(9)$ | an exception among the low-degree alternating groups | *The Classification of Finite Simple Groups* |
| $A_8 \cong \mathrm{PSL}_4(2)$ | an isomorphism between an alternating and a classical family member | *The Classification of Finite Simple Groups* |
| $\mathrm{PSL}_2(7) \cong \mathrm{PSL}_3(2)$ | order $168$; the second smallest nonabelian simple group | *The Classification of Finite Simple Groups* |
| $\mathrm{PSU}_4(2) \cong \mathrm{PSp}_4(3)$ | an isomorphism between two twisted and symplectic members | *The Classification of Finite Simple Groups* |
| Non-example: $S_6 \cong \mathrm{Sp}_4(2)$ | a symmetric group appearing as a non-simple member of a Lie family | *The Classification of Finite Simple Groups* |

## Summary

The list gathers the finite simple groups. The abelian family is the cyclic groups of prime order; the alternating family is the groups $A_n$ for $n \geq 5$, of order $n!/2$, beginning with $A_5$ of order $60$; the Lie family consists of the sixteen infinite families $\mathrm{PSL}_n(q)$, $\mathrm{PSp}_{2n}(q)$, $\mathrm{PSU}_n(q)$, $\mathrm{P}\Omega_n(q)$, $G_2(q)$, $F_4(q)$, $E_6(q)$, $E_7(q)$, $E_8(q)$, ${}^2B_2$, ${}^2G_2$, ${}^2F_4$ and ${}^3D_4$, together with the Tits group; and the sporadic family is the twenty-six groups, in the six subfamilies of Mathieu, Conway and Leech, Fischer, Held–Thompson–Harada–Norton, pariah and large sporadic. The non-examples — $A_4$, the cyclic group of composite order, $\mathrm{PSL}_2(2)$, $\mathrm{PSL}_2(3)$, $\mathrm{PSU}_3(2)$, $G_2(2)$, ${}^2G_2(3)$, ${}^2F_4(2)$, $\mathrm{Sp}_4(2)$ and the groups of two-prime order — are the small or degenerate members that fail simplicity.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $A_n$ | alternating group of degree $n$ |
| $\mathbb{Z}/p\mathbb{Z}$, $C_p$ | cyclic group of prime order |
| $\mathrm{PSL}_n(q)$, $\mathrm{PSp}_{2n}(q)$, $\mathrm{PSU}_n(q)$, $\mathrm{P}\Omega_n(q)$ | classical groups of Lie type |
| $G_2(q)$, $F_4(q)$, $E_6(q)$, $E_7(q)$, $E_8(q)$ | exceptional groups of Lie type |
| ${}^2B_2$, ${}^2G_2$, ${}^2F_4$, ${}^3D_4$ | twisted families |
| $M_{11},\dots,M_{24}$ | Mathieu groups |
| $\mathrm{Co}_1,\mathrm{Co}_2,\mathrm{Co}_3,\mathrm{McL},\mathrm{HS},\mathrm{Suz},J_2$ | Conway, McLaughlin, Higman–Sims, Suzuki and Hall–Janko groups |
| $\mathrm{Fi}_{22},\mathrm{Fi}_{23},\mathrm{Fi}_{24}'$ | Fischer groups |
| $\mathrm{He},\mathrm{Th},\mathrm{HN}$ | Held, Thompson and Harada–Norton groups |
| $J_1,J_3,J_4,\mathrm{O'N},\mathrm{Ru},\mathrm{Ly}$ | the six pariahs |
| $\mathbb{B}$, $\mathbb{M}$ | Baby Monster and Monster |
| $q$ | a prime power $p^f$ |
| $\mathbb{F}_q$, $\mathbb{F}_p$ | finite fields |
| $\mathbb{Z}$ | the integers |

## Further Reading

- Daniel Gorenstein, Richard Lyons and Ronald Solomon, *The Classification of the Finite Simple Groups* (American Mathematical Society, 1994–), for the statement, the four families and the second-generation proof.
- John Conway, Robert Curtis, Simon Norton, Richard Parker and Robert Wilson, *Atlas of Finite Groups* (Oxford University Press, 1985), for the orders, the subfamily grouping and the exceptional isomorphisms of the finite simple groups.
- Roger Carter, *Simple Groups of Lie Type* (Wiley, 1972), for the sixteen families of Lie type, their orders and their small degenerate members.
- Robert Wilson, *The Finite Simple Groups* (Springer, 2009), for a single-volume account of the four families with the orders tabulated.
