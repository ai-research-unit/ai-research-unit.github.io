# __Symmetric Pairs and Cartan Pairs: the Reductivity Criterion at $n=4$__

## Introduction

**The pair $(\mathfrak{gl}_4,\mathfrak{so}(4))$ with complement $\operatorname{Sym}_4$ satisfies the three bracket conditions, and it is symmetric because $\mathfrak{so}(4)$ is the fixed set of the involution $\theta(X)=-X^{\mathsf T}$; the pair $(\mathfrak{b},\mathfrak{h})$ satisfies the same three conditions and is not symmetric, which is exactly where the criterion needs reductivity.**

The article states the three conditions, verifies them for the two pairs $(\mathfrak{gl}_4,\mathfrak{so}(4))$ and $(\mathfrak{sl}_4,\mathfrak{so}(4))$, produces the Cartan involution and its two eigenspaces, proves the criterion that a reductive pair with the three conditions comes from an involution, shows the Borel pair as the counterexample that fails without reductivity, and records the symmetric spaces and their dimensions.

It assumes *The Two Halves as Orthogonal Complements at $n=4$* and *The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$*. The case $n=2$ is *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion at $n=2$*. The global picture is *The Symmetric Space $\mathrm{GL}_4/O(4)$ and Its Complex Twin*.

## The Three Bracket Conditions

**Definition.** A **symmetric pair** is a Lie algebra $\mathfrak{g}$ with a decomposition $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ into subspaces such that

$$
[\mathfrak{k},\mathfrak{k}]\subset\mathfrak{k},\qquad [\mathfrak{k},\mathfrak{p}]\subset\mathfrak{p},\qquad [\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}.
$$

**Proposition.** For $\mathfrak{k}=\operatorname{Skew}_4$ and $\mathfrak{p}=\operatorname{Sym}_4$ all three inclusions hold.

**Proof.** Let $K,K'$ be antisymmetric and $S,S'$ symmetric. Then $(KK'-K'K)^{\mathsf T}=K'{}^{\mathsf T}K^{\mathsf T}-K^{\mathsf T}K'{}^{\mathsf T}=K'K-KK'$, so the commutator of two antisymmetric matrices is antisymmetric. Next, $(KS-SK)^{\mathsf T}=S^{\mathsf T}K^{\mathsf T}-K^{\mathsf T}S^{\mathsf T}=-SK+KS$, so the commutator of an antisymmetric and a symmetric matrix is symmetric. Finally $(SS'-S'S)^{\mathsf T}=S'S-SS'$, so the commutator of two symmetric matrices is antisymmetric.

**Corollary.** $\mathfrak{so}(4)=\operatorname{Skew}_4$ is a Lie subalgebra of dimension $6$, $\operatorname{Sym}_4$ is a $\mathfrak{so}(4)$-module of dimension $10$, and the bracket of two symmetric matrices lands in $\mathfrak{so}(4)$.

**Proof.** The three inclusions with the dimensions $6$ and $10$.

**The same for the traceless algebra.** With $\mathfrak{sl}_4$ in place of $\mathfrak{gl}_4$ the decomposition is $\mathfrak{so}(4)\oplus\operatorname{Sym}_4^{0}$, of dimensions $6+9=15$, since an antisymmetric matrix is automatically traceless.

**Proof.** The trace of a commutator is zero, so both bracketed pieces stay traceless; the symmetric part is cut down by the traceless condition, from $10$ to $9$.

**The failure of the naive complement.** $\operatorname{Sym}_4$ itself is not a subalgebra, so the pair is not a direct sum of Lie algebras; and $\mathfrak{gl}_4$ is not the product $\mathfrak{so}(4)\times\operatorname{Sym}_4$ even as a vector space with brackets, because $[\mathfrak{p},\mathfrak{p}]\neq0$.

## The Cartan Involution

**Theorem.** The map $\theta(X)=-X^{\mathsf T}$ is an involutive automorphism of the Lie algebra $\mathfrak{gl}_4(\mathbb{C})$, with fixed set $\mathfrak{so}(4)$ and $(-1)$-eigenspace $\operatorname{Sym}_4$.

**Proof.** $\theta^{2}=\mathrm{id}$ is clear, and

$$
\theta[X,Y]=-(XY-YX)^{\mathsf T}=-(Y^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}Y^{\mathsf T})=(-X^{\mathsf T})(-Y^{\mathsf T})-(-Y^{\mathsf T})(-X^{\mathsf T})=[\theta X,\theta Y].
$$

The fixed equation $-X^{\mathsf T}=X$ is antisymmetry, and $-X^{\mathsf T}=-X$ is symmetry.

**Corollary.** An involution of $\mathfrak{g}$ always produces a symmetric pair by its two eigenspaces.

**Proof.** For an automorphism $\theta$ with $\theta^{2}=\mathrm{id}$, the eigenspaces satisfy $[\mathfrak{g}_\varepsilon,\mathfrak{g}_\delta]\subset\mathfrak{g}_{\varepsilon\delta}$; with $\varepsilon,\delta=\pm1$ this is the table of the three conditions.

**The form and the involution agree.** For the trace pairing, $\beta(\mathfrak{k},\mathfrak{p})=0$, and $\beta(\theta X,Y)=-\beta(X,\theta Y)$; the Cartan involution is symmetric for $\beta$.

**Proof.** $\beta(KS)=\operatorname{tr}(KS)=0$ was proved in the orthogonal-complement article, and $\beta(\theta X,Y)=\operatorname{tr}(-X^{\mathsf T}Y)=-\operatorname{tr}(X^{\mathsf T}Y)=-\beta(X,\theta Y)$ since $\operatorname{tr}(X^{\mathsf T}Y^{\mathsf T})=\operatorname{tr}(XY)$ after transposing.

**The signs of the pairing on the two pieces.** On $\mathfrak{so}(4)$ the trace form is negative definite, since $\operatorname{tr}(K^{2})=-2\sum_{i<j}k_{ij}^{2}$; on $\operatorname{Sym}_4$ it is positive semidefinite in the full algebra, with radical $\mathbb{C}\mathrm I_4$, and positive definite on the traceless part.

**Proof.** The first display was computed on the antisymmetric half. For symmetric $S$, $\operatorname{tr}(S^{2})=\sum_{ij}s_{ij}^{2}\ge0$, with equality exactly when $S=0$; the form $\beta$ pairs $\mathrm I_4$ with every symmetric matrix through $\operatorname{tr}S$, so the radical on $\operatorname{Sym}_4$ is the line of scalars.

## The Criterion

**Definition.** A pair $(\mathfrak{g},\mathfrak{k})$ is **reductive** when $\mathfrak{k}$ has an $\operatorname{ad}_{\mathfrak{k}}$-invariant complement, equivalently when $\mathfrak{g}$ is reductive and $\mathfrak{k}$ is reductive in it.

**Theorem (the reductivity criterion).** Let $\mathfrak{g}$ be reductive and $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ with the three bracket conditions. Then the linear map $\theta=+\mathrm{id}$ on $\mathfrak{k}$ and $-\mathrm{id}$ on $\mathfrak{p}$ is an automorphism of $\mathfrak{g}$.

**Proof.** Bilinearity reduces the check $\theta[X,Y]=[\theta X,\theta Y]$ to the three inclusions, using the sign table: $[+k,+k]=+[k,k]$, $[+k,-p]=-[k,p]$, $[-p,-p]=+[p,p]$. Each bracket lands in the piece required by the conditions, with the sign required by the eigenvalues.

**Corollary.** For a reductive algebra the three conditions are equivalent to being the pair of eigenspaces of an involution, so the symmetric pairs of a reductive algebra are exactly its involutions.

**Proof.** One direction is the corollary above; the other is the theorem.

**Where the proof uses reductivity.** Nothing in the sign table uses it; what reductivity supplies is the existence of the complement $\mathfrak{p}$ as an $\operatorname{ad}_{\mathfrak{k}}$-module and the nondegeneracy that makes such complements behave. Without it the three conditions can hold while no involution exists, which is the next section.

## The Cartan Pair That Is Not Symmetric

**Definition.** A **Cartan pair** is a pair $(\mathfrak{g},\mathfrak{h})$ with $\mathfrak{h}$ a Cartan subalgebra of $\mathfrak{g}$; for $\mathfrak{g}=\mathfrak{b}$ the diagonal $\mathfrak{h}$ is such a subalgebra.

**Proposition.** With $\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}_+$ the three bracket conditions hold: $[\mathfrak{h},\mathfrak{h}]\subset\mathfrak{h}$, $[\mathfrak{h},\mathfrak{n}_+]\subset\mathfrak{n}_+$ and $[\mathfrak{n}_+,\mathfrak{n}_+]\subset\mathfrak{n}_+$.

**Proof.** The diagonal is abelian; the bracket of a diagonal with an upper unit is a multiple of that unit; and the product of two strictly upper triangular matrices is strictly upper triangular.

**Proposition.** The pair $(\mathfrak{b},\mathfrak{h})$ with complement $\mathfrak{n}_+$ is not symmetric: there is no involutive automorphism of $\mathfrak{b}$ with fixed set $\mathfrak{h}$ and $(-1)$-eigenspace $\mathfrak{n}_+$.

**Proof.** The candidate is $\theta=+\mathrm{id}$ on $\mathfrak{h}$ and $-\mathrm{id}$ on $\mathfrak{n}_+$. It is not an automorphism, because for $N,N'\in\mathfrak{n}_+$ it would require $[\theta N,\theta N']=[N,N']$ to equal $\theta[N,N']=-[N,N']$, forcing $[\mathfrak{n}_+,\mathfrak{n}_+]=0$, which is false at order four since $[E_{12},E_{23}]=E_{13}$.

**Corollary.** The reductivity hypothesis in the criterion cannot be dropped, and the third condition $[\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}$ fails here: $[\mathfrak{n}_+,\mathfrak{n}_+]\subset\mathfrak{n}_+=\mathfrak{p}$.

**Proof.** The computation of the bracket of two units above shows the failure of the third inclusion, and a symmetric pair would need it.

**What the example teaches.** A Cartan pair is a statement about a maximal torus and a root decomposition; a symmetric pair is a statement about an involution. At order four the first is realised by the Borel with the diagonal, the second by the whole algebra with the antisymmetric part, and the two notions coincide only under reductivity.

## The Symmetric Spaces

**The real pairs.** $\mathrm{GL}_4(\mathbb{R})/O(4)$ has dimension $16-6=10$ and $\mathrm{SL}_4(\mathbb{R})/SO(4)$ has dimension $15-6=9$, with tangent spaces $\operatorname{Sym}_4(\mathbb{R})$ and $\operatorname{Sym}_4^{0}(\mathbb{R})$.

**Proof.** The dimension of a homogeneous space is the difference of the dimensions, and the tangent space at the identity coset is the complement $\mathfrak{p}$.

**The complex pair.** $\mathrm{GL}_4(\mathbb{C})/O(4,\mathbb{C})$ has complex dimension $10$ and real dimension $20$; the involution $\theta$ is $\mathbb{C}$-linear, so the complex theory runs in parallel.

**Proof.** The complex dimensions are $16-6=10$, and the real dimension is twice that.

**The compact dual.** $U(4)/O(4)$ is the compact form of the same pair, with the same tangent space $\operatorname{Sym}_4$ but the opposite sign of the curvature; it is the fixed set of the conjugation composed with $\theta$.

**Proof.** The Cartan decomposition of $\mathfrak{u}(4)$ with respect to the same $\theta$ gives $\mathfrak{so}(4)\oplus i\operatorname{Sym}_4$, and $i\operatorname{Sym}_4$ is the tangent space of $U(4)/O(4)$ at the identity.

## Summary

The three bracket conditions $[\mathfrak{k},\mathfrak{k}]\subset\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subset\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}$ hold for $\mathfrak{k}=\mathfrak{so}(4)$ and $\mathfrak{p}=\operatorname{Sym}_4$, in the full algebra and in the traceless one, of dimensions $6+10=16$ and $6+9=15$.

They hold because $\mathfrak{so}(4)$ is the fixed set of the involution $\theta(X)=-X^{\mathsf T}$, whose other eigenspace is $\operatorname{Sym}_4$; for a reductive algebra the three conditions are equivalent to coming from such an involution. The trace pairing is symmetric for $\theta$, negative definite on $\mathfrak{so}(4)$, and positive definite on the traceless symmetric part.

The Borel pair $(\mathfrak{b},\mathfrak{h})$ satisfies the same three conditions only in part and is not symmetric, since $[\mathfrak{n}_+,\mathfrak{n}_+]\subset\mathfrak{n}_+$ breaks the third. The symmetric spaces are $\mathrm{GL}_4/O(4)$ and $\mathrm{SL}_4/SO(4)$, of dimensions $10$ and $9$, with the compact dual $U(4)/O(4)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{k}$, $\mathfrak{p}$ | the two pieces of a symmetric pair |
| $\theta(X)=-X^{\mathsf T}$ | the Cartan involution |
| $\operatorname{Sym}_4^{0}$ | the traceless symmetric matrices, dimension $9$ |
| $\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}_+$ | the Borel, a Cartan pair but not symmetric |
| $\beta(X,Y)=\operatorname{tr}(XY)$ | the trace pairing |
| $\mathrm{GL}_4/O(4)$ | the symmetric space of dimension $10$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for symmetric pairs, Cartan involutions and the reductivity criterion.
- Anthony Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the classification of real reductive pairs and the compact dual.
- [The Two Halves as Orthogonal Complements at $n=4$](the-two-halves-as-orthogonal-complements-at-n-4.html), for the orthogonality of $\mathfrak{k}$ and $\mathfrak{p}$.
- [The Symmetric Space $\mathrm{GL}_4/O(4)$ and Its Complex Twin](the-symmetric-space-gl4-o4-and-its-complex-twin.html), for the global object attached to this pair.
- [Symmetric Pairs and Cartan Pairs: the Reductivity Criterion at $n=2$](symmetric-pairs-and-cartan-pairs-the-reductivity-criterion-at-n-2.html), for the same criterion at order two.
