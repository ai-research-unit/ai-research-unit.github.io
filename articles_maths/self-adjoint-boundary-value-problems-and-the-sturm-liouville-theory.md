# __Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory__

## Introduction

A boundary-value problem is self-adjoint when its boundary terms cancel, and the cancellation is not a technical convenience: it is the condition under which the eigenvalues of the problem are real, the eigenfunctions belonging to distinct eigenvalues are orthogonal, and the problem carries a complete eigenfunction expansion. The structure that decides all of this is a single object attached to the boundary, the **boundary form** obtained when the formal adjoint is moved across the equation: the difference

$$
\int_\Omega(Lu)\,\bar v\,dx - \int_\Omega u\,\overline{L^{\dagger}v}\,dx
$$

does not vanish for admissible pairs $u,v$, but it is a sesquilinear function of the boundary data alone. Self-adjointness is the vanishing of that form on the admissible subspace, and the reality, the orthogonality and the completeness are its consequences.

This article reads the boundary-value problem with the conjugation of the unknown functions, which is the reading of the star group. It fixes the Green formula of the problem, defines the boundary form and the admissible subspace, proves that the boundary form is skew-Hermitian, and shows that self-adjointness is exactly its vanishing; then it proves the reality of the eigenvalues and the orthogonality of the eigenfunctions; and it derives the completeness of the eigenfunction expansion from the compactness and self-adjointness of the inverse. It closes with the one-dimensional Sturm–Liouville theory, where the boundary form is the classical bracket $[\,p(u\bar v'-u'\bar v)\,]_a^b$ and the self-adjoint boundary conditions are the separated and the periodic ones.

The differential operator, its formal adjoint $L^{\dagger}$ and the boundary operator are those of *Differential Operators*; the Green operator, the characterisation of the Green function and the compactness of the inverse are those of *The Green Operator*; the Sturm–Liouville operator, the weighted space and the eigenfunction expansion are those of *The Sturm–Liouville Operator*; the spectral theorem for a compact self-adjoint operator and the reality of the spectrum of a self-adjoint operator are those of *Banach and Hilbert Spaces*; and the classical Sturm–Liouville theory of the interval — the eigenvalues, the Rayleigh quotient and the asymptotic law — is that of *Ordinary Differential Equations*, cited and not repeated. The general Lagrange identity and the bilinear concomitant are *The Lagrange Identity and the Self-Adjoint System*, the pairing of the boundary data that selects the self-adjoint conditions is *The Adjoint Boundary Condition*, and the construction of the self-adjoint operator from the form is *Self-Adjoint Sturm–Liouville Operators*, all below.

## The Green Formula and the Boundary Form

**Definition.** Let $L$ be a differential operator of order $m$ with smooth coefficients on a domain $\Omega\subseteq\mathbb{R}^n$ with smooth boundary, and let $L^{\dagger}$ be its formal adjoint. The **Green formula** for $L$ is the identity

$$
\int_\Omega(Lu)\,\bar v\,dx - \int_\Omega u\,\overline{L^{\dagger}v}\,dx = \int_{\partial\Omega} P(u,v)\,dS ,
$$

valid for functions of class $C^m$ on $\overline\Omega$, where $P(u,v)$ is a differential expression in $u$ and $v$ of order at most $m-1$ in each, linear in $u$ and conjugate-linear in $v$, the **bilinear concomitant**; it is the sum of the products of the boundary data of $u$ and $v$ up to order $m-1$.

**Definition.** The **boundary form** of $L$ on $\Omega$ is the sesquilinear form

$$
\langle u,v\rangle_\partial = \int_{\partial\Omega} P(u,v)\,dS ,
$$

defined on the functions of class $C^m$ on $\overline\Omega$; it depends on $u$ and $v$ only through their **boundary data**, the traces $\gamma u = (\gamma_0u,\dots,\gamma_{m-1}u)$ of the derivatives of order at most $m-1$ normal to the boundary. The **admissible subspace** of a boundary condition $B$ is

$$
\mathcal{A} = \{u : Bu=0 \text{ on } \partial\Omega, \ Lu\in L^2(\Omega)\} ,
$$

the domain of the realisation of $L$ under $B$ in the notation of *Differential Operators*.

**Theorem (the boundary form is skew-Hermitian).** For a formally self-adjoint operator $L=L^{\dagger}$ the boundary form is sesquilinear, linear in the first argument and conjugate-linear in the second, and

$$
\langle u,v\rangle_\partial = -\,\overline{\langle v,u\rangle_\partial} ,
$$

so that $\langle u,u\rangle_\partial$ is purely imaginary and the form is the imaginary part of a Hermitian pairing of the boundary data; it is a function of the traces $\gamma u,\gamma v$ alone.

*Proof.* The concomitant is linear in $u$ and conjugate-linear in $v$, so the form is sesquilinear. Exchanging the roles of $u$ and $v$ in the Green formula and conjugating give $\overline{\langle v,u\rangle_\partial} = -\langle u,v\rangle_\partial$ for $L=L^{\dagger}$, which is the skew-Hermitian identity; taking $v=u$ gives $\langle u,u\rangle_\partial=-\overline{\langle u,u\rangle_\partial}$, so the value is purely imaginary. That the form depends only on the traces follows from the concomitant involving the derivatives of order at most $m-1$: the expression inside the boundary integral is computed from the values of those derivatives at $\partial\Omega$.

**Definition.** The boundary-value problem $(L,B)$ is **self-adjoint** if

$$
\langle u,v\rangle_\partial = 0 \qquad \text{for every } u,v\in\mathcal{A} ,
$$

that is, if the boundary form vanishes identically on the admissible subspace, equivalently if the admissible subspace is **Lagrangian** for the skew-Hermitian form on the boundary data. The pairing of the boundary data that produces the self-adjoint conditions is *The Adjoint Boundary Condition*, below.

**Theorem (self-adjointness as the vanishing of the boundary term).** Let $L$ be formally self-adjoint and let $B$ be a boundary condition. Then the realisation of $L$ under $B$ is symmetric,

$$
\langle Lu,v\rangle = \langle u,Lv\rangle \qquad \text{for every } u,v\in\mathcal{A} ,
$$

if and only if the problem is self-adjoint in the sense above; the difference of the two sides is exactly $-\langle u,v\rangle_\partial$.

*Proof.* By the Green formula, $\langle Lu,v\rangle-\langle u,Lv\rangle=\int_\Omega(Lu)\bar v-\int_\Omega u\overline{L^{\dagger}v} = \langle u,v\rangle_\partial$, since $L=L^{\dagger}$; the identity vanishes for all admissible pairs exactly when the boundary form does.

**Example (the boundary space).** For a second-order operator on a domain the boundary data are the functions and their normal derivatives, the four numbers $(u,u_\nu)$ at each boundary point, and the boundary form is their skew-Hermitian pairing. A self-adjoint condition is a **Lagrangian subspace** of this pairing: a subspace on which the form vanishes identically. Conditions of the form $\alpha u+\beta u_\nu=0$ with real $\alpha,\beta$ are Lagrangian for the pairing $\overline{u}v_\nu-u\bar v_\nu$, and so is the periodic condition, while a condition that prescribes $u$ on part of the boundary and $u_\nu$ on the rest is Lagrangian as well; the classification of all of them, and the proof that a Lagrangian condition can always be written with half the data, is *The Adjoint Boundary Condition*, below.

## Reality and Orthogonality

**Theorem (reality of the eigenvalues).** Let the problem $(L,B)$ be self-adjoint and let $u$ be an eigenfunction, $Lu=\lambda u$ with $u\in\mathcal{A}$ and $u\neq0$. Then $\lambda$ is real.

*Proof.* From the eigenvector equation and the symmetry,

$$
\lambda\langle u,u\rangle = \langle Lu,u\rangle = \langle u,Lu\rangle = \bar\lambda\langle u,u\rangle ,
$$

so $(\lambda-\bar\lambda)\|u\|^2=0$; since $\|u\|\neq0$, $\lambda=\bar\lambda$.

**Theorem (orthogonality).** Let $u$ and $v$ be eigenfunctions of a self-adjoint problem for the eigenvalues $\lambda$ and $\mu$. If $\lambda\neq\mu$ then $\langle u,v\rangle=0$.

*Proof.* The symmetry gives $\lambda\langle u,v\rangle=\langle Lu,v\rangle=\langle u,Lv\rangle=\bar\mu\langle u,v\rangle$; since $\lambda=\bar\lambda\neq\bar\mu$, the difference $(\lambda-\bar\mu)\langle u,v\rangle$ vanishes only if the pairing does.

**Corollary (the eigenspaces and the spectral resolution).** In a self-adjoint problem the eigenspaces belonging to distinct eigenvalues are mutually orthogonal, the eigenfunctions of an eigenvalue may be orthogonalised within the eigenspace, and the eigenvalue equation $Lu=\lambda u$ may be read as the hermitian problem for the form

$$
a(u,v) = \langle Lu,v\rangle ,
$$

which is a Hermitian sesquilinear form on the admissible subspace $\mathcal{A}$, with $a(u,u)=\lambda\|u\|^2$ at an eigenfunction; the form $a$ is the **Hermitian form** of the problem, and its study is the subject of the variational articles below.

*Proof.* The orthogonality is the preceding theorem; within an eigenspace the Hermitian form $a$ is a nonzero scalar times the $L^2$ pairing, so the Gram–Schmidt process with respect to it produces an orthonormal basis. That $a$ is Hermitian on admissible pairs is the symmetry: $a(u,v)=\langle Lu,v\rangle=\langle u,Lv\rangle=\overline{a(v,u)}$. The value at an eigenfunction is $\langle\lambda u,u\rangle=\lambda\|u\|^2$.

## Completeness

**Theorem (completeness of the eigenfunction expansion).** Let the problem $(L,B)$ be self-adjoint and suppose that the Green operator $G$ of *The Green Operator* exists, is compact and is self-adjoint on $L^2(\Omega)$. Then the eigenvalues of the problem form a real sequence $\lambda_1,\lambda_2,\dots$ tending to infinity in absolute value, each of finite multiplicity, the eigenfunctions $\varphi_n$ may be chosen orthonormal in $L^2(\Omega)$, and they are complete:

$$
f = \sum_{n\ge1}\langle f,\varphi_n\rangle\,\varphi_n , \qquad \|f\|^2 = \sum_{n\ge1}\bigl|\langle f,\varphi_n\rangle\bigr|^2 ,
$$

the first series converging in $L^2(\Omega)$ for every $f$.

*Proof.* The Green operator $G$ is the inverse of $L$ on the admissible subspace, and the eigenvector equation $G\varphi=\mu\varphi$ with $\mu\neq0$ is equivalent to $L\varphi=\mu^{-1}\varphi$ with $\varphi\in\mathcal{A}$; hence the eigenvalues of $G$ are the reciprocals of the eigenvalues of $L$, and the eigenfunctions are the same. The spectral theorem for a compact self-adjoint operator on a Hilbert space, that of *Banach and Hilbert Spaces*, gives an orthonormal basis of eigenvectors of $G$ with real eigenvalues tending to $0$; reading the reciprocals gives the completeness, the reality and the finiteness of the multiplicity for $L$. The expansion is the expansion in that basis.

**Remark (self-adjointness of the inverse).** The hypothesis that $G$ is self-adjoint is the analytic form of the self-adjointness of the problem: the Green operator of a self-adjoint problem is self-adjoint, and the kernel identity $G(x,y)=\overline{G(y,x)}$ of *The Green Operator* is its integral form. The proof of the implication, with the boundary conditions of the adjoint problem entered, is the content of *The Adjoint Problem and the Green Function*, below; here it is used in the direction required, namely that the self-adjointness of the problem produces the complete expansion.

## The Sturm–Liouville Instance

**Theorem (the one-dimensional boundary form).** Let $\ell u=-(pu')'+qu$ on $(a,b)$ with $p>0$ and $q$ real, and let $L$ be the realisation of the Sturm–Liouville operator of *The Sturm–Liouville Operator*, formally self-adjoint for the weighted pairing. Then the boundary form is

$$
\langle u,v\rangle_\partial = \Bigl[p\,(u\bar v'-u'\bar v)\Bigr]_a^b ,
$$

a skew-Hermitian form in the four boundary values $u(a),u'(a),u(b),u'(b)$ and their conjugates, and the problem is self-adjoint exactly when this form vanishes for all admissible pairs.

*Proof.* The Green formula of the interval is the integration by parts, which produces the bracket $[\,p(u\bar v'-u'\bar v)\,]_a^b$; the form is the difference of the two boundary contributions, and the skew-Hermitian property follows from exchanging $u$ and $v$ and conjugating. Vanishing on the admissible pairs is the definition of self-adjointness.

**Theorem (the classical self-adjoint conditions).** For a regular Sturm–Liouville problem the separated conditions and the periodic conditions are self-adjoint, and the eigenfunction expansion they give is the classical Sturm–Liouville theory: the eigenvalues are real, simple and increasing to infinity, and the eigenfunctions are complete in $L^2((a,b),w\,dx)$.

*Proof.* For a separated condition, at each endpoint the pair $(u,(pu'))$ is a multiple of a fixed vector $(\alpha_2,-\alpha_1)$, so the bracket vanishes at each endpoint and the form is zero; for the periodic condition the two endpoints contribute opposite values which cancel. The reality, the simplicity and the completeness are then the theorems above applied to the Sturm–Liouville operator, whose Green operator is compact by *The Green Operator*; the classical statements in their differential-equation form are those of *Ordinary Differential Equations*.

**Example (the two model problems).** For $-y''=\lambda y$ on $(0,\pi)$ with $y(0)=y(\pi)=0$ the boundary form is $[\,y\bar z'-y'\bar z\,]_0^\pi$; the separated conditions make each endpoint term vanish, the eigenvalues are $n^2$, real and simple, and the eigenfunctions $\sin(nx)$ are complete, the expansion being the Fourier sine series. For the periodic problem on $(0,2\pi)$ with $y(0)=y(2\pi)$, $y'(0)=y'(2\pi)$ the endpoint terms cancel in pairs, the eigenvalues are $n^2$ for $n\ge0$ with the eigenfunctions $1$, $\cos(nx)$, $\sin(nx)$, and the expansion is the full Fourier series; the eigenvalue $0$ has multiplicity $1$ and each $n\ge1$ has multiplicity $2$, so the simplicity statement is particular to the separated case and the completeness is general.

## Summary

The boundary-value problem for a differential operator carries a boundary form, obtained from the Green formula as the difference $\int(Lu)\bar v-\int u\overline{L^{\dagger}v}$ expressed in the boundary data; for a formally self-adjoint $L$ the form is sesquilinear, skew-Hermitian, $\langle u,v\rangle_\partial=-\overline{\langle v,u\rangle_\partial}$, and determined by the traces of $u$ and $v$ up to order $m-1$. The problem is self-adjoint when the form vanishes on the admissible subspace, equivalently when the admissible subspace is Lagrangian for it, and that vanishing is exactly the symmetry of the realisation, $\langle Lu,v\rangle-\langle u,Lv\rangle=\langle u,v\rangle_\partial$. Self-adjointness makes the eigenvalues real, by $(\lambda-\bar\lambda)\|u\|^2=0$, and makes the eigenfunctions belonging to distinct eigenvalues orthogonal; the eigenspaces are mutually orthogonal and the eigenvalue equation is the hermitian problem for the form $a(u,v)=\langle Lu,v\rangle$.

If in addition the Green operator is compact and self-adjoint, the spectral theorem for a compact self-adjoint operator gives a complete orthonormal system of eigenfunctions, the eigenvalues being the reciprocals of its eigenvalues, real, of finite multiplicity and tending to infinity; this is the completeness of the eigenfunction expansion, $f=\sum\langle f,\varphi_n\rangle\varphi_n$. On an interval the boundary form is the classical bracket $[\,p(u\bar v'-u'\bar v)\,]_a^b$, the separated and periodic conditions are self-adjoint, and the resulting theory is the classical Sturm–Liouville theory: real, simple, increasing eigenvalues and a complete expansion in the weighted space, the periodic case differing only in the multiplicity of the eigenvalues.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$, $L^{\dagger}$ | Differential operator and its formal adjoint |
| $P(u,v)$ | Bilinear concomitant, the boundary integrand of the Green formula |
| $\langle u,v\rangle_\partial = \int_{\partial\Omega}P(u,v)\,dS$ | Boundary form |
| $\gamma u = (\gamma_0u,\dots,\gamma_{m-1}u)$ | Boundary data (traces of the normal derivatives) |
| $\mathcal{A}$ | Admissible subspace of the boundary condition |
| $a(u,v)=\langle Lu,v\rangle$ | Hermitian form of the problem |
| $\lambda_n$, $\varphi_n$ | Eigenvalues and orthonormal eigenfunctions |
| $G$ | Compact self-adjoint Green operator |

## Further Reading

- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (McGraw–Hill, 1955), for the self-adjoint Sturm–Liouville problem and the completeness of the expansion.
- Philip Hartman, *Ordinary Differential Equations* (Wiley, 2nd ed. 1982), for the boundary conditions that make a Sturm–Liouville problem self-adjoint.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the reality and the completeness of the spectrum of a self-adjoint operator.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness* (Academic Press, 1975), for the boundary form, the self-adjoint extensions and the spectral theorem.
- Michael E. Taylor, *Partial Differential Equations I* (Springer, 2nd ed. 2011), for the Green formula, the boundary form and the elliptic self-adjoint boundary-value problems.
- Gerald B. Folland, *Introduction to Partial Differential Equations* (Princeton University Press, 2nd ed. 1995), for the boundary terms of an elliptic operator and the self-adjoint conditions.
