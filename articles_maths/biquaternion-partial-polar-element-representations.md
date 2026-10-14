# __Biquaternion Partial Polar Element Representations__

## Introduction

The companion article *The Polar Element Representation of Biquaternions* writes a biquaternion with non-vanishing norm as four factors,

$$
\tilde{Q} = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} ,
$$

where the four factors are

- $r \in \mathbb{R}$, $r>0$, the positive real **scale**;
- $e^{i\alpha}$ with $\alpha \in \mathbb{R}$, the central **phase**, fixed to the branch $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$;
- $\tilde U_{\mathrm b}$, the Hermitian positive **boost** of unit norm ($\tilde U_{\mathrm b} \in \mathbb{M}_+$, $\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1$);
- $\tilde u_{\mathrm r}$, the **rotor**, a unit real quaternion ($\tilde u_{\mathrm r} \in \mathrm{Sp}(1)$).

This article is about the three two-factor representations that are obtained from it by grouping the four factors in pairs, and it proves that the Hamilton and complex representations of the biquaternion literature, together with the Cartan representation used throughout the physics articles, are exactly those groupings.

The result is a classification, and it has one sentence: there are exactly three ways to split four objects into two unordered pairs, so there are exactly three partial polar representations of a biquaternion, and they are

$$
\tilde{Q} = \underbrace{\big(r\,e^{i\alpha}\big)}_{R}\underbrace{\big(\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}\big)}_{\exp(\hat\Xi\Theta)} , \qquad
\tilde{Q} = \underbrace{\big(r\,\tilde u_{\mathrm r}\big)}_{Q}\underbrace{\big(e^{i\alpha}\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\big)}_{\exp(i\Psi)} , \qquad
\tilde{Q} = \underbrace{\big(r\,\tilde U_{\mathrm b}\big)}_{H}\underbrace{\big(e^{i\alpha}\,\tilde u_{\mathrm r}\big)}_{U} .
$$

The first is the Hamilton representation, whose modulus is the complex scalar $R = re^{i\alpha} \in \mathbb{C}_{\mathbb{B}}$ and whose second factor is $\exp(\hat\Xi\Theta)$ for a root $\hat\Xi$ of $-e_0$ and a complex angle $\Theta \in \mathbb{C}$; the second is the complex representation, whose modulus is the real quaternion $Q = r\tilde u_{\mathrm r} \in \mathbb{H}_{\mathbb{B}}$ and whose second factor is $\exp(i\Psi)$ for a central imaginary $i\Psi \in \mathbb{C}_{\mathbb{B}}$; the third is the Cartan representation, whose modulus is the Hermitian positive element $H = r\tilde U_{\mathrm b} \in \mathbb{M}_+$ and whose second factor is $U = e^{i\alpha}\tilde u_{\mathrm r}$. In each case the modulus of the named representation is a product of two of the four factors, and the second factor is the product of the other two, conjugated when necessary so that the order is restored.

Two consequences follow immediately and are the reason the partial representations are called partial.

- **The domain depends on the pairing.** Each representation is available only when its modulus can be computed from the element, and the three conditions differ: the Hamilton representation needs the vector part to be non-null so that its axis can be normalised; the complex representation as constructed from the element's parts needs the real quaternion part to be invertible; and only the Cartan representation shares the domain of the polar representation, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$.
- **Each calls a composite object the modulus.** The four-factor representation is what separates that object into a genuine scale and a genuine phase, or into a scale and a rotor, or into a scale and a boost.

The three named representations are therefore incomplete in a precise sense, not merely in the loose sense of being less general: each is the polar representation with a coarser grouping, and each loses the factors that the grouping merges.

Two further points are recorded in the Hamilton section, because they belong to the representation rather than to the algebra: the representation of $\tilde{Q}$ is not the representation of its exponential, and the three parameters carry correlated ambiguities that the branch choices remove and that survive as the multivaluedness of the logarithm.

The conventions are those of the corpus, and the four factors, their definitions, the modulus $\rho = re^{i\alpha} = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, the rotor's group $\mathrm{Sp}(1) = \{\tilde u_{\mathrm r} \in \mathbb{H} : \tilde u_{\mathrm r}\tilde u_{\mathrm r}^{\natural} = 1\}$ of unit real quaternions and the domain $\{N\neq0\}$ are those of the companion article and are not re-derived here. The Hamilton and complex representations are stated in the standard form of the literature, with their moduli $R$ and $Q$ and their angles $\Theta$ and $\Psi$, so that the regroupings can be checked against those definitions. No physics is invoked.

## The Four Factors as Exponentials

The four factors are exponentials, and the three groupings of this article are the three ways of pairing four exponentials. With the rapidity $\psi \in \mathbb{R}$, $\psi\ge0$, of the boost and its unit axis $\hat u_{\mathrm b} \in \mathcal{A}$, the axis sphere of unit vectors of $\mathbb{R}^3$, and the rotation angle $\theta \in [0,2\pi]$ of the rotor and its unit axis $\hat u_{\mathrm r} \in \mathcal{A}$, the word is

$$
\tilde{Q} = \exp(\ln r)\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) .
$$

| # | factor | name | real dimension | exponential | case | closed form | parameter and range | unit axis |
|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | $1$ | $\exp(\ln r)$ | hyperbolic | $r$ | $r \in \mathbb{R}_{>0}$ | $e_0$ |
| 2 | $e^{i\alpha}$ | central phase | $1$ | $\exp(i\alpha)$ | trigonometric | $\cos\alpha + i\sin\alpha$ | $\alpha \in (-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | $i$ |
| 3 | $\tilde U_{\mathrm b}$ | boost | $3$ | $\exp\bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\bigr)$ | hyperbolic | $\cosh\tfrac{\psi}{2} + i\sinh\tfrac{\psi}{2}\,\hat u_{\mathrm b}$ | rapidity $\psi \ge 0$ | $i\hat u_{\mathrm b}$ |
| 4 | $\tilde u_{\mathrm r}$ | rotor | $3$ | $\exp\bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\bigr)$ | trigonometric | $\cos\tfrac{\theta}{2} + \sin\tfrac{\theta}{2}\,\hat u_{\mathrm r}$ | rotation angle $\theta \in [0,2\pi]$ | $\hat u_{\mathrm r}$ |

Each exponent is a real parameter times a **root** of the algebra, and the square of that root decides the character of the exponential: for a root $\nu \in \mathbb{B}$ and a real $t \in \mathbb{R}$, the trigonometric case is $\exp(\nu t) = \cos t\,e_0 + \nu\sin t$ at $\nu^2 = -e_0$, the hyperbolic case is $\exp(\nu t) = \cosh t\,e_0 + \nu\sinh t$ at $\nu^2 = +e_0$, and the parabolic case is the truncation $\exp(\nu t) = e_0 + \nu t$ at $\nu^2 = 0$. The scale and the boost occupy the hyperbolic case, with the real root $e_0$ and the Hermitian root $i\hat u_{\mathrm b}$, and the phase and the rotor occupy the trigonometric case, with the central root $i$ and the real pure quaternion root $\hat u_{\mathrm r}$; the parabolic row carries no factor of the word. The root of each exponential is the reason the factor lies where it does in the algebra: the hyperbolic row gives the factor in $\mathbb{M}_+$ for the non-trivial boost exponent and on the positive real axis for the scale, and the trigonometric row gives the central phase and the rotor in $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$.

The pairing carried out in this article is a grouping of the exponentials, and the two exponents of a pair multiply as exponentials only when the pair commutes with the rest of the word up to the conjugation that restores the order. The Hamilton and the complex groups are the two pairings whose second factor is a single exponential, $\exp(\hat\Xi\Theta)$ and $\exp(i\Psi)$, and the Cartan group is the pairing whose second factor, $e^{i\alpha}\tilde u_{\mathrm r}$, is a product of two exponentials and is therefore not written as one; this is the exponential reason the four-factor representation separates an object that each named representation calls the modulus.

**The grouping is not free, because the exponents do not all commute.** The boost exponent and the rotor exponent fail to commute, so the pair products are **not** the exponentials of sums of exponents: $\exp(\hat\Xi\Theta)$ and $\exp(i\Psi)$ are computed from the element, not by adding the four exponents, and the Cartan second factor is a product of two exponentials that is no single exponential. Over $60$ random boosts and rotors the largest coefficient of the bracket of the two non-central exponents is $3.58$, and the largest coefficient of the failure of the sum rule is $0.76$. The three pairings stand as three distinct groupings of the same ordered word; none of them is obtained from another by reordering, and within the Cartan grouping the boost and the rotor may not be interchanged.

## The Four Factors and the Three Pairings

### The Factors

The four factors of the polar representation of an element with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$ are

$$
r \in (0,\infty), \qquad e^{i\alpha} \in \mathbb{C}_{\mathbb{B}}, \quad |e^{i\alpha}| = 1, \qquad \tilde U_{\mathrm b} \in \mathbb{M}_+, \quad \langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1, \qquad \tilde u_{\mathrm r}\in\mathbb{H}_{\mathbb{B}}, \quad \langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1, \quad \tilde u_{\mathrm r}\in\mathrm{Sp}(1) ,
$$

in the canonical order $\tilde{Q} = r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$. Two structural facts about them govern every regrouping below. The phase $e^{i\alpha}$ is central, so it may be moved freely across the other factors. The boost and the rotor are not central, so moving one past the other conjugates it: for any element $\tilde{Q}$,

$$
\tilde u_{\mathrm r}\,\tilde{Q} = \left(\tilde u_{\mathrm r}\tilde{Q}\tilde u_{\mathrm r}^{-1}\right)\tilde u_{\mathrm r} , \qquad \tilde u_{\mathrm r}^{-1}\tilde{Q} = \left(\tilde u_{\mathrm r}^{-1}\tilde{Q}\tilde u_{\mathrm r}\right)\tilde u_{\mathrm r}^{-1} ,
$$

which is the algebraic statement that a rotated object in the conjugate position is the same object.

### The Pairings

A **pairing** of the four factors is a splitting of the list $\{r, e^{i\alpha}, \tilde U_{\mathrm b}, \tilde u_{\mathrm r}\}$ into two unordered pairs, each pair then being multiplied together in the canonical order. The three pairings are displayed in the introduction. Written in the canonical order $\tilde{Q} = r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, they are obtained by inserting a parenthesis and, where a factor has crossed another, recording the conjugation:

$$
r\Big(e^{i\alpha}\Big)\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \Big(re^{i\alpha}\Big)\Big(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\Big) ,
$$

$$
r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \Big(r\tilde u_{\mathrm r}\Big)\Big(e^{i\alpha}\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\Big) ,
$$

$$
r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \Big(r\tilde U_{\mathrm b}\Big)\Big(e^{i\alpha}\tilde u_{\mathrm r}\Big) .
$$

In the second line the rotor has been moved to the left of the boost; the phase, being central, needed no correction; and the boost has been conjugated by the rotor, which is the conjugation that appears in the middle factor. The three right-hand sides are the Hamilton, complex and Cartan representations respectively.

### Why There Are Exactly Three

The number of partial representations is not a matter of taste. A pairing of a four-element set into two unordered pairs is the same as a partition of the set into two subsets of size two, and the number of such partitions is

$$
\frac{1}{2}\binom{4}{2} = 3 ,
$$

the factor $\tfrac12$ accounting for the fact that the two pairs are unordered. There are no other groupings of four objects into two factors, so there are no further two-factor polar representations of a biquaternion. Groupings into one and three factors are the polar representation itself and its trivial refinements, and are not two-factor representations.

## The Hamilton Representation

### The Pairing

The Hamilton representation is the pairing of the scale with the phase against the boost with the rotor:

$$
\tilde{Q} = R\,\exp(\hat\Xi\Theta), \qquad R = r\,e^{i\alpha} = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}, \qquad \exp(\hat\Xi\Theta) = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} .
$$

The modulus is the complex scalar $\rho$ of the polar representation, and the exponential is the whole rotor part, boost and rotation together. The identification of $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with a single exponential is the content of the companion article's construction, and it is the reason the Hamilton representation is the closest of the three to the quaternion polar representation: when all four coefficients are real, $\tilde U_{\mathrm b} = e_0$, $\tilde u_{\mathrm r}$ is the unit quaternion, and the representation reduces to $q = r\exp(\mu\tfrac{\theta}{2})$ term by term.

Both factors of the exponential are themselves exponentials of a single element, so the Hamilton factor is the single exponential of a **product of two exponentials**. The boost is

$$
\tilde U_{\mathrm b} = \exp\Bigl(i\frac{\psi}{2}\hat u_{\mathrm b}\Bigr) = \cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\hat u_{\mathrm b} ,
$$

with $\hat u_{\mathrm b}$ a unit vector and $\psi$ the rapidity, and the rotor is

$$
\tilde u_{\mathrm r} = \exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) = \cos\tfrac{\theta}{2}\,e_0 + \sin\tfrac{\theta}{2}\,\hat u_{\mathrm r} ,
$$

with $\hat u_{\mathrm r}$ a unit vector and $\theta$ the rotation angle. Each exponent is a parameter times a root of $\pm e_0$: $i\hat u_{\mathrm b}$ is a Hermitian root of $+e_0$ and $\hat u_{\mathrm r}$ a real pure root of $-e_0$. Their product is again a single exponential because the vector part is non-null on the domain of the representation, and its angle is the complex $\Theta$ whose real part is the rotation angle and whose imaginary part is the rapidity.

### The Statement

The representation is stated as follows. Write $\tilde{Q} = Q_0e_0+\vec Q$ with vector part $\vec Q = Q_1e_1+Q_2e_2+Q_3e_3$, suppose $(\vec Q,\vec Q) = Q_1^2+Q_2^2+Q_3^2 \neq 0$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$, and put

$$
R = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}, \qquad \hat\Xi = \frac{\vec Q}{B}, \qquad B = \sqrt{(\vec Q,\vec Q)}, \qquad \cos\Theta = \frac{Q_0}{R}, \qquad \sin\Theta = \frac{B}{R} .
$$

Then $\tilde{Q} = R(\cos\Theta+\hat\Xi\sin\Theta)$, and $\hat\Xi$ is a root of $-1$: $\hat\Xi^2 = \vec Q^2/B^2 = -(\vec Q,\vec Q)/B^2 = -1$, since the square of a pure biquaternion is $-\left(\vec Q,\vec Q\right)e_0$. The angle $\Theta$ is complex and the modulus $R$ is complex, and the constraint $\cos^2\Theta+\sin^2\Theta = 1$ is the identity $Q_0^2+(\vec Q,\vec Q) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$.

### The Constraint on the Axis

The axis of the Hamilton representation is not an arbitrary root of $-1$: it is the root parallel to the vector part of the element, and the parallelism is what makes the representation canonical. The accompanying constraints $\operatorname{Re}(\hat\Xi)\perp\operatorname{Im}(\hat\Xi)$ and $\|\operatorname{Re}\hat\Xi\|^2-\|\operatorname{Im}\hat\Xi\|^2 = 1$ are those of the companion article on the roots of minus one.

The constraint is exactly what fails when the vector part is null. If $(\vec Q,\vec Q) = 0$ then $B = 0$, the axis $\hat\Xi = \vec Q/B$ cannot be normalised, and the exponential factor has no axis to be built from. The pairing of the four factors still exists as a product, $\tilde{Q} = (re^{i\alpha})(\tilde U_{\mathrm b}\tilde u_{\mathrm r})$, but it is not a Hamilton representation, because the second factor cannot be written as an exponential along the vector part.

### The Domain

The Hamilton representation is therefore available on

$$
\left\{\tilde{Q} : \langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0 \ \text{ and } \ (\vec Q,\vec Q)\neq0\right\},
$$

which is the complement of the union of the null cone and the quadric cone $(\vec Q,\vec Q) = 0$. The second condition is not implied by the first and is not weaker: the element $1+e_1+ie_2$ has $N = 1$ and $(\vec Q,\vec Q) = 1+i^2 = 0$, so it is invertible and has no Hamilton representation. Within its domain the representation is unique once the branch of $R = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ is fixed; the literature states the uniqueness as up to the correlated replacement $(R,\Theta)\mapsto(-R,\Theta+\pi)$, which the branch choice of the polar representation removes.

### The Exponential of the Element

The representation $\tilde{Q} = R\exp(\hat\Xi\Theta)$ is a statement about $\tilde{Q}$ itself, and it must not be read as a statement about its exponential. Write $\vec Q = B\hat\Xi$ and $\tilde{Q} = Q_0e_0 + B\hat\Xi$. Since $Q_0e_0$ is central,

$$
\exp(\tilde{Q}) = e^{Q_0}\exp(B\hat\Xi) = e^{Q_0}\bigl(\cos B\,e_0 + \sin B\,\hat\Xi\bigr),
$$

using $\hat\Xi^2 = -e_0$ as above. The right-hand side is the Hamilton representation of the element $\exp(\tilde{Q})$, with modulus $e^{Q_0}$ and angle $B$; it is not the Hamilton representation of $\tilde{Q}$, whose modulus and angle are $R$ and $\Theta$. The two Hamilton data therefore agree only in the special case

$$
R = e^{Q_0} \ \text{ and }\ \Theta = B, \qquad\text{that is,}\qquad \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \exp(2Q_0) \ \text{ and the angle } \Theta \text{ equals } B ,
$$

by the identity $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = Q_0^2 + B^2$. In general the inverse relation is the one that holds: the logarithm of $\tilde{Q}$ reads off its own modulus and angle, $\log\tilde{Q} = \log R\,e_0 + \Theta\,\hat\Xi$ (*Biquaternion Elementary Functions*, §*The Logarithm*), so it is the logarithm, not the exponential, that recovers $(R,\Theta)$ from the element. The distinction matters whenever an element and its exponential are both in play, as for the exponential map of $\mathbb{B}^\times$ in *Biquaternion Lie Group and Exponential Structure*.

### Non-Uniqueness of the Parameters

The three parameters of the Hamilton representation are not determined independently; the representation is unique only up to three correlated replacements.

1. **The axis is defined up to sign.** The relation $\vec Q = B\hat\Xi$ determines $\hat\Xi$ only together with the sign of $B = \sqrt{(\vec Q,\vec Q)}$, since $B$ is a square root; replacing $B$ by $-B$ replaces $\hat\Xi$ by $-\hat\Xi$ and leaves both $\hat\Xi^2 = -e_0$ and $\vec Q$ unchanged.
2. **The angle is defined up to sign, correlated with the axis.** Replacing $(\hat\Xi,\Theta)$ by $(-\hat\Xi,-\Theta)$ leaves $\tilde{Q} = R(\cos\Theta + \hat\Xi\sin\Theta)$ fixed, because the two changes cancel in the term $\hat\Xi\sin\Theta$.
3. **The modulus is defined up to sign, correlated with a shift of the angle.** Replacing $(R,\Theta)$ by $(-R,\Theta+\pi)$ gives the same element, since $\cos(\Theta+\pi) = -\cos\Theta$ and $\sin(\Theta+\pi) = -\sin\Theta$.

Fixing the branches removes the first and the third: the four-factor representation fixes the modulus as $R = \rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ with $r>0$, and a choice of the square root $B$ fixes the axis; then $\hat\Xi$ and $\Theta$ are determined up to the period of the angle. What remains is the ambiguity of $\Theta$ modulo $2\pi$, which is precisely the multivaluedness of the logarithm: the branches of $\log\tilde{Q}$ differ by the kernel of the exponential, and the power functions inherit the ambiguity. This is why the logarithm and the powers are many-valued on $\mathbb{B}^\times$ while the exponential is single-valued.

## The Complex Representation

### The Pairing

The complex representation is the pairing of the scale with the rotor against the phase with the boost:

$$
\tilde{Q} = Q\,\exp(i\Psi), \qquad Q = r\,\tilde u_{\mathrm r}, \qquad \exp(i\Psi) = e^{i\alpha}\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r} .
$$

The modulus is a real quaternion, of norm $\langle Q,Q\rangle_{\natural} = r^2$, and the exponential is central in its phase but not in its boost: the boost has been conjugated by the rotor, so that it can stand to the right of the modulus in the canonical order. Writing the conjugated boost as

$$
\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \cosh\theta_{\mathrm b}\,e_0 + i\sinh\theta_{\mathrm b}\,\hat u_{\mathrm b}', \qquad \theta_{\mathrm b} = \frac{\psi}{2},
$$

with $\psi$ the rapidity of $\tilde U_{\mathrm b}$ and $\hat u_{\mathrm b}'$ its axis rotated by the rotor, the exponent is

$$
\Psi = \alpha + \theta_{\mathrm b}\,\hat u_{\mathrm b}' ,
$$

a real quaternion with scalar part $\alpha$ and pure quaternion part $\theta_{\mathrm b}\hat u_{\mathrm b}'$. This is the arrangement in which the representation is stated: its $\Psi$ has a scalar part and a pure part, and the two travel together.

### The Statement

The representation is stated as follows. Write $\tilde{Q} = Q_r + iQ_i$ with $Q_r,Q_i\in\mathbb{H}$ the real and imaginary quaternion parts, suppose $Q_r \neq 0$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$, put $\tan\Psi = Q_r^{-1}Q_i$ and $Q = Q_r(\cos\Psi)^{-1}$. Then $\tilde{Q} = Q\exp(i\Psi)$ with $Q$ and $\Psi$ real quaternions. The verification is the computation $Q\exp(i\Psi) = Q_r(\cos\Psi)^{-1}(\cos\Psi+i\sin\Psi) = Q_r + iQ_r\tan\Psi = Q_r+iQ_i$, in which the two trigonometric factors commute because they are functions of the single quaternion $\Psi$.

### The Modulus Is a Real Quaternion

The modulus $Q = r\tilde u_{\mathrm r}$ of the pairing is exactly the modulus $Q_r(\cos\Psi)^{-1}$ of the construction from the element's parts. The identity is not a coincidence of two constructions; it follows from the polar representation. Since $Q = r\tilde u_{\mathrm r}$ is a real quaternion and $\exp(i\Psi)$ is an exponential of the central imaginary, the real quaternion part of $\tilde{Q} = Q\exp(i\Psi)$ is

$$
Q_r = Q\,\frac{\exp(i\Psi)+\exp(-i\Psi)}{2} = Q\cos\Psi ,
$$

because the complex conjugation of $\exp(i\Psi)$ is $\exp(-i\Psi)$ and the modulus $Q = r\tilde u_{\mathrm r}$ is fixed by it. Hence $Q = Q_r(\cos\Psi)^{-1}$, which is the construction formula. This identity was checked numerically on random elements with invertible $Q_r$, to $1.3\times10^{-12}$ in the coefficients.

### The Domain

The construction from the element's parts needs $Q_r^{-1}$, so the complex representation as constructed there is available on

$$
\left\{\tilde{Q} : \langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0 \ \text{ and } \ Q_r\neq0\right\},
$$

the condition $Q_r\neq0$ being equivalent to the invertibility of the real quaternion part because $\mathbb{H}$ is a division algebra.

The two conditions are again independent, and the second is met or missed independently of the first: the element $ie_1+ie_2$ has $N = -2\neq0$, so it is invertible, while its real quaternion part vanishes, so the construction fails on it; and the element $1+e_1+ie_2$ has $Q_r = 1+e_1 \neq 0$ but no Hamilton representation, so the two domains are not nested. Within its domain the representation is unique up to the replacement $\Psi\mapsto\Psi+\pi$ with the sign of $Q$ adjusted, which is the same branch question as before.

### The Pairing Without the Construction

A remark is in order, because it separates two distinct statements. The pairing $\tilde{Q} = (r\tilde u_{\mathrm r})\exp(i\Psi)$ is a grouping of the four factors of the polar representation, and the four factors exist whenever $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. Hence the **factorisation** of $\tilde{Q}$ as a real quaternion times an exponential of the central imaginary exists on the whole complement of the null cone, while the **construction** of it from the real quaternion part needs $Q_r$ invertible. On the element $ie_1+ie_2$ the pairing gives

$$
ie_1+ie_2 = \left(e_1+e_2\right)\,\exp\!\left(i\frac{\pi}{2}\right),
$$

with modulus $e_1+e_2$, which is a real quaternion, and exponent $\pi/2$, which is real: the factorisation holds, and the construction formula $\tan\Psi = Q_r^{-1}Q_i$ is what fails, since $Q_r = 0$ has no inverse. The distinction between the factorisation and the construction is recorded here because the domain of a partial representation is a statement about the construction, and the pairing is what shows it to be a grouping of the four factors.

## The Cartan Representation

### The Pairing

The Cartan representation is the pairing of the scale with the Lorentz boost against the phase with the rotor:

$$
\tilde{Q} = H\,U , \qquad H = r\,\tilde U_{\mathrm b}, \qquad U = e^{i\alpha}\,\tilde u_{\mathrm r} .
$$

The modulus is Hermitian positive and the second factor is unitary, so this is the matrix polar decomposition of the biquaternion: $\mathsf{M}_2(H)$ is the unique positive definite Hermitian square root of $\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^\dagger$ and $\mathsf{M}_2(U)$ is the unique unitary factor. Indeed

$$
\tilde{Q}\tilde{Q}^{*} = r^2\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*} \tilde U_{\mathrm b}^{*} = r^2\tilde U_{\mathrm b}^2 = H^2 ,
$$

using $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*} = e_0$, the Hermitian character of $\tilde U_{\mathrm b}$ and $\tilde U_{\mathrm b}^2 = S$, so $H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$ is the Hermitian positive square root, of norm $\langle H,H\rangle_{\natural} = r^2$.

### The Statement

The representation is the standard polar decomposition, and it needs no separate existence theorem: for $\tilde{Q}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$ the matrix $\mathsf{M}_2(\tilde{Q})$ is invertible, its polar decomposition is unique, and translating the two factors back through the algebra isomorphism gives $H$ and $U$ above. The modulus $H = r\tilde U_{\mathrm b}$ combines the positive real scale with the Hermitian positive boost, and the second factor $U = e^{i\alpha}\tilde u_{\mathrm r}$ combines the central phase with the rotor.

### The Modulus Is Hermitian Positive

The modulus of the Cartan representation lies in $\mathbb{M}_+$, the Hermitian subspace, which the physics articles call the informational sector, and it is positive definite in the matrix picture. Its determinant is $\langle H,H\rangle_{\natural} = r^2$, which is positive, so $H$ is invertible and carries the scale of the element; its traceless part carries the rapidity and axis of the boost, and its scalar part carries the scale. The Cartan decomposition of the unit group is the statement that the boosts and the rotations generate the unit-norm elements, and it is the same statement as the existence of this factorisation.

### The Domain

The Cartan representation is available on the whole complement of the null cone,

$$
\left\{\tilde{Q} : \langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0\right\},
$$

which is the domain of the polar representation itself. It is the only one of the three partial representations with that domain, and its uniqueness is the uniqueness of the matrix polar decomposition: the positive definite Hermitian factor is determined by $\tilde{Q}\tilde{Q}^{*}$ and the unitary factor is then determined as $H^{-1}\tilde{Q}$.

### The Published Form of the Pairing

The pairing $HU$ is the factorisation proved by Sangwine & Hitzer for the unit semi-norm elements and, in the general case, by their Corollary 1, in the reversed word, angle first:

$$
\tilde{Q} = |\tilde{Q}|\,e^{\alpha\theta_t}\,e^{I\beta\theta_h},
$$

with $\alpha$ and $\beta$ pure real unit quaternions, $I\beta$ a pure imaginary unit biquaternion, and two real angles $\theta_t$ and $\theta_h$. Translating their letters into those of this article, the trigonometric exponential $e^{\alpha\theta_t}$ is the rotor $\tilde u_{\mathrm r} = \exp\bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\bigr)$ and the hyperbolic exponential $e^{I\beta\theta_h}$ is the boost, not about the original axis but about the axis rotated by the rotor: their product is $H = T^{-1}\tilde U_{\mathrm b}T$ with $T$ the rotor, so their boost and the corpus boost $\tilde U_{\mathrm b}$ are conjugate, with the same rapidity and the same norm. Their complex modulus $|\tilde{Q}|$ stands where the corpus writes the scale and the phase together.

Three differences are worth recording, because a reader arriving from the paper meets them. The **order** is reversed: the two non-central factors are written angle first there and boost first here, and the two words are related by the conjugation above, the rotor itself being invariant under the reversal. The **count** differs: their $2+3+3 = 8$ keeps the complex modulus whole, where the corpus writes $1+1+3+3 = 8$ with the phase split off, and the paper explicitly declines to split a complex exponential into a scale and a unit phase. And the **branch and the uniqueness** of the general form are fixed and proved here, at $\alpha\in(-\pi/2,\pi/2]$, while the paper states neither and admits both orders. The mathematics of the pairing is the same in both places; what the corpus adds is the split of the modulus, the branch, and the uniqueness.

## The Domain Comparison

### The Table

| representation | modulus | second factor | available when | condition on the element |
|---|---|---|---|---|
| Hamilton | $R = re^{i\alpha}$, complex scalar | $\exp(\hat\Xi\Theta) = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $(\vec Q,\vec Q)\neq0$ and $N\neq0$ | the vector part is non-null |
| complex | $Q = r\tilde u_{\mathrm r}$, real quaternion | $\exp(i\Psi) = e^{i\alpha}\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $Q_r\neq0$ and $N\neq0$ for the construction; $N\neq0$ for the pairing | the real quaternion part is invertible |
| Cartan | $H = r\tilde U_{\mathrm b}$, Hermitian positive | $U = e^{i\alpha}\tilde u_{\mathrm r}$, unitary | $N\neq0$ | none beyond invertibility |
| polar representation | four factors | four factors | $N\neq0$ | none beyond invertibility |

### The Inclusions and the Counterexamples

The domains are not nested. The domain of the Cartan representation contains the other two, and the Hamilton and complex domains overlap without containing each other. The following elements separate the cases, and each is computed in the examples below.

| element | $N$ | $(\vec Q,\vec Q)$ | $Q_r$ | Hamilton | complex | Cartan |
|---|---|---|---|---|---|---|
| $(1+i)e_0+e_1+2e_2$ | $5+2i$ | $5$ | $1+e_1+2e_2$ | yes | yes | yes |
| $1+e_1+ie_2$ | $1$ | $0$ | $1+e_1$ | no | yes | yes |
| $ie_1+ie_2$ | $-2$ | $-2$ | $0$ | yes | no | yes |
| $i$ | $-1$ | $0$ | $0$ | no | no | yes |

The first line is the generic case, in which all three representations are available and give three different groupings of the same four factors. The second line separates the Hamilton representation from the other two: the element is invertible and has an invertible real part, but its vector part is null, so no axis exists. The third line separates the complex representation from the other two: the vector part is non-null and the real part vanishes. The fourth line, the scalar imaginary, fails the two conditions simultaneously and lies outside both named representations; it is nevertheless an invertible element, and the polar representation is $i = 1\cdot e^{i\pi/2}\cdot e_0\cdot e_0$.

The union of the three domains is the whole complement of the null cone, and the elements that the Hamilton and complex representations miss between them are exactly the nonzero purely imaginary complex scalars. The reason is elementary: $Q_r = 0$ means that every coefficient is purely imaginary, $Q_\mu = ib_\mu$ with $b_\mu\in\mathbb{R}$, and then

$$
(\vec Q,\vec Q) = \sum_{k=1}^{3}(ib_k)^2 = -\sum_{k=1}^{3}b_k^2 \leq 0 ,
$$

a negative real that vanishes only when $b_1 = b_2 = b_3 = 0$; verified to $3.6\times10^{-15}$ over constructed purely imaginary elements, with the imaginary part of $(\vec Q,\vec Q)$ vanishing identically. So the two conditions fail together only on $\tilde{Q} = ib_0e_0$, $b_0\neq0$. Each such element lies in the Cartan domain, with $r = |b_0|$, $\alpha = \pm\pi/2$, $H = |b_0|e_0$ and $U = \pm ie_0$; and it has an ordinary complex polar form $ib_0 = |b_0|\exp(\pm i\pi/2)$, which is the complex representation of the algebra only in the degenerate sense of the section on the two degenerate limits below.

### Why the Four-Factor Form Is the Reference

Two properties of the polar representation explain its role as the reference of the series, and neither is shared by the named representations.

**Its domain is the largest.** The only obstruction is the vanishing of the biquaternion norm, which is the vanishing of the determinant of the matrix image. The partial representations fail on additional sets, and each failure is a failure to construct a modulus from the element: an axis cannot be normalised, or a quaternion cannot be inverted.

**Its modulus separates into a scale and a phase.** The Hamilton representation calls the complex number $R = re^{i\alpha}$ the modulus, and one of its two constituents, $r$, is a positive real and the other, $e^{i\alpha}$, is central. The complex representation calls the real quaternion $r\tilde u_{\mathrm r}$ the modulus, one factor of which is a positive real and the other a rotation. The Cartan representation calls $r\tilde U_{\mathrm b}$ the modulus, one factor of which is a positive real and the other a boost. In each case a positive real scale is entangled with a non-scalar factor, and only the four-factor representation exhibits the scale by itself.

## The Two Degenerate Limits

Two exact statements identify which classical polar form each named representation generalises. Both are cases in which the element lies in a proper subalgebra of $\mathbb{B}$.

**A real quaternion.** If all four coefficients of $\tilde{Q}$ are real then $\tilde{Q}\in\mathbb{H}_{\mathbb{B}}$, the biquaternion norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2$ is a positive real, and with the principal branch of the square root

$$
R = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}} \in \mathbb{R}_{>0}, \qquad \cos\Theta = \frac{q_0}{R}\in[-1,1], \qquad \sin\Theta = \frac{|\vec q|}{R}\in[0,1] ,
$$

so both the modulus and the angle are real and $\hat\Xi = \vec q/|\vec q|$ is a unit pure real quaternion. The Hamilton representation is then the quaternion polar representation $q = r\exp(\mu\tfrac{\theta}{2})$ of the companion article *Quaternion Polar Element Representation*, with $r = R$, $\mu = \hat\Xi$ and $\theta = \Theta$ real, and the identification is exact rather than asymptotic: over $100$ random real quaternions the imaginary parts of $R$, $\cos\Theta$ and $\sin\Theta$ vanished identically. The complex representation is available on the same elements and is degenerate there: $Q_i = 0$, hence $\tan\Psi = 0$, $\Psi = 0$ and $Q = Q_r = \tilde{Q}$, a representation by a modulus alone.

**A complex scalar.** If $\tilde{Q} = Ae_0$ with $A\in\mathbb{C}$ then the vector part vanishes, so $B = 0$ and the Hamilton representation is unavailable, while the complex representation gives

$$
Q_r = (\operatorname{Re}A)e_0, \qquad Q_i = (\operatorname{Im}A)e_0, \qquad \tan\Psi = \frac{\operatorname{Im}A}{\operatorname{Re}A}\,e_0, \qquad Q = \frac{\operatorname{Re}A}{\cos\Psi}\,e_0 = |A|\,e_0 ,
$$

so that $\Psi = (\arg A)e_0$ is a scalar and $\tilde{Q} = |A|\exp\!\big(i(\arg A)e_0\big)$: the complex representation is the ordinary complex polar form of $\mathbb{C}$, with the central scalar imaginary of the algebra in the role of the scalar imaginary of $\mathbb{C}$ and the quaternion modulus collapsed to a scalar.

The two limits are disjoint, and together they are the reason the two named representations are complementary rather than competing: the Hamilton representation is the one that carries the quaternion polar form into the biquaternions, and the complex representation is the one that carries the complex polar form.

## Behaviour Under the Three Conjugations

The algebra has three nontrivial conjugations: quaternion conjugation ${}^{\natural}$, the anti-automorphism fixing the centre $\mathbb{C}_{\mathbb{B}}$; complex conjugation $\bar{\cdot}$, the automorphism conjugating every coefficient; and Hermitian conjugation ${}^{*} = {}^{\natural}\circ\bar{\cdot}$, the two operations commuting because one acts on the coefficients and the other on the units. The three act differently on the two named representations, and the difference is stated below as a computation rather than as a contrast of styles.

### The Hamilton Representation

In $\tilde{Q} = R\exp(\hat\Xi\Theta)$ the modulus $R$ and the angle $\Theta$ are complex scalars and therefore central, while the axis $\hat\Xi$ is pure, so that $\hat\Xi^{\natural} = -\hat\Xi$. Quaternion conjugation fixes the centre and reverses a pure element, complex conjugation is an automorphism and conjugates the three parameters, and Hermitian conjugation does both:

$$
(\tilde{Q})^{\natural} = R\exp(-\hat\Xi\Theta), \qquad \bar{\tilde{Q}} = \bar{R}\exp(\hat\Xi^{\natural}\bar{\Theta}), \qquad \tilde{Q}^{*} = \bar{R}\exp(-\hat\Xi^{\natural}\bar{\Theta}) .
$$

| conjugation | $R$ | $\hat\Xi$ | $\Theta$ | result |
|---|---|---|---|---|
| quaternion ${}^{\natural}$ | $R$ | $-\hat\Xi$ | $\Theta$ | $R\exp(-\hat\Xi\Theta)$ |
| complex $\bar{\cdot}$ | $\bar{R}$ | $\hat\Xi^{\natural}$ | $\bar{\Theta}$ | $\bar{R}\exp(\hat\Xi^{\natural}\bar{\Theta})$ |
| Hermitian ${}^{*}$ | $\bar{R}$ | $-\hat\Xi^{\natural}$ | $\bar{\Theta}$ | $\bar{R}\exp(-\hat\Xi^{\natural}\bar{\Theta})$ |

The consistency of the second row is a consequence of $\langle\bar{\tilde{Q}},\bar{\tilde{Q}}\rangle_{\natural} = \overline{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, hence $R(\bar{\tilde{Q}}) = \overline{R(\tilde{Q})}$; the computed defect in that identity was exactly zero over $100$ random elements. Over the same sample the largest defect in the four coefficients of the three identities of the table was $9.9\times10^{-16}$, and the identity $R(\cos\Theta+\hat\Xi\sin\Theta) = \tilde{Q}$ itself was verified on the same run to the same order. Only quaternion conjugation and Hermitian conjugation reverse the axis; complex conjugation preserves it and conjugates it.

### The Complex Representation

In $\tilde{Q} = Q\exp(i\Psi)$ the modulus $Q$ and the angle $\Psi$ are real quaternions, so $\bar{Q} = Q$ and $\bar{\Psi} = \Psi$, while $Q^{\natural}\neq Q$ and $\Psi^{\natural}\neq\Psi$ in general; the two factors need not commute, and it is this that makes the complex representation the less symmetric of the two under conjugation.

**Complex conjugation.** Since $\bar{\cdot}$ is an automorphism fixing $Q$ and $\Psi$ and conjugating the scalar imaginary,

$$
\bar{\tilde{Q}} = Q\exp(-i\Psi) :
$$

the modulus and the angle are both unchanged and only the sign of the exponent changes. Equivalently, the canonical angle of $\bar{\tilde{Q}}$ is $-\Psi$, because the real and imaginary quaternion parts of $\bar{\tilde{Q}}$ are $(Q_r,-Q_i)$, whence $\tan\Psi(\bar{\tilde{Q}}) = Q_r^{-1}(-Q_i) = -\tan\Psi$.

**Quaternion conjugation.** Since ${}^{\natural}$ is an anti-automorphism, the two factors exchange order:

$$
(\tilde{Q})^{\natural} = \exp(i\Psi^{\natural})\,Q^{\natural} ,
$$

which is not the canonical shape, the modulus of the complex representation being the left factor. Recovering the canonical shape requires the parts of the conjugated element, and the result is not the conjugate angle in general. The parts of $(\tilde{Q})^{\natural}$ are $(Q_r^{\natural},Q_i^{\natural})$, so its angle $\Psi'$ satisfies

$$
\tan\Psi' = (Q_r^{\natural})^{-1}Q_i^{\natural} , \qquad\text{whereas}\qquad (\tan\Psi)^{\natural} = Q_i^{\natural}(Q_r^{\natural})^{-1} ,
$$

and the two agree exactly when $Q_r^{\natural}$ and $Q_i^{\natural}$ commute, equivalently when $Q_r$ and $Q_i$ commute. The commuting case was verified to be exact and the non-commuting case to be genuinely different: the element

$$
\tilde{Q} = (1+e_1) + i(e_1+e_2), \qquad \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 2i, \qquad Q_r = 1+e_1\ \text{invertible} ,
$$

has $\tan\Psi = \tfrac12(1+e_1+e_2-e_3)$, conjugate $\tfrac12(1-e_1-e_2+e_3)$, and angle of the conjugated element $\tan\Psi' = \tfrac12(1-e_1-e_2-e_3)$; the two differ in the $e_3$ coefficient alone, the commutator being $Q_rQ_i-Q_iQ_r = 2e_3$.

**Hermitian conjugation.** Combining the two, $\tilde{Q}^{*} = \exp(-i\Psi^{\natural})\,Q^{\natural}$, again with the factors in the reversed order.

### The Cartan Representation

For $\tilde{Q} = HU$ with $H$ Hermitian positive and $U$ unitary, Hermitian conjugation gives

$$
\tilde{Q}^{*} = U^{*} H^{*} = U^{*} H = \big(U^{*} HU\big)U^{*} ,
$$

so the Hermitian factor of $\tilde{Q}^{*}$ is the conjugate $U^{*} HU$ of the original one and the unitary factor is $U^{*}$. Both factors of the pair therefore change, and here the pairing itself changes: the Cartan pair of $\tilde{Q}^{*}$ is not a regrouping of the four factors of $\tilde{Q}$, because a Hermitian element and a unitary element multiplied in the other order is not the same element. The identity and the Hermiticity of $U^{*} HU$ were checked to $3.2\times10^{-15}$ and $2.7\times10^{-15}$ over $100$ random pairs.

### What the Comparison Shows

The two named representations are distinguished by conjugation as sharply as by domain. For the Hamilton representation all three conjugations act on the parameters, ${}^{\natural}$ and ${}^{*}$ reversing the axis and $^*$ conjugating the three parameters, and the representation is closed under every one of them. For the complex representation $^*$ touches only the scalar imaginary of the exponent, while ${}^{\natural}$ and ${}^{*}$ exchange the order of the two factors, and ${}^{\natural}$ preserves the angle only when the two quaternion parts of the element commute. A statement about a biquaternion and its conjugates is therefore cheapest in the representation whose conjugation action it needs, and this is a second sense, independent of domain, in which the Hamilton and complex representations are complementary.

## Worked Examples

### One Element, Three Representations

Take $\tilde{Q} = (1+i)e_0+e_1+2e_2$, the generic element of the table above. Its polar representation, computed in the companion article, is

$$
r = 2.320595787, \quad \alpha = 0.190253189, \quad \tilde U_{\mathrm b} = 1.072349609\,e_0 - 0.173166789\,i\,e_1 - 0.346333577\,i\,e_2, \quad \tilde u_{\mathrm r} = 0.470592172\,e_0+0.394599292\,e_1+0.789198585\,e_2 .
$$

*The Hamilton regrouping.* The vector part is $\vec Q = e_1+2e_2$, so $(\vec Q,\vec Q) = 5$ and $B_0 = \sqrt{5} = 2.236067978$; the axis is $\hat\Xi = (e_1+2e_2)/\sqrt{5} = 0.447213595\,e_1+0.894427191\,e_2$, which satisfies $\hat\Xi^2 = -1$. The modulus is $R = \rho = 2.278723854+0.438842117i$, and the complex angle is fixed by

$$
\cos\Theta = \frac{Q_0}{R} = 0.504639332+0.341657461i, \qquad \sin\Theta = \frac{\sqrt{5}}{R} = 0.946188580-0.182219271i ,
$$

so that $\tilde{Q} = R(\cos\Theta+\hat\Xi\sin\Theta)$; the reconstruction was checked to $3.9\times10^{-14}$ over random elements. The identity $\exp(\hat\Xi\Theta) = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ then holds term by term, both sides being $\tilde{Q}/R$, and with it the equality of the Hamilton representation with the first pairing of the four factors.

*The complex regrouping.* The modulus is the real quaternion

$$
Q = r\tilde u_{\mathrm r} = 1.092054\,e_0 + 0.915705\,e_1 + 1.831411\,e_2 ,
$$

matching the modulus $Q_r(\cos\Psi)^{-1}$ of the construction with $Q_r = 1+e_1+2e_2$, and the exponent is

$$
\Psi = \alpha + \frac{\psi}{2}\hat u_{\mathrm b}' = 0.190253 - 0.169101\,e_1 - 0.338202\,e_2 ,
$$

where $\psi = 0.756273220$ is the rapidity of $\tilde U_{\mathrm b}$ and $\hat u_{\mathrm b}' = -(1,2,0)/\sqrt5$ is its axis, unchanged by the rotor because the rotor's axis is parallel to it. The reconstruction $\tilde{Q} = Q\exp(i\Psi)$ holds to $1.1\times10^{-12}$ on random elements.

*The Cartan regrouping.* The modulus is

$$
H = r\tilde U_{\mathrm b} = 2.488489985\,e_0 - 0.401850120\,i\,e_1 - 0.803700241\,i\,e_2 ,
$$

Hermitian positive with $\langle H,H\rangle_{\natural} = r^2 = 5.385164807$, and the unitary factor is

$$
U = e^{i\alpha}\tilde u_{\mathrm r} = (0.462100989+0.088992519i)e_0 + (0.387479295+0.074621694i)e_1 + (0.774958590+0.149243388i)e_2 .
$$

The reconstruction $\tilde{Q} = HU$ was checked to $2.2\times10^{-16}$.

The three regroupings of the same four factors are therefore displayed on one element, and their moduli are visibly different objects: a complex scalar, a real quaternion, and a Hermitian positive biquaternion.

### The Element with a Null Vector Part

Take $\tilde{Q} = 1+e_1+ie_2$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1+1+i^2 = 1$ and $(\vec Q,\vec Q) = 1+i^2 = 0$, so the Hamilton representation does not exist: $B_0 = 0$ and the axis is undefined. The other two representations do exist, with

$$
r = 1, \qquad \alpha = 0, \qquad \tilde U_{\mathrm b} = 1.414213562\,e_0 + 0.707106781\,i\,e_2 + 0.707106781\,i\,e_3, \qquad \tilde u_{\mathrm r} = 0.707106781\left(e_0+e_1\right) ,
$$

so that the complex modulus is $Q = \tilde u_{\mathrm r} = 0.707106781(e_0+e_1)$ and the Cartan modulus is $H = \tilde U_{\mathrm b}$. The modulus computed from the parts, $Q_r(\cos\Psi)^{-1}$, is the same quaternion, and this equality is the identity proved in the section on the complex representation above; the element is also the non-scalar example of that section.

### The Element with a Vanishing Real Part

Take $\tilde{Q} = ie_1+ie_2$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -2$ and $Q_r = 0$, so the construction of the complex representation from the element's parts fails. The polar representation gives

$$
r = \sqrt{2}, \qquad \alpha = \frac{\pi}{2}, \qquad \tilde U_{\mathrm b} = e_0, \qquad \tilde u_{\mathrm r} = \frac{e_1+e_2}{\sqrt{2}} ,
$$

so the Hamilton representation exists, with $B_0 = \sqrt{-2} = i\sqrt{2}$, axis $\hat\Xi = (e_1+e_2)/\sqrt2$, $R = i\sqrt2$, $\cos\Theta = 0$ and $\sin\Theta = 1$:

$$
\tilde{Q} = i\sqrt{2}\,\exp\!\left(\frac{e_1+e_2}{\sqrt2}\frac{\pi}{2}\right) .
$$

The complex representation's pairing, on the other hand, exists with modulus $r\tilde u_{\mathrm r} = e_1+e_2$ and exponent $\Psi = \alpha = \pi/2$, as recorded above. The example therefore exhibits both the failure of the construction and the existence of the factorisation.

### The Scalar Imaginary

Take $\tilde{Q} = i$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -1$, so the element is invertible and the polar representation is $i = 1\cdot e^{i\pi/2}\cdot e_0\cdot e_0$: the scale is one and the boost and the rotor are trivial. Both partial constructions fail, since $\vec Q = 0$ and $Q_r = 0$. The Cartan representation is available and reads $i = e_0\cdot i$, with modulus $e_0$ and unitary factor $i$: the central phase of the polar representation has been absorbed into the unitary factor, which is exactly the grouping that defines the Cartan representation. The example is the clearest single illustration of the difference between having a representation and being able to construct one from the element's parts.

## Summary

The polar representation of a biquaternion has four factors, so it has exactly three pairings, and they are the Hamilton representation $R\exp(\hat\Xi\Theta)$ with $R = re^{i\alpha}$ and the exponential $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, the complex representation $Q\exp(i\Psi)$ with $Q = r\tilde u_{\mathrm r}$ and the exponential $e^{i\alpha}\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, and the Cartan representation $HU$ with $H = r\tilde U_{\mathrm b}$ and $U = e^{i\alpha}\tilde u_{\mathrm r}$. Each is obtained from the polar representation by multiplying two factors together, with a conjugation when the rotor has to cross the boost, and each is unique within its domain once the branch of the square root of the biquaternion norm is fixed. The Hamilton representation needs the vector part non-null, the complex representation as constructed needs the real quaternion part invertible, and the Cartan representation needs only $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$; the three domains are not nested, the Cartan domain contains the other two, the union of the three is the complement of the null cone, and the only elements in none of the first two are the purely imaginary complex scalars. The four-factor representation is the reference because its domain is the complement of the null cone alone and because it separates the scale from the phase, from the rotor and from the boost, whereas each partial representation entangles the scale with one of the other three.

The three named representations are also distinguished by their behaviour under the conjugations.

- **Hamilton representation.** Quaternion conjugation and Hermitian conjugation reverse the axis and leave the angle, while complex conjugation conjugates the modulus, the axis and the angle.
- **Complex representation.** Complex conjugation flips only the scalar imaginary of the exponent, and quaternion conjugation and Hermitian conjugation exchange the order of the two factors, the angle being preserved exactly when the two quaternion parts of the element commute.
- **Cartan representation.** Hermitian conjugation replaces the pair $(H,U)$ by $(U^{*} HU, U^{*})$.

In the two degenerate limits the named representations reproduce the classical polar forms: a real quaternion gives the quaternion polar representation in the Hamilton representation, and a complex scalar gives the ordinary complex polar form in the complex representation. Two facts recorded in the Hamilton section belong to the representation rather than to the grouping: the polar form of $\tilde{Q}$ is not the polar form of $\exp(\tilde{Q})$, the two agreeing only when $R = e^{Q_0}$ and $\Theta = B$, and the three parameters are unique only up to the correlated replacements that the branch choices remove, the residue being the multivaluedness of the logarithm.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the polar representation, four factors |
| $r$, $e^{i\alpha}$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}\in\mathrm{Sp}(1)$ | scale, central phase, Hermitian positive boost, unit real quaternion rotor |
| $\rho = re^{i\alpha} = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ | the complex modulus of the four-factor representation |
| $\vec Q = Q_1e_1+Q_2e_2+Q_3e_3$ | the vector part of $\tilde{Q}$ |
| $(\vec Q,\vec Q) = Q_1^2+Q_2^2+Q_3^2$ | the general plain bilinear square of the vector part |
| $Q_r$, $Q_i$ | the real and imaginary quaternion parts of $\tilde{Q}$ |
| $R$ | Hamilton modulus, the complex scalar $\rho$ |
| $\hat\Xi$, $\Theta$ | Hamilton axis, parallel to $\vec Q$, and complex angle |
| $\exp(\tilde{Q})$ | the exponential; its Hamilton modulus $e^{Q_0}$ and angle $B$ are generally not those of $\tilde{Q}$ |
| $Q$ | complex modulus, the real quaternion $r\tilde u_{\mathrm r}$ |
| $\Psi = \alpha+\theta_{\mathrm b}\hat u_{\mathrm b}'$ | complex angle, a real quaternion |
| $\theta_{\mathrm b} = \psi/2$, $\hat u_{\mathrm b}'$ | half the boost rapidity, and the rotor-rotated boost axis |
| $H = r\tilde U_{\mathrm b}$, $U = e^{i\alpha}\tilde u_{\mathrm r}$ | Cartan modulus, Hermitian positive, and unitary factor |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | quaternion, complex and Hermitian conjugation |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the four factors, the modulus $\rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, the algorithm and the domain.
- *Biquaternion Elementary Functions* (`articles_maths/biquaternion-elementary-functions.md`), for the exponential, the logarithm and the power functions, which fix the parameters of the Hamilton representation and carry its multivaluedness.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the classification of the roots of $-1$ and the constraints on the Hamilton axis.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the null cone on which all four representations fail.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), for the quaternion polar representation that the Hamilton representation generalises, and which the complex representation reduces to on the real quaternions.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the identification of the Cartan representation with the matrix polar decomposition.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the Cartan representation $\tilde{U} = \tilde{B}\tilde{R}$ of the physics articles.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`) and *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the two-dimensional members of the series and the rule of the exponential $\exp(\nu\theta)$ that all four factors of these pairings are built from.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for Theorem 1 and Corollary 1, the published form of the Cartan pairing discussed in the section above.
