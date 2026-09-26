
# __Bott Periodicity and the Classification__

## Introduction

This article states and uses the two periodicity properties of Clifford algebras: the complex classification is periodic of period two, and the real classification is periodic of period eight. Both are consequences of the graded tensor product decomposition $\mathrm{Cl}_{p,q}\hat\otimes\mathrm{Cl}_{r,s}\cong\mathrm{Cl}_{p+r,q+s}$ established in the opening of the Clifford layer, together with the identification of the rank-eight algebra

$$
\mathrm{Cl}_{0,8}\cong\mathrm{Cl}_{8,0}\cong M_{16}(\mathbb{R}).
$$

The reader is assumed to have the definition of $\mathrm{Cl}(V,q)$, the $\mathbb{Z}/2$-grading $\mathrm{Cl}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ and the graded tensor product from that layer; the present article derives nothing that belongs there and restates only what it uses.

The conventions are those of the article *The Low-Dimensional Classification*. The base is a field $F$ of characteristic not $2$; the real signature form is $q=\operatorname{diag}(+1^{p},-1^{q})$ and $\mathrm{Cl}_{p,q}$ is its Clifford algebra, so that $p$ counts generators of square $+1$. The volume element of an orthogonal basis $e_1,\dots,e_n$ is $\omega=e_1\cdots e_n$, with $\omega^2=(-1)^{n(n-1)/2}\prod_i q(e_i)$.

The periodicity statements are computations of the small-rank algebras together with the recursive structure of the tensor product; they are the source of the "eightfold way" of the title, and they organise the entire Clifford layer.

## The Stabilisation Recursions

Three isomorphisms generate the classification. The first is the recursive step, and the other two are its consequences over the two rank-two forms.

**Theorem (the recursion).** For all $p,q\ge 0$ there is an algebra isomorphism

$$
\mathrm{Cl}_{p+1,q+1}\cong M_2\bigl(\mathrm{Cl}_{p,q}\bigr).
$$

**Proof.** The form $\operatorname{diag}(+1,-1)$ on a two-dimensional space has Clifford algebra $\mathrm{Cl}_{1,1}\cong M_2(F)$, computed directly in the previous article: its generators act as the matrices $\sigma_3=\operatorname{diag}(1,-1)$ and $\tau=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, which together with the identity and their product $\sigma_3\tau=-\sigma_1$ span $M_2(F)$. The graded tensor product decomposition of an orthogonal sum gives $\mathrm{Cl}_{p+1,q+1}\cong\mathrm{Cl}_{p,q}\,\hat{\otimes}\,\mathrm{Cl}_{1,1}$, and the isomorphism with $M_2(\mathrm{Cl}_{p,q})$ is displayed by the following assignment. Let $e_1,\dots,e_n$ generate $\mathrm{Cl}_{p,q}$ and let $f_1,f_2$ generate the hyperbolic plane, with $f_1^2=+1$, $f_2^2=-1$ and $f_1f_2=-f_2f_1$. In $2\times2$ matrices over $\mathrm{Cl}_{p,q}$, with $\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, put

$$
\Phi(e_i)=e_i\,\sigma_1,\qquad \Phi(f_1)=\sigma_3,\qquad \Phi(f_2)=\tau .
$$

Each image squares to the value of its form on the corresponding generator times the identity, and any two images anticommute, by $\sigma_1^2=\sigma_3^2=1$, $\tau^2=-1$ and the anticommutations $\sigma_1\sigma_3=-\sigma_3\sigma_1$, $\sigma_1\tau=-\tau\sigma_1$, $\sigma_3\tau=-\tau\sigma_3$; hence $\Phi$ extends to an algebra homomorphism by the universal property. Its image contains $I\sigma_3$, $I\tau$, $I\sigma_1=-(I\sigma_3)(I\tau)$ and $e_iI=-\Phi(e_i)\Phi(f_1)\Phi(f_2)$, since $\sigma_3\tau=-\sigma_1$ and $\sigma_1^2=1$; these generate $M_2(\mathrm{Cl}_{p,q})$, both sides have dimension $2^{n+2}$, so $\Phi$ is an isomorphism. $\square$

The same argument with the rank-two forms gives the following two identities, which express the "stabilisation" of a Clifford algebra by a hyperbolic plane.

**Corollary.** For all $p,q\ge 0$,

$$
\mathrm{Cl}_{p+2,q}\cong \mathrm{Cl}_{p,q}\,\hat{\otimes}\,\mathrm{Cl}_{2,0}, \qquad
\mathrm{Cl}_{p,q+2}\cong \mathrm{Cl}_{p,q}\,\hat{\otimes}\,\mathrm{Cl}_{0,2}.
$$

These are the graded tensor product decomposition read with $\mathrm{Cl}_{2,0}=M_2(F)$ and $\mathrm{Cl}_{0,2}=\mathbb{H}$; they are *graded* tensor products, not ordinary ones. The distinction is essential: the ordinary tensor product $\mathrm{Cl}_{2,0}\otimes\mathrm{Cl}_{2,0}=M_4(F)$ is not $\mathrm{Cl}_{4,0}=M_2(\mathbb{H})$, whereas the graded tensor product $\mathrm{Cl}_{2,0}\hat\otimes\mathrm{Cl}_{2,0}\cong\mathrm{Cl}_{4,0}$ is correct by definition. The odd part of a Clifford algebra carries a sign in every exchange, and it is exactly this sign that produces period eight rather than the naive multiplicativity.

**Low-rank instances.** The recursion gives $\mathrm{Cl}_{2,2}\cong M_2(\mathrm{Cl}_{1,1})=M_4(F)$, $\mathrm{Cl}_{3,3}\cong M_2(\mathrm{Cl}_{2,2})=M_8(F)$, and $\mathrm{Cl}_{4,4}\cong M_2(\mathrm{Cl}_{3,3})=M_{16}(F)$, consistent with the table below.

## Real Bott Periodicity

The recursion reduces the classification to the two definite families $\mathrm{Cl}_{n,0}$ and $\mathrm{Cl}_{0,n}$. Two of the eight cases are already visible from the recursion, and the remaining ones are computed directly.

**Theorem (Bott periodicity for Clifford algebras).** There are isomorphisms

$$
\mathrm{Cl}_{p+8,q}\cong M_{16}\bigl(\mathrm{Cl}_{p,q}\bigr)\cong \mathrm{Cl}_{p,q+8},
$$

so that the isomorphism type of $\mathrm{Cl}_{p,q}$ is unchanged by increasing $p$ or $q$ by $8$, up to tensoring with $M_{16}(F)$.

**Proof.** The rank-eight definite forms are the tensor products of four copies of $\mathrm{Cl}_{2,0}$ and of four copies of $\mathrm{Cl}_{0,2}$ respectively, and a direct computation in $M_{16}(F)$ gives

$$
\mathrm{Cl}_{8,0}\cong M_{16}(F)\cong \mathrm{Cl}_{0,8}.
$$

Explicitly, put $\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\sigma_3=\operatorname{diag}(1,-1)$ and $\tau=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, and let the four $2\times2$ factors act in four tensor slots. The matrices

$$
A_j=\sigma_3^{\otimes(j-1)}\otimes\sigma_1\otimes I^{\otimes(4-j)},\qquad B_j=\sigma_3^{\otimes(j-1)}\otimes\tau\otimes I^{\otimes(4-j)}\qquad (j=1,\dots,4)
$$

are eight real $16\times16$ matrices, pairwise anticommuting, the $A_j$ of square $+1$ and the $B_j$ of square $-1$; so they realise $\mathrm{Cl}_{4,4}$ on $F^{16}$, and the $256$ products of subsets are linearly independent, so the algebra they generate is the full matrix algebra $M_{16}(F)$, in agreement with four applications of the recursion. The product $\Omega=B_1B_2B_3B_4$ satisfies $\Omega^2=1$, anticommutes with each $B_j$, and commutes with each $A_k$, the last because $\Omega$ anticommutes with $A_k$ once for each of the four factors $B_j$; hence $A_1,\dots,A_4,\Omega B_1,\dots,\Omega B_4$ are eight pairwise anticommuting matrices of square $+1$ generating the same algebra, which gives $\mathrm{Cl}_{8,0}\cong M_{16}(F)$. Interchanging the roles of the $A_j$ and the $B_j$ — with $\Omega'=A_1A_2A_3A_4$ the eight matrices $B_1,\dots,B_4,\Omega'A_1,\dots,\Omega'A_4$ are pairwise anticommuting of square $-1$ — gives $\mathrm{Cl}_{0,8}\cong M_{16}(F)$ in the same way. Tensoring the graded decomposition with $\mathrm{Cl}_{8,0}$ gives $\mathrm{Cl}_{p+8,q}\cong\mathrm{Cl}_{p,q}\hat\otimes\mathrm{Cl}_{8,0}=M_{16}(\mathrm{Cl}_{p,q})$; the other family is identical with $\mathrm{Cl}_{0,8}$. $\square$

**Remark.** The periodicity statement is genuine over any field in which the two rank-eight algebras are matrix algebras; over a general commutative ring the corresponding statement requires the form to be a sum of hyperbolic planes and the appropriate isomorphisms of Azumaya algebras, and is a theorem of the theory over rings.

## The Two Definite Tables

The classification is now reduced to the eight values of $n$ modulo $8$ in each of the two definite families. The following tables record them; all entries are verified from the recursion $\mathrm{Cl}_{p+1,q+1}\cong M_2(\mathrm{Cl}_{p,q})$, the rank-two cases, and the periodicity $\mathrm{Cl}_{n+8,0}\cong M_{16}(\mathrm{Cl}_{n,0})$.

**The family $\mathrm{Cl}_{n,0}$.** Here $e_i^2=+1$.

| $n \bmod 8$ | $\mathrm{Cl}_{n,0}$ | division algebra | center |
|---|---|---|---|
| $0$ | $M_{2^{n/2}}(F)$ | $F$ | $F$ |
| $1$ | $M_{2^{(n-1)/2}}(F)\times M_{2^{(n-1)/2}}(F)$ | $F$ | $F\times F$ |
| $2$ | $M_{2^{n/2}}(F)$ | $F$ | $F$ |
| $3$ | $M_{2^{(n-1)/2}}(F(\sqrt{-1}))$ | $F(\sqrt{-1})$ | $F(\sqrt{-1})$ |
| $4$ | $M_{2^{(n-2)/2}}(\mathbb{H})$ | $\mathbb{H}$ | $F$ |
| $5$ | $M_{2^{(n-3)/2}}(\mathbb{H})\times M_{2^{(n-3)/2}}(\mathbb{H})$ | $\mathbb{H}$ | $F\times F$ |
| $6$ | $M_{2^{(n-2)/2}}(\mathbb{H})$ | $\mathbb{H}$ | $F$ |
| $7$ | $M_{2^{(n-1)/2}}(F(\sqrt{-1}))$ | $F(\sqrt{-1})$ | $F(\sqrt{-1})$ |

**The family $\mathrm{Cl}_{0,n}$.** Here $e_i^2=-1$.

| $n \bmod 8$ | $\mathrm{Cl}_{0,n}$ | division algebra | center |
|---|---|---|---|
| $0$ | $M_{2^{n/2}}(F)$ | $F$ | $F$ |
| $1$ | $M_{2^{(n-1)/2}}(F(\sqrt{-1}))$ | $F(\sqrt{-1})$ | $F(\sqrt{-1})$ |
| $2$ | $M_{2^{(n-2)/2}}(\mathbb{H})$ | $\mathbb{H}$ | $F$ |
| $3$ | $M_{2^{(n-3)/2}}(\mathbb{H})\times M_{2^{(n-3)/2}}(\mathbb{H})$ | $\mathbb{H}$ | $F\times F$ |
| $4$ | $M_{2^{(n-2)/2}}(\mathbb{H})$ | $\mathbb{H}$ | $F$ |
| $5$ | $M_{2^{(n-1)/2}}(F(\sqrt{-1}))$ | $F(\sqrt{-1})$ | $F(\sqrt{-1})$ |
| $6$ | $M_{2^{n/2}}(F)$ | $F$ | $F$ |
| $7$ | $M_{2^{(n-1)/2}}(F)\times M_{2^{(n-1)/2}}(F)$ | $F$ | $F\times F$ |

For example $\mathrm{Cl}_{0,1}\cong F(\sqrt{-1})$, $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, $\mathrm{Cl}_{0,3}\cong\mathbb{H}\times\mathbb{H}$, $\mathrm{Cl}_{0,4}\cong M_2(\mathbb{H})$, $\mathrm{Cl}_{0,5}\cong M_4(F(\sqrt{-1}))$, $\mathrm{Cl}_{0,6}\cong M_8(F)$, $\mathrm{Cl}_{0,7}\cong M_8(F)\times M_8(F)$, $\mathrm{Cl}_{0,8}\cong M_{16}(F)$; and $\mathrm{Cl}_{1,0}\cong F\times F$, $\mathrm{Cl}_{2,0}\cong M_2(F)$, $\mathrm{Cl}_{3,0}\cong M_2(F(\sqrt{-1}))$, $\mathrm{Cl}_{4,0}\cong M_2(\mathbb{H})$, $\mathrm{Cl}_{5,0}\cong M_2(\mathbb{H})\times M_2(\mathbb{H})$, $\mathrm{Cl}_{6,0}\cong M_4(\mathbb{H})$, $\mathrm{Cl}_{7,0}\cong M_8(F(\sqrt{-1}))$, $\mathrm{Cl}_{8,0}\cong M_{16}(F)$. Over $\mathbb{R}$ this is the classical table; the two families are the two columns of the eightfold way.

## The General Classification

The mixed cases follow from the recursion, because increasing both indices by one multiplies by a matrix algebra and leaves the difference $p-q$ unchanged.

**Theorem (the classification).** Write $n=p+q$ and $d=p-q$, and let $q=\operatorname{diag}(+1^p,-1^q)$. If $d\ge 0$ then

$$
\mathrm{Cl}_{p,q}\cong M_{2^{q}}\bigl(\mathrm{Cl}_{d,0}\bigr),
$$

and if $d<0$ then

$$
\mathrm{Cl}_{p,q}\cong M_{2^{p}}\bigl(\mathrm{Cl}_{0,-d}\bigr).
$$

Consequently $\mathrm{Cl}_{p,q}$ is determined up to isomorphism by the total dimension $2^n$ together with the class of $d$ modulo $8$.

**Proof.** If $p\ge q$, apply the recursion $q$ times to reduce $\mathrm{Cl}_{p,q}$ to $\mathrm{Cl}_{p-q,0}$: each application removes one positive and one negative generator and multiplies by $M_2$. If $q>p$, the same reduction in the other order reaches $\mathrm{Cl}_{0,q-p}$. The dependence on $d\bmod 8$ is the periodicity of the two definite tables, and the total dimension fixes the size of the matrix algebra. $\square$

**The eightfold table.** Collecting the two definite tables and the reduction gives the following complete list of types. The symbol $n$ is the total dimension and $d=p-q$.

| $d \bmod 8$ | parity of $n$ | $\mathrm{Cl}_{p,q}$ | irreducible module, over |
|---|---|---|---|
| $0$ | even | $M_{2^{n/2}}(F)$ | $F$, dimension $2^{n/2}$ |
| $1$ | odd | $M_{2^{(n-1)/2}}(F)\times M_{2^{(n-1)/2}}(F)$ | $F$, dimension $2^{(n-1)/2}$ |
| $2$ | even | $M_{2^{n/2}}(F)$ | $F$, dimension $2^{n/2}$ |
| $3$ | odd | $M_{2^{(n-1)/2}}(F(\sqrt{-1}))$ | $F(\sqrt{-1})$, dimension $2^{(n-1)/2}$ |
| $4$ | even | $M_{2^{(n-2)/2}}(\mathbb{H})$ | $\mathbb{H}$, dimension $2^{(n-2)/2}$ |
| $5$ | odd | $M_{2^{(n-3)/2}}(\mathbb{H})\times M_{2^{(n-3)/2}}(\mathbb{H})$ | $\mathbb{H}$, dimension $2^{(n-3)/2}$ |
| $6$ | even | $M_{2^{(n-2)/2}}(\mathbb{H})$ | $\mathbb{H}$, dimension $2^{(n-2)/2}$ |
| $7$ | odd | $M_{2^{(n-1)/2}}(F(\sqrt{-1}))$ | $F(\sqrt{-1})$, dimension $2^{(n-1)/2}$ |

The entries with $d\bmod 8\in\{0,2\}$ are real matrix algebras; those with $d\bmod8\in\{4,6\}$ are quaternionic matrix algebras; those with $d\bmod 8\in\{3,7\}$ are complex matrix algebras; and in the classes $d\equiv 1,5\bmod 8$ the algebra splits as a product of two isomorphic matrix algebras. The table is the algebraic content of the eightfold way, and the type of the simple algebra — the division algebra over which its irreducible module is a vector space — is

$$
F\ \ (d\equiv0,1,2\bmod8),\qquad F(\sqrt{-1})\ \ (d\equiv3,7\bmod8),\qquad \mathbb{H}\ \ (d\equiv4,5,6\bmod8),
$$

the splitting into two matrix factors being the additional information carried by the classes $d\equiv1,5$. This is the reason the Clifford algebras are said to be periodic of period eight: the type of the algebra returns to itself after eight sign changes, the matrix size absorbing an overall factor.

**Example.** In the mixed case $\mathrm{Cl}_{1,3}$ one has $n=4$, $d=-2$, so $d\bmod 8=6$ and the table gives $M_{2^{(n-2)/2}}(\mathbb{H})=M_2(\mathbb{H})$, the algebra of the Clifford layer of the biquaternion articles. Its even subalgebra is $\mathrm{Cl}_{3,0}\cong M_2(F(\sqrt{-1}))\cong\mathbb{B}$, as the recursion below shows.

## The Even Subalgebra

The even subalgebra is again a Clifford algebra of one dimension less, and the shift it induces is the second mechanism behind the eightfold way.

**Theorem.** For $p,q\ge 1$,

$$
\mathrm{Cl}^0_{p,q}\cong \mathrm{Cl}_{p,q-1}\cong \mathrm{Cl}_{q,p-1}.
$$

**Proof.** Suppose $q\ge 1$ and let $e$ be a generator of square $-1$. By the recursion for the even subalgebra proved in the previous article, $\mathrm{Cl}^0_{p,q}\cong\mathrm{Cl}(e^\perp,q)$, and $e^\perp$ has signature $(p,q-1)$. The second isomorphism follows by choosing $p\ge 1$ and a generator of square $+1$: the same computation with a generator $f$ of square $+1$ gives $\mathrm{Cl}^0_{p,q}\cong\mathrm{Cl}(f^\perp,-q)$, and $f^\perp$ has signature $(q,p-1)$ after the sign is absorbed into the form. $\square$

**The shift of type.** The even subalgebra has dimension one half that of the Clifford algebra, and its type is obtained from the eightfold table by replacing $(p,q)$ with $(p,q-1)$ (or $(q,p-1)$). In terms of the difference $d=p-q$ this replaces $d$ by $d+1$, so passing to the even part advances the eightfold class by one step. Iterating, the chain of even subalgebras

$$
\mathrm{Cl}_{p,q}\supset \mathrm{Cl}^0_{p,q}\supset \mathrm{Cl}^{00}_{p,q}\supset\cdots
$$

runs through the eight classes and returns after eight steps to a matrix algebra over the original type. This is the same period eight seen from the subalgebra side, and it is the reason the eightfold way is often stated as the periodicity of the spinor type rather than of the algebra.

## The Type of the Irreducible Module

The classification of the algebras translates directly into a classification of their modules, and it is this form that the spin representation uses.

**Definition.** Let $A=\mathrm{Cl}_{p,q}$. A **Clifford module** is a left $A$-module, together with the $\mathbb{Z}/2$-grading it inherits when $A$ is simple and the module is the irreducible one. The **type** of the module is the division algebra over which it is a vector space.

**Theorem.** Let $(V,q)$ be a non-degenerate quadratic space of dimension $n$ over a field $F$ of characteristic not $2$, with volume element $\omega$ of an orthogonal basis and $\delta=\omega^{2}=(-1)^{n(n-1)/2}q(e_1)\cdots q(e_n)\in F^{\times}$, whose class modulo squares does not depend on the basis. Then

- if $n$ is even, $\mathrm{Cl}(V,q)$ is central simple over $F$, and it has exactly one isomorphism class of irreducible module;
- if $n$ is odd and $\delta$ is not a square in $F$, the center is the quadratic field $F(\sqrt{\delta})$ and $\mathrm{Cl}(V,q)$ is central simple over that field, hence simple, and again has exactly one isomorphism class of irreducible module;
- if $n$ is odd and $\delta$ is a square in $F$, the center is $F\times F$ and $\mathrm{Cl}(V,q)\cong A\times A$ with $A$ simple; there are then exactly two isomorphism classes of irreducible module, of the same dimension over the same division algebra, exchanged by the volume element.

In the simple cases the algebra is $M_k(D)$ with $k$ and the division algebra $D$ read from the eightfold table, and the irreducible module is $D^k$. Over $\mathbb{R}$ the second case is exactly $d=p-q\equiv3,7\bmod 8$, where $D=\mathbb{C}$, and the third is $d\equiv1,5\bmod 8$, where the two irreducible modules are those of the two factors; this is why the table displays a single matrix algebra in the classes $3,7$ and a product in the classes $1,5$.

**Proof.** For $n$ even the volume element anticommutes with every generator and the center is $F$; for $n$ odd the volume element commutes with every generator, so the center is the subalgebra $F[\omega]\cong F[x]/(x^{2}-\delta)$, which is a field when $\delta\notin F^{2}$ and is $F\times F$ when $\delta\in F^{2}$. An algebra whose center is a field and which has no proper nonzero two-sided ideal is central simple over that field, and Artin–Wedderburn then gives the uniqueness of its simple module. In the split case the two central idempotents $\tfrac12(1\pm\omega/\sqrt{\delta})$ exhibit $\mathrm{Cl}(V,q)$ as the product of the two ideals they generate; each factor is simple by the same argument, and the grade involution, which negates $\omega$ because $n$ is odd, is an isomorphism between the two factors, so their simple modules have the same dimension. $\square$

**The spinor module over $\mathbb{R}$.** Over $F=\mathbb{R}$ the type $D$ is one of $\mathbb{R},\mathbb{C},\mathbb{H}$, and the real dimension of the irreducible module is $k\dim_{\mathbb{R}}D$. For the definite forms these dimensions are the classical ones of the spin representations, and they are computed from the table: for $\mathrm{Cl}_{0,n}$ with $n\equiv 0\bmod 8$ the module is real of dimension $2^{n/2}$; with $n\equiv 1\bmod 8$ it is complex of dimension $2^{(n-1)/2}$; with $n\equiv 2\bmod 8$ it is quaternionic of dimension $2^{(n-2)/2}$; and so on around the eight cases. The pattern of dimensions and types is the "eightfold way" in the sense of the different kinds of spinor, and the reality conditions that distinguish them are not covered here.

## Complex Periodicity

Complexification forgets the signature, and the resulting classification is periodic of period two. For completeness, and to display the difference from the real case, the statement is repeated here in the conventions of this category.

**Theorem.** Let $\mathbb{C}\mathrm{l}_n$ be the complex Clifford algebra of an $n$-dimensional non-degenerate complex quadratic form. Then

$$
\mathbb{C}\mathrm{l}_{n+2}\cong \mathbb{C}\mathrm{l}_n\otimes_{\mathbb{C}} M_2(\mathbb{C}),
$$

and

$$
\mathbb{C}\mathrm{l}_{2m}\cong M_{2^m}(\mathbb{C}), \qquad \mathbb{C}\mathrm{l}_{2m+1}\cong M_{2^m}(\mathbb{C})\times M_{2^m}(\mathbb{C}).
$$

**Proof.** Over $\mathbb{C}$ the rank-two form is $\mathbb{C}\mathrm{l}_2\cong M_2(\mathbb{C})$, and the same explicit construction as for $\mathrm{Cl}_{p+1,q+1}$, carried out over $\mathbb{C}$, gives the stabilisation $\mathbb{C}\mathrm{l}_{n+2}\cong M_2(\mathbb{C}\mathrm{l}_n)$: the generators $e_i$ of $\mathbb{C}\mathrm{l}_n$ map to $e_i\sigma_1$, and the two new generators to $\sigma_3$ and $\tau$, with the same verification of the relations. The even case follows by induction from $\mathbb{C}\mathrm{l}_0=\mathbb{C}$ and $\mathbb{C}\mathrm{l}_2=M_2(\mathbb{C})$; the odd case from $\mathbb{C}\mathrm{l}_1=\mathbb{C}\times\mathbb{C}$. $\square$

**Remark.** The real classification is not the restriction of the complex one, because the complexification of $\mathrm{Cl}_{n,0}$ and of $\mathrm{Cl}_{0,n}$ coincide. Period two is what survives of period eight after the sign distinction is forgotten, and the two real forms of a complex Clifford algebra are the two real quadratic spaces of the corresponding signature class. The relation between the periodicities is exactly the relation between the complex and the real forms of a matrix algebra, and it is the algebraic origin of the eightfold way.

## Summary

The Clifford algebras satisfy two periodicity theorems. The graded tensor product decomposition $\mathrm{Cl}_{p+r,q+s}\cong\mathrm{Cl}_{p,q}\hat\otimes\mathrm{Cl}_{r,s}$, together with the rank-eight identifications $\mathrm{Cl}_{8,0}\cong\mathrm{Cl}_{0,8}\cong M_{16}(F)$, gives real Bott periodicity:

$$
\mathrm{Cl}_{p+8,q}\cong M_{16}(\mathrm{Cl}_{p,q})\cong \mathrm{Cl}_{p,q+8}.
$$

The recursion $\mathrm{Cl}_{p+1,q+1}\cong M_2(\mathrm{Cl}_{p,q})$ reduces the general classification to the two definite families, and an orthogonal direct sum decomposition reduces $\mathrm{Cl}_{p,q}$ to $M_{2^{\min(p,q)}}$ over the definite algebra $\mathrm{Cl}_{|p-q|,0}$ or $\mathrm{Cl}_{0,|p-q|}$. The type is therefore governed by $d=p-q$ modulo $8$ — the parity of $n=p+q$ being determined by it — and the eight classes form the eightfold way: real matrix algebras for $d\equiv0,2$, quaternionic for $d\equiv4,6$, complex for $d\equiv3,7$, and split into two factors for $d\equiv1,5$.

The even subalgebra satisfies $\mathrm{Cl}^0_{p,q}\cong\mathrm{Cl}_{p,q-1}\cong\mathrm{Cl}_{q,p-1}$; passing to it advances the eightfold class by one, so the spinor type is periodic of period eight. Over a complex ground field the classification collapses to period two, with $\mathbb{C}\mathrm{l}_{2m}\cong M_{2^m}(\mathbb{C})$ and $\mathbb{C}\mathrm{l}_{2m+1}\cong M_{2^m}(\mathbb{C})\times M_{2^m}(\mathbb{C})$. The irreducible module of a simple Clifford algebra is unique, and its dimension and division algebra are read off the eightfold table; this is the module that carries the spin representation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | Field of characteristic not $2$ |
| $q=\operatorname{diag}(+1^p,-1^q)$ | Real signature quadratic form |
| $\mathrm{Cl}_{p,q}$ | Clifford algebra of the signature form, $p$ positive and $q$ negative squares |
| $\mathrm{Cl}^0_{p,q}$ | Even subalgebra |
| $\hat\otimes$ | Graded tensor product, $\mathrm{Cl}_{p,q}\hat\otimes\mathrm{Cl}_{r,s}\cong\mathrm{Cl}_{p+r,q+s}$ |
| $n=p+q$ | Total dimension |
| $d=p-q$ | Signature difference, governing the eightfold class |
| $\mathbb{D}=F\times F$ | Split complex algebra |
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{B}$ | Biquaternion algebra, $\cong\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$ |
| $M_k(D)$ | Matrix algebra of size $k$ over the division algebra $D$ |
| $\mathbb{C}\mathrm{l}_n$ | Complex Clifford algebra, periodic of period two |
| $\omega=e_1\cdots e_n$ | Volume element |
| $\delta=\omega^{2}=(-1)^{n(n-1)/2}q(e_1)\cdots q(e_n)$ | Square of the volume element; decides whether the center is a field or $F\times F$ when $n$ is odd |
| $\mathrm{Cl}_{8,0}\cong\mathrm{Cl}_{0,8}\cong M_{16}(F)$ | Bott periodicity algebra |





## Further Reading

- Michael F. Atiyah, Raoul Bott and Arnold Shapiro, "Clifford modules," *Topology* **3** (1964), supplement 1, 3–38, for the original periodicity theorem and the eightfold classification of Clifford modules.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the classification tables and the periodicities.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the eightfold way and its relation to the classical groups.
- Dale Husemoller, *Fibre Bundles* (Springer, 3rd ed. 1994), for the use of Clifford-module periodicity in topological K-theory.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the quadratic-space framework that organises the classification.
