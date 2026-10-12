# __The Realification and the Effect of the Change of Scalars on the Split-Complex Numbers__

## Introduction

The split-complex algebra is one ring and it carries two scalar readings: the reading over itself, in which it is a module of rank one on the ring $\mathbb{D}$, and the reading over $\mathbb{R}$, in which it is a two-dimensional real algebra. The passage from the first to the second is the realification, the same construction that carries an algebra from its complex reading to its real reading, and this article reads that construction on $\mathbb{D}$: the doubling of the dimension, the **split complex structure** $J$, which is the multiplication by $j$ with $J^2=+\mathrm{id}$, the two kinds of real-linear map and the two block shapes they give, the realification of the two forms, and the dictionary of the statements that change and the statements that do not.

The general construction is *The Realification and the Effect of the Change of Scalars*, which owns the definitions of the realification of a vector space, of a linear map and of a form, the criteria $TJ=JT$ and $SJ=-JS$, the two realification rules and the four effects; none of that is reproved here, it is read on $\mathbb{D}$. The forms are *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, the article preceding this one, and their reading on the subspaces is *Remarkable Subspaces of the Split-Complex Numbers and the Two Forms*. The complex prototype, the first rung, is *The Realification and the Effect of the Change of Scalars* of the chapter `## Complex Numbers`.

**The reading fixed here.** The bar is the conjugation $j\mapsto-j$ and ${}^{*}=\bar{\cdot}$; the algebra is commutative. In this article $A=a+ja'$ and $C=c+jc'$ are elements, so $B$, $H$ and $N$ name forms and norms only, and the structure is $J$, the multiplication by $j$.

## The Two Scalar Interpretations and the Doubling

Read over itself, $\mathbb{D}$ is a free module of rank one on the basis $1$: every element is $\lambda\cdot1$ with $\lambda\in\mathbb{D}$, and the only $\mathbb{D}$-submodules are the ideals. Read over $\mathbb{R}$, it is a real vector space of dimension two on the basis $1,j$. The passage from the first reading to the second is restriction of scalars, and the dimension doubles:

$$
\dim_{\mathbb{D}}\mathbb{D}=1,
\qquad
\dim_{\mathbb{R}}\mathbb{D}=2,
$$

the real basis being $1,j$. The general proposition that the dimension doubles holds as stated, with a $\mathbb{D}$-basis $e_1$ giving the $\mathbb{R}$-basis $e_1,je_1$; the difference from the complex prototype is that the scalar algebra is the ring $\mathbb{D}$ rather than a field, so that the module theory over it is the theory of the ideals, not the theory of a vector space over a field. The rank-one module is $\mathbb{D}$ itself, and its proper non-zero submodules are the two idempotent lines.

## The Split Complex Structure

The multiplication by $j$ is the real-linear map

$$
J:\mathbb{D}\longrightarrow\mathbb{D},
\qquad
J(A)=jA,
$$

and the whole of the difference from the complex prototype is in its square:

$$
J^2=+\mathrm{id}_{\mathbb{D}},
$$

against $J^2=-\mathrm{id}_{\mathbb{C}}$ for the multiplication by $i$ on $\mathbb{C}$. The general construction names the operator of square $-\mathrm{id}$ a **complex structure**; the operator of square $+\mathrm{id}$ is a **product structure**, and it is the second kind that the split sign produces.

**Proposition (the structure is diagonalisable, and splits the algebra).** The operator $J$ is diagonalisable over $\mathbb{R}$, with eigenvalues $+1$ and $-1$ and eigenlines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, and

$$
\mathbb{D}=\mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2.
$$

**Proof.** In the basis $1,j$ the matrix of $J$ is $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, with eigenvalues the roots of $t^2-1=(t-1)(t+1)$, namely $+1$ and $-1$; the $+1$ eigenline is $\mathbb{R}(1+j)=\mathbb{R}\Pi_1$ and the $-1$ eigenline is $\mathbb{R}(1-j)=\mathbb{R}\Pi_2$, and the two eigenvectors are independent, so the operator is diagonalisable.

So the split complex structure does not make the space into a complex line; it **splits it into two real lines**, the two eigenspaces, which is the idempotent decomposition. On the complex field the corresponding operator has no real eigenvalue and no invariant real line; here the two eigenlines are real and are the two minimal ideals. The invariant subspaces of $J$ are exactly the real subspaces closed under $J$, and they are $\{0\}$, $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$ and $\mathbb{D}$: the two minimal ideals with the zero and the whole, where on $\mathbb{C}$ the invariant subspaces are only $\{0\}$ and $\mathbb{C}$.

## The Two Kinds of Real-Linear Map

The criteria of the general construction read: a real-linear map is $\mathbb{D}$-linear exactly when it commutes with the structure, and conjugate-$\mathbb{D}$-linear exactly when it anticommutes,

$$
T J=J T
\quad\text{for $\mathbb{D}$-linear }T,
\qquad
S J=-J S
\quad\text{for conjugate-}\mathbb{D}\text{-linear }S .
$$

On $\mathbb{D}$ the structure is $J=\operatorname{diag}(1,-1)$ in the eigenbasis $\Pi_1,\Pi_2$, so the two criteria become two block shapes, and they are the diagonal and the anti-diagonal matrix:

$$
TJ=JT\iff T=\begin{pmatrix}t_1&0\\0&t_2\end{pmatrix},
\qquad
SJ=-JS\iff S=\begin{pmatrix}0&s_1\\s_2&0\end{pmatrix},
$$

with real $t_1,t_2,s_1,s_2$. The commuting maps are the multiplications by an element of $\mathbb{D}$, $T=\lambda\,\mathrm{id}$, $\lambda=\tfrac12(t_1+t_2)+\tfrac12(t_1-t_2)j$, a family of real dimension two isomorphic to $\mathbb{D}$ itself; the anticommuting maps are the conjugate-$\mathbb{D}$-linear maps, $S(A)=\lambda\bar A$, also of real dimension two. The two families span the four-dimensional space of $\mathbb{R}$-linear maps,

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{D})=\operatorname{End}_{\mathbb{D}}(\mathbb{D})\oplus\operatorname{Ant}_{\mathbb{D}}(\mathbb{D}),
$$

each summand of real dimension two. The shapes are the split reading of the complex blocks: there the commuting maps had the block $\begin{pmatrix}u&-v\\v&u\end{pmatrix}$ and the anticommuting ones $\begin{pmatrix}u&v\\v&-u\end{pmatrix}$, with real $u,v$; here the same two shapes, read in the eigenbasis, become the diagonal and the anti-diagonal, because $J$ has real eigenvalues rather than the pair $+i,-i$.

**Remark (the Galois twist).** The real-algebra automorphisms of $\mathbb{D}$ are the identity and the bar, and the bar is conjugate-$\mathbb{D}$-linear, since $\overline{jA}=-j\bar A$. The automorphism group is therefore $\mathbb{Z}/2=\{1,\bar{\cdot}\}$, the group of the involution, and it is the conjugate-linear coset of the identity, exactly as the general construction describes the enlargement of the automorphisms by the Galois twist. On the complex field the corresponding twist is the conjugation of $\mathbb{C}$ over $\mathbb{R}$; here it is the conjugation of $\mathbb{D}$, which is the same involution that generates the whole of the remarkable-subspace content of the algebra.

## The Two Realification Rules and the Two Signatures

The realification of a form is its real part, read on $\mathbb{D}$ as a two-dimensional real space, and the two kinds of form realify by two rules: a form whose structure-action is $-1$ realifies to the **split signature** $(n,n)$, and a form whose structure-action is $+1$ realifies by **doubling its inertia**. The two signs are the ones of the proposition of *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*,

$$
B(JA,JC)=+B(A,C),
\qquad
H(JA,JC)=-H(A,C),
$$

so on $\mathbb{D}$ **the two forms take the two rules in the order opposite to the complex one**. The bilinear form has the $+1$ action, so it is the Hermitian rule that applies to it, and its realification is the definite form of signature $(2,0)$; the Hermitian form has the $-1$ action, so it is the bilinear rule that applies, and its realification is the indefinite form of signature $(1,1)$. The general corollary, read on the two forms, is

| form | rule on $\mathbb{D}$ | realified signature on $\mathbb{D}$ | realified signature on $\mathbb{C}$ |
|---|---|---|---|
| $B(A,C)=AC$ | Hermitian rule, doubling | $(2,0)$, definite | $(1,1)$, indefinite |
| $H(A,C)=A\overline{C}$ | bilinear rule, split | $(1,1)$, indefinite | $(2,0)$, definite |

The split sign exchanges the two signatures with respect to the complex prototype: the form that was indefinite there is definite here, and the form that was definite there is indefinite here. This is the local statement of the contrast the whole chapter turns on, and the reason the split complex structure, a product structure of square $+\mathrm{id}$, is the opposite reading of the complex structure of square $-\mathrm{id}$.

## The Dictionary of the Split Statements Against the Real Ones

The general construction distinguishes a statement **about the ring**, which is evaluated on the addition, the product and the identity alone and is unchanged by the passage, from a statement **about the scalars**, which names the field of scalars, a dimension, a tensor product or a scalar-linearity and may change. Read on $\mathbb{D}$, the dictionary is this.

| object or statement | over the ring $\mathbb{D}$ | over the reals $\mathbb{R}$ |
|---|---|---|
| the space | $\mathbb{D}$ as a module of rank $1$ over itself | the real plane on $1,j$ |
| a $\mathbb{D}$-linear map | $T=\lambda\,\mathrm{id}$, $\lambda\in\mathbb{D}$ | commutes with $J$, diagonal shape |
| a conjugate-$\mathbb{D}$-linear map | $S(A)=\lambda\bar A$ | anticommutes with $J$, anti-diagonal shape |
| the invariant subspaces of $J$ | the ideals | $\{0\}$, $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$, $\mathbb{D}$ |
| a bilinear form | $B(A,C)=AC$, rank $1$ | realified signature $(2,0)$ |
| a Hermitian form | $H(A,C)=A\overline{C}$, rank $1$ | realified signature $(1,1)$ |
| a subring or an ideal | the two ideals $\mathbb{R}\Pi_{1,2}$ | the same two real lines |
| the zero divisors, the idempotents | $\Pi_1\Pi_2=0$; $\Pi_{1,2}$ | unchanged (a statement about the ring) |
| the norm and its sign | $N=a^2-a'^2$, indefinite | unchanged (a statement about the ring) |

The two rows that matter are the last two. The zero divisors, the idempotents, the ideals and the sign of the norm are statements about the ring: they are formulated with the product and the elements alone, and they have the same truth value in the two readings. The dimension, the scalar-linearity of a map, the two block shapes and the two realified signatures are statements about the scalars: they change, and the change is the doubling of the dimension and the exchange of the two rules. This is the structural content of the passage, and it is the same content the general construction carries, with the split sign in place of the complex one.

## Comparison with the Complex Case

On $\mathbb{C}$ the structure $J$ is the multiplication by $i$, of square $-\mathrm{id}$: a complex structure, irreducible over $\mathbb{R}$, with no real eigenvalue and no invariant real line, whose field of scalars is a field and whose Hermitian form is definite of signature $(2,0)$. On $\mathbb{D}$ the structure $J$ is the multiplication by $j$, of square $+\mathrm{id}$: a product structure, diagonalisable over $\mathbb{R}$, with the two real eigenvalues $\pm1$ and the two invariant real lines $\mathbb{R}\Pi_{1,2}$, whose scalar algebra is the ring $\mathbb{R}\oplus\mathbb{R}$ and whose Hermitian form is indefinite of signature $(1,1)$.

The passage therefore has the same skeleton in the two cases and two different fillings. The skeleton is the same: the doubling of the dimension, the two kinds of real-linear map, the two block shapes, the two realification rules, and the general dictionary. The filling differs in the sign of the square of the structure, and that one sign flips the answer to three questions at once: whether the structure is irreducible over $\mathbb{R}$ or splits, whether the Hermitian form is definite or indefinite, and whether the surviving ring is a field or a ring with zero divisors. The split-complex numbers are thus the second rung of the ladder in which the complex field is the first, and the only difference between the two rungs is the sign that the whole chapter reads.

## Summary

The split-complex algebra carries two scalar readings, over the ring $\mathbb{D}$ and over $\mathbb{R}$, and the passage between them doubles the dimension, from rank one over $\mathbb{D}$ to dimension two over $\mathbb{R}$. The structure of the passage is the multiplication by $j$, $J^2=+\mathrm{id}$, a product structure rather than a complex structure: it is diagonalisable over $\mathbb{R}$ with the two eigenlines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, it splits the algebra into its two minimal ideals, and its invariant subspaces are the ideals where the complex structure has only the trivial two. The two kinds of real-linear map are the commuting, $\mathbb{D}$-linear maps $\lambda\,\mathrm{id}$ and the anticommuting, conjugate-$\mathbb{D}$-linear maps $\lambda\bar{\cdot}$, of real dimension two each, with the diagonal and the anti-diagonal block shapes in the eigenbasis, and the Galois twist is the bar.

The two forms realify by the two general rules, taken in the order opposite to the complex one because the structure has square $+\mathrm{id}$: the bilinear form $B$ takes the Hermitian rule and realifies to the definite $(2,0)$, and the Hermitian form $H$ takes the bilinear rule and realifies to the indefinite $(1,1)$. The split sign thus exchanges the two signatures with respect to the complex prototype, and the statements about the ring — the zero divisors, the idempotents, the ideals, the sign of the norm — are the ones the passage leaves unchanged. The whole difference between the split rung and the complex rung is the sign of the square of the structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ | the split-complex ring, $j^2=+1$ |
| $J$ | multiplication by $j$, $J^2=+\mathrm{id}$, the split complex structure |
| $\Pi_{1,2}=\tfrac12(1\pm j)$ | the eigenlines of $J$, the two minimal ideals |
| $\operatorname{End}_{\mathbb{D}}(\mathbb{D})$ | the commuting maps, $T=\lambda\,\mathrm{id}$ |
| $\operatorname{Ant}_{\mathbb{D}}(\mathbb{D})$ | the anticommuting maps, $S(A)=\lambda\bar A$ |
| $B$, $H$ | the two forms, of realified signatures $(2,0)$ and $(1,1)$ |
| $N(A)=a^2-a'^2$ | the norm, a statement about the ring |

## Further Reading

- Nathan Jacobson, *Basic Algebra II* (W. H. Freeman, 2nd ed. 1989), for restriction and extension of scalars and the complex structure of a real vector space.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, Colloquium Publications 44, 1998), for structures of square $+1$ and $-1$ and the forms attached to them.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the realification of bilinear and Hermitian forms and their signatures.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the endomorphism ring of a module, the Galois twist and the automorphisms of a two-dimensional real algebra.
