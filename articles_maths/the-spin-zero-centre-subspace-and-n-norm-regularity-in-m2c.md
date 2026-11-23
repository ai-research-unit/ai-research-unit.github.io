# __The Spin-Zero Centre Subspace and N Norm Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** On the centre of $M_2(\mathbb{C})$, what is the determinant, where does it vanish, and is the whole centre N-regular?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-Zero Centre Subspace and N Norm Regularity](the-spin-zero-centre-subspace-and-n-norm-regularity.html). The source's $N$ norm $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ is $\det A$ under the display, and on a central element $A=\lambda\mathrm I_2$ it is $\lambda^2$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That $\det(\lambda\mathrm I_2)=\lambda^2$ and that the null locus on the centre is the origin alone. That every non-zero central element is invertible with a central inverse. That the real part of the determinant is an indefinite form of inertia $(1,1)$ with isotropic lines $\mathbb{R}(\mathrm I_2\pm i\mathrm I_2)$, on which the determinant is $\pm2i$. That the polar form on the centre is $\lambda\mu$ and is nondegenerate. The comparison with the other two carriers.

**What the article does not do.** It does not treat spectral regularity on the centre, which is [The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-spectral-regularity-in-m2c.html); it does not treat the sectors, which is [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $Q_t=\tfrac12\operatorname{tr}A$ and $N(\tilde Q)=\det A$. The centre is $\mathbb{C}\mathrm I_2$; a central element is written $\lambda\mathrm I_2$ with $\lambda=a+ib$ real $a,b$. The predicate is $\det A\neq0$ for N-regular and $\det A=0$ for N-degenerate.

**Boundaries.** The subspace and its action are [Introduction to the Spin-Zero Centre Subspace in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-in-m2c.html). The dictionary is [The Pauli Representation : Operators](m2c-pauli-representation-operators.html). The zero theory is [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** $\lambda=a+ib$ is the complex coordinate, $B$ the polar form of the determinant, $\Sigma$ a minimal left ideal, $\mathfrak{su}(2)$ the vector part.

## The Norm on the Centre

**The array.** The central element is the scalar array
$$
\lambda\mathrm I_2=\begin{pmatrix}\lambda&0\\0&\lambda\end{pmatrix}.
$$

**The formula.**
$$
N(\lambda e_t)=\det\left(\lambda\mathrm I_2\right)=\lambda^2 ,
$$
verified on random complex $\lambda$ with residual $0$.

**The null locus.**
$$
\{X\in\mathbb{C}\mathrm I_2:\det X=0\}=\{0\},
$$
because $\lambda^2=0$ forces $\lambda=0$, and $\mathbb{C}$ has no nilpotents.

**The inverse.** $(\lambda\mathrm I_2)^{-1}=\lambda^{-1}\mathrm I_2$, with determinant $\lambda^{-2}$, and $\det(\lambda\mathrm I_2)\det(\lambda^{-1}\mathrm I_2)=1$. So the centre is closed under inversion and is a copy of $\mathbb{C}$ inside $M_2(\mathbb{C})$; it contains no zero divisor, and the null cone meets it at one point.

**The contrast with the general element.** A general matrix can be singular while non-zero; a central one cannot. The rank of $\lambda\mathrm I_2$ is two for $\lambda\neq0$ and zero for $\lambda=0$, and there is no intermediate value.

## The Two Real Forms

**The split.** With $\lambda=a+ib$,
$$
\det(\lambda\mathrm I_2)=\left(a^2-b^2\right)+2iab .
$$

**The real part.** $a^2-b^2$ has inertia $(1,1)$ on the real plane, positive on $b=0$ and negative on $a=0$, with isotropic lines $a=\pm b$, that is
$$
\mathcal I_\pm=\mathbb{R}\left(\mathrm I_2\pm i\mathrm I_2\right).
$$

**The determinant on those lines.**
$$
\det\left(\mathrm I_2+i\mathrm I_2\right)=2i,\qquad \det\left(\mathrm I_2-i\mathrm I_2\right)=-2i,
$$
verified exactly. So the isotropic lines of the real part are not null for the determinant.

**The imaginary part.** $2ab$ vanishes on the two coordinate lines $\mathbb{R}\mathrm I_2$ and $i\mathbb{R}\mathrm I_2$, and it is indefinite of inertia $(1,1)$ as well.

**The intersection.** The two zero loci meet only at the origin, which is why the null cone of the determinant meets the centre in one point.

**The square of the diagonal line.** $\left(\mathrm I_2+i\mathrm I_2\right)^2=2i\mathrm I_2$, which is neither the element nor zero; so the isotropic lines are not idempotents. The idempotents are the rank-one projections $\tfrac12(\mathrm I_2+n\cdot\sigma)$, and their determinant is zero, not $\pm2i$.

## The Polar Form

**The definition.** For matrices $X,Y$,
$$
B(X,Y)=\tfrac12\left(\det(X+Y)-\det X-\det Y\right),
$$
the polar form of the determinant.

**On the centre.** $B(\lambda\mathrm I_2,\mu\mathrm I_2)=\lambda\mu$, and the form is nondegenerate there: $B(\lambda\mathrm I_2,\mu\mathrm I_2)=0$ for every $\mu$ forces $\lambda=0$.

**Complex-bilinear, not Hermitian.** $B(iX,iY)=-B(X,Y)$, so $B(\lambda\mathrm I_2,\lambda\mathrm I_2)=\lambda^2$ is not a squared modulus. The Hermitian form on matrices is $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$, and on the centre it is $\bar\lambda\mu$; the two forms differ.

## The Centre Against the Other Carriers

| carrier | determinant on it | null locus in it |
|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | $\lambda^2$ | $\{0\}$ |
| minimal left ideal $\Sigma=M_2P$ | $0$ | the whole ideal |
| vector part $\mathfrak{su}(2)$ | $\lvert v\rvert^2$ | $\{0\}$ |

**The two extremes.** On the centre the determinant separates points; on the ideal it separates nothing, since every element of a minimal left ideal has rank at most one and hence determinant zero; on the vector part it separates points and is positive.

**The reason.** The determinant of $A=v\cdot E=-i\,v\cdot\sigma$ is $|v|^2$, positive definite; the determinant of a rank-one matrix is zero identically; and the determinant of a scalar is the square of the scalar.

**The check.** Verified on a hundred random elements of each carrier: the residual of $\det-\lambda^2$ on the centre, of $\det$ on the ideal and of $\det-|v|^2$ on the vector part are all at the $10^{-15}$ level.

## Where $n=2$ Differs

**The centre.** At $n=2$ the centre is one complex line and the determinant on it is the square of the coordinate, with a double zero at the origin. At order $n$ the determinant on the centre is $\lambda^n$, of multiplicity $n$ at the origin.

**The isotropic lines.** At $n=2$ the real part of the determinant is a form of inertia $(1,1)$ on a real plane, with two isotropic lines. At order $n$ it is a form of inertia $(1,1)$ on the same real plane, because the centre is still one complex line; the inertia does not change with $n$.

**What does differ.** At $n=2$ the ideal has complex dimension two and the vector part three. At order $n$ the ideal has dimension $n$ and the vector part $n^2-1$, and the determinant on the vector part is $|v|^2$ with $v\in\mathbb{R}^{n^2-1}$ only at $n=2$.

## Summary

On the centre the determinant is $N(\lambda e_t)=\lambda^2$, it vanishes only at the origin, and every non-zero central element is invertible with a central inverse. So the centre is N-regular away from zero, contains no zero divisor, and meets the null cone at one point.

Written in real coordinates, $\det=(a^2-b^2)+2iab$: the real part is indefinite of inertia $(1,1)$ with isotropic lines $\mathbb{R}(\mathrm I_2\pm i\mathrm I_2)$, and on those lines the determinant is $\pm2i$. The imaginary part vanishes on the two coordinate lines, and the two zero loci meet only at the origin.

The polar form on the centre is $\lambda\mu$, complex-bilinear and nondegenerate; the Hermitian form is $\bar\lambda\mu$, a different object. Against the other carriers the centre is the case where the determinant separates, the ideal the case where it vanishes identically, and the vector part the case where it is positive.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda=a+ib$ | the coordinate of a central element |
| $\mathbb{C}\mathrm I_2$ | the centre |
| $\mathcal I_\pm$ | the isotropic lines $\mathbb{R}(\mathrm I_2\pm i\mathrm I_2)$ |
| $B(X,Y)$ | the polar form of the determinant |
| $\Sigma=M_2P$ | a minimal left ideal |
| $\mathfrak{su}(2)$ | the vector part |

## Further Reading

- [The Spin-Zero Centre Subspace and N Norm Regularity](the-spin-zero-centre-subspace-and-n-norm-regularity.html), for the source's account of the two real forms.
- [Introduction to the Spin-Zero Centre Subspace in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-in-m2c.html), for the carrier, the closure and the trivial action.
- [The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-spectral-regularity-in-m2c.html), for the other predicate on the same space.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for multiplicativity and the null cone.
- [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-n-norm-regularity-in-m2c.html), for the opposite extreme on the spin-half carrier.
