
# __Octonion Analysis__

## Introduction

This article is the analysis slot of the octonion system. It sets up the differential calculus of octonion-valued functions of an octonion variable: the Cauchy–Riemann operator and its conjugate, their factorisation of the Laplacian, the class of monogenic functions, the exact form taken by the product rule when the algebra is not associative, and the consequences of that defect for the algebraic structure of the class of monogenic functions.

The article is the octonion member of the analysis slots of this Part, and it follows the model of the analysis of the quaternions and the biquaternions and of the split biquaternions: *Quaternion Analysis* and *Split-Biquaternion Analysis*, with the differential operators and the integration of *Clifford Modules and the Twisted Cauchy–Riemann Operator*. The general theory of hypercomplex analysis in the associative case is that of the Part III companions *Clifford Analysis*, *Clifford Modules and the Twisted Cauchy–Riemann Operator* and *Clifford Analysis in Several Variables*; the present article is the octonion case and states where non-associativity changes the theory rather than restating the general theory. Integration, the special functions and the harmonic analysis are not covered here.

**Conventions.** As throughout the octonion articles, $\mathbb{O}$ has basis $e_0 = 1,e_1,\dots,e_7$ with $e_k^2 = -e_0$ for $k\geq1$, $x = \sum_{k=0}^{7}x_ke_k$ is a variable octonion, $\partial_k = \partial/\partial x_k$, the conjugation is $\bar x$ with $\overline{xy} = \bar y\bar x$, the inner product is $\langle x,y\rangle = \operatorname{Sc}(x\bar y)$, and $\lvert x\rvert^2 = \langle x,x\rangle$ is the norm. The associator is $[x,y,z] = (xy)z - x(yz)$ and the commutator $[x,y] = xy - yx$. Functions are octonion-valued on a domain of $\mathbb{R}^8$ identified with $\mathbb{O}$ by the basis.

## The Cauchy–Riemann Operator

### Definition and Factorisation

**Definition.** The **Cauchy–Riemann operator** of the octonion algebra is

$$
D = \sum_{k=0}^{7}e_k\partial_k = \partial_0 + \sum_{k=1}^{7}e_k\partial_k ,
$$

and its **conjugate** is $\bar D = \partial_0 - \sum_{k=1}^{7}e_k\partial_k$. A function $f$ is **left-monogenic** if $Df = 0$ and **right-monogenic** if $(fD) = \sum_k\partial_kf\,e_k = 0$.

The operator acts on a function by applying the partial derivatives and then multiplying by the basis elements on the left; for a function with values in $\mathbb{O}$ and partial derivatives $\partial_kf$, the product $e_k\partial_kf$ is unambiguous because it is a product of two octonions, so the definition requires no bracketing and is well posed.

**Theorem.** The operator and its conjugate commute and their products are the Laplacian:

$$
D\bar D = \bar DD = \sum_{k=0}^{7}\partial_k^2 = \Delta_8 ,
$$

the Laplacian of $\mathbb{R}^8$ in the coordinates $x_0,\dots,x_7$. Consequently every left-monogenic or right-monogenic function is harmonic, $\Delta_8f = 0$.

*Proof.* Expanding, $D\bar D = \sum_{k,l}e_ke_l\partial_k\partial_l' $ with the sign $\partial_l' = \partial_l$ for $l = 0$ and $\partial_l' = -\partial_l$ otherwise; the partial derivatives commute, so the mixed terms combine as $\sum_{k<l}(e_ke_l + e_le_k)\partial_k\partial_l$ up to the sign of the conjugate, and the Clifford relations $e_ke_l + e_le_k = -2\delta_{kl}$ for $k,l\geq1$ together with $e_0e_0 = e_0$ give $\sum_k\partial_k^2$. Only products of two basis elements occur, so no associativity is needed. For the harmonicity, $\Delta_8f = \bar D(Df) = 0$ when $Df = 0$. $\square$

The factorisation is the same as in the quaternion and biquaternion cases, and it shows that the elliptic character of the octonionic Cauchy–Riemann operator is not affected by the failure of associativity: the operator is a first-order elliptic operator with the Laplace operator as its square.

### The Fundamental Solution

**Definition.** The **fundamental solution** of $D$ is the function

$$
E(x) = \frac{1}{\omega_7}\frac{\bar x}{\lvert x\rvert^8}, \qquad x\neq0,
$$

where $\omega_7 = \operatorname{vol}(S^7) = \pi^4/3$ is the volume of the unit sphere.

**Theorem.** The function $E$ is left-monogenic and right-monogenic on $\mathbb{R}^8\setminus\{0\}$, homogeneous of degree $1 - 8 = -7$, and it is the fundamental solution of $D$: in the sense of distributions,

$$
DE = E D = \delta_0 ,
$$

and $\Delta_8E = 0$ away from the origin.

*Proof.* Away from the origin, $D(\bar x/\lvert x\rvert^8) = 0$ and $(\bar x/\lvert x\rvert^8)D = 0$, by the same computation as in the associative Clifford case: $\bar x$ is the product of seven-tuples of basis elements... the identity is the one used to prove that $\bar x/\lvert x\rvert^n$ is the kernel of the Cauchy–Riemann operator in $\mathbb{R}^n$, and the computation uses the Clifford relations and the identity $\sum_kx_ke_k = x$, $\sum_k e_kx_k = \bar x$ for monomials; it requires no associativity because only products of two basis elements are formed at each step. The constant $\omega_7$ is chosen so that $\int_{\lvert x\rvert = 1}\bar x\,dS/n = 1$ in the distributional sense; the constant is the volume of the unit sphere, computed as $\pi^4/3$ in *Octonion Norm and Invertibility*. $\square$

The kernel reproduces the quaternionic situation, where the analogous function is $\bar x/\lvert x\rvert^4$, and it is the kernel out of which the Cauchy formula of the next section is built. What differs is not the kernel but the class of functions.

## Monogenic Functions

### Definition and Elementary Properties

**Definition.** Let $\Omega\subset\mathbb{O}$ be a domain, that is a connected open set. The space of **left-monogenic** functions on $\Omega$ is

$$
\mathcal{M}_L(\Omega) = \left\{f : \Omega\to\mathbb{O} \text{ of class } C^1 : Df = 0\right\},
$$

and the space of **right-monogenic** functions $\mathcal{M}_R(\Omega)$ is defined by $fD = 0$; a function that is both is **two-sided monogenic**.

**Proposition.** On a domain $\Omega$ the following hold.

1. The spaces $\mathcal{M}_L(\Omega)$ and $\mathcal{M}_R(\Omega)$ are real vector spaces of harmonic functions and are infinite-dimensional; the constants are monogenic, while the coordinate function $x\mapsto x$ is not, since $Dx = \sum_{k=0}^{7}e_k^2 = -6e_0$, and $x\mapsto\bar x$ is not either, since $D\bar x = 8e_0$.
2. The **radial reduction**: for functions of the form $f = u(r) + v(r)\bar x$ with $r = \lvert x\rvert$,

$$
Df = \frac{u'}{r}\,x + \left(8v + rv'\right),
$$

so that $f$ is left-monogenic if and only if $u$ is constant and $v = c\lvert x\rvert^{-8}$. The fundamental solution $E$ is the case $u = 0$, $v = \lvert x\rvert^{-8}/\omega_7$.
3. The same computation for $g = u(r) + v(r)x$ gives $Dg = \frac{u'}{r}x + \frac{v'}{r}x^2 + v\sum_{k=0}^{7}e_k^2$, and since $x^2 = 2x_0x - \lvert x\rvert^2e_0$ is not a scalar for general $x$, no nonconstant radial function of this ansatz is monogenic; only the $\bar x$ ansatz produces radial solutions.

*Proof.* (1) The constants are annihilated by $D$, and $Dx$ and $D\bar x$ are the displayed computations, using $e_0^2 = e_0$ and $e_k^2 = -e_0$ for $k\geq1$. (2) Differentiating, $\partial_kf = u'x_k/r + v'x_k\bar x/r + v\bar e_k$, so

$$
Df = \frac{u'}{r}\sum_ke_kx_k + \frac{v'}{r}\sum_kx_k(e_k\bar x) + v\sum_ke_k\bar e_k = \frac{u'}{r}x + \frac{v'}{r}x\bar x + 8v ,
$$

because $\sum_ke_kx_k = x$ for scalar coefficients $x_k$, because the associator with a scalar vanishes, and because $\sum_ke_k\bar e_k = e_0 - \sum_{k\geq1}e_k^2 = 8e_0$. Since $x\bar x = \lvert x\rvert^2 = r^2$, the display follows. (3) The second ansatz gives $\sum_ke_k(x_kx) = x^2$ in place of $x\bar x$, and $x^2$ is scalar only when $x$ lies in a one-dimensional subspace, so no nonconstant radial solution arises. $\square$

The radial reduction is worth isolating, since it is the source of the explicit examples and it shows how sharply the non-commutativity and non-associativity constrain them: the order of the factors in the ansatz matters, because $x\bar x$ is a scalar while $xx$ is not, and the associator-free step $\sum_ke_k(x_k\bar x) = x\bar x$ is the one that makes the kernel monogenic.

### The Failure of the Leibniz Rule

**Theorem (product rule).** For $C^1$ functions $f,g$ on $\Omega$,

$$
D(fg) = (Df)g + f(Dg) - \sum_{k=0}^{7}[e_k,\partial_kf,g] + \sum_{k=0}^{7}\Bigl([e_k,f]\partial_kg - 2[e_k,f,\partial_kg]\Bigr),
$$

and the two correction sums vanish identically for all $f,g$ if and only if the multiplication is associative. In particular for a constant $a\in\mathbb{O}$,

$$
D(af) = a(Df) + \sum_{k=0}^{7}[e_k,a,\partial_kf] ,
$$

so that the left multiplication of a monogenic function by a constant is monogenic only in special cases.

*Proof.* The product rule of the ordinary differential calculus gives $\partial_k(fg) = (\partial_kf)g + f(\partial_kg)$, and therefore

$$
D(fg) = \sum_k e_k(\partial_kf)g + \sum_k e_k(f\partial_kg) .
$$

The first sum is $\sum_k(e_k\partial_kf)g + \sum_k\bigl(e_k((\partial_kf)g) - (e_k\partial_kf)g\bigr) = (Df)g - \sum_k[e_k,\partial_kf,g]$. For the second sum, $f(Dg) = \sum_kf(e_k\partial_kg)$, and the difference term by term is $e_k(f\partial_kg) - f(e_k\partial_kg) = [e_k,f]\partial_kg - 2[e_k,f,\partial_kg]$, using the alternation of the associator; adding gives the display. The correction vanishes for all triples exactly when all associators vanish, that is exactly when the algebra is associative. The special case follows by putting $\partial_ka = 0$ and using $Da = 0$ for constant $a$. $\square$

The theorem is the precise form of the statement that the octonionic differential calculus is not associative: the Leibniz rule acquires two correction terms built from the commutator and the associator, and they are not a defect of a particular presentation but an invariant of the algebra, since they vanish for all arguments only in the associative case. The consequence is immediate and severe:

**Corollary.** The product of two left-monogenic functions need not be left-monogenic, and the space $\mathcal{M}_L(\Omega)$ is **not** a left module over $\mathbb{O}$ with respect to pointwise multiplication; indeed $D(af) = \sum_k[e_k,a,\partial_kf]$ for $a$ constant and $f$ monogenic, and this is nonzero for suitable $a,f$.

*Proof.* By the product rule with $Df = Dg = 0$ the first two terms vanish, and the correction terms remain; they do not vanish identically by the alternation properties of the associator, and an explicit example is obtained from $f = E$ and $a = e_1$: the function $e_1E$ is not monogenic, because $D(e_1E) = \sum_k[e_k,e_1,\partial_kE]$ and the associators $\partial_kE$ do not all commute with $e_1$. $\square$

This is the sharpest structural difference from the associative case: in Clifford analysis the monogenic functions form a module over the coefficient algebra, because the Cauchy–Riemann operator is a derivation with respect to the associative product, and in octonionic analysis they do not.

### Left and Right Monogenic Functions

**Proposition.** For a $C^1$ function $f$ the two operators are related by conjugation,

$$
\overline{Df} = \bar fD, \qquad \overline{fD} = \bar D\bar f ,
$$

so that $f$ is left-monogenic if and only if $\bar f$ is right-monogenic. Consequently

$$
\mathcal{M}_R(\Omega) = \left\{\bar f : f\in\mathcal{M}_L(\Omega)\right\},
$$

and the two classes are conjugate to one another.

*Proof.* Conjugating $Df = \sum_ke_k\partial_kf$ and using $\overline{\partial_kf} = \partial_k\bar f$ for real coordinates, $\bar e_0 = e_0$ and $\bar e_k = -e_k$ for $k\geq1$, one obtains $\overline{Df} = \sum_k\partial_k\bar f\,\bar e_k = \partial_0\bar f - \sum_{k\geq1}\partial_k\bar f\,e_k = \bar fD$, which is the first identity; the second follows by applying the involution again, since it is an anti-automorphism of order two and carries $0$ to $0$. $\square$

Since the algebra is neither commutative nor associative, the classes are not the same in general: a left-monogenic function need not be right-monogenic, and the two-sided monogenic functions are the intersection, which is closed under neither pointwise product in general. In the complex case the two classes coincide; in the quaternion and biquaternion cases they are distinct but related by conjugation, exactly as here.

## The Cauchy Integral Formula

**Theorem (Cauchy–Pompeiu).** Let $\Omega\subset\mathbb{O}$ be a bounded domain with smooth boundary $\partial\Omega$ oriented as the boundary of $\Omega$, let $n(y) = \sum_ky_ke_k$ be the outward unit normal at $y\in\partial\Omega$ in the identification of $\mathbb{R}^8$ with $\mathbb{O}$, and let $dS$ be the surface measure. Then for every $f\in C^1(\bar\Omega)$ and every $x\in\Omega$,

$$
f(x) = \frac{1}{\omega_7}\int_{\partial\Omega}\frac{\overline{y - x}}{\lvert y - x\rvert^8}\,n(y)\,f(y)\,dS(y) - \frac{1}{\omega_7}\int_{\Omega}\frac{\overline{y - x}}{\lvert y - x\rvert^8}\,(Df)(y)\,dV(y).
$$

If $f$ is left-monogenic in $\Omega$, the second term vanishes and the **Cauchy integral formula** results:

$$
f(x) = \frac{1}{\omega_7}\int_{\partial\Omega}\frac{\overline{y - x}}{\lvert y - x\rvert^8}\,n(y)\,f(y)\,dS(y), \qquad x\in\Omega .
$$

*Proof.* The formula is the standard Cauchy–Pompeiu formula for the octonionic Cauchy–Riemann operator: it follows from Stokes' theorem for the form $E(y-x)n(y)f(y)dS$, whose exterior derivative is computed with the product rule, and the resulting volume integrand is $E(y-x)(Df)(y)$ up to the correction terms, which are total derivatives and integrate to zero. The reader is referred to the sources cited for the details of the Stokes argument in the non-associative case. The passage to the monogenic case is the vanishing of the volume term. $\square$

Two features of the formula are worth recording. First, the order of the factors is part of the statement: the kernel multiplies the normal on the left and the function on the left of that, and a right-monogenic version of the formula requires the conjugate arrangement of the factors given by the conjugacy of the two classes. Second, the formula holds although the algebra is not associative; its proof uses the Clifford relations and Stokes' theorem and does not require the product of two monogenic functions to be monogenic, which is why it survives the failure of the Leibniz rule recorded above.

**Corollary (mean value).** For a left-monogenic function on a ball of radius $r$ centred at the origin,

$$
f(0) = \frac{1}{\omega_7r^7}\int_{\lvert y\rvert = r}f(y)\,dS(y),
$$

the integral being over the sphere of radius $r$, whose volume is $\omega_7r^7$; hence $f(0)$ is the mean value of $f$ over the sphere, and a non-constant monogenic function has no interior maximum of the modulus, so that the maximum principle holds.

*Proof.* In the Cauchy formula on the ball, the kernel and the normal are $\bar y/r^8$ and $n(y) = y/r$, and $\bar yy = r^2$, so the integrand reduces to $f(y)/r^9 \cdot r^2 = f(y)/r^7$ up to the constant; dividing by $\omega_7$ gives the mean value. Harmonicity gives the maximum principle. $\square$

## Comparison with the Associative Clifford Case

The octonionic Cauchy–Riemann operator is a first-order elliptic operator whose square is the Laplacian, and in this it is an operator of the family that the companion article *Dirac Operators*, written in parallel, treats as mathematics under the classical name. The comparison with the associative Clifford case isolates exactly what the failure of associativity costs, and what it does not.

**Theorem.** Let $A$ be a real associative algebra with a positive definite inner product and an orthonormal basis $f_1,\dots,f_m$ satisfying the Clifford relations, and let $\mathcal{D} = \sum_kf_k\partial_k$ on $A$-valued functions of $m$ variables. Then the left-monogenic functions form a left $A$-module, and for constant $a$ one has $\mathcal{D}(af) = a(\mathcal{D}f)$; the product of two monogenic functions need not be monogenic in this case either.

*Proof.* The first statement is the Leibniz rule of the associative case, which has no correction terms; the second is the observation that $\mathcal{D}(fg) = (\mathcal{D}f)g + \sum_kf_k(f\partial_kg)$, whose second term is a first-order operator applied to $g$ and is not zero for arbitrary monogenic $f,g$. $\square$

The comparison is therefore precise and asymmetric. The failure of the product of two monogenic functions to be monogenic is **not** a feature of the octonions: it holds already for the associative Clifford algebras. What is peculiar to the octonions is the failure of the **module** property, $D(af)\neq a(Df)$ for constant $a\in\mathbb{O}$, which in the associative case is a triviality and in the octonionic case is a sum of associators; and with it the failure of every structure that presupposes that the solutions are acted on by the coefficient algebra. This is why the octonionic analysis retains the elliptic, harmonic and integral theory — those never multiply two solutions — and loses the module-theoretic theory.

**Remark.** The obstruction has a single algebraic carrier: the associator, which is alternating and vanishes on any two generators, by Artin's theorem. Consequently every statement in the octonionic analysis whose proof would form a product of three elements coming from two distinct subalgebras is suspect, while every statement whose proof uses only one generator, or only two variable elements, stands. The Leibniz defect is the form of the obstruction in one line, and the module failure the form of the obstruction in one sentence.

## Summary

The octonionic Cauchy–Riemann operator $D = \sum_{k=0}^{7}e_k\partial_k$, with conjugate $\bar D = \partial_0 - \sum_{k\geq1}e_k\partial_k$, is a first-order elliptic operator satisfying $D\bar D = \bar DD = \Delta_8$, so that every left- or right-monogenic function is harmonic. Its fundamental solution is $E(x) = \bar x/(\omega_7\lvert x\rvert^8)$ with $\omega_7 = \pi^4/3$, homogeneous of degree $-7$, and the Cauchy–Pompeiu formula expresses a $C^1$ function on a domain by an integral over the boundary with the kernel $\overline{y-x}/\lvert y-x\rvert^8$ multiplied on the left by the outward normal, together with a volume term involving $Df$; for left-monogenic functions only the boundary term remains, and the maximum principle follows.

Non-associativity enters the analysis at exactly one place, the product rule, and it changes the theory there. The Leibniz rule acquires the correction terms

$$
D(fg) = (Df)g + f(Dg) - \sum_k[e_k,\partial_kf,g] + \sum_k\Bigl([e_k,f]\partial_kg - 2[e_k,f,\partial_kg]\Bigr),
$$

which vanish identically only when the algebra is associative. Consequences: the product of two monogenic functions need not be monogenic; the monogenic functions do not form a module over the octonions, since $D(af) = \sum_k[e_k,a,\partial_kf]$ for constant $a$; and the left- and right-monogenic classes are conjugate to each other but distinct. The factorisation of the Laplacian, the kernel and the integral formula are unaffected, because they involve only products of two basis elements, and the elliptic and harmonic theory carries over to the octonions unchanged.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{O}$, $e_0,\dots,e_7$ | Octonion algebra and basis, $e_k^2 = -e_0$ for $k\geq1$ |
| $x = \sum_kx_ke_k$, $\partial_k = \partial/\partial x_k$ | Octonion variable and partial derivatives |
| $D = \sum_{k=0}^{7}e_k\partial_k$ | Cauchy–Riemann operator |
| $\bar D = \partial_0 - \sum_{k\geq1}e_k\partial_k$ | Conjugate operator, $D\bar D = \bar DD = \Delta_8$ |
| $[x,y,z] = (xy)z - x(yz)$, $[x,y] = xy - yx$ | Associator and commutator |
| $\mathcal{M}_L(\Omega)$, $\mathcal{M}_R(\Omega)$ | Left- and right-monogenic functions, $Df = 0$, $fD = 0$ |
| $E(x) = \bar x/(\omega_7\lvert x\rvert^8)$ | Fundamental solution, $DE = ED = \delta_0$ |
| $\omega_7 = \pi^4/3$ | Volume of the unit sphere $S^7$ |
| $n(y)$, $dS$, $dV$ | Outward unit normal, surface measure, volume measure |
| $\Delta_8$ | Laplacian of $\mathbb{R}^8$ |





## Further Reading

- F. Brackx, Richard Delanghe and Frank Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy–Riemann operator, monogenic functions and the Cauchy–Pompeiu formula in the associative case.
- Richard Delanghe, "On regular analytic functions with values in a Clifford algebra", *Mathematische Annalen* **185** (1970), 91–111, for the module structure of the monogenic functions in the associative case, against which the octonionic failure is measured.
- John Ryan, "Complex Clifford analysis and domains of holomorphy", *Journal of the Australian Mathematical Society* **48** (1990), 264–288, for the Cauchy integral formula and its octonionic analogues.
- Rolf Sören Krausshar, *Generalized Analytic Automorphic Forms in Hypercomplex Spaces* (Birkhäuser, 2004), for the octonionic Cauchy–Riemann operator and the failure of the Leibniz rule.
- Guochang Li, *The Cauchy–Riemann Operator in Octonionic Analysis* (Harbin Institute of Technology Press, 2005), for the product rule with the associator corrections and the structure of the monogenic classes.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the operator factorisation, the fundamental solutions and the radial reductions used above.
