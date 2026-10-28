# __The One-Sided Operators of a N-Degenerate, Spectrally Degenerate Biquaternion__

## Introduction

This article treats the one-sided operators of the N-degenerate, spectrally degenerate sector $\Sigma_{00}$. The element is a pure null vector

$$
\tilde Q=\tilde\nu=\vec A+i\vec B,
\qquad
\vec A,\vec B\in\mathbb{R}^{3},
\qquad
\lVert\vec A\rVert=\lVert\vec B\rVert=a>0,
\qquad
\vec A\cdot\vec B=0,
\qquad
\tilde\nu^{2}=0 .
$$

The sector is the set of non-zero nilpotents; the origin is its only semisimple element. The word **N-degenerate** refers to $\langle\tilde Q\rangle_{\natural}=0$; the word **spectrally degenerate** to $B^{2}=0$. Both the element and its one-sided operators are nilpotent. The left and right multiplications satisfy

$$
L_{\tilde\nu}^{2}=L_{\tilde\nu^{2}}=0,
\qquad
R_{\tilde\nu}^{2}=R_{\tilde\nu^{2}}=0,
$$

and each has complex rank two. The Jordan form is two blocks of size two with eigenvalue zero. This is the maximal defect: no semisimple part survives, and the operator is not a projection up to scale. The rank is the same as on $\Sigma_{01}$; the block structure is the same as on $\Sigma_{10}$ (two blocks of size two), but the eigenvalue is zero instead of one; what is new is the combination of both defects.

The polar pair of *The Polar Decomposition of a N-Degenerate Biquaternion* survives on the null cone:

$$
\tilde Q=\tilde Q_H\tilde Q_0,
\qquad
\tilde Q_H=2a\tilde\Pi_+,
\qquad
\tilde Q_0=\frac{\tilde\nu}{2a},
\qquad
\tilde\Pi_\pm=\frac{e_t\pm i\vec c}{2},
\qquad
\vec c=\frac{\vec A\times\vec B}{a^{2}} .
$$

The Hermitian factor is a rank-one projection scaled by $2a$; the partial-isometry factor is itself nilpotent, $\tilde Q_0^{2}=0$. The main result is the scalar collapse

$$
\boxed{\;L_{\tilde Q}=2a\,L_{\tilde Q_0},\qquad R_{\tilde Q}=2a\,R_{\tilde Q_0}\;}
$$

with $L_{\tilde Q_0}$ and $R_{\tilde Q_0}$ nilpotent partial isometries. The one-sided operator is $2a$ times a nilpotent partial isometry; its non-zero singular value is $2a$, twice, while its only eigenvalue is zero.

The article is organized as follows. §*The Polar Pair* describes the canonical Hermitian idempotents and the rank-one singular value decomposition. §*The One-Sided Operators* computes the rank, the square, the spectrum, the image and the kernel, with the Peirce matrices. §*The Polar Pair, One-Sided* reads the scalar collapse. §*The Exponential* computes the unipotent group and identifies the sector of the element flow. §*Worked Example* gives the standard nilpotent.

## The Polar Pair

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The Hermitian conjugation is $\tilde X^{*}=\overline{\tilde X^{\natural}}$, the Hermitian norm is $\langle\tilde X\rangle_{*}=\operatorname{Sc}(\tilde X\tilde X^{*})$, and the quaternionic norm is $\langle\tilde X\rangle_{\natural}=\sum_\mu X_\mu^{2}$.

### The canonical Hermitian pair

Let $\tilde\nu=\vec A+i\vec B$ with $\vec A,\vec B$ real, orthogonal and of equal norm $a>0$. The vector

$$
\vec c=\frac{\vec A\times\vec B}{a^{2}}
$$

is real and unit. Define

$$
\tilde\Pi_+=\frac{e_t+i\vec c}{2},
\qquad
\tilde\Pi_-=\frac{e_t-i\vec c}{2},
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
\qquad
\tilde\Pi_\pm^{2}=\tilde\Pi_\pm,
\qquad
\tilde\Pi_\pm^{*}=\tilde\Pi_\pm .
$$

These are the canonical Hermitian idempotents of *The N-Degenerate, Spectrally Degenerate Sector*. They satisfy

$$
\tilde\Pi_+\tilde\nu=\tilde\nu,
\qquad
\tilde\nu\tilde\Pi_+=0,
\qquad
\tilde\Pi_-\tilde\nu=0,
\qquad
\tilde\nu\tilde\Pi_-=\tilde\nu .
$$

Thus $\tilde\nu=\tilde\Pi_+\tilde\nu\tilde\Pi_-$ lies in the mixed corner $\mathbb{B}_{+-}$ of the pair, and it is annihilated by the two products that would put it in a diagonal corner. In particular

$$
\langle\tilde\nu\rangle_{\natural}
=\operatorname{Sc}(\tilde\nu^{2})=0,
\qquad
\langle\tilde\nu\rangle_{*}
=\operatorname{Sc}(\tilde\nu\tilde\nu^{*})=2a^{2},
\qquad
\tilde\nu\tilde\nu^{*}=4a^{2}\tilde\Pi_+,
\qquad
\tilde\nu^{*}\tilde\nu=4a^{2}\tilde\Pi_- .
$$

### The polar pair

With $a=\sqrt{\langle\tilde\nu\rangle_{*}/2}$, the polar pair is

$$
\boxed{\;
P=\tilde\Pi_+,
\qquad
\tilde Q_H=2a\tilde\Pi_+,
\qquad
\tilde Q_0=\frac{\tilde\nu}{2a},
\qquad
\tilde Q=\tilde Q_H\tilde Q_0,
\qquad
\tilde Q_0^{2}=0 .
\;}
$$

The Hermitian factor is positive semidefinite of rank one and spectrum $\{0,2a\}$. The partial-isometry factor is nilpotent:

$$
\tilde Q_0\tilde Q_0^{*}=\tilde\Pi_+,
\qquad
\tilde Q_0^{*}\tilde Q_0=\tilde\Pi_-,
\qquad
\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0,
\qquad
\tilde Q_0^{2}=0 .
$$

A nilpotent partial isometry is not a contradiction: the Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ is a partial isometry and squares to zero. The polar pair is the rank-one singular value decomposition of the nilpotent; the "$*$-unitary" factor is a nilpotent partial isometry.

### The matrix model

In the matrix model $\mathsf M_2(e_t)=I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$. The null element is a rank-one matrix,

$$
\mathsf M_2(\tilde\nu)=2a\,u v^{\dagger},
\qquad
v^{\dagger}u=\frac{Q_t}{a}=0,
\qquad
u^{\dagger}u=v^{\dagger}v=1,
\qquad
u\perp v .
$$

The two singular vectors are orthogonal; this is the matrix form of the spectral degeneracy. The polar factors are

$$
P=u u^{\dagger}=\tilde\Pi_+,
\qquad
\tilde Q_H=2a\,u u^{\dagger},
\qquad
\tilde Q_0=u v^{\dagger},
\qquad
\tilde Q_0^{*}=v u^{\dagger},
\qquad
\tilde Q_0^{2}=u(v^{\dagger}u)v^{\dagger}=0 .
$$

The overlap $v^{\dagger}u=Q_t/a$ vanishes exactly on $\Sigma_{00}$. On $\Sigma_{01}$ it was $1/\sqrt{\kappa}\neq0$; the wall is the orthogonality of the two slots.

### The standard nilpotent

For

$$
\tilde\nu=\vec e_x+i\vec e_y,
$$

one has $a=1$, $\vec c=\vec e_z$, and

$$
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2},
\qquad
\tilde\Pi_-=\frac{e_t-i\vec e_z}{2},
\qquad
\tilde Q_H=e_t+i\vec e_z,
\qquad
\tilde Q_0=\frac{\vec e_x+i\vec e_y}{2}.
$$

The matrix model is

$$
\mathsf M_2(\tilde\nu)=
\begin{pmatrix}0&-2i\\0&0\end{pmatrix},
\qquad
\mathsf M_2(\tilde Q_H)=
\begin{pmatrix}2&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2(\tilde Q_0)=
\begin{pmatrix}0&-i\\0&0\end{pmatrix}.
$$

The singular value is $2$, the only eigenvalue is $0$, and the two singular vectors may be taken as $u=(1,0)$ and $v=(0,i)$, which are orthogonal.

## The One-Sided Operators

### Elementary properties

The one-sided operators are $L_{\tilde\nu}(\tilde X)=\tilde\nu\tilde X$ and $R_{\tilde\nu}(\tilde X)=\tilde X\tilde\nu$. They are $\mathbb{C}$-linear, satisfy the composition laws of *Operators of the Polar Word: The Common Framework*, and are injective as parameter maps. They are not invertible, because $\tilde\nu$ is a zero divisor.

### The square, the rank and the spectrum

**Theorem.** On $\Sigma_{00}$:

**(a)** $L_{\tilde\nu}^{2}=0$ and $R_{\tilde\nu}^{2}=0$;

**(b)** $L_{\tilde\nu}$ and $R_{\tilde\nu}$ have complex rank $2$;

**(c)** their only eigenvalue is $0$, with algebraic multiplicity $4$ and geometric multiplicity $2$;

**(d)** their Jordan form is $J_2(0)\oplus J_2(0)$, with minimal polynomial $X^{2}$;

**(e)** $\operatorname{tr}L_{\tilde\nu}=\operatorname{tr}R_{\tilde\nu}=0$ and $\det L_{\tilde\nu}=\det R_{\tilde\nu}=0$;

**(f)** for every $\tilde X$, $\langle L_{\tilde\nu}\tilde X\rangle_{\natural}=\langle R_{\tilde\nu}\tilde X\rangle_{\natural}=0$; both images lie on the null cone.

*Proof.* The square is $L_{\tilde\nu}^{2}=L_{\tilde\nu^{2}}=L_0=0$, and similarly on the right. In the matrix model, $\mathsf M_2(\tilde\nu)=2a\,u v^{\dagger}$ is a rank-one nilpotent. Left multiplication is $X\mapsto 2a\,u v^{\dagger}X$; its image is $\{u w^{\dagger}:w\in\mathbb{C}^{2}\}$, of dimension two, and its kernel is $\{X:v^{\dagger}X=0\}$, also of dimension two. Since the square is zero, the image is contained in the kernel, and the two dimensions are equal, so the image equals the kernel. The eigenvalues of left multiplication by a matrix are the eigenvalues of the matrix, each repeated twice; the only eigenvalue of $2a\,u v^{\dagger}$ is $0$, so the algebraic multiplicity is four. The geometric multiplicity is the dimension of the kernel, two. The minimal polynomial is $X^{2}$ because the operator is non-zero and squares to zero. The trace is $2\operatorname{tr}\mathsf M_2(\tilde\nu)=0$, and the determinant is $(\det\mathsf M_2(\tilde\nu))^{2}=0$. The norm is multiplicative and $\langle\tilde\nu\rangle_{\natural}=0$.
The same arguments apply to the right multiplication $X\mapsto 2a\,X u v^{\dagger}$.

### The image and the kernel

The image and the kernel of $L_{\tilde\nu}$ coincide, and likewise for $R_{\tilde\nu}$. The two common planes are distinct and meet in the line of the nilpotent.

**Proposition (the two planes).** On $\Sigma_{00}$,

$$
\boxed{\;
\operatorname{im}L_{\tilde\nu}
=\ker L_{\tilde\nu}
=\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_+,
\qquad
\operatorname{im}R_{\tilde\nu}
=\ker R_{\tilde\nu}
=\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_- .
\;}
$$

The two planes are distinct and

$$
\bigl(\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_+\bigr)
\cap
\bigl(\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_-\bigr)
=\mathbb{C}\tilde\nu .
$$

*Proof.* The multiplications by the canonical idempotents give

$$
\tilde\nu\tilde\Pi_+=0,
\qquad
\tilde\nu\tilde\Pi_-=\tilde\nu,
\qquad
\tilde\Pi_+\tilde\nu=\tilde\nu,
\qquad
\tilde\Pi_-\tilde\nu=0 .
$$

Hence $L_{\tilde\nu}(\tilde\Pi_+)=0$ and $L_{\tilde\nu}(\tilde\Pi_-)=\tilde\nu$, so the image contains $\mathbb{C}\tilde\nu$ and $\mathbb{C}\tilde\Pi_+$ after one more step: the corner vector $\vec X$ of §*The Peirce Matrices* satisfies $\tilde\nu\vec X\in\mathbb{C}\tilde\Pi_+$. The image is therefore the plane $\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_+$; the kernel contains the same plane by the square-zero property, and the dimensions agree. The right-hand statement is the mirror, using $\tilde\Pi_+\tilde\nu=\tilde\nu$ and $\tilde\Pi_-\tilde\nu=0$. The intersection is the common line $\mathbb{C}\tilde\nu$ because $\tilde\Pi_+$ and $\tilde\Pi_-$ are independent modulo $\tilde\nu$.

The image planes are totally isotropic: for $\tilde X=\tilde\nu\tilde Y$,

$$
\langle\tilde X\rangle_{\natural}
=\langle\tilde\nu\rangle_{\natural}\langle\tilde Y\rangle_{\natural}=0 .
$$

The kernels are the same planes, so the operator does not split the algebra into an image and a complement: the image is contained in the kernel, and the algebra is a non-trivial extension. This is the operator form of the absence of a spectral decomposition.

### The Peirce matrices

Let $\tilde\Pi_\pm$ be the canonical Hermitian idempotents. Choose a non-zero corner vector

$$
\vec X\in\tilde\Pi_-\mathbb{B}\tilde\Pi_+,
$$

and normalize it so that

$$
\tilde\nu\vec X=\tilde\Pi_+,
\qquad
\vec X\tilde\nu=\varkappa\,\tilde\Pi_-,
\qquad
\varkappa\neq0 .
$$

In the standard example one may take $\varkappa=1$. The four elements

$$
\bigl(\tilde\Pi_+,\ \tilde\nu,\ \vec X,\ \tilde\Pi_-\bigr)
$$

form a basis, the canonical Jordan basis of *The Jordan Basis of a Spectrally Degenerate Biquaternion*, with the Peirce form purely off-diagonal:

$$
\tilde\nu=\tilde\Pi_+\tilde\nu\tilde\Pi_-,
\qquad
\tilde\Pi_\pm\tilde\nu\tilde\Pi_\pm=0,
\qquad
\tilde\Pi_\pm\tilde\nu\tilde\Pi_\mp=0 \text{ except } \tilde\Pi_+\tilde\nu\tilde\Pi_-=\tilde\nu .
$$

The one-sided operators have the matrices

$$
\boxed{\;
\mathsf M\bigl(L_{\tilde\nu}\bigr)=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\qquad
\mathsf M\bigl(R_{\tilde\nu}\bigr)=
\begin{pmatrix}
0&0&0&0\\
1&0&0&0\\
0&0&0&0\\
0&0&\varkappa&0
\end{pmatrix}.
\;}
$$

The columns are the images of the basis vectors:

$$
L_{\tilde\nu}:\quad
\tilde\Pi_+\mapsto0,\quad
\tilde\nu\mapsto0,\quad
\vec X\mapsto\tilde\Pi_+,\quad
\tilde\Pi_-\mapsto\tilde\nu,
$$

$$
R_{\tilde\nu}:\quad
\tilde\Pi_+\mapsto\tilde\nu,\quad
\tilde\nu\mapsto0,\quad
\vec X\mapsto\varkappa\tilde\Pi_-,\quad
\tilde\Pi_-\mapsto0 .
$$

The Jordan chains are therefore

$$
L_{\tilde\nu}:\quad
\vec X\to\tilde\Pi_+\to0,
\qquad
\tilde\Pi_-\to\tilde\nu\to0,
$$

$$
R_{\tilde\nu}:\quad
\tilde\Pi_+\to\tilde\nu\to0,
\qquad
\vec X\to\varkappa\tilde\Pi_-\to0 .
$$

Each operator has two chains of length two. The chain starts are the two directions outside the common image plane; the chain ends are the two directions inside it.

### Singular values

The operator is $L_{\tilde\nu}=2aL_{\tilde Q_0}$ with $\tilde Q_0$ a nilpotent partial isometry. Hence $L_{\tilde Q_0}$ is a partial isometry of the operator space,

$$
L_{\tilde Q_0}L_{\tilde Q_0}^{*}L_{\tilde Q_0}
=L_{\tilde Q_0\tilde Q_0^{*}\tilde Q_0}
=L_{\tilde Q_0},
$$

and its singular values are $1$ (twice) and $0$ (twice). The singular values of $L_{\tilde\nu}$ are $2a$ (twice) and $0$ (twice). The projection $L_{\tilde\Pi_+}$ is an orthogonal projection of rank two with singular value one, but it is not the partial-isometry factor: $\tilde\Pi_+$ is the image projection, while $\tilde Q_0$ is nilpotent. The scalar collapse uses the nilpotent partial isometry, not the projection.

## The Polar Pair, One-Sided

### The scalar collapse

By the polar pair theorem, $\tilde\nu=2a\tilde Q_0$ with $\tilde Q_0=\tilde\nu/(2a)$ a partial isometry. The composition laws give

$$
\boxed{\;
L_{\tilde\nu}=2a\,L_{\tilde Q_0},
\qquad
R_{\tilde\nu}=2a\,R_{\tilde Q_0}.
\;}
$$

The operators $L_{\tilde Q_0}$ and $R_{\tilde Q_0}$ are partial isometries, because $\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0$. They are nilpotent, because $\tilde Q_0^{2}=0$; hence $L_{\tilde Q_0}^{2}=0$ and $R_{\tilde Q_0}^{2}=0$. The one-sided operator is $2a$ times a nilpotent partial isometry. Its non-zero singular value is $2a$, twice; its only eigenvalue is zero.

The canonical left polar factor of $L_{\tilde\nu}$ is

$$
\lvert L_{\tilde\nu}\rvert
=\bigl(L_{\tilde\nu}L_{\tilde\nu}^{*}\bigr)^{1/2}
=L_{\tilde Q_H}
=2a\,L_{\tilde\Pi_+},
$$

which is positive semidefinite of rank two. On the image of $L_{\tilde Q_0}$ it acts as the scalar $2a$, because $\tilde\Pi_+\tilde Q_0=\tilde Q_0$ and therefore $L_{\tilde\Pi_+}L_{\tilde Q_0}=L_{\tilde Q_0}$. This is the scalar collapse. The factorisation $L_{\tilde\nu}=L_{\tilde Q_H}L_{\tilde Q_0}$ is the polar decomposition of the operator; the simplified form $L_{\tilde\nu}=2aL_{\tilde Q_0}$ is its scalar reduction.

The right-hand version is

$$
R_{\tilde\nu}=R_{\tilde Q_0}R_{\tilde Q_H}=2a\,R_{\tilde Q_0}.
$$

### The phase and the sign

For a complex multiple

$$
\tilde\nu=c_0(\vec e_x+i\vec e_y),
\qquad
c_0=\lvert c_0\rvert e^{i\beta},
$$

one has $a=\lvert c_0\rvert$ and

$$
\tilde Q_0=\frac{c_0}{\lvert c_0\rvert}\frac{\vec e_x+i\vec e_y}{2},
\qquad
\tilde Q_H=2\lvert c_0\rvert\,\tilde\Pi_+,
\qquad
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2}.
$$

The phase $e^{i\beta}$ is carried by $\tilde Q_0$ and by $L_{\tilde\nu}$; the scalar $2a=2\lvert c_0\rvert$ is positive. The nilpotent direction $\vec e_x+i\vec e_y$ is unchanged. The sandwich of the companion article sees only $\lvert c_0\rvert$ and the canonical pair; the phase cancels. The sign $\tilde\nu\mapsto-\tilde\nu$ is also carried by $\tilde Q_0$; the scalar $2a$ is unchanged.

### The modulus and the singular value

The element modulus is zero, while the operator has rank two and non-zero singular value $2a$. The vanishing of the norm says that the element is a null vector and that both multiplications have a non-trivial kernel; it does not say that the operator is zero. The spectral degeneration $B^{2}=0$ makes the operator nilpotent; the norm degeneration makes its rank two. The two defects are independent.

## The Exponential

**The operator exponential.** Since $L_{\tilde\nu}^{2}=0$,

$$
\boxed{\;
\exp\bigl(tL_{\tilde\nu}\bigr)=I+tL_{\tilde\nu}
\;}
$$

for every complex $t$, and the same formula holds for $R_{\tilde\nu}$. The eigenvalues are all $1$; the Jordan form is $J_2(1)\oplus J_2(1)$; the determinant is $1$. The group is unipotent: it is a shear, not a dilation. It is invertible for every $t$, although the generator $L_{\tilde\nu}$ is nilpotent and singular.

**The element exponential.** Since $\tilde\nu^{2}=0$,

$$
\exp\bigl(t\tilde\nu\bigr)=e_t+t\tilde\nu .
$$

The quaternionic norm is

$$
\bigl\langle\exp(t\tilde\nu)\bigr\rangle_{\natural}=1,
$$

and the vector form is

$$
B^{2}\bigl(\exp(t\tilde\nu)\bigr)=t^{2}B^{2}(\tilde\nu)=0 .
$$

Hence the exponential is a unit with $B^{2}=0$: for every $t$ it lies in the N-regular, spectrally degenerate sector $\Sigma_{10}$ (at $t=0$ it is $e_t$), not in the doubly regular sector. This is the mirror of the generic $\Sigma_{01}$ flow, which leaves both walls and lies in $\Sigma_{11}$. The exponential moves the element one wall away: it removes the norm degeneration and preserves the spectral one.

The one-sided operator exponential is unipotent with two Jordan blocks of size two at eigenvalue one; this is the operator type of the N-regular, spectrally degenerate one-sided operator of *The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion*. The two-sided companion is a unipotent Lorentz flow of Jordan type $2+1+1$. The one-sided exponential is a shear of the operator space, not a Lorentz transformation.

## Worked Example

### The standard nilpotent

Take

$$
\tilde\nu=\vec e_x+i\vec e_y .
$$

Then $a=1$, $\vec c=\vec e_z$, and

$$
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2},
\qquad
\tilde\Pi_-=\frac{e_t-i\vec e_z}{2},
\qquad
\tilde Q_H=e_t+i\vec e_z,
\qquad
\tilde Q_0=\frac{\vec e_x+i\vec e_y}{2}.
$$

The matrix model is

$$
\mathsf M_2(\tilde\nu)=
\begin{pmatrix}0&-2i\\0&0\end{pmatrix},
\qquad
\mathsf M_2(\tilde Q_H)=
\begin{pmatrix}2&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2(\tilde Q_0)=
\begin{pmatrix}0&-i\\0&0\end{pmatrix}.
$$

In the standard basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the left multiplication is

$$
\mathsf M\bigl(L_{\tilde\nu}\bigr)=
\begin{pmatrix}
0&-1&-i&0\\
1&0&0&i\\
i&0&0&-1\\
0&-i&1&0
\end{pmatrix},
$$

with rank two, square zero, trace zero and determinant zero. The right multiplication is the mirror obtained by reversing the order of the factors. The singular values are $2,2,0,0$.

For the Peirce form, take the corner vector

$$
\vec X=\frac{-\vec e_x+i\vec e_y}{4},
$$

which satisfies

$$
\tilde\nu\vec X=\tilde\Pi_+,
\qquad
\vec X\tilde\nu=\tilde\Pi_- .
$$

In the basis $(\tilde\Pi_+,\tilde\nu,\vec X,\tilde\Pi_-)$,

$$
\mathsf M\bigl(L_{\tilde\nu}\bigr)=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\qquad
\mathsf M\bigl(R_{\tilde\nu}\bigr)=
\begin{pmatrix}
0&0&0&0\\
1&0&0&0\\
0&0&0&0\\
0&0&1&0
\end{pmatrix}.
$$

The two left chains are $\vec X\to\tilde\Pi_+\to0$ and $\tilde\Pi_-\to\tilde\nu\to0$; the two right chains are $\tilde\Pi_+\to\tilde\nu\to0$ and $\vec X\to\tilde\Pi_-\to0$.

### A complex scalar multiple

For

$$
\tilde\nu=c_0(\vec e_x+i\vec e_y),
\qquad
c_0=\lvert c_0\rvert e^{i\beta},
$$

the element has $a=\lvert c_0\rvert$, and

$$
\tilde Q_0=e^{i\beta}\frac{\vec e_x+i\vec e_y}{2},
\qquad
\tilde Q_H=2\lvert c_0\rvert\,\tilde\Pi_+,
\qquad
L_{\tilde\nu}=2\lvert c_0\rvert\,L_{\tilde Q_0}.
$$

The phase $e^{i\beta}$ is in $\tilde Q_0$; the singular value $2\lvert c_0\rvert$ is positive and phase-blind. The sandwich of the companion article is $4\lvert c_0\rvert^{2}\Theta_{\tilde Q_0}$, also phase-blind. This is the cleanest illustration of the one-sided/two-sided contrast in the sector.

## Summary

### Main Results

| item | value |
|---|---|
| sector | $\Sigma_{00}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}=0\}$ |
| parameter | $\tilde\nu=\vec A+i\vec B$, $\lVert\vec A\rVert=\lVert\vec B\rVert=a>0$, $\vec A\cdot\vec B=0$ |
| canonical pair | $\tilde\Pi_\pm=(e_t\pm i\vec c)/2$, $\vec c=\vec A\times\vec B/a^{2}$ |
| polar pair | $\tilde Q_H=2a\tilde\Pi_+$, $\tilde Q_0=\tilde\nu/(2a)$, $\tilde Q_0^{2}=0$ |
| one-sided operators | $L_{\tilde\nu}$, $R_{\tilde\nu}$ |
| squares | $L_{\tilde\nu}^{2}=0$, $R_{\tilde\nu}^{2}=0$ |
| rank | $2$ for both |
| spectrum | $\{0\}$, algebraic multiplicity $4$, geometric multiplicity $2$ |
| Jordan form | $J_2(0)\oplus J_2(0)$ |
| trace | $0$ |
| determinant | $0$ |
| singular values | $2a$ (twice), $0$ (twice) |
| image | $\operatorname{im}L_{\tilde\nu}=\ker L_{\tilde\nu}=\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_+$ |
| mirror | $\operatorname{im}R_{\tilde\nu}=\ker R_{\tilde\nu}=\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_-$ |
| intersection | the two planes meet in $\mathbb{C}\tilde\nu$ |
| scalar collapse | $L_{\tilde\nu}=2aL_{\tilde Q_0}$, $R_{\tilde\nu}=2aR_{\tilde Q_0}$ |
| exponential | $\exp(tL_{\tilde\nu})=I+tL_{\tilde\nu}$ |
| element flow | $\exp(t\tilde\nu)=e_t+t\tilde\nu$, a unit in $\Sigma_{10}$ for every $t$ (at $t=0$ it is $e_t$) |

### What the Operator Shows

- The norm degeneration fixes the rank: the one-sided operator has rank two and its image is a null plane.
- The spectral degeneration fixes the Jordan type: the operator is nilpotent with two blocks of size two, and its minimal polynomial is $X^{2}$.
- The image equals the kernel, so there is no spectral splitting; the algebra is a non-trivial extension with kernel equal to image.
- The polar pair collapses to $L_{\tilde\nu}=2aL_{\tilde Q_0}$ with $\tilde Q_0$ a nilpotent partial isometry; the positive factor acts as the scalar $2a$ on the image.
- The non-zero singular value is $2a$, twice; the only eigenvalue is zero. The gap is the maximal defect.
- The phase and the sign are one-sided; they sit in $\tilde Q_0$ and in $L_{\tilde\nu}$. The sandwich sees only $4a^{2}=(2a)^{2}$ and the canonical pair.
- The exponential is unipotent; it moves the element from $\Sigma_{00}$ to $\Sigma_{10}$, removing the norm degeneration and preserving the spectral one.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\nu=\vec A+i\vec B$ | a non-zero element of $\Sigma_{00}$ |
| $a=\lVert\vec A\rVert=\lVert\vec B\rVert$ | the half singular value, $2a$ the non-zero singular value |
| $\vec c=\vec A\times\vec B/a^{2}$ | the unit spectral direction |
| $\tilde\Pi_\pm=(e_t\pm i\vec c)/2$ | the canonical Hermitian idempotents |
| $\tilde Q_H=2a\tilde\Pi_+$ | the Hermitian factor |
| $\tilde Q_0=\tilde\nu/(2a)$ | the nilpotent partial-isometry factor |
| $L_{\tilde\nu},R_{\tilde\nu}$ | left and right multiplication |
| $\vec X$ | a normalized corner vector, $\tilde\nu\vec X=\tilde\Pi_+$ |
| $\varkappa$ | the corner constant, $\vec X\tilde\nu=\varkappa\tilde\Pi_-$ |
| $J_2(0)$ | the nilpotent Jordan block of size two |

## Further Reading

- [The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion](one-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the same two-block Jordan type with a non-zero eigenvalue.
- [The One-Sided Operators of a N-Degenerate, Spectrally Regular Biquaternion](one-sided-operator-and-the-polar-decomposition-of-a-n-degenerate-spectrally-regular-biquaternion.html), for the projection case of the same sector pair.
- [The Two-Sided Operator of a N-Degenerate, Spectrally Degenerate Biquaternion](two-sided-operator-and-the-polar-decomposition-of-a-n-degenerate-spectrally-degenerate-biquaternion.html), for the companion sandwich and the single nilpotent chain.
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the general two-factor pair on the null cone.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the canonical Hermitian pair, the Peirce data and the no-eigenbasis theorem.
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.html), for the Jordan basis used in the Peirce matrices.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the contrasting spectrally regular case.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the null cone and the quaternionic norm.
