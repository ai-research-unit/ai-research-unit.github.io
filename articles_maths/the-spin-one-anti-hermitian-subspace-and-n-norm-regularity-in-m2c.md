# __The Spin-One Anti-Hermitian Subspace and N Norm Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** What does the determinant give on the skew-adjoint space $\mathfrak{u}(2)$ and on the three-dimensional carrier inside it?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-One Anti-Hermitian Subspace and N Norm Regularity](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity.html). The source's norm is $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ on $\mathbb{R}(ie_t)\oplus\mathfrak{k}$; in the display the same space is $\mathbb{R}(i\mathrm I_2)\oplus\mathfrak{su}(2)$ and the norm is $\det A$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That $\det(i\lambda\mathrm I_2+v\cdot E)=|v|^2-\lambda^2$, a real form of inertia $(3,1)$. That the two summands are orthogonal and definite. That the null locus is a cone of real dimension three with two nappes. That the carrier is positive definite, hence norm-regular away from the origin. That the norm is invariant under unitary conjugation and constant on the orbits. The comparison with the Hermitian half.

**What the article does not do.** It does not treat the discriminant on the same space, which is [The Spin-One Anti-Hermitian Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-spectral-regularity-in-m2c.html); it does not treat the sectors in full, which is [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html).

**Conventions.** $A=i\lambda\mathrm I_2+v\cdot E$ with $\lambda\in\mathbb{R}$ and $v\in\mathbb{R}^3$, $E_k=-i\sigma_k$, and $|v|^2=v_1^2+v_2^2+v_3^2$. Then $Q_t=i\lambda$ and $N=\det A$. The adjoint is $A^{\dagger}=\bar A^{\mathsf T}$.

**A note on the signs.** The eigenvalues of $v\cdot\sigma$ are $\pm|v|$, so the eigenvalues of $A$ are $i(\lambda\mp|v|)$ and the determinant is $|v|^2-\lambda^2$, verified. The form is real on the whole skew space, which is why the inertia can be read off.

**Boundaries.** The space is [Introduction to the Spin-One Anti-Hermitian Subspace in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-in-m2c.html). The two halves of the algebra are [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html). The norm in general is [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $\lambda$ the real centre coordinate, $v$ the real vector coordinates, $E_k$ the generators, $U$ a unitary element.

## The Norm on the Closure

**The formula.**
$$
\det(i\lambda\mathrm I_2+v\cdot E)=|v|^2-\lambda^2,
$$
verified on random real $\lambda$ and $v$ to $10^{-15}$.

**The eigenvalues.** $\operatorname{spec}(i\lambda\mathrm I_2+v\cdot E)=\{i(\lambda-|v|),\,i(\lambda+|v|)\}$: purely imaginary, as they must be, since the matrix is skew.

**The two summands.**
$$
\det(i\lambda\mathrm I_2)=-\lambda^2,\qquad \det(v\cdot E)=|v|^2,\qquad B(i\lambda\mathrm I_2,v\cdot E)=0 .
$$

**The inertia.** Negative definite on the line $\mathbb{R}(i\mathrm I_2)$, positive definite on the carrier $\mathfrak{su}(2)$, orthogonal split: inertia $(3,1)$.

**The carrier is norm-regular away from the origin.** $\mathfrak{su}(2)\cap\{\det=0\}=\{0\}$, since $|v|^2>0$ for $v\neq0$.

**Where the indefiniteness comes from.** Neither summand is indefinite. The sign difference is created by the addition, and the addition is in the algebra, not in a choice of coordinates.

## The Null Cone

**The set.**
$$
\mathfrak{u}(2)\cap\{\det=0\}=\{i\lambda\mathrm I_2+v\cdot E:|v|=|\lambda|\}.
$$

**The shape.** Homogeneous of degree two, hence a cone with vertex at the origin; two nappes $\lambda=\pm|v|$; each nappe meets a sphere of radius $r$ in a two-sphere. Real dimension $3$.

**The null matrices are not nilpotent.** A null element has trace $2i\lambda$ and eigenvalues $0$ and $2i\lambda$, so it satisfies $A^2=2i\lambda A$ and not $A^2=0$; verified on $i\mathrm I_2+E_1$, which has $\det=0$, $\tau=2i$ and $A^2=2iA$. The nilpotent elements of the closure are the origin alone, because nilpotence needs $\tau=0$ as well, that is $\lambda=0$, and then $|v|=0$.

**The null lines.** Each non-zero null element spans a null line, and the lines are parametrised by the unit sphere in the carrier: the unit vector $u$ gives the line $\mathbb{C}(i\mathrm I_2+u\cdot E)$, and $u$ and $-u$ give the same line up to sign of $\lambda$.

**The cone is not a subspace.** It is closed under real scaling and not under addition.

## Invariance Under the Group

**The norm is invariant.** $\det(UAU^{\dagger})=\det A$ for unitary $U$, so the determinant is constant on each conjugacy orbit.

**The orbits.** On $\mathfrak{u}(2)$ the conjugation orbits are labelled by the pair $(\lambda,|v|)$, since the eigenvalues are $i(\lambda\mp|v|)$ and a skew matrix is determined up to unitary conjugation by its eigenvalues. The determinant is the difference of the two squares, so it is one function of the two labels and does not separate the orbits.

**The cone is a union of orbits.** It is the set of orbits with $|v|=|\lambda|$, and each nappe is a union of orbits.

## The Two Halves and the Sign

**The Hermitian partner.** On $\mathfrak{h}=\mathbb{R}\mathrm I_2\oplus i\mathfrak{su}(2)$, with $A=\lambda\mathrm I_2+v\cdot\sigma$,
$$
\det(\lambda\mathrm I_2+v\cdot\sigma)=\lambda^2-|v|^2,
$$
the negative of the value on the skew half at the same coordinates, and the inertia is $(1,3)$.

**Why the carrier sits in the skew half.** The carrier is real, and the real triple is $\mathfrak{su}(2)$, which is skew. On the Hermitian half the corresponding triple $i\mathfrak{su}(2)$ is negative definite. So the carrier sits in the half where its own triple is positive.

## The Three Carriers Compared

| carrier | $\det$ on it | singular locus in it |
|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | $\lambda^2$ | $\{0\}$ |
| plane $\mathbb{C}P$ | $0$ | the whole plane |
| carrier $\mathfrak{su}(2)$ | $\lvert v\rvert^2$ | $\{0\}$ |

**Where the carrier sits.** Away from the origin it is invertible and, by the companion article, spectrally regular: it lies in $\Sigma_{11}$.

**The positive carrier.** The carrier is the only one of the three on which the determinant is positive definite. That positivity is why the null cone of the closure is a cone over a sphere and not a pair of lines.

## Worked Example

**A unit vector.** $v=(1,0,0)$: $A=E_1=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$, $\det=1$, $\tau=0$, eigenvalues $\pm i$.

**A null element.** $A=i\mathrm I_2+E_1=\begin{pmatrix}i&-i\\-i&i\end{pmatrix}$: $\det=0$, $\tau=2i$, eigenvalues $0$ and $2i$, and $A^2=2iA$ verified.

**A Hermitian element.** $A=\mathrm I_2+\sigma_1=\begin{pmatrix}1&1\\1&1\end{pmatrix}$: $\det=0$, so the Hermitian partner is null at the same coordinates.

## Where $n=2$ Differs

**The inertia.** At $n=2$ the form on $\mathfrak{u}(2)$ is real of inertia $(3,1)$, read from the two eigenvalues. At order $n$ a skew matrix is $i$ times a Hermitian one, so $\det$ is real for even $n$ and purely imaginary for odd $n$; the real quadratic form of inertia $(3,1)$ has no direct order-$n$ analogue, and for odd $n$ the determinant of a skew matrix vanishes identically.

**The cone.** At $n=2$ the null cone of the closure is the set $|v|=|\lambda|$, a cone of real dimension three. At order $n$ it is the zero locus of one real polynomial, of real dimension $n^2-1$, and it is the set of skew matrices with a zero eigenvalue.

**What does not differ.** The split $\mathfrak{u}(n)=\mathfrak{u}(1)\oplus\mathfrak{su}(n)$ is orthogonal for the polar form of the determinant at every order, and the line is negative definite at every order.

## Summary

On the skew-adjoint space the determinant is $\det(i\lambda\mathrm I_2+v\cdot E)=|v|^2-\lambda^2$: real, of inertia $(3,1)$, negative on the trace line, positive on the carrier, with the two summands orthogonal. The null locus is the set $|v|=|\lambda|$, a cone of real dimension three with two nappes, and its lines are parametrised by the unit sphere of the carrier.

The carrier is positive definite and therefore norm-regular at every point except the origin, and the determinant is invariant under unitary conjugation, so it is constant on the orbits labelled by $(\lambda,|v|)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{u}(2)=\mathbb{R}(i\mathrm I_2)\oplus\mathfrak{su}(2)$ | the skew-adjoint space |
| $\lambda$ | the real coordinate of the trace line |
| $v=(v_1,v_2,v_3)$ | real coordinates of the carrier |
| $|v|^2$ | the positive definite form on the carrier |
| $\mathfrak{h}$ | the Hermitian half |

## Further Reading

- [The Spin-One Anti-Hermitian Subspace and N Norm Regularity](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity.html), for the source's inertia argument.
- [Introduction to the Spin-One Anti-Hermitian Subspace in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-in-m2c.html), for the space and its action.
- [The Spin-One Anti-Hermitian Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-spectral-regularity-in-m2c.html), for the discriminant on the same space.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm and its zero locus.
- [The Topology of the Zero Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the cone as a union of null lines.
