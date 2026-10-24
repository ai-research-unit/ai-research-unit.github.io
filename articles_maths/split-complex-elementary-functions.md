# __Split-Complex Elementary Functions__

## Introduction

This article defines the elementary functions of a split-complex variable: the exponential, the logarithm, the powers and roots, and the trigonometric and hyperbolic functions. The hyperbolic pair is the intrinsic family of the algebra, and the circular pair is included for comparison with the complex and reduced biquaternion cases. Each function is defined once, its basic properties are recorded, and its value is read on the two eigenvalues.

The spectral data are those of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*, §*The Spectrum and the Characteristic Polynomial*, §*The Eigenprojections* and §*Powers, Polynomial Calculus, and the Group of Units*; they are collected in §*The Eigenvalue Data* and used without proof. The idempotent coordinates and the eigenvalues are the same two numbers; this article writes $\lambda_\pm$ whenever the number is read as a value at an idempotent. The algebra, its basis and its conjugation are those of *Split-Complex Algebra*; the norm and the group of units are those of *Norm and Invertibility in the General Split-Complex Algebra*; the idempotents are those of *Square Roots of One and the Idempotents of the Split-Complex Algebra*.

**Plan.** The spectral setting is recalled first, with the two regimes and the Idempotent Principle (§*The Spectral Setting*). The exponential and the logarithm follow, with their kernels, images and fibres (§*The Exponential*, §*The Logarithm*); the powers and roots follow from the logarithm (§*Powers and Roots*); the trigonometric and hyperbolic functions and their inverses follow (§*The Trigonometric and Hyperbolic Functions*); the relations to the real and complex cases close the theory (§*Relations to the Neighbouring Cases*). The results are collected in tables in §*Summary*, including the comparison with the reduced biquaternion and biquaternion cases.

Every numerical value displayed below was recomputed in double precision.

**Notation.** A split-complex number is written $Q=q+jq'$ with $q,q'\in\mathbb{R}$ and $j^{2}=1$. The conjugate is $\bar Q=q-jq'$ and the norm is $\langle Q\rangle_{*}=Q\bar Q=q^{2}-q'^{2}$.

## The Spectral Setting

### The Eigenvalue Data

The spectral data are those of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*, §*The Spectrum and the Characteristic Polynomial*, §*The Eigenprojections* and §*Powers, Polynomial Calculus, and the Group of Units*. The definitions, the decomposition and their proofs are there; this article uses them and does not repeat them. The table collects the results in the form used below.

| Quantity | Value |
|---|---|
| Spectrum | $\sigma(Q)=\{\lambda_+,\lambda_-\}$ |
| Eigenvalues | $\lambda_+=q+q'=Q_+$, $\lambda_-=q-q'=Q_-$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$, primitive, orthogonal, complete, central |
| Eigenvalue decomposition | $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Characteristic polynomial | $p_Q(X)=(X-\lambda_+)(X-\lambda_-)$ |
| Distinctness | $\lambda_+\neq\lambda_-$ exactly when $q'\neq0$ |
| Norm | $\langle Q\rangle_{*}=q^2-q'^2=\lambda_+\lambda_-$ |
| Unit criterion | $Q$ is a unit exactly when $\lambda_+\lambda_-\neq0$ |
| Polynomial calculus | $f(Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-$ for every polynomial $f$ |
| Lattice | trivial, $\ker\exp=\{0\}$: the exponential is injective |

The idempotent coordinates and the eigenvalues are the same two numbers; this article writes $\lambda_\pm$ whenever the number is read as a value at an idempotent. The pair $(\Pi_+,\Pi_-)$ is the only nontrivial pair of complementary orthogonal idempotents, and both members are primitive and central because the algebra is commutative.

### The Regimes

The algebra has two spectral regimes, read from the discriminant $4q'^2$ of the characteristic polynomial; the distinct regime splits into the units and the zero divisors. The table gives what each regime changes for the functions below; the spectral data of each regime are those of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*, §*Degenerate Regimes*.

| Regime | Condition | Consequence for the functions |
|---|---|---|
| Distinct, not a zero divisor | $q'\neq0$, $\langle Q\rangle_{*}\neq0$ | $\log$ is defined on the future cone; the powers and roots read two nonzero eigenvalues |
| Zero divisor | $q'\neq0$, $\langle Q\rangle_{*}=0$ | $\exp$ does not reach it, so $\log$ is undefined; a trigonometric or hyperbolic value may be a zero divisor |
| Scalar | $q'=0$ | one eigenvalue; the two-term spectral form is a non-unique refinement |

The algebra is reduced: the only nilpotent is $0$ (*The Specificities of the Split-Complex Algebra*). There is therefore no nilpotent regime. The distinct regime splits into the units and the zero divisors according to whether the norm vanishes, and the scalar regime is the only spectral degeneration. In the scalar regime the eigenvalue decomposition has one term, and the two-term writing is a non-unique refinement; the functions below are unaffected, because their spectral form is continuous in $\lambda_\pm$.

### The Idempotent Principle

Every elementary function of this article, and every higher special function of *Split-Complex Higher Special Functions*, is read on the two eigenvalues. The rule is stated once.

**Theorem (Idempotent Principle).** Let $\Phi(x)=\sum_{n\geq0}c_nx^n$ be a real power series with radius of convergence $\rho$, and let $Q\in\mathbb{D}$ have eigenvalues $\lambda_\pm$ with $\lvert\lambda_\pm\rvert<\rho$. Then the series $\sum c_nQ^n$ converges and

$$
\Phi(Q)=\Phi(\lambda_+)\Pi_++\Phi(\lambda_-)\Pi_-.
$$

For a function defined by an integral, an inverse or another real formula, the same display is the definition of its split-complex extension: the formula is applied to the two eigenvalues, and the value is defined exactly when the real formula is defined at both $\lambda_\pm$.

**Proof.** *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*, §*Powers, Polynomial Calculus, and the Group of Units*, gives $Q^n=\lambda_+^n\Pi_++\lambda_-^n\Pi_-$ for every $n\geq0$, with $\Pi_\pm$ orthogonal idempotents and $\Pi_++\Pi_-=1$. Summing termwise,

$$
\sum_{n\geq0}c_nQ^n
=\sum_{n\geq0}c_n\bigl(\lambda_+^n\Pi_++\lambda_-^n\Pi_-\bigr)
=\Bigl(\sum_{n\geq0}c_n\lambda_+^n\Bigr)\Pi_+
+\Bigl(\sum_{n\geq0}c_n\lambda_-^n\Bigr)\Pi_-,
$$

and the rearrangement is legitimate because the series converges absolutely in each component. This proves the first statement; the second is the definition of the componentwise extension.

The principle is the spectral calculus of the algebra. It converts every function below into a pair of ordinary real functions, and it is the only ingredient the later articles need.

## The Exponential

### Definition

The **split-complex exponential** is defined for $Q\in\mathbb{D}$ by

$$
\exp(Q)=\sum_{n=0}^\infty \frac{Q^n}{n!}.
$$

The series converges absolutely for every $Q$ in the Euclidean norm. The function is entire in the split-complex sense, and it satisfies

$$
\exp(Q_1+Q_2)=\exp(Q_1)\exp(Q_2), \qquad \exp(0)=1, \qquad \frac{d}{dQ}\exp(Q)=\exp(Q).
$$

### The Closed Form

By the Idempotent Principle applied to the exponential series,

$$
\boxed{\exp(Q)=\exp(\lambda_+)\Pi_++\exp(\lambda_-)\Pi_-
=\exp(q)\bigl(\cosh q'+j\sinh q'\bigr)}.
$$

This is the **split Euler formula**, and it is the bridge between the exponential and the hyperbolic functions. In particular, for $q'=\theta$,

$$
\boxed{\; \exp(j\theta)=\cosh\theta+j\sinh\theta \;}.
$$

Both eigenvalues of $\exp Q$ are positive, $\exp(\lambda_\pm)>0$, so the image lies in the set $\{\lambda_+>0,\ \lambda_->0\}$, the future cone $F=\{Q:q>\lvert q'\rvert\}$.

### The Kernel and the Image

The exponential is injective. In the spectral form, $\exp(Q_1)=\exp(Q_2)$ forces $\exp(\lambda_{1+})=\exp(\lambda_{2+})$ and $\exp(\lambda_{1-})=\exp(\lambda_{2-})$, hence $\lambda_{1\pm}=\lambda_{2\pm}$ and $Q_1=Q_2$. There is no period to quotient out.

| Quantity | Value |
|---|---|
| Kernel | $\ker\exp=\{0\}$ |
| Image | the future cone $F=\{Q:\lambda_+>0,\ \lambda_->0\}=\{Q:q>\lvert q'\rvert\}$ |
| Periods | none |
| Injective | yes |
| Surjective onto the image | yes |

The exponential is therefore an isomorphism from $(\mathbb{D},+)$ onto $(F,\cdot)$.

### Properties

| Property | Statement |
|---|---|
| Multiplicativity | $\exp(Q_1+Q_2)=\exp(Q_1)\exp(Q_2)$ for all $Q_1,Q_2$ |
| Non-vanishing | $\exp(Q)\neq0$ for every $Q$ |
| Norm | $\langle\exp Q\rangle_{*}=\exp(2q)>0$ |
| Derivative | $d\exp_Q(H)=\exp(Q)H$ |
| Injective | yes, with kernel $\{0\}$ |
| Periods | none |

The norm row uses the split-complex norm $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2$.

## The Logarithm

### Definition

A **logarithm** of $Q\in\mathbb{D}$ is an element $Q_{\log}$ with $\exp(Q_{\log})=Q$. The exponential is injective (§*The Kernel and the Image*), so a logarithm is unique when it exists; the only question is its domain. Throughout, $\log$ applied to a positive real number is the ordinary real logarithm.

Write the unknown logarithm with the coefficient convention,

$$
Q_{\log}=q_{\log}+jq'_{\log},
\qquad q_{\log}=\operatorname{Re}Q_{\log}, \quad q'_{\log}=\operatorname{Im}Q_{\log}.
$$

The subscript is a label, not an operation: $q_{\log}$ is the real coordinate of $Q_{\log}$, not the logarithm of $q$.

### The Scalar Part

Let $Q_{\log}=q_{\log}+jq'_{\log}$ be a logarithm of $Q$. Taking norms in $\exp(Q_{\log})=Q$ gives
$$
\langle Q\rangle_{*}=\langle\exp Q_{\log}\rangle_{*}=\exp(2q_{\log}),
$$
so the scalar part is fixed by the norm,
$$
q_{\log}=\tfrac12\ln(\lambda_+\lambda_-),
$$
and the split coefficient $q'_{\log}$ is the hyperbolic angle, computed in §*The Eigenvalue Formula*.

### The Eigenvalue Formula

In the eigenvalue coordinates the exponential is diagonal, so $\exp(Q_{\log})=Q$ is the pair of real equations

$$
\exp\bigl(q_{\log}+q'_{\log}\bigr)=\lambda_+,
\qquad
\exp\bigl(q_{\log}-q'_{\log}\bigr)=\lambda_-,
$$

where $\lambda_\pm=q\pm q'$ are the eigenvalues of $Q$. Both left sides are positive, so a solution exists exactly when $\lambda_+>0$ and $\lambda_->0$. When it exists it is unique, because the two real exponentials are injective. Subtracting the two equations gives the split coordinate,
$$
q'_{\log}=\tfrac12\ln\frac{\lambda_+}{\lambda_-},
$$
and §*The Scalar Part* gives $q_{\log}$. The logarithm is

$$
\boxed{\; \log Q=\tfrac12\ln(\lambda_+\lambda_-)+\tfrac12 j\ln\frac{\lambda_+}{\lambda_-}
=\frac{1}{2}\ln(q^2-q'^2)+\frac{j}{2}\ln\left(\frac{q+q'}{q-q'}\right) \;},
$$

and in the idempotent basis it is the single line

$$
\log Q=\log(\lambda_+)\Pi_++\log(\lambda_-)\Pi_-.
$$

### The Coordinates of a Logarithm

The two coordinates are collected in one table.

| Component | Name | Value |
|---|---|---|
| $q_{\log}$ | logarithmic scale | $\tfrac12\ln(\lambda_+\lambda_-)=\tfrac12\ln(q^2-q'^2)$ |
| $q'_{\log}$ | hyperbolic angle | $\tfrac12\ln\dfrac{\lambda_+}{\lambda_-}=\operatorname{artanh}\dfrac{q'}{q}=\tfrac12\ln\dfrac{q+q'}{q-q'}$ |

**Example.** Take $Q=5+3j$. Then $\langle Q\rangle_{*}=25-9=16$ and $q_{\log}=\tfrac12\ln16=\ln4=1.3862944$. The ratio is $q'/q=3/5=0.6$, so $q'_{\log}=\operatorname{artanh}0.6=\tfrac12\ln\frac{1.6}{0.4}=\ln 2=0.6931472$. The logarithm is $Q_{\log}=1.3862944+0.6931472\,j$, and $4(\cosh\ln2+j\sinh\ln2)=4(1.25+0.75j)=5+3j$.

### The Domain and the Fibre

The domain is the future cone

$$
\operatorname{dom}\log = \{Q = q+jq' : q > |q'|\} = \{Q : \lambda_+ > 0,\ \lambda_- > 0\},
$$

which is exactly the image of the exponential.

| Quantity | Value |
|---|---|
| Domain | the future cone $F=\{Q:q>\lvert q'\rvert\}=\{\lambda_+>0,\ \lambda_->0\}$ |
| Fibre over a point | one point |
| Kernel | $\ker\exp=\{0\}$ |
| Principal domain | $F$, the whole domain, with a single branch |
| Existence | exactly on $F$ |

The four regions of the ambient algebra are classified as follows.

| Region | Condition | Logarithm |
|---|---|---|
| future cone | $q > \lvert q'\rvert$ | exists, unique |
| past cone | $q < -\lvert q'\rvert$ | none |
| spacelike wedges | $\lvert q'\rvert > \lvert q\rvert$ | none |
| null cone | $q = \pm q'$ | none |

The past cone fails because both eigenvalues are negative. The spacelike wedges fail because $\langle Q\rangle_{*} < 0$, while every exponential has positive norm. The null cone fails because one eigenvalue is zero. There is no branch cut to remove: the boundary is the null cone, where the logarithm diverges rather than jumps. As $\lambda_-\to0^+$, for instance, $\log\lambda_-\to-\infty$ and the $j$-component of $\log Q$ tends to $+\infty$. Since the exponential is injective, the fibre over a point of $F$ is a single point.

The product identity follows at once from injectivity:

$$
\log(QB) = \log Q + \log B
$$

whenever both sides are defined, because both sides have the same exponential, $QB$, and $\exp$ is injective.

### The Principal Logarithm

On this algebra the principal logarithm is the logarithm: the exponential is injective, so a point of $F$ has exactly one logarithm and no branch is selected. The principal value is the formula of §*The Eigenvalue Formula*,

$$
\log Q=\log(\lambda_+)\Pi_++\log(\lambda_-)\Pi_-,
$$

with the ordinary real logarithm at each positive eigenvalue. It is real-analytic on $F$ and tends to $-\infty$ on the boundary. There is no cut to choose, because the boundary is the null cone and no point of $F$ lies on it; this is the sharpest difference from the reduced biquaternion and biquaternion cases, where the logarithm has a branch lattice and cut walls.

### The Principal Domain

The principal domain — the domain of the principal logarithm — is the future cone $F$ itself. The exponential maps $\mathbb{D}$ bijectively onto $F$, so $\exp:\mathbb{D}\to F$ is bijective and $\log:F\to\mathbb{D}$ is its inverse. On $F$ there is one logarithm and no branch to choose; the principal domain and the domain of the logarithm coincide.

### The Two Compositions

Both inverse identities hold exactly, with no remainder.

| Identity | Holds | Example |
|---|---|---|
| $\exp(\log Q)=Q$ | on the future cone $F$ | $Q=5+3j$ |
| $\log(\exp Q_{\log})=Q_{\log}$ | for every $Q_{\log}\in\mathbb{D}$ | $Q_{\log}=-1+0.3j$ |
| $\log(\exp Q_{\log})=Q_{\log}$ modulo the kernel | always, and there is no kernel to remove | — |

**Right inverse.** For $Q$ in the future cone and $Q_{\log}$ its logarithm, $\exp(Q_{\log})=Q$ by the construction of §*The Eigenvalue Formula*.

**Left inverse.** For every $Q_{\log}\in\mathbb{D}$,

$$
\log(\exp(Q_{\log}))=Q_{\log}.
$$

**Proof.** In the eigenvalue coordinates, $\exp(Q_{\log})$ has eigenvalues $\exp(q_{\log}\pm q'_{\log})>0$. The logarithm returns

$$
\tfrac12\ln\bigl(\exp(2q_{\log})\bigr)=q_{\log},
\qquad
\tfrac12\ln\bigl(\exp(2q'_{\log})\bigr)=q'_{\log},
$$

so it returns $Q_{\log}$. Equivalently, $\exp(\log(\exp Q_{\log}))=\exp Q_{\log}$, and $\exp$ is injective.

There is no integer to lose: the kernel of the exponential is $\{0\}$. In group language, $\exp$ is an injective homomorphism from $(\mathbb{D},+)$ to the future cone, and $\log$ is its inverse.

For instance, $Q = 5+3j$ has $Q_{\log} = \ln 4 + j\ln 2$, and $\exp(Q_{\log}) = 5+3j$. In the other direction, $Q_{\log} = -1+0.3j$ gives $Q = \exp(Q_{\log}) = 0.3845585 + 0.1120268\,j$, whose logarithm is $Q_{\log}$ again.

### The Derivative

The derivative is forced by the inverse identity.

**Inverse function theorem.** The exponential is differentiable, and its derivative at $Q_{\log}$ is multiplication by $\exp(Q_{\log})$. The derivative is invertible everywhere, because $\langle \exp(Q_{\log})\rangle_{*} = \exp(2q_{\log}) > 0$. Hence $\exp$ is a local diffeomorphism, and its local inverse $\log$ has derivative

$$
\frac{d}{dQ}\log Q = \frac{1}{\exp(Q_{\log})} = \frac{1}{Q}.
$$

The global inverse is $\log$, so this holds on the future cone.

**Idempotent check.** Since $\log Q=\log(\lambda_+)\Pi_++\log(\lambda_-)\Pi_-$ and differentiation is componentwise,

$$
\frac{d}{dQ}\log Q=\frac{1}{\lambda_+}\Pi_++\frac{1}{\lambda_-}\Pi_-=\frac{1}{Q}.
$$

The last equality is the inverse formula of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*, §*Powers, Polynomial Calculus, and the Group of Units*. Both eigenvalues are positive on the future cone, so no exceptional point occurs inside the domain.

### Summary of the Logarithm

| Case | A logarithm | Principal logarithm | Fibre |
|---|---|---|---|
| Future cone, $q>\lvert q'\rvert$ | $\log\lambda_+\Pi_++\log\lambda_-\Pi_-$, unique | the same | one point |
| Past cone, $q<-\lvert q'\rvert$ | none | none | empty |
| Spacelike wedges, $\lvert q'\rvert>\lvert q\rvert$ | none | none | empty |
| Null cone, $q=\pm q'$ | none | none | empty |

## Powers and Roots

### The Power Function

For $P \in \mathbb{R}$ and $Q$ in the future cone,

$$
Q^{P} = \exp(P \log Q).
$$

This is single-valued, because $\log Q$ is unique. In the eigenvalue coordinates it is

$$
Q^P=\lambda_+^P\Pi_++\lambda_-^P\Pi_-,
\qquad
\lambda_\pm^P=\exp(P\log\lambda_\pm),
$$

the case of the Idempotent Principle for the function $x\mapsto x^P$ on the positive eigenvalues.

### Properties

| Property | Statement |
|---|---|
| Single-valued | one value for each $P\in\mathbb{R}$, because $\log Q$ is unique |
| Product law | $Q^{P_1}Q^{P_2}=Q^{P_1+P_2}$ |
| Power of a power | $(Q^P)^S=Q^{PS}$ |
| Norm | $\langle Q^P\rangle_{*}=\langle Q\rangle_{*}^{P}$ |

Both laws hold whenever the arguments stay in the future cone. The first follows because $\exp$ is a homomorphism and the exponents commute. The second follows because $\log(\exp(P\log Q))=P\log Q$ exactly; the base $Q^P$ is itself an exponential, hence lies in $F$, so its logarithm exists. This is the sharpest contrast with the complex case, where the same laws hold only modulo the ambiguity of the logarithm.

### The Roots

For $n\geq1$, a **root** of $Q$ is an element $R$ with $R^n=Q$.

**Theorem (the roots).** Let $n\ge1$ and let $Q\in\mathbb{D}$.

1. If $n$ is odd, there is exactly one root.
2. If $n$ is even and both eigenvalues are positive, there are exactly four roots.
3. If $n$ is even, exactly one eigenvalue is zero and the other is positive, there are exactly two roots.
4. If $n$ is even and both eigenvalues are zero, there is exactly one root, $R=0$.
5. If $n$ is even and at least one eigenvalue is negative, there is none.

*Proof.* In the eigenvalue coordinates the equation is the pair $r_+^n=\lambda_+$ and $r_-^n=\lambda_-$. A real $n$-th root is unique for odd $n$, two for a positive eigenvalue and even $n$, none for a negative eigenvalue and even $n$, and unique for the eigenvalue $0$. The two equations are independent, so the counts multiply.

| Case | Condition on $\lambda_\pm$ | Number of roots |
|---|---|---|
| $n$ odd | none | $1$ |
| $n$ even | $\lambda_+>0$, $\lambda_->0$ | $4$ |
| $n$ even | one eigenvalue $0$, the other $>0$ | $2$ |
| $n$ even | $\lambda_+=\lambda_-=0$ | $1$ |
| $n$ even | at least one eigenvalue $<0$ | $0$ |

For odd $n$ the unique root is $R=\lambda_+^{1/n}\Pi_++\lambda_-^{1/n}\Pi_-$, with the real $n$-th roots. For even $n$ the roots are $R=\epsilon_+\lambda_+^{1/n}\Pi_++\epsilon_-\lambda_-^{1/n}\Pi_-$ with $\epsilon_\pm\in\{\pm1\}$ allowed exactly where the corresponding eigenvalue is positive. For example $R^2=1$ has the four roots $\pm1,\pm j$, while $R^2=j$ has none, because the eigenvalue $\lambda_-=-1$ has no real square root; and $R^3=j$ has the unique root $j$.

## The Trigonometric and Hyperbolic Functions

In $\mathbb{D}$ the square of the imaginary unit is $+1$, so the exponential of $j\theta$ is hyperbolic, $\exp(j\theta)=\cosh\theta+j\sinh\theta$. The hyperbolic pair is the intrinsic family of the algebra and plays the role that the sine and cosine play in the complex and reduced biquaternion cases. The circular pair is defined by the same real power series; its periodic geometry is the geometry of the complexified direction, and it is included in the tables for comparison with the neighbouring cases. Both pairs are entire, and both are read at the two eigenvalues by the Idempotent Principle.

### Definitions

The four functions are defined by the real power series

$$
\sin Q=\sum_{n\geq0}\frac{(-1)^nQ^{2n+1}}{(2n+1)!},
\qquad
\cos Q=\sum_{n\geq0}\frac{(-1)^nQ^{2n}}{(2n)!},
$$

$$
\sinh Q=\sum_{n\geq0}\frac{Q^{2n+1}}{(2n+1)!},
\qquad
\cosh Q=\sum_{n\geq0}\frac{Q^{2n}}{(2n)!}.
$$

The hyperbolic pair satisfies

$$
\frac{d}{dQ}\sinh Q=\cosh Q,\qquad \frac{d}{dQ}\cosh Q=\sinh Q,
\qquad
\cosh^2Q-\sinh^2Q=1,
$$

and the circular pair satisfies the identities of the complex case with the signs of the sine and cosine series. The quotient functions are defined in §*The Other Functions*.

### The Closed Forms

By the Idempotent Principle applied to the power series,

$$
\sin Q=\sin(\lambda_+)\Pi_++\sin(\lambda_-)\Pi_-,
\qquad
\cos Q=\cos(\lambda_+)\Pi_++\cos(\lambda_-)\Pi_-,
$$

$$
\sinh Q=\sinh(\lambda_+)\Pi_++\sinh(\lambda_-)\Pi_-,
\qquad
\cosh Q=\cosh(\lambda_+)\Pi_++\cosh(\lambda_-)\Pi_-.
$$

In the basis $1,j$ the same values are the following.

| Function | Spectral form | Coefficient form |
|---|---|---|
| $\sin Q$ | $\sin(\lambda_+)\Pi_++\sin(\lambda_-)\Pi_-$ | $\sin q\cos q'+j\cos q\sin q'$ |
| $\cos Q$ | $\cos(\lambda_+)\Pi_++\cos(\lambda_-)\Pi_-$ | $\cos q\cos q'-j\sin q\sin q'$ |
| $\sinh Q$ | $\sinh(\lambda_+)\Pi_++\sinh(\lambda_-)\Pi_-$ | $\sinh q\cosh q'+j\cosh q\sinh q'$ |
| $\cosh Q$ | $\cosh(\lambda_+)\Pi_++\cosh(\lambda_-)\Pi_-$ | $\cosh q\cosh q'+j\sinh q\sinh q'$ |

The hyperbolic rows are the intrinsic reading: they pair the real hyperbolic functions of $q$ with those of $q'$. The circular rows pair the real trigonometric functions of the two coordinates; they are the ordinary circular pair of the algebra, not the exponential of a multiple of $j$.

### Identities, Periods and Zeros

| Property | Statement |
|---|---|
| Pythagorean | $\sin^{2}Q+\cos^{2}Q=1$, $\cosh^{2}Q-\sinh^{2}Q=1$ |
| Addition | $\sin(Q_1+Q_2)=\sin Q_1\cos Q_2+\cos Q_1\sin Q_2$, $\cos(Q_1+Q_2)=\cos Q_1\cos Q_2-\sin Q_1\sin Q_2$ |
| Hyperbolic addition | $\sinh(Q_1+Q_2)=\sinh Q_1\cosh Q_2+\cosh Q_1\sinh Q_2$, $\cosh(Q_1+Q_2)=\cosh Q_1\cosh Q_2+\sinh Q_1\sinh Q_2$ |
| Double angle | $\sin(2Q)=2\sin Q\cos Q$, $\cos(2Q)=\cos^{2}Q-\sin^{2}Q$, $\sinh(2Q)=2\sinh Q\cosh Q$, $\cosh(2Q)=\cosh^{2}Q+\sinh^{2}Q$ |
| Rotation | $\sin(j\theta)=j\sin\theta$, $\cos(j\theta)=\cos\theta$, $\sinh(j\theta)=j\sinh\theta$, $\cosh(j\theta)=\cosh\theta$ |
| Period of $\sin,\cos$ | $\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j)=\{a+jb:a\pm b\in2\pi\mathbb{Z}\}$ |
| Period of $\sinh,\cosh$ | none |
| Zeros of $\sin$ | $\lambda_+\in\pi\mathbb{Z}$ and $\lambda_-\in\pi\mathbb{Z}$ |
| Zeros of $\cos$ | $\lambda_+\in\frac{\pi}{2}+\pi\mathbb{Z}$ and $\lambda_-\in\frac{\pi}{2}+\pi\mathbb{Z}$ |
| Zeros of $\sinh$ | $Q=0$ |
| Zeros of $\cosh$ | none |
| Zero divisors of $\sin$ | $\lambda_+\in\pi\mathbb{Z}$ or $\lambda_-\in\pi\mathbb{Z}$ |
| Zero divisors of $\cos$ | $\lambda_+\in\frac{\pi}{2}+\pi\mathbb{Z}$ or $\lambda_-\in\frac{\pi}{2}+\pi\mathbb{Z}$ |
| Zero divisors of $\sinh$ | $\lambda_+=0$ or $\lambda_-=0$, the null cone |
| Zero divisors of $\cosh$ | none |
| Boundedness | $\sin$ and $\cos$ are bounded; $\sinh$ and $\cosh$ are unbounded |

The addition formulas hold for all arguments because the algebra is commutative; there is no ordering correction. The zeros and the zero divisors are read in the eigenvalues: an equality requires both eigenvalue equations, while a zero divisor requires only one. This is why the null cone is the zero-divisor set of $\sinh$ and not its zero set; the only zero of $\sinh$ is $Q=0$.

### The Other Functions

$$
\tan Q=\frac{\sin Q}{\cos Q},\qquad
\cot Q=\frac{\cos Q}{\sin Q},\qquad
\tanh Q=\frac{\sinh Q}{\cosh Q},\qquad
\coth Q=\frac{\cosh Q}{\sinh Q},
$$

$$
\sec Q=\frac{1}{\cos Q},\qquad
\csc Q=\frac{1}{\sin Q},\qquad
\operatorname{sech}Q=\frac{1}{\cosh Q},\qquad
\operatorname{csch}Q=\frac{1}{\sinh Q}.
$$

They are defined wherever the denominator is a unit. The eigenvalues of $\cosh Q$ are $\cosh\lambda_\pm\geq1$, so $\cosh Q$ is a unit for every $Q$ and $\tanh$ is defined on all of $\mathbb{D}$. The eigenvalues of $\sin Q$, $\cos Q$ and $\sinh Q$ can vanish on the sets of the table, and there the corresponding quotient is undefined; for $\coth$ this is the null cone. On the intrinsic hyperbolic pair the coefficient forms are

$$
\tanh Q=\frac{\tanh q+j\tanh q'}{1+j\tanh q\tanh q'},\qquad
\coth Q=\frac{1+j\tanh q\tanh q'}{\tanh q+j\tanh q'}.
$$

### The Inverse Functions

The inverse functions are the real inverse functions read at the two eigenvalues.

| Function | Formula | Domain |
|---|---|---|
| $\operatorname{arsinh}Q$ | $\log\left(Q+\sqrt{Q^2+1}\right)$ | all $\mathbb{D}$ |
| $\operatorname{arcosh}Q$ | $\log\left(Q+\sqrt{Q^2-1}\right)$ | $\lambda_+\geq1$ and $\lambda_-\geq1$ |
| $\operatorname{artanh}Q$ | $\dfrac{1}{2}\log\dfrac{1+Q}{1-Q}$ | $\lvert\lambda_+\rvert<1$ and $\lvert\lambda_-\rvert<1$ |

The square roots are the split-complex square roots of §*The Roots*, with the non-negative root in each eigenvalue. In each row the argument of the logarithm has positive eigenvalues: for $\operatorname{arsinh}$, the eigenvalues are $\lambda_\pm+\sqrt{\lambda_\pm^2+1}>0$; for $\operatorname{arcosh}$, they are $\lambda_\pm+\sqrt{\lambda_\pm^2-1}>0$ when $\lambda_\pm\geq1$; for $\operatorname{artanh}$, they are $(1+\lambda_\pm)/(1-\lambda_\pm)>0$ when $\lvert\lambda_\pm\rvert<1$. The inverse functions are therefore single-valued on their domains, like the logarithm.

The circular inverses are not functions on $\mathbb{D}$: their formulas require the scalar imaginary $i$, which is not in the algebra. They belong to the complexification and are not listed.

## Relations to the Neighbouring Cases

### The Real Case

The real axis is the fixed set of the conjugation, $q'=0$. There $\lambda_+=\lambda_-=q$, the two idempotent components coincide, and every function of this article restricts to its ordinary real counterpart:

$$
\exp(q)=\exp q,\quad \log q=\ln q\ (q>0),\quad \sin(q)=\sin q,\quad \cos(q)=\cos q,
$$

$$
\sinh(q)=\sinh q,\qquad \cosh(q)=\cosh q.
$$

The restriction is the diagonal of the pair of real functions, and it is the reason the logarithm on the positive real axis is the ordinary one.

### The Complex Case

The complex case is not a subalgebra of $\mathbb{D}$: the complexification $\mathbb{D}\otimes\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ is the algebra of the reduced biquaternions, where the same spectral formulas are read with two complex eigenvalues (*Reduced Biquaternion Elementary Functions*, §*Relations to the Neighbouring Cases*). The exponential, the logarithm, the powers and the four functions have the same eigenvalue formulas there; the difference is that the two eigenvalues are independent complex numbers, so the logarithm acquires the lattice $2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)$ and the powers acquire the matching ambiguity.

### The Relation Between the Two

The real case is the fixed set of the conjugation inside $\mathbb{D}$; the complex case is the scalar extension. The two are the two ends of the comparison table of §*Summary*: the real eigenvalues are the diagonal of the complex pair, and the reduced biquaternion formulas reduce to the split-complex ones when both eigenvalues are real.

## Summary

Every elementary function of a split-complex variable is a pair of ordinary real functions of the two eigenvalues $\lambda_+=q+q'$ and $\lambda_-=q-q'$, written in the idempotent basis. The exponential is injective, its kernel is $\{0\}$, and its image is the future cone $F=\{\lambda_\pm>0\}=\{q>\lvert q'\rvert\}$; the logarithm is its two-sided inverse on $F$, with no branch and no period. The powers are $Q^P=\exp(P\log Q)$ on $F$ for real $P$, single-valued because the logarithm is unique, and the roots are counted by the signs of the two eigenvalues. The hyperbolic functions are the intrinsic family, and the circular functions are the same power series read in the complexification. The Idempotent Principle reads every function at the two eigenvalues.

### Main Results

| Result | Statement |
|---|---|
| Regimes | distinct unit, zero divisor, scalar; the algebra is reduced, so there is no nilpotent regime |
| Spectrum | $\sigma(Q)=\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Idempotent Principle | $\Phi(Q)=\Phi(\lambda_+)\Pi_++\Phi(\lambda_-)\Pi_-$ for every real power series |
| Exponential | $\exp Q=\exp(\lambda_+)\Pi_++\exp(\lambda_-)\Pi_-=\exp q(\cosh q'+j\sinh q')$ |
| Kernel and image | $\ker\exp=\{0\}$; $\operatorname{im}\exp=F=\{q>\lvert q'\rvert\}$ |
| Logarithm | $\log Q=\log(\lambda_+)\Pi_++\log(\lambda_-)\Pi_-$ on $F$, unique |
| Principal domain | $F=\{q>\lvert q'\rvert\}$: the domain of $\log$, and $\exp$ maps onto $F$ |
| Fibre | one point over each point of $F$ |
| Derivative of the logarithm | $d\log_Q(H)=H/Q$ |
| Powers | $Q^P=\lambda_+^P\Pi_++\lambda_-^P\Pi_-$ on $F$, for $P\in\mathbb{R}$ |
| Roots | $1$ for odd $n$; $0$, $1$, $2$ or $4$ for even $n$, by the signs of $\lambda_\pm$ |
| Trigonometric functions | $\sin Q=\sin(\lambda_+)\Pi_++\sin(\lambda_-)\Pi_-$; $\cos Q=\cos(\lambda_+)\Pi_++\cos(\lambda_-)\Pi_-$ |
| Hyperbolic functions | $\sinh Q=\sinh(\lambda_+)\Pi_++\sinh(\lambda_-)\Pi_-$; $\cosh Q=\cosh(\lambda_+)\Pi_++\cosh(\lambda_-)\Pi_-$ |
| Identities | $\sin^2Q+\cos^2Q=1$, $\cosh^2Q-\sinh^2Q=1$, the addition and double-angle formulas |
| Periods | $\sin,\cos$: $\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j)$; $\sinh,\cosh$: none |
| Inverse functions | $\operatorname{arsinh}$, $\operatorname{arcosh}$, $\operatorname{artanh}$, read at $\lambda_\pm$ |

### Formulas

| Function | Value | Domain |
|---|---|---|
| $\exp Q$ | $\exp q(\cosh q'+j\sinh q')$ | all $\mathbb{D}$ |
| $\log Q$ | $\tfrac12\ln(q^2-q'^2)+\tfrac12 j\ln\dfrac{q+q'}{q-q'}$ | $q>\lvert q'\rvert$ |
| $Q^P$ | $\exp(P\log Q)$ | $q>\lvert q'\rvert$ |
| $\sin Q$ | $\sin q\cos q'+j\cos q\sin q'$ | all $\mathbb{D}$ |
| $\cos Q$ | $\cos q\cos q'-j\sin q\sin q'$ | all $\mathbb{D}$ |
| $\sinh Q$ | $\sinh q\cosh q'+j\cosh q\sinh q'$ | all $\mathbb{D}$ |
| $\cosh Q$ | $\cosh q\cosh q'+j\sinh q\sinh q'$ | all $\mathbb{D}$ |
| $\tan Q$ | $\sin Q/\cos Q$ | $\lambda_\pm\notin\frac{\pi}{2}+\pi\mathbb{Z}$ |
| $\cot Q$ | $\cos Q/\sin Q$ | $\lambda_\pm\notin\pi\mathbb{Z}$ |
| $\tanh Q$ | $\sinh Q/\cosh Q$ | all $\mathbb{D}$ |
| $\coth Q$ | $\cosh Q/\sinh Q$ | $q\neq\pm q'$ |
| $\operatorname{arsinh}Q$ | $\log(Q+\sqrt{Q^2+1})$ | all $\mathbb{D}$ |
| $\operatorname{arcosh}Q$ | $\log(Q+\sqrt{Q^2-1})$ | $\lambda_\pm\geq1$ |
| $\operatorname{artanh}Q$ | $\tfrac12\log\dfrac{1+Q}{1-Q}$ | $\lvert\lambda_\pm\rvert<1$ |

### Comparison with the Neighbouring Cases

The table compares the elementary functions across the three algebras; in the biquaternion column, $B^2=Q_x^2+Q_y^2+Q_z^2$, $\vec U=\vec Q/B$ and $\lambda_\pm=Q_t\pm iB$.

| Feature | Split-complex | Reduced biquaternion | Biquaternion |
|---|---|---|---|
| Algebra | $\mathbb{R}[x]/(x^2-1)\cong\mathbb{R}\times\mathbb{R}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ |
| Element | $Q=q+jq'$ | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $\tilde Q=Q_te_t+\vec Q$ |
| Eigenvalues | $\lambda_\pm=q\pm q'$ | $\lambda_1=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $\lambda_2=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | $\lambda_\pm=Q_t\pm iB$ |
| Spectral calculus | $\Phi(Q)=\Phi(\lambda_+)\Pi_++\Phi(\lambda_-)\Pi_-$ | $f(\breve Q)=f(\lambda_1)\Pi_++f(\lambda_2)\Pi_-$ | $f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-$ if $B\neq0$; truncated if $B=0$ |
| Exponential | $\exp q(\cosh q'+j\sinh q')$ | $\exp Q_{\blacktriangle}(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$ | $\exp Q_t(\cos B\,e_t+\sin B\,\vec U)$ if $B\neq0$; $\exp Q_t(e_t+\vec Q)$ if $B=0$ |
| Kernel | $\{0\}$ | $2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)$ | diagonalisable elements with eigenvalues in $2\pi i\mathbb{Z}$; not a subgroup |
| Image | $F=\{\lambda_\pm>0\}$ | $\{\lambda_1\lambda_2\neq0\}$ | $\{\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| Logarithm domain | $q>\lvert q'\rvert$ | $\lambda_1\lambda_2\neq0$ | $\langle\tilde Q\rangle_{\natural}\neq0$ |
| Logarithm | $\log\lambda_+\Pi_++\log\lambda_-\Pi_-$ | $\log\lambda_1\Pi_++\log\lambda_2\Pi_-$ | $\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-$, $\mu_\pm=\operatorname{Log}\lambda_\pm+2\pi i k_\pm$; Jordan formula if $B=0$ |
| Powers | $Q^P=\lambda_+^P\Pi_++\lambda_-^P\Pi_-$, $P\in\mathbb{R}$, single-valued | $\breve Q^s=\lambda_1^s\Pi_++\lambda_2^s\Pi_-$, multivalued for non-integer $s$ | $\tilde Q^\alpha=\exp(\alpha\operatorname{Log}\tilde Q)$, multivalued; continuous families on the scalar axis |
| Square roots | $4$, $2$, $1$ or $0$, by the signs of $\lambda_\pm$ | $4$ for a unit, $2$ for a zero divisor, $1$ for $0$ | $4$ for a generic unit, $2$ for a zero divisor or a Jordan unit, none for a nonzero nilpotent, a continuous family in the scalar case |
| Trigonometric | $\sin q\cos q'+j\cos q\sin q'$ | $\sin Q_{\blacktriangle}\cos Q_{\blacktriangledown}+j\cos Q_{\blacktriangle}\sin Q_{\blacktriangledown}$ | $\sin Q_t\cosh B\,e_t+\cos Q_t\sinh B\,\vec U$ |
| Hyperbolic | $\sinh q\cosh q'+j\cosh q\sinh q'$ | $\sinh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\cosh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}$ | $\sinh Q_t\cos B\,e_t+\cosh Q_t\sin B\,\vec U$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split-complex algebra |
| $j$ | Split imaginary unit, $j^2=+1$ |
| $Q=q+jq'$ | General split-complex number, $q=\operatorname{Re}Q$, $q'=\operatorname{Im}Q$ |
| $\lambda_\pm=q\pm q'=Q_\pm$ | Eigenvalues, equal to the idempotent coordinates |
| $\Pi_\pm=\tfrac12(1\pm j)$ | Eigenprojections, the standard idempotents |
| $\langle Q\rangle_{*}=q^2-q'^2=\lambda_+\lambda_-$ | Norm |
| $\exp(Q), \log Q$ | Split-complex exponential, logarithm |
| $Q_{\log}=q_{\log}+jq'_{\log}$ | A logarithm of $Q$, with $q_{\log}=\tfrac12\ln(\lambda_+\lambda_-)$ and $q'_{\log}=\tfrac12\ln(\lambda_+/\lambda_-)$ |
| $Q^P=\exp(P\log Q)$, $P\in\mathbb{R}$ | Split-complex power |
| $R$ | A root, $R^n=Q$ |
| $\sin Q, \cos Q, \tan Q, \cot Q$ | Split circular functions |
| $\sec Q, \csc Q$ | Split reciprocal circular functions |
| $\sinh Q, \cosh Q, \tanh Q, \coth Q$ | Split hyperbolic functions |
| $\operatorname{sech}Q, \operatorname{csch}Q$ | Split reciprocal hyperbolic functions |
| $\operatorname{arsinh}Q, \operatorname{arcosh}Q, \operatorname{artanh}Q$ | Split inverse hyperbolic functions |
| $\Phi(Q)=\Phi(\lambda_+)\Pi_++\Phi(\lambda_-)\Pi_-$ | Idempotent Principle for a real power series $\Phi$ |
| $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ | Eigenvalue decomposition |
| $\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j)$ | Period lattice of $\sin$ and $\cos$ |

## Further Reading

- [Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the eigenvalue decomposition and the idempotent basis used throughout.
- [Split-Complex Higher Special Functions](split-complex-higher-special-functions.html), for the Gamma, Beta, error, Airy, Bessel, hypergeometric and Lambert $W$ functions.
- [Split-Complex Exponential and Lie Group Structure](split-complex-exponential-and-lie-group-structure.html), for the group reading of the exponential and the logarithm.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split-complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.
