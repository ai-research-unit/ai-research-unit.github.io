# __The Adjoint Boundary Condition__

## Introduction

A boundary condition is a constraint on the boundary data, and the adjoint condition is the constraint obtained by pairing: the boundary form of the operator is a nondegenerate skew-Hermitian pairing of the boundary data, the admissible subspace of a condition is a subspace $M$ of the boundary space, and the **adjoint condition** is the annihilator of $M$ under that pairing. The problem is self-adjoint exactly when $M$ equals its annihilator, that is, when $M$ is **Lagrangian**: isotropic for the boundary form and of half the dimension, the largest possible for a nondegenerate skew form. The construction settles the questions left open in the preceding articles: it produces the adjoint condition of an arbitrary boundary-value problem, it explains why a self-adjoint condition determines half the boundary data, and it reduces self-adjointness to a single algebraic condition on a finite-dimensional space.

This article reads the boundary-value problem with the conjugation and builds the adjoint condition as an operator-level object. It fixes the boundary data, the boundary space and the boundary form as a pairing; proves that the adjoint of a problem $(L,B)$ is the problem $(L^{\dagger},B^{*})$ with $B^{*}$ the annihilator of the boundary subspace; proves that a formally self-adjoint operator under the condition $B$ is self-adjoint exactly when the boundary subspace is Lagrangian; describes the Lagrangian subspaces and their parameterisation; and works out the Sturm–Liouville case, where the boundary space is four-dimensional, the form is the classical bracket, and the Lagrangian subspaces are the separated and the coupled self-adjoint conditions.

The boundary data, the trace and the boundary operator are *Differential Operators* and *Sobolev Spaces and Weak Solutions*; the boundary form and the skew-Hermitian property are *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*; the Green formula that produces it is *The Lagrange Identity and the Self-Adjoint System*; the adjoint problem and the reciprocity are *The Adjoint Problem and the Green Function*; the self-adjoint Sturm–Liouville operators are *Self-Adjoint Sturm–Liouville Operators*; the classical separated and periodic conditions are *The Sturm–Liouville Operator* and *Ordinary Differential Equations*; and the sesquilinear forms and the adjoint operator are *Sesquilinear Forms and the Weak Formulation of an Elliptic Problem* and *Banach and Hilbert Spaces*.

## The Boundary Data and the Boundary Space

**Definition.** Let $L$ be a differential operator of order $m$ on a bounded domain $\Omega$ with smooth boundary, and for $u$ of class $C^m$ on $\overline\Omega$ let

$$
\gamma u = \bigl(\gamma_0u,\gamma_1u,\dots,\gamma_{m-1}u\bigr),\qquad \gamma_ku = \partial_\nu^k u\big|_{\partial\Omega} ,
$$

be the **boundary data** of $u$, the traces of the normal derivatives of order at most $m-1$. The **boundary space** is the product

$$
\mathcal{B} = \prod_{k=0}^{m-1}H^{m-k-1/2}(\partial\Omega) ,
$$

a Hilbert space, and the trace $\gamma$ is a bounded map from $H^m(\Omega)$ onto $\mathcal{B}$.

**Definition.** The **boundary form** of $L$, written as a pairing of the boundary data, is

$$
\langle u,v\rangle_\partial = \langle\gamma u,\ \Sigma\,\gamma v\rangle_{\mathcal B} ,
$$

where $\Sigma$ is the matrix of the form in the boundary data: sesquilinear, skew-Hermitian when $L=L^{\dagger}$, and nondegenerate on $\mathcal B$. That $\Sigma$ is nondegenerate is the statement that the boundary form pairs the boundary data without a kernel, so that the annihilator construction below is symmetric.

**Definition.** A **boundary condition** is a closed subspace $M\subseteq\mathcal B$, its admissible subspace being $\mathcal{A}=\{u\in H^m(\Omega) : \gamma u\in M\}$; a condition given by $B\gamma u=0$ with a boundary operator $B$ has $M=\ker B$. The **annihilator** of $M$ under the boundary form is

$$
M^{\perp} = \{w\in\mathcal B : \langle m,\Sigma w\rangle_{\mathcal B}=0 \ \text{for every } m\in M\} ,
$$

and the **adjoint boundary condition** is the condition whose boundary subspace is $M^{\perp}$.

## The Adjoint Condition

**Theorem (the adjoint of a boundary-value problem).** Let $L$ be a differential operator with smooth coefficients and let $B$ be a boundary condition with boundary subspace $M$. Then the realisation of $L$ under $B$ has the adjoint realisation of $L^{\dagger}$ under $B^{*}$, where $B^{*}$ is the boundary condition with subspace $M^{\perp}$:

$$
(L,B)^{*} = (L^{\dagger},B^{*}) .
$$

*Proof.* The domain of the adjoint consists of the $v$ for which $u\mapsto\langle Lu,v\rangle$ is bounded by the norm on the admissible subspace. By the Green formula, $\langle Lu,v\rangle=\langle u,L^{\dagger}v\rangle+\langle u,v\rangle_\partial$; the first term is controlled by $L^{\dagger}v$ and the second by the boundary data, so the boundedness is the simultaneous requirement $L^{\dagger}v\in L^2$ and $\langle m,\Sigma\gamma v\rangle=0$ for every $m\in M$, that is $\gamma v\in M^{\perp}$; the action of the adjoint is $L^{\dagger}v$.

**Theorem (the self-adjointness criterion).** Let $L$ be formally self-adjoint, $L=L^{\dagger}$. Then the realisation of $L$ under $B$ is self-adjoint if and only if

$$
M^{\perp} = M ,
$$

that is, if and only if $M$ is isotropic for the boundary form and of half the dimension of $\mathcal{B}$; such a subspace is **Lagrangian**, and the condition is **self-adjoint**.

*Proof.* By the preceding theorem the adjoint problem has the boundary subspace $M^{\perp}$; the realisation is self-adjoint exactly when the adjoint problem coincides with the problem, which for $L=L^{\dagger}$ is the equality of the boundary subspaces $M^{\perp}=M$. In a nondegenerate skew-Hermitian form the equality $M=M^{\perp}$ holds exactly when $M\subseteq M^{\perp}$ and $\dim M=\dim M^{\perp}=\tfrac12\dim\mathcal B$; the isotropy is $M\subseteq M^{\perp}$ and the dimension condition is the maximality.

**Theorem (the Lagrangian subspaces).** The maximal isotropic subspaces of a nondegenerate skew-Hermitian form on a space $\mathcal B$ have dimension $\tfrac12\dim\mathcal B$, they exist, and they are parameterised by the unitary operators of the space; the graph of every unitary relative to a Lagrangian splitting is Lagrangian, and every Lagrangian subspace arises this way.

*Proof.* Existence is by induction on the dimension, pairing a vector $e$ with a vector $f$ with $\langle e,\Sigma f\rangle\neq0$ and splitting off the hyperbolic plane spanned by $e,f$; the parameterisation is the standard correspondence between the Lagrangian subspaces and the unitaries of the associated Hermitian form, obtained by writing a Lagrangian subspace as the graph of a map from one Lagrangian subspace to another and observing that the isotropy is the isometry of the map. The construction is that of the Lagrangian Grassmannian, and for a real form the unitaries are the orthogonal matrices.

## The Sturm–Liouville Case

**Theorem (the boundary form and the boundary space).** For the Sturm–Liouville expression $\ell u=-(pu')'+qu$ on $(a,b)$ with real $p>0$ and real $q$, the boundary space is four-dimensional, $\gamma u=(u(a),(pu')(a),u(b),(pu')(b))$, and the boundary form is the classical bracket

$$
\langle u,v\rangle_\partial = \Bigl[u_1\bar v_2-u_2\bar v_1\Bigr]_a^b ,
$$

where $u_1=u$, $u_2=pu'$ are the components of the boundary data and $[\,\cdot\,]_a^b$ is the value at $b$ minus the value at $a$; the form is skew-Hermitian and nondegenerate in the four boundary values.

*Proof.* The bracket is $[p(u\bar v'-u'\bar v)]_a^b$ by *The Lagrange Identity and the Self-Adjoint System*, and $p(u\bar v'-u'\bar v)=u_1\bar v_2-u_2\bar v_1$ with $u_2=pu'$, $v_2=pv'$ and $p$ real; the nondegeneracy is that the determinant pairing of two vectors in $\mathbb C^2$ does not vanish identically.

**Theorem (the self-adjoint conditions).** The Lagrangian subspaces of the four-dimensional boundary space are exactly the self-adjoint boundary conditions of the Sturm–Liouville problem: they comprise the separated conditions

$$
\alpha_1u(a)+\alpha_2(pu')(a)=0,\qquad \beta_1u(b)+\beta_2(pu')(b)=0 ,
$$

with real $(\alpha_1,\alpha_2)$ and $(\beta_1,\beta_2)$ not both zero, and the coupled conditions, in which the boundary values at $a$ and at $b$ are related by a matrix whose graph is Lagrangian; the operator with such a domain is self-adjoint, and the classical Sturm–Liouville problems of *The Sturm–Liouville Operator* are the instances.

*Proof.* A separated condition at one endpoint singles out a one-dimensional subspace of that endpoint's two-dimensional data: if $(u_1,u_2)$ is parallel to $(\alpha_2,-\alpha_1)$ with $(\alpha_1,\alpha_2)$ real, then the endpoint form $u_1\bar v_2-u_2\bar v_1=\alpha_1\alpha_2(\bar st-t\bar s)$ vanishes for any two such vectors, so the subspace is isotropic and, being one-dimensional in a two-dimensional skew space, is maximal. A separated condition at $a$ and a separated condition at $b$ therefore give a two-dimensional isotropic subspace of the four-dimensional boundary space, which is Lagrangian because its dimension is half. A coupled condition is the graph of a form-preserving map between two Lagrangian subspaces, and its parameterisation is the previous theorem. The self-adjointness is the criterion, and the expansion is that of *Self-Adjoint Sturm–Liouville Operators*.

**Example (the self-adjoint conditions of the model problem).** For $\ell u=-u''$ on $(0,\pi)$ the boundary data are $(u(0),u'(0),u(\pi),u'(\pi))$ and the boundary form is $[u\bar v'-u'\bar v]_0^\pi$. The Dirichlet condition $u(0)=u(\pi)=0$ is Lagrangian and gives the eigenvalues $n^2$; the Neumann condition $u'(0)=u'(\pi)=0$ is Lagrangian and gives $n^2$, $n\ge0$; the periodic condition $u(0)=u(\pi)$, $u'(0)=u'(\pi)$ is the coupled Lagrangian condition spanned by the diagonal, and gives the full Fourier spectrum; and the Robin condition $u'(0)=\sigma u(0)$ with real $\sigma$, together with any Lagrangian condition at $\pi$, is Lagrangian. The problem $u'(0)=0$, $u(\pi)=0$ is Lagrangian as well, being separated with real coefficients; the problem $u'(0)=iu(0)$, with a nonreal coefficient, is not, and the corresponding operator is not self-adjoint.

## Summary

The boundary data of an operator of order $m$ are the traces of the normal derivatives up to order $m-1$, forming the boundary space $\mathcal B$; the boundary form pairs them through a nondegenerate skew-Hermitian matrix $\Sigma$, $\langle u,v\rangle_\partial=\langle\gamma u,\Sigma\gamma v\rangle$. A boundary condition is a subspace $M$ of the boundary space, and its adjoint is the annihilator $M^{\perp}$ under the form; the adjoint of the realisation $(L,B)$ is the realisation of $L^{\dagger}$ under the condition with subspace $M^{\perp}$. For a formally self-adjoint $L$ the realisation is self-adjoint exactly when $M=M^{\perp}$, that is, when $M$ is Lagrangian: isotropic with half the dimension of the boundary space. The Lagrangian subspaces exist, have the maximal isotropic dimension, and are parameterised by the unitary operators. In the Sturm–Liouville case the boundary space is four-dimensional and the form is the classical bracket $[u_1\bar v_2-u_2\bar v_1]_a^b$ with $u_2=pu'$; the Lagrangian subspaces are the separated conditions with real coefficients and the coupled conditions, the Dirichlet, Neumann, periodic and real Robin conditions among them, while a condition with a nonreal coefficient fails the Lagrangian test and the operator is not self-adjoint.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\gamma u=(\gamma_0u,\dots,\gamma_{m-1}u)$ | Boundary data (traces of normal derivatives) |
| $\mathcal B=\prod_kH^{m-k-1/2}(\partial\Omega)$ | Boundary space |
| $\Sigma$ | Matrix of the boundary form in the boundary data |
| $M$ | Boundary subspace of a condition |
| $M^{\perp}=\{w : \langle m,\Sigma w\rangle=0\}$ | Annihilator, the adjoint boundary condition |
| Lagrangian subspace | Isotropic subspace of half the dimension |
| $[u_1\bar v_2-u_2\bar v_1]_a^b$ | Classical bracket for Sturm–Liouville |
| $u_1=u,\ u_2=pu'$ | Components of the Sturm–Liouville boundary data |

## Further Reading

- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (McGraw–Hill, 1955), for the adjoint boundary conditions and the self-adjoint extensions of a Sturm–Liouville problem.
- Philip Hartman, *Ordinary Differential Equations* (Wiley, 2nd ed. 1982), for the boundary matrices and the separated and coupled conditions.
- Joachim Weidmann, *Spectral Theory of Ordinary Differential Operators* (Springer, 1987), for the boundary triplets and the Lagrangian parameterisation of the self-adjoint extensions.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the adjoint of an operator and the domains of the extensions.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness* (Academic Press, 1975), for the boundary conditions and the self-adjoint extensions of an operator.
- Michael E. Taylor, *Partial Differential Equations I* (Springer, 2nd ed. 2011), for the boundary operators, the trace and the adjoint boundary conditions.
