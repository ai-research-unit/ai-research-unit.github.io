# __$UT_4$ as the Complement of the Antisymmetric Part__

## Introduction

**The upper triangular matrices form a subspace of dimension $10$, the antisymmetric matrices one of dimension $6$, and the two are direct complements: every matrix is an antisymmetric matrix plus an upper triangular one, in exactly one way.**

The article proves the direct sum, writes the projection down entry by entry, contrasts this complement of $\operatorname{Skew}_4$ with the symmetric one, and states what each complement buys: the triangular one carries a flag and a solvable algebra, the symmetric one carries a Jordan product and a cone.

It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=4$* for the antisymmetric half and *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_4(\mathbb{C})$* for the Borel. The case $n=2$ is *$UT_2$ as the Complement of the Antisymmetric Part*. The product question on the same space is *$UT_4$ as a Linear Model of $\operatorname{Sym}_4$: Same Space, Wrong Product*.

## Which $UT_4$

**Definition.** In this category $UT_4$ is the space of **upper triangular** matrices including the diagonal, that is the span of the ten units $E_{ij}$ with $i\le j$. It is the Lie algebra of the group $B_4$ of invertible upper triangular matrices, and it is not the group and not the set of strictly upper triangular matrices.

**Proposition.** $\dim UT_4=10$, with the basis $E_{ii}$ for $1\le i\le4$ and $E_{ij}$ for $i<j$.

**Proof.** The pairs with $i\le j$ number $4+6=10$.

**The convention is fixed.** A strictly upper triangular space has dimension $6$ and is written $\mathfrak{n}_+$; the unipotent group is $\mathrm I+\mathfrak{n}_+$; $UT_4$ always means the ten-dimensional space. Mixing the three is the commonest source of wrong dimension counts in this block, so the article keeps to the definition above throughout.

## The Direct Sum

**Theorem.** $M_4(\mathbb{C})=\operatorname{Skew}_4\oplus UT_4$.

**Proof.** Suppose $A$ is both antisymmetric and upper triangular. Then $a_{ii}=-a_{ii}$, so the diagonal vanishes, and $a_{ij}=0$ for $i<j$ by triangularity; hence $A=0$, and the intersection is zero. The dimensions add to $6+10=16$, so the sum is everything.

**The projection, entry by entry.** For $A$ arbitrary, the decomposition $A=K+U$ is

$$
U_{ii}=a_{ii},\qquad U_{ij}=a_{ij}+a_{ji}\ (i<j),\qquad U_{ij}=0\ (i>j),
$$

and $K=A-U$, with $K_{ij}=a_{ij}$ for $i>j$ and $K_{ji}=-a_{ij}$.

**Proof.** The proposed $U$ is upper triangular, and $K=A-U$ has $K_{ii}=0$, $K_{ij}=a_{ij}$ for $i>j$ and $K_{ji}=a_{ji}-(a_{ij}+a_{ji})=-a_{ij}$ for $i<j$, which is antisymmetry. Uniqueness is the theorem.

**Corollary.** The map $A\mapsto U$ is linear and idempotent with image $UT_4$ and kernel $\operatorname{Skew}_4$.

**Proof.** It is the projection along a direct summand, and the formulas are linear.

**The projection is not orthogonal.** For the trace pairing, $\operatorname{tr}(KU)$ need not vanish: with $K=E_{12}-E_{21}$ and $U=E_{12}$ one has $KU=-E_{22}$, of trace $-1$.

**Proof.** Compute $KU=(E_{12}-E_{21})E_{12}=E_{12}E_{12}-E_{21}E_{12}=0-E_{22}$.

**What that means.** There are two natural complements of $\operatorname{Skew}_4$, the symmetric half and the triangular space, and only the first is orthogonal for the trace pairing. The triangular one is the complement defined by the flag, not by the form.

## The Two Complements Compared

**Proposition.** $\operatorname{Sym}_4\cap UT_4=\mathfrak{h}$, of dimension $4$, and $\operatorname{Sym}_4\neq UT_4$.

**Proof.** A symmetric upper triangular matrix is diagonal; a diagonal matrix is both. Both spaces have dimension $10$, so equality would force the intersection to have dimension $10$, which it does not.

**The table of what each buys.**

| Question | $\operatorname{Sym}_4$ | $UT_4$ |
|---|---|---|
| closed under the product | no | yes |
| a Lie algebra | no | yes |
| a Jordan algebra | yes | no |
| contains the diagonal | yes | yes |
| a Borel | no | yes |
| stabilises a flag | no | yes |
| carries a cone of squares | yes | no |
| orthogonal to $\operatorname{Skew}_4$ for $\beta$ | yes | no |

**Proof of the rows.** The symmetric half is closed under $\circ$ and not under the product; the triangular space is closed under the product and the commutator, and the Jordan product of two upper triangular matrices is again upper triangular but the Jordan identity fails, as the companion article shows. The symmetry row is the first proposition of this section and the orthogonality row was computed above.

**Why both complements matter.** The symmetric complement turns $\operatorname{Skew}_4$ into an orthogonal summand and produces the Cartan decomposition $\mathfrak{gl}_4=\mathfrak{so}(4)\oplus\operatorname{Sym}_4$. The triangular complement produces the quotient $M_4/\mathfrak{n}_-\cong\mathfrak{b}$ and the flag variety. One complement is adapted to a form, the other to a filtration, and no single complement is adapted to both.

## The Flag and the Triangular Complement

**Proposition.** $UT_4=\mathfrak{h}\oplus\mathfrak{n}_+$ and $\mathfrak{n}_-$ is a complement of $UT_4$ as well.

**Proof.** The position split gives the first identity; the second is the same dimension count with the disjoint index sets $i>j$ and $i\le j$.

**Corollary.** The algebra has at least three pairwise different complements of $\operatorname{Skew}_4$: the symmetric half, the triangular space, and the space $\mathfrak{h}\oplus\mathfrak{n}_-$ obtained by reflecting the flag.

**Proof.** Each has dimension $10$ and meets $\operatorname{Skew}_4$ only at zero, as the same argument with the transposed inequalities shows; they are pairwise different because their diagonal parts and their triangular parts differ.

**The reading of the projection onto $UT_4$.** The formula $U_{ij}=a_{ij}+a_{ji}$ for $i<j$ shows that the triangular complement keeps the diagonal, keeps the upper entries as they are plus the transposed lower entry, and discards the lower entry alone. The symmetric complement instead keeps $a_{ij}+a_{ji}$ on both sides. The two projections agree on the diagonal and differ by a factor of two on the off-diagonal pairs.

## A Worked Matrix

**The example.** Take $A$ with entries $a_{ij}=4(i-1)+j$, the matrix

$$
A=egin{pmatrix}1&2&3&4\ 5&6&7&8\ 9&10&11&12\ 13&14&15&16\end{pmatrix}.
$$

Then $U$ has the diagonal $1,6,11,16$, the strict upper entries $2+5=7$, $3+9=12$, $4+13=17$, $7+10=17$, $8+14=22$, $12+15=27$, and zeros below, and $K=A-U$ has the strict lower entries $5,9,13,10,14,15$ with the negatives in the transposed positions.

**The check.** $K$ is antisymmetric by construction, $U$ is upper triangular, and $K+U=A$; the six upper entries of $K$ are $-5,-9,-13,-10,-14,-15$, which are the negatives of the six strict lower entries of $A$ that $U$ discarded.

**The count of the discarded information.** In both cases six numbers are lost: the lower entries $a_{ij}$ with $i>j$ in the triangular reading, the differences $a_{ij}-a_{ji}$ in the symmetric reading. The information lost is the same size and a different content.

**Corollary.** The projection onto $UT_4$ along the antisymmetric half is the map that keeps the upper triangle and replaces the strict lower part by zero, so the two coordinates of an element are its upper triangle and its strictly lower triangle read as an antisymmetric matrix.

**Proof.** Decompose an arbitrary matrix into its upper triangular part and the negative of its strictly lower triangular part.

## Summary

The upper triangular matrices including the diagonal have dimension $10$, the antisymmetric matrices $6$, and their intersection is zero, so the two are direct complements of one another in the sixteen-dimensional algebra. The projection is written entry by entry: keep the diagonal, replace the strict upper entry by the sum of the two opposite entries, and set the strict lower entry to zero.

This complement differs from the symmetric complement of the same antisymmetric half, and only the symmetric one is orthogonal for the trace pairing. The symmetric complement is closed under the Jordan product and carries the cone of squares; the triangular complement is closed under the associative product, is a Borel, and stabilises the standard flag.

Three different ten-dimensional complements exist, one for the form, one for the flag and one for the reflected flag, and each discards six numbers of a different kind. The choice of complement is a choice of which structure on the algebra is to be visible.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UT_4$ | upper triangular including the diagonal, dimension $10$ |
| $\mathfrak{n}_+$ | strictly upper triangular, dimension $6$ |
| $\operatorname{Skew}_4$ | the antisymmetric half, dimension $6$ |
| $U_{ij}=a_{ij}+a_{ji}$ | the entry formula of the projection, for $i<j$ |
| $\mathfrak{h}$ | the diagonal, the common part of the two complements |
| $\beta$ | the trace pairing |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for triangular matrices and the $LU$ decomposition behind the projection.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_4(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m4c.html), for the Borel and its flag.
- [$UT_4$ as a Linear Model of $\operatorname{Sym}_4$: Same Space, Wrong Product](ut4-as-a-linear-model-of-sym-4-same-space-wrong-product.html), for the identical space under the wrong product.
- [The Two Halves as Orthogonal Complements at $n=4$](the-two-halves-as-orthogonal-complements-at-n-4.html), for the orthogonal complement of the antisymmetric half.
- [$UT_2$ as the Complement of the Antisymmetric Part](ut2-as-the-complement-of-the-antisymmetric-part.html), for the same split at order two.
