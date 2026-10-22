# __Split-Complex Elementary Functions__

## Introduction

This article defines the elementary functions of a split-complex variable: the exponential, the logarithm, the powers and roots, and the hyperbolic functions, which are the analogue of the trigonometric functions in this algebra. Each function is defined once, its basic properties are recorded, and its value is read on the two eigenvalues.

The spectral data are those of *Eigenvalue Decomposition of a Split-Complex Number*: the eigenvalues $\lambda_+=q+q'=Q_+$ and $\lambda_-=q-q'=Q_-$, the eigenprojections $\Pi_\pm=\tfrac12(1\pm j)$, the decomposition $Q=\lambda_+\Pi_++\lambda_-\Pi_-$, and the polynomial calculus $f(Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-$ of §*Powers, Polynomial Calculus, and the Group of Units*. That article owns these results, and this article uses them without proof. The idempotent coordinates and the eigenvalues are the same two numbers; this article writes $\lambda_\pm$ whenever the number is read as a value at an idempotent. The algebra, its basis and its conjugation are those of *Split-Complex Algebra*; the norm and the group of units are those of *Split-Complex Norm and Invertibility*; the idempotents are those of *Split-Complex Idempotents and Projections*.

This article owns the exponential and the logarithm, with their domains, their inverses and their derivatives, the power and root functions, and the hyperbolic functions. The higher special functions — the Gamma and Beta functions, the error function, the Airy and Bessel functions, the hypergeometric function and the Lambert $W$ function — are *Split-Complex Higher Special Functions*, which quotes the Idempotent Principle stated here. *Exponential Polar Decomposition of Split-Complex Numbers* cites the exponential and the logarithm and does not derive them. The polar decompositions themselves, the Lie group structure and the harmonic analysis are later articles; this one does not treat them.

**Placement.** The article is in the Analysis group of the Split-Complex Numbers category, after *Split-Complex Analysis* and *Split-Complex Integration*, and before *Split-Complex Higher Special Functions*, *Split-Complex Harmonic Analysis* and *Split-Complex Exponential and Lie Group Structure*.

**Plan.** The spectral setting is recalled first, with the two regimes and the Idempotent Principle (§*The Spectral Setting*). The exponential and the logarithm follow, with their kernels, images and fibres (§*The Exponential*, §*The Logarithm*); the powers and roots follow from the logarithm (§*Powers and Roots*); the hyperbolic functions and their inverses follow (§*The Trigonometric and Hyperbolic Functions*); the restriction to the real axis closes the theory (§*Relations to the Real Case*). The results are collected in tables in §*Summary*.

Every numerical value displayed below was recomputed in double precision.

## The Spectral Setting

### The Eigenvalue Data

The split-complex algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)=\mathbb{R}[j]$, with $j^2=+1$. A general element is $Q=q+jq'$, with $q,q'\in\mathbb{R}$. Its eigenvalues, eigenprojections and eigenvalue decomposition are

$$
\lambda_+=q+q'=Q_+,\qquad \lambda_-=q-q'=Q_-,
\qquad
\Pi_+=\frac{1+j}{2},\quad \Pi_-=\frac{1-j}{2},
\qquad
Q=\lambda_+\Pi_++\lambda_-\Pi_-.
$$

These are *Eigenvalue Decomposition of a Split-Complex Number*, §*The Spectrum and the Characteristic Polynomial* and §*The Eigenprojections*. The pair $(\Pi_+,\Pi_-)$ is the only nontrivial pair of complementary orthogonal idempotents, each is primitive, and both are central because the algebra is commutative. The characteristic polynomial and the norm are

$$
p_Q(X)=X^2-2qX+\langle Q\rangle_{*}=(X-\lambda_+)(X-\lambda_-),
\qquad
\langle Q\rangle_{*}=q^2-q'^2=\lambda_+\lambda_-.
$$

The element is a unit exactly when $\langle Q\rangle_{*}\neq0$, that is exactly when both eigenvalues are nonzero (*Split-Complex Norm and Invertibility*).

### The Regimes

The algebra has two regimes, read from the discriminant $4q'^2$ of the characteristic polynomial.

| Regime | Condition | Spectrum | Subalgebra | Eigenprojections |
|---|---|---|---|---|
| Distinct | $q'\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | $\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-\cong\mathbb{R}\times\mathbb{R}$ | $\Pi_\pm$ are the eigenprojections |
| Scalar | $q'=0$ | $\{q\}$, repeated | $\mathbb{R}[Q]=\mathbb{R}$ | the refinement $Q=q\Pi_++q\Pi_-$ is available |

The algebra is reduced: the only nilpotent is $0$ (*The Specificities of the Split-Complex Algebra*). There is therefore no nilpotent regime, and the scalar regime is the only degeneration. In the scalar regime the eigenvalue decomposition has one term, and the two-term writing is a non-unique refinement; the functions below are unaffected, because their spectral form is continuous in $\lambda_\pm$.

### The Idempotent Principle

Every elementary function of this article, and every higher special function of *Split-Complex Higher Special Functions*, is read on the two eigenvalues. The rule is stated once.

**Theorem (Idempotent Principle).** Let $\Phi(x)=\sum_{n\geq0}c_nx^n$ be a real power series with radius of convergence $\rho$, and let $Q\in\mathbb{D}$ have eigenvalues $\lambda_\pm$ with $\lvert\lambda_\pm\rvert<\rho$. Then the series $\sum c_nQ^n$ converges and

$$
\Phi(Q)=\Phi(\lambda_+)\Pi_++\Phi(\lambda_-)\Pi_-.
$$

For a function defined by an integral, an inverse or another real formula, the same display is the definition of its split-complex extension: the formula is applied to the two eigenvalues, and the value is defined exactly when the real formula is defined at both $\lambda_\pm$.

**Proof.** The eigenvalue article gives $Q^n=\lambda_+^n\Pi_++\lambda_-^n\Pi_-$ for every $n\geq0$, with $\Pi_\pm$ orthogonal idempotents and $\Pi_++\Pi_-=1$ (§*Powers, Polynomial Calculus, and the Group of Units*). Summing termwise,

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

### The Spectral Form

By the Idempotent Principle applied to the exponential series,

$$
\exp(Q)=\exp(\lambda_+)\Pi_++\exp(\lambda_-)\Pi_-
=\exp(q)\bigl(\cosh q'+j\sinh q'\bigr).
$$

This is the **split Euler formula**, and it is the bridge between the exponential and the hyperbolic functions. In particular, for $q'=\theta$,

$$
\exp(j\theta)=\cosh\theta+j\sinh\theta.
$$

Both eigenvalues of $\exp Q$ are positive, $\exp(\lambda_\pm)>0$, so the image lies in the set $\{\lambda_+>0,\ \lambda_->0\}$, the future cone $F=\{Q:q>\lvert q'\rvert\}$.

### The Kernel and the Image

The exponential is injective. In the spectral form, $\exp(Q_1)=\exp(Q_2)$ forces $\exp(\lambda_{1+})=\exp(\lambda_{2+})$ and $\exp(\lambda_{1-})=\exp(\lambda_{2-})$, hence $\lambda_{1\pm}=\lambda_{2\pm}$ and $Q_1=Q_2$. There is no period to quotient out.

| Quantity | Value |
|---|---|
| Kernel | $\ker\exp=\{0\}$ |
| Image | the future cone $F=\{Q:\lambda_+>0,\ \lambda_->0\}=\{Q:q>\lvert q'\rvert\}$ |
| Inverse | the logarithm, defined exactly on $F$ |
| Period | none |

The exponential is therefore an isomorphism from $(\mathbb{D},+)$ onto $(F,\cdot)$.

### Properties

| Property | Statement |
|---|---|
| Multiplicativity | $\exp(Q_1+Q_2)=\exp(Q_1)\exp(Q_2)$ for all $Q_1,Q_2$ |
| Non-vanishing | $\exp(Q)\neq0$ for every $Q$ |
| Norm | $\langle\exp Q\rangle_{*}=\exp(2q)>0$ |
| Derivative | $d\exp_Q(H)=\exp(Q)H$ |
| Injectivity | injective, with kernel $\{0\}$ |
| Image | the future cone $F$ |

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

### The Eigenvalue Formula

In the eigenvalue coordinates the exponential is diagonal, so $\exp(Q_{\log})=Q$ is the pair of real equations

$$
\exp\bigl(q_{\log}+q'_{\log}\bigr)=\lambda_+,
\qquad
\exp\bigl(q_{\log}-q'_{\log}\bigr)=\lambda_-,
$$

where $\lambda_\pm=q\pm q'$ are the eigenvalues of $Q$. Both left sides are positive, so a solution exists exactly when $\lambda_+>0$ and $\lambda_->0$. When it exists it is unique, because the two real exponentials are injective, and its coordinates are

| coordinate | formula |
|---|---|
| $q_{\log}$ | $\tfrac12\ln(\lambda_+\lambda_-)=\tfrac12\ln(q^2-q'^2)$ |
| $q'_{\log}$ | $\tfrac12\ln\dfrac{\lambda_+}{\lambda_-}=\operatorname{artanh}\dfrac{q'}{q}=\tfrac12\ln\dfrac{q+q'}{q-q'}$ |

The logarithm is

$$
\log Q=\tfrac12\ln(\lambda_+\lambda_-)+\tfrac12 j\ln\frac{\lambda_+}{\lambda_-}
=\frac{1}{2}\ln(q^2-q'^2)+\frac{j}{2}\ln\left(\frac{q+q'}{q-q'}\right),
$$

and in the idempotent basis it is the single line

$$
\log Q=\log(\lambda_+)\Pi_++\log(\lambda_-)\Pi_-.
$$

**Example.** Take $Q=5+3j$. Then $\langle Q\rangle_{*}=25-9=16$ and $q_{\log}=\tfrac12\ln16=\ln4=1.3862944$. The ratio is $q'/q=3/5=0.6$, so $q'_{\log}=\operatorname{artanh}0.6=\tfrac12\ln\frac{1.6}{0.4}=\ln 2=0.6931472$. The logarithm is $Q_{\log}=1.3862944+0.6931472\,j$, and $4(\cosh\ln2+j\sinh\ln2)=4(1.25+0.75j)=5+3j$.

### The Domain and the Fibre

The domain is the future cone

$$
\operatorname{dom}\log = \{Q = q+jq' : q > |q'|\} = \{Q : \lambda_+ > 0,\ \lambda_- > 0\},
$$

which is exactly the image of the exponential.

| region | condition | logarithm |
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

### The Two Compositions

Both inverse identities hold exactly, with no remainder.

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

The last equality is the inverse formula of *Eigenvalue Decomposition of a Split-Complex Number*, §*Powers, Polynomial Calculus, and the Group of Units*. Both eigenvalues are positive on the future cone, so no exceptional point occurs inside the domain.

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

the case of the Idempotent Principle for the function $x\mapsto x^P$ on the positive eigenvalues. The usual laws hold whenever the arguments stay in the domain:

$$
Q^{P_1} Q^{P_2} = Q^{P_1+P_2}, \qquad (Q^P)^S = Q^{PS}.
$$

The first follows because $\exp$ is a homomorphism and the exponents commute. The second follows because $\log(\exp(P\log Q)) = P\log Q$ exactly; the base $Q^P$ is itself an exponential, hence lies in the future cone, so its logarithm exists. This is the sharpest contrast with the complex case, where the same laws hold only modulo the ambiguity of the logarithm.

### The Roots

For $n\geq1$, a **root** of $Q$ is an element $R$ with $R^n=Q$. In the eigenvalue coordinates the equation is the pair $r_+^n=\lambda_+$ and $r_-^n=\lambda_-$, and the two real equations are independent.

| $n$ | condition on $\lambda_\pm$ | number of roots |
|---|---|---|
| odd | none | $1$ |
| even | $\lambda_+>0$, $\lambda_->0$ | $4$ |
| even | one eigenvalue $0$, the other $>0$ | $2$ |
| even | $\lambda_+=\lambda_-=0$ | $1$ |
| even | at least one eigenvalue $<0$ | $0$ |

For odd $n$ the unique root is $R=\lambda_+^{1/n}\Pi_++\lambda_-^{1/n}\Pi_-$, with the real $n$-th roots. For even $n$ the roots are $R=\epsilon_+\lambda_+^{1/n}\Pi_++\epsilon_-\lambda_-^{1/n}\Pi_-$ with $\epsilon_\pm\in\{\pm1\}$ allowed exactly where the corresponding eigenvalue is positive. For example $R^2=1$ has the four roots $\pm1,\pm j$, while $R^2=j$ has none, because the eigenvalue $\lambda_-=-1$ has no real square root; and $R^3=j$ has the unique root $j$.

## The Trigonometric and Hyperbolic Functions

In $\mathbb{D}$ the square of the imaginary unit is $+1$, so the exponential of $j\theta$ is hyperbolic, $\exp(j\theta)=\cosh\theta+j\sinh\theta$. The trigonometric analogue of the algebra is therefore the hyperbolic family, which plays the role that the sine and cosine play in the complex and reduced biquaternion cases; the circular functions are not the primary family here; their periodic geometry belongs to the complexification.

### Definitions

The **split hyperbolic sine** and **cosine** are defined by

$$
\sinh Q = \frac{\exp(Q) - \exp(-Q)}{2}, \qquad \cosh Q = \frac{\exp(Q) + \exp(-Q)}{2}.
$$

They are entire, and they satisfy

$$
\frac{d}{dQ}\sinh Q = \cosh Q, \qquad \frac{d}{dQ}\cosh Q = \sinh Q,
\qquad
\cosh^2 Q - \sinh^2 Q = 1.
$$

### The Closed Forms

By the Idempotent Principle applied to the power series,

$$
\sinh Q=\sinh(\lambda_+)\Pi_++\sinh(\lambda_-)\Pi_-,
\qquad
\cosh Q=\cosh(\lambda_+)\Pi_++\cosh(\lambda_-)\Pi_-.
$$

In the basis $1,j$ the same values are the following.

| Function | Spectral form | Coefficient form |
|---|---|---|
| $\sinh Q$ | $\sinh(\lambda_+)\Pi_++\sinh(\lambda_-)\Pi_-$ | $\sinh q\cosh q'+j\cosh q\sinh q'$ |
| $\cosh Q$ | $\cosh(\lambda_+)\Pi_++\cosh(\lambda_-)\Pi_-$ | $\cosh q\cosh q'+j\sinh q\sinh q'$ |
| $\tanh Q$ | $\dfrac{\sinh Q}{\cosh Q}$ | $\dfrac{\tanh q+j\tanh q'}{1+j\tanh q\tanh q'}$ |
| $\coth Q$ | $\dfrac{\cosh Q}{\sinh Q}$ | $\dfrac{1+j\tanh q\tanh q'}{\tanh q+j\tanh q'}$ |

So the split hyperbolic functions are pairs of ordinary real hyperbolic functions at the eigenvalues.

### Identities, Periods and Zeros

| Property | Statement |
|---|---|
| Pythagorean | $\cosh^2Q-\sinh^2Q=1$ |
| Addition | $\sinh(Q_1+Q_2)=\sinh Q_1\cosh Q_2+\cosh Q_1\sinh Q_2$ for all $Q_1,Q_2$ |
| Double angle | $\sinh(2Q)=2\sinh Q\cosh Q$, $\cosh(2Q)=\cosh^2Q+\sinh^2Q$ |
| Period | none; the real hyperbolic functions are not periodic |
| Zeros of $\sinh$ | $\sinh Q=0\iff\lambda_+=0$ or $\lambda_-=0$, that is on the null cone |
| Zeros of $\cosh$ | none, since $\cosh\lambda_\pm\geq1$ |

The addition formulas hold for all arguments because the algebra is commutative; there is no ordering correction.

### The Other Functions

$$
\tanh Q = \frac{\sinh Q}{\cosh Q}, \qquad \coth Q = \frac{\cosh Q}{\sinh Q}.
$$

These are defined wherever the denominator is invertible. The eigenvalues of $\cosh Q$ are $\cosh\lambda_\pm\geq1$, so $\cosh Q$ is invertible for every $Q$ and $\tanh$ is defined on all of $\mathbb{D}$. The eigenvalues of $\sinh Q$ vanish exactly when $\lambda_+=0$ or $\lambda_-=0$, that is on the null cone; there $\coth$ is undefined.

### The Inverse Functions

The inverse functions are the real inverse functions read at the two eigenvalues.

| Function | Formula | Domain |
|---|---|---|
| $\operatorname{arsinh}Q$ | $\log\left(Q+\sqrt{Q^2+1}\right)$ | all $\mathbb{D}$ |
| $\operatorname{arcosh}Q$ | $\log\left(Q+\sqrt{Q^2-1}\right)$ | $\lambda_+\geq1$ and $\lambda_-\geq1$ |
| $\operatorname{artanh}Q$ | $\dfrac{1}{2}\log\dfrac{1+Q}{1-Q}$ | $\lvert\lambda_+\rvert<1$ and $\lvert\lambda_-\rvert<1$ |

The square roots are the split-complex square roots of §*The Roots*, with the non-negative root in each eigenvalue. In each row the argument of the logarithm has positive eigenvalues: for $\operatorname{arsinh}$, the eigenvalues are $\lambda_\pm+\sqrt{\lambda_\pm^2+1}>0$; for $\operatorname{arcosh}$, they are $\lambda_\pm+\sqrt{\lambda_\pm^2-1}>0$ when $\lambda_\pm\geq1$; for $\operatorname{artanh}$, they are $(1+\lambda_\pm)/(1-\lambda_\pm)>0$ when $\lvert\lambda_\pm\rvert<1$. The inverse functions are therefore single-valued on their domains, like the logarithm.

## Relations to the Real Case

The real axis is the fixed set of the conjugation, $q'=0$. There $\lambda_+=\lambda_-=q$, the two idempotent components coincide, and every function of this article restricts to its ordinary real counterpart:

$$
\exp(q)=\exp q,\qquad \log q=\ln q\ (q>0),\qquad \sinh(q)=\sinh q,\qquad \cosh(q)=\cosh q.
$$

The complex case is not a subalgebra of $\mathbb{D}$; the complexification $\mathbb{D}\otimes\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ is the algebra of the reduced biquaternions, where the same spectral formulas are read with two complex eigenvalues (*Reduced Biquaternion Elementary Functions*, §*Relations to the Complex and Split-Complex Cases*).

## Summary

Every elementary function of a split-complex variable is a pair of ordinary real functions of the two eigenvalues $\lambda_+=q+q'$ and $\lambda_-=q-q'$, written in the idempotent basis. The exponential is injective, its kernel is $\{0\}$, and its image is the future cone $F=\{\lambda_\pm>0\}=\{q>\lvert q'\rvert\}$; the logarithm is its two-sided inverse on $F$, with no branch and no period. The powers are $Q^P=\exp(P\log Q)$ on $F$ for real $P$, single-valued because the logarithm is unique, and the roots are counted by the signs of the two eigenvalues. The hyperbolic functions are built from the exponential by the same series as in the real case, and the Idempotent Principle reads them at the two eigenvalues.

### Main Results

| Result | Statement |
|---|---|
| Spectrum | $\sigma(Q)=\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Exponential | $\exp Q=\exp(\lambda_+)\Pi_++\exp(\lambda_-)\Pi_-=\exp q(\cosh q'+j\sinh q')$ |
| Kernel and image | $\ker\exp=\{0\}$; $\operatorname{im}\exp=F=\{q>\lvert q'\rvert\}$ |
| Logarithm | $\log Q=\log(\lambda_+)\Pi_++\log(\lambda_-)\Pi_-$ on $F$, unique |
| Derivative of the logarithm | $d\log_Q(H)=H/Q$ |
| Powers | $Q^P=\lambda_+^P\Pi_++\lambda_-^P\Pi_-$ on $F$, for $P\in\mathbb{R}$ |
| Roots | $1$ for odd $n$; $0$, $1$, $2$ or $4$ for even $n$, by the signs of $\lambda_\pm$ |
| Hyperbolic functions | $\sinh Q=\sinh(\lambda_+)\Pi_++\sinh(\lambda_-)\Pi_-$; $\cosh Q=\cosh(\lambda_+)\Pi_++\cosh(\lambda_-)\Pi_-$ |
| Idempotent Principle | $\Phi(Q)=\Phi(\lambda_+)\Pi_++\Phi(\lambda_-)\Pi_-$ for every real power series |

### Formulas

| Function | Value | Domain |
|---|---|---|
| $\exp Q$ | $\exp q(\cosh q'+j\sinh q')$ | all $\mathbb{D}$ |
| $\log Q$ | $\tfrac12\ln(q^2-q'^2)+\tfrac12 j\ln\dfrac{q+q'}{q-q'}$ | $q>\lvert q'\rvert$ |
| $Q^P$ | $\exp(P\log Q)$ | $q>\lvert q'\rvert$ |
| $\sinh Q$ | $\sinh q\cosh q'+j\cosh q\sinh q'$ | all $\mathbb{D}$ |
| $\cosh Q$ | $\cosh q\cosh q'+j\sinh q\sinh q'$ | all $\mathbb{D}$ |
| $\tanh Q$ | $\sinh Q/\cosh Q$ | all $\mathbb{D}$ |
| $\coth Q$ | $\cosh Q/\sinh Q$ | $q\neq\pm q'$ |
| $\operatorname{arsinh}Q$ | $\log(Q+\sqrt{Q^2+1})$ | all $\mathbb{D}$ |
| $\operatorname{arcosh}Q$ | $\log(Q+\sqrt{Q^2-1})$ | $\lambda_\pm\geq1$ |
| $\operatorname{artanh}Q$ | $\tfrac12\log\dfrac{1+Q}{1-Q}$ | $\lvert\lambda_\pm\rvert<1$ |

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
| $\sinh Q, \cosh Q, \tanh Q, \coth Q$ | Split hyperbolic functions |
| $\operatorname{arsinh}Q, \operatorname{arcosh}Q, \operatorname{artanh}Q$ | Split inverse hyperbolic functions |
| $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ | Eigenvalue decomposition |

## Further Reading

- [Split-Complex Higher Special Functions](split-complex-higher-special-functions.html), for the Gamma, Beta, error, Airy, Bessel, hypergeometric and Lambert $W$ functions.
- [Split-Complex Exponential and Lie Group Structure](split-complex-exponential-and-lie-group-structure.html), for the group reading of the exponential and the logarithm.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split-complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.
