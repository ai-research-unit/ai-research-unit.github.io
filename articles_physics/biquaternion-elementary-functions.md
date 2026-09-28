# __Biquaternion Elementary Functions__

## Introduction

This article introduces the elementary functions of a biquaternion variable. It follows *Biquaternion Algebra*, which defined the biquaternion algebra $\mathbb{B}$, its conjugations and its six distinguished subspaces. The goal is to define the exponential, the trigonometric and hyperbolic functions, the logarithm and the power functions, and to compute them in closed form. The exponential is treated in full: its closed form, its exponential coordinates at the identity, its group law, its kernel, and the exponentials of the rotation and hyperbolic-rotation directions. Its Lie-group consequences — the group of units, the norm-one group and the Lorentz group — are in *Biquaternion Lie Group and Exponential Structure*.

The key structural fact is that the elementary functions of a biquaternion are determined by the **powers** of the biquaternion, and the powers simplify dramatically in two cases: when the vector part has a nonzero **complex norm**, and when the vector part is **nilpotent**. These two cases cover all possibilities, and they lead to two regimes, the **oscillatory regime** and the **nilpotent regime**, each of which is one of the three kinds of motion the framework carries.

Physically the two regimes are the quantum and the lightlike. The oscillatory regime $B \neq 0$ gives the purely phase-like functions of *Biquaternion Non Relativistic Quantum Theory* and *Biquaternion Elementary Functions*' exponential of a rotation; the hyperbolic subcase is the boost of a rapidity, the polar decomposition of a Lorentz transformation of *Biquaternion Relativity*; and the nilpotent regime $B = 0$ is the parabolic twist along a null direction, the degenerate case the material sector $\mathbb{M}_-$ reaches on the light cone and the wave equation of *The Wave Equation on $\mathbb{M}_-$* singles out. The closure of the elementary functions in the commutative subalgebra $\mathbb{C}[\tilde{Q}]$ is exactly what makes a single biquaternion field — an amplitude with a phase — an elementary object, while the failure of the addition formulas for two independent biquaternions is the algebraic reason the framework cannot superpose two fields by simply adding arguments.

The higher special functions — Bessel, hypergeometric, gamma, zeta, and the functions arising from the analysis — are treated in *Biquaternion Higher Special Functions*. Throughout, a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

The scalar part is $Q_0 \in \mathbb{C}$; the vector part is $\mathbf{Q}$. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, and the biquaternion norm is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2.
$$

The scalar imaginary is $i$, which commutes with the quaternion units. The material and informational sectors $\mathbb{M}_-$ and $\mathbb{M}_+$ are those of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.

## The Complex Norm and the Two Regimes

The **complex norm** of the vector part $\mathbf{Q}$ is a fixed square root

$$
B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}
$$

of the value $(\mathbf{Q}, \mathbf{Q}) = Q_1^2 + Q_2^2 + Q_3^2$ of the complex quadratic form on the vector part. The form and its polarisation are owned by *Biquaternion Norm and Invertibility*; the square root $B$ and the subalgebra it generates are in *Biquaternion Spectral Theory*.

It is a complex number in general and plays the role of the "magnitude" of $\mathbf{Q}$. When $B \neq 0$ the vector part can be written

$$
\mathbf{Q} = B \hat{n}, \qquad \hat{n} = \frac{\mathbf{Q}}{B},
$$

and $\hat{n}$ is a root of $-1$: since a pure biquaternion squares to $-\left(\mathbf{Q},\mathbf{Q}\right)e_0$, we have $\hat{n}^2 = \mathbf{Q}^2/B^2 = -e_0$. The choice of square root is a convention: replacing $B$ by $-B$ replaces the axis $\hat{n}$ by $-\hat{n}$, leaving both $\hat{n}^2$ and $\tilde{Q} = Q_0 e_0 + B\hat{n}$ unchanged.

The biquaternion norm is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = Q_0^2 + B^2,
$$

the sum of the square of the scalar part and the square of the complex norm; this is the biquaternion analogue of $|z|^2 = a^2 + b^2$ for $z = a + bi$, with $a$ replaced by $Q_0$ and $b$ by $B$.

### The Two Regimes

The vector part $\mathbf{Q}$ is a zero divisor exactly when $(\mathbf{Q}, \mathbf{Q}) = 0$, i.e. when $B = 0$; the criterion is in *Biquaternion Zero Divisors*. So there are two cases:

- **Oscillatory regime:** $B \neq 0$. The vector part is not a zero divisor, and it can be normalised to a root of $-1$. The powers of $\mathbf{Q}$ alternate, as in the quaternion case.
- **Nilpotent regime:** $B = 0$. The vector part is nilpotent, and $\mathbf{Q}^2 = 0$. The powers of $\mathbf{Q}$ truncate after the first.

These two cases cover all possibilities for the vector part. The elementary functions are computed separately in each case, and the formulas are different in the two regimes.

**Physical reading: the three kinds of motion.** The two regimes are the two physical signs of the square of the axis. An axis with $\hat{n}^2 = -e_0$ exponentiates to an oscillation, the phase of a quantum state; an axis with $(i\hat{n})^2 = +e_0$ exponentiates to a hyperbolic rotation, the boost of a rapidity; and a nilpotent axis with $\hat{n}^2 = 0$ exponentiates to a parabolic twist, the lightlike limit the material sector reaches on the null cone. The first two are the oscillatory regime seen from the two real directions of the exponent, and the third is the nilpotent regime. The trichotomy $\nu^2 = -1, 0, +1$ of the exponential is therefore not an algebraic accident but the classification of the motions the framework carries: elliptic, parabolic and hyperbolic.

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, the biquaternion is a complex scalar $\tilde{Q} = Q_0 e_0$, and the elementary functions reduce to the ordinary complex elementary functions. This is a degenerate subcase of both regimes, since $B = 0$ and $\mathbf{Q} = 0$. It is treated separately in each section.

### The Case $B = 0$, $\mathbf{Q} \neq 0$

In the nilpotent regime with a nonzero vector part, the element $\mathbf{Q}$ is a pure zero divisor, and its square vanishes. The elementary functions truncate, and the formulas are linear in $\mathbf{Q}$.

## The Subalgebra Generated by a Single Biquaternion

The elementary functions of a single biquaternion are tractable because the powers of one element span a commutative subalgebra. The $\mathbb{C}$-linear span of $\{e_0, \tilde{Q}, \tilde{Q}^2, \dots\}$ is the **commutative subalgebra generated by $\tilde{Q}$**, written $\mathbb{C}[\tilde{Q}]$; it is the smallest subalgebra of $\mathbb{B}$ containing $e_0$ and $\tilde{Q}$.

**Cayley–Hamilton.** Direct computation from the product formula gives $\tilde{Q}^2 = Q_0^2 e_0 + 2Q_0\mathbf{Q} - (\mathbf{Q},\mathbf{Q})e_0$, that is

$$
\tilde{Q}^2 - 2 Q_0 \tilde{Q} + N(\tilde{Q}) e_0 = 0.
$$

Hence every power $\tilde{Q}^n$ with $n \geq 2$ is a $\mathbb{C}$-linear combination of $e_0$ and $\tilde{Q}$, and $\mathbb{C}[\tilde{Q}] = \operatorname{span}_{\mathbb{C}}\{e_0, \tilde{Q}\}$, of dimension two when $B \neq 0$ or $\mathbf{Q} \neq 0$, and one (equal to $\mathbb{C}e_0$) when $\mathbf{Q} = 0$.

Because $\mathbb{C}[\tilde{Q}]$ is commutative, the standard identities of complex analysis — the Pythagorean identity, the hyperbolic identity, the double-angle formulas, the relation between the exponential and the trigonometric functions — hold within it, and every elementary function $F(\tilde{Q})$ defined by a power series with coefficients in $\mathbb{C}$ lies in $\mathbb{C}[\tilde{Q}]$. This is the precise sense in which the non-commutativity of $\mathbb{B}$ does not obstruct the standard identities for a single biquaternion variable. The structure of $\mathbb{C}[\tilde{Q}]$ — its minimal polynomial, its two isomorphism types and the convergence of power series in it — is developed in *Biquaternion Spectral Theory*.

**Physical reading.** The commutativity of $\mathbb{C}[\tilde{Q}]$ is why a *one-component* amplitude is as simple as a complex number: its exponential, its phase and its logarithm are single-valued functions of one element. The physically interesting content sits in the other direction — the failure of the identities for two independent biquaternions — which is the algebraic face of the fact that two fields do not simply superpose, and is what makes the module and representation theory of *Modules over the Biquaternion Algebra* and *Biquaternion Representation Theory* necessary.

## The Exponential

### Definition

The **exponential** of a biquaternion $\tilde{Q}$ is defined by the power series

$$
\exp(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^n}{n!}.
$$

The series converges for every $\tilde{Q} \in \mathbb{B}$, because $\mathbb{B}$ is finite-dimensional and the Euclidean norm grows at most exponentially with $n$. So the exponential is an entire function on $\mathbb{B}$.

### Reduction to the Vector Part

Write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$. The scalar part $Q_0 e_0$ commutes with everything, so by the identity $\exp(A + B) = \exp(A)\exp(B)$ for commuting $A$ and $B$,

$$
\exp(\tilde{Q}) = \exp(Q_0 e_0) \exp(\mathbf{Q}) = e^{Q_0} \exp(\mathbf{Q}),
$$

where $e^{Q_0}$ is the ordinary complex exponential. So it suffices to compute the exponential of the vector part $\mathbf{Q}$.

### The Case $B \neq 0$

If $B \neq 0$, write $\mathbf{Q} = B \hat{n}$ with $\hat{n}^2 = -e_0$. The powers of $\mathbf{Q}$ satisfy

$$
\mathbf{Q}^{2m} = (-1)^m B^{2m} e_0, \qquad \mathbf{Q}^{2m+1} = (-1)^m B^{2m+1} \hat{n}.
$$

Separating even and odd powers in the exponential,

$$
\exp(\mathbf{Q}) = \left(\sum_{m=0}^{\infty} \frac{(-1)^m B^{2m}}{(2m)!}\right) e_0 + \left(\sum_{m=0}^{\infty} \frac{(-1)^m B^{2m+1}}{(2m+1)!}\right) \hat{n}.
$$

These are the Taylor series of the complex cosine and sine:

$$
\exp(\mathbf{Q}) = \cos B \, e_0 + \sin B \, \hat{n}.
$$

So

$$
\exp(\tilde{Q}) = e^{Q_0} \bigl(\cos B \, e_0 + \sin B \, \hat{n}\bigr), \qquad B \neq 0.
$$

### The Case $B = 0$

If $B = 0$, then $\mathbf{Q}^2 = 0$, so

$$
\mathbf{Q}^n = 0 \quad \text{for all } n \geq 2.
$$

The power series of the exponential truncates to

$$
\exp(\mathbf{Q}) = e_0 + \mathbf{Q}.
$$

So

$$
\exp(\tilde{Q}) = e^{Q_0} (e_0 + \mathbf{Q}), \qquad B = 0.
$$

This is the analogue of the exponential of a nilpotent matrix: $\exp(N) = I + N$, and it is the parabolic motion along a null direction.

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, the biquaternion is a complex scalar, and both formulas reduce to

$$
\exp(\tilde{Q}) = e^{Q_0} e_0,
$$

which is the ordinary complex exponential. Physically this is the pure global phase.

### Summary of the Exponential

$$
\exp(\tilde{Q}) =
\begin{cases}
e^{Q_0} \bigl(\cos B \, e_0 + \sin B \, \hat{n}\bigr) & \text{if } B \neq 0, \\[2mm]
e^{Q_0} (e_0 + \mathbf{Q}) & \text{if } B = 0,
\end{cases}
$$

where $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ and $\hat{n} = \mathbf{Q}/B$.

### Properties

**Multiplicativity.** The exponential satisfies $\exp(\tilde{P} + \tilde{Q}) = \exp(\tilde{P}) \exp(\tilde{Q})$ if $\tilde{P}$ and $\tilde{Q}$ commute. In general, the exponential is not multiplicative.

**Non-vanishing.** The exponential is never zero. In the oscillatory case, $e^{Q_0} \neq 0$ and the factor $\cos B \, e_0 + \sin B \, \hat{n}$ is invertible: its inverse is $\cos B \, e_0 - \sin B \, \hat{n}$, as follows from the identity

$$
(\cos B \, e_0 + \sin B \, \hat{n})(\cos B \, e_0 - \sin B \, \hat{n}) = (\cos^2 B + \sin^2 B) e_0 = e_0.
$$

In the nilpotent case, $e^{Q_0} \neq 0$ and $(e_0 + \mathbf{Q})(e_0 - \mathbf{Q}) = e_0 - \mathbf{Q}^2 = e_0$.

**Derivative in the scalar direction.** The exponential satisfies $\partial_0 \exp(\tilde{Q}) = \exp(\tilde{Q})$, where $\partial_0 = \partial/\partial Q_0$ is the derivative in the scalar direction. This is the reason the exponential is the fundamental solution of the scalar differential operator $\partial_0$.

**Derivative in the vector directions.** The derivatives $\partial_k \exp(\tilde{Q})$ for $k = 1, 2, 3$ are **not** equal to $\exp(\tilde{Q}) e_k$ or $e_k \exp(\tilde{Q})$ in general. The reason is that $\partial_k \tilde{Q} = e_k$ does not commute with $\tilde{Q}$ unless $\tilde{Q}$ lies in the subalgebra generated by $e_0$ and $e_k$. The correct expression is the biquaternion analogue of the matrix identity $\partial e^M = \int_0^1 e^{sM}(\partial M)e^{(1-s)M}\,ds$, namely

$$
\partial_k \exp(\tilde{Q}) = \int_0^1 e^{s \tilde{Q}} e_k e^{(1-s)\tilde{Q}} \, ds.
$$

This reduces to $\exp(\tilde{Q}) e_k$ only when $e_k$ commutes with $\tilde{Q}$.

**Biquaternion norm.** The biquaternion norm of the exponential is

$$
N(\exp(\tilde{Q})) = \exp(2 Q_0) = \exp(\mathrm{Tr}(\tilde{Q})),
$$

where $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}\,\tilde{Q} = 2Q_0$ is the trace of the element. The verification is direct: in the oscillatory regime, $N(\exp(\tilde{Q})) = e^{2 Q_0}(\cos^2 B + \sin^2 B) = e^{2 Q_0}$; in the nilpotent regime, $N(\exp(\tilde{Q})) = e^{2 Q_0}(1 + 0) = e^{2 Q_0}$.

**Physical reading: the exponential as a one-parameter motion.** The norm formula is the reason the exponential is a motion of the unit group rather than an arbitrary map: $|\det|$ is preserved by the compact directions and rescaled by the non-compact ones, so a pure rotation leaves the norm at one while a boost rescales it and a parabolic twist leaves the first-order term. The vanishing of the derivative failure — the integral formula for $\partial_k\exp$ — is the biquaternionic statement that the vector directions do not commute, the algebraic origin of the Wigner rotation of two non-collinear boosts of *Biquaternion Rotations and Lorentz Transformations*. The fact that the exponential is never zero and never a zero divisor is the statement that an exponential field is always invertible, so no motion of the group ever lands on the light cone.

### Derivative at the Origin

The differential of the exponential at the origin is the identity, $d\exp_0 = \mathrm{id}$, so $\exp$ is a local diffeomorphism near $0$ and provides exponential coordinates near the identity of the group of units $\mathbb{B}^\times$ (the Lie-group side of this is in *Biquaternion Lie Group and Exponential Structure*).

### The Group Law: $\exp(a)\exp(b)$ versus $\exp(a+b)$

The exponential is not a homomorphism from the additive group of the algebra to the multiplicative group of the units. Its failure to be one is measured by the bracket.

**Commuting case.** If $[a,b] = 0$, then

$$
\exp(a)\exp(b) = \exp(a+b) = \exp(b)\exp(a).
$$

In particular, this holds when $a$ and $b$ lie in a common commutative subalgebra. For a single biquaternion $\tilde{Q}$, all elementary functions lie in the commutative subalgebra $\mathbb{C}[\tilde{Q}]$ generated by $e_0$ and $\tilde{Q}$, so the usual addition formula holds there.

**General case.** The Baker–Campbell–Hausdorff theorem gives, for sufficiently small $a, b$,

$$
\exp(a)\exp(b) = \exp\!\left(a + b + \frac{1}{2}[a,b] + \frac{1}{12}\bigl[a,[a,b]\bigr] - \frac{1}{12}\bigl[b,[a,b]\bigr] + \cdots\right),
$$

a convergent series of iterated brackets. Thus $\exp(a)\exp(b)$ differs from $\exp(a+b)$ by the term $\tfrac{1}{2}[a,b]$ and higher brackets; the difference vanishes whenever $[a,b] = 0$, though the converse can fail, since a non-commuting pair may still satisfy $\exp(a)\exp(b) = \exp(a+b)$ when the BCH remainder exponentiates to $e_0$. For instance, with $a = e_1$ and $b = e_2$ the product $\exp(e_1)\exp(e_2)$ carries a term $\sin^2 1\, e_3$ that is absent from $\exp(e_1+e_2)$.

**Physical reading.** The commutator term is the composition defect of two motions, and its physical name is the Wigner rotation: the composition of two non-collinear boosts is a boost followed by a rotation, not a boost. The framework's Lie-theoretic statement of this is *Biquaternion Rotations and Lorentz Transformations* and *The Operator Representation of Biquaternions*; the representation-theoretic reading of the same bracket is *Biquaternion Representation Theory*.

### The Kernel of the Exponential

Because $\exp$ is surjective onto the group of units but not injective, the fibre over the identity measures the ambiguity of the logarithm.

**Theorem.** For a biquaternion $\tilde{Q}$ one has $\exp(\tilde{Q}) = e_0$ if and only if $\tilde{Q}$ is diagonalisable over $\mathbb{C}$ and every eigenvalue of $\tilde{Q}$ lies in $2\pi i\mathbb{Z}$.

**Proof.** If $\tilde{Q}$ is diagonalisable with eigenvalues $\lambda_1, \lambda_2$, then $\exp(\tilde{Q})$ is diagonalisable with eigenvalues $e^{\lambda_1}, e^{\lambda_2}$, and equals $I$ exactly when $e^{\lambda_1} = e^{\lambda_2} = 1$. Conversely, write $\tilde{Q} = S + N$ with $S$ semisimple and $N$ nilpotent commuting. Then $\exp(\tilde{Q}) = \exp(S)\exp(N)$ is the product of a semisimple and a unipotent factor; if it equals $I$, the unipotent factor is semisimple, hence trivial, so $N = 0$.

**Concrete description.** A biquaternion lies in the kernel exactly when its representing matrix is conjugate to $\mathrm{diag}(2\pi i m, 2\pi i n)$ with $m, n \in \mathbb{Z}$. The kernel is thus an infinite subset of $\mathbb{B}$, not an additive subgroup, since $\exp$ is not a homomorphism. It contains the scalars $2\pi i k\, e_0$ but much more: $\mathrm{diag}(0, 2\pi i)$ also exponentiates to the identity.

**In biquaternion terms.** The eigenvalues of the matrix representing $\tilde{Q}$ are $\lambda_\pm = Q_0 \pm iB$, with $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$. So $\exp(\tilde{Q}) = e_0$ exactly when either $\mathbf{Q} = 0$ and $\tilde{Q} = Q_0 e_0$ is a scalar with $Q_0 \in 2\pi i\mathbb{Z}$, or $B \neq 0$ and both $Q_0 \pm iB$ lie in $2\pi i\mathbb{Z}$. The second condition is equivalent to

$$
Q_0 = \pi i k, \qquad B = \pi j, \qquad k, j \in \mathbb{Z}, \quad k \equiv j \pmod 2,
$$

the eigenvalues then being $2\pi i(k\pm j)/2$. If $B = 0$ but $\mathbf{Q} \neq 0$, the matrix is a nonzero nilpotent, hence not diagonalisable and not in the kernel: $\exp(\mathbf{Q}) = e_0 + \mathbf{Q} \neq e_0$.

**Example.** The biquaternion $\tilde{Q} = \pi i\, e_0 + \pi\, e_3$ has $Q_0 = \pi i$, $B = \pi$, so $k = j = 1$ and $\exp(\tilde{Q}) = e^{\pi i}(\cos\pi\, e_0 + \sin\pi\, e_3) = e_0$. Since $N(\tilde{Q}) = 0$, this kernel element is a zero divisor: the kernel is not contained in the group of units.

**On the phrase "eigenvalues differ by a multiple of $2\pi i$".** The condition implies such a difference, but the difference alone is weaker: $\tilde{Q} = e_0$ has equal eigenvalues yet $\exp(e_0) \neq e_0$. Each eigenvalue must be a multiple of $2\pi i$.

**Physical reading: the phase ambiguity.** The kernel is the statement that the phase of a field is defined only up to $2\pi i$, and the example $\pi i\,e_0 + \pi e_3$ is the case where a physical representative is a zero divisor — a lightlike element — although its exponential is the identity. This is the algebraic ancestor of the unobservability of the global phase: a field and its exponential differ by an element of the kernel, and no measurement of a phase can detect it. The fact that the kernel contains zero divisors is why the lift of the phase to the algebra, not only to the unit group, has to be watched.

### The Exponential of a Rotation and of a Hyperbolic Rotation

Let $\hat{n}$ be a real unit vector part, so that $\hat{n}^2 = -e_0$. The two real three-dimensional families of exponents — the bivector directions $\theta\hat{n}$ and the vector directions $\psi\, i\hat{n}$, with $\theta, \psi \in \mathbb{R}$ — exponentiate in closed form. They are the two real summands of the trace-free subalgebra of $\mathbb{B}$, developed in *Biquaternion Lie Algebra*.

**Rotations (the bivector directions).** For real $\theta$,

$$
\exp(\theta\hat{n}) = \cos\theta\, e_0 + \sin\theta\, \hat{n},
$$

a unit quaternion in $\mathbb{H}_{\mathbb{B}}$, since $N = \cos^2\theta + \sin^2\theta = 1$. It rotates the vector part: conjugation by $\exp(\theta\hat{n})$ rotates any real vector $\mathbf{v}$ about the axis $\hat{n}$ through $2\theta$, the double-cover relation $S^3 \to SO(3)$. The family $\theta \mapsto \exp(\theta\hat{n})$ has period $2\pi$ in $S^3$, since $\exp(2\pi\hat{n}) = e_0$; the induced rotation of the vector part has angle $2\theta$, so it is the identity already at $\theta = \pi$, where $\exp(\pi\hat{n}) = -e_0$, while the spinor returns to $e_0$ only after a $4\pi$ rotation.

**Hyperbolic rotations (the vector directions).** With $(i\hat{n})^2 = +e_0$ and rapidity $\psi \in \mathbb{R}$,

$$
\exp(\psi\, i\hat{n}) = \cosh\psi\, e_0 + \sinh\psi\, i\hat{n}.
$$

This element is Hermitian, lies in $\mathbb{M}_+$, and has $N = \cosh^2\psi - \sinh^2\psi = 1$. Unlike the rotation family it is not periodic and is unbounded as $\psi \to \pm\infty$; it is the rotor of a Lorentz transformation along $\hat{n}$ with rapidity $\psi$. The set of hyperbolic rotations is not a subgroup: the product of two hyperbolic rotations in non-parallel directions is a hyperbolic rotation followed by a rotation.

**Comparison.** A general exponent is $\tilde{Q} = q + iq'$ with $q, q'$ real vector parts; the rotation and hyperbolic families commute only when $q$ and $q'$ are parallel, since $[q, iq'] = 2i\,(q \times q')$, and in general the closed form of the exponential with $Q_0 = 0$ mixes the two behaviours.

**Physical reading: elliptic and hyperbolic motions.** These two families are the two canonical motions of the framework. The rotation family is the compact one, periodic, exponent of a bivector, and its $4\pi$ return is the spinorial double cover, the fact that a spinor needs a full turn of $4\pi$ to come back; its geometric home is *Biquaternion Spin Geometry* and *Biquaternion Rotations and Lorentz Transformations*. The hyperbolic family is the non-compact one, the exponent of a vector direction, unbounded as the rapidity tends to infinity, and it is the boost of special relativity, the home of *Biquaternion Relativity* and the Lorentz transformations of *Biquaternion Lorentzian and Conformal Geometry*. Both have norm one, so the unit group carries them, and the fact that the product of two non-parallel boosts is a boost times a rotation is the Wigner rotation, the content of the comparison above.

## The Trigonometric and Hyperbolic Functions

### Definitions

The trigonometric and hyperbolic functions are defined by the same power series as in the complex case:

$$
\sin(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{(-1)^n \tilde{Q}^{2n+1}}{(2n+1)!}, \qquad \cos(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{(-1)^n \tilde{Q}^{2n}}{(2n)!},
$$

$$
\sinh(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^{2n+1}}{(2n+1)!}, \qquad \cosh(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^{2n}}{(2n)!}.
$$

These series converge for every $\tilde{Q} \in \mathbb{B}$, for the same reason as the exponential.

### Computation via the Exponential

The trigonometric and hyperbolic functions can be expressed in terms of the exponential:

$$
\sin(\tilde{Q}) = \frac{\exp(i\tilde{Q}) - \exp(-i\tilde{Q})}{2i}, \qquad \cos(\tilde{Q}) = \frac{\exp(i\tilde{Q}) + \exp(-i\tilde{Q})}{2},
$$

$$
\sinh(\tilde{Q}) = \frac{\exp(\tilde{Q}) - \exp(-\tilde{Q})}{2}, \qquad \cosh(\tilde{Q}) = \frac{\exp(\tilde{Q}) + \exp(-\tilde{Q})}{2},
$$

where $i$ is the scalar imaginary. These identities hold because $i$ commutes with everything, so the standard derivations carry over. They reduce the computation to the exponential formula.

### The Case $B \neq 0$

For $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ with $B \neq 0$ and $\hat{n} = \mathbf{Q}/B$, we have

$$
\exp(\tilde{Q}) = e^{Q_0}(\cos B \, e_0 + \sin B \, \hat{n}), \qquad \exp(-\tilde{Q}) = e^{-Q_0}(\cos B \, e_0 - \sin B \, \hat{n}).
$$

Substituting into the formulas for the trigonometric and hyperbolic functions, we obtain

$$
\sin(\tilde{Q}) = \sin(Q_0) \cosh B \, e_0 + \cos(Q_0) \sinh B \, \hat{n},
$$

$$
\cos(\tilde{Q}) = \cos(Q_0) \cosh B \, e_0 - \sin(Q_0) \sinh B \, \hat{n},
$$

$$
\sinh(\tilde{Q}) = \sinh(Q_0) \cos B \, e_0 + \cosh(Q_0) \sin B \, \hat{n},
$$

$$
\cosh(\tilde{Q}) = \cosh(Q_0) \cos B \, e_0 + \sinh(Q_0) \sin B \, \hat{n}.
$$

### The Case $B = 0$

If $B = 0$, then $\mathbf{Q}^2 = 0$, and the powers of $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ satisfy

$$
\tilde{Q}^n = Q_0^n e_0 + n Q_0^{n-1} \mathbf{Q}, \qquad n \geq 1,
$$

and $\tilde{Q}^0 = e_0$. This follows from the binomial expansion, which truncates at first order in $\mathbf{Q}$ because $\mathbf{Q}^2 = 0$. Substituting into the power series of the trigonometric and hyperbolic functions, and using the Taylor series of the complex sine and cosine, we obtain

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
\sin(\tilde{Q}) =
\begin{cases}
\sin(Q_0) \cosh B \, e_0 + \cos(Q_0) \sinh B \, \hat{n} & \text{if } B \neq 0, \\[1mm]
\sin(Q_0) e_0 + \cos(Q_0) \mathbf{Q} & \text{if } B = 0,
\end{cases}
$$

$$
\cos(\tilde{Q}) =
\begin{cases}
\cos(Q_0) \cosh B \, e_0 - \sin(Q_0) \sinh B \, \hat{n} & \text{if } B \neq 0, \\[1mm]
\cos(Q_0) e_0 - \sin(Q_0) \mathbf{Q} & \text{if } B = 0,
\end{cases}
$$

$$
\sinh(\tilde{Q}) =
\begin{cases}
\sinh(Q_0) \cos B \, e_0 + \cosh(Q_0) \sin B \, \hat{n} & \text{if } B \neq 0, \\[1mm]
\sinh(Q_0) e_0 + \cosh(Q_0) \mathbf{Q} & \text{if } B = 0,
\end{cases}
$$

$$
\cosh(\tilde{Q}) =
\begin{cases}
\cosh(Q_0) \cos B \, e_0 + \sinh(Q_0) \sin B \, \hat{n} & \text{if } B \neq 0, \\[1mm]
\cosh(Q_0) e_0 + \sinh(Q_0) \mathbf{Q} & \text{if } B = 0.
\end{cases}
$$

### Properties

**Pythagorean identity.** The identity

$$
\sin^2(\tilde{Q}) + \cos^2(\tilde{Q}) = e_0
$$

holds for every $\tilde{Q} \in \mathbb{B}$.

**Proof.** Write $A = e^{i\tilde{Q}}$ and $B = e^{-i\tilde{Q}}$. Since $i\tilde{Q}$ commutes with $-i\tilde{Q}$, we have $AB = e^{i\tilde{Q}}e^{-i\tilde{Q}} = e^{i\tilde{Q}-i\tilde{Q}} = e_0$. Then

$$
\sin^2(\tilde{Q}) + \cos^2(\tilde{Q})
= \frac{(A - B)^2}{-4} + \frac{(A + B)^2}{4}
= \frac{-(A^2 - 2AB + B^2) + (A^2 + 2AB + B^2)}{4}
= \frac{4AB}{4}
= AB
= e_0.
$$

Alternatively, in the oscillatory regime, a direct expansion gives

$$
\sin^2(\tilde{Q}) + \cos^2(\tilde{Q}) = (\cosh^2 B - \sinh^2 B) e_0 = e_0,
$$

since the vector parts cancel by antisymmetry and the scalar parts combine via the hyperbolic identity. The reason the identity survives the non-commutativity of $\mathbb{B}$ is that both $\sin(\tilde{Q})$ and $\cos(\tilde{Q})$ lie in the **commutative subalgebra** $\mathbb{C}[\tilde{Q}]$ generated by $\tilde{Q}$, within which the standard complex-analytic identities hold. The identity fails only for expressions involving two or more independent biquaternions.

**Hyperbolic identity.** The identity

$$
\cosh^2(\tilde{Q}) - \sinh^2(\tilde{Q}) = e_0
$$

holds for every $\tilde{Q} \in \mathbb{B}$.

**Proof.** Write $A = e^{\tilde{Q}}$ and $B = e^{-\tilde{Q}}$. Since $\tilde{Q}$ commutes with $-\tilde{Q}$, we have $AB = e^{\tilde{Q}-\tilde{Q}} = e_0$. Then

$$
\cosh^2(\tilde{Q}) - \sinh^2(\tilde{Q})
= \frac{(A + B)^2 - (A - B)^2}{4}
= \frac{(A^2 + 2AB + B^2) - (A^2 - 2AB + B^2)}{4}
= \frac{4AB}{4}
= AB
= e_0.
$$

**Double-angle formulas.** The standard double-angle formulas hold:

$$
\sin(2\tilde{Q}) = 2\sin(\tilde{Q})\cos(\tilde{Q}), \qquad \cos(2\tilde{Q}) = \cos^2(\tilde{Q}) - \sin^2(\tilde{Q}),
$$

$$
\sinh(2\tilde{Q}) = 2\sinh(\tilde{Q})\cosh(\tilde{Q}), \qquad \cosh(2\tilde{Q}) = \cosh^2(\tilde{Q}) + \sinh^2(\tilde{Q}).
$$

These follow from the corresponding identities in the commutative subalgebra $\mathbb{C}[\tilde{Q}]$.

**Addition formulas.** The addition formulas, such as

$$
\sin(\tilde{P} + \tilde{Q}) = \sin(\tilde{P})\cos(\tilde{Q}) + \cos(\tilde{P})\sin(\tilde{Q}),
$$

hold **if $\tilde{P}$ and $\tilde{Q}$ commute**. In general they fail. For instance, with $\tilde{P} = e_1$ and $\tilde{Q} = e_2$, each is pure with complex norm $1$, so

$$
\sin(e_1) = \sinh(1) e_1, \qquad \cos(e_1) = \cosh(1) e_0,
$$

$$
\sin(e_2) = \sinh(1) e_2, \qquad \cos(e_2) = \cosh(1) e_0,
$$

and hence

$$
\sin(e_1)\cos(e_2) + \cos(e_1)\sin(e_2) = \sinh(1)\cosh(1)(e_1 + e_2) = \tfrac{1}{2}\sinh(2)(e_1 + e_2).
$$

On the other hand, $e_1 + e_2$ is pure with complex norm $\sqrt{2}$, so

$$
\sin(e_1 + e_2) = \frac{\sinh\sqrt{2}}{\sqrt{2}}(e_1 + e_2).
$$

These are unequal: $\tfrac{1}{2}\sinh(2) \approx 1.813$, whereas $\sinh\sqrt{2}/\sqrt{2} \approx 1.368$. The failure is a genuine consequence of non-commutativity.

**Relation to the exponential.** The relations $\sin(\tilde{Q}) = (\exp(i\tilde{Q}) - \exp(-i\tilde{Q}))/(2i)$ and so on hold in general, because the scalar imaginary $i$ commutes with everything.

**Physical reading: the superposition defect.** The failure of the addition formula for non-commuting arguments is the algebraic statement that two fields do not superpose by adding their phases: the interference of two amplitudes is not the sum of the two arguments' functions. The framework's resolution is to keep the fields as elements of modules over the algebra rather than as arguments of scalar functions, which is the content of *Modules over the Biquaternion Algebra* and *The Operator Representation of Biquaternions*, and the field-theoretic consequence is the non-linear-looking composition of two boost fields in *Biquaternion Relativity*.

## The Logarithm

### Definition

The **logarithm** of a biquaternion $\tilde{Q}$ is defined as the inverse of the exponential:

$$
\log(\tilde{Q}) = \tilde{L} \iff \exp(\tilde{L}) = \tilde{Q}.
$$

The exponential is never a zero divisor: from the property $N(\exp(\tilde{L})) = e^{2 L_0}$ for every $\tilde{L}$, the biquaternion norm of $\exp(\tilde{L})$ is always nonzero. So the logarithm can exist only on the group of units $\mathbb{B}^\times = \{N(\tilde{Q}) \neq 0\}$. The following theorem shows that it exists on the whole group of units, and on no larger set.

### Existence of the Logarithm

**Theorem.** Every invertible biquaternion has a logarithm. The domain of the logarithm is exactly the group of units

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\}.
$$

**Proof.** Let $\tilde{Q}$ be invertible, so $N(\tilde{Q}) \neq 0$. We treat the three cases.

**Case $B \neq 0$.** Set $R = \sqrt{N(\tilde{Q})}$, a fixed square root, $\hat{n} = \mathbf{Q}/B$, and let $\Theta$ be determined by $\cos\Theta = Q_0/R$ and $\sin\Theta = B/R$, so that $Q_0 = R\cos\Theta$ and $B = R\sin\Theta$. Since $N(\tilde{Q}) \neq 0$, we have $R \neq 0$, so the principal branch of $\log R$ is defined. Set

$$
\tilde{L} = \log R \, e_0 + \Theta \hat{n}.
$$

Then

$$
\exp(\tilde{L}) = R(\cos\Theta \, e_0 + \sin\Theta \, \hat{n}) = Q_0 e_0 + B \hat{n} = \tilde{Q},
$$

using the identity $\exp(\Theta \hat{n}) = \cos\Theta \, e_0 + \sin\Theta \, \hat{n}$, which follows from $\hat{n}^2 = -e_0$.

**Case $B = 0$, $\mathbf{Q} \neq 0$.** Then $\mathbf{Q}^2 = 0$ and $N(\tilde{Q}) = Q_0^2 \neq 0$, so $Q_0 \neq 0$. Set

$$
\tilde{L} = \log Q_0 \, e_0 + \mathbf{Q}/Q_0.
$$

Then

$$
\tilde{L}^2 = (\log Q_0)^2 e_0 + 2 \log Q_0 \cdot \mathbf{Q}/Q_0 + (\mathbf{Q}/Q_0)^2.
$$

The last term vanishes because $\mathbf{Q}^2 = 0$. The middle term commutes with the first term, since it is a scalar multiple of $\mathbf{Q}$ and the first term is a scalar multiple of $e_0$. So

$$
\exp(\tilde{L}) = \exp(\log Q_0 \cdot e_0) \exp(\mathbf{Q}/Q_0) = Q_0 (e_0 + \mathbf{Q}/Q_0) = Q_0 e_0 + \mathbf{Q} = \tilde{Q}.
$$

**Case $\mathbf{Q} = 0$.** Then $\tilde{Q} = Q_0 e_0$ with $Q_0 \neq 0$ (since $N(\tilde{Q}) = Q_0^2 \neq 0$), and $\log \tilde{Q} = \log Q_0 \cdot e_0$, the ordinary complex logarithm.

**Converse.** If $\tilde{Q}$ has a logarithm, then $\tilde{Q} = \exp(\tilde{L})$ for some $\tilde{L}$, and $N(\tilde{Q}) = N(\exp(\tilde{L})) = e^{2 L_0} \neq 0$. So $\tilde{Q}$ is invertible.

### Summary of the Logarithm

$$
\log(\tilde{Q}) =
\begin{cases}
\log R \, e_0 + \Theta \hat{n} & \text{if } B \neq 0, \\[2mm]
\log Q_0 \, e_0 + \dfrac{\mathbf{Q}}{Q_0} & \text{if } B = 0, \; \mathbf{Q} \neq 0, \\[2mm]
\log Q_0 \, e_0 & \text{if } \mathbf{Q} = 0,
\end{cases}
$$

defined on the group of units $\mathbb{B}^\times = \{N(\tilde{Q}) \neq 0\}$. Here $R = \sqrt{Q_0^2 + B^2}$, $\cos\Theta = Q_0/R$, and $\sin\Theta = B/R$. The branch is determined by the choice of $R$, the choice of $\Theta$, and the choice of branch of the complex logarithm.

### Properties

**Multiplicativity.** The logarithm satisfies $\log(\tilde{P} \tilde{Q}) = \log(\tilde{P}) + \log(\tilde{Q})$ whenever $\tilde{P}$ and $\tilde{Q}$ commute. In general the logarithm is not multiplicative, and the converse is not claimed: as for the exponential group law, a non-commuting pair may satisfy the identity under a compatible choice of branches. The failure is the same as in the quaternion case: when the two axes $\hat{n}$ and $\hat{m}$ do not commute, the product of the exponentials is not the exponential of the sum.

**Multivaluedness.** The logarithm is multivalued. The branches are parameterised by the integer shifts of the scalar logarithm and of the angle $\Theta$, that is, by $\log R \mapsto \log R + 2\pi i n$ and $\Theta \mapsto \Theta + 2\pi m$ with $n, m \in \mathbb{Z}$; equivalently, they differ by the elements of the kernel of the exponential.

**Domain.** The logarithm exists exactly on the group of units $\mathbb{B}^\times$. It fails on the zero divisor set $\mathcal{Z}$ and at the zero element $0$.

**Failure at pure nilpotents.** In particular, the logarithm does not exist at any pure nilpotent $\tilde{Q} = \mathbf{Q}$ with $\mathbf{Q}^2 = 0$ and $\mathbf{Q} \neq 0$: such an element is a nonzero zero divisor, hence not invertible, whereas every exponential is invertible.

**Physical reading: the domain of a phase.** The logarithm is the phase of the field, and its domain is exactly the nonzero-norm elements. The failure on the zero divisor set is the physical statement that a field on the light cone — a null momentum, a lightlike momentum four-vector — has no phase and no logarithm: it cannot be written as the exponential of a finite generator, which is the analytic face of the infinite-rapidity limit discussed in *Biquaternion Lie Group and Exponential Structure*. The multivaluedness is the same $2\pi i$ ambiguity as in the kernel of the exponential, the physical global phase.

## The Power Functions

### Definition

For $\tilde{Q} \in \mathbb{B}$ and $\alpha \in \mathbb{C}$, the **power function** is defined by

$$
\tilde{Q}^\alpha = \exp(\alpha \log \tilde{Q}).
$$

The power function inherits the multivaluedness of the logarithm: for non-integer $\alpha$, it is multivalued, and the principal branch is obtained from the principal logarithm. The domain is the group of units $\mathbb{B}^\times$.

### The Case $B \neq 0$

Using the formula for the logarithm and the exponential, we obtain

$$
\tilde{Q}^\alpha = R^\alpha \bigl(\cos(\alpha\Theta) \, e_0 + \sin(\alpha\Theta) \, \hat{n}\bigr), \qquad B \neq 0,
$$

where $R = \sqrt{Q_0^2 + B^2}$, $\cos\Theta = Q_0/R$, and $\sin\Theta = B/R$.

### The Case $B = 0$, $\mathbf{Q} \neq 0$

In the nilpotent regime,

$$
\tilde{Q}^\alpha = Q_0^\alpha e_0 + \alpha Q_0^{\alpha-1} \mathbf{Q}, \qquad B = 0, \quad \mathbf{Q} \neq 0,
$$

with $Q_0 \neq 0$ required for invertibility. This involves the linear term $\alpha Q_0^{\alpha-1} \mathbf{Q}$, which is the analogue of the expansion $(1 + x)^\alpha \approx 1 + \alpha x$ for small $x$ with $x^2 = 0$.

### The Case $\mathbf{Q} = 0$

If $\mathbf{Q} = 0$, the power function reduces to the ordinary complex power.

### Summary of the Power Function

$$
\tilde{Q}^\alpha =
\begin{cases}
R^\alpha \bigl(\cos(\alpha\Theta) \, e_0 + \sin(\alpha\Theta) \, \hat{n}\bigr) & \text{if } B \neq 0, \\[2mm]
Q_0^\alpha e_0 + \alpha Q_0^{\alpha-1} \mathbf{Q} & \text{if } B = 0, \; \mathbf{Q} \neq 0,
\end{cases}
$$

defined on $\mathbb{B}^\times$.

### Properties

**Integer powers.** For integer $n$, the power function is single-valued on $\mathbb{B}^\times$ and reduces to the ordinary power $\tilde{Q}^n$. Moreover, for integer $n$ the ordinary power $\tilde{Q}^n$ is defined by repeated multiplication on all of $\mathbb{B}$, including the zero divisors; the formula $\tilde{Q}^n = \exp(n \log \tilde{Q})$ holds only on the group of units.

**Non-multiplicativity.** In general, $(\tilde{P} \tilde{Q})^\alpha \neq \tilde{P}^\alpha \tilde{Q}^\alpha$, because the logarithm is not multiplicative.

**The square root.** The square root $\tilde{Q}^{1/2}$ is multivalued, and the two branches correspond to the two signs of the angle.

**Consistency with the biquaternion norm.** For a fixed choice of branch, the power function satisfies

$$
N(\tilde{Q}^\alpha) = N(\tilde{Q})^\alpha.
$$

**Proof.** In the oscillatory regime, $\tilde{Q}^\alpha = R^\alpha(\cos(\alpha\Theta) e_0 + \sin(\alpha\Theta) \hat{n})$, so

$$
N(\tilde{Q}^\alpha) = R^{2\alpha}(\cos^2(\alpha\Theta) + \sin^2(\alpha\Theta)) = R^{2\alpha} = (R^2)^\alpha = N(\tilde{Q})^\alpha.
$$

In the nilpotent regime, $\tilde{Q}^\alpha = Q_0^\alpha e_0 + \alpha Q_0^{\alpha-1}\mathbf{Q}$, so

$$
N(\tilde{Q}^\alpha) = (Q_0^\alpha)^2 + 0 = Q_0^{2\alpha} = N(\tilde{Q})^\alpha.
$$

The identity is **branch-dependent**: a consistent choice of branch must be made for $R^\alpha$ and $R^{2\alpha}$ (respectively $Q_0^\alpha$ and $Q_0^{2\alpha}$), since the multivaluedness of the power means that the two sides can differ by a phase if inconsistent branches are chosen. Equivalently, one must use a compatible choice of the complex logarithm on both sides of the identity.

**Physical reading: fractional powers and the phase.** The power function is what the framework uses for a fractional power of a field — a square root of a rotor, a half-boost — and its multivaluedness is the two-valuedness of the spinor lift: $\tilde{Q}^{1/2}$ is the spinor of $\tilde{Q}$, the element whose conjugation rotates by half the angle, and the two branches correspond to the two signs of $\hat{n}$, exactly the double cover $S^3 \to SO(3)$ of *Biquaternion Spin Geometry*. The pure nilpotent case is the lightlike fractional power, the parabolic limit whose logarithm does not exist on the algebra.

## Relations to the Quaternion and Complex Cases

### The Quaternion Case

The biquaternion algebra contains the quaternion algebra $\mathbb{H}$ as the subspace $\mathbb{H}_{\mathbb{B}}$, which is the fixed-point set of complex conjugation. For a quaternion $q = q_0 + \mathbf{q}$ with real coefficients, the complex norm $B = |\mathbf{q}|$ is real and non-negative, and the elementary functions reduce to the ordinary quaternion elementary functions:

$$
\exp(q) = e^{q_0}(\cos|\mathbf{q}| + \sin|\mathbf{q}| \, \hat{n}),
$$

$$
\log(q) = \log|q| + \arccos(q_0/|q|) \hat{n},
$$

and so on, where $|q| = \sqrt{q_0^2 + |\mathbf{q}|^2}$ is the quaternion norm. These are the standard formulas of quaternion analysis.

### The Complex Case

The biquaternion algebra contains the complex numbers as the subspace $\mathbb{C}_{\mathbb{B}}$, which is the fixed-point set of quaternion conjugation (the scalar part). For a complex scalar $\tilde{Q} = Q_0 e_0$, the vector part vanishes, and the elementary functions reduce to the ordinary complex elementary functions:

$$
\exp(Q_0 e_0) = e^{Q_0} e_0, \qquad \log(Q_0 e_0) = \log(Q_0) e_0,
$$

and so on. These are the standard formulas of complex analysis, the pure global phase and its logarithm.

### The Relation Between the Two

The quaternion case and the complex case are the two extremes of the biquaternion case: the quaternion case is the case where $B$ is real, and the complex case is the case where $\mathbf{Q} = 0$. The general biquaternion case interpolates between the two, with $B$ complex and $\mathbf{Q}$ nonzero. Physically the quaternion extreme is the spatial rotation sector and the complex extreme is the global phase; the general biquaternion interpolates between the compact rotation sector $S^3$ and the phase $U(1)$ of *Biquaternion Lie Group and Exponential Structure*.

## Non-Commutativity and the One-Variable Case

The elementary functions of a biquaternion variable are as simple as they are because the **vector part is a single element**, and it commutes with itself. Equivalently, all elementary functions of a single biquaternion $\tilde{Q}$ lie in the **commutative subalgebra** $\mathbb{C}[\tilde{Q}]$ generated by $\tilde{Q}$ and $e_0$. In the oscillatory regime or the nonzero nilpotent regime, this subalgebra is exactly two-dimensional over $\mathbb{C}$, and it is isomorphic either to $\mathbb{C} \times \mathbb{C}$ (in the oscillatory regime) or to $\mathbb{C}[\epsilon]/(\epsilon^2)$ (in the nilpotent regime). Within either isomorphism type, the standard complex-analytic identities — including the Pythagorean identity, the hyperbolic identity, the double-angle formulas, and the relation between the exponential and the trigonometric functions — hold, because the algebra is commutative.

The powers of $\mathbf{Q}$ are determined by the single relation $\mathbf{Q}^2 = -B^2 e_0$ (in the oscillatory regime) or $\mathbf{Q}^2 = 0$ (in the nilpotent regime), and the whole power series can be summed in closed form. The two cases correspond to the two isomorphism types of $\mathbb{C}[\tilde{Q}]$.

For functions of **two or more biquaternion variables**, the situation is different. The powers of a sum $\tilde{P} + \tilde{Q}$ involve the products $\tilde{P} \tilde{Q}$ and $\tilde{Q} \tilde{P}$, which are not equal in general. The binomial expansion does not hold, and the exponential of a sum is not in general the product of the exponentials when the two biquaternions do not commute. So the elementary functions of several biquaternion variables are much more complicated than the elementary functions of one variable, and their theory is largely open.

This is the fundamental reason the theory of the elementary functions of a biquaternion variable is tractable, while the theory of functions of several biquaternion variables is not — and the physical reason the framework represents a *single* field, not a collection, by an element of the algebra, with the multi-field structure carried by the module and operator layer.

## Collected Formulas

| Function | $B \neq 0$ | $B = 0$ |
|---|---|---|
| $\exp(\tilde{Q})$ | $e^{Q_0}(\cos B \, e_0 + \sin B \, \hat{n})$ | $e^{Q_0}(e_0 + \mathbf{Q})$ |
| $\sin(\tilde{Q})$ | $\sin(Q_0) \cosh B \, e_0 + \cos(Q_0) \sinh B \, \hat{n}$ | $\sin(Q_0) e_0 + \cos(Q_0) \mathbf{Q}$ |
| $\cos(\tilde{Q})$ | $\cos(Q_0) \cosh B \, e_0 - \sin(Q_0) \sinh B \, \hat{n}$ | $\cos(Q_0) e_0 - \sin(Q_0) \mathbf{Q}$ |
| $\sinh(\tilde{Q})$ | $\sinh(Q_0) \cos B \, e_0 + \cosh(Q_0) \sin B \, \hat{n}$ | $\sinh(Q_0) e_0 + \cosh(Q_0) \mathbf{Q}$ |
| $\cosh(\tilde{Q})$ | $\cosh(Q_0) \cos B \, e_0 + \sinh(Q_0) \sin B \, \hat{n}$ | $\cosh(Q_0) e_0 + \sinh(Q_0) \mathbf{Q}$ |
| $\log(\tilde{Q})$ | $\log R \, e_0 + \Theta \hat{n}$ | $\log Q_0 \, e_0 + \mathbf{Q}/Q_0$ |
| $\tilde{Q}^\alpha$ | $R^\alpha(\cos(\alpha\Theta) \, e_0 + \sin(\alpha\Theta) \, \hat{n})$ | $Q_0^\alpha e_0 + \alpha Q_0^{\alpha-1} \mathbf{Q}$ |

In the table, $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$, $\hat{n} = \mathbf{Q}/B$, $R = \sqrt{Q_0^2 + B^2}$, $\cos\Theta = Q_0/R$, and $\sin\Theta = B/R$. The exponential, the trigonometric functions and the hyperbolic functions are defined for every $\tilde{Q} \in \mathbb{B}$. The logarithm and the power function are defined only on the group of units $N(\tilde{Q}) \neq 0$; in the second column, the formulas for the logarithm and the power function assume $Q_0 \neq 0$, which is automatically implied by $N(\tilde{Q}) \neq 0$ when $B = 0$.

## Open Questions

1. **Functions of several biquaternion variables.** How do the elementary functions extend to functions of two or more biquaternion variables? The non-commutativity is a serious obstruction, and the theory is largely open.

2. **The transition between the two regimes.** As $B \to 0$, the oscillatory formulas degenerate into the nilpotent ones. What is the precise nature of this degeneration? Is there a uniform asymptotic expansion that interpolates between the two regimes, the parabolic limit of a boost as the rapidity tends to infinity?

3. **The complex norm.** What is the geometric or algebraic meaning of the complex norm $B$ when it is not real? The complex norm is a square root of the biquaternion norm, and it is complex for a general biquaternion, but its interpretation is not clear. In particular, $B$ is the analogue of the "magnitude" of the vector part, but its complex-valuedness means it has both a modulus and a phase.

4. **The relation to the analysis.** How do the elementary functions interact with the differential operators of *Biquaternion Analysis*? For example, what is $\tilde{\nabla} \exp(\tilde{Q})$ for a general biquaternion $\tilde{Q}$?

5. **The logarithm at the boundary of the group of units.** The logarithm exists on $\mathbb{B}^\times$ but not on its boundary, which is the zero divisor set $\mathcal{Z}$ together with $0$. What is the correct object that replaces the logarithm on the boundary? The answer is likely to involve a formal logarithm or a deformation of the algebra, and physically it is the phase of a lightlike field, which is the light-cone problem of *Biquaternion Analysis on Subspaces* and *The Wave Equation on $\mathbb{M}_-$*.

6. **The derivative of the exponential in the vector directions.** The formula $\partial_k \exp(\tilde{Q}) = \int_0^1 e^{s \tilde{Q}} e_k e^{(1-s)\tilde{Q}}\,ds$ is the biquaternion analogue of the usual identity for the derivative of the exponential. What are the consequences of this formula for the analysis of biquaternion-valued functions?

## Summary

Every elementary function is defined by applying the scalar power series to $\tilde{Q}$, and all its values lie in the commutative subalgebra $\mathbb{C}[\tilde{Q}]$ generated by $\tilde{Q}$. This is why the standard identities of complex analysis — the Pythagorean identity, the hyperbolic identity, the double-angle formulas, the relation between the exponential and the trigonometric functions — survive the non-commutativity of $\mathbb{B}$ for a single variable; the addition formulas for two independent biquaternions do not, and fail for explicit counterexamples such as $\tilde{P} = e_1$, $\tilde{Q} = e_2$.

The structure of $\mathbb{C}[\tilde{Q}]$ is governed by the discriminant and yields exactly two regimes. In the **oscillatory regime** $B \neq 0$ the subalgebra is $\mathbb{C} \times \mathbb{C}$, the element $\tilde{Q}$ is diagonalisable with eigenvalues $Q_0 \pm iB$, and the closed forms are the oscillatory-hyperbolic expressions of the collected table, built on $\tilde{Q} = Q_0 e_0 + B\hat{n}$ with $\hat{n}^2 = -e_0$. In the **nilpotent regime** $B = 0$, $\mathbf{Q} \neq 0$, the subalgebra is $\mathbb{C}[\epsilon]/(\epsilon^2)$ with the nilpotent $\epsilon = \mathbf{Q}$, and every power series truncates after the linear term: the exponential becomes $e^{Q_0}(e_0 + \mathbf{Q})$, the logarithm becomes $\log Q_0\,e_0 + \mathbf{Q}/Q_0$, and the higher functions reduce to their first-order Taylor expansions in $\mathbf{Q}$.

The exponential is the model of the theory. It is never zero, it satisfies $\exp(\tilde{P}+\tilde{Q}) = \exp(\tilde{P})\exp(\tilde{Q})$ when $\tilde{P}$ and $\tilde{Q}$ commute (the converse can fail), and the logarithm inverts it on the group of units, using the decomposition $\tilde{Q} = R(\cos\Theta\,e_0 + \sin\Theta\,\hat{n})$ with $R = \sqrt{N(\tilde{Q})}$, $\cos\Theta = Q_0/R$ and $\sin\Theta = B/R$, from which the power function $\tilde{Q}^{\alpha}$ is obtained. Because the scalar imaginary $i$ commutes with everything, it relates the trigonometric functions to the exponential and the trigonometric to the hyperbolic functions, but only for a single argument in a common plane.

Physically the trichotomy $\nu^2 = -1, 0, +1$ is the classification of the motions: the oscillation of a quantum phase, the parabolic twist along a null direction, and the hyperbolic boost of a rapidity, with the hyperbolic family non-compact and unbounded as the rapidity tends to infinity. The exponential, the trigonometric and the hyperbolic functions are defined for every $\tilde{Q} \in \mathbb{B}$; the logarithm and the power function are defined only on the group of units $N(\tilde{Q}) \neq 0$, which is the statement that only a non-null field has a phase, and the logarithm there is many-valued, the ambiguity coming from the multi-valuedness of $\Theta$ and of the scalar logarithm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ | Biquaternion; $\mathbf{Q} = \sum_k Q_k e_k$ the vector part |
| $B = \sqrt{Q_1^2+Q_2^2+Q_3^2}$ | Complex norm of the vector part |
| $\hat{n} = \mathbf{Q}/B$ | Axis of the vector part, $\hat{n}^2 = -e_0$, defined for $B \neq 0$ |
| $R = \sqrt{Q_0^2+B^2} = \sqrt{N(\tilde{Q})}$ | Modulus of the logarithm and the power function |
| $\Theta$ | Angle of the logarithm and the power function, $\cos\Theta = Q_0/R$, $\sin\Theta = B/R$ |
| $\mathbb{C}[\tilde{Q}]$ | Commutative subalgebra generated by $\tilde{Q}$; it contains every value $F(\tilde{Q})$ |
| Oscillatory regime | $B \neq 0$: $\mathbb{C}[\tilde{Q}] \cong \mathbb{C} \times \mathbb{C}$, diagonalisable case; the elliptic and hyperbolic motions |
| Nilpotent regime | $B = 0$, $\mathbf{Q} \neq 0$: $\mathbb{C}[\tilde{Q}] \cong \mathbb{C}[\epsilon]/(\epsilon^2)$, $\epsilon = \mathbf{Q}$; the parabolic, lightlike motion |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Biquaternion norm; $N \neq 0$ is the group of units, the domain of $\log$ and of powers |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of the quaternion exponential and logarithm.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the elementary functions of biquaternions.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the exponential of complexified quaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the classification of the roots of $-1$ that serve as axes of the vector part.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the zero divisors and nilpotents.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the connection to Clifford algebras.
