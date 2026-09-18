
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

Let $\tilde{Q}$ be a biquaternion with non-vanishing norm form. Write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ is the vector part, and suppose that the vector part is not null, i.e.

$$
(\mathbf{Q}, \mathbf{Q}) = Q_1^2 + Q_2^2 + Q_3^2 \neq 0,
$$

equivalently $B = \sqrt{(\mathbf{Q}, \mathbf{Q})} \neq 0$. The **Hamilton polar form** of $\tilde{Q}$ is

$$
\tilde{Q} = R \exp(\xi \Theta) = R(\cos\Theta + \xi \sin\Theta),
$$

where:

- $R = \sqrt{N(\tilde{Q})}$ is the **complex modulus**, a complex scalar;
- $\xi = \mathbf{Q}/B$ is the **axis**, a root of $-1$ in $\mathbb{B}$, where $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ is a complex square root of $(\mathbf{Q}, \mathbf{Q})$;
- $\Theta$ is the **complex angle**, defined by $\cos\Theta = Q_0/R$ and $\sin\Theta = B/R$.

The axis $\xi$ is a pure biquaternion satisfying $\xi^2 = -1$, and it is chosen to be **parallel to the vector part** of $\tilde{Q}$. Indeed, $\xi^2 = \mathbf{Q}^2/B^2 = -(\mathbf{Q},\mathbf{Q})/B^2 = -1$, using the identity $\mathbf{Q}^2 = -(\mathbf{Q},\mathbf{Q}) e_0$ for pure biquaternions.

### The Case $(\mathbf{Q}, \mathbf{Q}) = 0$

If the vector part is null — that is, $(\mathbf{Q}, \mathbf{Q}) = 0$ — then $B = 0$ and the axis $\xi$ cannot be normalized. Two sub-cases arise:

- **Complex scalar case.** If $\mathbf{Q} = 0$, then $\tilde{Q} = Q_0 e_0$ is a complex scalar, and the Hamilton polar form is not defined. This case is discussed in the section on the domain of definition below.
- **Nilpotent case.** If $\mathbf{Q} \neq 0$ but $(\mathbf{Q}, \mathbf{Q}) = 0$, then $\mathbf{Q}$ is a nilpotent ($\mathbf{Q}^2 = 0$). If $Q_0 \neq 0$, then $\tilde{Q}$ is invertible and can be written as
  $$
  \tilde{Q} = Q_0 \exp(\mathbf{Q}/Q_0),
  $$
  since $\exp(t\mathbf{Q}) = 1 + t\mathbf{Q}$ for any complex scalar $t$ (because $\mathbf{Q}^2 = 0$). This is a polar-like form with a **nilpotent angle** $\mathbf{Q}/Q_0$, and it is not of the Hamilton form $R\exp(\xi\Theta)$ with $\xi^2 = -1$. The Hamilton polar form is therefore unavailable in this case.

### The Case $N(\tilde{Q}) = 0$

If the norm form vanishes, $\tilde{Q}$ is a zero divisor, and $R = 0$. The Hamilton polar form degenerates: either $Q_0 = 0$ (pure case) or $Q_0 \neq 0$ (non-pure case), and in both cases the representation as a modulus times an exponential is not available in the same form. The zero divisors are treated in the article on biquaternion zero divisors.

### Existence and Uniqueness

**Theorem.** Every biquaternion $\tilde{Q}$ with $B \neq 0$ and $N(\tilde{Q}) \neq 0$ has a Hamilton polar form. The form is unique up to the sign of $R$ and the sign of $\Theta$, which are correlated: replacing $(R, \Theta)$ by $(-R, \Theta + \pi)$ gives the same $\tilde{Q}$.

**Proof.** The construction above gives $\xi$, $R$, and $\Theta$ explicitly from the components of $\tilde{Q}$. The verification that $\tilde{Q} = R(\cos\Theta + \xi \sin\Theta)$ is a direct computation:

$$
R(\cos\Theta + \xi \sin\Theta) = R \cdot \frac{Q_0}{R} + R \cdot \frac{\mathbf{Q}}{B} \cdot \frac{B}{R} = Q_0 + \mathbf{Q} = \tilde{Q}.
$$

The consistency condition $\cos^2\Theta + \sin^2\Theta = 1$ follows from

$$
\cos^2\Theta + \sin^2\Theta = \frac{Q_0^2}{R^2} + \frac{B^2}{R^2} = \frac{Q_0^2 + (\mathbf{Q},\mathbf{Q})}{N(\tilde{Q})} = 1.
$$

The uniqueness follows from the fact that $\xi$ is determined by the direction of $\mathbf{Q}$, and $R$ and $\Theta$ are determined by the equations $\cos\Theta = Q_0/R$ and $\sin\Theta = B/R$, up to the correlated sign choice. $\square$

### The Constraint on the Axis

The axis $\xi$ is not an arbitrary root of $-1$: it is the root parallel to the vector part $\mathbf{Q}$. This is a constraint, and it is the reason the Hamilton polar form is well-defined.

The roots of $-1$ that arise this way are characterized by the constraints

$$
\Re(\xi) \perp \Im(\xi), \qquad \|\Re(\xi)\|^2 - \|\Im(\xi)\|^2 = 1,
$$

which are stated and proved in the article on biquaternion roots of minus one. Here $\Re(\xi)$ and $\Im(\xi)$ denote the real and imaginary parts of $\xi$ with respect to the scalar imaginary $i$, and $\|\cdot\|$ denotes the quaternion norm on $\mathbb{H}$. These constraints are satisfied by the non-central roots of $-1$: the non-trivial roots (with both real and imaginary parts nonzero and perpendicular) and the real roots (with vanishing imaginary part).

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

Let $\tilde{Q}$ be a biquaternion with non-vanishing norm form. Write $\tilde{Q} = Q_r + i Q_i$ where $Q_r, Q_i \in \mathbb{H}$ are the **real and imaginary quaternion parts** of $\tilde{Q}$ (i.e., the parts whose coefficients are respectively real and purely imaginary). Suppose $Q_r \neq 0$, which for the division algebra $\mathbb{H}$ is equivalent to $Q_r$ being invertible. The **complex polar form** of $\tilde{Q}$ is

$$
\tilde{Q} = Q \exp(i \Psi) = Q(\cos\Psi + i \sin\Psi),
$$

where:

- $Q$ is a **quaternion** (a real quaternion, element of $\mathbb{H}$);
- $i$ is the **scalar imaginary**, the central root of $-1$ that commutes with everything;
- $\Psi$ is the **quaternion angle**, a real quaternion defined by $\tan\Psi = Q_r^{-1} Q_i$, and $Q = Q_r (\cos\Psi)^{-1}$.

The angle $\Psi$ is a real quaternion (element of $\mathbb{H}$), and $Q$ is a real quaternion. The exponential $\exp(i\Psi) = \cos\Psi + i\sin\Psi$ is a biquaternion, since $i$ is the scalar imaginary and $\cos\Psi, \sin\Psi$ are real quaternions.

### The Case $Q_r = 0$

If the real quaternion part vanishes, $\tilde{Q}$ is purely imaginary (all coefficients are purely imaginary), and the complex polar form is not defined (because $Q_r^{-1}$ does not exist). In this case, the Hamilton polar form may be the appropriate one, provided $B \neq 0$; and if both $Q_r = 0$ and $B = 0$, then neither polar form as constructed here applies. See the section on the domain of definition below.

### The Case $N(\tilde{Q}) = 0$

If the norm form vanishes and $\tilde{Q} \neq 0$, then $\tilde{Q}$ is a zero divisor. The complex polar form is not available, because the quaternion $Q$ would have to be a zero divisor in $\mathbb{H}$, and the real quaternions form a division algebra. The zero divisors are treated in the article on biquaternion zero divisors.

### Existence and Uniqueness

**Theorem.** Every biquaternion $\tilde{Q}$ with $Q_r$ invertible and $N(\tilde{Q}) \neq 0$ has a complex polar form. The form is unique up to the addition of $\pi$ to the scalar part of $\Psi$, with the sign of $Q$ adjusted accordingly.

**Proof.** The construction above gives $\Psi$ and $Q$ explicitly from $\tilde{Q}$. Set $\Psi = \arctan(Q_r^{-1}Q_i)$, which is a real quaternion: the arctangent of a real quaternion is defined by the standard power series

$$
\arctan q = \sum_{n=0}^{\infty} \frac{(-1)^n q^{2n+1}}{2n+1},
$$

convergent for $|q| < 1$ in the quaternion norm, or equivalently by analytic continuation; it satisfies $\tan(\arctan q) = q$ for all real quaternions $q$. Then $\cos\Psi$ and $\sin\Psi$ are real quaternions. Define $Q = Q_r (\cos\Psi)^{-1}$, which is a real quaternion because $Q_r$ and $(\cos\Psi)^{-1}$ are real quaternions. Since $\cos\Psi$ and $\sin\Psi$ are functions of the single quaternion $\Psi$, they commute with each other, so $(\cos\Psi)^{-1}\sin\Psi = \tan\Psi$. Then

$$
Q\exp(i\Psi) = Q\cos\Psi + iQ\sin\Psi = Q_r (\cos\Psi)^{-1} \cos\Psi + i Q_r (\cos\Psi)^{-1} \sin\Psi = Q_r + i Q_r \tan\Psi = Q_r + iQ_i = \tilde{Q},
$$

where we have used $Q_r (\cos\Psi)^{-1} \cos\Psi = Q_r$ and $Q_r \tan\Psi = Q_r Q_r^{-1} Q_i = Q_i$. The uniqueness follows from the fact that $\Psi$ is determined by the equation $\tan\Psi = Q_r^{-1}Q_i$, which determines $\Psi$ up to the addition of $\pi$ in the scalar part, with the sign of $Q$ adjusted accordingly. $\square$

### The Angle Is Quaternionic

The angle $\Psi$ is a general real quaternion: it has the form $\Psi = a + b\hat{u}$ with $a, b \in \mathbb{R}$ and $\hat{u}$ a unit pure real quaternion (with $b = 0$ in the case that $\Psi$ is real). In the special case $Q_r^{-1}Q_i = 0$, $\Psi = 0$; in the special case $Q_r^{-1}Q_i$ is pure, $\Psi$ is pure; and in general $\Psi$ has both a scalar part and a pure quaternion part.

### The Modulus Is a Quaternion

The modulus $Q$ is a real quaternion, not a complex scalar. This is the essential difference from the Hamilton polar form, where the modulus is a complex scalar.

### Example

Take $\tilde{Q} = 1 + i$, a complex scalar. Then $Q_r = 1$ and $Q_i = 1$, so $\tan\Psi = 1$, i.e., $\Psi = \pi/4$ (up to the addition of $\pi$ in the scalar part). And $Q = (1+i) \exp(-i\pi/4) = (1+i)(\cos(\pi/4) - i \sin(\pi/4)) = (1+i)(1/\sqrt{2} - i/\sqrt{2}) = \sqrt{2}$. So

$$
\tilde{Q} = \sqrt{2} \exp(i \pi/4).
$$

This is exactly the ordinary polar form of the complex number $1 + i$. So in the case of a scalar biquaternion, the complex polar form reduces to the ordinary complex polar form.

### A Non-Scalar Example

Take $\tilde{Q} = e_0 + e_1 + i e_2 = 1 + e_1 + ie_2$. Then $Q_r = 1 + e_1$ and $Q_i = e_2$. First verify that $N(\tilde{Q}) \neq 0$; the computation is given below. So the complex polar form exists.

Compute $\tan\Psi = Q_r^{-1}Q_i = (1+e_1)^{-1}e_2 = \frac{(1-e_1)}{2}e_2 = \frac{e_2 - e_3}{2}$, using $(1+e_1)^{-1} = (1-e_1)/2$ (from $(1+e_1)(1-e_1) = 1 - e_1^2 = 2$). The quaternion $q = (e_2-e_3)/2$ is pure, with unit direction $\hat{q} = (e_2-e_3)/\sqrt{2}$ and magnitude $|q| = 1/\sqrt{2}$. Therefore

$$
\Psi = \arctan(q) = \hat{q}\,\arctan(|q|) = \frac{e_2 - e_3}{\sqrt{2}}\,\arctan\!\left(\frac{1}{\sqrt{2}}\right),
$$

so $\Psi$ is a pure quaternion (scalar part zero) proportional to $e_2 - e_3$. The corresponding cosine and sine are

$$
\cos\Psi = \cos\!\left(\arctan\frac{1}{\sqrt{2}}\right) = \sqrt{\frac{2}{3}}, \qquad \sin\Psi = \hat{q}\,\sin\!\left(\arctan\frac{1}{\sqrt{2}}\right) = \frac{e_2 - e_3}{\sqrt{2}}\cdot\frac{1}{\sqrt{3}} = \frac{e_2-e_3}{\sqrt{6}},
$$

using $\sin(\arctan x) = x/\sqrt{1+x^2}$ and $\cos(\arctan x) = 1/\sqrt{1+x^2}$. The modulus is $Q = Q_r (\cos\Psi)^{-1} = (1+e_1)\sqrt{3/2}$, a real quaternion. The reconstruction $Q\exp(i\Psi) = \tilde{Q}$ can be verified directly by expansion, as in the existence proof.

**Verification that $N(\tilde{Q}) = 1$.** Compute $\tilde{Q}\bar{\tilde{Q}} = (1 + e_1 + ie_2)(1 - e_1 - ie_2)$:

$$
= 1 - e_1 - ie_2 + e_1 - e_1^2 - ie_1e_2 + ie_2 - ie_2e_1 - i^2 e_2^2
$$
$$
= 1 - e_1 - ie_2 + e_1 + 1 - ie_3 + ie_2 + ie_3 - (-1)(-1)
$$
$$
= 1 + 1 - 1 = 1.
$$

So $N(\tilde{Q}) = 1 \neq 0$, and $\tilde{Q}$ is not a zero divisor. The complex polar form applies.

## Comparison of the Two Polar Forms

The two polar forms differ in **which root of $-1$ is used in the exponential** and in **which factor is the modulus**:

| | Hamilton polar form | Complex polar form |
|---|---|---|
| Root of $-1$ | $\xi$, a non-central root | $i$, the central root |
| Modulus | $R$, a complex scalar | $Q$, a real quaternion |
| Angle | $\Theta$, a complex scalar | $\Psi$, a real quaternion |
| Existence requires | $B \neq 0$ | $Q_r$ invertible |
| Reduces to | Quaternion polar form (when $\tilde{Q} \in \mathbb{H}$) | Complex polar form (when $\tilde{Q} \in \mathbb{C}_{\mathbb{B}}$) |

### When Each Form Is Natural

The two polar forms are complementary. The Hamilton form generalizes the quaternion polar form, with the quaternion root $\mu$ replaced by a biquaternion root $\xi$, and the modulus and angle allowed to become complex. The complex form generalizes the complex polar form, with the scalar imaginary $i$ retained as the root, and the modulus allowed to become a quaternion.

The choice between the two polar forms depends on what is being computed:

- The **Hamilton polar form** is natural when the biquaternion is close to a quaternion, i.e., when the complexification is a small perturbation. The root $\xi$ is close to a pure real quaternion, and the exponential is close to the quaternion exponential.
- The **complex polar form** is natural when the biquaternion is close to a complex scalar, i.e., when the quaternion structure is a small perturbation. The modulus $Q$ is close to a complex scalar, and the exponential is close to the ordinary complex exponential.

In the case of a biquaternion that is neither close to a quaternion nor close to a complex scalar, neither polar form is canonical, and the choice is a matter of convenience.

### The Domain of Definition

The two polar forms are defined on overlapping but different domains, both assumed to be restricted to $N(\tilde{Q}) \neq 0$:

- The Hamilton polar form is defined for $B \neq 0$, i.e. $(\mathbf{Q}, \mathbf{Q}) \neq 0$.
- The complex polar form is defined for $Q_r$ invertible, equivalently $Q_r \neq 0$.

The union of the two domains covers all biquaternions with $N(\tilde{Q}) \neq 0$ except those with $B = 0$ and $Q_r = 0$ simultaneously, i.e., the elements

$$
\tilde{Q} = i Q'_0 e_0 + \mathbf{Q}, \qquad Q'_0 \in \mathbb{R} \setminus \{0\}, \qquad (\mathbf{Q}, \mathbf{Q}) = 0,
$$

whose real scalar part vanishes, whose vector part is null, and whose imaginary scalar part is nonzero (so that $N(\tilde{Q}) = -Q'^2_0 \neq 0$). The case $\mathbf{Q} = 0$ reduces to the purely imaginary complex scalars $\tilde{Q} = i Q'_0 e_0$; these do have polar forms as ordinary complex numbers (namely $iQ'_0 = |Q'_0| \exp(\pm i\pi/2)$), but these are not captured by either of the two biquaternion polar forms constructed above. The case $\mathbf{Q} \neq 0$ involves a nonzero nilpotent vector part, and its polar form, if one exists, is of the nilpotent-exponential kind discussed in the Hamilton section.

## The Role of the Roots of Minus One

The two polar forms correspond to the two classes of roots of $-1$ in $\mathbb{B}$:

- The **scalar imaginary** $i$ is the unique central root of $-1$ (up to sign). It is the root used in the complex polar form.
- The **non-central roots** of $-1$ are the roots used in the Hamilton polar form. They come in two kinds. The **real roots** $\pm\mu$, with $\mu$ a unit pure real quaternion, correspond to the case where the vector part $\mathbf{Q}$ has parallel real and imaginary components. The **non-trivial roots** $\xi = b\mu + d\nu i$ with $\mu \perp \nu$ unit pure real quaternions and $b^2 - d^2 = 1$, with both $b, d \neq 0$, correspond to the case where the real and imaginary parts of $\mathbf{Q}$ are not parallel.

The existence of the non-central roots is the reason the Hamilton polar form differs from the complex one. In the complex numbers, only the central root exists, and there is only one polar form. In the biquaternions, the central root and the non-central roots coexist, and the two polar forms reflect the two possibilities.

The classification of the roots of $-1$ is the subject of the article on biquaternion roots of minus one. The results are:

1. **Non-trivial roots:** $\xi = b\mu + d\nu i$, where $\mu$ and $\nu$ are perpendicular unit pure real quaternions, and $b, d \in \mathbb{R}$ with $b, d \neq 0$ satisfy $b^2 - d^2 = 1$.
2. **The trivial root:** $\xi = \pm i$.
3. **The real roots:** $\xi = \pm \mu$, where $\mu$ is a unit pure real quaternion.

The axis of the Hamilton polar form is a **real root** whenever the real and imaginary parts of the vector part $\mathbf{Q}$ are parallel (this includes the cases where one of them vanishes, i.e., the vector part is real or purely imaginary); it is a **non-trivial root** otherwise.

## Behavior Under the Four Conjugations

The four conjugations of the biquaternion algebra act on the two polar forms as follows. Throughout, the scalar imaginary $i$ is treated as a complex scalar, so it is conjugated by $^*$ and preserved by $\bar{\cdot}$. In the Hamilton form, $R$ and $\Theta$ are central (commuting with everything), while $\xi$ is pure. In the complex form, $Q$ and $\Psi$ are real quaternions, so $\bar{Q} \neq Q$ and $\bar\Psi \neq \Psi$ in general, and the factors do not commute; this makes the complex form less clean under conjugation than the Hamilton form.

### Quaternion Conjugation

**Hamilton form.** Quaternion conjugation $\bar{\cdot}$ is an anti-automorphism and fixes the center $\mathbb{C}$. Since $R$ is central, $\bar{R} = R$; since $\Theta$ is central, $\bar{\Theta} = \Theta$; since $\xi$ is pure, $\bar{\xi} = -\xi$. Therefore

$$
\overline{R \exp(\xi \Theta)} = \overline{\exp(\xi \Theta)} \cdot \bar{R} = \exp(\bar{\xi}\Theta) R = R \exp(-\xi \Theta).
$$

So quaternion conjugation reverses the sign of the axis in the Hamilton polar form.

**Complex form.** Applying the anti-automorphism property gives

$$
\overline{Q \exp(i \Psi)} = \overline{\exp(i \Psi)} \cdot \bar{Q} = \exp(i \bar{\Psi}) \bar{Q},
$$

using $\overline{i\Psi} = i\bar\Psi$. The factors $\exp(i\bar\Psi)$ and $\bar{Q}$ need not commute, so this is **not** in general equal to $\bar{Q} \exp(i\bar{\Psi})$; re-expressing the result in standard complex polar form requires computing the new real and imaginary quaternion parts of $\overline{Q \exp(i\Psi)}$.

### Complex Conjugation

**Hamilton form.** Complex conjugation $^*$ is an algebra automorphism (not anti-automorphism) and fixes the quaternion units. Since $R$, $\xi$, $\Theta$ transform coefficientwise,

$$
(R \exp(\xi \Theta))^* = R^* \exp(\xi^* \Theta^*).
$$

The modulus is complex-conjugated, and both the axis and the angle are complex-conjugated. Since the norm form transforms as $N(\tilde{Q}^*) = N(\tilde{Q})^*$, we have $R^* = \sqrt{N(\tilde{Q})^*} = \sqrt{N(\tilde{Q}^*)}$, which is consistent.

**Complex form.** Since $Q$ is a real quaternion ($Q^* = Q$) and $\Psi$ is a real quaternion ($\Psi^* = \Psi$),

$$
(Q \exp(i \Psi))^* = Q \exp(-i \Psi).
$$

Complex conjugation reverses the sign of $i$ and leaves both $Q$ and $\Psi$ unchanged.

### Hermitian Conjugation

**Hamilton form.** Since $\dagger = \bar{\cdot} \circ {}^*$,

$$
(R \exp(\xi \Theta))^\dagger = \overline{(R \exp(\xi \Theta))^*} = \overline{R^* \exp(\xi^* \Theta^*)} = \exp(-\xi^* \Theta^*) R^* = R^* \exp(-\xi^* \Theta^*),
$$

using $\overline{\xi^*} = -\xi^*$ and the centrality of $R^*$.

**Complex form.** Using the results above,

$$
(Q \exp(i \Psi))^\dagger = \overline{(Q \exp(i \Psi))^*} = \overline{Q \exp(-i \Psi)} = \overline{\exp(-i\Psi)}\bar{Q} = \exp(-i\bar{\Psi}) \bar{Q}.
$$

Again the factors need not commute, so this is not in general equal to $\bar{Q}\exp(-i\bar{\Psi})$.

### Summary

The following table records the action of the three nontrivial conjugations on each polar form. For the Hamilton form, the entries describe how the parameters transform. For the complex form, the entries record the full expression that results, since the parameters do not transform independently (the factors need not commute):

| Conjugation | Hamilton form | Complex form |
|---|---|---|
| Quaternion $\bar{\cdot}$ | $R \to R$, $\xi \to -\xi$, $\Theta \to \Theta$ | $\overline{Q \exp(i\Psi)} = \exp(i\bar\Psi)\bar{Q}$ |
| Complex $^*$ | $R \to R^*$, $\xi \to \xi^*$, $\Theta \to \Theta^*$ | $(Q \exp(i\Psi))^* = Q \exp(-i\Psi)$ |
| Hermitian $\dagger$ | $R \to R^*$, $\xi \to -\xi^*$, $\Theta \to \Theta^*$ | $(Q \exp(i\Psi))^\dagger = \exp(-i\bar\Psi)\bar{Q}$ |

The two polar forms respond differently to the four conjugations, and the choice of polar form determines which conjugation is "natural" for the expression. In particular, quaternion conjugation acts on the Hamilton form by reversing the axis, while it acts on the complex form by reversing the order of the two factors and conjugating both. Complex conjugation acts on the Hamilton form by conjugating all three complex quantities, while it acts on the complex form only by flipping the scalar imaginary.

## The Relation to the Algebraic Representations

The polar representations are related to the algebraic representations as follows.

**Relation to the matrix representation.** The polar form of a biquaternion is the analogue of the polar decomposition of the corresponding $2 \times 2$ complex matrix. The Hamilton form separates the biquaternion into a "magnitude" times an exponential of a non-central root of $-1$, in analogy with the quaternion polar form. The complex form separates the biquaternion into its "real" and "imaginary" quaternion parts, and then polar-decomposes the imaginary part relative to the real part.

**Relation to the four-vector representation.** The Hamilton polar form separates the four-vector into a "magnitude" $R$ and a "direction" $\xi$, in analogy with the polar form of a vector. The complex polar form separates the four-vector into its "real" and "imaginary" quaternion parts, and then polar-decomposes the imaginary part relative to the real part.

**Relation to the Clifford algebra representation.** The polar forms are not naturally expressed in the Clifford algebra representation, because the Clifford algebra is a real algebra and the polar forms use the complex scalar imaginary. However, the Clifford algebra does provide a natural setting for the roots of $-1$ and for the spinor structure that underlies the polar forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde{Q}$ | Biquaternion |
| $Q_0$ | Complex scalar part |
| $\mathbf{Q}$ | Complex vector part |
| $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ | Complex square root of $(\mathbf{Q}, \mathbf{Q})$ |
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ | Norm form |
| $R = \sqrt{N(\tilde{Q})}$ | Complex modulus (Hamilton) |
| $\xi = \mathbf{Q}/B$ | Axis (root of $-1$, Hamilton) |
| $\Theta$ | Complex angle (Hamilton) |
| $Q_r, Q_i$ | Real and imaginary quaternion parts |
| $Q$ | Real quaternion modulus (complex form) |
| $\Psi$ | Real quaternion angle (complex form) |
| $i$ | Scalar imaginary |

## Summary

The biquaternion algebra has **two** natural polar representations:

- The **Hamilton polar form** $\tilde{Q} = R \exp(\xi \Theta)$, where $R$ is a complex scalar modulus, $\xi$ is a non-central root of $-1$ parallel to the vector part, and $\Theta$ is a complex scalar angle. It is defined when $B = \sqrt{(\mathbf{Q},\mathbf{Q})} \neq 0$ and $N(\tilde{Q}) \neq 0$.
- The **complex polar form** $\tilde{Q} = Q \exp(i \Psi)$, where $Q$ is a real quaternion modulus, $i$ is the central root of $-1$, and $\Psi$ is a real quaternion angle. It is defined when the real quaternion part $Q_r$ is invertible and $N(\tilde{Q}) \neq 0$.

The two forms are complementary. The Hamilton form generalizes the quaternion polar form and is natural when the biquaternion is close to a quaternion. The complex form generalizes the ordinary complex polar form and is natural when the biquaternion is close to a complex scalar.

The existence of the two forms is a consequence of the existence of two classes of roots of $-1$ in the biquaternion algebra: the central root $i$, and the non-central roots (real and non-trivial). The classification of these roots is the subject of the article on biquaternion roots of minus one.

The two forms behave differently under the four conjugations of the algebra, and this difference is the algebraic content of the distinction between them. In particular, quaternion conjugation reverses the order of the two factors in the complex form (because it is an anti-automorphism), a feature that does not arise for the Hamilton form because the Hamilton factors are central and hence commute.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation of the quaternion polar form.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the polar representations of biquaternions.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607-636, for the two polar forms in the applied context.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63-68, for the classification of the roots of $-1$ on which the two polar forms depend.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.

