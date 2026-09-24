
# __Hypercomplex Analysis__

## Introduction

Complex analysis is the study of functions of one complex variable that are differentiable in the complex sense, and the Cauchy–Riemann equations are the explicit form of that differentiability. Hypercomplex analysis is the attempt to run the same programme over an algebra larger than $\mathbb{C}$. It has a general shape, and that shape is the subject of this article: the choice of a first-order differential operator, the class of functions it annihilates, and the theorems those functions obey. Particular systems — the quaternions, the split complex numbers, the dual numbers, the biquaternions and their relatives — are treated in categories 26 to 29, and this article deliberately keeps to the common method.

The point of departure is that the naive generalisation fails. Over a commutative field $\mathbb{K}$ the differentiable functions of a $\mathbb{K}$-variable are the holomorphic functions, and there are many of them. Over a non-commutative algebra, requiring the differential to be linear over the algebra forces the function to be affine; the class is far too small to support a theory. The remedy, standard in the subject, is to fix a first-order operator built from the algebra and to study the functions that operator annihilates. This is the general method, and every particular hypercomplex theory is an instance of it.

Throughout, $A$ is a finite-dimensional unital associative algebra over $\mathbb{R}$, of dimension $m$, with a fixed basis $e_0 = 1, e_1, \dots, e_{m-1}$. The underlying real vector space is identified with $\mathbb{R}^m$ and carries the Euclidean topology, which by *Topological Algebras and Banach Algebras* is the unique topology making $A$ a topological algebra. Thus $A$ is a real Banach algebra, open subsets of $A$ are open subsets of $\mathbb{R}^m$, and differentiability is Fréchet differentiability. The theory is over $\mathbb{R}$; the complex case is the case $A = \mathbb{C}$.

## The Failure of Algebra-Differentiability

**Definition.** Let $\Omega \subseteq A$ be open and let $f : \Omega \to A$. Then $f$ is **left $A$-differentiable** at $x \in \Omega$ if there exists $f'(x) \in A$ with

$$
f(x + h) = f(x) + f'(x)\,h + o(\|h\|) \qquad (h \to 0),
$$

and **right $A$-differentiable** at $x$ if the same holds with $h\,f'(x)$ in place of $f'(x)h$. The function is left (respectively right) $A$-differentiable on $\Omega$ if it is so at every point.

For a commutative $A$ the two notions agree, and for $A = \mathbb{C}$ they are the usual complex differentiability; the class of such functions is the class of holomorphic functions, which is as large as complex analysis requires. In the non-commutative case the class collapses.

**Theorem (rigidity over $\mathbb{H}$).** Let $\Omega \subseteq \mathbb{H}$ be a domain. A $C^1$ function $f : \Omega \to \mathbb{H}$ that is left $\mathbb{H}$-differentiable at every point of $\Omega$ is of the form

$$
f(x) = ax + b, \qquad a, b \in \mathbb{H}.
$$

*Proof.* Writing the differential as left multiplication by $f'(x)$ and comparing with the Fréchet derivative of $f$ expressed in the four real coordinates, one obtains the quaternionic Cauchy–Riemann equations; these force every second partial derivative of every component to vanish. Hence each component is affine in the coordinates, and the multiplicative constraint then forces the matrix of the linear part to be left multiplication by a quaternion and the constant part to be an arbitrary quaternion. $\square$

**Corollary.** Over $\mathbb{H}$ the requirement that the differential be left multiplication by an element of $A$ is too strong: the only such functions on a domain are the affine ones. The same collapse occurs over each real algebra for which the rigidity theorem holds. A theory rich enough to be useful must therefore weaken the differentiability requirement, and the weakening adopted in the subject is to require the vanishing of a fixed first-order operator.

**Remark (the ambiguity of the difference quotient).** The definition above is the difference-quotient definition written without a quotient. Classically one writes

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h},
$$

and this expression requires $h$ to be invertible in order to be formed at all. In a finite-dimensional real algebra the invertible elements form an open set, but that set is not all of $A\setminus\{0\}$ unless $A$ is a division algebra: for the split complex numbers the zero divisors are the real multiples of $1 \pm j$, for the dual numbers they are the multiples of $\varepsilon$. The limit is therefore taken over a set of directions with a hole in it, and the value of the limit may depend on the side from which the invertible elements are approached; this is the origin of the distinction between left and right $A$-differentiability, and it is why the difference quotient is not the right primitive notion over a general algebra.

**Remark (over-determination).** The condition that the differential be a multiplication is a strong linear constraint, and it is worth counting. The Fréchet derivative $df(x)$ is an arbitrary $\mathbb{R}$-linear map $A \to A$, and these form a space of dimension $m^2$; the left multiplications by elements of $A$ form the subspace $L_A$ of dimension $m$, isomorphic to $A$ itself. Requiring $df(x) \in L_A$ therefore imposes $m^2 - m$ independent linear conditions on the $m^2$ entries of the differential at each point. For $m = 2$ the two conditions are the Cauchy–Riemann equations, and the resulting class of functions is large; for $m = 4$ over $\mathbb{H}$ the twelve conditions admit only the affine solutions. The count $m^2 - m$ is thus the quantitative expression of the over-determination of the difference-quotient derivative, and it shows that the failure is a matter of the algebra and not merely of the dimension: a commutative algebra of large dimension, such as $\mathbb{C} \times \mathbb{C}$, still admits a rich class of $A$-differentiable functions, because its multiplications are simultaneously diagonalisable.

## Holomorphy in a Commutative Subalgebra

The first of the two notions that survive over an algebra is a restriction of the classical one: one chooses a commutative subalgebra and asks for differentiability there.

**Definition.** Let $C \subseteq A$ be a commutative subalgebra containing $1_A$, and let $\Omega \subseteq C$ be relatively open. A function $f : \Omega \to A$ is **$C$-holomorphic** on $\Omega$ if it is $C$-differentiable there, that is, if for each $x \in \Omega$ there is $f'(x) \in A$ with

$$
f(x + h) = f(x) + f'(x)\,h + o(\|h\|) \qquad (h \in C, \ h \to 0).
$$

Since $C$ is commutative, no distinction between the left and the right version arises inside $C$; the values of $f$ still lie in the possibly non-commutative algebra $A$, and it is only the variable that is restricted.

**Proposition (power series).** Let $f(x) = \sum_{n \geq 0} a_n (x - x_0)^n$ with $a_n \in A$, convergent on a $C$-ball $B_C(x_0, r) = \{x \in C : \|x - x_0\| < r\}$. Then $f$ is $C$-holomorphic on that ball, with

$$
f'(x) = \sum_{n \geq 1} n\,a_n (x - x_0)^{n-1}.
$$

*Proof.* Since $C$ is commutative, $(x_0 + h)^n - x_0^n = n x_0^{n-1}h + O(\|h\|^2)$ for $h \in C$, by the binomial theorem, and the terms of order $\geq 2$ contribute $O(\|h\|^2)$ in the norm by submultiplicativity. Uniform convergence on closed subballs of the differentiated series gives termwise differentiation, so the displayed series is the derivative. $\square$

**Example ($A = \mathbb{H}$, $C = \mathbb{R}[u] \cong \mathbb{C}$).** Let $u \in \mathbb{H}$ satisfy $u^2 = -1$, so that $C = \mathbb{R}[u]$ is isomorphic to $\mathbb{C}$; for instance $C = \mathbb{R}[e_1]$. Then the $C$-holomorphic functions with values in $\mathbb{H}$ are exactly the holomorphic functions of the complex variable $x \in C$ with coefficients in $\mathbb{H}$, they satisfy the Cauchy–Riemann equations in the two coordinates of $C$, they obey the classical Cauchy theorem for $\mathbb{H}$-valued integrals along curves in $C$, and they form a class as large as the holomorphic functions with values in $\mathbb{H} \otimes_\mathbb{R} \mathbb{C} \cong \mathbb{B} \cong M_2(\mathbb{C})$ (*Biquaternion Algebra ($\mathbb{B}$)*). This is the sense in which complex analysis survives verbatim inside a non-commutative algebra.

**Remark (the two notions are independent).** $C$-holomorphy and regularity with respect to a first-order operator are different conditions, and neither implies the other. The function $f(x) = x$ is both; the function $f(x) = x^2$ is $C$-holomorphic but is not left $\mathbb{H}$-regular for the operator $D = \partial_0 + e_1\partial_1 + e_2\partial_2 + e_3\partial_3$ of the next section, since $D(x^2) = -4x_0 \neq 0$; and the function $f(q) = q_1 - e_1q_0$ is left regular without being $C$-holomorphic on most commutative subalgebras: on $C = \mathbb{R}[u]$ it equals $x \mapsto u_1x_1 - e_1x_0$ for $x = x_0 + ux_1$, which is left multiplication by a single element — and so is $C$-holomorphic — only when $u = \pm e_1$, where it reduces to the linear function $-e_1x$. The classical link between the two is Fueter's construction, which promotes a holomorphic function of a complex variable to a monogenic function of a quaternion variable by a radially symmetric substitution; it is a theorem of the quaternion theory and is treated.

## Generalised Cauchy–Riemann Operators

**Definition.** A **generalised Cauchy–Riemann operator** on $A$ is a first-order linear differential operator with constant coefficients

$$
D = \sum_{\alpha=0}^{m-1} B_\alpha \,\partial_\alpha, \qquad B_\alpha \in A,
$$

where $\partial_\alpha = \partial/\partial x_\alpha$ and $x = \sum_\alpha x_\alpha e_\alpha$ are the coordinates of $x \in A$. Its **conjugate** is a second operator of the same shape,

$$
\bar D = \sum_{\alpha=0}^{m-1} \bar B_\alpha \,\partial_\alpha, \qquad \bar B_\alpha \in A.
$$

The operator $D$ acts on a differentiable function $f : \Omega \to A$ by

$$
D f = \sum_{\alpha=0}^{m-1} B_\alpha \,\partial_\alpha f,
$$

the product being the product of $A$, and $(D f)(x)$ is computed pointwise at $x$.

**Example (the complex numbers).** For $A = \mathbb{C}$ with basis $e_0 = 1$, $e_1 = i$, the operator

$$
D = \partial_0 + i\,\partial_1
$$

annihilates $f = u + iv$ exactly when $u_x = v_y$ and $u_y = -v_x$, the Cauchy–Riemann equations; thus regular functions in the sense below are the holomorphic functions. Its conjugate is $\bar D = \partial_0 - i\partial_1$, and $D\bar D = \bar D D = \Delta$.

**Example (the quaternions).** For $A = \mathbb{H}$ with basis $1, e_1, e_2, e_3$,

$$
D = \partial_0 + e_1 \partial_1 + e_2 \partial_2 + e_3 \partial_3, \qquad \bar D = \partial_0 - e_1 \partial_1 - e_2 \partial_2 - e_3 \partial_3,
$$

and $D\bar D = \bar D D = \Delta$, because $e_k^2 = -1$ and $e_j e_k + e_k e_j = 0$ for $j \neq k$. This operator is the Cauchy–Riemann operator of quaternion analysis.

**Example (general coefficients).** The structural condition that makes the theory work is the following.

**Proposition (factorisation of the Laplacian).** Let $D = \partial_0 + \sum_{k \geq 1} B_k \partial_k$ and let its conjugate be $\bar D = \partial_0 - \sum_{k \geq 1} B_k \partial_k$, so that $\bar B_0 = 1$ and $\bar B_k = -B_k$. Suppose the coefficients satisfy the **Clifford relations**

$$
B_j B_k + B_k B_j = -2\delta_{jk}\,1, \qquad j, k \geq 1.
$$

Then

$$
D \bar D = \bar D D = \Delta \cdot 1,
$$

where $\Delta = \sum_{\alpha} \partial_\alpha^2$ is the Laplacian of $\mathbb{R}^m$.

*Proof.* Expand

$$
D\bar D = \Bigl(\partial_0 + \sum_k B_k \partial_k\Bigr)\Bigl(\partial_0 - \sum_j B_j \partial_j\Bigr) = \partial_0^2 - \sum_{j,k} B_j B_k \,\partial_j \partial_k,
$$

the mixed terms in $\partial_0$ cancelling. Splitting the double sum into the diagonal and the off-diagonal parts,

$$
-\sum_{j,k} B_jB_k \partial_j\partial_k = -\sum_k B_k^2 \partial_k^2 - \sum_{j \neq k} B_jB_k \partial_j\partial_k,
$$

and since $B_k^2 = -1$ the first term is $+\sum_k \partial_k^2$, while the second cancels pairwise because $B_jB_k = -B_kB_j$. The computation for $\bar D D$ is identical. $\square$

The relations $B_j B_k + B_k B_j = -2\delta_{jk}$ are exactly the defining relations of a Clifford algebra, so the factorisation of the Laplacian requires the coefficients of $D$ to generate a Clifford subalgebra of $A$. This is the structural input that hypercomplex analysis needs: a general finite-dimensional algebra need not contain one, and the systems of categories 26 to 29 are those built from Clifford algebras and their relatives.

**Definition.** A **hypercomplex system** is a pair $(A, D)$ consisting of a finite-dimensional unital associative real algebra $A$ and a generalised Cauchy–Riemann operator $D$ on it. The system is **elliptic** if the coefficients have the factorisation property of the proposition, and $D$ is then an elliptic operator with injective symbol.

The word **hypercomplex** refers to the system, not to a particular algebra; a single algebra $A$ carries many admissible operators $D$, and the associated analyses differ.

## Regular Functions

**Definition.** Let $(A, D)$ be a hypercomplex system, $\Omega \subseteq A$ open, and $f : \Omega \to A$ of class $C^1$. Then $f$ is **left regular** (or **left monogenic**) on $\Omega$ if

$$
D f = 0 \quad \text{on } \Omega.
$$

It is **right regular** if $f D = 0$, where the operator acts on the right, $fD = \sum_\alpha \partial_\alpha f \,\bar B_\alpha$. The two notions coincide when $A$ is commutative.

**Example.** For $A = \mathbb{C}$ and $D = \partial_0 + i\partial_1$, the left regular functions are the holomorphic functions; for $A = \mathbb{H}$ and the operator above, they are the monogenic functions of quaternion analysis. Both are instances of one definition.

**Proposition (linear structure).** The left regular functions on $\Omega$ form a real vector space. If $f$ is left regular and $a \in A$, then:

1. $fa$ is left regular;
2. $af$ is left regular whenever $a$ commutes with every coefficient $B_\alpha$ of $D$, in particular whenever $a$ is central in $A$.

*Proof.* Linearity of $D$ gives the vector space statement. For a constant $a$, the Leibniz rule collapses to $\partial_\alpha(fa) = (\partial_\alpha f)a$ and $\partial_\alpha(af) = a\,\partial_\alpha f$, so

$$
D(fa) = \sum_\alpha B_\alpha (\partial_\alpha f) a = (Df)a = 0, \qquad D(af) = \sum_\alpha B_\alpha a\,\partial_\alpha f = a \sum_\alpha B_\alpha \partial_\alpha f = a\,Df = 0
$$

in the second line when $B_\alpha a = a B_\alpha$ for every $\alpha$. $\square$

**Proposition (Leibniz rule; failure of closure under products).** For $C^1$ functions $f, g$ on $\Omega$,

$$
D(fg) = \sum_{\alpha} B_\alpha \,\partial_\alpha(fg) = (Df)\,g + \sum_{\alpha} B_\alpha\, f\, (\partial_\alpha g),
$$

since the pointwise product is a derivation in each variable. If the coefficients $B_\alpha$ are central, the second term is $f\,(Dg)$, so the product of two left regular functions is again left regular. If the coefficients are not central, $D(fg)$ need not vanish for left regular $f$ and $g$, and the left regular functions do not form an algebra.

*Proof.* The derivative of a product of $A$-valued functions is the sum of the two one-sided products, $\partial_\alpha(fg) = (\partial_\alpha f)g + f(\partial_\alpha g)$, and $D$ is $A$-linear in the values. The first term is $(Df)g$ because $g$ does not depend on the summation index $\alpha$. For central coefficients, $\sum_\alpha B_\alpha f (\partial_\alpha g) = f \sum_\alpha B_\alpha \partial_\alpha g = f\,Dg$. $\square$

## The Obstructions

Four features of the algebra obstruct the programme, and they are logically independent of one another.

**Non-commutativity.** The pointwise product of $A$-valued functions is not commutative, so the operators of left and right multiplication differ; the equation $Df = 0$ and the equation $fD = 0$ define different classes (§Regular Functions), the product of two left regular functions is left regular only when the coefficients of $D$ are central, and the quotient rule is available only where the denominator is a unit. The Leibniz rule itself survives unchanged, because it is a statement about a derivation in each factor.

**Zero divisors.** The difference quotient requires a division by $h$, and $h$ is a zero divisor on a set of positive codimension whenever $A$ is not a division algebra. The split complex numbers, the dual numbers and the biquaternions all have zero divisors, and in each of them a nonzero element can have no inverse. Consequently the inverse function theorem holds only at points where the derivative is a unit, the quotient rule only where the denominator is a unit, and the algebraic manipulations of complex analysis that divide by a value of a function require a hypothesis in place of the classical one.

**The one-sided module structure.** The space of $A$-valued functions on $\Omega$ is a module over $A$ for multiplication of the values by a constant, but $D(af) = a\,Df$ requires $a$ to commute with the coefficients $B_\alpha$; the space of regular functions is therefore a module over the centre of $A$, and not over $A$ itself. Together with non-commutativity this produces the left and the right theory, and the two are exchanged by an anti-automorphism rather than identified.

**The dimension.** The symbol $\sigma(\xi) = \xi_0 + \sum_{k\geq1}B_k\xi_k$ must be invertible for every real $\xi \neq 0$ if the operator is to be elliptic, and the factorisation $D\bar D = \Delta$ requires the Clifford relations. Over a degenerate algebra this fails, and with it the whole elliptic apparatus: the characteristic variety meets the real space, the plane waves are real exponentials rather than oscillatory, and the components of a regular function satisfy a wave or transport equation in place of Laplace's equation.

**Proposition (elliptic and degenerate systems).** Let $A$ have dimension $m$ and let $D = \partial_0 + \sum_{k\geq1}B_k\partial_k$ with $B_k^2 = -1$ and $B_jB_k = -B_kB_j$ for $j \neq k$. Then the symbol satisfies $\sigma(\xi)\tilde\sigma(\xi) = |\xi|^2\cdot 1$ and $D$ is elliptic. By contrast:

- for $\mathbb{D}$ with $D = \partial_0 + j\partial_1$, the product $\sigma(\xi)\tilde\sigma(\xi) = \xi_0^2 - \xi_1^2$ vanishes on the two real lines $\xi_0 = \pm\xi_1$;
- for $\mathbb{D}'$ with $D = \partial_0 + \varepsilon\partial_1$, the same product is $\xi_0^2$ and vanishes on the hyperplane $\xi_0 = 0$.

In both degenerate cases $D$ is not elliptic, the characteristic variety meets the real space, and the theory of §Consequences of Ellipticity is not available.

**Example (the degenerate systems solved explicitly).** For $\mathbb{D}$, write a function in the idempotent decomposition $f = f_+e_+ + f_-e_-$ and use the characteristic coordinates $\xi_\pm = x_0 \pm x_1$, so that $\partial_0 = \partial_+ + \partial_-$ and $\partial_1 = \partial_+ - \partial_-$ and therefore $e_+\partial_+ + e_-\partial_- = \tfrac12(\partial_0 + j\partial_1)$. Then

$$
D = \partial_0 + j\partial_1 = 2\bigl(e_+\partial_+ + e_-\partial_-\bigr),
$$

so $f$ is left regular exactly when $f_+$ is a function of $\xi_-$ alone and $f_-$ is a function of $\xi_+$ alone. The regular functions of $\mathbb{D}$ therefore depend on arbitrary functions of one real variable, and they obey neither unique continuation nor Liouville's theorem nor the maximum principle: the bounded function

$$
f(x_0 + jx_1) = e^{-(x_0 - jx_1)^2} = e^{-(x_0^2+x_1^2)}\bigl(\cosh(2x_0x_1) + j\sinh(2x_0x_1)\bigr)
$$

is regular, is non-constant, and has $\|f\| \leq 1 = \|f(0)\|$, so its Euclidean norm attains its maximum at the interior point $0$. For $\mathbb{D}'$, a regular function has the form $f = u(x_1) + \varepsilon v(x_0, x_1)$ with $\partial_0 v = -u'$, so the bounded non-constant function $f = 1 + \varepsilon e^{-x_1^2}$ is regular, and $\|f\|$ attains its maximum along the line $x_1 = 0$. The mean value property fails in the same two systems.

## Consequences of Ellipticity

Assume from here on that $(A,D)$ is an elliptic hypercomplex system, so that $D\bar D = \bar D D = \Delta$, and that $\Omega \subseteq A$ is a domain, that is, open and connected.

**Theorem (regular implies harmonic).** If $f$ is left regular of class $C^2$ on $\Omega$, then each component of $f$ is harmonic:

$$
\Delta f = 0 \quad \text{componentwise}.
$$

*Proof.* If $Df = 0$ then

$$
\Delta f = \bar D D f = \bar D (0) = 0
$$

by the factorisation, and the Laplacian of an $A$-valued function is the $A$-valued function whose components are the Laplacians of the components. $\square$

**Theorem (analyticity).** Every left regular function on $\Omega$ is real-analytic. Consequently, if two left regular functions on a domain $\Omega$ agree on a subset with an accumulation point in $\Omega$, they agree on all of $\Omega$ (the **identity theorem**).

*Proof.* The operator $D$ is elliptic with smooth coefficients, so every solution of $Df = 0$ is smooth and, by analytic hypoellipticity of elliptic operators, real-analytic; the identity theorem for real-analytic functions then applies on the connected set $\Omega$. $\square$

**Theorem (maximum principle).** If $f$ is left regular on a domain $\Omega$ and the Euclidean norm $\|f\|$ attains its maximum at an interior point of $\Omega$, then $f$ is constant.

*Proof.* Each component of $f$ is harmonic by the previous theorem, so $\|f\|^2 = \sum_\alpha (f^\alpha)^2$ is a sum of squares of harmonic functions. A sum of squares of harmonic functions is subharmonic: for each squared term, $\Delta (u^2) = 2|\nabla u|^2 + 2u\Delta u = 2|\nabla u|^2 \geq 0$, and a sum of subharmonic functions is subharmonic. A subharmonic function that attains its maximum in the interior of a connected domain is constant, so $\|f\|^2$ is constant, and from $\Delta \|f\|^2 = 2\sum_\alpha |\nabla f^\alpha|^2 = 0$ each component is constant. $\square$

**Theorem (Liouville).** If $f$ is left regular on all of $A$ and $\|f\|$ is bounded, then $f$ is constant.

*Proof.* Each component of $f$ is a bounded harmonic function on all of $\mathbb{R}^m$, hence constant by Liouville's theorem for harmonic functions. $\square$

Both proofs are the honest generalisation of the complex-analytic arguments: the maximum principle and Liouville follow for regular functions because regularity reduces to harmonicity of the components.

## The Cauchy Formula of the General Theory

**Definition.** A **fundamental solution** of $D$ is a distribution $E$ on $A$ with $D E = \delta_0$, where $\delta_0$ is the delta distribution at the origin. A **Cauchy kernel** for the system is a function $E(x-y)$ obtained from a fundamental solution by translation.

**Theorem (existence of a fundamental solution).** Every nonzero constant-coefficient differential operator on $\mathbb{R}^m$ has a fundamental solution. In particular every generalised Cauchy–Riemann operator $D$ has one, and the kernel depends on the coefficients $B_\alpha$.

*Proof.* This is the Malgrange–Ehrenpreis theorem; the case at hand is the constant-coefficient case, where the fundamental solution may be taken as a finite combination of distributions of the form $P(\xi)^{-1}$ under the Fourier transform, with the singularities of the symbol handled by a suitable cut-off. $\square$

**Theorem (Cauchy–Pompeiu formula).** Let $\Omega \subseteq A$ be a bounded domain with smooth boundary $\partial\Omega$, oriented by the outward normal, and let $E$ be a Cauchy kernel for $D$. Then for $f$ of class $C^1$ on $\bar\Omega$ and $x \in \Omega$,

$$
f(x) = \int_{\partial\Omega} E(x-y)\,\nu_B(y)\,f(y)\,dS(y) - \int_\Omega E(x-y)\,(Df)(y)\,dy,
$$

where $\nu_B = \sum_\alpha \nu_\alpha B_\alpha$ is the **conormal element**, $\nu_\alpha$ the components of the outward unit normal, and $dS$ the surface measure.

**Corollary (Cauchy integral formula).** If $f$ is left regular on $\Omega$, the second integral vanishes and

$$
f(x) = \int_{\partial\Omega} E(x-y)\,\nu_B(y)\,f(y)\,dS(y), \qquad x \in \Omega.
$$

The Cauchy kernel $E$ and the explicit form of the boundary measure are different for each system. For the complex numbers the kernel is $E(z) = 1/(2\pi z)$ and the formula is the classical one; for a Clifford-type system the kernel is obtained by applying the conjugate operator $\bar D$ to a fundamental solution of the Laplacian, and its explicit form depends on the dimension $m$. What is general is the shape of the formula, and it is the shape that this article fixes: it expresses the values of a regular function inside a domain by its boundary values, through a kernel determined by the operator. The explicit kernels belong to the particular systems.

**Corollary (mean value property).** Let $f$ be left regular on a domain $\Omega$ and let $B(x,r) \subset \Omega$ be a ball. Then

$$
f(x) = \frac{1}{\mathrm{vol}\,B(x,r)} \int_{B(x,r)} f(y)\, dy,
$$

the average being taken componentwise. This is the mean value property of harmonic functions applied to each component of $f$.

## The Action of the Automorphism Group

**Proposition (automorphisms permute the operators).** Let $\sigma \in \operatorname{Aut}_{\mathbb{R}}(A)$ and let $D = \sum_\alpha B_\alpha \partial_\alpha$. Set

$$
\sigma \cdot D = \sum_\alpha \sigma(B_\alpha)\,\partial_\alpha.
$$

Then $f$ is $D$-regular if and only if $\sigma \circ f$ is $(\sigma \cdot D)$-regular.

*Proof.* Since $\sigma$ is an algebra automorphism and hence linear,

$$
\sigma(Df)(x) = \sigma\Bigl(\sum_\alpha B_\alpha \partial_\alpha f(x)\Bigr) = \sum_\alpha \sigma(B_\alpha)\,\partial_\alpha(\sigma \circ f)(x) = ((\sigma\cdot D)(\sigma\circ f))(x),
$$

using $\partial_\alpha(\sigma\circ f) = \sigma(\partial_\alpha f)$ in the last step by linearity of $\sigma$. Hence $Df = 0$ if and only if $(\sigma\cdot D)(\sigma \circ f) = 0$. $\square$

**Corollary.** The symmetry group of a hypercomplex system is the stabiliser

$$
\operatorname{Stab}(D) = \{\sigma \in \operatorname{Aut}_{\mathbb{R}}(A) : \sigma(B_\alpha) = B_\alpha \text{ for all } \alpha\},
$$

and it acts on the space of left regular functions by $f \mapsto \sigma \circ f$, preserving regularity, the maximum principle and the Cauchy formula. For a Clifford-type system the relevant stabiliser contains the orthogonal transformations of the generating subspace, and the resulting symmetry is the source of the conformal and Möbius structures of the particular theories. The algebra automorphisms themselves are the subject of *Automorphisms and Derivations of Algebras*.

## The Parallel Structure of the Systems

The method above takes a different shape for each algebra, and the articles of categories 26 to 29 are the rows of the following table. Three structural features decide the row: whether the algebra is a division algebra, whether it is commutative, and whether its natural operator is elliptic.

| Algebra | $m$ | $D$ | Left regular functions | What is lost |
|---|---|---|---|---|
| $\mathbb{R}$ | 1 | $d/dx_0$ | constants | richness |
| $\mathbb{C}$ | 2 | $\partial_0 + i\partial_1$ | holomorphic | nothing |
| $\mathbb{D}$ | 2 | $\partial_0 + j\partial_1$ | arbitrary functions of one characteristic variable | ellipticity, maximum principle, Liouville |
| $\mathbb{D}'$ | 2 | $\partial_0 + \varepsilon\partial_1$ | $u(x_1) + \varepsilon v(x_0,x_1)$ with $\partial_0 v = -u'$ | ellipticity, maximum principle, Liouville |
| $\mathbb{H}$ | 4 | $\partial_0 + e_1\partial_1 + e_2\partial_2 + e_3\partial_3$ | monogenic | closure under products, curve Morera |
| $\mathbb{H}_{\mathbb{D}}$ | 8 | $\partial_0 + e_1\partial_1 + e_2\partial_2 + e_3\partial_3$ in the four quaternionic coordinates | monogenic | closure under products, zero divisors |
| $\mathbb{B}$ | 8 | $\partial_0 + e_1\partial_1 + e_2\partial_2 + e_3\partial_3$ in the four complex coordinates | monogenic | closure under products, zero divisors |

The rows for $\mathbb{H}_{\mathbb{D}}$ and $\mathbb{B}$ treat the two eight-dimensional algebras through their four *quaternionic* coordinates: the variable is $\tilde Q = \sum_\mu Q_\mu e_\mu$ with coefficients $Q_\mu$ in $\mathbb{D}$ or in $\mathbb{C}$, the operator differentiates with respect to those four coordinates, and the remaining four real coordinates are carried as coefficients of the variable rather than as direction variables. The operator that $D$ factors is then the four-dimensional one, $\sum_\mu \partial^2/\partial Q_\mu^2$; it is the Euclidean Laplacian on the quaternion subspace, the negative of the Euclidean Laplacian on the anti-quaternion subspace, and it is indefinite in the underlying real coordinates on the Hermitian and anti-Hermitian subspaces. The theories so obtained are developed .

The rows are worked out system by system:for $\mathbb{C}$, where every classical theorem holds;and *Dual Numbers Analysis* for the two degenerate two-dimensional systems, where the idempotent and nilpotent structures replace the elliptic analysis;for $\mathbb{H}$, where the monogenic functions and the Fueter construction are developed. The general theorems of the present article are the common form of all of them: an operator, the kernel it defines, the Cauchy representation, and the consequences of ellipticity, with the last column of the table recording the price paid in each case.

## Summary

Hypercomplex analysis studies functions $f : \Omega \subseteq A \to A$ of a variable in a finite-dimensional unital associative real algebra $A$, using a **generalised Cauchy–Riemann operator** $D = \sum_\alpha B_\alpha \partial_\alpha$ and declaring $f$ **left regular** when $Df = 0$ (and right regular when $fD = 0$). Requiring the differential to be linear over $A$ is too strong: over $\mathbb{H}$ it forces $f(x) = ax + b$, so the construction proceeds through the operator instead. When the coefficients satisfy the Clifford relations $B_jB_k + B_kB_j = -2\delta_{jk}$ with $B_0 = 1$, the operator factors the Laplacian, $D\bar D = \bar D D = \Delta$, and this factorisation is the structural input the theory requires; a hypercomplex system is a pair $(A,D)$ for which it holds.

Regular functions form a real vector space, are closed under right multiplication by constants and under left multiplication by constants commuting with the coefficients, but not under products. Four features obstruct the naive programme: non-commutativity, which separates the left and the right theory; zero divisors, which make the difference quotient undefined along a set of directions and restrict the quotient rule to units; the one-sided module structure, which makes the regular functions a module over the centre rather than over $A$; and the dimension, which makes the requirement $df(x) \in L_A$ a system of $m^2 - m$ conditions on $m^2$ unknowns. The second notion that survives is $C$-holomorphy in a commutative subalgebra $C \subseteq A$: power series with coefficients in $A$ and variable in $C$ are $C$-differentiable, and for $C \cong \mathbb{C} \subseteq \mathbb{H}$ this recovers complex analysis with values in $\mathbb{B} \cong M_2(\mathbb{C})$. Under ellipticity regular functions are real-analytic (identity theorem), each component is harmonic (maximum principle via subharmonicity of $\|f\|^2$), and a bounded regular function on all of $A$ is constant (Liouville); for the degenerate systems $\mathbb{D}$ and $\mathbb{D}'$, whose operators have symbols vanishing on the real space, the last two fail, as does the mean value property, and the regular functions depend on arbitrary functions of fewer variables. The Cauchy–Pompeiu formula represents a general function by an integral of a Cauchy kernel of the system against its boundary values minus a volume integral of $Df$, and the Cauchy integral formula is the special case of a regular function; the kernel itself depends on the system. The algebra automorphisms act on the admissible operators and their stabiliser is the symmetry group of the system. Each system of categories 26 to 29 is a row of the table of the parallel structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Finite-dimensional unital associative real algebra, $\dim_\mathbb{R} A = m$ |
| $e_0 = 1, e_1, \dots, e_{m-1}$ | Fixed basis of $A$ |
| $\Omega$ | Open (or domain: open connected) subset of $A$ |
| $f : \Omega \to A$ | Hypercomplex-valued function |
| $D = \sum_\alpha B_\alpha \partial_\alpha$ | Generalised Cauchy–Riemann operator |
| $\bar D = \sum_\alpha \bar B_\alpha \partial_\alpha$ | Conjugate operator |
| $B_jB_k + B_kB_j = -2\delta_{jk}$ | Clifford relations on the coefficients |
| $Df = 0$ | Left regularity (monogenicity) |
| $fD = 0$ | Right regularity |
| $\Delta$ | Laplacian on $A \cong \mathbb{R}^m$ |
| $E$ | Fundamental solution / Cauchy kernel of $D$ |
| $\nu_B = \sum_\alpha \nu_\alpha B_\alpha$ | Conormal element of a boundary |
| $\sigma \cdot D$ | Action of $\sigma \in \operatorname{Aut}_\mathbb{R}(A)$ on operators |
| $A$-differentiability | $f(x+h) = f(x) + f'(x)h + o(\|h\|)$, too rigid for non-commutative $A$ |
| $C$-holomorphy | $A$-differentiability restricted to a commutative subalgebra $C \subseteq A$ |
| $L_A$ | Left multiplications in $\operatorname{End}_\mathbb{R}(A)$, $\dim = m$ |
| $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ | Split complex numbers, $j^2=+1$; degenerate for $D = \partial_0 + j\partial_1$ |
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual numbers, $\varepsilon^2=0$; degenerate for $D = \partial_0+\varepsilon\partial_1$ |
| $e_\pm = \tfrac12(1\pm j)$, $\xi_\pm = x_0\pm x_1$ | Idempotents and characteristic coordinates of $\mathbb{D}$ |



## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the classical theory of monogenic functions and the Cauchy integral formula.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the general function theory over Clifford algebras.
- Klaus Gürlebeck, Klaus Habetha and Wolfgang Sprößig, *Holomorphic Functions in the Plane and $n$-dimensional Space* (Birkhäuser, 2008), for the operator-theoretic general theory.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for a concrete account of the Cauchy kernel.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for Malgrange–Ehrenpreis and the existence of fundamental solutions.
- Walter Rudin, *Real and Complex Analysis* (McGraw–Hill, 3rd ed. 1987), for the harmonic-function theorems used here as standard.
