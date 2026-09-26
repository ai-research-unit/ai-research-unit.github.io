# __Split-Biquaternion Elementary Functions__

## Introduction

This article introduces the elementary functions of a split biquaternion variable. It follows the article on the split biquaternion polar representation, which defined the exponential and the polar decomposition of the algebra, and it uses the article on split biquaternion roots of minus one, which classified the roots of $-1$.

The treatment is purely mathematical. No physics is invoked. No examples are given. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ is assumed from the basic algebra article, together with its conjugations, its four fixed-point subspaces, and its three decompositions. The idempotents of the split complex algebra are $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$, and the idempotent decomposition of a split biquaternion is $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$ with $\tilde{Q}_\pm \in \mathbb{H}$.

The key structural fact is that the elementary functions of a split biquaternion are determined by the **idempotent decomposition** and by the **powers** of the split biquaternion. Because the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, the elementary functions of a split biquaternion reduce to the elementary functions of two ordinary quaternions, one for each idempotent component. This is the fundamental simplification relative to the biquaternion case, where the elementary functions involve a complex angle and the roots of $-1$.

There is, however, a second way to compute the elementary functions, via the **exponential polar form**, which is useful when the split biquaternion is given as the exponential of another. The two approaches agree, and the article develops both.

Throughout, a split biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The split complex unit is $j$, with $j^2 = +1$, and it commutes with the quaternion units. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The split complex conjugate is $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$, with $Q_\mu^* = q_\mu - j q'_\mu$. The Hermitian conjugate is $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^\dagger$. The norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$.

The **idempotent components** of $\tilde{Q}$ are the real quaternions

$$
\tilde{Q}_+ = \sum_{\mu=0}^{3} (q_\mu + q'_\mu) e_\mu, \qquad \tilde{Q}_- = \sum_{\mu=0}^{3} (q_\mu - q'_\mu) e_\mu.
$$

The **quaternion polar form** of a nonzero quaternion $q \in \mathbb{H}$ is

$$
q = r \exp(\mu \theta) = r(\cos\theta + \mu \sin\theta),
$$

where $r = |q| \geq 0$, $\mu$ is a unit pure real quaternion (the axis), and $\theta \in \mathbb{R}$ is the angle. The axis is defined when the vector part of $q$ is nonzero; when $q$ is a real scalar, the polar form reduces to $q = r$ (or $q = -r$, with $\theta = \pi$).

## The Exponential

### Definition

The **exponential** of a split biquaternion $\tilde{Q}$ is defined by the power series

$$
\exp(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^n}{n!}.
$$

The series converges for every $\tilde{Q} \in \mathbb{H}_{\mathbb{D}}$, because the algebra is finite-dimensional and the Euclidean norm grows at most exponentially with $n$. So the exponential is an entire function on $\mathbb{H}_{\mathbb{D}}$.

### Computation via the Idempotent Decomposition

The exponential is multiplicative on commuting elements, and the idempotent decomposition separates the algebra into two commuting copies of $\mathbb{H}$. So for $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$,

$$
\exp(\tilde{Q}) = \exp(\tilde{Q}_+) e_+ + \exp(\tilde{Q}_-) e_-,
$$

where $\exp(\tilde{Q}_\pm)$ is the ordinary quaternion exponential of the component $\tilde{Q}_\pm \in \mathbb{H}$. The quaternion exponential is

$$
\exp(\tilde{Q}_\pm) = e^{q_0^\pm} \left(\cos|\mathbf{Q}_\pm| + \frac{\sin|\mathbf{Q}_\pm|}{|\mathbf{Q}_\pm|} \mathbf{Q}_\pm\right),
$$

where $\tilde{Q}_\pm = q_0^\pm + \mathbf{Q}_\pm$ is the scalar-vector decomposition of the component, and $|\mathbf{Q}_\pm|$ is the ordinary quaternion modulus of the vector part. When the vector part vanishes, the formula reduces to $\exp(\tilde{Q}_\pm) = e^{q_0^\pm}$.

So the exponential of a split biquaternion is the pair of the quaternion exponentials of its two idempotent components:

$$
\boxed{\exp(\tilde{Q}) = \exp(\tilde{Q}_+) e_+ + \exp(\tilde{Q}_-) e_-}.
$$

This is the cleanest form of the exponential, and it is the reason the split biquaternion exponential is simpler than the biquaternion exponential.

### Computation via the Exponential Polar Form

The exponential can also be computed directly from the scalar-vector decomposition. Write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ with $Q_0 \in \mathbb{D}$ and $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The scalar part commutes with everything, so

$$
\exp(\tilde{Q}) = e^{Q_0} \exp(\mathbf{Q}),
$$

where $e^{Q_0}$ is the split complex exponential and $\exp(\mathbf{Q})$ is the exponential of the vector part.

The split complex exponential is

$$
e^{Q_0} = e^{q_0}(\cosh q'_0 + j \sinh q'_0), \qquad Q_0 = q_0 + j q'_0.
$$

The exponential of the vector part depends on the split complex norm

$$
\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}.
$$

Since $\mathbf{Q}^2 = -\theta^2 e_0$, the even and odd parts of the power series of the exponential are $\sum_m (-1)^m \theta^{2m}/(2m)!$ and $\sum_m (-1)^m \theta^{2m+1}/(2m+1)!$, so

$$
\exp(\mathbf{Q}) = \cos\theta \, e_0 + \frac{\sin\theta}{\theta} \mathbf{Q},
$$

where $\cos$ and $\sin$ are the power series functions of a split complex argument ($\theta$ itself is not needed: only the even functions of it occur, and $\cos$ is even while $\sin\theta/\theta$ depends on $\theta^2$ alone). No hyperbolic function occurs here. When $\theta^2 = r^2$ is a positive real number, the identity reads $\cos r \, e_0 + (\sin r/r)\mathbf{Q}$. The real part of $\theta^2$ is $Q_1^2 + Q_2^2 + Q_3^2$, so $\theta^2$ is never a negative real number and there is no separate trigonometric case. The formula agrees with the idempotent formula when evaluated componentwise.

### The Nilpotent Case

If the vector part is nilpotent, i.e., $\mathbf{Q}^2 = 0$, then $\theta = 0$ and the formula degenerates. In the split biquaternion algebra this happens only for $\mathbf{Q} = 0$: since $\mathbf{Q}^2 = -\theta^2 e_0$ and the real part of $\theta^2$ is $Q_1^2 + Q_2^2 + Q_3^2$, the equation $\mathbf{Q}^2 = 0$ forces $\mathbf{Q} = 0$, and then $\exp(\mathbf{Q}) = e_0$. In particular the vector elements of the zero divisor subspaces $Z_\pm$ are not nilpotent: for $\mathbf{Q} = (1 - j)e_1 \in Z_+$ one has $\mathbf{Q}^2 = -2(1 - j) \neq 0$, and similarly for $Z_-$. Unlike the biquaternion algebra, whose extra unit squares to $-1$, $\mathbb{H}_{\mathbb{D}}$ has no nonzero nilpotent vector part.

### Properties

**Non-vanishing.** The exponential is never zero, because both idempotent components are nonzero: $\exp(\tilde{Q}_\pm) \neq 0$ since the quaternion exponential is never zero.

**Multiplicativity.** The exponential satisfies $\exp(\tilde{P} + \tilde{Q}) = \exp(\tilde{P}) \exp(\tilde{Q})$ whenever $\tilde{P}$ and $\tilde{Q}$ commute, but commutativity is not necessary: for example $\tilde{P} = 2\pi e_1$ and $\tilde{Q} = -\pi e_1 + \pi\sqrt{3}\,e_2$ do not commute and all three exponentials equal $e_0$. In general, the exponential is not multiplicative.

**Derivative.** The exponential is its own derivative in the sense of the directional derivative along the scalar direction: $\partial_0 \exp(\tilde{Q}) = \exp(\tilde{Q})$.

## The Trigonometric and Hyperbolic Functions

### Definitions

The trigonometric and hyperbolic functions are defined by the same power series as in the complex case:

$$
\sin(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{(-1)^n \tilde{Q}^{2n+1}}{(2n+1)!}, \qquad \cos(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{(-1)^n \tilde{Q}^{2n}}{(2n)!},
$$

$$
\sinh(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^{2n+1}}{(2n+1)!}, \qquad \cosh(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^{2n}}{(2n)!}.
$$

### Computation via the Idempotent Decomposition

Because the idempotent decomposition separates the algebra into two commuting copies of $\mathbb{H}$, the trigonometric and hyperbolic functions also decompose:

$$
\sin(\tilde{Q}) = \sin(\tilde{Q}_+) e_+ + \sin(\tilde{Q}_-) e_-,
$$

and similarly for the other three functions. The quaternion trigonometric and hyperbolic functions are

$$
\sin(\tilde{Q}_\pm) = \sin(q_0^\pm) \cosh|\mathbf{Q}_\pm| + \cos(q_0^\pm) \sinh|\mathbf{Q}_\pm| \frac{\mathbf{Q}_\pm}{|\mathbf{Q}_\pm|},
$$

$$
\cos(\tilde{Q}_\pm) = \cos(q_0^\pm) \cosh|\mathbf{Q}_\pm| - \sin(q_0^\pm) \sinh|\mathbf{Q}_\pm| \frac{\mathbf{Q}_\pm}{|\mathbf{Q}_\pm|},
$$

$$
\sinh(\tilde{Q}_\pm) = \sinh(q_0^\pm) \cos|\mathbf{Q}_\pm| + \cosh(q_0^\pm) \sin|\mathbf{Q}_\pm| \frac{\mathbf{Q}_\pm}{|\mathbf{Q}_\pm|},
$$

$$
\cosh(\tilde{Q}_\pm) = \cosh(q_0^\pm) \cos|\mathbf{Q}_\pm| + \sinh(q_0^\pm) \sin|\mathbf{Q}_\pm| \frac{\mathbf{Q}_\pm}{|\mathbf{Q}_\pm|}.
$$

These are the standard quaternion formulas, and they reduce to the real formulas when the vector part vanishes.

### Computation via the Exponential

The trigonometric and hyperbolic functions can also be expressed in terms of the exponential:

$$
\sinh(\tilde{Q}) = \frac{\exp(\tilde{Q}) - \exp(-\tilde{Q})}{2}, \qquad \cosh(\tilde{Q}) = \frac{\exp(\tilde{Q}) + \exp(-\tilde{Q})}{2},
$$

which reduces the computation of the hyperbolic functions to the exponential formula. The trigonometric functions are not obtained this way: since $j$ is central with $j^2 = +1$, the combinations $\frac{\exp(j\tilde{Q}) \mp \exp(-j\tilde{Q})}{2}$ are $\cosh \tilde{Q} \mp j \sinh\tilde{Q}$, that is, the hyperbolic functions again, and there is no central element of $\mathbb{H}_{\mathbb{D}}$ with square $-1$ that could produce $\sin$ and $\cos$. The trigonometric functions are defined by their power series, equivalently as the ordinary quaternion trigonometric functions of the two idempotent components.

Note: in the biquaternion case, the trigonometric functions are defined using the scalar imaginary $i$, which satisfies $i^2 = -1$. In the split biquaternion case, the centre is $\mathbb{D}$, and $(a + bj)^2 = a^2 + b^2 + 2abj$ is never $-1$, so no such scalar imaginary exists. This is a fundamental difference: the split complex unit does not produce trigonometric functions, it produces hyperbolic functions.

### Properties

**Pythagorean identity.** The identity $\sin^2(\tilde{Q}) + \cos^2(\tilde{Q}) = e_0$ holds for every split biquaternion: componentwise it is the quaternion identity $\sin^2(q) + \cos^2(q) = 1$, and $\sin\tilde{Q}$ and $\cos\tilde{Q}$ both lie in the commutative subalgebra generated by $\tilde{Q}$ and the idempotents, so they commute and the two components add to $e_+ + e_- = e_0$. Non-commutativity obstructs only identities involving two independent variables.

**Hyperbolic identity.** Similarly, $\cosh^2(\tilde{Q}) - \sinh^2(\tilde{Q}) = e_0$ holds in the idempotent basis for each component.

## The Logarithm

### Definition

The **logarithm** of a split biquaternion $\tilde{Q}$ is defined as the inverse of the exponential:

$$
\log(\tilde{Q}) = \tilde{L} \iff \exp(\tilde{L}) = \tilde{Q}.
$$

The logarithm is multivalued in general, as in the complex case. We compute the principal branch.

### Computation via the Idempotent Decomposition

In the idempotent basis, the logarithm decomposes:

$$
\log(\tilde{Q}) = \log(\tilde{Q}_+) e_+ + \log(\tilde{Q}_-) e_-,
$$

where $\log(\tilde{Q}_\pm)$ is the ordinary quaternion logarithm of the component. The quaternion logarithm is

$$
\log(\tilde{Q}_\pm) = \log|\tilde{Q}_\pm| + \frac{\mathbf{Q}_\pm}{|\mathbf{Q}_\pm|} \arccos\left(\frac{q_0^\pm}{|\tilde{Q}_\pm|}\right),
$$

where $|\tilde{Q}_\pm|$ is the quaternion modulus, and $\arccos$ is the ordinary real arccosine. When the vector part vanishes, the logarithm reduces to $\log(\tilde{Q}_\pm) = \log|q_0^\pm|$ (with a branch ambiguity of $2\pi$ in the argument).

So the logarithm of a split biquaternion is the pair of the quaternion logarithms of its two idempotent components.

### The Domain of Definition

The logarithm is defined when both idempotent components are nonzero, i.e., when $\tilde{Q}$ is invertible. If one component vanishes, the corresponding logarithm is not defined, and the split biquaternion is a zero divisor.

### Properties

**Multiplicativity.** The logarithm satisfies $\log(\tilde{P} \tilde{Q}) = \log(\tilde{P}) + \log(\tilde{Q})$ if and only if $\tilde{P}$ and $\tilde{Q}$ commute. In general, the logarithm is not multiplicative.

**Multivaluedness.** The logarithm is multivalued. The branches are parameterized by the branches of the quaternion logarithm in each component, which are determined by the addition of $2\pi$ to the argument of each component.

## The Power Functions

### Definition

For $\tilde{Q} \in \mathbb{H}_{\mathbb{D}}$ and $\alpha \in \mathbb{D}$, the **power function** is defined by

$$
\tilde{Q}^\alpha = \exp(\alpha \log \tilde{Q}).
$$

The power function inherits the multivaluedness of the logarithm. For non-integer $\alpha$, it is multivalued, and the principal branch is obtained from the principal logarithm.

### Computation via the Idempotent Decomposition

In the idempotent basis, the power function decomposes:

$$
\tilde{Q}^\alpha = \tilde{Q}_+^{\alpha_+} e_+ + \tilde{Q}_-^{\alpha_-} e_-,
$$

where $\alpha = \alpha_+ e_+ + \alpha_- e_-$ with $\alpha_\pm \in \mathbb{R}$ (or, more generally, $\alpha_\pm \in \mathbb{H}$ if $\alpha$ has a non-scalar component), and $\tilde{Q}_\pm^{\alpha_\pm}$ is the quaternion power of the component. The quaternion power is defined by

$$
\tilde{Q}_\pm^{\alpha_\pm} = \exp(\alpha_\pm \log \tilde{Q}_\pm).
$$

When $\alpha$ is a real scalar, $\alpha_+ = \alpha_- = \alpha$, and the power function is the pair of the quaternion powers of the two components with the same exponent.

### Special Cases

**Integer powers.** For integer $n$, the power function is single-valued and reduces to the ordinary power $\tilde{Q}^n$.

**Square root.** The square root $\tilde{Q}^{1/2}$ is multivalued, and the branches correspond to the branches of the quaternion square root in each component.

### Properties

**Multiplicativity.** In general, $(\tilde{P} \tilde{Q})^\alpha \neq \tilde{P}^\alpha \tilde{Q}^\alpha$, because the logarithm is not multiplicative.

**Idempotent reduction.** The power function is the pair of the quaternion powers of the two idempotent components.

## Relations to the Quaternion and Split Complex Cases

### The Quaternion Case

The split biquaternion algebra contains the quaternion algebra $\mathbb{H}$ as the subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, which is the fixed-point set of split complex conjugation. For a quaternion $q = q_0 + \mathbf{q}$ with real coefficients, the idempotent components are equal: $\tilde{Q}_+ = \tilde{Q}_- = q$. So the elementary functions reduce to the ordinary quaternion elementary functions applied to the same quaternion in each component:

$$
\exp(\tilde{Q}) = \exp(q) e_+ + \exp(q) e_- = \exp(q),
$$

$$
\log(\tilde{Q}) = \log(q) e_+ + \log(q) e_- = \log(q),
$$

and so on. So the elementary functions of a split biquaternion that lies in the quaternion subspace are the ordinary quaternion elementary functions.

### The Split Complex Case

The split biquaternion algebra contains the split complex algebra $\mathbb{D}$ as the subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, which is the fixed-point set of quaternion conjugation. For a split complex scalar $Q_0 = q_0 + j q'_0$, the idempotent components are the real scalars

$$
\tilde{Q}_+ = q_0 + q'_0, \qquad \tilde{Q}_- = q_0 - q'_0.
$$

So the elementary functions reduce to the ordinary real elementary functions applied to the two real scalars:

$$
\exp(Q_0 e_0) = e^{q_0 + q'_0} e_+ + e^{q_0 - q'_0} e_-.
$$

In the standard basis, this is

$$
\exp(Q_0 e_0) = e^{q_0}(\cosh q'_0 + j \sinh q'_0),
$$

which is the split complex exponential.

### The Relation Between the Two

The quaternion case and the split complex case are the two extremes of the split biquaternion case: the quaternion case is the case where the two idempotent components are equal, and the split complex case is the case where the two components are real scalars. The general split biquaternion case interpolates between the two, with the two idempotent components being arbitrary quaternions.

## Non-Commutativity and the One-Variable Case

The elementary functions of a split biquaternion variable are as simple as they are because the idempotent decomposition reduces them to two independent quaternion elementary functions. The reduction works because the two idempotents $e_+$ and $e_-$ commute with everything, and the algebra is the direct sum of two commuting copies of $\mathbb{H}$.

For functions of **two or more split biquaternion variables**, the situation is different. The powers of a sum $\tilde{P} + \tilde{Q}$ involve the products $\tilde{P} \tilde{Q}$ and $\tilde{Q} \tilde{P}$, which are not equal in general. The binomial expansion does not hold, and the exponential of a sum is not the product of the exponentials unless the two split biquaternions commute. So the elementary functions of several split biquaternion variables are much more complicated than the elementary functions of one variable, and their theory is largely open.

This is the same situation as in the biquaternion case, and it is the fundamental reason the theory of the elementary functions of a single split biquaternion is tractable.

## Summary of Formulas

| Function | Idempotent form | Standard form |
|---|---|---|
| $\exp(\tilde{Q})$ | $\exp(\tilde{Q}_+) e_+ + \exp(\tilde{Q}_-) e_-$ | $e^{Q_0}(\cos\theta \, e_0 + \frac{\sin\theta}{\theta}\mathbf{Q})$ |
| $\sin(\tilde{Q})$ | $\sin(\tilde{Q}_+) e_+ + \sin(\tilde{Q}_-) e_-$ | (computed from the exponential) |
| $\cos(\tilde{Q})$ | $\cos(\tilde{Q}_+) e_+ + \cos(\tilde{Q}_-) e_-$ | (computed from the exponential) |
| $\sinh(\tilde{Q})$ | $\sinh(\tilde{Q}_+) e_+ + \sinh(\tilde{Q}_-) e_-$ | (computed from the exponential) |
| $\cosh(\tilde{Q})$ | $\cosh(\tilde{Q}_+) e_+ + \cosh(\tilde{Q}_-) e_-$ | (computed from the exponential) |
| $\log(\tilde{Q})$ | $\log(\tilde{Q}_+) e_+ + \log(\tilde{Q}_-) e_-$ | (computed from the components) |
| $\tilde{Q}^\alpha$ | $\tilde{Q}_+^{\alpha_+} e_+ + \tilde{Q}_-^{\alpha_-} e_-$ | $\exp(\alpha \log \tilde{Q})$ |

The idempotent form is the primary one, because it reduces the elementary functions of a split biquaternion to the elementary functions of two ordinary quaternions. The standard form, in terms of the scalar-vector decomposition and the split complex exponential, is useful when the split complex structure is the natural language.

## Comparison with the Biquaternion Case

| | $\mathbb{B}$ (biquaternion) | $\mathbb{H}_{\mathbb{D}}$ (split biquaternion) |
|---|---|---|
| Extra unit | $i$, $i^2 = -1$ | $j$, $j^2 = +1$ |
| Primary decomposition | Quaternion decomposition | Idempotent decomposition |
| Exponential | $e^{Q_0}(\cos\theta \, e_0 + \sin\theta \, \hat{n})$ with $\theta$ complex | $\exp(\tilde{Q}_+) e_+ + \exp(\tilde{Q}_-) e_-$ |
| Trigonometric functions | Defined via the scalar imaginary $i$ | Defined by the same power series, or componentwise by the quaternion trigonometric functions (no central scalar imaginary exists) |
| Hyperbolic functions | Defined via the exponential | Defined via the exponential, or via $j$ |
| Logarithm | $Q_0 e_0 + \theta \hat{n}$ with $\theta$ complex | $\log(\tilde{Q}_+) e_+ + \log(\tilde{Q}_-) e_-$ |
| Power function | $e^{\alpha Q_0}(\cos(\alpha\theta) \, e_0 + \sin(\alpha\theta) \, \hat{n})$ | $\tilde{Q}_+^{\alpha_+} e_+ + \tilde{Q}_-^{\alpha_-} e_-$ |
| Angle | Complex | Real (in each component) |
| Modulus | Complex scalar | Pair of real moduli |

The key differences are:

1. **The idempotent decomposition is the primary tool.** In the biquaternion case, the elementary functions use the quaternion decomposition and the complex scalar imaginary. In the split biquaternion case, they use the idempotent decomposition and reduce to two copies of the quaternion functions.

2. **The angles are real.** In the biquaternion case, the angle in the exponential is a complex number. In the split biquaternion case, the angles in the idempotent components are real numbers.

3. **The split complex unit produces hyperbolic functions, not trigonometric.** In the biquaternion case, the scalar imaginary $i$ produces trigonometric functions via the identity $e^{i\theta} = \cos\theta + i\sin\theta$. In the split biquaternion case, the split complex unit $j$ produces hyperbolic functions via the identity $e^{j\theta} = \cosh\theta + j\sinh\theta$.

4. **The logarithm and power function are simpler.** In the biquaternion case, the logarithm and power function involve the complex angle and the roots of $-1$. In the split biquaternion case, they reduce to the quaternion logarithm and power function in each component.

5. **The zero divisors play a role.** In the split biquaternion case, the logarithm is not defined when one of the idempotent components vanishes, i.e., when the split biquaternion is a zero divisor. In the biquaternion case, the logarithm is not defined when the norm form vanishes, which is a different condition.

## Open Questions

1. **Functions of several variables.** How do the elementary functions extend to functions of two or more split biquaternion variables? The non-commutativity is a serious obstruction, and the theory is largely open.

2. **The general case for the exponential.** For a general split biquaternion with both scalar and vector parts nonzero and with a general split complex norm, is the exponential always expressible in terms of the idempotent components, or are there cases where the direct formula is simpler?

3. **The logarithm and the zero divisors.** What is the structure of the logarithm on the complement of the zero divisor set? Are there natural branches that are continuous on the complement?

4. **The power function and the roots of $-1$.** In the biquaternion case, the power function is related to the roots of $-1$ through the complex angle. In the split biquaternion case, the roots of $-1$ are a four-dimensional family, but they do not appear in the power function directly. What is the role of the roots of $-1$ in the split biquaternion power function?

5. **The relation to the polar representation.** How do the elementary functions interact with the polar representation of the algebra, in its two-factor form and in its exponential form?

6. **The relation to the analysis.** How do the elementary functions interact with the differential operators of the analysis? For example, what is $\tilde{\nabla} \exp(\tilde{Q})$ for a general split biquaternion $\tilde{Q}$?

## Summary

The elementary functions of a split biquaternion variable are the exponential, the trigonometric and hyperbolic functions, the logarithm, and the power functions.

The key structural fact is the **idempotent decomposition**: the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, and the idempotents $e_\pm$ commute with everything. So every elementary function of a split biquaternion reduces to the corresponding elementary function of two ordinary quaternions, one for each idempotent component:

$$
\exp(\tilde{Q}) = \exp(\tilde{Q}_+) e_+ + \exp(\tilde{Q}_-) e_-,
$$

$$
\log(\tilde{Q}) = \log(\tilde{Q}_+) e_+ + \log(\tilde{Q}_-) e_-,
$$

$$
\tilde{Q}^\alpha = \tilde{Q}_+^{\alpha_+} e_+ + \tilde{Q}_-^{\alpha_-} e_-,
$$

and similarly for the trigonometric and hyperbolic functions.

The exponential can also be computed directly from the scalar-vector decomposition:

$$
\exp(\tilde{Q}) = e^{Q_0} \left(\cos\theta \, e_0 + \frac{\sin\theta}{\theta} \mathbf{Q}\right),
$$

where $\theta^2 = Q_1^2 + Q_2^2 + Q_3^2$ is the split complex norm of the vector part and $\cos$, $\sin$ are the power series functions. There is one formula, not three: it covers a real $\theta^2 = r^2$ (where it reads $\cos r$, $\sin r/r$) and a non-real $\theta^2$ alike, and a negative real $\theta^2$ cannot occur.

The elementary functions of a split biquaternion are **simpler** than the elementary functions of a biquaternion, because the idempotent decomposition reduces them to two copies of the quaternion case, the angles are real numbers, and the split complex unit produces hyperbolic functions rather than trigonometric ones. The main complication is the zero divisor set, on which the logarithm is not defined.

The elementary functions of several split biquaternion variables are largely open, because the non-commutativity prevents the simple reductions that work for a single variable.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the elementary functions of split biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.

