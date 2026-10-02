# __Self-Adjoint Sturm–Liouville Operators__

## Introduction

The Sturm–Liouville expression $\ell u=-(pu')'+qu$ defines many operators, one for each boundary condition, and the self-adjoint ones are those built from its formal self-adjointness: the domain is a subspace of the maximal domain on which the boundary form vanishes. The construction is the operator form of the theory of the preceding group. The expression generates a **minimal operator** $T_0$, the closure of the restriction to the compactly supported test functions, and a **maximal operator** $T_1$, its adjoint; the self-adjoint operators between them are the operators $T$ with $T_0\subseteq T\subseteq T_1$ and $T=T^{*}$, and they are parameterised by the boundary conditions that make the classical bracket vanish. The regular case, in which all self-adjoint extensions come from boundary conditions at the two endpoints, has a compact resolvent and a discrete spectrum with a complete eigenfunction expansion in the weighted space; the singular case, in which an endpoint fails to be regular, is classified by the **limit-point** and **limit-circle** alternatives of Weyl, and no boundary condition is needed at a limit-point endpoint.

This article builds the self-adjoint Sturm–Liouville operators from the involution. It fixes the minimal and maximal operators and proves that the maximal is the adjoint of the minimal; identifies the self-adjoint extensions with the Lagrangian boundary conditions for the bracket; proves the compactness of the resolvent and the eigenfunction expansion in the regular case; states the limit-point and limit-circle classification and the self-adjoint conditions at a singular endpoint; and describes the spectrum, discrete in the regular case and with an essential part in the singular case.

The Sturm–Liouville expression, the weighted space and the classical eigenvalue theory are those of *The Sturm–Liouville Operator* and *Ordinary Differential Equations*; the form of the expression and the boundary form are *Differential Operators* and *The Lagrange Identity and the Self-Adjoint System*; the boundary form, the reality and the completeness are *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*; the adjoint operator and its domain are *The Adjoint Problem and the Green Function* and *The Adjoint Boundary Condition*; the spectral theorem for the self-adjoint realisation is *Self-Adjoint Elliptic Operators and the Spectral Theorem*; and the compactness of the resolvent is *The Green Operator* and *Sobolev Spaces and Weak Solutions*.

## The Minimal and Maximal Operators

**Definition.** Let $\ell u=-(pu')'+qu$ on an interval $(a,b)$ with real $p>0$, real $q$, and $1/p$, $q$ locally integrable. Let $w>0$ be the weight and $L^2_w(a,b)$ the weighted space. The **minimal operator** $T_0$ is the closure in $L^2_w(a,b)$ of the operator defined on $C_c^\infty(a,b)$ by $\ell$; the **maximal operator** $T_1$ is the restriction of $\ell$, read in the distributional sense, to the set of $u\in L^2_w$ with $\ell u\in L^2_w$.

**Theorem (the adjoint of the minimal operator).** The minimal operator is symmetric, $T_0\subseteq T_0^{*}$, and its adjoint is the maximal operator:

$$
T_0^{*} = T_1 .
$$

*Proof.* The symmetry of $T_0$ is the vanishing of the bracket on compactly supported functions, which have both boundary terms zero. For the adjoint, $v\in\mathrm{dom}\,T_0^{*}$ means that the functional $u\mapsto\langle T_0u,v\rangle$ is bounded on $C_c^\infty$; integrating by parts twice writes the pairing as $\langle u,\ell v\rangle$ plus boundary terms, and the boundedness for all $u$ forces $\ell v\in L^2_w$ and the boundary terms to vanish; hence $v\in\mathrm{dom}\,T_1$, and the two domains agree by the same computation in reverse.

**Theorem (self-adjointness and the bracket).** An operator $T$ with $T_0\subseteq T\subseteq T_1$ is self-adjoint if and only if its domain is the set of $u\in\mathrm{dom}\,T_1$ for which the boundary form vanishes against the domain,

$$
\langle u,v\rangle_\partial = \Bigl[p\,(u\bar v'-u'\bar v)\Bigr]_a^b = 0 \qquad \text{for all } u,v\in\mathrm{dom}\,T .
$$

The conditions defining such domains are the **self-adjoint boundary conditions**, and they are exactly the Lagrangian subspaces of the boundary form of *The Lagrange Identity and the Self-Adjoint System*.

*Proof.* For $u,v\in\mathrm{dom}\,T_1$, the Green formula of the interval gives $\langle\ell u,v\rangle-\langle u,\ell v\rangle=[p(u\bar v'-u'\bar v)]_a^b$. The adjoint $T^{*}$ of an operator $\mathcal{D}$ between $T_0$ and $T_1$ has the domain of the $v\in\mathrm{dom}\,T_1$ for which this bracket vanishes against every $u\in\mathcal{D}$; hence $T=T^{*}$ exactly when the bracket vanishes for all pairs in the domain, which is the stated condition. The Lagrangian description is that of the general theory of the boundary form.

## The Regular Case

**Definition.** The endpoint $a$ is **regular** if it is finite and $1/p$, $q$, $w$ are integrable near it; the problem is **regular** if both endpoints are regular. For a regular problem the boundary values $u(a),(pu')(a),u(b),(pu')(b)$ are defined and the bracket is a skew-Hermitian form in them.

**Theorem (the self-adjoint conditions of a regular problem).** For a regular Sturm–Liouville problem every self-adjoint extension is given by two separated conditions

$$
\alpha_1 u(a)+\alpha_2 (pu')(a)=0,\qquad \beta_1 u(b)+\beta_2 (pu')(b)=0 ,
$$

with real pairs $(\alpha_1,\alpha_2)$, $(\beta_1,\beta_2)$ not both zero, or by a coupled condition whose boundary matrix satisfies the Lagrangian property; the resulting operator $T$ is self-adjoint, $T=T^{*}$, and its domain is

$$
\mathrm{dom}\,T = \Bigl\{u\in L^2_w : u,u'\in AC_{\mathrm{loc}},\ \ell u\in L^2_w,\ \text{the conditions hold at } a,b\Bigr\} .
$$

*Proof.* The bracket $[p(u\bar v'-u'\bar v)]_a^b$ is the sum of the two endpoint forms; a separated condition at each endpoint makes each endpoint form vanish because the pair $(u,(pu'))$ is parallel to $(\alpha_2,-\alpha_1)$, so the assembled vector is isotropic, and a coupled condition with a Lagrangian matrix makes the whole form vanish. The self-adjointness is the preceding theorem, and the domain is the maximal domain cut down by the conditions.

**Theorem (compact resolvent and the eigenfunction expansion).** Let the problem be regular and let $T$ be a self-adjoint extension. Then $T$ has a compact resolvent, its spectrum is discrete, real and simple, the eigenvalues $\lambda_1<\lambda_2<\cdots$ tend to infinity, and the eigenfunctions $\varphi_n$ are complete in $L^2_w(a,b)$:

$$
f=\sum_{n\ge1}\bigl(f,\varphi_n\bigr)_w\varphi_n , \qquad \|f\|_w^2=\sum_{n\ge1}\bigl|(f,\varphi_n)_w\bigr|^2 .
$$

*Proof.* The resolvent of a regular problem is the Green operator, which is compact on $L^2_w$ because it maps into a space of functions with an $L^2$ second derivative, compactly embedded by Rellich–Kondrachov; the compact self-adjoint spectral theorem of *Banach and Hilbert Spaces* then gives the orthonormal basis of eigenvectors, and the reality and the simplicity are those of the self-adjoint problem. The expansion is the expansion in that basis.

## The Singular Case

**Definition.** The endpoint $a$ is **singular** if it is infinite or if the coefficients fail to be integrable near it. The **limit-circle** and **limit-point** alternatives concern the number of solutions of $\ell u=\lambda u$ in $L^2_w(a,c)$: for a nonreal $\lambda$ that number is constant, and the endpoint is **limit-circle** if it is two and **limit-point** if it is one.

**Theorem (Weyl's classification).** For a formally self-adjoint Sturm–Liouville expression and a nonreal $\lambda$, the number of linearly independent solutions of $\ell u=\lambda u$ in $L^2_w$ near the endpoint $a$ is either one or two, independent of the nonreal $\lambda$; if it is one, the endpoint is limit-point, no boundary condition is needed there and the operator is essentially self-adjoint at that endpoint; if it is two, the endpoint is limit-circle, a boundary condition is needed, and the self-adjoint extensions are parameterised by the real boundary conditions of a one-dimensional family.

*Proof.* The solutions of $\ell u=\lambda u$ near a singular endpoint span a two-dimensional space, and the $L^2_w$ condition selects a subspace whose dimension is independent of $\lambda$ in the upper half-plane by the theory of the Weyl circle and the Weyl coefficient; the two cases are the two possibilities. At a limit-point endpoint the maximal and minimal domains require no boundary condition because only one solution is $L^2_w$, so the bracket vanishes automatically; at a limit-circle endpoint the two $L^2_w$ solutions make the bracket nontrivial and a one-parameter family of conditions is required. The detailed computation with the Weyl circles is that of *The Sturm–Liouville Operator* and *Ordinary Differential Equations*.

**Theorem (the expansion in the singular case).** For a self-adjoint singular Sturm–Liouville operator the spectrum is the union of the discrete eigenvalues and the essential spectrum, the eigenfunction expansion holds in the generalised sense with respect to a spectral measure $\rho$,

$$
f\sim\int_{\sigma(T)}\Bigl(\int f\varphi(x,w)\,w\,dx\Bigr)\varphi(\cdot,w)\,d\rho(w) ,
$$

and the measure $\rho$ is the Weyl–Titchmarsh measure of the problem; when the spectrum is discrete the integral is the sum of the regular expansion.

*Proof.* The self-adjoint operator has a spectral measure by the spectral theorem, and the generalised eigenfunctions $\varphi(\cdot,w)$ diagonalise it; the representation is the direct integral form of that theorem. The discrete case is the special case in which the spectral measure is a sum of atoms, which is the regular expansion above.

## Summary

A Sturm–Liouville expression $\ell u=-(pu')'+qu$ determines the minimal operator $T_0$, the closure on the compactly supported functions, and the maximal operator $T_1$, whose domain is the set of $L^2_w$ functions with $\ell u\in L^2_w$; the minimal operator is symmetric and $T_0^{*}=T_1$. The self-adjoint operators are the operators between them whose domain makes the classical bracket $[p(u\bar v'-u'\bar v)]_a^b$ vanish, that is, whose boundary conditions are Lagrangian for the boundary form; in the regular case they are given by separated or coupled boundary conditions, and the operator has a compact resolvent, a discrete real spectrum with eigenvalues going to infinity and a complete orthonormal eigenfunction expansion in $L^2_w$. At a singular endpoint the alternatives of Weyl apply: the endpoint is limit-point if only one solution of $\ell u=\lambda u$ is square-integrable there, in which case no boundary condition is needed and the endpoint is essentially self-adjoint, and limit-circle if two are, in which case a one-parameter family of boundary conditions is required. The self-adjoint singular operator has a discrete part and an essential part, and its eigenfunction expansion holds with respect to the Weyl–Titchmarsh spectral measure, the regular expansion being the discrete case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\ell u=-(pu')'+qu$ | Sturm–Liouville expression |
| $w$ | Weight, $L^2_w(a,b)$ the weighted space |
| $T_0$ | Minimal operator, closure on $C_c^\infty$ |
| $T_1$ | Maximal operator, adjoint of $T_0$ |
| $T$ | Self-adjoint extension, $T_0\subseteq T\subseteq T_1$, $T=T^{*}$ |
| $[p(u\bar v'-u'\bar v)]_a^b$ | Boundary form (classical bracket) |
| limit-point / limit-circle | One or two $L^2_w$ solutions at a singular endpoint |
| $\rho$ | Weyl–Titchmarsh spectral measure |
| $\lambda_n,\varphi_n$ | Eigenvalues and eigenfunctions in the regular case |

## Further Reading

- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (McGraw–Hill, 1955), for the minimal and maximal operators and the self-adjoint extensions.
- Philip Hartman, *Ordinary Differential Equations* (Wiley, 2nd ed. 1982), for the limit-point and limit-circle classification and the self-adjoint conditions.
- Hermann Weyl, *Über gewöhnliche Differentialgleichungen mit Singularitäten und die zugehörigen Entwicklungen willkürlicher Funktionen* (Mathematische Annalen 68, 1910), for the circle and point alternatives and the singular expansion.
- Edward C. Titchmarsh, *Eigenfunction Expansions Associated with Second-Order Differential Equations* (Oxford University Press, 2nd ed. 1962), for the spectral measure and the singular eigenfunction expansion.
- Joachim Weidmann, *Spectral Theory of Ordinary Differential Operators* (Springer, 1987), for the minimal and maximal operators, the self-adjoint extensions and the direct-integral expansion.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the self-adjoint extensions and the compact-resolvent argument.
