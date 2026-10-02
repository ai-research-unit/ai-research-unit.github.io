# __The Sturm–Liouville Operator__

## Introduction

The Sturm–Liouville operator is the second-order differential operator written in the self-adjoint form

$$
\ell u = -(p\,u')' + q\,u ,
$$

divided by a positive weight $w$, so that the operator acts on the weighted space $L^2((a,b),w\,dx)$. The form is not a convenience of notation: it is the unique way of writing a second-order expression so that the leading coefficient carries the derivative and the two integrations by parts produce the boundary term $[\,p(u\bar v'-u'\bar v)\,]_a^b$, whose vanishing is exactly the symmetry of the operator. Every second-order linear expression with a nonvanishing leading coefficient can be put in this form, and the passage is the **self-adjoint form**.

This article reads the Sturm–Liouville expression as an operator. It fixes the expression, the weight and the weighted space; proves that the operator is formally self-adjoint for the weighted Hermitian pairing, with the boundary term displayed; identifies the separated boundary conditions for which the operator with its domain is symmetric; and proves the two spectral facts that the operator supplies by itself — the eigenvalues are real and simple for a separated problem. It then states the eigenfunction expansion as the diagonalisation of the operator, gives the expansion of the solution of the boundary-value problem $Lu=f$, and works the classical instances.

The differential operators, their order, their symbol and their formal adjoint are those of *Differential Operators*; the Green operator and the compactness of the inverse are those of *The Green Operator*; the weighted $L^2$ space, the spectral theorem for a compact self-adjoint operator and the Rellich–Kondrachov theorem are those of *Measure Theory and Integration*, *Banach and Hilbert Spaces* and *Sobolev Spaces and Weak Solutions*. The classical Sturm–Liouville problem in its differential-equation form — the self-adjoint form, the reality and simplicity of the eigenvalues, the Rayleigh quotient, the asymptotic law and the expansion, all for a regular problem — is that of *Ordinary Differential Equations*, and this article cites it for the completeness and the asymptotics rather than repeating them. The boundary conditions that make the operator self-adjoint, and the pairing of the boundary data that decides it, are the subject of *Self-Adjoint Sturm–Liouville Operators* and *The Adjoint Boundary Condition* below.

## The Expression, the Weight and the Space

**Definition.** A **Sturm–Liouville expression** on an interval $(a,b)$ is a second-order differential expression of the form

$$
\ell u = -(p\,u')' + q\,u ,
$$

where $p$ is of class $C^1$, positive and real on $(a,b)$, and $q$ is continuous and real. The **weight** is a positive continuous function $w$ on $(a,b)$, and the **Sturm–Liouville operator** is

$$
Lu = \frac{1}{w}\,\ell u ,
$$

acting on functions $u$ of class $C^2$ for which $\ell u$ is locally integrable; the operator acts on the **weighted space** $L^2((a,b),w\,dx)$, whose pairing is

$$
\langle u,v\rangle_w = \int_a^b u(x)\,\overline{v(x)}\,w(x)\,dx .
$$

The problem is **regular** when $p$ and $w$ are positive and continuous on the closed interval $[a,b]$ and $q$ is continuous there; an endpoint at which $p$ vanishes or the interval is unbounded is **singular**, and the singular cases are those of Legendre's and Bessel's equations.

**Proposition (the self-adjoint form is universal).** Every second-order expression $Au''+Bu'+Cu$ with $A$ nonvanishing on $(a,b)$ can be written $\frac1w(-(pu')'+qu)$, and the form is unique up to a common factor multiplying $p$, $q$ and $w$.

*Proof.* One seeks $p,q,w$ with $\frac1w(-(pu')'+qu)=Au''+Bu'+Cu$. Comparing the second-order terms gives $pw=A$, and comparing the first-order terms gives $-p'w=-Bw$, that is $p'=Bw$; hence $(Aw)'=Bw$, so $w=A^{-1}\exp(\int B/A\,dx)$, then $p=Aw=\exp(\int B/A\,dx)$ and $q=Cw$. Any other solution multiplies all of $p$, $q$, $w$ by the same positive factor, and the operator $w^{-1}\ell$ is unchanged by that common factor.

**Proposition (formal self-adjointness).** The Sturm–Liouville operator is formally self-adjoint for the weighted pairing: for functions of class $C^2$ on $[a,b]$,

$$
\int_a^b(\ell u)\,\bar v\,dx - \int_a^b u\,\overline{\ell v}\,dx = \Bigl[p\,(u\bar v' - u'\bar v)\Bigr]_a^b ,
$$

and hence $\langle Lu,v\rangle_w = \langle u,Lv\rangle_w$ whenever the boundary term vanishes.

*Proof.* Twice integrating by parts,

$$
\int_a^b\bigl(-(pu')'\bigr)\bar v\,dx = \Bigl[-pu'\bar v\Bigr]_a^b + \int_a^b pu'\bar v'\,dx ,
\qquad \int_a^b qu\,\bar v\,dx = \int_a^b u\,\overline{qv}\,dx ,
$$

since $q$ is real; the same computation with the roles of $u$ and $v$ exchanged gives $\int u\,\overline{-(pv')'}$ together with the boundary term $[\,pu\bar v'\,]_a^b$, and subtracting the two identities gives the displayed form. Dividing by $w$ turns the plain pairing into the weighted one.

The identity is the Lagrange identity of *The Lagrange Identity and the Self-Adjoint System* in the one-dimensional case with the weight divided out, and the boundary term is the bilinear concomitant of that article. What the present article adds is the reading of the identity as the statement that $L$ is a symmetric operator on a suitable domain, which is the next section.

## The Boundary Conditions and Symmetry

**Definition.** A **separated boundary condition** for the Sturm–Liouville expression assigns, at each endpoint, one linear condition

$$
\alpha_1u(a) + \alpha_2(p\,u')(a) = 0, \qquad \beta_1u(b) + \beta_2(p\,u')(b) = 0 ,
$$

with $(\alpha_1,\alpha_2)$ and $(\beta_1,\beta_2)$ not both zero; a **periodic** condition identifies the values of $u$ and $pu'$ at the two endpoints. The **domain** $\mathcal{D}(L)$ of the Sturm–Liouville operator for a given condition is the space of $u \in L^2((a,b),w\,dx)$ of class $C^2$ satisfying it, with $Lu \in L^2((a,b),w\,dx)$.

**Theorem (the separated conditions are symmetric).** For a separated boundary condition the operator $L$ with domain $\mathcal{D}(L)$ is symmetric on $L^2((a,b),w\,dx)$:

$$
\langle Lu,v\rangle_w = \langle u,Lv\rangle_w \qquad \text{for every } u,v\in\mathcal{D}(L) .
$$

If the problem is regular, the closure of $L$ is self-adjoint on the domain obtained by taking the closure in the graph norm.

*Proof.* At each endpoint the boundary term vanishes. At $a$, the pair $(u(a),(pu')(a))$ is a multiple of $(\alpha_2,-\alpha_1)$ because of the condition, and the pair $(v(a),(pv')(a))$ is a multiple of the same vector; hence the determinant

$$
u(a)(pv')(a) - (pu')(a)v(a) = 0 ,
$$

and the conjugate determinant also vanishes, so $[\,p(u\bar v'-u'\bar v)\,]_{a}=0$; the argument at $b$ is the same. The symmetry is therefore the boundary-term identity of the preceding section. The self-adjointness of the closure in the regular case is the Weyl–Stone result quoted in *Ordinary Differential Equations*: an endpoint is in the limit-point case for every separated condition, and a symmetric operator with deficiency indices $(0,0)$ is self-adjoint.

**Definition.** A number $\lambda \in \mathbb{C}$ is an **eigenvalue** of the Sturm–Liouville operator if there is a nonzero $u\in\mathcal{D}(L)$ with $Lu=\lambda u$, i.e. $\ell u = \lambda w u$; such a $u$ is an **eigenfunction**. The **eigenvalue problem** is the equation $\ell\varphi = \lambda w\varphi$ together with the boundary condition, which is the Sturm–Liouville problem of *Ordinary Differential Equations*.

**Theorem (the eigenvalues are real and simple).** Let the boundary condition be separated and symmetric. Then every eigenvalue is real, and its eigenspace is one-dimensional.

*Proof.* Let $u\neq0$ satisfy $Lu=\lambda u$ and $v\neq0$ satisfy $Lv=\mu v$. The symmetry gives $\lambda\langle u,v\rangle_w=\langle Lu,v\rangle_w=\langle u,Lv\rangle_w=\bar\mu\langle u,v\rangle_w$, so $(\lambda-\bar\mu)\langle u,v\rangle_w=0$; taking $v=u$ gives $(\lambda-\bar\lambda)\|u\|_w^2=0$ and hence $\lambda=\bar\lambda$, so $\lambda$ is real, and eigenvectors belonging to distinct eigenvalues are orthogonal. For a real eigenvalue $\lambda$ the equation $\ell u=\lambda wu$ is a second-order equation with real coefficients and the separated conditions are one real condition at each end; the solution space of the equation is two-dimensional, the condition at $a$ cuts it to a one-dimensional subspace, and the condition at $b$ either annihilates that subspace — in which case $\lambda$ is an eigenvalue with a one-dimensional eigenspace — or leaves only the zero solution. There is no room for a second dimension.

**Theorem (the variational characterisation).** On the real domain the eigenvalues are the stationary values of the **Rayleigh quotient**

$$
R(u) = \frac{\int_a^b\bigl(p\,|u'|^2 + q\,|u|^2\bigr)dx}{\int_a^b |u|^2\,w\,dx} ,
$$

and may be characterised by the min-max principle: written in increasing order, $\lambda_n = \min\{\max_{u\in E\setminus0}R(u) : E \text{ an } n\text{-dimensional subspace of the domain}\}$. In particular $\lambda_1$ is the minimum of $R$.

*Proof.* The first variation of $R$ at $u$ in the direction $v$ is, after one integration by parts, $2\operatorname{Re}\langle \ell u - R(u)wu,\,v\rangle/\int|u|^2w$, so the stationary points are the eigenfunctions and the stationary values the eigenvalues. The Rayleigh quotient is the value of the quadratic form on the unit sphere of the weighted space, and the min-max characterisation of the eigenvalues of a symmetric operator with compact resolvent is the standard one; it shows in particular that the eigenvalues increase and tend to infinity.

## The Eigenfunction Expansion

**Theorem (the expansion).** Let the problem be regular. Then there are real numbers $\lambda_1<\lambda_2<\cdots$ with $\lambda_n\to\infty$ and eigenfunctions $\varphi_n$ such that $L\varphi_n=\lambda_n\varphi_n$, the $\varphi_n$ are orthonormal in $L^2((a,b),w\,dx)$, and they form a complete orthonormal basis: every $f$ of the space has

$$
f = \sum_{n\ge1}\langle f,\varphi_n\rangle_w\,\varphi_n , \qquad \|f\|_w^2 = \sum_{n\ge1}\bigl|\langle f,\varphi_n\rangle_w\bigr|^2 ,
$$

the series converging in the weighted $L^2$ norm; and, in the sense of the spectral theorem for a self-adjoint operator with compact resolvent,

$$
L = \sum_{n\ge1}\lambda_n\,\langle\cdot,\varphi_n\rangle_w\,\varphi_n , \qquad G = \sum_{n\ge1}\frac{1}{\lambda_n}\,\langle\cdot,\varphi_n\rangle_w\,\varphi_n ,
$$

where $G$ is the Green operator of *The Green Operator* for the same boundary condition, provided the homogeneous problem is trivial.

*Proof.* The eigenfunction expansion with the stated convergence is the Sturm–Liouville theorem of *Ordinary Differential Equations*; the eigenvalues are real and simple by the preceding section, and the asymptotic law of that article shows that they tend to infinity. For the operator form, the expansion of $f$ and the eigenvalue equation give $Lf=\sum\lambda_n\langle f,\varphi_n\rangle_w\varphi_n$ for $f$ in the domain, which is the first display. The second display follows from $LG=I$: applying the first display to $\varphi_n$ recovers $\lambda_n\varphi_n$, so $G$ acts on $\varphi_n$ by $\lambda_n^{-1}$, and the expansion of $G$ is its action on the eigenbasis. The two displays are the diagonalisation of $L$ and of its inverse.

**Corollary (the boundary-value problem).** If the homogeneous problem is trivial, then for every $\lambda$ that is not an eigenvalue the equation $Lu=\lambda u+f$, that is $\ell u = \lambda wu+wf$, has the unique solution

$$
u = \sum_{n\ge1}\frac{\langle f,\varphi_n\rangle_w}{\lambda_n-\lambda}\,\varphi_n ,
$$

the series converging in $L^2_w$; for $\lambda=0$ the solution is the Green-operator solution $Gf$.

*Proof.* Write $u=\sum c_n\varphi_n$ and $f=\sum f_n\varphi_n$ with $f_n=\langle f,\varphi_n\rangle_w$; the equation $Lu=\lambda u+f$ reads $(\lambda_n-\lambda)c_n=f_n$ for each $n$, and the coefficient is nonzero exactly when $\lambda$ is not an eigenvalue. The convergence in $L^2_w$ follows from the growth $\lambda_n\to\infty$ and the square-summability of $(f_n)$, and the case $\lambda=0$ is the expansion of $G$ above.

**Example (the classical instances).** The following are the regular and singular instances the category uses.

| Problem | $p$, $q$, $w$ | Interval | Eigenvalues | Eigenfunctions |
|---|---|---|---|---|
| Fourier sine | $1$, $0$, $1$ | $(0,\pi)$, $u(0)=u(\pi)=0$ | $n^2$ | $\sqrt{2/\pi}\sin(nx)$ |
| Fourier cosine | $1$, $0$, $1$ | $(0,\pi)$, $u'(0)=u'(\pi)=0$ | $n^2$ | normalised $\cos(nx)$, $n\ge0$ |
| Legendre | $1-x^2$, $0$, $1$ | $(-1,1)$, regular at the endpoints | $n(n+1)$ | Legendre polynomials $P_n$ |
| Bessel of order $\nu$ | $x$, $-\nu^2/x$, $x$ | $(0,R)$, bounded at $0$, $u(R)=0$ | $j_{\nu,k}^2/R^2$ | $J_\nu(j_{\nu,k}x/R)$ |
| Chebyshev | $\sqrt{1-x^2}$, $0$, $1/\sqrt{1-x^2}$ | $(-1,1)$ | $n^2$ | Chebyshev polynomials $T_n$ |

The Legendre and Bessel problems are singular at one endpoint and their conditions are the boundedness of the solution there; the completeness of their expansions is the singular case of the theorem. The special functions that arise — the Legendre, Bessel, Chebyshev and Hermite functions — are treated per system in the synthetic studies, and the harmonic polynomials whose restrictions give the Legendre functions are those of *Symmetric Tensors and Spherical Harmonics*.

## Summary

The Sturm–Liouville expression is $\ell u=-(pu')'+qu$ with $p>0$ and $q$ real, divided by a positive weight $w$ to give the operator $L=w^{-1}\ell$ on the weighted space $L^2((a,b),w\,dx)$; every second-order expression is put in this form, and the form is unique up to a common factor of $p$, $q$ and $w$. The two integrations by parts give the boundary-term identity $\int(\ell u)\bar v-\int u\overline{\ell v}=[p(u\bar v'-u'\bar v)]_a^b$, so the operator is formally self-adjoint for the weighted pairing, and a separated boundary condition makes it symmetric because the determinant of the boundary data vanishes at each endpoint; in the regular case the closure is self-adjoint. The eigenvalues are real and simple for a separated condition, they are the stationary values of the Rayleigh quotient and obey the min-max principle, and in the regular case they form an increasing sequence tending to infinity.

The eigenfunctions form a complete orthonormal basis of the weighted space, the expansion being the Sturm–Liouville theorem; in operator form the expansion diagonalises both the operator, $L=\sum\lambda_n\langle\cdot,\varphi_n\rangle_w\varphi_n$, and its inverse, the Green operator $G=\sum\lambda_n^{-1}\langle\cdot,\varphi_n\rangle_w\varphi_n$, and it solves the boundary-value problem in the form $u=\sum(\lambda_n-\lambda)^{-1}\langle f,\varphi_n\rangle_w\varphi_n$ away from the spectrum. The regular instances are the Fourier sine and cosine problems, and the singular ones are the Legendre, Bessel and Chebyshev problems, whose conditions are those of boundedness at the singular endpoint.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(a,b)$ | Interval of the problem |
| $\ell u = -(pu')'+qu$ | Sturm–Liouville expression |
| $p$, $q$, $w$ | Coefficient, potential and positive weight |
| $L = w^{-1}\ell$ | Sturm–Liouville operator on the weighted space |
| $\langle u,v\rangle_w = \int_a^b u\bar v\,w\,dx$ | Weighted Hermitian pairing |
| $L^2((a,b),w\,dx)$ | Weighted $L^2$ space |
| $\alpha_1,\alpha_2,\beta_1,\beta_2$ | Coefficients of the separated boundary conditions |
| $\lambda$, $\lambda_n$ | Spectral parameter and eigenvalues |
| $\varphi_n$ | Orthonormal eigenfunctions |
| $R(u)$ | Rayleigh quotient |
| regular, singular endpoint | $p,w$ positive and continuous on the closed interval, or not |
| $G$ | Green operator of the problem |

## Further Reading

- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (McGraw–Hill, 1955), for the Sturm–Liouville problem, the oscillation theory and the asymptotic law.
- Philip Hartman, *Ordinary Differential Equations* (Wiley, 2nd ed. 1982), for the singular Sturm–Liouville theory and the limit-point and limit-circle classification.
- Levitan and Sargsjan, *Sturm–Liouville and Dirac Operators* (Kluwer, 1991), for the operator-theoretic treatment and the eigenfunction expansion.
- Anton Zettl, *Sturm–Liouville Theory* (American Mathematical Society, 2005), for the self-adjoint boundary conditions and the modern formulation.
- Richard Beals, *Topics in Operator Theory* (University of Chicago Press, 1971), for the Sturm–Liouville operator as a self-adjoint operator with compact resolvent.
