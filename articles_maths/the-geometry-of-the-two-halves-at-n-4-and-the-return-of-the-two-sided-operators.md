# __The Geometry of the Two Halves at $n=4$, and the Return of the Two-Sided Operators__

## Introduction

**Every geometric object attached to the two halves — the cone in $\operatorname{Herm}_4$, the unitary group as the exponential of $\mathfrak{u}(4)$, the Grassmannians as the idempotents, the contractible symmetric space $\mathrm{GL}_4/U(4)$ with its trace metric — becomes an operator statement once a frame is chosen: the two-sided operators $T_{a,b}$, the sixteen axis-free basis elements, the Segre cone of dimension seven, the length, and the group of order $32$ as the finite skeleton.**

The article assembles the geometric picture, then turns it around. The turn is the point of the block: the geometry of the halves is the geometry of the operators in the frame, and each object on the list reappears as a statement about $\operatorname{End}(M_4)$.

It assumes *The Positive Cone and Its Boundary at $n=4$*, *The Space of Idempotents and the Flag Varieties at $n=4$*, *The Homotopy of $\mathrm{GL}_4(\mathbb{C})$ and of the Two Halves* and the four operator articles *$\operatorname{End}(M_4(\mathbb{C}))$ as an Algebra*, *The One-Sided Operators at $n=4$*, *The Two-Sided Operators and the Segre Cone at $n=4$* and *The Length and the Two Ranks at $n=4$*. The model at order two is *The Geometry of the Two Halves at $n=2$ and the Return of the Two-Sided Operators*.

## The Hermitian Half and Its Cone

**Proposition.** $\operatorname{Herm}_4$ is a real vector space of dimension $16$ with a positive definite inner product $\langle A,B\rangle=\operatorname{tr}(AB)$, and the positive definite cone $\operatorname{Herm}_4^{++}$ is an open convex cone in it, homogeneous under congruence by $\mathrm{GL}_4(\mathbb{C})$, self-dual for the inner product.

**Proof.** The trace of the product of two Hermitian matrices is real and positive definite; the cone properties are established in the article on the cone.

**Corollary.** The cone carries a Riemannian metric by restriction, and its group of isometries contains the unitary group acting by congruence.

**Proof.** The inner product restricts to a Riemannian metric on the open submanifold, and unitary congruence preserves the trace of the product.

**Corollary.** The cone is the set of squares, and the exponential maps the Hermitian half onto it diffeomorphically.

**Proof.** The spectral theorem.

**The boundary.** The boundary is stratified by rank with dimensions $15$, $12$, $7$ and $0$, and the faces are indexed by subspaces.

**Proof.** The rank-stratum dimension $r(8-r)$ and the face description.

## The Skew Half and the Lie Algebra

**Proposition.** $\mathfrak{u}(4)$ is a real Lie algebra of dimension $16$ under the commutator, it is the Lie algebra of $U(4)$, and the exponential maps it onto $U(4)$.

**Proof.** Closedness under the bracket for skew-Hermitian matrices, the identification of the tangent space at the identity, and the spectral theorem for unitaries.

**Corollary.** The group $U(4)$ is the compact real form of $\mathrm{GL}_4(\mathbb{C})$ inside the complex group, and its Lie algebra is the fixed set of the conjugation $X\mapsto-X^{\ast}$.

**Proof.** The unitary condition and its derivative.

**Corollary.** The two halves are the tangent space and its image at the identity: $\mathfrak{u}(4)=T_{\mathrm I}U(4)$ and $\operatorname{Herm}_4=T_{\mathrm I}\operatorname{Herm}_4^{++}$.

**Proof.** Both are linear spaces through the identity.

## The Idempotents and the Flags

**Proposition.** The Hermitian idempotents of rank $k$ form the Grassmannian $\mathrm{Gr}_k(\mathbb{C}^{4})=U(4)/(U(k)\times U(4-k))$ of real dimension $2k(4-k)$, inside $\operatorname{Herm}_4$.

**Proof.** Orthogonal projections are determined by their images.

**Corollary.** The Grassmannians of ranks one, two, three have real dimensions $6$, $8$, $6$, and the two extreme ranks give points; the full flag has real dimension $12$.

**Proof.** $2k(4-k)$ and twice the complex dimension $6$ of the full flag.

**Corollary.** The idempotents are the critical points of the distance function to a point of the cone, so the stratification of the cone and the flag varieties are the same geometry read twice.

**Proof.** The critical points of the distance to a fixed positive definite matrix are the projections onto its invariant subspaces.

## The Symmetric Space $\mathrm{GL}_4/U(4)$

**Theorem.** $\mathrm{GL}_4(\mathbb{C})/U(4)$ is a symmetric space of noncompact type, diffeomorphic to $\operatorname{Herm}_4^{++}$, hence contractible, of real dimension $16$.

**Proof.** The polar decomposition identifies the quotient with the cone; the cone is convex; the Cartan involution $\theta(X)=-X^{\ast}$ has fixed set $\mathfrak{u}(4)$ and $(-1)$-eigenspace $\operatorname{Herm}_4$, which is the model of the tangent space of the quotient.

**Corollary.** The trace metric $\langle X,Y\rangle=\operatorname{tr}(XY)$ on the tangent space is invariant under the group, and the geodesics are $t\mapsto A^{1/2}e^{tX}A^{1/2}$ for $A$ in the cone and $X$ Hermitian traceless in the appropriate normalisation.

**Proof.** The invariant metric on a symmetric space and the exponential map of the cone.

**Corollary.** The curvature is nonpositive, and the space is a manifold of noncompact type with no closed geodesics.

**Proof.** The sectional curvature of a symmetric space of noncompact type is nonpositive, and a nonpositively curved complete simply connected manifold has no closed geodesics.

**The compact dual.** The compact dual of $\mathrm{GL}_4(\mathbb{C})/U(4)$ is the group manifold $U(4)$ read as the symmetric space $(U(4)\times U(4))/\Delta U(4)$.

**Proof.** The Cartan decomposition of the group case, with the involution $\theta(g)=g^{-\ast}$ whose fixed set is the unitary group; the dual replaces $\operatorname{Herm}_4$ by $i\operatorname{Herm}_4$ and the noncompact group by the compact one.

**Corollary.** The geometry of the halves has two faces: a contractible noncompact one and a compact one obtained by replacing the Hermitian cone by its compact section.

**Proof.** The duality.

## The Return to the Operators

**Proposition.** A choice of frame carries each of these geometric objects to a statement about the two-sided operators. The element algebra $\mathbb{B}$ of dimension $4$ sits inside $\operatorname{End}(\mathbb{B})$ of dimension $16$ as the two families $\mathbb{B}_L$ and $\mathbb{B}_R$, and the two-sided products $T_{a,b}=L_aR_b$ are the sixteen-dimensional coordinate system of the operator space.

**Proof.** The product of a left and a right multiplication and the independence of the sixteen products.

**Corollary.** The cone and the idempotents become statements about the coefficient matrix: positivity becomes the constraint that the coefficient vector lies in the Hermitian direction, and the flags become the rank conditions on the mixed blocks.

**Proof.** The reading of an element in the axis-free coordinates and the Peirce blocks.

**Corollary.** The sixteen axis-free basis elements are signed permutations of determinant one, they are orthonormal up to the factor four for the Hilbert–Schmidt form, and their trace pairing takes the values $\pm4$ with ten plus signs and six minus signs.

**Proof.** The verified computation of the pairing on the axis-free basis.

**Corollary.** The ten and the six are the trace-form signature, and they coincide with the symmetric and antisymmetric directions, so the geometry of the halves is the signature of a single quadratic form on the operator basis.

**Proof.** The set equality between the $+4$ elements and the symmetric ones.

**The operators in order.** The operator algebra of dimension $256$ contains the algebra of dimension $16$ as the two families of one-sided operators; the two-sided products give the Segre cone of dimension seven; the length of an operator is the rank of its coefficient matrix; and the group of order $32$ generated by the signed basis elements is the finite skeleton of the whole picture.

**Proof.** The four operator articles of the block.

**Corollary.** The geometry of the halves is not a different subject: it is the geometry of the operator algebra restricted to the rank-one part, read in the axis-free frame.

**Proof.** The identifications above.

## Summary

The Hermitian half is a real space of dimension sixteen carrying the open convex self-dual cone; the skew half is the Lie algebra of the unitary group; the Hermitian idempotents of rank $k$ are the Grassmannians inside the Hermitian half, of real dimension $2k(4-k)$, and the cone is stratified by the same flags.

$\mathrm{GL}_4/U(4)$ is a symmetric space of noncompact type of dimension sixteen, contractible, with nonpositive curvature and the invariant trace metric; its compact dual replaces the cone by the compact section.

The return is the point: with a frame chosen, each object becomes an operator statement. The two-sided products give the sixteen coordinates, the signed permutations give the finite skeleton of order $32$, the trace pairing gives the signature $(10,6)$, the Segre cone gives the rank-one part, and the length measures the coefficient matrix. The geometry of the halves is the geometry of the operator algebra read on the rank-one cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_4^{++}$ | the self-dual cone of dimension $16$ |
| $\mathfrak{u}(4)$ | the Lie algebra of $U(4)$ |
| $\mathrm{Gr}_k=U(4)/(U(k)\times U(4-k))$ | the Hermitian idempotents |
| $\mathrm{GL}_4/U(4)$ | the contractible symmetric space |
| $T_{a,b}=L_aR_b$ | the two-sided operator |
| $(10,6)$ | the signature of the trace form |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (AMS, 2001), for symmetric spaces of noncompact type and their compact duals.
- [The Positive Cone and Its Boundary at $n=4$](the-positive-cone-and-its-boundary-at-n-4.html), for the cone and its faces.
- [The Space of Idempotents and the Flag Varieties at $n=4$](the-space-of-idempotents-and-the-flag-varieties-at-n-4.html), for the Grassmannians.
- [The Two-Sided Operators and the Segre Cone at $n=4$](the-two-sided-operators-and-the-segre-cone-at-n-4.html), for the operator side of the return.
- [The Length and the Two Ranks at $n=4$](the-length-and-the-two-ranks-at-n-4.html), for the coefficient matrix and its rank.
- [The Geometry of the Two Halves at $n=2$ and the Return of the Two-Sided Operators](the-geometry-of-the-two-halves-at-n-2-and-the-return-of-the-two-sided-operators.html), for the case at order two.
