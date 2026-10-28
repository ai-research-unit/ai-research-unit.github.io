# __The Involution and the Hermitian Structure of $M_6(\mathbb{C})$__

## Introduction

The conjugate transpose

$$
A\longmapsto A^*=\overline{A}^{\mathsf T}
$$

is a conjugate-linear involution of $M_6(\mathbb{C})$. Its fixed points are the Hermitian matrices, its antiefixed points the skew-Hermitian ones, and its isometries the $*$-unitary matrices. The Hermitian form

$$
\langle A,B\rangle=\operatorname{tr}(A^*B)
$$

is positive definite, and it defines the Frobenius norm

$$
\lVert A\rVert_F^2=\operatorname{tr}(A^*A)=\sum_{i,j}\lvert a_{ij}\rvert^2 .
$$

The skew-Hermitian matrices form the real Lie algebra $\mathfrak{u}(6)$ of dimension $36$; the traceless skew-Hermitian matrices form $\mathfrak{su}(6)$ of dimension $35$. The form is definite, so its only isotropic vector is $0$. This is the sharp contrast with the biquaternion algebra, whose conjugation is $\mathbb{C}$-linear and whose trace form has a nonzero null cone.

The article assumes the coordinates and the trace pairing of *The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$*. It uses no topology beyond the finite-dimensional metric. The polar decomposition is *The Polar Decomposition of $M_6(\mathbb{C})$*; the $*$-unitary group is *The Exponential and the Lie Group of $M_6(\mathbb{C})$*; the real forms of the biquaternion algebra are *The Biquaternion Algebra and Its Vector Spaces*.

## The Conjugate Transpose

### Definition

**Definition.** The **conjugate transpose** of $A$ is

$$
(A^*)_{ij}=\overline{a_{ji}} .
$$

**Theorem.** The map $A\mapsto A^*$ is conjugate-linear and involutive:

$$
(A+B)^*=A^*+B^*,\qquad
(\lambda A)^*=\overline{\lambda}A^*,\qquad
(A^*)^*=A,
$$

and it reverses products:

$$
(AB)^*=B^*A^* .
$$

**Proof.** The entries of $(AB)^*$ are $\overline{(AB)_{ji}}=\sum_k\overline{a_{jk}b_{ki}}=\sum_k\overline{b_{ki}}\,\overline{a_{jk}}=(B^*A^*)_{ij}$.

**Corollary (the *-algebra).** $M_6(\mathbb{C})$ is a complex *-algebra with the identity $I_6^*=I_6$.

**Proof.** The four identities above are the axioms of a *-algebra.

### Hermitian, Skew-Hermitian and $*$-Unitary Elements

**Definition.** An element $A$ is

- **Hermitian** if $A^*=A$;
- **skew-Hermitian** if $A^*=-A$;
- **$*$-unitary** if $A^*A=AA^*=I_6$;
- **normal** if $A^*A=AA^*$.

**Theorem (the Cartesian decomposition).** Every $A$ has a unique decomposition

$$
A=H+\mathrm iK,
\qquad
H=\frac{A+A^*}{2},\quad
K=\frac{A-A^*}{2\mathrm i},
$$

with $H,K$ Hermitian. The real vector space of Hermitian matrices has dimension $36$, and

$$
M_6(\mathbb{C})=\operatorname{Herm}_6\oplus\mathrm i\operatorname{Herm}_6
$$

as real vector spaces, of real dimension $72$.

**Proof.** $H$ and $K$ are Hermitian by construction, and $A=H+\mathrm iK$. The Hermitian matrices are the fixed points of the conjugate-linear involution $*$; a conjugate-linear involution on a complex vector space of dimension $36$ has a real fixed space of dimension $36$. The imaginary multiples fill the other half.

**Corollary (the Hermitian coordinates).** A Hermitian matrix has $6$ real diagonal entries and $15$ complex off-diagonal entries, hence $6+2\cdot15=36$ real dimensions. A skew-Hermitian matrix has $6$ purely imaginary diagonal entries and $15$ complex off-diagonal entries, also $36$ real dimensions.

**Proof.** The diagonal of a Hermitian matrix is real; the off-diagonal entries are paired by $a_{ji}=\overline{a_{ij}}$. For skew-Hermitian, the diagonal is purely imaginary and $a_{ji}=-\overline{a_{ij}}$.

**Theorem (the $*$-unitary group).** The $*$-unitary elements form the group

$$
U(6)=\{U\in GL_6(\mathbb{C}):U^*U=I_6\},
$$

of real dimension $36$; the special $*$-unitary elements

$$
SU(6)=\{U\in U(6):\det U=1\}
$$

form a subgroup of real dimension $35$.

**Proof.** $U(6)$ is the zero set of the $36$ real equations $U^*U=I_6$ in the $72$ real coordinates, and the differential is surjective (the Lie algebra computation below); so the dimension is $72-36=36$. The determinant is a homomorphism onto $U(1)$ with derivative the trace, so its kernel has dimension $35$.

**Corollary (the center).** The center of $U(6)$ is $U(1)I_6$, and

$$
PU(6)=U(6)/U(1)I_6
$$

has dimension $35$.

**Proof.** A $*$-unitary matrix commuting with all unitaries is scalar; the scalar unitaries are $U(1)I_6$. The quotient by a one-dimensional center has dimension $36-1=35$.

### The Lie Algebra

**Definition.** The **$*$-unitary Lie algebra** is

$$
\mathfrak{u}(6)=\{X\in M_6(\mathbb{C}):X^*=-X\},
$$

and the **special $*$-unitary Lie algebra** is

$$
\mathfrak{su}(6)=\{X\in\mathfrak{u}(6):\operatorname{tr}X=0\}.
$$

**Theorem.** $\mathfrak{u}(6)$ is a real Lie algebra of dimension $36$, $\mathfrak{su}(6)$ is a real Lie algebra of dimension $35$, and

$$
\mathfrak{u}(6)=\mathfrak{u}(1)\oplus\mathfrak{su}(6),
\qquad
\mathfrak{u}(1)=\mathrm i\mathbb{R}I_6 .
$$

**Proof.** If $X,Y$ are skew-Hermitian, then $[X,Y]^*=[Y^*,X^*]=[-Y,-X]=-[X,Y]$; the commutator is skew-Hermitian. The trace is linear, so the traceless subspace is an ideal. The scalar skew-Hermitian matrices are $\mathrm i\mathbb{R}I_6$, of dimension one; the traceless skew-Hermitian matrices have dimension $36-1=35$, and every skew-Hermitian matrix is the sum of its scalar trace part and its traceless part.

**Theorem (the exponential).** The Lie algebra $\mathfrak{u}(6)$ is the tangent space of $U(6)$ at the identity, and the exponential map

$$
\exp:\mathfrak{u}(6)\longrightarrow U(6)
$$

is surjective.

**Proof.** The curve $t\mapsto e^{tX}$ is $*$-unitary for $X$ skew-Hermitian, and its derivative at zero is $X$; the tangent space is exactly $\mathfrak{u}(6)$. Every $*$-unitary matrix is diagonalizable with eigenvalues on the unit circle, so it is the exponential of a skew-Hermitian matrix (the diagonal logarithm).

## The Positive Definite Trace Form

### Definition

**Definition.** The **Hermitian trace form** is

$$
\langle A,B\rangle=\operatorname{tr}(A^*B).
$$

**Theorem.** The form is Hermitian, positive definite:

$$
\langle A,B\rangle=\overline{\langle B,A\rangle},
\qquad
\langle A,A\rangle=\operatorname{tr}(A^*A)=\sum_{i,j}\lvert a_{ij}\rvert^2\ge0,
$$

with equality if and only if $A=0$.

**Proof.** $\operatorname{tr}(A^*B)=\sum_{i,j}\overline{a_{ij}}b_{ij}$, the Euclidean inner product of the entries; the conjugate symmetry is immediate, and the sum of squares vanishes only when every entry vanishes.

**Corollary (the Frobenius norm).** The form defines the **Frobenius norm**

$$
\lVert A\rVert_F=\sqrt{\langle A,A\rangle}
=\left(\sum_{i,j}\lvert a_{ij}\rvert^2\right)^{1/2},
$$

and the Cauchy–Schwarz and triangle inequalities hold.

**Proof.** The norm is the Euclidean norm on $\mathbb{C}^{36}\cong\mathbb{R}^{72}$; the inequalities are those of a positive definite inner product.

**Corollary (the real and imaginary parts).** For $A=X+\mathrm iY$,

$$
\operatorname{Re}\langle A,B\rangle
=\sum_{i,j}(x_{ij}u_{ij}+y_{ij}v_{ij}),
\qquad
\operatorname{Im}\langle A,B\rangle
=\sum_{i,j}(x_{ij}v_{ij}-y_{ij}u_{ij}).
$$

The real part is the Euclidean inner product of the $72$ real coordinates; the imaginary part is a symplectic form.

**Proof.** Expand $\operatorname{tr}(A^*B)=\sum_{ij}(x_{ij}-\mathrm iy_{ij})(u_{ij}+\mathrm iv_{ij})$ and take real and imaginary parts.

### The Adjoint Properties

**Theorem.** The form satisfies

$$
\langle AB,C\rangle=\langle B,A^*C\rangle,
\qquad
\langle A,BC\rangle=\langle AC^*,B\rangle .
$$

**Proof.** $\operatorname{tr}((AB)^*C)=\operatorname{tr}(B^*A^*C)=\langle B,A^*C\rangle$; the second is the same with the roles of the factors exchanged.

**Corollary (the adjoint).** The adjoint of left multiplication by $A$ with respect to the Hermitian form is left multiplication by $A^*$; the adjoint of right multiplication by $B$ is right multiplication by $B^*$.

**Proof.** Read the two identities as the definition of the adjoint.

**Remark (the contrast with the complex bilinear form).** The complex bilinear trace pairing $\operatorname{tr}(AB)$ of *The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$* is indefinite; the Hermitian form $\operatorname{tr}(A^*B)$ is positive definite. They agree on the real subspace of symmetric real matrices, where $A^*=A^{\mathsf T}$ and the entries are real, but not in general.

### The Unit Sphere

**Definition.** The **unit sphere** of $M_6(\mathbb{C})$ is

$$
S^{71}=\{A:\lVert A\rVert_F=1\}.
$$

**Proposition.** $S^{71}$ is a compact real manifold of dimension $71$; the unit ball is the set $\lVert A\rVert_F\le1$.

**Proof.** It is the Euclidean unit sphere in $\mathbb{R}^{72}$.

**Remark (the topology is the finite-dimensional one).** The Frobenius norm is equivalent to the operator norm and to every other norm on the finite-dimensional space; the metric topology is the standard one. The topological consequences are in *The Topology of $M_6(\mathbb{C})$*.

## The Real Forms

### The $*$-Unitary Form

**Theorem.** $\mathfrak{u}(6)$ is a real form of the complex Lie algebra $\mathfrak{gl}_6(\mathbb{C})$:

$$
\mathfrak{u}(6)\otimes_{\mathbb{R}}\mathbb{C}\cong\mathfrak{gl}_6(\mathbb{C}),
\qquad
X+\mathrm iY\longmapsto X+\mathrm iY .
$$

**Proof.** Every complex matrix is $X+\mathrm iY$ with $X,Y$ skew-Hermitian: given $A$, set $X=(A-A^*)/2$ and $Y=(A+A^*)/(2\mathrm i)$; both are skew-Hermitian, and $X+\mathrm iY=A$. The real dimension $36+36=72$ matches.

**Corollary (the Cartan decomposition).** The Cartan involution

$$
\theta(A)=-A^*
$$

is an involution of the real Lie algebra $\mathfrak{gl}_6(\mathbb{C})$, with fixed set $\mathfrak{u}(6)$ and $-1$ eigenspace $\mathrm i\mathfrak{u}(6)$, the Hermitian matrices. Hence

$$
\mathfrak{gl}_6(\mathbb{C})=\mathfrak{u}(6)\oplus\mathrm i\mathfrak{u}(6)
$$

as real vector spaces, and the symmetric space $GL_6(\mathbb{C})/U(6)$ is the space of positive definite Hermitian matrices.

**Proof.** $\theta$ is an involution because $(A^*)^*=A$; $\theta(X)=X$ iff $X^*=-X$; $\theta(X)=-X$ iff $X^*=X$. The quotient is the symmetric space of the Cartan involution, identified with the positive definite Hermitian matrices by the polar decomposition.

### The Special $*$-Unitary Form

**Theorem.** $\mathfrak{su}(6)$ is a simple real Lie algebra of dimension $35$, and its complexification is $\mathfrak{sl}_6(\mathbb{C})$.

**Proof.** The complexification of the traceless skew-Hermitian matrices is the traceless complex matrices, because the trace is complex-linear and the decomposition $A=X+\mathrm iY$ preserves tracelessness. Simplicity is the standard simplicity of $\mathfrak{su}(n)$ for $n\ge2$.

**Theorem (the Killing form).** On $\mathfrak{sl}_6(\mathbb{C})$ the Killing form is $12\operatorname{tr}(XY)$; on $\mathfrak{su}(6)$ it is negative definite.

**Proof.** The Killing form of $\mathfrak{gl}_6$ is $12\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$, and the second term vanishes on the traceless subalgebra. For $X\in\mathfrak{su}(6)$, $\operatorname{tr}(X^2)=-\operatorname{tr}(X^*X)=-\sum_{ij}\lvert x_{ij}\rvert^2<0$ for $X\neq0$.

**Corollary (the trace form versus the Killing form).** The Hermitian trace form $\operatorname{tr}(X^*Y)$ is positive definite on $\mathfrak{u}(6)$; the Killing form is negative definite on $\mathfrak{su}(6)$. The two differ by the sign and by the scalar $12$.

**Proof.** For skew-Hermitian $X$, $\operatorname{tr}(X^*X)=-\operatorname{tr}(X^2)$; the first is positive definite, the second is the Killing form up to $12$ and is negative definite.

## The Definite Form and the Isotropic Set

### The Isotropic Vectors

**Theorem.** The only isotropic vector of the Hermitian trace form is zero:

$$
\langle A,A\rangle=0
\quad\Longleftrightarrow\quad
A=0 .
$$

**Proof.** $\langle A,A\rangle=\sum_{ij}\lvert a_{ij}\rvert^2$; a sum of nonnegative terms vanishes only if every term vanishes.

**Corollary (the isotropic set).** The isotropic set of the Hermitian form is the single point $\{0\}$. There is no nonzero isotropic vector and no null cone, and no zero divisor in the metric sense.

**Proof.** The isotropic set is the zero set of the quadratic form $\langle A,A\rangle$; by the theorem it is $\{0\}$.

### The Contrast with the Biquaternion Algebra

**Theorem (the biquaternion null cone).** In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$, the conjugation is $\mathbb{C}$-linear, and the trace form

$$
\langle A,B\rangle_{\mathbb{B}}=\operatorname{tr}(A^*B)
$$

is indefinite. Its isotropic cone is the zero-divisor cone

$$
\{A\in\mathbb{B}:A\neq0,\ \det A=0\},
$$

which has real dimension $6$ in the eight-dimensional algebra.

**Proof.** The biquaternion conjugation fixes the complex scalars and negates the quaternionic vector part; it is $\mathbb{C}$-linear, not conjugate-linear. The norm $N(A)=\det A$ is the quadratic form of the conjugation, $A^*A=N(A)I_2$, so $\operatorname{tr}(A^*A)=2N(A)$; the isotropic vectors are the zero divisors. The zero-divisor cone is the determinantal variety $\det=0$ in $M_2(\mathbb{C})$, of complex dimension $3$ and real dimension $6$.

**Corollary (the difference).** The standard involution of $M_6(\mathbb{C})$ is conjugate-linear and its trace form is positive definite; the biquaternion conjugation is $\mathbb{C}$-linear and its trace form is indefinite. **The definite form has the single isotropic vector $0$; the biquaternion form has a genuine null cone.**

**Proof.** The conjugate-linear involution gives $\operatorname{tr}(A^*A)=\sum\lvert a_{ij}\rvert^2$; the $\mathbb{C}$-linear one gives $\operatorname{tr}(A^*A)=2\det A$, which changes sign and vanishes on the zero divisors.

**Remark (the two real forms).** The real Lie algebra $\mathfrak{u}(6)$ is a real form of $\mathfrak{gl}_6(\mathbb{C})$; the real associative algebra $M_6(\mathbb{R})$ is a real form of $M_6(\mathbb{C})$ under the conjugation $A\mapsto\overline A$, not under $*$. The Hermitian structure uses $*$; the real structure uses the bar. The two involutions commute, and their composition is the transpose.

**Proof.** $\overline{\overline A}=A$ and $A\mapsto\overline A$ is $\mathbb{C}$-antilinear; its fixed space is $M_6(\mathbb{R})$, of real dimension $36$. The composition $A\mapsto\overline{A}^{\mathsf T}=A^*$ is the conjugate transpose.

## Summary

The conjugate transpose is a conjugate-linear involution. Its Hermitian fixed points have real dimension $36$; its skew-Hermitian antiefixed points form the Lie algebra $\mathfrak{u}(6)$ of dimension $36$, with the traceless ideal $\mathfrak{su}(6)$ of dimension $35$.

$$
\boxed{\ \langle A,B\rangle=\operatorname{tr}(A^*B),\qquad \langle A,A\rangle=\sum_{ij}\lvert a_{ij}\rvert^2,\qquad \langle A,A\rangle=0\iff A=0 .\ }
$$

The form is positive definite and defines the Frobenius norm $\lVert A\rVert_F^2=\sum_{ij}\lvert a_{ij}\rvert^2$; the unit sphere is $S^{71}$. The real part of the form is the Euclidean inner product of the $72$ real coordinates; the imaginary part is symplectic.

The real forms are

$$
\mathfrak{u}(6)=\{X:X^*=-X\},\qquad
\mathfrak{su}(6)=\{X:X^*=-X,\ \operatorname{tr}X=0\},
$$

of dimensions $36$ and $35$; $\mathfrak{u}(6)\otimes\mathbb{C}=\mathfrak{gl}_6(\mathbb{C})$, and $\mathfrak{su}(6)\otimes\mathbb{C}=\mathfrak{sl}_6(\mathbb{C})$. The Cartan decomposition is $\mathfrak{gl}_6=\mathfrak{u}(6)\oplus\mathrm i\mathfrak{u}(6)$.

The definite form has no nonzero isotropic vector. The biquaternion algebra, whose conjugation is $\mathbb{C}$-linear, has the zero-divisor null cone of real dimension $6$.

| Object | Data |
|---|---|
| Conjugate transpose | $A^*=\overline{A}^{\mathsf T}$, conjugate-linear involution |
| Hermitian matrices | real dimension $36$ |
| Skew-Hermitian matrices | real dimension $36$ |
| $*$-Unitary group | $U(6)$, dimension $36$ |
| Special $*$-unitary group | $SU(6)$, dimension $35$ |
| Trace form | $\operatorname{tr}(A^*B)$, positive definite |
| Frobenius norm | $\lVert A\rVert_F^2=\sum\lvert a_{ij}\rvert^2$ |
| Isotropic vectors | only $0$ |
| Biquaternion null cone | zero divisors, real dimension $6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^*$ | the conjugate transpose $\overline{A}^{\mathsf T}$ |
| $\operatorname{Herm}_6$ | the Hermitian matrices, real dimension $36$ |
| $\mathfrak{u}(6)$ | the skew-Hermitian Lie algebra, dimension $36$ |
| $\mathfrak{su}(6)$ | the traceless skew-Hermitian Lie algebra, dimension $35$ |
| $\langle A,B\rangle$ | the Hermitian trace form $\operatorname{tr}(A^*B)$ |
| $\lVert A\rVert_F$ | the Frobenius norm |
| $\theta(A)=-A^*$ | the Cartan involution |
| $\mathbb{B}$ | the biquaternion algebra |

## Further Reading

- [The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m6c.html), for the coordinates and the complex bilinear trace pairing.
- [The Polar Decomposition of $M_6(\mathbb{C})$](the-polar-decomposition-of-m6c.html), for the Cartan decomposition and the positive Hermitian matrices.
- [The Exponential and the Lie Group of $M_6(\mathbb{C})$](the-exponential-and-the-lie-group-of-m6c.html), for the exponential $\mathfrak{u}(6)\to U(6)$.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_6(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m6c.html), for the adjoint action of $U(6)$ and $PU(6)$.
- [The Topology of $M_6(\mathbb{C})$](the-topology-of-m6c.html), for the unit sphere and the Frobenius metric.
- [The Biquaternion Algebra](the-biquaternion-algebra-and-its-vector-spaces.html), for the biquaternion conjugation and its null cone.
- [Hermitian Forms and Unitary Geometry](hermitian-forms-and-unitary-geometry.html), for the general theory.
