# __The 2×2 Matrix Representation under the Three Topologies__

## Introduction

The algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$ through the realization $\Phi$ of *Biquaternion 2×2 Matrix Element Representation*, and that article reads the isomorphism for the algebra it transports: the product, the trace, the determinant, the spectrum, the rank-one elements and the module. This article reads the same realization for its **topology**, and it does so three times, once for each of the three pairings of *The Three Pairings of the Biquaternion Algebra*.

Each pairing of the algebra is realized on the matrices as a pairing of the same formal type, with the trace taking the place of the scalar part and the adjugate and the conjugate transpose marking the two non-bilinear cases. The three pairings of the matrices are

$$
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q})\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

and they reproduce the bilinear, the Hermitian and the Krein form of the algebra respectively, the first preceded by adjugation and the third by the adjugate of the conjugate transpose. Each is a form on the matrix algebra with its own signature, its own definiteness, its own null set and its own group of isometries, so each induces its own topology on the representation; the three are kept apart in the three sections below.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$; $\Phi$ is the $2\times2$ matrix realization $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$ of *Biquaternion 2×2 Matrix Element Representation*.

## The Representation

**Definition.** The **matrix realization** is the $\mathbb{C}$-linear isomorphism

$$
\Phi:\mathbb{B}\longrightarrow M_2(\mathbb{C}), \qquad \Phi(e_0)=I, \qquad \Phi(e_k)=-i\sigma_k,
$$

with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices, so that for $\tilde{Q}=Q_0e_0+\mathbf{Q}$,

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0-iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & Q_0+iQ_3 \end{pmatrix}.
$$

The trace is $\operatorname{Tr}\Phi(\tilde{Q})=2Q_0$ and the determinant is $N(\tilde{Q})=\det\Phi(\tilde{Q})$, the biquaternion determinant; the trace identity $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\Phi(\tilde{R})\Phi(\tilde{S}))$ is what makes the matrix trace the carrier of the scalar part, and $\Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q})$ makes the adjugate the carrier of the natural conjugation.

## The Topology Induced by the Bilinear Form

**Theorem (the bilinear pairing of the matrices).** For all biquaternions,

$$
B(\tilde{P},\tilde{Q}) = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q})\bigr),
$$

the $\mathbb{C}$-bilinear pairing of the matrices in which the second argument is adjugated.

**Proof.** $\operatorname{adj}\Phi(\tilde{Q})=\Phi(\tilde{Q}^{\natural})$, so the right-hand side is $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}^{\natural}))=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})=B(\tilde{P},\tilde{Q})$ by the trace identity.

It is the pairing whose diagonal is the determinant, $B(\tilde{Q},\tilde{Q})=\det\Phi(\tilde{Q})=N(\tilde{Q})$; in the coefficient basis its Gram matrix is $\mathrm{I}_4$, of real signature $(4,4)$ on the eight real coordinates, the split form.

**The null set.** The set on which the pairing vanishes, $\det\Phi(\tilde{Q})=0$, is the singular matrices; these are exactly the rank-one matrices $\Phi(\tilde{Q})=uv^{T}$, that is the zero divisors of the algebra. It is a real cone of real dimension $6$ in $\mathbb{R}^8$, the vanishing of one complex quadratic; it is contained in the isotropic cone of the underlying real form $\mathrm{Re}\,B$, a hypersurface of real dimension $7$, which is the largest of the null sets of the three topologies.

**The isometry group.** The pairing has Gram matrix $\mathrm{I}_4$, so its group of isometries on the coefficient space is the complex orthogonal group $O_4(\mathbb{C})$ of *The Three Pairings of the Biquaternion Algebra*; on the matrix side it is the group of linear maps preserving the adjugated pairing, and its realification is the split orthogonal group $O(4,4)$.

## The Topology Induced by the Hermitian Form

**Theorem (the Hermitian pairing of the matrices).** For all biquaternions,

$$
\langle\tilde{P},\tilde{Q}\rangle = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

the **Hilbert–Schmidt pairing** of the matrices.

**Proof.** $\Phi(\tilde{P})^{\dagger}=\Phi(\tilde{P}^{*})$ because $\Phi$ is a $*$-homomorphism for the Hermitian conjugation and the conjugate transpose, so the right-hand side is $\tfrac12\operatorname{Tr}(\Phi(\tilde{P}^{*})\Phi(\tilde{Q}))=\mathrm{Sc}(\tilde{P}^{*}\tilde{Q})=\langle\tilde{P},\tilde{Q}\rangle$.

**Theorem (the Frobenius norm).** The diagonal of the pairing is one half of the squared Frobenius norm,

$$
\langle\tilde{Q},\tilde{Q}\rangle = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{Q})^{\dagger}\Phi(\tilde{Q})\bigr) = \tfrac12\bigl\lVert\Phi(\tilde{Q})\bigr\rVert_F^2 = \sum_\mu|Q_\mu|^2 = \lVert\tilde{Q}\rVert_E^2 ,
$$

so that $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$.

**Proof.** The first equality is the definition of the Frobenius norm of the matrix, the second is the diagonal case of the theorem above, and the square root gives the norm identity.

**The Euclidean topology.** The pairing is positive definite of signature $(8,0)$ on the eight real dimensions; it is the Hilbert–Schmidt inner product of the matrix algebra, and through $\Phi$ it is the Euclidean inner product of $\mathbb{B}$. It induces the Euclidean topology on the representation, the same topology that *The Euclidean Topology of the Biquaternion Algebra* reads on the algebra.

**The isometry group and the unit groups.** The Hilbert–Schmidt pairing lives on the four complex coordinates, so its isometry group is the unitary group $U(4)$, of real dimension $16$; among these, the maps $X\mapsto UXV^{\dagger}$ form the subgroup $U(2)\times U(2)$ modulo the common centre, which is the part that also preserves the algebra structure of $M_2(\mathbb{C})$. Under $\Phi$ the group of units of the algebra is the general linear group $GL_2(\mathbb{C})$, and the group $\{\tilde{A}:N(\tilde{A})=1\}$ is the special linear group $SL_2(\mathbb{C})$; the maximal compact subgroup is $U(2)$, and its special part is $SU(2)\cong\mathrm{Spin}(3)$. These are the groups of *The Unit Group and the Frobenius Norm in the Matrix Representation*.

## The Topology Induced by the Krein Form

**Theorem (the Krein pairing of the matrices).** For all biquaternions,

$$
[\tilde{P},\tilde{Q}] = \tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

the pairing in which the conjugate transpose of the first argument is adjugated.

**Proof.** $\operatorname{adj}\Phi(\tilde{P})^{\dagger}=\Phi(\tilde{P}^{\natural})^{\dagger}=\Phi\bigl((\tilde{P}^{\natural})^{*}\bigr)=\Phi(\bar{\tilde{P}})$, since $(\tilde{P}^{\natural})^{*}=\bar{\tilde{P}}$; the right-hand side is then $\tfrac12\operatorname{Tr}(\Phi(\bar{\tilde{P}})\Phi(\tilde{Q}))=\mathrm{Sc}(\bar{\tilde{P}}\tilde{Q})=[\tilde{P},\tilde{Q}]$.

It is the pairing whose Gram matrix in the coefficient basis is the sign matrix $E=\mathrm{diag}(1,-1,-1,-1)$, of real signature $(2,6)$ and complex inertia $(1,3)$; the adjugate and the conjugate transpose together are what distinguish the Krein case from the other two.

**The null set and the fundamental symmetry.** The set on which the Krein pairing vanishes is the isotropic cone of the form $\sum_\mu\varepsilon_\mu|Q_\mu|^2=0$, which is not the null set of either of the other two pairings: an element may be a zero divisor and definite for the Krein form, or Krein-isotropic and a unit. The natural conjugation $J={}^{\natural}$ is an isometry of all three pairings, and in the matrix picture it is the adjugation $\Phi(\tilde{Q})\mapsto\operatorname{adj}\Phi(\tilde{Q})$.

**The isometry group.** The form $[\cdot,\cdot]$ is the complex Hermitian form of signature $(1,3)$ on $\mathbb{C}^4$, so its isometry group is the indefinite unitary group $U(1,3)$ of *The Krein Isometry Group and Its $J$-Contractions*; on the matrix side it is the group preserving the adjugated conjugate-transpose pairing, whose realification has isometry group $O(2,6)$.

## The Three Topologies Compared

| topology | matrix pairing | signature over $\mathbb{R}$ | definiteness | null set | isometry group |
|---|---|---|---|---|---|
| bilinear | $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$ | $(4,4)$ | indefinite (split) | $\det\Phi(\tilde{Q})=0$ | $O_4(\mathbb{C})$; realification $O(4,4)$ |
| Hermitian | $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | $(8,0)$ | positive definite | $\{0\}$ | $U(4)$; $U(2)\times U(2)$ preserves the algebra |
| Krein | $\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | $(2,6)$ | indefinite | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^2=0$ | $U(1,3)$; real form $O(2,6)$ |

Three matrix operations carry the three topologies, and they are read off one another: the plain product gives the Hermitian pairing and the Frobenius norm, the adjugate gives the bilinear pairing and the determinant, and the adjugate of the conjugate transpose gives the Krein pairing and the sign matrix. The three determinant identities $B(\tilde{Q},\tilde{Q})=N(\tilde{Q})$, $\langle\tilde{Q},\tilde{Q}\rangle=\lVert\tilde{Q}\rVert_E^2$ and $[\tilde{Q},\tilde{Q}]=\sum_\mu\varepsilon_\mu|Q_\mu|^2$ are the diagonal readings of the three.

## Summary

Each of the three pairings of the algebra becomes a pairing of the matrices through the trace of *Biquaternion 2×2 Matrix Element Representation*. The bilinear form is $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$, the $\mathbb{C}$-bilinear pairing with the second argument adjugated, of real signature $(4,4)$, whose diagonal is the determinant and whose null set is the singular matrices; the Hermitian form is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$, positive definite of signature $(8,0)$, one half of the squared Frobenius norm, with $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\lVert\tilde{Q}\rVert_E$; and the Krein form is $\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$, of signature $(2,6)$, with the sign matrix $E$ as Gram matrix and the adjugate of the conjugate transpose as its characteristic operation. The three isometry groups are $O_4(\mathbb{C})$, $U(4)$, and $U(1,3)$; inside them, the algebra-preserving part of $U(4)$ is $U(2)\times U(2)$ modulo the centre.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(\tilde{Q})$ | the $2\times2$ matrix of the realization, $\det\Phi(\tilde{Q})=N(\tilde{Q})$ |
| $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$ | the bilinear pairing of the matrices |
| $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | the Hermitian pairing, the Hilbert–Schmidt pairing |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | the Krein pairing of the matrices |
| $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$ | the Frobenius norm and the Euclidean norm |
| $(4,4)$, $(8,0)$, $(2,6)$ | the three signatures over $\mathbb{R}$ |

## Further Reading

- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the realization in the Algebra group
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the three pairings of the matrices in full
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the adjugated trace pairings used here
- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for the three forms of the algebra and their isometry groups
- *The Unit Group and the Frobenius Norm in the Matrix Representation* (`articles_maths/the-unit-group-and-the-frobenius-norm-in-the-matrix-representation.md`), for the matrix form of the unit group and the topology of the algebra
