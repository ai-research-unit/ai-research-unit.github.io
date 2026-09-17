
# Biquaternion Polar Representations

## Introduction

The article on biquaternion algebraic representations described four ways of writing a biquaternion using only the algebra operations, the scalar imaginary, and the underlying complex vector space structure: the four-vector representation, the $2 \times 2$ matrix representation, the spinor representation, and the Clifford algebra representation.

This article describes the **polar representations** of the biquaternion algebra: ways of writing a biquaternion as a product of a modulus and an exponential. These representations use the exponential and the roots of $-1$, and they are therefore not algebraic in the sense of the preceding article.

The word "representation" is used here in the sense of "a concrete realization of the algebra as a collection of computable objects." It is not used in the technical sense of algebra representation theory.

For a complex number, the polar form is unique up to the sign of the modulus: $z = r e^{i\theta}$ with $r \geq 0$ and $\theta \in \mathbb{R}$. For a biquaternion, neither the modulus nor the root of $-1$ in the exponential is unique, and this is the reason there are **two** natural polar representations rather than one. The choice of which root of $-1$ to use in the exponential, and which factor to call the modulus, gives the two forms: the **Hamilton polar form** and the **complex polar form**. This article defines both, compares them, and describes their behavior under the four conjugations.

Throughout, we use the notation of the basic algebra article: a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C},
$$

with $e_0 = 1$ and $e_1, e_2, e_3$ the quaternion units. The scalar imaginary is $i$, which commutes with the quaternion units. The norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$, and the four fixed-point subspaces are $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, and $\mathbb{M}_-$.

## Why There Are Two Polar Forms

The polar form of a complex number $z$ is

$$
z = r e^{i\theta}, \qquad r = |z| \geq 0, \quad \theta \in \mathbb{R}.
$$

Two features are essential:

- The modulus $r$ is a **non-negative real number**, and it is the unique such number with $r^2 = |z|^2$.
- The exponential uses the **only** root of $-1$ available in $\mathbb{C}$, namely $i$ (up to sign).

For a biquaternion, neither feature survives unchanged.

**The modulus is not necessarily real.** The norm form $N(\tilde{Q})$ is a complex number in general, and its square root is a complex number, not a real number. There is no canonical way to choose a non-negative real modulus.

**There is more than one root of $-1$.** The biquaternion algebra contains a four-real-dimensional family of roots of $-1$, of which only one (up to sign), namely the scalar imaginary $i$, is central. The other roots are non-central and are classified in the article on biquaternion roots of minus one.

The two polar forms arise from the two possible choices:

- The **Hamilton polar form** uses a **non-central** root $\xi$ of $-1$ in the exponential, and calls the complex scalar $R$ the modulus.
- The **complex polar form** uses the **central** root $i$ of $-1$ in the exponential, and calls the real quaternion $Q$ the modulus.

The names are historical. The Hamilton form generalizes the quaternion polar form $q = r \exp(\mu \theta)$ discovered by Hamilton, in which $\mu$ is a unit pure real quaternion. The complex form generalizes the ordinary complex polar form $z = r \exp(i\theta)$.

## The Hamilton Polar Form

### Definition

Let $\tilde{Q}$ be a biquaternion with non-vanishing norm form. Write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ is the vector part, and suppose $\mathbf{Q} \neq 0$. The **Hamilton polar form** of $\tilde{Q}$ is

$$
\tilde{Q} = R \exp(\xi \Theta) = R(\cos\Theta + \xi \sin\Theta),
$$

where:

- $R = \sqrt{N(\tilde{Q})}$ is the **complex modulus**, a complex scalar;
- $\xi = \mathbf{Q}/B$ is the **axis**, a root of $-1$ in $\mathbb{B}$, where $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ is the complex modulus of the vector part;
- $\Theta$ is the **complex angle**, defined by $\cos\Theta = Q_0/R$ and $\sin\Theta = B/R$.

The axis $\xi$ is a pure biquaternion satisfying $\xi^2 = -1$, and it is chosen to be **parallel to the vector part** of $\tilde{Q}$. It is one of the non-central roots of $-1$ when the vector part has both real and imaginary components, and it is a unit pure real quaternion when the vector part is real.

### The Case $\mathbf{Q} = 0$

If the vector part vanishes, $\tilde{Q} = Q_0 e_0$ is a complex scalar, and the Hamilton polar form is not defined (because $\xi$ cannot be normalized). In this case, the complex polar form is the appropriate one.

### The Case $N(\tilde{Q}) = 0$

If the norm form vanishes, $\tilde{Q}$ is a zero divisor, and $R = 0$. The Hamilton polar form degenerates: either $Q_0 = 0$ (pure case) or $Q_0 \neq 0$ (non-pure case), and in both cases the representation as a modulus times an exponential is not available in the same form. The zero divisors are treated in the article on biquaternion zero divisors.

### Existence and Uniqueness

**Theorem.** Every biquaternion $\tilde{Q}$ with $\mathbf{Q} \neq 0$ and $N(\tilde{Q}) \neq 0$ has a Hamilton polar form. The form is unique up to the sign of $R$ and the sign of $\Theta$, which are correlated: replacing $(R, \Theta)$ by $(-R, \Theta + \pi)$ gives the same $\tilde{Q}$.

**Proof.** The construction above gives $\xi$, $R$, and $\Theta$ explicitly from the components of $\tilde{Q}$. The verification that $\tilde{Q} = R(\cos\Theta + \xi \sin\Theta)$ is a direct computation:

$$
R(\cos\Theta + \xi \sin\Theta) = R \cdot \frac{Q_0}{R} + R \cdot \frac{\mathbf{Q}}{B} \cdot \frac{B}{R} = Q_0 + \mathbf{Q} = \tilde{Q}.
$$

The uniqueness follows from the fact that $\xi$ is determined by the direction of $\mathbf{Q}$, and $R$ and $\Theta$ are determined by the equations $\cos\Theta = Q_0/R$ and $\sin\Theta = B/R$, up to the correlated sign choice. $\square$

### The Constraint on the Axis

The axis $\xi$ is not an arbitrary root of $-1$: it is the root parallel to the vector part $\mathbf{Q}$. This is a constraint, and it is the reason the Hamilton polar form is well-defined.

The roots of $-1$ that arise this way are characterized by the constraints

$$
\Re(\xi) \perp \Im(\xi), \qquad \|\Re(\xi)\| - \|\Im(\xi)\| = 1,
$$

which are stated and proved in the article on biquaternion roots of minus one. The axis of the Hamilton polar form is therefore one of the non-trivial roots of $-1$, unless the vector part $\mathbf{Q}$ happens to be a real quaternion, in which case the axis is a unit pure real quaternion (a "real root" of $-1$ in the classification of that article).

### The Angle Is Complex

The angle $\Theta$ is a complex number, not a real one. This is because both $Q_0$ and $B$ are complex, and their ratio $Q_0/B$ is a complex number. There is no canonical way to choose a real angle.

### Example

Take $\tilde{Q} = e_0 + e_1$. Then $Q_0 = 1$, $\mathbf{Q} = e_1$, $B = \sqrt{1} = 1$, and $N(\tilde{Q}) = 1 + 1 = 2$. So $R = \sqrt{2}$, $\xi = e_1$, $\cos\Theta = 1/\sqrt{2}$, $\sin\Theta = 1/\sqrt{2}$. So $\Theta = \pi/4$ (up to the addition of $2\pi$ in the real part, and up to the complex ambiguity), and

$$
\tilde{Q} = \sqrt{2} \exp(e_1 \pi/4) = \sqrt{2} (\cos(\pi/4) + e_1 \sin(\pi/4)) = 1 + e_1.
$$

This is the case of a quaternion with a positive real norm form, and the Hamilton polar form reduces to the ordinary quaternion polar form, with $\Theta$ real.

## The Complex Polar Form

### Definition

Let $\tilde{Q}$ be a biquaternion with non-vanishing real part $Q_0$. Write $\tilde{Q} = Q_r + i Q_i$ where $Q_r, Q_i \in \mathbb{H}$ are the real and imaginary quaternion parts. The **complex polar form** of $\tilde{Q}$ is

$$
\tilde{Q} = Q \exp(i \Psi) = Q(\cos\Psi + i \sin\Psi),
$$

where:

- $Q$ is a **quaternion** (a real quaternion, element of $\mathbb{H}$);
- $i$ is the **scalar imaginary**, the central root of $-1$ that commutes with everything;
- $\Psi$ is the **complex angle**, defined by $\tan\Psi = Q_r^{-1} Q_i$, and $Q = \tilde{Q} \exp(-i\Psi)$.

### The Case $Q_r = 0$

If the real part vanishes, $\tilde{Q}$ is purely imaginary, and the complex polar form is not defined (because $Q_r^{-1}$ does not exist). In this case, the Hamilton polar form is the appropriate one.

### The Case $N(\tilde{Q}) = 0$

If the norm form vanishes, $\tilde{Q}$ is a zero divisor. The complex polar form is not available in general, because the quaternion $Q$ may not be invertible. The zero divisors are treated in the article on biquaternion zero divisors.

### Existence and Uniqueness

**Theorem.** Every biquaternion $\tilde{Q}$ with $Q_r \neq 0$ and $N(\tilde{Q}) \neq 0$ has a complex polar form. The form is unique up to the addition of $2\pi$ to the real part of $\Psi$.

**Proof.** The construction above gives $\Psi$ and $Q$ explicitly from $\tilde{Q}$. The verification that $\tilde{Q} = Q \exp(i\Psi)$ is a direct computation:

$$
Q \exp(i\Psi) = \tilde{Q} \exp(-i\Psi) \exp(i\Psi) = \tilde{Q},
$$

where the second equality uses the fact that $i$ commutes with $\tilde{Q}$ and $\exp(-i\Psi)$ commutes with $\exp(i\Psi)$. The uniqueness follows from the fact that $\Psi$ is determined by the equation $\tan\Psi = Q_r^{-1} Q_i$, which determines $\Psi$ up to the addition of $\pi$ in the real part, with the sign of $Q$ adjusted accordingly. $\square$

### The Angle Is Complex

As in the Hamilton polar form, the angle $\Psi$ is a complex number, not a real one. This is because $Q_r^{-1} Q_i$ is a quaternion, not a real number, and its tangent is a complex angle.

### The Modulus Is a Quaternion

The modulus $Q$ is a real quaternion, not a complex scalar. This is the essential difference from the Hamilton polar form, where the modulus is a complex scalar.

### Example

Take $\tilde{Q} = 1 + i$, a complex scalar. Then $Q_r = 1$ and $Q_i = 1$, so $\tan\Psi = 1$, i.e., $\Psi = \pi/4$ (up to the addition of $\pi$ in the real part). And $Q = (1+i) \exp(-i\pi/4) = (1+i)(\cos(\pi/4) - i \sin(\pi/4)) = (1+i)(1/\sqrt{2} - i/\sqrt{2}) = \sqrt{2}$. So

$$
\tilde{Q} = \sqrt{2} \exp(i \pi/4).
$$

This is exactly the ordinary polar form of the complex number $1 + i$. So in the case of a scalar biquaternion, the complex polar form reduces to the ordinary complex polar form.

### A Non-Scalar Example

Take $\tilde{Q} = e_0 + i e_1$. Then $Q_r = e_0$ and $Q_i = e_1$, so $\tan\Psi = e_0^{-1} e_1 = e_1$, i.e., $\Psi = \arctan(e_1)$, which is a complex angle with real part $\pi/4$ and imaginary part $0$ in the quaternion basis. The modulus is $Q = \tilde{Q} \exp(-i\Psi)$, which is a real quaternion. The exact form of $Q$ depends on the branch of the arctangent, but the representation is well-defined.

## Comparison of the Two Polar Forms

The two polar forms differ in **which root of $-1$ is used in the exponential** and in **which factor is the modulus**:

| | Hamilton polar form | Complex polar form |
|---|---|---|
| Root of $-1$ | $\xi$, a non-central root | $i$, the central root |
| Modulus | $R$, a complex scalar | $Q$, a real quaternion |
| Angle | $\Theta$, a complex scalar | $\Psi$, a complex scalar |
| Existence requires | $\mathbf{Q} \neq 0$ | $Q_r \neq 0$ |
| Reduces to | Quaternion polar form (when $\tilde{Q} \in \mathbb{H}$) | Complex polar form (when $\tilde{Q} \in \mathbb{C}_{\mathbb{B}}$) |

### When Each Form Is Natural

The two polar forms are complementary. The Hamilton form generalizes the quaternion polar form, with the quaternion root $\mu$ replaced by a biquaternion root $\xi$, and the modulus and angle allowed to become complex. The complex form generalizes the complex polar form, with the scalar imaginary $i$ retained as the root, and the modulus allowed to become a quaternion.

The choice between the two polar forms depends on what is being computed:

- The **Hamilton polar form** is natural when the biquaternion is close to a quaternion, i.e., when the complexification is a small perturbation. The root $\xi$ is close to a pure real quaternion, and the exponential is close to the quaternion exponential.
- The **complex polar form** is natural when the biquaternion is close to a complex scalar, i.e., when the quaternion structure is a small perturbation. The modulus $Q$ is close to a complex scalar, and the exponential is close to the ordinary complex exponential.

In the case of a biquaternion that is neither close to a quaternion nor close to a complex scalar, neither polar form is canonical, and the choice is a matter of convenience.

### The Domain of Definition

The two polar forms are defined on overlapping but different domains:

- The Hamilton polar form is defined for $\mathbf{Q} \neq 0$ and $N(\tilde{Q}) \neq 0$.
- The complex polar form is defined for $Q_r \neq 0$ and $N(\tilde{Q}) \neq 0$.

The union of the two domains covers all biquaternions with $N(\tilde{Q}) \neq 0$ except those with $\mathbf{Q} = 0$ and $Q_r = 0$ simultaneously, i.e., the purely imaginary complex scalars $\tilde{Q} = i Q'_0 e_0$. These are the only biquaternions with non-vanishing norm form for which neither polar form is defined in the standard sense.

## The Role of the Roots of Minus One

The two polar forms correspond to the two classes of roots of $-1$ in $\mathbb{B}$:

- The **scalar imaginary** $i$ is the unique central root of $-1$ (up to sign). It is the root used in the complex polar form.
- The **non-central roots** $\xi$ of $-1$, of the form $\xi = b\mu + d i \nu$ with $\mu \perp \nu$ and $b^2 - d^2 = 1$, are the roots used in the Hamilton polar form. They form a four-dimensional family, parametrized by a pair of perpendicular unit pure real quaternions $\mu, \nu$ and a real parameter $b$ with $b^2 - d^2 = 1$.

The existence of the non-central roots is the reason the Hamilton polar form differs from the complex one. In the complex numbers, only the central root exists, and there is only one polar form. In the biquaternions, the central root and the non-central roots coexist, and the two polar forms reflect the two possibilities.

The classification of the roots of $-1$ is the subject of the article on biquaternion roots of minus one. The results are:

1. **Non-trivial roots:** $\xi = b\mu + d\nu i$, where $\mu$ and $\nu$ are perpendicular unit pure real quaternions, and $b, d \in \mathbb{R}$ satisfy $b^2 - d^2 = 1$.
2. **The trivial root:** $\xi = \pm i$.
3. **The real roots:** $\xi = \pm \mu$, where $\mu$ is a unit pure real quaternion.

The axis of the Hamilton polar form is a real root when the vector part is a real quaternion, and a non-trivial root when the vector part has both real and imaginary components.

## Behavior Under the Four Conjugations

The three conjugations of the biquaternion algebra act on the two polar forms as follows. Throughout, the scalar imaginary $i$ is treated as a complex scalar, so it is conjugated by $^*$ and preserved by $\bar{\cdot}$.

### Quaternion Conjugation

**Hamilton form.** $\bar{R \exp(\xi \Theta)} = \bar{R} \exp(\bar{\xi} \bar{\Theta})$. Since $\bar{R} = R$ (the norm form is invariant under quaternion conjugation, so $R$ is invariant up to sign), $\bar{\xi} = -\xi$ (the quaternion conjugate of a pure biquaternion is its negative), and $\bar{\Theta} = \Theta$ (the angle is a complex scalar and is not affected by quaternion conjugation), we get

$$
\bar{R \exp(\xi \Theta)} = R \exp(-\xi \Theta).
$$

So quaternion conjugation reverses the sign of the angle in the Hamilton polar form.

**Complex form.** $\bar{Q \exp(i \Psi)} = \bar{Q} \exp(i \Psi)$. Since $i$ commutes with the quaternion conjugate, the sign of the angle is not affected, and only the quaternion modulus is conjugated.

### Complex Conjugation

**Hamilton form.** $(R \exp(\xi \Theta))^* = R^* \exp(\xi^* \Theta^*)$. The modulus is conjugated, and both the root and the angle are conjugated. Since the norm form transforms as $N(\tilde{Q}^*) = N(\tilde{Q})^*$, we have $R^* = \sqrt{N(\tilde{Q})^*} = \sqrt{N(\tilde{Q}^*)}$, which is consistent.

**Complex form.** $(Q \exp(i \Psi))^* = Q^* \exp(-i \Psi^*)$. Since $i^* = -i$, the sign of the exponential is reversed, and both the modulus and the angle are conjugated.

### Hermitian Conjugation

**Hamilton form.** $(R \exp(\xi \Theta))^\dagger = (R^* \exp(\xi^* \Theta^*))$ with the additional quaternion conjugation, which reverses the sign of the angle:

$$
(R \exp(\xi \Theta))^\dagger = R^* \exp(-\xi^* \Theta^*).
$$

**Complex form.** $(Q \exp(i \Psi))^\dagger = Q^\dagger \exp(i \Psi^*)$. The quaternion modulus is Hermitian-conjugated, and the angle is complex-conjugated.

### Summary

| Conjugation | Hamilton form | Complex form |
|---|---|---|
| Quaternion $\bar{\cdot}$ | $\xi \to -\xi$ | $Q \to \bar{Q}$ |
| Complex $^*$ | $R \to R^*$, $\xi \to \xi^*$, $\Theta \to \Theta^*$ | $Q \to Q^*$, $\Psi \to -\Psi^*$ |
| Hermitian $\dagger$ | $R \to R^*$, $\xi \to -\xi^*$, $\Theta \to \Theta^*$ | $Q \to Q^\dagger$, $\Psi \to \Psi^*$ |

The two polar forms respond differently to the three conjugations, and the choice of polar form determines which conjugation is "natural" for the expression.

## The Relation to the Algebraic Representations

The polar representations are related to the algebraic representations as follows.

**Relation to the matrix representation.** The polar form of a biquaternion is the analogue of the polar decomposition of the corresponding $2 \times 2$ complex matrix. The Hamilton form corresponds to the **polar decomposition** $M = U P$ where $U$ is unitary and $P$ is positive semidefinite, but with the roles of the modulus and the phase interchanged. The complex form corresponds to the **Jordan decomposition** of the matrix into its complex scalar and quaternion parts.

**Relation to the four-vector representation.** The Hamilton polar form separates the four-vector into a "magnitude" $R$ and a "direction" $\xi$, in analogy with the polar form of a vector. The complex polar form separates the four-vector into its "real" and "imaginary" quaternion parts, and then polar-decomposes the imaginary part relative to the real part.

**Relation to the Clifford algebra representation.** The polar forms are not naturally expressed in the Clifford algebra representation, because the Clifford algebra is a real algebra and the polar forms use the complex scalar imaginary. However, the Clifford algebra does provide a natural setting for the roots of $-1$ and for the spinor structure that underlies the polar forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde{Q}$ | Biquaternion |
| $Q_0$ | Complex scalar part |
| $\mathbf{Q}$ | Complex vector part |
| $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ | Complex modulus of the vector part |
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ | Norm form |
| $R = \sqrt{N(\tilde{Q})}$ | Complex modulus (Hamilton) |
| $\xi = \mathbf{Q}/B$ | Axis (root of $-1$, Hamilton) |
| $\Theta$ | Complex angle (Hamilton) |
| $Q_r, Q_i$ | Real and imaginary quaternion parts |
| $Q$ | Quaternion modulus (complex form) |
| $\Psi$ | Complex angle (complex form) |
| $i$ | Scalar imaginary |

## Summary

The biquaternion algebra has **two** natural polar representations:

- The **Hamilton polar form** $\tilde{Q} = R \exp(\xi \Theta)$, where $R$ is a complex scalar modulus, $\xi$ is a non-central root of $-1$ parallel to the vector part, and $\Theta$ is a complex angle.
- The **complex polar form** $\tilde{Q} = Q \exp(i \Psi)$, where $Q$ is a real quaternion modulus, $i$ is the central root of $-1$, and $\Psi$ is a complex angle.

The two forms are complementary. The Hamilton form generalizes the quaternion polar form and is natural when the biquaternion is close to a quaternion. The complex form generalizes the ordinary complex polar form and is natural when the biquaternion is close to a complex scalar.

The existence of the two forms is a consequence of the existence of two classes of roots of $-1$ in the biquaternion algebra: the central root $i$, and the four-real-dimensional family of non-central roots $\xi = b\mu + d\nu i$ with $\mu \perp \nu$ and $b^2 - d^2 = 1$. The classification of these roots is the subject of the article on biquaternion roots of minus one.

The two forms behave differently under the four conjugations of the algebra, and this difference is the algebraic content of the distinction between them.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation of the quaternion polar form.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the polar representations of biquaternions.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the two polar forms in the applied context.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the classification of the roots of $-1$ on which the two polar forms depend.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.

