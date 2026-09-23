# __Groups categorization__

## Introduction

This article classifies groups by their structural properties. For each class we state the defining property, give concrete examples, and place the class in the hierarchy of group-theoretic structures.

The general theory is in the preceding article, *Groups*; we assume its definitions. We write $H \trianglelefteq G$ to mean that $H$ is a normal subgroup of $G$.

We classify groups by finiteness, commutativity, cyclicity, torsion, finite generation, simplicity, solvability, and nilpotency; we state the order theorems (Lagrange, Cauchy, Sylow), the classification of finite abelian groups, and the classification of finite simple groups; and we classify groups by realization as permutation, matrix, and geometric symmetry groups.

The standard examples are $C_n = \mathbb{Z}/n\mathbb{Z}$ and $\mathbb{Z}$ (cyclic groups), $V_4 = C_2 \times C_2$ (Klein four-group), $S_n$ and $A_n$ (symmetric and alternating), $D_{2n}$ (dihedral, order $2n$), $Q_8$ (quaternion group), the matrix groups $GL_n(F)$, $SL_n(F)$, $O(n)$, $SO(n)$, $U(n)$, $SU(n)$, and the quaternion groups $\mathbb{H}_1$, $\mathbb{H}^\times$, and $\mathbb{B}^\times$.

---

# Part I: The Main Classification

## 1. Classification by Properties

**(P1) Finiteness.** $|G| < \infty$. **(P2) Commutativity.** $a b = b a$ for all $a, b \in G$. **(P3) Cyclicity.** $G = \langle g \rangle$ for some $g \in G$. **(P4) Finite generation.** $G = \langle s_1, \ldots, s_k \rangle$ for finitely many elements $s_i$.

As in the companion categorization articles, "no" below means that groups of the class need not have the property, not that they never do.

| Class | Abelian | Cyclic | Torsion | Finitely generated |
|---|---|---|---|---|
| General group | no | no | no | no |
| Finite group | no | no | yes | yes |
| Torsion group | no | no | yes | no |
| Finitely generated group | no | no | no | yes |
| Abelian group | yes | no | no | no |
| Cyclic group | yes | yes | no | yes |

A cyclic group is the most restrictive class listed, a general group the least.

## 2. Finite and Infinite Groups

A group is **finite** if its underlying set is finite, with **order** $|G|$, and **infinite** otherwise.

Every finite group is finitely generated and is a torsion group, since every element order divides $|G|$ by Lagrange's theorem. Neither converse holds: $\mathbb{Z}$ is infinite and finitely generated, and $\mathbb{Q}/\mathbb{Z}$ is infinite and torsion, while $\mathbb{Q}$ under addition is infinite, torsion-free, and not finitely generated.

**Finite examples.** $C_n$, $V_4$, $S_n$, $A_n$, $D_{2n}$, $Q_8$, $GL_n(\mathbb{F}_q)$.

**Infinite examples.** $\mathbb{Z}$, $\mathbb{Z}^n$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ under addition, $\mathbb{Q}^\times$, the circle group $S^1$, $GL_n(\mathbb{R})$, $SL_n(\mathbb{Z})$, the free groups $F_n$, and $\mathbb{H}^\times$.

## 3. Abelian and Non-abelian Groups

A group $G$ is **abelian** if $a b = b a$ for all $a, b \in G$, and **non-abelian** otherwise. Equivalently,

$$
G \text{ is abelian} \iff [G, G] = \{e\},
$$

where $[G, G]$ is the commutator subgroup. Every subgroup and quotient of an abelian group is abelian, and the elements of finite order form a subgroup, the **torsion subgroup**; this fails for non-abelian groups.

**Examples.** $C_n$, $\mathbb{Z}$, $V_4$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ under addition, $\mathbb{Q}/\mathbb{Z}$, $\mathbb{Q}^\times$, $S^1$.

**Non-examples.** $S_n$ ($n \geq 3$), $A_n$ ($n \geq 4$), $D_{2n}$ ($n \geq 3$), $Q_8$, $GL_n(F)$ ($n \geq 2$), $\mathbb{H}^\times$, $F_n$ ($n \geq 2$).

The smallest non-abelian group is $S_3 \cong D_6$, of order $6$; the smallest non-abelian simple group is $A_5$, of order $60$.

## 4. Cyclic Groups

A group $G$ is **cyclic** if $G = \langle g \rangle = \{g^n : n \in \mathbb{Z}\}$ for some element $g$. Every cyclic group is isomorphic to exactly one of $\mathbb{Z}$ (infinite) or $C_n = \mathbb{Z}/n\mathbb{Z}$ for some $n \geq 1$ (with $C_1$ the trivial group).

Every cyclic group is abelian; every subgroup and quotient of a cyclic group is cyclic; for each divisor $d$ of $n$, the group $C_n$ has exactly one subgroup of order $d$; the group $C_n$ has $\varphi(n)$ generators, where $\varphi$ is Euler's totient function; and every group of prime order is cyclic. The presentations are

$$
C_n = \langle x \mid x^n = 1 \rangle, \qquad \mathbb{Z} = \langle x \mid \ \rangle.
$$

**Non-example.** $V_4$ is abelian but not cyclic, since it has no element of order $4$.

## 5. Torsion Groups

The **order** of an element $g \in G$ is the least positive $n$ with $g^n = e$, if it exists, and $g$ has infinite order otherwise. A group is a **torsion group** if every element has finite order, **torsion-free** if only the identity has finite order, and **mixed** otherwise.

Every finite group is torsion. The quotient $\mathbb{Q}/\mathbb{Z}$ is an infinite torsion group, and the **Prüfer $p$-subgroup** consists of its elements of $p$-power order. The additive groups $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$ are torsion-free, while $\mathbb{Q}^\times$ is mixed, with torsion subgroup $\{\pm 1\}$. For abelian groups, a finitely generated torsion group is finite, because a finitely generated abelian group is a direct product of cyclic groups (§11).

## 6. Finitely Generated Groups

A group $G$ is **finitely generated** if $G = \langle s_1, \ldots, s_k \rangle$ for finitely many elements. Every finite group is finitely generated, as are $\mathbb{Z}$, $\mathbb{Z}^n$, $C_n$, and the free groups $F_n$. The additive group $\mathbb{Q}$ is not: a finite set of rationals has a common denominator, so its integer combinations miss every rational with a larger denominator. The groups $\mathbb{Q}^\times$ and $\mathbb{Q}/\mathbb{Z}$ are not finitely generated either: $\mathbb{Q}/\mathbb{Z}$ is infinite torsion, and a finitely generated abelian torsion group is finite (§5), while a finitely generated subgroup of $\mathbb{Q}^\times$ involves only finitely many primes, and $\mathbb{R}$, $\mathbb{C}$ are uncountable.

---

# Part II: The Order Theorems

## 7. Lagrange's Theorem

If $G$ is finite and $H \leq G$ is a subgroup, then $|H|$ divides $|G|$, and

$$
|G| = |H| \cdot [G : H],
$$

where $[G : H]$ is the index of $H$ in $G$. Hence the order of every element divides $|G|$, so $g^{|G|} = e$ for all $g \in G$, and every group of prime order is cyclic. The converse fails: the group $A_4$ has order $12$ but no subgroup of order $6$. It holds for prime divisors, by Cauchy's theorem.

## 8. Cauchy's Theorem

If $G$ is finite and a prime $p$ divides $|G|$, then $G$ contains an element of order $p$. This is the correct converse of Lagrange's theorem for prime divisors, and a special case of the first Sylow theorem.

## 9. The Sylow Theorems

Let $G$ be finite, $p$ a prime, and $|G| = p^k m$ with $p \nmid m$. A **Sylow $p$-subgroup** of $G$ is a subgroup of order $p^k$.

**First Sylow theorem.** Sylow $p$-subgroups exist. **Second Sylow theorem.** Any two are conjugate in $G$. **Third Sylow theorem.** Their number $n_p$ satisfies

$$
n_p \equiv 1 \pmod p, \qquad n_p \mid m,
$$

and $n_p = [G : N_G(P)]$ for any Sylow $p$-subgroup $P$, where $N_G(P)$ is its normalizer. In particular, $P$ is normal in $G$ if and only if $n_p = 1$.

**Application.** If $|G| = pq$ with $p < q$ primes and $p \nmid (q - 1)$, the only group of order $pq$ is $C_{pq}$; if $p \mid (q - 1)$, there are exactly two, namely $C_{pq}$ and a non-abelian $C_q \rtimes C_p$. Thus the groups of order $6$ are $C_6$ and $S_3$, and the only group of order $15$ is $C_{15}$.

## 10. The Class Equation and Small Orders

Let $G$ be finite, with center $Z(G)$, and let $x_1, \ldots, x_m$ represent the conjugacy classes outside the center. The **class equation** is

$$
|G| = |Z(G)| + \sum_{i=1}^{m} [G : C_G(x_i)],
$$

which follows from the orbit–stabilizer theorem, $|G| = |\operatorname{Orb}(x)| \cdot |\operatorname{Stab}(x)|$. If $G$ is a nontrivial $p$-group, each term $[G : C_G(x_i)]$ is divisible by $p$, so the center is nontrivial; and a group of order $p^2$ is abelian, since otherwise $G/Z(G)$ would be cyclic of order $p$, forcing $G$ to be abelian.

The number of isomorphism classes of groups of order $n$, for $1 \leq n \leq 16$:

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Number of groups | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 5 | 2 | 2 | 1 | 5 | 1 | 2 | 1 | 14 |

For a prime $p$ there is one group of order $p$, namely $C_p$; two of order $p^2$, namely $C_{p^2}$ and $C_p \times C_p$; and five of order $p^3$, three abelian and two non-abelian (for $p = 2$, $D_8$ and $Q_8$). There is no simple formula for the number of groups of order $n$.

## 11. Classification of Finite Abelian Groups

Every finite abelian group is a direct product of cyclic groups, uniquely in each of two forms: the **invariant factors**

$$
G \cong C_{n_1} \times \cdots \times C_{n_k}, \qquad n_1 \mid n_2 \mid \cdots \mid n_k, \quad n_i > 1,
$$

or the **elementary divisors**, a direct product of cyclic groups of prime-power order, unique up to the order of the factors. Equivalently, every finite abelian group is the direct product of its Sylow subgroups, and every abelian $p$-group is a direct product of cyclic $p$-groups. For example $C_6 \cong C_2 \times C_3$ is cyclic, whereas $V_4 = C_2 \times C_2$ is not.

More generally, every finitely generated abelian group is isomorphic to $G \cong \mathbb{Z}^r \times T$, where $r \geq 0$ is the **rank** and $T$ is a finite abelian group, the torsion subgroup; the decomposition is unique, $G$ is finite precisely when $r = 0$, and torsion-free precisely when $T$ is trivial.

---

# Part III: Classes Defined by Normal Subgroups

## 12. Simple Groups

A nontrivial group is **simple** if its only normal subgroups are $\{e\}$ and $G$ itself. By convention the trivial group is not simple.

In an abelian group every subgroup is normal, so a simple abelian group has no proper nontrivial subgroup, and is therefore cyclic of prime order. Hence the abelian simple groups are exactly the groups $C_p$ with $p$ prime, and every non-abelian simple group is non-solvable.

**Examples.** $C_p$ for prime $p$; $A_n$ for $n \geq 5$; the projective special linear group $PSL_n(\mathbb{F}_q)$ except for $(n, q) = (2, 2)$ and $(2, 3)$; the Mathieu group $M_{11}$ of order $7920$.

**Non-examples.** $C_n$ for composite $n$; $S_n$ ($n \geq 3$) and $D_{2n}$ ($n \geq 2$), which have normal subgroups of index $2$; $A_4$, which has a normal Klein four-subgroup; any non-abelian group with nontrivial center; and any group with a proper nontrivial abelian normal subgroup.

The smallest non-abelian simple group is $A_5$, of order $60$, which is also the smallest non-solvable group. The second smallest is $PSL_2(\mathbb{F}_7)$, of order $168$, isomorphic to $GL_3(\mathbb{F}_2)$.

## 13. Composition Series and the Jordan–Hölder Theorem

A **subnormal series** of a group $G$ is a chain $\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_n = G$ in which each $G_{i-1}$ is normal in $G_i$. It is a **composition series** if every factor $G_i/G_{i-1}$ is simple.

Every finite group has a composition series, and by the **Jordan–Hölder theorem** any two composition series have the same composition factors up to isomorphism and order. A finite group is solvable if and only if all of its composition factors are cyclic of prime order. For example, $S_4$ has the composition series $\{e\} \trianglelefteq \langle (1\,2)(3\,4) \rangle \trianglelefteq V_4 \trianglelefteq A_4 \trianglelefteq S_4$, with composition factors $C_2$, $C_2$, $C_3$, and $C_2$.

## 14. Solvable Groups

A group $G$ is **solvable** if it has a subnormal series whose factors are abelian, equivalently if its **derived series**

$$
G^{(0)} = G, \qquad G^{(i+1)} = [G^{(i)}, G^{(i)}]
$$

reaches the trivial group. Every abelian group is solvable; every subgroup, quotient, and extension of solvable groups is solvable; and every group of order less than $60$ is solvable.

**Burnside's theorem.** Every finite group of order $p^a q^b$, with $p$ and $q$ primes, is solvable.

**Feit–Thompson theorem.** Every finite group of odd order is solvable.

**Non-examples.** $A_n$ and $S_n$ for $n \geq 5$; the groups $GL_n(\mathbb{R})$ and $GL_n(\mathbb{C})$ for $n \geq 2$, which contain a non-solvable free subgroup; and every non-abelian simple group.

## 15. Nilpotent Groups and p-Groups

The **lower central series** of $G$ is $\gamma_1(G) = G$, $\gamma_{i+1}(G) = [G, \gamma_i(G)]$; the group is **nilpotent** if $\gamma_{n+1}(G) = \{e\}$ for some $n$, equivalently if the **upper central series**, defined by $Z_0 = \{e\}$ and $Z_{i+1}/Z_i = Z(G/Z_i)$, reaches $G$.

Every nilpotent group is solvable, because the derived series is contained in the lower central series: $G^{(i)} \leq \gamma_{i+1}(G)$ for all $i$. A group is abelian if and only if its commutator subgroup is trivial, so every abelian group is nilpotent of class at most $1$. Subgroups, quotients, and direct products of nilpotent groups are nilpotent, and a nontrivial nilpotent group has a nontrivial center. A finite group is nilpotent if and only if each of its Sylow subgroups is normal, equivalently if and only if it is the direct product of its Sylow subgroups.

**Examples.** Every abelian group; every finite $p$-group; $Q_8$ and $D_8$; the upper unitriangular matrices over a field. **Non-examples.** $S_3$ is solvable but not nilpotent, its center being trivial; more generally $D_{2n}$ is nilpotent if and only if $n$ is a power of $2$. An extension of a nilpotent group by a nilpotent group need not be nilpotent, as $S_3$ (an extension of $C_3$ by $C_2$) shows.

A **$p$-group** is a finite group of order $p^k$. Every nontrivial $p$-group has a nontrivial center, by the class equation (§10), so every $p$-group is nilpotent, hence solvable. A group of order $p$ is cyclic; one of order $p^2$ is abelian, isomorphic to $C_{p^2}$ or $C_p \times C_p$; one of order $p^3$ is either abelian or one of two non-abelian groups. Large $p$-groups have no simple classification. The **Prüfer $p$-group**, the infinite torsion group of elements of $\mathbb{Q}/\mathbb{Z}$ of $p$-power order, is not a $p$-group in this finite sense.

---

# Part IV: Concrete Families

## 16. Permutation Groups and Cayley's Theorem

A **permutation group** is a subgroup of the symmetric group $S_X$ of all bijections of a set $X$; for $X = \{1, \ldots, n\}$ this is the symmetric group $S_n$.

**Cayley's theorem.** Every group $G$ embeds in the symmetric group on its own underlying set; in particular, every group of order $n$ embeds in $S_n$. The proof is the faithful action of $G$ on itself by left multiplication; examples include $S_n$, $A_n$, $C_n$ acting by rotations, $V_4$ acting on four points, and $D_{2n}$ acting on a regular $n$-gon.

## 17. Symmetric and Alternating Groups

The **symmetric group** $S_n$ is the group of all permutations of $n$ letters, of order $n!$. The **alternating group** $A_n$ is the subgroup of even permutations; it is normal of index $2$ for $n \geq 2$, so $|A_n| = n!/2$.

The groups $S_1$ and $S_2$ are cyclic and $S_3$ is the smallest non-abelian group; $S_n$ is non-abelian with trivial center for $n \geq 3$, solvable for $n \leq 4$ and non-solvable for $n \geq 5$. The group $A_n$ is non-abelian with trivial center for $n \geq 4$, and simple for $n \geq 5$, while $A_4$ is not simple, having a normal Klein four-subgroup. Finally, for $n \geq 2$, $S_n$ is a semidirect product

$$
S_n \cong A_n \rtimes C_2,
$$

where $C_2$ is generated by any transposition.

## 18. Dihedral Groups

For $n \geq 3$, the **dihedral group** $D_{2n}$ is the symmetry group of the regular $n$-gon. It has order $2n$ and consists of $n$ rotations, forming a cyclic subgroup $C_n$, and $n$ reflections, so

$$
D_{2n} \cong C_n \rtimes C_2, \qquad D_{2n} = \langle r, s \mid r^n = s^2 = 1, \ s r s = r^{-1} \rangle.
$$

The rotation subgroup is normal of index $2$, so $D_{2n}$ is never simple for $n \geq 3$, and $D_{2n}$ is non-abelian for $n \geq 3$. The smallest examples are $D_6 \cong S_3$ and $D_8$. The group $D_{2n}$ is nilpotent if and only if $n$ is a power of $2$, so $D_8$ is nilpotent while $D_6$ is not.

## 19. The Klein Four-Group and the Quaternion Group

The **Klein four-group** $V_4 = C_2 \times C_2 = \{e, a, b, ab\}$, with $a^2 = b^2 = (ab)^2 = e$, has order $4$, every non-identity element of order $2$, and is the smallest non-cyclic group. It is abelian, hence nilpotent and solvable, and it is not simple; it is the normal subgroup of $A_4$ that prevents $A_4$ from being simple.

The **quaternion group** $Q_8 = \{1, -1, i, -i, j, -j, k, -k\}$ has order $8$ and center $\{1, -1\}$, so it is non-abelian. It is a $2$-group, hence nilpotent and solvable, and every subgroup of $Q_8$ is normal. Unlike $D_8$, it is not a semidirect product of two proper nontrivial subgroups. It has the presentation

$$
Q_8 = \langle x, y \mid x^4 = 1, \ x^2 = y^2, \ y x y^{-1} = x^{-1} \rangle.
$$

The five groups of order $8$ are $C_8$, $C_4 \times C_2$, $C_2^3$, $D_8$, and $Q_8$.

## 20. Matrix Groups

A **matrix group** (or **linear group**) is a subgroup of $GL_n(F)$ for some field $F$ and some $n$, where

$$
GL_n(F) = \{A \in M_n(F) : \det A \neq 0\}, \qquad
SL_n(F) = \{A \in GL_n(F) : \det A = 1\} \trianglelefteq GL_n(F).
$$

Every finite group is a matrix group: by Cayley's theorem it embeds in $S_n$, and $S_n$ embeds in $GL_n(F)$ as permutation matrices. Over the finite field $\mathbb{F}_q$,

$$
|GL_n(\mathbb{F}_q)| = \prod_{i=0}^{n-1} (q^n - q^i), \qquad |SL_n(\mathbb{F}_q)| = \frac{|GL_n(\mathbb{F}_q)|}{q - 1}.
$$

With respect to the standard inner products, $O(n) = \{A : A^T A = I\}$ and $U(n) = \{A : A^* A = I\}$ are the isometry groups, with determinant-one subgroups $SO(n)$ and $SU(n)$. In particular,

$$
SO(2) \cong S^1 = U(1), \qquad SU(2) \cong \mathbb{H}_1, \qquad SO(3) \cong SU(2)/\{\pm 1\}.
$$

The center of $GL_n(F)$ consists of the scalar matrices; the quotient is $PGL_n(F)$, in which the image of $SL_n(F)$ is the projective special linear group $PSL_n(F)$, the source of the finite simple groups of Lie type (§23). Matrix groups form a proper subclass of all groups.

**The series' family.** The nonzero quaternions satisfy $\mathbb{H}^\times \cong \mathbb{R}_{>0} \times \mathbb{H}_1$, and since $\mathbb{B} \cong M_2(\mathbb{C})$ with the biquaternion norm corresponding to the determinant, the biquaternion units satisfy $\mathbb{B}^\times \cong GL_2(\mathbb{C})$, while the norm-one biquaternions form a group isomorphic to $SL_2(\mathbb{C})$.

## 21. Geometric Groups

The dihedral group $D_{2n}$ is the symmetry group of the regular $n$-gon, and the rotation groups of the Platonic solids are the tetrahedral, octahedral, and icosahedral groups, isomorphic to $A_4$, $S_4$, and $A_5$. The cyclic groups $C_n$, the dihedral groups $D_{2n}$, and these three are exactly the finite subgroups of the rotation group $SO(3)$. The circle group $S^1 = U(1) = SO(2)$ is an infinite abelian compact Lie group, and $SO(n)$, $SU(n)$ are the classical compact Lie groups, treated in the companion article *Lie Groups*.

---

# Part V: The Finite Simple Groups

## 22. The Classification

The **classification of finite simple groups** states that every finite simple group belongs to one of the following four families:

1. the cyclic groups $C_p$ of prime order, which are the abelian simple groups;
2. the alternating groups $A_n$ for $n \geq 5$;
3. the groups of Lie type, infinite families of matrix groups over finite fields;
4. the $26$ sporadic groups, which belong to no infinite family.

Every finite simple group is isomorphic to exactly one group in this list, up to the standard coincidences among the small groups.

## 23. The Groups of Lie Type

The **groups of Lie type** are the finite simple groups obtained from the classical matrix groups over finite fields and from the exceptional families. The simplest are the projective special linear groups

$$
PSL_n(\mathbb{F}_q) = SL_n(\mathbb{F}_q)/Z,
$$

where $Z$ is the center (the scalar matrices in $SL_n(\mathbb{F}_q)$). The group $PSL_n(\mathbb{F}_q)$ is simple except for $(n, q) = (2, 2)$ and $(2, 3)$, where it is $S_3$ and $A_4$ respectively. The other classical families are the projective special unitary, symplectic, and orthogonal groups; beyond these lies a finite list of exceptional families of Lie types $G_2$, $F_4$, $E_6$, $E_7$, $E_8$, together with the twisted groups of Lie type (the Steinberg, Suzuki, and Ree groups). The smallest are $PSL_2(\mathbb{F}_5) \cong A_5$, of order $60$, and $PSL_2(\mathbb{F}_7) \cong GL_3(\mathbb{F}_2)$, of order $168$.

Some alternating groups coincide with groups of Lie type:

$$
A_5 \cong PSL_2(\mathbb{F}_4) \cong PSL_2(\mathbb{F}_5), \qquad
A_6 \cong PSL_2(\mathbb{F}_9), \qquad
A_8 \cong PSL_4(\mathbb{F}_2) \cong GL_4(\mathbb{F}_2).
$$

## 24. Sporadic Groups

The **sporadic groups** are the $26$ finite simple groups belonging to none of the infinite families. The first discovered were the five **Mathieu groups** $M_{11}, M_{12}, M_{22}, M_{23}, M_{24}$, the smallest being $M_{11}$, of order $7920$. The largest is the **Monster group** $\mathbb{M}$, whose order is

$$
2^{46} \cdot 3^{20} \cdot 5^9 \cdot 7^6 \cdot 11^2 \cdot 13^3 \cdot 17 \cdot 19 \cdot 23 \cdot 29 \cdot 31 \cdot 41 \cdot 47 \cdot 59 \cdot 71,
$$

approximately $8.08 \times 10^{53}$. Other well-known sporadic groups include the Conway groups, the Fischer groups, the Baby Monster, and the Harada–Norton group.

## 25. Order Constraints on Simple Groups

The order of a finite simple group is strongly constrained. Every finite group of odd order is solvable (Feit–Thompson), so every non-abelian finite simple group has even order. Every group of order $p^a q^b$ is solvable (Burnside), so the order of a non-abelian finite simple group is divisible by at least three distinct primes. It is in fact divisible by $4$, and the smallest non-abelian finite simple group is $A_5$, of order $60 = 2^2 \cdot 3 \cdot 5$.

---

# Part VI: Hierarchy and Summary

## 26. The Main Hierarchy

The main classes are related by the chain of strict inclusions

$$
\text{Cyclic} \subset \text{Abelian} \subset \text{Nilpotent} \subset \text{Solvable} \subset \text{All groups}.
$$

In addition, every finite $p$-group is nilpotent, every finite group of order $p^a q^b$ is solvable, and every finite group of odd order is solvable. The simple groups form a separate axis rather than a step in the chain: an abelian simple group is cyclic of prime order, while a non-abelian simple group lies outside the solvable class. A finite group is solvable exactly when all of its composition factors are cyclic of prime order.

- Every **cyclic group** is **abelian**.
- Every **abelian group** is **nilpotent**.
- Every **nilpotent group** is **solvable**.
- Every **finite $p$-group** is **nilpotent**.
- Every **non-abelian simple group** is **not solvable**.

## 27. Examples Separating the Classes

- $C_n$ is cyclic; $V_4$ is abelian but not cyclic.
- $V_4$ is abelian; $Q_8$ and $D_8$ are nilpotent but not abelian.
- $Q_8$ and $D_8$ are nilpotent; $S_3$, $A_4$, and $S_4$ are solvable but not nilpotent.
- $A_5$ is simple; $A_4$ and $S_5$ are not simple.
- $\mathbb{Z}$ is infinite cyclic; $\mathbb{Q}$ is infinite abelian, not cyclic, and not finitely generated.

## 28. Standard Examples

| Group | Order | Abelian | Cyclic | Simple | Solvable | Nilpotent |
|---|---|---|---|---|---|---|
| $C_n$ | $n$ | yes | yes | iff $n$ prime | yes | yes |
| $\mathbb{Z}$ | $\infty$ | yes | yes | no | yes | yes |
| $V_4$ | $4$ | yes | no | no | yes | yes |
| $S_3 \cong D_6$ | $6$ | no | no | no | yes | no |
| $Q_8$ | $8$ | no | no | no | yes | yes |
| $D_8$ | $8$ | no | no | no | yes | yes |
| $A_4$ | $12$ | no | no | no | yes | no |
| $S_4$ | $24$ | no | no | no | yes | no |
| $A_5$ | $60$ | no | no | yes | no | no |
| $S_5$ | $120$ | no | no | no | no | no |
| $GL_n(\mathbb{R})$, $n \geq 2$ | $\infty$ | no | no | no | no | no |
| $\mathbb{H}_1 \cong SU(2)$ | $\infty$ | no | no | no | no | no |
| $F_n$, $n \geq 2$ | $\infty$ | no | no | no | no | no |

**Reading the table.** The group $C_n$ is simple exactly when $n$ is prime ($C_1$ is trivial, not simple by convention). The infinite groups in the last three rows are non-abelian, not simple, and not solvable.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, 4th ed. 1995).
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, 2nd ed. 1996).
- John S. Rose, *A Course on Group Theory* (Cambridge University Press, 1978).
- Michael Aschbacher, *Finite Group Theory* (Cambridge University Press, 2nd ed. 2000).
- Daniel Gorenstein, *Finite Groups* (Harper & Row, 1968).
- Robert A. Wilson, *The Finite Simple Groups* (Springer, 2009).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
