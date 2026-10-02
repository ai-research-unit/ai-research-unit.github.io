# __Self-Adjoint Elliptic Operators and the Spectral Theorem__

## Introduction

A self-adjoint elliptic operator under a self-adjoint boundary condition has a discrete spectrum and a complete set of eigenfunctions, and the eigenvalues obey a law of growth that depends only on the volume of the domain and the order of the operator. The realisation of the elliptic operator on its domain is self-adjoint when the boundary form of the problem vanishes, its inverse is compact, and the spectral theorem for a self-adjoint operator with compact resolvent then gives the complete orthonormal system and the eigenfunction expansion. The **Weyl law** is the asymptotic count of the eigenvalues: for the Laplacian on a bounded domain the number of eigenvalues below $\lambda$ grows like the volume of the region $\{|\xi|^2\le\lambda\}$ divided by $(2\pi)^n$,

$$
N(\lambda) \sim \frac{\omega_n}{(2\pi)^n}\,|\Omega|\,\lambda^{n/2} ,
$$

with $\omega_n$ the volume of the unit ball; the constant is the one the phase space of a particle in the domain would give, and the coincidence is the leading theorem of the spectral asymptotics of elliptic operators.

This article reads the self-adjoint elliptic operator with the conjugation that defines its adjoint. It fixes the realisation and its self-adjointness; states the spectral theorem in the elliptic setting, with the complete eigenfunction expansion and the functional calculus; derives the discreteness of the spectrum and the growth of the eigenvalues from the compactness of the inverse; and proves the Weyl law in its leading term, with the heat-kernel proof and the statement of the second term. It closes with the Dirichlet and Neumann cases, whose leading asymptotics coincide.

The self-adjointness of the boundary-value problem and the vanishing of the boundary form are *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*; the weak formulation, the coercivity and the solution operator are *Sesquilinear Forms and the Weak Formulation of an Elliptic Problem*; the Dirichlet principle and the regularity of the weak solution are *The Dirichlet Principle and the Hermitian Functional*; the min–max principle is *Variational Methods and the Hermitian Form*; the spectral theorem for a self-adjoint operator, the spectral measure and the functional calculus are *Unbounded Operators and Spectral Measures* and *Banach and Hilbert Spaces*; the compact self-adjoint theorem and Rellich–Kondrachov are *Banach and Hilbert Spaces* and *Sobolev Spaces and Weak Solutions*; and the heat kernel and the elliptic regularity are *Distributions and Fundamental Solutions* and *Partial Differential Equations*. The boundary-value problem of the classical second-order operator and its Green function are *Ordinary Differential Equations* and *The Green Operator*.

## The Self-Adjoint Realisation

**Definition.** Let $L$ be the elliptic operator of *Sesquilinear Forms and the Weak Formulation of an Elliptic Problem*, formally self-adjoint ($A=A^{\mathsf T}$, $b=0$, $c$ real) and uniformly elliptic, and let $B$ be a self-adjoint boundary condition, so that the boundary form of *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory* vanishes on the admissible subspace. The **realisation** of $L$ under $B$ is the operator

$$
\mathrm{dom}\,L = \{u\in H^2(\Omega) : Bu=0\},\qquad Lu = -\sum_{i,j}\partial_i(a_{ij}\partial_ju)+cu ,
$$

acting in $L^2(\Omega)$; it is the **self-adjoint realisation** of the boundary-value problem.

**Theorem (the realisation is self-adjoint with compact inverse).** Let the form be bounded and coercive on the admissible subspace and let the boundary condition be self-adjoint. Then the realisation is self-adjoint, $\langle Lu,v\rangle=\langle u,Lv\rangle$ for $u,v$ in the domain, and its inverse, the solution operator $S$ of the weak problem, is compact and self-adjoint on $L^2(\Omega)$.

*Proof.* The symmetry is the vanishing of the boundary form of the two functions, which is the definition of the self-adjoint condition; the self-adjointness of the realisation follows because the adjoint operator has the domain characterised by the adjoint boundary condition, which is the same condition. The solution operator is the inverse by construction; it is self-adjoint because the form is Hermitian and the operator is symmetric, and it is compact because it maps $L^2$ into $H^2\cap\mathrm{dom}$, compactly embedded by Rellich–Kondrachov.

## The Spectral Theorem

**Theorem (the spectral theorem for the elliptic realisation).** Let $L$ be a self-adjoint realisation with compact inverse. Then there is an orthonormal basis $(\varphi_n)$ of $L^2(\Omega)$ consisting of eigenfunctions,

$$
L\varphi_n = \lambda_n\varphi_n , \qquad \varphi_n\in\mathrm{dom}\,L ,
$$

the eigenvalues real, of finite multiplicity and with $|\lambda_n|\to\infty$; the operator has the spectral representation

$$
Lf = \sum_{n\ge1}\lambda_n\,\langle f,\varphi_n\rangle\,\varphi_n , \qquad \mathrm{dom}\,L = \Bigl\{f\in L^2(\Omega) : \sum_n\lambda_n^2|\langle f,\varphi_n\rangle|^2<\infty\Bigr\} ,
$$

and for every bounded Borel function $g$ on the real line the functional calculus is

$$
g(L)f = \sum_{n\ge1}g(\lambda_n)\,\langle f,\varphi_n\rangle\,\varphi_n ,
$$

with the spectral measure $E(B)=\sum_{\lambda_n\in B}P_n$, where $P_n$ is the orthogonal projection onto the eigenspace of $\lambda_n$.

*Proof.* The inverse $S$ is compact and self-adjoint, so by the spectral theorem for a compact self-adjoint operator of *Banach and Hilbert Spaces* it has an orthonormal basis of eigenvectors with eigenvalues $\mu_n$ real and $\to0$; the eigenvector equation $S\varphi=\mu\varphi$ is equivalent to $L\varphi=\mu^{-1}\varphi$ with $\varphi\in\mathrm{dom}\,L$, so the eigenfunctions of $S$ are those of $L$ and the eigenvalues are the reciprocals, giving the reality, the finite multiplicity and $|\lambda_n|\to\infty$. The spectral representation and the functional calculus are the spectral theorem for a self-adjoint operator as stated in *Unbounded Operators and Spectral Measures*, applied to the discrete spectrum produced by the compactness of $S$.

**Corollary (the expansion and the Green function).** For $f\in L^2(\Omega)$ the series $f=\sum_n\langle f,\varphi_n\rangle\varphi_n$ converges in $L^2$, and the solution of $Lu=f$ in the domain is $u=\sum_n\lambda_n^{-1}\langle f,\varphi_n\rangle\varphi_n$; the Green function of the problem is

$$
G(x,y) = \sum_{n\ge1}\frac{\varphi_n(x)\overline{\varphi_n(y)}}{\lambda_n} ,
$$

the series converging in $L^2(\Omega\times\Omega)$ and, when the eigenfunctions are continuous, absolutely and uniformly away from the diagonal.

*Proof.* The expansion is the Parseval identity in the orthonormal basis; applying $S=L^{-1}$ gives the solution series, and the kernel of $S$ is the displayed sum by the expansion of the kernel in the basis $(\varphi_n\otimes\overline{\varphi_m})$.

## The Discrete Spectrum

**Theorem (discreteness and growth).** Let the self-adjoint realisation be coercive and let the eigenvalues be ordered, $\lambda_1\le\lambda_2\le\cdots$. Then the spectrum is discrete, $\lambda_n\to+\infty$, and the counting function $N(\lambda)=\#\{n : \lambda_n\le\lambda\}$ is finite for every $\lambda$; the eigenvalues are characterised variationally by the min–max principle of *Variational Methods and the Hermitian Form*.

*Proof.* The compactness of the inverse gives $|\lambda_n|\to\infty$, and the coercivity gives $\lambda_n>0$ with $\lambda_1\ge c_*$; the count of the eigenvalues below a fixed $\lambda$ is finite because the eigenvalues tend to infinity. The variational characterisation is the min–max theorem, which needs the form coercive relative to the $L^2$ pairing, the hypothesis here.

## The Weyl Law

**Theorem (Weyl's law for the Laplacian).** Let $\Omega\subseteq\mathbb{R}^n$ be a bounded open set with smooth boundary, and let $N(\lambda)$ be the counting function of the eigenvalues of $-\Delta$ under the Dirichlet condition, ordered increasingly and counted with multiplicity. Then

$$
N(\lambda) \sim \frac{\omega_n}{(2\pi)^n}\,|\Omega|\,\lambda^{n/2} \qquad (\lambda\to\infty) ,
$$

where $\omega_n$ is the volume of the unit ball in $\mathbb{R}^n$ and $|\Omega|$ is the volume of the domain; equivalently the eigenvalues grow as

$$
\lambda_k \sim 4\pi^2\Bigl(\frac{k}{\omega_n|\Omega|}\Bigr)^{2/n} ,
$$

and the same leading term holds for the Neumann condition and for any self-adjoint elliptic realisation of the Laplacian.

*Proof.* The proof is the **heat-kernel method**. The trace of the heat semigroup is $\operatorname{tr}e^{t\Delta}=\sum_ne^{-\lambda_nt}$ for $t>0$, and the heat kernel of the Dirichlet problem satisfies $K(t,x,x)\sim(4\pi t)^{-n/2}$ as $t\downarrow0$ uniformly on compact subsets of $\Omega$ by *Distributions and Fundamental Solutions*; integrating over $\Omega$,

$$
\sum_{n\ge1}e^{-\lambda_nt} = \int_\Omega K(t,x,x)\,dx \sim \frac{|\Omega|}{(4\pi t)^{n/2}} \qquad (t\downarrow0) .
$$

The two sides of the asymptotics are related by Karamata's Tauberian theorem for the Laplace transform: if the $\lambda_n$ increase and $\sum_ne^{-\lambda_nt}\sim Ct^{-\alpha}$ as $t\downarrow0$, then $N(\lambda)\sim\frac{C}{\Gamma(\alpha+1)}\lambda^\alpha$. Here $\alpha=n/2$ and $C=|\Omega|(4\pi)^{-n/2}$, so

$$
N(\lambda) \sim \frac{|\Omega|}{(4\pi)^{n/2}\,\Gamma(n/2+1)}\,\lambda^{n/2} = \frac{\omega_n}{(2\pi)^n}\,|\Omega|\,\lambda^{n/2} ,
$$

the second equality using $\omega_n=\pi^{n/2}/\Gamma(n/2+1)$ and $(4\pi)^{n/2}\pi^{n/2}=(2\pi)^n$.

**Remark (the second term and the method of the proof).** The heat-kernel proof gives the leading term and, if the heat trace is expanded further, the second term $c_n|\partial\Omega|\lambda^{(n-1)/2}$, the **Weyl conjecture**, whose sign distinguishes the Dirichlet from the Neumann condition; the full expansion of the heat trace and the proof of the second term, with the role of the periodic orbits of the billiard, lie outside this article and belong to *Partial Differential Equations* and its spectral theory. The leading term depends only on the volume, and the term of order $n-1$ on the area of the boundary; the counting function of a general elliptic operator of order $2m$ has the same form with $\lambda^{n/(2m)}$ in place of $\lambda^{n/2}$ and the volume of the unit ball replaced by the phase-space volume $\{x\in\Omega,\ \sigma_L(x,\xi)\le1\}$.

## Examples

**Example (the interval).** For $-\Delta=-d^2/dx^2$ on $\Omega=(0,\pi)$ with the Dirichlet condition the eigenvalues are $\lambda_n=n^2$, $n\ge1$. The Weyl law in dimension $n=1$ has $\omega_1=2$, the volume of the interval $[-1,1]$, so

$$
N(\lambda)\sim\frac{2}{2\pi}\cdot\pi\cdot\lambda^{1/2}=\sqrt{\lambda} ,
$$

and indeed $\#\{n : n^2\le\lambda\}=\lfloor\sqrt\lambda\rfloor\sim\sqrt\lambda$. The eigenvalues are simple, and the counting function satisfies $N(\lambda)\approx\sqrt\lambda$ to within one.

**Example (the square).** For $-\Delta$ on $\Omega=(0,\pi)^2$ with the Dirichlet condition the eigenvalues are $m^2+n^2$ for $m,n\ge1$, with multiplicity equal to the number of representations. The Weyl law has $\omega_2=\pi$ and $|\Omega|=\pi^2$, so

$$
N(\lambda)\sim\frac{\pi}{4\pi^2}\cdot\pi^2\cdot\lambda=\frac{\pi}{4}\,\lambda ,
$$

which is the area of the quarter disc $\{x,y\ge0 : x^2+y^2\le\lambda\}$ of radius $\sqrt\lambda$; the leading count of the eigenvalues is the count of the lattice points in that quarter disc, a theorem of Gauss already visible in the constant $\pi/4$.

**Example (different boundary conditions).** For the Neumann condition on $(0,\pi)$ the eigenvalues are $n^2$, $n\ge0$, differing from the Dirichlet list by the single eigenvalue $0$ shifted into the count: $N_{\mathrm{D}}(\lambda)=\lfloor\sqrt\lambda\rfloor$ and $N_{\mathrm{N}}(\lambda)=\lfloor\sqrt\lambda\rfloor+1$, so the leading term of the Weyl law is the same and the difference is confined to the lower order. This is the statement that the leading term sees only the volume, while the boundary condition enters the second term.

## Summary

A formally self-adjoint uniformly elliptic operator with a self-adjoint boundary condition has a self-adjoint realisation on $H^2\cap\mathrm{dom}\,B$, its inverse being the compact self-adjoint solution operator of the weak problem. The spectral theorem gives an orthonormal basis of eigenfunctions, the spectral representation $Lf=\sum\lambda_n\langle f,\varphi_n\rangle\varphi_n$, the domain characterised by the square-summability of $\lambda_n\langle f,\varphi_n\rangle$, and the functional calculus $g(L)=\sum g(\lambda_n)P_n$; the Green function is the kernel $\sum\lambda_n^{-1}\varphi_n(x)\overline{\varphi_n(y)}$. The spectrum is discrete with $\lambda_n\to+\infty$ when the form is coercive, the eigenvalues are counted by the finite function $N(\lambda)$ and characterised by the min–max principle. The Weyl law gives the leading asymptotics $N(\lambda)\sim\frac{\omega_n}{(2\pi)^n}|\Omega|\lambda^{n/2}$, the same for the Dirichlet and the Neumann conditions, with the first correction of order $\lambda^{(n-1)/2}$ depending on the boundary area and, in sign, on the condition.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$ | Self-adjoint elliptic realisation |
| $\mathrm{dom}\,L=H^2\cap\{Bu=0\}$ | Domain of the realisation |
| $\lambda_n$, $\varphi_n$ | Eigenvalues and orthonormal eigenfunctions |
| $S=L^{-1}$ | Compact self-adjoint solution operator |
| $E(B)=\sum_{\lambda_n\in B}P_n$ | Spectral measure of $L$ |
| $g(L)$ | Functional calculus |
| $N(\lambda)$ | Counting function of the eigenvalues |
| $\omega_n$ | Volume of the unit ball in $\mathbb{R}^n$ |
| $|\Omega|$, $|\partial\Omega|$ | Volume of the domain and area of its boundary |

## Further Reading

- Hermann Weyl, *Das asymptotische Verteilungsgesetz der Eigenwerte linearer partieller Differentialgleichungen* (Mathematische Annalen 71, 1912), for the eigenvalue asymptotics and the phase-space constant.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators* (Academic Press, 1978), for the spectral theorem, the compact-resolvent case and the Weyl law.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the self-adjoint realisations and the spectral theory of elliptic operators.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators III* (Springer, 1985), for the spectral asymptotics of elliptic operators and the Tauberian method.
- Michael E. Taylor, *Partial Differential Equations I* (Springer, 2nd ed. 2011), for the variational eigenvalues, the spectral theorem and the heat-kernel asymptotics.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics I* (Interscience, 1953), for the eigenfunction expansion and the min–max principle.
