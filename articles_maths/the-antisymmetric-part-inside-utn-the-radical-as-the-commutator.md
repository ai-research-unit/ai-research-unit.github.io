# __The Antisymmetric Part inside $UT_n$: the Radical as the Commutator__

## Introduction

**Inside $UT_n$ the antisymmetric part vanishes, and the role that $\operatorname{Skew}_n$ plays in the whole algebra is played by the strictly upper triangular algebra $n_+$, which is at once the commutator subalgebra and the radical of the trace form.**

The article computes the three statements: $UT_n\cap\operatorname{Skew}_n=0$, so the antisymmetric half has no piece inside the triangular algebra; $[UT_n,UT_n]=n_+$, of dimension $n(n-1)/2$, the same as $\dim\operatorname{Skew}_n$; and the radical of the trace form restricted to $UT_n$ is also $n_+$. It then compares the derived series of $UT_n$, which terminates, with the perfectness of $\operatorname{Skew}_n$, which does not, for $n\ge3$. It assumes *$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)* for the direct sum and *The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$* for the bracket of the other half. It defers the Peirce reading to *The Peirce Decomposition and the Two Halves* and the general theory of the triangular sum to $UT_n$ as a Linear Model of $\operatorname{Sym}_n$: Same Space, Wrong Product.

## The Intersection with the Antisymmetric Part

**A matrix that is both upper triangular and antisymmetric is zero.** If $U\in UT_n$ and $U^{\mathsf T}=-U$, then the entries below the diagonal vanish by triangularity and the entries above vanish by antisymmetry, so $U$ is diagonal with $U_{ii}=-U_{ii}$, hence $U=0$. Therefore

$$
UT_n\cap\operatorname{Skew}_n=\{0\},\qquad \dim UT_n+\dim\operatorname{Skew}_n=\frac{n(n+1)}{2}+\frac{n(n-1)}{2}=n^{2},
$$

which is the direct sum $M_n(\mathbb{R})=UT_n\oplus\operatorname{Skew}_n$. The antisymmetric half is therefore a complement of the triangular algebra and has no overlap with it.

**The two summands have the same dimension as the two triangular pieces.** The strictly upper triangular algebra $n_+$ and the antisymmetric algebra have equal dimensions,

$$
\dim n_+=\dim\operatorname{Skew}_n=\frac{n(n-1)}{2},
$$

and the dimension count at $n=2,3,4,5$ gives $1,3,6,10$ for both. So $n_+$ is the piece of $UT_n$ that is "of antisymmetric size", and it is the piece that the whole article is about.

**The two pieces are not isomorphic as algebras.** The map $E_{ij}\mapsto E_{ij}-E_{ji}$ for $i<j$ is a linear isomorphism $n_+\to\operatorname{Skew}_n$, since both are spanned by the same number of independent elements and the images are independent. But it is not a Lie algebra isomorphism: $[E_{12},E_{23}]=E_{13}$ maps to $[X_{12},X_{23}]=X_{13}$, so the single bracket survives, while $[E_{13},E_{24}]=0$ maps to $[X_{13},X_{24}]=0$ as well; the failure is at the second bracket, since $[n_+,n_+]\subsetneq n_+$ while $[\operatorname{Skew}_n,\operatorname{Skew}_n]=\operatorname{Skew}_n$.

## The Commutator Subalgebra

**The commutator of two upper triangular matrices is strictly upper triangular.** For $U,V\in UT_n$, the diagonal entry of $UV$ is $U_{ii}V_{ii}$ and the diagonal entry of $VU$ is the same, so the diagonal of $[U,V]$ vanishes. Hence

$$
[UT_n,UT_n]\subseteq n_+ .
$$

**The inclusion is an equality.** The bracket $[E_{ij},E_{jl}]=E_{il}$ for $i<j<l$ produces every strictly upper triangular unit, and $E_{ij},E_{jl}\in UT_n$. So

$$
[UT_n,UT_n]=n_+,\qquad \dim[UT_n,UT_n]=\frac{n(n-1)}{2},
$$

which was verified by spanning the brackets of the standard basis at $n=2,3,4,5$: the ranks are $1,3,6,10$, the dimensions of $n_+$.

**The commutator is therefore the first layer of the filtration, not the whole algebra.** In the antisymmetric half the bracket of two elements can be everything, since $[\operatorname{Skew}_n,\operatorname{Skew}_n]=\operatorname{Skew}_n$ for $n\ge3$; in the triangular algebra the bracket loses the diagonal at the first step and keeps losing at every later step. That difference is the whole contrast of the article, and it is the Lie-theoretic form of the difference between a compact and a solvable algebra.

**The quotient by the commutator is the diagonal.** Since $UT_n/n_+\cong\mathbb{R}^{n}$ through the diagonal, the abelianisation of $UT_n$ is $n$-dimensional, and the derived series starts with the loss of exactly $n$ dimensions. At $n=2$ the abelianisation is two-dimensional and the commutator is the line $\mathbb{R}E_{12}$.

## The Radical of the Trace Form

**The trace form on $UT_n$ pairs only the diagonal units.** For $i\le j$ and $k\le l$,

$$
\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il},
$$

which is nonzero only when $i=l$ and $j=k$, and then $i\le j=k\le l=i$ forces $i=j=k=l$. So the Gram matrix of the trace form in the basis of the units is diagonal with entries $1$ on the diagonal units and $0$ elsewhere. Its rank is $n$ and its nullity is $n(n-1)/2$.

**The radical is $n_+$.** An element $U\in UT_n$ lies in the radical exactly when $\operatorname{tr}(UV)=0$ for every $V\in UT_n$, which by the computation above means that all diagonal entries of $U$ vanish. Hence

$$
\operatorname{rad}\big(\operatorname{tr}|_{UT_n}\big)=n_+=[UT_n,UT_n].
$$

The equality of the two spaces is the point of the title: the radical of the form and the commutator of the algebra coincide. The ranks $2,3,4,5$ and nullities $1,3,6,10$ at $n=2,3,4,5$ were computed directly from the Gram matrix.

**On the antisymmetric half the same form is definite, so its radical is zero.** For $K,K'\in\operatorname{Skew}_n$,

$$
\operatorname{tr}(KK')=-\operatorname{tr}(KK^{\mathsf T})=-\sum_{i,j}K_{ij}^{2},
$$

which is negative definite. So the radical is zero there, and the contrast is exact: the form has a radical of dimension $n(n-1)/2$ on $UT_n$ and none on $\operatorname{Skew}_n$, at the same value of the dimension of the space.

**The radical is also the nilpotent radical.** The algebra $n_+$ is nilpotent, since $n_+^{n}=0$, and it is an ideal of $UT_n$ with abelian quotient. So $n_+$ is at once the commutator, the radical of the trace form and the maximal nilpotent ideal, and the three descriptions agree because the algebra is solvable and the quotient is the diagonal torus.

## The Derived Series and Solvability

**The derived series is the filtration by the width of the band.** Put $UT_n^{(1)}=[UT_n,UT_n]$ and $UT_n^{(k+1)}=[UT_n^{(k)},UT_n^{(k)}]$. Since $[E_{ij},E_{jl}]=E_{il}$ whenever $j$ lies between $i$ and $l$,

$$
UT_n^{(k)}=\operatorname{span}\{E_{ij}:j-i\ge 2^{k-1}\},
$$

which was verified layer by layer at $n=2,3,4,5$. The band doubles in width at each step, so the series reaches zero after $\lceil\log_2 n\rceil$ steps and $UT_n$ is **solvable**.

**The layers shrink fast.** At $k=1$ the dimension is $n(n-1)/2$, the number of pairs $j-i\ge1$; at $k=2$ it is the number of pairs $j-i\ge2$; and the last nonzero term is the line $\mathbb{R}E_{1n}$. For $n=4$ the layers have dimensions $6,3,1,0$, and for $n=5$ they have $10,6,1,0$, which the computation confirms.

**The antisymmetric half is perfect, so its derived series never terminates.** For $n\ge3$,

$$
[\operatorname{Skew}_n,\operatorname{Skew}_n]=\operatorname{Skew}_n,
$$

which was verified at $n=3,4,5,6$ by spanning the brackets of the standard basis: the ranks are $3,6,10,15$, equal to the dimensions. At $n=2$ the algebra is abelian and the bracket vanishes, so the statement is exactly where $\mathfrak{so}(2)$ stops being perfect.

**Solvability is the global form of the failure of the two halves to be interchangeable.** The triangular algebra has a largest solvable ideal equal to itself, while the antisymmetric algebra has none, so the two spaces of dimension $n(n-1)/2$ sit at opposite ends of the structure theory. The complement relation $M_n=UT_n\oplus\operatorname{Skew}_n$ is therefore a decomposition into a solvable and a semisimple piece.

## The Case $n=2$ and $n=3$

**At $n=2$ the three spaces are lines and the contrast is exact.** With $UT_2$ spanned by $E_{11},E_{12},E_{22}$,

$$
[UT_2,UT_2]=\mathbb{R}E_{12}=n_+,\qquad \operatorname{rad}\big(\operatorname{tr}|_{UT_2}\big)=\mathbb{R}E_{12},\qquad \operatorname{Skew}_2=\mathbb{R}J,
$$

three lines of dimension one, the first two equal and the third disjoint from both. The trace form on $UT_2$ has rank $2$ and nullity $1$, and on $\operatorname{Skew}_2$ it is negative definite.

**At $n=3$ the two derived layers are visible one at a time.** The algebra has dimension $6$, the commutator has dimension $3$ and is spanned by $E_{12},E_{13},E_{23}$, and the second commutator is the line $\mathbb{R}E_{13}$:

$$
UT_3^{(1)}=\operatorname{span}\{E_{12},E_{13},E_{23}\},\qquad UT_3^{(2)}=\mathbb{R}E_{13},\qquad UT_3^{(3)}=0 .
$$

Meanwhile $\operatorname{Skew}_3\cong\mathfrak{so}(3)$ has dimension $3$ and is simple, so its commutator is itself. The two three-dimensional pieces therefore behave in opposite ways, which the computation confirms at every step.

**The biquaternion reading at $n=2$ makes the coincidence of radicals visible.** The strictly upper triangular piece $n_+$ is the line $E_{12}$, which is the corner $\mathbb{B}_{+-}$ when the idempotents are taken to be the coordinate projections; the idempotents $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm\tilde{Ζ})$ are symmetric, and the nilpotent $\vec\Pi_{\mathrm{nil},+-}$ lies in that corner. So the radical of the trace form is the line of the companion nilpotent, and the antisymmetric line $\mathbb{C}J$ is the rotation direction, which is not triangular and does not meet $UT_2$.

## Summary

The antisymmetric half meets $UT_n$ only at zero, and the two spaces are complements of dimensions $n(n-1)/2$ and $n(n+1)/2$. Inside the triangular algebra the strictly upper triangular part $n_+$ plays the role of the antisymmetric half by dimension, and it is characterised three ways at once: it is the commutator $[UT_n,UT_n]$, it is the radical of the trace form restricted to $UT_n$, and it is the maximal nilpotent ideal. The derived series of $UT_n$ is the band filtration $j-i\ge 2^{k-1}$ and terminates after $\lceil\log_2 n\rceil$ steps, while $\operatorname{Skew}_n$ is perfect for $n\ge3$ and has no solvable ideal. The trace form is negative definite on the antisymmetric half and degenerate with radical $n_+$ on the triangular algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UT_n$ | the upper triangular algebra, of dimension $n(n+1)/2$ |
| $n_+$ | the strictly upper triangular algebra, of dimension $n(n-1)/2$ |
| $[UT_n,UT_n]=n_+$ | the commutator subalgebra |
| $\operatorname{rad}(\operatorname{tr}\|_{UT_n})=n_+$ | the radical of the trace form |
| $UT_n^{(k)}=\operatorname{span}\{E_{ij}:j-i\ge2^{k-1}\}$ | the derived series |
| $\lceil\log_2 n\rceil$ | the number of steps at which the derived series reaches zero |
| $[\operatorname{Skew}_n,\operatorname{Skew}_n]=\operatorname{Skew}_n$ | the perfectness of the antisymmetric half for $n\ge3$ |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for solvable algebras, derived series and perfect algebras.
- Karin Erdmann and Mark J. Wildon, *Introduction to Lie Algebras* (Springer, 2006), for the triangular subalgebra of $\mathfrak{gl}_n$ and its radical.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the trace form, its radical and the nilpotent radical of a finite dimensional algebra.
- [$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)](utn-as-the-complement-of-the-antisymmetric-part-transpose-case.html), for the direct sum $M_n(\mathbb{R})=UT_n\oplus\operatorname{Skew}_n$.
- [The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$](the-lie-algebra-skew-n-and-so-n.html), for the perfectness of the antisymmetric half.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$](the-triangular-decomposition-h-n-plus-n-minus.html), for the three triangular summands and their dimensions.
