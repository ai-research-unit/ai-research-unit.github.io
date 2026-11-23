# __$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)__

## Introduction

**The antisymmetric matrices have two natural complements inside $M_n(\mathbb{R})$: the symmetric ones, which are the fixed half of the transpose, and the upper triangular ones, which are an algebra; the second complement is a vector space complement and not a structural one.**

The article proves the direct sum $M_n(\mathbb{R})=UT_n\oplus\operatorname{Skew}_n$, computes the projection onto the antisymmetric part along $UT_n$ in coordinates, and shows that this projection is not of the form $A\mapsto eA$ or $A\mapsto Ae$, so it is not a Peirce projection of any idempotent. It then shows what the complement fails to do: the bracket of an antisymmetric matrix with an upper triangular one is not upper triangular, so $UT_n$ is not the reductive complement of $\mathfrak{so}(n)$, and the projection is not a morphism for any of the products of the category. It assumes *The Two Halves as Orthogonal Complements* for the orthogonal complement and *The Triangular Decomposition $h\oplus n_+\oplus n_-$* for the triangular algebra. It defers the criterion that decides between the two complements to *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion* and the product comparison to *$UT_n$ as a Linear Model of $\operatorname{Sym}_n$: Same Space, Wrong Product*.

## Two Complements of the Antisymmetric Half

**The triangular algebra and the antisymmetric half add up to the whole algebra, and their intersection is zero.** Both statements are dimension counts plus one elementary observation:

$$
\dim UT_n+\dim\operatorname{Skew}_n=\frac{n(n+1)}{2}+\frac{n(n-1)}{2}=n^{2},\qquad UT_n\cap\operatorname{Skew}_n=\{0\},
$$

the intersection being zero because a matrix that is upper triangular and antisymmetric has vanishing diagonal and vanishing entries above it, since each such entry equals the negative of an entry below the diagonal which is absent. Hence

$$
M_n(\mathbb{R})=UT_n\oplus\operatorname{Skew}_n .
$$

**So the antisymmetric half has two complements of the same dimension, and they are different spaces.** The symmetric half is also of dimension $n(n+1)/2$ and also meets the antisymmetric half in zero, and

$$
\operatorname{Sym}_n\neq UT_n\qquad\text{for } n\ge2,
$$

since $E_{12}$ is upper triangular and not symmetric. The two complements are therefore two answers to the same question, and the category uses both: one is the fixed half of the involution, the other is the algebra whose product is the recurring contrast.

**Only one of the two is orthogonal to the antisymmetric half.** The symmetric half is the annihilator of $\operatorname{Skew}_n$ for the trace bilinear form, as *The Two Halves as Orthogonal Complements* proves. The triangular algebra is not: for $U=E_{12}$ and $K=E_{12}-E_{21}$,

$$
\operatorname{tr}(U^{\mathsf T}K)=\operatorname{tr}(E_{21}E_{12})-\operatorname{tr}(E_{21}E_{21})=1-0=1\neq0 .
$$

So $UT_n$ is a complement which is not the annihilator, and the projection along it is not the orthogonal projection.

## The Projection along $UT_n$

**The projection onto the antisymmetric part along $UT_n$ is computed entry by entry.** Write $A=U+K$ with $U$ upper triangular and $K$ antisymmetric. The diagonal of $K$ vanishes, so $U_{ii}=A_{ii}$; and for $i<j$ the entry below the diagonal of $A$ is $A_{ji}=K_{ji}=-K_{ij}$, since $U_{ji}=0$. Hence

$$
K_{ij}=-A_{ji}\ (i<j),\qquad K_{ji}=A_{ji}\ (i<j),\qquad K_{ii}=0,
$$

and $U=A-K$ recovers the triangular part. The formula in matrix terms is

$$
\pi(A)=\operatorname{strict}(A)-\operatorname{strict}(A)^{\mathsf T},
$$

where $\operatorname{strict}$ keeps the strictly lower triangular part and the superscript transposes it. The map $\pi$ is idempotent, its image is $\operatorname{Skew}_n$ and its kernel is $UT_n$; the three properties were verified at $n=2,3,4$.

**The projection is not the orthogonal projection, and the two differ by a shear.** The orthogonal projection onto the antisymmetric half is $\tfrac12(A-A^{\mathsf T})$, which uses the entries above the diagonal and their negatives below in equal weight. The projection along $UT_n$ uses the entries below the diagonal only, and doubles them:

$$
\pi(A)_{ij}=-A_{ji},\qquad \tfrac12(A-A^{\mathsf T})_{ij}=\tfrac12(A_{ij}-A_{ji})\qquad(i<j).
$$

The two agree exactly on the matrices whose strictly upper part vanishes, that is on the lower triangular matrices; elsewhere they differ, as the computation confirms at every tested size.

**A projection is determined by its kernel as much as by its image.** Both maps have the same image, and they differ because their kernels differ: $\ker\tfrac12(\mathrm{I}-{}^{\mathsf T})=\operatorname{Sym}_n$ and $\ker\pi=UT_n$. Choosing the antisymmetric part of a matrix is therefore not a well-posed operation until a complement is chosen, and the two complements of §*Two Complements of the Antisymmetric Half* give two different antisymmetric parts of the same matrix.

## Why It Is Not a Peirce Projection

**A Peirce projection is of the form $A\mapsto eA$ or $A\mapsto Ae$ for an idempotent $e$, and $\pi$ is not of either form.** The Peirce construction of *The Peirce Decomposition in $n$ Dimensions* uses multiplication by an idempotent, so its image is a left or a right ideal. The image of $\pi$ is $\operatorname{Skew}_n$, which is neither: for $K$ antisymmetric and $T=E_{12}$,

$$
TK=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&1\\-1&0\end{pmatrix}=\begin{pmatrix}-1&0\\0&0\end{pmatrix},
$$

which is symmetric and not antisymmetric, so $\operatorname{Skew}_n$ is not a left ideal and, by transposition, not a right ideal either.

**The image of $\pi$ is not even closed under multiplication, which no Peirce corner of a semisimple-looking algebra is.** A corner $eM_ne$ is closed under the product and contains $e$. The antisymmetric half is closed under neither: the product of two antisymmetric matrices is symmetric when they commute and has both parts in general, and it contains no nonzero idempotent at all: a nonzero idempotent has an eigenvector $v$ with $Ev=v$, while an antisymmetric matrix satisfies $v^{\mathsf T}Ev=0$ for every $v$, so $0=v^{\mathsf T}Ev=\|v\|^{2}$, a contradiction. So no antisymmetric matrix is an idempotent, and $\operatorname{Skew}_n$ is not a corner.

**Consequently $UT_n$ is not the Peirce corner of the split.** The corner attached to an idempotent $e$ with $e+e^{\mathsf T}=\mathrm{I}$ is $eM_ne$, which is a subalgebra of dimension $r^{2}$ for $e$ of rank $r$; the triangular algebra has dimension $n(n+1)/2$, which is $r^{2}$ only for $n=1$. The two constructions share the carrier space and nothing else, and the projection $\pi$ is the visible sign of the mismatch: a Peirce projection is multiplication by an element, and $\pi$ is not.

## What Fails: The Bracket

**The bracket of an antisymmetric matrix with an upper triangular one is not upper triangular.** Since $UT_n$ is a subalgebra and $\operatorname{Skew}_n$ is a Lie subalgebra, one might hope that the decomposition is a symmetric pair, which would require

$$
[\operatorname{Skew}_n,UT_n]\subseteq UT_n .
$$

The requirement fails: for a generic antisymmetric $K$ and a generic upper triangular $U$ the commutator $KU-UK$ has nonzero strictly lower entries. The computation at $n=2,3,4$ produces such entries every time, so the inclusion is false for every $n\ge2$.

**The failure is exactly what distinguishes $UT_n$ from the symmetric half.** For the symmetric half the corresponding inclusion holds,

$$
[\operatorname{Skew}_n,\operatorname{Sym}_n]\subseteq\operatorname{Sym}_n ,
$$

because the commutator of an antisymmetric and a symmetric matrix is symmetric; this is the closure rule of *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric*. So the two complements of the antisymmetric half are separated by one bracket computation, and the criterion is the subject of *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion*.

**The projection is not a morphism for any product of the category.** A map that is not multiplicative for the ordinary product cannot be multiplicative for the commutator or the anticommutator, and $\pi$ fails already on the commutator: $\pi([E_{12},E_{21}])=\pi(\sigma_3)=0$ while $[\pi E_{12},\pi E_{21}]$ involves the antisymmetrisations of the two units, which do not vanish. So $\pi$ is a projection of vector spaces and nothing more.

## The Case $n=2$

**At $n=2$ the complement is one line and the projection has a closed form.** Here $\operatorname{Skew}_2=\mathbb{R}J$ with $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, and $UT_2$ consists of the matrices $\begin{pmatrix}a&b\\0&c\end{pmatrix}$. The projection is

$$
\pi\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}0&-c\\c&0\end{pmatrix}=-c\,J ,
$$

so it reads one entry of the matrix and forgets the other three, and its kernel is exactly the triangular algebra.

**The two complements are the two readings of the same three-dimensional space.** The symmetric half is spanned by $\mathrm{I},\sigma_1,\sigma_3$ and the triangular algebra by $\mathrm{I},E_{12},\sigma_3$; both are three-dimensional, both meet $\operatorname{Skew}_2$ in zero, and they share the diagonal. The change from one to the other is the shear that replaces $\sigma_1$ by $E_{12}$, and that shear is the difference between $\tfrac12(A-A^{\mathsf T})$ and $\pi(A)$.

**The biquaternion frame sits in the antisymmetric side at $n=2$ only through one line.** The idempotents $\tilde\Pi_{\mathrm{id},\pm}$ are symmetric, the companion nilpotents are triangular at the coordinate flag, and the rotation $J$ is the single antisymmetric direction. The frame therefore uses the symmetric half for its idempotents and the triangular side for its nilpotents, and the two complements of this article are exactly the two pieces it borrows.

## Summary

The algebra is the direct sum of the upper triangular algebra, of dimension $n(n+1)/2$, and the antisymmetric half, of dimension $n(n-1)/2$, with zero intersection. The symmetric half is the other complement of the same dimension, and only it is the annihilator of the antisymmetric half for the trace form. The projection onto the antisymmetric part along $UT_n$ is $\pi(A)=\operatorname{strict}(A)-\operatorname{strict}(A)^{\mathsf T}$, idempotent with image $\operatorname{Skew}_n$ and kernel $UT_n$, and it differs from the orthogonal projection $\tfrac12(A-A^{\mathsf T})$ by a shear. The map is not of the form $A\mapsto eA$, the image is not an ideal and contains no nonzero idempotent, and the bracket $[\operatorname{Skew}_n,UT_n]$ is not contained in $UT_n$, so the decomposition is not a symmetric pair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UT_n$ | the upper triangular algebra, of dimension $n(n+1)/2$ |
| $\operatorname{Skew}_n$ | the antisymmetric half, of dimension $n(n-1)/2$ |
| $\operatorname{strict}(A)$ | the strictly lower triangular part of $A$ |
| $\pi(A)=\operatorname{strict}(A)-\operatorname{strict}(A)^{\mathsf T}$ | the projection onto $\operatorname{Skew}_n$ along $UT_n$ |
| $\tfrac12(A-A^{\mathsf T})$ | the orthogonal projection onto $\operatorname{Skew}_n$ |
| $[\operatorname{Skew}_n,UT_n]\subseteq UT_n$ | the inclusion that fails, and would make a symmetric pair |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions as multiplication by an idempotent.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Geometric Analysis* (AMS, 2001), for symmetric pairs and the reductivity of a complement.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the triangular factorisation and the antisymmetric part.
- [The Two Halves as Orthogonal Complements](the-two-halves-as-orthogonal-complements.html), for the complement that is the annihilator.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$](the-triangular-decomposition-h-n-plus-n-minus.html), for the triangular algebra inside the root decomposition.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the closure rule that $UT_n$ fails.
