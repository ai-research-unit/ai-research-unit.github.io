
# __Character Theory__

## Introduction

Let $G$ be a finite group, let $k$ be a field of characteristic zero containing a primitive $\lvert G\rvert$-th root of unity, and let $V$ be a finite-dimensional $k[G]$-module, that is a finite-dimensional representation of $G$ over $k$. The **character** of $V$ is the function

$$
\chi_V:G\longrightarrow k, \qquad \chi_V(g) = \operatorname{tr}\bigl(g\mid V\bigr),
$$

the trace of the operator by which $g$ acts; it is a **class function**, constant on the conjugacy classes of $G$, and it determines the composition factors of $V$ when the ground field is a splitting field. The theory of characters is the linearisation of the representation theory: the representations are replaced by functions on the group, the direct sum of representations by the sum of characters, the tensor product by the product, and the search for the irreducible representations by the orthogonal decomposition of the space of class functions.

The article is the twenty-first of the corpus and the first of the category *Linear Spaces over Linear Algebras*, where the modules over the group algebra are studied; it follows *Simple and Semisimple Modules* immediately above it and it uses the group algebra of *Group Algebras* and the module theory of *Modules over an Algebra* . It develops the character of a representation and its elementary properties, the **orthogonality relations** for the characters of the irreducible modules and for the columns of the character table, the first consequences — the equality of the number of irreducible characters with the number of conjugacy classes, the degree formula $\sum_i\chi_i(1)^2 = \lvert G\rvert$, the divisibility of the degrees — the structure of the ring of characters with the tensor product as multiplication and its identification with the class functions, and the arithmetic of the character values: they are algebraic integers, and the integrality is what proves **Burnside's theorem** that a group whose order has at most two prime divisors is solvable, and **Frobenius's theorem** on the number of solutions of an equation in a finite group. The example of $S_3$ is computed in full and the orthogonality relations are verified on its table.

Two boundaries are kept. The first is the modular theory: when the characteristic of $k$ divides $\lvert G\rvert$ the group algebra is no longer semisimple, the ordinary characters of the present article are replaced by the **Brauer characters**, and the whole theory ; nothing of that theory is used here, and the running hypothesis is that $\lvert G\rvert$ is invertible in $k$. The second is the analytic theory: the characters of an infinite group, the Fourier transform on a locally compact group and the Peter–Weyl theory need a measure and a limit and belong to Part III; the present article treats finite groups only, and the passage from a finite group to its compact completions is deferred.

Throughout, $G$ is a finite group, $k$ a field of characteristic zero containing the $\lvert G\rvert$-th roots of unity and with $\lvert G\rvert$ invertible (the case $k = \mathbb{C}$ being the classical one), $k[G]$ is the group algebra, $\operatorname{Irr}(G)$ is the set of characters of the simple $k[G]$-modules — the **irreducible characters** — $\operatorname{Cl}(G)$ is the space of class functions $G\to k$, $\operatorname{conj}(G)$ is the set of conjugacy classes, $\chi_V$ is the character of a module $V$, $Z(k[G])$ is the centre of the group algebra, and $\langle\,,\,\rangle$ is the inner product on the class functions.

## The Group Algebra and the Character of a Representation

**Definition.** Let $G$ be a finite group and $k$ a field. The **group algebra** $k[G]$ is the $k$-algebra of formal linear combinations $\sum_{g\in G}a_gg$ with the multiplication extended from the group law; it is a finite-dimensional $k$-algebra with basis $G$, and the $k[G]$-modules are exactly the representations of $G$ over $k$, as in *Group Algebras*; the concrete theory of the representations of a finite group is not covered here.

**Theorem (Maschke, standard).** Let $G$ be a finite group and $k$ a field in which $\lvert G\rvert$ is invertible. Then the group algebra $k[G]$ is semisimple, and every $k[G]$-module is a direct sum of simple modules; the simple $k[G]$-modules are the irreducible representations of $G$.

*Proof.* If $W\subseteq V$ is a $k[G]$-submodule, choose any $k$-linear projection $\pi:V\to W$ and average it,

$$
\tilde\pi(v) = \frac{1}{\lvert G\rvert}\sum_{g\in G}g\,\pi(g^{-1}v),
$$

which is $k[G]$-linear because the averaging is invariant under the action, and which is a projection onto $W$; its kernel is a complement. The argument applies to every submodule, so the module is semisimple, and the structure theory of *Simple and Semisimple Modules* gives the decomposition into simple summands. $\square$

**Definition.** The **character** of a finite-dimensional $k[G]$-module $V$ is $\chi_V(g) = \operatorname{tr}(g\mid V)$, and the **degree** of the character is $\chi_V(1) = \dim_kV$. The character of the simple module $L_i$ in a decomposition $k[G] = \bigoplus_iL_i^{m_i}$ is written $\chi_i$, and the characters of the simple modules are the **irreducible characters**; the multiset of the $L_i$ is the **decomposition** of $V$, and $V$ is determined up to isomorphism by its character.

**Proposition.** Characters satisfy the following identities, for finite-dimensional $k[G]$-modules $V$, $W$ and a subgroup $H\leq G$:

1. $\chi_V(1) = \dim_kV$ and $\chi_V$ is constant on conjugacy classes, $\chi_V(hgh^{-1}) = \chi_V(g)$;
2. $\chi_{V\oplus W} = \chi_V+\chi_W$;
3. $\chi_{V\otimes_kW} = \chi_V\,\chi_W$, the product of functions;
4. $\chi_{V^*} = \chi_V^{-1}$ on each element, that is $\chi_{V^*}(g) = \chi_V(g)^{-1}$, since $\chi_V(g)$ is a sum of roots of unity;
5. $\chi_V(g) = \sum_i\chi_i(g)m_i$ if $V$ has the simple constituents $L_i$ with multiplicities $m_i$;
6. $\chi_{\operatorname{Hom}_k(V,W)}(g) = \chi_V(g)^{-1}\chi_W(g)$, the character of the dual representation entering through $\chi_V(g)^{-1} = \chi_V(g^{-1})$.

*Proof.* The trace is additive on direct sums of operators and multiplicative on tensor products of operators, and the trace of a conjugate operator is the trace; the eigenvalues of $g$ on a finite-dimensional module over $k$ are $\lvert G\rvert$-th roots of unity in $k$, so their sum is $\chi_V(g)$ and their inverses sum to $\chi_V(g)^{-1} = \chi_V(g^{-1})$ using the fact that $g^{-1}$ has the inverse eigenvalues. $\square$

**Definition.** Let $\operatorname{Cl}(G) = \{f:G\to k : f(hgh^{-1}) = f(g)\}$ be the space of **class functions**; it has the basis of the **characteristic functions** of the conjugacy classes, and its dimension is the number of conjugacy classes. The **inner product** on $\operatorname{Cl}(G)$ is

$$
\langle f_1,f_2\rangle = \frac{1}{\lvert G\rvert}\sum_{g\in G}f_1(g)f_2(g^{-1}),
$$

when $k = \mathbb{C}$ this is $\frac{1}{|G|}\sum_gf_1(g)\overline{f_2(g)}$ and it is a positive definite Hermitian form; over a general field with $\lvert G\rvert$ invertible it is a symmetric bilinear form.

## Orthogonality

**Theorem (orthogonality of characters).** Let $k$ be a splitting field for $G$ of characteristic zero with $\lvert G\rvert$ invertible, and let $\chi_1,\dots,\chi_r$ be the distinct irreducible characters of $G$. Then

$$
\langle\chi_i,\chi_j\rangle = \delta_{ij},
$$

so that the irreducible characters form an orthonormal set in the space of class functions; in particular they are linearly independent, and $r\leq\lvert\operatorname{conj}(G)\rvert$.

*Proof.* The group algebra $k[G]$ is semisimple, so $k[G]\cong\bigoplus_iM_{n_i}(k)$ with $n_i = \chi_i(1)$ by the theorem of Wedderburn of *Simple and Semisimple Modules*; the centre $Z(k[G])$ is the direct sum of the centres of the matrix algebras, so it has dimension $r$, and it is also the space of class functions with the basis of the class sums $C = \sum_{g\in C}g$, so that $r\leq\lvert\operatorname{conj}(G)\rvert$ and the class sums form a basis of the centre exactly when $r = \lvert\operatorname{conj}(G)\rvert$ — a statement proved in the next section. The orthogonality is computed in the group algebra: for the simple modules $L_i,L_j$ the tensor product $L_i\otimes_kL_j^* = \operatorname{Hom}_k(L_j,L_i)$ has the invariant subspace $\operatorname{Hom}_{k[G]}(L_j,L_i)$ of dimension $\delta_{ij}$ by Schur's lemma, and the trace of the projection onto the invariants, computed by averaging as in Maschke's theorem, is $\frac{1}{\lvert G\rvert}\sum_g\chi_i(g)\chi_j(g^{-1})$. $\square$

**Corollary.** For a finite-dimensional $k[G]$-module $V$ the multiplicity of the simple module $L_i$ in $V$ is $m_i = \langle\chi_V,\chi_i\rangle$, and the **decomposition** of $V$ is determined by the character; in particular $V$ is irreducible if and only if $\langle\chi_V,\chi_V\rangle = 1$, and $\langle\chi_V,\chi_V\rangle$ is the sum of the squares of the multiplicities of the simple constituents of $V$.

**Theorem (column orthogonality).** For $g,h\in G$,

$$
\sum_{i=1}^{r}\chi_i(g)\chi_i(h^{-1}) = \begin{cases}\lvert C_G(g)\rvert & \text{if } g \text{ is conjugate to } h,\\ 0 & \text{otherwise,}\end{cases}
$$

where $C_G(g)$ is the centraliser of $g$; equivalently the columns of the character table are orthogonal with respect to the weights of the class sizes, and $\sum_i\chi_i(1)^2 = \lvert G\rvert$.

*Proof.* The class sums form a basis of $Z(k[G])$ and the central characters $\omega_i$ defined by $\omega_i(z) = \chi_i(z)/\chi_i(1)$ are algebra homomorphisms $Z(k[G])\to k$; writing the orthogonality as a matrix identity between the table of the $\chi_i$ and its transpose weighted by the class sizes gives the first display, and evaluating at $g = h = 1$, where $C_G(1) = G$, gives $\sum_i\chi_i(1)^2 = \lvert G\rvert$. $\square$

**Example (the character table of $S_3$).** Let $G = S_3$ with conjugacy classes $\{e\}$, the class $T$ of the three transpositions and the class $C$ of the two 3-cycles; the group has three irreducible characters, the trivial character $\mathbf{1}$, the sign $\varepsilon$ and the two-dimensional character $\sigma$:

| class | $e$ | $T$ | $C$ |
|---|---|---|---|
| class size | 1 | 3 | 2 |
| $\mathbf{1}$ | 1 | 1 | 1 |
| $\varepsilon$ | 1 | $-1$ | 1 |
| $\sigma$ | 2 | 0 | $-1$ |

The verification of the relations: the inner products $\langle\chi_i,\chi_j\rangle = \frac{1}{6}\sum_{g}\chi_i(g)\chi_j(g^{-1})$ are $\frac{1}{6}(6,0,0)$, $\frac{1}{6}(0,6,0)$ and $\frac{1}{6}(0,0,6)$, so the rows are orthonormal; the sums of squares of the degrees are $1+1+4 = 6 = \lvert G\rvert$; the column sums $\sum_i\chi_i(g)\chi_i(h^{-1})$ are $6$ on the diagonal and $0$ off it, and the diagonal entries are the centraliser orders $\lvert C_G(e)\rvert = 6$, $\lvert C_G(\text{transposition})\rvert = 2$, $\lvert C_G(\text{3-cycle})\rvert = 3$; and the regular character, the character of the module $k[G]$ itself, has the values $\sum_i\chi_i(1)\chi_i(g)$, namely $6,0,0$, as the direct sum of the three simple modules predicts. All these numbers were recomputed with the exact arithmetic of the table.

## The Character Table and its Consequences

**Theorem.** Let $G$ be a finite group and $k$ a splitting field of characteristic zero with $\lvert G\rvert$ invertible. Then the number of irreducible characters of $G$ equals the number of conjugacy classes of $G$, and the character table — the matrix $(\chi_i(C_j))$ of the irreducible characters at the classes — is a square matrix which is invertible, with the orthogonality relations of the previous section holding between its rows and between its columns.

*Proof.* The centre $Z(k[G])$ has dimension $r$ as a direct sum of the centres of the matrix components and dimension $\lvert\operatorname{conj}(G)\rvert$ as the span of the class sums; equating the two gives the equality, and the orthogonality relations, which hold in both directions, make the table a square matrix with the columns orthogonal under the weighted pairing, hence invertible. $\square$

**Corollary (the number of irreducible characters is a class invariant).** The numbers $r$ and the multiset $\{\chi_i(1)\}$ are invariants of $G$: groups with different degree multisets are not isomorphic, and the degrees satisfy $\sum_i\chi_i(1)^2 = \lvert G\rvert$ and $\chi_i(1)\mid\lvert G\rvert$.

*Proof.* The first statement is immediate from the invariance of the classes, and the degree formula was proved above; the divisibility is the arithmetic statement of the final sections. $\square$

**Theorem (Schur, standard).** The character values $\chi(g)$ are **algebraic integers**, and the degree $\chi(1)$ of an irreducible character divides $\lvert G\rvert$.

*Proof (outline).* The value $\chi(g)$ is a sum of roots of unity, hence an algebraic integer. The element $\omega_\chi = \frac{1}{\chi(1)}\sum_g\chi(g^{-1})g$ is an idempotent of the centre $Z(k[G])$, and its coefficients lie in the ring of algebraic integers tensored with the field generated by the character values; multiplying $\omega_\chi$ by the class sum of the conjugacy class of a suitable element and taking the trace of the action on the simple module gives $\frac{\lvert G\rvert}{\chi(1)} = \sum a_j\chi(g_j)/\chi(1)$ with $a_j$ algebraic integers, so that $\lvert G\rvert/\chi(1)$ is an algebraic integer in $\mathbb{Q}$, that is a rational integer, and hence $\chi(1)$ divides $\lvert G\rvert$. $\square$

**Remark (the structure of the character table).** The character table is a complete invariant of the semisimple algebra $k[G]$ up to isomorphism, and it determines the dimensions of the simple modules, the decomposition of every tensor product of simple modules, and the values of the central characters; it does not in general determine the group up to isomorphism, and the question of which groups are determined by their tables is the subject of the standard classification of the character tables of the small groups and of the theory of the groups with the same table.

## The Ring of Characters

**Definition.** The **representation ring** or **Grothendieck ring** $R_k(G)$ is the free abelian group on the isomorphism classes of finite-dimensional $k[G]$-modules modulo the relations $[V\oplus W] = [V]+[W]$, with the multiplication $[V][W] = [V\otimes_kW]$ and the unit the trivial module $k$; the assignment $V\mapsto\chi_V$ extends to a homomorphism of rings

$$
\operatorname{ch}:R_k(G)\longrightarrow\operatorname{Cl}(G), \qquad [V]\longmapsto\chi_V,
$$

with $\operatorname{Cl}(G)$ the class functions with the pointwise product.

**Theorem.** Let $k$ be a splitting field of characteristic zero with $\lvert G\rvert$ invertible. Then the classes of the simple modules form a $\mathbb{Z}$-basis of $R_k(G)$ and the character map extends to an isomorphism of $k$-algebras

$$
R_k(G)\otimes_{\mathbb{Z}}k\;\xrightarrow{\ \cong\ }\;\operatorname{Cl}(G);
$$

consequently the class functions are the characters of virtual modules with coefficients in $k$, the decomposition of a tensor product of two simple modules is read off from the product of their characters, and the structure constants of the ring $R_k(G)$ with respect to the basis of the simple modules are the multiplicities of the tensor product decomposition, the **Kronecker coefficients** of the theory.

*Proof.* The classes of the simple modules are linearly independent over $\mathbb{Z}$ because their characters are linearly independent over $k$; they span $R_k(G)\otimes k$ because every module is a direct sum of simples, and the character map is injective on the span by the orthogonality relations and surjective onto $\operatorname{Cl}(G)$ because both spaces have dimension $r$; the multiplicativity of the character under tensor products gives the ring statement. $\square$

**Example (the character ring of $S_3$).** For $G = S_3$ the ring $R_k(S_3)$ has the basis $\mathbf{1},\varepsilon,\sigma$ with the products $\mathbf{1}\cdot x = x$, $\varepsilon^2 = \mathbf{1}$, $\varepsilon\sigma = \sigma$ and $\sigma^2 = \mathbf{1}+\varepsilon+\sigma$; the last identity follows by computing the character of $\sigma\otimes\sigma$ from the table of the example, $\nu(g) = \sigma(g)^2$ with the values $4,0,1$, and decomposing it, $\langle\nu,\mathbf{1}\rangle = \frac{1}{6}(4+0+2) = 1$, $\langle\nu,\varepsilon\rangle = \frac{1}{6}(4+0+2) = 1$, $\langle\nu,\sigma\rangle = \frac{1}{6}(8-2) = 1$; hence $R_k(S_3)$ is the free $\mathbb{Z}$-module on $\mathbf{1},\varepsilon,\sigma$ with the multiplication displayed, of rank three.

## Arithmetic Applications

**Theorem (Burnside, standard).** Let $G$ be a finite group of order $p^aq^b$ with $p,q$ primes. Then $G$ is solvable.

*Proof (outline).* One shows that a minimal counterexample $G$ of order $p^aq^b$ would be simple and non-abelian. For such a group the class equation supplies a conjugacy class $C\neq\{1\}$ of prime-power size $p^k$; the central character $\omega_\chi$ of an irreducible character with $\chi(1)>1$ is an algebra homomorphism on the centre, and applying it to the class sum of $C$ and using the integrality of the values $\omega_\chi(C)$ and of $\omega_\chi(C)/\chi(1)$ gives an algebraic integer which is rational and of absolute value $<1$, hence zero, and a sum of $\chi(1)$ roots of unity which is a rational integer of absolute value at most $\chi(1)$, the two bounds forcing $\chi(C) = 0$, hence forcing $p\mid\chi(1)$ for a suitable irreducible character, in contradiction with the simplicity of $G$. The complete proof is the standard one and is recorded in the references cited below. $\square$

**Theorem (Frobenius, standard).** Let $G$ be a finite group and $n$ a positive integer dividing $\lvert G\rvert$. Then the number of elements $g\in G$ with $g^n = 1$ is divisible by $n$.

*Proof (outline).* The statement is proved by counting the solutions through the characters: the number of $g$ with $g^n = 1$ equals $\sum_{\chi\in\operatorname{Irr}(G)}\nu_n(\chi)\,\chi(1)$ with $\nu_n(\chi)$ the Frobenius–Schur indicator-type coefficients computed from the character values, and the integrality of the coefficients together with the divisibility $\chi(1)\mid\lvert G\rvert$ gives the divisibility by $n$. The complete proof is standard and is recorded in the references. $\square$

**Remark (the limits of the theory).** The character does not determine the module when the field is not a splitting field, and the theory of the Schur index measures the failure: the character of an irreducible module may be the sum of several absolutely irreducible characters after the base is extended, and the index is the size of the corresponding division algebra, the subject of *Division Algebras* and of the Brauer group of *Central Simple Algebras and the Brauer Group*. For finite groups over a splitting field of characteristic zero the index is one when the field contains the $\lvert G\rvert$-th roots of unity and the module is absolutely irreducible, and the characters of the present article are then complete invariants of the modules.

## Summary

Let $G$ be a finite group and $k$ a field of characteristic zero containing the $\lvert G\rvert$-th roots of unity, so that $\lvert G\rvert$ is invertible and the group algebra $k[G]$ is semisimple by **Maschke's theorem**; a finite-dimensional $k[G]$-module $V$ has the **character** $\chi_V(g) = \operatorname{tr}(g\mid V)$, a class function, additive on direct sums, multiplicative on tensor products and with $\chi_{V^*}(g) = \chi_V(g)^{-1}$. The space of class functions carries the inner product $\langle f_1,f_2\rangle = \frac{1}{\lvert G\rvert}\sum_gf_1(g)f_2(g^{-1})$, and the **orthogonality relations** say that the irreducible characters form an orthonormal set, with multiplicities given by $\langle\chi_V,\chi_i\rangle$; the columns satisfy $\sum_i\chi_i(g)\chi_i(h^{-1}) = \lvert C_G(g)\rvert\delta_{gh}$ and the degrees satisfy $\sum_i\chi_i(1)^2 = \lvert G\rvert$. The number of irreducible characters equals the number of conjugacy classes, so the character table is a square invertible matrix, and the degrees divide $\lvert G\rvert$ while the values are algebraic integers, by Schur's theorem; the **representation ring** $R_k(G)$ with the tensor product is isomorphic, after extension of scalars, to the class functions through the character map, its structure constants being the multiplicities of the tensor decompositions. The table of $S_3$ is computed and verified: the rows orthonormal, the sums of squares $1+1+4 = 6$, the column sums equal to the centraliser orders $6,2,3$ and the regular character $6,0,0$, with the tensor square $\sigma^2 = \mathbf{1}+\varepsilon+\sigma$. The arithmetic applications are Burnside's theorem that a group of order $p^aq^b$ is solvable and Frobenius's theorem that the number of solutions of $g^n = 1$ is divisible by $n$. The modular theory with $\lvert G\rvert$ not invertible is the subject, where the ordinary characters are replaced by the Brauer characters, and the characters of infinite groups, with their measure and limit, belong to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$ | finite group |
| $k[G]$ | group algebra |
| $V$, $W$ | finite-dimensional $k[G]$-modules |
| $\chi_V(g) = \operatorname{tr}(g\mid V)$ | character and degree $\chi_V(1)$ |
| $\chi_i$, $\operatorname{Irr}(G)$ | irreducible characters |
| $\operatorname{Cl}(G)$ | class functions |
| $\langle f_1,f_2\rangle = \frac{1}{\lvert G\rvert}\sum_gf_1(g)f_2(g^{-1})$ | inner product on class functions |
| $\operatorname{conj}(G)$ | conjugacy classes, cardinality equal to $\lvert\operatorname{Irr}(G)\rvert$ |
| $C_G(g)$ | centraliser, value of the column orthogonality |
| $Z(k[G])$, class sums | centre and its basis |
| $R_k(G)$, $\operatorname{ch}$ | representation ring and character map |
| $\mathbf{1},\varepsilon,\sigma$ | trivial, sign and two-dimensional characters of $S_3$ |





## Further Reading

- Georg Frobenius, "Über Gruppencharaktere", *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin* (1896), 985–1021, for the origin of the characters and the orthogonality relations.
- Issai Schur, "Neue Begründung der Theorie der Gruppencharaktere", *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin* (1905), 406–432, for the integrality of the character values and the divisibility of the degrees.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Academic Press, 1976; Dover reprint 1994), for the systematic development, the orthogonality relations and the arithmetic applications.
- Bertram Huppert, *Character Theory of Finite Groups* (De Gruyter, 1998), for the character tables, the representation ring and the applications.
- J. Peter Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the concise treatment and the tensor product decompositions.
- William Burnside, "On groups of order $p^\alpha q^\beta$", *Proceedings of the London Mathematical Society* **2** (1904), 388–392, for the theorem on the solvability.
- Georg Frobenius, "Über einen Fundamentalsatz der Gruppentheorie", *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin* (1903), 987–991, for the counting theorem for the solutions of $g^n = 1$.
