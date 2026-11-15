# __The Four Forms and Their Algebraic Norms__

## Introduction

**Four forms live on the matrix space — the trace form, the Killing form, the Hilbert–Schmidt form and the determinant — and each carries a norm: $\operatorname{tr}(X^{2})$, $2n\operatorname{tr}(X^{2})-2(\operatorname{tr}X)^{2}$, $\operatorname{tr}(X^{*}X)$ and $\det X$, of which only the last is multiplicative.**

The article puts the four forms side by side, computes the quadratic function attached to each, proves the three identities that relate them on the two halves and on the traceless part, proves the bound $|\det X|\le(\operatorname{tr}(X^{*}X)/n)^{n/2}$ from the arithmetic–geometric mean of the singular values, and explains which form is adapted to which structure. It assumes *The Trace Form and Its Signature on the Two Halves*, *The Killing Form, Its Radical and the Triangular Case* and *The Hilbert–Schmidt Form* for the three bilinear forms, and *The Element: Rank, Trace, Determinant, Characteristic Polynomial* for the determinant. It defers the cone to *The Positive Cone and Its Boundary* and the geometry of the group to *The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin*.

## The Four Forms

**Each form is a bilinear or multilinear object on the same space.** The four are

$$
\langle X,Y\rangle_{1}=\operatorname{tr}(XY),\qquad B(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$

$$
\langle X,Y\rangle_{3}=\operatorname{tr}(X^{*}Y),\qquad N(X)=\det X .
$$

The first is symmetric over $\mathbb{R}$ and complex bilinear over $\mathbb{C}$; the second is the Killing form, of which the first is the traceless part up to the factor $2n$; the third is Hermitian and positive definite; the fourth is not bilinear at all but homogeneous of degree $n$.

**The first three are the same formula read in three ways.** All three are $\operatorname{tr}(XY)$ with a different notion of adjoint: the trace form uses the transpose, the Killing form corrects by the traces, and the Hilbert–Schmidt form uses the conjugate transpose. So

$$
\langle X,Y\rangle_{1}=\operatorname{tr}(X^{\mathsf T}Y)\big|_{Y\to Y},\qquad B=2n\langle\cdot,\cdot\rangle_{1}-2\operatorname{tr}\otimes\operatorname{tr},\qquad \langle X,Y\rangle_{3}=\operatorname{tr}(X^{*}Y),
$$

and the passage from the first to the third is the passage from the real form to the Hermitian one.

**The fourth form is the only one that is multiplicative.** For all $X,Y$,

$$
N(XY)=N(X)N(Y),\qquad N(\mathrm{I})=1,
$$

so the determinant is a homomorphism from the multiplicative monoid of matrices to the scalars, and it is the algebraic norm in the sense of the theory of algebras: the norm of an element of a central simple algebra, of degree $n$. None of the three bilinear forms is multiplicative, and that is the structural difference between the determinant and the other three.

## The Norms Attached to the Three Bilinear Forms

**The trace form gives the quadratic function $\operatorname{tr}(X^{2})$, indefinite with the signature of the form.** Put $q_1(X)=\langle X,X\rangle_{1}=\operatorname{tr}(X^{2})$. On the two halves,

$$
q_1(S)=\sum_{i,j}S_{ij}^{2}>0\ (S\neq0),\qquad q_1(K)=-\sum_{i,j}K_{ij}^{2}<0\ (K\neq0),
$$

so $q_1$ is positive definite on $\operatorname{Sym}_n$ and negative definite on $\operatorname{Skew}_n$, with signature $(n(n+1)/2,n(n-1)/2)$ on the whole algebra. So the "norm" of the trace form is not a norm: it is a quadratic form of indefinite type, and it is a norm only after restriction to the symmetric half.

**The Killing form gives $q_2(X)=2n\operatorname{tr}(X^{2})-2(\operatorname{tr}X)^{2}$, which agrees with $2n\,q_1$ on the traceless part.** Since $\operatorname{tr}(X)=0$ there,

$$
q_2(X)=2n\operatorname{tr}(X^{2})=2n\,q_1(X)\qquad(X\in\mathfrak{sl}_n),
$$

which was verified at $n=2,3,4$. So the two forms have the same signs and differ only by the scalar $2n$ on the traceless algebra, and the correction term is what makes $q_2$ vanish on the scalars, since $q_1(\mathrm{I})=n$ and $q_2(\mathrm{I})=2n\cdot n-2n^{2}=0$.

**The Hilbert–Schmidt form gives the positive definite norm.** Put $q_3(X)=\operatorname{tr}(X^{*}X)$. On the real symmetric matrices $q_3$ agrees with $q_1$, since $X^{*}=X^{\mathsf T}=X$ there and

$$
\operatorname{tr}(X^{*}X)=\operatorname{tr}(X^{2})=\sum_{i,j}X_{ij}^{2},
$$

which was verified on real symmetric matrices at $n=2,3,4$. So the three forms agree in pairs on the two halves, and they differ in the directions where the involution does not act.

**The three quadratic functions are related by one inequality.** For every $X$,

$$
|\langle X,Y\rangle_{1}|\ \le\ \|X\|_{3}\,\|Y\|_{3},
$$

by the Cauchy–Schwarz inequality for the Hilbert–Schmidt form, which was verified on random pairs. So the indefinite form is bounded by the definite one, and the bound is sharp on the pairs $X$, $X^{*}$.

## The Determinant and Its Bound

**The determinant is bounded by the Hilbert–Schmidt norm.** If $s_1,\dots,s_n$ are the singular values of $X$, then $N(X)=\prod s_i$ up to the phase and $q_3(X)=\sum s_i^{2}$, so the arithmetic–geometric mean inequality gives

$$
|N(X)|=\prod_{i=1}^{n}s_i\ \le\ \Big(\frac{1}{n}\sum_{i=1}^{n}s_i^{2}\Big)^{n/2}=\Big(\frac{q_3(X)}{n}\Big)^{n/2}.
$$

The bound was verified at $n=2,3,4$ on random complex matrices, with the two sides differing by orders of magnitude away from equality.

**Equality holds exactly on the scalar multiples of unitary matrices.** The arithmetic–geometric mean is an equality exactly when all singular values are equal, which happens exactly when $X$ is a scalar multiple of a unitary matrix. So

$$
|N(X)|=\Big(\frac{q_3(X)}{n}\Big)^{n/2}\iff X=cU,\ |c|\ge0,\ U\in\mathrm{U}(n),
$$

and the group $\mathrm{U}(n)$ is the set on which the two norms agree.

**The same bound with the trace form holds on the symmetric half.** For $X$ positive semidefinite,

$$
N(X)=\det X\le\Big(\frac{\operatorname{tr}X}{n}\Big)^{n},
$$

the classical inequality for positive matrices, with equality exactly at $X=c\mathrm{I}$. So the determinant is controlled by the trace on the cone and by the Hilbert–Schmidt norm on the whole space, and the two bounds coincide on the scalars.

**The determinant vanishes exactly on the singular matrices, so its zero set is the hypersurface of rank $<n$.** The determinantal variety has dimension $n^{2}-1$, and the formula for its dimension is the rank formula of *The Element: Rank, Trace, Determinant, Characteristic Polynomial* read at $r=n-1$. So the fourth "norm" has a large zero set, unlike the other three, which vanish only at the origin.

## Which Form for Which Structure

**The trace form is the form of the Lie structure.** It is invariant under all of $\mathrm{GL}_n$ and every derivation is anti-self-adjoint for it, so it is the form in which the group acts by isometries and the Lie algebra sits as a space of anti-self-adjoint operators. Its indefiniteness is the price of the invariance, since a definite invariant form would make the group compact.

**The Killing form is the form of the structure theory.** It is invariant and it detects the radical, since its radical is the centre and its restriction to $\mathfrak{sl}_n$ is nondegenerate. So it is the form that decides semisimplicity, and it is a scalar multiple of the trace form exactly on the semisimple part.

**The Hilbert–Schmidt form is the form of the Hilbert space and of the operator theory.** It is definite, it gives the adjoints their familiar shape, and it turns the matrix space into a Hilbert space on which the one-sided and two-sided operators act. Its failure of invariance under the full group is the price of the definiteness.

**The determinant is the form of the multiplicative structure.** It is multiplicative, homogeneous of degree $n$, and it is the only one of the four that is a polynomial of degree $n$ rather than a bilinear pairing. So the four forms see the four structures — Lie, structure theory, Hilbert space and multiplicative monoid — and no one of them sees more than one.

## The Case $n=2$

**At $n=2$ the four forms are computable in one line each.** With $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,

$$
q_1(X)=a^{2}+d^{2}+2bc,\qquad q_2(X)=4(a^{2}+d^{2}+2bc)-2(a+d)^{2},
$$

$$
q_3(X)=|a|^{2}+|b|^{2}+|c|^{2}+|d|^{2},\qquad N(X)=ad-bc,
$$

and the four are related by $q_2=4q_1-2(\operatorname{tr}X)^{2}$ and $|N|\le q_3/2$, the second being the bound at $n=2$ with $(q_3/2)^{1}=q_3/2$. Both identities were verified numerically on random complex matrices.

**The bound $|N|\le q_3/2$ is attained exactly on the unitary multiples.** For $X=cU$ with $U\in\mathrm{U}(2)$,

$$
|N(X)|=|c|^{2},\qquad \frac{q_3(X)}{2}=\frac{2|c|^{2}}{2}=|c|^{2},
$$

so the two sides are equal, which the computation confirms on random unitary matrices.

**The biquaternion reading gives the four forms their names.** The algebraic norm is $N$, indefinite of signature $(2,2)$ on the four real coordinates; the trace form is its trace shadow of signature $(3,1)$; the Hilbert–Schmidt form is the Euclidean form of signature $(4,0)$; and the Killing form is the traceless part of the trace form, vanishing on the identity. So the four forms are the four ways of reading the same four coordinates, and the signatures $(2,2)$, $(3,1)$, $(4,0)$ and $(3,0)$ on the traceless part are the arithmetic of the biquaternion algebra.

## Summary

The matrix space carries four forms: the trace form $\operatorname{tr}(XY)$, indefinite with signature $(n(n+1)/2,n(n-1)/2)$; the Killing form $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$, equal to $2n$ times the trace form on the traceless algebra and vanishing on the scalars; the Hilbert–Schmidt form $\operatorname{tr}(X^{*}Y)$, positive definite and agreeing with the trace form on the real symmetric matrices; and the determinant, homogeneous of degree $n$ and the only multiplicative one. The determinant is bounded by the Hilbert–Schmidt norm through the arithmetic–geometric mean of the singular values, with equality exactly on the scalar multiples of unitary matrices, and by the trace on the positive cone, with equality exactly on the scalars. Each form is adapted to one structure: Lie, structure theory, Hilbert space and multiplicative monoid.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle_{1}=\operatorname{tr}(XY)$ | the trace form |
| $B(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$ | the Killing form |
| $\langle X,Y\rangle_{3}=\operatorname{tr}(X^{*}Y)$ | the Hilbert–Schmidt form |
| $N(X)=\det X$ | the algebraic norm, of degree $n$ |
| $q_1=\operatorname{tr}(X^{2})$, $q_2=B(X,X)$, $q_3=\operatorname{tr}(X^{*}X)$ | the three quadratic functions |
| $|N(X)|\le(q_3(X)/n)^{n/2}$ | the arithmetic–geometric mean bound |
| $cU$ with $U\in\mathrm{U}(n)$ | the equality case of the bound |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the determinant, the singular values and the classical inequalities.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the arithmetic–geometric mean inequality for matrices and the norm inequalities.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the algebraic norm of a central simple algebra and its multiplicativity.
- [The Hilbert–Schmidt Form](the-hilbert-schmidt-form.html), for the definite form and the norm used in the bound.
- [The Killing Form, Its Radical and the Triangular Case](the-killing-form-its-radical-and-the-triangular-case.html), for the second of the four forms.
- [The Trace Form and Its Signature on the Two Halves](the-trace-form-and-its-signature-on-the-two-halves.html), for the first of the four and its signature.
