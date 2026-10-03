# __The Forms in the Matrix Representation of the Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$ through the map $\Phi$ fixed by $\Phi(e_0) = I$ and $\Phi(e_k) = -i\sigma_k$, and both of the algebra's pairings — the complex bilinear form and the Hermitian form — have a closed matrix reading under that isomorphism. This article collects those readings. It is the FORM entry of the matrix-representation group of the Topology, and it exists because the algebra's forms, once moved out of the Algebra group, need their matrix form stated somewhere.

The algebra and the realization are *Biquaternion 2×2 Matrix Element Representation*, from which the trace, the determinant and the conjugations are taken; the forms themselves, in coefficient space, are *The Bilinear Form on the Biquaternion Algebra* and *The Hermitian Form on the Biquaternion Algebra*; the real forms of the subspaces are *Biquaternion Norm and Invertibility*; the second matrix realization and its own form are *The Minkowski Form and the Modulus-Squared Map in the Matrix Representation*. Only the transport of the forms along $\Phi$ is done here.

Notation is that of the companion articles: $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, and $\Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}$.

## The Trace and the Scalar Part

The bridge between the coefficient expressions and the matrix expressions is the trace. By the trace-and-determinant proposition of the matrix article,

$$
\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0 = 2\,\mathrm{Sc}(\tilde{Q}),
$$

so the scalar part is half the trace, and because $\Phi$ is an algebra isomorphism, the trace of a product is the trace of the product of the images:

$$
\operatorname{Tr}\bigl(\Phi(\tilde{P})\Phi(\tilde{Q})\bigr) = \operatorname{Tr}\Phi(\tilde{P}\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{Q}).
$$

Every bilinear statement of the algebra therefore transcribes into a trace of two matrices.

## The Bilinear Form in Matrix Form

**Proposition (the bilinear form as a trace).** For all biquaternions $\tilde{P}, \tilde{Q}$,

$$
N(\tilde{P}, \tilde{Q}) = \mathrm{Sc}\bigl(\tilde{P}\tilde{Q}^{\natural}\bigr) = \tfrac{1}{2}\operatorname{Tr}\bigl(\Phi(\tilde{P})\,\Phi(\tilde{Q}^{\natural})\bigr) = \tfrac{1}{2}\operatorname{Tr}\bigl(\Phi(\tilde{P})\,\operatorname{adj}\Phi(\tilde{Q})\bigr).
$$

The last step is the matrix form of the natural conjugation.

**Proposition (the natural conjugation is the adjugate).** For every biquaternion $\tilde{Q}$,

$$
\Phi(\tilde{Q}^{\natural}) = \operatorname{adj}\Phi(\tilde{Q}) .
$$

**Proof.** Quaternion conjugation is the adjugate in the realization: the product of a $2 \times 2$ matrix with the adjugate of another is the scalar pairing of their columns, and the second column of $\Phi(\tilde{Q})$ is the signed complex conjugate of the first, so the adjugate reproduces $\Phi$ on the conjugated coefficients. In entries, with $\Phi(\tilde{Q}) = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ one has $a = Q_0 - iQ_3$, $b = -iQ_1 - Q_2$, $c = -iQ_1 + Q_2$, $d = Q_0 + iQ_3$, and $\operatorname{adj}\Phi(\tilde{Q}) = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, which is $\Phi$ of $\tilde{Q}^{\natural} = Q_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$. $\square$

Two consequences are worth recording.

- The **determinant is the norm**, $N(\tilde{Q}) = \det\Phi(\tilde{Q})$, so the bilinear form evaluated on the diagonal is the determinant: $N(\tilde{Q}, \tilde{Q}) = N(\tilde{Q}) = \det\Phi(\tilde{Q})$. The vanishing of the bilinear form on a nonzero element is the singularity of its matrix, and the null elements of the algebra are exactly the nonzero singular matrices, that is, the rank-one matrices $\Phi(\tilde{Q}) = uv^{\mathsf{T}}$.
- The **conjugation pairs the two factors**: the second slot enters through the adjugate, not through the matrix itself, and this is the matrix expression of the fact that the bilinear form is $\mathbb{C}$-bilinear but pairs the algebra with its natural conjugate.

## The Gram Matrix

The Gram matrix is computed from the definition $N(\tilde{P},\tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$ and the squares of the units. The natural conjugation multiplies the $\nu$-th coefficient by $\varepsilon_\nu$, so

$$
N(e_\mu, e_\mu) = \mathrm{Sc}\bigl(e_\mu e_\mu^{\natural}\bigr) = \varepsilon_\mu \mathrm{Sc}(e_\mu^2) = \varepsilon_\mu^2 = +1,
\qquad
N(e_\mu, e_\nu) = \varepsilon_\nu \mathrm{Sc}(e_\mu e_\nu) = 0 \ \ (\mu \neq \nu),
$$

because $e_0^2 = e_0$ and $e_k^2 = -e_0$: the form pairs every unit with itself to $+1$. Hence

$$
G = \mathrm{I}_{4} , \qquad \det G = +1 ,
$$

and the non-degeneracy of the form is the invertibility of the identity matrix.

**Remark (where the sign matrix $D$ belongs).** The matrix $D = \operatorname{diag}(1,-1,-1,-1)$ is not the Gram matrix of the norm form. It is the Gram matrix of the *companion* pairing $\mathrm{Sc}(\tilde{P}\tilde{Q})$, in which no conjugation is present; the two forms differ exactly by the natural conjugation in the first slot. The norm form is the polarisation of $N$ and has Gram matrix $\mathrm{I}_4$, while $\mathrm{Sc}(\tilde{P}\tilde{Q})$ has Gram matrix $D$ and is the form whose transpose is the association of *Association and the Transpose on the Biquaternion Algebra*, whence the transposition identity $\rho_R(\tilde{Q}) = D\rho_L(\tilde{Q})^{\mathsf{T}}D$ of the $4 \times 4$ article. The same matrix $D$ is the Gram matrix of the Krein form $[\cdot,\cdot]$ in the coefficient basis (*The Biquaternion Krein Form and Its Signature*); the coincidence is the reason the Krein form is the indefinite companion of the norm form.

## The Restriction to the Hermitian and Anti-Hermitian Matrices

The determinant also reads the restriction of the bilinear form to the two four-dimensional subspaces of matrices.

**Proposition (the two signatures in matrix form).**

- On the Hermitian matrices $\begin{pmatrix} a & z \\ \bar z & b \end{pmatrix}$ with $a, b \in \mathbb{R}$ and $z \in \mathbb{C}$, the determinant is
$$
\det = ab - |z|^2 ,
$$
a form of signature $(1,3)$ on the real four-space $\mathbb{M}_+$.
- On the anti-Hermitian matrices $\begin{pmatrix} ia & z \\ -\bar z & ib \end{pmatrix}$ with $a, b \in \mathbb{R}$ and $z \in \mathbb{C}$, the determinant is
$$
\det = |z|^2 - ab ,
$$
a form of signature $(3,1)$ on $\mathbb{M}_-$.

**Proof.** Both determinants are computed directly from the entries; on each subspace the determinant is real, since it is the norm, and on each the four real coordinates split into a hyperbolic pair $(a,b)$ of signature $(1,1)$, from the diagonal, and a definite real two-plane of signature $(0,2)$, from the off-diagonal entry $z$. On $\mathbb{H}_2(\mathbb{C})$ the signs are $+$ on the hyperbolic pair and $-$ on the off-diagonal two-plane, giving $(1,3)$; on the anti-Hermitian matrices the hyperbolic pair enters with the opposite sign, giving $(3,1)$. $\square$

The general signature table over all six subspaces is in *The Bilinear Form on the Biquaternion Algebra*, §*The Restriction to the Six Subspaces*; this proposition is that table read on the matrices.

## The Hermitian Form in Matrix Form

**Proposition (the Hermitian form is the matrix product).** For every biquaternion $\tilde{Q}$,

$$
\Phi\bigl(\tilde{Q}\tilde{Q}^{*}\bigr) = \Phi(\tilde{Q})\,\Phi(\tilde{Q})^{\dagger},
$$

a positive semidefinite Hermitian matrix, and

$$
\operatorname{Tr}\bigl(\tilde{Q}\tilde{Q}^{*}\bigr) = 2\sum_{\mu=0}^{3} |Q_\mu|^2 = \bigl\|\Phi(\tilde{Q})\bigr\|_F^2 ,
$$

where $\|\cdot\|_F$ is the Frobenius norm.

**Proof.** The first identity is the multiplicativity of $\Phi$ together with $\Phi(\tilde{Q}^{*}) = \Phi(\tilde{Q})^{\dagger}$. For the second, the four entries of $\Phi(\tilde{Q})$ are $Q_0 - iQ_3$, $-iQ_1 - Q_2$, $-iQ_1 + Q_2$ and $Q_0 + iQ_3$, whose squared moduli sum to $2|Q_0|^2 + 2|Q_1|^2 + 2|Q_2|^2 + 2|Q_3|^2$ because the cross terms cancel in each pair; and the trace of a Hermitian form is twice its scalar part. $\square$

The identity $\Phi(\tilde{Q}\tilde{Q}^{*}) = \Phi(\tilde{Q})\Phi(\tilde{Q})^{\dagger}$ is the reason the Hermitian form is positive definite in the realization: it is the product of a matrix with its conjugate transpose. It also displays the failure of multiplicativity in matrix terms — the product $\Phi(\tilde{P})\Phi(\tilde{Q})\Phi(\tilde{Q})^{\dagger}\Phi(\tilde{P})^{\dagger}$ is not $\Phi(\tilde{P}\tilde{Q}(\tilde{P}\tilde{Q})^{*})$ in general, since the two intermediate factors do not cancel.

## The Inner Product as the Hilbert–Schmidt Pairing

The sesquilinear companion of the Hermitian form is the Hilbert–Schmidt inner product of the matrix algebra, normalised so that it agrees with the coefficient inner product:

$$
\langle \tilde{P}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} P_{\bar\mu} Q_\mu = \tfrac{1}{2}\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

linear in the second argument and conjugate-linear in the first, with diagonal value

$$
\langle \tilde{Q}, \tilde{Q} \rangle = \bigl\|\tilde{Q}\bigr\|_E^2 = \mathrm{Sc}\bigl(\tilde{Q}\tilde{Q}^{*}\bigr),
$$

where the Euclidean norm is

$$
\bigl\|\tilde{Q}\bigr\|_E = \sqrt{\mathrm{Sc}\bigl(\tilde{Q}\tilde{Q}^{*}\bigr)} = \sqrt{\sum_{\mu=0}^{3} |Q_\mu|^2} = \frac{1}{\sqrt 2}\bigl\|\Phi(\tilde{Q})\bigr\|_F .
$$

The factor $\tfrac{1}{2}$ is the trace normalisation $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$ of the article; with it the matrix pairing is exactly the coefficient pairing, without it every value would be doubled.

## The Two Pairings Compared

The two pairings differ in one operation, and the realization makes the difference visible in a single symbol:

| | bilinear form | Hermitian form |
|---|---|---|
| matrix expression | $\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q})\bigr)$ | $\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr)$ |
| second factor | adjugate, no conjugation of the entries | conjugate transpose |
| scalar field | $\mathbb{C}$-valued | $\mathbb{C}$-valued, real on the diagonal |
| diagonal | $N(\tilde{Q}) = \det\Phi(\tilde{Q})$ | $\|\tilde{Q}\|_E^2 \geq 0$ |
| Gram matrix in the coefficient basis | $I_4$ (the sign matrix $D$ belongs to the product form $\mathrm{Sc}(\tilde{P}\tilde{Q})$ and to the Krein form) | $I_4$ |
| definiteness | indefinite, signature $(4,4)$ on $\mathbb{B}_{\mathbb{R}}$ | positive definite |
| vanishing on a nonzero element | yes, the null elements | no |

The two are exchanged by the passage from the matrix to its adjugate, which is conjugation, so the difference between the bilinear and the Hermitian form in the realization is the difference between a matrix and its conjugate transpose, weighted by the determinant in the bilinear case. This is the matrix statement of the coefficient-space comparison of *The Hermitian Form on the Biquaternion Algebra* and *The Bilinear Form on the Biquaternion Algebra*.

## Summary

The matrix realization $\Phi:\mathbb{B} \to M_2(\mathbb{C})$ carries both of the algebra's pairings in closed form. The scalar part is half the trace, so the bilinear form is $N(\tilde{P},\tilde{Q}) = \tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$, the natural conjugation being the adjugate, $\Phi(\tilde{Q}^{\natural}) = \operatorname{adj}\Phi(\tilde{Q})$; its diagonal is the determinant, $N(\tilde{Q}) = \det\Phi(\tilde{Q})$, its Gram matrix in the coefficient basis is $I_4$, and on the Hermitian and anti-Hermitian matrices its restriction has the signatures $(1,3)$ and $(3,1)$. The Hermitian form is the matrix product with the conjugate transpose, $\Phi(\tilde{Q}\tilde{Q}^{*}) = \Phi(\tilde{Q})\Phi(\tilde{Q})^{\dagger}$, its trace is the squared Frobenius norm, $\operatorname{Tr}(\tilde{Q}\tilde{Q}^{*}) = \|\Phi(\tilde{Q})\|_F^2$, and the inner product is the normalised Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$, whose diagonal is the squared Euclidean norm $\|\tilde{Q}\|_E^2 = \tfrac12\|\Phi(\tilde{Q})\|_F^2$. The two pairings differ only in that the bilinear form uses the adjugate where the Hermitian form uses the conjugate transpose, which is the matrix image of the difference between a bilinear and a sesquilinear pairing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ | Matrix realization, $\Phi(e_0) = I$, $\Phi(e_k) = -i\sigma_k$ |
| $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$ | Trace, twice the scalar part |
| $N(\tilde{P}, \tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$ | Bilinear form |
| $\Phi(\tilde{Q}^{\natural}) = \operatorname{adj}\Phi(\tilde{Q})$ | Natural conjugation is the adjugate |
| $N(\tilde{Q}, \tilde{Q}) = \det\Phi(\tilde{Q})$ | Diagonal of the bilinear form is the determinant |
| $G = \mathrm{I}_4$ | Gram matrix of the bilinear form in the coefficient basis (the sign matrix $\operatorname{diag}(1,-1,-1,-1)$ belongs to the product form $\mathrm{Sc}(\tilde{P}\tilde{Q})$ and to the Krein form) |
| $(1,3)$ and $(3,1)$ | Signatures of the restriction to $\mathbb{M}_+$ and $\mathbb{M}_-$, read as $\det$ |
| $\Phi(\tilde{Q}\tilde{Q}^{*}) = \Phi(\tilde{Q})\Phi(\tilde{Q})^{\dagger}$ | Hermitian form as the matrix product |
| $\|\cdot\|_F$ | Frobenius norm, $\|\Phi(\tilde{Q})\|_F = \sqrt 2\,\|\tilde{Q}\|_E$ |
| $\langle \tilde{P}, \tilde{Q}\rangle = \tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | Inner product as the Hilbert–Schmidt pairing |

## Further Reading

- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the realization, its trace, its determinant and the identification of the natural conjugation with the adjugate
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), the coefficient-space form, its polarisation and the signature table over the six subspaces
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), the coefficient-space Hermitian form, the inner product and the Euclidean norm
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the real forms, the real size function and the group of units
- *The Minkowski Form and the Modulus-Squared Map in the Matrix Representation* (`articles_maths/the-minkowski-form-and-the-modulus-squared-map-in-the-matrix-representation.md`), the companion FORM article for the second realization
- *The Unit Group and the Frobenius Norm in the Matrix Representation* (`articles_maths/the-unit-group-and-the-frobenius-norm-in-the-matrix-representation.md`), for the topological reading of the Euclidean norm
