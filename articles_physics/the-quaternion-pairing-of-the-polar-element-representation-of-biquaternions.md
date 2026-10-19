# __The Quaternion Pairing of the Polar Element Representation of Biquaternions__

## Introduction

The quaternion pairing is the grouping of the polar word that puts the scale and the rotor on one side and the phase and the boost on the other. It writes the biquaternion as a **real quaternion modulus** times the exponential of a **real quaternion angle**,

$$
\tilde Q=\tilde q\,\exp(i\tilde\Psi),
\qquad \tilde q=r\,\tilde q_{\mathrm r},
\qquad \exp(i\tilde\Psi)=\exp(i\alpha)\,\tilde q_{\mathrm r}^{-1}B\tilde q_{\mathrm r}.
$$

The first factor is an ordinary quaternion in its polar form: a positive scale and a unit rotor. The second factor is the exponential of a central imaginary times a real quaternion angle; its scalar part is the phase and its pure part is the boost axis, rotated by the rotor.

The pairing is also a construction from the two real quaternion parts of the element. Write

$$
\tilde Q=\tilde q_r+i\tilde q_i,
\qquad \tilde q_r,\tilde q_i\in\mathbb{H}.
$$

Then, whenever $\tilde q_r$ is invertible and the norm does not vanish,

$$
\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i,
\qquad
\tilde q=\tilde q_r(\cos\tilde\Psi)^{-1}.
$$

The construction and the polar grouping give the same real quaternion modulus. That identity is the content of the article.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central $i$. An element is $\tilde Q=Q_te_t+\vec Q$, with complex coefficients. The quaternion conjugation is $\natural$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\overline{\ \cdot\ }^{\natural}$. The norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$, and the polar word is

$$
\tilde Q=r\exp(i\alpha)B\tilde q_{\mathrm r},
\qquad \rho=r\exp(i\alpha)=\sqrt{\langle\tilde Q\rangle_{\natural}},
$$

with $B=\exp(-i\eta\vec u_{\mathrm b})=\cosh\eta\,e_t-i\sinh\eta\,\vec u_{\mathrm b}$ the Hermitian positive unit-norm boost factor, and $\tilde q_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ a unit real quaternion. The symbols $r,\alpha,\eta,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r}$ are those of *The Polar Element Representation of Biquaternions*. The symbol $\eta$ is the frame rapidity, written $\psi$ in *The Polar Element Representation of Biquaternions*. The frame rotor is $\exp(i\eta\vec u_{\mathrm b}/2)$. The Hamilton and Cartan articles write the boost factor with $\psi/2$; the frame rotor is its inverse square root.

The physics articles write the boost factor as $B$ and the rotor as $\tilde q$; the present article uses $\tilde q_{\mathrm r}$ for the rotor and keeps $\tilde q$ for the quaternion modulus.

## The Two Real Quaternion Parts

Every biquaternion has a unique split

$$
\tilde Q=\tilde q_r+i\tilde q_i,
\qquad
\tilde q_r=\operatorname{Re}\tilde Q,
\qquad
\tilde q_i=\operatorname{Im}\tilde Q,
$$

with $\tilde q_r,\tilde q_i$ real quaternions. In coordinates,

$$
\tilde q_r=(\operatorname{Re}Q_t)e_t+(\operatorname{Re}Q_x)\vec e_x+(\operatorname{Re}Q_y)\vec e_y+(\operatorname{Re}Q_z)\vec e_z,
$$

and similarly for $\tilde q_i$ with the imaginary parts. The split is the decomposition of the complex vector space $\mathbb{B}$ into two real quaternion subspaces,

$$
\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}},
\qquad
\dim_{\mathbb{R}}\mathbb{H}_{\mathbb{B}}=\dim_{\mathbb{R}}i\mathbb{H}_{\mathbb{B}}=4.
$$

In the electromagnetic reading, $\tilde q_r$ is the electric part and $\tilde q_i$ the magnetic part of a biquaternionic field. The reading is a label on the two halves; the algebra below uses only the split.

The norm in the two parts is

$$
\langle\tilde Q\rangle_{\natural}
=\tilde q_r\tilde q_r^{\natural}-\tilde q_i\tilde q_i^{\natural}
+i\bigl(\tilde q_r\tilde q_i^{\natural}+\tilde q_i\tilde q_r^{\natural}\bigr),
$$

where the products are quaternion products and the two terms do not commute in general. The scalar part of the norm is $\lvert\tilde q_r\rvert^2-\lvert\tilde q_i\rvert^2$, the indefinite square; the imaginary part is the anticommutator sum. The norm is not the sum of the two quaternion norms; that sum is the scalar part of the Hermitian product below, and it agrees with the norm only when the imaginary quaternion part vanishes. The positive Euclidean square is therefore the scalar part of the Hermitian product, not of the norm.

The Hermitian product is simpler:

$$
\tilde Q\tilde Q^{*}
=(\tilde q_r+i\tilde q_i)(\tilde q_r^{\natural}-i\tilde q_i^{\natural})
=\tilde q_r\tilde q_r^{\natural}+\tilde q_i\tilde q_i^{\natural}
+i(\tilde q_i\tilde q_r^{\natural}-\tilde q_r\tilde q_i^{\natural}).
$$

Its scalar part is $\lvert\tilde q_r\rvert^2+\lvert\tilde q_i\rvert^2$, the positive Euclidean square. The vector part measures the failure of the two parts to commute after conjugation.

## The Ratio and the Tangent

The ratio of the two parts is the quaternion

$$
\tilde P=\tilde q_r^{-1}\tilde q_i.
$$

It is defined exactly when $\tilde q_r$ is invertible, that is, when $\tilde q_r\neq0$. The element is then

$$
\tilde Q=\tilde q_r(e_t+i\tilde P).
$$

This is the **right multiplication** form of the pairing: the real part acts on the left, and the imaginary part is recovered by right multiplication by the quaternion $\tilde P$. The form is the algebraic origin of the name.

The **quaternion tangent** is the real quaternion $\tilde\Psi$ with

$$
\tan\tilde\Psi=\tilde P.
$$

For a real quaternion, the tangent is defined by the same series as the scalar tangent, or by

$$
\tilde\Psi=\arctan\tilde P
=\frac{1}{2i}\log\frac{e_t+i\tilde P}{e_t-i\tilde P},
$$

on a branch on which the logarithm exists. The angle is real because $\tilde P$ is real.

**Theorem (the pairing).** Let $\tilde Q=\tilde q_r+i\tilde q_i$ with $\tilde q_r\neq0$ and $\langle\tilde Q\rangle_{\natural}\neq0$. Put $\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i$ and $\tilde q=\tilde q_r(\cos\tilde\Psi)^{-1}$. Then

$$
\tilde Q=\tilde q\,\exp(i\tilde\Psi),
$$

with $\tilde q$ and $\tilde\Psi$ real quaternions.

**Proof.** The two trigonometric factors commute because they are functions of the single real quaternion $\tilde\Psi$. Hence

$$
\tilde q\exp(i\tilde\Psi)
=\tilde q_r(\cos\tilde\Psi)^{-1}(\cos\tilde\Psi+i\sin\tilde\Psi)
=\tilde q_r+i\tilde q_r\tan\tilde\Psi
=\tilde q_r+i\tilde q_i.
$$

The inverse of $\cos\tilde\Psi$ exists exactly when the norm does not vanish, which is the hypothesis. $\square$

The theorem is a construction from the parts. The next section shows that its modulus is the polar factor $r\tilde q_{\mathrm r}$.

## The Polar Reading

The polar word gives

$$
\tilde Q=r\exp(i\alpha)B\tilde q_{\mathrm r}
=\bigl(r\tilde q_{\mathrm r}\bigr)\exp(i\tilde\Psi),
$$

with

$$
\tilde\Psi=\alpha-\eta\,\vec u_{\mathrm b}',
\qquad
\vec u_{\mathrm b}'=\tilde q_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde q_{\mathrm r}.
$$

The angle is a real quaternion: its scalar part is the phase $\alpha$, and its pure part is the boost axis rotated by the rotor, of length $\eta$ (the frame rapidity), in the negative of the boost direction. The modulus is the real quaternion $\tilde q=r\tilde q_{\mathrm r}$: the scale times the rotor, which is the polar form of an ordinary quaternion.

The two groupings agree:

$$
\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i,
\qquad
\tilde q=\tilde q_r(\cos\tilde\Psi)^{-1}=r\tilde q_{\mathrm r}.
$$

The identity of the modulus is not a coincidence of two constructions. The real part of $\tilde Q=\tilde q\exp(i\tilde\Psi)$ is

$$
\tilde q_r=\tilde q\,\frac{\exp(i\tilde\Psi)+\exp(-i\tilde\Psi)}{2}
=\tilde q\cos\tilde\Psi,
$$

because $\tilde q$ is real and the coefficient conjugation sends $\exp(i\tilde\Psi)$ to $\exp(-i\tilde\Psi)$. Hence $\tilde q=\tilde q_r(\cos\tilde\Psi)^{-1}$, which is the construction formula. The construction and the polar grouping are the same modulus.

**The two factors in one sentence.** The quaternion pairing carries the whole two-factor word of the quaternion algebra as its first factor, $\tilde q=r\tilde q_{\mathrm r}$, and only the second factor leaves that algebra. The second factor is the exponential of the central imaginary times a real quaternion angle; its scalar part is the central phase and its pure part is the boost.

## The Physical Reading

In the electromagnetic reading, the two real quaternion parts are the electric and magnetic fields,

$$
\tilde Q=\tilde E+i\tilde B,
\qquad
\tilde q_r=\tilde E,
\qquad
\tilde q_i=\tilde B.
$$

The ratio $\tilde P=\tilde E^{-1}\tilde B$ is the **duality quotient** of the field: the quaternion that carries the electric part to the magnetic part. The angle $\tilde\Psi$ is the quaternion angle of the field, with scalar part the duality phase and pure part the boost that the polar word associates with the field. The modulus $\tilde q=\tilde E(\cos\tilde\Psi)^{-1}$ is the normalized electric part, a real quaternion whose scalar is a scale and whose pure part is a rotor.

The reading is a dictionary, not a theorem of electrodynamics. Three points of the dictionary are worth keeping.

- **The scalar part of the angle is the phase.** It is the central $\mathrm{U}(1)$ of the polar word, the gauge phase of the corpus. On a pure Lorentz rotor it is zero; on a general element it is the phase of the determinant.
- **The pure part of the angle is the boost.** Its length is the frame rapidity $\eta$, and its direction is the negative of the boost axis in the rotor frame. The angle is the exponent of the boost factor; the congruence by the factor deposits the rapidity twice.
- **The modulus is the real quaternion polar form.** The scale and the rotor are the two factors of an ordinary quaternion; the pairing separates them from the phase and the boost. In the field reading, the modulus is the part of the field that is a real quaternion, and the angle is the part that is an exponential of the central imaginary.

The reading also explains the domain. The construction needs $\tilde E\neq0$: a purely magnetic field has no electric part to normalize. The factorisation of the polar word still exists on a purely imaginary element, because the polar word does not need the ratio; the construction from the parts fails, but the element has a scale, a phase and a rotor.

## The Domain and the Degenerate Cases

The construction has two conditions, and they are independent.

- **$\tilde q_r\neq0$.** The real quaternion part is invertible. If it vanishes, the ratio $\tilde q_r^{-1}\tilde q_i$ has no meaning.
- **$\langle\tilde Q\rangle_{\natural}\neq0$.** The polar word exists. If the norm vanishes, the modulus $\rho$ is zero and no factor exists.

The factorisation $\tilde Q=\tilde q\exp(i\tilde\Psi)$ exists whenever the norm does not vanish, because it is a regrouping of the polar word. The construction from the parts is the stronger requirement. The distinction matters at the boundary.

**The purely imaginary element.** Take

$$
\tilde Q=i\vec e_x+i\vec e_y=i(\vec e_x+\vec e_y).
$$

Its real part vanishes, so the construction fails. Its norm is $-\lvert\vec e_x+\vec e_y\rvert^2=-2$, so the polar word exists:

$$
\tilde Q=\sqrt{2}\,\exp\Bigl(i\frac{\pi}{2}\Bigr)(\vec e_x+\vec e_y).
$$

The modulus is the real quaternion $\tilde q=\vec e_x+\vec e_y$, the scale is $\sqrt2$, the phase is $\pi/2$, the boost is trivial, and the rotor is the unit real quaternion $(\vec e_x+\vec e_y)/\sqrt2$. The angle is the scalar $\pi/2$. The example shows the factorisation without the construction.

**The real quaternion.** If $\tilde q_i=0$, then $\tan\tilde\Psi=0$, the angle is zero, and $\tilde q=\tilde Q$. The pairing reduces to the polar form of an ordinary quaternion,

$$
\tilde Q=r\tilde q_{\mathrm r},
\qquad
r=\sqrt{\langle\tilde Q\rangle_{\natural}},
\qquad
\tilde q_{\mathrm r}=\tilde Q/r.
$$

The second factor is trivial. This is the case of a real quaternion, and it is the reason the pairing is a genuine extension of the quaternion polar form.

**The null element.** Take $\tilde Q=i e_t+\vec e_x$. Its real part is $\vec e_x\neq0$, but its norm is zero. The polar word fails. The construction does not fail at an inverse of $\cos\tilde\Psi$—that cosine is invertible for every finite angle—but at the equation $\tan\tilde\Psi=-e_x$, which has no finite pure-angle solution because $\lvert\tanh v\rvert<1$. The element is a zero divisor and a lightlike four-vector. The failure is the same failure as in the polar representation, seen through the real part.

## The Conjugations

The three conjugations act on the pairing in three different ways, and the differences are a compact way to see why the real quaternion modulus is not a complex modulus.

**Complex conjugation.** Since $\bar{\cdot}$ fixes $\tilde q_r$ and $\tilde q_i$ and sends $i$ to $-i$,

$$
\overline{\tilde Q}=\tilde q\,\exp(-i\tilde\Psi).
$$

The modulus and the angle are unchanged; only the sign of the exponent changes. The canonical angle of the conjugate is $-\tilde\Psi$.

**Quaternion conjugation.** The conjugation $\natural$ reverses the order of a product and conjugates the factors,

$$
\tilde Q^{\natural}=\exp(i\tilde\Psi^{\natural})\,\tilde q^{\natural}.
$$

This is not the canonical shape, because the modulus is on the left in the pairing. The parts of $\tilde Q^{\natural}$ are $(\tilde q_r^{\natural},\tilde q_i^{\natural})$, so its angle $\tilde\Psi'$ satisfies

$$
\tan\tilde\Psi'=(\tilde q_r^{\natural})^{-1}\tilde q_i^{\natural},
$$

whereas $(\tan\tilde\Psi)^{\natural}=\tilde q_i^{\natural}(\tilde q_r^{\natural})^{-1}$. The two differ by the commutator of the two parts; the pairing is not preserved by $\natural$ in the simple way that the polar word is.

**Hermitian conjugation.** Combining the two,

$$
\tilde Q^{*}=\exp(-i\tilde\Psi^{\natural})\,\tilde q^{\natural},
$$

again with the factors reversed. The Hermitian conjugate is not a pairing with the same modulus unless the two parts commute.

The asymmetry is the price of putting the modulus on the left. The polar word is symmetric under $\natural$ up to order; the quaternion pairing is not, because the two real quaternion factors need not commute.

## A Worked Example

Take the reference element

$$
\tilde Q=(1+i)e_t+\vec e_x+2\vec e_y.
$$

The two real quaternion parts are

$$
\tilde q_r=e_t+\vec e_x+2\vec e_y,
\qquad
\tilde q_i=e_t.
$$

The ratio is

$$
\tilde P=\tilde q_r^{-1}\tilde q_i
=\frac{1}{6}\bigl(e_t-\vec e_x-2\vec e_y\bigr),
$$

since $\tilde q_r^{-1}=(e_t-\vec e_x-2\vec e_y)/6$. The norm is $N=5+2i$, so the polar word has

$$
r=2.320595787,
\qquad
\alpha=0.190253189,
\qquad
\eta=0.378136610,
$$

and the rotor is

$$
\tilde q_{\mathrm r}=0.470592172\,e_t+0.394599292\,\vec e_x+0.789198585\,\vec e_y.
$$

The angle is

$$
\tilde\Psi=\alpha-\eta\,\vec u_{\mathrm b}'
=0.190253189-0.169108000\,\vec e_x-0.338216000\,\vec e_y,
$$

with $\vec u_{\mathrm b}'=(0.447213595,0.894427191,0)$. The modulus of the pairing is the real quaternion

$$
\tilde q=r\tilde q_{\mathrm r}
=1.092054213\,e_t+0.915705455\,\vec e_x+1.831410910\,\vec e_y.
$$

The construction gives the same modulus:

$$
\cos\tilde\Psi=1.053000547+0.032747142\,\vec e_x+0.065494284\,\vec e_y,
$$

$$
\tilde q_r(\cos\tilde\Psi)^{-1}=1.092054213\,e_t+0.915705455\,\vec e_x+1.831410910\,\vec e_y.
$$

The equality holds to $1.1\times10^{-9}$ with the displayed rounded coefficients, and to $6.7\times10^{-16}$ in double precision from the unrounded data. The example has $\tilde q_r\neq0$ and $N\neq0$, so both the construction and the factorisation are available. The angle has a scalar part (the phase) and a pure part (the boost in the rotor frame); the modulus has a scalar part (the scale) and a pure part (the rotor).

**A pure boost.** Take $\tilde Q=B=\cosh\eta e_t-i\sinh\eta\vec u_{\mathrm b}$ with $\eta=0.693147181$. Then $\tilde Q$ is real in the split $\tilde q_r=\cosh\eta e_t$, $\tilde q_i=-\sinh\eta\vec u_{\mathrm b}$, and the angle is $\tilde\Psi=-\eta\vec u_{\mathrm b}$. The modulus is $\tilde q=e_t$, and $\exp(i\tilde\Psi)=B$. The pure boost is a pure angle, and its pure part has length $\eta$: the frame rapidity.

## The Quaternion Pairing and the Other Pairings

The quaternion pairing and the Hamilton pairing are the two partial constructions of the polar word. They read different parts of the element.

- **The quaternion pairing** reads the real and imaginary quaternion parts, $\tilde q_r$ and $\tilde q_i$, and constructs the modulus and the angle from their ratio. It needs $\tilde q_r\neq0$.
- **The Hamilton pairing** reads the scalar and vector parts, $Q_t$ and $\vec Q$, and constructs the modulus and the complex axis-angle from their ratio. It needs $\vec Q\cdot\vec Q\neq0$.

The two domains are different. The element $e_t+\vec e_x+i\vec e_y$ has a real part and a quaternion construction but no Hamilton root; the element $i(\vec e_x+\vec e_y)$ has a Hamilton root but no quaternion construction. The polar word exists on both, because it needs only the norm.

The **Cartan pairing** reads the Hermitian and unitary factors, $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}=rB$ and $\tilde U=\tilde H^{-1}\tilde Q=e^{i\alpha}\tilde q_{\mathrm r}$. It is the matrix polar decomposition and needs only the norm. The three pairings are three readings of one word: the quaternion pairing separates scale and rotor from phase and boost; the Hamilton pairing separates the modulus from the complex axis-angle; the Cartan pairing separates the positive Hermitian factor from the unitary factor.

## Summary

The quaternion pairing writes a biquaternion as $\tilde q\exp(i\tilde\Psi)$, with $\tilde q=r\tilde q_{\mathrm r}$ the real quaternion modulus and $\tilde\Psi=\alpha-\eta\vec u_{\mathrm b}'$ the real quaternion angle. The construction from the two real quaternion parts is $\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i$ and $\tilde q=\tilde q_r(\cos\tilde\Psi)^{-1}$, valid when $\tilde q_r$ is invertible and the norm does not vanish. The factorisation exists on the whole complement of the null cone; the construction needs the real part. The pairing carries the quaternion polar form as its first factor and the central phase and the boost as its second.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=\tilde q_r+i\tilde q_i$ | the split into real quaternion parts |
| $\tilde q_r,\tilde q_i$ | the real and imaginary quaternion parts |
| $\tilde P=\tilde q_r^{-1}\tilde q_i$ | the ratio, the tangent of the angle |
| $\tilde\Psi=\alpha-\eta\vec u_{\mathrm b}'$ | the real quaternion angle |
| $\tilde q=r\tilde q_{\mathrm r}$ | the real quaternion modulus |
| $\vec u_{\mathrm b}'=\tilde q_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde q_{\mathrm r}$ | the boost axis in the rotor frame |
| $r,\alpha,\eta,\tilde q_{\mathrm r}$ | the scale, phase, frame rapidity and rotor of the polar word |
| $B$ | the positive Hermitian boost factor |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_physics/the-polar-element-representation-of-biquaternions.md`), the polar word and its four factors.
- *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`), the mathematics reference.
- *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`), the axis-angle reading.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), the positive-unitary reading.
- *The Polar Decomposition of Biquaternions in Practice* (`articles_physics/the-polar-decomposition-of-biquaternions-in-practice.md`), the algorithm.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), the two-factor word of the real quaternions.
