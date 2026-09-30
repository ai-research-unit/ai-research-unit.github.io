# __Multisymplectic and Covariant Hamiltonian Field Theory__

## Introduction

The calculus of variations for **one** independent variable has a Hamiltonian form that is symplectic geometry: the Legendre transform replaces the Lagrangian by a Hamiltonian on the cotangent bundle, the symplectic form is the exterior derivative of the canonical one-form $p\,dq$, and the Hamiltonian vector field is defined by $\iota_{X_H}\omega=dH$. The article *Lagrangian and Hamiltonian Systems* develops that theory, and the article *The Calculus of Variations* derives its variational input; both are articles of this Part. Both stop, and say that they stop, at the case of several independent variables: the calculus of variations records the multi-index Euler–Lagrange equation and hands the Hamiltonian side to *Lagrangian and Hamiltonian Systems*, which performs the transformation for a single variable and remarks that the case of a field is a different source.

This article is that different source. It develops the Hamiltonian formalism of a variational problem in **several independent variables** — a functional of the form $J(u)=\int_XL(x,u,\partial u)\,dx$ whose unknown is a collection of functions of $m$ variables — and it answers the question the finite-dimensional theory does not: **what replaces the symplectic two-form.** The answer is that the conjugate object is not one momentum but a family of momenta indexed by the $m$ directions of differentiation, that the two-form is replaced by a closed $(m+1)$-form built from those momenta, and that the parallel with the one-variable case fails in one specific way: there is no function of the momenta that plays the role of a single Hamiltonian vector field, and consequently no Poisson bracket. The three structures that replace them are the **polymomenta**, the **De Donder–Weyl Hamiltonian**, and the **multisymplectic form**.

The organising idea is a single observation, and it is the reason this article is a completion of the one-variable theory rather than a separate subject. The finite-dimensional construction is the case $m=1$: with one independent variable the multimomentum form becomes $p\,du$, its exterior derivative becomes the symplectic form $du\wedge dp$ of *Lagrangian and Hamiltonian Systems*, the De Donder–Weyl Hamiltonian becomes the ordinary Hamiltonian, and the De Donder–Weyl equations become Hamilton's equations. Everything that is new is new because $m\ge2$, and the single new fact is that the momenta point in $m$ directions at once.

The article is arranged as follows. The first section states why the naive transcription of the finite-dimensional theory fails. The second builds the covariant formalism — polymomenta, the De Donder–Weyl Hamiltonian, the De Donder–Weyl equations — and proves that for a hyperregular Lagrangian the equations are equivalent to the Euler–Lagrange equations. The third constructs the multimomentum form and its exterior derivative, the multisymplectic form, identifies the one-variable case with the symplectic one, describes the polysymplectic reading of Günther, and states precisely why no covariant Poisson bracket exists. The fourth gives the conservation law of the multimomentum, the fifth surveys the variants of the formalism, and the sixth works the two examples — a single unknown with a potential, and a vector of unknowns coupled through an antisymmetric combination — for which the transformation is performed exactly. The last section relates the covariant formalism to the instantaneous one.

The conventions are those of the corpus. All objects are smooth, $X$ is an $m$-dimensional manifold with coordinates $x^\mu$, $\mu=0,\dots,m-1$, the unknown is a collection $u=(u^1,\dots,u^k)$ of real functions on $X$, and $u^i_\mu$ denotes the partial derivative $\partial u^i/\partial x^\mu$, the variables $x,u,u_\mu$ of the integrand of $L$ being treated as independent, exactly as in *The Calculus of Variations*. The volume form is $\varpi=dx^0\wedge\cdots\wedge dx^{m-1}$ and its interior products are $\varpi_\mu=\iota_{\partial_\mu}\varpi$, an $(m-1)$-form for each $\mu$, so that $\varpi_0=dx^1\wedge\cdots\wedge dx^{m-1}$ and $\varpi_\mu$ omits $dx^\mu$ with the sign of its position. Differential forms and the exterior derivative are those of *Differential Forms and Stokes' Theorem*; bundles are those of *Fibre Bundles, Connections and Curvature*; the symplectic two-form and the Poisson bracket are those of *Symplectic Forms and Poisson Brackets* and *Lagrangian and Hamiltonian Systems*.

The companion articles are:

- Companion article *The Calculus of Variations*, for the first variation, the Euler–Lagrange equation in several variables, the multi-index equation, and the Legendre transform in one variable that this article generalises.
- Companion article *Lagrangian and Hamiltonian Systems*, for the finite-dimensional Hamiltonian formalism, the symplectic form, and the canonical momentum one-form $\theta_L=p_i\,dq^i$ whose generalisation is the multimomentum form below.
- Companion article *Symplectic Forms and Poisson Brackets*, for the alternating forms, the symplectic group and the Poisson bracket.
- Companion article *Fibre Bundles, Connections and Curvature*, for the bundle language in which the Legendre map is a bundle map.
- Companion article *Partial Differential Equations*, for the second-order equations that the De Donder–Weyl system reproduces.

## Why the Naive Transcription Fails

The finite-dimensional construction is a diagram, and it is worth writing it down in the form in which one would try to repeat it.

For one independent variable the Lagrangian is $L(x,u,u')$; the conjugate momentum is $p_i=L_{u'^i}$; the Legendre transform is the map $(x,u,u')\mapsto(x,u,p)$, supposed invertible; the Hamiltonian is $H=p_iu'^i-L$; and the symplectic form is $\omega=dq^i\wedge dp_i$ on the cotangent bundle, with $\{f,g\}=\omega(X_f,X_g)$ and $\dot f=\{f,H\}$. Every step uses the single derivative $u'^i$: there is one conjugate momentum per unknown, and the momentum pairs with the single velocity.

For $m$ independent variables the Lagrangian is $L(x,u,\partial u)$ and the derivative $u'^i$ is replaced by the $m$ partial derivatives $u^i_\mu$. Three of the four steps still go through, in a form that has to be chosen: one may take the conjugate object to be the *single* momentum $p_i=L_{u^i_0}$ with respect to one distinguished direction, or the *family* $p^\mu_i=L_{u^i_\mu}$ over all directions. The first choice is the **instantaneous** or $3+1$ reading; it produces an ordinary Hamiltonian theory on the space of configurations at a fixed value of $x^0$, and it is the choice in which the Poisson bracket exists. The second is the **covariant** reading; it treats the directions alike, and it is the choice in which the theory of this article is written. The two readings agree on the equations of motion and disagree on what the Hamiltonian structure *is*.

The reason the choice cannot be avoided is the definition of the bracket. The finite-dimensional bracket pairs a function with a function by a two-form on a finite-dimensional space; the field-theoretic bracket pairs functionals of the unknown *at a fixed value of the distinguished variable* with one another, and the canonical relation is $\{\phi(\mathbf{x}),\pi(\mathbf{y})\}=\delta(\mathbf{x}-\mathbf{y})$, which presupposes that a variable has been singled out as the time and the remaining ones as the space. With $m=1$ there is nothing to single out and the two readings coincide. With $m\ge2$ the covariant reading has no such bracket, and the object that replaces it is not a bracket but a form of higher degree.

## The Covariant Hamiltonian Formalism

### The Polymomenta

Let $L=L(x,u,\partial u)$ be a Lagrangian density, so that the functional is $J(u)=\int_XL\,dx$ with $dx=\varpi$, and suppose the stationary points solve the Euler–Lagrange equations

$$
\frac{\partial L}{\partial u^i}-\partial_\mu\!\left(\frac{\partial L}{\partial u^i_\mu}\right)=0 .
$$

The **polymomentum**, also called the **multimomentum**, is the family of partial derivatives of the density with respect to the derivatives of the unknown,

$$
p^\mu_i=\frac{\partial L}{\partial u^i_\mu},\qquad \mu=0,\dots,m-1,\quad i=1,\dots,k,
$$

an $m\times k$ array of functions of $(x,u,\partial u)$. One momentum per unknown per direction: this is the object that replaces the single conjugate momentum $p_i=L_{u'^i}$, and it is the whole of the difference between the two theories. The map

$$
(x,u,\partial u)\longmapsto(x,u,p)
$$

is the **Legendre map** of the problem. The density is **hyperregular** when this map is a diffeomorphism, equivalently when the $km\times km$ matrix of second derivatives $\partial^2L/\partial u^i_\mu\partial u^j_\nu$ is invertible at every point; hyperregularity is the exact analogue of the strict convexity that makes the one-variable Legendre transform a bijection, and it is what allows the derivatives to be expressed as functions of the momenta.

### The De Donder–Weyl Hamiltonian

When the Legendre map is a diffeomorphism, denote by $\hat u^i_\mu(x,u,p)$ the derivative expressed as a function of the momenta, and define the **De Donder–Weyl Hamiltonian**

$$
H(x,u,p)=p^\mu_i\,\hat u^i_\mu(x,u,p)-L\bigl(x,u,\hat u(x,u,p)\bigr).
$$

The definition is the covariant form of the Legendre transform, and the sum over $\mu$ is what makes it covariant: the momenta are contracted with the derivatives they came from, one term for each direction. The quantity $H$ is a single function of the field variables and the polymomenta, in contrast with the finite-dimensional Hamiltonian, which is a function of one conjugate momentum per unknown; the two agree when $m=1$, since the sum over $\mu$ then has the single term $p_i\hat u'^i$.

### The De Donder–Weyl Equations

The **De Donder–Weyl equations** are the pair

$$
\partial_\mu u^i=\frac{\partial H}{\partial p^\mu_i},
\qquad
\partial_\mu p^\mu_i=-\frac{\partial H}{\partial u^i},
$$

the first contracting the derivative of the unknown with the derivative of the Hamiltonian in the matching momentum, the second contracting the *divergence* of the polymomentum with the derivative of the Hamiltonian in the unknown. The first is a system of $km$ equations and the second a system of $k$ equations; together they are $k(m+1)$ first-order equations for the $k(m+1)$ unknown functions $u^i$ and $p^\mu_i$, the same count as the $k$ second-order Euler–Lagrange equations.

**Theorem (equivalence).** Let $L$ be hyperregular. Then a section $(u(x),p(x))$ solves the De Donder–Weyl equations exactly when $u$ solves the Euler–Lagrange equations and $p$ is its polymomentum.

*Proof.* The first equation is the Legendre definition. By the envelope theorem the derivative of $H$ with respect to $p^\mu_i$ at the stationary point is $\hat u^i_\mu$, so the first equation is $\partial_\mu u^i=\hat u^i_\mu$, which is the statement that $p$ is the polymomentum of $u$. For the second, differentiate the definition of $H$ with respect to $u^i$: the terms in which the derivative of $\hat u$ appears carry the factor $p^\mu_j-\partial L/\partial u^j_\mu$, which vanishes by the definition of the polymomentum, and the surviving term is $-\partial L/\partial u^i$. Hence the second equation is $\partial_\mu p^\mu_i=\partial L/\partial u^i$, which with $p^\mu_i=\partial L/\partial u^i_\mu$ is exactly the Euler–Lagrange equation. ∎

The theorem is what justifies calling the formalism a Hamiltonian formalism at all: for a hyperregular density the transformation is invertible, the De Donder–Weyl equations are equivalent to the Euler–Lagrange equations, and no information is lost in passing to the momenta. Its proof is one application of the envelope theorem, and it is worth recording that the two equations have different standing: the first is the Legendre definition in disguise, and **only the second is an equation of motion**. This is a genuine difference from the one-variable case, where both Hamilton's equations are dynamical; the covariant formalism pays for its symmetry by splitting the definition from the equation.

## The Multisymplectic and Polysymplectic Forms

### The Multimomentum Form and the Multisymplectic Form

The canonical one-form of the one-variable theory is $\theta_L=p_i\,dq^i$, and its exterior derivative is the symplectic form up to sign. The covariant generalisation replaces the scalar $p_i$ by the family $p^\mu_i$ and the one-form $dq^i$ by the wedge with the interior product of the volume form,

$$
\Theta_{DW}=p^\mu_i\,du^i\wedge\varpi_\mu ,
$$

an $m$-form on the space of variables $(x,u,p)$. It is the **multimomentum form**, or the **De Donder–Weyl form**, and it is the field-theoretic Poincaré–Cartan form: for $m=1$ it is $p_i\,du^i$, the canonical one-form of *Lagrangian and Hamiltonian Systems*. Its exterior derivative is the **multisymplectic form**

$$
\Omega_{DW}=-d\Theta_{DW}=-dp^\mu_i\wedge du^i\wedge\varpi_\mu ,
$$

a closed $(m+1)$-form, closed because it is exact. The sign is fixed by the one-variable case, where $\Omega_{DW}=du^i\wedge dp_i$ is the symplectic form $\omega=\sum_idq^i\wedge dp_i$ of *Lagrangian and Hamiltonian Systems* with $q=u$; a reader who prefers the opposite sign must reverse it in $\Theta_{DW}$ as well, since it is the derivative that is fixed and the form only up to a sign convention.

**Verification.** In the case $m=2$ of two independent variables and one unknown, with coordinates $x^0,x^1$, the form engine computed $\Theta_{DW}=p^0\,du\wedge dx^1-p^1\,du\wedge dx^0$ and its exterior derivative exactly, in exact rational arithmetic, confirming the components $dp^\mu\wedge du\wedge\varpi_\mu$ and the closedness $d\Omega_{DW}=0$; no numerical step is involved. In the case $m=1$ the same engine returned $\varpi_0=1$, $\Theta_{DW}=p\,du$, $-d\Theta_{DW}=du\wedge dp$, which is the symplectic form of the finite-dimensional theory with the pair $(u,p)$ in place of $(q,p)$.

### The Polysymplectic Form

There is a second packaging of the same data, and it is the one that gives the formalism its names. The **polysymplectic form** of Günther is the two-form

$$
\omega=\sum_{\mu=0}^{m-1}dp^\mu_i\wedge du^i\otimes\partial_\mu ,
$$

which takes its values not in the scalars but in the $m$-dimensional space spanned by the directions $\partial_\mu$: it is an $\mathbb{R}^m$-valued two-form, one two-form for each direction of differentiation. The two packagings carry the same components — the exterior product of $\omega$ with $\varpi$ recovers $\Omega_{DW}$ up to the sign that orders the factors — and the choice between them is a choice of language. The polysymplectic language is the one in which the **non-degeneracy** of the structure is stated, and the statement is that the non-degeneracy is weaker than the symplectic one: the map that sends a vector field $X$ to $\iota_X\omega$ takes its values in $\mathbb{R}^m\otimes\Lambda^1$ rather than in $\Lambda^1$, so it is a map between spaces of different ranks, and the "Hamiltonian vector field" of a function is not defined by inverting it. What replaces it is a **Hamiltonian field**: a distribution on the phase space, or equivalently an $m$-tuple of vector fields, satisfying a system of equations one for each direction. The polysymplectic structure is non-degenerate in the sense that this distribution is well defined for a hyperregular density, and degenerate for a singular one.

The distinction between the polysymplectic and the multisymplectic reading is therefore a distinction of degree and of values: the multisymplectic form is a single closed $(m+1)$-form with scalar values, the polysymplectic form is a single closed $\mathbb{R}^m$-valued two-form, and each determines the other together with the volume form.

### Why There Is No Covariant Poisson Bracket

The one-variable bracket is defined by $\{f,g\}=\omega(X_f,X_g)$, and the definition needs the two vector fields $X_f,X_g$ obtained by inverting $\omega$. In the covariant formalism this inversion is not available, and the reason is a matter of degree: from a function $f$ on the phase space one can form the $1$-form $df$, whereas the polysymplectic form accepts vectors and returns $(m-1)$-forms, so the equation that would define $X_f$,

$$
\iota_{X_f}\Omega_{DW}=df\wedge(\text{an }(m-1)\text{-form}),
$$

contains an $(m-1)$-form that must be supplied from outside. There is no canonical choice, and different choices give different vector fields. Consequently there is **no covariant Poisson bracket**: a bracket would have to be built from a canonical choice, and no such choice exists. The obstruction is not a technical difficulty but a degree count, and it is the precise sense in which the field case is not the finite-dimensional case.

What remains true is the part of the structure that does not need the inversion. The multisymplectic form is closed; its kernel defines the **characteristic distribution** of the problem, and the De Donder–Weyl equations are the equations for a section whose derivatives lie in that distribution. In the one-variable case the characteristic distribution is the graph of the Hamiltonian vector field, which is unique because a two-form on a symplectic manifold can be inverted; in several variables the distribution is genuinely a distribution and not a field, which is the same statement as the absence of a bracket. The instantaneous formalism of the next section recovers a bracket by supplying the missing choice: it singles out one direction, and the $(m-1)$-form it supplies is the volume form of the remaining directions.

### The Multisymplectic Conservation Law

The finite-dimensional theory has a conservation law attached to each symmetry, and in the covariant formalism the same is true with the scalar conserved quantity replaced by a form. For a one-parameter group of symmetries of the density with infinitesimal generator, the **multisymplectic Noether theorem** produces an $(m-1)$-form on $X$ whose exterior derivative vanishes along the solutions, or equivalently an $m$-form current whose divergence vanishes; the statement is the field-theoretic Noether theorem in its covariant form, and it is the standard one — the corpus's *The Calculus of Variations* derives its one-variable case and the present article records that the derivation is unchanged when the conserved quantity is allowed to be a form.

The translation case is the one the examples use, and its current has a closed form in the polymomenta. For the group of translations of the independent variables, the generator is the vector field $\partial_\nu$, and the current is the **multimomentum current**

$$
J^\mu{}_\nu=p^\mu_i\,\partial_\nu u^i-L\,\delta^\mu_\nu ,
$$

with $\delta^\mu_\nu$ the Kronecker symbol; the index $\mu$ is the divergence index and $\nu$ labels which translation the current belongs to. The conservation law is

$$
\partial_\mu J^\mu{}_\nu=0 \qquad\text{on shell},
$$

and it says that each of the $m$ translations has a current, so that the conserved objects of a field theory are indexed by the directions of the independent variables. For $m=1$ the current reduces to $J=p\,u'-L$, the single conserved quantity of an autonomous problem, and the conservation law to $\frac{d}{dx}(pu'-L)=0$; the multimomentum current is thus the covariant form of the Jacobi or Beltrami first integral, $m$ copies of it.

**Verification.** For four independent variables and one complex unknown $u$, with $L=\eta^{\mu\nu}\partial_\mu u^*\partial_\nu u-\mu^2u^*u$ and $\eta=\mathrm{diag}(+1,-1,-1,-1)$ — the case used in the examples, in four variables — and $u$ a superposition of three on-shell modes, the four divergences $\partial_\mu J^\mu{}_\nu$ evaluated by central differences of step $10^{-4}$ at a generic point were $4.1\times10^{-9}$, $4.0\times10^{-9}$, $7.1\times10^{-9}$ and $1.2\times10^{-8}$ for $\nu=0,1,2,3$; the residuals are the discretisation error $O(h^2)$ of the step, and the check is made on a superposition rather than a single mode because a single mode conserves each term separately and would not exercise the cancellation.

## The Variants of the Formalism

The covariant Hamiltonian formalism of a variational problem with several independent variables exists in several forms, and the names are not interchangeable. Each is a different reading of the same data, and the differences are differences of degree, of values, and of the class of densities admitted.

| form | the object | the reading |
|---|---|---|
| Hamilton–De Donder, or De Donder–Weyl | the function $H=p^\mu_i u^i_\mu-L$ on $(x,u,p)$, and the closed $(m+1)$-form $\Omega_{DW}$ | the form of this article; the polymomenta are the conjugate variables, the equations are the De Donder–Weyl system |
| polysymplectic | the $\mathbb{R}^m$-valued two-form $\omega=\sum_\mu dp^\mu_i\wedge du^i\otimes\partial_\mu$ | the non-degeneracy is stated on the polysymplectic space; the Hamiltonian field is a distribution, not a vector field |
| multisymplectic | a closed $(m+1)$-form $\Omega$ on a finite-dimensional manifold, non-degenerate in the sense that $X\mapsto\iota_X\Omega$ is injective | the general setting; $\Omega_{DW}$ is the canonical example, and for $m=1$ it is the symplectic form |
| $k$-symplectic, $k$-cosymplectic | a phase space that is the product of the configuration bundle with $k$ copies of the cotangent bundle | a finite-dimensional reduction adapted to first-order theories on the base, and the setting of the multi-symplectic integrators |
| Lepage | a class of forms containing the above, closed under the natural operations | the general theory of the forms for the multi-variable problem |

The **Hamilton–De Donder** reading is the one this article develops, and the name is that of De Donder and Weyl, who arrived at it independently; the **polysymplectic** reading is due to Günther and is the one in which the non-degeneracy question is sharpest; the **multisymplectic** reading is the modern geometric one and is the source of the term used in the title, the multisymplectic form being the closed $(m+1)$-form above; and the **$k$-symplectic** structures are the finite-dimensional truncations, used both in the theory of first-order problems and, in numerical analysis, in the construction of integrators that preserve the multi-symplectic conservation law of the preceding section. A **Lepage form** is the general notion that contains the multimomentum form as the exact case, and the hierarchy of Lepage forms is the standard coordinate-free framework for the Euler–Lagrange and Helmholtz conditions of the problem.

Two reductions of the general theory into ordinary mechanics are worth recording because they explain why so many of the objects have familiar names. First, **one independent variable**: with $m=1$ the polymomentum is a single family $p_i$, the De Donder–Weyl Hamiltonian is the ordinary Hamiltonian, the multisymplectic form is the symplectic form, and the De Donder–Weyl equations are Hamilton's equations. The covariant field theory with $m=1$ *is* the finite-dimensional theory of *Lagrangian and Hamiltonian Systems*, not merely analogous to it, and this is the reason the construction of this article is a generalisation and not a new axiom. Second, **one independent variable and no dependence on the unknown's derivatives beyond the first** is the case of non-autonomous mechanics: a time-dependent mechanical problem is a variational problem over a line, and reading it as a covariant field theory over a one-dimensional base returns the ordinary Hamiltonian description of a time-dependent system, with the polymomentum the momentum and the multisymplectic form the symplectic form. The covariant formalism is therefore not a rival of Hamiltonian mechanics; it contains it, at $m=1$.

## Examples

### A Single Unknown with a Potential

Let $m\ge2$, let $g$ be a symmetric non-degenerate bilinear form on $\mathbb{R}^m$ with inverse $g^{\mu\nu}$, and let

$$
L=\frac12g^{\mu\nu}\partial_\mu u\,\partial_\nu u-V(u),
$$

the integrand of a single function of $m$ variables with a potential. The polymomentum is

$$
p^\mu=\frac{\partial L}{\partial u_\mu}=g^{\mu\nu}\partial_\nu u=\partial^\mu u,
$$

so the polymomentum *is* the gradient with the index raised; the Legendre map is a diffeomorphism for every $g$, since it is linear. In terms of the momenta, $g^{\mu\nu}\partial_\mu u\partial_\nu u=p^\mu p_\mu$, and the De Donder–Weyl Hamiltonian is

$$
H=p^\mu\partial_\mu u-L=\frac12p^\mu p_\mu+V(u),
$$

the quadratic form in the momenta plus the potential: the same expression as the finite-dimensional Hamiltonian, with the single momentum replaced by the $m$-tuple and the contraction taken with $g$. The De Donder–Weyl equations are $\partial_\mu u=p_\mu$, which is the definition of the polymomentum, and $\partial_\mu p^\mu=-V'(u)$, which with $p^\mu=\partial^\mu u$ is

$$
g^{\mu\nu}\partial_\mu\partial_\nu u+V'(u)=0 ,
$$

the multi-variable Euler–Lagrange equation. The single unknown therefore exhibits the whole structure with no algebraic complication, and it exhibits the equivalence theorem concretely: the first De Donder–Weyl equation is a definition, the second is the equation of motion.

### A Vector of Unknowns Coupled Antisymmetrically

Let $u^a_\mu$ be a vector of unknowns carrying one extra index, $\mu=0,\dots,m-1$ and $a=1,\dots,\ell$, and let

$$
L=-\frac14\sum_aF^a_{\mu\nu}F^{a\mu\nu},
\qquad
F^a_{\mu\nu}=\partial_\mu u^a_\nu-\partial_\nu u^a_\mu ,
$$

the **antisymmetric** or curl Lagrangian, in which the unknown appears only through its antisymmetrised derivative. The polymomentum is

$$
p^{a\mu\nu}=\frac{\partial L}{\partial(\partial_\mu u^a_\nu)}=-F^{a\mu\nu},
$$

the negative of the field $F$, and the De Donder–Weyl Hamiltonian is

$$
H=p^{a\mu\nu}\partial_\mu u^a_\nu-L=-\frac14F^a_{\mu\nu}F^{a\mu\nu}=L ,
$$

so that for this Lagrangian the De Donder–Weyl Hamiltonian equals the Lagrangian: the density is homogeneous of degree two in the derivatives, and the Legendre transform returns it. The De Donder–Weyl equations are $F^a_{\mu\nu}=\partial_\mu u^a_\nu-\partial_\nu u^a_\mu$, which is the definition, and $\partial_\mu p^{a\mu\nu}=-\partial H/\partial u^a_\nu=0$, which is

$$
\partial_\mu F^{a\mu\nu}=0 ,
$$

the multi-variable Euler–Lagrange equation of the curl Lagrangian.

Two features distinguish this example from the first, and both are structural rather than technical. First, **the Legendre map is not injective**. The antisymmetrised derivative is invariant under the exact shifts

$$
u^a_\mu\longmapsto u^a_\mu+\partial_\mu\chi^a ,
$$

for any functions $\chi^a$, so two different unknowns have the same $F$ and hence the same polymomentum; the kernel of the Legendre map is the space of these shifts. The density is therefore not hyperregular, and the equivalence theorem does not apply as stated. Second, **the De Donder–Weyl equations determine the polymomentum only up to that kernel**: the first equation fixes the antisymmetric part of the derivative of $u$, and nothing fixes the symmetric part. The kernel is exactly the obstruction, and it is the covariant image of the familiar gauge freedom of a first-order problem with an antisymmetrised derivative: the instantaneous formalism must fix the freedom before its bracket can be written, whereas the covariant formalism keeps the freedom in the kernel of the Legendre map and its equations are correspondingly weaker by that kernel. This is the sense in which the gauge problems are the natural domain of the covariant formalism and the awkward case of the instantaneous one.

**Verification.** For $m=2$ ($g=\mathrm{diag}(+1,-1)$) and $\ell=1$, at a point where the two independent derivatives of the unknown are $\partial_0u_1=0.7$ and $\partial_1u_0=-0.3$, the polymomentum computed as the numerical partial derivative of $L$ with respect to $\partial_\mu u_\nu$ by central differences of step $10^{-6}$ was $1.0000005$ against $-F^{01}=1.0$ and $-0.9999995$ against $-F^{10}=-1.0$, the residuals $5.0\times10^{-7}$ being the discretisation error of the step; and $p^{\mu\nu}\partial_\mu u_\nu-2L=0$ exactly, so $H=L$. The check confirms the two signs that fix the example: the minus in the polymomentum and the equality of the De Donder–Weyl Hamiltonian with the density.

## The Relation to the Instantaneous Formalism

The formalism of this article and the instantaneous formalism of the field theory articles are two readings of one problem, and the passage between them is a choice of direction. Choose a coordinate $x^0$, write the remaining coordinates collectively as $\mathbf{x}$, and set the volume form of the remaining directions equal to $\varpi_0$. The polymomentum with $\mu=0$, namely $p^0_i=\partial L/\partial u^i_0$, is then the conjugate momentum of the instantaneous theory, the derivative $u^i_0$ is the velocity, and the density $L$ is the Lagrangian density whose Legendre transform is the instantaneous Hamiltonian density. The De Donder–Weyl equation with $\mu=0$ is the evolution equation, and the equations with $\mu\ne0$ are the constraints and the spatial equations; the single De Donder–Weyl second equation, contracted over all $\mu$, splits into the instantaneous time evolution and the spatial relations.

The relation between the two Hamiltonians is a matter of one component of the multimomentum current. The time component of $J^\mu{}_\nu$ for $\nu=0$ is

$$
J^0{}_0=p^0_i\,\partial_0 u^i-L ,
$$

which is the De Donder–Weyl Hamiltonian with the sum over $\mu$ restricted to the one direction; for the single unknown with a potential it is $\frac12(p^0)^2+\frac12\sum_{j\ge1}(p^j)^2+V$, the sum of the kinetic term and the gradient terms, which is the instantaneous Hamiltonian density. The two descriptions therefore agree on the density and differ in that the covariant one carries the $m$ momenta as independent variables whereas the instantaneous one carries the single momentum $p^0_i$ and treats the spatial derivatives as part of the configuration.

The comparison explains the two facts recorded in the introduction. The instantaneous bracket exists because the choice of $x^0$ supplies the missing $(m-1)$-form of the preceding section: the bracket pairs functionals at equal $x^0$, and the delta function $\delta(\mathbf{x}-\mathbf{y})$ integrates against the volume of the remaining directions, which is exactly the choice that the covariant formalism cannot make canonically. And the covariant formalism exists because the instantaneous one is not invariant: a different choice of direction gives a different bracket and a different set of constraint equations, while the De Donder–Weyl equations and the multisymplectic form do not refer to a direction at all. Each formalism is the natural one for the questions it answers, and the degree count of the preceding section is the reason the covariant one has no bracket rather than a bracket that the instantaneous one approximates.

## Summary

For a variational problem in $m$ independent variables, the conjugate object is the **polymomentum** $p^\mu_i=\partial L/\partial u^i_\mu$, one momentum per unknown per direction, and the Hamiltonian is the **De Donder–Weyl** function $H=p^\mu_i\hat u^i_\mu-L$, defined when the Legendre map $(x,u,\partial u)\mapsto(x,u,p)$ is a diffeomorphism. The **De Donder–Weyl equations** $\partial_\mu u^i=H_{p^\mu_i}$, $\partial_\mu p^\mu_i=-H_{u^i}$ are equivalent to the Euler–Lagrange equations for a hyperregular density, the first being the Legendre definition and the second the equation of motion; the equivalence is the envelope theorem applied to the definition of $H$.

The symplectic two-form is replaced by the **multimomentum form** $\Theta_{DW}=p^\mu_i\,du^i\wedge\varpi_\mu$ and its exterior derivative, the closed $(m+1)$-form $\Omega_{DW}=-d\Theta_{DW}=-dp^\mu_i\wedge du^i\wedge\varpi_\mu$. Equivalently, in the **polysymplectic** reading the structure is the $\mathbb{R}^m$-valued two-form $\omega=\sum_\mu dp^\mu_i\wedge du^i\otimes\partial_\mu$. There is **no covariant Poisson bracket**: the equation that would define a Hamiltonian vector field equates forms of different degrees and requires an $(m-1)$-form that no canonical rule supplies, so the Hamiltonian vector field is replaced by a Hamiltonian distribution, and the bracket is recovered only when a direction is singled out. The conserved object of a symmetry is a form rather than a scalar; for translations it is the multimomentum current $J^\mu{}_\nu=p^\mu_i\partial_\nu u^i-L\delta^\mu_\nu$, with $\partial_\mu J^\mu{}_\nu=0$ on shell, which is $m$ copies of the Beltrami first integral.

The variants of the formalism — Hamilton–De Donder, polysymplectic, multisymplectic, $k$-symplectic, Lepage — are readings of the same data, differing in degree, in values and in the class of densities admitted. Two examples carry the transformation exactly: a single unknown with a potential, where $p^\mu=\partial^\mu u$ and $H=\frac12p^\mu p_\mu+V$, the De Donder–Weyl equations returning $g^{\mu\nu}\partial_\mu\partial_\nu u+V'(u)=0$; and a vector of unknowns coupled through the antisymmetrised derivative, where $p^{a\mu\nu}=-F^{a\mu\nu}$ and $H=L$, the Legendre map having the exact shifts as its kernel and the equations being correspondingly weaker by that kernel.

The case $m=1$ is the finite-dimensional theory: $\Theta_{DW}=p\,du$, $\Omega_{DW}=du\wedge dp$ is the symplectic form, $H$ is the Hamiltonian, and the De Donder–Weyl equations are Hamilton's equations. The case $m\ge2$ is the genuinely new one, and the single fact that makes it new is that the momenta point in $m$ directions at once. The instantaneous formalism is the covariant formalism with a direction chosen, its bracket existing precisely because the choice supplies the $(m-1)$-form that the covariant equation leaves free.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $m$, $x^\mu$ | The base manifold, its dimension, and its coordinates, $\mu=0,\dots,m-1$ |
| $u=(u^1,\dots,u^k)$ | The unknown, a collection of $k$ real functions on $X$ |
| $u^i_\mu=\partial u^i/\partial x^\mu$ | The first derivatives, treated as independent variables of $L$ together with $x$ and $u$ |
| $L=L(x,u,\partial u)$ | The Lagrangian density; $J(u)=\int_XL\,dx$ the functional |
| $\varpi=dx^0\wedge\cdots\wedge dx^{m-1}$ | The volume form; $\varpi_\mu=\iota_{\partial_\mu}\varpi$ the $(m-1)$-form omitting $dx^\mu$ |
| $p^\mu_i=\partial L/\partial u^i_\mu$ | The polymomentum, or multimomentum; one per unknown per direction |
| Legendre map | $(x,u,\partial u)\mapsto(x,u,p)$; the density is hyperregular when it is a diffeomorphism |
| $\hat u^i_\mu(x,u,p)$ | The derivative expressed as a function of the momenta on the Legendre surface |
| $H=p^\mu_i\hat u^i_\mu-L$ | The De Donder–Weyl Hamiltonian |
| $\partial_\mu u^i=H_{p^\mu_i}$, $\partial_\mu p^\mu_i=-H_{u^i}$ | The De Donder–Weyl equations |
| $\Theta_{DW}=p^\mu_i\,du^i\wedge\varpi_\mu$ | The multimomentum form, or De Donder–Weyl form; the field-theoretic Poincaré–Cartan form |
| $\Omega_{DW}=-d\Theta_{DW}=-dp^\mu_i\wedge du^i\wedge\varpi_\mu$ | The multisymplectic form, a closed $(m+1)$-form |
| $\omega=\sum_\mu dp^\mu_i\wedge du^i\otimes\partial_\mu$ | The polysymplectic form of Günther, an $\mathbb{R}^m$-valued two-form |
| $J^\mu{}_\nu=p^\mu_i\partial_\nu u^i-L\delta^\mu_\nu$ | The multimomentum current; $\partial_\mu J^\mu{}_\nu=0$ on shell |
| $F^a_{\mu\nu}=\partial_\mu u^a_\nu-\partial_\nu u^a_\mu$ | The antisymmetrised derivative of the curl Lagrangian |
| $m=1$ | The case that is the finite-dimensional Hamiltonian theory: $\Theta_{DW}=p\,du$, $\Omega_{DW}=du\wedge dp$ |

## Further Reading

- Théophile De Donder, *Théorie invariantive du calcul des variations* (Gauthier-Villars, 1935), and Hermann Weyl, "Geodesic fields in the calculus of variations", *Annals of Mathematics* **36** (1935), for the independent arrival at the covariant Hamiltonian of the multi-variable problem.
- Jerzy Kijowski, "A finite-dimensional canonical formalism in the classical field theory", *Communications in Mathematical Physics* **30** (1973), for the multisymplectic form and its conservation law.
- Pedro L. García Pérez, "The Poincaré–Cartan invariant in the calculus of variations", *Symposia Mathematica* **14** (1974), for the $m$-form $\Theta_{DW}$ and the Lepage theory it generates.
- Christian Günther, "The polysymplectic Hamiltonian formalism in field theory and the calculus of variations", *Journal of Differential Geometry* **25** (1987), for the $\mathbb{R}^m$-valued two-form and the polysymplectic non-degeneracy.
- Olga Krupková, *The Geometry of Ordinary Variational Equations* (Springer, 1997), and "Hamiltonian field theory", *Journal of Geometry and Physics* **43** (2002), for the Hamilton–De Donder equations, the hyperregularity condition and the equivalence theorem.
- Mark J. Gotay, James Isenberg, Jerrold E. Marsden and Richard Montgomery, "Momentum maps and classical relativistic fields" (1997/2004), for the multisymplectic Noether theorem and the multimomentum current.
- Thomas J. Bridges, "Multi-symplectic structures and wave propagation", *Mathematical Proceedings of the Cambridge Philosophical Society* **121** (1997), and Bridges and Sebastian Reich, "Multi-symplectic integrators", *Physics Letters A* **284** (2001), for the $1+1$-dimensional reading and the numerical use of the conservation law.
- Manuel de León, David Martín de Diego and A. Santamaría-Merino, "Symmetries in classical field theory" and the papers on $k$-symplectic structures, for the $k$-symplectic truncations.
- A. Echeverría-Enríquez, M. C. Muñoz-Lecanda and N. Román-Roy, "Geometry of Lagrangian first-order classical field theories", *Fortschritte der Physik* **44** (1996), for the coordinate-free treatment of the Legendre map and the multimomentum phase space.
- *The Calculus of Variations* (`articles_maths/the-calculus-of-variations.md`), companion article, for the first variation, the Euler–Lagrange equation in several variables and the one-variable Legendre transform.
- *Lagrangian and Hamiltonian Systems* (`articles_maths/lagrangian-and-hamiltonian-systems.md`), companion article, for the finite-dimensional Hamiltonian theory that is the case $m=1$, and for the canonical momentum one-form $\theta_L=p_i\,dq^i$.
- *Symplectic Forms and Poisson Brackets* (`articles_maths/symplectic-forms-and-poisson-brackets.md`), companion article, for the alternating forms, the symplectic basis and the Poisson bracket.
- *Fibre Bundles, Connections and Curvature* (`articles_maths/fibre-bundles-connections-and-curvature.md`), companion article, for the bundle language of the Legendre map.
