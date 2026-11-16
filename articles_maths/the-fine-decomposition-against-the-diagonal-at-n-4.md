# __The Fine Decomposition against the Diagonal at $n=4$__

## Introduction

**The diagonal matrices form a subspace of dimension $4$, the strictly upper triangular ones a subspace of dimension $6$, and the strictly lower triangular ones another of dimension $6$; the three sum directly to the algebra, and the two halves sit against this split in opposite ways: the symmetric half contains the whole diagonal, the antisymmetric half contains none of it.**

The article defines the three pieces, proves the direct sum and the count $6+4+6=16$, identifies the diagonal as a Cartan subalgebra with its twelve weights, and makes precise the sense in which this decomposition is called "fine": it is the split by the position of the indices, not the split by root spaces, and the two sixes that occur in it are different subspaces.

It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=4$* for the halves and *The Matrix Algebra $M_4(\mathbb{C})$* for the invertibles. The root-space reading is *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_4(\mathbb{C})$*; the case $n=2$ is *The Fine Decomposition against the Diagonal at $n=2$*; the abstract notion is *Cartan Subalgebras and the Root Decomposition*.

## The Three Pieces

**Definition.** Let

$$
\mathfrak{h}=\operatorname{span}\{E_{ii}:1\le i\le4\},\qquad
\mathfrak{n}_+=\operatorname{span}\{E_{ij}:i<j\},\qquad
\mathfrak{n}_-=\operatorname{span}\{E_{ij}:i>j\}.
$$

**Proposition.** $\dim\mathfrak{h}=4$, $\dim\mathfrak{n}_+=6$, $\dim\mathfrak{n}_-=6$, and

$$
M_4(\mathbb{C})=\mathfrak{n}_-\oplus\mathfrak{h}\oplus\mathfrak{n}_+ .
$$

**Proof.** Each matrix unit belongs to exactly one of the three sets, according to whether its row index exceeds, equals or is less than its column index; the $16$ units are therefore split into groups of $6$, $4$ and $6$, and the sum is direct because the three sets of invertibles are disjoint.

**The count.** $6+4+6=16$, and the two sixes are $\binom{4}{2}$ each, the number of unordered pairs of distinct indices.

**Proposition.** $\mathfrak{h}$ is closed under multiplication and every element of it is diagonalisable; $\mathfrak{n}_+$ and $\mathfrak{n}_-$ are nilpotent subalgebras, with $\mathfrak{n}_+^{4}=0$ and $\mathfrak{n}_-^{4}=0$.

**Proof.** Diagonal matrices multiply diagonally. A strictly upper triangular matrix raises the column index at every multiplication, so the fourth power vanishes; the same argument with the row index for the strictly lower ones.

**Corollary.** $\mathfrak{h}$ is a Cartan subalgebra of $\mathfrak{gl}_4$: abelian, consisting of semisimple elements, and equal to its own centraliser.

**Proof.** Two diagonal matrices commute, each is diagonalisable, and a matrix commuting with every $E_{ii}$ is diagonal.

**The projection onto the diagonal.** Assembling the three pieces gives the map $\delta(A)_{ii}=A_{ii}$ and $\delta(A)_{ij}=0$ off the diagonal. It is linear, idempotent, kills $\mathfrak{n}_+\oplus\mathfrak{n}_-$, and is neither the trace nor the symmetric part: three different maps from the algebra onto $\mathfrak{h}$, distinguished by what they do to the off-diagonal entries.

## The Weights of the Diagonal

**Definition.** For $H=\operatorname{diag}(h_1,h_2,h_3,h_4)$ let $\varepsilon_i(H)=h_i$. The **weights** of the diagonal action are the linear functionals $\varepsilon_i-\varepsilon_j$.

**Proposition.** $[H,E_{ij}]=(\varepsilon_i-\varepsilon_j)(H)\,E_{ij}$.

**Proof.** The product $HE_{ij}$ has the entry $h_i$ in the position $(i,j)$ and $E_{ij}H$ has $h_j$ there; the difference is $(h_i-h_j)E_{ij}$.

**Corollary.** The algebra is the direct sum of the common eigenspaces of $\mathfrak{h}$,

$$
M_4=\mathfrak{h}\oplus\bigoplus_{i\neq j}\mathbb{C}E_{ij},
$$

with $12$ one-dimensional weight spaces and the four-dimensional zero weight space $\mathfrak{h}$ itself.

**Proof.** Each $E_{ij}$ with $i\neq j$ is an eigenvector with the nonzero weight $\varepsilon_i-\varepsilon_j$, and the elements of $\mathfrak{h}$ have weight zero.

**The distinction that the word "fine" carries.** The decomposition into $\mathfrak{n}_-$, $\mathfrak{h}$, $\mathfrak{n}_+$ is finer than the two halves but coarser than the weight decomposition: it groups the twelve weight spaces into two sixes by the sign of $i-j$, and it keeps the diagonal as one piece of dimension four. It is the split by **position**, not the split by **root spaces**, and the article uses the name in that sense only.

## The Two Halves against the Diagonal

**Proposition.** $\operatorname{Sym}_4$ contains the whole diagonal, and $\operatorname{Skew}_4$ meets it only at $0$.

**Proof.** A diagonal matrix is symmetric, so $\mathfrak{h}\subset\operatorname{Sym}_4$. A diagonal antisymmetric matrix has $k_{ii}=-k_{ii}$, hence all diagonal entries zero.

**Corollary.** $\operatorname{Sym}_4=\mathfrak{h}\oplus\operatorname{span}\{E_{ij}+E_{ji}:i<j\}$, of dimension $4+6=10$, and $\operatorname{Skew}_4=\operatorname{span}\{E_{ij}-E_{ji}:i<j\}$, of dimension $6$.

**Proof.** A symmetric matrix is determined by its diagonal and its entries above it; an antisymmetric one by its entries above it.

**Proposition.** $\operatorname{Skew}_4\cap\mathfrak{h}=0$ and $\mathfrak{h}+\operatorname{Skew}_4$ has dimension $10$, with quotient the six-dimensional space of symmetric off-diagonal pairs.

**Proof.** The intersection is zero by the previous proposition and the dimensions add as $4+6=10$.

**The two different sixes.** $\mathfrak{n}_+$ and $\operatorname{Skew}_4$ both have dimension $6$ and they are different subspaces: $\mathfrak{n}_+$ consists of upper triangular matrices, while $\operatorname{Skew}_4$ has entries both above and below the diagonal.

**Proposition.** $\mathfrak{n}_+\cap\operatorname{Skew}_4=0$, and $\mathfrak{n}_++\operatorname{Skew}_4$ is the whole off-diagonal part, of dimension $12$.

**Proof.** An upper triangular antisymmetric matrix has $k_{ii}=0$ on the diagonal and $k_{ij}=0$ for $i<j$, hence is zero. The sum of the dimensions is then $6+6=12$, and both summands lie in the off-diagonal part, which has dimension $12$ because the diagonal has dimension $4$ and the total is $16$.

## The Splits Side by Side

**Three decompositions of the same space of dimension $16$.**

| Split | Pieces | Dimensions |
|---|---|---|
| by the transpose | $\operatorname{Sym}_4\oplus\operatorname{Skew}_4$ | $10+6$ |
| by position | $\mathfrak{n}_-\oplus\mathfrak{h}\oplus\mathfrak{n}_+$ | $6+4+6$ |
| by triangularity | $\operatorname{Skew}_4\oplus UT_4$ | $6+10$ |

**Proposition.** The three splits are pairwise transverse: no piece of one is contained in a piece of another, except the diagonal, which lies in $\operatorname{Sym}_4$ and in $UT_4$.

**Proof.** $\operatorname{Sym}_4$ contains the diagonal and off-diagonal symmetric pairs, so it meets $\mathfrak{n}_+$ in the zero matrix only; $\operatorname{Skew}_4$ meets $\mathfrak{h}$ in zero; $UT_4$ contains $\mathfrak{h}$ and $\mathfrak{n}_+$. The stated inclusions are the only ones.

**What the fine split sees.** The diagonal is the fixed set of the torus action, and its dimension $4$ is the rank of the algebra; the two nilpotent pieces are the halves of the off-diagonal, and their dimensions $6$ and $6$ are the number of positive and negative roots. The symmetric half cuts across this split: it takes the whole diagonal and one combination from each pair of opposite off-diagonal slots, never a whole nilpotent piece, and never a piece of dimension $6$.

**The reading in the axis-free basis.** There the split is invisible: the sixteen elements $T_{\mu\nu}$ are signed permutations, and no subset of them is the set of diagonal matrices. The matrix units are the basis in which the diagonal and the triangular pieces are coordinate subspaces, and the axis-free basis is the one in which the halves and the trace pairing are coordinate subspaces. Each question has its own basis, and the fine decomposition belongs to the first.

**Corollary.** The diagonal is the only part of the space common to the two halves in the index language: a symmetric matrix has arbitrary diagonal and symmetric off-diagonal entries, an antisymmetric matrix has zero diagonal, and the diagonal coordinates belong to the symmetric side alone.

**Proof.** The two index patterns: the diagonal indices $i=i$ are symmetric, and no antisymmetric matrix has a nonzero diagonal entry.

**Corollary.** The count $4+6+6=16$ is read as the dimension of the flat part plus twice the dimension of the positive roots, which is the shape of the triangular decomposition of the next article.

**Proof.** The two counts of off-diagonal indices.

## Summary

The algebra splits by the position of the indices into the strictly lower part of dimension $6$, the diagonal of dimension $4$ and the strictly upper part of dimension $6$, and the three are direct. The diagonal is a Cartan subalgebra: abelian, semisimple, self-centralising, with twelve one-dimensional weight spaces attached to it.

The symmetric half contains the diagonal and the six symmetric off-diagonal pairs, of dimension $10$; the antisymmetric half is off-diagonal only, of dimension $6$, and meets the diagonal at zero. The two sixes of the fine split and the six of the antisymmetric half are different subspaces even though they share a dimension.

"Fine" names the split by position, not the root-space split: it groups the twelve weight spaces into two sixes and keeps the diagonal together. Against this split the symmetric half is transverse and the antisymmetric half is contained in the off-diagonal part, and the three decompositions of the sixteen-dimensional space — by the transpose, by position, by triangularity — are pairwise transverse.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{h}$ | the diagonal matrices, dimension $4$ |
| $\mathfrak{n}_+$, $\mathfrak{n}_-$ | strictly upper and strictly lower, dimension $6$ each |
| $UT_4$ | upper triangular including the diagonal, dimension $10$ |
| $\varepsilon_i$ | the coordinate functionals on $\mathfrak{h}$ |
| $\varepsilon_i-\varepsilon_j$ | the twelve weights |
| $\operatorname{Sym}_4$, $\operatorname{Skew}_4$ | the two halves, dimensions $10$ and $6$ |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for Cartan subalgebras, roots and the triangular decomposition.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_4(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m4c.html), for the root-space reading of the same three pieces.
- [$UT_4$ as the Complement of the Antisymmetric Part](ut4-as-the-complement-of-the-antisymmetric-part.html), for the third split in the table.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=4$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-4.html), for the defining properties of the halves.
- [The Fine Decomposition against the Diagonal at $n=2$](the-fine-decomposition-against-the-diagonal-at-n-2.html), for the same split at order two.
