# __The Hermitian Pair of Operators Acting on Two Sides in $M_n(\mathbb{C})$__

## Introduction

**The question.** When is a two-sided operator $T_{A,B}(X)=AXB$ self-adjoint, what are its eigenvalues, and what is the cone of positive two-sided operators?

**The answer in one line.** $T_{A,B}^{\dagger}=T_{A^{*},B^{*}}$, so for Hermitian $A,B$ the operator $T_{A,B}$ is self-adjoint with spectrum
$$
\{\lambda_i(A)\lambda_j(B)\},
$$
and it is positive semidefinite exactly when $A$ and $B$ are both positive semidefinite or both negative semidefinite.

**Why the article is needed.** A first guess is that the positive two-sided operators are the $T_{A,A^{*}}$ with $A$ positive. The guess is false: $T_{A,A}$ with $A=\operatorname{diag}(1,-1)$ is self-adjoint and has a negative eigenvalue. The positivity of a product is a property of the *pair*, not of a single parameter, and the one-sided intuition, where positivity is transported from the parameter without change, breaks at exactly this point.

**Boundaries.** The one-sided Hermitian pairs are *The Hermitian Pair of Operators Acting on One Side in $M_n(\mathbb{C})$*; the adjoints and the difference family are *The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$*; the singular values are *The SVD of Endomorphisms of $M_n(\mathbb{C})$*. The biquaternion original is *The Hermitian Pair of Operators Acting on Two Sides*.

**Conventions.** $\langle S,T\rangle=\operatorname{tr}(S^{*}T)$; $T_{A,B}(X)=AXB$; $T_{A,B}^{\dagger}=T_{A^{*},B^{*}}$ for this form and $T_{A,B}^{\mathsf T}=T_{A^{\mathsf T},B^{\mathsf T}}$ for the bilinear one. The parameters of a product are defined only up to $(A,B)\mapsto(\lambda A,\lambda^{-1}B)$.

## The Adjoint of a Product

**Proposition.** $T_{A,B}^{\dagger}=T_{A^{*},B^{*}}$ and $T_{A,B}^{\mathsf T}=T_{A^{\mathsf T},B^{\mathsf T}}$.

*Proof.* $\langle T_{A,B}X,Y\rangle=\operatorname{tr}((AXB)^{*}Y)=\operatorname{tr}(B^{*}X^{*}A^{*}Y)=\operatorname{tr}(X^{*}A^{*}YB^{*})=\langle X,T_{A^{*},B^{*}}Y\rangle$. The bilinear case is the same computation with the transpose in place of the conjugate transpose. $\square$

**The self-adjointness criterion.** $T_{A,B}$ is self-adjoint if and only if there are Hermitian $H,K$ and a nonzero scalar $\mu$ with $A=\mu H$ and $B=\mu^{-1}K$.

*Proof.* $T_{A,B}=T_{A^{*},B^{*}}$ and $T_{C,D}=T_{A,B}$ force $(C,D)=(\lambda A,\lambda^{-1}B)$. So self-adjointness means $A^{*}=\lambda A$ and $B^{*}=\lambda^{-1}B$. Taking adjoints of the first gives $A=\lvert\lambda\rvert^{2}A$, hence $\lvert\lambda\rvert=1$ for $A\neq0$, and then $\lambda=\bar\mu/\mu$ for a unit $\mu$, so $\mu A$ is Hermitian. Conversely a Hermitian pair scaled by reciprocal scalars satisfies both equations. $\square$

**The warning.** "Both parameters Hermitian" is the representative with $\mu=1$ and is not the general condition: $T_{i\mathrm I,iB}$ with $B$ skew-Hermitian is self-adjoint and neither parameter is Hermitian.

**The warning about $T_{A,A^{*}}$.** This product is self-adjoint only when $A$ is a scalar multiple of a Hermitian matrix. Generically $\lVert T_{A,A^{*}}-T_{A,A^{*}}^{\dagger}\rVert>0$, so the "Hermitian pair" $(T_{A,B},T_{A,B}^{\dagger})$ is not a pair of two products of the shape $T_{A,A^{*}}$ unless the parameter is special.

## The Spectrum of a Hermitian Pair

**Proposition.** Let $A,B$ be Hermitian. Then $T_{A,B}$ is self-adjoint and its spectrum is $\{\lambda_i(A)\lambda_j(B)\}$.

*Proof.* In the frame, $T_{A,B}=B^{\mathsf T}\otimes A=\bar B\otimes A$, a Kronecker product of Hermitian factors up to the entrywise conjugation, which preserves the spectrum. The spectrum of a Kronecker product is the set of pairwise products. $\square$

**The consequence for positivity.** $T_{A,B}\ge0$ if and only if all products $\lambda_i(A)\lambda_j(B)$ are nonnegative, that is if and only if $A$ and $B$ are both positive semidefinite or both negative semidefinite.

**The rank.** $\operatorname{rank}T_{A,B}=(\operatorname{rank}A)(\operatorname{rank}B)$ and the kernel has dimension $n^2-(\operatorname{rank}A)(\operatorname{rank}B)$.

*Proof.* The rank of a Kronecker product is the product of the ranks. $\square$

**The extreme case.** A rank-one Hermitian $A$ gives $\operatorname{rank}T_{A,A}=1$: the operator is $X\mapsto(AXA)$ and its image is spanned by the rank-one matrix $A$ itself.

**The count.** The rank-one positive operator $|E_{ij}\rangle\langle E_{ij}|$ is the product $T_{E_{ii},E_{jj}}$, since $E_{ii}YE_{jj}=Y_{ij}E_{ij}$. So the matrix units give the $n^2$ matrix-unit rays of the cone, and every positive two-sided operator is a sum of such rays, not a single one.

## Eigenvalues and Singular Values

**The singular values.** The singular values of $T_{A,B}$ are $\sigma_i(A)\sigma_j(B)$, with no assumption on $A$ or $B$.

*Proof.* $T_{A,B}^{*}T_{A,B}=T_{A^{*}A,BB^{*}}$ is a Kronecker product of positive factors, whose eigenvalues are the pairwise products of $\sigma_i(A)^2$ and $\sigma_j(B)^2$. $\square$

**The comparison.** For a Hermitian pair the singular values are the absolute values of the eigenvalues, which are $\lvert\lambda_i(A)\lambda_j(B)\rvert=\sigma_i(A)\sigma_j(B)$. The two statements agree, as they must.

**The operator norm.** $\lVert T_{A,B}\rVert=\lVert A\rVert\lVert B\rVert$.

**The modulus.** $\lvert T_{A,B}\rvert=T_{\lvert A\rvert,\lvert B^{*}\rvert}$.

*Proof.* $T^{*}T=T_{A^{*}A,BB^{*}}$, so $\lvert T\rvert$ is the positive square root of $\lvert A\rvert^{2}\otimes(\lvert B^{*}\rvert^{2})^{\mathsf T}$, which is $\lvert A\rvert\otimes(\lvert B^{*}\rvert)^{\mathsf T}=T_{\lvert A\rvert,\lvert B^{*}\rvert}$. $\square$

**The polar decomposition.** $T_{A,B}=T_{U_A,V_B}\lvert T_{A,B}\rvert$ with $A=U_A\lvert A\rvert$ and $B=\lvert B\rvert V_B$, and it is unique exactly when both parameters are invertible.

## Normal Products

**Proposition.** For nonzero $A,B$ the product $T_{A,B}$ is normal exactly when $A$ and $B$ are normal.

*Proof.* $T^{*}T=T_{A^{*}A,BB^{*}}$ and $TT^{*}=T_{AA^{*},B^{*}B}$; equality forces $A^{*}A=\lambda AA^{*}$ and $BB^{*}=\lambda^{-1}B^{*}B$. Comparing traces gives $\lvert\lambda\rvert=1$, taking adjoints gives $\lambda$ real, so $\lambda=\pm1$; the value $-1$ forces $\operatorname{tr}(A^{*}A)=0$, hence $A=0$. So for nonzero parameters $\lambda=1$, which is normality of both. $\square$

**The unitary products.** $T_{U,V}$ is unitary exactly when $U,V$ are unitary, and then it is an isometry of the carrier.

**The spectral reading.** For normal parameters the spectrum of $T_{A,B}$ is the set of products of the spectra, so the two-sided normal operators are exactly the Kronecker products of normal matrices.

## The Completely Positive Reading

**The map.** For fixed $A$ the map $\Phi_A(X)=AXA^{*}$ is completely positive with the single Kraus operator $A$, and its Choi matrix has rank one.

**The distinction that matters.** The Choi matrix of $\Phi_A$ and the Hilbert–Schmidt representative $T_{A,A^{*}}$ are different objects: they differ by a partial transpose and a realignment. The Choi matrix has rank one, the representative has rank $(\operatorname{rank}A)^2$, and the representative is generally not positive. Complete positivity of the map does not imply positivity of its Hilbert–Schmidt matrix.

**The consequence.** The positive elements of the two-sided family are the Hermitian pairs $T_{A,B}$ with $A,B$ of the same sign, and they are not the Kraus-rank-one maps. The two notions coincide only in the scalar case.

## The Real Structure

**The conjugation.** $\Theta(X)=X^{*}$ acts on the carrier, and
$$
\Theta T_{A,B}\Theta=T_{B^{*},A^{*}},\qquad \Theta\lvert T_{A,B}\rvert\Theta=\lvert T_{B,A}\rvert .
$$

*Proof.* $\Theta T_{A,B}\Theta(X)=(AX^{*}B)^{*}=B^{*}XA^{*}$. $\square$

**The fixed products.** $T_{A,B}$ is fixed by conjugation with $\Theta$ exactly when $B$ is a scalar multiple of $A^{*}$, which is the self-adjointness locus up to the scalar ambiguity.

**The consequence.** The self-adjoint products are the fixed points of the composition of $\Theta$ with the flip, and the positive ones are those fixed points of the same composition with a sign condition on the pair of spectra.

## What the One-Sided Picture Does Not Give

**The transported positivity.** On one side $L_A\ge0$ exactly when $A\ge0$, and the modulus of $L_A$ is $L_{\lvert A\rvert}$ with no transpose anywhere. On two sides the modulus carries $\lvert B^{*}\rvert$ and the positivity is a property of the pair.

**The transported spectrum.** On one side the spectrum is $\sigma(A)$ with multiplicity $n$; on two sides it is the product set with multiplicity one.

**The transported rank.** On one side the rank is $n\operatorname{rank}A$; on two sides it is $(\operatorname{rank}A)(\operatorname{rank}B)$.

**The reason.** One side is a Kronecker product with the identity, whose spectrum and rank are those of the parameter repeated $n$ times. Two sides multiplies two nontrivial factors, and products of eigenvalues are not eigenvalues of a single parameter.

## The Finite Check

Computed with numpy for $n=2,3,4,5$: the residual $\lVert T_{A,B}^{\dagger}-T_{A^{*},B^{*}}\rVert$ is below $10^{-14}$; for random $A$ the defect $\lVert T_{A,A^{*}}-T_{A,A^{*}}^{\dagger}\rVert$ is of order one, and it vanishes only when $A$ is a scalar multiple of a Hermitian matrix, checked on $A=\mu H$ with unit $\mu$.

For Hermitian $A,B$ the spectrum of $T_{A,B}$ matched the pairwise products of the spectra to $10^{-13}$, the rank matched $(\operatorname{rank}A)(\operatorname{rank}B)$ in every trial, and the sign criterion held: for $A,B$ both positive the minimal eigenvalue was positive ($0.294,0.039,0.296,0.090$ at $n=2,3,4,5$), and for $B$ with one negative diagonal entry the minimal eigenvalue was negative ($-12.4,-131,-85.1,-267$). The modulus identity $\lvert T_{A,B}\rvert=T_{\lvert A\rvert,\lvert B^{*}\rvert}$ held to $3\times10^{-14}$.

## The Cone

**Proposition.** Every positive operator on the Hilbert space $M_n$ is in the two-sided family: it is a sum of rank-one operators $\lvert X\rangle\langle X\lvert$, and $\lvert X\rangle\langle X\lvert=T_{uu^{*},vv^{*}}$ for $X=uv^{*}$.

*Proof.* $T_{uu^{*},vv^{*}}(Y)=uu^{*}Yvv^{*}=u\,(v^{*}Yu)\,v^{*}=\langle uv^{*},Y\rangle\,uv^{*}=\lvert X\rangle\langle X\lvert(Y)$. A positive operator is a sum of rank-one positive ones, and each is a two-sided product with positive semidefinite parameters. $\square$

**The extreme rays.** The extreme rays are the $\lvert X\rangle\langle X\lvert$ with $X$ of rank one, parametrised by pairs of rays $(u,v)$ and realised as $T_{uu^{*},vv^{*}}$. The $n^2$ matrix-unit rays $\lvert E_{ij}\rangle\langle E_{ij}\lvert=T_{E_{ii},E_{jj}}$ are the coordinate members of the family.

**The comparison with the one-sided cone.** The one-sided positive operators are the $L_A$ with $A$ positive, an $n^2$-dimensional section of the cone of the whole operator space; the two-sided cone is the whole cone, of real dimension $n^4$, and the one-sided cone is the image of the positive parameters inside it.

**The reading.** Positivity is a property of the full cone, not of a parameter. The one-sided cone is the image of the positive parameters, and the two-sided cone is the cone generated by the matrix units.

## The Scalar Case

**The centre.** The scalar operators $\lambda\,\mathrm{id}$ are self-adjoint exactly for real $\lambda$, and positive exactly for $\lambda\ge0$. The line of scalars meets the positive cone in a ray.

**The reading.** The scalar ray is the intersection of all the symmetric cones of the construction, and it is the only part of the picture that looks the same at every $n$.

## Summary

The adjoint of a product conjugates both parameters, so the self-adjoint products are the Hermitian pairs up to reciprocal scalars. For Hermitian parameters the spectrum is the product set and positivity is the same-sign condition on the two spectra. The rank is the product of the ranks, the modulus carries $\lvert B^{*}\rvert$, and the normal products are the products of normal parameters. The completely positive reading refers to the Choi matrix, not to the Hilbert–Schmidt representative, and the two differ by a partial transpose.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{A,B}^{\dagger}$ | the Hilbert–Schmidt adjoint, equal to $T_{A^{*},B^{*}}$ |
| $\lambda_i(A)\lambda_j(B)$ | the spectrum of a Hermitian pair |
| $(\operatorname{rank}A)(\operatorname{rank}B)$ | the rank of a product |
| $\lvert T_{A,B}\rvert$ | $T_{\lvert A\rvert,\lvert B^{*}\rvert}$ |
| $\Theta$ | the conjugation $X\mapsto X^{*}$ |

## Further Reading
- [The Hermitian Pair of Operators Acting on One Side in $M_n(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-mnc.html), for the one-sided version.
- [The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$](the-two-sided-operator-the-difference-family-and-the-adjoints-of-mnc.html), for the adjoints.
- [The SVD of Endomorphisms of $M_n(\mathbb{C})$](the-svd-of-endomorphisms-of-mnc.html), for the singular values.
- [Positivity and the Positive Cone of $M_n(\mathbb{C})$](the-cone-of-positive-operators.html), for the cone of the algebra.
- [The Hermitian Pair of Operators Acting on Two Sides](the-hermitian-pair-of-operators-acting-on-two-sides.html), for the case $n=2$.
- [The Length and the Two Ranks on $M_n(\mathbb{C})$](the-length-and-the-two-ranks-on-mnc.html), for the two ranks.
