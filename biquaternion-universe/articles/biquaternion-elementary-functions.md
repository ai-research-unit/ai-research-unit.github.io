
# Biquaternion Elementary Functions

## Introduction

This article introduces the elementary functions of a biquaternion variable. It follows the basic algebra article, which defined the biquaternion algebra $\mathbb{B}$, its conjugations, and its four fixed-point subspaces. The goal is to define the exponential, the trigonometric and hyperbolic functions, the logarithm, and the power functions, and to compute them in closed form.

The treatment is purely mathematical. No physics is invoked. No examples are given. The biquaternion algebra $\mathbb{B}$ is assumed from the basic algebra article, together with its scalar-vector decomposition, its norm form, and its four conjugations.

The key structural fact is that the elementary functions of a biquaternion are determined by the **powers** of the biquaternion, and the powers simplify dramatically in two cases: when the vector part has a nonzero **complex norm**, and when the vector part is **nilpotent**. These two cases cover all possibilities, and they lead to two regimes: the **oscillatory regime** and the **nilpotent regime**. The purpose of this article is to develop the elementary functions in both regimes.

The higher special functions — Bessel, hypergeometric, gamma, zeta, and the functions arising from the analysis — are treated in the companion article on biquaternion higher special functions. The polar representations are treated in the article on biquaternion polar representations; this article uses only the Hamilton polar form, which is the one that makes the elementary functions transparent.

Throughout, a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

The scalar part is $Q_0 \in \mathbb{C}$; the vector part is $\mathbf{Q}$. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, and the norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$. The scalar imaginary is $i$, which commutes with the quaternion units.

## The Complex Norm and the Two Regimes

### Definition

The **complex norm** of the vector part $\mathbf{Q}$ is

$$
\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}.
$$

It is a complex number in general. It is the square root of the norm form of the pure biquaternion $\mathbf{Q}$, and it plays the role of the "magnitude" of $\mathbf{Q}$.

### Relation to the Norm Form

The norm form of the full biquaternion is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = Q_0^2 + \theta^2.
$$

So the norm form is the sum of the square of the scalar part and the square of the complex norm. This is the biquaternion analogue of the identity $|z|^2 = a^2 + b^2$ for a complex number $z = a + bi$, with $a$ replaced by $Q_0$ and $b$ replaced by $\theta$.

### The Two Regimes

The vector part $\mathbf{Q}$ is a zero divisor if and only if $N(\mathbf{Q}) = 0$, i.e., if and only if $\theta = 0$. So there are two cases:

- **Oscillatory regime:** $\theta \neq 0$. The vector part is not a zero divisor, and it can be normalized to a square root of $-1$. The powers of $\mathbf{Q}$ alternate, as in the quaternion case.
- **Nilpotent regime:** $\theta = 0$. The vector part is nilpotent, and $\mathbf{Q}^2 = 0$. The powers of $\mathbf{Q}$ truncate after the first.

These two cases cover all possibilities for the vector part. The elementary functions are computed separately in each case, and the formulas are different in the two regimes.

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, the biquaternion is a complex scalar $\tilde{Q} = Q_0 e_0$, and the elementary functions reduce to the ordinary complex elementary functions. This is a degenerate subcase of both regimes, since $\theta = 0$ and $\mathbf{Q} = 0$. It is treated separately in each section.

## The Hamilton Polar Form

### Definition

Let $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ be a biquaternion with $\theta \neq 0$. Define the **axis**

$$
\hat{n} = \frac{\mathbf{Q}}{\theta}.
$$

Then $\hat{n}$ is a pure biquaternion satisfying $\hat{n}^2 = -e_0$, and

$$
\mathbf{Q} = \theta \hat{n}.
$$

So the biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + \theta \hat{n} = e^{Q_0} \exp(\theta \hat{n}),
$$

where the last equality is the **Hamilton polar form**, and the identification of $Q_0 e_0 + \theta \hat{n}$ with $e^{Q_0} \exp(\theta \hat{n})$ is justified by the formula for the exponential proved below.

The scalar $Q_0$ is the **complex scalar part**, the complex number $\theta$ is the **complex angle**, and the unit pure biquaternion $\hat{n}$ is the **axis**.

### The Case $\theta = 0$

If $\theta = 0$ and $\mathbf{Q} \neq 0$, the vector part is nilpotent, and the axis is not defined (the normalization $\mathbf{Q}/\theta$ involves division by zero). In this case, the polar form is not available, and the biquaternion is written in the **nilpotent form**

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q}^2 = 0.
$$

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, the biquaternion is a complex scalar, and the polar form is

$$
\tilde{Q} = Q_0 e_0 = e^{Q_0} e_0,
$$

which is the ordinary complex polar form of the scalar $e^{Q_0}$.

### Non-Uniqueness of the Polar Form

The Hamilton polar form is not unique. There are three sources of ambiguity:

1. **The axis $\hat{n}$ is defined up to sign.** The equation $\mathbf{Q} = \theta \hat{n}$ determines $\hat{n}$ only up to the sign of $\theta$, and $\theta$ itself is determined only up to sign (it is a square root).
2. **The angle $\theta$ is defined up to sign, correlated with the sign of $\hat{n}$.** If we replace $\hat{n}$ by $-\hat{n}$, we must replace $\theta$ by $-\theta$ to keep $\mathbf{Q}$ fixed.
3. **The scalar part $Q_0$ is defined up to an integer multiple of $2\pi i$.** The exponential $e^{Q_0}$ is invariant under $Q_0 \mapsto Q_0 + 2\pi i n$ for $n \in \mathbb{Z}$.

The first two ambiguities are related: the pair $(\theta, \hat{n})$ is determined only up to the simultaneous sign change $(\theta, \hat{n}) \mapsto (-\theta, -\hat{n})$. The third is independent. So the polar form is determined up to the transformations

$$
(\theta, \hat{n}) \mapsto (-\theta, -\hat{n}), \qquad Q_0 \mapsto Q_0 + 2\pi i n, \quad n \in \mathbb{Z}.
$$

The non-uniqueness of the polar form is the source of the multivaluedness of the logarithm, and it should be kept in mind throughout.

## The Exponential

### Definition

The **exponential** of a biquaternion $\tilde{Q}$ is defined by the power series

$$
\exp(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^n}{n!}.
$$

The series converges for every $\tilde{Q} \in \mathbb{B}$, because $\mathbb{B}$ is finite-dimensional and the Euclidean norm grows at most exponentially with $n$. So the exponential is an entire function on $\mathbb{B}$.

### Reduction to the Vector Part

Write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$. The scalar part $Q_0 e_0$ commutes with everything, so

$$
\exp(\tilde{Q}) = \exp(Q_0 e_0) \exp(\mathbf{Q}) = e^{Q_0} \exp(\mathbf{Q}),
$$

where $e^{Q_0}$ is the ordinary complex exponential. So it suffices to compute the exponential of the vector part $\mathbf{Q}$.

### The Case $\theta \neq 0$

If $\theta \neq 0$, write $\mathbf{Q} = \theta \hat{n}$ with $\hat{n}^2 = -e_0$. The powers of $\mathbf{Q}$ satisfy

$$
\mathbf{Q}^{2m} = (-1)^m \theta^{2m} e_0, \qquad \mathbf{Q}^{2m+1} = (-1)^m \theta^{2m+1} \hat{n}.
$$

Separating even and odd powers in the exponential,

$$
\exp(\mathbf{Q}) = \left(\sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m}}{(2m)!}\right) e_0 + \left(\sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m+1}}{(2m+1)!}\right) \hat{n}.
$$

These are the Taylor series of the complex cosine and sine:

$$
\exp(\mathbf{Q}) = \cos\theta \, e_0 + \sin\theta \, \hat{n}.
$$

So

$$
\exp(\tilde{Q}) = e^{Q_0} \left(\cos\theta \, e_0 + \sin\theta \, \hat{n}\right), \qquad \theta \neq 0.
$$

### The Case $\theta = 0$

If $\theta = 0$, then $\mathbf{Q}^2 = 0$, so

$$
\mathbf{Q}^n = 0 \quad \text{for all } n \geq 2.
$$

The power series of the exponential truncates to

$$
\exp(\mathbf{Q}) = e_0 + \mathbf{Q}.
$$

So

$$
\exp(\tilde{Q}) = e^{Q_0} (e_0 + \mathbf{Q}), \qquad \theta = 0.
$$

This is the analogue of the exponential of a nilpotent matrix: $\exp(N) = I + N$.

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, the biquaternion is a complex scalar, and both formulas reduce to

$$
\exp(\tilde{Q}) = e^{Q_0} e_0,
$$

which is the ordinary complex exponential.

### Summary of the Exponential

$$
\exp(\tilde{Q}) = \begin{cases} e^{Q_0} \left(\cos\theta \, e_0 + \sin\theta \, \hat{n}\right) & \text{if } \theta \neq 0, \\ e^{Q_0} (e_0 + \mathbf{Q}) & \text{if } \theta = 0, \end{cases}
$$

where $\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ and $\hat{n} = \mathbf{Q}/\theta$.

### Properties

**Multiplicativity.** The exponential satisfies $\exp(\tilde{P} + \tilde{Q}) = \exp(\tilde{P}) \exp(\tilde{Q})$ if and only if $\tilde{P}$ and $\tilde{Q}$ commute. In general, the exponential is not multiplicative.

**Non-vanishing.** The exponential is never zero, because $e^{Q_0} \neq 0$ and the factor $\cos\theta \, e_0 + \sin\theta \, \hat{n}$ is invertible when $\theta \neq 0$, and $e_0 + \mathbf{Q}$ is invertible when $\theta = 0$ (its inverse is $e_0 - \mathbf{Q}$).

**Derivative.** The exponential is its own derivative in the sense of the directional derivative along the scalar direction: $\partial_0 \exp(\tilde{Q}) = \exp(\tilde{Q})$. This is the reason the exponential is the fundamental solution of the scalar differential operator $\partial_0$.

## The Trigonometric and Hyperbolic Functions

### Definitions

The trigonometric and hyperbolic functions are defined by the same power series as in the complex case:

$$
\sin(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{(-1)^n \tilde{Q}^{2n+1}}{(2n+1)!}, \qquad \cos(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{(-1)^n \tilde{Q}^{2n}}{(2n)!},
$$

$$
\sinh(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^{2n+1}}{(2n+1)!}, \qquad \cosh(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^{2n}}{(2n)!}.
$$

### Computation via the Exponential

The trigonometric and hyperbolic functions can be expressed in terms of the exponential:

$$
\sin(\tilde{Q}) = \frac{\exp(i\tilde{Q}) - \exp(-i\tilde{Q})}{2i}, \qquad \cos(\tilde{Q}) = \frac{\exp(i\tilde{Q}) + \exp(-i\tilde{Q})}{2},
$$

$$
\sinh(\tilde{Q}) = \frac{\exp(\tilde{Q}) - \exp(-\tilde{Q})}{2}, \qquad \cosh(\tilde{Q}) = \frac{\exp(\tilde{Q}) + \exp(-\tilde{Q})}{2},
$$

where $i$ is the scalar imaginary. This reduces the computation to the exponential formula.

### The Case $\theta \neq 0$

For $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ with $\theta \neq 0$ and $\hat{n} = \mathbf{Q}/\theta$, we have

$$
\exp(\tilde{Q}) = e^{Q_0}(\cos\theta \, e_0 + \sin\theta \, \hat{n}),
$$

$$
\exp(-\tilde{Q}) = e^{-Q_0}(\cos\theta \, e_0 - \sin\theta \, \hat{n}).
$$

Substituting into the formulas for the trigonometric and hyperbolic functions, we obtain

$$
\sin(\tilde{Q}) = \sin(Q_0) \cosh\theta \, e_0 + \cos(Q_0) \sinh\theta \, \hat{n},
$$

$$
\cos(\tilde{Q}) = \cos(Q_0) \cosh\theta \, e_0 - \sin(Q_0) \sinh\theta \, \hat{n},
$$

$$
\sinh(\tilde{Q}) = \sinh(Q_0) \cos\theta \, e_0 + \cosh(Q_0) \sin\theta \, \hat{n},
$$

$$
\cosh(\tilde{Q}) = \cosh(Q_0) \cos\theta \, e_0 + \sinh(Q_0) \sin\theta \, \hat{n}.
$$

### The Case $\theta = 0$

If $\theta = 0$, then $\mathbf{Q}^2 = 0$, and the powers of $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ satisfy

$$
\tilde{Q}^n = Q_0^n e_0 + n Q_0^{n-1} \mathbf{Q},
$$

for $n \geq 1$. Substituting into the power series of the trigonometric and hyperbolic functions, and using the Taylor series of the complex sine and cosine, we obtain

$$
\sin(\tilde{Q}) = \sin(Q_0) e_0 + \cos(Q_0) \mathbf{Q},
$$

$$
\cos(\tilde{Q}) = \cos(Q_0) e_0 - \sin(Q_0) \mathbf{Q},
$$

$$
\sinh(\tilde{Q}) = \sinh(Q_0) e_0 + \cosh(Q_0) \mathbf{Q},
$$

$$
\cosh(\tilde{Q}) = \cosh(Q_0) e_0 + \sinh(Q_0) \mathbf{Q}.
$$

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, both formulas reduce to the ordinary complex trigonometric and hyperbolic functions.

### Summary of Trigonometric and Hyperbolic Functions

$$
\sin(\tilde{Q}) = \begin{cases} \sin(Q_0) \cosh\theta \, e_0 + \cos(Q_0) \sinh\theta \, \hat{n} & \text{if } \theta \neq 0, \\ \sin(Q_0) e_0 + \cos(Q_0) \mathbf{Q} & \text{if } \theta = 0, \end{cases}
$$

$$
\cos(\tilde{Q}) = \begin{cases} \cos(Q_0) \cosh\theta \, e_0 - \sin(Q_0) \sinh\theta \, \hat{n} & \text{if } \theta \neq 0, \\ \cos(Q_0) e_0 - \sin(Q_0) \mathbf{Q} & \text{if } \theta = 0, \end{cases}
$$

$$
\sinh(\tilde{Q}) = \begin{cases} \sinh(Q_0) \cos\theta \, e_0 + \cosh(Q_0) \sin\theta \, \hat{n} & \text{if } \theta \neq 0, \\ \sinh(Q_0) e_0 + \cosh(Q_0) \mathbf{Q} & \text{if } \theta = 0, \end{cases}
$$

$$
\cosh(\tilde{Q}) = \begin{cases} \cosh(Q_0) \cos\theta \, e_0 + \sinh(Q_0) \sin\theta \, \hat{n} & \text{if } \theta \neq 0, \\ \cosh(Q_0) e_0 + \sinh(Q_0) \mathbf{Q} & \text{if } \theta = 0. \end{cases}
$$

### Properties

**Pythagorean identity.** In the oscillatory regime, $\sin^2(\tilde{Q}) + \cos^2(\tilde{Q}) = e_0$ does **not** hold in general, because the biquaternion algebra is non-commutative and the product $\sin(\tilde{Q}) \cos(\tilde{Q})$ does not commute with $\cos(\tilde{Q}) \sin(\tilde{Q})$. The identity holds only in special cases, such as when $\tilde{Q}$ is a complex scalar.

**Hyperbolic identity.** Similarly, $\cosh^2(\tilde{Q}) - \sinh^2(\tilde{Q}) = e_0$ does not hold in general.

**Relation to the exponential.** The relations $\sin(\tilde{Q}) = (\exp(i\tilde{Q}) - \exp(-i\tilde{Q}))/(2i)$ and so on hold in general, because the scalar imaginary $i$ commutes with everything.

## The Logarithm

### Definition

The **logarithm** of a biquaternion $\tilde{Q}$ is defined as the inverse of the exponential:

$$
\log(\tilde{Q}) = \tilde{L} \iff \exp(\tilde{L}) = \tilde{Q}.
$$

The logarithm is multivalued in general, as in the complex case. We compute the principal branch.

### The Case $\theta \neq 0$

Write $\tilde{Q} = e^{Q_0}(\cos\theta \, e_0 + \sin\theta \, \hat{n})$, where $Q_0 \in \mathbb{C}$, $\theta \in \mathbb{C}$, and $\hat{n}^2 = -e_0$. We want to find $\tilde{L} = L_0 e_0 + \mathbf{L}$ such that $\exp(\tilde{L}) = \tilde{Q}$.

Suppose $\mathbf{L} = \phi \hat{m}$ with $\hat{m}^2 = -e_0$ and $\phi \in \mathbb{C}$. Then

$$
\exp(\tilde{L}) = e^{L_0}(\cos\phi \, e_0 + \sin\phi \, \hat{m}).
$$

Matching with $\tilde{Q}$:

$$
e^{L_0} = e^{Q_0} \implies L_0 = Q_0 + 2\pi i n, \quad n \in \mathbb{Z},
$$

$$
\cos\phi = \cos\theta, \qquad \sin\phi \, \hat{m} = \sin\theta \, \hat{n}.
$$

The second pair of equations gives $\phi = \pm\theta + 2\pi m$ with $m \in \mathbb{Z}$, and $\hat{m} = \pm \hat{n}$ with the sign chosen consistently with the sign of $\phi$.

The principal branch of the logarithm is therefore

$$
\log(\tilde{Q}) = Q_0 e_0 + \theta \hat{n}, \qquad \theta \neq 0,
$$

and the general branch is obtained by adding $2\pi i n \, e_0$ and choosing the sign of $\phi$.

### The Case $\theta = 0$

If $\theta = 0$ and $\mathbf{Q} \neq 0$, then $\tilde{Q} = e^{Q_0}(e_0 + \mathbf{Q})$ with $\mathbf{Q}^2 = 0$. We want $\tilde{L}$ with $\exp(\tilde{L}) = \tilde{Q}$. If $\mathbf{L}^2 \neq 0$, we are back in the $\theta \neq 0$ case, which gives $\sin\theta \hat{n} = \mathbf{Q}$, but $\mathbf{Q}$ is nilpotent, so this is impossible. So we must have $\mathbf{L}^2 = 0$, i.e., $\mathbf{L}$ nilpotent. Then

$$
\exp(\tilde{L}) = e^{L_0}(e_0 + \mathbf{L}),
$$

and matching with $\tilde{Q}$:

$$
e^{L_0} = e^{Q_0} \implies L_0 = Q_0 + 2\pi i n,
$$

$$
\mathbf{L} = \mathbf{Q}.
$$

So

$$
\log(\tilde{Q}) = Q_0 e_0 + \mathbf{Q}, \qquad \theta = 0.
$$

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, the biquaternion is a complex scalar, and the logarithm reduces to the ordinary complex logarithm.

### Summary of the Logarithm

$$
\log(\tilde{Q}) = \begin{cases} Q_0 e_0 + \theta \hat{n} & \text{if } \theta \neq 0, \\ Q_0 e_0 + \mathbf{Q} & \text{if } \theta = 0, \end{cases}
$$

where $\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ and $\hat{n} = \mathbf{Q}/\theta$.

### Properties

**Multiplicativity.** The logarithm satisfies $\log(\tilde{P} \tilde{Q}) = \log(\tilde{P}) + \log(\tilde{Q})$ if and only if $\tilde{P}$ and $\tilde{Q}$ commute. In general, the logarithm is not multiplicative.

**Multivaluedness.** The logarithm is multivalued. The branches are parameterized by $n \in \mathbb{Z}$ (from the scalar part) and by the sign of $\phi$ (from the angle).

## The Power Functions

### Definition

For $\tilde{Q} \in \mathbb{B}$ and $\alpha \in \mathbb{C}$, the **power function** is defined by

$$
\tilde{Q}^\alpha = \exp(\alpha \log \tilde{Q}).
$$

The power function inherits the multivaluedness of the logarithm: for non-integer $\alpha$, it is multivalued, and the principal branch is obtained from the principal logarithm.

### The Case $\theta \neq 0$

Using the formula for the logarithm and the exponential, we obtain

$$
\tilde{Q}^\alpha = e^{\alpha Q_0}(\cos(\alpha\theta) \, e_0 + \sin(\alpha\theta) \, \hat{n}), \qquad \theta \neq 0.
$$

### The Case $\theta = 0$

In the nilpotent regime,

$$
\tilde{Q}^\alpha = e^{\alpha Q_0}(e_0 + \alpha \mathbf{Q}), \qquad \theta = 0.
$$

This involves the linear term $\alpha \mathbf{Q}$, which is the analogue of the expansion $(1 + x)^\alpha \approx 1 + \alpha x$ for small $x$ with $x^2 = 0$.

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, the power function reduces to the ordinary complex power.

### Summary of the Power Function

$$
\tilde{Q}^\alpha = \begin{cases} e^{\alpha Q_0}(\cos(\alpha\theta) \, e_0 + \sin(\alpha\theta) \, \hat{n}) & \text{if } \theta \neq 0, \\ e^{\alpha Q_0}(e_0 + \alpha \mathbf{Q}) & \text{if } \theta = 0. \end{cases}
$$

### Properties

**Integer powers.** For integer $n$, the power function is single-valued and reduces to the ordinary power $\tilde{Q}^n$.

**Non-multiplicativity.** In general, $(\tilde{P} \tilde{Q})^\alpha \neq \tilde{P}^\alpha \tilde{Q}^\alpha$, because the logarithm is not multiplicative.

**The square root.** The square root $\tilde{Q}^{1/2}$ is multivalued, and the two branches correspond to the two signs of the angle.

## Relations to the Quaternion and Complex Cases

### The Quaternion Case

The biquaternion algebra contains the quaternion algebra $\mathbb{H}$ as the subspace $\mathbb{H}_{\mathbb{B}}$, which is the fixed-point set of complex conjugation. For a quaternion $q = q_0 + \mathbf{q}$ with real coefficients, the complex norm $\theta = |\mathbf{q}|$ is real and non-negative, and the elementary functions reduce to the ordinary quaternion elementary functions:

$$
\exp(q) = e^{q_0}(\cos|\mathbf{q}| + \sin|\mathbf{q}| \, \hat{n}),
$$

$$
\log(q) = \log|q| + \arccos(q_0/|q|) \hat{n},
$$

and so on. These are the standard formulas of quaternion analysis.

### The Complex Case

The biquaternion algebra contains the complex numbers as the subspace $\mathbb{C}_{\mathbb{B}}$, which is the fixed-point set of quaternion conjugation (the scalar part). For a complex scalar $\tilde{Q} = Q_0 e_0$, the vector part vanishes, and the elementary functions reduce to the ordinary complex elementary functions:

$$
\exp(Q_0 e_0) = e^{Q_0} e_0, \qquad \log(Q_0 e_0) = \log(Q_0) e_0,
$$

and so on. These are the standard formulas of complex analysis.

### The Relation Between the Two

The quaternion case and the complex case are the two extremes of the biquaternion case: the quaternion case is the case where $\theta$ is real, and the complex case is the case where $\mathbf{Q} = 0$. The general biquaternion case interpolates between the two, with $\theta$ complex and $\mathbf{Q}$ nonzero.

## Non-Commutativity and the One-Variable Case

The elementary functions of a biquaternion variable are as simple as they are because the **vector part is a single element**, and it commutes with itself. The powers of $\mathbf{Q}$ are determined by the single relation $\mathbf{Q}^2 = -\theta^2 e_0$ (in the oscillatory regime) or $\mathbf{Q}^2 = 0$ (in the nilpotent regime), and the whole power series can be summed in closed form.

For functions of **two or more biquaternion variables**, the situation is different. The powers of a sum $\tilde{P} + \tilde{Q}$ involve the products $\tilde{P} \tilde{Q}$ and $\tilde{Q} \tilde{P}$, which are not equal in general. The binomial expansion does not hold, and the exponential of a sum is not the product of the exponentials unless the two biquaternions commute. So the elementary functions of several biquaternion variables are much more complicated than the elementary functions of one variable, and their theory is largely open.

This is the fundamental reason the theory of the elementary functions of a biquaternion variable is tractable, while the theory of functions of several biquaternion variables is not.

## Summary of Formulas

| Function | $\theta \neq 0$ | $\theta = 0$ |
|---|---|---|
| $\exp(\tilde{Q})$ | $e^{Q_0}(\cos\theta \, e_0 + \sin\theta \, \hat{n})$ | $e^{Q_0}(e_0 + \mathbf{Q})$ |
| $\sin(\tilde{Q})$ | $\sin(Q_0) \cosh\theta \, e_0 + \cos(Q_0) \sinh\theta \, \hat{n}$ | $\sin(Q_0) e_0 + \cos(Q_0) \mathbf{Q}$ |
| $\cos(\tilde{Q})$ | $\cos(Q_0) \cosh\theta \, e_0 - \sin(Q_0) \sinh\theta \, \hat{n}$ | $\cos(Q_0) e_0 - \sin(Q_0) \mathbf{Q}$ |
| $\sinh(\tilde{Q})$ | $\sinh(Q_0) \cos\theta \, e_0 + \cosh(Q_0) \sin\theta \, \hat{n}$ | $\sinh(Q_0) e_0 + \cosh(Q_0) \mathbf{Q}$ |
| $\cosh(\tilde{Q})$ | $\cosh(Q_0) \cos\theta \, e_0 + \sinh(Q_0) \sin\theta \, \hat{n}$ | $\cosh(Q_0) e_0 + \sinh(Q_0) \mathbf{Q}$ |
| $\log(\tilde{Q})$ | $Q_0 e_0 + \theta \hat{n}$ | $Q_0 e_0 + \mathbf{Q}$ |
| $\tilde{Q}^\alpha$ | $e^{\alpha Q_0}(\cos(\alpha\theta) \, e_0 + \sin(\alpha\theta) \, \hat{n})$ | $e^{\alpha Q_0}(e_0 + \alpha \mathbf{Q})$ |

## Open Questions

1. **Functions of several biquaternion variables.** How do the elementary functions extend to functions of two or more biquaternion variables? The non-commutativity is a serious obstruction, and the theory is largely open.

2. **The general regime.** Are there biquaternions for which neither the oscillatory formula nor the nilpotent formula applies? The two regimes cover the cases $\theta \neq 0$ and $\theta = 0$, and these are exhaustive, but the transition between them (as $\theta \to 0$) is not studied.

3. **The complex norm.** What is the geometric or algebraic meaning of the complex norm $\theta$ when it is not real? The complex norm is the square root of the norm form, and it is complex for a general biquaternion, but its interpretation is not clear.

4. **The polar form and the polar representations.** How does the Hamilton polar form used in this article relate to the complex polar form discussed in the article on biquaternion polar representations?

5. **The relation to the analysis.** How do the elementary functions interact with the differential operators of the analysis article? For example, what is $\tilde{\nabla} \exp(\tilde{Q})$ for a general biquaternion $\tilde{Q}$?

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of the quaternion exponential and logarithm.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the polar representations and elementary functions of biquaternions.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the polar forms and the exponential.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the roots of $-1$ on which the polar form depends.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the zero divisors and nilpotents.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.

