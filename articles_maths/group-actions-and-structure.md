
# __Group Actions and Structure__

## Introduction

A group is a set with an operation, but almost every question one asks about a group is really a question about how it *acts*. The elementary theory of *Groups* introduces actions, orbits, stabilisers, conjugacy, the class equation and the Sylow theorems; this article develops the same material as a single structural method, in which the action is the hypothesis and the structure theorem is the conclusion. The emphasis falls on the three places where an action is used to *compute*: the class equation and its corollaries for finite groups, Burnside's lemma and the counting of orbits, and the Sylow theorems, whose proofs are themselves applications of the orbit–stabiliser theorem to a well-chosen action.

The action-theoretic definitions and the notion of a transformation group are as in the companion article *Transformation Groups*, and the notation of *Groups* is kept throughout: $\operatorname{Orb}(x)$ and $\operatorname{Stab}(x)$ for the orbit and stabiliser, $C_G(x)$ for the centraliser, $Z(G)$ for the centre, $[G,G]$ for the commutator subgroup and $G^{\mathrm{ab}} = G/[G,G]$ for the abelianization, $N_G(H)$ for the normaliser. Throughout, $R$ denotes a commutative ring with identity $1 \neq 0$, and $F$, $K$ fields; when a numerical invariant such as the order of a group is used, the group is assumed finite and this is said. No physics is invoked. The combinatorial companionbeing, takes up the constructions of groups and the descriptions of them by generators and relations.

## Actions and the Orbit Decomposition

### Orbits, Stabilisers, and the Orbit–Stabiliser Theorem

An action of a group $G$ on a set $X$ is a map $G \times X \to X$, $(a, x) \mapsto a \cdot x$, with $e \cdot x = x$ and $(ab) \cdot x = a \cdot (b \cdot x)$; equivalently, a homomorphism $\rho : G \to \operatorname{Sym}(X)$. The orbit and stabiliser of $x \in X$ are

$$
\operatorname{Orb}(x) = \{a \cdot x : a \in G\}, \qquad \operatorname{Stab}(x) = \{a \in G : a \cdot x = x\}.
$$

The stabiliser is a subgroup, and the relation $x \sim y$ if and only if $y \in \operatorname{Orb}(x)$ is an equivalence relation, so the orbits partition $X$.

**Theorem (orbit–stabiliser).** For every $x \in X$ the map

$$
\Phi_x : G / \operatorname{Stab}(x) \longrightarrow \operatorname{Orb}(x), \qquad a \operatorname{Stab}(x) \longmapsto a \cdot x
$$

is a well-defined bijection. Consequently, if $G$ is finite, then

$$
|\operatorname{Orb}(x)| = [G : \operatorname{Stab}(x)] = \frac{|G|}{|\operatorname{Stab}(x)|},
$$

so the size of every orbit divides $|G|$.

**Proof.** If $b = a h$ with $h \in \operatorname{Stab}(x)$, then $b \cdot x = a \cdot (h \cdot x) = a \cdot x$, so $\Phi_x$ is well defined. It is surjective by definition of the orbit. If $a \cdot x = b \cdot x$, then $b^{-1} a \cdot x = x$, so $b^{-1} a \in \operatorname{Stab}(x)$ and hence $a \operatorname{Stab}(x) = b \operatorname{Stab}(x)$; so $\Phi_x$ is injective. When $G$ is finite, $G / \operatorname{Stab}(x)$ is a coset space of size $[G : \operatorname{Stab}(x)]$, which equals $|G| / |\operatorname{Stab}(x)|$ by *Groups*, §6. $\square$

The theorem is the workhorse of the subject. Two immediate consequences are used constantly. First, the orbit decomposition

$$
|X| = \sum_{\text{orbits } \mathcal{O}} |\mathcal{O}|
$$

expresses the size of a $G$-set as a sum of divisors of $|G|$. Second, if $G$ acts transitively on $X$, then $X$ is isomorphic to the coset $G$-set $G/H$ for $H = \operatorname{Stab}(x)$, and so the transitive $G$-sets are classified up to isomorphism by the conjugacy classes of subgroups of $G$.

**Example.** The action of $S_4$ on the six two-element subsets of $\{1,2,3,4\}$ is transitive, and the stabiliser of $\{1,2\}$ has order $4$, so $6 = 24/4$, in accordance with *Groups*, §11.

**Example.** Let $H \leq G$ and let $G$ act on $G/H$ by left translation. The action is transitive and the stabiliser of the coset $H$ is $H$ itself. The kernel of the action is the **core** $\bigcap_{a \in G} a H a^{-1}$, the largest subgroup of $H$ normal in $G$; thus $G/\operatorname{core}(H)$ embeds in $\operatorname{Sym}(G/H)$.

### The Conjugation Action and the Class Equation

The action of $G$ on itself by conjugation, $a \cdot x = a x a^{-1}$, has for orbits the **conjugacy classes**, and the stabiliser of $x$ is the **centraliser**

$$
C_G(x) = \{a \in G : a x a^{-1} = x\} = \{a \in G : a x = x a\}.
$$

The fixed points of the conjugation action are exactly the elements of the centre $Z(G)$, so an element has a singleton conjugacy class if and only if it is central. Splitting the partition of $G$ into the central elements and the classes of size greater than one gives the **class equation**: if $x_1, \ldots, x_k$ represent the conjugacy classes of size greater than $1$, then

$$
|G| = |Z(G)| + \sum_{i=1}^{k} [G : C_G(x_i)],
$$

each index being greater than $1$ and dividing $|G|$. As a special case, for $x \in G$ the conjugacy class of $x$ has $[G : C_G(x)]$ elements.

**Theorem.** Every finite group of order $p^n$, $n \geq 1$, with $p$ prime, has nontrivial centre.

**Proof.** By the class equation, $|G| = |Z(G)| + \sum_i [G : C_G(x_i)]$. Each index is a divisor of $p^n$ greater than $1$, hence divisible by $p$. Since $p$ divides $|G|$, it follows that $p$ divides $|Z(G)|$, so $|Z(G)| \geq p$. $\square$

**Corollary.** Every group of order $p^2$ is abelian, hence is either $C_{p^2}$ or $C_p \times C_p$.

**Proof.** By the theorem, $Z(G)$ has order $p$ or $p^2$. If $|Z(G)| = p$, the quotient $G/Z(G)$ has order $p$, hence is cyclic. But if $G/Z(G)$ is generated by the class of $x$, every element of $G$ has the form $x^i z$ with $z \in Z(G)$, and any two such elements commute, so $G$ is abelian and $Z(G) = G$, a contradiction. Hence $|Z(G)| = p^2$ and $G$ is abelian. A finite abelian group of order $p^2$ is $C_{p^2}$ or $C_p \times C_p$ by the structure theorem for finite abelian groups. $\square$

**Lemma.** If $G/Z(G)$ is cyclic, then $G$ is abelian.

**Proof.** Let $G/Z(G) = \langle x Z(G) \rangle$. Every element of $G$ is $x^i z$ with $z \in Z(G)$, and $(x^i z)(x^j z') = x^{i+j} z z' = x^{j} z' x^i z$ because $z, z'$ are central. $\square$

**Remark.** The lemma is used in the form "if $G/Z(G)$ is cyclic then $G = Z(G)$", since abelian means $Z(G) = G$. It is the reason the class equation forces $|Z(G)| \geq p$ rather than merely $|Z(G)| > 1$ in the $p$-group theorem.

### Cauchy's Theorem by an Action

The existence of an element of order $p$ is a consequence of the orbit decomposition applied to a cleverly chosen set.

**Theorem (Cauchy).** Let $G$ be finite and let $p$ be a prime dividing $|G|$. Then $G$ contains an element of order $p$.

**Proof.** Let

$$
X = \{(x_1, \ldots, x_p) \in G^p : x_1 x_2 \cdots x_p = e\}.
$$

Then $|X| = |G|^{p-1}$, since the last coordinate is determined by the first $p-1$; in particular $p$ divides $|X|$. The cyclic group $C_p$ acts on $X$ by cyclic permutation of the coordinates,

$$
k \cdot (x_1, \ldots, x_p) = (x_{k+1}, x_{k+2}, \ldots, x_p, x_1, \ldots, x_k),
$$

which preserves the condition $x_1 \cdots x_p = e$: if $x_1 \cdots x_p = e$ then $x_{k+1} \cdots x_p = (x_1 \cdots x_k)^{-1}$, so the product of the rotated tuple is $(x_1 \cdots x_k)^{-1}(x_1 \cdots x_k) = e$. The orbits of this action have size $1$ or $p$, the size being the index of the stabiliser in $C_p$. The elements of $X$ fixed by the whole action are those with $x_1 = \cdots = x_p = x$ and $x^p = e$; the number of such elements is congruent to $|X|$ modulo $p$, because all non-fixed orbits have size $p$. Hence the number of solutions of $x^p = e$ is divisible by $p$. One solution is $x = e$, so there are at least $p - 1 \geq 1$ further solutions, each of order $p$. $\square$

The proof is a model of the method: an action is chosen so that the fixed-point congruence of a group of prime order extracts the desired arithmetic. It reappears in the counting of orbits below.

## Burnside's Lemma and Counting

### The Fixed-Point Formula

**Theorem (Burnside's lemma).** Let a finite group $G$ act on a finite set $X$ and let $\operatorname{Fix}(a) = \{x \in X : a \cdot x = x\}$. Then the number of orbits is

$$
|\text{orbits}| = \frac{1}{|G|} \sum_{a \in G} |\operatorname{Fix}(a)|.
$$

**Proof.** Count the set $S = \{(a, x) \in G \times X : a \cdot x = x\}$ in two ways. Grouping by $a$ gives $|S| = \sum_{a \in G} |\operatorname{Fix}(a)|$. Grouping by $x$ gives $|S| = \sum_{x \in X} |\operatorname{Stab}(x)|$. Now $\operatorname{Stab}(x)$ has index $|\operatorname{Orb}(x)|$, so $|\operatorname{Stab}(x)| = |G| / |\operatorname{Orb}(x)|$. Hence

$$
\sum_{x \in X} |\operatorname{Stab}(x)| = \sum_{x \in X} \frac{|G|}{|\operatorname{Orb}(x)|} = |G| \sum_{\text{orbits } \mathcal{O}} \sum_{x \in \mathcal{O}} \frac{1}{|\mathcal{O}|} = |G| \cdot |\text{orbits}|,
$$

because each orbit contributes $|\mathcal{O}| \cdot (1/|\mathcal{O}|) = 1$. Comparing the two expressions proves the formula. $\square$

**Remark.** The result is also attributed to Cauchy and to Frobenius and is sometimes called the Cauchy–Frobenius lemma, or the lemma that is not Burnside's. It counts *orbits*, not fixed points, and is the standard tool for enumeration up to symmetry.

### Example: Colourings of a Square

Let the vertices of a square be coloured with $q$ colours, two colourings being identified when one is carried to the other by an element of the dihedral group $D_4$ of order $8$, acting on the four vertices; its realisation as the symmetry group of the square belongs to Part II. Burnside's lemma counts the orbits of colourings.

| Element of $D_4$ | Cycle structure on vertices | Number of fixed colourings |
|---|---|---|
| identity | $1^4$ | $q^4$ |
| $r, r^3$ (order $4$) | $4^1$ | $q$ |
| $r^2$ (order $2$) | $2^2$ | $q^2$ |
| $s, r^2 s$ (involutions) | $1^2 2^1$ | $q^3$ |
| $rs, r^3 s$ (involutions) | $2^2$ | $q^2$ |

A colouring is fixed by a permutation exactly when it is constant on each cycle, so the number of fixed colourings is $q^{c}$, where $c$ is the number of cycles. Summing the last column,

$$
\sum_{a \in D_4} |\operatorname{Fix}(a)| = q^4 + 2q + q^2 + 2q^3 + 2q^2 = q^4 + 2q^3 + 3q^2 + 2q,
$$

and therefore the number of colourings up to symmetry is

$$
\frac{1}{8}\left(q^4 + 2q^3 + 3q^2 + 2q\right).
$$

For $q = 2$ this is $(16 + 16 + 12 + 4)/8 = 6$, and for $q = 3$ it is $(81 + 54 + 27 + 6)/8 = 21$; both agree with the direct enumeration of the six and twenty-one classes.

### Example: The Number of Conjugacy Classes

Applying the formula to the conjugation action of a finite group $G$ on itself, the orbits are the conjugacy classes and $\operatorname{Fix}(a) = C_G(a)$. Hence the number $k(G)$ of conjugacy classes is

$$
k(G) = \frac{1}{|G|} \sum_{a \in G} |C_G(a)| = \frac{1}{|G|} \sum_{\text{classes } \mathcal{C}} |\mathcal{C}| \cdot \frac{|G|}{|\mathcal{C}|},
$$

and the last expression collapses to the number of classes, so the formula is here an identity rather than a computation. The content is the other direction: since each $|C_G(a)|$ is a divisor of $|G|$ and $|C_G(a)| \geq 1$, the formula constrains the class structure, and for small groups it computes $k(G)$ quickly from the centraliser orders alone.

**Example.** For $S_4$ the conjugacy classes have sizes $1, 3, 6, 6, 8$ and centralisers of orders $24, 8, 4, 4, 3$; weighting each centraliser order by the size of its class, $\sum_{a \in G} |C_G(a)| = 1 \cdot 24 + 3 \cdot 8 + 6 \cdot 4 + 6 \cdot 4 + 8 \cdot 3 = 24 + 24 + 24 + 24 + 24 = 120 = 5 \cdot 24$, so $k(S_4) = 5$.

### Double Cosets

For subgroups $H, K \leq G$ the **double cosets** $H a K$ are the orbits of the action of $H \times K$ on $G$ given by $(h, k) \cdot a = h a k^{-1}$. They partition $G$, and the orbit–stabiliser theorem computes the size of $H a K$ as

$$
|H a K| = \frac{|H| \, |K|}{|H \cap a K a^{-1}|}.
$$

For $H = K$ the double cosets $H a H$ are the orbits of the action of $H \times H$ on $G$ by $(h, k) \cdot a = h a k^{-1}$, and each of them is invariant under conjugation by $H$, hence a union of $H$-conjugacy classes: writing $\mathrm{cl}_H(a) = \{h a h^{-1} : h \in H\}$ for the $H$-class of $a$, one has $H a H = H \cdot \mathrm{cl}_H(a)$. The decomposition into double cosets underlies the transfer and the Mackey formula in representation theory.

## The Centre and the Commutator Subgroup

### The Centre

The **centre** of $G$ is $Z(G) = \{z \in G : z a = a z \text{ for all } a \in G\}$, an abelian normal subgroup, indeed a characteristic subgroup: every automorphism of $G$ maps $Z(G)$ to itself, because it maps the set of elements commuting with everything to itself.

The centre controls the extent to which $G$ is nonabelian: $G$ is abelian exactly when $Z(G) = G$, and the quotient $G/Z(G)$ measures the failure. The lemma of the preceding section says that this quotient is never cyclic unless it is trivial: $G/Z(G)$ cyclic implies $G$ abelian. For a finite $p$-group the centre is nontrivial and the quotients $G/Z(G)$, and iterates of them, form the upper central series of the nilpotent structure treated below.

### The Commutator Subgroup

For $a, b \in G$ the **commutator** is $[a, b] = a b a^{-1} b^{-1}$, which equals $e$ exactly when $a$ and $b$ commute. The identities

$$
[a, b]^{-1} = [b, a], \qquad [a b, c] = a [b, c] a^{-1} \cdot [a, c], \qquad [a, b c] = [a, b] \cdot b [a, c] b^{-1}
$$

are the standard commutator identities, obtained by expanding the definitions. The **commutator subgroup** $[G, G]$, also written $G'$, is the subgroup generated by all commutators. It is normal, and $G/[G,G]$ is abelian; more precisely $[G,G]$ is the smallest normal subgroup of $G$ with abelian quotient, so it is characteristic.

**Theorem (universal property of the abelianization).** Every homomorphism $\varphi : G \to A$ with $A$ abelian has $[G, G] \leq \ker \varphi$ and therefore factors uniquely as $G \to G^{\mathrm{ab}} \to A$. The group $G^{\mathrm{ab}} = G/[G,G]$ is the largest abelian quotient of $G$.

**Proof.** If $A$ is abelian, then $\varphi(aba^{-1}b^{-1}) = \varphi(a)\varphi(b)\varphi(a)^{-1}\varphi(b)^{-1} = e$, so every commutator is in the kernel, and the kernel, being a subgroup, contains $[G,G]$. The first isomorphism theorem then gives a unique homomorphism $G/[G,G] \to A$ with the stated composite. $\square$

A group with $[G,G] = G$ is **perfect**; equivalently, it has no nontrivial abelian quotient. The alternating groups $A_n$ for $n \geq 5$ and the special linear groups $SL_n(F)$ for $n \geq 3$ over a field are perfect, and examples of perfect groups are the reason the abelianization alone is not enough to reconstruct $G$ from its abelian quotients.

## Composition Series and Solvability

### Normal and Composition Series

A **subnormal series** of a group $G$ is a chain

$$
\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_n = G
$$

in which each $G_{i}$ is normal in $G_{i+1}$. Its **factors** are the quotients $G_{i}/G_{i-1}$. A **refinement** inserts further subgroups; a series is **maximal** when no further subgroup can be inserted, that is, when every factor is simple. A maximal subnormal series is a **composition series** of $G$, and its factors are the **composition factors**.

**Theorem (Schreier refinement).** Any two subnormal series of $G$ have refinements that are equivalent in the sense that their factor lists agree up to order and isomorphism.

**Theorem (Jordan–Hölder).** If $G$ has a composition series, then any two composition series have the same length and isomorphic composition factors up to order.

Both theorems are standard and are proved by the Schreier refinement theorem, itself an application of the isomorphism theorems. The length of a composition series is the **composition length** of $G$. A group is **solvable** if it has a subnormal series with abelian factors. Composition series exist for every finite group and hence for every finite group the Jordan–Hölder theorem applies.

**Example.** The symmetric group $S_4$ has the composition series $\{e\} \trianglelefteq C_2 \trianglelefteq V_4 \trianglelefteq A_4 \trianglelefteq S_4$ with factors $C_2, C_2, C_3, C_2$, so it is solvable of composition length $4$; the derived series $S_4 \trianglerighteq A_4 \trianglerighteq V_4 \trianglerighteq \{e\}$ reaches $\{e\}$ in three steps, so the derived length is $3$. The symmetric group $S_5$ has composition factors $C_2$ and $A_5$, the sole nonabelian composition factor being simple.

### Solvable Groups

The **derived series** of $G$ is defined by $G^{(0)} = G$ and $G^{(i+1)} = [G^{(i)}, G^{(i)}]$, a descending chain of characteristic subgroups. The group is solvable exactly when this series reaches $\{e\}$ in finitely many steps.

**Theorem.** For a finite group $G$ the following are equivalent.

**(a)** $G$ is solvable: it has a subnormal series with abelian factors.

**(b)** The derived series of $G$ terminates at $\{e\}$.

**(c)** $G$ has a subnormal series whose factors are cyclic of prime order.

**Proof.** (b) $\Rightarrow$ (a): the derived series is subnormal, and each factor $G^{(i)}/G^{(i+1)} = G^{(i)}/[G^{(i)},G^{(i)}]$ is abelian by construction. (a) $\Rightarrow$ (b): if $\{e\} = H_0 \trianglelefteq \cdots \trianglelefteq H_n = G$ has abelian factors, then $G^{(1)} = [G,G] \leq H_{n-1}$ because $G/H_{n-1}$ is abelian, and descending induction with the same argument gives $G^{(i)} \leq H_{n-i}$, so the derived series terminates. (a) $\Leftrightarrow$ (c): a finite subnormal series with abelian factors can be refined (by the Schreier refinement, or by inserting a composition series of each factor) to one with simple abelian factors, that is, cyclic of prime order; conversely such a series has abelian factors. $\square$

**Corollary.** Subgroups and quotient groups of solvable groups are solvable, and an extension of a solvable group by a solvable group is solvable. A simple group is solvable if and only if it is cyclic of prime order.

The last statement is why solvability is detected by the composition factors: $G$ is solvable exactly when every composition factor is cyclic of prime order. In particular a finite group is solvable if and only if it has no nonabelian simple composition factor.

### Nilpotent Groups

A **central series** of $G$ is a subnormal series in which every factor is central in the quotient, $G_i/G_{i-1} \leq Z(G/G_{i-1})$. A group with such a series is **nilpotent**. The **upper central series** is defined by $Z_0 = \{e\}$, $Z_{i+1}/Z_i = Z(G/Z_i)$, and the **lower central series** by $\gamma_1 = G$, $\gamma_{i+1} = [G, \gamma_i]$; nilpotency is equivalent to $Z_c = G$ for some $c$, equivalently to $\gamma_{c+1} = \{e\}$.

Every nilpotent group is solvable, since a central series is a subnormal series with abelian factors, and the converse fails: $S_3$ is solvable but not nilpotent. Every finite $p$-group is nilpotent, because its centre is nontrivial and the same argument applies inductively to the quotient. Nilpotent groups have the **normaliser condition**: every proper subgroup is properly contained in its normaliser, and every maximal subgroup is normal. These are the standard facts that organise the study of $p$-groups and are used in the classification of the small orders.

## The Sylow Theorems

### Statements

Let $G$ be finite with $|G| = p^k m$, where $p$ is prime and $p \nmid m$. A **Sylow $p$-subgroup** of $G$ is a subgroup of order $p^k$, the full power of $p$ dividing $|G|$.

**Theorem (Sylow I, existence).** For every prime $p$ dividing $|G|$, the group $G$ has a subgroup of order $p^k$.

**Theorem (Sylow II, conjugacy).** Any two Sylow $p$-subgroups of $G$ are conjugate, and every $p$-subgroup of $G$ is contained in a Sylow $p$-subgroup.

**Theorem (Sylow III, counting).** The number $n_p$ of Sylow $p$-subgroups satisfies $n_p \equiv 1 \pmod p$ and $n_p = [G : N_G(P)]$ for any Sylow $p$-subgroup $P$, so $n_p$ divides $m$. In particular $P \trianglelefteq G$ if and only if $n_p = 1$.

### Proof of Existence

**Lemma.** For a prime $p$, a positive integer $m$ and $k \geq 0$, the binomial coefficient $\binom{p^k m}{p^k}$ is congruent to $m$ modulo $p$.

**Proof.** In the polynomial ring $\mathbb{F}_p[X]$ the Frobenius identity $(1 + X)^p \equiv 1 + X^p$ holds, and iterating gives $(1 + X)^{p^k} \equiv 1 + X^{p^k} \pmod p$. Raising to the $m$-th power,

$$
(1 + X)^{p^k m} = \big((1 + X)^{p^k}\big)^{m} \equiv (1 + X^{p^k})^{m} \pmod p.
$$

The coefficient of $X^{p^k}$ is $\binom{p^k m}{p^k}$ on the left and $m$ on the right, whence the congruence. $\square$

**Proof of Sylow I.** Let $\Omega$ be the set of subsets of $G$ of cardinality $p^k$, on which $G$ acts by left translation, $a \cdot S = a S$. By the lemma, $|\Omega| = \binom{p^k m}{p^k} \equiv m \not\equiv 0 \pmod p$. Decompose $\Omega$ into orbits: $|\Omega|$ is a sum of orbit sizes, each of which divides $|G|$; since $p \nmid |\Omega|$, at least one orbit has size not divisible by $p$. Let $S$ be a subset in such an orbit and let $H = \operatorname{Stab}(S)$. By the orbit–stabiliser theorem $[G : H] = |\operatorname{Orb}(S)|$ is not divisible by $p$, and $|H| = |G| / [G:H] = p^k (m/[G:H])$, where $[G:H]$ divides $m$ because it is a divisor of $|G|$ coprime to $p$. If $[G:H] = m$ then $|H| = p^k$ and $H$ is the required subgroup. Otherwise $[G:H] < m$, so $|H| < |G|$ and $p^k$ divides $|H|$; by induction on $|G|$ applied to $H$, the group $H$ has a subgroup of order $p^k$, which is a subgroup of $G$. $\square$

### Proof of Conjugacy and Counting

**Proof of Sylow II.** Let $P$ be a Sylow $p$-subgroup and let $Q$ be any $p$-subgroup of $G$. Consider the action of $Q$ on the coset space $G/P$ by left translation. The number of cosets is $[G:P] = m$, not divisible by $p$. A $p$-group acting on a set has fixed points congruent to the size of the set modulo $p$: the non-fixed orbits have size divisible by $p$, since the size of an orbit is the index of a stabiliser, a nontrivial divisor of $|Q|$. Since $m \not\equiv 0 \pmod p$, there is a fixed coset $gP$, so $a\,gP = gP$ for all $a \in Q$, that is, $g^{-1} Q g \leq P$, or $Q \leq g P g^{-1}$. Taking $Q = P'$ a Sylow subgroup gives $P' \leq gPg^{-1}$; both sides have order $p^k$, so $P' = gPg^{-1}$. $\square$

**Proof of Sylow III.** Let $P$ act on the set $\operatorname{Syl}_p(G)$ of all Sylow $p$-subgroups by conjugation. An element $Q \in \operatorname{Syl}_p(G)$ is fixed exactly when $P \leq N_G(Q)$. If so, then $P$ and $Q$ are both Sylow $p$-subgroups of $N_G(Q)$ and, by Sylow II applied inside $N_G(Q)$, they are conjugate in $N_G(Q)$; but $Q \trianglelefteq N_G(Q)$, so the only conjugate of $Q$ is $Q$ and $P = Q$. Hence the only fixed point is $Q = P$, and the fixed-point congruence for the action of the $p$-group $P$ gives $n_p \equiv 1 \pmod p$. The orbit of $P$ under the conjugation action of the whole group is all of $\operatorname{Syl}_p(G)$ by Sylow II, so $n_p = [G : N_G(P)]$ by the orbit–stabiliser theorem, and this divides $|G|$; since $n_p \equiv 1 \pmod p$, it divides $m$. $\square$

### Applications

**Groups of order $pq$.** Let $p < q$ be primes. Then $n_q$ divides $p$ and $n_q \equiv 1 \pmod q$, so $n_q = 1$; there is a normal $Q \cong C_q$. Also $n_p$ divides $q$ and $n_p \equiv 1 \pmod p$, so $n_p \in \{1, q\}$. If $p \nmid q - 1$ then $n_p = 1$, both Sylow subgroups are normal, and $G \cong C_p \times C_q \cong C_{pq}$. If $p \mid q - 1$ there is, in addition to the cyclic group, exactly one nonabelian group, the semidirect product $C_q \rtimes C_p$ in which $C_p$ acts through an automorphism of $C_q$ of order $p$; the construction is given.

**Groups of order $12$.** Write $|G| = 12 = 2^2 \cdot 3$. Then $n_3 \in \{1, 4\}$ and $n_2 \in \{1, 3\}$. If $n_3 = 4$, the four Sylow $3$-subgroups meet pairwise trivially and contribute $8$ elements of order $3$; with the identity they account for $9$ elements, leaving exactly $3$ non-identity elements besides. A Sylow $2$-subgroup $P$ has order $4$, so its three non-identity elements are among those three, and therefore the elements outside the Sylow $3$-subgroups are exactly the non-identity elements of $P$. Hence $P$ is the only Sylow $2$-subgroup, $n_2 = 1$, and $P$ is normal. The conjugation action on the four Sylow $3$-subgroups is transitive, so its image in $S_4$ has order divisible by $4$ and dividing $12$, hence order $4$ or $12$; order $4$ would give a normal subgroup of order $3$ and force $n_3 = 1$, so the image has order $12$ and is the transitive group $A_4$, whence $G \cong A_4$ and $P \cong V_4$. If $n_3 = 1$ there is a normal $N \cong C_3$ and a Sylow $2$-subgroup $P$ of order $4$ acting on $N$ through a homomorphism $P \to \operatorname{Aut}(C_3) \cong C_2$. If the action is trivial, $G \cong N \times P$, giving $C_{12}$ or $C_6 \times C_2$. If the action is nontrivial, its kernel has order $2$; for $P \cong V_4$ the group is $D_6 \cong S_3 \times C_2$, and for $P \cong C_4$ it is the dicyclic group $C_3 \rtimes C_4$ with the generator acting by inversion. Analysing the possible actions therefore gives exactly five groups of order $12$:

| Group | Abelian | $n_3$ | $n_2$ | Distinguishing feature |
|---|---|---|---|---|
| $C_{12}$ | yes | $1$ | $1$ | cyclic |
| $C_6 \times C_2$ | yes | $1$ | $1$ | $C_3 \times V_4$ |
| $A_4$ | no | $4$ | $1$ | $V_4 \trianglelefteq G$, no element of order $6$ |
| $D_6$ | no | $1$ | $3$ | Sylow $2$ is $V_4$ |
| $C_3 \rtimes C_4$ | no | $1$ | $3$ | Sylow $2$ is cyclic; unique involution |

The same counting arguments, applied order by order, give the classification of the small groups tabulated: one group of order $p$ up to isomorphism, two of order $p^2$ — namely $C_{p^2}$ and $C_p \times C_p$, by the corollary above — two of order $pq$ when $p \mid q - 1$ and one when $p \nmid q - 1$, and five of order $8$. The Sylow theorems do not by themselves settle every order — they leave the possible actions of a complement on a normal subgroup to be analysed — but they reduce the classification to a finite list of extensions.

## Summary

The orbit–stabiliser theorem identifies each orbit of a $G$-set with a coset space $G/\operatorname{Stab}(x)$, so orbit sizes divide $|G|$ and transitive $G$-sets are classified by conjugacy classes of subgroups. Applied to conjugation it yields the class equation, the nontriviality of the centre of a finite $p$-group, the abelianness of groups of order $p^2$, and, applied to the action of $C_p$ on $p$-tuples with product $e$, Cauchy's theorem.

Burnside's lemma expresses the number of orbits as the average number of fixed points, $\frac{1}{|G|}\sum_a |\operatorname{Fix}(a)|$; it counts colourings up to symmetry and conjugacy classes, and its proof is a double count of the set of pairs $(a,x)$ with $a \cdot x = x$.

The centre $Z(G)$ and the commutator subgroup $[G,G]$ are characteristic subgroups; $G/Z(G)$ is never cyclic unless trivial, and $G^{\mathrm{ab}} = G/[G,G]$ is the largest abelian quotient of $G$. Composition series exist for finite groups and their factor lists are unique up to isomorphism by the Jordan–Hölder theorem. A group is solvable when it has a subnormal series with abelian factors, equivalently when its derived series reaches $\{e\}$, equivalently when all composition factors are cyclic of prime order; nilpotent groups are those with a central series, and every finite $p$-group is nilpotent.

The Sylow theorems assert that a subgroup of order $p^k$ exists when $|G| = p^k m$ with $p \nmid m$; that all such subgroups are conjugate and contain every $p$-subgroup; and that their number $n_p$ satisfies $n_p \equiv 1 \pmod p$ and $n_p = [G:N_G(P)] \mid m$, so that $n_p = 1$ exactly when the Sylow subgroup is normal. All three are proved by acting on a suitable set: subsets of size $p^k$, cosets of a Sylow subgroup, and Sylow subgroups under conjugation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Orb}(x)$, $\operatorname{Stab}(x)$ | Orbit and stabiliser of $x$ under a group action |
| $C_G(x)$ | Centraliser of $x$; stabiliser of $x$ under conjugation |
| $Z(G)$ | Centre of $G$; the fixed points of the conjugation action |
| $G^{\mathrm{ab}} = G/[G,G]$ | Abelianization; largest abelian quotient of $G$ |
| $[a, b] = a b a^{-1} b^{-1}$ | Commutator of $a$ and $b$ |
| $[G,G] = G'$ | Commutator (derived) subgroup |
| $G^{(i)}$ | Terms of the derived series, $G^{(i+1)} = [G^{(i)}, G^{(i)}]$ |
| $Z_i$, $\gamma_i$ | Upper and lower central series |
| $N_G(H)$ | Normaliser of $H$ in $G$ |
| $C_n$ | Cyclic group of order $n$; $C_p$ when $n = p$ is prime |
| $\operatorname{Fix}(a)$ | Fixed-point set of $a$ in a $G$-set |
| $k(G)$ | Number of conjugacy classes of a finite group $G$ |
| $H a K$ | Double coset of $a$ with respect to $H$ and $K$ |
| $\operatorname{Syl}_p(G)$, $n_p$ | Set and number of Sylow $p$-subgroups of $G$ |
| $V_4$ | Klein four group $C_2 \times C_2$ |



## Further Reading

- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, 4th ed. 1995), for group actions, the class equation and a detailed account of the Sylow theorems.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, 2nd ed. 1996), for composition series, solvable and nilpotent groups and the structure theory of finite groups.
- John S. Rose, *A Course on Group Theory* (Dover, 1994), for the orbit–stabiliser theorem and Burnside's lemma with applications to enumeration.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for the Sylow theorems and their applications to the classification of groups of small order.
- I. Martin Isaacs, *Finite Group Theory* (American Mathematical Society, Graduate Studies in Mathematics 92, 2008), for the Sylow theory and the structural theory of finite groups in full.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, Graduate Texts in Mathematics 42, 1977), for the counting of orbits and its representation-theoretic refinements.
