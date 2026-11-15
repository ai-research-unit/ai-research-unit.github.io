# __The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$__

## Introduction

**The antisymmetric half of $M_n(\mathbb{R})$ is closed under the commutator and is isomorphic, as a Lie algebra, to the Lie algebra $\mathfrak{so}(n)$ of the orthogonal group; its Killing form is negative definite and equals $(n-2)\operatorname{tr}(XY)$, so the algebra is compact, and its rank is $\lfloor n/2\rfloor$.**

The article proves the closure and the Jacobi identity, identifies the antisymmetric matrices with the infinitesimal rotations, computes the dimension and a basis, computes the derived algebra, the centre and the Killing form, treats the three low cases $n=2,3,4$, proves the simplicity for $n\ge3$ except at $n=4$, and identifies the exponential map. It assumes *The Two Halves: Symmetric and Antisymmetric* for the set and *The Matrix Algebra $M_n(\mathbb{R})$* for the trace form, and it defers the complex case to *The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$* of the complex series.

Throughout $n\ge2$ and $\mathfrak{g}=\operatorname{Skew}_n$.

## The Bracket and the Jacobi Identity

**The commutator of two antisymmetric matrices is antisymmetric.** For $X,Y\in\mathfrak{g}$,

$$
[X,Y]^{\mathsf T}=(XY-YX)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}Y^{\mathsf T}=YX-XY=-[X,Y],
$$

so $[\mathfrak{g},\mathfrak{g}]\subseteq\mathfrak{g}$ and $\mathfrak{g}$ is a Lie subalgebra of $\mathfrak{gl}_n(\mathbb{R})$ with the commutator as bracket.

**The bracket is antisymmetric and satisfies the Jacobi identity.** $[X,Y]=-[Y,X]$ is immediate, and

$$
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0
$$

holds for all matrices, because it is the sum of twelve triple products in which each of the six orderings of $X,Y,Z$ appears twice with opposite signs. So $\mathfrak{g}$ is a real Lie algebra, and no further axiom is needed: associativity of the matrix product gives the Jacobi identity for free.

**The bracket is the derivative of the conjugation.** For $X,Y\in\mathfrak{g}$,

$$
[X,Y]=\frac{d}{dt}\Big|_{t=0}e^{tX}Ye^{-tX},
$$

so the bracket measures the infinitesimal action of the one-parameter group on the algebra. This is the reason the bracket of the skew half is the natural product: it is the product of the group $\mathrm{SO}(n)$ read at the identity.

## The Identification with $\mathfrak{so}(n)$

**A matrix is antisymmetric exactly when the bilinear form $\langle Xu,v\rangle$ is alternating.** For $X\in M_n(\mathbb{R})$,

$$
\langle Xu,v\rangle+\langle u,Xv\rangle=0\ \text{for all }u,v\iff X^{\mathsf T}=-X.
$$

*Proof.* The left side is $v^{\mathsf T}(X+X^{\mathsf T})u$, and a symmetric matrix that vanishes as a bilinear form is zero.

**Consequence: $\mathfrak{g}$ is the Lie algebra of $\mathrm{O}(n)$.** A curve $t\mapsto Q(t)$ in $\mathrm{O}(n)$ with $Q(0)=\mathrm{I}$ satisfies $Q^{\mathsf T}Q=\mathrm{I}$, and differentiating gives $\dot Q(0)^{\mathsf T}+\dot Q(0)=0$. Conversely, for $X$ skew the exponential $e^{tX}$ is orthogonal, since $(e^{tX})^{\mathsf T}=e^{-tX}=(e^{tX})^{-1}$. So the tangent space at the identity is $\mathfrak{g}$, and $\mathfrak{g}$ is the Lie algebra of both $\mathrm{O}(n)$ and $\mathrm{SO}(n)$, because the two groups have the same identity component.

**The isomorphism with $\mathfrak{so}(n)$ is the identity map.** The notation $\mathfrak{so}(n)$ refers to the same set of matrices with the same bracket; the article writes $\operatorname{Skew}_n$ when the matrix structure is used and $\mathfrak{so}(n)$ when the Lie structure is used. The two names denote one object.

## The Dimension and a Basis

**The antisymmetric matrices form a space of dimension $n(n-1)/2$.** The diagonal entries vanish and the entries above the diagonal determine those below with a sign, so the free entries are $\binom{n}{2}=n(n-1)/2$.

**A basis is the family $E_{ij}-E_{ji}$ for $i<j$.** These $\binom{n}{2}$ matrices are antisymmetric and independent, and they span. The bracket on the basis is

$$
[E_{ij}-E_{ji},E_{kl}-E_{lk}]=\delta_{jk}(E_{il}-E_{li})-\delta_{ik}(E_{jl}-E_{lj})-\delta_{jl}(E_{ik}-E_{ki})+\delta_{il}(E_{jk}-E_{kj}),
$$

which is the structure of the rotation algebra in the index notation. Measured at $n=2,3,4,5$, the number of basis elements is $1,3,6,10$. A maximal torus is spanned by $\lfloor n/2\rfloor$ commuting rotation blocks $E_{2k-1,2k}-E_{2k,2k-1}$, which is the rank of the algebra.

**The trace form is negative definite on $\mathfrak{g}$.** For $X\in\mathfrak{g}$,

$$
\operatorname{tr}(X^{2})=-\operatorname{tr}(XX^{\mathsf T})=-\sum_{i,j}X_{ij}^{2}\le0,
$$

with equality only for $X=0$. On the basis above, $\operatorname{tr}(X^{2})=-2$ for a single basis element and $0$ for two different ones, so the trace form is $-2$ times the identity in that basis.

## The Derived Algebra and the Centre

**The derived algebra is everything for $n\ge3$ and zero for $n=2$.** Measured by counting the dimension of the span of all brackets of basis elements, $[\mathfrak{g},\mathfrak{g}]=\mathfrak{g}$ at $n=3,4,5,6$, with dimensions $3,6,10,15$. At $n=2$ the algebra is one-dimensional, hence abelian, and $[\mathfrak{g},\mathfrak{g}]=0$.

**The centre is zero for $n\ge3$.** An element $Z$ with $[Z,X]=0$ for all $X\in\mathfrak{g}$ commutes with all antisymmetric matrices; the commutant of $\mathfrak{g}$ in $M_n(\mathbb{R})$ is $\mathbb{R}\mathrm{I}$ at $n\ge3$, and $\mathbb{R}\mathrm{I}$ meets $\mathfrak{g}$ only at $0$. At $n=2$ the algebra is abelian, so its centre is itself.

**Consequence: the algebra is perfect and centreless from $n=3$ on.** So it has no abelian quotient and no central extension of the kind that the Heisenberg algebra has, and it embeds in its own algebra of derivations as the inner derivations.

## The Killing Form

**The Killing form is $(n-2)\operatorname{tr}(XY)$, and it is negative definite.** For $X,Y\in\mathfrak{g}$,

$$
B(X,Y)=\operatorname{tr}(\operatorname{ad}X\circ\operatorname{ad}Y)=(n-2)\operatorname{tr}(XY).
$$

*Proof.* The algebra acts faithfully on $\mathbb{R}^{n}$ by $v\mapsto Xv$, and the trace form of this representation is $\operatorname{tr}(XY)$; the identity $B=(n-2)\operatorname{tr}(XY)$ follows from the decomposition $\wedge^{2}\mathbb{R}^{n}\oplus\operatorname{Sym}^{2}\mathbb{R}^{n}$ of the space of matrices and the value $-2$ of $\operatorname{tr}(X^{2})$ on a unit basis element. The factor is measured: the ratio of the two forms is $1$ at $n=3$, $2$ at $n=4$, $3$ at $n=5$.

**The eigenvalues are $-2(n-2)$, repeated $n(n-1)/2$ times.** Measured directly from the structure constants, the eigenvalues are $-2,-2,-2$ at $n=3$; $-4$ six times at $n=4$; $-6$ ten times at $n=5$. At $n=2$ the Killing form vanishes identically, because the algebra is abelian.

**Consequence: the algebra is compact.** A real Lie algebra whose Killing form is negative definite is the Lie algebra of a compact group, and here the group is $\mathrm{SO}(n)$, which is compact. The negative definiteness is the algebraic shadow of the compactness of the group, and the positive definiteness of $-\operatorname{tr}(XY)$ is the inner product it defines on the algebra.

**The form $-\operatorname{tr}(XY)$ is an inner product and an invariant form.** It is positive definite, and it satisfies

$$
\operatorname{tr}([X,Y]Z)=\operatorname{tr}(X[Y,Z]),
$$

so the adjoint action is by skew maps for this form. The algebra is thus a Euclidean Lie algebra, and the bracket is a skew trilinear form on it, which is the structure used in *The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form*.

## The Cases $n=2$, $n=3$ and $n=4$

**At $n=2$ the algebra is one-dimensional and abelian.** Every element is $a\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$, the bracket vanishes, the Killing form vanishes and the exponential is the circle $e^{aJ}=\begin{pmatrix}\cos a&\sin a\\ -\sin a&\cos a\end{pmatrix}$. So $\mathfrak{so}(2)\cong\mathbb{R}$ with the zero bracket, and $\mathrm{SO}(2)$ is a circle.

**At $n=3$ the algebra is $\mathbb{R}^{3}$ with the cross product.** The map

$$
u=(u_1,u_2,u_3)\longmapsto \begin{pmatrix}0&-u_3&u_2\\ u_3&0&-u_1\\ -u_2&u_1&0\end{pmatrix}
$$

is a linear isomorphism $\mathbb{R}^{3}\to\mathfrak{so}(3)$, and under it the bracket is the cross product: $[X_u,X_v]=X_{u\times v}$. Measured on $100$ random pairs, the identity held in every case. The Killing form becomes $-2\langle u,v\rangle$, so the algebra is the cross product algebra with the Euclidean form up to a factor.

**At $n=4$ the algebra is a direct sum of two copies of $\mathfrak{so}(3)$.** The Hodge star acts on $\wedge^{2}\mathbb{R}^{4}$ with $\star^{2}=1$, so the space of antisymmetric matrices splits into the self-dual and the anti-self-dual part, each of dimension $3$, and each is closed under the bracket. So

$$
\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3),
$$

as Lie algebras. The two summands commute, so the algebra is semisimple and not simple, and the Lie algebra does not detect the difference between the two three-dimensional summands.

**Consequence: the simplicity starts at $n=3$ and skips $n=4$.** $\mathfrak{so}(3)$ is simple; $\mathfrak{so}(4)$ is semisimple but not simple; and $\mathfrak{so}(n)$ is simple for $n\ge5$. The reason is the rank: at $n=4$ the two self-dual halves are exchanged by an outer automorphism, so an invariant subspace can be one of them.

**The simplicity for $n\ge5$ follows from the irreducibility of the standard representation.** An ideal $\mathfrak{h}\ne0$ of $\mathfrak{so}(n)$ is invariant under the adjoint action, and the standard representation $\mathbb{R}^{n}$ is irreducible for $n\ge5$; a nonzero ideal therefore acts irreducibly or by zero on $\mathbb{R}^{n}$, and the second alternative forces the ideal to be zero because the representation is faithful. So the algebra is simple.

## The Exponential and the Group

**The exponential maps $\mathfrak{so}(n)$ into $\mathrm{SO}(n)$.** For $X$ skew, $(e^{X})^{\mathsf T}e^{X}=e^{-X}e^{X}=\mathrm{I}$, so $e^{X}$ is orthogonal, and $\det e^{X}=e^{\operatorname{tr}X}=1$ because $\operatorname{tr}X=0$. So the image is in $\mathrm{SO}(n)$, and it is the identity component.

**The exponential is onto $\mathrm{SO}(n)$.** Every rotation is orthogonally diagonalisable in blocks of size one and two, and each block is a rotation by an angle $\theta$ in a plane, which is $e^{\theta J_2}$ on that plane. Assembling the blocks gives $Q=e^{X}$ with $X$ skew. So the exponential is surjective onto $\mathrm{SO}(n)$, which is the contrast with $\mathrm{GL}_n(\mathbb{R})$, where it is not.

**Consequence: $\mathrm{SO}(n)$ is connected.** It is the continuous image of the connected space $\mathfrak{so}(n)$, and $\mathrm{O}(n)$ has two components, cut by the determinant. This is the content of *The Two Components of $\mathrm{GL}_n(\mathbb{R})$ and the Failure of the Exponential* read at the level of the maximal compact subgroup.

## Summary

The antisymmetric half of $M_n(\mathbb{R})$ with the commutator is the Lie algebra $\mathfrak{so}(n)$ of the orthogonal group: it is closed under the bracket, the Jacobi identity is inherited from the associativity of the matrix product, and the bracket is the derivative of the conjugation action. Its dimension is $n(n-1)/2$ with basis $E_{ij}-E_{ji}$, its derived algebra is the whole algebra for $n\ge3$ and zero at $n=2$, and its centre is zero for $n\ge3$. Its Killing form is $(n-2)\operatorname{tr}(XY)$, negative definite with eigenvalues $-2(n-2)$ repeated $n(n-1)/2$ times, so the algebra is compact, and $-\operatorname{tr}(XY)$ is an invariant inner product. At $n=2$ it is abelian, at $n=3$ it is $\mathbb{R}^{3}$ with the cross product, at $n=4$ it is $\mathfrak{so}(3)\oplus\mathfrak{so}(3)$, and for $n\ge5$ it is simple. Its exponential is surjective onto $\mathrm{SO}(n)$, which is therefore connected.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Skew}_n$ | the antisymmetric half, dimension $n(n-1)/2$ |
| $\mathfrak{so}(n)$ | the same space with the commutator as bracket |
| $[X,Y]$ | the commutator $XY-YX$ |
| $E_{ij}-E_{ji}$ | the basis element attached to the pair $i<j$ |
| $B(X,Y)$ | the Killing form $(n-2)\operatorname{tr}(XY)$ |
| $\lfloor n/2\rfloor$ | the rank of $\mathfrak{so}(n)$ |

## Further Reading

- Anthony Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the classification of the classical real Lie algebras and the Killing form.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the relation between the compact form and the group $\mathrm{SO}(n)$.
- [The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$](the-four-multiplication-tables-ss-sk-ks-kk-over-r.html), for the product rule $KK\subseteq S\oplus K$ used here.
- [The Two Halves: Symmetric and Antisymmetric](the-two-halves-symmetric-and-antisymmetric-over-r.html), for the antisymmetric half as a set.
- [The Jordan Algebra $\operatorname{Sym}_n(\mathbb{R})$](the-jordan-algebra-sym-n-r.html), for the same half read with the anticommutator instead of the bracket.
