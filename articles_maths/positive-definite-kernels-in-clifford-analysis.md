
# __Positive Definite Kernels in Clifford Analysis__

## Introduction

A reproducing kernel Hilbert space is a Hilbert space of functions on which the point evaluations
are continuous; equivalently, it is the space $H_K$ attached by the Aronszajn construction to a
**positive definite kernel** $K$ on the product $X\times X$. The general theory — the positivity
condition, the Aronszajn theorem, the Hermitian kernels and their integral operators — belongs to
*Analysis on Linear Spaces*, in *Reproducing Kernel Hilbert Spaces*, *Positive Definite Functions*,
*Hermitian Kernels and the Integral Operator* and *Hermitian Integral Kernels*; this article
develops the instances that occur in Clifford analysis, in which the kernel takes values in the
Clifford algebra or in its modules and the functions take values in a Clifford module, and in which
the two classical instances are the **Bergman kernel** of the monogenic $L^2$ space and the **Szegő
kernel** of the monogenic Hardy space.

The setting is that of *Hermitian Hilbert Modules over a Clifford Algebra*: the Clifford algebra
$A=\mathrm{Cl}_{0,m}$ with conjugation $*$, a definite Clifford module $\mathcal{S}$ of values with
a compatible Hermitian form, and the Hilbert modules of sections $L^2(\Omega;\mathcal{S})$ and their
closed monogenic subspaces $\mathcal{A}^2=\ker D\cap L^2$ and $H^2$. The positivity is the
positivity of the module form, the Hermitian symmetry is the symmetry of that form combined with the
involution $*$, and the reproducing property is the continuity of the point evaluation, which the
elliptic theory supplies. The operator-theoretic background is *Hermitian Hilbert Modules over a
Clifford Algebra*; the Cauchy kernel and the boundary projections are *The Cauchy Integral
Operator*; the Hermitian refinement of the kernels is *The Hermitian Cauchy Integral and the
Boundary Values* and *The Hermitian Cauchy Kernel as an Adjoint*. Nothing of the general theory is
repeated: what is specific here is the Clifford-valued kernel, its Hermitian symmetry under $*$, and
the two kernels of the monogenic spaces.

## Positive Definite Kernels with Clifford Values

### Definition and Positivity

**Definition.** Let $X$ be a set and let $\mathcal{S}$ be a definite Clifford module with a
compatible Hermitian form $(\cdot,\cdot)$. A **kernel** is a map
$K:X\times X\to\mathrm{End}_\mathbb{R}(\mathcal{S})$ (or, in the scalar case, $K:X\times X\to A$);
it is **positive definite** when

$$
\sum_{i,j=1}^{n}\bigl(K(x_i,x_j)\,s_j,\,s_i\bigr)\ \ge\ 0
$$

for every finite family $x_1,\dots,x_n\in X$ and every $s_1,\dots,s_n\in\mathcal{S}$.

**Definition.** The kernel is **Hermitian** when

$$
K(x,y) = K(y,x)^{*} ,
$$

the adjoint being taken with respect to the module form; for a scalar kernel with values in $A$ this
reads $K(x,y)=K(y,x)^{*}$, the Clifford conjugation of the value.

**Theorem (Aronszajn; quoted from the general theory).** A Hermitian positive definite kernel $K$ on
$X\times X$ determines a Hilbert space $H_K$ of $\mathcal{S}$-valued functions on $X$ on which the
point evaluations are continuous, with the reproducing property

$$
(K(x,\cdot)s,\,f)_{H_K} = (s,\,f(x)) \qquad x\in X,\ s\in\mathcal{S},\ f\in H_K ,
$$

and every such space arises from exactly one kernel. The theorem is the general Aronszajn theorem of
*Reproducing Kernel Hilbert Spaces*; the Clifford-valued case is its instance over the module
$\mathcal{S}$.

*Proof.* Quoted. The proof is the general one: the span of the functions $K(x,\cdot)s$ with the
inner product induced by positivity is a pre-Hilbert space, its completion is $H_K$, and the
reproducing property makes the evaluation continuous and recovers the kernel from the space.
$\square$

**Remark (what the Clifford structure adds).** Three features distinguish the case at hand from the
scalar theory. The kernel takes values in a non-commutative algebra, so the order of the factors in
the reproducing property matters and the Hermitian symmetry carries the conjugation $*$; the module
form is the one of *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, so the
positivity of the kernel is the positivity of a family of module forms; and the functions of the
classical spaces are **monogenic**, so the kernel inherits monogenicity in each variable — it is
monogenic in the first and anti-monogenic in the second — and the kernel is determined by its
diagonal. These are the properties the next two sections use.

## The Bergman Kernel of the Monogenic Space

**Definition.** For a bounded domain $\Omega$ the **monogenic Bergman space** is
$\mathcal{A}^2(\Omega;\mathcal{S})=\ker D\cap L^2(\Omega;\mathcal{S})$ and the **Bergman kernel** is
the reproducing kernel $B:\Omega\times\Omega\to\mathrm{End}(\mathcal{S})$ of the space, so that

$$
f(w) = \int_\Omega B(w,z)\,f(z)\,dz , \qquad f\in\mathcal{A}^2(\Omega;\mathcal{S}) .
$$

**Theorem (properties of the Bergman kernel).** The Bergman kernel of the monogenic space exists and
is unique; it is Hermitian, $B(w,z)=B(z,w)^{*}$; it is monogenic in the variable $w$ for the
operator $D$ and anti-monogenic in $z$; it is determined by the diagonal through the identity
$\sum_i B(w,z_i)B(z_i,z)\to B(w,z)$; and it is the kernel of the orthogonal projection of
$L^2(\Omega;\mathcal{S})$ onto $\mathcal{A}^2(\Omega;\mathcal{S})$.

*Proof.* The point evaluation is continuous on $\mathcal{A}^2$ because $D$ is elliptic and the
domain is bounded, so the Aronszajn construction applies; the monogenicity in each variable follows
by applying $D$ in $w$ and $\bar D$ in $z$ to the reproducing identity, and the projection statement
is the reproducing property read as an integral operator. $\square$

**Remark (the relation to the Cauchy kernel).** The Bergman kernel of the monogenic space is not the
Cauchy kernel: the Cauchy kernel is the reproducing kernel of the space of boundary values, i.e. the
Szegő kernel of the following section, while the Bergman kernel reproduces the space of $L^2$
monogenic functions on the whole domain. The two agree only on the boundary in the limiting sense.
For the half-space and the ball the Bergman kernel of the monogenic space has the same shape as the
Bergman kernel of the holomorphic space, with the Clifford kernel in place of the complex one; the
explicit formula is the Clifford refinement of the classical Bergman kernel, cited to the
literature. The general Bergman operator of a domain is *The Bergman Operator* in a later category,
and the metric it defines is *Hermitian Symmetric Spaces and the Bergman Metric*.

## The Szegő Kernel and the Boundary

**Definition.** For a domain $\Omega$ with smooth boundary the **monogenic Szegő kernel** is the
reproducing kernel $S$ of the monogenic Hardy space $H^2(\Omega;\mathcal{S})$ of *The Cauchy
Integral Operator*, so that

$$
f(w) = \int_{\partial\Omega} S(w,z)\,f(z)\,dS(z) , \qquad f\in H^2(\Omega;\mathcal{S}) .
$$

**Theorem (the Szegő kernel is the Cauchy kernel read on the boundary).** The Szegő kernel is
determined by the Cauchy kernel and the conormal element:

$$
S(w,z) = E(w-z)\,\nu_B(z)
$$

up to the normalisation of the Cauchy–Pompeiu formula of *Clifford Analysis*, and it is Hermitian in
the sense of the module form, monogenic in $w$ and anti-monogenic in $z$; the projection it defines
is the Szegő projection $P^+=\tfrac12(I+\mathcal{S})$ of *The Cauchy Integral Operator*.

*Proof.* The boundary values of a monogenic function are reproduced by the Cauchy integral formula
against the Cauchy kernel and the conormal element, which is exactly the reproducing property for
the kernel $E(w-z)\nu_B(z)$; the Hermitian symmetry follows from the Hermitian symmetry of the
kernel $E$ and the reality of the conormal element, and the projection statement is the Cauchy
integral formula as the orthogonal projection onto the space of boundary values. $\square$

**Remark (why the boundary kernel is the Cauchy one).** In the monogenic theory the Hardy space is
the range of the boundary Cauchy transform, so its reproducing kernel is the Cauchy kernel itself;
this is the sense in which the Cauchy integral formula *is* the reproducing property of the
monogenic Hardy space, a statement that the general theory of *The Cauchy Integral Operator* records
as the identification of the Szegő projection with the Cauchy transform. The Bergman and the Szegő
kernels are therefore the two ends of the same structure: the second is the Cauchy kernel, and the
first is its interior analogue.

## The Kernel as an Operator

**Theorem (the integral operator of a Hermitian kernel).** To a Hermitian kernel $K$ on
$\Omega\times\Omega$ associate the integral operator

$$
(T_Kf)(x) = \int_\Omega K(x,y)\,f(y)\,dy .
$$

The kernel is Hermitian exactly when the operator is self-adjoint on $L^2(\Omega;\mathcal{S})$, and
positive definite exactly when the operator is positive, $\langle T_Kf,f\rangle\ge0$; the two
properties are the operator form of the two conditions defining the reproducing kernel.

*Proof.* The kernel of the adjoint of $T_K$ is the conjugate-reverse $K(y,x)^{*}$ by the general
theorem of *Hermitian Kernels and the Integral Operator*, so $T_K$ is self-adjoint exactly when
$K(x,y)=K(y,x)^{*}$; the positivity of the quadratic form is the definition of positive definiteness
read as the integral $\int\!\!\int(K(x,y)f(y),f(x))\,dy\,dx\ge0$. The statement is the
Clifford-module instance of the general theory of *Banach and Hilbert Spaces*. $\square$

**Remark (the spectral consequences).** A compact self-adjoint integral operator with a positive
definite kernel therefore has a nonnegative spectrum, an orthonormal basis of eigenspinors and a
Mercer-type expansion of the kernel in that basis; the reproducing kernel Hilbert space of the
kernel is the range of the square root of the operator, and the Cauchy and Bergman kernels of the
preceding sections are the entries of the projection operators onto the corresponding monogenic
spaces. The spectral theory of the integral operator, and the compactness on which the expansion
rests, are the subjects of *Hermitian Integral Kernels*, *Compact Operators* and *Self-Adjoint
Operators and the Spectral Theorem*; the Clifford case differs only in that the kernel and the
eigenspinors take values in the algebra and the module.

## Summary

A Clifford-valued kernel $K:X\times X\to\mathrm{End}(\mathcal{S})$ is **positive definite** when
$\sum_{i,j}(K(x_i,x_j)s_j,s_i)\ge0$ and **Hermitian** when $K(x,y)=K(y,x)^{*}$, the adjoint being
taken in the compatible module form; by the Aronszajn theorem of *Reproducing Kernel Hilbert Spaces*
it defines a Hilbert space $H_K$ with the reproducing property $(K(x,\cdot)s,f)_{H_K}=(s,f(x))$. The
Clifford case adds the non-commutativity of the algebra, the module form of Part II and the
monogenicity of the functions, so that the kernel is monogenic in the first and anti-monogenic in
the second variable. The **Bergman kernel** $B$ of the monogenic $L^2$ space
$\mathcal{A}^2=\ker D\cap L^2$ is Hermitian, monogenic in each variable and the kernel of the
orthogonal projection onto $\mathcal{A}^2$; the **Szegő kernel** $S$ of the monogenic Hardy space is
the Cauchy kernel read on the boundary, $S(w,z)=E(w-z)\nu_B(z)$, and its projection is the boundary
Cauchy transform $P^+=\tfrac12(I+\mathcal{S})$ of *The Cauchy Integral Operator*. The two kernels
are the interior and the boundary instances of the same structure, whose general theory is *Analysis
on Linear Spaces*' and whose module background is *Hermitian Hilbert Modules over a Clifford
Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K(x,y)$, $K(x,y)=K(y,x)^{*}$ | Clifford-valued kernel and its Hermitian symmetry |
| $\sum_{i,j}(K(x_i,x_j)s_j,s_i)\ge0$ | Positive definiteness |
| $H_K$, $(K(x,\cdot)s,f)=(s,f(x))$ | The kernel's Hilbert space and the reproducing property |
| $B(w,z)$ | Bergman kernel of $\mathcal{A}^2(\Omega;\mathcal{S})$ |
| $S(w,z)=E(w-z)\nu_B(z)$ | Szegő kernel of $H^2(\Omega;\mathcal{S})$; the Cauchy kernel on the boundary |
| $\mathcal{A}^2=\ker D\cap L^2(\Omega;\mathcal{S})$ | Monogenic Bergman space |
| $H^2(\Omega;\mathcal{S})$, $P^+$ | Monogenic Hardy space and Szegő projection |

## Further Reading

- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for monogenic Hilbert spaces and their reproducing kernels.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy kernel and the boundary spaces of monogenic functions.
- Saburou Saitoh, *Integral Transforms, Reproducing Kernels and their Applications* (Longman, 1997), for the Aronszajn theory and the Bergman and Szegő kernels in the classical setting.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the Clifford-valued kernels of the harmonic analysis of the theory.
