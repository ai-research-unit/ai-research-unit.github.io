
# __Hermitian Hilbert Modules over a Clifford Algebra__

## Introduction

The operators of Clifford analysis act on spaces of functions whose values lie in a Clifford module,
and the analytic theory needs those spaces to be Hilbert spaces and the module structure to be
compatible with the inner product. This article develops the resulting structure: a Clifford module
that is at the same time a Hilbert space, with a Hermitian form for which the Clifford action is
adjoint to the action of the conjugate element, so that the conjugation that defines the theory
becomes an adjoint operation on the module.

The setting is the one of *The Dirac Operator* and *Operators on a Clifford Module*: the Clifford
algebra $A=\mathrm{Cl}_{0,m}$, a left Clifford module $\mathcal{S}$ of values, the Clifford
multiplication $c:A\to\mathrm{End}_\mathbb{R}(\mathcal{S})$, and the involution $*$ — the Clifford
conjugation on the algebra, combined with the conjugation of the coefficient field when the values
are quaternionic or complex. A **Hermitian form** on $\mathcal{S}$ is a positive-definite
sesquilinear form for which the action obeys the self-adjointness axiom
$(x\cdot s,t)=(s,x^{*}\cdot t)$. The finite-dimensional algebraic theory of such forms — the
modules, the forms, the adjoints, the positivity and the cone — is Part II's, in *Hermitian Modules
over a Hilbert Algebra with Hermitian Adjoint*, *The Adjoint of the One-Sided Action with Hermitian
Adjoint*, *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint* and *The
Hilbert Adjoint on a Hilbert Module*; those articles are the algebraic reference and their results
are used here. What this article adds is the analytic layer: the Hilbert completion of the module of
sections, the boundedness of the action, the adjoint of the action with respect to the $L^2$ form,
the self-adjointness of the operator $D$ after the boundary terms are accounted for, and the
monogenic Hilbert spaces as closed subspaces. The Hermitian refinement of these objects with the
split of the operator is *Adjoints on a Clifford Module*, *The Hermitian Dirac Operator* and *The
Hermitian Cauchy Kernel as an Adjoint*; the reproducing kernels are *Positive Definite Kernels in
Clifford Analysis*; the operator theory on the module is *Operators on a Clifford Module*.

## Hermitian Forms on a Clifford Module

### The Form and the Self-Adjointness Axiom

**Definition.** Let $\mathcal{S}$ be a left $A$-module, $A$ a real or complex $\ast$-algebra with
involution $x\mapsto x^{*}$. A **Hermitian form** on $\mathcal{S}$ is a map
$(\cdot,\cdot):\mathcal{S}\times\mathcal{S}\to\mathbb{K}$ ($\mathbb{K}=\mathbb{R},\mathbb{C}$ or
$\mathbb{H}$) that is sesquilinear over the coefficient field, $\mathbb{H}$-Hermitian in the
quaternionic case, and positive definite, $(s,s)>0$ for $s\neq0$.

**Definition.** The form is **compatible with the module structure** when the Clifford action is
adjoint to the action of the conjugate element:

$$
(x\cdot s,\,t) = (s,\,x^{*}\cdot t) \qquad x\in A,\ s,t\in\mathcal{S} ,
$$

equivalently $\rho(x)^{\dagger}=\rho(x^{*})$ for the representation $\rho=c$ of the action.

**Proposition (the axioms are consistent and determine the module type).** A Clifford module carries
a compatible Hermitian form exactly when it is of the definite type; the form is unique up to a
positive scalar on each irreducible summand, and the involution $*$ under which the axiom holds is
the Clifford conjugation, possibly composed with the conjugation of the coefficient field. Under it
a generator $e_i$ is **skew**, $(e_i\cdot s,t)=-(s,e_i\cdot t)$ for $i\ge1$, so the multiplication
by a vector is skew-adjoint, and the scalar unit $e_0=1$ is Hermitian.

*Proof.* The skewness of $e_i$ is $e_i^{*}=-e_i$, which is the Clifford conjugation; the axiom then
reads $(e_i\cdot s,t)=(s,(-e_i)\cdot t)=-(s,e_i\cdot t)$, which is skew-adjointness. The existence
and uniqueness of a compatible definite form on a Clifford module are the results of Part II's
*Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*, and the involution is the one
fixed there. $\square$

**Remark (definite and indefinite).** The definite case is the one in which the form is positive and
the axiom holds as stated; in the indefinite case, where the form has a signature, the conjugation
is replaced by the Krein adjoint and the theory becomes the Krein-space theory of Part II, in *
$J$-Self-Adjoint and $J$-Unitary Operators* and *Spectral Theory on Krein Spaces*. This article is
the definite case, and the word *Hermitian* throughout refers to the positive form and the Clifford
conjugation.

## The Hilbert Module of Sections

### The $L^2$ Completion

**Definition.** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be open and let $\mathcal{S}$ be a definite
Clifford module with a compatible Hermitian form. The **Hilbert module of sections** is the
completion

$$
L^2(\Omega;\mathcal{S}) = \overline{C_c^\infty(\Omega;\mathcal{S})}^{\ \|\cdot\|} , \qquad
\|f\|^2 = \int_\Omega (f(x),f(x))\,dx ,
$$

of the compactly supported smooth sections in the norm of the inner product

$$
\langle f,g\rangle = \int_\Omega (f(x),g(x))\,dx .
$$

**Proposition (the module structure survives the completion).** For $a$ in the algebra of bounded
functions on $\Omega$ with values in $A$, the pointwise action $f\mapsto a\cdot f$ is a bounded
operator on $L^2(\Omega;\mathcal{S})$, with $\|a\|\le\sup_x\|a(x)\|$; the involution acts by
$a\mapsto a^{*}$ and the action satisfies $\rho(a)^{\dagger}=\rho(a^{*})$ with respect to the $L^2$
form. Hence $L^2(\Omega;\mathcal{S})$ is a Hilbert module over the algebra of bounded functions.

*Proof.* The bound is the pointwise estimate $\|a\cdot f\|\le\sup\|a\|\,\|f\|$; the adjoint identity
is the pointwise axiom integrated over $\Omega$, the measure being real. $\square$

### The Action of the Algebra

**Remark (the Hilbert-algebra structure).** The algebra of bounded functions with the involution $*$
and the inner product $\langle f,g\rangle=\int(f,g)$ is a Hilbert algebra in the sense of Part II,
and $L^2(\Omega;\mathcal{S})$ is a Hermitian module over it; the general theory of the one-sided
action, the commutant and the standard form is Part II's, in *Hermitian Modules over a Hilbert
Algebra with Hermitian Adjoint* and *The Hilbert Adjoint on a Hilbert Module*. The realisation here
is the concrete one of Clifford analysis, in which the algebra is generated by the Clifford
generators and the bounded functions and the module is the space of sections.

## The Adjoint of the Clifford Action

### The Adjoint of the Multiplication

**Theorem (the adjoint of the multiplication).** On $L^2(\Omega;\mathcal{S})$ the pointwise Clifford
multiplication $c(x)$ has adjoint $c(x^{*})$:

$$
c(x)^{\dagger} = c(x^{*}) , \qquad x\in A .
$$

In particular the multiplication by a generator is skew-adjoint and the multiplication by a unit
scalar is unitary.

*Proof.* The pointwise axiom $(x\cdot s,t)=(s,x^{*}\cdot t)$ integrates to
$\langle c(x)s,t\rangle=\langle s,c(x^{*})t\rangle$. $\square$

### The Adjoint of the Operator $D$

**Theorem (formal adjointness and the boundary term).** On $L^2(\Omega;\mathcal{S})$ the operator
$D=\sum_\mu c(e_\mu)\partial_\mu$ has formal adjoint $D^{\dagger}=-\bar D$ on compactly supported
sections, and for sections on a bounded domain with smooth boundary,

$$
\langle Df,g\rangle-\langle f,D^{\dagger}g\rangle = \int_{\partial\Omega}\bigl(c(\nu_B)f,g\bigr)\,dS ,
$$

the boundary term being the conormal pairing of *The Cauchy Integral Operator*.

*Proof.* The derivatives integrate by parts with a sign, the multiplications are skew or Hermitian
as in the preceding theorem, and the boundary term is the flux of the vector field $c(e_\mu)f$
against $g$; the computation is the one of *The Dirac Operator* for the formal adjoint
$D^{\dagger}=-\bar D$. $\square$

**Corollary (self-adjointness on a closed domain, and on the Hardy space).** If the boundary term
vanishes — for example on the boundary values of monogenic functions, or on a domain without
boundary — then $D$ is skew-adjoint up to the conjugation, and the operator
$D_{\mathrm{sa}}=\sum_{i\ge1}c(e_i) \partial_i$ is self-adjoint on the appropriate domain, with
$D_{\mathrm{sa}}^2=-\Delta$ and a real spectrum. The spectral theory of that operator is *Dirac
Differential Operators*', and the passage from the formal adjoint to the unbounded self-adjoint
operator is the one of *Unbounded Operators and Spectral Measures* in *Analysis on Linear Spaces*.

## The Monogenic Hilbert Spaces

**Definition.** The **monogenic Bergman space** is the closed subspace

$$
\mathcal{A}^2(\Omega;\mathcal{S}) = \{f\in L^2(\Omega;\mathcal{S}) : Df=0 \text{ in the distributional sense}\}
= \ker D\cap L^2(\Omega;\mathcal{S}) ,
$$

and the **monogenic Hardy space** $H^2(\Omega;\mathcal{S})$ is the closure of the boundary values of
the monogenic $L^2$ functions, as in *The Cauchy Integral Operator*.

**Theorem (the monogenic spaces are Hilbert modules).** $\mathcal{A}^2(\Omega;\mathcal{S})$ is a
closed subspace of $L^2(\Omega;\mathcal{S})$, hence a Hilbert space and a Hermitian module over the
algebra of bounded functions; the same holds for $H^2(\Omega;\mathcal{S})$. The orthogonal
projection onto $\mathcal{A}^2$ is the **Bergman projection**, and onto $H^2$ the **Szegő
projection** $P^+=\tfrac12(I+\mathcal{S})$ of *The Cauchy Integral Operator*; both are self-adjoint
idempotents with respect to the module form.

*Proof.* $\ker D$ is closed in the distributional sense because $D$ is elliptic, hence
$\mathcal{A}^2$ is a closed subspace; the module action preserves $\ker D$ because the coefficients
are constant, so the subspace is a submodule; the projections are the orthogonal projections onto
closed subspaces and are self-adjoint idempotents. The Szegő description is the boundary form of the
same statement. $\square$

**Remark (reproducing kernels).** A monogenic Hilbert space with continuous point evaluations has a
reproducing kernel, which for $\mathcal{A}^2$ and $H^2$ is a positive definite kernel in the sense
of *Positive Definite Kernels in Clifford Analysis*; the Bergman kernel and the Szegő kernel are the
two classical instances, and their relation to the Cauchy kernel is the integral theory of *The
Cauchy Integral Operator*. The kernel is Hermitian in the sense of the module form, and this is the
point at which the module structure and the Hilbert structure meet.

## Summary

A Hermitian Hilbert module over a Clifford algebra is a definite Clifford module $\mathcal{S}$ with
a positive Hermitian form for which the action obeys the self-adjointness axiom
$(x\cdot s,t)=(s,x^{*}\cdot t)$, completed to a Hilbert space of sections
$L^2(\Omega;\mathcal{S})=\overline{C_c^\infty(\Omega;\mathcal{S})}$. The algebra acts by bounded
operators with $c(x)^{\dagger}=c(x^{*})$; a generator is skew-adjoint and the scalar unit is
unitary. The operator $D$ has formal adjoint $D^{\dagger}=-\bar D$, the failure on a bounded domain
being the conormal boundary term $\int_{\partial\Omega}(c(\nu_B)f,g)dS$; when that term vanishes,
$D$ is skew and the vector operator $D_{\mathrm{sa}}$ is self-adjoint with
$D_{\mathrm{sa}}^2=-\Delta$ and a real spectrum, whose spectral theory is *Dirac Differential
Operators*'. The spaces of monogenic $L^2$ functions — the Bergman space
$\mathcal{A}^2=\ker D\cap L^2$ and the Hardy space $H^2$ — are closed subspaces, hence Hilbert
modules, and their orthogonal projections are the Bergman and Szegő projections, the second being
the boundary projection of *The Cauchy Integral Operator*. The algebraic theory of the forms, the
adjoints, the positivity and the cone is Part II's; the Hermitian refinement of the operator is
*Adjoints on a Clifford Module*, *The Hermitian Dirac Operator* and *The Hermitian Cauchy Kernel as
an Adjoint*; the reproducing kernels are *Positive Definite Kernels in Clifford Analysis*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=\mathrm{Cl}_{0,m}$, $*$ | Clifford algebra and its conjugation |
| $\mathcal{S}$ | Definite Clifford module of values |
| $(\cdot,\cdot)$, $(x\cdot s,t)=(s,x^{*}\cdot t)$ | Hermitian form and the self-adjointness axiom |
| $c(x)^{\dagger}=c(x^{*})$ | Adjoint of the multiplication |
| $L^2(\Omega;\mathcal{S})$ | Hilbert module of sections; $\langle f,g\rangle=\int(f,g)$ |
| $D$, $D^{\dagger}=-\bar D$ | Operator and its formal adjoint; conormal boundary term |
| $D_{\mathrm{sa}}=\sum_{i\ge1}c(e_i)\partial_i$ | Self-adjoint vector operator; $D_{\mathrm{sa}}^2=-\Delta$ |
| $\mathcal{A}^2(\Omega;\mathcal{S})=\ker D\cap L^2$ | Monogenic Bergman space; Bergman projection |
| $H^2(\Omega;\mathcal{S})$, $P^+=\tfrac12(I+\mathcal{S})$ | Monogenic Hardy space; Szegő projection |
| $c(\nu_B)$ | Conormal multiplication in the boundary term |

## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the $L^2$ theory of monogenic functions and the boundary spaces.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for monogenic Hilbert spaces and their reproducing kernels.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Hermitian structures on Clifford modules and the self-adjointness of Dirac-type operators.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the operator theory on the $L^2$ spaces of the Clifford theory.
