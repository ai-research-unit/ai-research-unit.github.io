# __The Two Halves as Orthogonal Complements for the Trace Form__

## Introduction

**The trace form $\operatorname{tr}(XY)$ is a nondegenerate symmetric bilinear form of inertia $(n(n+1)/2,n(n-1)/2)$ on $M_n(\mathbb{R})$, and the symmetric and antisymmetric halves are its exact positive and negative orthogonal complements.**

The article proves nondegeneracy, proves the orthogonality of the two halves, computes the inertia by exhibiting an orthogonal basis of matrix units, proves that the restrictions to the two halves are definite with opposite signs, and shows that the symmetrisation and antisymmetrisation are the orthogonal projections for the form. It then contrasts the trace form with the Hilbert–Schmidt form $\operatorname{tr}(X^{\mathsf T}Y)$, which is positive definite on the whole algebra and not invariant. It assumes *The Two Halves: Symmetric and Antisymmetric* for the two subspaces and *The Matrix Algebra $M_n(\mathbb{R})$* for the trace.

## The Trace Form

**Definition.** $\langle X,Y\rangle=\operatorname{tr}(XY)$ for $X,Y\in M_n(\mathbb{R})$.

**The form is bilinear and symmetric.** Bilinearity is linearity of the trace in each argument. Symmetry is the identity

$$
\operatorname{tr}(XY)=\operatorname{tr}(YX),
$$

which follows from the matrix units: $\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il}=\operatorname{tr}(E_{kl}E_{ij})$.

**The form is invariant under the product.** For all $X,Y,Z$,

$$
\langle XY,Z\rangle=\operatorname{tr}(XYZ)=\langle X,YZ\rangle.
$$

So the form is associative: moving a factor across the comma does not change the value. This is the property that the Hilbert–Schmidt form of the last section does not have.

**The trace form is not an inner product.** It has isotropic vectors: $\langle E_{12},E_{12}\rangle=\operatorname{tr}(E_{11}E_{22})=0$, and every nonzero nilpotent has square zero, hence $\langle N,N\rangle=\operatorname{tr}(N^{2})=0$. A symmetric bilinear form with a nonzero isotropic vector is indefinite.

## Nondegeneracy

**Proposition.** If $\langle X,Y\rangle=0$ for all $Y$ then $X=0$.

*Proof.* Test on the matrix units. $\langle X,E_{kl}\rangle=\operatorname{tr}(XE_{kl})=\sum_{i}X_{ik}\delta_{li}=X_{lk}$. So the value on $E_{kl}$ is the entry $X_{lk}$, and the hypothesis gives $X_{lk}=0$ for every pair.

**The matrix units pair only with their transposes.** $\langle E_{ij},E_{kl}\rangle=\delta_{il}\delta_{jk}$, so the basis $\{E_{ij}\}$ is not orthogonal but the pairing is a perfect matching: $E_{ij}$ pairs with $E_{ji}$ and with nothing else. Its Gram matrix is the permutation matrix of the involution $(i,j)\mapsto(j,i)$, of determinant $\pm1$.

**Nondegeneracy makes the form a duality.** The map $X\mapsto\langle X,\cdot\rangle$ is an isomorphism of $M_n(\mathbb{R})$ with its dual, and it is the reason why the orthogonal complement of a subspace has the complementary dimension, $\dim V^{\perp}=n^{2}-\dim V$.

## The Two Halves Are Orthogonal

**Proposition.** $\operatorname{tr}(SK)=0$ for every symmetric $S$ and every antisymmetric $K$.

*Proof.* $\operatorname{tr}(SK)=\operatorname{tr}((SK)^{\mathsf T})=\operatorname{tr}(K^{\mathsf T}S^{\mathsf T})=\operatorname{tr}(-KS)=-\operatorname{tr}(KS)$, and $\operatorname{tr}(KS)=\operatorname{tr}(SK)$, so the number equals its own negative.

**Measured on $100$ random pairs at each order.** At $n=2,3,4,5$ the value of $\operatorname{tr}(SK)$ differed from zero in $0$ cases out of $100$ at each order.

**So each half lies in the orthogonal complement of the other.** $\operatorname{Sym}_n\subseteq\operatorname{Skew}_n^{\perp}$ and $\operatorname{Skew}_n\subseteq\operatorname{Sym}_n^{\perp}$. Since the dimensions add to $n^{2}$,

$$
\dim\operatorname{Sym}_n+\dim\operatorname{Skew}_n=n^{2},
$$

and the form is nondegenerate, the inclusions are equalities:

$$
\operatorname{Sym}_n=\operatorname{Skew}_n^{\perp},\qquad \operatorname{Skew}_n=\operatorname{Sym}_n^{\perp}.
$$

**This is stronger than a direct sum.** A direct sum needs only $S\cap K=0$. An orthogonal complement needs the pairing to vanish between the two summands as well, and that is what the proposition supplies.

## The Inertia

**Theorem.** The trace form has inertia $(n(n+1)/2,\,n(n-1)/2)$.

*Proof.* Take the basis of $\operatorname{Sym}_n$ given by $E_{ii}$ and $E_{ij}+E_{ji}$ for $i<j$, together with the basis of $\operatorname{Skew}_n$ given by $E_{ij}-E_{ji}$ for $i<j$. The whole family is a basis of the algebra. Its elements pair diagonally, because the two halves are orthogonal and the units of each family are orthogonal among themselves:

$$
\langle E_{ii},E_{jj}\rangle=\delta_{ij},\qquad \langle E_{ij}+E_{ji},E_{ij}+E_{ji}\rangle=2,\qquad \langle E_{ij}-E_{ji},E_{ij}-E_{ji}\rangle=-2.
$$

So the Gram matrix in this basis is diagonal with $n(n+1)/2$ entries $+1$ or $+2$ and $n(n-1)/2$ entries $-2$. By Sylvester's law the inertia is the pair of counts.

**The measured values agree.** Diagonalising the Gram matrix of the matrix-unit basis gives inertia $(3,1)$, $(6,3)$, $(10,6)$, $(15,10)$ at $n=2,3,4,5$. The positive count is $n(n+1)/2$ and the negative count is $n(n-1)/2$ in each case.

**The positive and negative indices are the dimensions of the two halves.** This is not a coincidence: the halves diagonalise the form, so the index of the form is the dimension of the largest subspace on which it is positive definite, and that subspace is $\operatorname{Sym}_n$.

**The null cone is nontrivial for every $n\ge2$.** It contains every nilpotent matrix and every matrix unit $E_{ij}$ with $i\ne j$, since $\langle E_{ij},E_{ij}\rangle=\delta_{ij}\delta_{ji}=0$ for $i\ne j$. So the form is indefinite, and it is degenerate on many subspaces.

## Definiteness on Each Half

**Proposition.** The restriction of the form to $\operatorname{Sym}_n$ is positive definite, and its restriction to $\operatorname{Skew}_n$ is negative definite.

*Proof.* For symmetric $S$,

$$
\langle S,S\rangle=\operatorname{tr}(S^{2})=\sum_{i,j}S_{ij}S_{ji}=\sum_{i,j}S_{ij}^{2}\ge0,
$$

with equality exactly when $S=0$. For anti-Hermitian $K$,

$$
\langle K,K\rangle=\operatorname{tr}(K^{2})=-\sum_{i,j}K_{ij}^{2}\le0,
$$

with equality exactly when $K=0$.

**Each half is therefore an eigenspace of the form up to sign.** $\operatorname{Sym}_n$ is a maximal positive definite subspace and $\operatorname{Skew}_n$ a maximal negative definite subspace. Their dimensions are the two indices, and they are the extremal subspaces in the sense of Sylvester's law.

**The definiteness is what the real field provides.** Over $\mathbb{C}$ the numbers $S_{ij}^{2}$ are complex, no sign is defined, and the notion of a positive definite subspace disappears. The two sums above are the only place in the article where the base field $\mathbb{R}$ enters, and they carry the whole inertia.

## The Orthogonal Projections

**Definition.** Put $P_+(X)=\tfrac12(X+X^{\mathsf T})$ and $P_-(X)=\tfrac12(X-X^{\mathsf T})$.

**The two maps are projections onto the two halves along the other.** $P_+^{2}=P_+$, $P_-^{2}=P_-$, $P_+P_-=P_-P_+=0$, and $P_++P_-=\mathrm{id}$. The image of $P_+$ is $\operatorname{Sym}_n$ and its kernel is $\operatorname{Skew}_n$, and the roles are exchanged for $P_-$.

**The two maps are self-adjoint for the trace form.** The identity $\operatorname{tr}(X^{\mathsf T}Y)=\operatorname{tr}(XY^{\mathsf T})$ holds, since both sides are $\sum_{i,j}X_{ij}Y_{ij}$. Hence

$$
\langle P_+X,Y\rangle=\tfrac12\bigl(\operatorname{tr}(XY)+\operatorname{tr}(X^{\mathsf T}Y)\bigr)=\tfrac12\bigl(\operatorname{tr}(XY)+\operatorname{tr}(XY^{\mathsf T})\bigr)=\langle X,P_+Y\rangle,
$$

and the same computation gives $\langle P_-X,Y\rangle=\langle X,P_-Y\rangle$.

**A projection that is self-adjoint for a form with an orthogonal direct sum is the orthogonal projection.** For $X,Y$ arbitrary,

$$
\langle X-P_+X,\,Y\rangle=\langle P_-X,Y\rangle=\langle X,P_-Y\rangle,
$$

and $P_-Y$ lies in $\operatorname{Skew}_n$, which is orthogonal to $\operatorname{Sym}_n$. So $X-P_+X$ is orthogonal to $P_+Y$, and $P_+$ is the orthogonal projection onto $\operatorname{Sym}_n$ with kernel $\operatorname{Skew}_n$.

**The projection is the same map for both forms, and its meaning differs.** The next two sections show that the Hilbert–Schmidt form gives the same pair of projections and a different inertia.

## The Hilbert–Schmidt Form

**Definition.** $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)=\sum_{i,j}X_{ij}Y_{ij}$.

**The Hilbert–Schmidt form is an inner product.** $\operatorname{tr}(X^{\mathsf T}X)=\sum_{i,j}X_{ij}^{2}$ is positive for $X\ne0$, so the form is positive definite, and its inertia is $(n^{2},0)$. Measured on the matrix units it gives $(4,0)$ at $n=2$ and $(9,0)$ at $n=3$.

**It is not invariant.** Take $n=2$, $A=E_{12}$, $B=E_{21}$ and $C=\mathrm{I}$. Then

$$
\langle AB,C\rangle_{\mathrm{HS}}=\operatorname{tr}((E_{11})^{\mathsf T})=1,\qquad \langle A,BC\rangle_{\mathrm{HS}}=\operatorname{tr}(E_{21}E_{21})=0,
$$

so moving the factor across the comma changes the value. So the Hilbert–Schmidt form is an inner product on the algebra and not a form of the algebra.

**The two halves are still orthogonal for it.** $\operatorname{tr}(S^{\mathsf T}K)=\operatorname{tr}(SK)=0$ for symmetric $S$ and antisymmetric $K$, so the orthogonal complement statement survives. What fails is the sign: the form is positive definite on both halves, so the split is a decomposition into two positive definite pieces and not into a positive and a negative one.

**What the two forms exchange is exactly the pair of properties.** The trace form is invariant and indefinite. The Hilbert–Schmidt form is positive definite and not invariant. No form on $M_n(\mathbb{R})$ is both, and that dichotomy is one of the differences between the real and the complex algebra: over $\mathbb{C}$ the form $\operatorname{tr}(A^{*}B)$ is both.

## Two Complements, One Space

**The word complement names two different things.** The direct sum $M_n(\mathbb{R})=\operatorname{Sym}_n\oplus\operatorname{Skew}_n$ is a statement about dimensions and intersection. The orthogonal decomposition for the trace form is a statement about the pairing. In this case the two coincide, and the coincidence is what makes the two halves canonical.

**The trace form sees the two halves as a positive and a negative space, and it sees nothing else.** Any subspace on which the form is positive definite has dimension at most $n(n+1)/2$, and $\operatorname{Sym}_n$ attains the bound. Any subspace on which it is negative definite has dimension at most $n(n-1)/2$, and $\operatorname{Skew}_n$ attains that bound.

**The orthogonal complement of a half is the other half, and not a larger space.** For the trace form, $\operatorname{Sym}_n^{\perp}=\operatorname{Skew}_n$. For a degenerate restriction the complement would be larger than the other half, and the article *$UT_n$ as the Complement of the Antisymmetric Part* exhibits exactly that: the upper triangular matrices have the same dimension as $\operatorname{Sym}_n$, they meet $\operatorname{Skew}_n$ only at zero, and they are not the orthogonal complement of $\operatorname{Skew}_n$.

**The inertia is the invariant that separates the two halves from the two classes of fixed spaces.** For the symplectic fixed space the trace form is indefinite, of inertia $(2,1)$, $(6,4)$, $(12,9)$ at $n=2,4,6$, while for $\operatorname{Sym}_n$ it is definite. So the pair of indices, and not the dimension, is the marker of the orthogonal class.

## Summary

The trace form $\langle X,Y\rangle=\operatorname{tr}(XY)$ is symmetric, nondegenerate and invariant, and its inertia is $(n(n+1)/2,n(n-1)/2)$, measured as $(3,1)$, $(6,3)$, $(10,6)$, $(15,10)$ at $n=2,3,4,5$. The symmetric and antisymmetric halves are orthogonal for it, $\operatorname{tr}(SK)=0$, and since their dimensions add to $n^{2}$ each is the exact orthogonal complement of the other. The restriction is positive definite on $\operatorname{Sym}_n$ and negative definite on $\operatorname{Skew}_n$, and the two sums of squares that prove it are where the real base field enters. The maps $X\mapsto\tfrac12(X\pm X^{\mathsf T})$ are the trace-form orthogonal projections, self-adjoint for the form. The Hilbert–Schmidt form $\operatorname{tr}(X^{\mathsf T}Y)$ is positive definite with inertia $(n^{2},0)$ and is not invariant, so it keeps the orthogonal split and loses the inertia.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the trace form, of inertia $(n(n+1)/2,n(n-1)/2)$ |
| $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$ | the Hilbert–Schmidt form, positive definite |
| $\operatorname{Sym}_n$ | the positive definite half, of dimension $n(n+1)/2$ |
| $\operatorname{Skew}_n$ | the negative definite half, of dimension $n(n-1)/2$ |
| $V^{\perp}$ | the orthogonal complement of $V$ for the trace form, of dimension $n^{2}-\dim V$ |
| $P_{\pm}(X)=\tfrac12(X\pm X^{\mathsf T})$ | the trace-form orthogonal projections onto the two halves |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the trace, the transpose and the symmetrisation of a matrix.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the trace form of an associative algebra and its invariance.
- [The Two Halves: Symmetric and Antisymmetric](the-two-halves-symmetric-and-antisymmetric-over-r.html), for the two subspaces and their products.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace form and its inertia stated without proof.
- [$UT_n$ as the Complement of the Antisymmetric Part](utn-as-the-complement-of-the-antisymmetric-part-over-r.html), for a complement that is not orthogonal.
