# __Exponential Polar Decomposition of Split-Complex Numbers__

## Introduction

This article develops the **exponential polar decomposition** of a nonzero split-complex number: the writing

$$
Q = \epsilon\exp(L), \qquad \epsilon\in\{\pm1,\pm j\}, \qquad L = \ln r+\phi j,
$$

with $r=\sqrt{\lvert N(Q)\rvert}>0$ the modulus, $\ln r$ the logarithmic scale and $\phi$ the hyperbolic angle. The exponent is a point of $\mathbb{D}$, not a class modulo a lattice: the exponential of $\mathbb{D}$ has trivial kernel. The decomposition is the modulus–unit decomposition $Q=ru$ of *Modulus–Unit Polar Decomposition of Split-Complex Numbers* with each factor written exponentially, $r=\exp(\ln r)$ and $u=\epsilon\exp(\phi j)$. Since $\mathbb{D}$ is commutative, the two continuous exponentials amalgamate into the single exponential $\exp(L)$; the finite factor $\epsilon$ names the component.

The exponential form is the third of the three polar decompositions of $\mathbb{D}$. The first is the modulus–unit form $Q=ru$, with $r=\sqrt{\lvert N(Q)\rvert}$ and $u=Q/r$, developed in *Modulus–Unit Polar Decomposition of Split-Complex Numbers*; the second is the rational-chart form of *Rational-Chart Polar Decomposition of Split-Complex Numbers*; the third is treated here. The three present one factorisation in three ways: the modulus–unit form is coordinate-free, while the rational and exponential forms put a coordinate on the unit factor, the rational one local and the exponential one global on each component, at the price of a finite component label.

The symbols are those of *Split-Complex Algebra*, *Split-Complex Norm and Invertibility* and *Conventions in Mathematics*, and the exponential and its group law are recalled from *Split-Complex Exponential and Lie Group Structure*. The article proves that the exponential is injective, that its image is the future cone, and that the discrete factor restores the other three components. The matrix picture is the two-dimensional matrix exponential, and the indefinite conformal reading of the exponential coordinates closes the article.

The plan is as follows. The exponential and its closed form are recalled (§*The Exponential and Its Closed Form*), its trichotomy is recorded (§*The Three Rows of the Exponential*), its image and kernel are computed (§*The Image and the Kernel*), and the polar word is read as one exponential (§*The Polar Word as One Exponential*). The logarithm and its fundamental domain are treated (§*The Logarithm and the Fundamental Domain*), the decomposition is stated and proved (§*The Exponential Polar Decomposition*), and the matrix picture (§*The Matrix Picture*) and the comparison (§*The Three Polar Decompositions*) follow. Examples are computed (§*Worked Examples*), and the exponential coordinates close the article (§*The Exponential Coordinates*). Every numerical value below was recomputed in double precision.

## The Exponential Map and the Polar Word

### The Exponential and Its Closed Form

For $L=q+jq'$ the exponential is the power series

$$
\exp L = \sum_{n=0}^{\infty}\frac{L^n}{n!},
$$

which converges absolutely and locally uniformly. Separating even and odd powers, and using $j^{2n}=1$ and $j^{2n+1}=j$, gives the closed form

$$
\exp(q+jq') = \exp(q)\left(\sum_{n=0}^{\infty}\frac{(q')^{2n}}{(2n)!}+j\sum_{n=0}^{\infty}\frac{(q')^{2n+1}}{(2n+1)!}\right) = \exp(q)\bigl(\cosh q'+j\sinh q'\bigr).
$$

The norm follows:

$$
N(\exp L)=\exp(2q)\bigl(\cosh^2 q'-\sinh^2 q'\bigr)=\exp(2q)>0.
$$

The exponential never reaches the null cone, never reaches negative norm, and never reaches positive norm with negative real part (§*The Image and the Kernel*). It is a homomorphism from the additive group of $\mathbb{D}$ to $\mathbb{D}^\times$, because $\mathbb{D}$ is commutative and the binomial theorem reorders the product of the two series:

$$
\exp(L_1+L_2)=\exp(L_1)\exp(L_2).
$$

### The Three Rows of the Exponential

The closed form is one row of a trichotomy governed by the square of the exponent direction. For $\nu\in\mathbb{D}$ with $\nu^2\in\{-1,0,+1\}$ and $t\in\mathbb{R}$,

$$
\exp(\nu t)=
\begin{cases}
\cos t+\nu\sin t, & \nu^2=-1,\\[2pt]
1, & \nu^2=0,\\[2pt]
\cosh t+\nu\sinh t, & \nu^2=+1.
\end{cases}
$$

The rows are trigonometric, parabolic and hyperbolic. The parabolic row is degenerate: the only solution of $\nu^2=0$ in $\mathbb{D}$ is $\nu=0$.

| equation | roots in $\mathbb{D}$ | row | image of $t\mapsto\exp(\nu t)$ |
|---|---|---|---|
| $\nu^2=-1$ | none | trigonometric | empty |
| $\nu^2=0$ | $\nu=0$ | parabolic | $\{1\}$ |
| $\nu^2=+1$ | $\nu=\pm1,\ \pm j$ | hyperbolic | $\mathbb{R}_{>0}$ for $\pm1$; the future branch of the unit hyperbola for $\pm j$ |

The trigonometric row is empty because $\mathbb{D}$ has no square root of $-1$. The hyperbolic row has four roots: $\pm1$ generate the real scale, and $\pm j$ generate the future branch $\exp(tj)=\cosh t+j\sinh t$; the past branch is reached by multiplying by $-1$. This is the exchange of the complex case, where $-1$ has roots $\pm i$ and $+1$ has roots $\pm1$. In the polar word the scale occupies the roots $\pm1$ and the unit factor the roots $\pm j$; the first row is empty and the middle row contributes nothing. The split algebra has no compact generator.

### The Image and the Kernel

**Kernel.** If $\exp(q+jq')=1$, then $\exp(q)\cosh q'=1$ and $\exp(q)\sinh q'=0$. Hence $\sinh q'=0$, so $q'=0$, and then $\exp(q)=1$, so $q=0$. The kernel is $\{0\}$ and the exponential is injective.

**Image.** The image is the future cone

$$
\exp(\mathbb{D})=\{Q:N(Q)>0,\ \operatorname{Re}Q>0\}=\{q>\lvert q'\rvert\}.
$$

If $Q=\exp(q+jq')$, then $N(Q)=\exp(2q)>0$ and $\operatorname{Re}Q=\exp(q)\cosh q'>\lvert\exp(q)\sinh q'\rvert$, so $Q$ lies in the set. Conversely, for $Q=x+jy$ with $x>\lvert y\rvert$, put

$$
q=\tfrac12\ln(x^2-y^2), \qquad q'=\operatorname{artanh}\frac{y}{x}.
$$

Then $q,q'$ are real, and $\exp(q+jq')=x+jy=Q$. The inverse is unique:

$$
L=\tfrac12\ln N(Q)+j\operatorname{artanh}\frac{q'}{q}, \qquad Q=q+jq',\quad q>\lvert q'\rvert.
$$

The exponential is therefore a diffeomorphism of $\mathbb{D}$ onto the identity component $(\mathbb{D}^\times)_0=\{q>\lvert q'\rvert\}$.

The image is **not** all of $\{N>0\}$: the past cone $\{N>0,\ q<0\}$ is missed. The witness is $-1$, which has norm $1$ and real part $-1$; in $\mathbb{C}$, $-1=\exp(i\pi)$, but here $-1=-\exp(0)$ uses the discrete factor. This is the precise sense in which the exponential is not onto the timelike region.

### The Polar Word as One Exponential

**Definition.** For $Q\in\mathbb{D}$ with $N(Q)\neq0$, an **exponential polar decomposition** is a writing

$$
Q=\epsilon\exp(\ln r)\exp(\phi j), \qquad r>0,\quad \phi\in\mathbb{R},\quad \epsilon\in\{\pm1,\pm j\},
$$

in which $\exp(\ln r)$ is the positive scale and $\epsilon\exp(\phi j)$ is the unit factor.

If $Q=\epsilon\exp(\ln r+\phi j)$, then

$$
\exp(\ln r)=r=\sqrt{\lvert N(Q)\rvert}, \qquad \epsilon\exp(\phi j)=\frac{Q}{r},
$$

and the two exponents commute, since $\mathbb{R}$ is central:

$$
Q=\epsilon\exp(\ln r)\exp(\phi j)=\epsilon\exp(\ln r+\phi j).
$$

The word is one exponential and one finite factor, not a product of two independent continuous exponentials. The amalgamation is a property of the commutative algebra; in a noncommutative algebra the exponents need not commute, as the polar word of *The Polar Element Representation of Biquaternions* shows.

| factor | formula | real dimension | range | exponent | parameter |
|---|---|---|---|---|---|
| scale | $\exp(\ln r)$ | $1$ | $(0,\infty)$ | $\ln r$ | $r>0$ |
| unit factor | $\epsilon\exp(\phi j)$ | $1$ | four branches | $\phi j$ | $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ |

The counts add to two on each component. The scale is non-compact, and the unit factor is non-compact too: its identity component is a line, not a circle. This is where the complex count is reproduced but the compactness is not.

## The Logarithm and the Fundamental Domain

### The Logarithm

**Definition.** A **logarithm** of $Q\in\mathbb{D}^\times$ is an element $L\in\mathbb{D}$ with $\exp L=Q$.

**Theorem.** An invertible split-complex number has a logarithm if and only if it lies in the future cone $\{N>0,\ \operatorname{Re}Q>0\}$; the logarithm is then unique.

**Proof.** If $Q=\exp L$, the image computation puts $Q$ in the future cone. Conversely, for $Q=q+jq'$ with $q>\lvert q'\rvert$,

$$
L=\tfrac12\ln N(Q)+j\operatorname{artanh}\frac{q'}{q}
$$

satisfies $\exp L=Q$ (§*The Image and the Kernel*). Uniqueness is injectivity.

The logarithm exists on one component of four; the other three have none. In $\mathbb{C}$ every nonzero element has a logarithm and only uniqueness fails. On the identity component,

$$
\operatorname{Log}Q=\tfrac12\ln N(Q)+j\operatorname{artanh}\frac{q'}{q}, \qquad Q=q+jq',\quad q>\lvert q'\rvert,
$$

is the unique logarithm: there is no principal branch to choose.

### The Fundamental Domain

**Theorem.** The exponential is a bijection $\mathbb{D}\to(\mathbb{D}^\times)_0=\{q>\lvert q'\rvert\}$, with inverse $\operatorname{Log}$.

**Proof.** This is the existence and uniqueness theorem above, read as a statement about the map.

The whole algebra is the domain; there is no strip. Since the kernel is $\{0\}$, the only fundamental domain is $\mathbb{D}$ itself. The quotient by the image is the component group:

$$
\mathbb{D}^\times/\exp(\mathbb{D})\cong\{\pm1,\pm j\}\cong(\mathbb{Z}/2\mathbb{Z})^2, \qquad \mathbb{D}^\times\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{D}.
$$

In $\mathbb{C}$ the exponential is onto, and $\mathbb{C}^\times\cong\mathbb{C}/2\pi i\mathbb{Z}$ is a cylinder, with a fundamental domain a strip of width $2\pi$. Here $\mathbb{D}^\times\cong(\mathbb{Z}/2)^2\times\mathbb{R}^2$: four planes. The discrete factor is not a period; it is the component label.

### The Logarithms of Some Elements

| $Q$ | $N(Q)$ | $\operatorname{Re}Q$ | $\operatorname{Log}Q$ |
|---|---|---|---|
| $2$ | $4$ | $2$ | $\ln2$ |
| $5+3j$ | $16$ | $5$ | $\ln4+j\ln2$ |
| $4+3j$ | $7$ | $4$ | $\tfrac12\ln7+j\operatorname{artanh}\tfrac34=0.9729550745\,(1+j)$ |
| $j$ | $-1$ | $0$ | none |
| $-1$ | $1$ | $-1$ | none |

The third line uses $\operatorname{artanh}(3/4)=\tfrac12\ln7$, and reconstructs $4+3j$ up to $9\times10^{-16}$. The last two lines have no logarithm at all. In the complex table $-1$ and $i$ would appear with logarithms $i\pi$ and $i\pi/2$; here neither has one.

## The Exponential Polar Decomposition

### Existence and Uniqueness

**Theorem.** Every split-complex number $Q$ with $N(Q)\neq0$ has exactly one exponential polar decomposition

$$
Q=\epsilon\exp(L), \qquad \epsilon\in\{\pm1,\pm j\},\quad L\in\mathbb{D}.
$$

**Existence.** Put $r=\sqrt{\lvert N(Q)\rvert}$ and $u=Q/r$, so $\lvert N(u)\rvert=1$. Write $u=x+yj$. Exactly one of the four elements $\epsilon u$ has norm $+1$ and positive real part: for $N(u)=1$ take $\epsilon=1$ if $x>0$ and $\epsilon=-1$ if $x<0$; for $N(u)=-1$ take $\epsilon=j$ if $y>0$ and $\epsilon=-j$ if $y<0$. For that $\epsilon$, $\epsilon u$ has a unique logarithm $L_0$. Then $L=L_0+\ln r$ satisfies $\exp L=r\exp L_0=r\epsilon u=\epsilon Q$.

**Uniqueness.** If $\epsilon\exp L=\epsilon_1\exp L_1$, then $\exp L=\epsilon\epsilon_1\exp L_1$. If $\epsilon\epsilon_1=1$, injectivity gives $L=L_1$ and $\epsilon=\epsilon_1$. If the product is $-1$, the right side has negative real part and the left side positive; if it is $\pm j$, the right side has negative norm and the left side positive. Both are impossible, so the pair is unique.

The decomposition is defined on $\mathbb{D}^\times$ and never uses the null cone. It does not claim that $\exp$ is onto $\{N>0\}$: the past cone uses $\epsilon=-1$. The four factors are the four components of the unit set.

### The Two Factors

The factors are

$$
\exp(\ln r)=r=\sqrt{\lvert N(Q)\rvert}, \qquad \epsilon\exp(\phi j)=\frac{Q}{r},
$$

and the exponent is their sum $L=\ln r+\phi j=\operatorname{Log}(\epsilon Q/r)+\ln r$. The logarithm is a right inverse of the exponential on the identity component, and the discrete factor extends this to the other three components. The continuous count is two on each component, the modulus and the angle; the component is a finite label. The group of units is

$$
\mathbb{D}^\times\cong\mathbb{R}_{>0}\times\mathbb{R}\times(\mathbb{Z}/2\mathbb{Z})^2.
$$

### The Group Law in Exponential Coordinates

The exponential turns multiplication into addition. In the coordinates $(\epsilon,\ln r,\phi)$,

$$
(\epsilon_1,\ln r_1,\phi_1)*(\epsilon_2,\ln r_2,\phi_2)=\bigl(\epsilon_1\epsilon_2,\ \ln(r_1r_2),\ \phi_1+\phi_2\bigr).
$$

The component, the logarithmic scale and the angle do not mix: $\mathbb{D}^\times$ is the product of the four-element group, a line and a line. In $\mathbb{C}$ the corresponding statement is $\mathbb{C}^\times\cong\mathbb{C}/2\pi i\mathbb{Z}$, with a periodic angle. Here the kernel is trivial, the exponent is a point of $\mathbb{D}$, and there is no period.

### The Decomposition in One Table

| datum | exponential polar decomposition |
|---|---|
| domain | $N(Q)\neq0$ |
| exponent | $L=\ln r+\phi j$, $r=\sqrt{\lvert N(Q)\rvert}$, $\phi\in\mathbb{R}$ |
| scale | $\exp(\ln r)=r=\sqrt{\lvert N(Q)\rvert}$ |
| unit factor | $\epsilon\exp(\phi j)=Q/r$ |
| uniqueness | $(\epsilon,L)$ unique; no period |
| group | $\mathbb{D}^\times\cong(\mathbb{Z}/2)^2\times\mathbb{D}$ |
| factor types | non-compact scale, non-compact unit factor, finite component label |

## The Matrix Picture

### The Exponential of a Symmetric Matrix

In the basis $\{1,j\}$, multiplication by $Q=q+jq'$ is $M_Q=qI+q'K$ with $K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $K^2=I$. Since $I$ and $K$ commute,

$$
\exp(xI+yK)=\exp(x)\bigl(\cosh y\,I+\sinh y\,K\bigr)=\exp(x)\begin{pmatrix}\cosh y&\sinh y\\ \sinh y&\cosh y\end{pmatrix}.
$$

The matrix is symmetric, with eigenvalues $\exp(x\pm y)>0$: the matrix exponential of a symmetric matrix is positive definite. Every positive definite matrix in the family has a unique real symmetric logarithm,

$$
\log M_Q=\tfrac12\ln N(Q)\,I+\operatorname{artanh}\frac{q'}{q}\,K, \qquad Q=q+jq',\quad q>\lvert q'\rvert.
$$

The symmetric matrix exponential therefore maps onto the positive definite matrices of the family, exactly the identity component. The other components are obtained by multiplying by $M_\epsilon\in\{I,-I,K,-K\}$; their matrices are not in that image.

The unit matrix is not orthogonal in general. The Euclidean polar factor of $M_Q$ is $I$ on the identity component, $-I$ on the opposite component, and a reflection on the spacelike region, as in *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, §*The Matrix Polar Decomposition*. The algebraic unit factor and the orthogonal matrix factor are different objects: the orthogonal factor is only the discrete part $\epsilon$, while the continuous factor $\exp(\phi j)$ is absorbed into the positive factor.

### The Matrix Logarithm

On the identity component the real symmetric logarithm is unique and is the matrix of $L$. There is no $2\pi i$ ambiguity: the eigenvalues are positive and the logarithm is taken in the symmetric subalgebra. For the other components $M_Q=M_\epsilon\exp(L)$. The Euclidean polar decomposition is $(M_Q,I)$ on the identity component, $(-M_Q,-I)$ on the opposite one, and $(\lvert M_Q\rvert,\text{reflection})$ on the spacelike region.

In $\mathbb{C}$ the matrix of a unit is a rotation in $SO(2)$ and the matrix exponential is periodic. Here the matrix of a unit of the identity component is symmetric positive definite, its logarithm is real and unique, and the matrix exponential is injective on the symmetric algebra.

### The Derivative and the Jacobian

The derivative of the exponential at $L$ is multiplication by $\exp L$:

$$
d\exp_L(H)=\exp(L)H,
$$

because $\exp(L+tH)=\exp(L)\exp(tH)$ when $\mathbb{D}$ is commutative. It is invertible, with inverse multiplication by $\exp(-L)$, so the exponential is a local diffeomorphism. The Jacobian determinant is

$$
\det d\exp_L=N(\exp L)=\exp(2q)=N(Q).
$$

The exponential multiplies the indefinite area by $N(Q)$ and is not a Euclidean conformal map.

## The Three Polar Decompositions

### The Three Forms

| decomposition | formula | parameters | domain | uniqueness | functions | group reading |
|---|---|---|---|---|---|---|
| modulus–unit | $Q=ru$ | $r>0$, $\lvert N(u)\rvert=1$ | $N\neq0$ | unique | square root | $\mathbb{R}_{>0}\times\mathbb{R}\times(\mathbb{Z}/2)^2$ |
| rational-chart | $Q=r\epsilon\frac{1-sj}{1+sj}$ | $r>0$, $\epsilon\in\{1,\pm j\}$, $s\neq\pm1$ | $N\neq0$ minus the negative real axis | unique on the chart | rational | group chunk, local |
| exponential | $Q=\epsilon\exp(\ln r+\phi j)$ | $r>0$, $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ | $N\neq0$ | unique; no period | exponential and logarithm | $(\mathbb{Z}/2)^2\times\mathbb{D}$ |

### The Modulus–Unit Form

The modulus–unit form $Q=ru$ is unique on $\mathbb{D}^\times$, uses the square root of the absolute norm, and is the product decomposition of the group of units.

### The Rational-Chart Form

The rational-chart form writes the unit factor by the Cayley chart

$$
u(s)=\frac{1-sj}{1+sj}=\frac{1+s^2}{1-s^2}-j\frac{2s}{1-s^2}, \qquad s\neq\pm1,
$$

a bijection from $\mathbb{R}\setminus\{\pm1\}$ onto $\{N=1\}\setminus\{-1\}$; it is rational and misses the negative real axis.

### The Exponential Form

The exponential form $Q=\epsilon\exp(\ln r+\phi j)$ is global on $\mathbb{D}^\times$, uses the exponential and the logarithm, and has a unique exponent; the price is the finite factor $\epsilon$.

### The Change of Coordinates

Comparing $u(s)$ with $u=\exp(\phi j)$ gives

$$
\frac{1-sj}{1+sj}=\exp\bigl(-2j\operatorname{artanh}s\bigr), \qquad s=-\tanh\frac{\phi}{2},\quad \phi=-2\operatorname{artanh}s.
$$

On the identity component this sends $\mathbb{R}$ onto $(-1,1)$. On the past component the rational chart has $\epsilon=1$ and the exponential chart $\epsilon=-1$; the same element satisfies $u(s)=-\exp(\phi j)$, hence $s=-\coth(\phi/2)=1/s_{\text{exp}}$. On the spacelike components the formula $s=-\tanh(\phi/2)$ holds with $s\in(-1,1)$.

### What the Comparison Says

The three forms are three presentations of one factorisation. The modulus–unit form is global and algebraic, with a square root; the rational-chart form is rational and local, missing the negative real axis; the exponential form is global and transcendental, with a finite component label instead of a kernel. The exponential form is the only one in which the group law is addition, and the modulus–unit form the only one that is algebraic and global.

In $\mathbb{C}$ the exponential is onto $\mathbb{C}^\times$, the angle is periodic, and no discrete factor is needed. Here the image is one component and $\mathbb{D}^\times/\exp(\mathbb{D})\cong(\mathbb{Z}/2)^2$. In a noncommutative algebra the amalgamation into one exponential fails; in the polar word of *The Polar Element Representation of Biquaternions* the order of the factors carries information.

## Worked Examples

### A Generic Split-Complex Number

Take $Q=5+3j$. Then $N(Q)=16$, $r=4$, and

$$
\phi=\operatorname{artanh}\tfrac35=\ln2=0.6931471805599453, \qquad L=\ln4+j\ln2=1.3862943611198906+0.6931471805599453\,j.
$$

The reconstruction is

$$
\exp L=4\bigl(\cosh(\ln2)+j\sinh(\ln2)\bigr)=4(1.25+0.75j)=5+3j,
$$

with error zero in double precision.

### A Table of Examples

| $Q$ | $N(Q)$ | $\epsilon$ | $L$ | $\exp L$ | $\lvert\epsilon\exp L-Q\rvert$ |
|---|---|---|---|---|---|
| $2$ | $4$ | $1$ | $\ln2$ | $2$ | $0$ |
| $-2$ | $4$ | $-1$ | $\ln2$ | $2$ | $0$ |
| $j$ | $-1$ | $j$ | $0$ | $1$ | $0$ |
| $-j$ | $-1$ | $-j$ | $0$ | $1$ | $0$ |
| $5+3j$ | $16$ | $1$ | $\ln4+j\ln2$ | $5+3j$ | $0$ |
| $-5-3j$ | $16$ | $-1$ | $\ln4+j\ln2$ | $5+3j$ | $0$ |
| $1+2j$ | $-3$ | $j$ | $\tfrac12\ln3+j\operatorname{artanh}\tfrac12$ | $2+j$ | $2.2\times10^{-16}$ |
| $-1-2j$ | $-3$ | $-j$ | $\tfrac12\ln3+j\operatorname{artanh}\tfrac12$ | $2+j$ | $2.2\times10^{-16}$ |
| $-1+2j$ | $-3$ | $j$ | $\tfrac12\ln3-j\operatorname{artanh}\tfrac12$ | $2-j$ | $2.2\times10^{-16}$ |
| $1-2j$ | $-3$ | $-j$ | $\tfrac12\ln3-j\operatorname{artanh}\tfrac12$ | $2-j$ | $2.2\times10^{-16}$ |

The error is at most $2.3\times10^{-16}$. The table covers the four components; the vertices $\pm j$ have exponent $0$ and are pure discrete factors.

### The Trivial Kernel

The kernel is $\{0\}$:

$$
\exp(0)=1, \qquad \exp(2\pi j)=\cosh(2\pi)+j\sinh(2\pi)=267.7467614837482+267.7448940410164\,j\neq1.
$$

There is no period and no lattice. The equation $\exp L=1$ has the sole solution $L=0$. The element $-1$ has no logarithm, not infinitely many: the complex non-uniqueness is replaced by a failure of existence on three components.

### The Missed Past Cone

The element $-1$ has norm $1$ but no real logarithm, because its real part is negative; it is reached only as $-\exp(0)$, with $\epsilon=-1$. Every element of the past cone is written $\epsilon\exp(L)$ with $\epsilon=-1$, where $L$ is the logarithm of its opposite. The exponential alone reaches exactly the future cone.

## The Exponential Coordinates

### The Coordinate Lines

On each component the exponential coordinates are

$$
Q=\epsilon\exp(q+jq'), \qquad (q,q')\in\mathbb{R}^2,
$$

with the coordinate pairs

$$
\epsilon=\pm1:\quad (x,y)=\pm\bigl(\exp(q)\cosh q',\ \exp(q)\sinh q'\bigr),
$$

$$
\epsilon=\pm j:\quad (x,y)=\pm\bigl(\exp(q)\sinh q',\ \exp(q)\cosh q'\bigr),
$$

a diffeomorphism of $\mathbb{R}^2$ onto the component, with inverse

$$
q=\tfrac12\ln\lvert N(Q)\rvert, \qquad q'=\operatorname{artanh}\frac{y'}{x'},
$$

where $(x',y')$ are the coordinates of $\epsilon Q$, which lies in the future cone.

| coordinate | image | geometry |
|---|---|---|
| $q=\text{const}$ | $x^2-y^2=N(\epsilon)\exp(2q)$ | a hyperbola branch, the level set of the norm |
| $q'=\text{const}$ | the ray $t(\cosh q',\sinh q')$, $t>0$, mapped by $Q=\epsilon\exp(q+jq')$ | a ray from the origin |

The grid is hyperbolic polar. The curves of constant $q$ are the hyperbolas of constant norm; the curves of constant $q'$ are the rays of constant rapidity. There is no angular periodicity: $q'$ runs over the whole line.

### The Conformal Factor

The Jacobian of $(q,q')\mapsto(x,y)$ is

$$
J=\begin{pmatrix}\partial x/\partial q&\partial x/\partial q'\\ \partial y/\partial q&\partial y/\partial q'\end{pmatrix}=\begin{pmatrix}x&y\\ y&x\end{pmatrix},
\qquad \det J=x^2-y^2=N(Q)=\pm\exp(2q).
$$

The signed Jacobian is $N(Q)$, positive on the timelike components and negative on the spacelike ones; its absolute value is $\exp(2q)$. The pullback of the indefinite metric is

$$
dx^2-dy^2=N(Q)\bigl(dq^2-dq'^2\bigr),
$$

because $dx=x\,dq+y\,dq'$ and $dy=y\,dq+x\,dq'$ cancel their cross terms. The map is conformal for the indefinite metric with factor $N(Q)$: positive on the two timelike components and negative on the two spacelike ones.

There is no Euclidean conformal claim. The Euclidean pullback is

$$
dx^2+dy^2=(x^2+y^2)\bigl(dq^2+dq'^2\bigr)+4xy\,dq\,dq',
$$

which is not proportional to $dq^2+dq'^2$ unless $xy=0$.

### The Harmonic Reading

The coordinate $q=\tfrac12\ln\lvert N\rvert$ and the angle $q'$ are linear, hence harmonic for the indefinite Laplacian $\square=\partial_q^2-\partial_{q'}^2$. The pair $(q,q')$ is the global coordinate supplied by the logarithm on the identity component, and the exponential is its inverse. The logarithm is not global because its domain is one component of four; the obstruction is the discrete quotient $(\mathbb{Z}/2)^2$, not a period.

## Summary

The exponential is $\exp(q+jq')=\exp(q)(\cosh q'+j\sinh q')$, with $N(\exp L)=\exp(2q)>0$. It is injective, its image is the future cone $\{N>0,\ \operatorname{Re}Q>0\}$, and it is not onto $\{N>0\}$: the past cone is missed. The inverse on the future cone is $\operatorname{Log}Q=\tfrac12\ln N(Q)+j\operatorname{artanh}(q'/q)$, and it is unique.

Every invertible split-complex number has a unique exponential polar decomposition $Q=\epsilon\exp(L)$, with $\epsilon\in\{\pm1,\pm j\}$ and $L=\ln r+\phi j$. The factor $\epsilon$ records the component; the exponent is computed from $\epsilon Q$, which lies in the future cone. The group law is $(\epsilon_1,L_1)(\epsilon_2,L_2)=(\epsilon_1\epsilon_2,L_1+L_2)$, so $\mathbb{D}^\times\cong(\mathbb{Z}/2)^2\times\mathbb{D}$. The kernel is trivial, so there is no periodic ambiguity. The logarithm exists on one component and fails on the other three: this is the exchange of the complex case, where it exists everywhere and fails to be unique.

In the matrix picture the exponential of $xI+yK$ is $\exp(x)(\cosh y\,I+\sinh y\,K)$, symmetric positive definite on the identity component, with a unique real symmetric logarithm; the matrix of a unit is not orthogonal in general. The exponential coordinates map each component onto $\mathbb{R}^2$, with Jacobian $N(Q)$ and indefinite conformal factor $N(Q)$: $dx^2-dy^2=N(Q)(dq^2-dq'^2)$. The map is not Euclidean conformal.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra, $j^2=+1$ |
| $Q=q+jq'$ | a split-complex number |
| $N(Q)=q^2-q'^2$ | the norm |
| $\exp(L)$ | the exponential, $\exp(q)(\cosh q'+j\sinh q')$ |
| $L=q+jq'$ | an exponent in $\mathbb{D}$ |
| $\epsilon$ | the component sign, $\epsilon\in\{\pm1,\pm j\}$ |
| $\phi$ | the hyperbolic angle, $L=\ln r+\phi j$ |
| $\operatorname{Log}Q$ | the logarithm on the future cone |
| $(\mathbb{D}^\times)_0=\{q>\lvert q'\rvert\}$ | the identity component, the future cone |
| $K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | the reflection, $K^2=I$ |
| $M_Q=qI+q'K$ | the matrix of multiplication by $Q$ |
| $\operatorname{artanh}$ | the inverse hyperbolic tangent, $\lvert\cdot\rvert<1$ |
| $SO(1,1)$ | the determinant-one Lorentz group of the plane, two components |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic functions and the split-complex exponential.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra, its idempotents and its exponential.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map, the Lorentz group and its components.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds* (Springer, Graduate Texts in Mathematics 149, 2nd ed. 2006), for the rapidity coordinate and the Lorentzian conformal structure.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for indefinite metrics and conformal structures.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for indefinite forms and their isometry groups.
