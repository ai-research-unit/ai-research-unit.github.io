# __The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$__

## Introduction

For a pair $A,B$ of matrices of $M_4(\mathbb{C})$ the **Sylvester operator** is the linear map

$$
\mathcal S_{A,B}:M_4(\mathbb{C})\longrightarrow M_4(\mathbb{C}),\qquad
\mathcal S_{A,B}(X)=AX-XB .
$$

It is the operator form of the **Sylvester equation** $AX-XB=C$, and it is the difference of a left and a right multiplication, $\mathcal S_{A,B}=L_A-R_B$. Its spectrum, its kernel and its invertibility are therefore read from the spectra of $A$ and $B$ alone, and the three linear matrix equations that the corpus meets — the Sylvester equation, the Lyapunov equation and the discrete equation $AXB-X=C$ — are the same computation in three forms.

This article states the matrix of $\mathcal S_{A,B}$ in the matrix units, the vec identities, the spectrum, the trace and the determinant, the invertibility criterion, the kernel and the image, and the Kronecker-sum forms of the three equations. It closes with the place of the operator in the category: the adjoint representation, the root space decomposition, and the difference family $\{L_A-R_B\}$ of dimension $31$ inside $\operatorname{End}(M_4)$.

The spectral theory is *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*; the Kronecker product and its two factors are *The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$*; the commutant is *$M_4(\mathbb{C})_{\mathbb{B},L}$ Model : The Centraliser and the Double Centraliser*; the two-sided operators are *$M_4(\mathbb{C})_{\mathbb{B},L}$ Representation : The Two-Sided Operators on the Biquaternion Algebra*; and the Lie algebra is *The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$*. The Clifford-algebra form of the same equation, with the dagger and its adjoint theory, is *The Hermitian Sylvester Equation with Hermitian Adjoint*, and the spectra of the sums $L_a+R_b$ on a Clifford algebra are *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*; the present article is the matrix case, and its criteria are the matrix forms of those. The numerical solution of the equations and their perturbation theory are not treated here.

## The Operator and Its Matrix

**Definition.** For $A,B\in M_4(\mathbb{C})$ the Sylvester operator is $\mathcal S_{A,B}(X)=AX-XB$. It is linear, and it is the difference of the two one-sided operators

$$
L_A(X)=AX,\qquad R_B(X)=XB,\qquad \mathcal S_{A,B}=L_A-R_B .
$$

**Proposition.** The operator $\mathcal S_{A,B}$ acts on the sixteen-dimensional complex vector space $M_4(\mathbb{C})$, and it is $\mathbb{C}$-linear.

**Proof.** The product is bilinear, so $X\mapsto AX$ and $X\mapsto XB$ are linear, and so is their difference.

**The matrix in the matrix units.** Write $\operatorname{vec}X$ for the column of length sixteen obtained by stacking the columns of $X$. Then

$$
\operatorname{vec}\bigl(\mathcal S_{A,B}(X)\bigr)
=\bigl(I_4\otimes A-B^{\mathsf T}\otimes I_4\bigr)\operatorname{vec}X .
$$

**Proof.** The entry $(i,j)$ of $AX$ is $\sum_k A_{ik}X_{kj}$ and the entry $(i,j)$ of $XB$ is $\sum_l X_{il}B_{lj}$. The coefficient of $X_{kj}$ in the first sum is $A_{ik}$ and the coefficient of $X_{il}$ in the second is $B_{lj}$, which is the display.

**The entry form.** With the row index $(i,j)$ and the column index $(k,l)$ of the operator matrix, the entries are

$$
\bigl(I_4\otimes A-B^{\mathsf T}\otimes I_4\bigr)_{(i,j),(k,l)}
=\delta_{jl}A_{ik}-\delta_{ik}B_{lj} .
$$

The first term fixes the column of $X$ and reads a row of $A$, the second fixes the row of $X$ and reads a column of $B$; the operator matrix is neither symmetric nor antisymmetric in general.

**The row form.** Stacking the rows instead of the columns gives the similar matrix

$$
\operatorname{vec}_{\mathrm r}\bigl(\mathcal S_{A,B}(X)\bigr)
=\bigl(A\otimes I_4-I_4\otimes B^{\mathsf T}\bigr)\operatorname{vec}_{\mathrm r}X .
$$

The two matrices are exchanged by the flip permutation $E_{ij}\mapsto E_{ji}$, so they have the same spectrum; the row form is the one used in the proof of the theorem below.

## The Spectrum

**Proposition (the rank-one eigenvectors).** Let $u$ be an eigenvector of $A$ with eigenvalue $\lambda$ and let $v$ be a left eigenvector of $B$ with eigenvalue $\mu$, that is, $v^{\mathsf T}B=\mu v^{\mathsf T}$. Then $X=uv^{\mathsf T}$ satisfies

$$
\mathcal S_{A,B}(X)=(\lambda-\mu)X .
$$

**Proof.** $Auv^{\mathsf T}-uv^{\mathsf T}B=\lambda uv^{\mathsf T}-\mu uv^{\mathsf T}$.

**Theorem (the spectrum).** For every pair $A,B\in M_4(\mathbb{C})$,

$$
\operatorname{spec}\mathcal S_{A,B}
=\bigl\{\lambda_i(A)-\lambda_j(B):\ 1\le i,j\le 4\bigr\},
$$

with algebraic multiplicities.

**Proof.** Choose $P$ and $Q$ invertible with $P^{-1}AP=T_A$ and $Q^{-1}B^{\mathsf T}Q=T_B$ upper triangular; the triangular forms exist by Schur's theorem over $\mathbb{C}$. The row form of the operator matrix is $A\otimes I_4-I_4\otimes B^{\mathsf T}$, and conjugation by $P\otimes Q$ carries it to $T_A\otimes I_4-I_4\otimes T_B$. In the row order $(i,j)$ the first term has the block $(i,k)=(T_A)_{ik}I_4$, hence is block upper triangular, and the second has the block $(i,k)=\delta_{ik}T_B$, hence is block diagonal with upper triangular blocks. The difference is block upper triangular, and each diagonal block is $(T_A)_{ii}I_4-T_B$, which is upper triangular. So the matrix is upper triangular, and its diagonal entries are

$$
(T_A)_{ii}-(T_B)_{jj},\qquad 1\le i,j\le 4 .
$$

The spectrum is therefore the set of differences, and the diagonal of an upper triangular matrix carries the algebraic multiplicities.

**Corollary (the trace).** $\operatorname{tr}\mathcal S_{A,B}=4\bigl(\operatorname{tr}A-\operatorname{tr}B\bigr)$.

**Proof.** Sum the sixteen eigenvalues: each $\lambda_i$ occurs four times and each $\lambda_j$ occurs four times.

**Corollary (the determinant).** $\det\mathcal S_{A,B}=\prod_{i,j}\bigl(\lambda_i(A)-\lambda_j(B)\bigr)$.

**Proof.** The determinant is the product of the eigenvalues of the operator.

**Corollary (the invertibility criterion).** The operator $\mathcal S_{A,B}$ is invertible exactly when

$$
\operatorname{spec}A\cap\operatorname{spec}B=\varnothing .
$$

**Proof.** The determinant vanishes exactly when one of the factors $\lambda_i-\lambda_j$ vanishes.

The corollary is the classical criterion of Sylvester: the equation $AX-XB=C$ has a unique solution for every $C$ exactly when the two spectra are disjoint.

**The kernel.** The kernel of $\mathcal S_{A,B}$ is the space of the intertwiners,

$$
\ker\mathcal S_{A,B}=\{X\in M_4(\mathbb{C}):AX=XB\}.
$$

For $A=B$ it is the commutant of $A$, whose dimension is read from the Jordan form. For a diagonalisable $A$ with eigenvalues of multiplicities $m_1,\dots,m_r$ the commutant has dimension $\sum_s m_s^{2}$; thus it has dimension $4$ for a cyclic matrix, $6$ for $\operatorname{diag}(1,1,2,3)$ and $16$ for a scalar matrix. For $A=B=J_4$ the commutant is the four-dimensional space of polynomials in $J_4$, although every eigenvalue has algebraic multiplicity four: the dimension is read from the Jordan block structure, not from the algebraic multiplicities alone.

**The image for $A=B$.** Let $\operatorname{ad}_A=\mathcal S_{A,A}$. With respect to the trace form $\langle X,Y\rangle=\operatorname{tr}(XY)$,

$$
\operatorname{im}\operatorname{ad}_A=(\ker\operatorname{ad}_A)^{\perp},\qquad
\dim\operatorname{im}\operatorname{ad}_A=16-\dim\mathfrak z(A),
$$

where $\mathfrak z(A)$ is the commutant of $A$.

**Proof.** For every $Y$,

$$
\operatorname{tr}\bigl(Y[A,X]\bigr)=\operatorname{tr}(YAX)-\operatorname{tr}(YXA)
=-\operatorname{tr}\bigl([A,Y]X\bigr),
$$

so $\operatorname{ad}_A$ is skew-adjoint for the trace form and its image is orthogonal to its kernel; the two dimensions add to sixteen because the form is nondegenerate.

## The Kronecker Sum and the Linear Equations

**Definition.** The **Kronecker sum** of $A$ and $B$ is

$$
A\oplus B=A\otimes I_4+I_4\otimes B .
$$

**Proposition (the vec identities).** For every $X$,

$$
\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}X,\qquad
\operatorname{vec}(AX+XB)=\bigl(I_4\otimes A+B^{\mathsf T}\otimes I_4\bigr)\operatorname{vec}X .
$$

**Proof.** The first identity is the composition of the two one-sided identities, $\operatorname{vec}(AXB)=\operatorname{vec}(A(XB))=(B^{\mathsf T}\otimes A)\operatorname{vec}X$; the second is the sum of the two terms.

**Corollary (the sum equation).** The equation $AX+XB=C$ has a unique solution for every $C$ exactly when

$$
\lambda_i(A)+\lambda_j(B)\ne0\qquad\text{for all }i,j .
$$

**Proof.** $AX+XB=\mathcal S_{A,-B}(X)$, and the spectrum of $-B$ is the set $-\lambda_j(B)$.

This is the matrix case of the Clifford criterion $\det(L_A+R_B)=\prod_{i,j}(\lambda_i+\mu_j)$ of *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*: the determinant vanishes exactly when some sum vanishes.

**Theorem (the Sylvester solution).** Suppose that $\operatorname{spec}A\cap\operatorname{spec}B=\varnothing$, and let $\Gamma$ be a simple closed contour that encloses $\operatorname{spec}A$ and excludes $\operatorname{spec}B$. Then the unique solution of $AX-XB=C$ is

$$
X=\frac{1}{2\pi i}\oint_\Gamma (zI_4-A)^{-1}C\,(zI_4-B)^{-1}\,dz .
$$

**Proof.** The contour avoids both spectra, so the integrand is continuous and the integral converges. Write $R_A(z)=(zI_4-A)^{-1}$ and $R_B(z)=(zI_4-B)^{-1}$. The identities

$$
A R_A(z)=zR_A(z)-I_4,\qquad R_B(z)B=zR_B(z)-I_4
$$

give

$$
A R_A(z)C R_B(z)-R_A(z)C R_B(z)B
=-C R_B(z)+R_A(z)C .
$$

The contour encloses $\operatorname{spec}A$ and excludes $\operatorname{spec}B$, so

$$
\frac{1}{2\pi i}\oint_\Gamma R_A(z)\,dz=I_4,\qquad
\frac{1}{2\pi i}\oint_\Gamma R_B(z)\,dz=0 .
$$

Integrating the identity therefore gives $AX-XB=C$. The solution is unique by the invertibility criterion.

**The Lyapunov equation.** The equation $AX+XA^*=Q$ is the sum equation with $B=A^*$. Its operator has spectrum $\lambda_i(A)+\overline{\lambda_j(A)}$, so it is invertible exactly when no eigenvalue of $A$ is the negative conjugate of another.

**Proposition (the integral form).** Suppose that $\operatorname{Re}\lambda_i(A)<0$ for every $i$. Then for every $Q$ the equation

$$
AX+XA^*=-Q
$$

has the unique solution

$$
X=\int_0^\infty e^{tA}Qe^{tA^*}\,dt .
$$

If $Q$ is Hermitian, so is $X$.

**Proof.** The integrand decays exponentially, because $\|e^{tA}\|\le Ce^{-\gamma t}$ for some $\gamma>0$. Its derivative is

$$
\frac{d}{dt}\bigl(e^{tA}Qe^{tA^*}\bigr)
=Ae^{tA}Qe^{tA^*}+e^{tA}Qe^{tA^*}A^* .
$$

Integrating from $0$ to $\infty$ gives $-Q$ on the left, because the limit at infinity vanishes and the value at zero is $Q$; the right side is $AX+XA^*$. The homogeneous equation has only the zero solution, because its operator has spectrum $\lambda_i+\overline{\lambda_j}\ne0$. The Hermitian symmetry follows by taking the conjugate transpose of the integral.

**The discrete equation.** The equation $AXB-X=C$ has the operator form

$$
\operatorname{vec}(AXB-X)=\bigl(B^{\mathsf T}\otimes A-I_{16}\bigr)\operatorname{vec}X .
$$

The eigenvalues of $B^{\mathsf T}\otimes A$ are the products $\lambda_i(A)\lambda_j(B)$: triangularise $A=P T_A P^{-1}$ and $B^{\mathsf T}=Q T_B Q^{-1}$, and note that $(Q\otimes P)^{-1}(B^{\mathsf T}\otimes A)(Q\otimes P)=T_B\otimes T_A$, a triangular matrix with diagonal products. Hence

$$
AXB-X=C\ \text{has a unique solution for every }C
\iff
\lambda_i(A)\lambda_j(B)\ne1\ \text{for all }i,j .
$$

## The Place in the Category

**The adjoint representation.** The case $A=B$ is the adjoint operator: $\mathcal S_{A,A}=\operatorname{ad}_A$. For $A=\operatorname{diag}(\lambda_1,\dots,\lambda_4)$ the matrix units are eigenvectors,

$$
\operatorname{ad}_A(E_{ij})=(\lambda_i-\lambda_j)E_{ij},
$$

so the spectrum of $\operatorname{ad}_A$ is the set of differences, the twelve roots and the zero of the root space decomposition. The kernel is the Cartan subalgebra, of dimension four, and the image is its orthogonal complement for the trace form, of dimension twelve. The derivations are the operators $\operatorname{ad}_A$ with $A$ traceless: they form the fifteen-dimensional algebra of *The Derivations and the Automorphisms of $M_4(\mathbb{C})$*, because $\operatorname{ad}$ kills the scalars and is injective on the traceless part.

**The difference family.** The Sylvester operators are the elements of the linear subspace

$$
\mathcal D=\{L_A-R_B:\ A,B\in M_4(\mathbb{C})\}\subset\operatorname{End}(M_4(\mathbb{C})).
$$

The parametrisation $(A,B)\mapsto L_A-R_B$ has kernel the scalars: $L_A=R_B$ forces $A=B$ by evaluation at $I_4$, and then $[A,X]=0$ for every $X$ forces $A$ to be scalar. Hence

$$
\dim\mathcal D=16+16-1=31 .
$$

The subspace is the difference of the two copies $L(M_4)$ and $R(M_4)$ of $M_4$ inside $\operatorname{End}(M_4)$, whose intersection is the scalars. It is much smaller than the span of the products $L_AR_B$, which is the whole of $\operatorname{End}(M_4)$ of dimension $256$; the products themselves form the cone over the Segre variety, not a linear subspace. The case $B=A$ cuts out the fifteen-dimensional adjoint representation inside $\mathcal D$.

**The flow.** The one-parameter family $X(t)=e^{tA}Ce^{-tB}$ satisfies

$$
\frac{d}{dt}X(t)=A X(t)-X(t)B,
$$

so the Sylvester operator is the generator of the two-sided flow, and the contour formula of the theorem is the stationary form of the flow when the two spectra are separated.

**The determinant as a resultant.** The determinant $\prod_{i,j}(\lambda_i-\lambda_j)$ is the resultant of the two characteristic polynomials, $\operatorname{Res}(\chi_A,\chi_B)$, up to a sign; the vanishing criterion is therefore the statement that two polynomials have a common root. This is the form in which the criterion is used in the spectral theory of *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*.

## Summary

The Sylvester operator $\mathcal S_{A,B}(X)=AX-XB$ is a linear operator on the sixteen-dimensional algebra $M_4(\mathbb{C})$. In the column-stacking basis its matrix is $I_4\otimes A-B^{\mathsf T}\otimes I_4$, and its spectrum is the set of differences $\lambda_i(A)-\lambda_j(B)$, with algebraic multiplicities. Its trace is $4(\operatorname{tr}A-\operatorname{tr}B)$, its determinant is the product of the differences, and it is invertible exactly when the spectra of $A$ and $B$ are disjoint. Its kernel is the space of intertwiners $AX=XB$; for $A=B$ it is the commutant, and the image of $\operatorname{ad}_A$ is the orthogonal complement of the commutant for the trace form. The Kronecker sum gives the analogous criteria for $AX+XB=C$ and $AXB-X=C$, and the contour integral gives the solution of the Sylvester equation when the spectra are separated. The operators $\{L_A-R_B\}$ form a subspace of dimension $31$, and the case $A=B$ is the adjoint representation, whose spectrum on the matrix units is the root system of $\mathfrak{sl}_4$.

| Quantity | Value for $M_4(\mathbb{C})$ |
|---|---|
| $\dim M_4$ | $16$ |
| Matrix of $\mathcal S_{A,B}$ (column stacking) | $I_4\otimes A-B^{\mathsf T}\otimes I_4$ |
| $\operatorname{spec}\mathcal S_{A,B}$ | $\lambda_i(A)-\lambda_j(B)$ |
| $\operatorname{tr}\mathcal S_{A,B}$ | $4(\operatorname{tr}A-\operatorname{tr}B)$ |
| $\det\mathcal S_{A,B}$ | $\prod_{i,j}(\lambda_i(A)-\lambda_j(B))$ |
| $\mathcal S_{A,B}$ invertible iff | $\operatorname{spec}A\cap\operatorname{spec}B=\varnothing$ |
| $\ker\mathcal S_{A,A}$ | the commutant of $A$ |
| $\dim\{L_A-R_B\}$ | $31$ |
| $AX+XB=C$ solvable iff | $\lambda_i(A)+\lambda_j(B)\ne0$ |
| $AXB-X=C$ solvable iff | $\lambda_i(A)\lambda_j(B)\ne1$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal S_{A,B}$ | the Sylvester operator $X\mapsto AX-XB$ |
| $L_A,R_B$ | left and right multiplication by $A$ and $B$ |
| $\operatorname{ad}_A$ | the commutator operator $X\mapsto AX-XA$ |
| $\operatorname{vec}X$ | the column of the entries of $X$, stacked by columns |
| $\operatorname{vec}_{\mathrm r}X$ | the same entries stacked by rows |
| $A\oplus B$ | the Kronecker sum $A\otimes I_4+I_4\otimes B$ |
| $\operatorname{spec}A$ | the spectrum of $A$, with algebraic multiplicities |
| $\mathfrak z(A)$ | the commutant of $A$ in $M_4(\mathbb{C})$ |
| $\mathcal D$ | the subspace $\{L_A-R_B\}$ of $\operatorname{End}(M_4)$ |

## Further Reading

- [Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m4c.html), for the spectrum, the resolvent and the spectral projectors.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c.html), for the Kronecker product and the two factors.
- [$M_4(\mathbb{C})_{\mathbb{B},L}$ Model : The Centraliser and the Double Centraliser](m4c-model-the-centraliser-and-the-double-centraliser.html), for the commutant and its dimension.
- [$M_4(\mathbb{C})_{\mathbb{B},L}$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the operators $L_A$, $R_B$ and $T_{A,B}$.
- [The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$](the-lie-algebra-gl4-and-sl4-of-m4c.html), for the root space decomposition and the derivations.
- [The Derivations and the Automorphisms of $M_4(\mathbb{C})$](the-derivations-and-the-automorphisms-of-m4c.html), for $\operatorname{Der}(M_4)=\operatorname{ad}\mathfrak{sl}_4$.
- [The Hermitian Sylvester Equation with Hermitian Adjoint](the-hermitian-sylvester-equation-with-hermitian-adjoint.html), for the same equation on a Clifford algebra, with the dagger and the adjunction $L_a^*=L_{a^\dagger}$.
- [The Spectra of Self-Adjoint Operators with Hermitian Adjoint](the-spectra-of-self-adjoint-operators-with-hermitian-adjoint.html), for $\det(L_a+R_b)=\prod_{i,j}(\lambda_i+\mu_j)$ and the spectral criterion in the Clifford setting.
- [Analysis on $M_4(\mathbb{C})$](analysis-on-m4c.html), for the functional calculus and the resolvent.
- [The Exponential and the Lie Group of $M_4(\mathbb{C})$](the-exponential-and-the-lie-group-of-m4c.html), for the flow $e^{tA}Ce^{-tB}$.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the Sylvester and Lyapunov equations and the Kronecker product.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the spectrum of the Kronecker sum and the resultant criterion.
- Feliks R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959), for the classical treatment of the matrix equations.
