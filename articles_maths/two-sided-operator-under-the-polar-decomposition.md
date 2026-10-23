# __Two-Sided Operator Under the Polar Decomposition__

## Introduction

The **Hermitian sandwich** of the biquaternion algebra is the operator

$$
\Theta_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\qquad \Theta_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*},
$$

the two-sided operator whose right factor is the Hermitian conjugate of its left factor. It is the operator that carries the Lorentz group on the algebra: on the norm-one slice it acts on the anti-Hermitian and Hermitian subspaces by the proper orthochronous Lorentz group, and on the full group of units it is that action composed with a dilation.

The polar decomposition writes an element of non-vanishing norm as four factors,

$$
\tilde Q=\Rho\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r\exp(i\alpha)\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr),
\qquad \Rho=r\exp(i\alpha),
$$

the four being the scale $r>0$, the central phase $\exp(i\alpha)$ collected in $\Rho$, the Hermitian positive boost $\tilde U_{\mathrm b}$ of rapidity $\psi\ge0$ about the real unit axis $\vec u_{\mathrm b}$, and the rotor $\tilde u_{\mathrm r}$ of angle $\theta\in[0,2\pi]$ about the real unit axis $\vec u_{\mathrm r}$. This article reads the sandwich one factor at a time and answers one question: **what does each factor do to the operator, and what becomes of its exponent?** The answer is a table with one row per factor, and the row that matters is the second. The phase does nothing.

The article is the vector-side companion of *The Twisted Spinor Operator Representation of Biquaternions*. There the same word acts by left multiplication on the spinor module and all four factors are visible: the scale and the phase form the twist $\chi(\Rho)=\Rho$, and the boost and the rotor form the norm-one operator. Here the action is the sandwich on the algebra, the phase is invisible, and the boost and the rotor are the only factors that act on a vector by a Lorentz transformation. The one-sided companion is *One-Sided Operator Under the Polar Decomposition*: there the same word is read through a single left or right multiplication, the phase is visible, and the two real forms $\mathbb{M}_\pm$ are exchanged at $\alpha=\tfrac{\pi}{2}$.

The plan is the following. §*The Sandwich of the Word* proves the multiplicativity and the closed form $\Theta_{\tilde Q}=r^{2}\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}}$. §*The Scale* to §*The Rotor* take the four factors in the order of the word. §*The Angle Bookkeeping* collects the exponents and states the doubling rule. §*The Image and the Kernel* identifies the image as the conformal Lorentz group and the kernel as the central unit circle. §*The Null Cone* records the degenerate case. The article closes with the summary, the notation and the readings.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The scalar imaginary is $i$, central, $i^{2}=-1$. An element is $\tilde Q=Q_te_t+\vec Q$ with the four coefficients $Q_\mu$ complex.

The three conjugations are the quaternion conjugation $\natural$, the coefficient conjugation $\bar\cdot$ and their composite, the **Hermitian conjugation**

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z .
$$

The Hermitian and anti-Hermitian subspaces are

$$
\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}.
$$

On $\mathbb{M}_-$ an element is $\tilde Q_-=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b$ a real vector; on $\mathbb{M}_+$ an element is $\tilde Q_+=a\,e_t+i\vec b$ with the same real data. The two sectors are exchanged by multiplication by $i$, which is central.

The **norm** of the polar series is the complex number

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},\qquad \tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\,e_t ,
$$

and the **domain** of the polar word is $\langle\tilde Q\rangle_{\natural}\neq0$. The word is

$$
\tilde Q=\Rho\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},\qquad
\Rho=r\exp(i\alpha),\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr),\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit vectors. The modulus is $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ on the principal branch, so $r=\lvert\Rho\rvert$ and $\alpha=\tfrac12\arg \langle\tilde Q\rangle_{\natural}$. The factors satisfy

$$
\Rho^{*}=\bar\Rho,\qquad \tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},\qquad \tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1},\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=\langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, the $\sigma_k$ being the Pauli matrices. It is $\mathbb{C}$-linear and satisfies $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, and its determinant is the norm, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

The sandwich is written $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ throughout. It uses the Hermitian conjugate in the right slot and never the inverse; the two coincide only where $\tilde Q$ is unitary.

## The Sandwich of the Word

### Elementary Properties

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$ and $\tilde X\in\mathbb{B}$. Then:

**(a)** $\Theta_{\tilde Q\tilde Q'}=\Theta_{\tilde Q}\circ\Theta_{\tilde Q'}$;

**(b)** $\Theta_{\tilde Q}$ is $\mathbb{C}$-linear in $\tilde X$;

**(c)** $\Theta_{\tilde Q}$ is invertible if and only if $\tilde Q$ is invertible, and then $\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}$;

**(d)** $\Theta_{\tilde Q}$ preserves each of $\mathbb{M}_+$ and $\mathbb{M}_-$;

**(e)** $\Theta_{\tilde Q}(e_t)=\tilde Q\tilde Q^{*}$.

*Proof.* (a) $(\tilde Q\tilde Q')\tilde X(\tilde Q\tilde Q')^{*}=\tilde Q(\tilde Q'\tilde X\tilde Q'^{*})\tilde Q^{*}$. (b) The multiplication and the right factor are $\mathbb{C}$-linear. (c) The inverse of $\Theta_{\tilde Q}$ is $\Theta_{\tilde Q^{-1}}$, because $\tilde Q^{-1}\tilde Q\tilde X\tilde Q^{*}\tilde Q^{-*}=\tilde X$ and $(\tilde Q^{-1})^{*}=(\tilde Q^{*})^{-1}$. (d) If $\tilde X^{*}=\pm\tilde X$, then

$$
\bigl(\tilde Q\tilde X\tilde Q^{*}\bigr)^{*}=\tilde Q\tilde X^{*}\tilde Q^{*}=\pm\tilde Q\tilde X\tilde Q^{*}.
$$

(e) Put $\tilde X=e_t$.

The preservation of the two sectors is the structural reason the action splits into two formulas, one per sector, and the reason a sandwich cannot mix the Hermitian and the anti-Hermitian parts.

### The Closed Form

**Theorem (the sandwich of the polar word).** Let $\tilde Q=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\langle\tilde Q\rangle_{\natural}\neq0$. Then

$$ \boxed{\;\Theta_{\tilde Q}=\Theta_r\circ\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}}\;}, $$

that is,

$$
\boxed{\;\Theta_{\tilde Q}(\tilde X)=r^{2}\,\tilde U_{\mathrm b}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\bigr)\tilde U_{\mathrm b}\;},
$$

and $\Theta_{\exp(i\alpha)}=\mathrm{id}$.

*Proof.* The Hermitian conjugate of the word is

$$
\tilde Q^{*}=\bigl(\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)^{*}
=\tilde u_{\mathrm r}^{*}\tilde U_{\mathrm b}^{*}\Rho^{*}
=\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\bar\Rho
=\bar\Rho\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b},
$$

because the scalars are central. Hence

$$
\tilde Q\tilde X\tilde Q^{*}
=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\bar\Rho
=\Rho\bar\Rho\,\tilde U_{\mathrm b}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\bigr)\tilde U_{\mathrm b},
$$

and $\Rho\bar\Rho=r^{2}$. The phase has disappeared in the last step.

**Remark (the order).** The rightmost factor of the word acts first: the rotor, then the boost, then the scale. The phase may be inserted anywhere, and so may the scale, because both are central. The boost and the rotor do not commute, so their order is part of the word and cannot be exchanged.

The theorem is the article in one line. The four sections that follow read its four factors.

## The Scale

### The Factor

The scale is $r=\exp(\ln r)$, a positive real. It is central, real and Hermitian, $r^{*}=r$, and it is the only factor whose exponent is a real scalar.

### The Sandwich

$$
\Theta_r(\tilde X)=r\tilde Xr^{*}=r^{2}\tilde X .
$$

On $\mathbb{M}_-$ and on $\mathbb{M}_+$ alike, every coordinate is multiplied by $r^{2}$: $a\mapsto r^{2}a$ and $\vec b\mapsto r^{2}\vec b$. The scale is a dilation of ratio $r^{2}$ of the whole algebra, and the only factor that changes the norm of the argument,

$$
\langle\Theta_r(\tilde X)\rangle_{\natural}=r^{4}\langle \tilde X\rangle_{\natural}.
$$

### The Exponent

The exponent is $\ln r$, and the sandwich sends it to

$$
\boxed{\;\ln r\longmapsto 2\ln r\;}.
$$

There is no angle. The factor two is nevertheless the same factor two as in the boost and the rotor: the exponent of the factor is half the exponent of its image. The scale is the case in which the doubled parameter is a dilation and not a rotation or a rapidity. The map $r\mapsto r^{2}$ is an isomorphism of $\mathbb{R}_{>0}$, so the scale is recovered from its sandwich; only the sign of the factor is lost, and the polar word has $r>0$.

## The Central Phase

### The Factor

The phase is $P=\exp(i\alpha)$, central and unitary,

$$
P^{*}=P^{-1}=\exp(-i\alpha),\qquad N(P)=\exp(2i\alpha).
$$

Its exponent is $i\alpha$, purely imaginary and central.

### The Sandwich

$$
\Theta_P(\tilde X)=\exp(i\alpha)\,\tilde X\,\exp(-i\alpha)=\tilde X .
$$

The two scalars commute with $\tilde X$ and with each other, and the second is the inverse of the first, so the product is the identity operator.

**The phase is not a half-angle of the sandwich.** The exponent $i\alpha$ is the full generator of the multiplication by $\exp(i\alpha)$ on the module; the sandwich cancels it. It is already half of the argument of the norm, $N=\Rho^{2}=r^{2}\exp(2i\alpha)$, and that is the only doubling in which it takes part. Writing $\exp(i\alpha/2)$ in the word would not change the sandwich, which is the identity either way; it would only change the meaning of the letter $\alpha$, and it would break $\Rho=\sqrt N$ unless $\alpha$ were redefined as $\arg N$.

### Remark (the Cancelled Phase)

This is the central remark of the article. The phase is the only factor of the word whose sandwich is the identity whatever the value of its parameter. It is not halved, not doubled and not shifted: it is annihilated. Six consequences follow.

**First, the cancellation is exact and global.** It holds for every $\tilde X$, not merely on one subspace, and it uses only two properties, centrality and unitarity. Any central factor of modulus one cancels in any sandwich: if $C$ is central and $C^{*}=C^{-1}$, then

$$
C\tilde XC^{*}=\tilde XCC^{-1}=\tilde X .
$$

**Second, two elements that differ by a phase have the same sandwich.** For a central complex $\lambda$,

$$
\Theta_{\lambda\tilde Q}(\tilde X)=\lambda\tilde Q\tilde X\tilde Q^{*}\bar\lambda=|\lambda|^{2}\,\Theta_{\tilde Q}(\tilde X).
$$

On the unit circle $|\lambda|=1$ the two sandwiches are equal, so the whole $U(1)$-orbit of $\tilde Q$ has one sandwich. On the positive real axis the sandwich scales by $\lambda^{2}$, which is the scale row of the table. The phase is the unit-modulus part of the centre, and it is exactly the part that disappears.

**Third, the phase is absent from this action but not from the algebra.** It reappears in three places, and the list is the reason the polar word needs it:

- the norm, $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\Rho^{2}=r^{2}\exp(2i\alpha)$;
- the determinant, $\det\mathsf M_2(\tilde Q)=\Rho^{2}=r^{2}\exp(2i\alpha)$;
- the module, where left multiplication by $\tilde Q$ acts on the spinor module by the scalar $\Rho=r\exp(i\alpha)$, the twist $\chi(\Rho)=\Rho$ of *The Twisted Spinor Operator Representation of Biquaternions*.

The first two are quadratic in $\Rho$ and see $2\alpha$; the third is linear and sees $\alpha$; the sandwich multiplies by $\Rho$ on the left and by $\bar\Rho$ on the right and sees $0$.

**Fourth, the spectral reading confirms it.** In *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* the eigenvalues of $\Theta_{\tilde Q}$ are the products $\lambda_i\bar\lambda_j$ of the eigenvalues of $\mathsf M_2(\tilde Q)$. A phase multiplies every $\lambda_i$ by $\exp(i\alpha)$ and every $\bar\lambda_j$ by $\exp(-i\alpha)$, so every product is unchanged. The cancellation is visible in the spectrum without any computation in coordinates.

**Fifth, the factor $\exp(2i\alpha)$ of the norm is not a doubling by the sandwich.** It is the square of the factor in the product $\tilde Q\tilde Q^{\natural}$: the product has two factors and both carry $\exp(i\alpha)$. The doubling of the boost and the rotor is a different phenomenon, computed in the next two sections. The two must not be conflated: the norm doubles the phase because the product has two factors, while the sandwich doubles the boost because its two slots carry the same exponent, and doubles the rotor because the conjugation is the double cover.

**Sixth, the phase row of the table is zero.** A table that halves every exponent would put $\alpha/2$ in the phase row and would be wrong by the whole phase; a table that repeats the exponent would put $\alpha$ there and would be wrong by the sign of the right factor. The only correct entry is $0$.

## The Boost

### The Factor

The boost is

$$
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\tfrac{\psi}{2}\,e_t+i\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b},
\qquad \psi\ge0,\qquad \lvert\vec u_{\mathrm b}\rvert=1 .
$$

It is Hermitian and of norm one,

$$
\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=1,
$$

and its square and inverse are

$$
\tilde U_{\mathrm b}^{2}=\exp(i\psi\vec u_{\mathrm b}),\qquad
\tilde U_{\mathrm b}^{-1}=\exp\Bigl(-i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr).
$$

The boost is not unitary, because $\tilde U_{\mathrm b}^{-1}\neq\tilde U_{\mathrm b}$ unless $\psi=0$.

### The Sandwich on the Two Sectors

The right slot is $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, so the sandwich is a **congruence**,

$$
\Theta_{\tilde U_{\mathrm b}}(\tilde X)=\tilde U_{\mathrm b}\,\tilde X\,\tilde U_{\mathrm b},
$$

and not a conjugation. Write $b_\parallel=\vec u_{\mathrm b}\cdot\vec b$ and $\vec b_\perp=\vec b-b_\parallel\vec u_{\mathrm b}$.

On $\mathbb{M}_-$, for $\tilde X=ia\,e_t+\vec b$,

$$
\Theta_{\tilde U_{\mathrm b}}(\tilde X)=ia'\,e_t+\vec b',
\qquad
a'=a\cosh\psi-b_\parallel\sinh\psi,\qquad
b_\parallel'=b_\parallel\cosh\psi-a\sinh\psi,\qquad
\vec b_\perp'=\vec b_\perp .
$$

On $\mathbb{M}_+$, for $\tilde X=a\,e_t+i\vec b$,

$$
\Theta_{\tilde U_{\mathrm b}}(\tilde X)=a'\,e_t+i\vec b',
\qquad
a'=a\cosh\psi+b_\parallel\sinh\psi,\qquad
b_\parallel'=b_\parallel\cosh\psi+a\sinh\psi,\qquad
\vec b_\perp'=\vec b_\perp .
$$

The two formulas differ only in the signs of the cross terms. The derivation is one line per piece. For the time piece,

$$
\tilde U_{\mathrm b}\,(ia\,e_t)\,\tilde U_{\mathrm b}=ia\,\tilde U_{\mathrm b}^{2}
=ia\cosh\psi-a\sinh\psi\,\vec u_{\mathrm b},
$$

and for the vector piece the perpendicular part is fixed and the parallel part is stretched by $\cosh\psi$; the cross terms combine into the formulas above. In the coordinates $(a,b_x,b_y,b_z)$ the matrices of the two actions are

$$
B_-(\psi,\vec u_{\mathrm b})=
\begin{pmatrix}
\cosh\psi & -\sinh\psi\,\vec u_{\mathrm b}^{\,T}\\
-\sinh\psi\,\vec u_{\mathrm b} & I_3+(\cosh\psi-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

$$
B_+(\psi,\vec u_{\mathrm b})=
\begin{pmatrix}
\cosh\psi & \sinh\psi\,\vec u_{\mathrm b}^{\,T}\\
\sinh\psi\,\vec u_{\mathrm b} & I_3+(\cosh\psi-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

with $B_+=B_-^{-1}$. Each preserves its form, $B_\pm^{T}G_\pm B_\pm=G_\pm$, where $G_+=\operatorname{diag}(1,-1,-1,-1)$ and $G_-=-G_+=\operatorname{diag}(-1,1,1,1)$.

### The Exponent and the Rapidity

The exponent is $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ and the output is the rapidity $\psi$. The parameter of the factor is half the parameter of its image, and the doubling is exact. The boost is Hermitian, so both slots carry the exponent with the same sign; the sandwich adds the two exponents instead of cancelling them, and the sum is $2\cdot\tfrac{\psi}{2}=\psi$.

## The Rotor

### The Factor

The rotor is

$$
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r},
\qquad \theta\in[0,2\pi],\qquad \lvert\vec u_{\mathrm r}\rvert=1 .
$$

It is a real quaternion, of norm one, and unitary,

$$
\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1},\qquad \langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

Unlike the boost, the rotor is both norm-one and unitary, and its right slot is therefore the inverse.

### The Sandwich

$$
\Theta_{\tilde u_{\mathrm r}}(\tilde X)=\tilde u_{\mathrm r}\,\tilde X\,\tilde u_{\mathrm r}^{-1}.
$$

The sandwich is a conjugation by an invertible element, hence an algebra automorphism. On a general element $\tilde X=X_te_t+\vec X$ it fixes the scalar part and rotates the vector part,

$$
\Theta_{\tilde u_{\mathrm r}}(\tilde X)=X_te_t+\mathsf R(\theta,\vec u_{\mathrm r})\,\vec X,
$$

where $\mathsf R$ is the Rodrigues rotation

$$
\mathsf R(\theta,\vec u_{\mathrm r})=I_3+\sin\theta\,[\vec u_{\mathrm r}]_\times+(1-\cos\theta)\,[\vec u_{\mathrm r}]_\times^{2},
$$

or, on a vector $\vec X$,

$$
\mathsf R(\theta,\vec u_{\mathrm r})\,\vec X
=\vec X\cos\theta+(\vec u_{\mathrm r}\times\vec X)\sin\theta
+\vec u_{\mathrm r}(\vec u_{\mathrm r}\cdot\vec X)(1-\cos\theta).
$$

On $\mathbb{M}_-$ the rotor fixes the time direction $ie_t$ and rotates $\vec b$; on $\mathbb{M}_+$ it fixes $e_t$ and rotates $i\vec b$. The formula is the same on the two sectors because $i$ is central.

### The Exponent and the Angle

The exponent is $\tfrac{\theta}{2}\vec u_{\mathrm r}$ and the output is the rotation of angle $\theta$ about $\vec u_{\mathrm r}$. The parameter of the factor is half the parameter of its image. The rotor is unitary, so the two slots carry opposite signs; the sandwich conjugates instead of composing the two exponents, and the conjugation by $\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ is the rotation of angle $\theta$. Equivalently, the double cover $SU(2)\to SO(3)$ sends $\pm\tilde u_{\mathrm r}$ to the same rotation, and the parameter $\theta$ of the image is twice the parameter $\theta/2$ of the rotor.

## The Angle Bookkeeping

### The Table

| factor | exponent | kind of exponent | sandwich | output parameter | angle |
|---|---|---|---|---|---|
| scale $r$ | $\ln r$ | real scalar | $r^{2}\tilde X$ | $2\ln r$ | none |
| phase $\exp(i\alpha)$ | $i\alpha$ | imaginary scalar | $\tilde X$ | $0$ | none |
| boost $\tilde U_{\mathrm b}$ | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | imaginary vector | congruence | rapidity $\psi$ | rapidity |
| rotor $\tilde u_{\mathrm r}$ | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | real vector | automorphism | angle $\theta$ | rotation |

The table is a table of exponents, not of angles alone. The scale doubles its exponent and produces no angle; the phase produces no exponent and no angle; the boost and the rotor double theirs and produce a rapidity and a rotation.

### The Doubling Rule

**Proposition (the doubling rule).** Write each factor as $F=\exp(tA)$, where $t$ is its scalar parameter and $A$ its generator: $A=e_t$ for the scale, $A=i$ for the phase, $A=i\vec u_{\mathrm b}$ for the boost and $A=\vec u_{\mathrm r}$ for the rotor. Then

$$
\Theta_F(\tilde X)=\exp(tA)\,\tilde X\,\exp(tA^{*}).
$$

Three cases exhaust the word:

**(a)** $A^{*}=A$ (Hermitian). The two slots carry the same exponent $+tA$. If $A$ is central, as for the scale with $A=e_t$, the sandwich is multiplication by $\exp(2tA)$; if $A$ is non-central, as for the boost with $A=i\vec u_{\mathrm b}$, the sandwich is the congruence whose parameter is $2t$. In both cases the output parameter is $2t$.

**(b)** $A^{*}=-A$ and $A$ non-central (the rotor, $A=\vec u_{\mathrm r}$). The two slots carry opposite exponents, so the sandwich is the conjugation $\exp(t\,\mathrm{ad}_A)$, whose vector action is the rotation of angle $2t$; the output parameter is $2t$.

**(c)** $A^{*}=-A$ and $A$ central (the phase, $A=i$). The two slots carry opposite exponents and $A$ commutes with everything, so $\mathrm{ad}_A=0$ and the output parameter is $0$.

In one formula,

$$
\text{output parameter}=
\begin{cases}
2t, & A^{*}=A,\\
2t, & A^{*}=-A\ \text{and}\ A\ \text{non-central},\\
0, & A^{*}=-A\ \text{and}\ A\ \text{central}.
\end{cases}
$$

The doubling is therefore a property of the non-central factors, and of the Hermitian central one; the cancellation is a property of the skew-Hermitian central one. "Half-angle" is the name of the boost and rotor rows; it is not a property of the phase.

## The Image and the Kernel

**Theorem.** Let $\Theta:\mathbb{B}^{\times}\to GL_{\mathbb{R}}(\mathbb{B})$ be the sandwich map $\tilde Q\mapsto\Theta_{\tilde Q}$.

**(a)** The kernel is the central unit circle,
$$
\ker\Theta=U(1)=\{\lambda e_t:\lambda\in\mathbb{C},\ \lvert\lambda\rvert=1\}.
$$

**(b)** The image is the linear conformal Lorentz group,
$$
\boxed{\;\operatorname{im}\Theta\cong CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3)\;},
$$
acting on $\mathbb{M}_-$ by a dilation of ratio $r^{2}$ composed with a proper orthochronous Lorentz transformation.

**(c)** On the modulus-one slice $r=1$, the image is $SO^{+}(1,3)$ and the kernel is $U(1)$.

**(d)** On the norm-one slice $\langle\tilde Q\rangle_{\natural}=1$, the image is $SO^{+}(1,3)$ and the kernel is $\{\pm e_t\}$; the map is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$.

*Proof.* (a) If $\Theta_{\tilde Q}=\mathrm{id}$, then $\tilde Q\tilde Q^{*}=e_t$ by evaluating at $e_t$, so $\tilde Q^{*}=\tilde Q^{-1}$ and $\tilde Q\tilde X\tilde Q^{-1}=\tilde X$ for every $\tilde X$. Hence $\tilde Q$ is central, $\tilde Q=\lambda e_t$, and $\lvert\lambda\rvert=1$. Conversely, a central $\lambda e_t$ with $\lvert\lambda\rvert=1$ gives the identity, by the computation of §*The Central Phase*.

(b) Every unit is $\Rho U$ with $\Rho\in\mathbb{C}^{\times}$ and $U\in SL(2,\mathbb{C})$, the pair unique up to $(\Rho,U)\mapsto(-\Rho,-U)$. The kernel (a) is the unit circle in the first factor, so after that quotient the first factor is $\mathbb{R}_{>0}$ and the second is $SL(2,\mathbb{C})/\{\pm e_t\}=PSL(2,\mathbb{C})\cong SO^{+}(1,3)$:

$$
\operatorname{im}\Theta\cong\mathbb{R}_{>0}\times SO^{+}(1,3)=CO^{+}(1,3).
$$

(c) At $r=1$ the element is $\exp(i\alpha)U$ with $U\in SL(2,\mathbb{C})$, the pair unique up to $(\alpha,U)\mapsto(\alpha+\pi,-U)$. The kernel is still $U(1)$, and the quotient is $SO^{+}(1,3)$.

(d) At $\langle\tilde Q\rangle_{\natural}=1$ the element lies in $SL(2,\mathbb{C})$ and the kernel of the action on $\mathbb{M}_-$ is $\{\pm e_t\}$.

**Corollary (the isometry slice).** The sandwich is an isometry of the Lorentzian norm on $\mathbb{M}_-$ exactly when $r=1$. For general $r$,

$$ \boxed{\;L^{T}G_-L=r^{4}G_-,\qquad \det L=r^{8}\;}, $$

so the form is multiplied by $r^{4}$ and the volume by $r^{8}$; the causal type is preserved and the transformation is a similarity of ratio $r^{2}$.

**Remark (what the image is not).** The image is not the unitary group and not $GL(2,\mathbb{C})$. The unitary group acts on the spinor module and sees the phase; the sandwich sees only the conformal Lorentz group. The two readings of the same word are the subject of *The Twisted Spinor Operator Representation of Biquaternions*.

## The Null Cone

On the null cone $\langle\tilde Q\rangle_{\natural}=0$ the polar word does not exist, but the sandwich does. If $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$, the matrix $\mathsf M_2(\tilde Q)$ is a nonzero $2\times2$ matrix of determinant zero, hence of complex rank one. The sandwich therefore has complex rank one, and its image is the complex line spanned by $\tilde Q\tilde Q^{*}$: writing $\mathsf M_2(\tilde Q)=uv^{*}$ with column $u$ and row $v^{*}$,

$$
\mathsf M_2(\tilde Q)\,X\,\mathsf M_2(\tilde Q)^{*}
=u\,(v^{*}Xv)\,u^{*},
$$

which is a multiple of $uu^{*}=\mathsf M_2(\tilde Q\tilde Q^{*})$. The element $\tilde Q\tilde Q^{*}$ is nonzero because its trace in the matrix model is the squared Frobenius norm of $\mathsf M_2(\tilde Q)$. The action collapses the eight-dimensional algebra onto one complex line; it is not invertible, and it has no polar reading because the scale, the phase, the boost and the rotor are not available on the cone.

## Summary

The Hermitian sandwich of the polar word is read factor by factor. The closed form is

$$
\Theta_{\tilde Q}=r^{2}\,\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}},
\qquad
\Theta_{\exp(i\alpha)}=\mathrm{id}.
$$

The scale dilates by $r^{2}$ and doubles its exponent $\ln r$ to $2\ln r$. The phase cancels: its exponent $i\alpha$ produces nothing, because it is central and unitary, and the whole $U(1)$-orbit of an element has one sandwich. The boost is a congruence by the Hermitian positive $\tilde U_{\mathrm b}$; its exponent $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ produces the rapidity $\psi$. The rotor is an inner automorphism; its exponent $\tfrac{\theta}{2}\vec u_{\mathrm r}$ produces the rotation of angle $\theta$. The doubling rule is that a Hermitian exponent and a non-central skew-Hermitian exponent double, while a central skew-Hermitian exponent cancels.

The image of the sandwich on the group of units is $CO^{+}(1,3)$, the kernel is $U(1)$, and the isometry slice is $r=1$, where the image is $SO^{+}(1,3)$. On the norm-one slice the map is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$. On the null cone the sandwich survives as an operator of complex rank one, with image the line spanned by $\tilde Q\tilde Q^{*}$.

The phase is the one factor that the sandwich does not see. It is visible to the norm, to the determinant and to the module, which is why the polar word carries it; it is invisible to the vector action, which is why the sandwich is a representation whose image is the conformal Lorentz group and not the full group of units.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | the central scalar imaginary, $i^{2}=-1$ |
| $\tilde Q^{*}$ | the Hermitian conjugation $\overline{\tilde Q^{\natural}}$ |
| $\natural$, $\bar\cdot$ | the quaternion and coefficient conjugations |
| $\mathbb{M}_\pm$ | the Hermitian and anti-Hermitian subspaces, $\tilde Q^{*}=\pm\tilde Q$ |
| $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the Hermitian sandwich |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the complex norm of the polar series |
| $\Rho=r\exp(i\alpha)$ | the complex modulus, the principal square root of $\langle\tilde Q\rangle_{\natural}$ |
| $P=\exp(i\alpha)$ | the central phase factor |
| $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ | the scale and the phase angle |
| $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ | the Hermitian positive unit-norm boost |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $\psi\ge0$, $\theta\in[0,2\pi]$ | the rapidity and the rotation angle |
| $B_\pm$ | the $4\times4$ matrices of the boost on $\mathbb{M}_\pm$ |
| $\mathsf R(\theta,\vec u_{\mathrm r})$ | the Rodrigues rotation matrix of the rotor |
| $G_\pm$ | the matrices of the norm on the two sectors, $G_+=\operatorname{diag}(1,-1,-1,-1)$ and $G_-=-G_+$ |
| $CO^{+}(1,3)$ | the linear conformal Lorentz group, the image of the sandwich |
| $U(1)$ | the kernel of the sandwich, the central unit circle |
| $\langle\tilde Q\rangle_{\natural}=1$ | the norm-one slice, $SL(2,\mathbb{C})$ |

## Further Reading

- [One-Sided Operator Under the Polar Decomposition](one-sided-operator-under-the-polar-decomposition.html), for the one-sided companion: the left and right multiplications, the sector decomposition and the exchange $\mathbb{M}_-\leftrightarrow\mathbb{M}_+$ by the phase $i$.
- [The Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the four factors, the modulus, the branch and the domain.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), §*The Action on the Two Halves*, for the detailed action on the two sectors, the boost matrices and the comparison of the two signs.
- [The Twisted Spinor Operator Representation of Biquaternions](the-twisted-spinor-operator-representation-of-biquaternions.html), for the same word on the spinor module, where the phase is the twist and all four factors are visible.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the Hermitian positive and unitary factors and the equation $\tilde Q\tilde Q^{*}=\tilde H^{2}$.
- [The Quaternion Pairing of the Polar Decomposition of Biquaternions](the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html) and [The Hamilton Root Pairing of the Polar Decomposition of Biquaternions](the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html), for the two partial two-factor groupings.
- [The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint](the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.html), for the eigenvalues $\lambda_i\bar\lambda_j$ of the sandwich and the spectral proof of the phase cancellation.
- [The Four-Vector Operator Representation of Biquaternions](the-four-vector-operator-representation-of-biquaternions.html), for the sandwich written in the four complex coefficients and its degenerate image on the cone.
- [Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint](completely-positive-maps-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the sandwich as a completely positive map and its place among the two-sided operators.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz group in biquaternionic form and the double cover.
