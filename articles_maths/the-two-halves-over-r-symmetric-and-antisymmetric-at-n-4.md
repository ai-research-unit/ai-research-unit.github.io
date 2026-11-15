# __The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=4$__

## Introduction

**The symmetric and the antisymmetric matrices are the two eigenspaces of the transpose, of complex dimensions $10$ and $6$, and over the real numbers they are the positive and the negative halves of the trace form: on a real symmetric matrix $\operatorname{tr}(S^{2})$ is a sum of squares, and on a real antisymmetric matrix it is minus a sum of squares.**

The article defines the two halves, proves the projections and the uniqueness of the split, shows that neither half is closed under the product while each is closed under the appropriate symmetrised product, and reads the split in the axis-free basis, where symmetry becomes an index pattern on the sixteen coordinates and the trace pairing has the sign of that pattern with no transpose taken.

It assumes *The Involutions of $M_4(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$* for the transpose and its two eigenspaces, and *$M_4(\mathbb{C})$ Axis-Free Representation* for the basis. The case $n=2$ is *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*. The signature of the trace form on the two halves is *The Trace Form and Its Signature on the Two Halves of $M_4(\mathbb{C})$*.

## The Two Halves and the Projections

**Definition.** $\operatorname{Sym}_4=\{A:A^{\mathsf T}=A\}$ and $\operatorname{Skew}_4=\{A:A^{\mathsf T}=-A\}$.

**Proposition.** $\operatorname{Sym}_4$ has complex dimension $10$ and $\operatorname{Skew}_4$ complex dimension $6$, and

$$
M_4(\mathbb{C})=\operatorname{Sym}_4\oplus\operatorname{Skew}_4,\qquad A=\tfrac12(A+A^{\mathsf T})+\tfrac12(A-A^{\mathsf T}).
$$

**Proof.** A symmetric matrix is determined by the ten entries on and above the diagonal, an antisymmetric one by the six entries above it, and the two formulas are the projections onto the eigenspaces of an involution; their sum is $A$ and their difference of transposes is zero.

**Corollary.** The two maps $A\mapsto\tfrac12(A\pm A^{\mathsf T})$ are linear, idempotent, and their images meet only at $0$.

**Proof.** They are the spectral projections of $\mathsf T$ for the eigenvalues $+1$ and $-1$.

**The real reading.** On the real slice the same formulas give $\operatorname{Sym}_4(\mathbb{R})$ of real dimension $10$ and $\operatorname{Skew}_4(\mathbb{R})$ of real dimension $6$, and $M_4(\mathbb{R})=\operatorname{Sym}_4(\mathbb{R})\oplus\operatorname{Skew}_4(\mathbb{R})$.

**Proof.** The projections have real coefficients, so they preserve the real matrices, and the dimensions are the numbers of free real entries.

## Neither Half Is an Algebra

**Proposition.** $\operatorname{Sym}_4$ is not closed under the product, and neither is $\operatorname{Skew}_4$.

**Proof.** Take $S=E_{11}+E_{22}$ and $S'=E_{11}$, both symmetric; their product is $E_{11}+E_{22}$, symmetric. Now take $S=E_{12}+E_{21}$ and $S'=E_{11}$, both symmetric; their product is $E_{21}$, antisymmetric. For the second half, $K=E_{12}-E_{21}$ and $K'=E_{34}-E_{43}$ are antisymmetric and their product has the entries $\pm1$ at $(1,4)$ and $(2,3)$, which is symmetric.

**Proposition (the truth about the four products).** For $A,B$ of the **same** parity the anticommutator is symmetric and the commutator is skew; for $A,B$ of **opposite** parity the anticommutator is skew and the commutator is symmetric. Hence

$$
AB=\tfrac12\{A,B\}+\tfrac12[A,B]
$$

is the symmetric-plus-antisymmetric split of $AB$ when the parities agree, and the reverse split when they do not.

**Proof.** Take $A,B$ symmetric: $\{A,B\}^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}+A^{\mathsf T}B^{\mathsf T}=BA+AB$, so the anticommutator is symmetric, and $[A,B]^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}-A^{\mathsf T}B^{\mathsf T}=-[A,B]$. Take $A,B$ antisymmetric: $\{A,B\}^{\mathsf T}=(-B)(-A)+(-A)(-B)$, again symmetric, and $[A,B]^{\mathsf T}=(-B)(-A)-(-A)(-B)=-K'K+KK'=-[A,B]$. Take $S$ symmetric and $K$ antisymmetric: $\{S,K\}^{\mathsf T}=-KS-SK=-\{S,K\}$ and $[S,K]^{\mathsf T}=-KS+SK=[S,K]$.

**The product of two antisymmetric matrices is not symmetric.** At order four the example is decisive: with $K=E_{12}-E_{21}$ and $K'=E_{23}-E_{32}$ one has $KK'=E_{13}$, which is neither symmetric nor antisymmetric.

**Proof.** Expand: $K$ sends $e_1\mapsto e_2$ and $e_2\mapsto-e_1$, $K'$ sends $e_2\mapsto e_3$ and $e_3\mapsto-e_2$, so $KK'$ sends $e_3\mapsto-e_1$ and kills the other two basis vectors; that map is $E_{13}$. Its transpose is $E_{31}\neq\pm E_{13}$.

**Why order two is different.** At $n=2$ the antisymmetric matrices form a one-dimensional space, so they all commute and $KK'$ is symmetric there. At $n=4$ the antisymmetric half is $\mathfrak{so}(4)$, of dimension $6$ and not abelian, and the commutator $[K,K']$ is a nonzero skew matrix; the symmetric product of order two is the accident, and the general statement carries both parts.

**Corollary (what each half does support).** $\operatorname{Sym}_4$ is closed under the anticommutator and not under the product; $\operatorname{Skew}_4$ is closed under the commutator and not under the product.

**Proof.** The anticommutator of two symmetric matrices is symmetric and $\{S,E_{12}+E_{21}\}$ with $S=E_{11}+E_{22}$ stays symmetric, while the product $SE_{12}$ is not; the commutator of two antisymmetric matrices is antisymmetric by the proposition, while the product $KK'=E_{13}$ is not.

**The graded picture.** The two halves are the even and odd parts of a $\mathbb{Z}_2$-grading by the transpose, and the multiplication is graded-commutative up to the twist: the symmetric half is the even part and the antisymmetric half the odd part, and the parity of a product is the product of the parities. Reading the four products as a graded table is *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=4$*.

## The Trace and the Two Halves

**Proposition.** $\operatorname{tr}S$ is real for a real symmetric matrix, $\operatorname{tr}K=0$ for every antisymmetric matrix, and $\operatorname{tr}(SK)=0$ for $S$ symmetric and $K$ antisymmetric.

**Proof.** The diagonal of an antisymmetric matrix vanishes. For the third, $\operatorname{tr}(SK)=\operatorname{tr}((SK)^{\mathsf T})=\operatorname{tr}(K^{\mathsf T}S^{\mathsf T})=\operatorname{tr}(-KS)=-\operatorname{tr}(SK)$, hence zero.

**Corollary.** The trace functional vanishes on $\operatorname{Skew}_4$, and the traceless part of $\operatorname{Sym}_4$ has dimension $9$.

**Proof.** The trace of a skew matrix is zero; on the symmetric half the trace is a nonzero linear functional, so its kernel has dimension $10-1=9$.

**The definiteness over $\mathbb{R}$.** For real $S$ and real $K$,

$$
\operatorname{tr}(S^{2})=\sum_{i}s_{ii}^{2}+2\sum_{i<j}s_{ij}^{2}>0,\qquad
\operatorname{tr}(K^{2})=-2\sum_{i<j}k_{ij}^{2}<0 .
$$

**Proof.** Expand $S^{2}$ and $K^{2}$ entry by entry: the diagonal of $S^{2}$ is $\sum_j s_{ij}^{2}$ and the diagonal of $K^{2}$ is $-\sum_j k_{ij}^{2}$, and each off-diagonal pair occurs twice.

**Corollary.** On the real halves the trace form $\beta(X,Y)=\operatorname{tr}(XY)$ is positive definite on $\operatorname{Sym}_4(\mathbb{R})$ and negative definite on $\operatorname{Skew}_4(\mathbb{R})$.

**Proof.** A symmetric bilinear form with $\beta(X,X)>0$ for every $X\neq0$ is positive definite; the polarisation of $\operatorname{tr}(X^{2})$ is $\operatorname{tr}(XY)$.

**Corollary.** The signature of $\beta$ on $M_4(\mathbb{R})$ is $(10,6)$.

**Proof.** The two halves are orthogonal for $\beta$ and carry $10$ positive and $6$ negative directions.

## The Axis-Free Reading

**Symmetry is an index pattern.** In the basis $T_{\mu\nu}=L^{\mathrm{axf}}_{e_\mu}R^{\mathrm{axf}}_{e_\nu}$ the pairing is diagonal,

$$
\operatorname{tr}(T_{\mu\nu}T_{\rho\sigma})=\pm4\,\delta_{\mu\rho}\delta_{\nu\sigma},
$$

and the sign is determined by the two indices alone: it is $+4$ when both are equal or both are vector indices, and $-4$ when exactly one of them is the scalar index $t$.

**The ten and the six, named.** The positive set is

$$
T_{tt},\ T_{xx},\ T_{yy},\ T_{zz},\ T_{xy},\ T_{xz},\ T_{yx},\ T_{yz},\ T_{zx},\ T_{zy},
$$

and the negative set is $T_{tx},T_{ty},T_{tz},T_{xt},T_{yt},T_{zt}$.

**Proposition.** The positive set is exactly the set of symmetric matrices among the sixteen, and the negative set is exactly the set of antisymmetric ones; no element is neither and none is both.

**Proof.** Each $T_{\mu\nu}$ is a signed permutation matrix, so its transpose is again a signed permutation matrix, and it is among the sixteen by the closure of the set. Comparing each of the sixteen with its transpose sorts them into the two displayed sets, of sizes ten and six.

**Corollary.** In this basis the trace pairing has the sign of the symmetry, and the symmetric decomposition is read without taking a single transpose.

**Proof.** The sign is $+4$ exactly on the symmetric elements, which is the statement that the positive eigenspace of the form and the symmetric half coincide.

**The coordinates.** Write $A=\sum c_{\mu\nu}T_{\mu\nu}$. The symmetric half is the set of matrices whose negative-slot coefficients vanish,

$$
A\in\operatorname{Sym}_4\iff c_{tx}=c_{ty}=c_{tz}=c_{xt}=c_{yt}=c_{zt}=0,
$$

and the antisymmetric half is the set whose remaining ten coefficients vanish.

**Proof.** The sixteen form a basis and the two displayed sets are complementary, so each half is the coordinate subspace spanned by its own six or ten elements.

## Summary

The transpose is an involution of $M_4(\mathbb{C})$, so the algebra is the direct sum of its $+1$ and $-1$ eigenspaces, of complex dimensions $10$ and $6$ and real dimensions $10$ and $6$ on the real slice. The projections are $\tfrac12(A\pm A^{\mathsf T})$ and they are unique.

Neither half is closed under the product. For two matrices of the same parity the anticommutator is symmetric and the commutator skew, for opposite parities the reverse, and every product splits accordingly; in particular a product of two antisymmetric matrices is not symmetric at order four. The trace vanishes on the antisymmetric half and on every mixed pairing.

Over the reals the trace of a symmetric square is a sum of squares and the trace of an antisymmetric square is minus a sum of squares, so the two halves are the positive and negative parts of the form, of signature $(10,6)$. In the axis-free basis this is an index pattern with no transpose in sight: ten symmetric slots, six antisymmetric ones, and a sign of $4$ attached to each.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_4$ | the symmetric matrices, complex dimension $10$ |
| $\operatorname{Skew}_4$ | the antisymmetric matrices, complex dimension $6$ |
| $\tfrac12(A\pm A^{\mathsf T})$ | the two projections |
| $\{S,K\}$, $[S,K]$ | anticommutator and commutator of two halves |
| $\beta(X,Y)=\operatorname{tr}(XY)$ | the trace pairing |
| $T_{\mu\nu}$ | the sixteen axis-free basis matrices |
| $c_{\mu\nu}$ | the axis-free coordinates |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for symmetric and skew-symmetric matrices and their eigenvalue structure.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the dagger and the Hermitian half.
- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for the sixteen matrices and the coefficient basis.
- [The Trace Form and Its Signature on the Two Halves of $M_4(\mathbb{C})$](the-trace-form-and-its-signature-on-the-two-halves-of-m4c.html), for the signature computed in full.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the same split at order two.
