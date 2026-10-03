# __The 4×4 Regular Matrix Representation under the Three Topologies__

## Introduction

The regular representation $\rho_L$ of *Biquaternion 4×4 Regular Matrix Element Representation* is the algebra acting on itself on the left, and the $4\times4$ regular matrix $\rho_L(\tilde{Q})$ is its carrier. That article reads the representation for the algebra: the left and right copies, their transposition relation, the determinant and the trace, the double centralizer and the decomposition $\mathbb{B}=I_1\oplus I_2$ of the regular module. This article reads the same representation for its **topology**, once for each of the three pairings of *The Three Pairings of the Biquaternion Algebra*.

The three pairings of the algebra act on the regular matrix through the three matrix operations that the representation makes available: the trace, which supplies the scalar part; the determinant and the adjugate; and the conjugate transpose, which supplies the Hermitian adjoint and makes $\rho_L$ a $*$-representation. In the coefficient basis the three can be read on the regular matrix itself, and they are kept apart in the three sections below.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$, sign matrix $D=\operatorname{diag}(-1,1,1,1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$; $\rho_L$ is the left regular representation in the basis $e_0,e_1,e_2,e_3$ of *Biquaternion 4×4 Regular Matrix Element Representation*.

## The Representation

**Definition.** The **left regular representation** is

$$
\rho_L(\tilde{Q})(\tilde{R})=\tilde{Q}\tilde{R},
$$

with $\rho_L(\tilde{Q})$ the $4\times4$ matrix of left multiplication in the basis $e_0,e_1,e_2,e_3$. It is a homomorphism, and the right regular representation $\rho_R(\tilde{Q})(\tilde{R})=\tilde{R}\tilde{Q}$ is the representation of the opposite algebra. In the basis of the corpus the two are related by the sign matrix $D=\operatorname{diag}(-1,1,1,1)$,

$$
\rho_R(\tilde{Q}) = D\,\rho_L(\tilde{Q})^{\mathsf{T}}D ,
$$

and the determinant and trace of the regular matrix are

$$
\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2 , \qquad \operatorname{Tr}\rho_L(\tilde{Q}) = 4Q_0 .
$$

## The Topology Induced by the Bilinear Form

**Theorem (the transpose relation is the bilinear pairing).** The bilinear form $B(\tilde{P},\tilde{Q})=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$ is read on the regular matrix by the transpose, in the form of the identity

$$
\rho_R(\tilde{Q}) = D\,\rho_L(\tilde{Q})^{\mathsf{T}}D ,
$$

In the basis of the corpus the transpose is the left matrix of the conjugate, $\rho_L(\tilde{Q})^{\mathsf{T}}=\rho_L(\tilde{Q}^{\natural})$, and the right matrix is its conjugate by the sign matrix, $\rho_R(\tilde{Q})=D\,\rho_L(\tilde{Q}^{\natural})D$.

**Proof.** These are the two transposition identities of *Biquaternion 4×4 Regular Matrix Element Representation*, read as pairings: the adjoint of $\rho_L(\tilde{Q})$ for the bilinear pairing is $\rho_L(\tilde{Q}^{\natural})$, exactly as $(L_{\tilde{Q}})^{B}=L_{\tilde{Q}^{\natural}}$ on the algebra in *The Three Pairings of the Biquaternion Algebra*.

**The determinant and the realification.** The bilinear invariant of the regular matrix is the determinant, $\det\rho_L(\tilde{Q})=N(\tilde{Q})^2$, the square of the algebra determinant because the regular module is the direct sum of two copies of the simple module; the trace is $4Q_0$. Over $\mathbb{R}$ the regular matrix is $8\times8$, of determinant $\lvert N(\tilde{Q})\rvert^4$ and trace $8\operatorname{Re}(Q_0)$, and the underlying real form of the bilinear pairing is the split form of signature $(4,4)$ on the coefficient space of the algebra.

**The null set.** The regular matrix is singular exactly when $\det\rho_L(\tilde{Q})=0$, that is when $N(\tilde{Q})=0$: the zero divisors of the algebra are the singular regular matrices, of rank two.

**The isometry group.** The bilinear pairing has Gram matrix $\mathrm{I}_4$ on the coefficients, so its isometry group is the complex orthogonal group $O_4(\mathbb{C})$, whose realification is the split orthogonal group $O(4,4)$; the transpose $M\mapsto M^{\mathsf{T}}$ is the elementary operator it defines, and the sign matrix $D$ conjugates it into the right multiplication.

## The Topology Induced by the Hermitian Form

**Theorem (the Hilbert–Schmidt pairing of the regular matrix).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q})\bigr) = 2\,\langle\tilde{P},\tilde{Q}\rangle ,
$$

so the Hilbert–Schmidt pairing of the regular matrices is twice the Hermitian form of the algebra.

**Proof.** The regular representation is built from the multiplication, and $\rho_L(\tilde{P})^{\dagger}=\rho_L(\tilde{P}^{*})$ because the left multiplication by $\tilde{P}$ has adjoint the left multiplication by $\tilde{P}^{*}$ for the Hermitian form; then $\operatorname{Tr}(\rho_L(\tilde{P}^{*}\tilde{Q}))=4\,\mathrm{Sc}(\tilde{P}^{*}\tilde{Q})=4\langle\tilde{P},\tilde{Q}\rangle$, and the factor $2$ follows.

**The Frobenius norm.** The diagonal case is

$$
\lVert\rho_L(\tilde{Q})\rVert_F^2 = \operatorname{Tr}\bigl(\rho_L(\tilde{Q})^{\dagger}\rho_L(\tilde{Q})\bigr) = 4\,\lVert\tilde{Q}\rVert_E^2 ,
$$

so the Frobenius norm of the regular matrix is twice the Euclidean norm of the element, and the Hilbert–Schmidt topology on the representation is the Euclidean topology of the algebra.

**The two-sided action and the double cover.** The positive definite form makes the Hermitian subspace $\mathbb{M}_+$ a Euclidean space of real dimension $4$, and the group $\tilde{G}=\{\tilde{A}:N(\tilde{A})=1\}$ acts on it by $\tilde{Q}\mapsto\tilde{A}\tilde{Q}\tilde{A}^{*}$, preserving the algebra determinant:

$$
N(\tilde{A}\tilde{Q}\tilde{A}^{*}) = N(\tilde{Q}) , \qquad \tilde{A}\in\tilde{G}.
$$

The group $\tilde{G}$ is $SL_2(\mathbb{C})$, and the action defines a surjective homomorphism

$$
SL_2(\mathbb{C}) \longrightarrow SO^+(1,3),
$$

with kernel $\{\pm e_0\}$: the two-to-one cover of the identity component of the orthogonal group of the restricted form. This is the group-theoretic content of the Hermitian topology on the regular representation, and it is read on the module in *Biquaternion Spin Geometry*; the connectedness of the image is *The Unit Group and the Frobenius Norm in the Matrix Representation*.

**The isometry group.** The Hilbert–Schmidt pairing on $M_4(\mathbb{C})$ lives on the sixteen complex coordinates, so its isometry group is $U(16)$, positive definite of real signature $(32,0)$; among these, the structure-preserving maps $X\mapsto UXV^{\dagger}$ form the subgroup $U(4)\times U(4)$ modulo the common centre.

## The Topology Induced by the Krein Form

**Theorem (the adjugate of the regular matrix).** The adjugate of the regular matrix is a scalar multiple of the regular matrix of the conjugate,

$$
\operatorname{adj}\rho_L(\tilde{P}) = N(\tilde{P})\,\rho_L(\tilde{P}^{\natural}),
$$

because $\det\rho_L(\tilde{P})=N(\tilde{P})^2$ and $\rho_L(\tilde{P})^{-1}=\rho_L(\tilde{P}^{\natural})/N(\tilde{P})$. Consequently the adjugated conjugate-transpose pairing of the regular matrices is

$$
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q})\bigr) = 2\,\overline{N(\tilde{P})}\,[\tilde{P},\tilde{Q}],
$$

the Krein form of the algebra up to the factor $2\overline{N(\tilde{P})}$; on the group $N=1$ it is exactly twice the Krein form, as on the $2\times2$ representation, whose coefficient Gram matrix is the sign matrix $E=\mathrm{diag}(1,-1,-1,-1)$.

**The inertia and the null set.** The form has complex inertia $(1,3)$ and real inertia $(2,6)$ on the coefficient space; its isotropic set is the cone $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^2=0$, distinct from the determinant null set. The operators that preserve it are the $J$-unitary operators of *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*, characterised in the coefficient basis by $\rho_L(\tilde{Q})^{*}E\rho_L(\tilde{Q})=E$; the $J$-self-adjoint operators are the ones self-adjoint for the same form.

**The fundamental symmetry.** The natural conjugation $J={}^{\natural}$ is an isometry of the Krein form; on the regular representation it is the transpose of the matrix, $\rho_L(\tilde{Q}^{\natural})=\rho_L(\tilde{Q})^{\mathsf{T}}$, and its role on the two-block decomposition is the theme of *The Fundamental Symmetry of the Biquaternion Algebra* and *The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra*.

**The isometry group.** The form is the complex Hermitian form of signature $(1,3)$, so its isometry group is $U(1,3)$; on the matrix side it is the group preserving the adjugated conjugate-transpose pairing, whose realification has isometry group $O(2,6)$.

## The Three Topologies Compared

| topology | reading on the regular matrix | signature over $\mathbb{R}$ | definiteness | null set |
|---|---|---|---|---|
| bilinear | transpose $\rho_R=D\rho_L^{\mathsf{T}}D$, determinant $\det\rho_L=N^2$ | $(4,4)$ on the coefficients | indefinite (split) | $N(\tilde{Q})=0$ |
| Hermitian | conjugate transpose, $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$ | $(32,0)$ on the matrices | positive definite | $\{0\}$ |
| Krein | adjugate of the conjugate transpose, Gram $E$ | $(2,6)$ | indefinite | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^2=0$ |

The three operations that carry the three topologies on the regular matrix are the transpose, the conjugate transpose and the adjugate of the conjugate transpose, and they correspond to the three operations on the algebra: the natural conjugation, the Hermitian conjugation and the complex conjugation. The determinant $\det\rho_L=N^2$ is the bilinear invariant, the Frobenius norm $2\lVert\tilde{Q}\rVert_E$ is the Hermitian invariant, and the sign matrix $E$ is the Krein invariant.

## Summary

The regular matrix carries the three topologies of the algebra through the three operations of the matrix algebra. The bilinear form is read by the transpose, through the identity $\rho_R(\tilde{Q})=D\rho_L(\tilde{Q})^{\mathsf{T}}D$ and the determinant $\det\rho_L(\tilde{Q})=N(\tilde{Q})^2$, on a split form of signature $(4,4)$; the Hermitian form is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$, positive definite, with the Frobenius norm $\lVert\rho_L(\tilde{Q})\rVert_F=2\lVert\tilde{Q}\rVert_E$ and the two-sided action of $\tilde{G}=SL_2(\mathbb{C})$ on $\mathbb{M}_+$ giving the double cover $SL_2(\mathbb{C})\to SO^+(1,3)$; and the Krein form is the adjugated conjugate-transpose pairing with Gram matrix $E$, of signature $(2,6)$, whose isometries are the $J$-unitary operators of the regular representation. The three operations are the transpose, the conjugate transpose and the adjugate of the conjugate transpose, corresponding to the natural, Hermitian and complex conjugations of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_L(\tilde{Q})$ | the $4\times4$ regular matrix of left multiplication |
| $\rho_R(\tilde{Q})=D\rho_L(\tilde{Q})^{\mathsf{T}}D$ | the right regular matrix, the transpose up to $D$ |
| $\det\rho_L(\tilde{Q})=N(\tilde{Q})^2$ | the bilinear invariant; $\operatorname{Tr}\rho_L(\tilde{Q})=4Q_0$ |
| $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$ | the Hermitian pairing of the regular matrices |
| $\lVert\rho_L(\tilde{Q})\rVert_F=2\lVert\tilde{Q}\rVert_E$ | the Frobenius norm of the regular matrix |
| $\operatorname{adj}\rho_L(\tilde{Q})^{\dagger}$ | the adjugate of the conjugate transpose, the Krein operation |
| $(4,4)$, $(32,0)$, $(2,6)$ | the three signatures over $\mathbb{R}$ |

## Further Reading

- *Biquaternion 4×4 Regular Matrix Element Representation* (`articles_maths/biquaternion-4x4-regular-matrix-element-representation.md`), for the regular representation in the Algebra group
- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for the three forms of the algebra and their isometry groups
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the three pairings of the matrices
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the adjugated trace pairings and the sign matrix
- *The Unit Group and the Frobenius Norm in the Matrix Representation* (`articles_maths/the-unit-group-and-the-frobenius-norm-in-the-matrix-representation.md`), for the unit group, the Frobenius norm and the connectedness of the Lorentz image
- *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-biquaternion-algebra.md`), for the operators attached to the third topology
