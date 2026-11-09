# __The Biquaternion Fourier Transform: Support, Rank and Wave Fronts__

## Introduction

This article answers two questions about the biquaternion Fourier transform of a solution of a constant-coefficient equation: where the transformed object can be nonzero, and how much of the eight-dimensional algebra its value can occupy at a frequency where the equation is singular.

The setting is the one of *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, the relations $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, and the central scalar imaginary $i$. The symbol of the operator $P(D)=\sum_{\lvert\alpha\rvert\le m}a_\alpha\partial^\alpha$ is $\sigma_P(\zeta)=\sum_\alpha a_\alpha(i\zeta)^\alpha$, an element of $\mathbb{B}$, and the zero set is $Z(P)=\{\zeta\in\mathbb{R}^n:\sigma_P(\zeta)\text{ is not a unit}\}$. Two facts from that article are used throughout: the element is a unit exactly when its norm $N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ is nonzero, and the rank of left multiplication $L_{\tilde Q}$ is $8$ on the units, $4$ on the null elements other than $0$, and $0$ at $0$.

**The transform.** The transform is the one of *Biquaternion Continuous Harmonic Analysis*: a pure root $\rho$ of $-e_t$, fixed once and for all, the kernel $W(t,\omega)=\exp(-2\pi\rho\omega t)$, and the kernel multiplying the function on the left. For functions of $n$ real variables the kernel is the product of the one-variable kernels on the $n$ coordinates, which is the case $\rho_1=\dots=\rho_n=\rho$ of the two-unit transform, read on the linear form $\omega\cdot t$.

**What is proved.** That the transform diagonalises $P(D)$ at each frequency, with the symbol read at an algebra-valued frequency and with the sign of the transpose (§*The Transform and the Eigenvalue Identity*). That the transform of a solution vanishes off a set $\Omega(P)$ cut by two real equations, and that at each point of that set its value lies in the kernel of left multiplication by the symbol, a real subspace of $\mathbb{B}$ of dimension four (§*Support Inside the Zero Set*). That the rank of left multiplication takes the three values $8$, $4$, $0$, that at a null element the kernel and the cokernel are both of real dimension four and are described explicitly, and that the rank falls below four only at the origin (§*The Rank of Left Multiplication*). That the norm can degenerate identically, in which case the rank is four at every frequency and no frequency solves the equation for all data (§*The Degenerate Norm*). The last section reads the same data microlocally; the scalar theorem it quotes is Hörmander's, and the algebra-valued form of it is stated and not proved (§*The Microlocal Reading*).

**Boundaries.** The inversion of the transform and the growth of the inverse are *The Inverse Fourier Transform of a Symbol* and *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*; the placement of the kernel on the left, on the right or on both sides is *The Three Kernel Placements of the Biquaternion Fourier Transform*; the two quadratic forms and the sign that separates them are *The Biquaternion Fourier Transform and the Two Quadratic Forms*; the inversion where the symbol is not a unit is *Biquaternion Fourier Inversion on the Degenerate Set*. This article stops at the support of the transformed object, the rank of the symbol, and the reading of the two microlocally.

## The Transform and the Eigenvalue Identity

### The Kernel on Several Variables

**Definition (the one-root transform).** Let $\rho$ be a pure root of $-e_t$ and let $f:\mathbb{R}^n\to\mathbb{B}$. The **transform** of $f$ is

$$
F(\omega)=\int_{\mathbb{R}^n}\exp\bigl(-2\pi\rho\,\omega\cdot t\bigr)f(t)\,dt,\qquad \omega\cdot t=\sum_{k=1}^{n}\omega_kt_k ,
$$

and the exponential is the product $\prod_k\exp(-2\pi\rho\omega_kt_k)$, taken in that order.

**Remark (the product is a single exponential because the factors commute).** Each factor is $\cos(2\pi\omega_kt_k)e_t-\sin(2\pi\omega_kt_k)\rho$ by the closed form of the kernel, so every factor lies in the plane $\mathbb{C}e_t\oplus\mathbb{C}\rho$, which is commutative; the factors therefore commute among themselves, the product is independent of the order, and it equals $\exp(-2\pi\rho\sum_k\omega_kt_k)$. **The single root on several variables costs nothing**, and the two-unit transform of the corpus is the case of two distinct roots, where the order becomes part of the definition.

**Remark (why the placement on the left matters for the sign).** The kernel multiplies $f$ on the left, so integration by parts moves each derivative onto the kernel and produces a sign. The sign is not an accident of the computation: it says that the transform carries $P(D)$ into the symbol of the **transpose** of $P$, and that is the content of the next proposition.

### The Eigenvalue Identity

**Proposition (the kernel is an eigenfunction).** Let $\zeta=2\pi\omega\rho i\in\mathbb{B}^n$ and let $P^t(D)=\sum_\alpha(-1)^{\lvert\alpha\rvert}a_\alpha\partial^\alpha$ be the transpose of $P$. Then

$$
P^t(D)\,W(\cdot,\omega)=\sigma_{P^t}(\zeta)\,W(\cdot,\omega),\qquad \sigma_{P^t}(\zeta)=\sigma_P(-\zeta).
$$

*Proof.* For one variable and one derivative, $\partial_tW=-2\pi\rho\omega W$, so $\partial_t^kW=(-2\pi\rho\omega)^kW$; the coefficient is $a_k$, on the left, and $a_k$ is constant. For the multi-index, the derivative acts on the product of factors and distributes, and the factor $k$ contributes $(-2\pi\rho\omega_k)^{\alpha_k}$. In the symbol, $(i\zeta_k)^{\alpha_k}$ at $\zeta_k=2\pi\omega_k\rho i$ is $\bigl(i\cdot2\pi\omega_k\rho i\bigr)^{\alpha_k}=(-2\pi\rho\omega_k)^{\alpha_k}$, and the two agree. The sign $(-1)^{\lvert\alpha\rvert}$ in the transpose cancels the sign produced by moving the derivative from $f$ to $W$, which is the content of the next computation.

**Theorem (the eigenvalue identity of the transform).** Let $f$ be a Schwartz function with values in $\mathbb{B}$ and let $F$ be its transform. Then

$$
\bigl(P(D)f\bigr)^{\wedge}(\omega)=\sigma_{P^t}(\zeta)\,F(\omega)=\Sigma_P(\omega)F(\omega),\qquad \Sigma_P(\omega)=\sum_{\lvert\alpha\rvert\le m}a_\alpha\prod_{k=1}^{n}(2\pi\rho\omega_k)^{\alpha_k}.
$$

*Proof.* By the definition of the transpose, $\int_{\mathbb{R}^n}\bigl(P^t(D)W(\cdot,\omega)\bigr)f=\int_{\mathbb{R}^n}W(\cdot,\omega)\bigl(P(D)f\bigr)$ for every $\omega$, the boundary terms vanishing because $W$ is bounded and $f$ is Schwartz; the identity is the integration by parts on each variable, with the coefficients unchanged because they are constants. The left side is $\sigma_{P^t}(\zeta)F(\omega)$ by the previous proposition. The second equality is the previous proposition written out: $\sigma_P(-\zeta)$ at $\zeta=2\pi\omega\rho i$ is $\sum_\alpha a_\alpha\prod_k(2\pi\rho\omega_k)^{\alpha_k}$.

**Remark (two symbols, and which one is used below).** The article uses $\Sigma_P(\omega)$ for the eigenvalue of the transform and $\sigma_P(\zeta)$ for the symbol of the operator; they are related by $\Sigma_P(\omega)=\sigma_P(-\zeta)$ at $\zeta=2\pi\omega\rho i$, the minus sign being the sign of the transpose. **The distinction is not pedantry, because the sign is a sign of a derivative**, and an argument that mixes the two conventions reports an eigenvalue of the wrong sign; every formula in this article uses $\Sigma_P$.

**Corollary (the frequency set).** The equation at the frequency $\omega$ is solvable for every right-hand side exactly when $\Sigma_P(\omega)$ is a unit. The set of frequencies where it is not is

$$
\Omega(P)=\{\omega\in\mathbb{R}^n:N(\Sigma_P(\omega))=0\},
$$

the **frequency set** of $P$ for the transform with root $\rho$.

*Proof.* The transform of a constant-coefficient equation is the multiplication by $\Sigma_P(\omega)$ at each frequency, by the theorem; a multiplication by an element of $\mathbb{B}$ is surjective exactly when the element is a unit, by the solvability at one frequency of *The Fourier Transform and the Symbol of a Differential Operator*; and the units are the elements of nonzero norm, by the corollary of *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*.

**Remark (the frequency is an element of the algebra).** The point $-2\pi\omega\rho i$ has a nonzero vector part whenever $\rho$ is pure and $\omega\ne0$, so the frequency set is not the real zero set of $\sigma_P$ but the trace on the plane $-2\pi i\rho\mathbb{R}^n$ of the set of $\zeta\in\mathbb{B}^n$ where $\sigma_P(\zeta)$ is not a unit. **The transform with a pure root reads the symbol at algebra-valued frequencies**, and the real-frequency theory is the theory of the central root, where the plane collapses to the real axis of each variable.

**Example (two frequencies, computed).** For $P(D)=e_t+i\,e_t\partial_t$ on $\mathbb{R}$, with $\rho=\vec e_x$, the eigenvalue is $\Sigma_P(\omega)=e_t+2\pi i\omega\vec e_x$. For coefficients $a,b\in\mathbb{C}$ in the plane of $e_t$ and $\rho$ the norm is $a^2+b^2$, because $\rho^2=-e_t$; the coefficients here are $a=1$ and $b=2\pi i\omega$, so the norm is the second of the two expressions below.

$$
N\bigl(a\,e_t+b\rho\bigr)=a^2+b^2,\qquad N(\Sigma_P(\omega))=1-(2\pi\omega)^2 .
$$

So $\Omega(P)=\{-1/(2\pi),1/(2\pi)\}$: two real frequencies, and the equation is solvable for all data at every other one. The coefficient $i$ is what makes the two frequencies real, and dropping it makes the norm positive definite and the frequency set empty.

**Example (the gradient, computed).** For $P(D)=e_t\partial_0+\vec e_x\partial_1+\vec e_y\partial_2+\vec e_z\partial_3$ on $\mathbb{R}^4$ with $\rho=\vec e_x$ the eigenvalue is $\Sigma_\nabla(\omega)=2\pi\sum_k\omega_k\vec e_k\vec e_x$, and the products of the units with $\vec e_x$ on the right give $\vec e_x\vec e_x=-e_t$, $\vec e_y\vec e_x=-\vec e_z$, $\vec e_z\vec e_x=\vec e_y$. So

$$
N(\Sigma_\nabla(\omega))=4\pi^2\bigl(\omega_0^2+\omega_1^2+\omega_2^2+\omega_3^2\bigr),
$$

and the frequency set is the single point $\omega=0$. The real part is definite and the imaginary part vanishes identically, so this is the atypical shape of *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, transported to the frequency line.

**Remark (why the ordering had to be watched in the gradient).** The products $\vec e_k\vec e_x$ do not all equal $\vec e_x\vec e_k$: two of them change sign. Had the eigenvalue been written $2\pi\rho\sum_k\omega_k\vec e_k$, the norm would have come out with the opposite sign, because $\vec e_x$ does not commute with $\vec e_y$ and $\vec e_z$. **The coefficient sits on the left and the frequency factor on the right**, and the order is part of the answer.

## Support Inside the Zero Set

### The Division Formula

**Proposition (division by the symbol).** Let $f$ be Schwartz with values in $\mathbb{B}$, let $P(D)f=g$, and suppose $g$ has a transform $G$. Then

$$
\Sigma_P(\omega)F(\omega)=G(\omega)\qquad\text{for every }\omega ,
$$

and off the frequency set the transform of $f$ is recovered from that of $g$ by left multiplication by the inverse:

$$
F(\omega)=\Sigma_P(\omega)^{-1}G(\omega),\qquad \omega\notin\Omega(P).
$$

*Proof.* The first is the eigenvalue identity applied to $f$ and the definition of $G$. For the second, multiply the first on the left by $\Sigma_P(\omega)^{-1}$, which exists off $\Omega(P)$.

**Remark (the inverse symbol is smooth off the frequency set).** The inverse of left multiplication by an element is given by cofactors over the determinant: in a real basis of $\mathbb{B}$ the block $L_{\tilde Q}$ has entries linear in the coordinates, and its inverse has entries rational with denominator $\det L_{\tilde Q}$, a polynomial that does not vanish where the element is a unit. **So the inverse symbol is a smooth function of $\omega$ on the complement of $\Omega(P)$**, and this is the only analytic fact the next theorem needs.

### The Support Theorem

**Theorem (the transformed object is supported in the frequency set).** Let $f$ be a $\mathbb{B}$-valued distribution on $\mathbb{R}^n$ whose transform $F$ is defined, and suppose $P(D)f=0$. Then the support of $F$ is contained in $\Omega(P)$.

*Proof.* The identity $\Sigma_PF=0$ holds in the sense of distributions, by the eigenvalue identity applied to test functions. Let $U$ be the complement of $\Omega(P)$, an open set on which $\Sigma_P(\omega)$ is a unit at every point. Fix a real basis of $\mathbb{B}$ and write the equation as the eight scalar equations $\sum_j\Sigma_{ij}F_j=0$, where $\Sigma_{ij}$ are smooth functions on $U$ and $F_j$ are scalar distributions. The matrix $\Sigma=(\Sigma_{ij})$ is invertible at every point of $U$, and its inverse has smooth entries there by the previous remark. Then $F_j=\sum_i(\Sigma^{-1})_{ji}\bigl(\sum_k\Sigma_{ik}F_k\bigr)=0$ on $U$, because multiplication of a distribution by a smooth function is associative and the inner sum vanishes. Hence $F$ vanishes on $U$, that is, its support lies in $\Omega(P)$.

**Remark (the theorem is the statement that the transformed object lives on the zero set).** The frequency set is where the symbol stops being a unit, and the theorem says that a solution of the homogeneous equation has no transform elsewhere. **In the scalar case the corresponding set is the zero set of the principal symbol, a hypersurface; here it is cut by two real equations**, so the transformed object of a solution is confined to a thinner set than in the scalar case, and the thinness is a property of the algebra and not of the operator.

**Remark (the inhomogeneous case at a singular frequency).** Off the frequency set, $F$ is the product of the inverse symbol with $G$, and there is nothing more to say. At a point of the frequency set the equation $\Sigma_P(\omega)F(\omega)=G(\omega)$ is a linear system in the algebra, solvable exactly when $G(\omega)$ lies in the image of left multiplication by $\Sigma_P(\omega)$, and then with a kernel of solutions. **The two halves of the frequency set — where the system is solvable and where it is not — are separated by the cokernel**, and the next section measures both.

### The Value at a Singular Frequency

**Proposition (the value lies in the kernel).** Let $P(D)f=g$ with transforms $F$ and $G$, and let $\omega\in\Omega(P)$ with $\Sigma_P(\omega)\ne0$. Then the difference of any two solutions of the equation $\Sigma_P(\omega)X=G(\omega)$ lies in $\ker L_{\Sigma_P(\omega)}$, a real subspace of $\mathbb{B}$ of dimension four; in particular, when $G(\omega)=0$ the value $F(\omega)$ itself lies there.

*Proof.* The equation is $L_{\Sigma_P(\omega)}X=G(\omega)$, and the difference of two solutions lies in the kernel of $L_{\Sigma_P(\omega)}$; the dimension is $8-4=4$ by the rank theorem of the next section.

**Remark (two statements, one about the set and one about the value).** The support theorem confines the transform to a subset of $\mathbb{R}^n$; this proposition confines the value, at each point of that subset, to a four-dimensional subspace of the eight-dimensional algebra. **The two confinements are independent**, and together they say that a solution of the homogeneous equation has a transform that lives on a thin set and, there, in a thin subspace.

### What the Dimension Leaves

**Remark (the generic size of the frequency set).** The function $N(\Sigma_P(\omega))$ is a complex polynomial in $\omega$, so $\Omega(P)$ is cut by two real equations in $n$ real variables. When the two equations are independent, the frequency set has dimension $n-2$: **empty for one variable, a finite set for two, a curve for three, a surface for four**. The one-variable transform of *Biquaternion Continuous Harmonic Analysis* is therefore the case in which the frequency set is generically empty, and the singular phenomena of the biquaternion theory need at least two variables to appear on a set of positive dimension.

**Remark (independence is not automatic, and the exceptions are the interesting cases).** For the gradient the two equations are not independent: the imaginary part vanishes identically and the real part is definite, so the frequency set is one point and its codimension is $n$ and not $2$. For a symbol with a null constant term the frequency set contains $\omega=0$ and is cut there by two independent equations. **The codimension of the frequency set is a property of the operator, and the number of equations bounds it from above only.**

## The Rank of Left Multiplication

### The Three Values

**Theorem (the three values of the rank).** For $\tilde Q\in\mathbb{B}$ the rank of $L_{\tilde Q}$ is $8$ when $\tilde Q$ is a unit, $4$ when $\tilde Q$ is null and $\tilde Q\ne0$, and $0$ when $\tilde Q=0$.

*Proof.* In the model $\mathbb{B}=M_2(\mathbb{C})$, left multiplication is $X\mapsto\mathsf M(\tilde Q)X$, which is block diagonal with two copies of $\mathsf M(\tilde Q)$ acting on the two columns. So the complex rank of $L_{\tilde Q}$ is twice the rank of $\mathsf M(\tilde Q)$, and the real rank is twice the complex rank. A nonzero element of $M_2(\mathbb{C})$ is invertible or of rank one, so the complex rank of $L_{\tilde Q}$ is $2$, $1$ or $0$, and the real rank is $8$, $4$ or $0$ accordingly.

**Remark (the rank is constant on the null set, and this is the structural fact).** The rank does not vary within the null set away from the origin: it is $4$ at every null element and $8$ at every other element except $0$. **A symbol that leaves the units by becoming null loses exactly half of the algebra**, and no null element loses more. The drop is $8\to4$ as the symbol leaves the units, and the second drop $4\to0$ happens only at $0$.

### The Kernel at a Null Element

**Proposition (the kernel is the right annihilator).** Let $\tilde Q\ne0$ be null. Then $\ker L_{\tilde Q}=\{X:\tilde QX=0\}$, a minimal left ideal of $\mathbb{B}$ of real dimension four. In the model, if $u$ spans $\ker\mathsf M(\tilde Q)$, then

$$
\ker L_{\tilde Q}=\bigl\{u\,v^{\mathsf T}:v\in\mathbb{C}^2\bigr\},
$$

the set of matrices all of whose columns are multiples of $u$.

*Proof.* The equation $\tilde QX=0$ is $\mathsf M(\tilde Q)\mathsf M(X)=0$, which says that each column of $\mathsf M(X)$ lies in the kernel of $\mathsf M(\tilde Q)$. That kernel is a line, since $\mathsf M(\tilde Q)$ is nonzero and singular and a nonzero singular $2\times2$ matrix has rank one; so $\mathsf M(X)=u\,v^{\mathsf T}$ for a unique $v$, and the parameters are the two complex entries of $v$, that is four real ones. The set is a left ideal because $\tilde Q(YX)=(\tilde QY)X=0$, and it is minimal because it has complex dimension two, the least possible for a nonzero left ideal of the matrix algebra.

**Remark (the kernel is not the two-sided annihilator).** The left annihilator $\{Y:Y\tilde Q=0\}$ is a different subspace: it is a **right** ideal, of the same real dimension four, and the two meet in a complex line. In the model the left annihilator is $\{a\,w^{\mathsf T}:a\in\mathbb{C}^2\}$, where $w$ spans the annihilator of the image of $\mathsf M(\tilde Q)$, and the intersection is spanned by $u\,w^{\mathsf T}$. **The two annihilators are distinct objects and the phrase "the annihilator" without a side names neither**, which is why the kernel and the cokernel below are described separately.

### The Cokernel at a Null Element

**Proposition (the cokernel is dual to the left annihilator).** Let $\tilde Q\ne0$ be null. Then $\operatorname{coker}L_{\tilde Q}=\mathbb{B}/L_{\tilde Q}(\mathbb{B})$ has real dimension four, and the trace pairing identifies its dual with the left annihilator of $\tilde Q$.

*Proof.* Define the complex bilinear pairing $\langle X,Y\rangle=\operatorname{tr}\bigl(\mathsf M(X)\mathsf M(Y)\bigr)$, which is nondegenerate because the trace form on $M_2(\mathbb{C})$ is. For all $X,Y$,

$$
\langle Y,\tilde QX\rangle=\operatorname{tr}\bigl(\mathsf M(Y)\mathsf M(\tilde Q)\mathsf M(X)\bigr)=\operatorname{tr}\bigl(\mathsf M(Y\tilde Q)\mathsf M(X)\bigr)=\langle Y\tilde Q,X\rangle ,
$$

by the cyclicity of the trace, so the adjoint of $L_{\tilde Q}$ with respect to the pairing is $R_{\tilde Q}$, right multiplication. For a linear map of a finite-dimensional space carrying a nondegenerate bilinear form, the dual of the cokernel is the kernel of the adjoint, so the dual of $\operatorname{coker}L_{\tilde Q}$ is $\ker R_{\tilde Q}$; that kernel is four-dimensional by the proposition of the previous subsection applied on the other side.

**Remark (the cokernel described by rows).** Concretely, the cokernel is the quotient of the algebra by the space of matrices whose columns lie in a fixed line, so two elements of $\mathbb{B}$ have the same class exactly when their difference is such a matrix. **The obstruction at a null frequency is therefore two-dimensional over $\mathbb{C}$ and four-dimensional over $\mathbb{R}$**, the same size as the kernel, and the quotient is described by the rows that annihilate the image.

**Remark (the two lines, and the two cases of the null set).** Write $\mathsf M(\tilde Q)$ for a null element and let $u$ span its kernel and $w$ span the annihilator of its image. For $\tilde Q$ with $Q_t\ne0$ the image and the kernel are **complementary** lines, because $\mathsf M(\tilde Q)^2=2Q_t\mathsf M(\tilde Q)\ne0$ forces every vector of the image to be outside the kernel; for $\tilde Q$ with $Q_t=0$ the two lines **coincide**, because $\mathsf M(\tilde Q)^2=0$ puts the image inside the kernel, and both have dimension one. So the kernel and the image of $L_{\tilde Q}$ are transverse in one case and nested in the other, and the two cases are the third and fourth rows of the table of *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*.

### Below Four Only at the Origin

**Proposition (the origin is the only element of rank less than four).** The rank of $L_{\tilde Q}$ is $4$ or $8$ for every $\tilde Q\ne0$, and $0$ at $\tilde Q=0$.

*Proof.* Immediate from the theorem of §*The Three Values*.

**Remark (why this deserves a name).** The statement reads as trivial and is not: it says that the algebra has no element of rank $1$, $2$, $3$, $5$, $6$ or $7$, so the rank is a two-valued function on the null set and a one-valued function on its complement. **The reason is that the model is a full matrix algebra and left multiplication is two copies of one matrix**; in a general finite-dimensional algebra the rank of left multiplication can take intermediate values, and the biquaternion case is the regular one.

## The Degenerate Norm

### The Definition and the Example

**Definition (degenerate norm).** The operator $P$ has **degenerate norm** when $N(\Sigma_P(\omega))=0$ for every $\omega\in\mathbb{R}^n$, that is, when the frequency set is all of $\mathbb{R}^n$.

**Proposition (a criterion).** Let $q\in\mathbb{B}$ be null and let $u(\omega)\in\mathbb{B}$ be arbitrary. Then the operator whose eigenvalue is $\Sigma_P(\omega)=q\,u(\omega)$ has degenerate norm.

*Proof.* The norm is multiplicative, so $N(q\,u(\omega))=N(q)N(u(\omega))=0$ for every $\omega$.

**Example (a first-order operator with degenerate norm).** Take $q=\vec e_x+i\vec e_y$, which is null because $1+i^2=0$, and $u(\omega)=e_t+2\pi\omega\rho$. Then $\Sigma_P(\omega)=q+2\pi\omega q\rho$, and $N(\Sigma_P(\omega))=0$ for every $\omega$. The rank of $L_{\Sigma_P(\omega)}$ is four at every frequency, and the determinant $\lvert N\rvert^4$ is the zero polynomial, so the equation is not solvable for all data at any frequency.

**Remark (the symbol stays on the cone).** The example is the general mechanism: the symbol takes all its values in the null set, which is the cone of *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*. **Degeneracy is not a property of one frequency but of the whole symbol map**, and it is invisible at any single frequency taken alone.

**Proposition (degenerate symbols are a proper algebraic subset).** The set of coefficient vectors $(a_\alpha)$ for which $P$ has degenerate norm is the zero set of finitely many polynomials in the coefficients, and it is not all of the coefficient space.

*Proof.* Degeneracy says that the polynomial $\omega\mapsto N(\Sigma_P(\omega))$ is identically zero, which is the vanishing of each of its finitely many coefficients; each coefficient is a polynomial in the coefficients $a_\alpha$. The set is proper because the gradient of §*The Transform and the Eigenvalue Identity* has $N=4\pi^2\lvert\omega\rvert^2$, which is not identically zero.

### The Cone and Its Linear Pieces

**Proposition (linear families with degenerate norm).** Let $M$ be a real linear subspace of $\mathbb{B}$ consisting of null elements. Then every operator whose symbol takes its values in $M$ has degenerate norm. Such subspaces exist of real dimension four, and none has larger dimension.

*Proof.* The first sentence is the definition of $M$ read pointwise. For the dimension, a real subspace of null elements is totally isotropic for the bilinear form polarising $N$, by $2(v,w)=N(v+w)-N(v)-N(w)$; the complex span of such a subspace is totally isotropic for the complex bilinear form on $\mathbb{C}^4$, whose maximal totally isotropic subspaces have complex dimension two; so the real dimension is at most four, and the example of *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, spanned by $\vec e_x+i\vec e_y$ and $e_t+i\vec e_z$, attains it.

**Remark (the cone is not linear, and it is not free of linear pieces either).** The null set is not a linear subspace: $\vec e_x$ and $\vec e_x+i\vec e_y$ are null and $2\vec e_x+i\vec e_y$ has norm $3$. It nevertheless contains linear subspaces of real dimension four, and those are exactly the largest families of symbols on which the norm can vanish identically. **The two statements are compatible and both are needed**: a cone of real dimension six that is not linear, and planes of dimension four inside it. A reader who takes the first for the whole truth concludes that no degenerate family of symbols can be linear, and that is false; a reader who takes the second for the whole truth loses the six-dimensional shape of the cone.

**Remark (what degeneracy costs at a point).** At every frequency the equation is unsolvable for some data, the kernel is four-dimensional, and the cokernel is four-dimensional; the transform of any solution is supported in the whole space and confined there to a four-plane. **Nothing is gained by refining the frequency**, because no frequency is better than another; the information lost at the symbol is lost everywhere.

## The Microlocal Reading

### The Definition

**Definition (the wave front set).** Let $u$ be a $\mathbb{B}$-valued distribution on an open set $X\subseteq\mathbb{R}^n$ and let $(x_0,\zeta_0)\in X\times(\mathbb{R}^n\setminus\{0\})$. The point is **not** in the wave front set $\operatorname{WF}(u)$ when there are an open neighbourhood $U$ of $x_0$, an open cone $\Gamma$ containing $\zeta_0$, and a test function $\varphi$ supported in $U$ with $\varphi(x_0)\ne0$, such that for every $N$ there is $C_N$ with

$$
\lvert(\varphi u)^{\wedge}(\zeta)\rvert\le C_N(1+\lvert\zeta\rvert)^{-N},\qquad \zeta\in\Gamma .
$$

The wave front set is the complement of the set of such points.

**Remark (the definition is scalar, applied eight times).** The inequality is read on the eight real components of $\varphi u$, and the conclusion is that all eight are rapidly decreasing in the cone. **The set records two pieces of information at once**: the projection to $X$ is the singular support, and the fibre over a point records the directions in which the transform decays slowly.

### The Theorem, Quoted and Not Proved

**Theorem (quoted; Hörmander).** Let $P$ be a classical pseudodifferential operator of order $m$ on $X$, scalar-valued, with principal symbol $\sigma_P(x,\zeta)$, and let $u$ be a distribution on $X$ with $Pu$ smooth. Then

$$
\operatorname{WF}(u)\subseteq\operatorname{char}(P)=\{(x,\zeta):\sigma_P(x,\zeta)=0\}.
$$

This is Hörmander's theorem that the characteristic set contains the wave front set of any solution whose right-hand side is smooth; it is stated in *The Analysis of Linear Partial Differential Operators I*, in the chapter on the wave front set, and it is quoted here and not proved. The inclusion needs no hypothesis of principal type; the converse, that every point of the characteristic set carries a singularity, is false in general.

**Remark (the algebra case, stated and not proved).** For a biquaternion-valued operator with constant coefficients the same inclusion is expected, with the characteristic set read as the set where the symbol is not a unit,

$$
\operatorname{char}(P)=\mathbb{R}^n\times Z(P)=\{(x,\zeta):\sigma_P(\zeta)\text{ is not a unit}\},
$$

and the statement is **stated and not proved** here. The pointwise input is available: off the zero set the inverse symbol is smooth, by Cramer's rule and the non-vanishing of the determinant, which is the remark of §*The Division Formula*. What is missing is the microlocal one, namely the symbolic calculus for algebra-valued operators: the composition of two such operators has a symbol given by an asymptotic sum of derivatives of the symbol of the first against the symbol of the second, and that calculus is not developed in this article. **A reader who needs the inclusion in the algebra case must supply the calculus or cite a source that does.**

**Remark (a consistency check).** For the pure-root gradient of §*The Transform and the Eigenvalue Identity* the frequency set is $\{0\}$ and the zero set is $\{0\}$, so the characteristic set is $\mathbb{R}^4\times\{0\}$, which is empty over the nonzero frequencies; the inclusion then predicts that every solution of $\nabla f=g$ with $g$ smooth is smooth. **That is true and it is not a coincidence**: a function whose gradient is smooth is recovered by integrating the gradient along the coordinate lines, and smoothness of the gradient gives smoothness of the function.

### The Rank Read Microlocally

**Proposition (the two readings agree over constant coefficients).** For a constant-coefficient operator the characteristic set is $\mathbb{R}^n\times Z(P)$, and the frequency set $\Omega(P)$ is the trace on the plane $-2\pi i\rho\mathbb{R}^n$ of the set of points of $\mathbb{B}^n$ at which $\sigma_P$ is not a unit.

*Proof.* The characteristic set is the set of pairs whose symbol is not a unit, and the symbol does not depend on $x$, so the set is the product of $\mathbb{R}^n$ with the zero set. The second sentence is the corollary of §*The Eigenvalue Identity*: $\Sigma_P(\omega)$ is $\sigma_P$ at the point $-2\pi\omega\rho i$, and the map $\omega\mapsto-2\pi\omega\rho i$ is injective because $\rho\ne0$, so the $\omega$ at which the symbol is not a unit are exactly the points of the plane at which it is not a unit.

**Remark (the rank read microlocally).** At a point $(x,\zeta)$ of the characteristic set the two remaining numbers are the rank of $L_{\sigma_P(\zeta)}$ and the dimension of its kernel: eight and zero off the set, four and four on it away from the origin, zero and eight at the origin. **The microlocal reading says that at a singular frequency the singularity of a solution can occupy exactly the kernel directions and no others**, because the cokernel directions are the ones the equation cannot produce. That is the same data as the support theorem, read at one frequency instead of at all of them.

**Remark (what this article does not claim).** It does not claim that a singularity actually occurs at a point of the characteristic set: that is a statement about the solution and not about the operator, and the converse fails in the scalar theory, where a solution can be smooth although its principal symbol vanishes somewhere. It does not claim the algebra-valued inclusion of §*The Theorem, Quoted and Not Proved* as a theorem. **It claims the three values of the rank, the two descriptions of the kernel and the cokernel, the support of the transformed object in the frequency set, and the confinement of its value there to the kernel.**

## Summary

The transform of a biquaternion-coefficient operator multiplies the transform of the function by an element of the algebra at each frequency, and the element is the symbol read at the algebra-valued frequency $-2\pi\omega\rho i$, with the sign of the transpose because the kernel sits on the left. Where that element is a unit the transform is inverted by left multiplication by its inverse; where it is not, the transform of a solution is confined to the frequency set and, at each point of it, to the kernel of left multiplication, a real four-plane.

The rank of left multiplication takes three values: eight on the units, four on the null elements away from the origin, and zero at the origin. At a null element the kernel is the right annihilator, described as the matrices whose columns lie in a fixed line, and the cokernel is dual to the left annihilator, described as the matrices whose rows annihilate the image; both have real dimension four, and the two annihilators meet in a complex line. Below four the rank falls only at the origin.

Degeneracy is the case in which the symbol takes all its values in the null cone. The cone is not a linear subspace and contains linear subspaces of real dimension four; a symbol whose values lie in one of those has degenerate norm, and then every frequency is singular and nothing is gained by refining the frequency. Degenerate symbols are a proper algebraic subset of the coefficient space.

Microlocally the same data reads as the inclusion of the wave front set in the characteristic set, which for constant coefficients is the product of the space with the zero set. The scalar inclusion is Hörmander's and is quoted; the algebra-valued inclusion is stated and not proved, and the pointwise input to it, the smooth inverse of the symbol off the zero set, is proved here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, of real dimension $8$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The units, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | The central scalar imaginary |
| $\tilde Q$ | An element of $\mathbb{B}$ |
| $N(\tilde Q)$ | The norm $Q_t^2+Q_x^2+Q_y^2+Q_z^2$, central and complex-valued |
| $\rho$ | A pure root of $-e_t$, fixed once |
| $a_\alpha$ | The coefficient of $\partial^\alpha$ in $P(D)$, an element of $\mathbb{B}$ |
| $W(t,\omega)$ | The kernel $\exp(-2\pi\rho\omega t)$ |
| $f$, $g$ | A function and the right-hand side $P(D)f$, both $\mathbb{B}$-valued |
| $F(\omega)$, $G(\omega)$ | Their transforms |
| $\omega$ | The frequency, a point of $\mathbb{R}^n$ |
| $n$ | The number of variables |
| $\zeta$ | The algebra-valued frequency $\zeta=2\pi\omega\rho i$ |
| $P(D)$ | A constant-coefficient operator $\sum a_\alpha\partial^\alpha$ with $a_\alpha\in\mathbb{B}$ |
| $P^t(D)$ | Its transpose $\sum(-1)^{\lvert\alpha\rvert}a_\alpha\partial^\alpha$ |
| $m$ | The order of $P$ |
| $\sigma_P(\zeta)$ | The symbol $\sum a_\alpha(i\zeta)^\alpha$ |
| $\Sigma_P(\omega)$ | The eigenvalue $\sum a_\alpha\prod_k(2\pi\rho\omega_k)^{\alpha_k}$ |
| $Z(P)$ | The zero set $\{\zeta\in\mathbb{R}^n:\sigma_P(\zeta)\text{ is not a unit}\}$ |
| $\Omega(P)$ | The frequency set $\{\omega:N(\Sigma_P(\omega))=0\}$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | Left and right multiplication by $\tilde Q$ |
| $\operatorname{rank}L_{\tilde Q}$ | The real rank, $8$, $4$ or $0$ |
| $\ker L_{\tilde Q}$ | The right annihilator of $\tilde Q$, of real dimension $4$ when $\tilde Q\ne0$ is null |
| $\operatorname{coker}L_{\tilde Q}$ | The quotient $\mathbb{B}/L_{\tilde Q}(\mathbb{B})$, of real dimension $4$ when $\tilde Q\ne0$ is null |
| $u$, $w$ | In the model, a vector spanning $\ker\mathsf M(\tilde Q)$ and one spanning its cokernel |
| $\mathsf M(\tilde Q)$ | The matrix model of $\tilde Q$ |
| $\langle X,Y\rangle$ | The trace pairing $\operatorname{tr}(\mathsf M(X)\mathsf M(Y))$ |
| $\operatorname{char}(P)$ | The characteristic set, $\mathbb{R}^n\times Z(P)$ for constant coefficients |
| $X$ | An open subset of $\mathbb{R}^n$ |
| $(x_0,\zeta_0)$ | A point of $X\times(\mathbb{R}^n\setminus\{0\})$ |
| $U$, $\Gamma$, $\varphi$ | A neighbourhood, an open cone, and a test function, in the definition of the wave front set |
| $C_N$ | The constant in the rapid-decay bound, one for each $N$ |
| $\operatorname{WF}(u)$ | The wave front set of $u$ |
| $q$ | A null element used as the coefficient of a degenerate symbol |

## Further Reading

- *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, for the symbol, the block determinant $\lvert N\rvert^4$, the five cases of root and multiplicity, and the null cone with its linear subspaces; this article takes those objects and asks where and how much.
- *Biquaternion Continuous Harmonic Analysis*, for the kernel $W(t,\omega)$, the one-unit and two-unit transforms, the closed form of the kernel and the condition $\rho^2=-e_t$.
- *The Fourier Transform and the Symbol of a Differential Operator*, for the solvability at one frequency and the determinant of the regular representation, which are the two inputs of the eigenvalue identity.
- *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*, for what the frequency set does to the inverse when it is a set of codimension two and no contour can be closed.
- *Biquaternion Fourier Inversion on the Degenerate Set*, for the case treated here as the degenerate norm, where the symbol is null at every frequency and the inversion must go through a generalised inverse.
- *The Three Kernel Placements of the Biquaternion Fourier Transform*, for the sign of the transpose used here, which becomes a difference between three transforms when the kernel moves to the right or to both sides.
- *The Biquaternion Fourier Transform and the Two Quadratic Forms*, for the two forms whose disagreement is the modulus of the block determinant used throughout.
