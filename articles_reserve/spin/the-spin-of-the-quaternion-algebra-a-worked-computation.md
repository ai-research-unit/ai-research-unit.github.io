# __The Spin of the Quaternion Algebra: A Worked Computation__

## Introduction

The table of cases in *The General Definition of Spin* has the following row.

| algebra | base field | pair | elementary spins | adjoint content |
|---|---|---|---|---|
| $\mathbb{H}$ | $\mathbb{R}$ | frame pair in $\mathbb{B}$ | $0,\tfrac12,1$ | $0,1$ |

The pair is not in $\mathbb{H}$. It is in the complexification $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$, which is the biquaternion algebra. The row records the spins of the real carriers after complexification.

### The Result

**The quaternion algebra has no spin pair in itself.** For every $S\in\mathbb{H}$ the eigenvalues of $\operatorname{ad}_S$ are $0$ and $\pm2i\lvert s\rvert$, where $s$ is the imaginary part of $S$. The value $1$ never occurs, so $[S,U]=U$ has no nonzero real solution.

**The pair exists in $\mathbb{B}$.** It is

$$
S=\tfrac{i}{2}e_z,\qquad U=\tfrac{i}{2}e_x-\tfrac12e_y,\qquad V=\tfrac{i}{2}e_x+\tfrac12e_y,
$$

and it satisfies $[S,U]=U$, $[S,V]=-V$, $[U,V]=2S$. The elements $S,U,V$ are not in $\mathbb{H}$.

**The carriers and their spins are these.**

| carrier | action | $\dim_{\mathbb{R}}$ | spin |
|---|---|---|---|
| $\mathbb{H}$ | left multiplication | $4$ | $\tfrac12$ |
| $\mathbb{R}\cdot1$ | adjoint | $1$ | $0$ |
| $\operatorname{Im}\mathbb{H}$ | adjoint | $3$ | $1$ |
| $\mathbb{H}$ | adjoint | $4$ | content $0,1$ |

The last line is the decomposition of the adjoint module, not a fourth carrier. The elementary list is $\Sigma=\{0,\tfrac12,1\}$.

### The Point of the Row

The real dimension of the spin-$\tfrac12$ carrier is $4$, not $2$. The complexification of $\mathbb{H}$ as a left $\mathbb{H}$-module is $\mathbb{C}^2\oplus\mathbb{C}^2=2W_{1/2}$, and the spin is read from that complex module. The bound $2j+1\le N$ applies to the dimension of an irreducible complex carrier, not to the real dimension of a real form. This is why the row has $\tfrac12$ beside $4$.

## The Algebra and Its Matrix Model

**Definition.** The quaternion algebra is

$$
\mathbb{H}=\mathbb{R}\{1,e_x,e_y,e_z\},\qquad
e_x^2=e_y^2=e_z^2=-1,\qquad
e_xe_y=e_z,\quad e_ye_z=e_x,\quad e_ze_x=e_y,
$$

with the opposite products negative, for example $e_ye_x=-e_z$. The conjugate of $q=a+q_xe_x+q_ye_y+q_ze_z$ is $\bar q=a-q_xe_x-q_ye_y-q_ze_z$.

**The matrix model.** The map

$$
\mathsf{M}(1)=I,\qquad
\mathsf{M}(e_x)=-i\sigma_1,\quad
\mathsf{M}(e_y)=-i\sigma_2,\quad
\mathsf{M}(e_z)=-i\sigma_3
$$

is an injective real algebra homomorphism into $M_2(\mathbb{C})$. Explicitly,

$$
\mathsf{M}(e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}(e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}(e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

The complex span of the image is all of $M_2(\mathbb{C})$, so $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$. The image of $\mathbb{H}$ is a real form: the matrices $\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$.

## No Pair in the Real Algebra

### The Eigenvalues of the Adjoint Action

Let $S=a+s$ with $a\in\mathbb{R}$ and $s\in\operatorname{Im}\mathbb{H}$. Since $\operatorname{ad}_a=0$, $\operatorname{ad}_S=\operatorname{ad}_s$. Identify $\operatorname{Im}\mathbb{H}$ with $\mathbb{R}^3$; then for $u\in\operatorname{Im}\mathbb{H}$,

$$
[s,u]=2\,s\times u,
$$

because $[e_x,e_y]=2e_z$ and the cyclic companions. The cross-product operator $s\times$ has eigenvalues $0,\pm i\lvert s\rvert$ on $\mathbb{R}^3\otimes\mathbb{C}$, so $\operatorname{ad}_s$ has eigenvalues

$$
0,\quad 2i\lvert s\rvert,\quad -2i\lvert s\rvert
$$

on $\operatorname{Im}\mathbb{H}$, and $0$ on the centre $\mathbb{R}\cdot1$.

**Proposition (no real spin element).** There are no $S,U\in\mathbb{H}$ with $U\neq0$ and $[S,U]=U$.

*Proof.* Such a relation says that $1$ is an eigenvalue of $\operatorname{ad}_S$. But the eigenvalues are $0$ and $\pm2i\lvert s\rvert$, none of which is $1$. For $s=0$ the operator is zero.

**Corollary (no real spin pair).** A spin pair requires $[U,V]\neq0$, so $U$ and $V$ are nonzero, and the proposition excludes the relation $[S,U]=U$ for $S=\tfrac12[U,V]\in\mathbb{H}$.

**Result.** The quaternion algebra $\mathbb{H}$ has no spin pair. Its spin structure is carried by the complexification.

**Remark (the real weights are imaginary).** Left multiplication by a nonzero $S\in\operatorname{Im}\mathbb{H}$ on $\mathbb{H}$ has eigenvalues $\pm i\lvert S\rvert$, each twice: it is a complex structure, with no real eigenvector. The weights $\pm\tfrac12$ of the spin carrier are not real weights of a real element; they appear only after complexification.

## The Pair in the Biquaternion

### The Three Elements

In $\mathbb{B}=\mathbb{H}\otimes\mathbb{C}$ put

$$
S=\tfrac{i}{2}e_z,\qquad
U=\tfrac{i}{2}e_x-\tfrac12e_y,\qquad
V=\tfrac{i}{2}e_x+\tfrac12e_y.
$$

In the basis $(1,e_x,e_y,e_z)$ the coordinates are

$$
S=\left(0,0,0,\tfrac{i}{2}\right),\qquad
U=\left(0,\tfrac{i}{2},-\tfrac12,0\right),\qquad
V=\left(0,\tfrac{i}{2},\tfrac12,0\right).
$$

The coefficients of $e_x$ are $\tfrac{i}{2}$, not real, so $S,U,V\notin\mathbb{H}$. Also $V=\bar U$ and $\bar S=S$ under the conjugation that sends $i\mapsto-i$ and $e_k\mapsto-e_k$.

### The Three Relations

The products use $e_ze_x=e_y$, $e_ze_y=-e_x$ and $e_xe_y=e_z$. First,

$$
SU=\tfrac{i}{2}e_z\left(\tfrac{i}{2}e_x-\tfrac12e_y\right)
=-\tfrac14e_y+\tfrac{i}{4}e_x,
$$

$$
US=\left(\tfrac{i}{2}e_x-\tfrac12e_y\right)\tfrac{i}{2}e_z
=\tfrac14e_y-\tfrac{i}{4}e_x,
$$

so $[S,U]=\tfrac{i}{2}e_x-\tfrac12e_y=U$. The same computation with the plus sign gives

$$
SV=-\tfrac14e_y-\tfrac{i}{4}e_x,\qquad
VS=\tfrac14e_y+\tfrac{i}{4}e_x,\qquad
[S,V]=-V.
$$

For the third relation,

$$
UV=\left(\tfrac{i}{2}e_x-\tfrac12e_y\right)\left(\tfrac{i}{2}e_x+\tfrac12e_y\right)
=\tfrac12+\tfrac{i}{2}e_z,
$$

$$
VU=\left(\tfrac{i}{2}e_x+\tfrac12e_y\right)\left(\tfrac{i}{2}e_x-\tfrac12e_y\right)
=\tfrac12-\tfrac{i}{2}e_z,
$$

so

$$
[U,V]=ie_z=2S.
$$

**Result.** The three relations hold in $\mathbb{B}$ with zero residual:

$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S.
$$

The triple spans a copy of $\mathfrak{sl}_2(\mathbb{C})$ inside $\mathbb{B}\cong M_2(\mathbb{C})$. In the matrix model above,

$$
\mathsf{M}(S)=\begin{pmatrix}\tfrac12&0\\0&-\tfrac12\end{pmatrix},\qquad
\mathsf{M}(U)=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
\mathsf{M}(V)=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

which is the principal pair of $M_2(\mathbb{C})$.

## The Left Module: Spin $\tfrac12$

### The Two Complex Planes

Left multiplication by $S$ preserves the two complex planes

$$
P_1=\mathbb{C}\{1,e_z\},\qquad P_2=\mathbb{C}\{e_x,e_y\}.
$$

On $P_1$,

$$
S\cdot1=\tfrac{i}{2}e_z,\qquad S\cdot e_z=\tfrac{i}{2}e_z^2=-\tfrac{i}{2},
$$

so the matrix in the basis $(1,e_z)$ is

$$
\begin{pmatrix}0&-\tfrac{i}{2}\\ \tfrac{i}{2}&0\end{pmatrix},
$$

with eigenvalues $\pm\tfrac12$. On $P_2$,

$$
S\cdot e_x=\tfrac{i}{2}e_y,\qquad S\cdot e_y=-\tfrac{i}{2}e_x,
$$

so the matrix in the basis $(e_x,e_y)$ is the same, with eigenvalues $\pm\tfrac12$.

**Result.** As a left $\mathbb{B}$-module, $\mathbb{B}=P_1\oplus P_2=2W_{1/2}$. The spin is $\tfrac12$, with multiplicity $2$.

### The Real Carrier

As a left $\mathbb{H}$-module, $\mathbb{H}$ is simple: every nonzero element is invertible, so the left ideal it generates is all of $\mathbb{H}$. Its real dimension is $4$ and its endomorphism ring is $\mathbb{H}$. After complexification, $\mathbb{H}\otimes\mathbb{C}=\mathbb{B}=2W_{1/2}$.

**Result.** The elementary associative carrier is $\mathbb{H}$ itself, of real dimension $4$ and spin $\tfrac12$. The carrier is quaternionic: its endomorphism ring is $\mathbb{H}$, not $\mathbb{C}$.

**Remark (dimension and spin).** The formula $\dim W_j=2j+1$ gives $2$ for $j=\tfrac12$. The complexified carrier has complex dimension $4=2\cdot2$, and the real carrier has real dimension $4$. The number $4$ is the real dimension of $\mathbb{H}$, and also the complex dimension of its complexification $2W_{1/2}$; it is not the dimension of an irreducible complex carrier.

## The Adjoint Action: Content $0,1$

### The Four Weights

On the basis $(1,e_x,e_y,e_z)$,

$$
\operatorname{ad}_S(1)=0,\qquad
\operatorname{ad}_S(e_x)=ie_y,\qquad
\operatorname{ad}_S(e_y)=-ie_x,\qquad
\operatorname{ad}_S(e_z)=0.
$$

The matrix is

$$
\operatorname{ad}_S=\begin{pmatrix}
0&0&0&0\\
0&0&-i&0\\
0&i&0&0\\
0&0&0&0
\end{pmatrix},
$$

with characteristic polynomial

$$
\lambda^2(\lambda-1)(\lambda+1).
$$

The weights are $0$ with multiplicity $2$, and $\pm1$ with multiplicity $1$ each.

### The Content

The centre $\mathbb{R}\cdot1$ is fixed, of dimension $1$. The imaginary part is spanned by $e_x,e_y,e_z$; on it the weights are $1,0,-1$, one each, so it is $W_1$. Hence

$$
\mathbb{H}=\mathbb{R}\cdot1\oplus\operatorname{Im}\mathbb{H}=W_0\oplus W_1
$$

as a module for the triple, with dimensions $1+3=4$. The multiplicity formula gives $m_0=2-1=1$ and $m_1=1-0=1$.

**Result.** The adjoint content is $0,1$.

**Remark (the two zero weights).** The value $\mu(0)=2$ counts the vectors $1$ and $e_z$. They belong to different summands: $1$ spans the centre $W_0$, and $e_z$ is the weight-$0$ state of $W_1$. A multiplicity count alone does not separate them; the module structure does.

### The Adjoint Carriers

The adjoint action of $\mathbb{H}$ on itself is irreducible on $\operatorname{Im}\mathbb{H}$: the derived algebra $[\mathbb{H},\mathbb{H}]=\operatorname{Im}\mathbb{H}$ is simple of dimension $3$, and it is $W_1$. The centre is the trivial module.

**Result.** The adjoint elementary carriers are $\mathbb{R}\cdot1$ (spin $0$) and $\operatorname{Im}\mathbb{H}$ (spin $1$).

## The Elementary List

| carrier | action | dimension | content | spin |
|---|---|---|---|---|
| $\mathbb{H}$ | left multiplication | $4$ over $\mathbb{R}$ | $2W_{1/2}$ | $\tfrac12$ |
| $\mathbb{R}\cdot1$ | adjoint | $1$ | $W_0$ | $0$ |
| $\operatorname{Im}\mathbb{H}$ | adjoint | $3$ | $W_1$ | $1$ |

**Result.** The elementary spin list is $\Sigma=\{0,\tfrac12,1\}$, the same list as for the biquaternion.

**Remark (same list, different carriers).** The biquaternion $\mathbb{B}$ and the quaternion $\mathbb{H}$ have the same spin list and the same adjoint content. The carriers are not the same: the simple left module of $\mathbb{B}$ is $\mathbb{C}^2$ of complex dimension $2$, while the simple left module of $\mathbb{H}$ is $\mathbb{H}$ of real dimension $4$. The complexification of the second is two copies of the first. The spin is computed after complexification, so it is the same; the real form changes the type, not the spin.

## The Two Actions on the Algebra

**Left multiplication.** As a left module, $\mathbb{H}$ is simple, with complexification $2W_{1/2}$. As a real module it is one carrier of spin $\tfrac12$, not two.

**The adjoint action.** $\mathbb{H}=W_0\oplus W_1$, with content $0,1$.

**Result.** The two columns of the row use the two actions. The list takes the defining spin $\tfrac12$ from the left action and the values $0,1$ from the adjoint; the content is the adjoint decomposition.

## Checks

### The Casimir

In $\mathbb{B}$,

$$
C=S^2+\tfrac12(UV+VU)=\tfrac14+\tfrac12\cdot1=\tfrac34,
$$

which is $j(j+1)$ for $j=\tfrac12$.

On the adjoint module the image of $C$ has characteristic polynomial

$$
\lambda(\lambda-2)^3,
$$

with eigenvalues $0$ and $2=j(j+1)$ for $j=0$ and $j=1$, of multiplicities $1$ and $3$.

**Result.** The Casimir confirms the left spin $\tfrac12$ and the adjoint content $0,1$.

### The Table of Checks

| check | result |
|---|---|
| $e_x^2,e_y^2,e_z^2$ | $-1$ |
| $e_xe_y-e_z$ | $0$ |
| $[S,U]-U$ | $0$ |
| $[S,V]+V$ | $0$ |
| $[U,V]-2S$ | $0$ |
| left weights on $\mathbb{B}$ | $\pm\tfrac12$, each twice |
| adjoint characteristic polynomial | $\lambda^2(\lambda-1)(\lambda+1)$ |
| adjoint content | $W_0\oplus W_1$ |
| Casimir on the left module | $\tfrac34$ |
| Casimir on the adjoint | eigenvalues $0,2$ |

## Summary

- The quaternion algebra has no spin pair: for real $S$ the eigenvalues of $\operatorname{ad}_S$ are $0,\pm2i\lvert s\rvert$, never $1$.
- The pair is in the biquaternion: $S=\tfrac{i}{2}e_z$, $U=\tfrac{i}{2}e_x-\tfrac12e_y$, $V=\tfrac{i}{2}e_x+\tfrac12e_y$.
- The three relations hold with zero residual, and $V=\bar U$, $\bar S=S$.
- The left module is $\mathbb{H}$ of real dimension $4$; its complexification is $2W_{1/2}$, and its spin is $\tfrac12$.
- The adjoint module is $\mathbb{H}=W_0\oplus W_1$, of content $0,1$; the two zero weights are the centre vector $1$ and the state $e_z$ of $W_1$.
- The elementary carriers are $\mathbb{R}\cdot1$ (spin $0$), $\mathbb{H}$ (spin $\tfrac12$) and $\operatorname{Im}\mathbb{H}$ (spin $1$); the list is $0,\tfrac12,1$.
- The list is the same as the biquaternion's; the real dimensions and the endomorphism rings are not.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | quaternion algebra over $\mathbb{R}$ |
| $\mathbb{B}$ | biquaternion $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$ |
| $e_x,e_y,e_z$ | imaginary quaternion units |
| $i$ | the complex scalar of the complexification |
| $\bar q$ | quaternion conjugate |
| $S$ | spin element $\tfrac{i}{2}e_z$ |
| $U,V$ | ladders |
| $\operatorname{ad}_X$ | $Y\mapsto XY-YX$ |
| $W_j$ | irreducible carrier, dimension $2j+1$ |
| $C$ | Casimir element $S^2+\tfrac12(UV+VU)$ |

## Further Reading

- [The General Definition of Spin](../articles_maths/the-general-definition-of-spin.html), for the definition, the real forms and the table of cases.
- [The Spin of a Biquaternion](../articles_maths/the-spin-of-a-biquaternion.html), for the same triple in the biquaternion frame.
- [The Quaternion Algebra in the 2x2 Matrix Element Representation](../articles_maths/the-quaternion-algebra-in-the-2x2-matrix-element-representation.html), for the embedding used here.
- [The Spin of the Principal Pair of $M_2(\mathbb{C})$](the-principal-pair-of-m2c-a-worked-computation.html), for the matrix form of the same row.
- [Modules over the Quaternion Algebra](../articles_maths/modules-over-the-quaternion-algebra.html), for the simple module.
- [The Casimir Operator](../articles_maths/the-casimir-operator.html), for the eigenvalue $j(j+1)$.
