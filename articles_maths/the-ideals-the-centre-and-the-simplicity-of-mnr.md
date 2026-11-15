# __The Ideals, the Centre and the Simplicity of $M_n(\mathbb{R})$__

## Introduction

**The algebra $M_n(\mathbb{R})$ has exactly two two-sided ideals, its centre is $\mathbb{R}\mathrm{I}$, and every automorphism and every derivation is inner; the same statements hold over $\mathbb{C}$, and the proofs over $\mathbb{R}$ are not weaker.** The one-sided ideals are richer, and they are the objects that the Peirce decomposition uses.

The article proves the simplicity from the matrix units, computes the centre, classifies the right and left ideals by subspaces of $\mathbb{R}^{n}$ with their dimensions, identifies the minimal ones with the rows and the columns, proves that every automorphism and every derivation is inner, records the single irreducible module, and contrasts the algebra with the triangular algebra $UT_n$, which is not simple and has a radical. It assumes *The Matrix Algebra $M_n(\mathbb{R})$*. It defers the corners to *The Peirce Decomposition in $n$ Dimensions over $\mathbb{R}$*.

## The Two-Sided Ideals

**Definition.** A two-sided ideal is a real subspace $J\subseteq M_n(\mathbb{R})$ with $AJ\subseteq J$ and $JA\subseteq J$ for every $A$. The algebra is **simple** when its only two-sided ideals are $0$ and itself.

**Theorem.** $M_n(\mathbb{R})$ is simple.

*Proof.* Let $J\ne0$ and pick $0\ne X\in J$ with $X_{kl}\ne0$. For all $i,j$,

$$
E_{ik}XE_{lj}=X_{kl}E_{ij}\in J,
$$

so $E_{ij}\in J$ for every pair, because $X_{kl}\ne0$ is a nonzero real scalar and $J$ is a real subspace. The $n^{2}$ matrix units span the algebra, so $J=M_n(\mathbb{R})$.

**The proof uses only that the scalar $X_{kl}$ is invertible.** Over any field the same line gives simplicity, so simplicity is not a real phenomenon. What is a real phenomenon is the classification of the *forms* of the algebra, which is *The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*.

**A consequence: no decomposition into two-sided ideals exists.** When the algebra is later written as a sum of corner subspaces $A_{kl}=P_kM_nP_l$, that sum is a decomposition of the vector space and a block-diagonal subalgebra, never a decomposition into ideals. The Peirce decomposition is not a Wedderburn decomposition into simple summands.

## The Centre

**Theorem.** The centre is $\mathbb{R}\mathrm{I}$.

*Proof.* Let $Z$ commute with every matrix unit. Then $ZE_{ij}=E_{ij}Z$. The entry $(i,j)$ of the left side is $Z_{ii}$ and of the right side is $Z_{jj}$, so all diagonal entries are equal, say $\lambda$. The entry $(i,l)$ with $l\ne i$ of the left side is $0$ for $j=i$; comparing the off-diagonal entries for $i\ne j$ gives $Z_{il}=0$ when $i\ne l$. So $Z=\lambda\mathrm{I}$. Conversely a scalar matrix commutes with everything.

**Central simplicity.** The algebra is simple and its centre is the base field, so it is a **central simple algebra** over $\mathbb{R}$. The dimension is $n^{2}$, so the degree is $n$, and the algebra is the split one of degree $n$.

**The centre is one-dimensional over $\mathbb{R}$ and therefore two-dimensional over $\mathbb{R}$ when read in the complex algebra.** Inside $M_n(\mathbb{C})$ the centre of the complex algebra is $\mathbb{C}\mathrm{I}$, of real dimension two; the centre of $M_n(\mathbb{R})$ is $\mathbb{R}\mathrm{I}$, of real dimension one. So the centre doubles on complexification, exactly like the algebra.

## Right and Left Ideals

**A right ideal is the set of matrices whose image lies in a fixed subspace.** Let $W\subseteq\mathbb{R}^{n}$ be a subspace and put

$$
J_W=\{X:X(\mathbb{R}^{n})\subseteq W\}.
$$

Then $J_W$ is a right ideal, because $(XA)(\mathbb{R}^{n})=X(A\mathbb{R}^{n})\subseteq X(\mathbb{R}^{n})\subseteq W$. Conversely, if $J$ is a right ideal and $W=\sum_{X\in J}\operatorname{im}X$, then $J=J_W$: the inclusion $J\subseteq J_W$ is the definition of $W$, and the reverse holds because $W$ is spanned by images of elements of $J$ and $J$ is closed under right multiplication by the projections onto the summands.

**The dimension of $J_W$ is $n\dim W$.** Choosing a basis adapted to $W$, the matrices of $J_W$ are those whose last $n-\dim W$ rows vanish, so the free entries are $\dim W$ per column.

**A left ideal is the set of matrices whose kernel contains a fixed subspace.** For $U\subseteq\mathbb{R}^{n}$ put

$$
I_U=\{X:U\subseteq\ker X\}.
$$

Then $I_U$ is a left ideal, because $\ker(AX)\supseteq\ker X$. Conversely every left ideal is of this form, with $U=\bigcap_{X\in J}\ker X$. Its dimension is $n(n-\dim U)$, the matrices whose first $\dim U$ columns vanish in adapted coordinates.

**The two classifications are exchanged by the transpose.** Transposition sends a right ideal to a left ideal and $J_W$ to $I_W$, since $\operatorname{im}X\subseteq W$ is equivalent to $W\subseteq\ker X^{\mathsf T}$. So the asymmetry between the two lists is only apparent.

**At $n=2$ the count is small enough to write out.** The right ideals are $0$, the three-dimensional set of matrices with image in a line, and the whole algebra. The left ideals are $0$, the three-dimensional set of matrices vanishing on a line, and the whole algebra. There are as many of each as there are lines in $\mathbb{R}^{2}$, that is a circle's worth.

## The Minimal Ideals Are the Rows and the Columns

**The minimal nonzero right ideals are the columns of the Peirce array.** Take $W$ of dimension one, spanned by $v$. Then $J_W=\{v\ell:\ell\in(\mathbb{R}^{n})^{*}\}$, of dimension $n$, and no proper nonzero right ideal sits inside it, because a subspace of $W$ of dimension less than one is zero. So the minimal right ideals are the sets $v\ell$, one for each line of $\mathbb{R}^{n}$.

**The minimal nonzero left ideals are the rows.** Take $U$ of codimension one. Then $I_U=\{v\ell:U\subseteq\ker(v\ell)\}$, again of dimension $n$, and minimal.

**In a Peirce basis these are the rows and the columns of the matrix of coordinates.** With $E_{kl}=v_k\ell_l$, the minimal right ideal for the line $V_k$ is spanned by $E_{k1},\dots,E_{kn}$, the $k$-th row; the minimal left ideal for the hyperplane $\bigoplus_{l\ne k}V_l$ is spanned by $E_{1k},\dots,E_{nk}$, the $k$-th column. So the minimal one-sided ideals are exactly the rows and the columns of the Peirce array, which is the statement the Peirce articles use.

**The algebra is the sum of its minimal right ideals, and the sum is direct only in a coarse sense.** $M_n(\mathbb{R})=\bigoplus_k(\text{row }k)$, of dimension $n^{2}=n\cdot n$, and each summand is minimal as a right ideal. The same space is also a left ideal only for $n=1$; for $n\ge2$ a row is not a left ideal.

## Automorphisms and Derivations

**Theorem (Skolem–Noether over $\mathbb{R}$).** Every automorphism of $M_n(\mathbb{R})$ is inner: $\varphi=\operatorname{Ad}_S$ for some $S\in\mathrm{GL}_n(\mathbb{R})$, unique up to a nonzero scalar.

*Proof.* Let $V=\mathbb{R}^{n}$ and let $\varphi$ act on the algebra. The algebra is $\operatorname{End}(V)$, so $\varphi$ carries the minimal right ideals to minimal right ideals; these are the rank-one maps $v\ell$. So $\varphi$ permutes the lines of $V$ by a map induced by a linear $S$, and $\varphi$ agrees with $\operatorname{Ad}_S$ on every rank-one map, hence on the whole algebra because the rank-one maps span it. If $\operatorname{Ad}_S=\operatorname{Ad}_{S'}$ then $S^{-1}S'$ commutes with everything, hence is a scalar.

**Theorem.** Every derivation of $M_n(\mathbb{R})$ is inner: $D=\operatorname{ad}_A$ with $\operatorname{ad}_A(X)=AX-XA$ for some $A$, unique up to a scalar.

*Proof.* A derivation is determined by its values on a generating set, and the matrix units generate. Write $D(E_{ij})=\sum_{p,q}c^{ij}_{pq}E_{pq}$ and impose $D(E_{ij}E_{kl})=\delta_{jk}D(E_{il})$. The resulting relations force $D(E_{ij})=E_{ij}B-BE_{ij}$ for the matrix $B=\sum_p D(E_{pj})E_{jp}$ with $j$ fixed; then $D=\operatorname{ad}_B$ on the units, hence everywhere. Two inner derivations agree exactly when the matrices differ by a scalar.

**The dimension of the derivation algebra is $n^{2}-1$.** The map $A\mapsto\operatorname{ad}_A$ is linear with kernel the centre $\mathbb{R}\mathrm{I}$, of dimension one, so

$$
\dim\operatorname{Der}\bigl(M_n(\mathbb{R})\bigr)=n^{2}-1,
$$

which is also the dimension of $\mathfrak{sl}_n(\mathbb{R})$ and of the Lie algebra of $PGL_n(\mathbb{R})$.

**These statements hold over any field, and they are what makes the real and the complex categories run in parallel.** The proofs use only the matrix units and the invertibility of scalars. The real content of the real category is elsewhere: in the involution, the spectrum and the form.

## The Modules

**The algebra has exactly one irreducible module up to isomorphism, namely $\mathbb{R}^{n}$.** A module is a real vector space with an action of the algebra; an irreducible one is a nonzero space with no invariant subspace. Since the algebra is the full endomorphism algebra of $\mathbb{R}^{n}$, any nonzero vector generates the whole space under the action: the rank-one maps send it to any other vector. So an irreducible module is spanned by one vector and is a quotient of $\mathbb{R}^{n}$, hence isomorphic to it.

**Every module is a direct sum of copies of $\mathbb{R}^{n}$.** A module is a vector space $V$ with an algebra map $M_n(\mathbb{R})\to\operatorname{End}(V)$, and such a map is determined by the images of the matrix units, which are the projections onto the summands of a decomposition of $V$ into $n$ isomorphic pieces. So $V\cong(\mathbb{R}^{n})^{\oplus m}$ and $M_n(\mathbb{R})$ is a simple algebra with a single simple module.

**The module picture explains the one-sided ideals.** A right ideal is a submodule of the regular module, and the regular module is $\mathbb{R}^{n}\otimes(\mathbb{R}^{n})^{*}$; the minimal right ideals are the summands $\mathbb{R}^{n}\otimes\ell$ for a line $\ell$ in the dual. This is the tensor form of §*The Minimal Ideals Are the Rows and the Columns*.

## The Contrast with $UT_n$

**The triangular algebra is not simple, and its radical is explicit.** Let $UT_n$ be the algebra of upper triangular matrices, of dimension $n(n+1)/2$. Its strictly upper triangular part

$$
\mathfrak{n}=\{N\in UT_n:N_{ii}=0\}
$$

is a two-sided ideal, nilpotent of index $n$, and the quotient $UT_n/\mathfrak{n}$ is the diagonal algebra $\mathbb{R}^{n}$, which is commutative. So $UT_n$ has a nonzero nilpotent ideal and is not semisimple.

**At $n=3$ the ideal lattice is small and visible.** $UT_3$ has dimension $6$ and contains the ideals $0$, $\mathfrak{n}$ of dimension $3$, the span of $E_{13}$ of dimension $1$, the span of $E_{12},E_{13}$ and the span of $E_{23},E_{13}$, each of dimension $2$, and the whole algebra. The nilpotent radical is $\mathfrak{n}$.

**The two algebras have the same dimension of diagonal but different products.** $\operatorname{Sym}_n$ has dimension $n(n+1)/2$, the same as $UT_n$, and it is not an algebra under the matrix product; $UT_n$ is an algebra and is not simple. *The Triangular Decomposition $h\oplus n_+\oplus n_-$* and *$UT_n$ as a Linear Model of $\operatorname{Sym}_n$: Same Space, Wrong Product* make the comparison exact.

## Summary

$M_n(\mathbb{R})$ is simple and its centre is $\mathbb{R}\mathrm{I}$, so it is a central simple algebra of degree $n$. The right ideals are the sets of matrices with image in a fixed subspace, of dimension $n\dim W$, and the left ideals are the sets vanishing on a fixed subspace, of dimension $n(n-\dim U)$; the minimal ones are the rows and the columns of a Peirce basis. Every automorphism and every derivation is inner, with $\dim\operatorname{Der}=n^{2}-1$. There is one irreducible module, $\mathbb{R}^{n}$, and every module is a sum of copies of it. The triangular algebra $UT_n$ of the same dimension $n(n+1)/2$ as $\operatorname{Sym}_n$ is not simple and has the strictly upper triangular part as nilpotent radical.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J_W$ | the right ideal of matrices with image in $W$ |
| $I_U$ | the left ideal of matrices vanishing on $U$ |
| $\operatorname{Ad}_S(X)=SXS^{-1}$ | the inner automorphism |
| $\operatorname{ad}_A(X)=AX-XA$ | the inner derivation |
| $\operatorname{Der}(A)$ | the Lie algebra of derivations, of dimension $n^{2}-1$ |
| $UT_n$, $\mathfrak{n}$ | the upper triangular algebra and its strictly upper triangular radical |

## Further Reading

- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for simple rings, the Skolem–Noether theorem and the density theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the ideals of a matrix algebra and the Peirce decomposition.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the algebra, its centre and its matrix units.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-mnc.html), for the complex case.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the ideal lattice at $n=3$.
