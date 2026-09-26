# __Representation Theory of Symmetric Groups__

## Introduction

A representation of the symmetric group $S_n$ over a field $K$ is an action of $S_n$ on a $K$-module by $K$-linear automorphisms, equivalently a homomorphism $S_n \to \operatorname{Aut}_K(M)$, equivalently a module over the group ring $K[S_n]$ — the ring of formal $K$-linear combinations of group elements with multiplication induced by the group law. The theory is the most explicit in all of representation theory: the irreducible representations are indexed by the partitions of $n$, their dimensions are given by the hook length formula of *Symmetric Functions and Schur Functions*, their characters are computed by the Murnaghan–Nakayama rule, their construction is the tableau calculus of Alfred Young, and their combinatorics — Young diagrams, standard and semistandard tableaux, the Young lattice — is the same combinatorics that indexes the symmetric functions. In characteristic zero the theory is completely understood; in characteristic $p$ it is still the object of an extensive literature, but its structure — the blocks, the $p$-cores, the decomposition numbers — is known in its broad outlines.

This article develops the characteristic-zero theory and states the modular theory. The connection with symmetric functions is the Frobenius characteristic of *Symmetric Functions and Schur Functions*, which identifies the character ring with the ring of symmetric functions and sends the irreducible character $\chi^\lambda$ to the Schur function $s_\lambda$; the connection with the general linear group is Schur–Weyl duality. The group ring is used only as a ring acting on modules; the systematic theory of algebras — of a module carrying a product — belongs to *Linear Algebras*, and the modules and vector spaces used below are the standard ones. The symmetric-algebra side of the combinatorial theory, the Hecke algebras of type $A$ and their deformations, belongs to *Symmetric Linear Algebras*, owned by another agent of this Part, and is cited rather than developed.

Throughout, $K$ is a field of characteristic not dividing $n!$ unless a modular statement is explicitly made, so that by Maschke's theorem every representation is a direct sum of irreducibles; $S_n$ is the symmetric group, its **conjugacy classes** are indexed by cycle type, that is, by partitions $\mu$ of $n$; $\lambda$, $\mu$ denote partitions; $M^\lambda$ is a permutation module, $S^\lambda$ the corresponding Specht module, $\chi^\lambda$ its character, and $\lambda'$ the conjugate partition. The hook length formula, the Kostka numbers $K_{\lambda\mu}$, the Hall inner product and the Frobenius characteristic are those of *Symmetric Functions and Schur Functions* and are used freely.

---

## Representations, Classes and Characters

### Basic Structure

**Definition.** A **representation** of $S_n$ over $K$ is a pair $(M,\rho)$ with $M$ a $K$-module and $\rho : S_n \to \operatorname{Aut}_K(M)$ a group homomorphism; a **subrepresentation** is a submodule stable under the action, an **irreducible** representation is one with no proper nonzero subrepresentation, and a representation is **completely reducible** if it is a direct sum of irreducibles. Two representations are **isomorphic** if there is an isomorphism of modules intertwining the actions, and their **characters** are equal exactly when they are isomorphic (over a field of characteristic zero).

**Theorem (Maschke).** Let $G$ be a finite group and $K$ a field whose characteristic does not divide $\lvert G\rvert$. Then every representation of $G$ over $K$ is completely reducible.

**Proof.** Let $N \subseteq M$ be a subrepresentation and $\pi : M \to N$ any $K$-linear projection; the averaged map $\tilde\pi = \frac{1}{\lvert G\rvert}\sum_{g}\rho(g)\pi\rho(g)^{-1}$ is $G$-equivariant, has image $N$, and is a projection, so its kernel is a complementary subrepresentation. Iterating gives the decomposition. $\square$

**Lemma (Schur).** Let $M, N$ be irreducible representations over a field $K$. Then every nonzero homomorphism $M \to N$ is an isomorphism, and over an algebraically closed field every endomorphism of an irreducible $M$ is a scalar.

**Proof.** The kernel and image of an intertwining map are subrepresentations; an endomorphism of an irreducible has an eigenvalue over an algebraically closed field, and the corresponding eigenspace is a nonzero subrepresentation, hence all of $M$. $\square$

**Definition.** The **character** of a finite-dimensional representation $M$ is the function $\chi : S_n \to K$, $\chi(\sigma) = \operatorname{tr}(\rho(\sigma))$; it is constant on conjugacy classes, so it is determined by its values on the partitions $\mu$ of $n$. Characters of representations are sums of characters of irreducible constituents, and the irreducible characters are exactly those that cannot be written as such a sum.

**Theorem (the numbers).** The number of irreducible representations of $S_n$ over an algebraically closed field of characteristic zero equals the number of conjugacy classes, hence the number of partitions of $n$. The regular representation, that is, the action of $S_n$ on $K[S_n]$ by left multiplication, decomposes as

$$
K[S_n] \cong \bigoplus_{\lambda \vdash n}(S^\lambda)^{\oplus \dim S^\lambda},
$$

whence $\sum_{\lambda\vdash n}(\dim S^\lambda)^2 = n!$, and the character of the regular representation is $n!$ at the identity and $0$ elsewhere.

**Proof sketch.** The number of irreducible characters is the dimension of the centre of the group ring, which has as a basis the class sums, one for each conjugacy class; the decomposition of the regular representation into isotypic components gives the displayed multiplicity $\dim S^\lambda$, and evaluating at the identity gives $\sum_\lambda(\dim S^\lambda)^2 = n!$ together with the character values: the identity contributes $n!$, and the transformation of characters under the regular action gives $\sum_\lambda\dim(S^\lambda)\chi^\lambda(\sigma) = 0$ for $\sigma \neq 1$. $\square$

**Example.** For $n = 3$: the partitions are $(3)$, $(2,1)$, $(1,1,1)$ with hook length dimensions $1$, $2$, $1$, and $1^2+2^2+1^2 = 6 = \lvert S_3\rvert$. The three irreducibles are the trivial representation, the sign representation, and the two-dimensional **standard representation**, on which $S_3$ acts by permuting the three coordinates of the submodule $\{(a,b,c) : a+b+c = 0\}$ of $K^3$.

### The Character Table of $S_4$

**Definition.** The **character table** of $S_n$ is the matrix $\chi^\lambda_\mu = \chi^\lambda(\mu)$ of irreducible character values at the conjugacy classes, with rows indexed by partitions $\lambda$ (the irreducible characters) and columns by partitions $\mu$ (the classes).

**Theorem (orthogonality).** With $\lvert C_\mu\rvert$ the size of the class of cycle type $\mu$,

$$
\sum_{\mu\vdash n}\lvert C_\mu\rvert\,\chi^\lambda_\mu\overline{\chi^{\lambda'}_\mu} = n!\,\delta_{\lambda\lambda'}, \qquad \sum_{\lambda\vdash n}\chi^\lambda_\mu\overline{\chi^\lambda_\nu} = \frac{n!}{\lvert C_\mu\rvert}\delta_{\mu\nu},
$$

the row and column orthogonality relations.

**Example.** For $S_4$ the classes $\mu$, their sizes, and the five irreducible characters are, with dimensions $1,3,2,3,1$ from the hook length formula:

| $\mu$ | $\lvert C_\mu\rvert$ | $\chi^{(4)}$ | $\chi^{(3,1)}$ | $\chi^{(2,2)}$ | $\chi^{(2,1,1)}$ | $\chi^{(1^4)}$ |
|---|---|---|---|---|---|---|
| $(1^4)$ | $1$ | $1$ | $3$ | $2$ | $3$ | $1$ |
| $(2,1,1)$ | $6$ | $1$ | $1$ | $0$ | $-1$ | $-1$ |
| $(2,2)$ | $3$ | $1$ | $-1$ | $2$ | $-1$ | $1$ |
| $(3,1)$ | $8$ | $1$ | $0$ | $-1$ | $0$ | $1$ |
| $(4)$ | $6$ | $1$ | $-1$ | $0$ | $1$ | $-1$ |

The class sizes sum to $24$, and the columns are orthogonal with the weights $\lvert C_\mu\rvert$: for example the second and third columns give $1\cdot3\cdot2 + 6\cdot1\cdot0 + 3\cdot(-1)\cdot2 + 8\cdot0\cdot(-1)+6\cdot(-1)\cdot0 = 6-6 = 0$. Each row satisfies $\sum_\mu\lvert C_\mu\rvert\lvert\chi^\lambda_\mu\rvert^2 = 24$, as it must.

---

## Young Tableaux and the Specht Modules

### Permutation Modules and Young's Rule

**Definition.** Fix $n$ and a partition $\lambda$ of $n$. A **Young subgroup** $S_\lambda$ is the subgroup preserving the set of the first $\lambda_1$ symbols, then the next $\lambda_2$, and so on; a **$\lambda$-tabloid** is a partition of $\{1,\ldots,n\}$ into blocks of sizes $\lambda_1,\lambda_2,\ldots$, that is, a coset of $S_\lambda$; and the **permutation module** $M^\lambda$ is the $K$-module with the tabloids as basis, on which $S_n$ acts by permuting the symbols.

**Theorem (Young's rule).** The permutation module decomposes as

$$
M^\lambda \cong \bigoplus_{\mu \vdash n}(S^\mu)^{\oplus K_{\mu\lambda}},
$$

with $K_{\mu\lambda}$ the Kostka number, the number of semistandard tableaux of shape $\mu$ and weight $\lambda$.

**Proof sketch.** The endomorphism ring of $M^\lambda$ is a Hecke-type double coset ring, and the multiplicity of $S^\mu$ in $M^\lambda$ equals the dimension of the space of $S_n$-invariant maps, which is computed by counting semistandard tableaux: a standard argument assigns to each semistandard tableau of shape $\mu$ and weight $\lambda$ a nonzero homomorphism, and shows these form a basis of $\operatorname{Hom}_{S_n}(S^\mu, M^\lambda)$. $\square$

**Example.** For $n = 3$ and $\lambda = (2,1)$: the permutation module is the natural three-dimensional module $K^3$ spanned by three tabloids, and $K^3$ is the direct sum of the trivial representation (spanned by the sum of the basis) and the two-dimensional standard representation. Correspondingly $h_2h_1 = s_{(3)}+s_{(2,1)}$ in the symmetric function notation of *Symmetric Functions and Schur Functions*, since $M^\lambda$ has characteristic $\operatorname{ch}(M^\lambda) = h_\lambda$, and the Kostka numbers $K_{(3),(2,1)} = 1$, $K_{(2,1),(2,1)} = 1$.

### Specht Modules

**Definition.** A **polytabloid** attached to a tableau $t$ of shape $\lambda$ is $e_t = \sum_{\sigma\in C_t}\operatorname{sgn}(\sigma)\{\sigma t\}$, the alternating sum over the column group of $t$ of the tabloids obtained from $t$; the **Specht module** $S^\lambda$ is the submodule of $M^\lambda$ spanned by the polytabloids. A tableau is **standard** if it is strictly increasing along rows and down columns; the number of standard tableaux of shape $\lambda$ is written $f^\lambda$.

**Theorem (the irreducible representations).** Let $K$ be a field of characteristic $0$.

**(a)** $S^\lambda$ is irreducible, and every irreducible representation of $S_n$ is isomorphic to exactly one $S^\lambda$; in particular the irreducible representations are indexed by partitions of $n$, and $\chi^\lambda$ is the character of $S^\lambda$.

**(b)** The polytabloids $e_t$ with $t$ standard form a $K$-basis of $S^\lambda$, so $\dim S^\lambda = f^\lambda$.

**(c)** (hook length formula) $f^\lambda = \frac{n!}{\prod_{u\in\lambda}h(u)}$, the product over the hook lengths of the cells of $\lambda$.

**(d)** (branching rule) $S^\lambda$ restricted to $S_{n-1}$ decomposes as $\bigoplus_{\lambda^-}S^{\lambda^-}$, the sum over partitions $\lambda^-$ of $n-1$ whose Young diagram is obtained from that of $\lambda$ by removing one cell.

**Proof sketch.** (a) The standard filtration argument: the polytabloids span, and the submodule structure of $M^\lambda$ over an arbitrary field is controlled by the dominance order, the Specht modules being the layers, and over a field of characteristic $0$ each layer is a direct summand, hence irreducible. (b) The standard basis theorem, proved by the straightening algorithm: a straightening rule expresses any polytabloid as an integer combination of standard ones, and the leading terms are distinct, which gives independence and spanning. (d) follows from the same description, since removing a cell from the diagram of $\lambda$ is exactly what restriction does to the standard bases. $\square$

**Example.** Dimensions of the irreducible representations of $S_4$, computed by the hook length formula: $f^{(4)} = 24/(4\cdot3\cdot2\cdot1) = 1$; $f^{(3,1)} = 24/(4\cdot2\cdot1\cdot1) = 3$; $f^{(2,2)} = 24/(3\cdot2\cdot2\cdot1) = 2$; $f^{(2,1,1)} = 3$; $f^{(1^4)} = 1$. The squares sum to $1+9+4+9+1 = 24 = \lvert S_4\rvert$. The hook lengths used are those tabulated in *Symmetric Functions and Schur Functions*.

**Example (branching).** For $S_4$: $S^{(4)}$ restricts to $S^{(3)}$; $S^{(3,1)}$ restricts to $S^{(2,1)}\oplus S^{(3)}$; $S^{(2,2)}$ restricts to $S^{(2,1)}$; $S^{(2,1,1)}$ restricts to $S^{(1,1,1)}\oplus S^{(2,1)}$; $S^{(1^4)}$ restricts to $S^{(1^3)}$. The dimensions check: $1 = 1$; $3 = 2+1$; $2 = 2$; $3 = 1+2$; $1 = 1$. Iterating the branching rule produces the **Young lattice** of partitions, whose saturated chains from $\emptyset$ to $\lambda$ are exactly the standard tableaux of shape $\lambda$, whence $f^\lambda = \sum_{\lambda^-}f^{\lambda^-}$ and the hook length formula in its recursive form $f^\lambda = \binom{n-1}{\lvert\lambda^-\rvert}\cdots$ is equivalent to the product form.

### The Murnaghan–Nakayama Rule

**Definition.** A **rim hook** (or border strip) of a Young diagram $\lambda$ is a connected skew shape $\xi = \lambda/\mu$ containing no $2\times2$ block; its **height** $\operatorname{ht}(\xi)$ is one less than the number of rows it occupies, and its sign is $(-1)^{\operatorname{ht}(\xi)}$.

**Theorem (Murnaghan–Nakayama).** Let $\lambda \vdash n$ and let $\mu = (\mu_1,\ldots,\mu_k)$ be a partition. Then

$$
\chi^\lambda_\mu = \sum_{\xi}(-1)^{\operatorname{ht}(\xi)},
$$

the sum over all ways to remove from $\lambda$ a rim hook $\xi$ of size $\mu_1$ such that the remaining diagram is the diagram of a partition $\lambda^-$ with $\chi^{\lambda^-}_{(\mu_2,\ldots,\mu_k)} \neq 0$, each removal weighted by its sign.

**Proof sketch.** The rule follows from the restriction of $S^\lambda$ to the Young subgroup of a cycle and the explicit combinatorics of the $n$-cycle acting on the polytabloid basis; equivalently, it is the translation into tableaux of the identity $\operatorname{ch}(\chi)(p_\mu) = \chi_\mu$ together with the Jacobi–Trudi expansion of the Schur function. $\square$

**Example.** For $\lambda = (2,1)$ and $\mu = (3)$: the border strips of $(2,1)$ are the single cells $(1,2)$ and $(2,1)$ and the whole rim $\{(1,1),(1,2),(2,1)\}$ of size $3$ and height $1$; only the whole rim has size $3$, so $χ^{(2,1)}_{(3)} = -1$. For $\mu = (2,1)$ there is no border strip of size $2$ at all — the two ways of deleting two cells of the rim leave the shapes $\{(2,1)\}$ and $\{(1,2)\}$, neither of which is a Young diagram — so the sum is empty and $\chi^{(2,1)}_{(2,1)} = 0$. For $\mu = (1^3)$, each removal of a single corner leaves a Young diagram, giving $\chi^{(2,1)}_{(1^3)} = \chi^{(1,1)}_{(1,1)}+\chi^{(2)}_{(1,1)} = 1+1 = 2 = f^{(2,1)}$. The three values $2, 0, -1$ are exactly the row of the character table of $S_3$ for $\chi^{(2,1)}$.

**Example.** For $\lambda = (3,1)$ and $\mu = (2,2)$: the border strips of size $2$ of $(3,1)$ are $\{(1,3),(1,2)\}$, of height $0$, and no other, because deleting $\{(1,2),(1,1)\}$ or $\{(1,1),(2,1)\}$ leaves a shape that is not a Young diagram. The strip $\{(1,3),(1,2)\}$ leaves the diagram $(1,1)$, of size $2$, and $\chi^{(1,1)}_{(2)} = -1$ since $(1,1)$ carries the sign representation. Hence

$$
\chi^{(3,1)}_{(2,2)} = (+1)\cdot(-1) = -1,
$$

in agreement with the character table of $S_4$ displayed above. Computing the whole row $(3,1)$ by the rule — sizes $2+1+1$ in all orders for the class $(2,1,1)$ and sizes $1+1+1+1$ for the identity — reproduces $3, 1, -1, 0, -1$ as tabulated, and the dimensions $f^\lambda$ arise as the values at the identity, since every removal of a corner from a Young diagram leaves a Young diagram.

---

## The Modular Theory

**Definition.** Let $K$ be a field of characteristic $p$, and call a partition **$p$-regular** if no part is repeated $p$ times. The irreducible $K[S_n]$-modules are then indexed by the $p$-regular partitions of $n$, so that in characteristic $p$ the number of irreducible representations need not equal the number of conjugacy classes.

**Theorem (Brauer, James).** Let $K$ have characteristic $p$.

**(a)** The number of irreducible representations of $S_n$ over $K$ equals the number of $p$-regular partitions of $n$; the irreducible module $D^\lambda$ attached to a $p$-regular $\lambda$ is the head of the Specht module $S^\lambda$, and the other Specht modules have $D^\mu$ as a composition factor of $S^\lambda$ with multiplicity given by the **decomposition numbers** $d_{\lambda\mu}$.

**(b)** The **$p$-core** of a partition is obtained by repeatedly removing border strips of size $p$; it does not depend on the order of removal. Two partitions $\lambda, \mu dash n$ lie in the same **$p$-block** of $S_n$ if and only if they have the same $p$-core, a statement known as Nakayama's conjecture and proved by Brauer.

**(c)** The decomposition matrix of $S_n$ is unitriangular with respect to the dominance order among $p$-regular partitions, and its entries are the composition multiplicities, not generally known by a closed formula.

**Example.** For $p = 2$ and $n = 3$: the $2$-cores of the partitions of $3$ are obtained by deleting dominoes, giving $(1)$ for $(3)$ and for $(2,1)$, and $\emptyset$ for $(1,1,1)$. Hence there are two $2$-blocks, $\{(3),(2,1)\}$ and $\{(1,1,1)\}$, and the $2$-regular partitions — those with no part repeated twice — are $(3)$ and $(2,1)$, so there are two irreducible $2$-modular representations, in agreement with the two blocks. In characteristic $2$ the trivial and sign representations of $S_n$ are isomorphic, since $-1 = 1$ in $K$.

**Remark.** The modular theory of $S_n$ is equivalent, through the Schur–Weyl correspondence, to the theory of polynomial representations of the general linear group in the same characteristic, and the decomposition numbers of $S_n$ are the multiplicities in the decomposition of the Weyl modules. The Hecke algebra deformations of the group ring, in which the symmetric-group theory is the case $q = 1$, belong to *Symmetric Linear Algebras* and are not developed here.

---

## Bridges to the Rest of the Theory

**Theorem (Frobenius characteristic, restated).** The map $\operatorname{ch}$, sending a character $\chi$ of $S_n$ to $\frac{1}{n!}\sum_{\sigma\in S_n}\chi(\sigma)p_{\operatorname{cyc}(\sigma)}$, is an isometric isomorphism from the character ring of $S_n$ to the symmetric functions of degree $n$, and it sends the irreducible character $\chi^\lambda$ to the Schur function $s_\lambda$. Under this map the regular representation corresponds to $\sum_\lambda(\dim S^\lambda)s_\lambda$, the permutation module $M^\mu$ to $h_\mu$, and the restriction from $S_n$ to $S_{n-1}$ to multiplication by $h_1 = p_1$, which is the branching rule written in the Schur basis.

**Example.** The branching rule in the symmetric function form reads $s_\lambda\cdot h_1 = \sum_{\lambda^+}s_{\lambda^+}$, the sum over partitions $\lambda^+$ obtained from $\lambda$ by adding one cell; this is the Pieri rule for a single row and it is the Young lattice in the Schur basis. For $\lambda = (2,1)$ in degree $3$: $s_{(2,1)}h_1 = s_{(3,1)}+s_{(2,2)}+s_{(2,1,1)}$, matching the three ways of adding a cell to $(2,1)$, and this identity is the branching rule of the standard basis of the Specht module.

**Theorem (Schur–Weyl duality, statement).** Let $K$ be a field of characteristic $0$ and let $V = K^n$; the symmetric group $S_d$ acts on $V^{\otimes d}$ by permuting the factors and $GL(V)$ acts diagonally, the two actions commuting. Then

$$
V^{\otimes d} \cong \bigoplus_{\lambda\vdash d,\ \ell(\lambda)\leq n}S^\lambda\otimes W^\lambda,
$$

with $S^\lambda$ the Specht module and $W^\lambda$ the irreducible polynomial representation of $GL(V)$ of highest weight $\lambda$; the multiplicity of $S^\lambda$ is $\dim W^\lambda = s_\lambda(1^n)$, and the two endomorphism rings are the homomorphic images of the respective group rings. The pro, the construction of $W^\lambda$ as a Weyl module, and the modular version arebeing.

**Example.** For $d = 2$ and $n \geq 2$: $V^{\otimes2} = \operatorname{Sym}^2V\oplus\Lambda^2V$, with $S^{(2)}$ acting trivially on the symmetric part and by the sign on the exterior part; the multiplicity of $S^{(2)}$ is $\dim\operatorname{Sym}^2V = \binom{n+1}{2} = s_{(2)}(1^n)$ and that of $S^{(1,1)}$ is $\binom{n}{2} = s_{(1,1)}(1^n)$, in agreement with the dimension formula $s_\lambda(1^n) = \prod_{i<j}\frac{\lambda_i-\lambda_j+j-i}{j-i}$ of *Symmetric Functions and Schur Functions*. For $n = 2$ this gives $3+1 = 4 = 2^2$; for $n = 3$ it gives $6+3 = 9 = 3^2$.

**Corollary (the coinvariant algebra).** For the natural action of $S_n$ on $K[x_1,\ldots,x_n]$ the coinvariant algebra of *Symmetric Functions and Schur Functions* has dimension $n!$ and carries the regular representation; its decomposition into irreducibles is the multiplicity formula above with $d$ ranging over the degrees of the generators, and it is the quotient of the polynomial ring by the ideal generated by the invariants of *Invariant Theory*.

---

## Summary

A representation of $S_n$ over a field $K$ is an action of $S_n$ on a $K$-module by linear automorphisms, equivalently a module over the group ring $K[S_n]$; when the characteristic of $K$ does not divide $n!$, Maschke's theorem makes every representation a direct sum of irreducibles, Schur's lemma makes the intertwining maps between irreducibles isomorphisms, and the number of irreducible representations equals the number of conjugacy classes, that is, the number of partitions of $n$. The regular representation decomposes as $K[S_n] \cong \bigoplus_{\lambda\vdash n}(S^\lambda)^{\oplus\dim S^\lambda}$, whence $\sum_\lambda(\dim S^\lambda)^2 = n!$.

The irreducible representations are the Specht modules $S^\lambda$, constructed from tabloids and polytabloids, with the standard polytabloids as a basis, so that $\dim S^\lambda = f^\lambda$ is the number of standard tableaux and equals $n!/\prod_{u\in\lambda}h(u)$ by the hook length formula: for $S_4$ the dimensions are $1,3,2,3,1$, squaring and summing to $24$. The permutation modules $M^\lambda$ decompose as $\bigoplus_\mu(S^\mu)^{\oplus K_{\mu\lambda}}$ by Young's rule, restriction to $S_{n-1}$ obeys the branching rule $S^\lambda\downarrow = \bigoplus_{\lambda^-}S^{\lambda^-}$ along the Young lattice, and the characters are computed by the Murnaghan–Nakayama rule, which removes border strips of sizes $\mu_1,\mu_2,\ldots$ with signs from the heights; the character table of $S_4$ is displayed with its orthogonality relations verified, and the values $\chi^{(2,1)}_{(3)} = -1$, $\chi^{(2,1)}_{(2,1)} = 0$, $\chi^{(3,1)}_{(2,2)} = -1$ are computed by the rule.

The Frobenius characteristic identifies the character ring of $S_n$ with the symmetric functions of degree $n$, sending $\chi^\lambda$ to $s_\lambda$, $M^\mu$ to $h_\mu$, and restriction to $S_{n-1}$ to multiplication by $h_1$, which recovers the branching rule as the single-row Pieri rule $s_\lambda h_1 = \sum_{\lambda^+}s_{\lambda^+}$. Schur–Weyl duality writes $V^{\otimes d} \cong \bigoplus_{\lambda\vdash d}S^\lambda\otimes W^\lambda$ with multiplicity $\dim W^\lambda = s_\lambda(1^n)$, the case $d = 2$ giving $\operatorname{Sym}^2V\oplus\Lambda^2V$. In characteristic $p$ the irreducible representations are indexed by the $p$-regular partitions rather than by all partitions, the Specht modules acquire composition series with the decomposition numbers as multiplicities, and two partitions lie in the same $p$-block exactly when they share a $p$-core; for $p = 2$ and $n = 3$ the blocks are $\{(3),(2,1)\}$ and $\{(1,1,1)\}$, matching the two $2$-regular partitions. The Hecke algebra and Macdonald polynomial deformations of this theory belong to *Symmetric Linear Algebras* and are not treated here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_n$ | Symmetric group on $n$ symbols |
| $K[S_n]$ | The group ring, used as a ring acting on modules |
| $\lambda$, $\mu$ | Partitions; a partition labels a conjugacy class by cycle type |
| $M^\lambda$ | Permutation module on $\lambda$-tabloids |
| $S^\lambda$, $D^\lambda$ | Specht module, irreducible modular module |
| $\chi^\lambda$, $\chi^\lambda_\mu$ | Irreducible character, its value at the class $\mu$ |
| $f^\lambda$ | Number of standard tableaux of shape $\lambda$ |
| $K_{\lambda\mu}$ | Kostka number |
| $h(u)$, $c(u)$ | Hook length and content of a cell |
| $\unrhd$ | Dominance order |
| $\xi$, $\operatorname{ht}(\xi)$ | Rim (border) hook, its height |
| $d_{\lambda\mu}$ | Decomposition number |
| $p$-core, $p$-block | Modular invariants of a partition and of $S_n$ |
| $W^\lambda$ | Irreducible polynomial representation of $GL_n$ |
| $\operatorname{ch}$, $z_\lambda$ | Frobenius characteristic, power-sum normalisation |





## Further Reading

- Alfred Young, "On quantitative substitutional analysis", *Proceedings of the London Mathematical Society* 33 (1901), 97–146, and later parts, for the tableau calculus and the standard basis.
- Georg Frobenius, "Über die Primfaktoren der Gruppendeterminante", *Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften* (1896), 1343–1382, for the characters of the symmetric group and the characteristic map.
- T. Murnaghan and T. Nakayama, respectively "On the representations of the symmetric group", *American Journal of Mathematics* 59 (1937), 437–488, and "On some modular properties of irreducible representations of a symmetric group", *Japanese Journal of Mathematics* 17 (1940), 89–108 and 411–423, for the character rule and the blocks.
- Gordon James, *The Representation Theory of the Symmetric Groups* (Springer, 1978), for the modular theory, the Specht modules over an arbitrary field and the decomposition numbers.
- Gordon James and Adalbert Kerber, *The Representation Theory of the Symmetric Group* (Addison-Wesley, 1981), for the complete classical treatment including the symmetric function bridge.
- Bruce Sagan, *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* (Springer, 2nd ed. 2001), for the accessible development of the standard basis, the branching rule and Young's rule.
- Richard P. Stanley, *Enumerative Combinatorics*, Volume 2 (Cambridge University Press, 1999), for the Young lattice, the RSK correspondence and the symmetric function identities.
- Hermann Weyl, *The Classical Groups* (Princeton University Press, 1939), for the duality with the general linear group.
- Richard Brauer, "On a conjecture by Nakayama", *Transactions of the Royal Society of Canada* 41 (1947), 11–25, for the proof of the block classification.
