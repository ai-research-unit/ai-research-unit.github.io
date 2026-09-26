# __The Polar Representation in Subspaces__

## Introduction

The polar representation of a biquaternion,

$$
\tilde{Q} = r\,e^{i\alpha}\,B\,\hat{q} , \qquad r\in\mathbb{R}_{>0}, \quad \alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right], \quad B\in\mathbb{M}_+, \quad \hat{q}\in\mathrm{Sp}(1) ,
$$

decomposes a general element of the algebra into a positive scale, a central phase, a Hermitian positive factor and a rotor. The companion article *The Polar Representation of Biquaternions* reads the four factors on the Lorentz group and on the four-vector. This article restricts the same representation to the **six distinguished subspaces** of *Relations Between Subspaces* and records what the restriction does to the four factors.

The restriction is not a cosmetic exercise, because each subspace is the fixed space of one of the algebra's involutions, and each involution constrains the factors in a different way. Two of the factors are always the modulus of the norm form, and the norm form on a subspace takes one of five forms — positive definite, negative definite, real indefinite, complex anisotropic, complex indefinite — and its argument is what the phase measures. The other two factors are the positive Hermitian square root of $\tilde{Q}\tilde{Q}^\dagger$ and the unitary part of $\tilde{Q}/\rho$, and the subspaces are exactly the cases in which one of those two products degenerates. The six restrictions therefore say which of the four factors a subspace is able to carry, and the answer is that no subspace carries all four freely:

| subspace | real dim | norm form | phase | boost | rotor |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ — center | 2 | complex, anisotropic | free | $e_0$ | $\pm e_0$ |
| $\mathrm{Vect}(\mathbb{B})$ — vector subspace | 6 | complex, indefinite | free | boost about $\mathbf{v}\times\mathbf{w}$ | unit vector in the plane of $\mathbf{v}$ and $\mathbf{w}$ |
| $\mathbb{H}_{\mathbb{B}}$ — quaternions | 4 | positive definite | $0$ | $e_0$ | free in $\mathrm{Sp}(1)$ |
| $i\mathbb{H}_{\mathbb{B}}$ — antiquaternions | 4 | negative definite | $\pi/2$ | $e_0$ | free in $\mathrm{Sp}(1)$ |
| $\mathbb{M}_+$ — informational sector | 4 | real, indefinite | $0$ or $\pi/2$ | the boost, explicit | $\pm e_0$ or a direction |
| $\mathbb{M}_-$ — material sector | 4 | real, indefinite | $0$ or $\pi/2$ | the boost, explicit | $\pm e_0$ or a direction |

The conventions are those of *Conventions in the Biquaternion Universe*: $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2 = \det\Phi(\tilde{Q})$ with $\Phi(e_0) = I$, $\Phi(e_k) = -i\sigma_k$, $\Phi(i) = iI$; $\mathbb{C}_{\mathbb{B}}$ is the center; $\mathrm{Vect}(\mathbb{B})$ is the kernel of the scalar part; $\mathbb{H}_{\mathbb{B}}$ is the fixed space of complex conjugation, the home of the rotations; $i\mathbb{H}_{\mathbb{B}}$ is the anti-fixed space of complex conjugation, its imaginary half; $\mathbb{M}_+$ is the fixed space of Hermitian conjugation, the home of the boosts; and $\mathbb{M}_-$ is the anti-fixed space of Hermitian conjugation, with $Q_0 = iq'_0$ and $Q_k$ real, the home of the four-vectors. Every numerical value below was recomputed in double precision; the residuals of the identities quoted are below $2\times10^{-12}$.

The six restrictions are taken one at a time in the sections that follow, in the order in which the framework names the subspaces — center, vector, quaternion, antiquaternion, informational, material — and each part is built the same way: it opens with the element and its norm form, states which of the four factors survive, gives the surviving factors explicitly, and closes with worked examples. Where a subspace's defining condition needs a computation of its own — the boost axis and the orthogonality of the rotor in the vector subspace, the two branches of each sector — that computation is a subsection of the part. Three further sections close the article, each a comparison across all six: the norm form as the single object that decides the phase, the count of the dimensions each factor accounts for, and the four coordinate blocks, on which the six restrictions have to agree element by element.

## The Four Factors and the Two Criteria

### The Factors in Terms of Two Products

The representation is constructed in two steps, and each step produces two factors. First the modulus is extracted, with

$$
\rho = re^{i\alpha} = \sqrt{N(\tilde{Q})}, \qquad r = \left|\det\Phi(\tilde{Q})\right|^{1/2}, \qquad \alpha = \tfrac12\arg\det\Phi(\tilde{Q}) ,
$$

the principal branch of the square root fixing the pair $(r,\alpha)$ uniquely. The remaining element $U = \tilde{Q}/\rho$ has unit norm form, and its polar decomposition is the Cartan decomposition

$$
U = B\,\hat{q} , \qquad B = \sqrt{UU^\dagger}, \qquad \hat{q} = B^{-1}U ,
$$

with $B$ the unique Hermitian positive square root. In terms of the element itself,

$$
B = \frac{\sqrt{\tilde{Q}\tilde{Q}^\dagger}}{r} , \qquad \hat{q} = B^{-1}\frac{\tilde{Q}}{\rho} , \qquad \tilde{Q}\tilde{Q}^\dagger = r^2B^2 .
$$

The last identity is the one that decides the whole of what follows, because it shows that the boost factor is a scalar exactly when the product $\tilde{Q}\tilde{Q}^\dagger$ is one.

### Criterion for the Boost Factor

**The boost factor is trivial, $B = e_0$, if and only if $\tilde{Q}\tilde{Q}^\dagger$ is a positive real multiple of the unit.**

*Proof.* Let $\tilde{Q}\tilde{Q}^\dagger = ce_0$ with $c > 0$. Then $B^2 = (c/r^2)e_0$, a positive real multiple of the unit; the unique Hermitian positive square root of such an element is the positive real multiple $\sqrt{c/r^2}\,e_0$ of the unit, and $N(B) = 1$ forces $\sqrt{c/r^2} = 1$ and $B = e_0$. Conversely $B = e_0$ gives $\tilde{Q}\tilde{Q}^\dagger = r^2e_0$. $\square$

In the matrix picture the criterion reads $\Phi(\tilde{Q})\Phi(\tilde{Q})^\dagger = \lambda I$ with $\lambda > 0$: the boost factor is trivial exactly when the element is, up to a scale, a **unitary** matrix rather than a general invertible one. That is a condition on the element alone, and it is satisfied on three of the six subspaces for every element — the center and the two halves — on the vector subspace only for a parallel pair, and on the two sectors only in the two exceptional cases computed below.

### Criterion for the Rotor

**The rotor is a central sign, $\hat{q} = \pm e_0$, if and only if $\tilde{Q}/\rho$ is Hermitian**, equivalently if and only if $\tilde{Q} = \pm\rho B$ for a Hermitian positive $B$ of unit norm form.

*Proof.* If $\hat{q} = \pm e_0$ then $\tilde{Q}/\rho = \pm B$ is Hermitian. Conversely let $\tilde{Q}/\rho = H$ be Hermitian of norm form one; then $H$ is either positive definite or negative definite, so $H = B$ or $H = -B$ with $B$ Hermitian positive of norm form one, and therefore $\hat{q} = e_0$ or $\hat{q} = -e_0$. $\square$

The rotor is thus the part of the element that obstructs its being a complex multiple of a Hermitian element, and the central sign $\pm e_0$ is the discrete residue of that obstruction, which is the kernel of the two-to-one cover of the Lorentz group.

### The Matrix Image of Each Subspace

The matrix representative makes the criteria computable at a glance. With $\Phi(e_k) = -i\sigma_k$,

| subspace | $\Phi(\tilde{Q})$ | class of matrix |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $zI$ | scalar |
| $\mathrm{Vect}(\mathbb{B})$ | $\left(w_k - i v_k\right)\sigma_k$ | traceless |
| $\mathbb{H}_{\mathbb{B}}$ | $q_0I - i q_k\sigma_k = \begin{pmatrix} a & b \\ -\bar{b} & \bar{a}\end{pmatrix}$ | quaternionic |
| $i\mathbb{H}_{\mathbb{B}}$ | $i q_0I + q_k\sigma_k$ | $i$ times quaternionic |
| $\mathbb{M}_+$ | $aI + w_k\sigma_k$ | Hermitian |
| $\mathbb{M}_-$ | $i\left(aI - v_k\sigma_k\right)$ | $i$ times Hermitian |

All six classes are closed under the map $\tilde{Q}\mapsto\tilde{Q}\tilde{Q}^\dagger$, and the resulting matrices are what the following sections compute.

## The Center Subspace $\mathbb{C}_{\mathbb{B}}$: the Modulus and the Free Phase

### The Element and Its Norm Form

The center is the set of complex scalars, $\tilde{Q} = ze_0$ with $z\in\mathbb{C}$, $z\neq0$. It is two-dimensional over the reals, and its norm form is the complex anisotropic form

$$
N(\tilde{Q}) = z^2 , \qquad r = |z| ,
$$

whose argument is $2\arg z$. The norm form vanishes only at $z = 0$: the center carries no zero divisor other than the origin, and the representation is defined on $\mathbb{C}_{\mathbb{B}}\setminus\{0\}$.

### Which Factors Survive

Both criteria apply automatically. Since $\tilde{Q}\tilde{Q}^\dagger = |z|^2e_0$ is a positive scalar, the first criterion gives the trivial boost $B = e_0$, and since $\tilde{Q}/\rho = (z/\rho)e_0$ is a real multiple of the unit, the second criterion gives a rotor that is a central sign, $\hat{q} = \pm e_0$. The four factors therefore collapse to one number, the phase, which is the only factor with a continuous range:

$$
ze_0 = \rho\,(\pm e_0) , \qquad \rho = \sqrt{z^2} , \qquad r = |z| , \qquad \alpha \equiv \arg z \ (\mathrm{mod}\ \pi)\ \text{taken in}\ \left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right] ,
$$

### The Explicit Factors

The rotor carries the sign of the element. With $\hat{q} = z/\rho$, that is

$$
\hat{q} = \frac{z}{\rho} = \begin{cases} +e_0 , & \arg z\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right] , \\ -e_0 , & \arg z\in\left(\tfrac{\pi}{2},\pi\right]\cup\left(-{\pi},-\tfrac{\pi}{2}\right] ,\end{cases}
$$

the two lines being $\rho = z$ and $\rho = -z$. The polar representation of a biquaternion in the center is therefore the polar form of the complex number $z$: the phase is **free**, and it is the argument of the element itself, taken modulo the branch of $\pi$. The two rotors have nothing to act on and reduce to the element $-e_0$ of the kernel of the two-to-one map, and the boundary case $\arg z = -\pi/2$ is the one on which the branch matters: for $\tilde{Q} = -2ie_0$ the phase is pulled from $-\pi/2$ to $+\pi/2$ and the sign is carried by the rotor.

The matrix statement is the same one: $\Phi(\tilde{Q}) = zI$ is a scalar matrix, its positive Hermitian polar factor is $|z|I$, and the unitary polar factor is the number $z/|z|$ read as $\pm I$ after the branch of the square root has absorbed the sign.

### Worked Examples

| example | $N = z^2$ | $r = |z|$ | $\alpha$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|
| $\tilde{Q} = (1+i)e_0$ | $2i$ | $1.414213562$ | $0.785398163$ | $e_0$ | $e_0$ |
| $\tilde{Q} = -e_0$ | $1$ | $1$ | $0$ | $e_0$ | $-e_0$ |
| $\tilde{Q} = 2ie_0$ | $-4$ | $2$ | $1.570796327$ | $e_0$ | $e_0$ |
| $\tilde{Q} = -2ie_0$ | $-4$ | $2$ | $1.570796327$ | $e_0$ | $-e_0$ |

In the first row $\rho = 1+i$, the principal square root of $2i$, and $\alpha = \pi/4$; in the second row $\rho = 1$ and the sign of $z$ is carried by $\hat{q}$; in the third and fourth rows $\rho = 2i$ and the phase is the angle $\pi/2$ that turns the unit into the imaginary unit, the two rows differing by the sign of the rotor.

## The Vector Subspace $\mathrm{Vect}(\mathbb{B})$: the Rotor Relative to the Boost

### The Element and Its Norm Form

The vector subspace is the kernel of the scalar part, of real dimension six. Written with two real vectors, the element and its norm form are

$$
\tilde{Q} = \mathbf{v} + i\,\mathbf{w} , \qquad \mathbf{v},\mathbf{w}\in\mathbb{R}^3 , \qquad N(\tilde{Q}) = |\mathbf{v}|^2 - |\mathbf{w}|^2 + 2i\,\mathbf{v}\cdot\mathbf{w} , \qquad \operatorname{Sc}(\tilde{Q}) = 0 .
$$

The norm form is complex and indefinite, so the phase is free here exactly as it is on the center; it vanishes on the four-dimensional complex null cone $|\mathbf{v}| = |\mathbf{w}|$, $\mathbf{v}\cdot\mathbf{w} = 0$, and the representation is defined on the complement of that cone. In the matrix picture the subspace is the traceless class, $\Phi(\tilde{Q}) = \left(w_k - iv_k\right)\sigma_k$.

### Which Factors Survive

Neither criterion applies automatically, and both factors are genuinely present:

$$
\tilde{Q}\tilde{Q}^\dagger = \left(|\mathbf{v}|^2 + |\mathbf{w}|^2\right)e_0 + 2i\left(\mathbf{v}\times\mathbf{w}\right) ,
$$

which is a positive scalar only when $\mathbf{v}\times\mathbf{w} = 0$. Hence the boost factor is trivial **exactly when the two vectors are parallel**, and in that case $\tilde{Q} = z\hat{\mathbf{v}}$ with $z = |\mathbf{v}|\pm i|\mathbf{w}|$ according to the relative sign, so the element is a complex multiple of a single real direction, $N(\tilde{Q}) = z^2$, and on the line $\mathbb{R}\{\mathbf{v}\}$ the representation is the representation of the center. When the two vectors are not parallel the boost factor is

$$
B = \frac{\sqrt{\left(|\mathbf{v}|^2+|\mathbf{w}|^2\right)e_0 + 2i\left(\mathbf{v}\times\mathbf{w}\right)}}{\sqrt{|N(\tilde{Q})|}} = \cosh\varphi\,e_0 + i\sinh\varphi\,\frac{\mathbf{v}\times\mathbf{w}}{|\mathbf{v}\times\mathbf{w}|} ,
$$

a boost about the axis $\mathbf{v}\times\mathbf{w}$, with the rapidity fixed by

$$
\cosh 2\varphi = \frac{|\mathbf{v}|^2+|\mathbf{w}|^2}{\left|N(\tilde{Q})\right|} , \qquad \sinh 2\varphi = \frac{2\left|\mathbf{v}\times\mathbf{w}\right|}{\left|N(\tilde{Q})\right|} , \qquad \cosh^2 2\varphi - \sinh^2 2\varphi = 1 ,
$$

the last identity being the Lagrange identity $\left(|\mathbf{v}|^2+|\mathbf{w}|^2\right)^2 - 4\left|\mathbf{v}\times\mathbf{w}\right|^2 = |N(\tilde{Q})|^2$, which is what makes the argument of the square root positive definite.

### The Rotor Is Orthogonal to the Boost Axis

The defining condition $\operatorname{Sc}(\tilde{Q}) = 0$ is a condition on the two factors. Write $\bar{\tilde{Q}} = -\tilde{Q}$ and use the anti-automorphism property of quaternion conjugation, $\overline{AB} = \bar{B}\bar{A}$:

$$
\overline{\rho B\hat{q}} = \bar{\hat{q}}\,\bar{B}\,\rho = (-\hat{q})\left(\cosh\varphi\,e_0 - i\sinh\varphi\,\hat{\mathbf{u}}\right)\rho = -\rho\,\hat{q}\left(\cosh\varphi\,e_0 - i\sinh\varphi\,\hat{\mathbf{u}}\right) ,
$$

and equating this to $-\rho\left(\cosh\varphi + i\sinh\varphi\,\hat{\mathbf{u}}\right)\hat{q}$ gives

$$
\hat{q}\,\hat{\mathbf{u}} = -\hat{\mathbf{u}}\,\hat{q} \quad\Longleftrightarrow\quad -2\,\hat{q}\cdot\hat{\mathbf{u}} = 0 \quad\Longleftrightarrow\quad \hat{q}\perp\hat{\mathbf{u}} ,
$$

where $\hat{\mathbf{u}} = \mathbf{v}\times\mathbf{w}/|\mathbf{v}\times\mathbf{w}|$ is the boost axis. A pure unit vector orthogonal to $\hat{\mathbf{u}}$ lies in the plane orthogonal to $\hat{\mathbf{u}}$, and that plane is $\operatorname{span}(\mathbf{v},\mathbf{w})$, because $\mathbf{v}\cdot(\mathbf{v}\times\mathbf{w}) = 0$ and $\mathbf{w}\cdot(\mathbf{v}\times\mathbf{w}) = 0$. The rotor is therefore a unit vector **in the plane spanned by $\mathbf{v}$ and $\mathbf{w}$**, perpendicular to the boost axis. The two conditions are equivalent: the vanishing of the scalar part is the orthogonality of the rotor to the boost axis, and conversely. This is the exact sense in which the vector subspace exhibits the rotor relative to the boost rather than the rotor alone.

The count of the six dimensions of the subspace is then complete:

$$
\underbrace{2}_{r,\ \alpha} + \underbrace{3}_{B:\ \text{axis}\ (2) + \text{rapidity}\ (1)} + \underbrace{2}_{\hat{q}} - \underbrace{1}_{\hat{q}\perp\hat{\mathbf{u}}} = 6 ,
$$

or, in the plane, $2$ for the modulus, $2$ for the axis, $1$ for the rapidity and $1$ for the angle of the rotor in the plane.

### Worked Examples

| example | $N$ | $r$ | $\alpha$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|
| $\tilde{Q} = e_1+i\left(e_2+e_3\right)$ | $-1$ | $1$ | $1.570796327$ | $1.414213562\,e_0 - 0.707106781\,ie_2 + 0.707106781\,ie_3$ | $0.707106781\,e_2 + 0.707106781\,e_3$ |
| $\tilde{Q} = e_1+2ie_1$ | $-3+4i$ | $2.236067977$ | $1.107148718$ | $e_0$ | $e_1$ |

In the first row $\mathbf{v}\times\mathbf{w} = e_3-e_2$, the boost axis is $(e_3-e_2)/\sqrt2$, the rapidity satisfies $\cosh 2\varphi = 3$, and the rotor is $(e_2+e_3)/\sqrt2$, which is orthogonal to the axis by construction. In the second row the two vectors are parallel, the boost factor is $e_0$, the element is $z e_1$ with $z = 1+2i$, the modulus is $\rho = 1+2i$ and the phase is $\arg(1+2i) = 1.107148718$.

## The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$: the Rotor Alone

### The Element and Its Norm Form

Let $\tilde{Q}\in\mathbb{H}_{\mathbb{B}}$, that is $\tilde{Q}^* = \tilde{Q}$, so that $\tilde{Q} = \sum_\mu q_\mu e_\mu$ with all four coefficients real. The subspace is the image of the real quaternion algebra inside $\mathbb{B}$, of real dimension four, and its norm form is the sum of four squares,

$$
N(\tilde{Q}) = \sum_\mu q_\mu^2 > 0 \quad (\tilde{Q}\neq0), \qquad r = |\tilde{Q}| , \qquad \alpha = 0 ,
$$

positive definite, so its only zero is the origin and the representation is defined on the whole subspace except $0$. In the matrix picture it is the quaternionic class, $\Phi(\tilde{Q}) = q_0I - iq_k\sigma_k$.

### Which Factors Survive

On this subspace $\tilde{Q}^\dagger = \bar{\tilde{Q}}$, hence

$$
\tilde{Q}\tilde{Q}^\dagger = \tilde{Q}\bar{\tilde{Q}} = N(\tilde{Q})e_0 = |\tilde{Q}|^2e_0 ,
$$

a positive scalar, so the first criterion gives $B = e_0$, and the rotor is the unit quaternion $\hat{q} = \tilde{Q}/|\tilde{Q}|$. The four-factor representation reduces to

$$
\tilde{Q} = r\,\hat{q} , \qquad r = |\tilde{Q}| > 0 , \qquad \hat{q}\in\mathrm{Sp}(1) ,
$$

which is the classical polar form of a quaternion, with the boost factor absent: **the real quaternion subspace is the subspace on which the representation carries a rotor and no boost**. Writing $\hat{q} = \cos\theta + \sin\theta\,\hat{\mathbf{u}}$ with $\hat{\mathbf{u}}$ a unit real vector, the rotor is a rotation of angle $2\theta$ about the axis $\hat{\mathbf{u}}$, and the four real parameters of the subspace are $r$ and the three parameters of $\hat{\mathbf{u}}$ and $\theta$.

The matrix image explains the absence of the boost factor: a quaternionic matrix has the form $\begin{pmatrix} a & b \\ -\bar{b} & \bar{a}\end{pmatrix}$, and for every such matrix

$$
A A^\dagger = \left(|a|^2 + |b|^2\right) I ,
$$

a positive scalar, so the positive Hermitian polar factor of $A$ is the scalar $\sqrt{|a|^2+|b|^2}\,I$, which is the matrix image of a real multiple of $e_0$.

### Worked Examples

| example | $N$ | $r$ | $\alpha$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|
| $\tilde{Q} = e_0+2e_1$ | $5$ | $2.236067977$ | $0$ | $e_0$ | $0.447213595\,e_0 + 0.894427191\,e_1$ |
| $\tilde{Q} = e_0+e_1+e_2+e_3$ | $4$ | $2$ | $0$ | $e_0$ | $0.5\left(e_0+e_1+e_2+e_3\right)$ |

Both rows have the trivial boost and the phase $0$, and the rotor is free: the first is a rotation by $2\arctan 2 = 2.214297436$ rad about $e_1$, and the second is a rotation by $2\pi/3 = 2.094395102$ rad about $(e_1+e_2+e_3)/\sqrt3$.

## The Antiquaternion Subspace $i\mathbb{H}_{\mathbb{B}}$: the Same Rotor with the Phase Frozen

### The Element and Its Norm Form

Let $\tilde{Q}\in i\mathbb{H}_{\mathbb{B}}$, that is $\tilde{Q}^* = -\tilde{Q}$ and $\tilde{Q} = iq$ with $q$ a real quaternion. The subspace is the imaginary half of the coefficient split $\mathbb{B} = \mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$, of real dimension four, and its norm form is the negative of a sum of four squares,

$$
N(\tilde{Q}) = -\sum_\mu q_\mu^2 < 0 \quad (\tilde{Q}\neq0), \qquad r = |q| > 0 , \qquad \alpha = \frac{\pi}{2} ,
$$

negative definite, so again the only zero is the origin and the representation is defined on $i\mathbb{H}_{\mathbb{B}}\setminus\{0\}$. The principal square root of a negative real is positive imaginary, which is what freezes the phase at $\pi/2$.

### Which Factors Survive

The product $\tilde{Q}\tilde{Q}^\dagger = |q|^2e_0$ is again a positive scalar, so the first criterion gives the trivial boost $B = e_0$, and the rotor is the unit quaternion $\hat{q} = q/|q|$, free in $\mathrm{Sp}(1)$. The four factors are those of $\mathbb{H}_{\mathbb{B}}$ with the phase **frozen at $\pi/2$**:

$$
\tilde{Q} = re^{i\pi/2}\hat{q} = i\,r\,\hat{q} .
$$

The two halves therefore exhibit the same decomposition of the rotor, and differ by exactly the multiplication by the central phase $e^{i\pi/2} = i$, which is the map $i\mathbb{H}_{\mathbb{B}} = i\cdot\mathbb{H}_{\mathbb{B}}$. In the corpus's notation the same fact is the sector exchange $\mathbb{M}_+ = i\mathbb{M}_-$; here it appears between the two halves, and it is the cleanest instance of the phase acting as a map rather than as a coordinate. In the matrix picture the half is carried by $i$ times the quaternionic class, $\Phi(\tilde{Q}) = i\Phi(q)$, and $\Phi(\tilde{Q})\Phi(\tilde{Q})^\dagger = \Phi(q)\Phi(q)^\dagger = (|a|^2+|b|^2)I$ is the same positive scalar as on $\mathbb{H}_{\mathbb{B}}$, so the boost factor is absent there for the same reason.

The two halves are the two definite subspaces — norm form of signature $(4,0)$ and $(0,4)$ — and on a definite subspace the phase cannot vary, because the norm form takes values on a ray of $\mathbb{C}$: the positive real axis on $\mathbb{H}_{\mathbb{B}}$ and the negative real axis on $i\mathbb{H}_{\mathbb{B}}$. This is the first instance of the rule proved in the section on the norm form below.

### Worked Examples

| example | $N$ | $r$ | $\alpha$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|
| $\tilde{Q} = i\left(e_0+2e_1\right)$ | $-5$ | $2.236067977$ | $1.570796327$ | $e_0$ | $0.447213595\,e_0 + 0.894427191\,e_1$ |
| $\tilde{Q} = i\left(e_1-e_2\right)$ | $-2$ | $1.414213562$ | $1.570796327$ | $e_0$ | $0.707106781\,e_1 - 0.707106781\,e_2$ |

Both rows have the trivial boost and the phase frozen at $\pi/2$: the first is the element $e_0+2e_1$ carried into the antiquaternion subspace by the central $i$, with the same scale and the same rotor as in the quaternion table above, and the second is a rotation by $\pi$ about the direction $(e_1-e_2)/\sqrt2$.

## The Informational Sector $\mathbb{M}_+$: the Element Is Its Own Boost

### The Element and Its Norm Form

Let $\tilde{Q}\in\mathbb{M}_+$, written as

$$
\tilde{Q} = a\,e_0 + i\,\mathbf{w} , \qquad a\in\mathbb{R}, \quad \mathbf{w}\in\mathbb{R}^3, \quad s = |\mathbf{w}| , \qquad N(\tilde{Q}) = a^2 - s^2 \in\mathbb{R} .
$$

The sector is the fixed space of Hermitian conjugation, of real dimension four; its norm form is the real indefinite form $a^2-s^2$, vanishing on the cone $|a| = s$, and the representation is defined off that cone. The element is Hermitian, $\tilde{Q}^\dagger = \tilde{Q}$, and in the matrix picture it is the Hermitian class, $\Phi(\tilde{Q}) = aI + w_k\sigma_k$.

### Why There Are Exactly Two Branches

Write the representation as $\tilde{Q} = \rho B\hat{q}$ and impose Hermitian conjugation. With $\hat{q}$ a real unit quaternion, $\hat{q}^\dagger = \bar{\hat{q}} = 2q_0 - \hat{q}$, while $B$ and the central factor $\rho$ are fixed by $\dagger$, so

$$
\tilde{Q}^\dagger = \bar{\rho}\,B\,\bar{\hat{q}} = \tilde{Q} = \rho\,B\,\hat{q} \quad\Longrightarrow\quad \bar{\hat{q}} = e^{2i\alpha}\hat{q} \quad\Longrightarrow\quad 2q_0 = \left(1 + e^{2i\alpha}\right)\hat{q} .
$$

The left-hand side is a real multiple of the unit, so either $q_0 = 0$, which forces $e^{2i\alpha} = -1$, or $\hat{q} = \pm e_0$, which forces $e^{2i\alpha} = 1$ with the same sign in $q_0$ and in $\hat{q}$. The two branches are therefore

$$
\alpha = 0 \ \text{with}\ \hat{q} = \pm e_0 \quad (\text{the case}\ N = a^2-s^2 > 0) , \qquad \alpha = \frac{\pi}{2}\ \text{with}\ \hat{q}\ \text{a pure unit vector} \quad (\text{the case}\ N < 0) ,
$$

and no third possibility exists: the Hermitian condition permits exactly two branches, one for each sign of the norm form. The pairing is reversed with respect to the material sector of the next section, and the reason is the sign of the Hermitian condition — the element is a boost up to its modulus: on the branch $N > 0$ the element is definite, the rotor is the central sign, and $\tilde{Q} = \pm rB$ with the sign absorbed by the rotor; on the branch $N < 0$ the element is indefinite, the phase is $\pi/2$, and the rotor is the direction of the vector part.

### The Boost Factor

The boost factor is

$$
B = \frac{1}{r}\left(M\,e_0 + i\,\operatorname{sign}(a)\,m\,\hat{\mathbf{w}}\right) , \qquad M = \max(|a|,s), \quad m = \min(|a|,s) , \qquad \hat{\mathbf{w}} = \frac{\mathbf{w}}{s} ,
$$

which squares to $\left((a^2+s^2)e_0 + 2ia\mathbf{w}\right)/r^2 = \tilde{Q}\tilde{Q}^\dagger/r^2$ because $\tilde{Q}\tilde{Q}^\dagger = (a^2+s^2)e_0 + 2ia\mathbf{w}$; the sign in front of the vector part is opposite to that of the material sector, and the two formulas are consistent under the map $\tilde{Q}\mapsto i\tilde{Q}$ from $\mathbb{M}_+$ to $\mathbb{M}_-$, which sends the pair $(a,\mathbf{w})$ to $(a,-\mathbf{w})$ and therefore flips the vector part: the material formula with $\mathbf{v} = -\mathbf{w}$ returns the informational formula.

### Worked Examples

| example | $N$ | $r$ | $\alpha$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|
| $\tilde{Q} = 2e_0+ie_1$ | $3$ | $1.732050808$ | $0$ | $1.154700538\,e_0 + 0.577350269\,ie_1$ | $e_0$ |
| $\tilde{Q} = -2e_0+ie_1$ | $3$ | $1.732050808$ | $0$ | $1.154700538\,e_0 - 0.577350269\,ie_1$ | $-e_0$ |
| $\tilde{Q} = e_0+2ie_1$ | $-3$ | $1.732050808$ | $1.570796327$ | $1.154700538\,e_0 + 0.577350269\,ie_1$ | $e_1$ |

All three rows have the same scale, and the pattern of the two branches is complete. The first and second rows are the definite branch: the same boost factor in magnitude, the same phase $0$, and rotors of opposite sign, which is the sign of $a$ absorbed by the fourth factor. The first and third rows have the same boost factor and the same scale and differ in the phase and in the rotor, the definite branch against the indefinite one, and it is the third row that exhibits the direction $\hat{\mathbf{w}} = e_1$. The third and fourth factors are therefore never both continuous here: either the rotor is the discrete sign $\pm e_0$ and the boost is a general boost of axis $\hat{\mathbf{w}}$ and rapidity $\operatorname{arctanh}(s/|a|)$, or the rotor is the direction $\hat{\mathbf{w}}$ itself and the boost is reduced to a rapidity about that same direction.

## The Material Sector $\mathbb{M}_-$: the Boost of a Four-Vector

### The Element and Its Norm Form

Let $\tilde{X}\in\mathbb{M}_-$, written in the physics coordinates as

$$
\tilde{X} = i\,a\,e_0 + \mathbf{v} , \qquad a = ct\in\mathbb{R}, \quad \mathbf{v}\in\mathbb{R}^3, \quad s = |\mathbf{v}| , \qquad N(\tilde{X}) = s^2 - a^2 \in\mathbb{R} .
$$

The sector is the fixed space of the anti-Hermitian conjugation $\flat$ and the $-1$ eigenspace of Hermitian conjugation, of real dimension four; its norm form is the real indefinite form $s^2-a^2$, vanishing on the light cone $s = |a|$, and the representation is defined off that cone. In the matrix picture it is $i$ times the Hermitian class, $\Phi(\tilde{X}) = i\left(aI - v_k\sigma_k\right)$. The norm form is real, so the phase takes one of the two values compatible with a real norm form, and the element is anti-Hermitian, $\tilde{X}^\dagger = -\tilde{X}$. That single condition fixes the shape of the representation.

### Why There Are Exactly Two Branches

Write the representation as $\tilde{X} = \rho B\hat{q}$ and apply the anti-Hermitian condition. With $\hat{q}$ a real unit quaternion, $\hat{q}^\dagger = \bar{\hat{q}} = 2q_0 - \hat{q}$, so

$$
\tilde{X}^\dagger = \bar{\rho}\,B\,\bar{\hat{q}} = -\tilde{X} = -\rho\,B\,\hat{q} \quad\Longrightarrow\quad \bar{\hat{q}} = -e^{2i\alpha}\hat{q} \quad\Longrightarrow\quad 2q_0 = \left(1 - e^{2i\alpha}\right)\hat{q} .
$$

The left-hand side is a real multiple of the unit, so either $q_0 = 0$, which forces $e^{2i\alpha} = 1$, or $\hat{q} = \pm e_0$, which forces $e^{2i\alpha} = -1$ with the same sign in $q_0$ and in $\hat{q}$. The two solutions are therefore

$$
\alpha = 0 \ \text{with}\ \hat{q}\ \text{a pure unit vector} , \qquad \text{or} \qquad \alpha = \frac{\pi}{2}\ \text{with}\ \hat{q} = \pm e_0 ,
$$

and no third possibility exists. Since $N = r^2e^{2i\alpha}$, the first branch is the **spacelike** case $s > |a|$ and the second is the **timelike** case $|a| > s$. On the material sector the phase is thus a two-valued label of the causal character of the four-vector, and it is exactly the $ict$ reading of the companion article: a timelike four-vector has interval $N < 0$, its square root is imaginary, and the phase is the angle $\pi/2$ that makes the time component imaginary.

### The Boost Factor

From $\tilde{X}\tilde{X}^\dagger = (a^2+s^2)e_0 - 2ia\mathbf{v}$ and $r^2 = |N|$ one gets the explicit factor

$$
B = \frac{1}{r}\left(M\,e_0 - i\,\operatorname{sign}(a)\,m\,\hat{\mathbf{v}}\right) , \qquad M = \max(|a|,s), \quad m = \min(|a|,s) , \qquad \hat{\mathbf{v}} = \frac{\mathbf{v}}{s} ,
$$

which is a boost rotor $B = \cosh\varphi\,e_0 - i\operatorname{sign}(a)\sinh\varphi\,\hat{\mathbf{v}}$ of rapidity $2\varphi$ with $\tanh\varphi = m/M$. Squaring it uses $Mm = |a|s$ and gives $B^2 = \left((a^2+s^2)e_0 - 2ia\mathbf{v}\right)/r^2 = \tilde{X}\tilde{X}^\dagger/r^2$, so the closed form is verified by squaring. In the timelike case with $a = ct > 0$ it is the four-velocity identity of the companion article,

$$
B = \frac{ct\,e_0 - i\mathbf{x}}{c\tau} = \gamma\left(e_0 - i\frac{\mathbf{v}}{c}\right) = -\frac{i}{c}\tilde{U} , \qquad \gamma = \frac{ct}{c\tau} = \frac{1}{\sqrt{1-\beta^2}} ,
$$

with $\beta = s/(ct)$; the scale is the proper length $r = c\tau = ct\sqrt{1-\beta^2}$ and the rotor is the central sign.

### The Two Branches of the Material Sector

| branch | $N$ | $r$ | $\alpha$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|
| timelike, $|a| > s$ | $< 0$ | $\sqrt{a^2-s^2}$ | $\pi/2$ | $\cosh\varphi\,e_0 - i\operatorname{sign}(a)\sinh\varphi\,\hat{\mathbf{v}}$ | $\operatorname{sign}(a)e_0$ |
| spacelike, $s > |a|$ | $> 0$ | $\sqrt{s^2-a^2}$ | $0$ | $\cosh\varphi\,e_0 - i\operatorname{sign}(a)\sinh\varphi\,\hat{\mathbf{v}}$ | $\hat{\mathbf{v}}$ |
| pure time, $s = 0$ | $< 0$ | $|a|$ | $\pi/2$ | $e_0$ | $\operatorname{sign}(a)e_0$ |
| pure space, $a = 0$ | $> 0$ | $s$ | $0$ | $e_0$ | $\hat{\mathbf{v}}$ |

On the **timelike** branch the rotor is a central sign, so the continuous data of the four-vector are the scale and the boost alone: $1 + 3 = 4$, the dimension of the sector. The boost factor is the four-velocity in the Hermitian normalisation, which is the identification of the companion article; the phase is the constant $\pi/2$; and the rotor is the discrete sign $\operatorname{sign}(a)$. This is the precise sense in which the physics of the corpus uses two of the four factors.

On the **spacelike** branch the rotor is the pure unit vector $\hat{\mathbf{v}}$, a point of $S^2$, and the boost is a boost about the same line: with $\tanh\varphi = m/M$ and $m/M = |a|/s < 1$, its axis is $-\operatorname{sign}(a)\hat{\mathbf{v}}$, opposite to the direction the rotor carries when $a$ is positive. The four parameters of a spacelike displacement are therefore the scale $r$, the direction $\hat{\mathbf{v}}$ carried by the rotor, and the remaining number $m/M$ carried by the rapidity of the boost. The direction of the displacement is a property of the rotor and not of the boost, and the boost measures how far the displacement is tilted out of the spatial slice: it is the unit, $m = 0$, exactly for a displacement in the spatial slice, $a = 0$.

### Worked Examples

| example | $N$ | $r$ | $\alpha$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|
| $\tilde{X} = ie_0+0.6\,e_1$ | $-0.64$ | $0.8$ | $1.570796327$ | $1.25\,e_0 - 0.75\,ie_1$ | $e_0$ |
| $\tilde{X} = 0.5\,ie_0+e_1$ | $0.75$ | $0.866025404$ | $0$ | $1.154700538\,e_0 - 0.577350269\,ie_1$ | $e_1$ |

The first row is the four-position of the companion article at $ct = 1$ and $0.6c$: $r = 0.8 = c\tau$, $\alpha = \pi/2$, $B = \gamma(e_0-i\beta)$ with $\gamma = 1.25$ and $\beta = 0.6$, and the rotor is $e_0$. The second row is spacelike: $r = \sqrt{3}/2 = 0.866025404$, the phase vanishes, the rotor is the direction $e_1$, and the boost is a boost about the axis $-e_1$ of rapidity $2\operatorname{arctanh}(0.5) = 1.098612289$.

## The Norm Form Decides the Phase

The phase is $\alpha = \tfrac12\arg N(\tilde{Q})$, so the phase is constant on a subset exactly when the argument of the norm form is constant there, and the six subspaces realise the five possible behaviours of the norm form:

| subspace | $N(\tilde{Q})$ | argument of the norm form | phase |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $z^2$, complex anisotropic | $2\arg z$ | $\arg z$ mod $\pi$, free |
| $\mathrm{Vect}(\mathbb{B})$ | $|\mathbf{v}|^2-|\mathbf{w}|^2+2i\,\mathbf{v}\cdot\mathbf{w}$, complex indefinite | free | free |
| $\mathbb{H}_{\mathbb{B}}$ | $\sum q_\mu^2$, positive definite | $0$ | $0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $-\sum q_\mu^2$, negative definite | $\pi$ | $\pi/2$ |
| $\mathbb{M}_+$ | $a^2-s^2$, real indefinite | $0$ or $\pi$ | $0$ or $\pi/2$ |
| $\mathbb{M}_-$ | $s^2-a^2$, real indefinite | $0$ or $\pi$ | $0$ or $\pi/2$ |

The rule is therefore: **the phase is frozen when the norm form is definite, two-valued when the norm form is real indefinite, and free when the norm form is complex.** The center and the vector subspace are the two subspaces with a complex norm form, and they are the two on which the phase is a genuine coordinate. The two halves, whose norm forms have signature $(4,0)$ and $(0,4)$, are the subspaces on which the phase is a constant — the two constants being the two angles $0$ and $\pi/2$ that distinguish a real from a purely imaginary real quaternion. The two sectors, on which the norm form is a real indefinite quadratic form, are the subspaces on which the phase is a two-valued label, and the label is the causal character of the element: on $\mathbb{M}_+$ the pattern is the reverse of that on $\mathbb{M}_-$, where $\alpha = 0$ for a spacelike and $\alpha = \pi/2$ for a timelike element.

The same table decides where the representation fails. The norm form vanishes only where the quadratic form is isotropic:

| subspace | zeros of $N$ | representation |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $z = 0$ (anisotropic) | defined on $\mathbb{C}_{\mathbb{B}}\setminus\{0\}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $|\mathbf{v}| = |\mathbf{w}|$ and $\mathbf{v}\cdot\mathbf{w} = 0$ | fails on the complex null cone |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | $\tilde{Q} = 0$ (definite) | defined on the whole subspace except $0$ |
| $\mathbb{M}_+$ | the cone $|a| = s$ | fails on the cone |
| $\mathbb{M}_-$ | the light cone $s = |a|$ | fails on the light cone |

The two halves and the center carry no zero divisors other than the origin, which is the corpus's statement that the degeneracy of the algebra lies in the sectors and in the vector subspace. The null cones are the boundaries between the two branches of the phase in the sectors: crossing the light cone in $\mathbb{M}_-$ is crossing from $\alpha = 0$ to $\alpha = \pi/2$, and the representation fails exactly at the crossing because the two branches meet at $r = 0$. In the vector subspace the null cone is the four-dimensional cone $|\mathbf{v}| = |\mathbf{w}|$, $\mathbf{v}\cdot\mathbf{w} = 0$, on which the two vectors are the real and imaginary parts of a null complex vector; there the boost factor and the rotor both blow up, and the element is a zero divisor, as in the sectors.

## Where the Dimensions Go

Each row below is the count of the real dimensions of the subspace, distributed over the four factors. A factor that is trivial contributes nothing, a factor that is fixed contributes nothing, and a factor that is discrete contributes nothing continuous.

| subspace | dim | $r$ | $e^{i\alpha}$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $1$ | $1$ | $0$ | $0$ (discrete $\pm e_0$) |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $1$ | $1$ | $3$ | $2$, less $1$ for $\hat{q}\perp\hat{\mathbf{u}}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $1$ | $0$ (fixed $0$) | $0$ | $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $1$ | $0$ (fixed $\pi/2$) | $0$ | $3$ |
| $\mathbb{M}_+$, $N>0$ | $4$ | $1$ | $0$ (fixed $0$) | $3$ | $0$ (discrete $\pm e_0$) |
| $\mathbb{M}_+$, $N<0$ | $4$ | $1$ | $0$ (fixed $\pi/2$) | $1$ (the rapidity) | $2$ (the direction) |
| $\mathbb{M}_-$, timelike | $4$ | $1$ | $0$ (fixed $\pi/2$) | $3$ | $0$ (discrete $\pm e_0$) |
| $\mathbb{M}_-$, spacelike | $4$ | $1$ | $0$ (fixed $0$) | $1$ (the rapidity) | $2$ (the direction) |

Only the vector subspace carries the phase as a dimension of its own together with a nontrivial boost and a nontrivial rotor, and this is why it is the largest of the six. On the center only the modulus survives; on the two halves the boost is absent and the rotor absorbs everything but the scale; on the two sectors either the rotor or the boost is reduced to a single number or to a direction. No subspace carries the four factors independently, and the counting above is the exact statement of the dependencies.

## The Four Blocks

The four coordinate blocks

$$
T_{\mathrm{m}} = \mathbb{R}(ie_0) , \qquad T_{\mathrm{i}} = \mathbb{R}e_0 , \qquad X_{\mathrm{m}} = \mathbb{R}(e_1,e_2,e_3) , \qquad X_{\mathrm{i}} = \mathbb{R}(ie_1,ie_2,ie_3)
$$

are the intersections of the six subspaces, and each block lies in three of them. The restrictions must agree on the overlaps, and they do:

| block | subspaces containing it | element | $r$ | $\alpha$ | $B$ | $\hat{q}$ |
|---|---|---|---|---|---|---|
| $T_{\mathrm{i}}$ | $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ | $t\,e_0$ | $|t|$ | $0$ | $e_0$ | $\operatorname{sign}(t)e_0$ |
| $T_{\mathrm{m}}$ | $\mathbb{C}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ | $it\,e_0$ | $|t|$ | $\pi/2$ | $e_0$ | $\operatorname{sign}(t)e_0$ |
| $X_{\mathrm{m}}$ | $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ | $\mathbf{x}$ | $|\mathbf{x}|$ | $0$ | $e_0$ | $\hat{\mathbf{x}}$ |
| $X_{\mathrm{i}}$ | $\mathrm{Vect}(\mathbb{B})$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ | $i\mathbf{w}$ | $|\mathbf{w}|$ | $\pi/2$ | $e_0$ | $\hat{\mathbf{w}}$ |

Every entry satisfies the restrictions of each subspace that contains it. On $T_{\mathrm{i}}$ the center gives $\hat{q} = \pm e_0$, the quaternion subspace gives $\hat{q} = \tilde{Q}/|\tilde{Q}| = \pm e_0$, and the informational sector with $s = 0$ gives $m = 0$, hence $B = e_0$ and $\hat{q} = \operatorname{sign}(a)e_0$; the three readings are the same. On $X_{\mathrm{m}}$ the vector subspace reading has $\mathbf{w} = 0$, which is the degenerate case $\mathbf{v}\times\mathbf{w} = 0$, hence $B = e_0$; the quaternion reading gives the rotor $\hat{\mathbf{x}}$; and the material-sector reading with $a = 0$ gives the spacelike rotor $\hat{\mathbf{v}} = \hat{\mathbf{x}}$ with the trivial boost $B = e_0$; the three readings are the same. On $X_{\mathrm{i}}$ the vector, antiquaternion and informational readings agree the same way, with the phase $\pi/2$ and the rotor $\hat{\mathbf{w}}$ in all three. The blocks are therefore the elements on which all the applicable simplifications hold at once, and the table is a consistency check of the six sections above rather than a new computation.

## Summary

Restricted to the six distinguished subspaces, the polar representation $\tilde{Q} = re^{i\alpha}B\hat{q}$ loses one or more of its factors, and the loss is computable from the involution that defines the subspace. The scale is always the square root of the absolute value of the determinant, and it never degenerates except on the null cones. The phase is half the argument of the norm form: it is a free coordinate on the center and on the vector subspace, where the norm form is complex; it is frozen at $0$ on the real quaternion subspace and at $\pi/2$ on the antiquaternion subspace, where the norm form is definite; and it is a two-valued label of the causal character of the element on the two sectors, where the norm form is real indefinite. The boost factor is trivial exactly on the subspaces and on the elements for which $\tilde{Q}\tilde{Q}^\dagger$ is a positive scalar: that is every element of the center, every parallel pair $\mathbf{v}\parallel\mathbf{w}$ in the vector subspace, and every element of the two halves; it is the exceptional case of a vanishing time coordinate, $a = 0$, or a vanishing vector part, in the sectors. The rotor is a central sign exactly when $\tilde{Q}/\rho$ is Hermitian: that is the center, and one branch of each sector — the definite branch of the informational sector and the timelike branch of the material sector — while on the other branch it is a pure unit vector, the direction of the element. The vector subspace exhibits the rotor relative to the boost, with the scalar part vanishing exactly when the two axes are orthogonal; on the two halves the rotor is free and the boost is absent, so the halves exhibit the rotor alone; and the sectors exhibit the boost alone and reduce the rotor to a sign or to a direction. The six restrictions together exhaust the ways in which the four factors can depend on one another, and the norm form — positive definite, negative definite, real indefinite, complex anisotropic, complex indefinite — is what decides which way each subspace goes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | a biquaternion, $Q_\mu\in\mathbb{C}$ |
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2 = \det\Phi(\tilde{Q})$ | the norm form and the determinant of the $2\times2$ representative |
| $\rho = re^{i\alpha} = \sqrt{N(\tilde{Q})}$ | the complex modulus, in the principal branch $\alpha\in(-\pi/2,\pi/2]$ |
| $B = \sqrt{\tilde{Q}\tilde{Q}^\dagger}/r$ | the boost factor, Hermitian positive of norm form one |
| $\hat{q} = B^{-1}\tilde{Q}/\rho$ | the rotor, a unit real quaternion |
| $\hat{q} = \pm e_0 \iff \tilde{Q}/\rho$ Hermitian | the criterion for a trivial rotor |
| $B = e_0 \iff \tilde{Q}\tilde{Q}^\dagger\in\mathbb{R}_{>0}e_0$ | the criterion for a trivial boost |
| $\mathbb{C}_{\mathbb{B}}$ | the center |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, $\operatorname{Sc}(\tilde{Q}) = 0$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | real quaternion subspace, antiquaternion subspace |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | informational and material sectors |
| $\tilde{X} = iae_0+\mathbf{v}$, $s = |\mathbf{v}|$ | element of the material sector; $a = ct$ for a four-position |
| $\tilde{Q} = ae_0+i\mathbf{w}$, $s = |\mathbf{w}|$ | element of the informational sector |
| $\tilde{Q} = \mathbf{v}+i\mathbf{w}$ | element of the vector subspace |
| $\varphi$ | the half-rapidity of $B$: $B = \cosh\varphi\,e_0 + i\sinh\varphi\,\hat{\mathbf{u}}$, rapidity $2\varphi$ |
| $M = \max(|a|,s)$, $m = \min(|a|,s)$ | the two numbers that fix the rapidity of the sector boost |
| $T_{\mathrm{m}}, T_{\mathrm{i}}, X_{\mathrm{m}}, X_{\mathrm{i}}$ | the four coordinate blocks |

## Further Reading

- *The Polar Representation of Biquaternions* (`articles_physics/the-polar-representation-of-biquaternions.md`), for the four factors read on the Lorentz group and on the four-vector, and for the determinant, the interval and the light cone.
- *Biquaternion Polar Representation* (`articles_maths/biquaternion-polar-representation.md`), for the theorem, the algorithm and the uniqueness of the four factors.
- *Biquaternion Partial Polar Representations* (`articles_maths/biquaternion-partial-polar-representations.md`), for the three pairings of the four factors, which is the complementary way of losing factors.
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), for the six subspaces, the involutions, the four blocks, the intersections and the norm form of each subspace.
- *The Center Subspace C_B as the Complex Time Sector* (`articles_physics/the-center-subspace-c-b-as-the-complex-time-sector.md`), for the center on its own terms.
- *The Vector Subspace Vect(B) as the Complex Space Sector* (`articles_physics/the-vector-subspace-vect-b-as-the-complex-space-sector.md`), for the complex null cone and the derived subspace.
- *The Quaternion Subspace H_B as the Real Sector* (`articles_physics/the-quaternion-subspace-hb-as-the-real-sector.md`), for the real quaternions and their polar form.
- *The Anti-Quaternion Subspace iH_B as the Imaginary Sector* (`articles_physics/the-anti-quaternion-subspace-ihb-as-the-imaginary-sector.md`), for the antiquaternions.
- *The Hermitian Subspace M+ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the boosts and the information reading.
- *The Anti-Hermitian Subspace M- as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`), for the four-vectors and the light cone.
- *The 2×2 Matrix Representation of Biquaternions* (`articles_physics/the-2x2-matrix-representation-of-biquaternions.md`), for the matrix classes of the six subspaces and $\det\Phi(\tilde{Q}) = N(\tilde{Q})$.
