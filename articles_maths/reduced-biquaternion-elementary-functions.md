# __Reduced Biquaternion Elementary Functions__

## Introduction

This article records the elementary functions of a reduced biquaternion variable: the exponential, the trigonometric and hyperbolic functions, the logarithm and the power functions. The key structural fact is the **idempotent decomposition**: the algebra is the direct product of two copies of $\mathbb{C}$, the idempotents $\Pi_{1,2}$ commute with everything, and the multiplication is componentwise, so every elementary function of a reduced biquaternion reduces to the corresponding elementary function of two ordinary complex numbers, one for each idempotent coordinate. Because the algebra is **commutative**, the functional equations that hold for commuting arguments in the quaternion and split biquaternion cases hold here for all arguments. The treatment is purely mathematical.

Throughout the element is $T=A+Bj$ with $A=a+ia'$, $B=b+ib'$, the idempotent coordinates are $q_1=A+B$, $q_2=A-B$, and $T=q_1\Pi_{1}+q_2\Pi_{2}$ with $\Pi_{1,2}=\tfrac12(1\pm j)$. The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$.

## The Exponential

**Definition.** For $T\in\mathbb{B}_{\mathrm{r}}$ the **exponential** is the series
$$
\exp T=\sum_{n\ge0}\frac{T^{n}}{n!},
$$
which converges for every $T$ because the algebra is finite-dimensional and the series converges in each coordinate.

**Theorem (the reduction and the closed form).** The exponential acts coefficientwise,
$$
\exp T=e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2}=e^{A}\bigl(\cosh B+j\sinh B\bigr),
$$
and it satisfies the functional equation for **all** arguments,
$$
\exp(T+W)=\exp T\;\exp W ,
$$
with $\exp 0=1$.

*Proof.* Using $T^{n}=q_1^{n}\Pi_{1}+q_2^{n}\Pi_{2}$, the series splits into $e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2}$; the second form follows from $q_1=A+B$, $q_2=A-B$ and $e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2}=\tfrac12(e^{q_1}+e^{q_2})+\tfrac12(e^{q_1}-e^{q_2})j=e^{A}\cosh B+e^{A}\sinh B\,j$, because $e^{q_1}+e^{q_2}=e^{A}(e^{B}+e^{-B})$ and $e^{q_1}-e^{q_2}=e^{A}(e^{B}-e^{-B})$. The functional equation holds because the algebra is commutative, so the binomial series reassembles as the Cauchy product of the two exponentials; in the split biquaternion and quaternion cases the same computation fails for non-commuting arguments, the defect being measured by the commutator.

**Corollary (the hyperbolic unit).** The element $j$ has $j^{2}=+1$, so
$$
\exp(j\phi)=\cosh\phi+j\sinh\phi,\qquad \phi\in\mathbb{R},
$$
the **hyperbolic exponential**, whose image is the hyperbola $H(\exp(j\phi))=\cosh^{2}\phi-\sinh^{2}\phi=1$ in the plane $\mathbb{R}\{1,j\}$, where $H(a+bj)=a^{2}-b^{2}$. The element $i$ has $i^{2}=-1$, so $\exp(i\theta)=\cos\theta+i\sin\theta$, whose image is the circle $K=1$ in the plane $\mathbb{R}\{1,i\}$, where $K(a+bi)=a^{2}+b^{2}$.

*Proof.* The first identity is the closed form with $A=0$ and $B=\phi$ real, or the Maclaurin series of $\cosh$ and $\sinh$ in the split complex plane; the second is Euler's formula in the complex plane, where $q_1=q_2=i\theta$.

## The Trigonometric and Hyperbolic Functions

**Definition.** For $T\in\mathbb{B}_{\mathrm{r}}$,
$$
\cos T=\sum_{n\ge0}\frac{(-1)^{n}T^{2n}}{(2n)!},\qquad
\sin T=\sum_{n\ge0}\frac{(-1)^{n}T^{2n+1}}{(2n+1)!},
$$
and likewise $\cosh T$ and $\sinh T$ without the alternating signs. Equivalently, from the exponential,
$$
\cos T=\frac{e^{iT}+e^{-iT}}{2},\quad \sin T=\frac{e^{iT}-e^{-iT}}{2i},\quad
\cosh T=\frac{e^{T}+e^{-T}}{2},\quad \sinh T=\frac{e^{T}-e^{-T}}{2}.
$$

**Theorem (the reduction and the identities).** Each function acts coefficientwise,
$$
\cos T=\cos q_1\,\Pi_{1}+\cos q_2\,\Pi_{2},\qquad \mathrm{etc.},
$$
and the Pythagorean and addition identities hold for all arguments,
$$
\cos^{2}T+\sin^{2}T=1,\qquad \cosh^{2}T-\sinh^{2}T=1,\qquad \cos(T+W)=\cos T\cos W-\sin T\sin W .
$$

*Proof.* The series split in the idempotent coordinates into the corresponding series of $q_1$ and of $q_2$; the identities hold in each coordinate by the classical complex identities, and since the algebra is commutative the addition formula needs no ordering correction.

**Corollary (the two kinds of rotation).** In the plane $\mathbb{R}\{1,i\}$ the map $T\mapsto e^{i\theta}T$ is the ordinary elliptic rotation by $\theta$; in the plane $\mathbb{R}\{1,j\}$ the map $T\mapsto e^{j\phi}T$ is the hyperbolic rotation by $\phi$, dilating the two halves $q_1,q_2$ reciprocally. This is the elliptic-versus-hyperbolic dichotomy carried by the two directions $i$ and $j$.

*Proof.* Multiplication by $e^{i\theta}=\cos\theta+i\sin\theta$ is the complex rotation in the first plane; multiplication by $e^{j\phi}=\cosh\phi+j\sinh\phi$ sends $q_1\mapsto e^{\phi}q_1$ and $q_2\mapsto e^{-\phi}q_2$, a reciprocal dilation, which is the hyperbolic rotation of the split complex plane.

## The Logarithm

**Definition.** A **logarithm** of $T$ is a solution $S$ of $\exp S=T$.

**Theorem (existence and the reduction).** An element has a logarithm if and only if it is a **unit**, that is $q_1\neq0$ and $q_2\neq0$, and then
$$
\log T=\log q_1\,\Pi_{1}+\log q_2\,\Pi_{2}
$$
for a choice of the two complex branches. The principal value is obtained from the principal branch of the complex logarithm in each coordinate; the solution is determined modulo the kernel, which is the lattice $2\pi i\bigl(\mathbb{Z}\Pi_{1}+\mathbb{Z}\Pi_{2}\bigr)$.

*Proof.* The equation $e^{S}=T$ splits into $e^{s_{1}}=q_1$ and $e^{s_{2}}=q_2$, each solvable exactly for non-zero right-hand side, with solutions differing by $2\pi i$; the two coordinates are independent, and the non-units, having a vanishing coordinate, have no logarithm.

**Corollary (the branch structure).** The logarithm exists on the unit group $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ but is not single-valued: it is a covering map onto the algebra, and a single-valued branch exists exactly on a simply connected domain of the unit group avoiding the two coordinate lines.

*Proof.* The exponential is a local biholomorphism with discrete kernel, so its inverse is multivalued with the stated kernel, and a single-valued branch on a domain exists precisely when the domain is simply connected and avoids the two coordinate axes.

## The Power Functions

**Definition.** For a unit $T$ and a complex exponent $s$, the **power** is
$$
T^{s}=\exp(s\log T)=q_1^{s}\Pi_{1}+q_2^{s}\Pi_{2},
$$
for a choice of the logarithms, and for an integer $s=n$ it agrees with the ordinary power $T^{n}$.

**Theorem (the roots).** For a non-zero integer $n$ the equation $S^{n}=T$ has, for each unit $T$, exactly $n^{2}$ solutions, namely
$$
S=\Bigl(\eta_{1}\,q_1^{1/n}\Bigr)\Pi_{1}+\Bigl(\eta_{2}\,q_2^{1/n}\Bigr)\Pi_{2},
$$
where $\eta_{1},\eta_{2}$ range over the $n$-th roots of unity. In particular a unit has four square roots, $\pm q_1^{1/2}\Pi_{1}\pm q_2^{1/2}\Pi_{2}$; a zero divisor has the roots with the corresponding factor absent.

*Proof.* In each coordinate the equation $s^{n}=q_1$ has the $n$ roots $\eta q_1^{1/n}$, and the two coordinates are independent, giving the product of the two counts; for the square root $n=2$ the roots of unity are $\pm1$ in each coordinate, whence the four sign combinations.

**Corollary (the integer powers are polynomial).** For an integer $n\ge0$, $T^{n}=q_1^{n}\Pi_{1}+q_2^{n}\Pi_{2}$ is a polynomial in $T$, and for $n<0$ it is the inverse power on the units; the map $T\mapsto T^{n}$ is a homomorphism of the multiplicative monoid whose kernel on the unit group is the group of the $n$-th roots of unity in the two coordinates.

*Proof.* The integer powers are the iterated products, read in the coordinates; the kernel is the set of the $T$ with $q_1^{n}=q_2^{n}=1$.

## Relations to the Complex and Split-Complex Cases

**The complex case.** If the second coefficient vanishes, $T=A$, then $q_1=q_2=A$ and every elementary function reduces to the ordinary complex function, $f(T)=f(A)$: the reduced biquaternion function restricts to the complex function on the complex line $\mathbb{C}=\mathbb{R}\{1,i\}$.

**The split-complex case.** If both coefficients are real, $T=a+bj$ in the split complex algebra $\mathbb{D}=\mathbb{R}\{1,j\}$, then $q_1=a+b$ and $q_2=a-b$ are real and
$$
\exp(a+bj)=e^{a}\bigl(\cosh b+j\sinh b\bigr),\qquad \log(a+bj)=\tfrac12\log(a^{2}-b^{2})+\tfrac12 j\log\frac{a+b}{a-b},
$$
on the units with $a>|b|$, so that $a\pm b>0$ and the principal logarithms are real; the reduced biquaternion functions restrict to these on the split complex plane.

*Proof.* On the complex line $B=0$ and $q_1=q_2=A$, so both coordinates carry the same function; on the split complex plane the coefficients are real, $q_1=a+b$ and $q_2=a-b$, and substitution in the two-factor formulas gives the displayed expressions, the sums and differences of the two logarithms reproducing the hyperbolic and the logarithmic forms.

## The Reduction to Two Complex Factors

**Theorem (the general reduction principle).** Let $F$ be a function defined on a set of complex numbers by a power series with a non-zero radius of convergence, or by an integral of a holomorphic kernel. Then $F$ extends to the reduced biquaternion algebra by
$$
F(T)=F(q_1)\,\Pi_{1}+F(q_2)\,\Pi_{2},
$$
and the extension is a homomorphism property for the pointwise operations: it commutes with sums, with products, with the conjugations that preserve the factors, and with the differentiation $\bar\partial$. Every elementary function above is the special case of the principle applied to the corresponding complex function.

*Proof.* A convergent power series can be evaluated in each coordinate by substitution, and the integral representation is evaluated coefficientwise; the algebraic identities hold in each coordinate and hence in the algebra; the differentiation $\bar\partial$ acts coefficientwise, so it commutes with the extension.

## Summary of Formulas

| Function | Value | Domain |
|---|---|---|
| $\exp T$ | $e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2}=e^{A}(\cosh B+j\sinh B)$ | all $T$ |
| $\exp(T+W)$ | $\exp T\exp W$ | all $T,W$, the algebra being commutative |
| $\exp(j\phi)$ | $\cosh\phi+j\sinh\phi$ | $\phi\in\mathbb{R}$ |
| $\exp(i\theta)$ | $\cos\theta+i\sin\theta$ | $\theta\in\mathbb{R}$ |
| $\cos T,\ \sin T$ | $\cos q_1\,\Pi_{1}+\cos q_2\,\Pi_{2}$, $\sin q_1\,\Pi_{1}+\sin q_2\,\Pi_{2}$ | all $T$ |
| $\cosh T,\ \sinh T$ | $\cosh q_1\,\Pi_{1}+\cosh q_2\,\Pi_{2}$, $\sinh q_1\,\Pi_{1}+\sinh q_2\,\Pi_{2}$ | all $T$ |
| $\log T$ | $\log q_1\,\Pi_{1}+\log q_2\,\Pi_{2}$ | the units, branch choice |
| $T^{s}$ | $q_1^{s}\Pi_{1}+q_2^{s}\Pi_{2}$ | the units, branch choice |
| $S^{n}=T$ | $n^{2}$ solutions $\eta_{1}q_1^{1/n}\Pi_{1}+\eta_{2}q_2^{1/n}\Pi_{2}$ | $T$ a unit |

## Comparison with the Biquaternion Case

The biquaternion algebra $M_{2}(\mathbb{C})$ is simple and non-commutative; its exponential is a matrix exponential, its trigonometric functions are entire but the functional equations fail for non-commuting arguments, and the logarithm requires the matrix logarithm with its own branch structure. The reduced biquaternion algebra replaces the single matrix exponential by the **pair** of complex exponentials of the two idempotent coordinates: the functional equation $\exp(T+W)=\exp T\exp W$ holds for all arguments because the algebra is commutative, the trigonometric functions are the two complex trigonometric functions, the logarithm exists exactly on the units and is the pair of complex logarithms, and the power functions have the $n^{2}$ roots of the two coordinates. The split biquaternion case is the same pair structure with the quaternion exponential in each half; the reduced case is the commutative member in which every elementary function is a pair of complex elementary functions.

## Summary

Every elementary function of a reduced biquaternion variable is the pair of the corresponding complex elementary functions of the two idempotent coordinates: the exponential is $\exp T=e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2}=e^{A}(\cosh B+j\sinh B)$, with the functional equation holding for all arguments because the algebra is commutative; the element $i$ generates the elliptic rotation, $\exp(i\theta)=\cos\theta+i\sin\theta$, and the element $j$ the hyperbolic one, $\exp(j\phi)=\cosh\phi+j\sinh\phi$, dilating the two halves reciprocally. The trigonometric and hyperbolic functions are the pairs $\cos q_1\Pi_{1}+\cos q_2\Pi_{2}$ and the like, and the Pythagorean and addition identities hold for all arguments. The logarithm exists exactly on the units, $q_1,q_2\neq0$, and is $\log q_1\Pi_{1}+\log q_2\Pi_{2}$ for a branch choice in each coordinate, the kernel being the lattice $2\pi i(\mathbb{Z}\Pi_{1}+\mathbb{Z}\Pi_{2})$. The power $T^{s}=q_1^{s}\Pi_{1}+q_2^{s}\Pi_{2}$, and the equation $S^{n}=T$ has $n^{2}$ solutions for a unit, in particular four square roots. On the complex line the functions restrict to the complex ones, on the split complex plane to the split complex ones, and the general principle is that every function defined by a power series or a holomorphic integral extends coefficientwise. Against the biquaternion case, where the matrix exponential and the matrix logarithm carry the non-commutative branch structure, the reduced biquaternion elementary functions are the two commutative complex ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T=A+Bj$ | Element, $A=a+ia'$, $B=b+ib'$ |
| $q_1=A+B$, $q_2=A-B$ | Idempotent coordinates |
| $\Pi_{1,2}=\tfrac12(1\pm j)$ | Idempotents |
| $\exp T=e^{q_1}\Pi_{1}+e^{q_2}\Pi_{2}$ | Exponential |
| $e^{j\phi}=\cosh\phi+j\sinh\phi$ | Hyperbolic exponential |
| $e^{i\theta}=\cos\theta+i\sin\theta$ | Elliptic exponential |
| $\log T=\log q_1\,\Pi_{1}+\log q_2\,\Pi_{2}$ | Logarithm on the units |
| $T^{s}=q_1^{s}\Pi_{1}+q_2^{s}\Pi_{2}$ | Power function |
| $\eta_{1},\eta_{2}$ | $n$-th roots of unity of the two coordinates |

## Further Reading

- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the exponential, the trigonometric functions and the logarithm of one complex variable.
- Lars V. Ahlfors, *Complex Analysis*, 3rd edition (McGraw-Hill, 1979), for the branch structure of the logarithm and the power functions.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the exponential and the elementary functions of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the idempotent reduction of the elementary functions.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the exponential of the hypercomplex algebras and the comparison with the division-algebra cases.
