# __The Quaternion Pairing of the Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

The quaternion pairing regroups the four polar factors into a real quaternion modulus and the exponential of a real quaternion angle,

$$
\tilde Q=\tilde q\exp(i\tilde\Psi),
\qquad
\tilde q=r\tilde u_{\mathrm r},
\qquad
\tilde\Psi=\alpha+\frac{\psi}{2}\vec u_{\mathrm b}',
\qquad
\vec u_{\mathrm b}'=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}.
$$

On the N-regular, spectrally degenerate sector $\Sigma_{10}$ the pairing inherits one extra condition. The axes of the word are orthogonal, $\vec u_{\mathrm b}\perp\vec u_{\mathrm r}$, so the conjugated axis is orthogonal to the rotor,

$$
\vec u_{\mathrm b}'\perp\vec u_{\mathrm r}.
$$

The modulus $\tilde q=r\tilde u_{\mathrm r}$ and the vector part of $\tilde\Psi$ are therefore orthogonal. This orthogonality is the signature of the sector inside the pairing. It does not make the pairing new; it restricts the general pairing of *The Quaternion Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion* to the wall.

## The Pairing

**Theorem (the quaternion pairing on $\Sigma_{10}$).** Let $\tilde Q\in\Sigma_{10}$ and write the polar word as above. Then

$$
\tilde Q=\tilde q\exp(i\tilde\Psi),
\qquad
\tilde q=r\tilde u_{\mathrm r},
\qquad
\tilde\Psi=\alpha+\frac{\psi}{2}\vec u_{\mathrm b}',
$$

with $\tilde q$ a real quaternion of norm $r$ and $\tilde\Psi$ a real quaternion. The vector part of $\tilde\Psi$ is orthogonal to $\tilde q$.

*Proof.* The factorisation is the regrouping of the four factors of the word, which exists on the sector. The orthogonality is the orthogonality of the axes, transported by the rotor conjugation. $\square$

The pairing is a regrouping, not a new decomposition: the factors $\tilde q$ and $\exp(i\tilde\Psi)$ are the scale-times-rotor and the phase-times-boost of the unique word. Uniqueness is inherited from the word.

### The Construction From the Parts

Write $\tilde Q=\tilde q_r+i\tilde q_i$ with $\tilde q_r,\tilde q_i\in\mathbb{H}$ the real and imaginary quaternion parts. Where $\tilde q_r$ is invertible,

$$
\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i,
\qquad
\tilde q=\tilde q_r(\cos\tilde\Psi)^{-1}.
$$

The construction is partial. The factorisation exists on all of $\Sigma_{10}$; the construction needs $\tilde q_r\neq0$ as well. On the scalar line $\tilde Q=Q_te_t$ the real part is $\operatorname{Re}(Q_t)e_t$, so the construction fails exactly on the pure imaginary scalars, where the factorisation still exists with $\tilde q=|Q_t|e_t$ and $\tilde\Psi=\pm\pi/2$.

## The Degenerate Signature

The word of the sector is rigid:

$$
\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\varepsilon,
\qquad
\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0.
$$

On the Jordan part the second equation gives $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$, and the first gives $|\cos\frac{\theta}{2}|=1/\cosh\frac{\psi}{2}$ with $\varepsilon=\operatorname{sgn}\cos\frac{\theta}{2}$. The pairing reads these relations on its two factors:

| Pairing datum | Word datum | Sector condition |
|---|---|---|
| $\tilde q=r\tilde u_{\mathrm r}$ | $r,\theta,\vec u_{\mathrm r}$ | $\lvert\tilde q\rvert=r>0$ |
| $\operatorname{Sc}\tilde\Psi=\alpha$ | $\alpha$ | none beyond the branch |
| $\operatorname{Vect}\tilde\Psi=\frac{\psi}{2}\vec u_{\mathrm b}'$ | $\psi,\vec u_{\mathrm b}$ | $\vec u_{\mathrm b}'\perp\vec u_{\mathrm r}$ |
| $\cos\tilde\Psi=\cos\alpha\cosh\frac{\psi}{2}-\sin\alpha\sinh\frac{\psi}{2}\vec u_{\mathrm b}'$ | the phase and the boost | $\operatorname{Sc}\cos\tilde\Psi=\cos\alpha\cosh\frac{\psi}{2}$ |

The last row separates the phase from the boost. The rigidity is not read from $\cos\tilde\Psi$ alone; it relates the boost angle to the scalar part of the rotor,

$$
\cosh\frac{\psi}{2}\,\operatorname{Sc}\tilde u_{\mathrm r}=\varepsilon.
$$

This is the same wall as $\operatorname{Sc}\tilde U=\pm1$, read in the pairing: $\operatorname{Sc}\tilde u_{\mathrm r}=\cos\frac{\theta}{2}$.

## Worked Example

Take

$$
\tilde Q=e_t+\vec e_x+i\vec e_y.
$$

The polar data are $r=1$, $\alpha=0$, $\psi=2\operatorname{arcosh}\sqrt2$, $\theta=\frac{\pi}{2}$,

$$
\vec u_{\mathrm b}=\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\vec u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The quaternion modulus is

$$
\tilde q=r\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The conjugated axis is

$$
\vec u_{\mathrm b}'=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}
=\frac{\vec e_y-\vec e_z}{\sqrt2},
$$

and the exponent is

$$
\tilde\Psi=\frac{\psi}{2}\frac{\vec e_y-\vec e_z}{\sqrt2}
=\beta\vec u,
\qquad
\beta=\operatorname{arcosh}\sqrt2,
\qquad
\vec u=\frac{\vec e_y-\vec e_z}{\sqrt2}.
$$

Then

$$
\exp(i\tilde\Psi)=\cosh\beta+i\sinh\beta\,\vec u
=\sqrt2+\frac{i}{\sqrt2}(\vec e_y-\vec e_z),
$$

and

$$
\tilde q\exp(i\tilde\Psi)
=\frac{e_t+\vec e_x}{\sqrt2}\left(\sqrt2+\frac{i}{\sqrt2}(\vec e_y-\vec e_z)\right)
=e_t+\vec e_x+i\vec e_y.
$$

The real and imaginary quaternion parts are $\tilde q_r=e_t+\vec e_x$ and $\tilde q_i=\vec e_y$, and

$$
\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i
=\frac12(\vec e_y-\vec e_z)
=\tanh\beta\,\vec u,
$$

as the construction requires. The modulus and the vector part of the exponent are orthogonal, $\tilde q\perp\operatorname{Vect}\tilde\Psi$. The scalar part of $\cos\tilde\Psi$ is $\cosh\beta=\sqrt2$, and the rotor has $\operatorname{Sc}\tilde u_{\mathrm r}=\cos\frac{\theta}{2}=1/\sqrt2$; their product is the rigidity value $\varepsilon=1$.

## Comparison with the Regular Sector

| Property | Regular sector | Degenerate sector |
|---|---|---|
| axes | not orthogonal in general | orthogonal on the Jordan part |
| modulus and exponent | no orthogonality in general | $\tilde q\perp\operatorname{Vect}\tilde\Psi$ |
| scalar part of $\cos\tilde\Psi$ | $\cos\alpha\cosh\frac{\psi}{2}$, arbitrary | $\cos\alpha\cosh\frac{\psi}{2}$; the rigidity uses $\operatorname{Sc}\tilde u_{\mathrm r}$ |
| construction domain | $\tilde q_r\neq0$, plus $N\neq0$ | $\tilde q_r\neq0$, plus $N\neq0$ |
| factorisation | all of $\Sigma_{11}$ | all of $\Sigma_{10}$ |

The pairing is therefore the same regrouping on both sides of the wall. The wall is visible in the orthogonality of the two data and in the real scalar part of $\cos\tilde\Psi$.

## Summary

### Main Results

| Item | Value |
|---|---|
| equation | $\tilde Q=\tilde q\exp(i\tilde\Psi)$ |
| modulus | $\tilde q=r\tilde u_{\mathrm r}$, a real quaternion of norm $r$ |
| exponent | $\tilde\Psi=\alpha+\frac{\psi}{2}\vec u_{\mathrm b}'$, a real quaternion |
| sector signature | $\vec u_{\mathrm b}'\perp\vec u_{\mathrm r}$, hence $\tilde q\perp\operatorname{Vect}\tilde\Psi$ |
| rigidity | $\cosh\frac{\psi}{2}\operatorname{Sc}\tilde u_{\mathrm r}=\varepsilon=\pm1$ on the Jordan part |
| construction | $\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i$, $\tilde q=\tilde q_r(\cos\tilde\Psi)^{-1}$ |
| domain | factorisation on $\Sigma_{10}$; construction where $\tilde q_r\neq0$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product |
| $B^2=\langle\vec Q,\vec Q\rangle_{\natural}$ | the vector form |
| $\Sigma_{10}$ | the N-regular, spectrally degenerate sector |
| $\Rho=r e^{i\alpha}$ | the modulus |
| $\tilde U=\varepsilon(e_t+\vec\Upsilon)$ | the unit factor |
| $\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the positive factor and the rotor |
| $\psi,\theta$ | the rapidity and the rotor angle |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the orthogonal axes of the Jordan part |
| $\vec u_{\mathrm b}'=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ | the conjugated boost axis |
| $\tilde q=r\tilde u_{\mathrm r}$ | the quaternion modulus |
| $\tilde\Psi$ | the quaternion angle |
| $\tilde q_r,\tilde q_i$ | the real and imaginary quaternion parts of $\tilde Q$ |

## Further Reading

- [The Quaternion Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](the-quaternion-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the unrestricted pairing.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the word and the rigidity.
- [The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the other pairing that survives the wall.
