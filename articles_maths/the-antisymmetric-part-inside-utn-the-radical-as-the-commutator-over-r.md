# __The Antisymmetric Part inside $UT_n$: the Radical as the Commutator over $\mathbb{R}$__

## Introduction

**The upper triangular matrices contain no nonzero antisymmetric matrix, so the antisymmetric part of $UT_n$ is zero and the antisymmetric part of a general matrix is its strictly lower triangular part; the trace form on $UT_n$ is degenerate, and its radical is exactly the commutator subalgebra $[UT_n,UT_n]=n_+$, of dimension $n(n-1)/2$.**

The article computes the intersection of the two spaces, the dimensions of the splitting, the rank of the trace form on the triangular algebra, and proves that the radical of that form is the commutator subalgebra and that it is nilpotent. It assumes *The Triangular Decomposition $h\oplus n_+\oplus n_-$* for the notation and *The Two Halves: Symmetric and Antisymmetric* for the two halves, and it defers the companion statement that $UT_n$ is a linear model of $\operatorname{Sym}_n$ to *$UT_n$ as a Linear Model of $\operatorname{Sym}_n$: Same Space, Wrong Product*.

Throughout $n\ge2$. The pieces are

$$
UT_n=\left\{X:X_{ij}=0\text{ for }i>j\right\},\qquad n_+=\{X\in UT_n:X_{ii}=0\},\qquad h=\{\text{diagonal matrices}\},
$$

so that $UT_n=h\oplus n_+$, of dimensions $n(n+1)/2$, $n(n-1)/2$ and $n$.

## The Intersection with the Antisymmetric Part Is Zero

**No nonzero upper triangular matrix is antisymmetric.** If $X\in UT_n$ and $X^{\mathsf T}=-X$ then for $i<j$ the entry $X_{ij}$ below the diagonal is zero, so $-X_{ji}=0$ and the entry $X_{ji}$ vanishes too; hence every entry above the diagonal vanishes as well, and $X=0$. So

$$
UT_n\cap\operatorname{Skew}_n=0.
$$

**Consequence: the two spaces are complementary and the splitting is exact.** Since $\dim UT_n=n(n+1)/2$ and $\dim\operatorname{Skew}_n=n(n-1)/2$ and the two sum to $n^{2}$,

$$
M_n(\mathbb{R})=UT_n\oplus\operatorname{Skew}_n,
$$

and every matrix is a unique sum of an upper triangular one and an antisymmetric one. This is the content of *$UT_n$ as the Complement of the Antisymmetric Part*, and the emptiness of the intersection is what makes the sum direct and not merely spanning.

**The antisymmetric part of an upper triangular matrix is not upper triangular, and the projection onto the antisymmetric half is onto.** For $X\in UT_n$ the projection $\pi_-(X)=\tfrac12(X-X^{\mathsf T})$ has the entries $\tfrac12X_{ij}$ above the diagonal and $-\tfrac12X_{ij}$ below it, and every antisymmetric matrix arises this way: given $K\in\operatorname{Skew}_n$, the matrix with $X_{ij}=2K_{ij}$ for $i<j$ and all other entries zero lies in $n_+$ and satisfies $\pi_-(X)=K$. So

$$
\pi_-(UT_n)=\operatorname{Skew}_n,\qquad \ker\left(\pi_-|_{UT_n}\right)=h,
$$

and the projection has rank $n(n-1)/2$, the dimension of the antisymmetric half.

**The antisymmetric part leaves the triangular half in both directions.** The projection $\pi_-$ carries an upper triangular matrix to a genuinely antisymmetric one, which has entries above the diagonal as well, so it is in neither $n_+$ nor $n_-$; the two strictly triangular halves are exchanged by the transpose with a sign, and the antisymmetric part averages the two. The only upper triangular matrices whose antisymmetric part vanishes are the diagonal ones, which is the kernel $h$.

## The Trace Form on $UT_n$ Is Degenerate

**The trace of a product of two upper triangular matrices depends only on the diagonals.** For $X,Y\in UT_n$ the product $XY$ is upper triangular and its diagonal entries are $(XY)_{ii}=X_{ii}Y_{ii}$, so

$$
\operatorname{tr}(XY)=\sum_{i=1}^{n}X_{ii}Y_{ii}.
$$

So the trace form on $UT_n$ is the standard form on the diagonal, pulled back by the projection onto $h$, and it sees nothing above the diagonal.

**The rank of the trace form on $UT_n$ is $n$.** The form is degenerate exactly on the matrices with zero diagonal, and its rank equals $\dim h=n$. Measured by computing the Gram matrix on the basis of matrix units inside $UT_n$, the rank is $2,3,4$ at $n=2,3,4$ and the nullity is $1,3,6$, which is $n(n-1)/2$.

**The radical is $n_+$, of dimension $n(n-1)/2$.** The radical is

$$
\operatorname{rad}UT_n=\{X\in UT_n:\operatorname{tr}(XY)=0\text{ for all }Y\in UT_n\}=\{X\in UT_n:X_{ii}=0\}=n_+,
$$

because for $X$ with a nonzero diagonal entry $X_{ii}$ the matrix $Y=E_{ii}$ gives $\operatorname{tr}(XY)=X_{ii}\ne0$. So the radical is the strictly upper triangular part, and the quotient $UT_n/n_+$ is the diagonal, on which the form is positive definite.

## The Radical Is the Commutator

**The commutator subalgebra of $UT_n$ is $n_+$.** The bracket of two upper triangular matrices is strictly upper triangular, because the trace of the commutator is zero and the commutator is upper triangular; and the bracket of a diagonal matrix with an upper triangular one is again strictly upper triangular. Hence

$$
[UT_n,UT_n]=n_+,
$$

of dimension $n(n-1)/2$, measured as $1,3,6$ at $n=2,3,4$ by spanning the brackets of a basis.

*Proof.* The inclusion $[UT_n,UT_n]\subseteq n_+$ is the two observations above. For the other inclusion, let $H=\operatorname{diag}(1,2,\dots,n)$; then $[H,E_{ij}]=(i-j)E_{ij}$ for $j>i$, which is a nonzero multiple of each basis element of $n_+$, so $n_+\subseteq UT_n'$. Hence the two coincide.

**Consequence: the radical of the trace form is the commutator subalgebra.** The two spaces are equal as sets, and the equality is not an accident of the count: the trace form vanishes on the diagonal only in the sense that the diagonal is where it is nondegenerate, and the radical is the full derived algebra. So

$$
\operatorname{rad}UT_n=[UT_n,UT_n]=n_+,
$$

and this is the content of the title: the radical of the invariant form on the triangular algebra is the commutator, not a proper subspace of it.

**The radical is a two-sided ideal.** For $X\in n_+$ and $U,V\in UT_n$, the product $UXV$ is upper triangular with a zero diagonal, so it lies in $n_+$. Hence $UT_n\,n_+\,UT_n\subseteq n_+$, and the radical is an ideal, as it must be for the radical of an invariant form on an algebra.

**The radical is nilpotent.** Every product of $n$ strictly upper triangular matrices is zero, because each factor raises the index by at least one and there is no room above the diagonal after $n$ steps. So $n_+^{n}=0$, and $n_+$ is a nilpotent ideal of index $n$.

## The Derived Series of $UT_n$

**The derived series descends inside $n_+$ and stops at zero.** Write $n_+^{(1)}=n_+$ and $n_+^{(k+1)}=[n_+^{(k)},n_+^{(k)}]$. The $k$-th space consists of the upper triangular matrices whose entries vanish on the first $2^{k-1}-1$ superdiagonals, so

$$
\dim n_+^{(2)}=\frac{(n-1)(n-2)}{2},
$$

measured as $1,3,6,10$ at $n=3,4,5,6$. The dimension is strictly decreasing, so the series reaches zero, and $UT_n$ is solvable.

**The derived length is $\lceil\log_2n\rceil$ and the nilpotency index of $n_+$ is $n$.** The radical satisfies $n_+^{n}=0$ and $n_+^{n-1}\ne0$, so it is nilpotent of index $n$; the derived series of the whole algebra ends at zero after $\lceil\log_2n\rceil$ steps. The two measures differ: nilpotence counts the products and solvability counts the nested commutators.

**Consequence: the algebra is solvable, and both of its forms are degenerate on the same space.** A real Lie algebra is semisimple exactly when its Killing form is nondegenerate, and a solvable algebra has $B(\mathfrak{g},[\mathfrak{g},\mathfrak{g}])=0$, so the Killing form of $UT_n$ vanishes on $n_+$ and is degenerate there. The radical of the trace form is the same space $n_+$, and the coincidence is the algebraic reading of the triangular decomposition: the Borel is the extreme opposite of the compact algebra $\mathfrak{so}(n)$.

## The Two Splittings Compared

**The trace form on $M_n$ is nondegenerate and the one on $UT_n$ is not.** On $M_n(\mathbb{R})$ the form $\operatorname{tr}(XY)$ is nondegenerate with inertia $(n(n+1)/2,n(n-1)/2)$; on the subspace $UT_n$ the restriction has rank $n$ and radical $n_+$. So the degeneration appears exactly when the algebra is replaced by a triangular half of it, and its size is the dimension of the commutator.

**The antisymmetric half is nondegenerate and the triangular half is not.** On $\operatorname{Skew}_n$ the form is negative definite, hence nondegenerate; on $UT_n$ it is degenerate with the maximal possible radical for a Borel. The two complementary subspaces of the splitting $M_n=UT_n\oplus\operatorname{Skew}_n$ therefore behave in opposite ways for the same form: one is definite, the other is maximally degenerate.

**The two halved decompositions are not the same decomposition.** The splitting by the transpose is $M_n=\operatorname{Sym}_n\oplus\operatorname{Skew}_n$, with both summands nondegenerate for the trace form; the splitting by triangularity is $M_n=UT_n\oplus\operatorname{Skew}_n$, with one summand degenerate. So the antisymmetric half is a complement of two different spaces, and only one of the two complements is itself nondegenerate.

## The Numbers at $n=2$, $n=3$ and $n=4$

**The count is uniform.** The table is

$$
\begin{array}{c|cccc}
n & \dim UT_n & \dim n_+ & \operatorname{rank}\operatorname{tr}|_{UT_n} & \dim\operatorname{rad}\\ \hline
2 & 3 & 1 & 2 & 1\\
3 & 6 & 3 & 3 & 3\\
4 & 10 & 6 & 4 & 6
\end{array}
$$

and each row satisfies $\dim UT_n=\operatorname{rank}+\dim\operatorname{rad}$, with the rank equal to $n$ and the radical equal to $n(n-1)/2$. The numbers were recomputed from the Gram matrix on the matrix units, and the dimension of the commutator was recomputed from the span of the brackets; the two agreed in every case.

**At $n=2$ the statement is visible in one line.** $UT_2=\left\{\begin{pmatrix}a&b\\ 0&c\end{pmatrix}\right\}$, $n_+=\mathbb{R}E_{12}$, and $\operatorname{tr}(XY)=aa'+cc'$, so the radical is $\mathbb{R}E_{12}$ and the commutator is $\mathbb{R}E_{12}$. The antisymmetric part of $\begin{pmatrix}a&b\\ 0&c\end{pmatrix}$ is $\tfrac12b\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$, which is the whole antisymmetric half at $n=2$ and lies in neither $UT_2$ nor $n_-$.

**At $n=3$ the count separates the two phenomena.** $\dim UT_3=6$, the rank is $3$, the radical is $n_+$ of dimension $3$, and the commutator is the same three-dimensional space. So the degenerate form and the derived algebra have the same size, and the two halves of the algebra that the transpose cuts have dimensions $6$ and $3$, the second equal to the radical.

## Summary

The upper triangular matrices meet the antisymmetric matrices only at zero, so the antisymmetric part of $UT_n$ is zero and $M_n=UT_n\oplus\operatorname{Skew}_n$ is a direct sum of dimension $n(n+1)/2$ and $n(n-1)/2$. The antisymmetric part of an upper triangular matrix is not triangular at all, and the projection onto the antisymmetric half is onto with kernel the diagonal. The trace form restricted to $UT_n$ depends only on the diagonal, so it has rank $n$ and radical $n_+$ of dimension $n(n-1)/2$, and that radical is exactly the commutator subalgebra $[UT_n,UT_n]$, which is a two-sided ideal and is nilpotent of index $n$. The two complementary splittings of $M_n$, by the transpose and by triangularity, behave differently for the same invariant form: the symmetric and antisymmetric halves are both nondegenerate, while the triangular half is degenerate with the largest radical a Borel can have.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UT_n$ | the upper triangular matrices, dimension $n(n+1)/2$ |
| $n_+$ | the strictly upper triangular matrices, dimension $n(n-1)/2$ |
| $n_-$ | the strictly lower triangular matrices |
| $h$ | the diagonal matrices, dimension $n$ |
| $\operatorname{rad}$ | the radical of the restricted trace form, equal to $n_+$ |
| $[UT_n,UT_n]$ | the commutator subalgebra, equal to $n_+$ |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the Borel and nilpotent subalgebras and the role of the radical.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the triangular factorisations and the trace of a product.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$](the-triangular-decomposition-h-n-plus-n-minus-of-mnr.html), for the three pieces used here.
- [$UT_n$ as the Complement of the Antisymmetric Part](utn-as-the-complement-of-the-antisymmetric-part.html), for the splitting $M_n=UT_n\oplus\operatorname{Skew}_n$.
- [The Two Halves: Symmetric and Antisymmetric](the-two-halves-symmetric-and-antisymmetric.html), for the half that $UT_n$ misses.
