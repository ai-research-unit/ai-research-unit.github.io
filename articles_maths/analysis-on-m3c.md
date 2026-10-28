# __Analysis on $M_3(\mathbb{C})$__

## Introduction

**The algebra $M_3(\mathbb{C})$ is a complex vector space of dimension $9$, hence a real vector space of dimension $18$, and it carries the flat Hermitian metric $\operatorname{tr}(dA^{*}dA)$ together with the Lebesgue measure $dA$.** Analysis on the algebra is the analysis of nine complex variables $a_{ij}$ with the flat Kähler structure, the polynomial and entire functions, the $\bar\partial$ operator, the Laplacian

$$
\Delta=4\sum_{i,j=1}^{3}\frac{\partial^{2}}{\partial a_{ij}\,\partial\bar a_{ij}},
$$

the Gaussian measure $\pi^{-9}e^{-\operatorname{tr}(A^{*}A)}dA$, and the heat kernel $(4\pi t)^{-9}e^{-\operatorname{tr}(A^{*}A)/(4t)}$. The determinant is a cubic polynomial whose critical set is the variety of matrices of rank at most $1$, of complex dimension $5$; the hypersurface $\det A=0$ has real codimension $2$ and is singular exactly on that variety. The group $GL_3(\mathbb{C})$ is the open dense set where the determinant does not vanish, and $U(3)$ is a compact real form of real dimension $9$ with its Haar measure.

The article sets up the holomorphic and the real-analytic structures, computes the Laplacian and the Gaussian integrals, analyses the determinant and the discriminant, discusses the exponential and the logarithm as analytic maps, and states the Weyl integration formula for the $*$-unitary group. Every identity is either proved or referred to a standard source. The spectral theory is *Spectral Theory and the Spectral Projectors of $M_3(\mathbb{C})$*; the cubic is *The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$*; the geometry of the singular set is *The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$*; the topology is *The Topology of $M_3(\mathbb{C})$*.

## The Holomorphic Structure

**Coordinates.** Write $A=(a_{ij})_{i,j=1}^{3}$ with $a_{ij}=x_{ij}+iy_{ij}$. The $18$ real coordinates $x_{ij},y_{ij}$ identify $M_3$ with $\mathbb{R}^{18}$, and the $9$ complex coordinates $a_{ij}$ identify it with $\mathbb{C}^{9}$.

**Wirtinger derivatives.** For a smooth function $f$,

$$
\frac{\partial f}{\partial a_{ij}}=\frac12\Big(\frac{\partial f}{\partial x_{ij}}-i\frac{\partial f}{\partial y_{ij}}\Big),
\qquad
\frac{\partial f}{\partial\bar a_{ij}}=\frac12\Big(\frac{\partial f}{\partial x_{ij}}+i\frac{\partial f}{\partial y_{ij}}\Big).
$$

**Proposition.** A $C^{1}$ function is holomorphic exactly when

$$
\frac{\partial f}{\partial\bar a_{ij}}=0
$$

for all $i,j$.

**Proof.** The two real equations $\partial f/\partial x+i\partial f/\partial y=0$ are the Cauchy–Riemann equations for the pair $(x_{ij},y_{ij})$; the equation says that the $\mathbb{R}$-linear differential of $f$ is $\mathbb{C}$-linear.

**The polynomial ring.** The holomorphic polynomials on $M_3$ form the ring

$$
\mathbb{C}[a_{11},a_{12},\dots,a_{33}],
$$

the polynomials of degree at most $d$ forming a space of dimension $\binom{9+d}{d}$. The determinant is the homogeneous cubic

$$
\det A=\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,a_{1\sigma(1)}a_{2\sigma(2)}a_{3\sigma(3)},
$$

which is irreducible. The trace is the linear form $\tau=a_{11}+a_{22}+a_{33}$.

**Theorem (entire functions).** Every holomorphic function on $M_3$ is entire, and is the uniform limit on compact sets of its Taylor polynomials. The Taylor series converges on all of $\mathbb{C}^{9}$, by Hartogs' theorem and the several-variable Cauchy integral formula.

**Proof.** A holomorphic function on $\mathbb{C}^{9}$ has a convergent power series at every point, and the several-variable Cauchy formula gives the coefficients as integrals over a polydisc. The radius of convergence is infinite because the function is defined on the whole space.

**The Cauchy integral.** For a polydisc $D$ with distinguished boundary $\partial_{0}D$,

$$
f(A)=\frac{1}{(2\pi i)^{9}}\oint_{\partial_{0}D}\frac{f(Z)}{\prod_{i,j}(z_{ij}-a_{ij})}\,dZ .
$$

The formula is the several-variable Cauchy formula; it is the analytic foundation of the residue calculus on the algebra.

## The Flat Metric and the Measure

**The metric.** The Hermitian metric

$$
ds^{2}=\operatorname{tr}(dA^{*}dA)=\sum_{i,j}|da_{ij}|^{2}
$$

is flat: in the coordinates $a_{ij}$ it is the standard Hermitian metric of $\mathbb{C}^{9}$. Its real part is the Euclidean metric of $\mathbb{R}^{18}$, and its Kähler form is

$$
\omega=\frac{i}{2}\sum_{i,j}da_{ij}\wedge d\bar a_{ij}.
$$

**The measure.** The Lebesgue measure is

$$
dA=\prod_{i,j}dx_{ij}\,dy_{ij}=2^{-9}\prod_{i,j}da_{ij}\wedge d\bar a_{ij},
$$

in the sense that $|da\wedge d\bar a|=2\,dx\,dy$ for one complex coordinate. The volume of the ball of radius $R$ is $\pi^{9}R^{18}/9!$, the volume of the real ball of dimension $18$.

**The Gaussian measure.** The probability measure

$$
d\mu(A)=\pi^{-9}e^{-\operatorname{tr}(A^{*}A)}\,dA
$$

is the standard complex Gaussian on $\mathbb{C}^{9}$. Its moments factorise over the entries:

$$
\int |a_{ij}|^{2}\,d\mu=1,\qquad
\int |a_{ij}|^{4}\,d\mu=2,\qquad
\int a_{ij}\bar a_{kl}\,d\mu=\delta_{ik}\delta_{jl}.
$$

**Proof.** For one complex coordinate, $\int_{\mathbb{C}}e^{-|z|^{2}}dA(z)=\pi$, and the moments are $\int|z|^{2}e^{-|z|^{2}}dA=\pi$ and $\int|z|^{4}e^{-|z|^{2}}dA=2\pi$. The measure is a product over the nine entries, so the moments factorise and the normalisation is $\pi^{-9}$.

**The Laplacian.** The Laplacian is

$$
\Delta=\sum_{i,j}\Big(\frac{\partial^{2}}{\partial x_{ij}^{2}}+\frac{\partial^{2}}{\partial y_{ij}^{2}}\Big)
=4\sum_{i,j}\frac{\partial^{2}}{\partial a_{ij}\partial\bar a_{ij}} .
$$

It is the Euclidean Laplacian of $\mathbb{R}^{18}$, and it is invariant under translations and under $*$-unitary conjugation.

**Proposition.** For the squared norm $N(A)=\operatorname{tr}(A^{*}A)$,

$$
\Delta N=36,\qquad
\Delta N^{2}=80N .
$$

**Proof.** In one complex coordinate, $\Delta|z|^{2}=4$ and $\Delta|z|^{4}=16|z|^{2}$. For nine coordinates, $N=\sum_k f_k$ with $f_k$ the contributions of the individual entries, and $\Delta(f_i f_j)=2\nabla f_i\cdot\nabla f_j+f_i\Delta f_j+f_j\Delta f_i$. The gradients of distinct entries have disjoint supports, so their inner product vanishes; $\Delta f_k=4$. Hence

$$
\Delta N^{2}=\sum_k16f_k+2\sum_{i<j}4(f_i+f_j)=16N+64N=80N .
$$

**The heat kernel.** The heat equation $\partial_{t}u=\Delta u$ on $M_3$ has the kernel

$$
K_{t}(A,B)=(4\pi t)^{-9}\exp\Big(-\frac{\operatorname{tr}((A-B)^{*}(A-B))}{4t}\Big),
$$

so that $u(t,A)=\int K_{t}(A,B)u_{0}(B)\,dB$ solves the initial value problem.

**Proof.** The kernel is the product of the one-dimensional heat kernels for the $18$ real coordinates, and the real heat kernel of $\mathbb{R}^{18}$ is $(4\pi t)^{-9}e^{-|x-y|^{2}/(4t)}$.

## The Determinant and the Singular Set

**The differential.** The determinant is a polynomial of degree $3$, and

$$
d(\det)_{A}(B)=\operatorname{tr}(\operatorname{adj}(A)B),
$$

where $\operatorname{adj}(A)$ is the adjugate matrix, the transpose of the cofactor matrix.

**Proof.** The derivative of $\det$ in the direction $B$ is the sum over $i,j$ of the cofactor $C_{ji}$ times $B_{ij}$, which is $\operatorname{tr}(\operatorname{adj}(A)B)$ by the definition of the adjugate. Equivalently, $\det(A+\epsilon B)=\det A+\epsilon\operatorname{tr}(\operatorname{adj}(A)B)+O(\epsilon^{2})$.

**Theorem (critical set).** The critical points of $\det$ are exactly the matrices of rank at most $1$:

$$
d(\det)_{A}=0\iff \operatorname{adj}(A)=0\iff \operatorname{rank}A\le1 .
$$

**Proof.** The rank of the adjugate is $3$ if $\operatorname{rank}A=3$, is $1$ if $\operatorname{rank}A=2$, and is $0$ if $\operatorname{rank}A\le1$. This is the standard identity $\operatorname{rank}\operatorname{adj}(A)=n$ for $\operatorname{rank}A=n$, $\operatorname{rank}\operatorname{adj}(A)=1$ for $\operatorname{rank}A=n-1$, and $\operatorname{adj}(A)=0$ for $\operatorname{rank}A\le n-2$. For $n=3$ this gives $3$, $1$, $0$. Hence the differential vanishes exactly when the rank is at most $1$.

**The singular locus.** The hypersurface $\{\det A=0\}$ is smooth at every matrix of rank $2$, and singular at every matrix of rank at most $1$. The singular locus is therefore the determinantal variety

$$
\Sigma=\{A:\operatorname{rank}A\le1\},
$$

of complex dimension $5$ and real dimension $10$.

**Proof.** A hypersurface is singular at a point exactly when the gradient of its defining equation vanishes there. The gradient of $\det$ vanishes exactly on $\Sigma$ by the theorem above. The rank-one matrices are the image of

$$
\mathbb{C}^{3}\times(\mathbb{C}^{3})^{*}\longrightarrow M_3,\qquad (u,\varphi)\longmapsto u\varphi,
$$

modulo the scaling $(u,\varphi)\mapsto(\lambda u,\lambda^{-1}\varphi)$. The pair has six parameters and the scaling is one-dimensional, so the rank-one matrices have dimension $5$; they are the affine cone, with apex $0$, over the Segre variety $\mathbb{P}^{2}\times\mathbb{P}^{2}$ of dimension $4$. The whole variety $\Sigma$ has dimension $5$.

**The nilpotent part.** Inside $\Sigma$, the rank-one matrices with $\varphi(u)=0$ are the nilpotent ones. They form the orbit of $E_{12}$, of dimension $4$, and they are the affine cone over the incidence variety of dimension $3$. The singular locus of the determinant hypersurface is the full $\Sigma$, not only its nilpotent part.

**Worked example.** For $A=\operatorname{diag}(1,1,0)$, of rank $2$,

$$
\operatorname{adj}(A)=\operatorname{diag}(0,0,1)\neq0,
$$

so $A$ is a smooth point of $\{\det=0\}$. For $A=E_{12}$, of rank $1$, $\operatorname{adj}(A)=0$, so $A$ is a singular point. The tangent cone of $\{\det=0\}$ at $E_{12}$ is the whole tangent space, because the gradient vanishes.

**The discriminant.** The discriminant of the characteristic cubic is

$$
\Delta=\tau^{2}\sigma^{2}-4\sigma^{3}-4\tau^{3}\delta-27\delta^{2}+18\tau\sigma\delta,
$$

a polynomial in the entries. Each monomial has degree $6$: $\tau^{2}\sigma^{2}$ has degree $2+4=6$, $\sigma^{3}$ has degree $6$, $\tau^{3}\delta$ has degree $3+3=6$, $\delta^{2}$ has degree $6$, and $\tau\sigma\delta$ has degree $1+2+3=6$. Hence $\Delta$ is homogeneous of degree $6$ in the entries. Its zero set is the discriminant hypersurface, the locus of matrices with a repeated eigenvalue.

## Gaussian Integrals

**Theorem.** For the standard complex Gaussian on $M_3$,

$$
\int_{M_3}\det(A^{*}A)\,d\mu(A)=3!=6 .
$$

The same argument gives $\mathbb{E}[\det(A^{*}A)]=n!$ for the $n\times n$ complex Gaussian, and for $n=3$ the value is $6$.

**Proof.** The determinant is the sum over permutations,

$$
\det(A^{*}A)=\sum_{\sigma,\tau\in S_3}\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)\,
\prod_{i=1}^{3}\overline{a_{i\sigma(i)}}a_{i\tau(i)} .
$$

Take expectations. Rows are independent, and within row $i$ the entry $\overline{a_{i\sigma(i)}}$ and the entry $a_{i\tau(i)}$ are independent zero-mean Gaussians unless $\sigma(i)=\tau(i)$; in that case the expectation is $\mathbb{E}[|a_{i\sigma(i)}|^{2}]=1$. Hence the only nonzero terms have $\sigma=\tau$, and each contributes $1$:

$$
\mathbb{E}\big[\det(A^{*}A)\big]=\sum_{\sigma\in S_3}1=3!=6 .
$$

The argument is the $n=3$ case of the general formula $\mathbb{E}[\det(A^{*}A)]=n!$ for the complex Gaussian, due to Edelman (*Eigenvalues and condition numbers of random matrices*, 1988).

**The moment $|{\det A}|^{2}$.** Since $\det(A^{*}A)=|\det A|^{2}$, the theorem says

$$
\mathbb{E}\big[|\det A|^{2}\big]=6 .
$$

**The trace moment.** Similarly,

$$
\mathbb{E}\big[\operatorname{tr}(A^{*}A)\big]=9,
\qquad
\mathbb{E}\big[\operatorname{tr}(A^{*}A)^{2}\big]=90 . 
$$

**Proof.** $\operatorname{tr}(A^{*}A)=\sum|a_{ij}|^{2}$ is a sum of nine independent $\chi^{2}$ variables with mean $1$, so the mean is $9$. The second moment is the sum of the variances plus the square of the mean: each $|a_{ij}|^{2}$ has variance $1$, so the sum has variance $9$ and second moment $9^{2}+9=90$.

**The Gaussian is not invariant.** The measure $d\mu$ is invariant under translations only up to the exponential weight, and under $*$-unitary conjugation it is invariant because $\operatorname{tr}((UAU^{*})^{*}(UAU^{*}))=\operatorname{tr}(A^{*}A)$. It is not invariant under the general linear group. For $S\in GL_3$, the map $A\mapsto SA$ is complex-linear on $\mathbb{C}^{9}$ with complex determinant $(\det S)^{3}$, hence real Jacobian $|\det S|^{6}$. The pushforward density is

$$
\pi^{-9}|\det S|^{-6}e^{-\operatorname{tr}(A^{*}S^{*}SA)},
$$

which is not $d\mu$ unless $S$ is $*$-unitary.

**Proof.** A complex-linear map $T$ on $\mathbb{C}^{9}$ has real determinant $|\det_{\mathbb{C}}T|^{2}$; here $\det_{\mathbb{C}}(A\mapsto SA)=(\det S)^{3}$, so the real determinant is $|\det S|^{6}$. The density transforms by the inverse of this factor, $|\det S|^{-6}$, and the exponent becomes $\operatorname{tr}((SA)^{*}(SA))=\operatorname{tr}(A^{*}S^{*}SA)$.

**The $*$-unitary group.** On $U(3)$ the Haar probability measure is characterised by invariance under left and right multiplication. The Weyl integration formula for a class function $f$ is

$$
\int_{U(3)}f(U)\,dU
=\frac{1}{3!}\int_{[0,2\pi]^{3}}f\big(\operatorname{diag}(e^{i\theta_1},e^{i\theta_2},e^{i\theta_3})\big)
\prod_{j<k}|e^{i\theta_j}-e^{i\theta_k}|^{2}\,\frac{d\theta}{(2\pi)^{3}} .
$$

**Proof.** The formula is the Weyl integration formula for the compact connected Lie group $U(3)$; the factor $\prod_{j<k}|e^{i\theta_j}-e^{i\theta_k}|^{2}$ is the square of the Vandermonde, the Jacobian of the map from the torus to the conjugacy classes, and $1/3!$ is the order of the Weyl group $S_3$. The normalisation is the Haar probability.

**The character moments.** For the standard representation,

$$
\int_{U(3)}|\operatorname{tr}U|^{2}\,dU=1,
\qquad
\int_{U(3)}|\operatorname{tr}U|^{4}\,dU=2 .
$$

**Proof.** The functions $U\mapsto\operatorname{tr}U$ and $U\mapsto\overline{\operatorname{tr}U}$ are the character of the standard representation and its conjugate. By the orthogonality of irreducible characters, the integral of $|\operatorname{tr}U|^{2}$ is $1$. For the fourth moment, $(\operatorname{tr}U)^{2}=\chi_{\operatorname{Sym}^{2}}+\chi_{\wedge^{2}}$, the sum of the characters of the symmetric square (highest weight $(2,0,0)$, dimension $6$) and the exterior square (highest weight $(1,1,0)$, dimension $3$). These two representations are irreducible and inequivalent, so orthogonality gives $1^{2}+1^{2}=2$.

## The Exponential and the Logarithm as Analytic Maps

**The exponential.** The series $\exp X=\sum X^{n}/n!$ converges uniformly on compact subsets of $M_3$, so $\exp$ is an entire map $\mathbb{C}^{9}\to GL_3(\mathbb{C})$. Its right-trivialized derivative at $X$ is

$$
d\exp_X(Y)\,e^{-X}=\sum_{n\ge0}\frac{\operatorname{ad}_X^{n}(Y)}{(n+1)!},
$$

and $d\exp_X$ is invertible exactly when no two eigenvalues of $X$ differ by a nonzero multiple of $2\pi i$. The map is surjective, and its fibres are the discrete sets described in *The Exponential and the Lie Group of $M_3(\mathbb{C})$*.

**The logarithm.** On the open set where the spectrum avoids a ray from $0$, the logarithm is analytic. On the Jordan block $\lambda I+N$ with $|\lambda|$ larger than $\|N\|$, the series

$$
\log(\lambda I+N)=(\log\lambda)I+\sum_{k\ge1}\frac{(-1)^{k-1}}{k}\Big(\frac{N}{\lambda}\Big)^{k}
$$

converges; for $3\times3$ blocks the sum stops at $k=2$. A global analytic logarithm does not exist on $GL_3(\mathbb{C})$. If $L$ were one, then $\operatorname{tr}L(A)$ would be a holomorphic logarithm of $\det A$ on $GL_3$; since $\det:GL_3(\mathbb{C})\to\mathbb{C}^{\times}$ is surjective, $\mathbb{C}^{\times}$ would carry a global holomorphic logarithm, which it does not.

**The BCH series.** Near the identity, the product is computed by the Baker–Campbell–Hausdorff series

$$
\log(e^{X}e^{Y})=X+Y+\frac12[X,Y]+\frac1{12}[X,[X,Y]]-\frac1{12}[Y,[X,Y]]+\cdots,
$$

which converges in a neighbourhood of $0$ and defines the local group law in exponential coordinates.

**The Jacobian of the exponential.** The eigenvalues of the right-trivialized differential $d\exp_X\,e^{-X}$ are

$$
1\ \text{on the diagonal},\qquad
\frac{e^{\lambda_i-\lambda_j}-1}{\lambda_i-\lambda_j}\ \text{on the root space }E_{ij},
$$

so the right-trivialized differential is singular exactly when $\lambda_i-\lambda_j\in2\pi i\mathbb{Z}\setminus\{0\}$, and the same holds for $d\exp_X$. The exponential is a local analytic isomorphism at every other point.

**Proof.** The operator $\operatorname{ad}_X$ acts on $E_{ij}$ by multiplication by $\lambda_i-\lambda_j$ and on the diagonal by $0$. The factor $(e^{z}-1)/z$ is nonzero exactly away from the nonzero multiples of $2\pi i$.

## The Calculus of the Algebra

**The product.** The multiplication map $m(A,B)=AB$ is a quadratic polynomial in the entries, hence smooth, and

$$
dm_{(A,B)}(X,Y)=XB+AY .
$$

**Proof.** $(A+tX)(B+tY)=AB+t(XB+AY)+t^{2}XY$, so the linear term is $XB+AY$.

**The inverse.** On $GL_3$ the inverse is smooth and

$$
d(\operatorname{inv})_{A}(X)=-A^{-1}XA^{-1}.
$$

**Proof.** Differentiate $A(t)A(t)^{-1}=I$ at $t=0$ with $A(0)=A$ and $A'(0)=X$: $X A^{-1}+A\,d(\operatorname{inv})_A(X)=0$.

**The determinant.** $d(\det)_{A}(B)=\operatorname{tr}(\operatorname{adj}(A)B)$, proved in §*The Determinant and the Singular Set*. The exponential is entire, and its derivative is computed in §*The Exponential and the Logarithm as Analytic Maps*.

**The holomorphic functional calculus.** Let $A\in M_3(\mathbb{C})$ and let $f$ be holomorphic on a neighbourhood of the spectrum $\sigma(A)$. Then

$$
f(A)=\frac{1}{2\pi i}\oint_{\gamma}f(z)(zI-A)^{-1}\,dz
$$

is independent of the contour $\gamma$ that winds once around $\sigma(A)$ and avoids it, and $f\mapsto f(A)$ is an algebra homomorphism from the holomorphic functions on that neighbourhood to $M_3(\mathbb{C})$. It agrees with the polynomial calculus, and with the Lagrange interpolation when the spectrum is simple. The spectral projectors are the case where $f$ is $1$ on one spectral cluster and $0$ on the others; the Dunford calculus is developed in *Spectral Theory and the Spectral Projectors of $M_3(\mathbb{C})$*.

**Proof.** The resolvent $R(z)=(zI-A)^{-1}$ is holomorphic on the complement of $\sigma(A)$, and the resolvent identity $R(z)-R(w)=(w-z)R(z)R(w)$ shows that the integral is unchanged by a homotopy of $\gamma$ that avoids the spectrum. The product $f(A)g(A)$ is the double contour integral of $f(z)g(w)R(z)R(w)$; the resolvent identity splits it into the integral of $(fg)(z)R(z)$, which is $(fg)(A)$. The polynomial case is the Cauchy integral formula for the derivatives at $0$.

**Zero divisors.** $M_3(\mathbb{C})$ is not a division algebra: $E_{11}E_{22}=0$ with both factors nonzero. A matrix is a zero divisor exactly when it is singular. If $AB=0$ with $B\neq0$, then $\operatorname{im}B\subseteq\ker A$, so $\ker A\neq0$; conversely, if $\ker A\neq0$, choose a nonzero $B$ with image in $\ker A$, and $AB=0$. The zero divisors therefore form the singular set $\{\det=0\}$, which is not an ideal: the algebra is simple, and the singular set is not closed under addition.

**Proof of the last sentence.** $E_{11}$ and $I-E_{11}$ are singular, and their sum is $I$; so the singular set is not closed under addition and cannot be an ideal.

**The boundary against Fueter theory.** Fueter regularity is a notion for functions of a quaternionic or Clifford variable, defined by a Dirac-type operator and requiring a Clifford module. The algebra $M_3(\mathbb{C})$ as such carries neither; its analysis is the ordinary several-variable analysis of $\mathbb{C}^{9}$ developed here. The two theories meet only after a choice of a representation on a Clifford module, which is extra structure and not part of the algebra.

## Integration and the Group

**The flat measure and the group.** The Lebesgue measure $dA$ is invariant under translations, and it is invariant under $*$-unitary conjugation because conjugation by $U$ is a real orthogonal transformation of $M_3$. It is not invariant under the general linear group; the group $GL_3$ carries its own Haar measure, which in the polar coordinates $A=UP$ is a product of the Haar measure of $U(3)$ and a measure on $\operatorname{Herm}_{>0}(3)$ with a density depending only on the eigenvalues of $P$.

**The polar Jacobian.** The map $(U,P)\mapsto UP$ from $U(3)\times\operatorname{Herm}_{>0}(3)$ to $GL_3$ is a diffeomorphism. Its Jacobian is invariant under the conjugation $P\mapsto UPU^{*}$ and under $U(3)$ on the left, so it is a positive function of the eigenvalues of $P$ alone. The explicit formula is not needed in this article; the existence of the positive density is enough for the change of variables.

**Proof.** The map is a bijection by the polar decomposition, and its inverse $A\mapsto\big((AA^{*})^{-1/2}A,(AA^{*})^{1/2}\big)$ is smooth on $GL_3$ because $(AA^{*})^{1/2}$ is positive definite; hence it is a diffeomorphism and its Jacobian is nowhere zero. The Jacobian is invariant under left multiplication by $U(3)$ and under the conjugation $P\mapsto UPU^{*}$, because both are isometries of the trace metric; a function with these invariances depends only on the eigenvalues of $P$.

**The Haar measure of $U(3)$.** The group $U(3)$ is compact of real dimension $9$, and its Haar probability measure is the Weyl measure of the previous section, normalised by $\int_{U(3)}dU=1$. The Weyl formula gives the integral of every class function as an integral over the maximal torus with the Vandermonde density.

**The Fourier transform.** On the abelian group $\mathbb{R}^{18}$ the Fourier transform is the usual one; on the nonabelian group $U(3)$ the Fourier transform is the Peter–Weyl decomposition into matrix coefficients of irreducible representations. The representation theory of $U(3)$ is the representation theory of $GL_3(\mathbb{C})$ restricted to the compact form, and the characters are the Schur functions in three variables.

## Summary

The algebra $M_3(\mathbb{C})$ is $\mathbb{C}^{9}$ with the flat Kähler metric and the Lebesgue measure; its holomorphic functions are the entire functions of nine variables, and the $\bar\partial$ operator detects holomorphy. The Gaussian measure $\pi^{-9}e^{-\operatorname{tr}(A^{*}A)}dA$ has entry moments $1$ and $2$, trace moment $9$, and determinant moment $\mathbb{E}[|\det A|^{2}]=6$. The Laplacian of $\mathbb{R}^{18}$ satisfies $\Delta\operatorname{tr}(A^{*}A)=36$ and $\Delta(\operatorname{tr}(A^{*}A))^{2}=80\operatorname{tr}(A^{*}A)$, with heat kernel $(4\pi t)^{-9}e^{-\|A-B\|^{2}/(4t)}$. The determinant is a cubic whose critical set is the rank-at-most-one variety, of complex dimension $5$; the hypersurface $\det=0$ has real codimension $2$ and singular locus that variety. The exponential is entire and surjective, with critical set the matrices whose eigenvalue differences are nonzero multiples of $2\pi i$. The $*$-unitary group is compact of real dimension $9$, and its Haar measure is the Weyl measure. The algebra has zero divisors — exactly the singular matrices — but no nontrivial two-sided ideals; the holomorphic functional calculus is the matrix substitute for Fueter theory, which requires an extra Clifford module.

$$
\boxed{\ \dim_\mathbb{C}M_3=9,\quad \dim_\mathbb{R}M_3=18,\quad \mathbb{E}|\det A|^{2}=6,\quad \Delta N=36,\quad \operatorname{crit}(\det)=\{\operatorname{rank}\le1\},\ \dim_\mathbb{C}=5.\ }
$$

| Quantity | Value |
|---|---|
| complex dimension | $9$ |
| real dimension | $18$ |
| Gaussian normalisation | $\pi^{-9}$ |
| $\mathbb{E}\operatorname{tr}(A^{*}A)$ | $9$ |
| $\mathbb{E}|\det A|^{2}$ | $6$ |
| $\dim_\mathbb{C}\{\operatorname{rank}\le1\}$ | $5$ |
| $\dim_\mathbb{R}U(3)$ | $9$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a_{ij}=x_{ij}+iy_{ij}$ | matrix entries and real coordinates |
| $\partial_{a},\partial_{\bar a}$ | Wirtinger derivatives |
| $dA$ | Lebesgue measure on $\mathbb{C}^{9}$ |
| $d\mu$ | Gaussian probability measure |
| $\Delta$ | Euclidean Laplacian of $\mathbb{R}^{18}$ |
| $\operatorname{adj}(A)$ | adjugate matrix |
| $\tau,\sigma,\delta$ | trace, second elementary symmetric function, determinant |
| $\Delta_{\mathrm{disc}}$ | discriminant of the characteristic cubic |

## Further Reading

- Lars Hörmander, *An Introduction to Complex Analysis in Several Variables* (North-Holland, 1990), for the Cauchy formula and holomorphic functions of several variables.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the adjugate, the determinant and the characteristic polynomial.
- Alan Edelman, "Eigenvalues and condition numbers of random matrices", *SIAM Journal on Matrix Analysis and Applications* 9 (1988), for the Gaussian determinant moments.
- Barry Simon, *Representations of Finite and Compact Groups* (AMS, 1996), for the Weyl integration formula and the character moments.
- [The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$](the-cubic-the-discriminant-and-the-spectral-strata-of-m3c.html), for the strata of the discriminant.
- [The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m3c.html), for the singular set.
- [The Exponential and the Lie Group of $M_3(\mathbb{C})$](the-exponential-and-the-lie-group-of-m3c.html), for the exponential and the logarithm.
- [The Topology of $M_3(\mathbb{C})$](the-topology-of-m3c.html), for the global topology.
- [Biquaternion Regular Functions](biquaternion-regular-functions.html), for Fueter regularity, the Dirac operator and the Clifford module that $M_3(\mathbb{C})$ does not carry.
