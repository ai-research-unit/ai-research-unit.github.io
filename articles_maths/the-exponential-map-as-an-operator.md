
# __The Exponential Map as an Operator__

## Introduction

The exponential map $\exp : \mathrm{G} \to G$ carries the Lie algebra of a Lie group to the group, and it is the operator by which the linear data become group data: the one-parameter subgroups are its images, the local group law is the Campbell--Baker--Hausdorff series, and the adjoint representation of the group is the exponential of the adjoint representation of the algebra, $\operatorname{Ad}_{\exp X} = e^{\operatorname{ad}_X}$. Its differential is not the identity, and the correction is the operator $\frac{1 - e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}$; the correction is the source of every failure of the map to be a homomorphism, and the measure of that failure is the series of the next order.

This article treats the exponential map as an operator: the map itself and its functoriality, its differential in the left trivialisation, the local diffeomorphism theorem and the logarithm, the Campbell--Baker--Hausdorff series, and the special features of the compact and the nilpotent case. It is the third article of the `- Operator Theory` group of the category; the exponential map as a construction is from *Lie Groups* and *The Lie Algebra and the Exponential Map*, the invariant operators are from *Operators on a Lie Group*, and the map at the level of the enveloping algebra is *The Involution on the Enveloping Algebra of a Lie Group* of the `- * Theory` group.

The article assumes the Lie algebra as the space of left-invariant vector fields, the exponential of a vector field and the one-parameter subgroups from *The Lie Algebra and the Exponential Map*, the smooth manifold and the inverse function theorem from *Smooth Manifolds and Differential Geometry*, and the adjoint representation from *Lie Algebras*. No form, no norm and no metric is used; the convergence statements of the series are those of the finite-dimensional endomorphism algebra.

## The Map and its Functoriality

### The One-Parameter Subgroups

**Definition.** The **exponential map** of $G$ is

$$
\exp : \mathrm{G} \to G, \qquad \exp(X) = \gamma_X(1),
$$

where $\gamma_X : \mathbb{R} \to G$ is the one-parameter subgroup with $\gamma_X'(0) = X$; equivalently $\exp X = \Phi_1^X(e)$, with $\Phi^X$ the flow of the left-invariant vector field $\tilde X$ of *Operators on a Lie Group*.

**Proposition.** The map $\exp$ is smooth, $\exp(0) = e$, and for every $X$ the curve $t \mapsto \exp(tX)$ is the one-parameter subgroup with derivative $X$ at $0$; the differential of $\exp$ at the origin, $d_0\exp : \mathrm{G} \to T_eG = \mathrm{G}$, is the identity of $\mathrm{G}$.

*Proof.* The flow of a smooth vector field is smooth in the time and the initial condition, and $\exp(tX)$ is the integral curve, so its derivative at $0$ is $X$; the differential at the origin is therefore $X \mapsto X$.

### Naturality

**Theorem (the exponential is natural in the group).** For a homomorphism of Lie groups $\varphi : G \to H$ with differential $\varphi_* : \mathrm{G} \to \mathrm{H}$ at the identity, the diagram

$$
\begin{array}{ccc}
\mathrm{G} & \xrightarrow{\varphi_*} & \mathrm{H}\\
\big\downarrow\scriptstyle{\exp} & & \big\downarrow\scriptstyle{\exp}\\
G & \xrightarrow{\varphi} & H
\end{array}
$$

commutes: $\exp(\varphi_*X) = \varphi(\exp X)$ for every $X \in \mathrm{G}$. In particular the exponential commutes with the inner automorphisms, $\exp(\operatorname{Ad}_gX) = g(\exp X)g^{-1}$, with the adjoint representation of the group.

*Proof.* The curve $t \mapsto \varphi(\exp tX)$ is a one-parameter subgroup of $H$ with derivative $\varphi_*X$ at $0$, and the one-parameter subgroup is unique; the inner automorphism statement is the special case $\varphi = \Psi_g$.

## The Differential and the Correction

### The Differential of the Exponential

**Theorem (the differential in the left trivialisation).** Identify the tangent space $T_X\mathrm{G}$ with $\mathrm{G}$ by the left translation $dL_{\exp X}$, so that $d\exp_X$ becomes a linear operator on $\mathrm{G}$. Then

$$
d\exp_X = \frac{1 - e^{-\operatorname{ad}_X}}{\operatorname{ad}_X} = \sum_{k \geq 0}\frac{(-1)^k}{(k+1)!}\,\operatorname{ad}_X^k ,
$$

the series being finite because $\operatorname{ad}_X$ is nilpotent on a finite-dimensional Lie algebra at every $X$ if $\mathrm{G}$ is nilpotent and being convergent in every case for the endomorphism algebra.

*Proof.* Let $Y \in \mathrm{G}$ and consider the curve $s \mapsto \exp(X + sY)$. Writing the derivative in the right trivialisation and using the left-invariant field equation $d\exp_{X}(Y) = dL_{\exp X}\bigl(\frac{1-e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}Y\bigr)$, one solves the differential equation $\frac{d}{ds}\big|_{s=0}\exp(X+sY) = dL_{\exp X}\,u(X)Y$ with $u$ the indicated series; the standard computation is that of the left and right trivialisations of the Maurer--Cartan form, and the displayed series is the solution.

**Corollary (the kernel of the differential).** $d\exp_X$ is invertible exactly when $\operatorname{ad}_X$ has no eigenvalue in $2\pi i\,\mathbb{Z}\setminus\{0\}$; in particular $d\exp_0 = \mathrm{id}$, so $\exp$ is a local diffeomorphism at the origin.

*Proof.* The eigenvalues of $\frac{1-e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}$ are $\frac{1-e^{-\lambda}}{\lambda}$ on the generalised eigenspaces of $\operatorname{ad}_X$ with eigenvalue $\lambda$, and such an expression vanishes exactly for $\lambda \in 2\pi i\mathbb{Z}\setminus\{0\}$; at $X = 0$ the series is the identity.

### The Local Diffeomorphism

**Theorem (the logarithm).** There is an open neighbourhood $U$ of $0$ in $\mathrm{G}$ and an open neighbourhood $V$ of $e$ in $G$ such that $\exp$ restricts to a diffeomorphism $U \to V$ whose inverse is a smooth map $\log : V \to U$.

*Proof.* The differential at the origin is the identity, so the inverse function theorem of *Smooth Manifolds and Differential Geometry* applies at $0$ and gives open neighbourhoods and a smooth inverse; the inverse is the logarithm, which is therefore defined and smooth near the identity.

**Corollary (exponential coordinates).** The map $X \mapsto \exp X$ carries the coordinate $X$ of $\mathrm{G}$ to a chart at the identity of $G$, the **exponential chart**; in this chart the group law is the Campbell--Baker--Hausdorff series, and the left-invariant fields are the coordinate derivations transformed by the same series.

*Proof.* The chart is the inverse of $\log$ and the group law in it is by definition $\log(\exp X\exp Y)$, which is the Campbell--Baker--Hausdorff series expanded in the neighbourhood of the identity; the field statement is the transformation rule for the trivialisation.

## The Campbell--Baker--Hausdorff Series

### The Series

**Theorem (Campbell--Baker--Hausdorff).** In the neighbourhood of the origin in which the logarithm is defined,

$$
\log(\exp X\exp Y) = X + Y + \tfrac12[X,Y] + \tfrac1{12}\bigl([X,[X,Y]] + [Y,[Y,X]]\bigr) + \cdots ,
$$

a series in the free Lie algebra on two generators whose terms of degree $n$ are polynomials of degree $n$ in $X$ and $Y$; the series is the exponential of the Lie series $\log(e^Xe^Y)$, and its coefficients are the Bernoulli numbers.

*Proof.* The series is obtained by taking the logarithm of the product of the two exponentials in the free associative algebra on two generators and collecting the result in the free Lie algebra; the bracket operation enters through the associative product, and the integration of the differential equation $\frac{\partial}{\partial t}Z(t) = \frac{\operatorname{ad}_{Z(t)}}{1-e^{-\operatorname{ad}_{Z(t)}}}\dot Z(t)$ with $Z(t) = \log(e^{tX}e^{Y})$ produces the displayed low order terms. The convergence and the closed form are those of the free Lie algebra, developed in *Universal Enveloping Algebras*.

**Corollary.** The group law is recovered from the bracket by the series, so the Lie algebra determines the local Lie group; the map $\exp$ is a homomorphism exactly when the bracket vanishes, that is on an abelian algebra, and the first obstruction is the bilinear term $\tfrac12[X,Y]$.

*Proof.* The first two terms of the series are $X + Y$ and the group is abelian exactly when the commutator vanishes; the first nonzero correction away from the abelian case is the bracket term.

### The Adjoint Representation

**Theorem.** For all $X \in \mathrm{G}$,

$$
\operatorname{Ad}_{\exp X} = e^{\operatorname{ad}_X} = \sum_{k\geq0}\frac{1}{k!}\operatorname{ad}_X^k ,
$$

as an identity of automorphisms of $\mathrm{G}$, and the derivative at the origin of $\operatorname{Ad} : G \to \operatorname{Aut}(\mathrm{G})$ is $\operatorname{ad}$.

*Proof.* The naturality of the exponential applied to the inner automorphism $\Psi_{\exp X}$ gives $\exp(\operatorname{Ad}_{\exp X}Y) = \exp X\,\exp Y\,\exp(-X)$, whose differential at $Y = 0$ is $\operatorname{Ad}_{\exp X}$; expanding the right side by the product rule and the series of the group commutator gives $e^{\operatorname{ad}_X}Y$, and the derivative statement is the first-order term.

## The Compact and Nilpotent Cases

### The Compact Case

**Theorem (surjectivity on a compact group).** If $G$ is compact and connected, then the exponential map is surjective: every element of $G$ lies on a one-parameter subgroup.

*Proof.* A compact connected group carries a bi-invariant metric, and the one-parameter subgroups are the geodesics through $e$; the completeness of a bi-invariant metric on a compact group makes the exponential of the geodesics exhaust the group, which is the statement of the Hopf--Rinow theorem applied to the bi-invariant metric. Equivalently every element lies in a maximal torus, and the exponential maps the Cartan subalgebra onto the torus.

### The Nilpotent Case

**Theorem (global diffeomorphism for a simply connected nilpotent group).** If $\mathrm{G}$ is nilpotent and $G$ is the simply connected group with algebra $\mathrm{G}$, then $\exp$ is a diffeomorphism $\mathrm{G} \to G$; the Campbell--Baker--Hausdorff series is a polynomial, and the group law is the polynomial $\exp$ of the finite series.

*Proof.* For a nilpotent algebra the series terminates, so $\log(\exp X\exp Y)$ is a polynomial in $X$ and $Y$ and defines a group law on the vector space $\mathrm{G}$; the resulting group is simply connected with the given algebra, and by uniqueness of the simply connected group it is $G$, with $\exp$ the identity of the underlying vector space.

**Corollary (the exponential is not injective in general).** On the circle group $S^1$ the exponential map is $\mathbb{R} \to S^1$, $t \mapsto e^{2\pi i t}$, which is a local diffeomorphism and a covering but not injective; on $SU(2)$ the exponential is surjective and a local diffeomorphism away from a measure-zero set of conjugacy classes but not injective.

*Proof.* The kernel of the covering $\mathbb{R} \to S^1$ is $\mathbb{Z}$, and the corresponding statement for $SU(2)$ is computed from the diagonalisation of the elements of the group; the corrections to injectivity are the periods $2\pi i\,\mathbb{Z}$ of the differential.

## Summary

The exponential map $\exp : \mathrm{G} \to G$ sends $X$ to the value at $1$ of the one-parameter subgroup with derivative $X$, it is smooth, its differential at the origin is the identity, and it commutes with every homomorphism of Lie groups, so $\operatorname{Ad}_{\exp X} = e^{\operatorname{ad}_X}$. In the left trivialisation its differential at $X$ is the operator $\frac{1-e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}$, which is invertible exactly when $\operatorname{ad}_X$ has no nonzero eigenvalue in $2\pi i\mathbb{Z}$; at the origin it is the identity, so $\exp$ is a local diffeomorphism whose inverse is the logarithm, giving the exponential chart and the Campbell--Baker--Hausdorff series for the group law. The series recovers the group from the bracket and measures the failure of $\exp$ to be a homomorphism by the bracket term $\tfrac12[X,Y]$ and its higher corrections. On a compact connected group the exponential is surjective, and on a simply connected nilpotent group it is a global diffeomorphism with a polynomial group law; in general it is neither injective nor surjective, the periods of the differential being the obstruction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\exp : \mathrm{G} \to G$ | the exponential map |
| $\log : V \to U$ | the local inverse, the logarithm |
| $d_0\exp = \mathrm{id}$ | the differential at the origin |
| $d\exp_X = \frac{1-e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}$ | the differential in the left trivialisation |
| $d\exp_X$ invertible $\iff \operatorname{ad}_X$ has no eigenvalue in $2\pi i\mathbb{Z}\setminus\{0\}$ | the local diffeomorphism criterion |
| $\log(\exp X\exp Y) = X + Y + \frac12[X,Y] + \cdots$ | the Campbell--Baker--Hausdorff series |
| $\operatorname{Ad}_{\exp X} = e^{\operatorname{ad}_X}$ | the adjoint representation of the group |
| $\exp(\varphi_*X) = \varphi(\exp X)$ | naturality of the exponential |
| $\exp$ surjective for $G$ compact connected | the compact case |
| $\exp$ bijective for $G$ simply connected nilpotent | the nilpotent case |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the differential of the exponential and the exponential chart.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the Campbell--Baker--Hausdorff series and the logarithm.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Springer, 1992), for the convergence of the series and the correspondence between Lie algebras and Lie groups.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the one-parameter subgroups, the exponential map and its naturality.
- John M. Lee, *Introduction to Smooth Manifolds* (Springer, second edition, 2013), for the inverse function theorem and the flow of a vector field.
