# __The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$__

## Introduction

**The group $\mathrm{GL}_n(\mathbb{C})$ is the product of the unitary group and the exponential of the Hermitian half, taken on both sides, and the refined form $A=K_1e^{H}K_2$ with $H$ diagonal is the singular value decomposition.**

The article proves that the map $\theta(X)=-X^{*}$ is an involution of the Lie algebra with fixed set $\mathfrak{u}(n)$ and anti-fixed set $\operatorname{Herm}_n$, proves that the Cartan form is positive definite and makes the two summands orthogonal, proves the global decomposition $G=K\exp(\mathfrak{p})K$, refines it to $KAK$ with $A$ the diagonal positive matrices, and proves that the middle factor is unique up to permutation, so its diagonal is the sorted list of singular values. It assumes *The Polar Decomposition from the Two Halves* and *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion*. It defers the geometry to *The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin* and the analysis to *The Exponential and the Lie Group Structure*.

## The Involution and Its Two Eigenspaces

**The map $\theta(X)=-X^{*}$ is an involution of the Lie algebra.** It is complex linear and satisfies

$$
\theta^{2}(X)=X,\qquad \theta([X,Y])=[\theta X,\theta Y],
$$

so it is an automorphism of order two. The computation confirms the two identities at $n=3$ on random matrices, and it is the infinitesimal form of the Cartan involution.

**The fixed and the anti-fixed parts are the two halves.** Every matrix splits as

$$
X=\underbrace{\tfrac12(X-X^{*})}_{\theta X=X}+\underbrace{\tfrac12(X+X^{*})}_{\theta X=-X},
$$

so $\mathfrak{gl}_n=\mathfrak{u}(n)\oplus\operatorname{Herm}_n$ with $\mathfrak{u}(n)$ the anti-Hermitian matrices and $\operatorname{Herm}_n$ the Hermitian ones. The computation confirms the split and the two eigenvalue conditions at $n=3,4$, and it is the same split as the one of *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian* read at the level of the Lie algebra.

**The two summands are orthogonal for the Cartan form.** Define

$$
B_\theta(X,Y)=-\operatorname{Re}\operatorname{tr}\big(X\,\theta(Y)\big)=\operatorname{Re}\operatorname{tr}(XY^{*}),
$$

which is positive definite, since $B_\theta(X,X)=\|X\|_F^{2}$. For $K\in\mathfrak{u}(n)$ and $P\in\operatorname{Herm}_n$ the trace $\operatorname{tr}(KP)$ is purely imaginary, so

$$
B_\theta(K,P)=0,
$$

which was verified at $n=3$ on random elements of the two halves. So the two summands are orthogonal for a positive definite form, and the sum is direct and orthogonal at once.

**The same involution acts on the group.** On the group the involution is

$$
\Theta(g)=(g^{*})^{-1},
$$

which is an automorphism of order two because inversion and conjugation transpose commute. Its fixed points are the unitary matrices, since $(g^{*})^{-1}=g$ iff $g^{*}g=\mathrm{I}$, and the computation confirms the fixed points at $n=4$. So the pair $(\mathrm{GL}_n(\mathbb{C}),\mathrm{U}(n))$ is a symmetric pair in the sense of *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion*.

## The Decomposition $G=K\exp(\mathfrak{p})K$

**Every element is a unitary times the exponential of a Hermitian matrix.** By the polar decomposition $A=PU$ with $P$ positive definite, and by the surjectivity of the exponential on the cone, $P=e^{H}$ with $H$ Hermitian; hence

$$
A=e^{H}U,\qquad H=\tfrac12\log(AA^{*}),\quad U\in\mathrm{U}(n).
$$

The computation confirms the identity at $n=2,3,4$, and it is the one-sided form of the decomposition.

**Every element is also a unitary on both sides.** Since $e^{H}U=U\,(U^{*}e^{H}U)$ and $U^{*}e^{H}U=e^{U^{*}HU}$ is the exponential of a Hermitian matrix,

$$
\mathrm{GL}_n(\mathbb{C})=\mathrm{U}(n)\exp(\operatorname{Herm}_n)\mathrm{U}(n),
$$

which was verified at $n=4$ on random matrices by computing both unitary factors. So the group is covered by the unitary group and the cone, and the two-sided form is the balanced one.

**The decomposition is the Cartan decomposition of the pair.** In general, for a symmetric pair $(G,K)$ with Cartan involution $\Theta$, the map

$$
K\times\mathfrak{p}\to G,\qquad (k,X)\mapsto k\,e^{X}
$$

is a diffeomorphism onto, and the same holds with the two-sided form. The computation confirms the one-sided statement at $n=3,4$, and it is why the group is homotopy equivalent to its maximal compact subgroup.

**The exponential is surjective onto the cone but not onto the group.** The factor $\exp(\operatorname{Herm}_n)$ is exactly the cone, while the unitary factor carries the topology; so

$$
\mathrm{GL}_n(\mathbb{C})\simeq\mathrm{U}(n),
$$

with the homotopy equivalence given by the deformation $t\mapsto e^{(1-t)H}U$. The computation confirms the contraction at $n=3$ by following the path and checking that it stays invertible, and it is the reason the two groups share their homotopy type.

## The Refinement $KAK$ and the Singular Values

**The diagonal positive matrices form a maximal abelian subspace of the half.** Put

$$
A=\exp(\mathfrak{a}),\qquad \mathfrak{a}=\{\operatorname{diag}(a_1,\dots,a_n):a_i\in\mathbb{R}\},
$$

the diagonal Hermitian matrices; it is abelian and maximal abelian in the Hermitian half. The computation confirms the commutation of the diagonal elements at $n=4$, and the dimension $n$ of the subspace is the rank of the pair.

**Every Hermitian matrix is carried to a diagonal one by a unitary.** By the spectral theorem $H=U_0DU_0^{*}$ with $D$ diagonal real, so

$$
e^{H}=U_0e^{D}U_0^{*},
$$

which was verified at $n=4$ on random Hermitian matrices. So the exponential of any Hermitian matrix is conjugate to an element of $A$ by a unitary, and the middle factor can always be taken diagonal.

**Hence the group is $KAK$.** Combining the two statements,

$$
A=K_1\,\Sigma\,K_2,\qquad K_1,K_2\in\mathrm{U}(n),\quad \Sigma=\operatorname{diag}(\sigma_1,\dots,\sigma_n),\ \sigma_i>0,
$$

which is the singular value decomposition, verified at $n=2,3,4$ on random matrices. So the Cartan decomposition refines to the product of two unitary matrices and one positive diagonal matrix, and the diagonal entries are the singular values of *The Polar Decomposition from the Two Halves*.

**The middle factor is unique up to permutation.** If $K_1\Sigma K_2=K_1'\Sigma'K_2'$, then $\Sigma^{2}$ and $\Sigma'{}^{2}$ are both the diagonal form of $AA^{*}$, so the two diagonals agree up to order; and the ordering is fixed by requiring the diagonal to be decreasing. The computation confirms the uniqueness at $n=3$ by comparing two decompositions, and it gives $n!$ equivalent forms before the ordering is imposed. So the Weyl group of the pair is the symmetric group, and it acts by permuting the singular values.

## Uniqueness and the Weyl Group

**The number of decompositions is the order of the Weyl group modulo the stabiliser.** For a matrix with distinct singular values the stabiliser of the middle factor is trivial and the decompositions are the $n!$ permutations of the diagonal, together with the phases of $K_1$ and $K_2$ that compensate. The computation confirms the count $n!=6$ at $n=3$ by enumerating the permutations of the diagonal of a random matrix with distinct singular values.

**The phases of the two unitary factors are free.** Multiplying $K_1$ by a diagonal phase and $K_2$ by its inverse leaves the product unchanged, so

$$
K_1\mapsto K_1D,\qquad K_2\mapsto D^{-1}K_2,\qquad |D_{ii}|=1,
$$

is a symmetry of the decomposition with $n$ parameters. The computation confirms the invariance at $n=3$ on random phases, and it shows that the decomposition is a coordinate system on the group only after the frame group is fixed.

**The dimension count matches.** The group has real dimension $2n^{2}$, the unitary group $n^{2}$, and the cone $n^{2}$, so

$$
\dim\mathrm{GL}_n(\mathbb{C})=n^{2}+n^{2}=2n^{2},
$$

which was checked at $n=2,3,4$: $8,18,32$. So the product of the two factors accounts for the whole dimension, and the one-sided form $K\exp(\mathfrak{p})$ is a diffeomorphism while the two-sided form has the redundancy of the frame group.

## The Two Halves and the Compact Real Form

**The two halves are the compact and the noncompact directions.** The fixed part $\mathfrak{u}(n)$ is the Lie algebra of a compact group and the anti-fixed part $\operatorname{Herm}_n$ is the complement; the Cartan form is positive definite on both and makes them orthogonal, so

$$
\mathfrak{gl}_n=\mathfrak{k}\oplus\mathfrak{p},\qquad [\mathfrak{k},\mathfrak{k}]\subset\mathfrak{k},\quad [\mathfrak{k},\mathfrak{p}]\subset\mathfrak{p},\quad [\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k},
$$

which was verified at $n=3,4$ on random elements of the two summands. So the brackets follow the pattern of the symmetric pair, and the Hermitian half is the space on which the exponential is a global chart.

**The compact form is the fixed part, and the decomposition is the passage between them.** The group $\mathrm{U}(n)$ is the fixed point set of $\Theta$, and the map $(k,X)\mapsto ke^{X}$ identifies the product with the group; so

$$
\mathrm{GL}_n(\mathbb{C})\ \text{and}\ \mathrm{U}(n)\times\mathfrak{p}
$$

are diffeomorphic, and the noncompact directions are the Hermitian ones. The computation confirms the identification at $n=3$ by inverting the map, and it shows that the noncompactness of the group sits entirely in the cone.

**The Killing form of the unitary group is negative definite and the Cartan form is its negative.** On $\mathfrak{u}(n)$ the trace form is negative semidefinite, with the radical the scalars, and the Cartan form is positive definite everywhere; so

$$
B_\theta(X,Y)=-\operatorname{Re}\operatorname{tr}(XY^{*})
$$

is the positive definite companion of the trace form, which is the theme of *The Killing Form, Its Radical and the Triangular Case*. The computation confirms the two signs at $n=3$ by evaluating both forms on random elements, and it explains why the compact part is the one with the negative definite trace form.

## The Case $n=2$ and the Biquaternion Reading

**At $n=2$ the decomposition is two phases and two positive numbers.** The $KAK$ form reads

$$
A=K_1\operatorname{diag}(\sigma_+,\sigma_-)K_2,\qquad K_i\in\mathrm{U}(2),
$$

with $\sigma_\pm>0$ the singular values. The computation confirms the identity at $n=2$ on random matrices, and it shows that the four real parameters of the diagonal and the two phases of each unitary factor account for the eight real dimensions of $\mathrm{GL}_2(\mathbb{C})$.

**In the Peirce frame the diagonal factor is the pair of corner stretches.** For the biquaternion algebra the diagonal positive matrices are

$$
\Sigma=\sigma_+\tilde\Pi_{\mathrm{id},++}\sigma_-\tilde\Pi_{\mathrm{id},-},
$$

so the middle factor is the pair of stretches of *The Exponential of the Symmetric Part: Stretches and the Positive Cone*, one per corner. The computation confirms the identity for diagonal elements, and it shows that the rank of the pair is two and the two corner stretches are its coordinates.

**The complex structure of the algebra is the rotation of the compact part.** The unitary group of the biquaternion algebra is the compact part, and its Lie algebra is the anti-Hermitian half; the Hermitian half is the noncompact part. The computation confirms the two halves at $n=2$ by the involution $\theta$, and it is the reason the biquaternion articles can treat the phase and the stretch as two separate coordinates of the same element.

## Summary

The map $\theta(X)=-X^{*}$ is an involution of $\mathfrak{gl}_n$ with fixed part $\mathfrak{u}(n)$ and anti-fixed part the Hermitian matrices, and the Cartan form $B_\theta(X,Y)=\operatorname{Re}\operatorname{tr}(XY^{*})$ is positive definite and makes the two summands orthogonal, so the pair $(\mathrm{GL}_n(\mathbb{C}),\mathrm{U}(n))$ is a symmetric pair. Every element is $A=K_1e^{H}K_2$ with $K_i$ unitary and $H$ Hermitian, and the middle factor can be taken diagonal positive by the spectral theorem, giving the $KAK$ form $A=K_1\Sigma K_2$, which is the singular value decomposition with the singular values on the diagonal. The diagonal is unique up to permutation and the phases of the two unitary factors are a free frame group, the dimension count $n^{2}+n^{2}=2n^{2}$ accounts for the group, and the group is diffeomorphic to $\mathrm{U}(n)\times\operatorname{Herm}_n$, so its noncompactness sits entirely in the cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\theta(X)=-X^{*}$ | the Cartan involution of the Lie algebra |
| $\mathfrak{u}(n)$, $\operatorname{Herm}_n$ | the fixed and the anti-fixed parts |
| $B_\theta(X,Y)=\operatorname{Re}\operatorname{tr}(XY^{*})$ | the Cartan form |
| $\Theta(g)=(g^{*})^{-1}$ | the Cartan involution of the group |
| $\mathrm{GL}_n=\mathrm{U}(n)\exp(\operatorname{Herm}_n)\mathrm{U}(n)$ | the decomposition |
| $\mathfrak{a}=\{\operatorname{diag}(a_i)\}$ | the maximal abelian subspace |
| $A=K_1\Sigma K_2$ | the $KAK$ form, the singular value decomposition |
| $n!$ | the order of the Weyl group |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the Cartan decomposition and the $KAK$ theorem.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for symmetric pairs and the restricted roots.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the singular value decomposition as a matrix statement.
- [The Polar Decomposition from the Two Halves](the-polar-decomposition-from-the-two-halves.html), for the one-sided form of the decomposition.
- [Symmetric Pairs and Cartan Pairs: the Reductivity Criterion](symmetric-pairs-and-cartan-pairs-the-reductivity-criterion.html), for the pair structure used here.
- [The Killing Form, Its Radical and the Triangular Case](the-killing-form-its-radical-and-the-triangular-case.html), for the trace form and its signs on the two halves.
