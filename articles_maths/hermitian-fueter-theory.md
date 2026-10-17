
# __Hermitian Fueter Theory__

## Introduction

Fueter theory is the function theory of the quaternionic variable built from the Fueter operator
$\bar\partial=\partial/\partial q_t+\sum_{i\in\{x,y,z\}}e_i\,\partial/\partial q_i$; *Fueter Theory* develops it in this category,
with the factorisation of the Laplacian, the Cauchy–Fueter kernel, Fueter's theorem and the axial
description. This article treats the Hermitian refinement of that theory: the same four-dimensional
quaternionic setting read with the Hermitian structure of *Hermitian Quaternionic Analysis and the
Conjugate Cauchy–Riemann Operator*, in which the operator is split and the functions are the
simultaneous null solutions of the split system.

Two features of Fueter theory make the refinement interesting. The first is the **axial**
description: a regular function constant on the spheres about the real axis is determined by two
real functions $A(q_t,r),B(q_t,r)$ of the axial radius $r=|\vec q|$, satisfying the reduced
Cauchy–Riemann system $A_0=3B+rB_r$, $B_0=-A_r/r$, and Fueter's theorem constructs the regular
functions from the holomorphic ones through this reduction. The second is the **spherical**
structure: the homogeneous regular polynomials, the Fueter variables and the Fueter polynomials, and
their organisation by the Fischer decomposition. The Hermitian refinement keeps both, with the
operator replaced by the Hermitian pair and the class replaced by the Hermitian monogenic functions;
what changes is the size of the classes and the symmetry group.

The setting is four-dimensional, and the conventions are those of *Fueter Theory* and *Hermitian
Quaternionic Analysis*: the quaternions $\mathbb{H}$ with basis $1,\vec e_x,\vec e_y,\vec e_z$, the variable
$q=q_t+\vec q$, the Fueter operator $\bar\partial$ of *Fueter Theory*, and the Hermitian
construction in $N=4$ dimensions with the four twisted vectors and the four Hermitian Dirac
operators. The complex refinement is *Hermitian Clifford Analysis and the Hermitian Monogenic
Functions*; the operator and the Fischer decomposition are *The Hermitian Dirac Operator and the
Fischer Decomposition*; the integral theory is *The Hermitian Cauchy Integral and the Boundary
Values*; the ordinary Fueter theory is *Fueter Theory*, and the biquaternionic and
split-quaternionic Fueter theories are Part V, cited as deferrals.

## The Fueter Operator and its Hermitian Split

### The Two Operators

**Definition.** The **Fueter operator** and its conjugate are

$$
\bar\partial = \partial/\partial q_t+\vec e_x\,\partial/\partial q_x+\vec e_y\,\partial/\partial q_y+\vec e_z\,\partial/\partial q_z , \qquad
\partial = \partial/\partial q_t-\vec e_x\,\partial/\partial q_x-\vec e_y\,\partial/\partial q_y-\vec e_z\,\partial/\partial q_z ,
$$

acting on $C^1$ functions $f:\Omega\to\mathbb{H}$; they satisfy
$\bar\partial\partial=\partial\bar\partial=\Delta$, and the vector parts
$\partial/\partial\vec X=\sum_{i\in\{x,y,z\}}e_i\,\partial/\partial q_i$ and its negative are the objects that the Hermitian
refinement of *Hermitian Quaternionic Analysis* splits further.

**Proposition (the vector part and its Hermitian split).** Put $N=4$ and read $\mathbb{R}^4$ as the
quaternions with the four directions $\vec e_x,\vec e_y,\vec e_z,e_4$, where $e_4$ is the fourth generator of
$\mathrm{Cl}_{0,4}$ and the identification of the four Euclidean directions with the quaternion
basis is the one appropriate to the Hermitian construction. Then the vector part
$\partial/\partial X=\sum_{a=1}^{4}e_a\,\partial/\partial x_a$ satisfies $(\partial/\partial X)^{2}=-\Delta_4$, and the four
Hermitian Dirac operators $\partial/\partial Z_0,\dots,\partial/\partial Z_3$ of *Hermitian Quaternionic Analysis*
split it:

$$
\partial/\partial X = \text{ (a fixed quaternionic combination of the four } \partial/\partial Z_r\,\text{)} ,
\qquad
\Delta_4 = 16\sum_{r\in\{t,x,y,z\}}\partial/\partial Z_r\,(\partial/\partial Z_r)^{\dagger} .
$$

*Proof.* The four Hermitian operators are invertible $\mathbb{H}$-linear combinations of
$\partial/\partial X_0,\dots,\partial/\partial X_3$ by the Hadamard matrix with $SS^{\mathsf T}=4I_4$; in
dimension $4$ each $X_r$ is a single sum over $l=1$, and the Euclidean vector is recovered as a
quaternionic combination of the twisted ones. The split of the Laplacian is the theorem of
*Hermitian Quaternionic Analysis*, of which the four-dimensional case is the instance $n=1$.

**Remark (the two structures kept apart).** The Fueter operator carries the scalar direction
$\partial/\partial q_t$ with coefficient $1$, whose square is $+1$; the Hermitian construction uses the pure
vector part, whose generators all square to $-1$. The two structures therefore meet on the vector
part and not on the scalar one: the Hermitian refinement of Fueter theory is the Hermitian
refinement of the vector part, and the scalar direction plays the role of an extra axial variable.
This is why the axial description — in which the scalar variable $q_t$ is paired with the radius $r$
— is the natural form of the Hermitian Fueter theory, and the reason the class of Hermitian
monogenic functions is a restricted class of regular functions rather than a separate theory.

## The Axial Structure

### The Axial Form

**Definition.** Write the quaternionic variable as $q=q_t+\vec q$ with $r=|\vec q|$. A function is
**axial** when it is invariant under the rotations of $\vec q$, equivalently when it has the form

$$
f(q) = A(q_t,r)+\vec q\,B(q_t,r)
$$

away from the axis $\vec q=0$, with $A,B$ scalar-valued.

**Proposition (the axial regular functions).** The function $f=A+\vec qB$ is left regular for the
Fueter operator exactly when

$$
A_0 = 3B+rB_r , \qquad B_0 = -\tfrac{1}{r}A_r ,
$$

the **reduced Cauchy–Riemann system** of *Fueter Theory*; equivalently, with $A=\phi$, $B=\psi/r$,
the system $\phi_0=\psi_r+2\psi/r$, $\psi_0=-\phi_r$. Every axial regular function is determined by
the pair $(A,B)$ of scalar functions of the two variables $(q_t,r)$, and the class of such pairs is
the axial quaternionic function theory.

*Proof.* Quoted from *Fueter Theory*: the derivation uses
$D(A+\vec qB)=(A_0-3B-rB_r)+(B_0+A_r/r)\vec q$, which follows from $\sum_ie_i\vec q\,q_i=-r^2$ and
the radial identities for the Laplacian in the axial coordinates. The substitution
$A=r^2\phi,B=r\psi$ carries the system into the displayed pair.

### The Spherical Reduction of the Hermitian System

**Theorem (the Hermitian system on axial functions).** On an axial function the four Hermitian Dirac
operators reduce to a system of first-order operators in the two axial variables $(q_t,r)$: the
derivatives $\partial/\partial X_r$ act on the axial form by combinations of $\partial/\partial q_t$ and
$\partial/\partial r$ with coefficients rational in $r$, so the Hermitian monogenicity conditions are a
system of four ordinary differential equations in $(q_t,r)$ for the pair $(A,B)$.

*Proof.* The twisted vectors $X_r$ are constant-coefficient combinations of the Euclidean
derivatives $\partial/\partial x_a$, and an axial function depends on the coordinates only through $q_t$
and $r=|\vec q|$; the chain rule gives
$\partial/\partial x_a=(\partial/\partial x_a\,q_t)\partial/\partial q_t +(\partial/\partial x_a\,r)\partial/\partial r$, with
$\partial/\partial x_a\,r=q_a/r$, and substituting the twisted patterns gives the reduction. The resulting
system is overdetermined in four equations for the two scalar functions $(A,B)$, and its solvability
is the sharpening that the Hermitian refinement imposes on the axial regular functions.

**Corollary (the Hermitian axial functions).** The Hermitian monogenic axial functions form a proper
subclass of the axial regular functions, determined by the reduction of the theorem; in the extreme
cases $A=0$ and $B=0$ of *Fueter Theory* — giving $B=cr^{-3}$ and $A=A(q_t)$ respectively — the
Hermitian conditions select the members of the corresponding families that are also annihilated by
the conjugate Hermitian operators, and the surviving functions are the axial Hermitian monogenic
functions.

*Proof.* The class is the simultaneous kernel of the four reduced operators; the two extreme
families are those of *Fueter Theory*, and imposing the additional equations restricts them.

## Fueter's Theorem in the Hermitian Setting

**Theorem (Fueter; quoted).** Let $f=u+iv$ be holomorphic on a domain of $\mathbb{C}$, and let
$f^{\mathrm{ax}}(q)=u(q_t,r)+(\vec q/r)v(q_t,r)$ be its axial extension. Then $F=\Deltaf^{\mathrm{ax}}$ is left
and right regular for the Fueter operator, the construction shifting the homogeneity by two and
annihilating the constant and the identity.

*Proof.* Quoted from *Fueter Theory* (Fueter 1935; Sudbery). The verification is the computation in
axial coordinates: the pair $(A,B)$ built from $(u,v)$ by the Laplacian satisfies the reduced system
$A_0=3B+rB_r$, $B_0=-A_r/r$ exactly when $f$ is holomorphic.

**Proposition (the Hermitian refinement of the construction).** The Hermitian Fueter construction is
the restriction of the construction above to the axial functions whose axial pair $(A,B)$ satisfies,
in addition, the Hermitian axial system of the preceding section; the image is the Hermitian
monogenic axial functions, and it is obtained from the holomorphic functions by the same radial
extension followed by the Hermitian projection.

*Proof.* The Fueter construction produces regular functions; the Hermitian monogenic axial functions
are those regular axial functions that also satisfy the Hermitian axial system; the projection onto
them is the operator of the Hermitian theory applied to $F=\Deltaf^{\mathrm{ax}}$, and it commutes with the
axial reduction because both are rotation-invariant. The statement is the Hermitian form of the
classical construction; the explicit basis of the image is obtained by applying the Hermitian
Fischer decomposition of *The Hermitian Dirac Operator and the Fischer Decomposition* to the Fueter
polynomials.

**Remark (what the refinement shifts).** In the classical theory the point of Fueter's theorem is
that it is *not* the naive substitution of a quaternion for the complex variable but a radial
extension followed by the Laplacian, and this is what makes the quaternionic theory a genuine
generalisation of complex analysis. The Hermitian refinement preserves this: the construction is
still the radial extension and the Laplacian, and the refinement adds the Hermitian projection. What
the refinement changes is the target class — Hermitian monogenic instead of regular — and hence the
size of the image, which is smaller because the Hermitian system is a pair (respectively four) of
equations.

## The Spherical Structure

**Remark (the spherical monogenics).** The homogeneous axial regular functions are the spherical
part of the theory: the Fueter variables $z_i=q_te_i-q_i$, the Fueter polynomials, and the solid
spherical monogenics of *Fueter Theory* and *Clifford Analysis*. The Hermitian refinement organises
the same polynomials by the Hermitian Fischer decomposition, whose multiplier $Z$ is the Hermitian
variable and whose kernel is the space of Hermitian monogenic polynomials; the Hermitian monogenic
spherical functions are those whose axial pair satisfies both the Fueter and the Hermitian
conditions, and their count is the dimension of the joint kernel, computed in *The Hermitian Dirac
Operator and the Fischer Decomposition*. The spherical monogenics of the ordinary theory are the
larger class from which the Hermitian ones are selected.

**Remark (the symmetry groups).** The Fueter theory of this article is invariant under the rotations
of the imaginary part — the group $SU(2)$ of unit quaternions acting on $\vec q$ — and this is what
makes the axial description available; the Hermitian refinement enlarges the structure to the
Hermitian symmetry group of the split, which contains the $\mathrm{U}(1)$ or $\mathrm{U}(2)$ structure of the
quaternionic central algebra. The two actions commute on the axial functions, and the axial
reduction is the restriction to the invariants of the first. The conformal and the spin symmetries
of the corresponding Clifford theories are Part II's and Part IV's, and the Vahlen action is
*Clifford Analysis*'s.

## Summary

Hermitian Fueter theory is the quaternionic Fueter theory of *Fueter Theory* read with the Hermitian
split of *Hermitian Quaternionic Analysis*: in four dimensions the vector part
$\partial/\partial X=\sum_{a=1}^{4}e_a\,\partial/\partial x_a$, with $(\partial/\partial X)^{2}=-\Delta_4$, splits into the four
Hermitian Dirac operators, and the Fueter operator differs from it by the scalar direction
$\partial/\partial q_t$, whose square is $+1$. The axial structure survives: the axial functions
$f=A(q_t,r)+\vec qB(q_t,r)$ are regular exactly when $A_0=3B+rB_r$, $B_0=-A_r/r$, and on such
functions the four Hermitian Dirac operators reduce to a system of ordinary differential equations
in the two axial variables, whose simultaneous solutions are the axial Hermitian monogenic
functions, a proper subclass of the axial regular ones. **Fueter's theorem**, $F=\Deltaf^{\mathrm{ax}}$ for
the axial extension of a holomorphic function, is quoted from the ordinary theory, and its Hermitian
refinement is the same construction followed by the Hermitian projection; what the refinement
changes is the target class, not the construction. The spherical structure — the Fueter variables,
the Fueter polynomials and the solid spherical monogenics — is refined by the Hermitian Fischer
decomposition, and the symmetry group of the axial description, the unit quaternions acting on
$\vec q$, is contained in the Hermitian symmetry group of the split. The complex case is *Hermitian
Clifford Analysis and the Hermitian Monogenic Functions*; the integral theory is *The Hermitian
Cauchy Integral and the Boundary Values*; the biquaternionic and split-quaternionic Fueter theories
are Part V's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar\partial=\partial/\partial q_t+\sum_ie_i\,\partial/\partial q_i$, $\partial$ | Fueter operator and its conjugate; $\partial\bar\partial=\Delta$ |
| $\partial/\partial X=\sum_{a=1}^4e_a\,\partial/\partial x_a$ | Vector part; $(\partial/\partial X)^{2}=-\Delta_4$ |
| $\partial/\partial Z_0,\dots,\partial/\partial Z_3$ | Hermitian Dirac operators; $\Delta_4=16\sum_r\partial/\partial Z_r\,(\partial/\partial Z_r)^{\dagger}$ |
| $q=q_t+\vec q$, $r=|\vec q|$ | Quaternionic and axial variables |
| $f=A(q_t,r)+\vec qB(q_t,r)$ | Axial form of a function |
| $A_0=3B+rB_r$, $B_0=-A_r/r$ | Reduced Cauchy–Riemann system |
| $f^{\mathrm{ax}}=u+\frac{\vec q}{r}v$, $F=\Deltaf^{\mathrm{ax}}$ | Fueter construction; Hermitian refinement adds the Hermitian projection |
| $z_i=q_te_i-q_i$, $V_\lambda$ | Fueter variables and Fueter polynomials |
| $SU(2)$, $\mathrm{U}(2)$ | Axial symmetry group; Hermitian symmetry group of the split |

## Further Reading

- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u=0$ und $\Delta\Delta u=0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* 7 (1935), for the original regularity and the construction from holomorphic functions.
- A. Sudbery, "Quaternionic Analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* 85 (1979), for the axial description, the Fueter variables and the Taylor expansion.
- F. Brackx, H. De Schepper and F. Sommen, *Hermitean Clifford Analysis*, for the Hermitian split used here.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Clifford–Fueter background and the spherical monogenics.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the axial and spherical computations.
