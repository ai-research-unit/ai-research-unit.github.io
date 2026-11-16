# __The Triangular Decomposition $h\oplus n_+\oplus n_-$__

## Introduction

**The algebra splits as a vector space into the diagonal, the strictly upper triangular part and the strictly lower triangular part, with dimensions $n$, $n(n-1)/2$ and $n(n-1)/2$, and the three summands are the weight-zero and the two signs of the root spaces.**

The article proves the decomposition and the dimension count, the nilpotency of $n_+$ with index exactly $n$, and the bracket relations that make $\mathfrak{b}=\mathfrak{h}\oplus n_+$ a solvable subalgebra with $[\mathfrak{b},\mathfrak{b}]=n_+$. It shows that the sum is not a Lie algebra decomposition, since $[n_+,n_-]$ is strictly larger than $\mathfrak{h}$ and contains the invertibles of gap at least two, and it records the comparison with the involution split: $\mathfrak{b}$ has the dimension of $\operatorname{Sym}_n$ and is not that half. It reads the decomposition as the infinitesimal form of the $LDU$ factorisation. It assumes *The Fine Decomposition against the Diagonal* for the grading and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the contrast. It defers the radical and the Killing form to *The Killing Form, Its Radical and the Triangular Case* and the quotient structure to *The Antisymmetric Part inside $UT_n$: the Radical as the Commutator*.

## The Three Summands

**Every matrix is the sum of a diagonal, a strictly upper triangular and a strictly lower triangular matrix, uniquely.** Write

$$
n_+=\{A:A_{ij}=0\ \text{for } i\ge j\},\qquad n_-=\{A:A_{ij}=0\ \text{for } i\le j\},
$$

and $\mathfrak{h}$ for the diagonal. Then

$$
M_n(\mathbb{C})=\mathfrak{h}\oplus n_+\oplus n_-,\qquad \dim=n+\frac{n(n-1)}{2}+\frac{n(n-1)}{2}=n^{2},
$$

because each entry of a matrix lies on the diagonal, above it or below it, and the three regions are disjoint. The decomposition is the root space decomposition of *The Fine Decomposition against the Diagonal* collected by the sign of the root: $\mathfrak{h}$ is the zero weight, $n_+$ is the sum of the lines of positive roots and $n_-$ the sum of the lines of negative roots.

**The two nilpotent summands have the same dimension and are exchanged by the transpose.** For $A\in n_+$ the transpose $A^{\mathsf T}$ is in $n_-$, so

$$
n_+^{\mathsf T}=n_-,\qquad \dim n_+=\dim n_-=\frac{n(n-1)}{2}.
$$

At $n=2$ the two dimensions are $1$ and $1$, at $n=3$ they are $3$ and $3$, and at $n=4$ they are $6$ and $6$. The diagonal is fixed by the transpose, so the whole decomposition is stable as a set of three summands.

**The three summands are mutually orthogonal and each restriction is definite.** Since

$$
\operatorname{tr}(A^{\mathsf T}C)=\sum_{i,j}A_{ij}C_{ij},
$$

and the supports of the three summands — the diagonal, the region above it, the region below it — are disjoint, the trace vanishes whenever $A$ and $C$ lie in different summands. On a single summand the form reduces to a sum of the products of matching entries, so it is positive definite there:

$$
M_n(\mathbb{C})=\mathfrak{h}\perp n_+\perp n_- ,\qquad (n^{2},0)\ \text{in total}.
$$

Each summand is therefore nondegenerate and is its own annihilator complement, and the three-way orthogonality was verified on random elements at $n=3,4$.

## The Nilpotent Summands

**A strictly triangular matrix is nilpotent, and the index is exactly $n$.** If $A\in n_+$ then $A^{k}$ has zero entries whenever $j-i<k$, by induction on $k$: the product of two matrices whose supports lie above the $r$-th and $s$-th superdiagonals lies above the $(r+s)$-th. Hence

$$
A^{n}=0\ \text{for every } A\in n_+,
$$

and the index is exactly $n$ for a generic element, since $A^{n-1}$ has the single entry $\prod_{k=1}^{n-1}A_{k,k+1}$ on the corner. The computation at $n=2,3,4,5$ gives index $2,3,4,5$ for a random strictly upper triangular matrix.

**The two summands are subalgebras, and they are abelian only at $n=2$.** For $A,C\in n_+$ the commutator is strictly upper triangular, since both products are, so

$$
[n_+,n_+]\subseteq n_+,\qquad [n_-,n_-]\subseteq n_- ,
$$

and $n_+$ is a **nilpotent Lie algebra**. Its derived algebra is spanned by the units of gap at least two,

$$
[n_+,n_+]=\operatorname{span}\{E_{ij}: j-i\ge2\},\qquad \dim=\frac{(n-1)(n-2)}{2},
$$

which vanishes exactly at $n\le2$. The values $0,1,3,6$ at $n=2,3,4,5$ were verified by bracketing the invertibles and taking the rank.

**The bracket of the two summands is not confined to the diagonal.** For units,

$$
[E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj},
$$

and with $i<j$ and $k>l$ the first term can produce an invertible element $E_{il}$ of any position, so $[n_+,n_-]$ contains $\mathfrak{h}$ and much of $n_+$ as well. The computed dimensions at $n=3,4$ are $6$ and $13$, against $n=3$ and $n=4$ for the diagonal, so the bracket is far from being the diagonal alone. The triangular decomposition is a decomposition of the vector space, not of the Lie algebra.

## The Borel Subalgebra

**The sum $\mathfrak{b}=\mathfrak{h}\oplus n_+$ is a solvable subalgebra of dimension $n(n+1)/2$, and $n_+$ is its derived algebra.** For $H\in\mathfrak{h}$ and $A\in n_+$ the commutator $[H,A]$ is strictly upper triangular, so $\mathfrak{b}$ is closed under the bracket; and

$$
[\mathfrak{b},\mathfrak{b}]=[n_+,n_+]+[\mathfrak{h},n_+]=n_+,
$$

since $[\mathfrak{h},n_+]=n_+$, which the computation confirms: the bracket of the diagonal with $n_+$ has the full dimension $n(n-1)/2$. Hence $\mathfrak{b}$ is solvable of derived length $2$ and its radical is $\mathfrak{b}$ itself, of dimension $n(n+1)/2$.

**The dimension of $\mathfrak{b}$ is the dimension of the symmetric half.** Both are $n(n+1)/2$:

$$
\dim(\mathfrak{h}\oplus n_+)=n+\frac{n(n-1)}{2}=\frac{n(n+1)}{2}=\dim\operatorname{Sym}_n .
$$

So $\mathfrak{b}$ is a linear model of $\operatorname{Sym}_n$ with the wrong product: the symmetric half is a Jordan algebra with a definite trace form, and $\mathfrak{b}$ is a solvable Lie algebra with a degenerate Killing form. The two are compared in *$UT_n$ as a Linear Model of $\operatorname{Sym}_n$: Same Space, Wrong Product*.

**The opposite summand gives the opposite Borel, and the two generate the algebra.** The subalgebra $\mathfrak{b}_{-}=\mathfrak{h}\oplus n_-$ is the image of $\mathfrak{b}$ under the transpose, and together the two generate $M_n$ as a Lie algebra, since $[n_+,n_-]$ fills in the diagonal and the missing units. The pair $(\mathfrak{b},\mathfrak{b}_{-})$ is the pair of opposite Borels of the Gauss decomposition, and the vector space sum $\mathfrak{b}+\mathfrak{b}_{-}$ is already everything.

## The Comparison with the Involution Split

**The triangular decomposition and the involution split cut the same space in two different ways.** With respect to the transpose, $\mathfrak{b}\cap\mathfrak{b}^{\mathsf T}=\mathfrak{h}$ and $\mathfrak{b}+\mathfrak{b}^{\mathsf T}=M_n$, so the two Borels are complementary modulo the diagonal. With respect to the two halves,

$$
\operatorname{Sym}_n\cap\mathfrak{b}=\mathfrak{h},\qquad \operatorname{Skew}_n\cap\mathfrak{b}=\{0\},
$$

since an antisymmetric matrix has no strictly upper triangular part that could survive being symmetric, and the symmetric half meets the Borel exactly on the diagonal.

**The involution exchanges the two Borels and fixes the diagonal, so the split and the decomposition interact by a sign.** The symmetric part of a matrix in $\mathfrak{b}$ is its diagonal plus the symmetrised off-diagonal entries, and the anti-Hermitian part of a matrix in $\mathfrak{b}$ is the antisymmetrised one. So each Borel element has a nonzero part in both halves, and the passage from the triangular decomposition to the involution split is a change of basis inside the same space.

**The contrast is the recurring one of the category.** The involution gives two halves that are stable under a product up to sign and orthogonal for a definite form; the triangular decomposition gives three summands that are stable under the bracket in a nested way and orthogonal for a degenerate pairing. The first is the spine, the second is the contrast, and every article that mentions $UT_n$ states which of the two it is using.

## The LU Reading

**The decomposition is the infinitesimal form of the $LDU$ factorisation.** A matrix that needs no row exchange factors as

$$
A=LDU,\qquad L\in\text{unit lower triangular},\ D\ \text{diagonal},\ U\in\text{unit upper triangular},
$$

and the counts of parameters match the three summands: $n(n-1)/2$ for $L$, $n$ for $D$ and $n(n-1)/2$ for $U$, totalling $n^{2}$. The factorisation is the exponentiated form of the decomposition $M_n=n_-\oplus\mathfrak{h}\oplus n_+$, and it is unique when it exists.

**The factorisation fails on a set of measure zero, and that failure is the interesting part.** The condition is the nonvanishing of the leading principal minors, so the set where $LDU$ exists is the open cell of the Bruhat decomposition and its complement is the union of the other cells, indexed by the permutations. The dimensions are read from the same root data: the open cell has dimension $n^{2}$ and the other cells have strictly smaller dimension.

**The two readings of the same decomposition are the group and the algebra.** At the group level the factorisation is $GL_n$ decomposed into the unipotent, the torus and the opposite unipotent; at the algebra level it is $M_n$ decomposed into the three summands. The correspondence is exact near the identity, which is where the exponential is a diffeomorphism, and it breaks at the elements that need a permutation.

## The Case $n=2$

**At $n=2$ the decomposition is $4=2+1+1$.** The diagonal is spanned by $\mathrm{I}$ and $\sigma_3=\operatorname{diag}(1,-1)$, and

$$
n_+=\mathbb{C}E_{12},\qquad n_-=\mathbb{C}E_{21},\qquad [E_{12},E_{21}]=\sigma_3 .
$$

So the two nilpotent summands are abelian, each of dimension $1$, and their bracket is the whole diagonal: the bracket of the two summands fills exactly the third, and the triangular decomposition is as close to a Lie algebra decomposition as it ever gets.

**The four Peirce lines of the coordinate flag are the three summands split once more.** The lines $\mathbb{C}E_{11}$ and $\mathbb{C}E_{22}$ make up the diagonal, and $n_+$ and $n_-$ are the two off-diagonal lines. So the triangular decomposition is the Peirce decomposition of *The Fine Decomposition against the Diagonal* with the four lines collected by the sign of the weight, and at $n=2$ no line is lost in the collecting.

**The biquaternion frame uses the opposite grouping.** The idempotents $\tilde\Pi_\pm$ lie in the diagonal, the two companion nilpotents $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ lie one in $n_+$ and one in $n_-$ at the coordinate flag, and the gauge rescales the pair reciprocally. The grouping of the frame is by the two corners, not by the sign of the root, and the difference between the two groupings is the difference between the Peirce reading and the triangular one.

## Summary

The algebra is the direct sum of the diagonal, of dimension $n$, and the two strictly triangular summands, of dimension $n(n-1)/2$ each, which are the weight-zero and the two signs of the root spaces. Each nilpotent summand is a nilpotent Lie algebra of index exactly $n$, with derived algebra spanned by the invertibles of gap at least two, of dimension $(n-1)(n-2)/2$, vanishing only at $n\le2$. The sum $\mathfrak{b}=\mathfrak{h}\oplus n_+$ is solvable of dimension $n(n+1)/2$, equal to $[\mathfrak{b},\mathfrak{b}]=n_+$ being its derived algebra and to the dimension of the symmetric half. The bracket $[n_+,n_-]$ is strictly larger than the diagonal, of dimension $13$ at $n=4$, so the decomposition is not a Lie algebra decomposition. The group-level form is the $LDU$ factorisation, valid on the open cell where the leading principal minors do not vanish.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{h}$ | the diagonal subalgebra, of dimension $n$ |
| $n_+$ | the strictly upper triangular matrices, of dimension $n(n-1)/2$ |
| $n_-$ | the strictly lower triangular matrices, of dimension $n(n-1)/2$ |
| $\mathfrak{b}=\mathfrak{h}\oplus n_+$ | the Borel subalgebra, of dimension $n(n+1)/2$ |
| $\mathfrak{b}_{-}=\mathfrak{h}\oplus n_-$ | the opposite Borel |
| $[n_+,n_+]=\operatorname{span}\{E_{ij}:j-i\ge2\}$ | the derived algebra, of dimension $(n-1)(n-2)/2$ |
| $LDU$ | the unit lower, diagonal and unit upper factorisation |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the triangular decomposition, the Borel subalgebras and the root spaces.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for triangular matrices, nilpotency and the $LU$ factorisation.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the Gauss decomposition of $GL_n$ and its open cell.
- [The Fine Decomposition against the Diagonal](the-fine-decomposition-against-the-diagonal.html), for the weight lines that the three summands collect.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the half whose dimension matches the Borel.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the upper triangular algebra $UT_n$ and its radical.
