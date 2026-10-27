# __The One-Sided Operator Exponential of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

This article is the analytic companion of *The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion*. On the sector the element is $Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^{2}=0$, so the one-sided operator is $Q_t(I+L_{\vec\Upsilon})$ with $L_{\vec\Upsilon}^{2}=0$. Its exponential therefore truncates at degree one: the one-parameter group is a line of shears, not a circle of rotations.

The algebra of the operator — the two Jordan blocks, the determinant and the trace, the polar word, the image and the kernel — is in the companion. This article reads the exponent: the exact logarithm of the element, the operator exponential, and the constraints that the wall imposes on the rapidity and the angle. The two polar factors survive at the wall, but their exponents are locked to the single null parameter $a$.

## The Exponential at the Wall

**One null exponent.** On the sector the element is a scalar times a unipotent element, so its exponential is polynomial. Since $\vec\Upsilon^2=0$,

$$
\boxed{\;\tilde Q=Q_t\bigl(e_t+\vec\Upsilon\bigr)=r e^{i\alpha}\varepsilon\,e^{\vec\Upsilon},\qquad
e^{\vec\Upsilon}=e_t+\vec\Upsilon,\qquad
\varepsilon=\frac{Q_t}{\Rho}=\pm1.\;}
$$

Write $\vec\Upsilon=\vec A+i\vec B$ with $\vec A$ and $\vec B$ real; then $\vec A\cdot\vec B=0$ and $\lvert\vec A\rvert=\lvert\vec B\rvert=a$. The regular word carries two independent exponents, $i\frac{\psi}{2}\vec u_{\mathrm b}$ and $\frac{\theta}{2}\vec u_{\mathrm r}$, about two independent axes. At the wall both factors remain, but their exponents do not add. The formal exponent $i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ is not the logarithm: its difference from the true exponent $\vec\Upsilon$ is the log defect of *Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion*, §*The Formal Exponent and the Defect*, whose cross term $i\varepsilon\tanh\frac{\psi}{2}\tan\frac{\theta}{2}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ is non-zero because the axes are orthogonal. The exact exponent is $\vec\Upsilon$ itself. What the wall leaves is a pair of constraints between the two factors:

$$
\boxed{\;\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0,\qquad
\varepsilon\tan\frac{\theta}{2}=\sinh\frac{\psi}{2}=a.\;}
$$

*Proof.* From the coordinate boxes of *Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion*, $\cosh\frac{\psi}{2}=\sqrt{1+a^2}$, $\sinh\frac{\psi}{2}=a$, $\lvert\cos\frac{\theta}{2}\rvert=1/\sqrt{1+a^2}$ and $\sin\frac{\theta}{2}=a/\sqrt{1+a^2}$. Hence $\varepsilon\tan\frac{\theta}{2}=a=\sinh\frac{\psi}{2}$. The axes are $\vec u_{\mathrm b}\propto\vec B+\vec A\times\vec B$ and $\vec u_{\mathrm r}=\varepsilon\vec A/a$. The vectors $\vec B$ and $\vec A\times\vec B$ are both orthogonal to $\vec A$, because $\vec A\cdot\vec B=0$, so $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$.

The wall therefore removes neither factor. It removes two real degrees of freedom: the rapidity and the angle are locked to the single parameter $a$, and the two axes are forced orthogonal. The product of the two factors is the unipotent $\tilde U$, up to the sign $\varepsilon$.

**The operator exponential.** Left multiplication is a representation, $L_{\tilde X}L_{\tilde Y}=L_{\tilde X\tilde Y}$, hence $L_{\exp\tilde X}=\exp L_{\tilde X}$. Since $L_{\vec\Upsilon}^2=L_{\vec\Upsilon^2}=0$,

$$
\boxed{\;\exp\bigl(tL_{\tilde Q}\bigr)
=\exp\bigl(tQ_t(I+L_{\vec\Upsilon})\bigr)
=e^{tQ_t}\bigl(I+tQ_tL_{\vec\Upsilon}\bigr)\;}
$$

for every complex $t$. In particular $\exp L_{\tilde Q}=e^{Q_t}(I+Q_tL_{\vec\Upsilon})$.

*Proof.* $L_{\tilde Q}=Q_tL_{e_t+\vec\Upsilon}=Q_t(I+L_{\vec\Upsilon})$ and $L_{\vec\Upsilon}^2=0$. The two terms of the exponent commute, because both are polynomials in $L_{\vec\Upsilon}$, so the exponential is $e^{tQ_t}\exp(tQ_tL_{\vec\Upsilon})$, and the second factor is $I+tQ_tL_{\vec\Upsilon}$.

**Interpretation.** The one-parameter group is a line of shears, not a circle of rotations. The exponential moves the identity along the nilpotent direction and stops at degree one; it has no period and carries no angle. The polar angles are in the factors: $L_{\tilde U_{\mathrm b}}$ has the eigenvalues $e^{\pm\psi/2}$, each twice, and $L_{\tilde u_{\mathrm r}}$ has $e^{\pm i\theta/2}$, each twice. Their product has the single eigenvalue $Q_t$, with two Jordan blocks of size two, and its spectrum carries no angle at all. In the regular sector the eigenvalues of $L_{\tilde Q}$ are $\Rho\mu_\pm$ with $\mu_\pm=U_t\pm i\sqrt{1-U_t^2}$ and $U_t=\operatorname{Sc}\tilde U$; at the wall $U_t\to\varepsilon$ and both eigenvalues tend to $\Rho\varepsilon=Q_t$. The only trace of the two angles is the single parameter $a$ that measures the nilpotent part.

At the wall the spinor exponent is $\vec\Upsilon$ itself, carried by the left slot. The vector exponent of the sandwich is $\vec\Upsilon$ in the left slot plus $\vec\Upsilon^{*}$ in the right. That is the wall form of the doubling: the spinor reading has one slot, the vector reading has two, and the scalar part appears once per slot. This is why the modulus is $Q_t$ in the one-sided reading and $\lvert Q_t\rvert^2$ in the two-sided one, and not a doubled exponent.

## Worked Example

The companion gives the operator and its nilpotent part in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$. Its exponential is the shear

$$
\exp\bigl(tL_{\tilde Q}\bigr)=e^{t}\bigl(I+t\,\mathsf M(L_{\vec\Upsilon})\bigr)
=e^{t}
\begin{pmatrix}
1&-t&-it&0\\
t&1&0&it\\
it&0&1&-t\\
0&-it&t&1
\end{pmatrix},
$$

which is the identity plus $t$ times the nilpotent matrix above, multiplied by $e^{t}$. At $t=1$ it is $e$ times the unipotent matrix of the operator, as the box requires.

The example displays the general form: $\exp(tL_{\tilde Q})=e^{tQ_t}(I+tQ_tL_{\vec\Upsilon})$ with $Q_t=1$ and $\mathsf M(L_{\vec\Upsilon})$ the nilpotent matrix above.

## Summary

The element is a scalar times a unipotent element, so its exponential is polynomial:

$$
\tilde Q=Q_t(e_t+\vec\Upsilon)=r e^{i\alpha}\varepsilon\,e^{\vec\Upsilon},
\qquad
e^{\vec\Upsilon}=e_t+\vec\Upsilon,
\qquad \varepsilon=\frac{Q_t}{\Rho}=\pm1 .
$$

The one-sided operator exponential is a shear,

$$
\exp\bigl(tL_{\tilde Q}\bigr)=e^{tQ_t}\bigl(I+tQ_tL_{\vec\Upsilon}\bigr),
$$

with no period and no angle. Its eigenvalues are $e^{tQ_t}$, each with a Jordan block of size two; the spectrum of the product $L_{\tilde Q}$ itself is $Q_t$ alone, with two Jordan blocks of size two.

The two polar factors survive at the wall, with the eigenvalues $e^{\pm\psi/2}$ and $e^{\pm i\theta/2}$, each twice, but their parameters are not free: the axes are orthogonal and

$$
\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0,
\qquad
\varepsilon\tan\frac{\theta}{2}=\sinh\frac{\psi}{2}=a .
$$

The two angles leave a single trace in the spectrum, the null parameter $a$. The spinor exponent is $\vec\Upsilon$ itself, carried by one slot; the vector exponent is $\vec\Upsilon$ in the left slot plus $\vec\Upsilon^{*}$ in the right, which is the wall form of the doubling.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=Q_t(e_t+\vec\Upsilon)$ | the normal form on $\Sigma_{10}$ |
| $\vec\Upsilon=\vec A+i\vec B$ | the null vector, with $\vec A\cdot\vec B=0$ and $\lvert\vec A\rvert=\lvert\vec B\rvert=a$ |
| $L_{\tilde Q},R_{\tilde Q}$ | the left and right multiplications |
| $L_{\vec\Upsilon}$ | the left multiplication by the null vector, $L_{\vec\Upsilon}^{2}=0$ |
| $\Rho=r e^{i\alpha}$ | the complex modulus |
| $\varepsilon=Q_t/\Rho=\pm1$ | the sign of the scalar part |
| $\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the positive factor and the rotor |
| $\psi,\theta$ | the rapidity and the rotor angle |
| $a$ | the null parameter |

## Further Reading

- [The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion](one-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the algebraic companion: the Jordan structure, the polar word and the image.
- [The Two-Sided Operator Exponential of a N-Regular, Spectrally Degenerate Biquaternion](the-two-sided-operator-exponential-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the null rotation generated by the sandwich.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the element word, the exact logarithm and the log defect.
- [Operators of the Polar Word: The Common Framework](operators-of-the-polar-word-the-common-framework.html), for the three operators and the sector table.
