# __The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$ with the Hermitian conjugation ${}^{*}$, and write $A=\mathsf{M}_2(\tilde Q)$ for the matrix of an element. This article is the spectral registry of the one-sided and two-sided operators of the algebra, and it owns the two results that the neighbouring articles do not state: the spectrum and the explicit solution of the two-parameter Sylvester operator $L_{\tilde Q_1}+R_{\tilde D}$, and the signature of the sandwich of a Hermitian element.

The spectra of the one-sided operators and of the sandwich are not proved here. They are proved in *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Eigenbasis of Left Multiplication*, *Eigenbasis of a Biquaternion in Matrix Elements Representations*, §*The Diagonal Form*, and *Two-Sided Operator and the Polar Decomposition*, §*The Spectrum of the Sandwich*; the type criteria and the phase blindness are in *Two-Sided Operators on the General Plain Sesqualgebra*. The one-parameter Hermitian Sylvester equation is *The Hermitian Sylvester Equation with Hermitian Adjoint*. The article restates the rules once, without proof, and then develops only what is new.

## The Spectral Registry

**Convention (two vectorisations).** The Kronecker formulas below are written for the row-major vectorisation of the matrix, $\mathrm{vec}(A)=(A_{11},A_{12},A_{21},A_{22})$. The coefficient vector $(Q_t,Q_x,Q_y,Q_z)$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is another vectorisation; the two are related by the fixed invertible change of basis $\tilde Q\mapsto\mathrm{vec}(\mathsf{M}_2(\tilde Q))$, so an operator has similar matrices in the two and the same spectrum. The Kronecker formulas are exact in the matrix vectorisation and are not identities in the coefficient basis. In particular the Sylvester solution below is a matrix identity, not a coefficient identity.

**Proposition (the operators as Kronecker products).** Let $A=\mathsf{M}_2(\tilde Q_1)$ and $B=\mathsf{M}_2(\tilde D)$. On $\mathbb{C}^{4}$,

$$
L_{\tilde Q_1}=A\otimes I_{2},\qquad R_{\tilde D}=I_{2}\otimes B^{T},\qquad \Theta_{\tilde Q}=A\otimes\overline{A},
$$

and the Sylvester operator is $L_{\tilde Q_1}+R_{\tilde D}=A\otimes I_{2}+I_{2}\otimes B^{T}$.

*Proof.* Left multiplication acts on the row index of the matrix and right multiplication on the column index; the row-major vectorisation turns the two actions into the two Kronecker factors. For the sandwich, $\tilde Q^{*}$ contributes the right factor $(\mathsf{M}_2(\tilde Q^{*}))^{T}=\overline{\mathsf{M}_2(\tilde Q)}$.

**The registry.** Let $\lambda_1,\lambda_2$ be the eigenvalues of $A$ and $\mu_1,\mu_2$ those of $B$, repeated with algebraic multiplicity. Then

$$
\operatorname{spec}(L_{\tilde Q_1})=\{\lambda_1,\lambda_1,\lambda_2,\lambda_2\},\qquad
\operatorname{spec}(R_{\tilde D})=\{\mu_1,\mu_1,\mu_2,\mu_2\},
$$

$$
\operatorname{spec}(\Theta_{\tilde Q})=\{\lambda_i\overline{\lambda_j}\ :\ i,j=1,2\},\qquad
\operatorname{spec}(\mathrm{ad}_{\tilde Q_1})=\{\lambda_i-\lambda_j\ :\ i,j=1,2\},
$$

the derivation being $L_{\tilde Q_1}-R_{\tilde Q_1}$. The one-sided rules are the doubling of the element spectrum in the eigenbasis of the two regular representations; the sandwich rule is that of *Two-Sided Operator and the Polar Decomposition*, §*The Spectrum of the Sandwich*; the derivation rule is the difference of the one-sided rules. The sandwich has

$$
\operatorname{tr}(\Theta_{\tilde Q})=\lvert\operatorname{tr}A\rvert^{2},\qquad
\det(\Theta_{\tilde Q})=\lvert\det A\rvert^{4},\qquad
\operatorname{rank}(\Theta_{\tilde Q})=(\operatorname{rank}A)^{2}.
$$

The central phase is invisible to the sandwich, $\Theta_{\omega\tilde Q}=\Theta_{\tilde Q}$ for $\lvert\omega\rvert=1$, and the type criteria are those of *Two-Sided Operators on the General Plain Sesqualgebra*.

## The Two-Parameter Sylvester Operator

**Theorem (the spectrum).** For $A=\mathsf{M}_2(\tilde Q_1)$ and $B=\mathsf{M}_2(\tilde D)$,

$$
\operatorname{spec}(L_{\tilde Q_1}+R_{\tilde D})=\{\lambda_i+\mu_j\ :\ i,j=1,2\},\qquad
\det(L_{\tilde Q_1}+R_{\tilde D})=\prod_{i,j}(\lambda_i+\mu_j).
$$

The operator is invertible exactly when no eigenvalue of $A$ is the negative of an eigenvalue of $B$.

*Proof.* The Kronecker sum $A\otimes I_2+I_2\otimes B^{T}$ has the pairwise sums as eigenvalues, and its determinant is their product.

**Theorem (the solution).** When the operator is invertible, the unique solution of $\tilde Q_1X+X\tilde D=c$ is

$$
\operatorname{vec}(\mathsf{M}_2(X))=\bigl(A\otimes I_{2}+I_{2}\otimes B^{T}\bigr)^{-1}\operatorname{vec}(\mathsf{M}_2(c)).
$$

If $A$ and $B$ commute and are diagonalisable, let $P$ diagonalise both, $\Lambda=P^{-1}AP$, $M=P^{-1}BP$, and put $Y=P^{-1}\mathsf{M}_2(X)P$ and $C'=P^{-1}\mathsf{M}_2(c)P$. Then

$$
Y_{ij}=\frac{C'_{ij}}{\lambda_i+\mu_j}.
$$

Without commutativity there is no common eigenbasis, and the entrywise formula does not apply; the Kronecker inverse is the general solution.

*Proof.* Conjugate the equation by $P^{-1}$ and $P$: the two terms become $\Lambda Y$ and $YM$, so each entry is multiplied by $\lambda_i+\mu_j$. The Kronecker inverse is the vectorised form of the same equation and needs no commutativity.

**Example (the singular Hermitian case).** For $\tilde Q_1=\tilde D=i\vec e_z$ the matrix is $A=B=\sigma_3=\operatorname{diag}(1,-1)$, the operator $L_{i\vec e_z}+R_{i\vec e_z}$ has the spectrum $\{2,0,0,-2\}$ and is singular. The homogeneous equation $i\vec e_zX+Xi\vec e_z=0$ has the two-dimensional solution space spanned by the matrix units $E_{12}$ and $E_{21}$.

**Example (the anti-Hermitian case).** For $\tilde Q_1=\vec e_z$ and $\tilde D=\tilde Q_1^{*}=-\vec e_z$ the matrices are $A=\operatorname{diag}(-i,i)$ and $B=-A$, and the operator is the inner derivation

$$
L_{\vec e_z}+R_{-\vec e_z}=L_{\vec e_z}-R_{\vec e_z}=\mathrm{ad}_{\vec e_z},
$$

skew-adjoint, of spectrum $\{0,2i,-2i,0\}$. The equation is the derivation equation, not the Hermitian Sylvester equation; the choice $\tilde D=\tilde Q_1^{*}$ gives the Hermitian Sylvester operator of *The Hermitian Sylvester Equation with Hermitian Adjoint*, which is self-adjoint when $\tilde Q_1$ is Hermitian.

## The Sandwich of a Hermitian Element

**Theorem (the signature).** Let $\tilde Q$ be Hermitian, and let $(n_+,n_-,n_0)$ be the inertia of $A=\mathsf{M}_2(\tilde Q)$: $n_+$ positive, $n_-$ negative and $n_0$ zero eigenvalues, with $n_++n_-+n_0=2$. Then

$$
\operatorname{sig}(\Theta_{\tilde Q})=\bigl(n_+^{2}+n_-^{2},\ 2n_+n_-\bigr).
$$

Hence $\Theta_{\tilde Q}$ is positive semidefinite exactly when $n_+n_-=0$, and positive definite exactly when moreover $n_0=0$.

*Proof.* The eigenvalues of $A$ are real, so the four eigenvalues of the sandwich are the products $\lambda_i\lambda_j$. A product is positive exactly for an ordered pair of eigenvalues of the same nonzero sign, of which there are $n_+^{2}+n_-^{2}$, and negative exactly for an ordered pair of opposite signs, of which there are $2n_+n_-$; a zero eigenvalue gives a zero product.

**Remark (a real spectrum is not self-adjointness).** The spectrum of $\Theta_{\tilde Q}$ can be real without the operator being self-adjoint. Take

$$
\mathsf{M}_2(\tilde Q)=\begin{pmatrix}1&1\\0&2\end{pmatrix},\qquad
\tilde Q=\tfrac32e_t+\tfrac{i}{2}\vec e_x-\tfrac12\vec e_y-\tfrac{i}{2}\vec e_z .
$$

The matrix is not normal, and $A^{*}=\omega A$ with $\lvert\omega\rvert=1$ would make it normal, so $\tilde Q$ is not Hermitian up to a central phase and $\Theta_{\tilde Q}$ is not self-adjoint; its spectrum is $\{1,2,2,4\}$, real. Self-adjointness is the identity $\Theta_{\tilde Q}=\Theta_{\tilde Q}^{*}$, and the reality of the spectrum is only a consequence of it. For a non-self-adjoint $\Theta_{\tilde Q}$ the numerical range is not real, by the Toeplitz–Hausdorff theorem, even when every eigenvalue is real; the quadratic form then takes complex values.

## Summary

On the biquaternion algebra the spectral registry is $\operatorname{spec}L_{\tilde Q}=\{\lambda_1,\lambda_1,\lambda_2,\lambda_2\}$, the same for $R_{\tilde D}$ with $\mu_j$; $\operatorname{spec}\Theta_{\tilde Q}=\{\lambda_i\overline{\lambda_j}\}$, with trace $\lvert\operatorname{tr}A\rvert^{2}$, determinant $\lvert\det A\rvert^{4}$ and rank $(\operatorname{rank}A)^{2}$; and $\operatorname{spec}\mathrm{ad}_{\tilde Q}=\{\lambda_i-\lambda_j\}$. The two-parameter Sylvester operator has the pairwise sums $\lambda_i+\mu_j$, is invertible exactly when no $\lambda_i$ equals $-\mu_j$, and is solved by the Kronecker inverse, or entrywise by $Y_{ij}=C'_{ij}/(\lambda_i+\mu_j)$ when the two parameters commute. For a Hermitian element of inertia $(n_+,n_-,n_0)$ the sandwich has signature $(n_+^{2}+n_-^{2},2n_+n_-)$, so it is positive semidefinite exactly when $n_+n_-=0$ and positive definite exactly when moreover $n_0=0$. A real spectrum does not imply self-adjointness: the counterexample $\mathsf{M}_2(\tilde Q)=\begin{pmatrix}1&1\\0&2\end{pmatrix}$ has the real spectrum $\{1,2,2,4\}$ and is not self-adjoint.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=\mathsf{M}_2(\tilde Q)$ | The $2\times2$ matrix of the element $\tilde Q$ |
| $\mathrm{vec}$ | Row-major vectorisation of the matrix, $\mathrm{vec}(A)=(A_{11},A_{12},A_{21},A_{22})$ |
| $L_{\tilde Q_1}=A\otimes I_2$ | Left multiplication; spectrum $\lambda_i$, each twice |
| $R_{\tilde D}=I_2\otimes B^{T}$ | Right multiplication; spectrum $\mu_j$, each twice |
| $\Theta_{\tilde Q}=A\otimes\overline{A}$ | Sandwich $\tilde QX\tilde Q^{*}$; spectrum $\lambda_i\overline{\lambda_j}$ |
| $\mathrm{ad}_{\tilde Q}=L_{\tilde Q}-R_{\tilde Q}$ | Inner derivation; spectrum $\lambda_i-\lambda_j$ |
| $L_{\tilde Q_1}+R_{\tilde D}$ | Sylvester operator; spectrum $\lambda_i+\mu_j$ |
| $(n_+,n_-,n_0)$ | Inertia of a Hermitian element; $\operatorname{sig}(\Theta_{\tilde Q})=(n_+^{2}+n_-^{2},2n_+n_-)$ |

## Further Reading

- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the element spectrum and the eigenbasis of left multiplication.
- [Eigenbasis of a Biquaternion in Matrix Elements Representations](eigenbasis-of-a-biquaternion-in-matrix-elements-representations.html), §*The Diagonal Form*, for the doubling of the one-sided spectra in the $4\times4$ representation.
- [Two-Sided Operator and the Polar Decomposition](two-sided-operator-and-the-polar-decomposition.html), §*The Spectrum of the Sandwich*, for the products $\lambda_i\overline{\lambda_j}$ and the phase cancellation.
- [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html), for the type criteria, the phase blindness and the positivity of the sandwich.
- [The Hermitian Sylvester Equation with Hermitian Adjoint](the-hermitian-sylvester-equation-with-hermitian-adjoint.html), for the one-parameter equation $L_{\tilde Q}+R_{\tilde Q^{*}}$.
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the derivations whose spectrum is the difference rule.
- [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the trace and the determinant of the sandwich in the regular basis.
