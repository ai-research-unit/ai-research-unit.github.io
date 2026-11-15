# __The Two Halves and Their Topology at $n=4$__

## Introduction

**The complex matrix space splits as $\operatorname{Herm}_4\oplus\mathfrak{u}(4)$ into two real sixteen-dimensional halves, and the polar decomposition contracts the first onto the second, so $\mathrm{GL}_4(\mathbb{C})\simeq U(4)$; over the reals the symmetric half has dimension ten and the antisymmetric half six, the singular set of each is a hypersurface, the invertible symmetric matrices have five components indexed by inertia, and the invertible skew matrices have two indexed by the sign of the Pfaffian.**

The article proves the two decompositions, computes the dimensions, identifies the singular sets as the zero sets of the determinant and of the Pfaffian, counts the components of the invertible halves, identifies the halves with homogeneous spaces of the general linear group, and writes the contraction that reduces the topology of $\mathrm{GL}_4(\mathbb{C})$ to that of $U(4)$.

It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric*, *The Two Halves as Orthogonal Complements* and *The Hilbert–Schmidt Form at $n=4$*. The model at order two is *The Two Halves and Their Topology at $n=2$*; the homotopy groups are *The Homotopy of $\mathrm{GL}_4(\mathbb{C})$ and of the Two Halves*.

## The Two Decompositions of the Complex Space

**Definition.** $\operatorname{Herm}_4=\{A:A^{\ast}=A\}$ and $\mathfrak{u}(4)=\{A:A^{\ast}=-A\}$.

**Proposition.** $\operatorname{Herm}_4$ and $\mathfrak{u}(4)$ are real vector spaces of real dimension $16$ each, and
$$
M_4(\mathbb{C})=\operatorname{Herm}_4\oplus\mathfrak{u}(4)
$$
as real vector spaces, with the projections $\tfrac12(A+A^{\ast})$ and $\tfrac12(A-A^{\ast})$.

**Proof.** A Hermitian matrix has four real diagonal entries and six complex off-diagonal ones, so $4+12=16$ real parameters; the same count for the anti-Hermitian ones with the diagonal purely imaginary; the two projections are idempotent, have the two spaces as images and add to the identity.

**Corollary.** The real dimension of $M_4(\mathbb{C})$ is $32$, twice the dimension of each half.

**Proof.** $16+16=32$.

**Corollary.** The two halves are orthogonal for the Hilbert–Schmidt form but not for the trace form.

**Proof.** $\operatorname{tr}(H^{\ast}K)=\operatorname{tr}(HK)$ vanishes for $H$ Hermitian and $K$ anti-Hermitian because the product is anti-Hermitian with real trace; the trace pairing restricted to the two halves is indefinite.

**Corollary.** The decomposition is the eigenspace decomposition of the involution $A\mapsto A^{\ast}$, with eigenvalues $+1$ and $-1$.

**Proof.** The two fixed and anti-fixed spaces of an involution.

## The Singular Sets

**Definition.** The **singular set** of a half is the set of its elements that are not invertible.

**Proposition.** In $\operatorname{Herm}_4$ the singular set is $\{\det A=0\}$, a real hypersurface, and in $\mathfrak{u}(4)$ it is $\{\det A=0\}$, also a real hypersurface.

**Proof.** The determinant is a polynomial function of the real coordinates on each half, nonzero as a polynomial, so its zero set is a hypersurface; and the two halves are real vector spaces of dimension sixteen, so a hypersurface has dimension fifteen.

**Corollary.** The invertible elements of each half form the complement of a hypersurface, hence are dense and open.

**Proof.** A hypersurface has empty interior and is closed.

**Corollary.** The singular set of $\operatorname{Herm}_4$ is the cone over the set of singular Hermitian matrices of norm one, and it is the boundary of the positive cone together with the boundary of its negative.

**Proof.** Scale invariance of the determinant and the spectral description of the boundary.

**The real halves.** In the real Symmetric half of dimension $10$ the singular set is $\{\det=0\}$, a hypersurface of dimension nine; in the real antisymmetric half of dimension $6$ it is $\{\operatorname{Pf}=0\}$ or equivalently $\{\det=0\}$, a hypersurface of dimension five.

**Proof.** The Pfaffian squares to the determinant, and both are nonconstant polynomials.

**Corollary.** A real skew matrix of order four is singular exactly when one of its two angles vanishes, since $\det=\theta_1^{2}\theta_2^{2}$.

**Proof.** The normal form of the real skew matrix.

## The Components of the Invertible Halves

**Theorem.** The invertible real symmetric matrices of order four form five connected components, indexed by the inertia $(p,q)$ with $p+q=4$.

**Proof.** The inertia is locally constant and invariant under congruence, so it is constant on each component; conversely, two symmetric matrices with the same inertia are related by a congruence with an invertible matrix, and $\mathrm{GL}_4(\mathbb{R})$ has two components which act transitively on each inertia class once joined with the orthogonal group, so each class is connected.

**Corollary.** The sign of the determinant groups the five components into three with $\det>0$, namely $(4,0)$, $(2,2)$ and $(0,4)$, and two with $\det<0$, namely $(3,1)$ and $(1,3)$; the sign of the determinant alone does not separate the components.

**Proof.** $\det$ has the sign $(-1)^{q}$.

**Theorem.** The invertible real antisymmetric matrices of order four form exactly two components, distinguished by the sign of the Pfaffian.

**Proof.** $\operatorname{Pf}^{2}=\det$ is nonzero, so the Pfaffian is a continuous function into $\mathbb{R}\setminus\{0\}$, which forces at least two components; and a skew matrix with a given sign of the Pfaffian is carried to the standard form by a congruence with positive determinant, so each sign class is connected.

**Corollary.** The two components of the invertible skew half are the two orientations of the pair of rotations, and the Pfaffian is the obstruction to connecting them.

**Proof.** The sign of the Pfaffian changes under an orientation-reversing congruence and does not change under an orientation-preserving one.

**The symmetric contrast.** The symmetric half has more components because the inertia has more freedom; the skew half has only two because the spectrum of a real skew matrix is forced into conjugate pairs.

**Proof.** The two theorems.

## The Homogeneous Spaces

**Proposition.** Each inertia class of invertible real symmetric matrices is the homogeneous space $\mathrm{GL}_4(\mathbb{R})/O(p,q)$ of dimension $10$, and the invertible skew matrices form $\mathrm{GL}_4(\mathbb{R})/\mathrm{Sp}_4(\mathbb{R})$ up to the two components, of dimension $6$.

**Proof.** The stabiliser of a fixed symmetric form of inertia $(p,q)$ is the corresponding orthogonal group, of dimension $6$; the stabiliser of a nondegenerate skew form is the symplectic group, of dimension $10$; the orbit-stabiliser theorem with $\dim\mathrm{GL}_4(\mathbb{R})=16$ gives $16-6=10$ and $16-10=6$.

**Corollary.** $\dim O(p,q)=6$, $\dim\mathrm{Sp}_4(\mathbb{R})=10$ and $\dim\mathrm{GL}_4(\mathbb{R})=16$, so the symmetric orbit has dimension ten and the skew orbit six.

**Proof.** The dimensions of the classical groups of order four.

**The complex analogue.** Over $\mathbb{C}$ the invertible symmetric matrices form the single orbit $\mathrm{GL}_4(\mathbb{C})/O(4,\mathbb{C})$ of complex dimension $10$, and the invertible skew matrices the single orbit $\mathrm{GL}_4(\mathbb{C})/\mathrm{Sp}_4(\mathbb{C})$ of complex dimension $6$.

**Proof.** Over $\mathbb{C}$ every nondegenerate symmetric form is congruent to the standard one, so there is one orbit; the same orbit-stabiliser count gives the dimensions, with $\dim\mathrm{GL}_4(\mathbb{C})=16$.

**Corollary.** Over $\mathbb{C}$ each half is connected, and the multiplicity of components in the real case is the multiplicity of the real inertia; over $\mathbb{C}$ the inertia disappears.

**Proof.** One orbit each, and the real classification by inertia.

## The Contraction

**Theorem.** The polar decomposition gives a diffeomorphism $\operatorname{Herm}_4^{++}\times U(4)\to\mathrm{GL}_4(\mathbb{C})$, and $\operatorname{Herm}_4^{++}$ is convex, hence contractible.

**Proof.** The polar decomposition of an element and the convexity of the open cone of positive definite Hermitian matrices.

**Corollary.** $\mathrm{GL}_4(\mathbb{C})$ is homotopy equivalent to $U(4)$, and $\dim_{\mathbb{R}}\mathrm{GL}_4(\mathbb{C})=32=\dim_{\mathbb{R}}\operatorname{Herm}_4^{++}+\dim_{\mathbb{R}}U(4)=16+16$.

**Proof.** A product with a contractible factor is homotopy equivalent to the other factor.

**Corollary.** Over the reals, $\mathrm{GL}_4(\mathbb{R})\simeq O(4)$, with $\dim_{\mathbb{R}}\mathrm{GL}_4(\mathbb{R})=16=\dim\operatorname{Sym}_4^{++}+\dim O(4)=10+6$.

**Proof.** The real polar decomposition $A=HU$ with $H$ positive definite symmetric and $U$ orthogonal.

**The inconsistent count.** The product $\operatorname{Sym}_4^{++}\times U(4)$ does not give $\mathrm{GL}_4(\mathbb{C})$: its dimension would be $10+16=26$, not $32$. The correct contraction pairs $\operatorname{Herm}_4^{++}$ with $U(4)$, and the real symmetric cone pairs with the real orthogonal group.

**Proof.** The dimension count of the two products.

**Corollary.** The two halves of the complex space are of real dimension sixteen, equal to the dimension of $U(4)$, so the contraction is dimensionally balanced; the real symmetric half of dimension ten pairs with $O(4)$ of dimension six.

**Proof.** The two dimension counts.

**The two-sided return.** The contraction is not an accident of coordinates: the polar decomposition is the statement that every element is a stretch times a rotation, and the stretch is the exponential of the Hermitian half.

**Proof.** The exponential of the Hermitian half is a diffeomorphism onto the open cone.

## Summary

The complex matrix space splits into the Hermitian and the anti-Hermitian halves, each of real dimension sixteen, and the split is the eigenspace decomposition of the adjoint involution. The singular set of each half is a hypersurface, the zero set of the determinant.

The invertible real symmetric matrices have five components indexed by inertia, grouped by the sign of the determinant into three and two, so the sign of the determinant alone does not separate them; the invertible real skew matrices have two components indexed by the sign of the Pfaffian. Each class is a homogeneous space of the general linear group.

The polar decomposition contracts the positive definite cone onto a point and leaves the unitary group, so $\mathrm{GL}_4(\mathbb{C})\simeq U(4)$, and over the reals $\mathrm{GL}_4(\mathbb{R})\simeq O(4)$. The dimension count must pair the Hermitian cone of dimension sixteen with $U(4)$, not the real symmetric cone of dimension ten.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_4$, $\mathfrak{u}(4)$ | the two halves, real dimension $16$ each |
| $\{\det=0\}$ | the singular set, a hypersurface |
| $(p,q)$, $p+q=4$ | the inertia of a real symmetric matrix |
| $\operatorname{Pf}$ | the Pfaffian of a real skew matrix |
| $\mathrm{GL}_4/O(p,q)$ | the homogeneous space of an inertia class |
| $\operatorname{Herm}_4^{++}\times U(4)\cong\mathrm{GL}_4$ | the contraction |

## Further Reading

- James R. Munkres, *Topology* (Pearson, 2000), for components and hypersurfaces.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-4.html), for the two real halves and the projections.
- [The Homotopy of $\mathrm{GL}_4(\mathbb{C})$ and of the Two Halves](the-homotopy-of-gl4c-and-of-the-two-halves.html), for the homotopy groups computed from this contraction.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$](the-exponential-of-sym-4-stretches-and-the-positive-cone.html), for the exponential and the polar decomposition.
- [The Two Halves and Their Topology at $n=2$](the-two-halves-and-their-topology-at-n-2.html), for the case at order two.
