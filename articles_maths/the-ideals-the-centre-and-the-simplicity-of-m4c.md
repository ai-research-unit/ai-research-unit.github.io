# __The Ideals, the Centre and the Simplicity of $M_4(\mathbb{C})$__

## Introduction

**The centre of $M_4(\mathbb{C})$ is the line of scalars, the only two-sided ideals are $0$ and the whole algebra, and the algebra is therefore central simple of degree four and index one; the two Kronecker factors are subalgebras and not ideals.**

The article proves the two-sided simplicity through the matrix units, identifies the one-sided ideals as column and row spaces attached to subspaces of $\mathbb{C}^{4}$, records the central-simple invariants, and explains why the Kronecker factorisation $M_4=M_2\otimes M_2$ does not contradict simplicity: a tensor factor is a subalgebra, and a subalgebra is not an ideal.

It assumes *The Matrix Algebra $M_4(\mathbb{C})$* for the units and the trace, and *The Kronecker Factorisation of $M_4(\mathbb{C})$ into $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$* for the tensor reading. The case $n=2$ is *The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$*. The finite-dimensional theory is *The Structure of Semisimple Algebras*.

## The Centre

**Proposition.** A matrix $Z$ is central exactly when it is a scalar, so the centre is $\mathbb{C}\mathrm I_4$ and has dimension $1$.

**Proof.** If $Z$ is central then $ZE_{ij}=E_{ij}Z$ for all $i,j$. The left side has the column $j$ of $Z$ in the column $j$ and zeros elsewhere; the right side has $Z_{ij}$ in the entry $(i,i)$ and zeros elsewhere. Comparing entries forces $Z_{ij}=0$ for $i\neq j$ and forces all diagonal entries equal.

**Corollary.** The algebra is central over $\mathbb{C}$: its centre is exactly the scalars of the base field.

**Proof.** The scalars are central and the previous proposition excludes anything else.

**Corollary.** The image of the left regular representation commutes with the image of the right one, and their intersection is the scalars.

**Proof.** $L_ZX=ZX=XZ=XL_Z$ for central $Z$, and a matrix commuting with every left and every right multiplication is central.

## The Two Two-Sided Ideals

**Theorem.** The only two-sided ideals of $M_4(\mathbb{C})$ are $0$ and $M_4(\mathbb{C})$.

**Proof.** Let $I\neq0$ be a two-sided ideal and pick $A\in I$ with $A_{rs}\neq0$. For any $i,j$,

$$
E_{ij}=\frac{1}{A_{rs}}E_{ir}AE_{sj}\in I,
$$

since $E_{ir}A$ selects the $r$-th row into the $i$-th and $E_{sj}$ places it in the column $j$; the coefficient $A_{rs}$ is nonzero. The units generate the algebra, so $I$ is everything.

**Corollary.** The algebra is simple, and it has no nonzero nilpotent two-sided ideal, so it is semisimple in the sense of Jacobson.

**Proof.** Simplicity excludes every proper two-sided ideal, and a nilpotent ideal is proper unless it is the algebra, which is not nilpotent.

**The matrix-unit picture.** The proof shows the mechanism: a two-sided ideal is closed under the two operations that move a single nonzero entry anywhere, so a single entry generates everything. There is no room for a proper nonzero two-sided ideal because the units act transitively on the $16$ entries.

**Corollary.** Every nonzero element generates the whole algebra as a two-sided ideal, so $M_4(\mathbb{C})$ has one nonzero two-sided ideal class.

**Proof.** An element with a nonzero entry contains a unit as in the proof above, and the units generate.

## Central Simplicity

**Definition.** A finite-dimensional algebra over a field is **central simple** when it is simple and its centre is the base field. Its **degree** is the square root of the dimension, and its **index** is the degree of the division algebra in its Brauer class.

**Proposition.** $M_4(\mathbb{C})$ is central simple of degree $4$ and index $1$.

**Proof.** Simplicity is the theorem above, the centre is $\mathbb{C}\mathrm I_4$, and $\sqrt{16}=4$. The algebra is already a full matrix algebra, so its Brauer class is trivial and the index is $1$.

**Corollary (Wedderburn).** Every finite-dimensional simple complex algebra is a full matrix algebra, and $M_4(\mathbb{C})$ is the simple algebra of dimension $16$ over $\mathbb{C}$.

**Proof.** By Wedderburn's theorem a simple algebra is $\operatorname{End}_D(V)$ for a division algebra $D$; over an algebraically closed field $D=\mathbb{C}$, so the algebra is a full matrix algebra, and the dimension fixes the size.

**Corollary.** The trace form $\beta(X,Y)=\operatorname{tr}(XY)$ is non-degenerate, so the algebra is semisimple by Cartan's criterion.

**Proof.** If $\operatorname{tr}(AY)=0$ for all $Y$ then $A=0$ by choosing $Y=E_{ji}$ with $A_{ij}\neq0$. A semisimple algebra has non-degenerate trace form; here the converse direction is direct.

**The consequences of centrality.** Every derivation is inner, every automorphism is conjugation by an invertible element, and the algebra is a central simple algebra of degree $4$ in the Brauer group. The first two are *The Derivations and the Automorphisms of $M_4(\mathbb{C})$*.

## The One-Sided Ideals

**Theorem.** For a subspace $W\subset\mathbb{C}^{4}$ of dimension $k$, the set

$$
L_W=\{A:\ \operatorname{Im}A\subset W\}=\{A:\ AW^{\perp}=0\}
$$

is a left ideal of dimension $4k$, and every left ideal is of this form.

**Proof.** If $\operatorname{Im}A\subset W$ then $\operatorname{Im}(BA)\subset\operatorname{Im}A\subset W$, so $L_W$ is a left ideal. Conversely a left ideal $J$ is stable under left multiplication, so it is a union of orbits of the left action, and the left action moves the image subspace arbitrarily: the image of an element of $J$ is a fixed subspace $W$ and $J$ is contained in $L_W$; counting dimensions with $W$ the largest image subspace gives equality.

**Corollary.** The minimal left ideals have dimension $4$ and are the column spaces $\mathbb{C}^{4}E_{jj}$, each isomorphic to $\mathbb{C}^{4}$ as a left module; $M_4$ is the direct sum of four of them.

**Proof.** Take $W$ of dimension $1$: the space of matrices with all columns proportional to one fixed vector. Four such, one for each coordinate direction, are independent and span.

**The right ideals are dual.** Right ideals are the row spaces $\{A:\operatorname{Ker}A\supset W'\}$, of dimension $4(4-k)$; the minimal right ideals are the rows.

**Proposition.** No left ideal of intermediate dimension is two-sided, and the only left ideals that are also right ideals are $0$ and the algebra.

**Proof.** A two-sided ideal is a left ideal stable under right multiplication, which forces $W=0$ or $W=\mathbb{C}^{4}$; the two-sided ideals were classified above.

## The Kronecker Reading: Subalgebras, Not Ideals

**The factorisation.** $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes_{\mathbb{C}}M_2(\mathbb{C})$ via $E_{ij}\leftrightarrow E^{1}_{ab}\otimes E^{2}_{cd}$ with $(i,j)$ read as the pair $((a,c),(b,d))$.

**Proposition.** Each factor $M_2\otimes\mathrm I$ and $\mathrm I\otimes M_2$ is a subalgebra, of dimension $4$, and neither is an ideal.

**Proof.** Each is closed under multiplication and contains the unit. For an ideal it would have to absorb multiplication by arbitrary elements; but $(M_2\otimes\mathrm I)(\mathrm I\otimes E^{2}_{12})=M_2\otimes E^{2}_{12}$, which is not contained in $M_2\otimes\mathrm I$ when $M_2$ is not the whole of $M_2\otimes M_2$.

**Corollary.** The Kronecker factors are the images of $\mathbb{B}_L$ and $\mathbb{B}_R$ under the two-sided construction, and the "product of two algebras" is not a product of ideals.

**Proof.** In the basis $T_{\mu\nu}=L^{\mathrm{axf}}_{e_\mu}R^{\mathrm{axf}}_{e_\nu}$ the index $\mu$ runs over the first factor and $\nu$ over the second; the two index sets are independent, which is the tensor split.

**Why simplicity survives.** A tensor product of simple algebras is simple, so the factorisation is consistent with simplicity: the two factors are independent directions inside one simple algebra, not two summands of it. The mistake to avoid is reading $M_2\otimes M_2$ as $M_2\oplus M_2$; a direct sum of two matrix algebras is never simple, while a tensor product of two is.

**The counting check.** A direct sum $M_2\oplus M_2$ has dimension $8$ and two two-sided ideals; the tensor product has dimension $16$ and none. The biquaternion algebra $\mathbb{B}$ is $M_2(\mathbb{C})$, of dimension $4$, and it is simple for the same reason.

## Summary

A matrix is central exactly when it is scalar, so the centre is $\mathbb{C}\mathrm I_4$ of dimension $1$, and the two operations that move one entry anywhere show that a nonzero two-sided ideal is everything. Hence $M_4(\mathbb{C})$ is simple, central simple of degree $4$ and index $1$, with a non-degenerate trace form.

The left ideals are the sets of matrices whose image lies in a fixed subspace, of dimensions $4k$; the minimal ones are the four column spaces. The right ideals are dual. No intermediate left ideal is two-sided.

The Kronecker decomposition $M_4=M_2\otimes M_2$ is a tensor product of subalgebras, not a direct sum of ideals, and it is exactly the split between the left and the right families of operators. Simplicity survives because simplicity is preserved by tensor products and destroyed by direct sums.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Z(M_4)$ | the centre, equal to $\mathbb{C}\mathrm I_4$ |
| $E_{ij}$ | the matrix units |
| $I$ | a two-sided ideal |
| $L_W$ | the left ideal of matrices with image in $W$ |
| $k$ | the dimension of $W$, so $\dim L_W=4k$ |
| $M_2\otimes M_2$ | the Kronecker factorisation, two subalgebras |
| $\mathbb{B}$ | the biquaternion algebra $M_2(\mathbb{C})$, of dimension $4$ |

## Further Reading

- Israel Nathan Herstein, *Noncommutative Rings* (Carus Mathematical Monographs, 1968), for simplicity, central simplicity and the density theorem.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the matrix-unit argument and the classification of simple algebras.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the units, the trace and the rank.
- [The Kronecker Factorisation of $M_4(\mathbb{C})$ into $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c-into-m2c-tensor-m2c.html), for the index calculus behind the factorisation.
- [The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-m2c.html), for the same proof at order two.
