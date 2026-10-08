
# __The Hermitian Cauchy Kernel as an Adjoint__

## Introduction

An integral kernel is not only a function of two variables but the matrix of an operator, and the
kernel of the adjoint operator is the conjugate-reverse of the kernel: if $T$ has kernel $K(x,y)$,
then $T^{\dagger}$ has kernel $K(y,x)^{*}$. The Hermitian Cauchy kernel
$E_r(Z)=Z_r^{*}/(a_{4n}|Z|^{4n})$ is, literally, built from the **adjoint** variable $Z_r^{*}$ of
the Hermitian theory, and this article reads the kernel in that way: as the kernel of the adjoint,
as the object implementing the adjoint pairing between the Hermitian monogenic functions and the
boundary densities, and as the entry of the matrix that is the inverse of the adjoint matrix
operator. In this reading the integral theory of *The Hermitian Cauchy Integral and the Boundary
Values* becomes a statement about adjoints, and the boundary projections of the monogenic Hardy
space appear as self-adjoint idempotents.

The setting is that of *Hermitian Quaternionic Analysis and the Conjugate Cauchy–Riemann Operator*:
the algebra $\mathbb{H}_N$, the four Hermitian operators $\partial_{Z_r}$ and their conjugates
$\partial_{Z_r}^{\dagger}$, the Hermitian variables $Z_r$ and their adjoints $Z_r^{*}$, and the
kernels $E_r(Z)=Z_r^{*}/(a_{4n}|Z|^{4n})$. The module and form background is *Hermitian Hilbert
Modules over a Clifford Algebra*; the operator-theoretic statements about the Hermitian Dirac
operator are *The Hermitian Dirac Operator*; the integral formulae and the matrix device are *The
Hermitian Cauchy Integral and the Boundary Values*; the one-operator statements — the Cauchy
transform, the Hilbert transform, the self-adjointness of the projection — are *The Cauchy Integral
Operator* and *The Hermitian Adjoint on a Hermitian Module* (Part II), and the general kernel theory of
the adjoint is *Analysis on Linear Spaces*', in *Hermitian Kernels and the Integral Operator*.

## Kernels and their Adjoints

### The General Principle

**Theorem (the adjoint kernel).** Let $K$ be a distributional kernel on $X\times X$ and let $T$ be
the operator $Tf(x)=\int_XK(x,y)f(y)\,dy$. Then the adjoint with respect to the module form has
kernel

$$
K^{\dagger}(x,y)=K(y,x)^{*} ,
$$

the conjugate-reverse of $K$. In particular the kernel is the kernel of a **self-adjoint** operator
exactly when $K(y,x)^{*}=K(x,y)$ — the Hermitian symmetry of *Positive Definite Kernels in Clifford
Analysis* — and the kernel is that of an **antiself-adjoint** operator exactly when
$K(y,x)^{*}=-K(x,y)$.

*Proof.* Compute $\langle Tf,g\rangle=\int\!\!\int(K(x,y)f(y),g(x))\,dy\,dx$ and move the form to
the other factor using its sesquilinearity and the module axiom; the resulting expression is
$\int\!\!\int(f(y),K(x,y)^{*}g(x))\,dy\,dx$, which is $\langle f,T^{\dagger}g\rangle$ with the
kernel $K(y,x)^{*}$ after the interchange of the variables. The statement is the Clifford-module
instance of the general kernel theorem of *Hermitian Kernels and the Integral Operator*. $\square$

**Remark (why the conjugate-reverse is the object of this article).** The Euclidean and Hermitian
Cauchy kernels are built from the **conjugate** variable: $F_r(X)=-X_r/(a_{4n}|X|^{4n})$ is odd,
$F_r(-X)=-F_r(X)$, and $E_r(Z)=Z_r^{*}/(a_{4n}|Z|^{4n})$ carries the conjugated variable in the
numerator and the conjugated value in the kernel. The recursion $K\mapsto K^{\dagger}$ is therefore
not an afterthought: the kernels of the Hermitian theory are constructed from the adjoint, and the
whole integral theory is a theory of adjoint pairings. This is the reason the Hermitian Cauchy
kernel is naturally read as an adjoint, and the reason the boundary projections of the theory come
out self-adjoint.

### The Hermitian Cauchy Kernel

**Proposition (the Hermitian Cauchy kernel and the adjoint variable).** The Hermitian kernel
$E_r(Z)=Z_r^{*}/(a_{4n}|Z|^{4n})$ is odd, $E_r(-Z)=-E_r(Z)$, and is built from the adjoint Hermitian
variable $Z_r^{*}$; under the involution $*$ the kernel is carried to the kernel of the conjugate
operator,

$$
(E_r)^{*}(Z) \sim Z_r/(a_{4n}|Z|^{4n}) ,
$$

so the four Hermitian Cauchy kernels pair into the four conjugate Hermitian Dirac operators, and the
matrix $E$ is correspondingly the adjoint partner of the matrix $D$ of the operators.

*Proof.* The oddness is immediate from $(Z_r)^{*}=-Z_r$-type skewness of the variables and the
evenness of $|Z|$; the involution statement is the conjugation of the numerator and of the
coefficients, with the same normalisation; the matrix statement is that $D^{\mathsf T}E=\delta I$ of
*The Hermitian Cauchy Integral and the Boundary Values*, which exhibits $E$ as the kernel of the
operation inverse to the adjoint matrix operator. The verification in
$\mathbb{H}\otimes_{\mathbb{R}}\mathrm{Cl}_{0,4}$ is in *Clifford Analysis*. $\square$

**Theorem (the matrix kernel is the adjoint partner of the matrix operator).** With the circulant
matrix $D$ of the four Hermitian Dirac operators, the circulant matrix $E$ of the four Hermitian
kernels satisfies

$$
D^{\mathsf T}E = \delta I , \qquad E\,D^{\mathsf T} = \delta I \ \text{ on the appropriate domain} ,
$$

so the matrix kernel is the two-sided inverse of the adjoint matrix operator on the level of
distributions, and it is the kernel of the adjoint operation that inverts $D^{\mathsf T}$.

*Proof.* The first identity is the fundamental-solution theorem of *The Hermitian Cauchy Integral
and the Boundary Values*; the second follows by the Hermitian symmetry of the matrix kernel and the
commutativity of the circulant matrices, or by the second Borel–Pompeiu formula. $\square$

## The Adjoint Pairing of the Cauchy Theory

**Remark (the pairing).** The Hermitian Cauchy theory is a duality between two spaces: the
$q$-Hermitian monogenic functions on a domain and the densities on the boundary, paired by the
integral of the pointwise module form,

$$
\langle f,\mu\rangle = \int_{\partial\Omega}(f,\mu) ,
$$

and the Cauchy kernel is the object that realises the duality: the transform $\mathcal{C}$ with
kernel $E\,N^{\mathsf T}$, and its adjoint $\mathcal{C}^{\dagger}$ with the conjugate-reverse
kernel, are the two members of the pairing, and the Cauchy integral formula is the statement that
the pairing of the boundary values reproduces the interior function. In the complex refinement this
pairing is the Martinelli–Bochner pairing of forms in several complex variables, and the
conjugate-reverse kernel is the conjugate form; the general theory of the several-variable pairing
is *Several Complex Variables*'.

**Theorem (the boundary projections are self-adjoint).** The Cauchy transform $\mathcal{C}$ has
adjoint $\mathcal{C}^{\dagger}=I-\mathcal{C}$ up to the parity of the kernel, so that the boundary
operators $\mathcal{C}^{\pm}$ of the Plemelj–Sokhotski decomposition of *The Cauchy Integral
Operator* are complementary projections and the singular operator is self-adjoint with respect to
the module form:

$$
(\mathcal{C}^{+})^{\dagger}=\mathcal{C}^{+} , \qquad (\mathcal{C}^{-})^{\dagger}=\mathcal{C}^{-} , \qquad
\mathcal{S}^{\dagger}=\mathcal{S} , \qquad \mathcal{S}^2=I .
$$

*Proof.* The one-operator statement is that of *The Cauchy Integral Operator*; passing to the matrix
of the Hermitian theory, the conjugate-reverse kernel of the matrix transform is the same matrix
transform with the conormal on the other side, and the Hermitian symmetry of the kernel $E$ and the
reality of the conormal element give the self-adjointness of the singular operator. $\square$

**Corollary (the Szegő projection and the adjoint).** The Szegő projection $P^+$ of the monogenic
Hardy space is self-adjoint, and its kernel — the Szegő kernel of *Positive Definite Kernels in
Clifford Analysis* — is the Cauchy kernel read on the boundary; the Bergman projection is likewise
self-adjoint. Hence the two projections of the monogenic $L^2$ theory are orthogonal projections in
the sense of the module form, and the structure they define is the one of *Hermitian Hilbert Modules
over a Clifford Algebra*.

*Proof.* A projection is self-adjoint exactly when it is the orthogonal projection onto its range;
the range of $P^+$ is the monogenic Hardy space, closed by *Hermitian Hilbert Modules over a
Clifford Algebra*, and the reproducing property of its kernel makes $P^+$ the orthogonal projection.
$\square$

## The Jump Relations

**Theorem (the Plemelj formulae of the Hermitian Cauchy kernel).** For a density $f$ of Hölder class
on the boundary the one-sided extensions $\mathcal{C}^{\pm}f$ exist as continuous limits and satisfy
the **Plemelj–Sokhotski formulae**

$$
\mathcal{C}^{\pm}f = \pm\tfrac12 f + \mathcal{S}f , \qquad \mathcal{C}^{+}f-\mathcal{C}^{-}f = f ,
\qquad \mathcal{C}^{+}f+\mathcal{C}^{-}f = 2\mathcal{S}f ,
$$

with $\mathcal{S}=2\mathcal{C}^{+}-I$ the singular operator of *The Cauchy Integral Operator*; the
**jump** $\mathcal{C}^{+}-\mathcal{C}^{-}$ is the identity, and the **sum** is twice the singular
operator.

*Proof.* The formulae are the decompositions of the identity with the projections
$\mathcal{C}^{\pm}=\tfrac12(I\pm\mathcal{S})$; the existence of the limits is the Plemelj calculus
of *The Cauchy Integral Operator* and *The Hermitian Cauchy Integral and the Boundary Values* read
in the Hermitian refinement. $\square$

**Theorem (the jump of the adjoint).** The adjoint of the jump is the jump of the adjoint: with the
adjoint taken with respect to the module form,

$$
(\mathcal{C}^{+}-\mathcal{C}^{-})^{\dagger} = I , \qquad (\mathcal{C}^{+}+\mathcal{C}^{-})^{\dagger} =
2\mathcal{S} ,
$$

so the jump operator is self-adjoint and the singular operator is self-adjoint. Read through the
conjugate-reverse rule, the statement is that the difference of the two boundary values of the
kernel $K(y,x)^{*}$ is the kernel of the identity, which is the distributional form of the jump
relation.

*Proof.* The jump is the identity by the theorem above, and the identity is self-adjoint; the sum is
twice $\mathcal{S}$, whose self-adjointness is the preceding section. The kernel form of the jump is
the conjugate-reverse of the Plemelj formula $K\,N^{\mathsf T}$ computed on the two sides, where the
two sides differ by the conormal term of the Cauchy–Pompeiu formula. $\square$

**Remark (the jump as the boundary of the adjoint pairing).** The jump relation and the adjointness
of the boundary operators are two readings of the same structure: the pairing
$\langle f,\mu\rangle=\int_{\partial\Omega}(f,\mu)$ of the Cauchy theory is non-degenerate, the
kernel is its reproducing object, and the difference of the two one-sided extensions of the
transform is the identity exactly because the transform is a projection differing from its adjoint
by the parity of the kernel. In the Hermitian refinement the jump is the identity on the boundary
spinors, the singular operator is the reflection $\mathcal{S}=\mathcal{C}^{+}-\mathcal{C}^{-}$ of
the splitting $\mathcal{H}=P^+L^2\oplus P^-L^2$ of the boundary space, and the two projections are
the self-adjoint projections of the monogenic Hardy theory.

## Summary

A kernel $K(x,y)$ is the matrix of an operator, and the kernel of the adjoint is the
conjugate-reverse $K^{\dagger}(x,y)=K(y,x)^{*}$; the kernel is self-adjoint exactly when it is
Hermitian in the sense of *Positive Definite Kernels in Clifford Analysis*. The Hermitian Cauchy
kernel $E_r(Z)=Z_r^{*}/(a_{4n}|Z|^{4n})$ is built from the **adjoint** Hermitian variable, is odd,
and is carried by the involution to the kernel of the conjugate operator; the four kernels pair with
the four conjugate Hermitian Dirac operators, and the circulant matrix $E$ is the two-sided inverse
of the adjoint matrix operator, $D^{\mathsf T}E=\delta I$. The Hermitian Cauchy theory is a
**duality**: the kernel realises the adjoint pairing between the $q$-Hermitian monogenic functions
and the boundary densities, whose complex refinement is the Martinelli–Bochner pairing of several
complex variables, and the conjugate-reverse kernel is the conjugate form. The boundary operators of
the Plemelj–Sokhotski decomposition are complementary **self-adjoint** projections with respect to
the module form, $\mathcal{S}^{\dagger}=\mathcal{S}$ and $\mathcal{S}^2=I$, and the Szegő and
Bergman projections of the monogenic spaces are likewise self-adjoint, their kernels being the
reproducing kernels of *Positive Definite Kernels in Clifford Analysis*. The one-operator statements
are *The Cauchy Integral Operator*'s and *The Hermitian Adjoint on a Hermitian Module*'s; the integral
formulae and the matrix device are *The Hermitian Cauchy Integral and the Boundary Values*; the
operator-theoretic companion is *The Hermitian Dirac Operator*; and the general kernel theory of
adjoints is *Analysis on Linear Spaces*'.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K(x,y)$, $K^{\dagger}(x,y)=K(y,x)^{*}$ | Kernel and the kernel of the adjoint |
| $K(y,x)^{*}=K(x,y)$ | Hermitian symmetry (self-adjoint kernel) |
| $E_r(Z)=Z_r^{*}/(a_{4n}|Z|^{4n})$ | Hermitian Cauchy kernel built from the adjoint variable |
| $E_r(-Z)=-E_r(Z)$ | Oddness of the Hermitian kernel |
| $D^{\mathsf T}E=\delta I$ | Matrix kernel as the inverse of the adjoint matrix operator |
| $\langle f,\mu\rangle=\int_{\partial\Omega}(f,\mu)$ | Adjoint pairing of functions and densities |
| $\mathcal{C}^{\pm}$, $\mathcal{S}=2\mathcal{C}^+-I$ | Plemelj projections and singular operator; $\mathcal{S}^{\dagger}=\mathcal{S}$, $\mathcal{S}^2=I$ |
| $P^+$, Szegő kernel | Self-adjoint Szegő projection and its Cauchy-kernel realisation |

## Further Reading

- F. Brackx, H. De Schepper and F. Sommen, *Hermitean Clifford Analysis*, for the Hermitian Cauchy kernels and their conjugation properties.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the one-operator Cauchy transform, the Plemelj formulae and the self-adjointness of the projections.
- R. Rocha-Chávez, M. Shapiro and F. Sommen, *Integral Theorems for Functions and Differential Forms in $\mathbb{C}^m$* (Chapman & Hall, 2002), for the Martinelli–Bochner pairing and its adjoint structure.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the kernel and adjoint framework of the boundary-value theory.
