# __The $SU(2)$ of $M_n(\mathbb{C})$ Acting on $n^2$ Dimensions__

## Introduction

**The question.** Read $M_n$ as a real vector space of dimension $2n^2$ and let the principal $SU(2)$ act by conjugation. What are the orbits, and what does the four-real-dimensional biquaternion picture become?

**The answer in one line.** The orbits are at most three-dimensional: a point for the scalars, a two-sphere for the diagonal matrices, a copy of $SO(3)$ for the generic element; the orbit space therefore has dimension $2n^2-3$ and the four-dimensional picture is the smallest case only.

**Why the article is needed.** At $n=2$ the number of real dimensions is small enough that the orbit picture and the carrier decomposition can be confused with each other. At $n=4$ the space has thirty-two real dimensions and the orbits have dimension at most three; the two pictures separate completely. An article that transfers the biquaternion orbit description to $n=4$ will be wrong by an order of magnitude in dimension.

**Boundaries.** The carrier decomposition is *The Spin Decomposition of $M_n(\mathbb{C})$*; the counting of carriers is *The Carriers, the Closures and the Spin of $M_n(\mathbb{C})$*; the real forms of the algebra are *The Real Structures of the Operators of $M_n(\mathbb{C})$*; the biquaternion case is *The Spin Group: Unit Elements, Rotors and the Two-to-One Cover*.

**Conventions.** The action is $X\mapsto gXg^{-1}$ for $g\in SU(2)$ in the principal copy. The orbit dimension is computed as the rank of the map $\xi\mapsto[\xi,X]$ from $\mathfrak{su}_2$ to $M_n$. The real dimension of $M_n$ is $2n^2$.

## The Action

**Proposition.** The action is faithful up to the centre: the kernel is $\{\pm\mathrm I\}$ for $n$ even and $\{\mathrm I\}$ for $n$ odd.

*Proof.* The principal copy is the representation $\operatorname{Sym}^{n-1}$, whose kernel is $\{\pm\mathrm I\}$ acting by $(-1)^{n-1}$. $\square$

**The effective group.** For odd $n$ the copy is isomorphic to $SO(3)$; for even $n$ it is $SU(2)$ acting faithfully. In both cases the group acting effectively is three-dimensional.

**The consequence.** Every orbit has dimension at most three, whatever $n$ is.

## The Orbits

**The orbit dimensions.** Computed at $n=2,3,4,5$ from the rank of $\xi\mapsto[\xi,X]$:

| $X$ | orbit dimension |
|---|---|
| $\mathrm I$ | $0$ |
| $J_z$, $J_x$, $E_{00}$ | $2$ |
| generic complex $X$ | $3$ |

**The scalar orbit.** The scalars are fixed, so the orbit of $\mathrm I$ is a point.

**The diagonal orbit.** The stabiliser of $J_z$ is the diagonal torus $U(1)$, so its orbit is $SU(2)/U(1)=S^2$, of dimension two.

*Proof.* $gJ_zg^{-1}=J_z$ if and only if $g$ is diagonal in the weight basis, and the diagonal elements of the principal copy form a circle. $\square$

**The generic orbit.** A generic $X$ commutes only with its own polynomials, which meet the principal copy in the scalars, so the stabiliser is $\{\pm\mathrm I\}$ for even $n$ and trivial for odd $n$. The orbit is $SU(2)/\{\pm\mathrm I\}=SO(3)$ or $SU(2)$ itself, of dimension three in both cases.

**The orbit space.** Since the generic orbit has dimension three in a space of dimension $2n^2$, the orbit space has dimension $2n^2-3$: $5,15,29,47$ for $n=2,3,4,5$.

## The Invariants

**The traces.** The functions $X\mapsto\operatorname{tr}(X^k)$, $k=1,\dots,n$, are invariant under conjugation, hence constant on every orbit.

**The insufficiency.** The traces do not separate the orbits of the principal copy: two matrices with the same characteristic polynomial can lie on different orbits, since the orbits are three-dimensional and the level sets of the characteristic polynomial are of dimension $2n^2-n$.

**The reading.** The orbit picture of a three-dimensional group on a $2n^2$-dimensional space is small: the orbits are submanifolds of the similarity classes, and the similarity classes are themselves large.

## The Biquaternion Case

**The numbers.** At $n=2$ the space is $\mathbb{R}^8$, the orbits are of dimensions $0$, $2$ and $3$, and the orbit space has dimension five.

**The four real dimensions.** The biquaternion series works with a real algebra of four real dimensions, which is the reduced algebra $\mathbb{C}\times\mathbb{C}$ or the real form of the four-complex-dimensional $\mathbb{B}$. The operator space $M_2(\mathbb{C})$ has eight real dimensions, twice as many, and the four-dimensional picture is a picture of the algebra, not of its endomorphisms.

**What does not generalise.** The biquaternion orbit description uses the fact that the space is four-dimensional: in four real dimensions an orbit can be the complement of a point, and the orbit classification can be read off a discriminant. At $n\ge3$ the space has dimension at least eighteen and the orbits are at most three-dimensional, so no orbit is open and no orbit classification is a finite list.

**The honest statement.** The case $n=2$ of the orbit picture is a special case in dimension, not only in label. The four-dimensional reading of the biquaternion algebra is the case of the algebra itself, and it does not extend to the operator space.

## The Comparison with the Carrier Decomposition

**Two decompositions.** The carrier decomposition is a decomposition of the *complex* space into invariant subspaces; the orbit decomposition is the partition of the *real* space into orbits. They are different partitions, and neither refines the other.

**The reason.** A carrier is a complex subspace, so it is a union of orbits only if the group acts inside it, which it does; but an orbit meets many carriers, since a generic element has components in all of them.

**The count.** The carriers number $n$; the orbit dimensions number three. Neither count grows with the dimension of the space in the same way.

## The Finite Check

The orbit dimensions were computed as the rank of the real matrix of the three maps $\xi\mapsto[\xi,X]$: at $n=2,3,4,5$ the ranks are $0$ for $X=\mathrm I$, $2$ for $X=J_z$, $X=J_x$ and $X=E_{00}$, and $3$ for a random complex $X$.

The kernel of the action was checked by computing $\exp(2\pi iJ_z)$: it equals $(-1)^{n-1}\mathrm I$ to $10^{-16}$ for $n=2,\dots,6$, confirming that $-\mathrm I$ acts by $+1$ for odd $n$ and by $-1$ for even $n$.

The orbit-space dimension $2n^2-3$ was checked against $8-3=5$, $18-3=15$, $32-3=29$, $50-3=47$.

## Inside the Similarity Class

**The containment.** The principal orbit of $X$ lies in the similarity class of $X$ under $GL_n$.

**The dimensions.** The similarity class of a regular $X$ has complex dimension $n^2-n$, hence real dimension $2n^2-2n$; the principal orbit has real dimension at most three.

**The table.**

| $n$ | similarity class, real | principal orbit | codimension |
|---|---|---|---|
| $2$ | $4$ | $3$ | $1$ |
| $3$ | $12$ | $3$ | $9$ |
| $4$ | $24$ | $3$ | $21$ |
| $5$ | $40$ | $3$ | $37$ |

**The reading.** At $n=2$ the generic orbit is a hypersurface of the similarity class, which is why the two pictures nearly coincide there. At $n=3$ the codimension is already nine.

## What the Four Dimensions Were

**The biquaternion space.** Four real dimensions, orbits of dimensions $0$, $2$, $3$, and an orbit space of dimension one.

**The general space.** $2n^2$ real dimensions, the same three orbit dimensions, and an orbit space of dimension $2n^2-3$.

**The reading.** The four-dimensional picture is the case where the orbit space has dimension one and the orbits can be listed. At $n=3$ the orbit space has dimension fifteen and no list exists.

## The Two Groups

**The principal copy.** $SU(2)$, three real dimensions, acting by conjugation on $M_n$.

**The full unitary group.** $U(n)$, $n^2$ real dimensions, acting by conjugation on $M_n$.

**The comparison.** The principal orbits have dimension at most three; the $U(n)$ orbits are the similarity classes, of dimension up to $2n^2-2$.

**The reading.** The principal copy is a three-dimensional subgroup of the $n^2$-dimensional group, and its orbits are correspondingly small. The carrier decomposition is the statement that the small group's action is completely reducible with the stated multiplicities.

## The Invariant Functions

**The traces.** $\operatorname{tr}X^k$ for $k=1,\dots,n$ are invariant under conjugation, hence under the principal copy.

**The separation.** They separate the similarity classes but not the principal orbits: two matrices in different principal orbits can have the same characteristic polynomial.

**The reading.** The principal copy is too small to see the invariants of the big group, which is why the orbit picture and the spectral picture are different pictures.

## The Reading

**The picture.** Three orbit dimensions in a space of dimension $2n^2$, classified by the type of the matrix: scalar, semisimple with a torus stabiliser, generic.

**The limit.** The picture is the same at every $n$; only the ambient space grows, and the orbit space grows with it.

## The Count

**The numbers.** The orbit dimensions $0,2,3$ do not grow with $n$; the ambient dimension $2n^{2}$ does, and the codimension of a generic orbit is $2n^{2}-3$.

## Summary

The principal $SU(2)$ acts on the $2n^2$ real dimensions of $M_n$ with orbits of dimension $0$, $2$ or $3$ and an orbit space of dimension $2n^2-3$. The scalar orbit is a point, the diagonal orbit a two-sphere, the generic orbit a copy of $SO(3)$. The invariants are the traces and they do not separate the orbits. The biquaternion four-dimensional picture is the picture of the algebra, not of the operator space, and it does not extend.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $2n^2$ | the real dimension of $M_n$ |
| $[\xi,X]$ | the infinitesimal action, whose rank is the orbit dimension |
| $S^2$ | the orbit of $J_z$ |
| $SO(3)$ | the generic orbit |
| $2n^2-3$ | the dimension of the orbit space |

## Further Reading
- [The Spin Decomposition of $M_n(\mathbb{C})$: $n$ Carriers, One for Each Spin from $0$ to $n-1$](the-spin-decomposition-of-mnc.html), for the complex decomposition.
- [The Carriers, the Closures and the Spin of $M_n(\mathbb{C})$](the-carriers-the-closures-and-the-spin-of-mnc.html), for the counts.
- [The Spin Group: Unit Elements, Rotors and the Two-to-One Cover](the-spin-group-unit-elements-rotors-and-the-two-to-one-cover.html), for the case $n=2$ read over $\mathbb{R}$.
- [The Real Structures of the Operators of $M_n(\mathbb{C})$, including Lie Algebras and Lie Groups](the-real-structures-of-the-operators-of-mnc.html), for the real forms.
- [The Odd Rows: $M_3(\mathbb{C})$ and $M_5(\mathbb{C})$](the-odd-rows-m3-and-m5.html), for the rows where the action factors through $SO(3)$.
- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the case $n=4$ in four readings.
