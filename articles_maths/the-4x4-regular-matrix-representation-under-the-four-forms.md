# __The 4×4 Regular Matrix Representation under the Four Forms__

## Introduction

The regular representation $\rho_L$ of *Biquaternion 4×4 Regular Matrix Element Representation* is the algebra acting on itself on the left, and the $4\times4$ regular matrix $\rho_L(\tilde{Q})$ is its carrier. That article reads the representation for the algebra: the left and right copies, their transposition relation, the determinant and the trace, the double centralizer and the decomposition $\mathbb{B}=I_1\oplus I_2$ of the regular module. This article reads the same representation for its **topology**, once for each of the four pairings of *The Four Pairings of the Biquaternion Algebra*.

The four pairings of the algebra act on the regular matrix through the four matrix operations that the representation makes available: the trace and the plain product, which supply the scalar part; the determinant and the adjugate; and the conjugate transpose, which supplies the Hermitian adjoint and makes $\rho_L$ a $*$-representation. In the coefficient basis the four can be read on the regular matrix itself, and they are kept apart in the four sections below.

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
\det\rho_L(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2 , \qquad \operatorname{Tr}\rho_L(\tilde{Q}) = 4Q_0 .
$$

## The Complex Bilinear Pairing of the Regular Matrix

**Theorem (the plain pairing of the regular matrix).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\rho_L(\tilde{P})\rho_L(\tilde{Q})\bigr) = 2\,\langle\tilde{P},\tilde{Q}\rangle ,
$$

so the plain trace pairing of the regular matrices is twice the complex bilinear form of the algebra.

**Proof.** The regular representation is a homomorphism, so $\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q}))=\operatorname{Tr}\rho_L(\tilde{P}\tilde{Q})=4\,\mathrm{Sc}(\tilde{P}\tilde{Q})=4\langle\tilde{P},\tilde{Q}\rangle$, and the factor $2$ follows.

**The invariant and the realification.** The diagonal case is $\tfrac12\operatorname{Tr}(\rho_L(\tilde{Q})\rho_L(\tilde{Q}))=2\langle\tilde{Q},\tilde{Q}\rangle=2\sum_\mu\varepsilon_\mu Q_\mu^2$, the complex bilinear invariant of the regular matrix; over $\mathbb{R}$ its coefficient Gram matrix is the sign matrix $E=\mathrm{diag}(1,-1,-1,-1)$, of real signature $(4,4)$ on the coefficient space of the algebra.

**The null set.** The set on which the pairing vanishes is the cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of the complex bilinear form, of real dimension $6$ in the coefficient space; it is not the null set of any of the other three pairings.

**The isometry group.** The pairing has coefficient Gram matrix $E$, so its isometry group is the complex orthogonal group $O_4(\mathbb{C})$, and the real part of the form
is a real bilinear form of signature $(4,4)$ with isometry group $O(4,4)$; the plain product is the
elementary operator it defines on the regular matrix.

## The Quaternion Bilinear Pairing of the Regular Matrix

**Theorem (the transpose relation is the quaternion bilinear pairing).** The bilinear form $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$ is read on the regular matrix by the transpose, in the form of the identity

$$
\rho_R(\tilde{Q}) = D\,\rho_L(\tilde{Q})^{\mathsf{T}}D ,
$$

In the basis of the corpus the transpose is the left matrix of the conjugate, $\rho_L(\tilde{Q})^{\mathsf{T}}=\rho_L(\tilde{Q}^{\natural})$, and the right matrix is its conjugate by the sign matrix, $\rho_R(\tilde{Q})=D\,\rho_L(\tilde{Q}^{\natural})D$.

**Proof.** These are the two transposition identities of *Biquaternion 4×4 Regular Matrix Element Representation*, read as pairings: the adjoint of $\rho_L(\tilde{Q})$ for the quaternion bilinear pairing is $\rho_L(\tilde{Q}^{\natural})$, exactly as $(L_{\tilde{Q}})^{B}=L_{\tilde{Q}^{\natural}}$ on the algebra in *The Four Pairings of the Biquaternion Algebra*.

**The determinant and the realification.** The bilinear invariant of the regular matrix is the determinant, $\det\rho_L(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$, the square of the algebra determinant because the regular module is the direct sum of two copies of the simple module; the trace is $4Q_0$. Over $\mathbb{R}$ the regular matrix is $8\times8$, of determinant $\lvert \langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert^4$ and trace $8\operatorname{Re}(Q_0)$, and the underlying real form of the quaternion bilinear pairing is the split form of signature $(4,4)$ on the coefficient space of the algebra.

**The null set.** The regular matrix is singular exactly when $\det\rho_L(\tilde{Q})=0$, that is when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0$: the zero divisors of the algebra are the singular regular matrices, of rank two.

**The isometry group.** The quaternion bilinear pairing has Gram matrix $\mathrm{I}_4$ on the coefficients, so its isometry group is the complex orthogonal group $O_4(\mathbb{C})$, whose realification is the split orthogonal group $O(4,4)$; the transpose $M\mapsto M^{\mathsf{T}}$ is the elementary operator it defines, and the sign matrix $D$ conjugates it into the right multiplication.

## The Complex Sesquilinear Pairing of the Regular Matrix

**Theorem (the Hilbert–Schmidt pairing of the regular matrix).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q})\bigr) = 2\,\langle\tilde{Q},\tilde{P}\rangle_{*} ,
$$

so the Hilbert–Schmidt pairing of the regular matrices is twice the complex sesquilinear form of the algebra.

**Proof.** The regular representation is built from the multiplication, and $\rho_L(\tilde{P})^{\dagger}=\rho_L(\tilde{P}^{*})$ because the left multiplication by $\tilde{P}$ has adjoint the left multiplication by $\tilde{P}^{*}$ for the complex sesquilinear form; then $\operatorname{Tr}(\rho_L(\tilde{P}^{*}\tilde{Q}))=4\,\mathrm{Sc}(\tilde{P}^{*}\tilde{Q})=4\langle\tilde{Q},\tilde{P}\rangle_{*}$, and the factor $2$ follows.

**The Frobenius norm.** The diagonal case is

$$
\lVert\rho_L(\tilde{Q})\rVert_F^2 = \operatorname{Tr}\bigl(\rho_L(\tilde{Q})^{\dagger}\rho_L(\tilde{Q})\bigr) = 4\,\lVert\tilde{Q}\rVert_E^2 ,
$$

so the Frobenius norm of the regular matrix is twice the Euclidean norm of the element, and the Hilbert–Schmidt topology on the representation is the Euclidean topology of the algebra.

**The two-sided action and the double cover.** The positive definite form makes the Hermitian subspace $\mathbb{M}_+$ a Euclidean space of real dimension $4$, and the group $\tilde{G}=\{\tilde{A}:\langle\tilde{A},\tilde{A}\rangle_{\natural}=1\}$ acts on it by $\tilde{Q}\mapsto\tilde{A}\tilde{Q}\tilde{A}^{*}$, preserving the algebra determinant:

$$
\langle\tilde{A}\tilde{Q}\tilde{A}^{*},\tilde{A}\tilde{Q}\tilde{A}^{*}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} , \qquad \tilde{A}\in\tilde{G}.
$$

The group $\tilde{G}$ is $SL_2(\mathbb{C})$, and the action defines a surjective homomorphism

$$
SL_2(\mathbb{C}) \longrightarrow SO^+(1,3),
$$

with kernel $\{\pm e_0\}$: the two-to-one cover of the identity component of the orthogonal group of the restricted form. This is the group-theoretic content of the complex sesquilinear topology on the regular representation, and it is read on the module in *Biquaternion Spin Geometry*; the connectedness of the image is *The Unit Group and the Frobenius Norm in the Matrix Representation*.

**The isometry group.** The Hilbert–Schmidt pairing on $M_4(\mathbb{C})$ lives on the sixteen complex coordinates, so its isometry group is $U(16)$, positive definite of real signature $(32,0)$; among these, the structure-preserving maps $X\mapsto UXV^{\dagger}$ form the subgroup $U(4)\times U(4)$ modulo the common centre.

## The Quaternion Sesquilinear Pairing of the Regular Matrix

**Theorem (the adjugate of the regular matrix).** The adjugate of the regular matrix is a scalar multiple of the regular matrix of the conjugate,

$$
\operatorname{adj}\rho_L(\tilde{P}) = \langle\tilde{P},\tilde{P}\rangle_{\natural}\,\rho_L(\tilde{P}^{\natural}),
$$

because $\det\rho_L(\tilde{P})=\langle\tilde{P},\tilde{P}\rangle_{\natural}^2$ and $\rho_L(\tilde{P})^{-1}=\rho_L(\tilde{P}^{\natural})/\langle\tilde{P},\tilde{P}\rangle_{\natural}$. Consequently the adjugated conjugate-transpose pairing of the regular matrices is

$$
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q})\bigr) = 2\,\overline{\langle\tilde{P},\tilde{P}\rangle_{\natural}}\,\langle\tilde{Q},\tilde{P}\rangle_{\natural*},
$$

the quaternion sesquilinear form of the algebra up to the factor $2\overline{\langle\tilde{P},\tilde{P}\rangle_{\natural}}$; on the group $N=1$ it is exactly twice the quaternion sesquilinear form, as on the $2\times2$ representation, whose coefficient Gram matrix is the sign matrix $E=\mathrm{diag}(1,-1,-1,-1)$.

**The inertia and the null set.** The form has complex inertia $(1,3)$ and real inertia $(2,6)$ on the coefficient space; its isotropic set is the cone $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^2=0$, distinct from the determinant null set. The operators that preserve it are the $J$-unitary operators of *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*, characterised in the coefficient basis by $\rho_L(\tilde{Q})^{*}E\rho_L(\tilde{Q})=E$; the $J$-self-adjoint operators are the ones self-adjoint for the same form.

**The fundamental symmetry.** The natural conjugation $J={}^{\natural}$ is an isometry of the quaternion sesquilinear form; on the regular representation it is the transpose of the matrix, $\rho_L(\tilde{Q}^{\natural})=\rho_L(\tilde{Q})^{\mathsf{T}}$, and its role on the two-block decomposition is the theme of *The Fundamental Symmetry of the Biquaternion Algebra* and *The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra*.

**The isometry group.** The form is the quaternion sesquilinear form of signature $(1,3)$, so its isometry group is $U(1,3)$; on the matrix side it is the group preserving the adjugated conjugate-transpose pairing, whose realification has isometry group $O(2,6)$.

## The Four Forms Compared

| form | reading on the regular matrix | signature over $\mathbb{R}$ | definiteness | null set |
|---|---|---|---|---|
| complex bilinear | plain product, $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$ | $(4,4)$ on the coefficients | indefinite | $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ |
| quaternion bilinear | transpose $\rho_R=D\rho_L^{\mathsf{T}}D$, determinant $\det\rho_L(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$ | $(4,4)$ on the coefficients | indefinite (split) | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0$ |
| complex sesquilinear | conjugate transpose, $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q}))=2\langle\tilde{Q},\tilde{P}\rangle_{*}$ | $(32,0)$ on the matrices | positive definite | $\{0\}$ |
| quaternion sesquilinear | adjugate of the conjugate transpose, Gram $E$ | $(2,6)$ | indefinite | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^2=0$ |

The four operations that carry the four topologies on the regular matrix are the plain product, the transpose, the conjugate transpose and the adjugate of the conjugate transpose, and they correspond to the four operations on the algebra: the plain product, the natural conjugation, the Hermitian conjugation and the complex conjugation. The complex bilinear invariant is $\tfrac12\operatorname{Tr}(\rho_L(\tilde{Q})\rho_L(\tilde{Q}))=2\sum_\mu\varepsilon_\mu Q_\mu^2$, the quaternion bilinear invariant is the determinant $\det\rho_L(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$, the complex sesquilinear invariant is the Frobenius norm $2\lVert\tilde{Q}\rVert_E$, and the quaternion sesquilinear invariant is the sign matrix $E$.
## Summary

The regular matrix carries the four topologies of the algebra through the four operations of the matrix algebra. The complex bilinear form is read by the plain product, $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$, on a form of signature $(4,4)$ with the sign matrix $E$ as coefficient Gram matrix; the quaternion bilinear form is read by the transpose, through the identity $\rho_R(\tilde{Q})=D\rho_L(\tilde{Q})^{\mathsf{T}}D$ and the determinant $\det\rho_L(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$, on a split form of signature $(4,4)$; the complex sesquilinear form is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q}))=2\langle\tilde{Q},\tilde{P}\rangle_{*}$, positive definite, with the Frobenius norm $\lVert\rho_L(\tilde{Q})\rVert_F=2\lVert\tilde{Q}\rVert_E$ and the two-sided action of $\tilde{G}=SL_2(\mathbb{C})$ on $\mathbb{M}_+$ giving the double cover $SL_2(\mathbb{C})\to SO^+(1,3)$; and the quaternion sesquilinear form is the adjugated conjugate-transpose pairing with Gram matrix $E$, of signature $(2,6)$, whose isometries are the $J$-unitary operators of the regular representation. The four operations are the plain product, the transpose, the conjugate transpose and the adjugate of the conjugate transpose, corresponding to the plain product, the natural conjugation, the Hermitian conjugation and the complex conjugation of the algebra.
## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_L(\tilde{Q})$ | the $4\times4$ regular matrix of left multiplication |
| $\rho_R(\tilde{Q})=D\rho_L(\tilde{Q})^{\mathsf{T}}D$ | the right regular matrix, the transpose up to $D$ |
| $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})\rho_L(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$ | the complex bilinear pairing of the regular matrices |
| $\det\rho_L(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$ | the quaternion bilinear invariant; $\operatorname{Tr}\rho_L(\tilde{Q})=4Q_0$ |
| $\tfrac12\operatorname{Tr}(\rho_L(\tilde{P})^{\dagger}\rho_L(\tilde{Q}))=2\langle\tilde{Q},\tilde{P}\rangle_{*}$ | the complex sesquilinear pairing, the Hilbert–Schmidt pairing |
| $\lVert\rho_L(\tilde{Q})\rVert_F=2\lVert\tilde{Q}\rVert_E$ | the Frobenius norm of the regular matrix |
| $\operatorname{adj}\rho_L(\tilde{Q})^{\dagger}$ | the adjugate of the conjugate transpose, the quaternion sesquilinear operation |
| $(4,4)$, $(4,4)$, $(32,0)$, $(2,6)$ | the four signatures over $\mathbb{R}$ |
## Further Reading

- *Biquaternion 4×4 Regular Matrix Element Representation* (`articles_maths/biquaternion-4x4-regular-matrix-element-representation.md`), for the regular representation in the Algebra group
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms of the algebra and their isometry groups
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the four pairings of the matrices
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the plain pairing and its isotropic structure
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the adjugated trace pairings and the sign matrix
- *The Unit Group and the Frobenius Norm in the Matrix Representation* (`articles_maths/the-unit-group-and-the-frobenius-norm-in-the-matrix-representation.md`), for the unit group, the Frobenius norm and the connectedness of the Lorentz image
- *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-biquaternion-algebra.md`), for the operators attached to the quaternion sesquilinear form
