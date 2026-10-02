
# __The Hermitian Dirac Operator__

## Introduction

The Hermitian refinement supplies, in addition to the pair of Hermitian Dirac operators, a single
first-order operator whose square is the Laplacian and which is **symmetric** with respect to the
Hermitian form: the operator obtained by adding the two Hermitian Dirac operators, which the
involution of the form exchanges. This article treats that operator — the Hermitian Dirac operator —
its splitting, its adjointness with respect to the Hermitian form, its essential self-adjointness on
the Sobolev space and the spectral consequences, and it fixes the place of the operator in relation
to the finite-dimensional Dirac element of Part II's *Dirac Operators with Hermitian Adjoint*.

The setting is that of *Hermitian Clifford Analysis and the Hermitian Monogenic Functions* and
*Hermitian Quaternionic Analysis and the Conjugate Cauchy–Riemann Operator*: the even-dimensional
space $\mathbb{R}^{2n}=\mathbb{C}^n$ with the Witt basis and the pair
$\partial_{\underline z}=\sum_jf_j\partial_{z_j}$,
$\partial_{\bar z}=\sum_jf_j^{*}\partial_{\bar z_j}$, or the four-dimensional-per-block quaternionic
case with the four operators $\partial_{Z_r}$; the value module $\mathcal{S}$ with its Hermitian
form; and the Hilbert module $L^2(\Omega;\mathcal{S})$ of *Hermitian Hilbert Modules over a Clifford
Algebra*. The operator-algebraic content of the split — the symbols, the Fischer decomposition, the
bivariate representation — is *The Hermitian Dirac Operator and the Fischer Decomposition*, and is
not repeated; the integral theory is *The Hermitian Cauchy Integral and the Boundary Values*; the
kernel as an adjoint is *The Hermitian Cauchy Kernel as an Adjoint*; the finite-dimensional Dirac
element, its square and its Hermitian adjoint are Part II's *Dirac Operators with Hermitian
Adjoint*, cited and distinguished; and the general spectral theory of Dirac-type operators is *Dirac
Differential Operators*' and *Unbounded Operators and Spectral Measures*.

## The Operator and its Splitting

**Definition.** The **Hermitian Dirac operator** is

$$
\mathcal{D} = \partial_{\underline z}+\partial_{\bar z} ,
$$

the sum of the two Hermitian Dirac operators of the complex refinement; in the quaternionic
refinement the corresponding operator is the sum of the four,
$\mathcal{D}=\sum_{r=0}^{3}\partial_{Z_r}$.

**Theorem (the square is the Laplacian).** The Hermitian Dirac operator satisfies

$$
\mathcal{D}^2 = \{\partial_{\underline z},\partial_{\bar z}\} = \tfrac14\Delta_{2n} ,
$$

because the two squares vanish separately; in the quaternionic case the sum of the four operators
has square the corresponding multiple of $\Delta_N$ from the split
$\Delta_N=16\sum_r\partial_{Z_r}\partial_{Z_r}^{\dagger}$.

*Proof.* Expand $(\partial_{\underline z}+\partial_{\bar z})^2$ and use
$\partial_{\underline z}^2=\partial_{\bar z}^2=0$ and
$\{\partial_{\underline z},\partial_{\bar z}\}=\tfrac14\Delta_{2n}$ of *Hermitian Clifford Analysis
and the Hermitian Monogenic Functions*. $\square$

**Remark (two square roots of the Laplacian).** The Euclidean operator gives another square root,
$D=2(\partial_{\underline z}-\partial_{\bar z})$ with $D^2=-\Delta_{2n}$; the two square roots are
interchanged by the reflection $\partial_{\bar z}\mapsto-\partial_{\bar z}$, i.e. by the complex
conjugation of the Hermitian structure, and they correspond to the two signs of the complex
structure. The Hermitian Dirac operator is the one adapted to the Hermitian form, as the next
section shows.

**Remark (the splitting as a grading).** The splitting
$\mathcal{D}=\partial_{\underline z}+\partial_{\bar z}$ is a decomposition into two **isotropic**
parts: each part alone has square zero, so the operator is a sum of two anticommuting square-zero
operators, and the algebra they generate is the exterior algebra on the Witt basis. This is the
operator form of the bidegree decomposition of *The Hermitian Dirac Operator and the Fischer
Decomposition*: the two parts raise and lower the bidegree, and $\mathcal{D}$ is the total
differential of the resulting bicomplex.

## Self-Adjointness with Respect to the Hermitian Form

### Symmetry

**Theorem (the Hermitian Dirac operator is symmetric).** With respect to the Hermitian form of the
module, the involution $*$ exchanges the two halves of the split,

$$
(\partial_{\underline z})^{\dagger} \sim \partial_{\bar z} , \qquad
(\partial_{\bar z})^{\dagger} \sim \partial_{\underline z} ,
$$

the symbol $\sim$ meaning equality up to the conjugation of the variables and the normalisation of
the theorem; consequently the Hermitian Dirac operator is **symmetric**,

$$
\langle \mathcal{D}f,g\rangle = \langle f,\mathcal{D}g\rangle ,
$$

on compactly supported smooth sections.

*Proof.* The involution $*$ is the composition of the conjugation of the coefficient field with the
Clifford conjugation; it carries the Witt basis element $f_j$ to $f_j^{*}$, the coefficient
differentiation $\partial_{z_j}$ to $\partial_{\bar z_j}$, and conversely, so it interchanges
$\partial_{\underline z}$ and $\partial_{\bar z}$; a sum of two terms that the involution
interchanges is fixed by it, and the symmetry with respect to the form is precisely the fixed-point
property. Integrating by parts on compactly supported sections removes the boundary terms. $\square$

**Remark (why the two halves are conjugate).** The pairing is the module form's version of the
pairing of $\partial_{\underline z}$ with $\partial_{\bar z}$: the two operators are conjugate
linear in each other under $*$, so each is the adjoint of the other with respect to the form, and
any symmetric combination of them is a symmetric operator. The Hermitian Dirac operator is the
symmetric combination; the Euclidean operator $D=2(\partial_{\underline z}-\partial_{\bar z})$ is
the antisymmetric one — being the difference it changes sign under the exchange — and this is why
$D$ is skew-adjoint rather than self-adjoint with respect to the form, with $\bar D$ as its formal
adjoint as in *Hermitian Hilbert Modules over a Clifford Algebra*.

### Essential Self-Adjointness and the Spectrum

**Theorem (essential self-adjointness).** On the Hilbert module $L^2(\mathbb{R}^{2n};\mathcal{S})$
the Hermitian Dirac operator, defined on the Sobolev space $H^1$, is essentially self-adjoint; its
closure has square the Laplacian, and its spectrum is the whole real line, with the Fourier symbol
$c(\sum_jf_j\xi_{z_j})+c(\sum_jf_j^{*}\xi_{\bar z_j})$ whose square is $\tfrac14|\xi|^2$.

*Proof.* The operator has constant coefficients and its symbol is real-linear and elliptic in the
sense that its square is $\tfrac14|\xi|^2$, so the Fourier transform diagonalises the closure and
shows self-adjointness on $H^1$; the symbol takes all real values — it is a sum of two isotropic
parts — so the spectrum is the whole line, in contrast with a symmetric elliptic operator with
positive square, whose spectrum is a half line if the square is positive. The argument is the
standard one for a first-order constant-coefficient operator, and the statement is the Hermitian
refinement of the spectral statement of *Dirac Differential Operators*' for the Euclidean operator.
$\square$

**Corollary (the sign of the square and the spectrum).** The spectrum of $\mathcal{D}$ is the whole
real line because $\mathcal{D}^2=\tfrac14\Delta_{2n}$ is a **negative** operator — the Laplacian
with the sign of the metric — so its square root has the whole line as spectrum; the Euclidean
operator $D$ has the imaginary axis, $D^2=-\Delta_{2n}$, and its self-adjoint variant is $iD$, with
the real spectrum corresponding to $-\Delta$ having the positive half line. The two conventions are
related by the choice of sign in the square root of the Laplacian, and the choice that makes the
operator self-adjoint with respect to the Hermitian form is the one of the definition above.

*Proof.* The spectrum of a self-adjoint operator whose square is $-\Delta$ with $\Delta$ negative is
$\mathbb{R}$ when the square root is chosen as $\mathcal{D}$ and $i\mathbb{R}$ when it is chosen as
$D$; the two differ by the factor $i$, and the Hermitian choice absorbs that factor into the switch
from difference to sum. $\square$

## The Relation to the Finite-Dimensional Dirac Element

**Remark (two operators with the same name).** Part II's *Dirac Operators with Hermitian Adjoint*
introduces the finite-dimensional **Dirac element** $D_{\mathrm{alg}}=\sum_kL_{e_k}$, the sum of the
left multiplications by the generators, and computes its square
$D_{\mathrm{alg}}^2=-\dim V\cdot\mathrm{id}$ (up to the convention), its Hermitian adjoint
$D_{\mathrm{alg}}^{\dagger}=-D_{\mathrm{alg}}$, and the absence of harmonic spinors; that article is
algebraic and the operator acts on the module itself. The operator of this article is the
**differential** one: it acts on functions, has the Laplacian as its square, and its
self-adjointness is with respect to the analytic form on the Hilbert module. The relation between
the two is the relation between the symbol and the operator: $c(\sum e_a\xi_a)$ is the symbol of
$D$, the finite-dimensional Dirac element is the same expression evaluated at the covector of the
generators, and the passage from the algebraic to the analytic statement is the passage from the
Fourier symbol to the operator by the spectral theorem.

**Remark (the picture).** The article completes the operator-theoretic account of the Hermitian
refinement: the two Hermitian Dirac operators are isotropic and anticommute, their sum is the
Hermitian Dirac operator with square the Laplacian and with the Hermitian form's symmetry, their
difference is the Euclidean operator with the antisymmetry and the formal adjoint $\bar D$, and the
split of the Laplacian is the statement that the two square roots agree on the second power. The
Fischer decomposition, the integral formulae and the kernel are the remaining faces of the same
object, developed in *The Hermitian Dirac Operator and the Fischer Decomposition*, *The Hermitian
Cauchy Integral and the Boundary Values* and *The Hermitian Cauchy Kernel as an Adjoint*.

## Summary

The **Hermitian Dirac operator** of the complex refinement is
$\mathcal{D}=\partial_{\underline z}+\partial_{\bar z}$, the sum of the two Hermitian Dirac
operators; because each square vanishes,
$\mathcal{D}^2=\{\partial_{\underline z},\partial_{\bar z}\}=\tfrac14\Delta_{2n}$, so $\mathcal{D}$
is a square root of the Laplacian, the other being the Euclidean operator
$D=2(\partial_{\underline z}-\partial_{\bar z})$ with $D^2=-\Delta_{2n}$. The involution $*$ of the
Hermitian form interchanges the two halves,
$(\partial_{\underline z})^{\dagger}\sim\partial_{\bar z}$ and
$(\partial_{\bar z})^{\dagger}\sim\partial_{\underline z}$, so the **sum** is symmetric with respect
to the form while the **difference** is antisymmetric; this is the operator-theoretic meaning of the
split. On the Hilbert module $L^2(\mathbb{R}^{2n};\mathcal{S})$, on the Sobolev space $H^1$,
$\mathcal{D}$ is essentially self-adjoint, its closure has square the Laplacian, and its spectrum is
the whole real line, the symbol
$\sigma(\mathcal{D})(\xi)=c(\sum_jf_j\xi_{z_j})+c(\sum_jf_j^{*}\xi_{\bar z_j})$ having square
$\tfrac14|\xi|^2$ and taking all real values; the Hermitian choice of square root is the one that
absorbs the factor that makes the operator self-adjoint in place of the Euclidean operator, whose
self-adjoint variant is $iD$. The quaternionic refinement has the four-operator analogue. The
finite-dimensional **Dirac element** $D_{\mathrm{alg}}=\sum_kL_{e_k}$ of Part II's *Dirac Operators
with Hermitian Adjoint* is the same expression as the symbol of the differential operator and is
distinguished from it: the one acts on the module, the other on functions, and they are related by
the Fourier transform and the spectral theorem. The split, the Fischer decomposition and the
integral theory are *The Hermitian Dirac Operator and the Fischer Decomposition*, *The Hermitian
Cauchy Integral and the Boundary Values* and *The Hermitian Cauchy Kernel as an Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\partial_{\underline z},\partial_{\bar z}$ | Hermitian Dirac operators; isotropic, anticommuting |
| $\mathcal{D}=\partial_{\underline z}+\partial_{\bar z}$ | Hermitian Dirac operator; $\mathcal{D}^2=\tfrac14\Delta_{2n}$ |
| $D=2(\partial_{\underline z}-\partial_{\bar z})$ | Euclidean operator; $D^2=-\Delta_{2n}$; formal adjoint $D^{\dagger}=-\bar D$ |
| $(\partial_{\underline z})^{\dagger}\sim\partial_{\bar z}$, $(\partial_{\bar z})^{\dagger}\sim\partial_{\underline z}$ | Conjugation interchanging the halves |
| $\langle\mathcal{D}f,g\rangle=\langle f,\mathcal{D}g\rangle$ | Symmetry with respect to the form |
| $\sigma(\mathcal{D})(\xi)=c(\sum_jf_j\xi_{z_j})+c(\sum_jf_j^{*}\xi_{\bar z_j})$ | Symbol; square $\tfrac14|\xi|^2$ |
| $D_{\mathrm{alg}}=\sum_kL_{e_k}$ | Finite-dimensional Dirac element (Part II) |
| $iD$ | The self-adjoint variant of the Euclidean operator |

## Further Reading

- F. Brackx, H. De Schepper and F. Sommen, *Hermitean Clifford Analysis*, for the Hermitian Dirac operators and their combination.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for Dirac operators, their squares and the Laplace-type operators.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the operator theory of Dirac-type operators and their self-adjointness.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the module and form background of the analytic statements.
