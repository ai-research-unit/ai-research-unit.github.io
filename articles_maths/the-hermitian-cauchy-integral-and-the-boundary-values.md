
# __The Hermitian Cauchy Integral and the Boundary Values__

## Introduction

The Hermitian refinement of Clifford analysis replaces the single Cauchy kernel of *Clifford
Analysis* by a matrix of kernels, and the single Cauchy integral formula by a matrix formula from
which the ordinary one is recovered as a special case. This article develops the integral theory:
the Euclidean kernels of the four twisted operators, the Hermitian kernels of the four Hermitian
Dirac operators, the circulant matrix that carries the fundamental solution, the Hermitian
Clifford–Stokes theorem, the corresponding Borel–Pompeiu and Cauchy integral formulae, the
Martinelli–Bochner formula they contain, and the boundary values — the jump relations and the
projections of the Hermitian theory.

The setting is that of *Hermitian Quaternionic Analysis and the Conjugate Cauchy–Riemann Operator*:
the algebra $\mathbb{H}_N=\mathbb{H}\otimes_{\mathbb{R}}\mathrm{Cl}_{0,N}$, $N=4n$, the twisted
vectors $X_0,\dots,X_3$, the Hermitian variables $Z_0,\dots,Z_3$, the Hermitian Dirac operators
$\partial_{Z_0},\dots,\partial_{Z_3}$ and the Hermitian conjugation $*$. The complex case, with two
operators and a circulant $(2\times2)$ matrix, is the instance $n=1$ read in $\mathbb{C}^n$; the
operator and the Fischer decomposition are *The Hermitian Dirac Operator and the Fischer
Decomposition*; the adjoint reading of the kernel is *The Hermitian Cauchy Kernel as an Adjoint*;
the ordinary one-operator integral theory is *The Cauchy Integral Operator* and *Clifford Analysis*,
whose formulae are the one-operator case of those below.

## The Hermitian Cauchy Kernels

### The Euclidean Kernels

**Definition.** The **Euclidean kernels** of the four twisted operators are

$$
F_r(X) = -\frac{X_r}{a_{4n}\,|X|^{4n}} , \qquad
a_{4n} = \frac{2\pi^{2n}}{\Gamma(2n)} = |S^{4n-1}| ,
$$

the area of the unit sphere in $\mathbb{R}^{4n}$; the normalisation is the one of the corpus's
Cauchy kernel $\omega_m^{-1}x^{\natural}|x|^{-m-1}$, for the pure vector variable, where
$\bar X_r=-X_r$ and the sphere is $S^{4n-1}$, and the homogeneity is $1-4n$.

**Proposition (the Euclidean identities).** The Euclidean kernels satisfy

$$
\partial_{X_r}F_r = \delta , \qquad
\partial_{X_r}F_s+\partial_{X_s}F_r = 0 \quad (r\neq s),
$$

the second identity being the operator form of $\{X_r,X_s\}=0$.

*Proof.* $F_r$ is the fundamental solution of $\partial_{X_r}$, which is elliptic with symbol the
pure vector $\sum e_a\xi_a$; the pairing with the second operator vanishes by the anticommutation
relation for the twisted vectors, as computed in *Clifford Analysis*. $\square$

### The Hermitian Kernels and the Circulant Matrix

**Definition.** The **Hermitian kernels** are

$$
E_r(Z) = \frac{Z_r^{*}}{a_{4n}\,|Z|^{4n}} .
$$

**Remark (the kernel is not a fundamental solution).** The kernel $E_r$ is **not** a fundamental
solution of $\partial_{Z_r}$; the four kernels are needed together, and the object that carries the
fundamental solution is a matrix. This is the structural difference from the one-operator theory,
where the kernel and the fundamental solution coincide.

**Definition (the circulant matrices).** With the operators and the kernels of the Hermitian theory,
put

$$
D=\begin{pmatrix}\partial_{Z_0}&\partial_{Z_3}&\partial_{Z_2}&\partial_{Z_1}\\
\partial_{Z_1}&\partial_{Z_0}&\partial_{Z_3}&\partial_{Z_2}\\
\partial_{Z_2}&\partial_{Z_1}&\partial_{Z_0}&\partial_{Z_3}\\
\partial_{Z_3}&\partial_{Z_2}&\partial_{Z_1}&\partial_{Z_0}\end{pmatrix},
\qquad
E=\begin{pmatrix}E_0&E_3&E_2&E_1\\ E_1&E_0&E_3&E_2\\ E_2&E_1&E_0&E_3\\ E_3&E_2&E_1&E_0\end{pmatrix},
$$

the **circulant matrices** of the Hermitian theory.

**Theorem (the fundamental solution).** The matrix $E$ is a fundamental solution of the matrix Dirac
operator $D^{\mathsf T}$:

$$
D^{\mathsf T}E = \delta\,I .
$$

*Proof.* The $(0,0)$ entry of $D^{\mathsf T}E$ is the combination
$\partial_{Z_0}E_0+\partial_{Z_1}E_1+\partial_{Z_2}E_2+\partial_{Z_3}E_3$; evaluating it with the
Hadamard patterns and the Euclidean identities above gives

$$
\partial_{Z_0}E_0+\partial_{Z_1}E_1+\partial_{Z_2}E_2+\partial_{Z_3}E_3
=\tfrac{1}{16}\bigl(4\,\delta(X_0)+4\,\delta(X_1)+4\,\delta(X_2)+4\,\delta(X_3)\bigr)=\delta(Z),
$$

a single delta: the four Euclidean deltas coincide, because the vectors $X_r$ are related to $X$ by
an orthogonal change of variables, and the factor of four in front of each is the contribution of
the four rows of the Hadamard matrix. The sixteen cross terms cancel in antisymmetric pairs, the
cancellation resting on $\partial_{X_r}F_s+\partial_{X_s}F_r=0$ for $r\neq s$, and the diagonal
terms contribute $\delta$ with coefficient one. The same calculus gives the matrix form of the
Laplacian split, $16\,D^{\mathsf T}D^{\dagger}=\Delta_N\,I_4$. The full computation is in *Clifford
Analysis*. $\square$

## The Integral Formulae

### The Hermitian Clifford–Stokes Theorem

**Definition.** Let $\Gamma$ be a compact, oriented $4n$-dimensional manifold with smooth boundary
in $\Omega$, write $\Gamma^+$ for its interior and $\Gamma^-$ for $\Omega\setminus\Gamma$, and let
$N$ be the circulant matrix associated with the four Hermitian conormals

$$
N_r = \tfrac{1}{16}\bigl(n_0+s_{r1}\,i\,n_1+s_{r2}\,j\,n_2+s_{r3}\,k\,n_3\bigr) ,
$$

where $n_0,\dots,n_3$ are the twisted normals of $\partial\Gamma$ and $s_{ra}$ the entries of the
Hadamard matrix.

**Theorem (Hermitian Clifford–Stokes).** For circulant matrix functions $F,G$ of the shape above,

$$
\int_\Gamma\bigl[(FD^{\mathsf T})G+F(D^{\mathsf T}G)\bigr]dV = \int_{\partial\Gamma}F N^{\mathsf T}G\,dS .
$$

*Proof.* The identity is the divergence theorem for the matrix-valued field built from $F,G$ and the
Hermitian conormals; the two terms on the left are the two ways the matrix operator $D^{\mathsf T}$
can act, and the right-hand side is the boundary flux. The statement is the matrix form of the
Clifford–Stokes theorem of the one-operator theory, and the circulant shape is required so that the
conormal matrix multiplies in the correct order. $\square$

### Borel–Pompeiu and Cauchy

**Theorem (Q-Hermitian Borel–Pompeiu).** With $E$ the fundamental solution above,

$$
\int_{\partial\Gamma}E(Z-V)N^{\mathsf T}(Z)G(X)\,dS(X)-\int_\Gamma E(Z-V)\bigl[D^{\mathsf T}G(X)\bigr]dV(X)
=\begin{cases}G(Y),&Y\in\Gamma^+,\\ O,&Y\in\Gamma^-,\end{cases}
$$

for a $C^1$ matrix function $G$.

*Proof.* Apply the Hermitian Clifford–Stokes theorem to the field built from $E(Z-\cdot)$ and $G$ on
the domain punctured at $Z$; the volume term collects $D^{\mathsf T}G$ and the punctured domain
supplies the delta, exactly as in the one-operator Cauchy–Pompeiu formula of *Clifford Analysis*.
$\square$

**Corollary (Q-Hermitian Cauchy integral formula).** When the volume term vanishes because $G$ is
$q$-Hermitian monogenic, the Borel–Pompeiu formula becomes the **Q-Hermitian Cauchy integral
formula**

$$
\int_{\partial\Gamma}E(Z-V)N^{\mathsf T}(Z)G(X)\,dS(X) = \begin{cases}G(Y),&Y\in\Gamma^+,\\ O,&Y\in\Gamma^-,\end{cases}
$$

with the same right-hand side. Applied to the diagonal matrix whose four diagonal entries coincide
with a single function $g$, the two statements become the corresponding formulae for $g$, and the
kernel $E$ is the quaternionic **Hermitian Cauchy kernel**.

**Remark (the special case).** In a special case the representation reduces to the
**Martinelli–Bochner type formula**

$$
\sum_{s=0}^{3}\Bigl[\int_{\partial\Gamma}E_s(Z-V)N_s(Z)g(X)\,dS(X)
-\int_{\Gamma}E_s(Z-V)\bigl(\partial_{Z_s}g(X)\bigr)dV(X)\Bigr]=g(Y),
$$

the integral representation of several complex variables, which is the classical Cauchy formula when
$n=1$. The formula shows the kernel of the Hermitian theory as the several-variable Cauchy kernel:
the bouquet of four kernels, one for each operator, reproduces the Martinelli–Bochner kernel of the
underlying complex structure.

## The Boundary Values

### The Jump Relations

**Remark (the Hermitian Plemelj formulae).** The boundary values of the Hermitian Cauchy integral
are governed by the matrix analogue of the Plemelj–Sokhotski formulae of *The Cauchy Integral
Operator*: the one-sided traces of the integral of a matrix density differ by the density, and their
mean is a singular matrix integral. The involution property of the singular operator, and hence the
projection onto the Hermitian monogenic boundary values, are the matrix form of the one-operator
statements; the trace of the matrix projection is the sum of the four scalar projections, one for
each Hermitian operator.

**Remark (why the matrix is necessary).** In the one-operator theory the kernel $E$ is the
fundamental solution of $D$ and the transform of a boundary datum is the monogenic extension of that
datum. In the Hermitian theory no single kernel is a fundamental solution; the four kernels must be
combined into the circulant matrix, and the boundary values of the four transforms must be read
together. The matrix formulae above are therefore not a generalisation for its own sake: they are
the only form in which the Hermitian Cauchy theory exists, and the ordinary one-operator formulae
are recovered from them by restricting to the diagonal. This is the same phenomenon as in the
operator algebra, where the four Hermitian operators are the components of one object and their
Cauchy kernels the entries of one matrix.

### The Complex Case

**Remark (the $(2\times2)$ case).** For the complex refinement of *Hermitian Clifford Analysis and
the Hermitian Monogenic Functions* the same plan is carried out with two operators and a circulant
$(2\times2)$ matrix: the Euclidean kernels of the two twisted operators, the Hermitian kernels, the
matrix fundamental solution, the Hermitian Clifford–Stokes theorem and the Borel–Pompeiu and Cauchy
formulae follow with two indices in place of four. In this case Hermitian monogenicity is equivalent
to holomorphy in the underlying complex variables in particular cases, and the Hermitian Cauchy
integral reduces to the Martinelli–Bochner formula of several complex variables; the general theory
of that formula is *Several Complex Variables*'. The quaternionic case is the one developed above,
and the complex one is its two-index shadow.

## Summary

The Hermitian integral theory begins with the Euclidean kernels $F_r(X)=-X_r/(a_{4n}|X|^{4n})$ of
the four twisted operators, satisfying $\partial_{X_r}F_r=\delta$ and
$\partial_{X_r}F_s+\partial_{X_s}F_r=0$ for $r\neq s$, and the Hermitian kernels
$E_r(Z)=Z_r^{*}/(a_{4n}|Z|^{4n})$. No single Hermitian kernel is a fundamental solution; the four
combine into the circulant matrix $E$, and with the circulant matrix $D$ of the operators one has
$D^{\mathsf T}E=\delta I$, so the matrix is the fundamental solution of the matrix Dirac operator,
with $16\,D^{\mathsf T}D^{\dagger}=\Delta_NI_4$. The **Hermitian Clifford–Stokes theorem**,
$\int_\Gamma[(FD^{\mathsf T})G+F(D^{\mathsf T}G)]dV=\int_{\partial\Gamma}FN^{\mathsf T}G\,dS$, gives
the **Q-Hermitian Borel–Pompeiu formula** and, when the volume term vanishes, the **Q-Hermitian
Cauchy integral formula**; on diagonal matrices these reduce to the formulae for a single function,
the kernel being the quaternionic Hermitian Cauchy kernel, and a special case is the
**Martinelli–Bochner type formula** of several complex variables, the classical Cauchy formula for
$n=1$. The boundary values obey the matrix form of the Plemelj–Sokhotski formulae, with the singular
matrix integral and the matrix projection onto the Hermitian monogenic boundary values. The complex
refinement uses a $(2\times2)$ circulant matrix, and the one-operator theory is *The Cauchy Integral
Operator*; the general construction is *Clifford Analysis*, and the adjoint reading of the kernel is
*The Hermitian Cauchy Kernel as an Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F_r(X)=-X_r/(a_{4n}|X|^{4n})$ | Euclidean kernels; $\partial_{X_r}F_r=\delta$ |
| $E_r(Z)=Z_r^{*}/(a_{4n}|Z|^{4n})$ | Hermitian kernels |
| $D$, $E$ | Circulant matrices of operators and kernels; $D^{\mathsf T}E=\delta I$ |
| $N$, $N_r$ | Circulant matrix of Hermitian conormals |
| $a_{4n}=|S^{4n-1}|=2\pi^{2n}/\Gamma(2n)$ | Area of the unit sphere in $\mathbb{R}^{4n}$ |
| $\int_\Gamma[(FD^{\mathsf T})G+F(D^{\mathsf T}G)]dV=\int_{\partial\Gamma}FN^{\mathsf T}G\,dS$ | Hermitian Clifford–Stokes |
| $D^{\mathsf T}D^{\dagger}=\tfrac1{16}\Delta_NI_4$ | Matrix Laplacian split |
| $\Gamma^\pm$, $Y$ | Interior and exterior of the domain, and the evaluation point |

## Further Reading

- F. Brackx, H. De Schepper and F. Sommen, *Hermitean Clifford Analysis* and the associated papers, for the Hermitian kernels and the matrix integral formulae.
- R. Rocha-Chávez, M. Shapiro and F. Sommen, *Integral Theorems for Functions and Differential Forms in $\mathbb{C}^m$* (Chapman & Hall, 2002), for the Martinelli–Bochner formula and the several-variable integral theory.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the one-operator Cauchy–Pompeiu formula and the circulant device.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the Clifford–Stokes theorem and the boundary-value framework.
