# __The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set__

## Introduction

This article computes, for a constant-coefficient differential operator with biquaternion coefficients, the symbol, the real block matrix that left multiplication by the symbol induces, the determinant of that block, and the zero set of the determinant.

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of real dimension eight, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, the products $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$, and the relations $\vec e_k^{2}=-e_t$. Its element is

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_\mu\in\mathbb{C},
$$

and the scalar imaginary $i$ is central. Two forms of $\tilde Q$ are used throughout, and they are kept apart: the **norm** $N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, which is complex-valued, and the **vector form** $B^2=Q_x^2+Q_y^2+Q_z^2$, so that $N=Q_t^2+B^2$. The letter $B$ alone is never an element of the algebra; a root of $B^2$ enters only through the notation $\lambda_\pm=Q_t\pm iB$ of §*The Two Roots*.

**What is proved.** That the algebra is the complex matrix algebra of $2\times2$ matrices and that the norm is the determinant there (§*The Algebra and Its Model*). That the symbol of an operator is an element which is not central, so that the equation it defines is complex and not real (§*The Symbol in the Biquaternion Algebra*). That left multiplication by an element is a $4\times4$ complex matrix $\Lambda(\tilde Q)$ and a real $8\times8$ matrix in two $4\times4$ blocks (§*The Block Matrix of Left Multiplication*). That the block determinant is $\lvert N(\tilde Q)\rvert^{4}$, and why the modulus is not decoration (§*The Block Determinant*). That the two roots of the characteristic polynomial are $Q_t\pm iB$, and that the roots, their multiplicities and the rank are given by five cases (§*The Two Roots and the Five Cases*). That the zero set is cut by one complex equation, that is two real equations, that it is a cone of real codimension two which contains real linear subspaces of dimension four and is not one, and that its nonzero points are exactly the zero divisors (§*The Zero Set: One Complex Equation, Two Real Equations* and §*The Zero Divisors*).

**What is quoted.** The general theory of the symbol, of solvability at one frequency and of the determinant of the regular representation is *The Fourier Transform and the Symbol of a Differential Operator*, and two of its results are used: that at the frequency $\zeta$ the equation is solvable for every right-hand side exactly when $\sigma_P(\zeta)$ is a unit, and that the kernel and the cokernel of $L_a$ have dimension $d-\operatorname{rank}L_a$. The product, the conjugation and the two forms are *Product and Form Conventions*; the matrix model with $\mathsf M_2(\vec e_k)=-i\sigma_k$ and $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ is *Matrix Representations Conventions*; the algebra itself is *The Biquaternion Algebra*. The kernel $W(t,\omega)=\exp(-2\pi i\tilde{Ζ}\omega t)$ and the condition $\tilde{Ζ}^2=e_t$ are *Biquaternion Continuous Harmonic Analysis*. The classification of the roots of $e_t$ is quoted there and not proved here.

**The root.** The transform of the ladder uses a root $\tilde{Ζ}$ of $1$, fixed once and for all, and the kernel is $\exp(-2\pi i\tilde{Ζ}\omega t)$: the element carries the square $e_t$, the scalar $i$ beside it carries the sign. This article takes the root **pure**, so that $\tilde{Ζ}$ has zero scalar part and $(\tilde{Ζ},\tilde{Ζ})=-1$, the value forced by $\tilde{Ζ}^2=e_t$. The central pair $\pm e_t$ is excluded, and not by taste: a spectrally regular element supplies the pure root $\tilde{Ζ}=-i\vec Q/B$ and never a central one (§*The Root and the Frequency*). The symbol of this article is nevertheless defined with the central $i$, which is the convention of *The Fourier Transform and the Symbol of a Differential Operator*, and §*The Root and the Frequency* says exactly how the two readings are related, and which of the statements below survive the change of root.

**Boundaries.** The inversion of the transform, the poles of the inverse and the growth of its tails are *The Inverse Fourier Transform of a Symbol* and *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*; the support of the transformed object, the rank of left multiplication as a function of the frequency, and the degenerate norm are the subject of the next article of the ladder; the three placements of the kernel are *The Three Kernel Placements of the Biquaternion Fourier Transform*. This article stops at the algebraic objects: the symbol, the block, its determinant, and the set where the determinant vanishes.

## The Algebra and Its Model

### The Product and the Quadratic Identity

**The product.** In coordinates the multiplication is

$$
\tilde Q_1\tilde Q_2=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]e_t+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2,
$$

where $(\vec Q_1,\vec Q_2)=Q_{1x}Q_{2x}+Q_{1y}Q_{2y}+Q_{1z}Q_{2z}$ is the complex bilinear form and $\vec Q_1\times\vec Q_2$ the complex bilinear cross product with $\vec e_x\times\vec e_y=\vec e_z$. The coefficients are complex, so neither object is the real form of its name; both are the complex bilinear extensions of the real ones, and every identity below is an algebraic identity in the four coefficients.

**Proposition (the quadratic identity).** Every element satisfies

$$
\tilde Q^2-2Q_t\tilde Q+N(\tilde Q)e_t=0 .
$$

*Proof.* Put $\vec Q_1=\vec Q_2=\vec Q$ in the product formula. Then $\vec Q\times\vec Q=0$ by the antisymmetry of the cross product, and

$$
\tilde Q^2=\bigl(Q_t^2-(\vec Q,\vec Q)\bigr)e_t+2Q_t\vec Q=\bigl(2Q_t^2-N\bigr)e_t+2Q_t\vec Q ,
$$

the last step because $(\vec Q,\vec Q)=B^2=N-Q_t^2$; subtracting $2Q_t\tilde Q=2Q_t^2e_t+2Q_t\vec Q$ and adding $N e_t$ leaves zero.

**Remark (what the identity says, and what it is for).** Every element satisfies a quadratic equation whose coefficients lie in the centre $\mathbb{C}e_t$. So the subalgebra generated by one element has complex dimension at most two, and the algebra generated by the left multiplications of one element has dimension at most two as well. **Everything in this article that concerns the spectrum follows from that one fact**: the characteristic polynomial of left multiplication has degree four and its two roots, once found, exhaust the spectrum.

**The norm.** The quaternion conjugate is $\tilde Q^{\natural}=Q_te_t-\vec Q$, and $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$. Expanded, $N=Q_t^2+(\vec Q,\vec Q)=Q_t^2+B^2$. It is a polynomial in the four coefficients with complex values, so it is a complex multiple of $e_t$, and a multiple of the identity commutes with everything. **The norm is central because it is a scalar, not because of any accident of the formula.**

### The Model as a Complex Matrix Algebra

**Proposition (the model).** The map

$$
\mathsf M(\tilde Q)=Q_tI-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)
$$

is an isomorphism of $\mathbb{C}$-algebras from $\mathbb{B}$ onto $M_2(\mathbb{C})$, and for every element $\det\mathsf M(\tilde Q)=N(\tilde Q)$ and $\operatorname{tr}\mathsf M(\tilde Q)=2Q_t$.

*Proof.* The images of the units are $\mathsf M(e_t)=I$, $\mathsf M(\vec e_x)=-i\sigma_1$, $\mathsf M(\vec e_y)=-i\sigma_2$, $\mathsf M(\vec e_z)=-i\sigma_3$, and these satisfy the defining relations: the product of each of the three with itself is $-I$, and the products are $\mathsf M(\vec e_x)\mathsf M(\vec e_y)=(-i)^2\sigma_1\sigma_2=-i\sigma_3=\mathsf M(\vec e_z)$, with the two other products the same, because $\sigma_1\sigma_2=i\sigma_3$, $\sigma_2\sigma_3=i\sigma_1$ and $\sigma_3\sigma_1=i\sigma_2$. A linear map that carries the units to elements satisfying the relations of the units is a homomorphism. It is injective because the four images are linearly independent over $\mathbb{C}$, and both spaces have complex dimension four, so it is an isomorphism. For the determinant, expand:

$$
\mathsf M(\tilde Q)=\begin{pmatrix}Q_t-iQ_z&-(Q_y+iQ_x)\\ Q_y-iQ_x&Q_t+iQ_z\end{pmatrix},
$$

whose determinant is $(Q_t-iQ_z)(Q_t+iQ_z)+(Q_y+iQ_x)(Q_y-iQ_x)=Q_t^2+Q_z^2+Q_y^2+Q_x^2=N(\tilde Q)$, and the trace is $2Q_t$ by inspection.

**Corollary (multiplicativity, and the units).** For all $\tilde Q,\tilde R$ one has $N(\tilde Q\tilde R)=N(\tilde Q)N(\tilde R)$, and $\tilde Q$ is a unit exactly when $N(\tilde Q)\ne0$.

*Proof.* The model is multiplicative and the determinant is multiplicative; an element of $M_2(\mathbb{C})$ is invertible exactly when its determinant is nonzero.

**Remark (why the model is the right tool and not a detour).** Left multiplication by $\tilde Q$ is multiplication of matrices on the left, so the model turns a question about an algebra into a question about a $2\times2$ matrix, and the answer to every question of this article is a statement about that matrix. **The model is used for the determinant and for the rank; the units are used for the block form, and the two computations are independent.**

### What Is Central and What Is Not

**Proposition (the norm is central and the product is not).** $N(\tilde Q)$ lies in $\mathbb{C}e_t$ for every $\tilde Q$, and $\tilde Q^2$ is central exactly when $Q_t\vec Q=0$, that is when $Q_t=0$ or $\vec Q=0$.

*Proof.* The first is that $N$ is a polynomial in the four complex coefficients. For the second, the quadratic identity gives $\tilde Q^2=2Q_t\tilde Q-N(\tilde Q)e_t$, whose second term is central and whose first is central exactly when $Q_t\vec Q=0$.

**Example (a product that is not central).** Take $\tilde Q=e_t+\vec e_x$. Then $\tilde Q^2=e_t+2\vec e_x$, and

$$
[\tilde Q^2,\vec e_y]=2[\vec e_x,\vec e_y]=2(\vec e_x\vec e_y-\vec e_y\vec e_x)=4\vec e_z\ne0 ,
$$

so the product of an element with itself need not commute with the algebra.

**Remark (the one reason the zero set is one complex equation).** A central element defines a scalar equation; a non-central one defines none. The symbol of the next section is not central, and its product with itself is not central, so neither can cut the zero set. **The norm is the only scalar the symbol carries**, and the zero set of the transform is the vanishing of that scalar. In a commutative algebra the symbol is central, and the zero set is the vanishing of the symbol itself, of degree $m$. Here the symbol is not central, the scalar it carries is the norm, and the degree is $2m$: **the loss of centrality costs one factor of degree two in the equation, and no more than that.**

## The Symbol in the Biquaternion Algebra

### Definition and Examples

**Definition (the symbol).** Let $P(D)=\sum_{\lvert\alpha\rvert\le m}a_\alpha\partial^\alpha$ with $a_\alpha\in\mathbb{B}$ and let $\zeta\in\mathbb{R}^n$. The **symbol** of $P$ is

$$
\sigma_P(\zeta)=\sum_{\lvert\alpha\rvert\le m}a_\alpha(i\zeta)^\alpha\in\mathbb{B},
$$

a polynomial of degree $m$ in the $n$ real variables $\zeta_1,\dots,\zeta_n$, with values in the algebra; $m$ is the **order** of $P$.

**Remark (the symbol is an element, not a number).** For a scalar symbol the condition "not a unit" is the single condition "nonzero". Here the symbol is an element of an eight-dimensional algebra and the condition "not a unit" is $N(\sigma_P(\zeta))=0$, which by the last proposition is one complex condition on a real variable, that is two real conditions. **A frequency is a point of $\mathbb{R}^n$; what the transform asks at that point is whether a certain algebra element is a unit, and the answer is a complex equation.**

**Example (the gradient).** For $P(D)=e_t\partial_0+\vec e_x\partial_1+\vec e_y\partial_2+\vec e_z\partial_3$ on $\mathbb{R}^4$ the symbol is

$$
\sigma_\nabla(\zeta)=i\bigl(\zeta_0e_t+\zeta_1\vec e_x+\zeta_2\vec e_y+\zeta_3\vec e_z\bigr),
$$

whose norm is $N(\sigma_\nabla(\zeta))=-s$ with $s=\zeta_0^2+\zeta_1^2+\zeta_2^2+\zeta_3^2$, because each coefficient is $i\zeta_k$ and $(i\zeta_k)^2=-\zeta_k^2$. The norm is real and non-positive, and it vanishes only at $\zeta=0$; the zero set is the single point $0$.

**Example (a zero set of two lines).** For $P(D)=e_t\partial_1+\vec e_x\partial_2+i\vec e_x\partial_3$ on $\mathbb{R}^3$ the symbol is $\sigma_P(\zeta)=i\zeta_1e_t+(i\zeta_2-\zeta_3)\vec e_x$, whose norm is

$$
N(\sigma_P(\zeta))=-\zeta_1^2-\zeta_2^2+\zeta_3^2-2i\zeta_2\zeta_3 .
$$

The real part and the imaginary part are independent polynomials here, and their common zeros are $\zeta_2=0$ with $\zeta_3=\pm\zeta_1$: two lines through the origin, of real dimension one and codimension two. **This is the typical shape of a biquaternion zero set, and the previous example is the atypical one**, in which the imaginary part vanishes identically and a definite polynomial cuts a point.

**Example (a norm that vanishes identically).** For $P(D)=(\vec e_x+i\vec e_y)\partial_1$ the symbol is $\sigma_P(\zeta)=i\zeta_1\vec e_x-\zeta_1\vec e_y$, whose norm is $-\zeta_1^2+\zeta_1^2=0$ for every $\zeta$. The coefficient is nilpotent, the determinant vanishes identically, and every frequency is a zero. The zero set is then the whole line, and no power of the determinant narrows it; this is the degenerate case treated in the next article of the ladder.

### The Root and the Frequency

**The kernel and the frequency it carries.** The transform of the ladder is built on $W(t,\omega)=\exp(-2\pi i\tilde{Ζ}\omega t)$ with $\tilde{Ζ}^2=e_t$, and the derivative of the kernel is $\partial_tW=-2\pi i\tilde{Ζ}\omega W$. So $D^kW=(-2\pi i\tilde{Ζ}\omega)^kW$ and, for a one-variable operator,

$$
P(D)W(\cdot,\omega)=\sigma_P(\zeta)\,W(\cdot,\omega)\qquad\text{at}\qquad\zeta=-2\pi\omega\tilde{Ζ} .
$$

**Remark (the frequency is an element of the algebra).** For a pure root the frequency $-2\pi\omega\tilde{Ζ}$ is a pure biquaternion with a nonzero vector part, so **the symbol of the transform is read at an algebra-valued frequency and not at a real one**, and it is the element $i\zeta$ that is real, not $\zeta$. Only for the central root $\tilde{Ζ}=\pm e_t$ does the substitution collapse to a real number, $\zeta=\mp2\pi\omega\in\mathbb{R}$, and only then is the frequency set of the transform the real zero set of this article. The real-frequency theory is therefore the theory of the central root, and the pure roots are a different problem with the same algebra.

**Proposition (a regular element supplies a pure root).** Let $\tilde Q$ have $B^2\ne0$ and let $B$ be a root of $B^2$. Then $\tilde{Ζ}=-i\vec Q/B$ is pure, $\tilde{Ζ}^2=e_t$, and $\tilde{Ζ}$ is not central.

*Proof.* The element $\vec Q/B$ is pure because $\vec Q$ is, and $\tilde{Ζ}$ is a complex multiple of it, so $\tilde{Ζ}$ is pure; it is not central because a central element has zero vector part. Its square is $(-i)^2\vec Q^2/B^2$, and $\vec Q^2=-(\vec Q,\vec Q)e_t=-B^2e_t$ by the quadratic identity applied to the pure element $\vec Q$, so $\tilde{Ζ}^2=(-1)(-1)e_t=e_t$.

**Remark (the sign of the norm depends on the root, and the determinant does not).** Write $\lVert\omega\rVert^2=\omega_0^2+\omega_1^2+\omega_2^2+\omega_3^2$ for the frequency vector of the transform. The gradient symbol at the frequency the transform supplies is $\sigma_\nabla=-2\pi i\tilde{Ζ}\vec\omega$, and its norm is

$$
N(\sigma_\nabla)=-4\pi^2\lVert\omega\rVert^2 \ \text{at the central root},\qquad N(\sigma_\nabla)=+4\pi^2\lVert\omega\rVert^2 \ \text{at a pure root},
$$

the sign being $N(\tilde{Ζ})=\pm1$. The zero set is the same point in both readings, and the determinant is the same function,

$$
\det L_{\sigma_\nabla}= \lvert N(\sigma_\nabla)\rvert^{4}=(4\pi^2\lVert\omega\rVert^2)^4 ,
$$

because the fourth power absorbs the sign. **The root moves the sign of the norm and cannot move the determinant**, and that is the first indication that the determinant, and not the norm, is the invariant object of the theory.

## The Block Matrix of Left Multiplication

### The Complex Block

**Definition (left multiplication).** For $\tilde Q\in\mathbb{B}$ the map $L_{\tilde Q}:\mathbb{B}\to\mathbb{B}$, $X\mapsto\tilde QX$, is linear over $\mathbb{R}$ and also linear over the central complex numbers, because $i$ is central.

**Proposition (the complex block).** In the complex basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the matrix of $L_{\tilde Q}$ is

$$
\Lambda(\tilde Q)=\begin{pmatrix}Q_t&-Q_x&-Q_y&-Q_z\\ Q_x&Q_t&-Q_z&Q_y\\ Q_y&Q_z&Q_t&-Q_x\\ Q_z&-Q_y&Q_x&Q_t\end{pmatrix},
$$

whose trace is $4Q_t$, and $\Lambda(\tilde Q\tilde R)=\Lambda(\tilde Q)\Lambda(\tilde R)$ with $\Lambda(e_t)=I$.

*Proof.* The $k$-th column is the coordinate vector of $\tilde Q\vec e_k$. For $k=x$ the product is $-Q_xe_t+Q_te_x-Q_z\vec e_y+Q_y\vec e_z$, which is the second column, and the three other columns are the same computation with the cyclic order of the units. The trace is the sum of the diagonal entries. The multiplicativity is the associativity of the product, $(XY)Z=X(YZ)$, read as a statement about matrices, and $L_{e_t}$ is the identity.

**Remark (the block is the regular representation).** The matrix $\Lambda$ is the left regular representation of the algebra in its own basis, and the two properties just proved are the two properties of every regular representation: it is multiplicative and it carries the unit to the identity. **Nothing about the biquaternions is used in the proof, and everything about them is visible in the entries**: the four rows are the coordinates of the products with the four units.

### The Real Block

**Proposition (the real block).** In the real basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ the matrix of $L_{\tilde Q}$ is

$$
L_{\tilde Q}=\begin{pmatrix}A&-C\\ C&A\end{pmatrix},\qquad A=\operatorname{Re}\Lambda(\tilde Q),\quad C=\operatorname{Im}\Lambda(\tilde Q).
$$

*Proof.* A complex-linear map on a complex space, written in a real basis made of the vectors $v$ and $iv$, has that block form: the image of $v$ is $(\operatorname{Re}\Lambda)v+(\operatorname{Im}\Lambda)iv$, and the image of $iv$ is $-(\operatorname{Im}\Lambda)v+(\operatorname{Re}\Lambda)iv$. The two statements are the two block columns.

**Remark (the block form is the realification, and it is not a new computation).** The real block contains no information beyond the complex one; it is the same operator read in a real basis. **Its use is that the determinant of a realification is a modulus**, and that is what makes the answer of the next section $\lvert N\rvert^4$ and not $N^4$.

### The Matrix-Unit Block

**Proposition (two copies of the model).** In the basis $E_{11},E_{21},E_{12},E_{22}$ of the matrix units, the matrix of $L_{\tilde Q}$ is block diagonal with two copies of $\mathsf M(\tilde Q)$.

*Proof.* Left multiplication is $X\mapsto \mathsf M(\tilde Q)X$, which acts on the two columns of $X$ separately; in the basis that lists the first column before the second, each column is multiplied by $\mathsf M(\tilde Q)$, and no entry mixes the columns.

**Remark (the two blocks and the two minimal left ideals).** The two copies are the two columns: an element of the first is a matrix whose second column vanishes, an element of the second is one whose first column vanishes, and left multiplication preserves each of the two spaces, which are minimal left ideals of complex dimension two. **The decomposition is not the spectral decomposition**, which depends on the element and is the subject of §*The Two Roots and the Five Cases*; it is the decomposition that exists for every element at once.

## The Block Determinant

**Theorem (the determinant of left multiplication).** For every $\tilde Q\in\mathbb{B}$,

$$
\det\Lambda(\tilde Q)=N(\tilde Q)^2,\qquad \det L_{\tilde Q}=\lvert N(\tilde Q)\rvert^{4}.
$$

*Proof.* The quadratic identity, applied through the homomorphism $\Lambda$, gives $\Lambda(\tilde Q)^2-2Q_t\Lambda(\tilde Q)+N(\tilde Q)I=0$, so the minimal polynomial of $\Lambda(\tilde Q)$ divides $x^2-2Q_tx+N(\tilde Q)$, and the spectrum lies in the set of its two roots, counted with multiplicity. The trace of $\Lambda(\tilde Q)$ is $4Q_t$. If the two roots $\lambda_+,\lambda_-$ are distinct, the multiplicities $m_+,m_-$ satisfy $m_++m_-=4$ and $m_+\lambda_++m_-\lambda_-=4Q_t=2(\lambda_++\lambda_-)$, whence $m_+=m_-=2$; if they coincide, the single root is $Q_t$ and the eigenvalue $Q_t$ has multiplicity four. In both cases the characteristic polynomial is the product of the two linear factors each taken twice, and its constant term, which is the determinant, is $N(\tilde Q)^2$. For the real block: the determinant of the realification of a complex matrix is the product of its complex determinant with its conjugate, that is $\lvert\det\Lambda\rvert^2$, and $\lvert N^2\rvert^2=\lvert N\rvert^4$.

**Remark (why $\lvert N\rvert^4$ and not $N^4$).** The norm is complex-valued, so $N^4$ is a complex number and cannot be the determinant of a real matrix; the modulus is not decoration, it is the only real function of $N$ that the realification can produce. When the norm happens to be real on the frequencies in question — for the gradient, and for every symbol whose coefficients make $N(\sigma_P(\zeta))$ real — the two expressions agree and the modulus is invisible. **The distinction is invisible exactly on the real-norm symbols and visible everywhere else**, and a computation that writes $N^4$ is right on one class of examples and wrong on the rest.

**Remark (the determinant is a repeated factor, and this matters later).** Writing $N(\sigma_P(\zeta))=a(\zeta)+ib(\zeta)$ with $a,b$ real polynomials, the determinant is $(a^2+b^2)^2$, the product of two conjugate factors, each taken twice. **Every zero of the determinant is therefore a multiple zero as a polynomial in $\zeta$**, and no statement about the order of a zero of the determinant can be read off the degree of the symbol alone. The consequences for the inverse transform are the subject of *The Inverse Fourier Transform of a Symbol* and *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*.

**Proposition (the gradient, computed).** For the gradient symbol of §*Definition and Examples*,

$$
\det L_{\sigma_\nabla(\zeta)}=s^4,\qquad s=\zeta_0^2+\zeta_1^2+\zeta_2^2+\zeta_3^2 ,
$$

and the statement holds with either sign of the norm.

*Proof.* The norm is $-s$ for the central root and $+s$ for the pure one, and the determinant is the fourth power of the modulus of the norm, which is $s^4$ in both readings.

**Remark (the degree).** The determinant of $L_{\sigma_P}$ is a real polynomial of degree $8m$ in $\zeta$ when $P$ has order $m$, which is $dm$ with $d=8$, as it must be for the determinant of a $d\times d$ block with entries of degree $m$. The complex equation $N(\sigma_P(\zeta))=0$ has degree $2m$. **The two degrees differ by the factor four that the modulus contributes**, and only the second is the degree of the equation that the zero set actually solves.

## The Two Roots and the Five Cases

### The Two Roots

**Proposition (the roots).** Let $B$ be a root of $B^2=(\vec Q,\vec Q)$. Then

$$
x^2-2Q_tx+N(\tilde Q)=(x-Q_t-iB)(x-Q_t+iB),
$$

so the two roots are $\lambda_\pm=Q_t\pm iB$, and the characteristic polynomial of $\Lambda(\tilde Q)$ is $(x-Q_t-iB)^2(x-Q_t+iB)^2$.

*Proof.* Expand $(x-Q_t)^2+B^2=x^2-2Q_tx+Q_t^2+B^2=x^2-2Q_tx+N(\tilde Q)$, and factor the sum of two terms as a difference, $(x-Q_t)^2-(iB)^2$, which gives the two linear factors because $(iB)^2=-B^2$. The characteristic polynomial is the product of the two factors each twice by the argument of §*The Block Determinant*.

**Remark (the root of $B^2$ is not canonical, and the pair of roots is).** The choice of $B$ exchanges the two roots and changes nothing else; when $B^2=0$ the two roots coincide at $Q_t$ and no choice is made. **The pair of roots is a function of the element, and the labelling of the pair is not**, which is why every statement below is a statement about the pair or about the multiset of roots with multiplicities.

**Remark (multiplicity is counted in the complex plane).** The matrix $\Lambda(\tilde Q)$ is complex $4\times4$, and the multiplicities of the table below are its algebraic multiplicities. A root of complex multiplicity $m$ occupies $2m$ real dimensions, so multiplicity two is four real dimensions and multiplicity four is all eight. As a real $8\times8$ matrix the operator also has the conjugate roots, and the real spectrum is the union of the roots with their conjugates; **the table is read in the complex plane, where the two generalized eigenspaces of $\Lambda(\tilde Q)$ live.**

### The Five Cases

**Theorem (roots, multiplicities and rank).** The following five rows are exhaustive and mutually exclusive.

| Condition | The roots, with algebraic multiplicity | $\operatorname{rank}L_{\tilde Q}$ | The element |
|---|---|---|---|
| $N\ne0$, $B^2\ne0$ | $Q_t+iB$ and $Q_t-iB$, each twice | $8$ | a unit, diagonalisable |
| $N\ne0$, $B^2=0$ | $Q_t$, four times | $8$ | a unit, not diagonalisable |
| $N=0$, $Q_t\ne0$ | $0$ and $2Q_t$, each twice | $4$ | a null element, diagonalisable |
| $N=0$, $Q_t=0$, $\tilde Q\ne0$ | $0$, four times | $4$ | nilpotent, minimal polynomial $x^2$ |
| $\tilde Q=0$ | $0$, four times | $0$ | zero |

*Proof.* The rows are exhaustive because $N=Q_t^2+B^2$: if $B^2\ne0$ then $N\ne0$ unless $Q_t^2=-B^2$, in which case $N=0$ and $Q_t\ne0$; if $B^2=0$ then $N=Q_t^2$, so $N=0$ exactly when $Q_t=0$, which is the fourth row, and $N\ne0$ exactly when $Q_t\ne0$, which is the second. They are mutually exclusive by inspection.

Row one: the roots are distinct, so the minimal polynomial has distinct roots and the matrix is diagonalisable; their multiplicities are two and two by the trace; the determinant $N^2$ is nonzero, so the rank is eight.

Row two: $B^2=0$ means $\vec Q^2=-B^2e_t=0$, so $\vec Q$ is nilpotent and $\tilde Q=Q_te_t+\vec Q$ with $(\tilde Q-Q_t)^2=\vec Q^2=0$. The single root is $Q_t$ with multiplicity four; the determinant is $Q_t^4\ne0$, so the rank is eight; and the matrix is not diagonalisable, because a diagonalisable matrix with the single eigenvalue $Q_t$ is $Q_tI$, and $\Lambda(\tilde Q)\ne Q_tI$ since $\vec Q\ne0$.

Row three: $Q_t^2=-B^2\ne0$, so the roots are $0$ and $2Q_t$ and they are distinct; the matrix is diagonalisable, and the rank is the dimension of the eigenspace of the nonzero root: two over $\mathbb{C}$, that is four over $\mathbb{R}$, which is the entry of the table. The identity $\tilde Q^2=2Q_t\tilde Q$, obtained from the quadratic identity and $N=0$, gives the same conclusion as a factorisation: $\Lambda(\Lambda-2Q_tI)=0$.

Row four: $B^2=0$ and $Q_t=0$ give $\tilde Q^2=0$ by the quadratic identity, so $\Lambda(\tilde Q)^2=0$; and $\Lambda(\tilde Q)\ne0$ because $\tilde Q\ne0$. The minimal polynomial is therefore $x^2$, the algebraic multiplicity of the root $0$ is four, and the matrix is not diagonalisable. For the rank, a nonzero nilpotent of $M_2(\mathbb{C})$ has rank one, so its column space is a line; the image of $L_{\tilde Q}$ is the set of matrices whose columns lie in that line, of complex dimension two, and the kernel is the set of matrices $X$ with $\tilde QX=0$, likewise of complex dimension two. The rank is four over $\mathbb{R}$.

Row five: $\Lambda(0)=0$.

**Remark (the two rows with $N\ne0$ differ, and the difference is not a technicality).** Both rows are units, and both have full rank; they differ in whether the left multiplication can be diagonalised. An element of the second row is a unit of the form $Q_te_t+\vec Q$ with $\vec Q$ nilpotent, such as $e_t+\vec e_x+i\vec e_y$, and its left multiplication is a unipotent operator: invertible, with a single eigenvalue, and with a nontrivial Jordan block. **In the vocabulary of the corpus the first row is spectrally regular and the second is spectrally degenerate, and both are units**; the two conditions are independent, and the split by the norm alone does not see the difference.

**Remark (the nilpotent row, stated by the minimal polynomial).** In the fourth row the eigenvalues are not the object to compute: a numerical eigensolver returns small nonzero numbers for a matrix whose spectrum is exactly zero, and a reported spectrum is then an artefact of the arithmetic. **The right statement is the algebraic one**: $\tilde Q^2=0$, the minimal polynomial is $x^2$, the algebraic multiplicity is four, the geometric multiplicity is two, and the matrix is not diagonalisable. Every one of those five statements is exact.

**Remark (the rank on the null set).** The third and fourth rows both have rank four, and between them they are the whole null set away from the origin. So on the null set the rank is four, off it the rank is eight, and at the origin the rank is zero. **The rank does not vary within the null set away from the origin**, and this is why the next article of the ladder can speak of the rank on the cone as a single number.

## The Zero Set: One Complex Equation, Two Real Equations

### The Equation

**Definition (the zero set).** For the operator $P$ the **zero set** is

$$
Z(P)=\{\zeta\in\mathbb{R}^n:\sigma_P(\zeta)\text{ is not a unit of }\mathbb{B}\}=\{\zeta\in\mathbb{R}^n:N(\sigma_P(\zeta))=0\},
$$

the second form by the corollary of §*The Model as a Complex Matrix Algebra*.

**Proposition (one complex equation, two real equations).** There are real polynomials $a,b$ of degree at most $2m$ with

$$
N(\sigma_P(\zeta))=a(\zeta)+ib(\zeta),
$$

and $Z(P)=\{\zeta:a(\zeta)=0,\ b(\zeta)=0\}$: the zero set is cut by one complex equation, that is by two real equations.

*Proof.* $N(\sigma_P(\zeta))$ is a polynomial in $\zeta$ with complex coefficients, since $N$ is a polynomial with complex coefficients in the four components of $\sigma_P$, which are themselves complex polynomials in $\zeta$. Every complex polynomial is $a+ib$ with $a,b$ real, and a complex number vanishes exactly when both parts do.

**Remark (this is the structural difference from a real algebra).** In a real algebra the determinant is a real polynomial, the zero set is one real equation, and in the generic case the codimension is one; the shapes of that case are catalogued in *The Fourier Transform and the Symbol of a Differential Operator*. **Here the algebra is complex, the equation is complex, and the codimension is two**, unless the imaginary part vanishes identically or the two parts are dependent. The gradient is the case of a vanishing imaginary part and the two-lines example is the typical case.

### The Cone in the Algebra

**Proposition (the null set is a cone of real codimension two).** The set $\{\tilde Q:N(\tilde Q)=0\}$ is invariant under multiplication by real scalars, and away from the origin it is a real manifold of dimension six in the eight coordinates.

*Proof.* Homogeneity is clear from the formula. Write $Q_\mu=u_\mu+iv_\mu$ with real $u_\mu,v_\mu$; then $a=\sum(u_\mu^2-v_\mu^2)$ and $b=2\sum u_\mu v_\mu$, and the Jacobian of the pair $(a,b)$ with respect to $(u,v)$ has the two rows $(2u,-2v)$ and $(2v,2u)$. The rows are dependent exactly when $u=\lambda v$ and $-v=\lambda u$ for a real $\lambda$, which forces $\lambda^2=-1$ unless $u=v=0$; so the Jacobian has rank two at every point other than the origin, and the fibre has dimension $8-2=6$ there.

**Remark (a cone is not a linear subspace, and this one contains maximal ones).** The null set is not closed under addition: the pure elements $\vec e_x$ and $\vec e_x+i\vec e_y$ are null, and $2\vec e_x+i\vec e_y$ has norm $3$. It nevertheless contains linear subspaces, of real dimension four, and they are the largest possible. **A reader who concludes from "not a subspace" that it contains none would be wrong**, and the mistake is easy to make because the analogous real cone, of a definite form, contains only the origin.

**Proposition (maximal null subspaces).** Let $M$ be a complex subspace of $\mathbb{C}^4$ on which the complex bilinear form $(\cdot,\cdot)$ vanishes identically. Then every element of $M$, read as an element of $\mathbb{B}$, is null, and $\dim_\mathbb{C}M\le2$. Conversely, a real subspace all of whose elements are null has real dimension at most four, and dimension four is attained.

*Proof.* For $v=\sum_kc_ku_k$ with $u_k\in M$ and $c_k\in\mathbb{C}$, bilinearity gives $(v,v)=\sum_{k,l}c_kc_l(u_k,u_l)=0$, so $v$ is null, that is $N(v)=0$. The form is nondegenerate on $\mathbb{C}^4$, and a totally isotropic subspace of a nondegenerate symmetric form in four complex dimensions has complex dimension at most two. For the bound over $\mathbb{R}$: if a real subspace $L$ consists of null elements, polarisation gives $2(v,w)=N(v+w)-N(v)-N(w)=0$ for $v,w\in L$, so $L$ is totally isotropic, its complex span has complex dimension $\dim_\mathbb{R}L$, and therefore $\dim_\mathbb{R}L\le4$. The bound is attained by the example below.

**Example (a maximal null subspace).** Take $M$ spanned over $\mathbb{C}$ by $\vec e_x+i\vec e_y$ and $e_t+i\vec e_z$. Each of the two is null, since $1+i^2=0$, and the form of one with the other vanishes because distinct units are orthogonal; so every element of $M$ is null. A general element is $c_1(\vec e_x+i\vec e_y)+c_2(e_t+i\vec e_z)$ with $c_1,c_2\in\mathbb{C}$, and the two complex parameters are four real ones.

### The Three Shapes, in This Algebra

**The point.** For the gradient, $a=-s$ is definite and $b=0$: one equation remains, the zero set is the single point $\zeta=0$, and the codimension is four. **A definite polynomial cuts more than a hypersurface, and the codimension of the zero set is not a function of the number of equations alone.**

**The cone.** For a symbol whose two parts are independent, as in the two-lines example, the zero set has codimension two and is a genuine cone. It is the shape a generic biquaternion symbol produces.

**The whole space.** For a symbol with a nilpotent coefficient, as in the third example of §*Definition and Examples*, the norm vanishes identically and $Z(P)=\mathbb{R}^n$. **The determinant is then the zero polynomial, and no statement about the transform can be made from it**; the algebra of the operator has degenerated along a whole family of symbols, and the phenomenon is the one treated in the next article of the ladder under the name of the degenerate norm.

## The Zero Divisors

**Proposition (the null elements and the zero divisors).** Let $\tilde Q\ne0$. Then $\tilde Q$ is a zero divisor of $\mathbb{B}$ exactly when $N(\tilde Q)=0$.

*Proof.* If $\tilde Q\tilde X=0$ with $\tilde X\ne0$, then $L_{\tilde Q}$ is not injective, so its determinant vanishes; the determinant is $\lvert N(\tilde Q)\rvert^4$, so $N(\tilde Q)=0$. Conversely, if $\tilde Q\ne0$ is null then row three or row four of §*The Five Cases* gives $\operatorname{rank}L_{\tilde Q}=4<8$, so $L_{\tilde Q}$ has a nonzero kernel and there is $\tilde X\ne0$ with $\tilde Q\tilde X=0$.

**Remark (the zero set is the set of zero divisors, and the origin is the exception).** By the proposition, the null set away from the origin is exactly the set of two-sided zero divisors, and it is also exactly the zero set of the symbol at a frequency where the symbol is null. **The three sets coincide**: the frequencies where the transform is not solvable, the frequencies where the symbol is a zero divisor, and the zeros of the determinant. The origin is null and is not a zero divisor under the strict definition, which asks for a nonzero cofactor; and at the origin the rank is zero and every element annihilates every element.

**Proposition (the annihilators have dimension four).** For $\tilde Q\ne0$ with $N(\tilde Q)=0$, both the right annihilator $\{X:\tilde QX=0\}$ and the left annihilator $\{Y:Y\tilde Q=0\}$ have real dimension four.

*Proof.* The right annihilator is the kernel of $L_{\tilde Q}$, of dimension $8-4=4$ by rank and nullity. For the left annihilator, the model gives $\tilde Q\mapsto\mathsf M(\tilde Q)$, a nonzero singular matrix of rank one, and $Y\tilde Q=0$ means that each row of $\mathsf M(Y)$ lies in the left null space of $\mathsf M(\tilde Q)$, which is a line; so the space of such $Y$ has complex dimension two, that is real dimension four.

**Remark (why the rank is four, structurally).** The image of $L_{\tilde Q}$ is the left ideal $\mathbb{B}\tilde Q$, and for a null element this is a minimal left ideal. The algebra is the full matrix algebra $M_2(\mathbb{C})$, which is **simple**: it has no two-sided ideal other than $0$ and the algebra itself, so no smaller two-sided object can hold the null elements. It does have one-sided ideals, namely the spaces of matrices whose columns lie in a fixed line, and those are exactly the image and the two annihilators of a null element. **The simplicity of the algebra is why the null set cannot be narrowed by any algebraic condition finer than one determinant, and the one-sided ideals are why the rank drops to four and not lower.**

## Summary

The symbol of a biquaternion-coefficient operator is an element of the algebra, not a number, and it is not central. Its product with itself is not central either, so the only scalar it carries is the norm $N=Q_t^2+B^2$, and the frequency at which the equation becomes singular is the frequency where that scalar vanishes. The vanishing is one complex equation, that is two real equations, and the zero set is a cone of real codimension two, containing real linear subspaces of dimension four while not being one.

The block of left multiplication is a $4\times4$ complex matrix in the units and a real $8\times8$ matrix in two $4\times4$ blocks, the second being the realification of the first. Its determinant is $\lvert N\rvert^4$: the complex determinant is $N^2$, and the realification replaces it by its product with its conjugate. The modulus is not decoration; on symbols with real norm it agrees with $N^4$, and off them it is the only real function available.

The spectrum has two roots, $Q_t\pm iB$, and the five cases separate what the roots alone do not: a unit can have a non-diagonalisable left multiplication, and the nilpotent case has a single root at zero with a minimal polynomial of degree two. On the null set away from the origin the rank is four, the two annihilators have dimension four, and the null elements are exactly the zero divisors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of real dimension $8$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The units, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $\tilde Q$ | An element $Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with complex coefficients |
| $N(\tilde Q)$ | The norm $Q_t^2+Q_x^2+Q_y^2+Q_z^2$, central and complex-valued |
| $B^2$ | The vector form $Q_x^2+Q_y^2+Q_z^2$, so that $N=Q_t^2+B^2$ |
| $B$ | A root of $B^2$, used only in $\lambda_\pm=Q_t\pm iB$ |
| $\tilde Q^{\natural}$ | The quaternion conjugate $Q_te_t-\vec Q$ |
| $i$ | The central scalar imaginary |
| $\mathsf M(\tilde Q)$ | The matrix model $Q_tI-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$ |
| $\sigma_k$ | The Pauli matrices $\sigma_1,\sigma_2,\sigma_3$ |
| $L_{\tilde Q}$ | Left multiplication $X\mapsto\tilde QX$, real-linear and complex-linear |
| $\Lambda(\tilde Q)$ | The matrix of $L_{\tilde Q}$ in the complex basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $A$, $C$ (in §*The Real Block*) | The real and imaginary parts of $\Lambda(\tilde Q)$ |
| $\zeta$ | The frequency, a point of $\mathbb{R}^n$; $n$ the number of variables |
| $-2\pi\omega\tilde{Ζ}$ | The algebra-valued frequency the transform supplies |
| $P(D)$ | A constant-coefficient operator $\sum_{\lvert\alpha\rvert\le m}a_\alpha\partial^\alpha$ with $a_\alpha\in\mathbb{B}$ |
| $\sigma_P(\zeta)$ | The symbol $\sum a_\alpha(i\zeta)^\alpha$, an element of $\mathbb{B}$ |
| $m$ | The order of $P$ |
| $Z(P)$ | The zero set $\{\zeta\in\mathbb{R}^n:N(\sigma_P(\zeta))=0\}$ |
| $a(\zeta)$, $b(\zeta)$ | The real and imaginary parts of $N(\sigma_P(\zeta))$ |
| $\lambda_\pm$ | The two roots $Q_t\pm iB$ of the characteristic polynomial |
| $s$ | The Euclidean quadratic form $\zeta_0^2+\zeta_1^2+\zeta_2^2+\zeta_3^2$ |
| $\tilde{Ζ}$ | A root of $1$, taken pure and fixed once, $\tilde{Ζ}^2=e_t$ |
| $W(t,\omega)$ | The kernel $\exp(-2\pi i\tilde{Ζ}\omega t)$ |
| $E_{ij}$ | The matrix units of $M_2(\mathbb{C})$ |

## Further Reading

- *The Fourier Transform and the Symbol of a Differential Operator*, for the symbol of a general algebra-valued operator, the solvability at one frequency, the determinant of the regular representation and its table of four algebras, and the three shapes of a zero set; this article is the biquaternion row of that table, developed.
- *The Biquaternion Algebra*, for the units, the product, the conjugations and the two forms, and for the proofs of the identities used in §*The Algebra and Its Model*.
- *Product and Form Conventions*, for the twelve products and the four forms, the letters $P$, $N$, $H$ and $\mathrm{Kr}$, and the convention on the cross product that fixes the sign of the products of the units.
- *Matrix Representations Conventions*, for the isomorphism onto $M_2(\mathbb{C})$, the assignment $\mathsf M_2(\vec e_k)=-i\sigma_k$, and the identity $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.
- *Biquaternion Continuous Harmonic Analysis*, for the kernel $W(t,\omega)$, the condition $\tilde{Ζ}^2=e_t$, the classification of the roots of $1$, the transform pair, and the gradient whose symbol is computed here.
- *The Inverse Fourier Transform of a Symbol*, for the pole order of the inverse against the multiplicity of a factor of the determinant, which is where the repeated factors of §*The Block Determinant* become the growth of an inverse.
