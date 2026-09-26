
# __Induced Representations__

## Introduction

Let $G$ be a finite group, $H\leq G$ a subgroup and $W$ a $k[H]$-module. The **induced module**

$$
\operatorname{Ind}_H^GW = k[G]\otimes_{k[H]}W
$$

is the $k[G]$-module obtained from $W$ by extending the scalars along the inclusion $k[H]\subseteq k[G]$, and the **restriction** $\operatorname{Res}_H^GV$ of a $k[G]$-module $V$ is the same space regarded as a $k[H]$-module; the two constructions are the two directions of the change of rings along the inclusion, and the **Frobenius reciprocity** that relates them is the adjunction between the extension and the restriction of scalars. Induction is the principal construction of the representation theory of a finite group: the irreducible representations of $G$ are built from those of its subgroups, and the questions of the theory — which induced modules are irreducible, how an induced module restricts, how tensor products of induced modules decompose — are answered by the double coset decompositions of $G$ relative to $H$.

The article is the twenty-second of the corpus, in the category *Linear Spaces over Linear Algebras*, and it follows *Morita Equivalence*, *The Balanced Product over an Algebra* and *Change of Rings* immediately above it; the definition of the induced module is the **balanced product** of *The Balanced Product over an Algebra* with the group algebra of *Group Algebras*, and the adjunction of Frobenius reciprocity is the tensor-hom adjunction of *Change of Rings*. The article develops induction and coinduction and their coincidence for finite groups, the reciprocity and its consequences for the character theory of *Character Theory*, the explicit formula for the character of an induced module together with its verification on $S_3$, the theorem of Mackey on the restriction of an induced module with the double coset decomposition and the resulting irreducibility criterion, the theorem of Clifford on the restriction of an irreducible module to a normal subgroup and the reduction of the classification to the projective representations of an inertia quotient, and the permutation and monomial modules with the induction theorems of Artin and Brauer.

Two boundaries are kept. The first is with the modular theory: the induction is defined for any field, but the results quoted here on the characters and on the multiplicities are formulated for the semisimple case, that is with $\lvert G\rvert$ invertible in $k$; the modular theory and the Brauer characters are not covered here, and the integral form of the induction theorems over a discrete valuation ring belongs. The second is with the analytic theory: the induced representations of a locally compact group, the Hilbert space of the induction and the measure-theoretic forms of the theorems need Part III, and the present article treats finite groups, in which case the induction is a purely algebraic balanced product.

Throughout, $G$ is a finite group and $H,K\leq G$ are subgroups, $k$ is a field with $\lvert G\rvert$ invertible, $W$ is a $k[H]$-module and $V$ a $k[G]$-module, $\operatorname{Ind}_H^GW = k[G]\otimes_{k[H]}W$ and $\operatorname{Res}_H^GV$ are the induced and the restricted modules, $\operatorname{Coind}_H^GW = \operatorname{Hom}_{k[H]}(k[G],W)$, $G = \bigsqcup_{x}HxK$ is a double coset decomposition, $\mathbf{1}_H$ is the trivial $k[H]$-module, and $k[G/H]$ is the permutation module of the action on the cosets.

## Induction and Coinduction

**Definition.** Let $H\leq G$, let $W$ be a $k[H]$-module and $V$ a $k[G]$-module. The **induced module** is the $k[G]$-module $\operatorname{Ind}_H^GW = k[G]\otimes_{k[H]}W$ with $G$ acting on the left factor, and the **coinduced module** is $\operatorname{Coind}_H^GW = \operatorname{Hom}_{k[H]}(k[G],W)$ with $(g\cdot f)(x) = f(xg)$; the **restriction** $\operatorname{Res}_H^GV$ is the $k[H]$-module obtained by restricting the action.

**Proposition.** Let $H\leq G$ and let $V$ be a $k[G]$-module. Then there are natural isomorphisms of $k[G]$-modules

$$
\operatorname{Ind}_H^G\operatorname{Res}_H^GV = k[G]\otimes_{k[H]}V\;\cong\;\bigoplus_{g\in T}g\otimes V, \qquad \operatorname{Coind}_H^GW\cong W^{\oplus[G:H]},
$$

where $T$ is a set of left coset representatives of $H$ in $G$; for finite $G$ the induced and the coinduced module are isomorphic, $\operatorname{Ind}_H^GW\cong\operatorname{Coind}_H^GW$.

*Proof.* The induced module is a free right $k[H]$-module $k[G]$ tensored with $W$, and $k[G] = \bigoplus_{g\in T}gk[H]$ as a right $k[H]$-module, giving the first isomorphism; for finite $G$ the $k[G]$-module $k[G]$ is finitely generated and free over $k[H]$, and the duality between the tensor product over $k[H]$ and the hom functor, applied to the finite free module $k[G]$, identifies the induced and the coinduced module. $\square$

**Definition (the function model).** A $k[G]$-module structure on the $k$-module of functions $f:G\to W$ with the **equivariance condition**

$$
f(gh) = h^{-1}\cdot f(g) \quad\text{for } g\in G,\ h\in H, \qquad (g_0\cdot f)(g) = f(g_0^{-1}g),
$$

is the **induced module in the function model**; it is isomorphic to $k[G]\otimes_{k[H]}W$ by $g\otimes w\mapsto f$ with $f(g_0) = 0$ unless $g_0\in gH$ and $f(g) = w$, and it is the model in which the character formula of the third section is read. The $k$-linear maps $G\to W$ satisfying the condition are constant on the left cosets of $H$ and are determined by their values on a transversal, so the function module has $k$-dimension $[G:H]\dim_kW$.

**Example (permutation modules).** Taking $W = \mathbf{1}_H$ the trivial module gives $\operatorname{Ind}_H^G\mathbf{1}_H = k[G]\otimes_{k[H]}k = k[G/H]$, the **permutation module** of the action of $G$ on the left cosets of $H$; its character is the **permutation character** $g\mapsto\lvert\{xH : gxH = xH\}\rvert$, the number of fixed points, and for $H = 1$ it is the regular module $k[G]$ with character $\lvert G\rvert\delta_{g,1}$. The induction from the trivial module is thus the linearisation of a group action, and every permutation representation arises in this way.

**Proposition (transitivity).** For subgroups $K\leq H\leq G$ there is a natural isomorphism

$$
\operatorname{Ind}_H^G\bigl(\operatorname{Ind}_K^HW\bigr)\;\cong\;\operatorname{Ind}_K^GW,
$$

the **transitivity of the induction**, and $\operatorname{Res}_H^G$ is transitive in the other direction, $\operatorname{Res}_K^H\operatorname{Res}_H^GV = \operatorname{Res}_K^GV$.

*Proof.* Both sides are $k[G]\otimes_{k[K]}W$ up to the canonical isomorphism $k[G]\otimes_{k[H]}(k[H]\otimes_{k[K]}W)\cong k[G]\otimes_{k[K]}W$, which is the associativity of the balanced product of *The Balanced Product over an Algebra*; the restriction is transitive because the inclusion of modules of the group algebras is. $\square$

## Frobenius Reciprocity

**Theorem (Frobenius reciprocity).** Let $H\leq G$, let $W$ be a $k[H]$-module and $V$ a $k[G]$-module. Then there are natural isomorphisms of $k$-modules

$$
\operatorname{Hom}_{k[G]}\bigl(\operatorname{Ind}_H^GW,V\bigr)\;\cong\;\operatorname{Hom}_{k[H]}\bigl(W,\operatorname{Res}_H^GV\bigr), \qquad \operatorname{Hom}_{k[G]}\bigl(V,\operatorname{Coind}_H^GW\bigr)\;\cong\;\operatorname{Hom}_{k[H]}\bigl(\operatorname{Res}_H^GV,W\bigr),
$$

the **adjunction** between the induction and the restriction of scalars.

*Proof.* This is the tensor-hom adjunction of *Change of Rings* for the ring homomorphism $k[H]\to k[G]$: the extension of scalars along a ring map is left adjoint to the restriction, and the tensor product over $k[H]$ with $k[G]$ is the extension functor. $\square$

**Corollary (the character form).** Let $k$ be a splitting field of characteristic zero with $\lvert G\rvert$ invertible, let $\chi$ be the character of $W$ and $\psi$ the character of $V$. Then

$$
\bigl\langle\operatorname{Ind}_H^G\chi,\ \psi\bigr\rangle_G = \bigl\langle\chi,\ \operatorname{Res}_H^G\psi\bigr\rangle_H ,
$$

the inner products being those of *Character Theory* taken in the respective groups; consequently the multiplicity of the simple $k[G]$-module $V$ in $\operatorname{Ind}_H^GW$ equals the multiplicity of $W$ in $\operatorname{Res}_H^GV$, and $\operatorname{Ind}_H^G\chi = \sum_jd_j\psi_j$ with $d_j = \langle\chi,\operatorname{Res}\psi_j\rangle_H$.

*Proof.* The reciprocity of the theorem is an isomorphism of Hom spaces; taking dimensions over $k$ and dividing by the orders, the left side counts the multiplicity of $V$ in the induced module and the right side the multiplicity of $W$ in the restricted module, and the character pairing is the dimension of the Hom space by Schur's lemma. $\square$

**Corollary (the induction of the trivial character).** For any $H\leq G$ the induced module $\operatorname{Ind}_H^G\mathbf{1}_H$ contains a unique copy of the trivial $k[G]$-module, corresponding to the constant functions in the function model, and $\langle\operatorname{Ind}_H^G\mathbf{1},\mathbf{1}\rangle_G = 1$; the multiplicities of the other simple modules in the permutation module are the multiplicities with which the trivial module of $H$ occurs in their restrictions.

*Proof.* $\langle\operatorname{Ind}_H^G\mathbf{1},\mathbf{1}\rangle_G = \langle\mathbf{1},\operatorname{Res}_H^G\mathbf{1}\rangle_H = 1$ by the reciprocity, and the Hom space of the invariants of the permutation module is one-dimensional, spanned by the constant function. $\square$

## The Character Formula

**Theorem (the induced character formula).** Let $k$ be a splitting field of characteristic zero with $\lvert G\rvert$ invertible, let $H\leq G$, let $W$ be a $k[H]$-module with character $\chi$ and let $\widetilde\chi = \operatorname{Ind}_H^G\chi$ be the character of the induced module. Then for $g\in G$

$$
\widetilde\chi(g) = \frac{1}{\lvert H\rvert}\sum_{\substack{x\in G\\x^{-1}gx\in H}}\chi\bigl(x^{-1}gx\bigr) = \sum_{\substack{x\in T\\x^{-1}gx\in H}}\chi\bigl(x^{-1}gx\bigr),
$$

the second sum being taken over a set $T$ of left coset representatives of $H$ in $G$; in particular $\widetilde\chi(g) = 0$ unless $g$ is conjugate to an element of $H$, and $\widetilde\chi(1) = [G:H]\chi(1)$.

*Proof.* The module $k[G]\otimes_{k[H]}W$ has the $k$-basis $x\otimes w$ with $x\in T$ running over a transversal, and the trace of $g$ on this module is the sum over the $x$ for which $g$ maps the summand $x\otimes W$ to itself; the condition for that is $x^{-1}gx\in H$, and on such a summand the action of $g$ on $x\otimes W$ corresponds to the action of $x^{-1}gx$ on $W$, whose trace is $\chi(x^{-1}gx)$. This gives the second display, and the first follows since each $h\in H$ with $x^{-1}gx\in H$ contributes the same term over the $\lvert H\rvert$ elements of the coset. $\square$

**Corollary (permutation characters).** For the trivial module $W = \mathbf{1}_H$ the formula gives the number of fixed points: $\widetilde{\mathbf{1}}(g) = \frac{1}{\lvert H\rvert}\lvert\{x\in G : x^{-1}gx\in H\}\rvert$, the number of left cosets fixed by $g$, and $\widetilde{\mathbf{1}}(g) = \lvert\{x\in T : x^{-1}gx\in H\}\rvert$.

**Example (induction from $S_2$ to $S_3$).** Let $G = S_3$, let $H = S_2 = \{e,(12)\}$ be the stabiliser of the point $3$, and let $W$ be the trivial $k[H]$-module. The induced module is the permutation module $k[S_3/S_2]$, of dimension $3$, and the formula gives the values $3$ at the identity, $1$ at each transposition and $0$ at each 3-cycle. Decomposing with the table of *Character Theory*: the multiplicities are $\langle\widetilde{\mathbf{1}},\mathbf{1}\rangle = \frac{1}{6}(3+3\cdot1+2\cdot0) = 1$, $\langle\widetilde{\mathbf{1}},\varepsilon\rangle = \frac{1}{6}(3+3\cdot(-1)+0) = 0$ and $\langle\widetilde{\mathbf{1}},\sigma\rangle = \frac{1}{6}(3\cdot2+3\cdot0+2\cdot0) = 1$, so that

$$
\operatorname{Ind}_{S_2}^{S_3}\mathbf{1}_{S_2} \cong \mathbf{1}\oplus\sigma ,
$$

the trivial module plus the two-dimensional standard module; the reciprocity was also checked numerically for this example: $\langle\operatorname{Ind}\mathbf{1},\sigma\rangle_G = 1 = \langle\mathbf{1},\operatorname{Res}\sigma\rangle_H$, the restriction of $\sigma$ to $H$ being the direct sum of the trivial and the sign characters of $H$, of which exactly one copy of the trivial occurs. The multiplicities, the values of the induced character on all six elements and the reciprocity equality were recomputed by direct enumeration of the permutations of $S_3$ with the exact arithmetic of the character table.

## Mackey's Theorem and the Double Cosets

**Definition.** Let $H,K\leq G$. The **double cosets** $HxK = \{hxk\}$ partition $G$ into disjoint subsets, $G = \bigsqcup_{x\in S}HxK$ with $S$ a set of representatives, and for $x\in S$ the intersection $H\cap xKx^{-1}$ is a subgroup of $H$.

**Theorem (Mackey).** Let $H,K\leq G$, let $W$ be a $k[H]$-module and let $W^x$ be the $k[H\cap xKx^{-1}]$-module obtained from $W$ by the conjugation $h\mapsto x^{-1}hx$ followed by restriction to $H\cap xKx^{-1}$. Then there is an isomorphism of $k[K]$-modules

$$
\operatorname{Res}_K^G\operatorname{Ind}_H^GW \;\cong\; \bigoplus_{x\in S}\operatorname{Ind}_{H\cap xKx^{-1}}^{K}\bigl(W^x\bigr),
$$

the sum being over a set of double coset representatives of $H\backslash G/K$.

*Proof (outline).* The double coset decomposition refines the coset decomposition of $k[G]$ as a right $k[H]$-module, and the summand $k[HxK]\otimes_{k[H]}W$ is a $k[K]$-module induced from the stabiliser of the coset: the elements of $k[HxK]$ are the $hxk$, and the action of $K$ on the right leads to the intersection group $H\cap xKx^{-1}$ with the twisted module $W^x$. The details are the standard proof and are recorded in the references. $\square$

**Corollary (the intertwining number formula).** For finite $G$ the dimension of the space of $k[K]$-homomorphisms between the restrictions of induced modules is

$$
\dim_k\operatorname{Hom}_{k[K]}\bigl(\operatorname{Ind}_H^GW,\operatorname{Ind}_K^GV\bigr) = \sum_{x\in S}\dim_k\operatorname{Hom}_{k[K\cap x^{-1}Hx]}\bigl(W^x,\operatorname{Res}V\bigr),
$$

and the **irreducibility criterion** of Mackey: for $H = K$ and $W$ irreducible, $\operatorname{Ind}_H^GW$ is irreducible if and only if no double coset $HxH$ with $x\notin H$ contributes to the endomorphism ring, that is if and only if $W$ has no irreducible constituent in common with its conjugate $W^x$ under restriction to $H\cap xHx^{-1}$ for any $x\in G\smallsetminus H$.

*Proof.* The formula is the dimension count of the theorem applied with the reciprocity; the criterion follows by counting the endomorphisms of $\operatorname{Ind}_H^GW$, of dimension $\sum_{x\in S}\langle\operatorname{Res}_{H\cap xHx^{-1}}W^x,\operatorname{Res}W\rangle$, the inner products being taken in $H\cap xHx^{-1}$, which equals one exactly when the only non-zero term is the one of $x = 1$. $\square$

**Example (the tensor product of two permutation modules).** For $H,K\leq G$ and the trivial modules there is an isomorphism

$$
k[G/H]\otimes_kk[G/K]\;\cong\;\bigoplus_{x\in S}k\bigl[G/(H\cap xKx^{-1})\bigr],
$$

the **Mackey tensor product theorem**, whose right-hand side is induced from the trivial module of the intersections; the identity shows that the tensor product of two permutation representations is again a direct sum of permutation representations, one for each double coset, and it computes the tensor square of a permutation module, the case $H = K$ being the one used in the theory of the Hecke algebras of the permutation representations.

## Clifford Theory

**Definition.** Let $N\trianglelefteq G$ be a normal subgroup, let $\theta$ be an irreducible character of $N$ and let $V$ be an irreducible $k[G]$-module. One says that $V$ **lies over** $\theta$ if $\theta$ occurs in $\operatorname{Res}_N^GV$, and the **inertia group** of $\theta$ is

$$
I_G(\theta) = \{g\in G : \theta^g = \theta\}, \qquad \theta^g(n) = \theta(gng^{-1}),
$$

the stabiliser of $\theta$ under the conjugation action of $G$ on the irreducible characters of $N$; the inertia group lies between $N$ and $G$, and $\lvert G:I_G(\theta)\rvert$ equals the number of distinct conjugates of $\theta$.

**Theorem (Clifford, standard).** Let $N\trianglelefteq G$ and let $V$ be an irreducible $k[G]$-module with $\lvert G\rvert$ invertible in $k$. Then:

1. the restriction $\operatorname{Res}_N^GV$ is a direct sum of irreducible $k[N]$-modules conjugate under $G$, say of the $G$-orbit of a character $\theta$, each with the same multiplicity;
2. $V$ lies over $\theta$ if and only if it lies over every conjugate, and the irreducible modules of $G$ lying over $\theta$ are exactly the modules $\operatorname{Ind}_{I}^{G}U$ with $U$ an irreducible module of the inertia group $I = I_G(\theta)$ lying over $\theta$;
3. the modules $U$ lying over $\theta$ correspond to the **projective representations** of the quotient $I/N$ with the cocycle determined by $\theta$, so that the classification of the irreducible modules of $G$ over $\theta$ is the classification of the projective representations of $I/N$;

the last correspondence is not covered here, and the case of a trivial cocycle recovers the ordinary representations of $I/N$.

*Proof (outline).* The set of irreducible constituents of $\operatorname{Res}_N^GV$ is permuted by $G$ because $N$ is normal, and the trace argument shows that the conjugates are the constituents and occur with equal multiplicity; the induction from the inertia group produces the modules lying over $\theta$, and the exact sequence $1\to N\to I\to I/N\to1$ turns the lifting problem into a problem of projective representations, the cocycle being the failure of a fixed module over $\theta$ to extend to $I$. The proof is the standard one of Clifford's theory, recorded in the references. $\square$

**Corollary.** If $\theta$ extends to a representation of $I = I_G(\theta)$, then the irreducible modules of $G$ lying over $\theta$ are the inductions of the twists of the extension by the irreducible representations of $I/N$; in particular if $G = N\rtimes Q$ is a semidirect product and $\theta$ extends to its stabiliser, the classification is by the ordinary irreducible representations of $Q$, and no projective representation intervenes.

## Permutation and Monomial Modules

**Definition.** A $k[G]$-module is **monomial** if it is induced from a one-dimensional module of a subgroup, that is if it is isomorphic to $\operatorname{Ind}_H^G\lambda$ for a homomorphism $\lambda:H\to k^\times$; the permutation modules $k[G/H]$ are the case $\lambda = 1$, and every simple module of a finite group over a splitting field of characteristic zero occurs as a constituent of a monomial module, the precise statements being the induction theorems below.

**Theorem (Artin's induction theorem, standard).** Let $G$ be a finite group. Then every character of $G$ is a $\mathbb{Q}$-linear combination of characters induced from the trivial character of the cyclic subgroups of $G$: there are rational numbers $q_H$ with

$$
\chi = \sum_{\text{cyclic } H\leq G}q_H\operatorname{Ind}_H^G\mathbf{1}_H ,
$$

so that the rational representation ring is generated by the inductions from the cyclic subgroups.

**Theorem (Brauer's induction theorem, standard).** Let $G$ be a finite group. Then every character of $G$ is a $\mathbb{Z}$-linear combination of characters induced from the one-dimensional characters of the elementary subgroups of $G$, that is of the subgroups which are the direct product of a cyclic group and a $p$-group; consequently every character is a $\mathbb{Z}$-linear combination of monomial characters.

*Proof (outline).* Artin's theorem is proved by comparing the values on the cyclic subgroups and using the arithmetic of the cyclotomic fields, and Brauer's theorem by reducing to the $p$-elementary subgroups and using the induction from the one-dimensional characters of these, the theory of the Brauer characters supplying the stepping stone between the two. The proofs are standard and are recorded in the references. $\square$

**Remark.** The two induction theorems are the sense in which the representations of a finite group are controlled by its subgroups of restricted type: the cyclic subgroups for the rational theory and the elementary subgroups for the integral theory. They are the engine of the applications of the character theory to the arithmetic of the group rings and to the conjectures relating the group algebra to the representations, and their modular forms — the induction over a discrete valuation ring, with the lattices — are the subject of the final article of this category.

## Summary

For a subgroup $H\leq G$ of a finite group and a $k[H]$-module $W$, the **induced module** is $\operatorname{Ind}_H^GW = k[G]\otimes_{k[H]}W$, the balanced product of *The Balanced Product over an Algebra*, with the function model $f(gh) = h^{-1}f(g)$ and with $\operatorname{Coind}_H^GW = \operatorname{Hom}_{k[H]}(k[G],W)$ isomorphic to it; the induction is transitive and commutes with the restriction in the sense of the adjunction. **Frobenius reciprocity** is the isomorphism $\operatorname{Hom}_{k[G]}(\operatorname{Ind}_H^GW,V)\cong\operatorname{Hom}_{k[H]}(W,\operatorname{Res}_H^GV)$ of *Change of Rings*, whose character form $\langle\operatorname{Ind}\chi,\psi\rangle_G = \langle\chi,\operatorname{Res}\psi\rangle_H$ computes the multiplicities in an induced module; the **induced character formula** is

$$
\operatorname{Ind}_H^G\chi(g) = \frac{1}{\lvert H\rvert}\sum_{x\in G,\ x^{-1}gx\in H}\chi(x^{-1}gx),
$$

which for the trivial character gives the permutation character of $k[G/H]$. The example of $S_3$ is computed: $\operatorname{Ind}_{S_2}^{S_3}\mathbf{1} = \mathbf{1}\oplus\sigma$ with the values $3,1,1,0,0,1$, the multiplicities $1,0,1$ and the reciprocity verified numerically. **Mackey's theorem** decomposes the restriction of an induced module over the double cosets, $\operatorname{Res}_K^G\operatorname{Ind}_H^GW\cong\bigoplus_{x\in S}\operatorname{Ind}_{H\cap xKx^{-1}}^K(W^x)$, with the intertwining number formula and the irreducibility criterion as consequences, and the tensor product of two permutation modules decomposes as the sum of the permutation modules of the double coset intersections. **Clifford theory** describes the irreducible modules of $G$ lying over an irreducible $\theta$ of a normal subgroup $N$ as the inductions from the inertia group $I_G(\theta)$, the remaining freedom being the projective representations of $I_G(\theta)/N$, which is not covered here. Finally the **permutation and monomial modules** and the induction theorems of Artin and Brauer express every character as a combination of characters induced from the cyclic and from the elementary subgroups respectively. The modular case is deferred, the integral lattices, and the infinite-dimensional and measure-theoretic inductions to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $H$, $K$ | finite group and subgroups |
| $\operatorname{Ind}_H^GW = k[G]\otimes_{k[H]}W$ | induced module |
| $\operatorname{Coind}_H^GW = \operatorname{Hom}_{k[H]}(k[G],W)$ | coinduced module, isomorphic for finite $G$ |
| $\operatorname{Res}_H^GV$ | restricted module |
| $G = \bigsqcup_{x\in S}HxK$ | double coset decomposition |
| $W^x$, $H\cap xKx^{-1}$ | conjugate module and intersection group |
| $k[G/H]$, permutation character | permutation module and its character, fixed points |
| $\operatorname{Ind}_H^G\chi(g) = \frac{1}{\lvert H\rvert}\sum_{x^{-1}gx\in H}\chi(x^{-1}gx)$ | induced character formula |
| $I_G(\theta)$ | inertia group of an irreducible character $\theta$ of a normal subgroup |
| $\operatorname{Ind}_H^G\lambda$ | monomial module, $\lambda$ one-dimensional |
| $\mathbf{1}_H$ | trivial module of $H$ |





## Further Reading

- Georg Frobenius, "Über Relationen zwischen den Charakteren einer Gruppe und denen ihrer Untergruppen", *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin* (1898), 501–515, for the reciprocity and the induced characters.
- George W. Mackey, "On induced representations of groups", *American Journal of Mathematics* **73** (1951), 576–592, and "Induced representations of locally compact groups I", *Annals of Mathematics* **55** (1952), 101–139, for the double coset decomposition, the intertwining number formula and the tensor product theorem.
- Alfred H. Clifford, "Representations induced in an invariant subgroup", *Annals of Mathematics* **38** (1937), 533–550, for the theory of the inertia group and the reduction to projective representations.
- Emil Artin, "Zur Theorie der L-Reihen mit allgemeinen Gruppencharakteren", *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* **8** (1931), 292–306, for the induction theorem from the cyclic subgroups.
- Richard Brauer, "On Artin's L-series with general group characters", *Annals of Mathematics* **48** (1947), 502–514, and "Applications of induced characters", *American Journal of Mathematics* **69** (1947), 709–716, for the induction theorem from the elementary subgroups.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Academic Press, 1976), for the systematic treatment of the induced characters, the reciprocity and the Clifford theory.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the induced modules, the double coset formulas and the integral form of the theory.
