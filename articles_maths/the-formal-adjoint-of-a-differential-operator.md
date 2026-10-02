# __The Formal Adjoint of a Differential Operator__

## Introduction

The **formal adjoint** of a differential operator $P$ is the operator $P^*$ obtained by **integrating by parts**: it is the operator for which the identity $\int\langle Pu, v\rangle = \int\langle u, P^*v\rangle$ holds for all compactly supported sections. The construction is local — it uses only the metrics on the bundles and the density on the manifold — so it produces a differential operator of the same order, not a boundary condition and not a global operator. It is the algebraic skeleton of the adjoint, and it is what the global $L^2$ adjoint of the next entry is the closure of.

The article develops the formal adjoint. It fixes the pairing of the sections by a density and metrics, defines $P^*$ by integration by parts, and proves that the formal adjoint of an operator of order at most $k$ is an operator of order at most $k$ and is unique; it proves the **Lagrange identity**, that the difference $v\,Pu - u\,P^*v$ is a divergence, hence integrable to the boundary term of **Green's formula**; it computes the symbol of $P^*$ as $(-1)^k$ times the adjoint of the symbol of $P$; and it treats the formally self-adjoint operators, the Sturm–Liouville operator, the divergence and the exterior derivative as the examples.

The article assumes the differential operators, their order, their principal symbol and the jet-bundle theorem of *Differential Operators on a Manifold*; the covariant derivative and the curvature of *The Covariant Derivative*; the exterior derivative, the Hodge star and the codifferential of *The Exterior Derivative* and *The Codifferential*, all in this category; the Riemannian metrics, the volume form and the metrics on vector bundles of *Hermitian Metrics and the Levi-Civita Connection* and *Hermitian Vector Bundles and the Chern Connection*; the integration and Stokes' theorem of *Differential Forms and Stokes' Theorem*; and the Hermitian metrics on the fibres of *Hermitian Structures and the Almost Complex Structure*. The global adjoint — the domain, the boundary conditions, the weak formulation and the closedness — is *The L2 Adjoint of a Differential Operator*, the next entry of this group; the formulas are stated here in the form that the global theory then closes. No physics is invoked.

## The Pairing and the Definition

### The Data

Let $M$ be a smooth manifold of dimension $n$, oriented and with a fixed smooth positive **density** $d\mu$ — a volume form when $M$ is oriented; let $E \to M$ and $F \to M$ be vector bundles with smooth fibrewise inner products $\langle\cdot,\cdot\rangle_E$ and $\langle\cdot,\cdot\rangle_F$, real or Hermitian; and let $P : \Gamma(E)\to\Gamma(F)$ be a differential operator of order at most $k$ in the sense of *Differential Operators on a Manifold*. The **pairing** of two compactly supported sections is

$$
\langle u, v\rangle_{L^2} = \int_M \langle u, v\rangle\, d\mu,
$$

where the integrand is the fibrewise inner product at each point; the density is the integration measure, and no orientation is needed for it, only a top-degree positive form or a Radon measure with a smooth positive density.

### The Definition

**Definition.** The **formal adjoint** of $P$ with respect to the densities and the metrics is a differential operator $P^* : \Gamma(F)\to\Gamma(E)$ such that

$$
\langle Pu, v\rangle_{L^2} = \langle u, P^*v\rangle_{L^2}
$$

for all $u \in \Gamma_c(E)$ and $v \in \Gamma_c(F)$ of compact support. This is the **integration-by-parts** identity, and it is required to hold for all pairs of compactly supported sections.

**Theorem (existence and uniqueness).** For every differential operator $P$ of order at most $k$ there is exactly one formal adjoint $P^*$, and it is a differential operator of order at most $k$. In a chart with coordinates and frames, if

$$
Pu = \sum_{|\alpha|\le k} A_\alpha(x)\,\partial_\alpha u, \qquad d\mu = \rho(x)\,dx,
$$

then

$$
P^*v = \sum_{|\alpha|\le k} (-1)^{|\alpha|}\,\partial_\alpha^{\dagger}\bigl(A_\alpha(x)^* v\bigr),
$$

where $A_\alpha^*$ is the pointwise adjoint of the coefficient matrix with respect to the two fibrewise metrics, and $\partial_\alpha^{\dagger}$ is the formal adjoint of the monomial $\partial_\alpha$ with respect to the density $\rho\,dx$;

$$
\partial_i^{\dagger} = -\partial_i - \partial_i\log\rho,
$$

so that each $\partial_\alpha^{\dagger}$ is a differential operator of order $|\alpha|$, and $P^*$ is of order at most $k$.

*Proof.* It is enough to treat the operator $u\mapsto A(x)\,u$ of order zero and the operator $\partial_i$, because integration by parts composes. For the order-zero operator, $\int\langle Au,v\rangle\rho\,dx = \int\langle u, A^*v\rangle\rho\,dx$ with $A^*$ the pointwise adjoint, so $(A)^* = A^*$. For the derivative,

$$
\int\langle\partial_iu,v\rangle\rho\,dx = -\int\langle u,\partial_iv\rangle\rho\,dx - \int\langle u,v\rangle\,\partial_i\rho\,dx = \int\langle u,(-\partial_i-\partial_i\log\rho)v\rangle\rho\,dx,
$$

by the Leibniz rule $\partial_i(\rho\langle u,v\rangle) = \rho\langle\partial_iu,v\rangle + \rho\langle u,\partial_iv\rangle + \partial_i\rho\,\langle u,v\rangle$ and the fundamental theorem of calculus, the boundary term vanishing for compact support. Hence $\partial_i^{\dagger} = -\partial_i-\partial_i\log\rho$. Composing the transposes in reverse order gives the displayed formula, and each term is a differential operator of the stated order. Uniqueness: if $Q$ and $Q'$ are two formal adjoints, then $\langle u,(Q-Q')v\rangle_{L^2}=0$ for all compactly supported $u$ and $v$, which forces $Q=Q'$ by the fundamental lemma of the calculus of variations, the localisation of the pairing.

### The Boundary Term

**Theorem (Lagrange identity).** For $P$ of order at most $k$ and sections $u,v$,

$$
\langle v, Pu\rangle - \langle u, P^*v\rangle = \operatorname{div} W(u,v)
$$

for a vector field $W(u,v)$ depending smoothly and bilinearly on $u$, $v$ and their derivatives up to order $k-1$, the divergence being taken with respect to the density $d\mu$. Integrating over a compact region $\Omega$ with smooth boundary and applying the divergence theorem,

$$
\int_\Omega \langle v, Pu\rangle\,d\mu - \int_\Omega \langle u, P^*v\rangle\,d\mu = \int_{\partial\Omega}\langle W(u,v), \nu\rangle\,dS,
$$

the **Green formula**, whose right-hand side is the boundary term. The formal adjoint is therefore the adjoint on the compactly supported sections exactly when the boundary term vanishes, which is the origin of the boundary conditions of the global theory.

*Proof.* The difference $\langle v,Pu\rangle-\langle u,P^*v\rangle$ is, by the computation of the previous theorem, a sum of terms each of which is a total divergence: the integration by parts was performed by writing each term $\langle A_\alpha\partial_\alpha u,v\rangle\rho$ as $\partial(\cdots) + \langle u,(\cdots)\rangle\rho$, and the total derivatives collect into the divergence of a single vector field $W$. The Green formula is the divergence theorem of *Differential Forms and Stokes' Theorem*, with the boundary measure $dS$ and the outer normal $\nu$.

## The Symbol of the Adjoint

**Proposition.** The formal adjoint has the same order as $P$ and its principal symbol is the adjoint of the symbol of $P$ with the sign $(-1)^k$:

$$
\sigma_k(P^*)(x,\xi) = (-1)^k\,\sigma_k(P)(x,\xi)^* \ : \ F_x \longrightarrow E_x,
$$

the adjoint being taken with respect to the fibrewise metrics; consequently $P$ and $P^*$ have the same characteristic variety and $P$ is elliptic exactly when $P^*$ is.

*Proof.* The transposition of the local expression $\sum_{|\alpha|\le k}A_\alpha\partial_\alpha$ reverses the order of the factors and sends each top-order derivative $\partial_\alpha$ to $(-1)^{|\alpha|}\partial_\alpha$ up to lower-order terms, which are produced by the derivatives of the density and of the coefficients; the contributions to order $k$ come only from $|\alpha|=k$, and the density contributes a zeroth-order term. Hence the symbol of the adjoint is the adjoint matrix with the sign $(-1)^k$; the lower-order terms do not affect it. The characteristic variety is the zero set of the determinant of the symbol, which is transported to its adjoint with the same dimension and the same invertibility.

## Formally Self-Adjoint Operators

**Definition.** The operator $P$ is **formally self-adjoint** if $P^* = P$; it is **formally skew-adjoint** if $P^* = -P$, and **formally normal** if $P^*P = PP^*$. Its formal self-adjointness is a condition on the coefficients read through the metrics and the density.

**Proposition.** A formally self-adjoint operator of order $k$ has

$$
\sigma_k(P)(x,\xi) = (-1)^k\,\sigma_k(P)(x,\xi)^*,
$$

so its principal symbol is Hermitian for $k$ even and skew-Hermitian for $k$ odd; in particular an elliptic formally self-adjoint operator of even order has a definite symbol.

*Proof.* Setting $P=P^*$ in the symbol formula of the previous proposition gives the display; a matrix equal to $(-1)^k$ times its adjoint is Hermitian or skew-Hermitian according to the parity of $k$. For the ellipticity statement, the symbol of a second-order formally self-adjoint operator is a Hermitian matrix, whose determinant vanishes exactly where an eigenvalue vanishes, so the definiteness off the zero section is a nondegeneracy condition.

**Examples.** The **Sturm–Liouville operator** on an interval with the density $dx$ is

$$
Lu = -(p\,u')' + qu, \qquad p, q \ \text{real},
$$

and it is formally self-adjoint: $L^* = L$, because the two integrations by parts over the second-order term return the operator and the first-order terms cancel against the derivative of $p$. The **Laplace–Beltrami operator** $\Delta = -\operatorname{div}\nabla$ (equivalently $d\delta+\delta d$ on functions and the Laplace–de Rham operator on forms) is formally self-adjoint for the metric density, and it is the elliptic second-order self-adjoint operator of the corpus. The **divergence** $\operatorname{div}$, read as a map from the fields to the functions, has formal adjoint $-\nabla$, the negative gradient, read as the map from the functions to the fields; the pairing of the two is the Green formula of the vector calculus. The **exterior derivative** $d$ on forms has formal adjoint $\delta$, the codifferential of *The Codifferential*.

**Example (a nonsymmetric operator).** Let $X$ be a vector field and let $Pu = Xu = du(X)$ be the directional derivative, acting on functions with the metric density. Its formal adjoint is

$$
P^*v = -Xv - (\operatorname{div}X)\,v,
$$

because the integration by parts against the density produces the divergence term; hence $P$ is skew-adjoint exactly when $X$ is divergence-free, and it is not symmetric in general. The density correction is visible in the formula, and it shows that the formal adjoint depends on the density and not only on the operator's principal part.

## The Dirichlet Form and the Variational Reading

**Definition.** For a formally self-adjoint operator $P$ the **quadratic form** (or **Dirichlet form**) is

$$
Q(u) = \langle Pu, u\rangle_{L^2} = \int_M \langle Pu, u\rangle\, d\mu,
$$

defined on the compactly supported sections; it is real when the fibrewise metrics and the operator are real, and it is the object from which the variational characterisation of the eigenvalues and the weak solutions proceeds.

**Proposition.** For a formally self-adjoint second-order operator $P = -\nabla^*\nabla + V$ with $V$ self-adjoint, the quadratic form is

$$
Q(u) = \lVert\nabla u\rVert_{L^2}^2 + \langle Vu, u\rangle_{L^2} = \int_M\bigl(\lvert\nabla u\rvert^2 + \langle Vu,u\rangle\bigr)\,d\mu,
$$

which is the energy form of the operator; the operator is nonnegative, $P \geq 0$, when $V \geq 0$, and the association of the operator with the form is the content of the **Dirichlet principle**.

*Proof.* Integrate $\langle\nabla^*\nabla u,u\rangle = \langle\nabla u,\nabla u\rangle$ by parts, which is the adjointness of $\nabla$ and $-\nabla^*$; the identity is the metric-compatibility of the connection and the definition of $\nabla^*$ as the formal adjoint of $\nabla$. The positivity and the variational reading are then immediate from the display.

**Remark (formal versus global).** The formal adjoint is defined by the pairing of the compactly supported sections and is a differential operator; the **$L^2$ adjoint** is the adjoint of the closed unbounded operator on the Hilbert space $L^2$, whose domain carries the boundary conditions and whose existence requires the completeness of the space. The two agree on the overlap of their domains, and the difference is exactly the boundary term of the Lagrange identity; the passage from the one to the other, the domains, the closedness and the self-adjointness of the Laplace-type operators are *The L2 Adjoint of a Differential Operator*, the next entry of this group.

## Summary

The formal adjoint of a differential operator is defined by the integration-by-parts identity $\int\langle Pu,v\rangle d\mu=\int\langle u,P^*v\rangle d\mu$ for compactly supported sections; it exists, is unique, has the same order as the operator, and its local form is the transposed expression $\sum(-1)^{|\alpha|}\partial_\alpha^{\dagger}(A_\alpha^*v)$ with the density correction $\partial_i^{\dagger}=-\partial_i-\partial_i\log\rho$ in each derivative. The difference $\langle v,Pu\rangle-\langle u,P^*v\rangle$ is the divergence of a vector field, the Lagrange identity, which integrates to the boundary term of Green's formula; the formal adjoint is the true adjoint on the compactly supported sections exactly when the boundary term vanishes, which is the origin of the boundary conditions of the global theory.

The symbol of the adjoint is $\sigma_k(P^*)(\xi)=(-1)^k\sigma_k(P)(\xi)^*$, so the characteristic variety and the ellipticity are preserved; a formally self-adjoint operator has a Hermitian symbol for even order and a skew-Hermitian one for odd order. The Sturm–Liouville operator, the Laplace–Beltrami operator, the divergence/gradient pair and the exterior derivative/codifferential pair are the examples; the quadratic form $\langle Pu,u\rangle$ is the Dirichlet form and the energy of the operator. The global $L^2$ adjoint, with its domain and boundary conditions, is the subject of the next entry.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $d\mu = \rho\,dx$ | Density; the integration measure of the pairing |
| $\langle\cdot,\cdot\rangle_E$, $\langle\cdot,\cdot\rangle_F$ | Fibrewise inner products on the bundles |
| $\langle u,v\rangle_{L^2} = \int_M\langle u,v\rangle\,d\mu$ | Pairing of compactly supported sections |
| $P^*$ | Formal adjoint; $\langle Pu,v\rangle_{L^2}=\langle u,P^*v\rangle_{L^2}$ |
| $A_\alpha^*$, pointwise adjoint | Adjoint of the coefficient matrix for the fibrewise metrics |
| $\partial_i^{\dagger}=-\partial_i-\partial_i\log\rho$ | Formal adjoint of a derivative with respect to the density |
| $P^*v=\sum(-1)^{\lvert\alpha\rvert}\partial_\alpha^{\dagger}(A_\alpha^*v)$ | Local formula for the formal adjoint |
| $\langle v,Pu\rangle-\langle u,P^*v\rangle=\operatorname{div}W$ | Lagrange identity |
| $\int_\Omega(\langle v,Pu\rangle-\langle u,P^*v\rangle)=\int_{\partial\Omega}\langle W,\nu\rangle\,dS$ | Green formula; the boundary term |
| $\sigma_k(P^*)(\xi)=(-1)^k\sigma_k(P)(\xi)^*$ | Symbol of the adjoint; ellipticity preserved |
| Formally self-adjoint, skew-adjoint, normal | $P^*=P$; $P^*=-P$; $P^*P=PP^*$ |
| $Q(u)=\langle Pu,u\rangle_{L^2}$ | Dirichlet form; energy of a self-adjoint operator |

## Further Reading

- Michael E. Taylor, *Partial Differential Equations*, vol. I (Springer, 2nd ed. 2011), for the formal adjoint, the integration by parts and the boundary terms.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators*, vol. III (Springer, 1985), for the algebra of the differential operators, the transposition and the symbol of the adjoint.
- Gerald B. Folland, *Introduction to Partial Differential Equations*, 2nd ed. (Princeton University Press, 1995), for the formal adjoint, the Lagrange identity and the Green formula.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics*, vol. I (Interscience, 1953), for the Dirichlet form, the variational reading and the boundary conditions.
- Elias M. Stein and Rami Shakarchi, *Real Analysis* (Princeton University Press, 2005), for the integration by parts on smooth domains and the divergence theorem.
