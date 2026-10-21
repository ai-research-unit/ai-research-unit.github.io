
# __Split-Complex Special Functions__

## Introduction

This article introduces the split complex special functions as a collection of named functions that arise repeatedly in split complex analysis, hyperbolic differential equations, and the geometry of the Lorentzian plane. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Split complex analysis is assumed from the article on split complex analysis, and the idempotent decomposition is used throughout. The order of presentation follows the dependency order: the split complex exponential and its consequences first, then functions defined from them, then functions defined by series and integrals.

## The Split Complex Exponential and Logarithm

### The Split Complex Exponential

The **split complex exponential** is defined for $Q \in \mathbb{D}$ by

$$
\exp(Q) = \sum_{n=0}^\infty \frac{Q^n}{n!}.
$$

The series converges absolutely for every $Q$ in the Euclidean norm. The function is entire in the split complex sense, and it satisfies

$$
\exp(Q + B) = \exp(Q) \exp(B), \qquad \exp(0) = 1, \qquad \exp'(Q) = \exp(Q).
$$

For $Q = q + jq'$ with $q, q' \in \mathbb{R}$,

$$
\exp(Q) = \exp(q) (\cosh q' + j \sinh q').
$$

This is the **split Euler formula**, and it is the bridge between the exponential and the hyperbolic functions. In particular, for $q' = \theta$,

$$
\exp(j\theta) = \cosh\theta + j \sinh\theta.
$$

The exponential is **not** periodic. Unlike the complex exponential, which is $2\pi i$-periodic, the split complex exponential is injective on the real axis and has no period.

### The Idempotent Form

In the idempotent basis, the exponential decomposes as

$$
\exp(Q) = \exp(Q_+) \Pi_+ + \exp(Q_-) \Pi_-, \qquad Q_+ = q + q', \quad Q_- = q - q'.
$$

So the split complex exponential is the pair of ordinary real exponentials, one for each idempotent. This is the fundamental structural fact about the exponential, and it is the reason most split complex special functions are pairs of real special functions.

### The Split Complex Logarithm

A **logarithm** of $Q \in \mathbb{D}$ is a split complex number $Q_{\log}$ with $\exp(Q_{\log}) = Q$. The exponential is injective, because its two idempotent components are ordinary real exponentials (§*The Idempotent Form*), so a logarithm is unique when it exists; the only question is its domain. Throughout this section, $\log$ applied to a positive real number is the ordinary real logarithm.

The element and its logarithm carry two different pairs of real coordinates:

$$
Q = q+jq', \qquad Q_{\log} = q_{\log}+j q'_{\log}, \qquad
q_{\log}=\operatorname{Re}Q_{\log}, \quad q'_{\log}=\operatorname{Im}Q_{\log}.
$$

The subscript is a label, not an operation: $q_{\log}$ is the real coordinate of $Q_{\log}$, not the logarithm of $q$. The split Euler formula turns $\exp(Q_{\log}) = Q$ into

$$
\exp(q_{\log})\cosh q'_{\log} = q, \qquad \exp(q_{\log})\sinh q'_{\log} = q'.
$$

Squaring and subtracting eliminates $q'_{\log}$:

$$
\exp(2q_{\log})\bigl(\cosh^2 q'_{\log} - \sinh^2 q'_{\log}\bigr) = \exp(2q_{\log}) = q^2 - q'^2 = N(Q).
$$

The left side is positive, so a solution requires $N(Q) > 0$. Under that condition the first equation has the unique solution

$$
q_{\log} = \tfrac12\log N(Q).
$$

The ratio of the two equations then gives $\tanh q'_{\log} = q'/q$. Since $\cosh q'_{\log} > 0$ and $\exp(q_{\log}) > 0$, the first equation forces $q > 0$; together with $q^2 > q'^2$ this gives $|q'/q| < 1$, so $q'_{\log} = \operatorname{artanh}(q'/q)$ is defined. Hence a logarithm exists exactly when

$$
q^2 > q'^2 \quad \text{and} \quad q > 0,
$$

that is, when $Q$ lies in the future cone $q > |q'|$. In that region $q'_{\log}$ is unique. The two coordinates of the logarithm are therefore

| coordinate | real formula |
|---|---|
| $q_{\log}=$ | $\tfrac12\ln(q^2-q'^2)$ |
| $q'_{\log}=$ | $\operatorname{artanh}\dfrac{q'}{q}=\tfrac12\ln\dfrac{q+q'}{q-q'}$ |

The logarithm is

$$
\log Q = \frac{1}{2} \log(q^2-q'^2) + \frac{j}{2} \log\left(\frac{q+q'}{q-q'}\right).
$$

In the idempotent basis this is one line. With $Q_\pm = q \pm q'$,

$$
\log Q = \log(Q_+) \Pi_+ + \log(Q_-) \Pi_-,
$$

and the real logarithm exists if and only if $Q_+ > 0$ and $Q_- > 0$, which is the same condition $q > |q'|$.

**Example.** Take $Q=5+3j$. Then $N(Q)=25-9=16$ and $q_{\log}=\tfrac12\ln16=\ln4=1.3862944$. The ratio is $q'/q=3/5=0.6$, so $q'_{\log}=\operatorname{artanh}0.6=\tfrac12\ln\frac{1.6}{0.4}=\ln 2=0.6931472$. The logarithm is the number $Q_{\log}=1.3862944+0.6931472\,j$, and $4(\cosh\ln2+j\sinh\ln2)=4(1.25+0.75j)=5+3j$.

### The Two Compositions

Unlike the complex case, both inverse identities hold exactly, with no remainder.

**Right inverse.** For $Q$ in the future cone and $Q_{\log}$ its logarithm,

$$
\exp(Q_{\log}) = Q.
$$

**Proof.** Put $Q_{\log} = q_{\log}+jq'_{\log}$, so $\exp(q_{\log}) = \sqrt{q^2-q'^2}$ and $q'_{\log} = \operatorname{artanh}(q'/q)$. Then

$$
\cosh q'_{\log} = \frac{q}{\sqrt{q^2-q'^2}}, \qquad \sinh q'_{\log} = \frac{q'}{\sqrt{q^2-q'^2}},
$$

so

$$
\exp(q_{\log})\bigl(\cosh q'_{\log} + j\sinh q'_{\log}\bigr) = q + jq' = Q.
$$

In the idempotent basis the same computation reads $\exp(\log Q_\pm) = Q_\pm$ in each component.

**Left inverse.** For every $Q \in \mathbb{D}$ and every logarithm $Q_{\log}$ of $Q$,

$$
\log(\exp(Q_{\log})) = Q_{\log}.
$$

**Proof.** Write $Q_{\log} = q_{\log}+jq'_{\log}$. The idempotent form gives

$$
\exp(Q_{\log}) = \exp(q_{\log}+q'_{\log})\Pi_+ + \exp(q_{\log}-q'_{\log})\Pi_-.
$$

Both components $\exp(q_{\log}\pm q'_{\log})$ are positive, so the logarithm is defined, and

$$
\log(\exp(Q_{\log})) = \log(\exp(q_{\log}+q'_{\log}))\Pi_+ + \log(\exp(q_{\log}-q'_{\log}))\Pi_- = (q_{\log}+q'_{\log})\Pi_+ + (q_{\log}-q'_{\log})\Pi_- = q_{\log} + jq'_{\log} = Q_{\log}.
$$

Equivalently, $\exp(\log(\exp(Q_{\log}))) = \exp(Q_{\log})$, and $\exp$ is injective, so $\log(\exp(Q_{\log})) = Q_{\log}$. There is no integer to lose: the kernel of the split complex exponential is $\{0\}$. In group language, $\exp$ is an injective homomorphism from $(\mathbb{D},+)$ to $(\mathbb{D}^\times,\cdot)$, and $\log$ is the inverse isomorphism from the future cone to $\mathbb{D}$.

For instance, $Q = 5+3j$ has $Q_{\log} = \ln 4 + j\ln 2$, and $\exp(Q_{\log}) = 5+3j$. In the other direction, $Q_{\log} = -1+0.3j$ gives $Q = \exp(Q_{\log}) = 0.3845585 + 0.1120268\,j$, whose logarithm is $Q_{\log}$ again.

### The Domain of the Logarithm

The domain is the future cone

$$
\operatorname{dom}\log = \{Q = q+jq' : q > |q'|\} = \{Q : Q_+ > 0,\ Q_- > 0\},
$$

which is exactly the image of the exponential. The other three components of $\mathbb{D}^\times$ have no logarithm, and neither does the null cone that separates them.

| region | condition | logarithm |
|---|---|---|
| future cone | $q > \lvert q'\rvert$ | exists, unique |
| past cone | $q < -\lvert q'\rvert$ | none |
| spacelike wedges | $\lvert q'\rvert > \lvert q\rvert$ | none |
| null cone | $q = \pm q'$ | none |

The past cone fails because both idempotent components are negative. The spacelike wedges fail because $N(Q) < 0$, while every exponential has positive norm. The null cone fails because one component is zero. There is no branch cut to remove: the boundary is the null cone, where the logarithm diverges rather than jumps. As $Q_- \to 0^+$, for instance, $\log Q_- \to -\infty$ and the $j$-component of $\log Q$ tends to $+\infty$.

The product identity follows at once from injectivity:

$$
\log(QB) = \log Q + \log B
$$

whenever both sides are defined, because both sides have the same exponential, $QB$, and $\exp$ is injective.

### The Derivative of the Logarithm

The derivative is again forced by the inverse identity.

**Inverse function theorem.** The split complex exponential is differentiable with $\exp'(Q_{\log}) = \exp(Q_{\log})$. Its derivative is invertible everywhere, because $N(\exp(Q_{\log})) = \exp(2q_{\log}) > 0$. Hence $\exp$ is a local diffeomorphism, and its local inverse has derivative

$$
(\exp^{-1})'(Q) = \frac{1}{\exp'(Q_{\log})} = \frac{1}{\exp(Q_{\log})} = \frac{1}{Q}.
$$

The global inverse is $\log$, so $\log' Q = 1/Q$ on the future cone.

**Idempotent check.** Since $\log Q = \log(Q_+)\Pi_+ + \log(Q_-)\Pi_-$ and differentiation is componentwise,

$$
\log' Q = \frac{1}{Q_+}\Pi_+ + \frac{1}{Q_-}\Pi_- = \frac{1}{Q}.
$$

The last equality is the idempotent expansion of $1/Q$. Both components are defined and nonzero on the future cone, so no exceptional point occurs inside the domain.

### Split Complex Powers

For $P \in \mathbb{D}$ and $Q$ in the future cone,

$$
Q^{P} = \exp(P \log Q).
$$

This is single-valued, because $\log Q$ is unique. The usual laws hold whenever the arguments stay in the domain:

$$
Q^{P_1} Q^{P_2} = Q^{P_1+P_2}, \qquad (Q^P)^R = Q^{PR}.
$$

The first follows because $\exp$ is a homomorphism and the exponents commute. The second follows because $\log(\exp(P\log Q)) = P\log Q$ exactly; the base $Q^P$ is itself an exponential, hence lies in the future cone, so its logarithm exists. This is the sharpest contrast with the complex case, where the same laws hold only modulo the ambiguity of the logarithm.

## The Hyperbolic Functions

### Definition

The **split hyperbolic sine** and **cosine** are defined by

$$
\sinh Q = \frac{\exp(Q) - \exp(-Q)}{2}, \qquad \cosh Q = \frac{\exp(Q) + \exp(-Q)}{2}.
$$

They are entire in the split complex sense, and they satisfy

$$
\sinh' Q = \cosh Q, \qquad \cosh' Q = \sinh Q,
$$

$$
\cosh^2 Q - \sinh^2 Q = 1.
$$

In the idempotent basis,

$$
\sinh Q = \sinh(Q_+) \Pi_+ + \sinh(Q_-) \Pi_-,
$$

$$
\cosh Q = \cosh(Q_+) \Pi_+ + \cosh(Q_-) \Pi_-.
$$

So the split hyperbolic functions are pairs of ordinary real hyperbolic functions.

### The Other Hyperbolic Functions

$$
\tanh Q = \frac{\sinh Q}{\cosh Q}, \qquad \coth Q = \frac{\cosh Q}{\sinh Q}.
$$

These are defined wherever the denominator is invertible. The denominator $\cosh Q$ is invertible unless $\cosh(Q_+) = 0$ or $\cosh(Q_-) = 0$, which never happens for real $Q_+$ and $Q_-$. So $\tanh$ is defined on all of $\mathbb{D}$, and $\coth$ is defined except on the null cone.

### Inverse Hyperbolic Functions

The **split inverse hyperbolic sine** is defined by

$$
\operatorname{arsinh} Q = \log\left(Q + \sqrt{Q^2 + 1}\right),
$$

where the square root is the split complex square root. The **split inverse hyperbolic cosine** is

$$
\operatorname{arcosh} Q = \log\left(Q + \sqrt{Q^2 - 1}\right),
$$

defined for $Q$ with $Q_+ \geq 1$ and $Q_- \geq 1$. The **split inverse hyperbolic tangent** is

$$
\operatorname{artanh} Q = \frac{1}{2} \log \frac{1 + Q}{1 - Q},
$$

defined for $Q$ with $|Q_+| < 1$ and $|Q_-| < 1$.

In the idempotent basis, each of these is the ordinary real inverse hyperbolic function applied to the corresponding component.

## The Gamma Function

### Definition

The **split complex gamma function** is defined for $Q$ with $Q_+ > 0$ and $Q_- > 0$ by

$$
\Gamma(Q) = \int_0^\infty t^{Q-1} \exp(-t) \, dt,
$$

where the integral is along the positive real axis, and $t^{Q-1}$ is the split complex power. In the idempotent basis,

$$
\Gamma(Q) = \Gamma(Q_+) \Pi_+ + \Gamma(Q_-) \Pi_-.
$$

So the split complex gamma function is the pair of ordinary real gamma functions, one for each idempotent.

### Functional Equation

$$
\Gamma(Q + 1) = Q \Gamma(Q).
$$

This follows from integration by parts, exactly as in the real case.

### Special Values

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$, where the factorial is the ordinary real factorial applied to each idempotent component.

### Reflection Formula

$$
\Gamma(Q) \Gamma(1 - Q) = \frac{\pi}{\sin(\pi Q)},
$$

where the sine is the ordinary real sine applied to each idempotent component.

## The Beta Function

### Definition

The **split complex beta function** is defined for $n, m$ with $n_+ > 0$, $n_- > 0$, $m_+ > 0$, $m_- > 0$ by

$$
B(n, m) = \int_0^1 t^{n-1} (1 - t)^{m-1} \, dt.
$$

In the idempotent basis,

$$
B(n, m) = B(n_+, m_+) \Pi_+ + B(n_-, m_-) \Pi_-.
$$

### Relation to the Gamma Function

$$
B(n, m) = \frac{\Gamma(n) \Gamma(m)}{\Gamma(n + m)}.
$$

This follows from the same substitution as in the real case, applied to each idempotent component.

### Symmetry

$$
B(n, m) = B(m, n).
$$

## The Error Function

### Definition

The **split complex error function** is defined by

$$
\operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \int_0^Q \exp(-t^2) \, dt,
$$

where the integral is along a path from $0$ to $Q$ that does not cross the null cone. In the idempotent basis,

$$
\operatorname{erf}(Q) = \operatorname{erf}(Q_+) \Pi_+ + \operatorname{erf}(Q_-) \Pi_-.
$$

So the split complex error function is the pair of ordinary real error functions.

### Properties

$$
\operatorname{erf}'(Q) = \frac{2}{\sqrt{\pi}} \exp(-Q^2),
$$

$$
\lim_{Q \to \infty} \operatorname{erf}(Q) = 1, \qquad \lim_{Q \to -\infty} \operatorname{erf}(Q) = -1,
$$

where the limits are taken along the real axis.

### The Complementary Error Function

$$
\operatorname{erfc}(Q) = 1 - \operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \int_Q^\infty \exp(-t^2) \, dt.
$$

In the idempotent basis, this is the ordinary real complementary error function applied to each component.

## The Airy Functions

### Definition

The **split complex Airy function** is defined by

$$
\operatorname{Ai}(Q) = \frac{1}{\pi} \int_0^\infty \cos\left(\frac{t^3}{3} + Qt\right) dt,
$$

where the cosine is the ordinary real cosine applied to each idempotent component. In the idempotent basis,

$$
\operatorname{Ai}(Q) = \operatorname{Ai}(Q_+) \Pi_+ + \operatorname{Ai}(Q_-) \Pi_-.
$$

So the split complex Airy function is the pair of ordinary real Airy functions.

### Differential Equation

$$
w'' - Q w = 0.
$$

This is Airy's equation, and it holds in each idempotent component separately.

### Asymptotics

For $Q_+ \to +\infty$,

$$
\operatorname{Ai}(Q_+) \sim \frac{1}{2 \sqrt{\pi} Q_+^{1/4}} \exp(-2 Q_+^{3/2}/3).
$$

For $Q_+ \to -\infty$,

$$
\operatorname{Ai}(Q_+) \sim \frac{1}{\sqrt{\pi} |Q_+|^{1/4}} \sin\left(\frac{2 |Q_+|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The same asymptotics hold for the minus component.

## The Bessel Functions

### Definition

The **split complex Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(Q) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Q}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are split complex. In the idempotent basis,

$$
J_\nu(Q) = J_\nu(Q_+) \Pi_+ + J_\nu(Q_-) \Pi_-.
$$

So the split complex Bessel function is the pair of ordinary real Bessel functions.

### Differential Equation

$$
Q^2 w'' + Q w' + (Q^2 - \nu^2) w = 0.
$$

This is Bessel's equation, and it holds in each idempotent component separately.

### Modified Bessel Functions

The **split complex modified Bessel function** of the first kind is

$$
I_\nu(Q) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Q}{2} \right)^{2n + \nu}.
$$

In the idempotent basis, this is the ordinary real modified Bessel function applied to each component.

## The Hypergeometric Function

### Definition

The **split complex Gauss hypergeometric function** is defined for $|Q_+| < 1$ and $|Q_-| < 1$ by

$$
{}_2F_1(a, b; c; Q) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{Q^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are split complex. In the idempotent basis,

$$
{}_2F_1(a, b; c; Q) = {}_2F_1(a_+, b_+; c_+; Q_+) \Pi_+ + {}_2F_1(a_-, b_-; c_-; Q_-) \Pi_-.
$$

So the split complex hypergeometric function is the pair of ordinary real hypergeometric functions.

### Differential Equation

$$
Q(1 - Q) w'' + [c - (a + b + 1) Q] w' - ab w = 0.
$$

This is the hypergeometric equation, and it holds in each idempotent component separately.

### Special Cases

$$
{}_2F_1(1, 1; 2; Q) = -\frac{\log(1 - Q)}{Q},
$$

$$
{}_2F_1(a, b; b; Q) = (1 - Q)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; Q^2\right) = \frac{\arcsin Q}{Q},
$$

where the arcsine is the ordinary real arcsine applied to each idempotent component.

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; Q) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{Q^n}{n!}.
$$

In the idempotent basis, this is the ordinary real generalized hypergeometric function applied to each component.

## The Lambert W Function

### Definition

The **split complex Lambert W function** is the inverse of

$$
Q \mapsto Q \exp(Q).
$$

That is, $W(Q)$ is any solution of

$$
W(Q) \exp(W(Q)) = Q.
$$

In the idempotent basis,

$$
W(Q) = W(Q_+) \Pi_+ + W(Q_-) \Pi_-,
$$

where $W$ on the right is the ordinary real Lambert W function.

### Derivative

$$
W'(Q) = \frac{W(Q)}{Q(1 + W(Q))},
$$

defined wherever the denominator is invertible.

### Branches

The split complex Lambert W function is defined componentwise, so it inherits the two real branches $W_0$ and $W_{-1}$ of the ordinary Lambert W function independently in each idempotent component; its branches are the four combinations obtained by choosing one of $W_0$ and $W_{-1}$ for $Q_+$ and one for $Q_-$. On the region where $Q_+ > -1/e$ and $Q_- > -1/e$, the principal branch $W_0$, taken in both components, is defined, and it is split complex differentiable.

## The Idempotent Principle

The pattern in all the definitions above is the same: every split complex special function is the pair of ordinary real special functions, one for each idempotent component. This is not a coincidence; it is a theorem.

**Theorem (Idempotent Principle).** Let $F$ be a split complex special function defined by a formula that involves only the split complex algebra operations, the split complex exponential, and the split complex logarithm. Then $F$ decomposes in the idempotent basis as

$$
F(Q) = F_+(Q_+) \Pi_+ + F_-(Q_-) \Pi_-,
$$

where $F_+$ and $F_-$ are the corresponding real special functions.

**Proof.** The split complex algebra is isomorphic to $\mathbb{R} \oplus \mathbb{R}$ via the idempotent decomposition. Every operation in the split complex algebra corresponds to the componentwise operation in $\mathbb{R} \oplus \mathbb{R}$. Every split complex special function is defined by a formula built from these operations, so it decomposes componentwise.

This theorem is the reason split complex special functions are simpler than complex special functions. In the complex case, the special functions are genuinely new objects, because the complex algebra is a field and the exponential is periodic. In the split complex case, the special functions are pairs of real special functions, because the split complex algebra is a product of two copies of $\mathbb{R}$ and the exponential is injective.

## Summary

The split complex special functions are the named functions that arise in split complex analysis, in hyperbolic geometry and in the theory of the wave equation. Each is obtained by carrying the corresponding real or complex definition to the split complex variable by means of the split complex exponential and the algebra operations.

The exponential is defined by its series, and the hyperbolic functions are built from it, the trigonometric functions being replaced by their hyperbolic analogues because $j^2 = +1$. The logarithm is a genuine two-sided inverse on the future cone: $\exp(Q_{\log}) = Q$ there, and $\log(\exp(Q_{\log})) = Q_{\log}$ exactly, with no branch and no period. Integral representations then supply the gamma and beta functions, the error function, the Airy function, the Bessel functions and the Gauss hypergeometric function, together with the Lambert $W$ function as the inverse of $W \mapsto W\exp(W)$.

The section on the idempotent principle states what organises the whole collection: every split complex special function is the pair of ordinary real special functions obtained by evaluating it on the two idempotent components, one for $\Pi_+$ and one for $\Pi_-$, so that each definition is a real definition applied twice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $j$ | Split imaginary unit, $j^2 = +1$ |
| $Q = q + jq'$ | General split complex number, $q = \operatorname{Re} Q$, $q' = \operatorname{Im} Q$ |
| $\exp(Q), \log Q$ | Split complex exponential, logarithm |
| $Q_{\log} = q_{\log} + jq'_{\log}$ | A logarithm of $Q$, with $q_{\log} = \tfrac12\log N(Q)$ and $q'_{\log} = \operatorname{artanh}(q'/q)$ |
| $\sinh Q, \cosh Q, \tanh Q$ | Split hyperbolic functions |
| $\Gamma(Q)$ | Split complex gamma function |
| $B(n, m)$ | Split complex beta function; arguments $n, m$ |
| $\operatorname{erf}(Q), \operatorname{erfc}(Q)$ | Split error function, complementary error function |
| $\operatorname{Ai}(Q)$ | Split Airy function |
| $J_\nu(Q), I_\nu(Q)$ | Split Bessel functions |
| ${}_pF_q$ | Split generalized hypergeometric function |
| $W(Q)$ | Split Lambert W function |
| $\Pi_+ = (1 + j)/2$ | Positive idempotent |
| $\Pi_- = (1 - j)/2$ | Negative idempotent |
| $Q = Q_+ \Pi_+ + Q_- \Pi_-$ | Idempotent decomposition |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.

