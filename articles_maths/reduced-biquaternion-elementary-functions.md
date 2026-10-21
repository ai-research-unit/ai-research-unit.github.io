# __Reduced Biquaternion Elementary Functions__

## Introduction

This article records the elementary functions of a reduced biquaternion variable: the exponential, the trigonometric and hyperbolic functions, the logarithm and the power functions. The key structural fact is the **idempotent decomposition**: the algebra is the direct product of two copies of $\mathbb{C}$, the idempotents $\Pi_{\pm}$ commute with everything, and the multiplication is componentwise, so every elementary function of a reduced biquaternion reduces to the corresponding elementary function of two ordinary complex numbers, one for each idempotent coordinate. Because the algebra is **commutative**, the functional equations that hold for commuting arguments in the quaternion and split biquaternion cases hold here for all arguments. The treatment is purely mathematical.

Throughout the element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, the idempotent coordinates are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, and $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$.

## The Exponential

**Definition.** For $\breve Q\in\mathbb{B}_{\mathrm{r}}$ the **exponential** is the series
$$
\exp \breve Q=\sum_{n\ge0}\frac{\breve Q^{n}}{n!},
$$
which converges for every $\breve Q$ because the algebra is finite-dimensional and the series converges in each coordinate.

**Theorem (the reduction and the closed form).** The exponential acts coefficientwise,
$$
\exp \breve Q=e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-=e^{Q_{\blacktriangle}}\bigl(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown}\bigr),
$$
and it satisfies the functional equation for **all** arguments,
$$
\exp(\breve Q+\breve Q_{2})=\exp \breve Q\;\exp \breve Q_{2} ,
$$
with $\exp 0=1$.

*Proof.* Using $\breve Q^{n}=Q_{+}^{n}\Pi_++Q_{-}^{n}\Pi_-$, the series splits into $e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-$; the second form follows from $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ and $e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-=\tfrac12(e^{Q_{+}}+e^{Q_{-}})+\tfrac12(e^{Q_{+}}-e^{Q_{-}})j=e^{Q_{\blacktriangle}}\cosh Q_{\blacktriangledown}+e^{Q_{\blacktriangle}}\sinh Q_{\blacktriangledown}\,j$, because $e^{Q_{+}}+e^{Q_{-}}=e^{Q_{\blacktriangle}}(e^{Q_{\blacktriangledown}}+e^{-Q_{\blacktriangledown}})$ and $e^{Q_{+}}-e^{Q_{-}}=e^{Q_{\blacktriangle}}(e^{Q_{\blacktriangledown}}-e^{-Q_{\blacktriangledown}})$. The functional equation holds because the algebra is commutative, so the binomial series reassembles as the Cauchy product of the two exponentials; in the split biquaternion and quaternion cases the same computation fails for non-commuting arguments, the defect being measured by the commutator.

**Corollary (the hyperbolic unit).** The element $j$ has $j^{2}=+1$, so
$$
\exp(j\phi)=\cosh\phi+j\sinh\phi,\qquad \phi\in\mathbb{R},
$$
the **hyperbolic exponential**, whose image is the hyperbola $H(\exp(j\phi))=\cosh^{2}\phi-\sinh^{2}\phi=1$ in the plane $\mathbb{R}\{1,j\}$, where $H(a+bj)=a^{2}-b^{2}$. The element $i$ has $i^{2}=-1$, so $\exp(i\theta)=\cos\theta+i\sin\theta$, whose image is the circle $K=1$ in the plane $\mathbb{R}\{1,i\}$, where $K(a+bi)=a^{2}+b^{2}$.

*Proof.* The first identity is the closed form with $Q_{\blacktriangle}=0$ and $Q_{\blacktriangledown}=\phi$ real, or the Maclaurin series of $\cosh$ and $\sinh$ in the split complex plane; the second is Euler's formula in the complex plane, where $Q_{+}=Q_{-}=i\theta$.

## The Trigonometric and Hyperbolic Functions

**Definition.** For $\breve Q\in\mathbb{B}_{\mathrm{r}}$,
$$
\cos \breve Q=\sum_{n\ge0}\frac{(-1)^{n}\breve Q^{2n}}{(2n)!},\qquad
\sin \breve Q=\sum_{n\ge0}\frac{(-1)^{n}\breve Q^{2n+1}}{(2n+1)!},
$$
and likewise $\cosh \breve Q$ and $\sinh \breve Q$ without the alternating signs. Equivalently, from the exponential,
$$
\cos \breve Q=\frac{e^{i\breve Q}+e^{-i\breve Q}}{2},\quad \sin \breve Q=\frac{e^{i\breve Q}-e^{-i\breve Q}}{2i},\quad
\cosh \breve Q=\frac{e^{\breve Q}+e^{-\breve Q}}{2},\quad \sinh \breve Q=\frac{e^{\breve Q}-e^{-\breve Q}}{2}.
$$

**Theorem (the reduction and the identities).** Each function acts coefficientwise,
$$
\cos \breve Q=\cos Q_{+}\,\Pi_++\cos Q_{-}\,\Pi_-,\qquad \mathrm{etc.},
$$
and the Pythagorean and addition identities hold for all arguments,
$$
\cos^{2}\breve Q+\sin^{2}\breve Q=1,\qquad \cosh^{2}\breve Q-\sinh^{2}\breve Q=1,\qquad \cos(\breve Q_{1}+\breve Q_{2})=\cos \breve Q_{1}\cos \breve Q_{2}-\sin \breve Q_{1}\sin \breve Q_{2} .
$$

*Proof.* The series split in the idempotent coordinates into the corresponding series of $Q_{+}$ and of $Q_{-}$; the identities hold in each coordinate by the classical complex identities, and since the algebra is commutative the addition formula needs no ordering correction.

**Corollary (the two kinds of rotation).** In the plane $\mathbb{R}\{1,i\}$ the map $\breve Q\mapsto e^{i\theta}\breve Q$ is the ordinary elliptic rotation by $\theta$; in the plane $\mathbb{R}\{1,j\}$ the map $\breve Q\mapsto e^{j\phi}\breve Q$ is the hyperbolic rotation by $\phi$, dilating the two halves $Q_{+},Q_{-}$ reciprocally. This is the elliptic-versus-hyperbolic dichotomy carried by the two directions $i$ and $j$.

*Proof.* Multiplication by $e^{i\theta}=\cos\theta+i\sin\theta$ is the complex rotation in the first plane; multiplication by $e^{j\phi}=\cosh\phi+j\sinh\phi$ sends $Q_{+}\mapsto e^{\phi}Q_{+}$ and $Q_{-}\mapsto e^{-\phi}Q_{-}$, a reciprocal dilation, which is the hyperbolic rotation of the split complex plane.

## The Logarithm

**Definition.** A **logarithm** of $\breve Q$ is a solution $\breve Q_{\log}$ of $\exp \breve Q_{\log}=\breve Q$.

**Theorem (existence and the reduction).** An element has a logarithm if and only if it is a **unit**, that is $Q_{+}\neq0$ and $Q_{-}\neq0$, and then
$$
\log \breve Q=\log Q_{+}\,\Pi_++\log Q_{-}\,\Pi_-
$$
for a choice of the two complex branches. The principal value is obtained from the principal branch of the complex logarithm in each coordinate; the solution is determined modulo the kernel, which is the lattice $2\pi i\bigl(\mathbb{Z}\Pi_++\mathbb{Z}\Pi_-\bigr)$.

*Proof.* The equation $e^{\breve Q_{\log}}=\breve Q$ splits into $e^{s_{1}}=Q_{+}$ and $e^{s_{2}}=Q_{-}$, each solvable exactly for non-zero right-hand side, with solutions differing by $2\pi i$; the two coordinates are independent, and the non-units, having a vanishing coordinate, have no logarithm.

**Corollary (the branch structure).** The logarithm exists on the unit group $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ but is not single-valued: it is a covering map onto the unit group, and a single-valued branch exists exactly on a simply connected domain of the unit group.

*Proof.* The exponential is a local biholomorphism with discrete kernel, so its inverse is multivalued with the stated kernel, and a single-valued branch on a domain exists precisely when the domain is simply connected and avoids the two coordinate axes.

## The Power Functions

**Definition.** For a unit $\breve Q$ and a complex exponent $s$, the **power** is
$$
\breve Q^{s}=\exp(s\log \breve Q)=Q_{+}^{s}\Pi_++Q_{-}^{s}\Pi_-,
$$
for a choice of the logarithms, and for an integer $s=n$ it agrees with the ordinary power $\breve Q^{n}$.

**Theorem (the roots).** For a non-zero integer $n$ the equation $\breve Q_{2}^{n}=\breve Q$ has, for each unit $\breve Q$, exactly $n^{2}$ solutions, namely
$$
\breve Q_{2}=\Bigl(\eta_{1}\,Q_{+}^{1/n}\Bigr)\Pi_++\Bigl(\eta_{2}\,Q_{-}^{1/n}\Bigr)\Pi_-,
$$
where $\eta_{1},\eta_{2}$ range over the $n$-th roots of unity. In particular a unit has four square roots, $\pm Q_{+}^{1/2}\Pi_+\pm Q_{-}^{1/2}\Pi_-$; a zero divisor has the roots with the corresponding factor absent.

*Proof.* In each coordinate the equation $s^{n}=Q_{+}$ has the $n$ roots $\eta Q_{+}^{1/n}$, and the two coordinates are independent, giving the product of the two counts; for the square root $n=2$ the roots of unity are $\pm1$ in each coordinate, whence the four sign combinations.

**Corollary (the integer powers are polynomial).** For an integer $n\ge0$, $\breve Q^{n}=Q_{+}^{n}\Pi_++Q_{-}^{n}\Pi_-$ is a polynomial in $\breve Q$, and for $n<0$ it is the inverse power on the units; the map $\breve Q\mapsto \breve Q^{n}$ is a homomorphism of the multiplicative monoid whose kernel on the unit group is the group of the $n$-th roots of unity in the two coordinates.

*Proof.* The integer powers are the iterated products, read in the coordinates; the kernel is the set of the $\breve Q$ with $Q_{+}^{n}=Q_{-}^{n}=1$.

## Relations to the Complex and Split-Complex Cases

**The complex case.** If the second coefficient vanishes, $\breve Q=Q_{\blacktriangle}$, then $Q_{+}=Q_{-}=Q_{\blacktriangle}$ and every elementary function reduces to the ordinary complex function, $f(\breve Q)=f(Q_{\blacktriangle})$: the reduced biquaternion function restricts to the complex function on the complex line $\mathbb{C}=\mathbb{R}\{1,i\}$.

**The split-complex case.** If both coefficients are real, $\breve Q=q_{\blacktriangle}+jq_{\blacktriangledown}$ in the split complex algebra $\mathbb{D}=\mathbb{R}\{1,j\}$, then $Q_{+}=q_{\blacktriangle}+q_{\blacktriangledown}$ and $Q_{-}=q_{\blacktriangle}-q_{\blacktriangledown}$ are real and
$$
\exp(q_{\blacktriangle}+jq_{\blacktriangledown})=e^{q_{\blacktriangle}}\bigl(\cosh q_{\blacktriangledown}+j\sinh q_{\blacktriangledown}\bigr),\qquad \log(q_{\blacktriangle}+jq_{\blacktriangledown})=\tfrac12\log(q_{\blacktriangle}^{2}-q_{\blacktriangledown}^{2})+\tfrac12 j\log\frac{q_{\blacktriangle}+q_{\blacktriangledown}}{q_{\blacktriangle}-q_{\blacktriangledown}},
$$
on the units with $q_{\blacktriangle}>|q_{\blacktriangledown}|$, so that $q_{\blacktriangle}\pm q_{\blacktriangledown}>0$ and the principal logarithms are real; the reduced biquaternion functions restrict to these on the split complex plane.

*Proof.* On the complex line $Q_{\blacktriangledown}=0$ and $Q_{+}=Q_{-}=Q_{\blacktriangle}$, so both coordinates carry the same function; on the split complex plane the coefficients are real, $Q_{+}=q_{\blacktriangle}+q_{\blacktriangledown}$ and $Q_{-}=q_{\blacktriangle}-q_{\blacktriangledown}$, and substitution in the two-factor formulas gives the displayed expressions, the sums and differences of the two logarithms reproducing the hyperbolic and the logarithmic forms.

## The Reduction to Two Complex Factors

**Theorem (the general reduction principle).** Let $F$ be a function defined on a set of complex numbers by a power series with a non-zero radius of convergence, or by an integral of a holomorphic kernel. Then $F$ extends to the reduced biquaternion algebra by
$$
F(\breve Q)=F(Q_{+})\,\Pi_++F(Q_{-})\,\Pi_-,
$$
and the extension is a homomorphism property for the pointwise operations: it commutes with sums, with products, with the conjugations that preserve the factors, and with the differentiation $\bar\partial$. Every elementary function above is the special case of the principle applied to the corresponding complex function.

*Proof.* A convergent power series can be evaluated in each coordinate by substitution, and the integral representation is evaluated coefficientwise; the algebraic identities hold in each coordinate and hence in the algebra; the differentiation $\bar\partial$ acts coefficientwise, so it commutes with the extension.

## Summary of Formulas

| Function | Value | Domain |
|---|---|---|
| $\exp \breve Q$ | $e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-=e^{Q_{\blacktriangle}}(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$ | all $\breve Q$ |
| $\exp(\breve Q_{1}+\breve Q_{2})$ | $\exp \breve Q_{1}\exp \breve Q_{2}$ | all $\breve Q_{1},\breve Q_{2}$, the algebra being commutative |
| $\exp(j\phi)$ | $\cosh\phi+j\sinh\phi$ | $\phi\in\mathbb{R}$ |
| $\exp(i\theta)$ | $\cos\theta+i\sin\theta$ | $\theta\in\mathbb{R}$ |
| $\cos \breve Q,\ \sin \breve Q$ | $\cos Q_{+}\,\Pi_++\cos Q_{-}\,\Pi_-$, $\sin Q_{+}\,\Pi_++\sin Q_{-}\,\Pi_-$ | all $\breve Q$ |
| $\cosh \breve Q,\ \sinh \breve Q$ | $\cosh Q_{+}\,\Pi_++\cosh Q_{-}\,\Pi_-$, $\sinh Q_{+}\,\Pi_++\sinh Q_{-}\,\Pi_-$ | all $\breve Q$ |
| $\log \breve Q$ | $\log Q_{+}\,\Pi_++\log Q_{-}\,\Pi_-$ | the units, branch choice |
| $\breve Q^{s}$ | $Q_{+}^{s}\Pi_++Q_{-}^{s}\Pi_-$ | the units, branch choice |
| $\breve Q_{2}^{n}=\breve Q$ | $n^{2}$ solutions $\eta_{1}Q_{+}^{1/n}\Pi_++\eta_{2}Q_{-}^{1/n}\Pi_-$ | $\breve Q$ a unit |

## Comparison with the Biquaternion Case

The biquaternion algebra $M_{2}(\mathbb{C})$ is simple and non-commutative; its exponential is a matrix exponential, its trigonometric functions are entire but the functional equations fail for non-commuting arguments, and the logarithm requires the matrix logarithm with its own branch structure. The reduced biquaternion algebra replaces the single matrix exponential by the **pair** of complex exponentials of the two idempotent coordinates: the functional equation $\exp(\breve Q+\breve Q_{2})=\exp \breve Q\exp \breve Q_{2}$ holds for all arguments because the algebra is commutative, the trigonometric functions are the two complex trigonometric functions, the logarithm exists exactly on the units and is the pair of complex logarithms, and the power functions have the $n^{2}$ roots of the two coordinates. The split biquaternion case is the same pair structure with the quaternion exponential in each half; the reduced case is the commutative member in which every elementary function is a pair of complex elementary functions.

## Summary

Every elementary function of a reduced biquaternion variable is the pair of the corresponding complex elementary functions of the two idempotent coordinates: the exponential is $\exp \breve Q=e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-=e^{Q_{\blacktriangle}}(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$, with the functional equation holding for all arguments because the algebra is commutative; the element $i$ generates the elliptic rotation, $\exp(i\theta)=\cos\theta+i\sin\theta$, and the element $j$ the hyperbolic one, $\exp(j\phi)=\cosh\phi+j\sinh\phi$, dilating the two halves reciprocally. The trigonometric and hyperbolic functions are the pairs $\cos Q_{+}\Pi_++\cos Q_{-}\Pi_-$ and the like, and the Pythagorean and addition identities hold for all arguments. The logarithm exists exactly on the units, $Q_{+},Q_{-}\neq0$, and is $\log Q_{+}\Pi_++\log Q_{-}\Pi_-$ for a branch choice in each coordinate, the kernel being the lattice $2\pi i(\mathbb{Z}\Pi_++\mathbb{Z}\Pi_-)$. The power $\breve Q^{s}=Q_{+}^{s}\Pi_++Q_{-}^{s}\Pi_-$, and the equation $\breve Q_{2}^{n}=\breve Q$ has $n^{2}$ solutions for a unit, in particular four square roots. On the complex line the functions restrict to the complex ones, on the split complex plane to the split complex ones, and the general principle is that every function defined by a power series or a holomorphic integral extends coefficientwise. Against the biquaternion case, where the matrix exponential and the matrix logarithm carry the non-commutative branch structure, the reduced biquaternion elementary functions are the two commutative complex ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | Element, $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ |
| $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | Idempotent coordinates |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | Idempotents |
| $\exp \breve Q=e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-$ | Exponential |
| $e^{j\phi}=\cosh\phi+j\sinh\phi$ | Hyperbolic exponential |
| $e^{i\theta}=\cos\theta+i\sin\theta$ | Elliptic exponential |
| $\log \breve Q=\log Q_{+}\,\Pi_++\log Q_{-}\,\Pi_-$ | Logarithm on the units |
| $\breve Q^{s}=Q_{+}^{s}\Pi_++Q_{-}^{s}\Pi_-$ | Power function |
| $\eta_{1},\eta_{2}$ | $n$-th roots of unity of the two coordinates |

## Further Reading

- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the exponential, the trigonometric functions and the logarithm of one complex variable.
- Lars V. Ahlfors, *Complex Analysis*, 3rd edition (McGraw-Hill, 1979), for the branch structure of the logarithm and the power functions.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the exponential and the elementary functions of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the idempotent reduction of the elementary functions.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the exponential of the hypercomplex algebras and the comparison with the division-algebra cases.
