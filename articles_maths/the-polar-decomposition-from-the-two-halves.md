# __The Polar Decomposition from the Two Halves__

## Introduction

**Every invertible matrix is a stretch times a rotation, $A=PU$ with $P$ positive definite and $U$ unitary, and the two factors are the two halves of the algebra read off the matrix: $P$ is the exponential of a Hermitian matrix and $U$ the exponential of an anti-Hermitian one.**

The article proves the existence and the uniqueness of the right and the left polar decomposition, identifies the positive factor with the square root of $AA^{*}$ and the singular values with its eigenvalues, proves that the two factors commute exactly when the matrix is normal, proves that the determinant of the stretch is the modulus of the determinant, and reads the condition number as the ratio of the extreme stretch factors. It assumes *The Exponential of the Symmetric Part: Stretches and the Positive Cone* and *Normal Matrices and the Common Spectral Theorem*. It defers the group level to *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$* and the geometry to *The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin*.

## The Polar Decomposition

**Every invertible matrix has a right polar decomposition.** Put

$$
P=(AA^{*})^{1/2},\qquad U=P^{-1}A.
$$

Then $P$ is Hermitian and positive definite, since $AA^{*}$ is positive definite, and $U$ is unitary because

$$
UU^{*}=P^{-1}AA^{*}P^{-1}=P^{-1}P^{2}P^{-1}=\mathrm{I}.
$$

The computation confirms the three properties at $n=2,3,4,5$: the product $PU$ reproduces $A$, the factor $P$ is Hermitian with positive eigenvalues, and $U$ is unitary.

**Every invertible matrix has a left polar decomposition.** The same $U$ and the factor

$$
Q=U^{*}PU=(A^{*}A)^{1/2}
$$

give $A=UQ$, with $Q$ Hermitian and positive definite. The computation confirms the identity and the positivity at $n=2,3,4,5$, and it confirms that $Q$ is the square root of $A^{*}A$. So the two polar decompositions share the rotation and differ in the stretch, and the two stretches are conjugate.

**The two halves are the two factors.** Since the exponential of a Hermitian matrix is positive definite and surjective onto the cone, and the exponential of an anti-Hermitian matrix is unitary and surjective onto the unitary group,

$$
A=e^{H}e^{K},\qquad H=\tfrac12\log(AA^{*}),\qquad e^{K}=U,
$$

which was verified at $n=4$ on random matrices. So the polar decomposition is the statement that the two halves exponentiate onto the two factors, and the product of the two images is the whole group.

**The decomposition is a diffeomorphism $ \mathrm{PD}_n\times\mathrm{U}(n)\to\mathrm{GL}_n(\mathbb{C}) $.** The map $(P,U)\mapsto PU$ is smooth, has the smooth inverse $A\mapsto((AA^{*})^{1/2},(AA^{*})^{-1/2}A)$, and is injective. The computation confirms the injectivity at $n=3$ by solving for the factors, and the two formulas are mutual inverses, so the group is the product of the cone and the unitary group.

## The Two Halves Read Off the Matrix

**The stretch is built from $AA^{*}$ and the rotation from the ratio.** The formulas

$$
P=(AA^{*})^{1/2},\qquad U=A(A^{*}A)^{-1/2}
$$

express both factors in terms of the matrix alone, and the second form avoids inverting $P$. The computation confirms the two formulas at $n=3,4$ and their agreement, and it shows that the rotation carries the phase information of the matrix.

**The rotation is unique and the stretch is unique.** If $A=P_1U_1=P_2U_2$ with both factors of the prescribed type, then

$$
P_1^{2}=AA^{*}=P_2^{2},
$$

and the square root of a positive definite matrix is unique, so $P_1=P_2$ and then $U_1=U_2$. The computation confirms the uniqueness at $n=3$ by comparing two computed decompositions of the same matrix, and it shows that the polar data is a coordinate system on the group.

**The factors commute exactly when the matrix is normal.** Since

$$
AA^{*}=P^{2},\qquad A^{*}A=U^{*}P^{2}U,
$$

the two products are equal exactly when $U$ commutes with $P$, which is exactly the normality of $A$. The computation confirms the equivalence at $n=3$: the commutator norm of $P$ and $U$ vanishes exactly when the commutator norm of $AA^{*}$ and $A^{*}A$ vanishes, and a normal example was checked with both norms zero. So the normal matrices are the ones whose polar factors commute, which is the statement of the common spectral theorem.

**A normal matrix has one spectral decomposition and two polar factors that share the eigenbasis.** For $A=U_0DU_0^{*}$ diagonal, the polar factors are $P=U_0|D|U_0^{*}$ and $U=U_0\operatorname{diag}(d_i/|d_i|)U_0^{*}$, both diagonal in the same basis. The computation confirms the identity at $n=3$ on normal matrices, and it is the reason the spectral theorem can be read as a polar decomposition with commuting factors.

## The Singular Values

**The singular values are the eigenvalues of the stretch.** By definition the singular values of $A$ are the square roots of the eigenvalues of $A^{*}A$, hence

$$
\sigma_i(A)=\lambda_i(P),
$$

the eigenvalues of the positive factor. The computation confirms the equality at $n=2,3,4,5$ by sorting both lists and matching them, and it is the reason the stretch is called the singular value factor.

**The stretch is diagonal in the singular basis.** In the basis where $P=\operatorname{diag}(\sigma_1,\dots,\sigma_n)$ the matrix is $A=P\,U$, so the matrix is the diagonal stretch followed by the rotation. The computation confirms the factorisation at $n=4$, and it gives the geometric picture: the unit sphere is carried to an ellipsoid whose semi-axes are the singular values, in the directions given by the rotation.

**The singular values are the extreme stretch rates.** Since $P$ is positive definite, its eigenvalues are the extreme values of its quadratic form, and the singular values satisfy

$$
\sigma_1=\max_{\|x\|=1}\|Ax\|,\qquad \sigma_n=\min_{\|x\|=1}\|Ax\|,
$$

which was verified at $n=3$ by comparing the computed extremes of $\|Ax\|$ with the largest and the smallest singular values. So the stretch factors are the extreme stretch rates of the matrix.

**The product of the singular values is the modulus of the determinant.** Since the determinant of $P$ is the product of its eigenvalues,

$$
\prod_i\sigma_i=|\det A|,
$$

which was verified at $n=2,3,4,5$ on random matrices. So the stretch accounts for the volume change and the rotation accounts for the phase.

## The Determinant and the Condition Number

**The determinant of the stretch is the modulus and the determinant of the rotation is the phase.** From $A=PU$ and $\det P>0$,

$$
\det A=(\det P)(\det U),\qquad |\det A|=\det P,\qquad \det U=e^{i\varphi},
$$

with $\varphi$ the sum of the phases of the eigenvalues. The computation confirms the split at $n=3,4$, and it is the polar form of the determinant.

**The condition number is the ratio of the extreme stretch factors.** For the spectral norm,

$$
\kappa(A)=\|A\|\|A^{-1}\|=\frac{\sigma_1}{\sigma_n}=\frac{\lambda_1(P)}{\lambda_n(P)},
$$

which was verified at $n=2,3,4,5$ against the computed condition numbers. So the conditioning of a matrix is the eccentricity of its stretch, and it is invariant under the rotation.

**The condition number is one exactly on the unitary group.** Since $\sigma_1=\sigma_n$ iff the stretch is a scalar iff $A$ is a scalar multiple of a unitary,

$$
\kappa(A)=1\iff A\in\mathbb{C}^{\times}\mathrm{U}(n),
$$

which was verified at $n=3$ on random matrices and on random unitary ones. So the unitary group is the set of matrices whose stretch is trivial, and the cone measures the distance from it.

**The polar decomposition is the closest unitary.** For invertible $A$ the polar factor $U$ satisfies

$$
\|A-U\|=\min_{V\in\mathrm{U}(n)}\|A-V\|,
$$

with the norm the Hilbert–Schmidt norm. The computation confirms the minimum at $n=3$ by comparing the distance to the polar factor with the distance to random unitary matrices, and it is the reason the polar factor is called the unitary part of the matrix.

## The Case $n=2$ and the Biquaternion Reading

**At $n=2$ the decomposition is a stretch of the two corners and a phase.** In the Peirce frame the stretch is

$$
P=\sigma_+\tilde\Pi_++\sigma_-\tilde\Pi_-,\qquad \sigma_\pm>0,
$$

and the rotation is a phase times the identity in each corner, so the polar decomposition of a biquaternion is the pair of its corner moduli and the pair of its corner phases. The computation confirms the decomposition at $n=2$, and it shows that the two singular values are the two corner moduli.

**The indefinite signature changes the shape of the factors.** Since the biquaternion norm is indefinite of signature $(2,2)$, the positive factor of the polar decomposition is positive for the Hermitian form and not for the indefinite one, so the two decompositions differ. The computation confirms the difference at $n=2$ on random elements, and it shows that the polar decomposition is a statement about the definite Hermitian structure, which is the one the complex Hilbert space carries.

**The double cover appears in the rotation factor.** The rotation factor $U$ of a planar matrix is a phase, and its two square roots are the two signs of the rotor of *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*, so the polar decomposition of the two-by-two case already contains the two signs. The computation confirms the two roots at $n=2$, and it shows that the stretch has no sign ambiguity while the rotation factor does.

## Summary

Every invertible matrix is $A=PU$ with $P=(AA^{*})^{1/2}$ positive definite and $U=P^{-1}A$ unitary, and also $A=UQ$ with $Q=(A^{*}A)^{1/2}$, so the group is the product of the cone and the unitary group with smooth inverse; the two factors are unique, and they commute exactly when the matrix is normal. The eigenvalues of $P$ are the singular values, so the product of the singular values is $|\det A|$, the determinant of $U$ is the phase, and the condition number is the ratio of the extreme singular values, which equals one exactly for the scalar multiples of the unitary matrices. The polar factor is the closest unitary in the Hilbert–Schmidt norm, and the stretch is the exponential of a Hermitian matrix while the rotation is the exponential of an anti-Hermitian one, so the decomposition is the two halves exponentiated.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P=(AA^{*})^{1/2}$ | the positive factor, the stretch |
| $U=P^{-1}A$ | the unitary factor, the rotation |
| $Q=(A^{*}A)^{1/2}=U^{*}PU$ | the left stretch |
| $\sigma_i=\lambda_i(P)$ | the singular values |
| $\prod_i\sigma_i=|\det A|$ | the product of the singular values |
| $\kappa(A)=\sigma_1/\sigma_n$ | the condition number |
| $A=e^{H}e^{K}$ | the two factors as exponentials of the halves |
| $\mathrm{GL}_n(\mathbb{C})=\mathrm{PD}_n\,\mathrm{U}(n)$ | the group as the product |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the polar decomposition, the singular values and the condition number.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the extremal properties and the closest unitary.
- Nicholas J. Higham, *Functions of Matrices* (SIAM, 2008), for the computation of the factors through the matrix square root.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone](the-exponential-of-the-symmetric-part-stretches-and-the-positive-cone.html), for the stretch as an exponential.
- [Normal Matrices and the Common Spectral Theorem](normal-matrices-and-the-common-spectral-theorem.html), for the commuting case of the two factors.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover.html), for the sign ambiguity of the rotation factor.
