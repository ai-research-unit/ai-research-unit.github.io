# __The Symmetric Space $\mathrm{GL}_4/O(4)$ and Its Complex Twin__

## Introduction

**The pair $(\mathfrak{gl}_4,\mathfrak{so}(4))$ with the Cartan involution $\theta(X)=-X^{\mathsf T}$ gives the decomposition $\mathfrak{gl}_4=\mathfrak{so}(4)\oplus\operatorname{Sym}_4$ with $\mathfrak{p}=\operatorname{Sym}_4$ of dimension $10$ over $\mathbb{R}$ and of complex dimension $10$ over $\mathbb{C}$; the corresponding symmetric spaces are $\mathrm{GL}_4(\mathbb{R})/O(4)$ and $\mathrm{GL}_4(\mathbb{C})/O(4,\mathbb{C})$, both diffeomorphic to a cone hence contractible, with compact dual $U(4)/O(4)$ of dimension $10$.**

The article establishes the Cartan decomposition, computes the dimensions over both fields, identifies the quotients with the cones of positive definite symmetric matrices, describes the geodesics and the curvature, identifies the compact dual, and reads the ten symmetric directions in the axis-free basis, where the trace form takes the value $+4$ on exactly ten elements.

It assumes *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion at $n=4$*, *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* and *The Trace Form and Its Signature on the Two Halves of $M_4(\mathbb{C})$*. The model at order two is *The Symmetric Space $\mathrm{GL}_2/O(2)$ and Its Complex Twin*.

## The Pair and the Cartan Involution

**Definition.** $\theta(X)=-X^{\mathsf T}$ on $\mathfrak{gl}_4$, extended to $\mathfrak{gl}_4(\mathbb{C})$ by complex linearity.

**Proposition.** $\theta$ is an involutive automorphism of the Lie algebra, its fixed set is $\mathfrak{so}(4)=\{X:X^{\mathsf T}=-X\}$, and its $(-1)$-eigenspace is $\operatorname{Sym}_4=\{X:X^{\mathsf T}=X\}$.

**Proof.** $\theta([X,Y])=-[X^{\mathsf T},Y^{\mathsf T}]=[\theta X,\theta Y]$ because transposition reverses the order twice; the eigenspaces are the two classical halves and add to the whole.

**Corollary.** The decomposition $\mathfrak{gl}_4=\mathfrak{so}(4)\oplus\operatorname{Sym}_4$ is a Cartan decomposition: $[\mathfrak{k},\mathfrak{k}]\subset\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subset\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}$.

**Proof.** The bracket of an antisymmetric and a symmetric matrix is symmetric; the bracket of two symmetric matrices is antisymmetric.

**Corollary.** The form $\langle X,Y\rangle=-\operatorname{tr}(XY)$ is positive definite on $\mathfrak{so}(4)$ and negative definite on $\operatorname{Sym}_4$, so $\theta$ is the involution associated with this form.

**Proof.** On a real antisymmetric matrix $\operatorname{tr}(X^{2})$ is negative, and on a symmetric one positive.

**Corollary.** $\mathfrak{so}(4)$ is a maximal compact subalgebra, and the pair is a symmetric pair of the noncompact type.

**Proof.** The fixed set of a Cartan involution is a maximal compact subalgebra.

## The Dimensions

**Proposition.** Over $\mathbb{R}$: $\dim\mathfrak{gl}_4=16$, $\dim\mathfrak{so}(4)=6$, $\dim\operatorname{Sym}_4=10$, and $16=6+10$.

**Proof.** The dimension of the general linear algebra is $n^{2}=16$; the antisymmetric matrices of order four are $\binom{4}{2}=6$; the symmetric ones are $\binom{5}{2}=10$.

**Corollary.** Over $\mathbb{C}$ the same numbers hold with complex dimensions, and the real dimensions are doubled: $32=12+20$.

**Proof.** Complexification doubles every real dimension.

**Corollary.** The quotient $\mathrm{GL}_4(\mathbb{R})/O(4)$ has dimension $10$ and its complex twin $\mathrm{GL}_4(\mathbb{C})/O(4,\mathbb{C})$ has complex dimension $10$, real dimension $20$.

**Proof.** The dimension of a quotient by a closed subgroup is the difference.

**The rank.** The maximal flat subspace of $\operatorname{Sym}_4$ is the space of diagonal matrices, of dimension $4$, so the symmetric space has rank $4$; the Weyl group is the group of permutations and sign changes of the four entries, of order $2^{4}\cdot4!=384$.

**Proof.** The diagonal matrices commute and are maximal among the commutative subalgebras of the symmetric part; the normaliser in $O(4)$ permutes the coordinates and changes their signs.

**Corollary.** The rank four is the same four as the order of the matrix, and the Weyl group of order $384$ is the hyperoctahedral group.

**Proof.** The two computations.

## The Quotient and Its Identification

**Theorem.** Every invertible real matrix is uniquely $A=HU$ with $H$ positive definite symmetric and $U$ orthogonal, so $\mathrm{GL}_4(\mathbb{R})/O(4)$ is diffeomorphic to the open cone $\operatorname{Sym}_4^{++}$.

**Proof.** The real polar decomposition, and the uniqueness of the positive definite square root.

**Corollary.** The quotient is contractible, and all its homotopy groups vanish.

**Proof.** The cone is convex.

**Corollary.** The complex twin is $\mathrm{GL}_4(\mathbb{C})/O(4,\mathbb{C})$, the space of nondegenerate complex symmetric forms, of complex dimension $10$; it is not contractible, since it contains a circle of scalars modulo the sign.

**Proof.** The quotient is the space of nondegenerate complex symmetric matrices, and in the long exact sequence of $O(4,\mathbb{C})\to\mathrm{GL}_4(\mathbb{C})\to\mathrm{GL}_4/O(4,\mathbb{C})$ the finite group $\pi_1(O(4,\mathbb{C}))$ maps trivially into $\pi_1(\mathrm{GL}_4(\mathbb{C}))=\mathbb{Z}$, so the quotient has infinite fundamental group.

**Corollary.** The real and the complex quotients differ in topology although they agree in dimension over their fields.

**Proof.** The real cone is convex over $\mathbb{R}$; over $\mathbb{C}$ the positivity disappears and with it the convexity.

## Geodesics and Curvature

**Proposition.** The geodesics of $\mathrm{GL}_4(\mathbb{R})/O(4)$ through the identity coset are $t\mapsto e^{tX}$ with $X\in\operatorname{Sym}_4$, and in the cone model they are $t\mapsto A^{1/2}e^{tX}A^{1/2}$ for $A$ positive definite.

**Proof.** The exponential map of a symmetric space and the identification of the quotient with the cone.

**Corollary.** The sectional curvature is nonpositive, and it vanishes exactly on the planes spanned by two commuting diagonal directions.

**Proof.** The curvature of a symmetric space of noncompact type computed from the bracket $[\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}$, which vanishes on a flat.

**Corollary.** The exponential map of the cone is a diffeomorphism, so the space is complete and simply connected with nonpositive curvature.

**Proof.** Cartan–Hadamard.

**The distance.** The invariant distance from the identity coset to the coset of $e^{X}$ is $\lVert X\rVert$ for the trace form, and in the cone model the distance from the identity to $A$ is $\lVert\log A\rVert$.

**Proof.** The Riemannian distance in a symmetric space of noncompact type.

## The Compact Dual

**Theorem.** The compact dual of $\mathrm{GL}_4(\mathbb{R})/O(4)$ is $U(4)/O(4)$, of dimension $10$, and the compact dual of the complex twin is $U(4)/O(4)$ as well.

**Proof.** The compact real form $U(4)$ with the same involution has fixed set $O(4)$ and $(-1)$-eigenspace $i\operatorname{Sym}_4$, of real dimension $10$.

**Corollary.** $U(4)/O(4)$ is the space of real structures on $\mathbb{C}^{4}$ compatible with the Hermitian form, and it is the set of conjugations of the complex structure.

**Proof.** A symmetric unitary matrix of square one is a conjugation, and the quotient by the orthogonal group identifies the conjugate-linear structures up to unitary change of basis.

**Corollary.** The compact dual has nonnegative curvature and closed geodesics, in contrast with the noncompact space.

**Proof.** Compactness and the sign of the curvature.

**The duality.** The two spaces have the same complexification, and the noncompact one is obtained by multiplying the tangent space by $i$.

**Proof.** The duality between the two real forms of the same complex group.

## The Axis-Free Reading

**Proposition.** In the axis-free basis of the operator space the trace form takes the value $+4$ on exactly ten elements and $-4$ on six, and the ten are exactly the operators whose index pattern is symmetric.

**Proof.** The verified computation $\operatorname{tr}(T_{\mu\nu}T_{\rho\sigma})=\pm4\delta$ with the set equality between the plus signs and the symmetric patterns.

**Corollary.** The dimension ten of $\mathfrak{p}$ is read off as the number of plus signs, so the Cartan decomposition and the signature of the trace form are the same split read twice.

**Proof.** The ten plus signs and the six minus signs.

**Corollary.** The compact dual replaces the ten symmetric directions by their imaginary multiples, which is the multiplication of $\mathfrak{p}$ by $i$.

**Proof.** The $(-1)$-eigenspace of the compact form is $i\operatorname{Sym}_4$.

**The split of the ten.** The ten symmetric directions split as four with equal indices and six with distinct ones, so the diagonal directions of dimension four are the flat part and the six mixed ones are transverse to it.

**Proof.** The count of symmetric index patterns: four with equal indices and six with distinct ones.

## The Comparison

**Proposition.** $\mathrm{GL}_4(\mathbb{C})/U(4)$ has real dimension $16$ and is contractible; $\mathrm{GL}_4(\mathbb{R})/O(4)$ has real dimension $10$ and is contractible; $\mathrm{GL}_4(\mathbb{C})/O(4,\mathbb{C})$ has real dimension $20$ and is not contractible.

**Proof.** The three dimension counts and the three quotient identifications.

**Corollary.** The choice of the compact form decides both the dimension of the quotient and its topology; the unitary quotient is the largest and the simplest.

**Proof.** The three cases.

**Corollary.** The symmetric space of the pair $(\mathfrak{gl}_4,\mathfrak{so}(4))$ is the smallest of the three and the one attached to the transpose, that is to the biquaternion conjugation in the axis-free frame.

**Proof.** The involution $\theta(X)=-X^{\mathsf T}$ and the identification of the transpose with the biquaternion conjugation.

**The meaning.** The pair $(\mathfrak{gl}_4,\mathfrak{so}(4))$ is the pair of the transpose, and the transpose is the conjugation of the biquaternion algebra in the axis-free frame; so the symmetric space $GL_4/O(4)$ is the geometric face of that conjugation.

**Proof.** The two identifications.

## Summary

The transpose gives a Cartan involution of $\mathfrak{gl}_4$ with fixed set $\mathfrak{so}(4)$ and $(-1)$-eigenspace $\operatorname{Sym}_4$, of dimensions $6$ and $10$ over $\mathbb{R}$, and $6$ and $10$ again over $\mathbb{C}$ in complex dimensions. The quotient by the orthogonal group is the open cone of positive definite symmetric matrices, of rank four, with Weyl group of order $384$, nonpositive curvature and contractible topology.

The complex twin is the space of nondegenerate complex symmetric forms, of complex dimension ten, not contractible because the positivity is gone. The compact dual is $U(4)/O(4)$, of dimension ten, with nonnegative curvature and closed geodesics.

In the axis-free basis the ten symmetric directions are exactly the ten elements on which the trace form is positive, so the Cartan decomposition is the signature of the trace form read twice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\theta(X)=-X^{\mathsf T}$ | the Cartan involution |
| $\mathfrak{k}=\mathfrak{so}(4)$, $\mathfrak{p}=\operatorname{Sym}_4$ | the two eigenspaces, dims $6$ and $10$ |
| $\mathrm{GL}_4(\mathbb{R})/O(4)\cong\operatorname{Sym}_4^{++}$ | the noncompact space |
| $U(4)/O(4)$ | the compact dual |
| rank $4$, Weyl group $384$ | the flat and its symmetry group |
| ten plus signs | $\mathfrak{p}$ in the axis-free basis |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (AMS, 2001), for Cartan decompositions, duality and curvature.
- [Symmetric Pairs and Cartan Pairs: the Reductivity Criterion at $n=4$](symmetric-pairs-and-cartan-pairs-the-reductivity-criterion-at-n-4.html), for the three bracket conditions.
- [The Trace Form and Its Signature on the Two Halves of $M_4(\mathbb{C})$](the-trace-form-and-its-signature-on-the-two-halves-of-m4c.html), for the $(10,6)$ signature.
- [The Symmetric Space $\mathrm{GL}_2/O(2)$ and Its Complex Twin](the-symmetric-space-gl2-o2-and-its-complex-twin.html), for the case at order two.
- [The Geometry of the Two Halves at $n=4$, and the Return of the Two-Sided Operators](the-geometry-of-the-two-halves-at-n-4-and-the-return-of-the-two-sided-operators.html), for the geometric picture as a whole.
