# __The Green Operator__

## Introduction

A differential expression $L$ has no inverse by itself: the equation $Lu=f$ leaves the solutions of $Lu=0$ free, and the choice of an inverse is the choice of the boundary conditions that kill them. Once a boundary condition is imposed and the homogeneous problem has only the trivial solution, the inverse exists, and on a bounded domain it is an **integral operator**, whose kernel is the **Green function**. The Green operator is therefore the second object of this group: the differential operator is the expression, and the Green operator is the inverse of that expression under a boundary condition.

This article fixes the boundary-value problem of a differential operator, proves that its inverse exists exactly when the homogeneous problem is trivial, and identifies that inverse as the integral operator with kernel the Green function. It then characterises the Green function by three properties — it solves $L_xG(x,y)=\delta_y$ in the first variable, it satisfies the boundary condition there, and across the diagonal its first derivative jumps by the reciprocal of the leading coefficient of $L$ — proves that the Green function of a formally self-adjoint problem is Hermitian-symmetric, and works the one-dimensional Sturm–Liouville construction and the Dirichlet Laplacian. It closes by placing the Green operator in the operator calculus: it is compact on a bounded domain, it is the resolvent of $L$ at the parameter $0$, and the resolvent at a nonzero parameter is the Green operator of the shifted expression.

The differential operator, its order and its symbol are those of *Differential Operators*. The fundamental solution of $L$ on the whole space, of which the Green function is a boundary-corrected instance, and the parametrix are those of *Distributions and Fundamental Solutions*; the classical Green function of the Laplacian with the harmonic corrector is that of *Partial Differential Equations*; the Green function of a linear ordinary boundary-value problem and the Sturm–Liouville theory are those of *Ordinary Differential Equations*; and the compactness used below is the Rellich–Kondrachov theorem of *Sobolev Spaces and Weak Solutions*. The symmetry of the Green function for a formally self-adjoint problem and the reciprocity it expresses are the subject of *The Adjoint Problem and the Green Function*, and the resolvent read as a Green operator is *The Resolvent Operator*, both below.

## The Boundary-Value Problem and Its Inverse

**Definition.** Let $L$ be a differential operator of order $m$ of *Differential Operators* on a domain $\Omega\subseteq\mathbb{R}^n$ with smooth boundary, and let

$$
B = (B_1,\dots,B_m)
$$

be a **boundary operator**: each $B_j$ is a differential operator of order $m_j<m$ on $\partial\Omega$, and $B$ has order at most $m-1$. The **boundary-value problem** for $L$ and $B$ asks, for a given $f$, for a function $u$ with

$$
Lu = f \ \text{on }\Omega, \qquad Bu = 0 \ \text{on }\partial\Omega ,
$$

where $Bu=0$ means $B_ju=0$ for $j=1,\dots,m$. The **homogeneous problem** is the case $f=0$; its solutions form the kernel of $L$ under the boundary condition, written $\ker(L,B)$.

**Definition.** A **Green operator** for $(L,B)$ is a linear operator $G$ with

$$
GLu = u \ \text{for every } u \text{ with } Bu=0, \qquad LGu = f \ \text{and } B(Gu)=0 \ \text{for every admissible } f .
$$

It is the inverse of the operator $u\mapsto Lu$ from the domain $\{u : Bu=0\}$ onto the range, and it exists exactly when that map is injective.

**Theorem (invertibility criterion).** The Green operator exists exactly when $\ker(L,B)=\{0\}$. If $\ker(L,B)\neq\{0\}$, then the problem $Lu=f$, $Bu=0$ has either no solution or infinitely many, and it has a solution exactly when $f$ is orthogonal to the kernel of the adjoint problem; the adjoint problem and the pairing that decides it are the subject of *The Adjoint Problem and the Green Function*.

*Proof.* If $Gu$ exists for every $u$ with $Bu=0$ and $Lu=0$ then $u=G0=0$, so the kernel is trivial. Conversely, if the kernel is trivial then $L$ maps its domain injectively; the range is the image, and the inverse on the range is defined by $G(Lu)=u$, extended by linearity. If the kernel is nontrivial and $u_0$ is a nonzero element of it, then a solution $u$ of $Lu=f$ produces the whole affine family $u+cu_0$, and no solution exists when $f$ is not in the range; the solvability condition in the self-adjoint case is the orthogonality to the kernel, the Fredholm alternative of *Fredholm Theory*.

**Theorem (the inverse is an integral operator).** Suppose that $\Omega$ is bounded and that the Green operator $G$ exists and maps $L^2(\Omega)$ into $L^2(\Omega)$. Then there is a measurable function $G : \Omega\times\Omega\to\mathbb{C}$, the **Green function**, with

$$
(Gu)(x) = \int_\Omega G(x,y)\,u(y)\,dy
$$

for every $u \in L^2(\Omega)$; the function $G(x,\cdot)$ is locally integrable for almost every $x$, and the integral converges for every $u$ of the space.

*Proof.* The map $f \mapsto Gf$ is the composition of the inverse of $L$ with the inclusion $L^2\to H^{-m}$ and is a linear operator on $L^2$; it is bounded under the hypothesis, and its Schwartz kernel is the Green function. The identification with the displayed integral is the statement of the Schwartz kernel theorem for the pair of measure spaces $\Omega$ and $\Omega$ with Lebesgue measure, applied to the bounded operator $G$; the kernel is a function and not merely a distribution because $G$ maps $L^2$ to $L^2$ by hypothesis.

**Proposition (regularity gain).** If $L$ is elliptic of order $m$ with smooth coefficients and $G$ maps $L^2(\Omega)$ into $H^m(\Omega)$, then $G : L^2(\Omega)\to H^m(\Omega)$ is bounded and its kernel is of class $C^\infty$ away from the diagonal.

*Proof.* The operator $G$ is bounded on $L^2$ by the preceding theorem, and its range lies in $H^m$ by hypothesis, so the graph of $G$ as an operator into $H^m$ is closed; the closed graph theorem of *Banach and Hilbert Spaces* makes it bounded as a map into $H^m$. The smoothness away from the diagonal follows from the elliptic regularity of $L$ applied in the variable $y$ to the equation $L_yG(x,y)=0$, valid for $y\neq x$ because the delta is supported on the diagonal; the coefficients are smooth and the equation is elliptic, so the solution is smooth off the diagonal.

## The Green Function

**Theorem (characterisation).** Let $L$ be of order $2$ with leading coefficient $p$, and suppose the Green operator exists. Then the Green function is characterised by the three conditions

$$
L_xG(x,y) = \delta(x-y), \qquad B_xG(\cdot,y) = 0 \ \text{for } y\in\Omega, \qquad G(\cdot,y)\in L^1_{\mathrm{loc}}(\Omega) ,
$$

the equation being read in the distributional sense of *Distributions and Fundamental Solutions*; equivalently, $G(\cdot,y)$ solves $L_xG=0$ away from $x=y$ and has the singularity fixed by the delta.

*Proof.* For fixed $y$ take $f=\delta_y$, which is admissible for the equation; the solution supplied by the Green operator is $G(\cdot,y)$, so $L_xG(x,y)=\delta(x-y)$ and $B_xG(\cdot,y)=0$. The local integrability of $G(\cdot,y)$ is the statement that the kernel is a function of $y$, which it is because $G$ maps $L^2$ into $L^2$ and the Schwartz kernel of such an operator is locally integrable. Conversely, if a locally integrable kernel $K(x,y)$ satisfies $L_xK(x,y)=\delta(x-y)$ and $B_xK(\cdot,y)=0$, then

$$
u(x) = \int_\Omega K(x,y)\,f(y)\,dy
$$

satisfies $Lu=f$ and $Bu=0$ for every admissible $f$, by interchanging $L_x$ with the integral; so $K$ defines a right inverse of $L$ on the admissible functions, and it is the Green function by uniqueness of the inverse.

**Theorem (the jump condition).** Let $L = -(p\,\partial_x)' + q$ act on functions of one variable, with $p\in C^1$, $p>0$, and let $G$ be its Green function for a boundary condition of order $1$ at each endpoint. Then $G$ is continuous on the diagonal, $G$ is of class $C^2$ off it, and

$$
p(y)\Bigl(\partial_xG(y^-,y) - \partial_xG(y^+,y)\Bigr) = 1 .
$$

*Proof.* The equation $L_xG=\delta(x-y)$ says that $L_xG=0$ away from the diagonal. Integrating the equation against the indicator of the interval $(y-\varepsilon,y+\varepsilon)$ gives

$$
-\bigl[p\,\partial_xG\bigr]_{y-\varepsilon}^{y+\varepsilon} + \int_{y-\varepsilon}^{y+\varepsilon}q\,G\,dx = 1 ,
$$

and letting $\varepsilon\to0$ the integral tends to $0$ because $G$ is locally integrable, so the jump of $p\,\partial_xG$ is $1$. The continuity of $G$ itself follows from the same integration once more, the right-hand side being bounded; the regularity off the diagonal is that of the solutions of $Lw=0$ with $C^1$ coefficients, which are of class $C^2$.

**Theorem (symmetry).** Let $(L,B)$ be formally self-adjoint, so that $L=L^{\dagger}$ and the boundary condition pairs with itself. Then the Green function is **Hermitian-symmetric**,

$$
G(x,y) = \overline{G(y,x)} ,
$$

and for a real operator it is symmetric, $G(x,y)=G(y,x)$. The identity expresses the **reciprocity** of the boundary-value problem: the response at $x$ to a source at $y$ equals the conjugate response at $y$ to a source at $x$.

*Proof.* By the defining identity of the formal adjoint applied with $u=G(\cdot,x)$ and $v=G(\cdot,y)$,

$$
\int_\Omega \bigl(L_yG(y,x)\bigr)\,\overline{G(y,y')}\,dy = \int_\Omega G(y,x)\,\overline{L^{\dagger}_yG(y,y')}\,dy .
$$

Since $L=L^{\dagger}$, the left-hand side is $\int\delta(y-x)\overline{G(y,y')}dy=\overline{G(x,y')}$, and the right-hand side is $\int G(y,x)\overline{\delta(y-y')}dy=G(y',x)$. Comparing gives $\overline{G(x,y')}=G(y',x)$, which is the stated symmetry after renaming the variables. Both functions satisfy the boundary condition, so the two applications of the defining identity are legitimate. For a real operator the bar is the identity and the symmetry is the plain equality $G(x,y)=G(y,x)$.

**Example (the interval).** For $-y''=f$ on $(0,1)$ with $y(0)=y(1)=0$ the Green function is

$$
G(x,y) = \begin{cases} x(1-y), & x\le y,\\ y(1-x), & x\ge y,\end{cases}
$$

which is continuous, has the jump $\partial_xG(y^-,y)-\partial_xG(y^+,y) = (1-y)-(-y) = 1$, and is symmetric; the jump condition is satisfied with $p\equiv1$, and a direct differentiation confirms that $u(x)=\int_0^1G(x,y)f(y)\,dy$ solves $-u''=f$ with $u(0)=u(1)=0$.

**Example (the Dirichlet Laplacian).** For $-\Delta u=f$ on a bounded domain $\Omega$ with $u|_{\partial\Omega}=0$, the Green function is

$$
G(x,y) = \Phi(x-y) - H(x,y),
$$

where $\Phi$ is the fundamental solution of the Laplacian and $H(\cdot,y)$ is the harmonic corrector solving $\Delta_yH=0$ with $H(x,y)=\Phi(x-y)$ for $y\in\partial\Omega$; the subtraction removes the boundary value of $\Phi(x-\cdot)$ and is exactly the choice of the boundary condition. The construction and the Poisson kernel of the ball are those of *Partial Differential Equations*.

## Construction and the Operator Calculus

**Theorem (the one-dimensional construction).** Let $L = -(p\,\partial_x)'+q$ with $p>0$ of class $C^1$ and $q$ continuous on $[a,b]$, and let the boundary condition be separated. If the homogeneous problem is trivial, let $u_<$ be the solution of $Lu=0$ satisfying the condition at $a$, normalised by $u_<'(a)=1$, and $u_>$ the solution satisfying the condition at $b$, normalised by $u_>'(b)=1$. Then

$$
G(x,y) = \frac{u_<(x\wedge y)\,u_>(x\vee y)}{p(y)\,W(y)} , \qquad W = u_<'u_> - u_<u_>' ,
$$

where $x\wedge y$ and $x\vee y$ are the smaller and the larger of $x$ and $y$, and $W$ is a nonzero constant by the Liouville identity.

*Proof.* The function on the right is, in each of the two regions $x<y$ and $x>y$, a product of two solutions of $Lu=0$, hence a solution of $Lu=0$; it satisfies the boundary conditions because one factor does at each end. Across $x=y$ it is continuous, both expressions reducing to $u_<(y)u_>(y)/(pW)$, and the jump of its first derivative is

$$
\frac{u_<'(y)u_>(y)-u_<(y)u_>'(y)}{p(y)W(y)} = \frac{W(y)}{p(y)W(y)} = \frac1{p(y)} ,
$$

which is the jump condition. The characterisation theorem then identifies it with the Green function. The constancy of $W$ is $(pW)'=p'W + pW' = p'W + p(u_<''u_>-u_<u_>'') = p'W - p'W = 0$, using $-(pu_<')'+qu_<=0$ and the same for $u_>$.

**Proposition (compactness).** If $\Omega$ is bounded and $L$ is elliptic of order $m$ with smooth coefficients, and if the boundary condition is coercive enough that $G(L^2(\Omega))\subseteq H^m(\Omega)$, then $G$ is a compact operator on $L^2(\Omega)$.

*Proof.* The operator $G$ factors as $L^2(\Omega)\to H^m(\Omega)\to L^2(\Omega)$, the first map bounded by the regularity hypothesis and the second compact by the Rellich–Kondrachov theorem of *Sobolev Spaces and Weak Solutions* on a bounded Lipschitz domain; a composition of a bounded with a compact operator is compact.

**Theorem (the shifted operator).** Let $G$ be the Green operator of $(L,B)$ and let $\lambda$ be a complex number for which the homogeneous problem $(L-\lambda)u=0$, $Bu=0$ has only the trivial solution. Then the Green operator $G_\lambda$ of $(L-\lambda,B)$ exists and

$$
G_\lambda = G\,(I-\lambda G)^{-1} = (I-\lambda G)^{-1}G , \qquad G_\lambda = G + \lambda\,G\,G_\lambda .
$$

*Proof.* The operator $I-\lambda G$ is the composition $\lambda^{-1}(L-\lambda)G$ for $\lambda\neq0$, so it is invertible exactly when $(L-\lambda,B)$ has trivial kernel, and its inverse is $G$ composed with $G_\lambda$; the two expressions agree because $G$ commutes with $(I-\lambda G)^{-1}$, both being functions of $G$. The identity $G_\lambda = G+\lambda GG_\lambda$ is the algebraic rearrangement. For $\lambda=0$ the operator is $G$, and the family depends on $\lambda$ as the resolvent does; the identification of $G_\lambda$ with the resolvent of $L$ under the boundary condition is the content of *The Resolvent Operator* below.

**Theorem (the spectral reading of the Green operator).** Suppose in addition that $G$ is compact and self-adjoint on $L^2(\Omega)$, with orthonormal eigenfunctions $\varphi_n$ and eigenvalues $\mu_n$ of $G$. Then the eigenfunctions of $G$ are the eigenfunctions of $L$ under $B$, with $\mu_n = 1/\lambda_n$ where $L\varphi_n=\lambda_n\varphi_n$ and $B\varphi_n=0$, and

$$
G = \sum_n \frac{1}{\lambda_n}\langle\cdot,\varphi_n\rangle\,\varphi_n , \qquad G(x,y) = \sum_n \frac{\varphi_n(x)\overline{\varphi_n(y)}}{\lambda_n} ,
$$

the second series converging in $L^2(\Omega\times\Omega)$, the first in the operator norm; the eigenvalues $\lambda_n$ are real and tend to infinity, and none is $0$ because the kernel is trivial.

*Proof.* The eigenvector equation $G\varphi=\mu\varphi$ with $\mu\neq0$ is equivalent, on applying $L$, to $L\varphi=\mu^{-1}\varphi$ together with $B\varphi=0$; hence $\mu=1/\lambda$ for an eigenvalue $\lambda$ of $L$ under $B$, and every eigenfunction of $L$ arises so. The spectral theorem for a compact self-adjoint operator on a Hilbert space, that of *Banach and Hilbert Spaces*, gives the orthonormal eigenbasis and the norm-convergent series for $G$; the kernel form is the expansion of the kernel of a Hilbert–Schmidt operator. The eigenvalues of $L$ are real because $L$ is formally self-adjoint and $G$ is self-adjoint, and they tend to infinity because their reciprocals tend to $0$. The spectral theory of these operators, and the Weyl law for their counting function, is *Self-Adjoint Elliptic Operators and the Spectral Theorem* below.

## Summary

The boundary-value problem for a differential operator $L$ of order $m$ and a boundary operator $B$ of orders at most $m-1$ has an inverse exactly when the homogeneous problem $Lu=0$, $Bu=0$ has only the trivial solution, and when it does the inverse is the Green operator $G$; if the homogeneous problem is nontrivial, the inhomogeneous problem has no solution or infinitely many, and the solvability is decided by the orthogonality to the adjoint kernel. On a bounded domain the Green operator is an integral operator whose kernel is the Green function $G(x,y)$, and the Green function is characterised by $L_xG(x,y)=\delta(x-y)$, by the boundary condition $B_xG(\cdot,y)=0$ in the first variable, and by local integrability. For a second-order operator it is smooth off the diagonal, continuous on it, and its first derivative jumps by the reciprocal of the leading coefficient; for a formally self-adjoint problem it is Hermitian-symmetric, $G(x,y)=\overline{G(y,x)}$, which is the reciprocity of the problem.

On an interval the Green function is assembled from the two solutions of $Lu=0$ that satisfy the boundary conditions at the two ends, $G(x,y)=u_<(x\wedge y)u_>(x\vee y)/(pW)$, with the Wronskian $W$ constant; for the Dirichlet Laplacian it is the fundamental solution corrected by the harmonic term that makes the boundary value vanish. On a bounded domain the Green operator is compact, and it is the resolvent of $L$ at the parameter zero, the resolvent at a nonzero parameter being the Green operator of the shifted expression, $G_\lambda=G+\lambda GG_\lambda$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$ | Differential operator of order $m$ |
| $B=(B_1,\dots,B_m)$ | Boundary operator, $B_ju=0$ on $\partial\Omega$ |
| $\ker(L,B)$ | Kernel of the homogeneous problem |
| $G$ | Green operator, the inverse of $L$ under $B$ |
| $G(x,y)$ | Green function, the kernel of $G$ |
| $\delta$, $\delta_y$ | Delta distribution at the origin, respectively at $y$ |
| $\Phi$ | Fundamental solution of the Laplacian |
| $H(x,y)$ | Harmonic corrector for the Dirichlet problem |
| $u_<$, $u_>$ | Solutions of $Lu=0$ satisfying the condition at the left, respectively the right, end |
| $W = u_<'u_>-u_<u_>'$ | Wronskian of $u_<,u_>$ |
| $x\wedge y$, $x\vee y$ | Minimum and maximum of $x$ and $y$ |
| $G_\lambda$ | Green operator of $L-\lambda$ |

## Further Reading

- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (McGraw–Hill, 1955), for the Green function of a two-point boundary-value problem and the construction from two solutions.
- Ivar Stakgold, *Green's Functions and Boundary Value Problems* (Wiley, 3rd ed. 2011), for the Green function, the jump condition and the reciprocity.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for the Green function of an elliptic boundary-value problem and the harmonic corrector.
- Gerald B. Folland, *Introduction to Partial Differential Equations* (Princeton University Press, 2nd ed. 1995), for the Green function as the kernel of the inverse operator.
- François Treves, *Basic Linear Partial Differential Equations* (Academic Press, 1975), for the relation between the Green function, the fundamental solution and the parametrix.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the inverse of a closed operator and the resolvent of a shifted operator.
