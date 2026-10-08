# __The Biquaternion Holomorphic Dynamics and the Jacobian__

## Introduction

The biquaternion quadratic map is holomorphic for the complex structure of the algebra, so it has a complex derivative, a Jacobian, a critical set and a local inverse, and the local theory of holomorphic dynamics begins there. The article computes the Jacobian, identifies the critical set and the critical values, defines the Fatou set and the Julia set for the biquaternion map, proves that for a central parameter the two definitions of the Julia set coincide through the eigenvalues, and describes the local picture at the critical set. The several-variable theory differs from the one-variable theory in that the Fatou set and the Julia set can be defined in several inequivalent ways, and the article keeps the definitions apart and states which equivalences are proved.

The quadratic family, its critical set and its derivative are *The Biquaternion Quadratic Map and Its Julia Sets*; the matrix model and the operator reading of the derivative are *The Matrix Representation and the Biquaternion Dynamics*; the cone and the singular Julia set are *The Zero Divisors and the Singular Julia Sets*; the Green's function and the equilibrium measure are *The Escape Radius and the Green's Function for the Biquaternions* and *The Pluripotential Theory of the Biquaternion Dynamics*. The general theory is *The Fatou Components and the Classification of the Dynamics* and *Several Complex Variables*.

The article owns the Jacobian and its determinant, the local biholomorphism off the critical set, the definition of the Fatou and Julia sets, the central-parameter theorem identifying the two Julia sets, the fixed-point multiplier computation, and the local picture at the cone. It does not re-derive the derivative.

**Standing convention.** $F=F_{\tilde C}$ is the quadratic family in the general plain bilinear product, $dF|_{\tilde Q}(\tilde P)=\tilde Q\tilde P+\tilde P\tilde Q$ is its complex derivative, and $\Sigma(\mathbb{B})=\mathscr{Z}\cup\mathrm{Vect}(\mathbb{B})$ is the critical set.

## Holomorphy and the Jacobian

**Proposition (holomorphy).** The map $F$ is holomorphic for the complex structure of the algebra: in the four complex coordinates of the model it is a polynomial map with no conjugated coordinate. Its derivative at $\tilde Q$ is the complex-linear map

$$
dF|_{\tilde Q}:\tilde P\longmapsto\tilde Q\tilde P+\tilde P\tilde Q ,
$$

whose determinant, in the coordinates of the model, is $4\,N(\tilde Q)\,(2Q_0)^2$.

**Proof.** The general plain bilinear product is complex-bilinear and the map is a polynomial in it; the derivative is the product rule, and the determinant is the critical-set proposition of *The Biquaternion Quadratic Map and Its Julia Sets*, where the matrix model gives the explicit form $I\otimes M+M^{\mathsf{T}}\otimes I$ and the determinant $\det(M)\operatorname{tr}(M)^2\cdot4$.

**Corollary (the local inverse).** Off the critical set $\Sigma(\mathbb{B})$ the map $F$ is a local biholomorphism: every $\tilde Q\notin\Sigma(\mathbb{B})$ has a neighbourhood $U$ with $F:U\to F(U)$ biholomorphic and $F^{-1}$ holomorphic on $F(U)$.

**Proof.** $\det dF|_{\tilde Q}\neq0$ exactly off $\Sigma(\mathbb{B})$, and the inverse function theorem for holomorphic maps of several variables applies.

**Remark (the derivative is an operator and the Jacobian is its determinant).** The derivative is the sum of two multiplication operators and not a multiplication; this is why the critical set is read from the pair of eigenvalues of the model and not from the element alone (*The Matrix Representation and the Biquaternion Dynamics*, §*The Warning: Elements and Operators*). **The Jacobian vanishes on the union of the zero-divisor cone and the vector subspace, and nowhere else.**

## The Critical Set, the Critical Values and the Local Picture

**Proposition (the critical values).** The critical set $\Sigma(\mathbb{B})$ is the union of the cone $\mathscr{Z}$ and the vector subspace $\mathrm{Vect}(\mathbb{B})$, both of complex dimension three. The image of the cone is the translate of the cone, $F(\mathscr{Z})=\mathscr{Z}+\tilde C$, and the image of the vector subspace is the complex line through the parameter in the scalar direction, $F(\mathrm{Vect}(\mathbb{B}))=\tilde C+\mathbb{C}e_0$; hence the set of critical values is $(\mathscr{Z}+\tilde C)\cup(\tilde C+\mathbb{C}e_0)$.

**Proof.** On the cone $F(\tilde Q)=\tilde Q^2+\tilde C=2Q_0\tilde Q+\tilde C$ with $\tilde Q^2=2Q_0\tilde Q$ by Cayley–Hamilton, and $2Q_0\tilde Q$ ranges over the cone as $\tilde Q$ does, so the image is the cone translated by $\tilde C$. On the vector subspace, $\mathbf P^2=-(\mathbf P,\mathbf P)e_0$ is central, and $-(\mathbf P,\mathbf P)$ ranges over all of $\mathbb{C}$ as $\mathbf P$ ranges over the pure vectors, so the image is the scalar line through $\tilde C$.

**Remark (the derivative is nilpotent at the square-zero points).** At a square-zero $\tilde Q$ the derivative is $\tilde P\mapsto\tilde P\tilde Q+\tilde Q\tilde P$, of image of complex dimension two, so the map is not a local biholomorphism there and the local degree is degenerate; **on the cone the map is not finite, and this is the local form of the obstruction of the category.**

## The Fatou Set and the Julia Set

**Definition.** The **Fatou set** $\mathcal{F}_{\tilde C}$ is the set of the points $\tilde Q$ having a neighbourhood on which the sequence of iterates $(F^n)$ is equicontinuous, equivalently a neighbourhood on which the family is normal; the **Julia set** $\mathcal{J}_{\tilde C}$ is its complement in $\mathbb{B}$. This is the **dynamical Julia set**, to be distinguished from the **set-theoretic Julia set** $J_{\tilde C}=\partial\mathcal K_{\tilde C}$ of the previous articles and from the support of the equilibrium measure, the **small Julia set** of *The Pluripotential Theory of the Biquaternion Dynamics*.

**Remark (the three definitions).** In one variable the Fatou set, the complement of the boundary of the filled Julia set and the complement of the support of the equilibrium measure all coincide after the extension to the Riemann sphere, and the three objects are one. In several variables the definitions are inequivalent in general: the equicontinuity definition uses the normalisation at infinity, the boundary of the filled Julia set uses the escape dichotomy, and the small Julia set uses the equilibrium measure. **The article proves the identification for a central parameter and states the general equivalence as open.**

**Proposition (the small Julia set is contained in the dynamical one).** The support of the equilibrium measure is contained in the dynamical Julia set, and the dynamical Julia set is contained in the complement of the interior of the filled Julia set.

**Proof.** On a neighbourhood where the iterates are equicontinuous the dynamics is stable and the equilibrium measure, if it exists, is invariant and cannot charge an open set of stability by the classical argument of the one-variable theory transported to the model; the second inclusion is that the interior of the filled Julia set is a region of stable bounded dynamics.

## The Central Parameter and the Eigenvalue Reduction

**Theorem (the central-parameter identification).** Let $\tilde C=Ce_0$ be central and let $\mathcal{F}_C$, $\mathcal{J}_C$ be the Fatou set and the Julia set of $\zeta\mapsto\zeta^2+C$ in the complex plane. Then for a diagonalisable $\Phi(\tilde Q)$ with spectrum $\{\lambda_1,\lambda_2\}$,

$$
\tilde Q\in\mathcal{J}_{\tilde C}\iff \mathrm{spec}\,\Phi(\tilde Q)\cap\mathcal{J}_C\neq\emptyset ,
$$

and

$$
\mathcal{J}_{\tilde C}=\partial\mathcal K_{\tilde C}=\{\tilde Q : \mathrm{spec}\,\Phi(\tilde Q)\subset K_C \text{ and } \mathrm{spec}\,\Phi(\tilde Q)\cap J_C\neq\emptyset\}.
$$

So for a central parameter the dynamical Julia set, the boundary of the filled Julia set and the set of the matrices with an eigenvalue on the complex Julia set are one and the same set.

**Proof.** For a central parameter the orbit is the polynomial in one element and the spectrum iterates by the complex map, so the stability of the biquaternion orbit at a diagonalisable point is the stability of the two eigenvalue orbits: if an eigenvalue lies on the complex Julia set, an arbitrarily small perturbation of the eigenvalue produces an arbitrarily large change in the iterates and the family is not equicontinuous; if both eigenvalues lie in the complex Fatou set, the orbits are stable and the diagonaliser contributes a bounded, harmless factor, so the family is equicontinuous. The three sets on the right are equal by the eigenvalue reduction and the spectral description of the boundary of *The Hausdorff Dimension of the Biquaternion Julia Sets*.

**Remark (the normalisation at infinity).** In the complex plane the Fatou set includes the basin of infinity because the constant limit $\infty$ is normal on the sphere; in the model the same holds after the compactification of $\mathbb{C}^4$ by the hyperplane at infinity, on which the map is the squaring of the highest-degree part and the hyperplane is (super)attracting. **The identification of the theorem uses this normalisation and is not available without it.**

## Fixed Points and Their Multipliers

**Proposition (the fixed points).** For a central parameter $C$, the fixed points of $F$ are the solutions of $\tilde Q^2-\tilde Q+Ce_0=0$. They are the scalar solutions $\lambda e_0$ with $\lambda^2-\lambda+C=0$, and the non-scalar solutions $\tilde Q=\tfrac12e_0+\mathbf Q$ with $(\mathbf Q,\mathbf Q)=C-\tfrac14$, one for each complex isotropic vector of the quadratic form $\mathbf Q\cdot\mathbf Q$ with that value. The multiplier spectrum of a fixed point is

$$
\{2\lambda_1,\ 2\lambda_2,\ 2Q_0,\ 2Q_0\} ,
$$

the eigenvalues of the differential $L_{\tilde Q}+R_{\tilde Q}$, and the fixed point is attracting exactly when $\rho(\Phi(\tilde Q))<1/2$.

**Proof.** Insert $\tilde Q^2=2Q_0\tilde Q-N(\tilde Q)e_0$ (Cayley–Hamilton) into $\tilde Q^2+\tilde C=\tilde Q$: $(2Q_0-1)\tilde Q+(C-N)e_0=0$. If $\tilde Q$ is not central the two terms are independent and give $Q_0=\tfrac12$ and $N=C$, that is $(\mathbf Q,\mathbf Q)=C-\tfrac14$. The differential of the family is $L+R$, whose eigenvalues are the sums $\lambda_i+\lambda_j$ of the eigenvalues of the model, that is $\{2\lambda_1,\ \lambda_1+\lambda_2,\ \lambda_2+\lambda_1,\ 2\lambda_2\}=\{2\lambda_1,\ 2\lambda_2,\ 2Q_0,\ 2Q_0\}$; the attracting condition is that all four have modulus below one, and since $2Q_0=\lambda_1+\lambda_2$ is dominated by the two doubled eigenvalues, the condition is $|\lambda_i|<1/2$ for both, that is $\rho(\Phi(\tilde Q))<1/2$.

**Corollary (the neutral fixed points).** The non-scalar fixed points have $2Q_0=1$ among their multipliers, so they are never attracting; the ones with $\operatorname{tr}\Phi(\tilde Q)=1$ are neutral in the trace direction and repelling or neutral in the other, and they carry the parabolic local dynamics at the singular set.

## The Local Dynamics at the Singular Set

**Remark (the local model at the square-zero cone).** At a square-zero $\tilde Q$ the derivative has image of complex dimension two and kernel of complex dimension two, so the local map is not finite; the first non-linear term is the square itself, and on the cone the local picture is the familiar one of a map with a positive-dimensional fibre, the petals of the parabolic case being replaced by the cone directions. **The local dynamics at the cone is the only part of the Fatou–Julia theory of the category that is not inherited from the one-variable theory**, and it is where the local classification must be built if it is built at all.

**Remark (what is open).** The classification of the Fatou components of a biquaternion map, the equivalence of the three definitions of the Julia set for a non-central parameter, the structure of the Fatou set at the cone and the existence of a local normal form there are all open. **The article reports the central-parameter theory, which is complete because it is the one-variable theory read on the eigenvalues, and states the non-central theory as the research problem it is.**

## Summary

The biquaternion quadratic map is holomorphic, its derivative at a point is the sum of the left and the right multiplications by the point, and its Jacobian determinant is proportional to $N(\tilde Q)Q_0^2$, so the map is a local biholomorphism exactly off the critical set, the union of the zero-divisor cone and the vector subspace. The Fatou set is defined by the equicontinuity of the iterates and the dynamical Julia set is its complement; the set-theoretic Julia set of the escape dichotomy and the small Julia set of the equilibrium measure are two other objects, and the three coincide in one variable and are not known to coincide in general here. For a central parameter the three do coincide: the dynamical Julia set, the boundary of the filled Julia set, and the set of the matrices with an eigenvalue on the complex Julia set are one set, and the Fatou set is its complement. The fixed points are the scalar solutions of $\lambda^2-\lambda+C=0$ and the non-scalar elements $\tfrac12e_0+\mathbf Q$ with $(\mathbf Q,\mathbf Q)=C-\tfrac14$; the multiplier spectrum is $\{2\lambda_1,2\lambda_2,2Q_0,2Q_0\}$, the attracting condition is $\rho(\Phi(\tilde Q))<1/2$, and the non-scalar fixed points are neutral in the trace direction. The local dynamics at the cone, the classification of the Fatou components and the general equivalence of the definitions are open.

## Summary of Notation

| symbol | meaning |
|---|---|
| $dF|_{\tilde Q}(\tilde P)=\tilde Q\tilde P+\tilde P\tilde Q$ | the complex derivative |
| $\det dF=4N(\tilde Q)(2Q_0)^2$ | the Jacobian determinant |
| $\Sigma(\mathbb{B})=\mathscr{Z}\cup\mathrm{Vect}(\mathbb{B})$ | the critical set |
| $\mathcal{F}_{\tilde C}$, $\mathcal{J}_{\tilde C}$ | the Fatou set and the dynamical Julia set |
| $\mathcal K_{\tilde C}$, $J_{\tilde C}=\partial\mathcal K_{\tilde C}$ | the filled Julia set and the set-theoretic Julia set |
| $\mathcal{F}_C$, $\mathcal{J}_C$, $K_C$, $J_C$ | the one-variable Fatou, Julia, filled and boundary sets |
| $\{\lambda_1,\lambda_2\}$ | the spectrum of $\Phi(\tilde Q)$ |
| $\rho(\Phi(\tilde Q))$ | the spectral radius, the attracting condition $\rho<1/2$ |

## Further Reading

- *The Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-biquaternion-quadratic-map-and-its-julia-sets.md`), for the family and the critical set.
- *The Matrix Representation and the Biquaternion Dynamics* (`articles_maths/the-matrix-representation-and-the-biquaternion-dynamics.md`), for the operator reading of the derivative.
- *The Zero Divisors and the Singular Julia Sets* (`articles_maths/the-zero-divisors-and-the-singular-julia-sets.md`), for the cone and the singular part of the fractal.
- *The Fatou Components and the Classification of the Dynamics* (`articles_maths/the-fatou-components-and-the-classification-of-the-dynamics.md`), for the one-variable classification the central-parameter theorem reproduces.
- *Several Complex Variables* (`articles_maths/several-complex-variables.md`), for the several-variable definitions kept apart here.
